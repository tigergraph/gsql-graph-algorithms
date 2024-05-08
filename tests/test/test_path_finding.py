import json
import os

import pytest
import requests
import util


class TestPathFinding:
    pass
    # feat = util.get_featurizer()
    # base_url = os.environ["TG_DATA"]
    #
    # # includes unweighted directed and undirected graphs, as well as one weighted graph (Line_Weighted)
    # test_graphs1 = [
    #     "Empty",
    #     "Empty_Directed",
    #     "Line",
    #     "Line_Directed",
    #     "Ring",
    #     "Ring_Directed",
    #     "Hub_Spoke",
    #     "Hub_Spoke_Directed",
    #     "Hub_Connected_Hub_Spoke",
    #     "Tree",
    #     "Tree_Directed",
    #     "DAG_Directed",
    #     "Line_Weighted",
    # ]
    # complete = ["Complete", "Complete_Directed"]
    #
    # @pytest.mark.parametrize("test_name", test_graphs1)
    # def test_bfs1(self, test_name):
    #     params = {
    #         "v_type_set": ["V20"],
    #         "e_type_set": [test_name],
    #         "max_hops": 10,
    #         "v_start": {"id": "A", "type": "V20"},
    #         "print_results": True,
    #         "result_attribute": "",
    #         "file_path": "",
    #         "display_edges": True,
    #     }
    #     url = os.path.join(self.base_url, "bfs/", test_name + ".json")
    #     baseline = requests.get(url).text
    #     result = json.dumps(self.feat.runAlgorithm("tg_bfs", params=params))
    #     assert sorted(baseline) == sorted(result)
    #
    # @pytest.mark.parametrize("test_name", complete)
    # def test_bfs2(self, test_name):
    #     params = {
    #         "v_type_set": ["V8"],
    #         "e_type_set": [test_name],
    #         "max_hops": 10,
    #         "v_start": {"id": "A", "type": "V8"},
    #         "print_results": True,
    #         "result_attribute": "",
    #         "file_path": "",
    #         "display_edges": True,
    #     }
    #     url = os.path.join(self.base_url, "bfs/", test_name + ".json")
    #     baseline = requests.get(url).text
    #     result = json.dumps(self.feat.runAlgorithm("tg_bfs", params=params))
    #     assert sorted(baseline) == sorted(result)
    #
    # @pytest.mark.parametrize("test_name", test_graphs1)
    # def test_shortest_ss_no_wt(self, test_name):
    #     params = {
    #         "source": {"id": "A", "type": "V20"},
    #         "v_type_set": ["V20"],
    #         "e_type_set": [test_name],
    #         "print_limit": -1,
    #         "print_results": True,
    #         "result_attribute": "",
    #         "file_path": "",
    #         "display_edges": True,
    #     }
    #     url = os.path.join(self.base_url, "shortest_ss_no_wt/", test_name + ".json")
    #     baseline = requests.get(url).text
    #     result = json.dumps(
    #         self.feat.runAlgorithm("tg_shortest_ss_no_wt", params=params)
    #     )
    #     assert sorted(baseline) == sorted(result)
    #
    # @pytest.mark.parametrize("test_name", complete)
    # def test_shortest_ss_no_wt2(self, test_name):
    #     params = {
    #         "source": {"id": "A", "type": "V8"},
    #         "v_type_set": ["V8"],
    #         "e_type_set": [test_name],
    #         "print_limit": -1,
    #         "print_results": True,
    #         "result_attribute": "",
    #         "file_path": "",
    #         "display_edges": True,
    #     }
    #     url = os.path.join(self.base_url, "shortest_ss_no_wt/", test_name + ".json")
    #     baseline = requests.get(url).text
    #     result = json.dumps(
    #         self.feat.runAlgorithm("tg_shortest_ss_no_wt", params=params)
    #     )
    #     assert sorted(baseline) == sorted(result)
