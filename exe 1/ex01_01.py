from PIL import Image
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python ex01_01.py <image_file>")
        return
    filename = sys.argv[1]
    
    # פתיחת התמונה
    image = Image.open(filename).convert("RGB")

    #פירוק הצבעים
    r, g, b = image.split()

    #הצגת כל צבע בנפרד
    r.show(title="Red Channel")
    g.show(title="Green Channel")
    b.show(title="Blue Channel")

if __name__ == "__main__":
    main()
