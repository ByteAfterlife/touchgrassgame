from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import Texture, GeomNode, GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import LVector3
import sys
import random
import customtkinter as CTk
import hashlib, sys
from base64 import b64decode
import os
stupidtips = ["Did you know that grass has ass in it?", "Touching virtual grass won't increase your actual health! Go touch real grass.", "Why did the sheep eat grass? Because it was hungry *cricket chirping*", "What is in between the letters G and H on your keyboard is the last time you touched grass (if you don't understand, never)", "Why did the grass learn to walk? Because since you don't want to touch it, it will touch you..", "Why did the grass learn science? I honestly don't know.. you tell me.. like seriously I cant think of a punchline- Comment in the github discussions your punchline for this.."]
def mct():
        os.system("python3.11 mct.py")
class menus():
    def help():
        helpgui = CTk.CTk()
        helpgui.title("Help")
        label_text = """-: Zoom out
    =: Zoom in
    W: Move camera forward
    A: Move camera left
    S: Move camera backward
    D: Move camera right
    Left click: Touch the grass"""

        label = CTk.CTkLabel(helpgui, text=label_text, font=("Arial", 16))
        label.pack(pady=20, padx=20)
        helpgui.mainloop()
    def mainmenu():
        menu = CTk.CTk()
        menu.title("Main menu")

        def on_closing():
            print("Closing the main menu is mean. The menu refuses to open the game cause you were mean to it :(")
            sys.exit()

        menu.protocol("WM_DELETE_WINDOW", on_closing)

        startbutton = CTk.CTkButton(menu, text="Touch grass", font=("Arial", 16), command=menu.destroy, width=230)
        startbutton.place(relx=0.5, rely=0.5, anchor="center")
        infothingy = CTk.CTkLabel(menu, text="Tip: When in the grass simulator (the thing after you press the touch grass button), you can press \"/\" for a list of keybinds!")
        infothingy.pack()
        startbutton.pack()
        selectedjoke = random.choice(stupidtips)
        stupidjoketext = CTk.CTkLabel(menu, text="Stupid grass related thing: " + selectedjoke)
        stupidjoketext.pack()
        menu.mainloop()
    def ggs():
        gameover = CTk.CTk()
        gameover.title("GG!")
        if len(sys.argv) == 2:
            finale = CTk.CTkLabel(gameover, text="Nice! You touched grass, but since it was custom provided, we can't really be sure..")
        else:
            finale = CTk.CTkLabel(gameover, text="Nice! You touched grass :D")
            certificategen = CTk.CTkButton(gameover, text="Want a certificate?", command=mct)
        finale.pack()
        try:
            certificategen.pack()
        except UnboundLocalError:
            pass
        gameover.mainloop()
loadPrcFileData("", "win-size 800 600")
loadPrcFileData("", "window-title Grass")
loadPrcFileData("", "texture-anisotropic-degree 16")
arguments = [
    {
        "name": "Filename",
        "description": "The image to 3Dify",
        "example": "grass.jpg"
    }
]
def c_f_h(f_p, a='sha256'):
    h = hashlib.sha256()
    with open(f_p, 'rb') as f:
        for c in iter(lambda: f.read(4096), b""):
            h.update(c)
    return h.hexdigest()
e_h = "29c0ac12bc1ebdf8905cb83248d0a9b788690664768e908c2dd760642954e1b7"
f_p = b64decode(b64decode("WjNKaGMzTXVhbkJu")).decode()
a_h = c_f_h(f_p)
if a_h != e_h:
    sys.exit(b64decode(b64decode("VG1salpTQjBjbmtnWm1GcmFXNW5JSFJvWlNCbmNtRnpjeUJtYVd4bA==")).decode())
menus.mainmenu()
class dagrass(ShowBase):
    def donegg(self):
        menus.ggs()
        self.exitFunc()
    def __init__(self):
        ShowBase.__init__(self)
        try:
            if len(sys.argv) != 2:
                grasstexture = "grass.jpg"
                print("Tip: If you have some rare photo of grass that you want to custom use, you can just import it into here by just adding the grass file name as a command line argument, e.g. python (scriptname) mycoolgrass.png, but you won't get a certificate.")
                grass_texture = self.loader.loadTexture(grasstexture)
            else:
                grass_texture = self.loader.loadTexture(sys.argv[1])
        except FileNotFoundError:
            print("Shiver me timbers! Thats some invisible grass you got there! (ok in all seriousness, this means the file for grass you provided doesn't exist)")
        grass_texture.setAnisotropicDegree(16)  
        ambient_light = AmbientLight("ambient_light")
        ambient_light.setColor((0.4, 0.4, 0.4, 1))
        ambient_light_node = self.render.attachNewNode(ambient_light)
        self.render.setLight(ambient_light_node)

        directional_light = DirectionalLight("directional_light")
        directional_light.setDirection(LVector3(0, -1, -1))
        directional_light.setColor((0.9, 0.9, 0.9, 1))
        directional_light_node = self.render.attachNewNode(directional_light)
        self.render.setLight(directional_light_node)
        self.terrain_node = self.create_terrain(grass_texture)
        self.camera.setPos(0, -256, 256) 
        self.camera.setHpr(0, -45, 0)
        self.disable_mouse()
        self.accept("escape", sys.exit)
        self.accept("w", self.move_camera, [0, 20, 0])
        self.accept("s", self.move_camera, [0, -20, 0])
        self.accept("a", self.move_camera, [-20, 0, 0])
        self.accept("d", self.move_camera, [20, 0, 0])
        self.accept("=", self.move_camera, [0, 0, -10])
        self.accept("+", self.move_camera, [0, 0, -10])
        self.accept("-", self.move_camera, [0, 0, 10])
        self.accept("/", menus.help)
        self.accept("mouse1", self.donegg)

    def create_terrain(self, texture):
        format = GeomVertexFormat.getV3n3cpt2()
        vdata = GeomVertexData("terrain", format, Geom.UHStatic)

        vertex = GeomVertexWriter(vdata, "vertex")
        normal = GeomVertexWriter(vdata, "normal")
        color = GeomVertexWriter(vdata, "color")
        texcoord = GeomVertexWriter(vdata, "texcoord")

        vertex.addData3f(-64, -64, 0)
        normal.addData3f(0, 0, 1)
        color.addData4f(1, 1, 1, 1)
        texcoord.addData2f(0, 0)

        vertex.addData3f(64, -64, 0)
        normal.addData3f(0, 0, 1)
        color.addData4f(1, 1, 1, 1)
        texcoord.addData2f(1, 0)

        vertex.addData3f(64, 64, 0)
        normal.addData3f(0, 0, 1)
        color.addData4f(1, 1, 1, 1)
        texcoord.addData2f(1, 1)

        vertex.addData3f(-64, 64, 0)
        normal.addData3f(0, 0, 1)
        color.addData4f(1, 1, 1, 1)
        texcoord.addData2f(0, 1)

        triangles = GeomTriangles(Geom.UHStatic)
        triangles.addVertices(0, 1, 2)
        triangles.addVertices(2, 3, 0)

        geom = Geom(vdata)
        geom.addPrimitive(triangles)

        node = GeomNode("terrain")
        node.addGeom(geom)

        terrain = self.render.attachNewNode(node)
        terrain.setTexture(texture)
        return terrain

    def move_camera(self, dx, dy, dz):
        self.camera.setPos(self.camera.getPos() + (dx, dy, dz))


    
engine = dagrass()
engine.run()
