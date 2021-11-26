import subprocess
import argparse
import os

"""
Script to convert into mbtiles from geojson

Author: Bipin Kumar
Company: Laminaar Aviation Infotech India Pvt. Ltd.
Date: 15 Nov 2021
"""


def get_args():
    parser = argparse.ArgumentParser(
        description="Script to convert from geojson to mbtiles"
    )
    parser.add_argument("--dir", type=str, help="GeoJSON Directory")

    return parser.parse_args()


def geojson_to_mbtiles(geojson_dir):

    output_dir = os.path.join(geojson_dir, "mbtiles")
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    for file in os.listdir(geojson_dir):
        if file.endswith(".geojson"):
            output_file_name = file.split(".")[0] + ".mbtiles"

            output_file = os.path.join(output_dir, output_file_name)
            subprocess.run(
                [
                    "tippecanoe",
                    "-zg",
                    "-o",
                    output_file,
                    "--drop-densest-as-needed",
                    os.path.join(geojson_dir, file),
                    "--force",
                ]
            )
    print("ALL OUTPUTS ARE SAVED AT {}".format(output_dir))


def main(data_dir):
    geojson_to_mbtiles(data_dir)


if __name__ == "__main__":
    args = get_args()

    main(args.dir)
