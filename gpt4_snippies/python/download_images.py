import os
import json
import requests


def download_images_from_json(json_file_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load image URLs from the JSON file
    with open(json_file_path, 'r') as file:
        image_urls = json.load(file)

    # Download each image
    for idx, url in enumerate(image_urls):
        print(url)
        try:
            # Get the image data
            response = requests.get(url)
            if response.status_code == 200:
                # Determine the file name
                file_name = os.path.join(output_folder, f"image_{idx}.jpg")
                # Save the image to the output folder
                with open(file_name, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Downloaded image {idx+1}/{len(image_urls)}")
            else:
                print(
                    f"Failed to download image {idx+1}: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while downloading image {idx+1}: {e}")


if __name__ == "__main__":
    json_file_path = "imagesList.json"  # Path to the JSON file containing image URLs
    output_folder = "downloaded_images"  # Output folder to save downloaded images

    download_images_from_json(json_file_path, output_folder)
