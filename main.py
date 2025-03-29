import subprocess

hotel_name = input("Enter the hotel name: ") 
num_images=int(input("Enter the number of images do you want : ")) 


if num_images == 1:
    dish_names = [input(f"Enter dish {i+1}: ").strip().lower() for i in range(1)]
    processes = [
        subprocess.Popen(["python", "template9.py", hotel_name] + dish_names),]
    for process in processes:
        process.wait()

elif num_images == 2:
    dish_names = [input(f"Enter dish {i+1}: ").strip().lower() for i in range(2)] 
    processes = [
        subprocess.Popen(["python", "template7.py", hotel_name] + dish_names),
        subprocess.Popen(["python", "template6.py", hotel_name] + dish_names),
        subprocess.Popen(["python", "template2.py", hotel_name] + dish_names),
        subprocess.Popen(["python", "template5.py", hotel_name] + dish_names), 
        ] 
    for process in processes:
        process.wait()
    
elif num_images == 3:
    dish_names = [input(f"Enter dish {i+1}: ").strip().lower() for i in range(3)]
    processes = [
        subprocess.Popen(["python", "template8.py", hotel_name] + dish_names),
        subprocess.Popen(["python", "template4.py", hotel_name] + dish_names),
        subprocess.Popen(["python", "zaaroz.py", hotel_name] + dish_names), 
    ]
    for process in processes:
        process.wait()

else:
    print("Invalid input! Please enter 1, 2, or 3.") 