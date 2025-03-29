import sys
import textwrap
from PIL import Image,ImageDraw,ImageFont

# Get inputs from main.py
hotel_name = sys.argv[1]
dish1, dish2 = sys.argv[2:5]

background = Image.new("RGB", (1080,1080), "#1F9173")
draw = ImageDraw.Draw(background)

logo = Image.open("zaaroz_logo1.png")
logo_size = logo.resize((160, 170))
mask = Image.new("L", logo_size.size, 0) 
draw = ImageDraw.Draw(mask)
border_radius = 20
draw.rounded_rectangle([(0, 0), logo_size.size], radius=border_radius, fill=255)
rounded_logo = Image.new("RGBA", logo_size.size)
rounded_logo.paste(logo_size, (0, 0), mask) 
logo_position = (89, 59)
background.paste(rounded_logo, logo_position, rounded_logo)

draw = ImageDraw.Draw(background)

bio="All in One Delivery App"
bio_position=((36,255))
bio_font=ImageFont.truetype("arialbd.ttf",30)
draw.text(bio_position, bio, fill="white", font=bio_font)

description="All Your Home Need In a Single App"
description_font=ImageFont.truetype("arialbd.ttf",30)
max_width=20
wrapped_text = textwrap.fill(description, width=max_width)
description_x = 40
description_y = 985
draw.multiline_text((description_x, description_y), wrapped_text, fill="white", font=description_font, spacing=5)

order_now=Image.open("order_now1.png")
now_size=order_now.resize((350,350)) 
green_bg2 = Image.new("RGBA", now_size.size, "#1F9173") 
mask = now_size.split()[0] if order_now.mode == "RGBA" else None 
green_bg2.paste(now_size, (0, 0), mask)
now_position = (740,0)
background.paste(green_bg2, now_position, green_bg2)

quote="I'm not sure what's more addictive, biryani or the feeling of having a plate of biryani in front of me."
quote_font=ImageFont.truetype("arialbd.ttf",33)
max_width=28
wrapped_text = textwrap.fill(quote, width=max_width)
quote_x=445
quote_y=58
draw.multiline_text((quote_x, quote_y), wrapped_text, fill="#0D1850", font=quote_font, spacing=10)


description="Get 50% Off   On your First  \t\tOrder!!"
description_font=ImageFont.truetype("arialbd.ttf",35)
max_width=15
wrapped_text = textwrap.fill(description, width=max_width)
text_lines = wrapped_text.split("\n")  
line_heights = [description_font.getbbox(line)[3] for line in text_lines]  
text_width = max(description_font.getbbox(line)[2] for line in text_lines) 
text_height = sum(line_heights) + (len(line_heights) - 1) * 5 
description_x = 759
description_y = 740 
padding_x = 15
padding_y = 15
border_radius = 15
box_x1 = description_x - padding_x
box_y1 = description_y - padding_y
box_x2 = description_x + text_width + padding_x
box_y2 = description_y + text_height + padding_y
draw.rounded_rectangle(
    [(box_x1, box_y1), (box_x2, box_y2)],
    fill="orange",
    outline="orange",
    width=3,
    radius=border_radius
)
draw.multiline_text((description_x, description_y), wrapped_text, fill="white", font=description_font, spacing=5)

"""quote="Happiness Can't be bought But Food can!!!"
quote_font=ImageFont.truetype("arialbd.ttf",60)
max_width=15
wrapped_text = textwrap.fill(quote, width=max_width)
quote_x=490
quote_y=58
draw.multiline_text((quote_x, quote_y), wrapped_text, fill="white", font=quote_font, spacing=10)"""

playstore_img=Image.open("playstore.png")
playstore_size=playstore_img.resize((170,70))
playstore_position=(365,1000)
background.paste(playstore_size,playstore_position)

ios_img=Image.open("ios.png")
ios_size=ios_img.resize((170,70))
ios_position=(590,1000)
background.paste(ios_size,ios_position)

tc="T&C"
tc_position=((960,1049))
tc_font=ImageFont.truetype("arialbd.ttf",20)
draw.text(tc_position,f"{tc}",fill="black",font=tc_font)

location="Andipatty"
location_font=ImageFont.truetype("arialbd.ttf",40) 
text_width, text_height = draw.textbbox((0, 0), location, font=location_font)[2:4]   
x, y = 455,920
padding_x = 5
padding_y = 5
border_radius = 20
draw.rounded_rectangle(
    [(x - padding_x, y - padding_y), (x + text_width + padding_x, y + text_height + padding_y)], 
    fill="white", 
    outline="white",  
    width=2,
    radius=border_radius 
    )
draw.text((x, y), f"{location}", fill="#188067", font=location_font) 

app_site="zaaroz.com"
app_position=((815,1010))
app_font=ImageFont.truetype("arialbd.ttf",35)
draw.text(app_position,f"{app_site}",fill="white",font=app_font)

order_now1=Image.open("bnwon1.png")
now_size1=order_now1.resize((210,210)) 
green_bg2 = Image.new("RGBA", now_size1.size, "#1F9173") 
mask = now_size1.split()[3] if order_now1.mode == "RGBA" else None 
green_bg2.paste(now_size1, (0, 0), mask)
now_position1 = (39,714)
background.paste(green_bg2, now_position1, green_bg2)

smile=Image.open("smile.png")
smile_size=smile.resize((420,210))
green_bg1 = Image.new("RGBA", smile_size.size, "#1F9173")
mask = smile_size.split()[3] if smile.mode == "RGBA" else None 
green_bg1.paste(smile_size, (0, 0), mask)
smile_position = (317,692)
background.paste(green_bg1, smile_position, green_bg1)

"""right_img= Image.open("bike1.png").convert("RGBA")
right_size=right_img.resize((300,295))
rotated_right = right_size.rotate(0, expand=True)
green_bg2 = Image.new("RGBA", rotated_right.size, "#1F9173")
green_bg2.paste(rotated_right, (0, 0), rotated_right)
right_position=(739,625)
background.paste(green_bg2, right_position, green_bg2)"""

"""food_img=Image.open("nveg1.png")
img_size=food_img.resize((270,270))
mask = Image.new("L", img_size.size, 0)
draw = ImageDraw.Draw(mask)
circle_padding = 30  
left = circle_padding
top = circle_padding
right = img_size.size[0] - circle_padding
bottom = img_size.size[1] - circle_padding
draw.ellipse((left, top, right, bottom), fill=255)
rounded_type_img = Image.new("RGBA", img_size.size)
rounded_type_img.paste(img_size, (0, 0), mask)
img_position = (179,417)
background.paste(rounded_type_img, img_position, rounded_type_img)

food_img2 = Image.open("cfry.png").convert("RGBA")
img_size2 = food_img2.resize((277, 278))
mask2 = Image.new("L", img_size2.size, 0)
draw2 = ImageDraw.Draw(mask2)
draw2.ellipse((left, top, right, bottom), fill=255)
rounded_food_img2 = Image.new("RGBA", img_size2.size)
rounded_food_img2.paste(img_size2, (0, 0), mask2)
img2_position = (629,417) 
background.paste(rounded_food_img2, img2_position, rounded_food_img2)"""



# Map dish names to images
dish_images = {
    "chickenbiriyani": "nveg1.png",
    "grill": "grill1.png",
    "dosa": "dosa4.png",
    "chicken": "c65.png",
    "meals": "veg1.png",
    "idli": "id2.png",
    "sambarvadai":"sambarvadaiwbg.png",
    "uthappam":"uthappamwbg.png",
    "venpongal":"venpongalwbg.png",
    "poori":"pooriwbg.png",
    "vegbiriyani":"vbiriyaniwbg.png",
    "mushroombiriyani":"musbiriyaniwbg.png",
    "sambarrice":"sambarricewbg1.png",
    "lemonrice":"lemonricewbg.png",
    "tomatorice":"tomatoricewbg4.png",
    "curdrice":"curdricewbg1.png",
    "vegfriedrice":"vegricewbg.png",
    "mushroomfriedrice":"mushroomricewbg1.png",
    "paneerfriedrice":"paneerricewbg.png",
    "kothuparotta":"kothuparottawbg.png",
    "mushroom65":"mushroom65wbg.png",
    "paneerbuttermasala":"paneerbuttermasalawbg.png",
    "mushroomnoodles":"mushroomnoodleswbg1.png",
    "chappathi":"cg1.png",
    "appam":"appamwbg.png",
    "idiyappam":"idiyappamwbg.png",
    "puttu":"put2.png",
    "omelette":"omelettewbg.png",
    "kalaki":"kalakiwbg.png",
    "eggbiriyani":"eb2.png",
    "muttonbiriyani":"muttonbiriyaniwbg.png",
    "karidosa":"dosa4.png",
    "vazhai ilai parotta":"kpwbg.png",
    "fishfry":"fishfrywbg.png",
    "muttonchukka":"muttonchukkawbg.png",
    "chickenfriedrice":"chickenrisewbg.png",
    "prawnbiriyani":"prawnbiriyaniwbg.png",
    "kaadaibiriyani":"kaadaibiriyaniwbg.png",
    "nattu kozhi biriyani":"nveg1.png",
    "kaadairoast":"kaadairoastwbg.png",
    "chilli kaadai":"kaadairoastwbg.png",
    "chickentikka":"chickentikkawbg.png",
    "sandwich":"sandwhichwbg.png",
    "pizza":"piz3.png",
    "shawarma":"shawarmawbg.png",
    "burger":"burgerwbg.png",
    "frenchfries":"ff.png",
    "friedchickenlolipop":"fclolipopwbg.png",
    "lime juice":"limewbg.png",
}


# Get the correct image paths
dish1_img_path = dish_images.get(dish1, "default.png")
dish2_img_path = dish_images.get(dish2, "default.png")

# Define positions for the images
positions = [(179, 417), (629, 417)]
dish_paths = [dish1_img_path, dish2_img_path]

# Load and paste each dish image with a circular mask
for i, dish_img_path in enumerate(dish_paths):
    # Load and resize image
    dish_img = Image.open(dish_img_path).convert("RGBA")
    img_size = dish_img.resize((270, 270))

    # Create a circular mask
    mask = Image.new("L", img_size.size, 0)
    draw = ImageDraw.Draw(mask)
    circle_padding = 30
    draw.ellipse(
        (circle_padding, circle_padding, img_size.size[0] - circle_padding, img_size.size[1] - circle_padding),
        fill=255
    )

    # Apply the circular mask
    rounded_img = Image.new("RGBA", img_size.size)
    rounded_img.paste(img_size, (0, 0), mask)

    # Paste onto background at the given position
    background.paste(rounded_img, positions[i], rounded_img)


draw = ImageDraw.Draw(background)
"""hotel_name = "Hotel karna"
hotel_font = ImageFont.truetype("arialbd.ttf", 50)
try:
    text_width, text_height = draw.textbbox((0, 0), hotel_name, font=hotel_font)[2:4]  
except AttributeError:
    text_width, text_height = hotel_font.getbbox(hotel_name)[2:4] 
x, y = 420, 330
padding_x = 15
padding_y = 15
border_radius = 20
box_x1 = x - padding_x  
box_y1 = y - padding_y  
box_x2 = x + text_width + padding_x  
box_y2 = y + text_height + padding_y  
draw.rounded_rectangle(
    [(box_x1, box_y1), (box_x2, box_y2)], 
    fill="white", 
    outline="white",  
    width=2,
    radius=border_radius
)
text_x = (box_x1 + box_x2 - text_width) // 2  
text_y = (box_y1 + box_y2 - text_height) // 2  
draw.text((text_x, text_y), hotel_name, fill="#188067", font=hotel_font)"""


"""hotel_font = ImageFont.truetype("arialbd.ttf", 50) 
try:
    text_width, text_height = draw.textbbox((0, 0), hotel_name, font=hotel_font)[2:4]  
except AttributeError: 
    text_width, text_height = hotel_font.getbbox(hotel_name)[2:4] 
center_x = 1080 // 2  
text_x = center_x - (text_width // 2)  
text_y = 330  
padding_x = 40
padding_y = 10
border_radius = 30
box_x1 = text_x - padding_x  
box_y1 = text_y - padding_y  
box_x2 = text_x + text_width + padding_x  
box_y2 = text_y + text_height + padding_y  
draw.rounded_rectangle(
    [(box_x1, box_y1), (box_x2, box_y2)], 
    fill="white", 
    outline="white",  
    width=2,
    radius=border_radius
)
draw.text((text_x, text_y), hotel_name, fill="#188067", font=hotel_font)"""

# Font size limits
max_font_size = 50  
min_font_size = 25  
max_text_width = 800  # Maximum width allowed for text

# Function to adjust font size dynamically
def adjust_font_size(text, max_width, font_path, max_size, min_size):
    font_size = max_size
    while font_size >= min_size:
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getbbox(text)[2]  
        if text_width <= max_width:
            return font, text_width
        font_size -= 2  # Reduce font size gradually
    return ImageFont.truetype(font_path, min_size), text_width  # Use minimum font size if needed

# Adjust font size based on text length
hotel_font, text_width = adjust_font_size(hotel_name, max_text_width, "arialbd.ttf", max_font_size, min_font_size)

# Centered text position
center_x = 1080 // 2  
text_x = center_x - (text_width // 2)  
text_y = 330  

# Padding and border settings
padding_x = 40
padding_y = 10
border_radius = 30

# Box dimensions (dynamically adjusted)
box_x1 = text_x - padding_x  
box_y1 = text_y - padding_y  
box_x2 = text_x + text_width + padding_x  
box_y2 = text_y + hotel_font.getbbox(hotel_name)[3] + padding_y  

# Draw the rounded rectangle for the hotel name background
draw.rounded_rectangle(
    [(box_x1, box_y1), (box_x2, box_y2)], 
    fill="white", 
    outline="white",  
    width=2,
    radius=border_radius
)

# Draw the hotel name text
draw.text((text_x, text_y), hotel_name, fill="#188067", font=hotel_font)





background.show()