from PIL import Image

class ShadowForge():

    def GetGrayscale(self):
        with Image.open('test.png') as img:
            img_gray = img.copy()
            img_gray = img.convert('L')
            img_gray.show()
    

    def FindShadows(self, img):
        img_shadow = img.copy()
        for y in range(img.height):
            for x in range(img.width):
                pix = img.getpixel((x,y))
                if pix <= 105:
                    img_shadow.putpixel((x,y), (0,0,255,255))
                else:
                    img_shadow.putpixel((x,y), (255,255,255,255))
    

def main():
    sf = ShadowForge()
    #img = sf.GetGrayscale()
    img_gray = sf.GetGrayscale()
    sf.FindShadows(img_gray)
    

if __name__ == "__main__":
    main()