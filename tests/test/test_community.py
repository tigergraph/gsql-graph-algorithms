import json
import os

import pytest
import requests
import util


class TestCommunity:
    pass
    # feat = util.get_featurizer()
    # base_url = os.environ["TG_DATA"]
    # graph_types1 = [
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
    # graph_types2 = ["Complete", "Complete_Directed"]
    #
    # @pytest.mark.parametrize("test_name", graph_types1)
    # def test_lcc1(self, test_name):
    #     params = {
    #         "v_type": "V20",
    #         "e_type": test_name,
    #         "top_k": 100,
    #         "print_results": True,
    #         "result_attribute": "",
    #         "file_path": "",
    #         "display_edges": False,
    #     }
    #     url = os.path.join(self.base_url, "lcc", test_name + ".json")
    #     baseline = requests.get(url).text
    #     result = json.dumps(self.feat.runAlgorithm("tg_lcc", params=params))
    #     assert sorted(baseline) == sorted(result)
    #
    # @pytest.mark.parametrize("test_name", graph_types2)
    # def test_lcc2(self, test_name):
    #     params = {
    #         "v_type": "V8",
    #         "e_type": test_name,
    #         "top_k": 100,
    #         "print_results": True,
    #         "result_attribute": "",
    #         "file_path": "",
    #         "display_edges": False,
    #     }
    #     url = os.path.join(self.base_url, "lcc", test_name + ".json")
    #     baseline = requests.get(url).text
    #     result = json.dumps(self.feat.runAlgorithm("tg_lcc", params=params))
    #     assert sorted(baseline) == sorted(result)
