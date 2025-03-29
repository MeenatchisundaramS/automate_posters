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
logo_position = (180,50)
background.paste(rounded_logo, logo_position, rounded_logo)

draw = ImageDraw.Draw(background)

bio="All in One Delivery App"
bio_position=((90,247))
bio_font=ImageFont.truetype("arialbd.ttf",30)
draw.text(bio_position, bio, fill="white", font=bio_font)

quote="If You're Hungry And You Want Thousands Of Something,Then Order and Eat!"
quote_font=ImageFont.truetype("arialbd.ttf",45)
max_width=20
wrapped_text = textwrap.fill(quote, width=max_width)
quote_x=483
quote_y=337
draw.multiline_text((quote_x, quote_y), wrapped_text, fill="#0D1850", font=quote_font, spacing=10)

description="All Your Home Need In a Single App"
description_font=ImageFont.truetype("arialbd.ttf",30)
max_width=20
wrapped_text = textwrap.fill(description, width=max_width)
description_x = 483
description_y = 560
draw.multiline_text((description_x, description_y), wrapped_text, fill="white", font=description_font, spacing=5)

app_site="zaaroz.com"
app_position=((483,643))
app_font=ImageFont.truetype("arialbd.ttf",35)
draw.text(app_position,f"{app_site}",fill="white",font=app_font)

playstore_img=Image.open("playstore.png")
playstore_size=playstore_img.resize((140,40))
playstore_position=(697,640)
background.paste(playstore_size,playstore_position)

ios_img=Image.open("ios.png")
ios_size=ios_img.resize((140,45))
ios_position=(861,637)
background.paste(ios_size,ios_position)



start_point = (483, 694)   
end_point = (998, 694)    
draw.line([start_point, end_point], fill="black", width=6)

"""right_img = Image.open("nveg1.png").convert("RGBA")

small_size = 330 
right_img = right_img.resize((small_size, small_size))

square_canvas = Image.new("RGBA", (small_size, small_size), (255, 255, 255, 0))

square_canvas.paste(right_img, (0, 0), right_img)
border_size = 5  
border_img = Image.new("RGBA", (small_size + border_size*2, small_size + border_size*2), (255, 255, 255, 0))
border_draw = ImageDraw.Draw(border_img)"""
"""border_draw.rectangle(
    [(border_size, border_size), (small_size + border_size, small_size + border_size)],
    fill="white"
)"""
"""border_img.paste(square_canvas, (border_size, border_size), square_canvas)

right_position = (50, 385)  
background.paste(border_img, right_position, border_img)



right_img = Image.open("dosabg.png").convert("RGBA")

new_width = 370  
new_height = 350  
right_img = right_img.resize((new_width, new_height))
wide_canvas = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))
paste_x = (new_width - right_img.width) // 2  
wide_canvas.paste(right_img, (paste_x, 0), right_img)
border_size = 0 
border_img = Image.new("RGBA", (new_width + border_size*2, new_height + border_size*2), (255, 255, 255, 0))
border_draw = ImageDraw.Draw(border_img)"""

"""# Draw the white border
border_draw.rectangle(
    [(border_size, border_size), (new_width + border_size, new_height + border_size)],
    fill="white"
)"""
"""border_img.paste(wide_canvas, (border_size, border_size), wide_canvas)
right_position = (50, 687)
background.paste(border_img, right_position, border_img)""" 



# Ask for 2 dish names


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
dish1_img_path = dish_images.get(dish1, "default.png")  # Default image if not found
dish2_img_path = dish_images.get(dish2, "default.png")

# Load and paste first dish image
right_img = Image.open(dish1_img_path).convert("RGBA")
right_img = right_img.resize((330, 330))
square_canvas = Image.new("RGBA", (330, 330), (255, 255, 255, 0))
square_canvas.paste(right_img, (0, 0), right_img)
border_size = 5
border_img = Image.new("RGBA", (340, 340), (255, 255, 255, 0))
border_img.paste(square_canvas, (border_size, border_size), square_canvas)
background.paste(border_img, (50, 405), border_img)

# Load and paste second dish image 
right_img = Image.open(dish2_img_path).convert("RGBA")
right_img = right_img.resize((350, 350))
wide_canvas = Image.new("RGBA", (370, 350), (255, 255, 255, 0))
wide_canvas.paste(right_img, (0, 0), right_img)
border_img = Image.new("RGBA", (370, 350), (255, 255, 255, 0))
border_img.paste(wide_canvas, (0, 0), wide_canvas)
background.paste(border_img, (50, 707), border_img)

right_img= Image.open("bikenew.png").convert("RGBA")
right_size=right_img.resize((300,275))
rotated_right = right_size.rotate(0, expand=True)
green_bg2 = Image.new("RGBA", rotated_right.size, "#1F9173")
green_bg2.paste(rotated_right, (0, 0), rotated_right)
right_position=(447,702)
background.paste(green_bg2, right_position, green_bg2)

draw = ImageDraw.Draw(background)



"""hotel_name = "Hotel Karna"
hotel_font = ImageFont.truetype("arialbd.ttf", 50)
try:
    text_width, text_height = draw.textbbox((0, 0), hotel_name, font=hotel_font)[2:4]  
except AttributeError:
    text_width, text_height = hotel_font.getbbox(hotel_name)[2:4] 
x, y = 722,79
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

# Get hotel name from user


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
location_font=ImageFont.truetype("arialbd.ttf",40) 
text_width, text_height = draw.textbbox((0, 0), location, font=location_font)[2:4]  
x, y = 620, 247
padding_x = 10
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

tomato=Image.open("tomato.png")
tomato_size1=tomato.resize((260,210)) 
green_bg2 = Image.new("RGBA", tomato_size1.size, "#1F9173") 
mask =tomato_size1.split()[0] if tomato.mode == "RGBA" else None 
green_bg2.paste(tomato_size1, (0, 0), mask)
tomato_position1 = (813,871)
background.paste(green_bg2, tomato_position1, green_bg2) 

draw = ImageDraw.Draw(background)

description="Get 50% Off   On your First Order!!"
description_font=ImageFont.truetype("arialbd.ttf",40)
max_width=15
wrapped_text = textwrap.fill(description, width=max_width)
text_lines = wrapped_text.split("\n")  
line_heights = [description_font.getbbox(line)[3] for line in text_lines]  
text_width = max(description_font.getbbox(line)[2] for line in text_lines) 
text_height = sum(line_heights) + (len(line_heights) - 1) * 5 
description_x = 731
description_y = 734
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

tc="T&C"
tc_position=((960,1049))
tc_font=ImageFont.truetype("arialbd.ttf",20)
draw.text(tc_position,f"{tc}",fill="black",font=tc_font)

background.show()