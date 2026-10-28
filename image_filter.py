from PIL import Image, ImageFilter

image_path = input("Enter image filename: ")

try:
    pic = Image.open(image_path)
    print("Image opened successfully.")
    print("Size:", pic.size)

    gray_pic = pic.convert("L")
    gray_pic.save("grayscale.png")

    mono_pic = gray_pic.point(lambda val: 255 if val > 128 else 0)
    mono_pic.save("black_white.png")

    blurred_pic = pic.filter(ImageFilter.BLUR)
    blurred_pic.save("blurred.png")

    print("Processed images saved successfully.")

except FileNotFoundError:
    print("Image file not found.")

except Exception as err:
    print("Error:", err)
