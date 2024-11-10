from PIL import Image

class ShadowForge():

    def GetGrayscale(self):
        with Image.open('test.png') as img:
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
    

def main():
    sf = ShadowForge()
    #img = sf.GetGrayscale()
    img_gray = sf.GetGrayscale()
    sf.FindShadows(img_gray)
    

if __name__ == "__main__":
    main()