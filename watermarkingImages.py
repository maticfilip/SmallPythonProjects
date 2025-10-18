from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter

root=Tk()
root.title("Watermarking Images")
root.geometry("800x600")

original_image=None
watermark_image=None

#funkcije
def upload(event=None):
    global original_image
    filename=filedialog.askopenfilename()
    original_image = Image.open(filename)
    resized_image = original_image.resize((600,400), Image.LANCZOS)  # Resize as needed
    img_display = ImageTk.PhotoImage(resized_image)
    image_label.config(image=img_display)
    image_label.image=img_display
    image_loaded=True

def upload_watermark(event=None):
    global watermark_image
    filename=filedialog.askopenfilename()
    watermark_image=Image.open(filename)
    watermark_image.thumbnail((100,100))
    img_tk=ImageTk.PhotoImage(watermark_image)


#GUI
Label(root, text="Upload an image to add a watermark").pack()
upload_button=Button(root,text="Upload", command=upload)
upload_button.pack()

image_label=Label(root)
image_label.pack(pady=10)

Label(root, text="Upload Watermark").pack()
watermark_button=Button(root,text="Upload Watermark", command=upload_watermark)
watermark_button.pack()

def combine_images():
    if original_image and watermark_image:
        combined=original_image.copy()
        combined.paste(watermark_image, (combined.width - watermark_image.width -10,
                                         combined.height - watermark_image.height -10), watermark_image)
        combined.show()

Button(root, text="Combine Images", command=combine_images).pack(pady=10)

root.mainloop()
