import sys
import textwrap
from PIL import Image,ImageDraw,ImageFont



# Get inputs from main.py
hotel_name = sys.argv[1]
dish1, dish2, dish3 = sys.argv[2:5]  # Extract dish names

background = Image.new("RGB", (1080,1080), "#1F9173")
draw = ImageDraw.Draw(background)

order_now=Image.open("order_now1.png")
now_size=order_now.resize((390,390)) 
green_bg2 = Image.new("RGBA", now_size.size, "#1F9173") 
mask = now_size.split()[0] if order_now.mode == "RGBA" else None 
green_bg2.paste(now_size, (0, 0), mask)
now_position = (704,0)
background.paste(green_bg2, now_position, green_bg2)

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

"""hotel_name="Hotel Shiva"
hote_position=((390,49))
hotel_font=ImageFont.truetype("arialbd.ttf",70)
draw.text(hote_position,hotel_name,fill="white",font=hotel_font)"""


# Get hotel name from user


# Font size limits
max_font_size = 55  
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
line_spacing = 3
total_text_height = sum(draw.textbbox((0, 0), line, font=hotel_font)[3] for line in wrapped_text) + (line_spacing * (len(wrapped_text) - 1))

# Fixed position
x, y = 370, 49  
padding_x = 10
padding_y = 10
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

order_now1=Image.open("bnwon1.png")
now_size1=order_now1.resize((210,210)) 
green_bg2 = Image.new("RGBA", now_size1.size, "#1F9173") 
mask = now_size1.split()[3] if order_now1.mode == "RGBA" else None 
green_bg2.paste(now_size1, (0, 0), mask)
now_position1 = (450,560)
background.paste(green_bg2, now_position1, green_bg2)

available_device="App available on"
available_position=((36,995))
available_font=ImageFont.truetype("arialbd.ttf",25)
draw.text(available_position,f"{available_device}",fill="white",font=available_font)

playstore_img=Image.open("playstore.png")
playstore_size=playstore_img.resize((150,50))
playstore_position=(36,1030)
background.paste(playstore_size,playstore_position)

ios_img=Image.open("ios.png")
ios_size=ios_img.resize((150,50))
ios_position=(201,1030)
background.paste(ios_size,ios_position)

tc="T&C"
tc_position=((960,1049))
tc_font=ImageFont.truetype("arialbd.ttf",20)
draw.text(tc_position,f"{tc}",fill="black",font=tc_font)

location="Andipatty"
location_font=ImageFont.truetype("arialbd.ttf",40) 
text_width, text_height = draw.textbbox((0, 0), location, font=location_font)[2:4]  
x, y = 470, 1010
padding_x = 20
padding_y = 20
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

description="WHATEVER'S YUMMY GOES IN MY TUMMY"
description_font = ImageFont.truetype("arialbd.ttf", 45)
max_width = 20
wrapped_text = textwrap.fill(description, width=max_width)
description_x = 304  
description_y = 801
draw.multiline_text((description_x, description_y), wrapped_text, fill="white", font=description_font, spacing=5)

red_cap=Image.open("redcap1.png")
red_cap_size1=red_cap.resize((260,220)) 
green_bg2 = Image.new("RGBA", red_cap_size1.size, "#1F9173") 
mask = red_cap_size1.split()[3] if red_cap.mode == "RGBA" else None 
green_bg2.paste(red_cap_size1, (0, 0), mask)
red_cap_position1 = (20,580)
background.paste(green_bg2, red_cap_position1, green_bg2)

tomato=Image.open("tomato.png")
tomato_size1=tomato.resize((260,210)) 
green_bg2 = Image.new("RGBA", tomato_size1.size, "#1F9173") 
mask =tomato_size1.split()[0] if tomato.mode == "RGBA" else None 
green_bg2.paste(tomato_size1, (0, 0), mask)
tomato_position1 = (20,785)
background.paste(green_bg2, tomato_position1, green_bg2)

green_cap=Image.open("green1.png")
green_cap_size1=green_cap.resize((260,220)) 
green_bg2 = Image.new("RGBA", green_cap_size1.size, "#1F9173") 
mask = green_cap_size1.split()[3] if green_cap.mode == "RGBA" else None 
green_bg2.paste(green_cap_size1, (0, 0), mask)
green_cap_position1 = (825,716)
background.paste(green_bg2, green_cap_position1, green_bg2)

"""chicken_img = Image.open("nveg1.png").convert("RGBA")  
zoom_out_factor = 0.6  
new_size = (int(chicken_img.width * zoom_out_factor), int(chicken_img.height * zoom_out_factor))
chicken_img = chicken_img.resize(new_size)
canvas_size = (350, 340)  
canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))  
paste_x = (canvas_size[0] - new_size[0]) // 2
paste_y = (canvas_size[1] - new_size[1]) // 2
canvas.paste(chicken_img, (paste_x, paste_y), chicken_img)  
mask = Image.new("L", canvas_size, 0)
draw = ImageDraw.Draw(mask)
diamond_points = [(canvas_size[0]//2, 0), (canvas_size[0], canvas_size[1]//2), 
                  (canvas_size[0]//2, canvas_size[1]), (0, canvas_size[1]//2)]
draw.polygon(diamond_points, fill=255)
diamond_image = Image.new("RGBA", canvas_size)
diamond_image.paste(canvas, (0, 0), mask)
border_size = 10 
border_img = Image.new("RGBA", (canvas_size[0] + border_size*2, canvas_size[1] + border_size*2), (255, 255, 255, 0))
border_draw = ImageDraw.Draw(border_img)
border_points = [(p[0] + border_size, p[1] + border_size) for p in diamond_points]
border_draw.polygon(border_points, fill="white")
border_img.paste(diamond_image, (border_size, border_size), diamond_image)
chicken_position = (380, 140)  
background.paste(border_img, chicken_position, border_img)

left_img = Image.open("dosabg.png").convert("RGBA") 
zoom_out_factor = 0.6  
new_size = (int(left_img.width * zoom_out_factor), int(left_img.height * zoom_out_factor))
left_img = left_img.resize(new_size)
canvas_size = (350, 340)
left_canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))  
paste_x = (canvas_size[0] - new_size[0]) // 2
paste_y = (canvas_size[1] - new_size[1]) // 2
left_canvas.paste(left_img, (paste_x, paste_y), left_img) 
mask = Image.new("L", canvas_size, 0)
draw = ImageDraw.Draw(mask)
diamond_points = [(canvas_size[0]//2, 0), (canvas_size[0], canvas_size[1]//2), 
                  (canvas_size[0]//2, canvas_size[1]), (0, canvas_size[1]//2)]
draw.polygon(diamond_points, fill=255)
diamond_image = Image.new("RGBA", canvas_size)
diamond_image.paste(left_canvas, (0, 0), mask)
border_size = 10  
border_img = Image.new("RGBA", (canvas_size[0] + border_size*2, canvas_size[1] + border_size*2), (255, 255, 255, 0))
border_draw = ImageDraw.Draw(border_img)
border_points = [(p[0] + border_size, p[1] + border_size) for p in diamond_points]
border_draw.polygon(border_points, fill="white")
border_img.paste(diamond_image, (border_size, border_size), diamond_image)
left_position = (200, 320)  
background.paste(border_img, left_position, border_img)

right_img = Image.open("c65.png").convert("RGBA")  
new_size = (int(right_img.width * zoom_out_factor), int(right_img.height * zoom_out_factor))
right_img = right_img.resize(new_size)
right_canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))
paste_x = (canvas_size[0] - new_size[0]) // 2
paste_y = (canvas_size[1] - new_size[1]) // 2
right_canvas.paste(right_img, (paste_x, paste_y), right_img) 
mask = Image.new("L", canvas_size, 0)
draw = ImageDraw.Draw(mask)
draw.polygon(diamond_points, fill=255)
diamond_image = Image.new("RGBA", canvas_size)
diamond_image.paste(right_canvas, (0, 0), mask)
border_img = Image.new("RGBA", (canvas_size[0] + border_size*2, canvas_size[1] + border_size*2), (255, 255, 255, 0))
border_draw = ImageDraw.Draw(border_img)
border_draw.polygon(border_points, fill="white")
border_img.paste(diamond_image, (border_size, border_size), diamond_image)
right_position = (560, 320)  
background.paste(border_img, right_position, border_img)"""







# Dish mapping
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
    "chappathi":"chappathiwbg2.png",
    "appam":"appamwbg.png",
    "idiyappam":"idiyappamwbg.png",
    "puttu":"puttuwbg.png",
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

dish_paths = [dish_images.get(dish, "default.png") for dish in [dish1, dish2, dish3]]

# Define positions for the images
positions = [(380, 140), (200, 320), (560, 320)]
canvas_size = (350, 340)  # Fixed size for each canvas
border_size = 10  # Border thickness

# Process and paste images
for i, dish_img_path in enumerate(dish_paths):
    # Load and resize image
    img = Image.open(dish_img_path).convert("RGBA")
    zoom_out_factor = 0.6  
    new_size = (int(img.width * zoom_out_factor), int(img.height * zoom_out_factor))
    img = img.resize(new_size)

    # Create transparent canvas
    canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))
    paste_x = (canvas_size[0] - new_size[0]) // 2
    paste_y = (canvas_size[1] - new_size[1]) // 2
    canvas.paste(img, (paste_x, paste_y), img)

    # Create diamond mask
    mask = Image.new("L", canvas_size, 0)
    draw_mask = ImageDraw.Draw(mask)
    diamond_points = [
        (canvas_size[0]//2, 0), (canvas_size[0], canvas_size[1]//2),
        (canvas_size[0]//2, canvas_size[1]), (0, canvas_size[1]//2)
    ]
    draw_mask.polygon(diamond_points, fill=255)

    # Apply diamond mask
    diamond_image = Image.new("RGBA", canvas_size)
    diamond_image.paste(canvas, (0, 0), mask)

    # Create white border
    border_img = Image.new("RGBA", (canvas_size[0] + border_size*2, canvas_size[1] + border_size*2), (255, 255, 255, 0))
    border_draw = ImageDraw.Draw(border_img)
    border_points = [(p[0] + border_size, p[1] + border_size) for p in diamond_points]
    border_draw.polygon(border_points, fill="white")
    border_img.paste(diamond_image, (border_size, border_size), diamond_image)

    # Paste final image onto background
    background.paste(border_img, positions[i], border_img)

background.show()