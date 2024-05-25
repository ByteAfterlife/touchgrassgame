from PIL import Image, ImageDraw, ImageFont
import os
import customtkinter
import sys
name = customtkinter.CTkInputDialog(text="Name?", title="Certificate generation")
name = name.get_input()
image = Image.open("grass.jpg")
draw = ImageDraw.Draw(image)
size = len(name) * 1.1
font = ImageFont.truetype("arial.ttf", int(size))
draw.text((0, 0), f"Grass touch certificate presented to {name}", font=font, fill=(255, 0, 0))
if not os.path.exists("./certificate/"):
    os.mkdir("./certificate/")
if not os.path.exists("./certificate/grasstouchery.jpg"):
    os.open("./certificate/grasstouchery.jpg", os.O_RDONLY | os.O_CREAT)
image.save("./certificate/grasstouchery.jpg")
done = customtkinter.CTk()
finished = customtkinter.CTkLabel(master=done, text="Completed. Look in (game root folder)/certificate")
finished.pack()
done.protocol("WM_DELETE_WINDOW", sys.exit)
done.mainloop()