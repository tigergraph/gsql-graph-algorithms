import gzip
import json

import numpy as np
import pytest
from dotenv import load_dotenv

from util import get_featurizer

load_dotenv()
data_path_root = "data"
baseline_path_root = f"{data_path_root}/baseline"
graph_name = "CoraV2"


def cos_sim(x, y):
    x_mag = np.linalg.norm(x)
    y_mag = np.linalg.norm(y)

    return np.dot(x, y) / (x_mag * y_mag)


class TestML:
    feat = get_featurizer(graph_name)

    @pytest.mark.skip(reason="Relies on udf that comes with DB, but was overridden. Must make new testing db")
    def test_fastRP(self):
        params = {
            "v_type_set": ["Paper"],
            "e_type_set": ["Cite", "reverse_Cite"],
            "output_v_type_set": ["Paper"],
            "iteration_weights": "1,2,4",
            "beta": -0.1,
            "embedding_dimension": 8,
            "embedding_dim_map": [],
            "default_length": 8,
            "sampling_constant": 3,
            "random_seed": 42,
            "print_results": True,
        }

        with gzip.open(f"{baseline_path_root}/ml/fastRP.json.gz", "rb") as f:
            baseline = json.load(f)

        self.feat.installAlgorithm(
            "tg_fastRP", "../algorithms/GraphML/Embeddings/FastRP/tg_fastRP.gsql"
        )
        result = self.feat.runAlgorithm(
            "tg_fastRP",
            params=params,
        )
        result = {
            v["v_id"]: v["attributes"]["res.@final_embedding_list"]
            for v in result[1]["res"]
        }
        threshold = 0.5
        for bk, bv in baseline.items():
            v = result[bk]
            sim = abs(cos_sim(v, bv))
            if sim < threshold:
                pytest.fail(f"cos-sim of ID: {bk} is {sim} (< threshold of {threshold}")
