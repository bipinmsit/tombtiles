import multiprocessing as mp
from os.path import dirname as up
import argparse
import subprocess
import shutil
import os

'''
"""
Script to merge tiles and convert into mbtiles - parallel processing
Author: Bipin Kumar
Company: Laminaar Aviation Infotech India Pvt. Ltd.
Date: 15 Nov 2021
"""
'''


def get_args():
    parser = argparse.ArgumentParser(description="Merging mbtiles")
    parser.add_argument("--dir", type=str, help="GeoJSON Directory")

    return parser.parse_args()


def geojson_to_mbtiles(geojson_dir):

    os.chdir(geojson_dir)

    output_dir = os.path.join(up(up(geojson_dir)), "output")
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    subprocess.call(
        [
            "tippecanoe",
            "-zg",
            "-o",
            os.path.join(
                output_dir, "{}.mbtiles".format(os.path.basename(geojson_dir)),
            ),
            "--drop-densest-as-needed",
            "--force",
            os.listdir(".")[0],
            os.listdir(".")[1],
            os.listdir(".")[2],
            os.listdir(".")[3],
            os.listdir(".")[4],
            os.listdir(".")[5],
            os.listdir(".")[6],
            os.listdir(".")[7],
            os.listdir(".")[8],
            os.listdir(".")[9],
            os.listdir(".")[10],
            os.listdir(".")[11],
            os.listdir(".")[12],
            os.listdir(".")[13],
            os.listdir(".")[14],
            os.listdir(".")[15],
        ]
    )


def main(dir_path):

    input_dir = os.path.abspath(dir_path)
    pool = mp.Pool(mp.cpu_count())
    pool.map(
        geojson_to_mbtiles,
        [os.path.join(input_dir, folder) for folder in os.listdir(input_dir)],
    )


if __name__ == "__main__":
    args = get_args()
    main(args.dir)
