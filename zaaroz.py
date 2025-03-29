import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

def green():

    hotel_name = sys.argv[1]
    dish1, dish2, dish3 = sys.argv[2:5]
    background = Image.new("RGB", (1000, 1000), "#1F9173")
    draw = ImageDraw.Draw(background)


    logo = Image.open("zaaroz_logo1.png")
    logo_size = logo.resize((150, 150))
    logo_position = (780, 0)
    background.paste(logo_size, logo_position)

    bio="is now available in ZAAROZ!"
    bio_position=((285,117))
    bio_font=ImageFont.truetype("arial.ttf",30)
    draw.text(bio_position, bio, fill="white", font=bio_font)

    available_device="App available on"
    available_position=((21,910))
    available_font=ImageFont.truetype("arial.ttf",20)
    draw.text(available_position,f"{available_device}",fill="white",font=available_font)

    playstore_img=Image.open("playstore.png")
    playstore_size=playstore_img.resize((150,40))
    playstore_position=(20,940)
    background.paste(playstore_size,playstore_position)

    ios_img=Image.open("ios.png")
    ios_size=ios_img.resize((150,40))
    ios_position=(181,940)
    background.paste(ios_size,ios_position)

    app_site="zaaroz.com"
    app_position=((780,930))
    app_font=ImageFont.truetype("arialbd.ttf",30)
    draw.text(app_position,f"{app_site}",fill="white",font=app_font)

    tc="T&C"
    tc_position=((880,970))
    tc_font=ImageFont.truetype("arialbd.ttf",20)
    draw.text(tc_position,f"{tc}",fill="black",font=tc_font)

    quote="If You're Hungry And You Want Thousands Of Something,Then Order and Eat!"
    quote_font=ImageFont.truetype("arialbd.ttf",45)
    max_width=20
    wrapped_text = textwrap.fill(quote, width=max_width)
    quote_x=52
    quote_y=307
    draw.multiline_text((quote_x, quote_y), wrapped_text, fill="#0D1850", font=quote_font, spacing=10)

    
    order_now=Image.open("or1.png")
    now_size=order_now.resize((210,210))
    green_bg2 = Image.new("RGBA", now_size.size, "#1F9173") 
    mask = now_size.split()[3] if order_now.mode == "RGBA" else None 
    green_bg2.paste(now_size, (0, 0), mask)
    now_position = (667, 722)
    background.paste(green_bg2, now_position, green_bg2)

    default_img = Image.open("phone1.png").convert("RGBA")  
    default_size = default_img.resize((210, 220))
    orange_bg = Image.new("RGBA", default_size.size, "#1F9173")  
    orange_bg.paste(default_size, (0, 0), default_size)  
    default_position = (1, 0)
    background.paste(orange_bg, default_position, orange_bg)  

    right_img= Image.open("bike1.png").convert("RGBA")
    right_size=right_img.resize((350,370))
    orange_bg2=Image.new("RGBA",right_size.size, "#1F9173")
    orange_bg2.paste(right_size,(0,0),right_size)
    right_position=(620,160)
    background.paste(orange_bg2,right_position,orange_bg2)

    #background.save("zaaroz_template.jpg","JPEG")

    """hotel_name="Hotel Karna"
    hotel_font=ImageFont.truetype("arialbd.ttf",60)
    image_width = background.width
    text_width = draw.textlength(hotel_name, font=hotel_font)
    hotel_position = ((image_width - text_width) // 2, 401)
    draw.text(hotel_position, hotel_name, fill="white", font=hotel_font)"""

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
    max_font_size = 50
    min_font_size = 30

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



    location="Andipatty"
    location_font=ImageFont.truetype("arialbd.ttf",40) 
    text_width, text_height = draw.textbbox((0, 0), location, font=location_font)[2:4]  
    x, y = 410, 930 
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

    description="Get 50% Off   On your First Order!!"
    description_font=ImageFont.truetype("arialbd.ttf",40)
    max_width=15
    wrapped_text = textwrap.fill(description, width=max_width)
    text_lines = wrapped_text.split("\n")  
    line_heights = [description_font.getbbox(line)[3] for line in text_lines]  
    text_width = max(description_font.getbbox(line)[2] for line in text_lines) 
    text_height = sum(line_heights) + (len(line_heights) - 1) * 5 
    description_x = 660
    description_y = 600
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
    type_size = type_img2.resize((300, 300))
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
    type_position = (320, 80)
    background.paste(rounded_type_img, type_position, rounded_type_img)"""
    

    

    """img1=Image.open("chicken.jpg")
    img1_size=img1.resize((166,250))
    img1_position=(52,576)
    background.paste(img1_size,img1_position)

    img2=Image.open("biriyani.jpg")
    img2_size=img2.resize((166,250))
    img2_position=(217,576)
    background.paste(img2_size,img2_position)

    img3=Image.open("grill.jpg")
    img3_size=img3.resize((166,250))
    img3_position=(383,576)
    background.paste(img3_size,img3_position)"""


    # Define dish-to-image mapping
    dish_images = {
        "chickenbiriyani": "biriyani.jpg",
        "grill": "grillbg.jpg",
        "dosa": "dosa1.png",
        "chicken": "chicken.jpg",
        "meals": "mealsbg.jpg",
        "parotta":"parottabg1.jpg",
        "idli": "idlybg.jpg",
        "sambarvadai":"sambarvadaibg.jpg",
        "uthappam":"uthappambg.jpeg",
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

    dish_paths = [dish_images.get(dish, "default.png") for dish in [dish1, dish2, dish3]]

    # Define positions for the images
    positions = [(52,576), (227, 576), (410, 576)]

    # Paste images
    for i, dish_img_path in enumerate(dish_paths):
        img = Image.open(dish_img_path).convert("RGBA").resize((186,260))
        background.paste(img, positions[i], img)

    







    background.show()
    #background.save("zaaroz_output.jpg","JPEG")

def orange():
    background=Image.new("RGB",(1000,1000),"#FF6E00")
    draw = ImageDraw.Draw(background)

    logo = Image.open("zaaroz_logo1.png")
    logo_size = logo.resize((150, 150))
    logo_position = (780, 0)
    background.paste(logo_size, logo_position)

    bio="is now available in ZAAROZ!"
    bio_position=((260,518))
    bio_font=ImageFont.truetype("arial.ttf",40)
    draw.text(bio_position, bio, fill="white", font=bio_font)

    available_device="App available on"
    available_position=((21,910))
    available_font=ImageFont.truetype("arial.ttf",20)
    draw.text(available_position,f"{available_device}",fill="white",font=available_font)

    playstore_img=Image.open("playstore.png")
    playstore_size=playstore_img.resize((150,40))
    playstore_position=(20,940)
    background.paste(playstore_size,playstore_position)

    ios_img=Image.open("ios.png")
    ios_size=ios_img.resize((150,40))
    ios_position=(181,940)
    background.paste(ios_size,ios_position)

    app_site="zaaroz.com"
    app_position=((760,930))
    app_font=ImageFont.truetype("arialbd.ttf",40)
    draw.text(app_position,f"{app_site}",fill="white",font=app_font)

    order_now = "Order \n Now"
    now_position = (667, 762) 
    now_font = ImageFont.truetype("arialbd.ttf", 30)
    now_text_width, now_text_height = draw.textbbox((0, 0), order_now, font=now_font)[2:4]
    button_width = now_text_width + 40  
    button_height = now_text_height + 30 
    button_x = now_position[0]
    button_y = now_position[1]
    draw.rounded_rectangle(
        [(button_x, button_y), (button_x + button_width, button_y + button_height)],  
        fill="#188067",  
        outline="#188067",  
        width=3,  
        radius=10  
    )
    text_x = button_x + (button_width - now_text_width) // 2
    text_y = button_y + (button_height - now_text_height) // 2
    draw.text((text_x, text_y), order_now, fill="white", font=now_font)



    default_img = Image.open("phone1.png").convert("RGBA")  
    default_size = default_img.resize((320, 350))
    orange_bg = Image.new("RGBA", default_size.size, "#FF6E00")  
    orange_bg.paste(default_size, (0, 0), default_size)  
    default_position = (1, 0)
    background.paste(orange_bg, default_position, orange_bg)  

    right_img= Image.open("bike1.png").convert("RGBA")
    right_size=right_img.resize((300,300))
    orange_bg2=Image.new("RGBA",right_size.size, "#FF6E00")
    orange_bg2.paste(right_size,(0,0),right_size)
    right_position=(700,160)
    background.paste(orange_bg2,right_position,orange_bg2)

    #background.save("zaaroz_template.jpg","JPEG")

    hotel_name=input("Enter the Hotel or bakery Name : ")
    hotel_font=ImageFont.truetype("arialbd.ttf",60)
    image_width = background.width
    text_width = draw.textlength(hotel_name, font=hotel_font)
    hotel_position = ((image_width - text_width) // 2, 431)
    draw.text(hotel_position, hotel_name, fill="white", font=hotel_font)

    location=input("Enter the location : ")
    location_font=ImageFont.truetype("arialbd.ttf",40) 
    text_width, text_height = draw.textbbox((0, 0), location, font=location_font)[2:4]  
    x, y = 410, 930 
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
    draw.text((x, y), f"{location}", fill="#FF6E00", font=location_font) 

    offer=int(input("Enter the offer percentage : "))
    offer_font=ImageFont.truetype("arialbd.ttf",50)
    image_x, image_y = 480, 700
    image_width, image_height = 500, 250 
    text_x = image_x + (image_width // 2)  
    text_y = image_y - 60  
    text_width, text_height = draw.textbbox((0, 0), f"Get {offer}% OFF", font=offer_font)[2:4]
    text_x = text_x - (text_width // 2)  
    padding_x = 20
    padding_y = 10
    border_radius = 30  
    draw.rounded_rectangle(
        [(text_x - padding_x, text_y - padding_y),
        (text_x + text_width + padding_x, text_y + text_height + padding_y)], 
        fill="white",  
        outline="white", 
        width=3, 
        radius=border_radius  
    )
    draw.text((text_x, text_y), f"Get {offer}% OFF", fill="#188067", font=offer_font)

    offer_day=input("Enter the offer day (firstOrder/Weekend/Weekdays) : ")
    day_font=ImageFont.truetype("arial.ttf",40)
    day_text_width, day_text_height = draw.textbbox((0, 0), f"{offer_day} Only", font=day_font)[2:4]
    offset_x = 10 
    day_x = text_x + (text_width // 2) - (day_text_width // 2) + offset_x  
    day_y = text_y + text_height + 20  
    padding_x = 20
    padding_y = 10
    border_radius = 30
    draw.rounded_rectangle(
        [(day_x - padding_x, day_y - padding_y),
        (day_x + day_text_width + padding_x, day_y + day_text_height + padding_y)], 
        fill="#188067",  
        outline="#188067",  
        width=3,  
        radius=border_radius  
    )
    draw.text((day_x, day_y), f"{offer_day} Only", fill="white", font=day_font)

    hotel_type = input("Enter the hotel type (Veg/NonVeg/Bakery) : ")

    if hotel_type.lower() == "veg":
        type_img = Image.open("mus1.jpg").convert("RGBA")  
        type_size = type_img.resize((320, 300))
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
        type_position = (320, 100)
        background.paste(rounded_type_img, type_position, rounded_type_img)
    elif hotel_type.lower()=="nonveg":
        type_img2= Image.open("non_veg.jpeg")
        type_size = type_img2.resize((300, 300))
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
        type_position = (320, 100)
        background.paste(rounded_type_img, type_position, rounded_type_img)
    elif hotel_type.lower()=="bakery":
        type_img3=Image.open("bakery1.jpeg")
        type_size = type_img3.resize((300, 300))
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
        type_position = (320, 100)
        background.paste(rounded_type_img, type_position, rounded_type_img)
    else:
        print("Please Enter valid type of Restaurant!")

    input_img=int(input("How many images to you want in add the poster (Maximum 3) : "))
    if input_img==1:
        input_img1=input("Enter the image 1 : ")
        img1=Image.open(input_img1)
        img1_size=img1.resize((500,250))
        img1_position=((49,596))
        background.paste(img1_size,img1_position)

    elif input_img==2:
        img_position=[(49,596),(300,596)]
        for i in range(2):  
            input_img = input(f"Enter the image {i + 1}: ")  
            img = Image.open(input_img)  
            img_size = img.resize((250, 250))  
            background.paste(img_size, img_position[i])

    elif input_img==3:
        img_position=[(52,596),(217,596),(383,596)]
        for i in range(3):
            input_img=input(f"Enter the image {i+1} : ")
            img=Image.open(input_img)
            img_size=img.resize((166,250))
            background.paste(img_size,img_position[i])

    else:
        print("Please Enter below 3 images!")






    background.show()

green()