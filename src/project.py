from PIL import Image
import random
#from appJar import gui

class ShadowForge():

    def GetGrayscale(self):
        with Image.open('Face.png') as img:
            img_gray = img.copy()
            img_gray = img.convert('L')
            img_gray.show()
        return img_gray
    

    def FindShadows(self, img_gray):
        img_shadow = Image.new('RGB', (img_gray.width, img_gray.height), (255,255,255,255))
        for y in range(img_gray.height):
            for x in range(img_gray.width):
                pix = img_gray.getpixel((x,y))
                if pix <= 105:
                    img_shadow.putpixel((x,y), (0,0,255,255))

        img_shadow.show()
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

        img_outline.show()
        return img_outline
    
    def RandomColorFilling(self, img_shadow):
        img_colors = Image.new('RGB', (img_shadow.width, img_shadow.height), (255,255,255,255))
        for y in range(img_shadow.height):
            for x in range(img_shadow.width):
                #Runs through all of the pixels to find out if they are blue
                color = img_shadow.getpixel((x,y))
                if color == (0,0,255):
                    #assigns random assortment of colors to fill blue pixels
                    img_colors.putpixel((x,y),(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), 255))
                    img_colors.size=20

        img_colors.show()
        return img_colors
    

def main():
    sf = ShadowForge()
    #img = sf.GetGrayscale()
    img_gray = sf.GetGrayscale()
    img_shadow = sf.FindShadows(img_gray)
    img_outline = sf.OutlineImage(img_shadow)
    img_colors = sf.RandomColorFilling(img_shadow)
    

if __name__ == "__main__":
    main()