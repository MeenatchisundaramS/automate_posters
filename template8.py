import sys
import textwrap
from PIL import Image,ImageDraw,ImageFont


hotel_name = sys.argv[1] 
dish1, dish2, dish3 = sys.argv[2:5]  


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
draw.text((text_x, text_y), hotel_name, fill="#188067", font=hotel_font)"""


"""max_font_size = 60  
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
x, y = 532, 79  
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
draw.text((text_x, text_y), hotel_name, fill="#188067", font=hotel_font)"""


# Font size limits
max_font_size = 60  
min_font_size = 30  
max_text_width = 400  # Maximum width for text before wrapping

# Function to adjust font size dynamically
def adjust_font_size(text, max_width, font_path, max_size, min_size):
    font_size = max_size
    while font_size >= min_size:
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getbbox(text)[2]
        if text_width <= max_width:
            return font
        font_size -= 2  # Reduce font size gradually
    return ImageFont.truetype(font_path, min_size)  # Use minimum font size if needed

# Adjust font based on text length
hotel_font = adjust_font_size(hotel_name, max_text_width, "arialbd.ttf", max_font_size, min_font_size)

# Wrap text into multiple lines
wrapped_text = textwrap.wrap(hotel_name, width=18)  # Adjust width for wrapping

# Get text height dynamically based on number of lines
line_spacing = 5
total_text_height = sum(draw.textbbox((0, 0), line, font=hotel_font)[3] for line in wrapped_text) + (line_spacing * (len(wrapped_text) - 1))

# Fixed position
x, y = 532, 79  
padding_x = 10
padding_y = 20
border_radius = 20

# Box dimensions (Adjust height for multi-line text)
box_x1 = x - padding_x  
box_y1 = y - padding_y  
box_x2 = x + max_text_width + padding_x  
box_y2 = y + total_text_height + padding_y  

# Draw rounded rectangle for background
draw.rounded_rectangle(
    [(box_x1, box_y1), (box_x2, box_y2)], 
    fill="white", 
    outline="white",  
    width=2,
    radius=border_radius
)

# Draw text (centered inside the box, line by line)
text_y = (box_y1 + box_y2 - total_text_height) // 2  # Center vertically
for line in wrapped_text:
    text_width = draw.textlength(line, font=hotel_font)
    text_x = (box_x1 + box_x2 - text_width) // 2  # Center horizontally
    draw.text((text_x, text_y), line, fill="#188067", font=hotel_font)
    text_y += draw.textbbox((0, 0), line, font=hotel_font)[3] + line_spacing  # Move to next line

location="Andipatty"
location_font=ImageFont.truetype("arialbd.ttf",60) 
location_position=((568,189))
draw.text(location_position,f"{location}",fill="white",font=location_font)

description="Get 50% Off   On your First Order!!"
description_font=ImageFont.truetype("arialbd.ttf",40)
max_width=15
wrapped_text = textwrap.fill(description, width=max_width)
text_lines = wrapped_text.split("\n")  
line_heights = [description_font.getbbox(line)[3] for line in text_lines]  
text_width = max(description_font.getbbox(line)[2] for line in text_lines) 
text_height = sum(line_heights) + (len(line_heights) - 1) * 5 
description_x = 580
description_y = 279
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

quote="If You're Hungry And You Want Thousands Of Something,Then Order and Eat!"
quote_font=ImageFont.truetype("arialbd.ttf",38)
max_width=40
wrapped_text = textwrap.fill(quote, width=max_width)
quote_x=171
quote_y=448
draw.multiline_text((quote_x, quote_y), wrapped_text, fill="#0D1850", font=quote_font, spacing=10)

ex_img = Image.open("greenleaf.png")
ex_img_size = ex_img.resize((110, 350))
green_bg2 = Image.new("RGBA", ex_img_size.size, "#1F9173")
mask = ex_img_size.split()[3] if ex_img_size.mode == "RGBA" else None  
green_bg2.paste(ex_img_size, (0, 0), mask) 
green_cap_position1 = (17,292) 
background.paste(green_bg2, green_cap_position1, green_bg2)  


"""food_images = ["biriyani.jpg", "chicken.jpg", "grill.jpg"]  
positions = [(70, 600), (400, 600), (730, 600)]  

for i, food_image in enumerate(food_images):
    img = Image.open(food_image).convert("RGBA")
    img = img.resize((270, 270))  
    border_size = (290, 290)
    border = Image.new("RGBA", border_size, "white")
    border.paste(img, (10, 10), img)
    rotated_img = border.rotate(15, expand=True)  
    bg_x, bg_y = positions[i] 
    rotated_x = bg_x - (rotated_img.width - border_size[0]) // 2  
    rotated_y = bg_y - (rotated_img.height - border_size[1]) // 2  
    background.paste(rotated_img, (rotated_x, rotated_y), rotated_img)"""



# Map dish names to images
dish_images = {
        "chickenbiriyani": "biriyani.jpg",
        "grill": "grillbg.jpg",
        "dosa": "dosa1.png",
        "chicken": "chicken.jpg",
        "meals": "mealsbg.jpg",
        "parotta":"parottabg1.jpg",
        "idli": "idlybg.jpg",
        "uthappam":"uthappambg.jpeg",
        "sambarvadai":"sambarvadaibg.jpg",
        "venpongal":"venpongalbg.jpg",
        "poori":"pooribg.jpg",
        "vegbiriyani":"vbiriyanibg.jpg",
        "mushroombiriyani":"musbiriyani.jpg",
        "sambarrice":"sambarrice.jpg",
        "lemonrice":"lemon.jpg",
        "tomatorice":"tomatoricebg.jpg",
        "curdrice":"curdricebg.jpeg",
        "vegfriedrice":"vegrice.jpg",
        "mushroomfriedrice":"mushroomricebg.jpg",
        "paneerfriedrice":"paneerricebg.jpg",
        "kothuparotta":"kothuparotta.jpg",
        "mushroom65":"mushroom65bg.jpg",
        "paneerbuttermasala":"paneerbuttermasalabg.jpg",
        "mushroomnoodles":"mushroomnoodlesbg.png",
        "chappathi":"chappathibg.jpg",
        "appam":"appambg.jpg",
        "idiyappam":"idiyappambg.jpg",
        "puttu":"puttubg.jpg",
        "omelette":"omelettebg.jpg",
        "kalaki":"kalakibg.jpg",
        "eggbiriyani":"eggbiriyanibg.jpg",
        "muttonbiriyani":"muttonbiriyanibg.jpg",
        "karidosa":"karidosabg.png",
        "vazhai ilai parotta":"kiliparottabg.jpeg",
        "fishfry":"fishfrybg.jpg",
        "muttonchukka":"chukkabg.jpeg",
        "chickenfriedrice":"chickenricebg.png",
        "prawnbiriyani":"prawnbiriyanibg.jpg",
        "kaadaibiriyani":"kaadaibiriyanibg.jpg",
        "nattu kozhi biriyani":"nattukozhibiriyani.jpg",
        "kaadairoast":"kaadairoastbg.jpg",
        "chilli kaadai":"chillikaadaibg.jpg",
        "chickentikka":"chickentikkabg.jpg",
        "sandwich":"sandwichbg.jpg",
        "pizza":"pizzabg.jpg",
        "shawarma":"sawarmabg.png",
        "burger":"burgerbg.jpg",
        "frenchfries":"friesbg.jpg",
        "friedchickenlolipop":"chickenlolipopbg.jpg",
        "lime juice":"limejuicebg.jpg", 
}


# Get Dish Image Paths
dish_paths = [
    dish_images.get(dish1, "default.png"),
    dish_images.get(dish2, "default.png"),
    dish_images.get(dish3, "default.png")
]

# Positions for Three-Image Horizontal Layout
positions = [(70, 600), (400, 600), (730, 600)]

# Load and Paste Each Dish Image
for i, dish_img_path in enumerate(dish_paths):
    dish_img = Image.open(dish_img_path).convert("RGBA").resize((270, 270))
    
    # Add Border
    border = Image.new("RGBA", (290, 290), "white")
    border.paste(dish_img, (10, 10), dish_img)

    # Rotate Image
    rotated_img = border.rotate(15, expand=True)

    # Positioning
    bg_x, bg_y = positions[i]
    rotated_x = bg_x - (rotated_img.width - 290) // 2  
    rotated_y = bg_y - (rotated_img.height - 290) // 2  

    background.paste(rotated_img, (rotated_x, rotated_y), rotated_img)



background.show()