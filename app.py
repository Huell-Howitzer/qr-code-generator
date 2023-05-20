import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox

class QRCodeWindow:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        master.configure(background="#F0F0F0")  # Set the background color

        # Create a label and an entry widget for the text to encode
        self.label = tk.Label(master, text="Enter text:", font=("Arial", 12), bg="#F0F0F0")
        self.label.pack()

        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack()

        # Create a button to generate the QR code
        self.generate_button = tk.Button(master, text="Generate QR Code", font=("Arial", 12, "bold"), fg="white",
                                bg="#4CAF50", activebackground="#45A049", relief=tk.FLAT,
                                command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        # Create a canvas to display the QR code
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Create a button to save the QR code as SVG
        self.save_button = tk.Button(master, text="Save as SVG", font=("Arial", 12), fg="white",
                                bg="#2196F3", activebackground="#1976D2", relief=tk.FLAT,
                                command=self.save_as_svg)
        self.save_button.pack(pady=10)

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

        # Resize the image to fit the canvas dimensions
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        img = img.resize((canvas_width, canvas_height))

        # Convert the PIL image to a Tkinter-compatible format
        self.photo = ImageTk.PhotoImage(img)

        # Display the image in the canvas
        self.canvas.create_image((0, 0), image=self.photo, anchor=tk.NW)

    def save_as_svg(self):
        # Get the text to encode from the entry widget
        text = self.entry.get()

        # Generate the QR code using the qrcode library
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)

        # Save the QR code as an SVG file
        qr.make_image(fill_color="black", back_color="white").save("qrcode.svg")

        # Show a confirmation message
        messagebox.showinfo("QR Code Generator", "QR code saved as SVG.")

root = tk.Tk()
app = QRCodeWindow(root)
root.mainloop()




