from PIL import Image
import requests
from io import BytesIO


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def doImage(url, name):
    image1 = Image.open(name + ".png")

    r = requests.get(url)
    image2 = Image.open(BytesIO(r.content))
    image2 = image2.resize((59, 59))

    combined_image = image1.copy()
    combined_image.paste(image2, (13, 14))
    # new_size = (375, 90)
    # combined_image = combined_image.resize(new_size)
    combined_image.save("результат.png")

    image1.close()
    image2.close()
