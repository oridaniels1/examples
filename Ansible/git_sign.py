import json
import os
import sys


# Function to create ship_id JSON
def create_ship_id_json(directory, fleet_name, ship_name, mmsi):
    mmsi = int(mmsi.strip('\"'))  # Remove double quotes and convert to integer
    ship_id_data = {
        "shared": {
            "HOST_NAME": f"{fleet_name}-{ship_name}",
            "SHIP_MMSI": mmsi,
            "SHIP_NAME": f"{fleet_name.upper()}_{ship_name.upper()}",
            "FLEET_NAME": fleet_name
        },
        "communication-engine": {
            "aws_access_key_id": "manually fill",
            "aws_secret_access_key": "manually fill"
        }
    }
    file_path = os.path.join(directory, f"ship_id_{fleet_name}-{ship_name}.json")
    with open(file_path, "w") as ship_id_file:
        json.dump(ship_id_data, ship_id_file, indent=4)

# Function to create recipe JSON
def create_recipe_json(directory, fleet_name, ship_name):
    recipe_data = {
        "ingredients": [
            {"path": "prod/ingredients/versions/{version}/sw.json"},
            {"path": "prod/ingredients/LOU_cameras_layout/o3_eight_cameras.json"},
            {"path": f"prod/ingredients/LOU_calib/camera_calib_{fleet_name}-{ship_name}.json"},
            {"path": "prod/ingredients/env_alerts/env_alert_no_speed_drop_recordings.json"},
            {"path": f"prod/ingredients/ship_id/ship_id_{fleet_name}-{ship_name}.json"},
            {"path": "prod/ingredients/LOU_cameras_layout/thermal_camera_rescale.json"},
            {"path": "prod/ingredients/upload_priority/frame_priority_and_probability.json"}
        ]
    }
    file_path = os.path.join(directory, f"{fleet_name}-{ship_name}.recipe.json")
    with open(file_path, "w") as recipe_file:
        json.dump(recipe_data, recipe_file, indent=4)

# Function to create camera_calib JSON
def create_camera_calib_json(directory, fleet_name, ship_name, example_camera_calib_file):
    with open(example_camera_calib_file, "r") as example_file:
        example_camera_calib_data = example_file.read()

    file_path = os.path.join(directory, f"camera_calib_{fleet_name}-{ship_name}.json")
    with open(file_path, "w") as camera_calib_file:
        camera_calib_file.write(example_camera_calib_data)

# Check if the input file path and example camera calibration file path are provided
if len(sys.argv) < 3:
    print("Usage: python git_sign.py <input_file_path> <example_camera_calib_file>")
    sys.exit(1)

input_file = sys.argv[1]
example_camera_calib_file = sys.argv[2]
output_directory = '/home/ori/Desktop/Work/tests'  # Replace with the desired output directory

# Read input from file
with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        ship_data = line.strip().split(',')
        ship_name, mmsi, fleet_name = ship_data[0], ship_data[1].strip('\"'), ship_data[2].lower()  # Remove double quotes from mmsi
        create_ship_id_json(output_directory, fleet_name, ship_name, mmsi)
        create_recipe_json(output_directory, fleet_name, ship_name)
        create_camera_calib_json(output_directory, fleet_name, ship_name, example_camera_calib_file)
