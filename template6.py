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

playstore_img=Image.open("playstore.png")
playstore_size=playstore_img.resize((170,70))
playstore_position=(365,1000)
background.paste(playstore_size,playstore_position)

ios_img=Image.open("ios.png")
ios_size=ios_img.resize((170,70))
ios_position=(590,1000)
background.paste(ios_size,ios_position)

app_site="zaaroz.com"
app_position=((815,1010))
app_font=ImageFont.truetype("arialbd.ttf",35)
draw.text(app_position,f"{app_site}",fill="white",font=app_font)

tc="T&C"
tc_position=((960,1049))
tc_font=ImageFont.truetype("arialbd.ttf",20)
draw.text(tc_position,f"{tc}",fill="black",font=tc_font)

order_now=Image.open("or1.png")
now_size=order_now.resize((240,240))
green_bg2 = Image.new("RGBA", now_size.size, "#1F9173") 
mask = now_size.split()[3] if order_now.mode == "RGBA" else None 
green_bg2.paste(now_size, (0, 0), mask)
now_position = (345,704)
background.paste(green_bg2, now_position, green_bg2)

"""meals=Image.open("meals.png")
meals_size=meals.resize((455,365))
green_bg2 = Image.new("RGBA", meals_size.size, "#1F9173") 
mask = meals_size.split()[3] if meals.mode == "RGBA" else None 
green_bg2.paste(meals_size, (0, 0), mask)
meals_position = (29,362)
background.paste(green_bg2, meals_position, green_bg2)


biriyani=Image.open("nveg1.png")
biriyani_size=biriyani.resize((405,395))
green_bg2 = Image.new("RGBA", biriyani_size.size, "#1F9173") 
mask = biriyani_size.split()[3] if biriyani.mode == "RGBA" else None 
green_bg2.paste(biriyani_size, (0, 0), mask)
biriyani_position = (600,580)
background.paste(green_bg2, biriyani_position, green_bg2)""" 

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
dish1_img_path = dish_images.get(dish1, "default.png")  # Default image if not found
dish2_img_path = dish_images.get(dish2, "default.png")

# Load and paste first dish image ("meals")
dish1_img = Image.open(dish1_img_path).convert("RGBA")
dish1_img = dish1_img.resize((405,395))
square_canvas = Image.new("RGBA", (455, 365), (255, 255, 255, 0))
square_canvas.paste(dish1_img, (0, 0), dish1_img)
border_size = 5
border_img = Image.new("RGBA", (465, 375), (255, 255, 255, 0))
border_img.paste(square_canvas, (border_size, border_size), square_canvas)
background.paste(border_img, (29, 342), border_img)

draw = ImageDraw.Draw(background)

quote="I'm not sure what's more addictive, biryani or the feeling of having a plate of biryani in front of me."
quote_font=ImageFont.truetype("arialbd.ttf",45)
max_width=28
wrapped_text = textwrap.fill(quote, width=max_width)
quote_x=480
quote_y=339
draw.multiline_text((quote_x, quote_y), wrapped_text, fill="#0D1850", font=quote_font, spacing=10)

# Load and paste second dish image ("biriyani")
dish2_img = Image.open(dish2_img_path).convert("RGBA")
dish2_img = dish2_img.resize((405, 395))
square_canvas = Image.new("RGBA", (405, 395), (255, 255, 255, 0))
square_canvas.paste(dish2_img, (0, 0), dish2_img)
border_size = 5
border_img = Image.new("RGBA", (415, 405), (255, 255, 255, 0))
border_img.paste(square_canvas, (border_size, border_size), square_canvas)
background.paste(border_img, (600, 580), border_img)



"""right_img= Image.open("bikenew.png").convert("RGBA")
right_size=right_img.resize((380,335))
rotated_right = right_size.rotate(0, expand=True)
green_bg2 = Image.new("RGBA", rotated_right.size, "#1F9173")
green_bg2.paste(rotated_right, (0, 0), rotated_right)
right_position=(569,278)
background.paste(green_bg2, right_position, green_bg2)"""

draw = ImageDraw.Draw(background)

description="Get 50% Off   On your First Order!!"
description_font=ImageFont.truetype("arialbd.ttf",40)
max_width=15
wrapped_text = textwrap.fill(description, width=max_width)
text_lines = wrapped_text.split("\n")  
line_heights = [description_font.getbbox(line)[3] for line in text_lines]  
text_width = max(description_font.getbbox(line)[2] for line in text_lines) 
text_height = sum(line_heights) + (len(line_heights) - 1) * 5 
description_x = 46
description_y = 756
padding_x = 10
padding_y = 10
border_radius = 15
box_x1 = description_x - padding_x
box_y1 = description_y - padding_y
box_x2 = description_x + text_width + padding_x
box_y2 = description_y + text_height + padding_y
draw.rounded_rectangle(
    [(box_x1, box_y1), (box_x2, box_y2)],
    fill="orange",
    outline="orange",
    width=2,
    radius=border_radius
)
draw.multiline_text((description_x, description_y), wrapped_text, fill="white", font=description_font, spacing=5)

"""hotel_name = "Hotel Karna"
hotel_font = ImageFont.truetype("arialbd.ttf", 60)
try:
    text_width, text_height = draw.textbbox((0, 0), hotel_name, font=hotel_font)[2:4]  
except AttributeError:
    text_width, text_height = hotel_font.getbbox(hotel_name)[2:4] 
x, y = 532,79
padding_x = 10
padding_y = 20
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
draw.text((text_x, text_y), hotel_name, fill="#188067", font=hotel_font)
"""

max_font_size = 60  
min_font_size = 30  
def adjust_font_size(text, max_width, font_path, max_size, min_size):
    font_size = max_size
    while font_size >= min_size:
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getbbox(text)[2]
        if text_width <= max_width:
            return font, text_width
        font_size -= 2
    return ImageFont.truetype(font_path, min_size), text_width 
hotel_font, hotel_text_width = adjust_font_size(hotel_name, 400, "arialbd.ttf", max_font_size, min_font_size)
hotel_text_height = hotel_font.getbbox(hotel_name)[3]
x, y = 500, 79  
padding_x = 10
padding_y = 20
border_radius = 20
box_x1 = x - padding_x  
box_y1 = y - padding_y  
box_x2 = x + hotel_text_width + padding_x  
box_y2 = y + hotel_text_height + padding_y  
draw.rounded_rectangle(
    [(box_x1, box_y1), (box_x2, box_y2)], 
    fill="white", 
    outline="white",  
    width=2,
    radius=border_radius
)
text_x = (box_x1 + box_x2 - hotel_text_width) // 2  
text_y = (box_y1 + box_y2 - hotel_text_height) // 2  
draw.text((text_x, text_y), hotel_name, fill="#188067", font=hotel_font)

location="Andipatty"
location_font=ImageFont.truetype("arialbd.ttf",60) 
location_position=((568,189))
draw.text(location_position,f"{location}",fill="white",font=location_font)

background.show()