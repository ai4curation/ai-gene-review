from pathlib import Path
import importlib.util

import pytest
import yaml


SCRIPT = Path(__file__).parents[1] / "projects" / "REACTOME" / "inventory_reactome.py"
spec = importlib.util.spec_from_file_location("inventory_reactome", SCRIPT)
assert spec and spec.loader
inventory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inventory)


def test_repeated_mf_resolutions_require_unique_reactome_ids(
    tmp_path: Path,
) -> None:
    path = tmp_path / "repeated_mf_resolutions.yaml"
    rows = [
        {
            "reactome_id": "R-HSA-1",
            "resolution_status": "resolved",
            "resolution_bucket": "reactome_family_overbroad",
            "resolution_summary": "first",
            "resolution_follow_up": "first",
        },
        {
            "reactome_id": "R-HSA-1",
            "resolution_status": "resolved",
            "resolution_bucket": "reactome_family_overbroad",
            "resolution_summary": "second",
            "resolution_follow_up": "second",
        },
    ]
    path.write_text(yaml.safe_dump(rows))

    with pytest.raises(ValueError, match="duplicate repeated MF resolution: R-HSA-1"):
        inventory.load_repeated_mf_resolutions(path)


def test_summarize_repeated_mf_events_attaches_resolution() -> None:
    rows = [
        {
            "reactome_id": "R-HSA-1",
            "gene": "GENE1",
            "organism": "human",
            "candidate_bucket": "accepted_mf",
            "candidate_verdict": "reaction_mf_exact",
            "reactome_display_name": "shared event",
            "reactome_title": "",
            "reactome_species": "Homo sapiens",
            "term_id": "GO:1",
            "term_label": "first activity",
            "review_action": "ACCEPT",
            "candidate_flags": "multi_gene_reactome_id",
        },
        {
            "reactome_id": "R-HSA-1",
            "gene": "GENE2",
            "organism": "human",
            "candidate_bucket": "activity_contradicted",
            "candidate_verdict": "activity_contradicted",
            "reactome_display_name": "shared event",
            "reactome_title": "",
            "reactome_species": "Homo sapiens",
            "term_id": "GO:1",
            "term_label": "first activity",
            "review_action": "REMOVE",
            "candidate_flags": "manual_verdict|multi_gene_reactome_id",
        },
    ]

    repeated = inventory.summarize_repeated_mf_events(
        rows,
        {
            "R-HSA-1": {
                "resolution_status": "resolved",
                "resolution_bucket": "reactome_family_overbroad",
                "resolution_summary": "Drop GENE2 from the family set.",
                "resolution_follow_up": "Ask Reactome to update the family set.",
            }
        },
    )

    assert set(inventory.REPEATED_MF_RESOLUTION_FIELDS[1:]).isdisjoint(
        inventory.REPEATED_MF_EVENT_FIELDS
    )
    assert inventory.select_fields(repeated, inventory.REPEATED_MF_EVENT_FIELDS) == [
        {
            "reactome_id": "R-HSA-1",
            "reactome_display_name": "shared event",
            "reactome_species": "Homo sapiens",
            "row_count": "2",
            "gene_count": "2",
            "organisms": "human",
            "genes": "GENE1|GENE2",
            "actions": "ACCEPT:1|REMOVE:1",
            "candidate_verdicts": "activity_contradicted:1|reaction_mf_exact:1",
            "candidate_buckets": "accepted_mf:1|activity_contradicted:1",
            "terms": "GO:1 first activity",
            "audit_bucket": "mixed_manual_failure",
            "audit_priority": "HIGH",
            "has_mixed_actions": "true",
            "has_mixed_verdicts": "true",
            "has_manual_failure": "true",
            "has_local_module_mf": "false",
            "row_details": "human/GENE1:ACCEPT/reaction_mf_exact|human/GENE2:REMOVE/activity_contradicted",
        }
    ]
    assert repeated == [
        {
            "reactome_id": "R-HSA-1",
            "reactome_display_name": "shared event",
            "reactome_species": "Homo sapiens",
            "row_count": "2",
            "gene_count": "2",
            "organisms": "human",
            "genes": "GENE1|GENE2",
            "actions": "ACCEPT:1|REMOVE:1",
            "candidate_verdicts": "activity_contradicted:1|reaction_mf_exact:1",
            "candidate_buckets": "accepted_mf:1|activity_contradicted:1",
            "terms": "GO:1 first activity",
            "audit_bucket": "mixed_manual_failure",
            "audit_priority": "HIGH",
            "has_mixed_actions": "true",
            "has_mixed_verdicts": "true",
            "has_manual_failure": "true",
            "has_local_module_mf": "false",
            "resolution_status": "resolved",
            "resolution_bucket": "reactome_family_overbroad",
            "resolution_summary": "Drop GENE2 from the family set.",
            "resolution_follow_up": "Ask Reactome to update the family set.",
            "row_details": "human/GENE1:ACCEPT/reaction_mf_exact|human/GENE2:REMOVE/activity_contradicted",
        }
    ]
