import json
import os
import time

with open("./settings/config.json", "r") as file:
    json_string = file.read()

config_json = json.loads(json_string)
print(config_json["image_location"])

# path to the directory containing the photos
photos_dir = './build/images'

# path to the directory to store the JSON files
json_dir = os.path.join(os.path.dirname(photos_dir), 'jsoon')

# create the directory to store the JSON files, if it doesn't exist
if not os.path.exists(json_dir):
    os.makedirs(json_dir)

# list all the files in the directory
for filename in os.listdir(photos_dir):
    # check if the file is a photo
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # create a JSON file with the same name and .json extension
        json_file = os.path.splitext(filename)[0] + '.json'
        json_file_path = os.path.join(json_dir, json_file)

        # get the modification time of the photo in epoch time
        photo_path = os.path.join(photos_dir, filename)
        photo_modification_time = int(os.path.getmtime(photo_path))

        # write data to the JSON file
        data = {
            'id': str(config_json['image_location']) + '/' + filename,
            'filename': filename,
            'description': 'A beautiful photo',
            'date': photo_modification_time,
            'image': 'image_url',
            'edition': 1,
            'attributes': [
                {
                    'trait_type': 'location',
                    'value': 'Mountains'
                },
                {
                    'trait_type': 'weather',
                    'value': 'Sunny'
                },
            ],
        }
        with open(json_file_path, 'w') as f:
            json.dump(data, f, indent=4)