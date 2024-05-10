import json

import pytest
import util


class TestTopologicalLinkPrediction:
    feat = util.get_featurizer()
    base_path = "data/baseline/graph_algorithms_baselines/topological_link_prediction"
    testdata = [
        "topo_link1",
        "topo_link2",
        "topo_link3",
        "topo_link4",
        "topo_link5",
        "topo_link6",
        "topo_link_directed",
    ]
    testdata_sc = [
        ("A", "B", "community_int", "INT", "test1"),
        ("A", "C", "community_int", "INT", "test2"),
        ("A", "B", "community_string", "STRING", "test3"),
        ("A", "C", "community_string", "STRING", "test4"),
    ]

    @pytest.mark.parametrize("test_name", testdata)
    def test_adamic_adar(self, test_name):
        params = {
            "v_source": {"id": "A", "type": "V8"},
            "v_target": {"id": "B", "type": "V8"},
            "e_type_set": [test_name],
            "print_results": True,
        }
        with open(f"{self.base_path}/adamic_adar/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = baseline[0]["@@sum_closeness"]

        result = self.feat.runAlgorithm("tg_adamic_adar", params=params)
        result = result[0]["@@sum_closeness"]
        assert result == baseline

    @pytest.mark.parametrize("test_name", testdata)
    def test_common_neighbors(self, test_name):
        params = {
            "v_source": {"id": "A", "type": "V8"},
            "v_target": {"id": "B", "type": "V8"},
            "e_type_set": [test_name],
            "print_results": True,
        }

        with open(f"{self.base_path}/common_neighbors/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = baseline[0]["closeness"]

        result = self.feat.runAlgorithm("tg_common_neighbors", params=params)
        result = result[0]["closeness"]
        assert result == baseline

    @pytest.mark.parametrize("test_name", testdata)
    def test_preferential_attachment(self, test_name):
        params = {
            "v_source": {"id": "A", "type": "V8"},
            "v_target": {"id": "B", "type": "V8"},
            "e_type_set": [test_name],
            "print_results": True,
        }

        with open(f"{self.base_path}/preferential_attachment/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = baseline[0]["closeness"]

        result = self.feat.runAlgorithm("tg_preferential_attachment", params=params)
        result = result[0]["closeness"]
        assert result == baseline

    @pytest.mark.parametrize("test_name", testdata)
    def test_resource_allocation(self, test_name):
        params = {
            "v_source": {"id": "A", "type": "V8"},
            "v_target": {"id": "B", "type": "V8"},
            "e_type_set": [test_name],
            "print_results": True,
        }

        with open(f"{self.base_path}/resource_allocation/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = baseline[0]["@@sum_closeness"]

        result = self.feat.runAlgorithm("tg_resource_allocation", params=params)
        result = result[0]["@@sum_closeness"]
        assert result == baseline

    @pytest.mark.parametrize("test_name", testdata)
    def test_total_neighbors(self, test_name):
        params = {
            "v_source": {"id": "A", "type": "V8"},
            "v_target": {"id": "B", "type": "V8"},
            "e_type_set": [test_name],
            "print_results": True,
        }

        with open(f"{self.base_path}/total_neighbors/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = baseline[0]["closeness"]

        result = self.feat.runAlgorithm("tg_total_neighbors", params=params)
        result = result[0]["closeness"]
        assert result == baseline

    @pytest.mark.parametrize("source, target, attr, attr_type, test_name", testdata_sc)
    def test_same_community(self, source, target, attr, attr_type, test_name):
        params = {
            "v_source": {"id": source, "type": "V4"},
            "v_target": {"id": target, "type": "V4"},
            "community_attribute": attr,
            "community_attr_type": attr_type,
            "print_results": True,
        }
        # result = json.dumps(self.feat.runAlgorithm("tg_same_community", params=params))
        # url = os.path.join(self.base_url, "same_community/", test_name + ".json")
        # baseline = requests.get(url).text
        # assert sorted(baseline) == sorted(result)

        with open(f"{self.base_path}/same_community/{test_name}.json") as f:
            baseline = json.dumps(json.load(f))

        result = self.feat.runAlgorithm("tg_same_community", params=params)
        result = json.dumps(result)
        assert result == baseline
