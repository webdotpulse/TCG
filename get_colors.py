import sys
from PIL import Image
from collections import Counter

def get_colors(image_path):
    img = Image.open(image_path).convert('RGBA')
    pixels = list(img.getdata())

    # Filter out transparent and very light colors
    valid_pixels = []
    for r, g, b, a in pixels:
        if a > 50 and not (r > 240 and g > 240 and b > 240):
            valid_pixels.append((r, g, b))

    counts = Counter(valid_pixels)
    for color, count in counts.most_common(5):
        print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x} - Count: {count}")

if __name__ == "__main__":
    get_colors(sys.argv[1])
