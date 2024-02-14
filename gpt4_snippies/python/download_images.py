import os
import json
import requests

HEADERS = [
    {
        "name": "Accept",
        "value": "image/avif,image/webp,*/*"
    },
    {
        "name": "Accept-Encoding",
        "value": "gzip, deflate, br"
    },
    {
        "name": "Accept-Language",
        "value": "en-US,en;q=0.5"
    },
    {
        "name": "Connection",
        "value": "keep-alive"
    },
    {
        "name": "Cookie",
        "value": "__stripe_mid=b930d8d7-9346-44b4-b787-35f2c4a8ac1f71fc55; __Secure-civitai-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Kfjl6Up7GU5161o6.CBB2wvslf0AGpmd4iCGBikYRr11KrZwhWyCQwTgaEjPUPOAGQoZTkmBc7KUeDJsbGF2FVinXDsql3cea3Icbeyom8g84dcgxVizWNgjcDrUoZ1z3gGz3cKESPi7C0oXISKi3wjCW0GzBKTSBhjVAdD8vV-7BIefsBkGRtbtz2TI75Yhix3vYZT9RVNx7vDdZhgf4HMo3sJPKT6kV68chEG21xGbMUisDF58cIfJftzczPE8BpI5wSDwBjyhMt4HQziAG6TBMqrw6o2gdc7uTTvOy3EkhJmL9VXD2WcM9JGnht96u7VI6yhcEqvTWx6SndXvMod78rsAeAMW5hiiAe4vWJZoXRrH_1NVQuAtu3gyWMA-ICyy_l0B92XTLeR6NLuuCWw-FW5p08qDg5v3K5H5DxI2822II2eZvyeUZjoU4bzY3CQN1-Xnj0UZ61RvoG-IEM6GFZRBGsyOvPEf3sFT9KOpMqH27ua_him_w7LHNc863SmnUq2bvrrZV5qs6lmxbXT4LqFNjyGurJPTL64bR0qqhCXQpT0K5u2LXkrstTd9u1ncGaTbcitFVoDPKdZ291A45sZhLIRpBQfZ__a5PKYzFPmWc27vjam2iSRkIsXoLaLb01_yV9h3VoYSVBL_aPm01eA6X8ESlCqnrx8tjqOyyma3vNMLTN9VX4Cuck6R5Tx5ln5-OnaOMEL6dJZCxEb4I-it52LyZWvDdghuq2Dbxh3HeWon8XPeF91pjML6wKY2kvrm3K0COV7-kjj6CTFPnPsTwygBpTmFM8P3MgpEKmdw4KuG0tMkIwIR-9IqW7vYzfx8gjtr4f5pXe8nMIMnrB4fF1XJtCZm3o-xt1A6MBoOGYGaasPeztYrDXJCJ-Z47LzQ0HcQ5NbIBvBdsh5T66ugJlWx1q7vCe7vdlfdsblb4qG49Klq5NceNypqUBcorwoq1yzFTlDvgGrdDYZFkZh81_UVSlWwl9TGW1wCJIacyCXISVkG_Cnu7VnsmTJTiTTlsQdnS.rignRkdrzNOTpoBhQLx-5w; __stripe_sid=50cca682-a9f0-449b-ad15-6815408d9665c242a0"
    },
    {
        "name": "DNT",
        "value": "1"
    },
    {
        "name": "Host",
        "value": "orchestration.civitai.com"
    },
    {
        "name": "Referer",
        "value": "https://civitai.com/"
    },
    {
        "name": "Sec-Fetch-Dest",
        "value": "image"
    },
    {
        "name": "Sec-Fetch-Mode",
        "value": "no-cors"
    },
    {
        "name": "Sec-Fetch-Site",
        "value": "same-site"
    },
    {
        "name": "Sec-GPC",
        "value": "1"
    },
    {
        "name": "User-Agent",
        "value": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
    }
]


def download_images_from_json(json_file_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load image URLs from the JSON file
    with open(json_file_path, 'r') as file:
        image_urls = json.load(file)

    session = requests.Session()
    for header in HEADERS:
        session.headers[header["name"]] = header["value"]

    # Download each image
    for idx, url in enumerate(image_urls):
        print(url)
        try:
            # Get the image data
            response = session.get(url)
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
    # Path to the JSON file containing image URLs
    json_file_path = "/home/robertc/Git/gpt4-snippies/gpt4_snippies/javascript/imagesList.json"
    # Output folder to save downloaded images
    output_folder = "/home/robertc/media/stable-diffusion-webui/output/civitai-downloads"

    download_images_from_json(json_file_path, output_folder)
