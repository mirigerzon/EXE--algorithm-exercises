from PIL import Image
import sys

def stretch_histogram(image):
    hist = image.histogram()
    min_pixel = next(i for i, v in enumerate(hist) if v != 0)
    max_pixel = next(i for i in reversed(range(len(hist))) if hist[i] != 0)

    def stretch_pixel(value):
        return int((value - min_pixel) * 255 / (max_pixel - min_pixel))

    return image.point(stretch_pixel)

def main():
    if len(sys.argv) != 2:
        print("Usage: python ex01_02.py <image_file>")
        return

    filename = sys.argv[1]

    # א. קריאת תמונה + ב. המרה לשחור־לבן
    image = Image.open(filename)
    bw_img = image.convert("L")

    # ג + ד. מתיחת היסטוגרמה
    stretched_img = stretch_histogram(bw_img)

    # הצגה
    bw_img.show(title="Original Grayscale Image")
    stretched_img.show(title="Stretched Image")

if __name__ == "__main__":
    main()
