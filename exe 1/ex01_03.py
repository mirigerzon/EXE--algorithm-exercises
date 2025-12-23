from PIL import Image
import sys

def stretch_channel(channel):
    hist = channel.histogram()
    min_pixel = next(i for i, v in enumerate(hist) if v != 0)
    max_pixel = next(i for i in reversed(range(len(hist))) if hist[i] != 0)

    if min_pixel == max_pixel:
        return channel
        
    def stretch(value):
        return int((value - min_pixel) * 255 / (max_pixel - min_pixel))

    return channel.point(stretch)


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex01_03.py <image_file>")
        return

    filename = sys.argv[1]
    #פתיחת תמונה
    image = Image.open(filename).convert("RGB")
    #פירוק הצבעים
    r, g, b = image.split()
    #חישוב הסטוגרמה לכל צבע בנפרד
    r.stretched = stretch_channel(r)
    g.stretched = stretch_channel(g)
    b.stretched = stretch_channel(b)
    result_image = Image.merge("RGB", (r.stretched, g.stretched, b.stretched))
    #הצגה
    image.show(title="Original Image")
    result_image.show(title="Stretched Image")

if __name__ == "__main__":
    main()