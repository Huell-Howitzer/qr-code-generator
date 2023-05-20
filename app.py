import tkinter as tk
import qrcode
from PIL import Image, ImageTk

class QRCodeWindow:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        # Create a label and an entry widget for the text to encode
        self.label = tk.Label(master, text="Enter text:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        # Create a button to generate the QR code
        self.button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.button.pack()

        # Create a canvas to display the QR code
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        # Store the PhotoImage object
        self.photo = None

    def generate_qr_code(self):
        # Get the text to encode from the entry widget
        text = self.entry.get()

        # Generate the QR code using the qrcode library
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert the PIL image to a Tkinter-compatible format
        self.photo = ImageTk.PhotoImage(img)

        # Display the image in the canvas
        self.canvas.create_image((0, 0), image=self.photo, anchor=tk.NW)

root = tk.Tk()
app = QRCodeWindow(root)
root.mainloop()

