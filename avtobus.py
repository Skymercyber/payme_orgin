from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def add_datetime(image_path="sess.jpg", output_path="edit.jpg"):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("font.ttf", 40)
    now = datetime.now()
    soat = now.strftime("%H:%M")
    today = now.strftime("%d.%m.%Y")

    # Yuqori soat
    rect_coords = (45, 20, 260, 105)
    draw.rectangle(rect_coords, fill=(32, 32, 44))
    draw.text((50, 40), soat, fill="white", font=font)

    # Pastki sana va soat
    rect_coords_bottom = (0, 820, 500, 900)
    draw.rectangle(rect_coords_bottom, fill=(32, 32, 44))
    draw.text((45, 820), today, fill="white", font=font)
    draw.text((280, 820), soat, fill="white", font=font)

    img.save(output_path)
    return output_path
