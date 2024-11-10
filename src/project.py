from PIL import Image

class ShadowForge():

    def GetGrayscale(self):
        with Image.open('test.png') as img:
            img_gray = img.copy()
            img_gray = img.convert('L')
            img_gray.show()
    

    def function_n():
        print()
    

def main():
    sf = ShadowForge()
    #img = sf.GetGrayscale()
    sf.GetGrayscale()
    

if __name__ == "__main__":
    main()