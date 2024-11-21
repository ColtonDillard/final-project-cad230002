from PIL import Image
import random
from appJar import gui

class ShadowForge():

    def GetGrayscale(self, path):
        with Image.open(path) as img:
            img_gray = img.copy()
            img_gray = img.convert('L')
        return img_gray
    

    def FindShadows(self, img_gray, thresh):
        img_shadow = Image.new('RGB', (img_gray.width, img_gray.height), (255,255,255,255))
        for y in range(img_gray.height):
            for x in range(img_gray.width):
                pix = img_gray.getpixel((x,y))
                if pix <= thresh:
                    img_shadow.putpixel((x,y), (0,0,255,255))

        return img_shadow
    
    def OutlineImage(self, img_shadow):
        img_outline = Image.new('RGB', (img_shadow.width, img_shadow.height), (255,255,255,255))
        for y in range(img_shadow.height):
            for x in range(img_shadow.width):
                pix = img_shadow.getpixel((x,y))
                adjacent_pixels = [(x-1, y),(x+1, y),(x,y+1),(x,y-1)]
                #Checks if the pixel is white
                if pix == (255,255,255):
                #Loops through all adjacent pixels
                    for dot in adjacent_pixels:
                        nx,ny=dot
                        if 0 <= nx < img_shadow.width and 0 <= ny < img_shadow.height:
                        #Checks if adjacent pixels are blue
                            if img_shadow.getpixel(dot) == (0,0,255):
                                img_outline.putpixel((x,y), (0,0,0,255))
                                break

        return img_outline
    
    def MosaicFilling(self, img_shadow):
        img_mosaic = Image.new('RGB', (img_shadow.width, img_shadow.height), (255,255,255,255))
        for y in range(img_shadow.height):
            for x in range(img_shadow.width):
                #Runs through all of the pixels to find out if they are blue
                color = img_shadow.getpixel((x,y))
                if color == (0,0,255):
                    #assigns random assortment of colors to fill blue pixels
                    img_mosaic.putpixel((x,y),(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), 255))

        return img_mosaic
    
greyscale_img = None
shadow_img = None
outline_img = None
mosaic_img = None
    
def press(button, app):
    if button == "Close":
        app.stop()
    if button == "Upload":
        sf = ShadowForge()
        global greyscale_img
        global shadow_img
        global outline_img
        global mosaic_img
        greyscale_img = sf.GetGrayscale(app.getEntry("image_file"))
        shadow_img = sf.FindShadows(greyscale_img, app.getScale("Shadow Threshold"))
        outline_img = sf.OutlineImage(shadow_img)
        mosaic_img = sf.MosaicFilling(shadow_img)

        app.setLabel("currpath", f"Current File {app.getEntry("image_file")}")

def show(button):
    if button == "Grayscale":
        global greyscale_img
        greyscale_img.show()
    if button == "Shadow":
        global shadow_img
        shadow_img.show()
    if button == "Outline":
        global outline_img
        outline_img.show()
    if button == "Mosaic":
        global mosaic_img
        mosaic_img.show()


def main():
    sf = ShadowForge()
    # img = sf.GetGrayscale()
    # img_gray = sf.GetGrayscale()
    # img_shadow = sf.FindShadows(img_gray)
    # img_outline = sf.OutlineImage(img_shadow)
    # img_mosaic = sf.MosaicFilling(img_shadow)
    

    #Import gui
    app = gui("Shadow Forge", "400x200")

    app.addLabel("Shadow Forge", "Welcome to Shadow Forge")
    app.setLabelBg("Shadow Forge", "yellow")

    app.addLabel("currpath", "Current File: None")

    app.addFileEntry("image_file")

    app.addButtons(["Upload", "Close"], lambda btn: press(btn, app))

    #adds image buttons to gui
    app.addButtons(["Shadow", "Greyscale", "Outline", "Mosaic"], show)

    app.addLabelScale("Shadow Threshold")
    app.showScaleValue("Shadow Threshold", show=True)
    app.setScaleRange("Shadow Threshold", 0, 255, curr=105)

    app.go()


if __name__ == "__main__":
    main()