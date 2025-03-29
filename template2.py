import sys
import textwrap
from PIL import Image,ImageDraw,ImageFont


# Get inputs from main.py
hotel_name = sys.argv[1]
dish1, dish2 = sys.argv[2:5]

background = Image.new("RGB", (736,736), "#1F9173")
draw = ImageDraw.Draw(background)

logo = Image.open("zaaroz_logo1.png")
logo_size = logo.resize((130, 130))
logo_position = (607,0)
background.paste(logo_size, logo_position)

bio="is now available in ZAAROZ!"
bio_position=((230,107))
bio_font=ImageFont.truetype("arial.ttf",20)
draw.text(bio_position, bio, fill="white", font=bio_font)

side_img=Image.open("s_offer.png")
side_size=side_img.resize((130,130))
green_bg2=Image.new("RGBA",side_size.size, "#1F9173")
green_bg2.paste(side_size,(0,0),side_size)
side_position=(1,0)
background.paste(green_bg2,side_position,green_bg2)

quote="I'm not sure what's more addictive, biryani or the feeling of having a plate of biryani in front of me."
quote_font=ImageFont.truetype("arialbd.ttf",30)
max_width=25
wrapped_text = textwrap.fill(quote, width=max_width)
quote_x=250
quote_y=150
draw.multiline_text((quote_x, quote_y), wrapped_text, fill="#0D1850", font=quote_font, spacing=10)

"""order_now=Image.open("or1.png")
now_size=order_now.resize((165,200))
green_bg2 = Image.new("RGBA", now_size.size, "#1F9173") 
mask = now_size.split()[3] if order_now.mode == "RGBA" else None 
green_bg2.paste(now_size, (0, 0), mask)
now_position = (515, 160)
background.paste(green_bg2, now_position, green_bg2)""" 


right_img= Image.open("bike1.png").convert("RGBA")
right_size=right_img.resize((300,300))
green_bg2=Image.new("RGBA",right_size.size, "#1F9173")
green_bg2.paste(right_size,(0,0),right_size)
right_position=(210,356)
background.paste(green_bg2,right_position,green_bg2)

available_device="App available on"
available_position=((10,620))
available_font=ImageFont.truetype("arial.ttf",20)
draw.text(available_position,f"{available_device}",fill="white",font=available_font)

playstore_img=Image.open("playstore.png")
playstore_size=playstore_img.resize((150,40))
playstore_position=(10,644)
background.paste(playstore_size,playstore_position)

ios_img=Image.open("ios.png")
ios_size=ios_img.resize((150,40))
ios_position=(10,686)
background.paste(ios_size,ios_position)

app_site="zaaroz.com"
app_position=((545,670))
app_font=ImageFont.truetype("arialbd.ttf",25)
draw.text(app_position,f"{app_site}",fill="white",font=app_font)

tc="T&C"
tc_position=((639,699))
tc_font=ImageFont.truetype("arialbd.ttf",20)
draw.text(tc_position,f"{tc}",fill="black",font=tc_font)

location="Andipatty"
location_font=ImageFont.truetype("arialbd.ttf",30) 
text_width, text_height = draw.textbbox((0, 0), location, font=location_font)[2:4]  
x, y = 273,658
padding_x = 20
padding_y = 10
border_radius = 20
draw.rounded_rectangle(
    [(x - padding_x, y - padding_y), (x + text_width + padding_x, y + text_height + padding_y)], 
    fill="white", 
    outline="white",  
    width=2,
    radius=border_radius 
    )
draw.text((x, y), f"{location}", fill="#188067", font=location_font) 

"""hotel_name="Hotel Karna"
name_font = ImageFont.truetype("arialbd.ttf", 35)  # Increased font size for better visibility

# Wrap text into multiple lines with **increased width** (more characters per line)
wrapped_text = textwrap.wrap(hotel_name, width=18)  # Adjusted width to fit more text per line

# Position text at the **top center** of the image
y_start = 20  # Keep it near the top
line_spacing = 5  # Reduce line gap for better alignment

# Draw all lines **centered horizontally**
for i, line in enumerate(wrapped_text):
    text_width, text_height = draw.textbbox((0, 0), line, font=name_font)[2:4]
    x_position = (background.width - text_width) // 2  # Center horizontally
    y_position = y_start + i * (text_height + line_spacing)  # Stack lines properly

    draw.text((x_position, y_position), line, fill="white", font=name_font)"""

# Get hotel name from user


# Function to adjust font size dynamically based on text length
def get_adjusted_font(text, max_width, font_path, max_size, min_size):
    font_size = max_size
    while font_size >= min_size:
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getbbox(text)[2]
        if text_width <= max_width:
            return font
        font_size -= 2  # Decrease font size
    return ImageFont.truetype(font_path, min_size)  # Return smallest font if needed

# Define font size limits
max_font_size = 35
min_font_size = 20

# Adjust font based on text length
name_font = get_adjusted_font(hotel_name, 600, "arialbd.ttf", max_font_size, min_font_size)

# Wrap text into multiple lines dynamically
wrapped_text = textwrap.wrap(hotel_name, width=18)  # Adjust width as needed

# Position text at the **top center** of the image
y_start = 20  # Keep it near the top
line_spacing = 5  # Reduce line gap for better alignment

# Draw all lines **centered horizontally**
for i, line in enumerate(wrapped_text):
    text_width, text_height = draw.textbbox((0, 0), line, font=name_font)[2:4]
    x_position = (background.width - text_width) // 2  # Center horizontally
    y_position = y_start + i * (text_height + line_spacing)  # Stack lines properly

    draw.text((x_position, y_position), line, fill="white", font=name_font)


description="Get 50% Off   On your First Order!!"
description_font=ImageFont.truetype("arialbd.ttf",30)
max_width=15
wrapped_text = textwrap.fill(description, width=max_width)
text_lines = wrapped_text.split("\n")  
line_heights = [description_font.getbbox(line)[3] for line in text_lines]  
text_width = max(description_font.getbbox(line)[2] for line in text_lines) 
text_height = sum(line_heights) + (len(line_heights) - 1) * 5 
description_x = 29
description_y = 210
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





"""type_img2= Image.open("non_veg.jpeg")
type_size = type_img2.resize((230,230))
mask = Image.new("L", type_size.size, 0)
draw = ImageDraw.Draw(mask)
circle_padding = 30  
left = circle_padding
top = circle_padding
right = type_size.size[0] - circle_padding
bottom = type_size.size[1] - circle_padding
draw.ellipse((left, top, right, bottom), fill=255)
rounded_type_img = Image.new("RGBA", type_size.size)
rounded_type_img.paste(type_size, (0, 0), mask)
type_position = (250,150)
background.paste(rounded_type_img, type_position, rounded_type_img)"""



   
"""food_img1 = Image.open("input1.jpg").convert("RGBA")
img_size1 = food_img1.resize((230, 230))
mask1 = Image.new("L", img_size1.size, 0)
draw1 = ImageDraw.Draw(mask1)
circle_padding = 30  
left = circle_padding
top = circle_padding
right = img_size1.size[0] - circle_padding
bottom = img_size1.size[1] - circle_padding
draw1.ellipse((left, top, right, bottom), fill=255)
rounded_food_img1 = Image.new("RGBA", img_size1.size)
rounded_food_img1.paste(img_size1, (0, 0), mask1)
img1_position = (47, 325)
background.paste(rounded_food_img1, img1_position, rounded_food_img1)

food_img2 = Image.open("chicken1.jpg").convert("RGBA")
img_size2 = food_img2.resize((230, 230))
mask2 = Image.new("L", img_size2.size, 0)
draw2 = ImageDraw.Draw(mask2)
draw2.ellipse((left, top, right, bottom), fill=255)
rounded_food_img2 = Image.new("RGBA", img_size2.size)
rounded_food_img2.paste(img_size2, (0, 0), mask2)
img2_position = (512,329) 
background.paste(rounded_food_img2, img2_position, rounded_food_img2)"""

    
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

dish_paths = [dish_images.get(dish, "default.png") for dish in [dish1, dish2]]


positions = [(47, 325), (495,329)]

for i, dish_img_path in enumerate(dish_paths):
    img = Image.open(dish_img_path).convert("RGBA").resize((230, 230))
    background.paste(img, positions[i], img)
    

background.show()