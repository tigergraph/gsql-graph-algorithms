import json
import os

import pytest
import util


class TestCommunity:
    feat = util.get_featurizer()

    base_path = "data/baseline/graph_algorithms_baselines/community"
    graph_types1 = [
        "Empty",
        "Empty_Directed",
        "Line",
        "Line_Directed",
        "Ring",
        "Ring_Directed",
        "Hub_Spoke",
        "Hub_Spoke_Directed",
        "Hub_Connected_Hub_Spoke",
        "Tree",
        "Tree_Directed",
        "DAG_Directed",
        "Line_Weighted",
    ]
    graph_types2 = ["Complete", "Complete_Directed"]

    @pytest.mark.parametrize("test_name", graph_types1)
    def test_lcc1(self, test_name):
        params = {
            "v_type": "V20",
            "e_type": test_name,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(f"{self.base_path}/lcc/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        result = self.feat.runAlgorithm("tg_lcc", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types2)
    def test_lcc2(self, test_name):
        params = {
            "v_type": "V8",
            "e_type": test_name,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(f"{self.base_path}/lcc/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        result = self.feat.runAlgorithm("tg_lcc", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()
