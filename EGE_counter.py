from PIL import Image, ImageDraw
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


def counter(name):
    color = (255, 204, 0)
    img = Image.new("RGB", (275, 150))
    drawer = ImageDraw.Draw(img)
    drawer.rectangle([0, 0, 300, 300], color)
    fnt = ImageFont.truetype("1.ttf", 30)
    drawer.text((10, 30), f"До ЕГЭ Осталось:\n\n          {(datetime(year=2023, month=6, day=19)-datetime.now()).days} дня", font=fnt, fill=(0, 0, 0))
    img.save(name)
    


if __name__ == '__main__':
    counter('5.png')
