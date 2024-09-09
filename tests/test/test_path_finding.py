import json

import pytest
import util


class TestPathFinding:
    pass
    feat = util.get_featurizer()
    base_path = "data/baseline/graph_algorithms_baselines/path_finding"

    # includes unweighted directed and undirected graphs, as well as one weighted graph (Line_Weighted)
    test_graphs1 = [
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
    complete = ["Complete", "Complete_Directed"]

    @pytest.mark.parametrize("test_name", test_graphs1)
    def test_bfs1(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "max_hops": 10,
            "v_start": {"id": "A", "type": "V20"},
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": True,
        }

        with open(f"{self.base_path}/bfs/{test_name}.json") as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_bfs", params=params)

        for b in baseline[0]["Start"]:
            found = False
            for r in result[0]["Start"]:
                if (
                    b["v_id"] == r["v_id"]
                    and b["v_type"] == r["v_type"]
                    and b["attributes"]["Start.@sum_step"]
                    == r["attributes"]["Start.@sum_step"]
                ):
                    found = True
            if not found:
                pytest.fail()

        for b in baseline[1]["@@edge_set"]:
            found = False
            for r in result[1]["@@edge_set"]:
                if (
                    b["e_type"] == r["e_type"]
                    and b["from_id"] == r["from_id"]
                    and b["to_id"] == r["to_id"]
                    and b["to_type"] == r["to_type"]
                ):
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", complete)
    def test_bfs2(self, test_name):
        params = {
            "v_type_set": ["V8"],
            "e_type_set": [test_name],
            "max_hops": 10,
            "v_start": {"id": "A", "type": "V8"},
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": True,
        }
        with open(f"{self.base_path}/bfs/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_bfs", params=params)
        for b in baseline[0]["Start"]:
            found = False
            for r in result[0]["Start"]:
                if (
                    b["v_id"] == r["v_id"]
                    and b["v_type"] == r["v_type"]
                    and b["attributes"]["Start.@sum_step"]
                    == r["attributes"]["Start.@sum_step"]
                ):
                    found = True
            if not found:
                pytest.fail()

        for b in baseline[1]["@@edge_set"]:
            found = False
            for r in result[1]["@@edge_set"]:
                if (
                    b["e_type"] == r["e_type"]
                    and b["from_id"] == r["from_id"]
                    and b["to_id"] == r["to_id"]
                    and b["to_type"] == r["to_type"]
                ):
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", test_graphs1)
    def test_shortest_ss_no_wt(self, test_name):
        params = {
            "source": {"id": "A", "type": "V20"},
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "print_limit": -1,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": True,
        }
        with open(f"{self.base_path}/shortest_ss_no_wt/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_shortest_ss_no_wt", params=params)
        for b in baseline[0]["ResultSet"]:
            found = False
            for r in result[0]["ResultSet"]:
                if (
                    b["v_id"] == r["v_id"]
                    and b["v_type"] == r["v_type"]
                    and b["attributes"]["ResultSet.@min_dis"]
                    == r["attributes"]["ResultSet.@min_dis"]
                    and b["attributes"]["ResultSet.@path_list"]
                    == r["attributes"]["ResultSet.@path_list"]
                ):
                    found = True
            if not found:
                pytest.fail()

        for b in baseline[1]["@@edge_set"]:
            found = False
            for r in result[1]["@@edge_set"]:
                if (
                    b["e_type"] == r["e_type"]
                    and b["from_id"] == r["from_id"]
                    and b["from_type"] == r["from_type"]
                    and b["to_id"] == r["to_id"]
                    and b["to_type"] == r["to_type"]
                ):
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", complete)
    def test_shortest_ss_no_wt2(self, test_name):
        params = {
            "source": {"id": "A", "type": "V8"},
            "v_type_set": ["V8"],
            "e_type_set": [test_name],
            "print_limit": -1,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": True,
        }
        # url = os.path.join(self.base_url, "shortest_ss_no_wt/", test_name + ".json")
        # baseline = requests.get(url).text
        # result = json.dumps(
        #     self.feat.runAlgorithm("tg_shortest_ss_no_wt", params=params)
        # )
        # assert sorted(baseline) == sorted(result)
        with open(f"{self.base_path}/shortest_ss_no_wt/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_shortest_ss_no_wt", params=params)
        for b in baseline[0]["ResultSet"]:
            found = False
            for r in result[0]["ResultSet"]:
                if (
                    b["v_id"] == r["v_id"]
                    and b["v_type"] == r["v_type"]
                    and b["attributes"]["ResultSet.@min_dis"]
                    == r["attributes"]["ResultSet.@min_dis"]
                    and b["attributes"]["ResultSet.@path_list"]
                    == r["attributes"]["ResultSet.@path_list"]
                ):
                    found = True
            if not found:
                pytest.fail()

        for b in baseline[1]["@@edge_set"]:
            found = False
            for r in result[1]["@@edge_set"]:
                if (
                    b["e_type"] == r["e_type"]
                    and b["from_id"] == r["from_id"]
                    and b["from_type"] == r["from_type"]
                    and b["to_id"] == r["to_id"]
                    and b["to_type"] == r["to_type"]
                ):
                    found = True
            if not found:
                pytest.fail()
