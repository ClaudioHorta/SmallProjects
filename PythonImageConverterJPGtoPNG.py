import sys
import os
from PIL import Image, ImageFilter

folder_name = str(sys.argv[1])
new_folder = str(sys.argv[2])

if os.path.exists(folder_name):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_name)

    # Filter out only image files (you can customize the image extensions as needed)
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    image_list = [file for file in file_list if any(file.lower().endswith(ext) for ext in image_extensions)]

    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Process each image
    for image_file in image_list:
        # Construct the full path to the image
        image_path = os.path.join(folder_name, image_file)

        # Open the image
        img = Image.open(image_path)

        # Save each image in the new folder with a .png extension
        new_path = os.path.join(new_folder, os.path.splitext(image_file)[0] + '.png')
        img.save(new_path, 'png')

    # Print the message after processing all images
    print("Conversion completed.")
else:
    print(f"The folder '{folder_name}' does not exist.")
