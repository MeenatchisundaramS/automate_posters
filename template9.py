import sys
import textwrap
from PIL import Image,ImageDraw,ImageFont

hotel_name = sys.argv[1]
dish_names = sys.argv[2:]

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

location="Andipatty"
location_font=ImageFont.truetype("arialbd.ttf",40) 
text_width, text_height = draw.textbbox((0, 0), location, font=location_font)[2:4]  
x, y = 45, 995
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

title_text = "Enjoy the Irresistible Taste of Special Foods"
title_font = ImageFont.truetype("arialbd.ttf", 50)
max_width = 25  
wrapped_text = textwrap.fill(title_text, width=max_width)
title_x, title_y = 450, 180
draw.multiline_text((title_x, title_y), wrapped_text, fill="#0D1850", font=title_font, spacing=10)

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

# Get hotel name from user

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

"""biriyani_img = Image.open("biriyani.jpg").convert("RGBA")
biriyani_img = biriyani_img.resize((450, 450))  
frame_width = 500
frame_height = 580  
frame = Image.new("RGBA", (frame_width, frame_height), "white")
paste_x = (frame_width - biriyani_img.width) // 2
paste_y = 20  
frame.paste(biriyani_img, (paste_x, paste_y), biriyani_img)
rotated_frame = frame.rotate(0, expand=True)  
background.paste(rotated_frame, (280, 320), rotated_frame)"""



# Map dish names to images
dish_images = {
        "chickenbiriyani": "biriyani.jpg",
        "grill": "grillbg.jpg",
        "dosa": "dosa1.png",
        "parotta":"parottabg1.jpg",
        "chicken": "chicken.jpg",
        "meals": "mealsbg.jpg",
        "idli": "idlibg.jpg",
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

dish_img_path = [dish_images.get(dish, "default.png") for dish in dish_names] 

# Load and paste dish image inside a white frame
dish_img = Image.open(dish_img_path[0]).convert("RGBA")
dish_img = dish_img.resize((450, 450))

frame_width = 500
frame_height = 580
frame = Image.new("RGBA", (frame_width, frame_height), "white")

# Center image inside frame
paste_x = (frame_width - dish_img.width) // 2
paste_y = 20
frame.paste(dish_img, (paste_x, paste_y), dish_img)

# Rotate if needed (currently set to 0)
rotated_frame = frame.rotate(0, expand=True)

# Paste final framed image onto background
background.paste(rotated_frame, (280, 320), rotated_frame)


draw = ImageDraw.Draw(background)

order="     Get 50% off \non Your first Order"
order_font=ImageFont.truetype("arialbd.ttf",50)
order_position=((314,790))
draw.text(order_position,f"{order}",fill="orange",font=order_font)

right_img= Image.open("bikenew.png").convert("RGBA")
right_size=right_img.resize((300,275))
rotated_right = right_size.rotate(0, expand=True)
green_bg2 = Image.new("RGBA", rotated_right.size, "#1F9173")
green_bg2.paste(rotated_right, (0, 0), rotated_right)
right_position=(780,717)
background.paste(green_bg2, right_position, green_bg2)

red_cap=Image.open("redcap1.png")
red_cap_size1=red_cap.resize((260,220)) 
green_bg2 = Image.new("RGBA", red_cap_size1.size, "#1F9173") 
mask = red_cap_size1.split()[3] if red_cap.mode == "RGBA" else None 
green_bg2.paste(red_cap_size1, (0, 0), mask)
red_cap_position1 = (20,550)
background.paste(green_bg2, red_cap_position1, green_bg2)

green_cap=Image.open("green1.png")
green_cap_size1=green_cap.resize((260,220)) 
green_bg2 = Image.new("RGBA", green_cap_size1.size, "#1F9173") 
mask = green_cap_size1.split()[3] if green_cap.mode == "RGBA" else None  
green_bg2.paste(green_cap_size1, (0, 0), mask) 
green_cap_position1 = (825,426)
background.paste(green_bg2, green_cap_position1, green_bg2)

tomato=Image.open("tomato.png")
tomato_size1=tomato.resize((260,210)) 
green_bg2 = Image.new("RGBA", tomato_size1.size, "#1F9173") 
mask =tomato_size1.split()[0] if tomato.mode == "RGBA" else None 
green_bg2.paste(tomato_size1, (0, 0), mask)
tomato_position1 = (20,765)
background.paste(green_bg2, tomato_position1, green_bg2) 

background.show() 