from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random

image_path = "cart.jpg"
output_path = "edited.jpg"

# Random generator
random_names = ["Dilshod", "Javohir", "Malika", "Sevinch", "Azizbek", "Zufar"]
def random_card():
    return "".join(str(random.randint(0, 9)) for _ in range(16))

def mask_card(num):
    blocks = [num[i:i+4] for i in range(0, len(num), 4)]
    blocks[1] = blocks[1][:2] + "**"
    blocks[2] = "****"
    return " ".join(blocks)

def edit_card(pul, user_name, card_num, victim_name, victim_card,
              image_path=image_path, output_path=output_path):

    # Random tanlash
    if user_name.lower() == "skip":
        user_name = random.choice(random_names)
    if victim_name.lower() == "skip":
        victim_name = random.choice(random_names)
    if card_num.lower() == "skip":
        card_num = random_card()
    if victim_card.lower() == "skip":
        victim_card = random_card()

    masked_card = mask_card(card_num)
    masked_victim_card = mask_card(victim_card)

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("font.ttf", 20)
    font1 = ImageFont.truetype("mi_bolt_font.ttf", 45)

    now = datetime.now()
    soat = now.strftime("%H:%M")
    today = now.strftime("%d.%m.%Y")

    # Vaqt yuqorida
    rect_coords = (5, 20, 260, 55)
    draw.rectangle(rect_coords, fill=(32, 32, 44))
    draw.text((30, 20), soat, fill="white", font=font)

    # Sana pastda
    rect_coords_bottom = (0, 410, 250, 440)
    draw.rectangle(rect_coords_bottom, fill=(32, 32, 44))
    draw.text((25, 412), today, fill="white", font=font)
    draw.text((150, 412), soat, fill="white", font=font)

    # Pul
    rect_coords_bottom = (0, 305, 300, 365)
    draw.rectangle(rect_coords_bottom, fill=(32, 32, 44))
    draw.text((28, 310), f"{pul:,} so’m", fill="white", font=font1)

    # Foiz
    foiz = 1
    natija = pul * foiz / 100
    natija_str = f"{natija:>10.2f}"
    rect_coords_bottom = (280, 570, 600, 600)
    draw.rectangle(rect_coords_bottom, fill=(32, 32, 44))
    draw.text((417, 570), natija_str + " so’m", fill="white", font=font)

    # ===== Normal karta va ism =====
    rect_coords_bottom = (250, 700, 600, 800)
    draw.rectangle(rect_coords_bottom, fill=(32, 32, 44))
    x_right = 550

    bbox = draw.textbbox((0,0), masked_card, font=font)
    draw.text((x_right - (bbox[2]-bbox[0]), 715), masked_card, fill="white", font=font)

    bbox = draw.textbbox((0,0), user_name, font=font)
    draw.text((x_right - (bbox[2]-bbox[0]), 750), user_name, fill="white", font=font)

    # ===== Victim karta va ism =====
    rect_coords_bottom = (270, 450, 600, 550)
    draw.rectangle(rect_coords_bottom, fill=(32, 32, 44))

    bbox = draw.textbbox((0,0), masked_victim_card, font=font)
    draw.text((x_right - (bbox[2]-bbox[0]), 475), masked_victim_card, fill="white", font=font)

    bbox = draw.textbbox((0,0), victim_name, font=font)
    draw.text((x_right - (bbox[2]-bbox[0]), 500), victim_name, fill="white", font=font)

    img.save(output_path)
    return output_path
