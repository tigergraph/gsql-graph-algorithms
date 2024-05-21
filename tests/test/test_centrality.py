import json

import pytest
import util


class TestCentrality:
    feat = util.get_featurizer()
    # undirected graphs
    graph_types1 = ["Empty", "Line", "Ring", "Hub_Spoke", "Tree"]
    # directed graphs
    graph_types2 = [
        "Line_Directed",
        "Ring_Directed",
        "Hub_Spoke_Directed",
        "Tree_Directed",
    ]
    # weighted undirected graphs
    graph_types3 = [
        "Line_Weighted",
        "Ring_Weighted",
        "Hub_Spoke_Weighted",
        "Tree_Weighted",
        "CompleteWeighted",
    ]
    # weighted directed graphs
    graph_types4 = [
        "Line_Directed_Weighted",
        "Ring_Directed_Weighted",
        "Hub_Spoke_Directed_Weighted",
        "Tree_Directed_Weighted",
        "CompleteUnweighted",
    ]

    @pytest.mark.parametrize("test_name", graph_types1)
    def test_degree_centrality1(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type_set": [test_name],
            "in_degree": True,
            "out_degree": False,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/degree_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types2)
    def test_degree_centrality2(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type_set": ["reverse_" + test_name],
            "in_degree": True,
            "out_degree": False,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/degree_centrality/in_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types2)
    def test_degree_centrality3(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type_set": ["reverse_" + test_name],
            "in_degree": False,
            "out_degree": True,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/degree_centrality/out_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types3)
    def test_weighted_degree_centrality1(self, test_name):
        params = {
            "v_type": "V20",
            "e_type": test_name,
            "reverse_e_type": test_name,
            "weight_attribute": "weight",
            "in_degree": True,
            "out_degree": False,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/weighted_degree_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_weighted_degree_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types4)
    def test_weighted_degree_centrality2(self, test_name):
        params = {
            "v_type": "V20",
            "e_type": test_name,
            "reverse_e_type": "reverse_" + test_name,
            "weight_attribute": "weight",
            "in_degree": True,
            "out_degree": False,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/weighted_degree_centrality/in_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_weighted_degree_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types4)
    def test_weighted_degree_centrality3(self, test_name):
        params = {
            "v_type": "V20",
            "e_type": test_name,
            "reverse_e_type": "reverse_" + test_name,
            "weight_attribute": "weight",
            "in_degree": False,
            "out_degree": True,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/weighted_degree_centrality/out_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_weighted_degree_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types1)
    def test_closeness_centrality(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type": [test_name],
            "max_hops": 100,
            "top_k": 100,
            "wf": True,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/closeness_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_closeness_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types2)
    def test_closeness_centrality2(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type": ["reverse_" + test_name],
            "max_hops": 100,
            "top_k": 100,
            "wf": True,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/closeness_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_closeness_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types1)
    def test_harmonic_centrality(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type_set": [test_name],
            "max_hops": 100,
            "top_k": 100,
            "wf": True,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/harmonic_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_harmonic_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types2)
    def test_harmonic_centrality2(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type_set": ["reverse_" + test_name],
            "max_hops": 100,
            "top_k": 100,
            "wf": True,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/harmonic_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_harmonic_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types1 + graph_types2)
    def test_article_rank(self, test_name):
        params = {
            "v_type": "V20",
            "e_type": test_name,
            "max_change": 0.001,
            "maximum_iteration": 25,
            "damping": 0.85,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/article_rank/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_article_rank", params=params)
        result = sorted(result[0]["@@top_scores_heap"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(
            baseline[0]["@@top_scores_heap"], key=lambda x: x["Vertex_ID"]
        )

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()

    @pytest.mark.parametrize("test_name", graph_types1 + graph_types2)
    def test_pagerank(self, test_name):
        params = {
            "v_type": "V20",
            "e_type": test_name,
            "max_change": 0.001,
            "maximum_iteration": 10,
            "damping": 0.85,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(
            f"data/baseline/graph_algorithms_baselines/centrality/pagerank/{test_name}.json"
        ) as f:
            baseline = json.load(f)
        result = self.feat.runAlgorithm("tg_pagerank", params=params)
        result = sorted(result[0]["@@top_scores_heap"], key=lambda x: x["Vertex_ID"])
        baseline = sorted(
            baseline[0]["@@top_scores_heap"], key=lambda x: x["Vertex_ID"]
        )

        for b in baseline:
            found = False
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] == r["score"]:
                    found = True
            if not found:
                pytest.fail()
