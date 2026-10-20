from pathlib import Path
import importlib.util

import yaml


SCRIPT = (
    Path(__file__).parents[1] / "projects" / "REACTOME" / "ingest_reactome_pathways.py"
)
spec = importlib.util.spec_from_file_location("ingest_reactome_pathways", SCRIPT)
assert spec and spec.loader
ingest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ingest)


def test_write_yaml_disables_aliases(tmp_path: Path) -> None:
    shared = {"id": "R-HSA-1"}
    path = tmp_path / "import.yaml"

    ingest.write_yaml(path, {"events": {"a": shared, "b": shared}})

    text = path.read_text()
    assert "&id" not in text
    assert "*id" not in text
    assert yaml.safe_load(text) == {
        "events": {"a": {"id": "R-HSA-1"}, "b": {"id": "R-HSA-1"}}
    }


def test_align_module_separates_reactome_and_module_only_events() -> None:
    imported = {
        "events": {
            "R-HSA-1": {
                "schema_class": "Reaction",
                "catalysts": [
                    {
                        "activity": {"id": "GO:1"},
                        "physical_entity": {"members": ["UniProtKB:P1"]},
                    }
                ],
            },
            "R-HSA-2": {
                "schema_class": "Reaction",
                "catalysts": [
                    {
                        "activity": {"id": "GO:3"},
                        "physical_entity": {"members": ["UniProtKB:P3"]},
                    }
                ],
            },
            "R-HSA-4": {
                "schema_class": "BlackBoxEvent",
                "catalysts": [],
            },
            "R-HSA-ROOT": {
                "schema_class": "Pathway",
            },
        }
    }
    module_sources = [
        {
            "scope": "activity_evidence",
            "reactome_id": "R-HSA-1",
            "node_id": "step1",
            "annoton_id": "activity1",
            "function_id": "GO:1",
            "participant_ids": ["UniProtKB:P1"],
        },
        {
            "scope": "activity_evidence",
            "reactome_id": "R-HSA-3",
            "node_id": "step3",
            "annoton_id": "activity3",
            "function_id": "GO:3",
            "participant_ids": ["UniProtKB:P3"],
        },
        {
            "scope": "module_evidence",
            "reactome_id": "R-HSA-ROOT",
        },
    ]

    alignment = ingest.align_module(
        {
            "module": "example",
            "reactome_root": "R-HSA-ROOT",
            "scope": "curated_slice",
        },
        imported,
        module_sources,
    )

    assert alignment == {
        "module": "example",
        "reactome_root": "R-HSA-ROOT",
        "scope": "curated_slice",
        "matches": [
            {
                "module_node": "step1",
                "module_annoton": "activity1",
                "reactome_event": "R-HSA-1",
                "verdict": "reaction_id_exact",
                "match_basis": [
                    "cited_reactome_id",
                    "executor_match",
                    "mf_match",
                ],
            }
        ],
        "container_evidence": ["R-HSA-ROOT"],
        "reactome_only_events": [
            {
                "reactome_event": "R-HSA-2",
                "verdict": "same_executor_different_reaction",
                "candidate_module_activities": ["step3/activity3"],
            },
            {
                "reactome_event": "R-HSA-4",
                "verdict": "black_box_event",
                "candidate_module_activities": [],
            },
        ],
        "module_only_events": [
            {
                "module_node": "step3",
                "module_annoton": "activity3",
                "reactome_event": "R-HSA-3",
                "verdict": "same_executor_different_reaction",
                "candidate_reactome_events": ["R-HSA-2"],
            }
        ],
    }


def test_align_module_flags_same_reaction_missing_executor() -> None:
    imported = {
        "events": {
            "R-HSA-1": {
                "schema_class": "Reaction",
                "catalysts": [
                    {
                        "activity": {"id": "GO:1"},
                        "physical_entity": {"members": ["UniProtKB:P1"]},
                    }
                ],
            }
        }
    }
    module_sources = [
        {
            "scope": "activity_evidence",
            "reactome_id": "R-HSA-1",
            "node_id": "step1",
            "annoton_id": "activity1",
            "function_id": "GO:1",
            "participant_ids": ["UniProtKB:P2"],
        }
    ]

    alignment = ingest.align_module(
        {
            "module": "example",
            "reactome_root": "R-HSA-ROOT",
            "scope": "curated_slice",
        },
        imported,
        module_sources,
    )

    assert alignment["matches"] == [
        {
            "module_node": "step1",
            "module_annoton": "activity1",
            "reactome_event": "R-HSA-1",
            "verdict": "same_reaction_missing_executor",
            "match_basis": ["cited_reactome_id", "mf_match"],
        }
    ]


def test_select_pathways_filters_by_id() -> None:
    config = {
        "pathways": [
            {"id": "urea_cycle"},
            {"id": "gpi_anchor_core_glycan_assembly"},
            {"id": "glycosphingolipid_lysosomal_degradation"},
        ]
    }

    selected = ingest.select_pathways(
        config,
        {
            "gpi_anchor_core_glycan_assembly",
            "glycosphingolipid_lysosomal_degradation",
        },
    )

    assert [pathway["id"] for pathway in selected] == [
        "gpi_anchor_core_glycan_assembly",
        "glycosphingolipid_lysosomal_degradation",
    ]


def test_select_pathways_rejects_unknown_id() -> None:
    config = {"pathways": [{"id": "urea_cycle"}]}

    try:
        ingest.select_pathways(config, {"not_a_slice"})
    except ValueError as e:
        assert str(e) == "Unknown pathway id(s): not_a_slice"
    else:
        raise AssertionError("expected an unknown pathway id to fail")
