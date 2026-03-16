import json

import pytest

import util


class TestCentrality:
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

    @staticmethod
    def _sorted_top_scores(payload, key="top_scores"):
        return sorted(payload[0][key], key=lambda x: x["Vertex_ID"])

    @staticmethod
    def _assert_top_scores_match(result, baseline):
        for b in baseline:
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] != pytest.approx(
                    b["score"]
                ):
                    pytest.fail(f"{r['Vertex_ID']}: {r['score']} != {b['score']}")

    @pytest.mark.parametrize("test_name", undirected_graphs)
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
        with open(f"data/baseline/centrality/degree_centrality/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", directed_graphs)
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
            f"data/baseline/centrality/degree_centrality/in_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", directed_graphs)
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
            f"data/baseline/centrality/degree_centrality/out_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", complete_graphs)
    def test_degree_centrality4(self, test_name):
        params = {
            "v_type_set": ["V8"],
            "e_type_set": [test_name],
            "reverse_e_type_set": ["reverse_" + test_name],
            "in_degree": False,
            "out_degree": True,
            "print_results": True,
        }
        with open(f"data/baseline/centrality/degree_centrality/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", weighted_undirected_graphs)
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
            f"data/baseline/centrality/weighted_degree_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_weighted_degree_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", weighted_directed_graphs)
    def test_weighted_degree_centrality2(self, test_name):
        vt = "V20" if "Complete" not in test_name else "V8"
        params = {
            "v_type": vt,
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
            f"data/baseline/centrality/weighted_degree_centrality/in_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_weighted_degree_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", weighted_directed_graphs)
    def test_weighted_degree_centrality3(self, test_name):
        vt = "V20" if "Complete" not in test_name else "V8"
        params = {
            "v_type": vt,
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
            f"data/baseline/centrality/weighted_degree_centrality/out_degree/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_weighted_degree_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", undirected_graphs)
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
            f"data/baseline/centrality/closeness_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_closeness_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", directed_graphs)
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
            f"data/baseline/centrality/closeness_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_closeness_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", undirected_graphs)
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
            f"data/baseline/centrality/harmonic_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_harmonic_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", directed_graphs)
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
            f"data/baseline/centrality/harmonic_centrality/{test_name}.json"
        ) as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_harmonic_cent", params=params)
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", undirected_graphs + directed_graphs)
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
        with open(f"data/baseline/centrality/article_rank/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_article_rank", params=params)
        result = self._sorted_top_scores(result, key="@@top_scores_heap")
        baseline = self._sorted_top_scores(baseline, key="@@top_scores_heap")

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", undirected_graphs + directed_graphs)
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
        with open(f"data/baseline/centrality/pagerank/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.runAlgorithm("tg_pagerank", params=params)
        result = self._sorted_top_scores(result, key="@@top_scores_heap")
        baseline = self._sorted_top_scores(baseline, key="@@top_scores_heap")

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", undirected_graphs)
    def test_betweenness_centrality1(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type": [test_name],
            "max_hops": 100,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(f"data/baseline/centrality/betweenness/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.conn.runInstalledQuery(
            "brandes_betweenness",
            params=params,
        )
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)

    @pytest.mark.parametrize("test_name", directed_graphs)
    def test_betweenness_centrality2(self, test_name):
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type": ["reverse_" + test_name],
            "max_hops": 100,
            "top_k": 1000,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
            "display_edges": False,
        }
        with open(f"data/baseline/centrality/betweenness/{test_name}.json") as f:
            baseline = json.load(f)

        result = self.feat.conn.runInstalledQuery(
            "brandes_betweenness",
            params=params,
        )
        result = self._sorted_top_scores(result)
        baseline = self._sorted_top_scores(baseline)

        self._assert_top_scores_match(result, baseline)
