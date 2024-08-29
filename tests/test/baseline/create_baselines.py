from .algos import *

data_path_root = "data/"
baseline_path_root = f"{data_path_root}/baseline/"


def run():
    PagerankBaseline(data_path_root, baseline_path_root).run()
    # DegreeCentralityBaseline(data_path_root, baseline_path_root).run()
    # FastRPBaseline(data_path_root, baseline_path_root).run()


if __name__ == "__main__":
    run()
