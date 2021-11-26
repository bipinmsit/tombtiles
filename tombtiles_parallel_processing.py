import multiprocessing as mp
import subprocess
import argparse
import os

"""
Script to convert into mbtiles from geojson - parallel processing

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


def geojson_to_mbtiles(input_geojson):

    output_dir = os.path.join(os.path.dirname(input_geojson), "mbtiles")
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    output_file_name = os.path.basename(input_geojson).split(".")[0] + ".mbtiles"
    output_file = os.path.join(output_dir, output_file_name)

    subprocess.run(
        [
            "tippecanoe",
            "-zg",
            "-o",
            output_file,
            "--drop-densest-as-needed",
            input_geojson,
            "--force",
        ]
    )

    return output_dir


def main(data_dir):
    pool = mp.Pool(mp.cpu_count())
    pool.map(
        geojson_to_mbtiles,
        [
            os.path.join(data_dir, file)
            for file in os.listdir(data_dir)
            if file.endswith("geojson")
        ],
    )


if __name__ == "__main__":
    args = get_args()

    main(args.dir)
