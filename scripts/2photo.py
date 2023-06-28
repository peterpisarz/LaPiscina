#THIS IS THE ONE THAT WORKS

import json
import os
import pandas as pd

with open("./settings/config.json", "r") as file:
    json_string = file.read()

config_json = json.loads(json_string)

# path to the Excel file
excel_file = './scripts/data.xlsx'

# path to the directory containing the photos
photos_dir = './build/images'
print(os.listdir(photos_dir)[0])

# path to the directory to store the JSON files
json_dir = os.path.join(os.path.dirname(photos_dir), 'jsoon')

# create the directory to store the JSON files, if it doesn't exist
if not os.path.exists(json_dir):
    os.makedirs(json_dir)

# read data from the Excel file
df = pd.read_excel(excel_file)

photo = 1

# iterate over each row in the dataframe
for i, row in df.iterrows():
    # create a JSON file with the same name as the value in the 'filename' column
    json_file = str(row['id']) + '.json'
    json_file_path = os.path.join(json_dir, json_file)

    # write data to the JSON file
    data = {
        'id': row['id'],
        'name': row['name'],
        'description': row['description'],
        'date': row['date'],
        'image': str(config_json['image_location']) + '/' + str(photo) + '.png',
        'edition': row['edition'],
        'attributes': [
            {
                'trait_type': row['trait_type_1'],
                'value': row['value_1'],
            },
            {
                'trait_type': row['trait_type_2'],
                'value': row['value_2'],
            },
        ],
    }

    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

    photo += 1