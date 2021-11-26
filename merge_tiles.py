import multiprocessing as mp
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
    parser.add_argument("--time", type=str, help="Time Parameters")

    return parser.parse_args()


def filter_file(geojson_dir, time_params):

    """
    Here time_arr is first time parameters & time_params is the second
    time parameter (know as 6 hourly data i.e 00, 06, 12, 18)
    """

    time_arr = ["06", "09", "12", "15", "18", "21", "24", "27", "30", "33", "36"]

    for time in time_arr:
        for file in os.listdir(geojson_dir):
            if "_{}_{}_".format(time, time_params) in file and file.endswith("geojson"):
                output_dir = os.path.join(
                    geojson_dir, "{}_{}".format(time, time_params)
                )
                if not os.path.isdir(output_dir):
                    os.mkdir(output_dir)
                shutil.move(
                    os.path.join(os.path.abspath(geojson_dir), file), output_dir
                )


def geojson_to_mbtiles(geojson_dir):

    os.chdir(geojson_dir)

    # for folder in os.listdir(geojson_dir):
    #     os.chdir(os.path.join(output_dir, folder))
    #     files = os.listdir(".")
    #     print(files)

    subprocess.call(
        [
            "tippecanoe",
            "-zg",
            "-o",
            os.path.join(
                os.path.dirname(geojson_dir),
                "{}.mbtiles".format(os.path.basename(geojson_dir)),
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


def main(dir_path, time):
    filter_file(dir_path, time)
    # geojson_to_mbtiles(dir_path)

    pool = mp.Pool(mp.cpu_count())
    pool.map(
        geojson_to_mbtiles,
        [os.path.join(dir_path, folder) for folder in os.listdir(dir_path)],
    )
    # geojson_to_mbtiles(dir_path)


if __name__ == "__main__":
    args = get_args()
    main(args.dir, args.time)
