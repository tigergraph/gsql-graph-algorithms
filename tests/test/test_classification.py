import json

import pytest

import util


class TestClassification:
    feat = util.get_featurizer()
    undirected_graphs = [
        "Empty",
        "Line",
        "Ring",
        "Hub_Spoke",
        "Tree",
    ]
    directed_graphs = [
        "Line_Directed",
        "Ring_Directed",
        "Hub_Spoke_Directed",
        "Tree_Directed",
    ]
    weighted_undirected_graphs = [
        "Line_Weighted",
        "Ring_Weighted",
        "Hub_Spoke_Weighted",
        "Tree_Weighted",
    ]
    weighted_directed_graphs = [
        "Line_Directed_Weighted",
        "Ring_Directed_Weighted",
        "Hub_Spoke_Directed_Weighted",
        "Tree_Directed_Weighted",
        "Complete_Directed_Weighted",
    ]
    complete_graphs = [
        "Complete",
    ]

    @pytest.mark.parametrize("test_name", undirected_graphs)
    def test_graph_coloring(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "max_colors": 999999,
            "print_color_count": False,
            "print_stats": True,
            "file_path": ""
        }
        
        with open(f"data/baseline/classification/graph_coloring/{test_name}.json") as f:
            baseline_data = json.load(f)

        response = self.feat.runAlgorithm("tg_greedy_graph_coloring", params=params)
        
        # Sort both by v_id to ensure a 1:1 comparison
        result = sorted(response[0]["start"], key=lambda x: x["v_id"])
        baseline = sorted(baseline_data[0]["start"], key=lambda x: x["v_id"])

        # 1. Check if the number of vertices matches
        assert len(result) == len(baseline), f"Vertex count mismatch for {test_name}"

        # 2. Compare values directly using zip (O(n) complexity)
        for r, b in zip(result, baseline):
            v_id = r["v_id"]
            res_color = r["attributes"]["start.@sum_color_vertex"]
            base_color = b["attributes"]["start.@sum_color_vertex"]
            
            assert v_id == b["v_id"], f"ID mismatch at index: {v_id} vs {b['v_id']}"
            assert res_color == base_color, f"Color mismatch for vertex {v_id}: Expected {base_color}, got {res_color}"

   