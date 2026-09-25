"""Family function compliance uses curated scope, never representative count."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.module_family_conformance import module_family_function_findings


FAMILY = "PANTHER:PTHR11022"
CATALYTIC = f"{FAMILY}:SF66"
RECEPTOR = f"{FAMILY}:SF41"
AMIDASE = "GO:0008745"
HYDROLASE = "GO:0016787"
BINDING = "GO:0042834"


def _module(family: str | None = FAMILY, function: str | None = AMIDASE) -> dict:
    """Create a minimal family annoton using known PGRP identifiers."""
    descriptor: dict[str, str | dict[str, str]] = {"preferred_term": "PGRP family"}
    if family:
        descriptor["term"] = {"id": family}
    activity: dict[str, str | dict[str, str]] = {"preferred_term": "amidase activity"}
    if function:
        activity["term"] = {"id": function}
    return {
        "module": {
            "annotons": [
                {
                    "id": "hydrolysis",
                    "participant": {"selector_type": "FAMILY", "family": descriptor},
                    "function": activity,
                }
            ]
        }
    }


def _review(tmp_path: Path, scope: str, *, term: str = AMIDASE, **extra) -> Path:
    """Write a real review fixture to the documented PANTHER sidecar location."""
    path = tmp_path / "PTHR11022" / "PTHR11022-review.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    document = {
        "family_id": FAMILY,
        "functional_coherence": "HETEROGENEOUS",
        "review_status": "DRAFT",
        "term_assessments": [
            {
                "assessed_term": {"id": term},
                "scope": scope,
                "scope_reason": "Curated functional assessment.",
                **extra,
            }
        ],
    }
    path.write_text(yaml.safe_dump(document))
    return path


@pytest.mark.parametrize(
    "scope,family,status,severity",
    [
        ("FAMILY_WIDE", FAMILY, "FAMILY_SUPPORTED", "info"),
        ("FAMILY_WIDE", CATALYTIC, "FAMILY_SUPPORTED", "info"),
        ("SUBFAMILY_ONLY", CATALYTIC, "FAMILY_SUPPORTED", "info"),
        ("SUBFAMILY_ONLY", RECEPTOR, "FAMILY_CONFLICT", "error"),
        ("SUBFAMILY_ONLY", FAMILY, "FAMILY_SCOPE_RESTRICTED", "warning"),
        ("RESIDUE_DETERMINED", CATALYTIC, "FAMILY_SCOPE_RESTRICTED", "warning"),
        ("NOT_APPLICABLE", FAMILY, "FAMILY_CONFLICT", "error"),
        ("UNRESOLVED", FAMILY, "FAMILY_FUNCTION_UNREVIEWED", "warning"),
    ],
)
def test_panther_scope_is_checked(tmp_path, scope, family, status, severity):
    path = _review(
        tmp_path,
        scope,
        applicable_subfamilies=[{"id": CATALYTIC}],
        determined_by_site="zn_triad",
    )
    rows = module_family_function_findings(_module(family), family_reviews_dir=tmp_path)
    assert len(rows) == 1
    assert rows[0]["status"] == status
    assert rows[0]["severity"] == severity
    assert rows[0]["scope"] == "family"
    assert rows[0]["participant_id"] == family
    assert rows[0]["function_id"] == AMIDASE
    assert rows[0]["review_path"] == str(path)


@pytest.mark.parametrize(
    "family,function,status",
    [
        (FAMILY, AMIDASE, "FAMILY_REVIEW_MISSING"),
        (None, AMIDASE, "FAMILY_ID_MISSING"),
        (FAMILY, None, "NO_FUNCTION_ID"),
        ("InterPro:IPR000573", AMIDASE, "FAMILY_REVIEW_MISSING"),
    ],
)
def test_missing_grounding_or_review_is_reported(tmp_path, family, function, status):
    rows = module_family_function_findings(
        _module(family, function), family_reviews_dir=tmp_path
    )
    assert rows[0]["status"] == status
    assert rows[0]["severity"] == "warning"


def test_missing_function_assessment_does_not_inherit_reference_member(tmp_path):
    path = _review(tmp_path, "FAMILY_WIDE", term=BINDING)
    data = _module()
    data["module"]["annotons"][0]["participant"]["family"]["representative_members"] = [
        {"term": {"id": "UniProtKB:Q96PD5"}, "preferred_term": "PGLYRP2"}
    ]
    row = module_family_function_findings(data, family_reviews_dir=tmp_path)[0]
    assert row["status"] == "FAMILY_FUNCTION_UNREVIEWED"
    assert row["review_path"] == str(path)


def _subclass_of(child: str, parent: str) -> bool:
    """The known amidase -> hydrolase subsumption used in these fixtures."""
    return child == parent or (child, parent) == (AMIDASE, HYDROLASE)


@pytest.mark.parametrize(
    "scope,reviewed,requested,status",
    [
        ("FAMILY_WIDE", AMIDASE, HYDROLASE, "FAMILY_SUPPORTED"),
        ("FAMILY_WIDE", HYDROLASE, AMIDASE, "FAMILY_FUNCTION_UNREVIEWED"),
        ("NOT_APPLICABLE", HYDROLASE, AMIDASE, "FAMILY_CONFLICT"),
        ("NOT_APPLICABLE", AMIDASE, HYDROLASE, "FAMILY_FUNCTION_UNREVIEWED"),
    ],
)
def test_go_matching_respects_subsumption_direction(
    tmp_path, scope, reviewed, requested, status
):
    _review(tmp_path, scope, term=reviewed)
    row = module_family_function_findings(
        _module(function=requested),
        family_reviews_dir=tmp_path,
        subclass_of=_subclass_of,
    )[0]
    assert row["status"] == status


def test_conflict_is_visible_even_with_positive_assessment(tmp_path):
    path = _review(tmp_path, "FAMILY_WIDE")
    review = yaml.safe_load(path.read_text())
    review["term_assessments"].append(
        {
            "assessed_term": {"id": AMIDASE},
            "scope": "NOT_APPLICABLE",
        }
    )
    path.write_text(yaml.safe_dump(review))
    rows = module_family_function_findings(_module(), family_reviews_dir=tmp_path)
    assert any(row["status"] == "FAMILY_CONFLICT" for row in rows)


def test_multiple_family_terms_are_separately_checked_and_deduplicated(tmp_path):
    _review(tmp_path, "FAMILY_WIDE")
    data = _module()
    family = data["module"]["annotons"][0]["participant"]["family"]
    family["family_terms"] = [{"id": FAMILY}, {"id": "Pfam:PF02431"}]
    rows = module_family_function_findings(
        data,
        family_reviews_dir=tmp_path,
        pfam_reviews_dir=tmp_path / "pfam",
    )
    assert [(row["participant_id"], row["status"]) for row in rows] == [
        (FAMILY, "FAMILY_SUPPORTED"),
        ("Pfam:PF02431", "FAMILY_REVIEW_MISSING"),
    ]


def test_active_unit_uses_own_function_and_nested_variants_are_visited(tmp_path):
    _review(tmp_path, "FAMILY_WIDE")
    unit = _module()["module"]["annotons"][0]
    unit["id"] = "catalytic_unit"
    unannotated_unit = {"id": "other_unit", "participant": unit["participant"]}
    data = {
        "module": {
            "parts": [
                {
                    "node": {
                        "variant_sets": [
                            {
                                "variants": [
                                    {
                                        "annotons": [
                                            {
                                                "id": "complex_activity",
                                                "participant": {
                                                    "protein_complex": {
                                                        "active_units": [
                                                            unit,
                                                            unannotated_unit,
                                                        ]
                                                    }
                                                },
                                                "function": {"term": {"id": BINDING}},
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                    }
                }
            ]
        }
    }
    rows = module_family_function_findings(data, family_reviews_dir=tmp_path)
    assert [(row["annoton_id"], row["function_id"], row["status"]) for row in rows] == [
        ("catalytic_unit", AMIDASE, "FAMILY_SUPPORTED"),
    ]


@pytest.mark.parametrize(
    "explicit,required,expected",
    [
        (None, AMIDASE, [("hydrolysis", AMIDASE, "FAMILY_SUPPORTED")]),
        (AMIDASE, AMIDASE, [("hydrolysis", AMIDASE, "FAMILY_SUPPORTED")]),
        (
            AMIDASE,
            BINDING,
            [
                ("hydrolysis", AMIDASE, "FAMILY_SUPPORTED"),
                ("hydrolysis:required_function", BINDING, "FAMILY_FUNCTION_UNREVIEWED"),
            ],
        ),
    ],
)
def test_participant_required_function_is_checked_and_deduplicated(
    tmp_path,
    explicit,
    required,
    expected,
):
    """A selector's function constraint is an assertion requiring family review."""
    _review(tmp_path, "FAMILY_WIDE")
    data = _module(function=explicit)
    annoton = data["module"]["annotons"][0]
    if explicit is None:
        del annoton["function"]
    annoton["participant"]["required_function"] = {
        "preferred_term": "Required family function",
        "term": {"id": required},
    }
    rows = module_family_function_findings(data, family_reviews_dir=tmp_path)
    assert [
        (row["annoton_id"], row["function_id"], row["status"]) for row in rows
    ] == expected


def test_active_unit_required_function_does_not_inherit_complex_function(tmp_path):
    _review(tmp_path, "FAMILY_WIDE")
    unit = _module()["module"]["annotons"][0]
    unit["id"] = "catalytic_unit"
    unit["participant"]["required_function"] = unit.pop("function")
    data = {
        "module": {
            "annotons": [
                {
                    "id": "complex_activity",
                    "function": {"term": {"id": BINDING}},
                    "participant": {"protein_complex": {"active_units": [unit]}},
                }
            ]
        }
    }
    rows = module_family_function_findings(data, family_reviews_dir=tmp_path)
    assert [(row["annoton_id"], row["function_id"], row["status"]) for row in rows] == [
        ("catalytic_unit", AMIDASE, "FAMILY_SUPPORTED"),
    ]


def test_wrong_sidecar_identity_is_not_support(tmp_path):
    path = _review(tmp_path, "FAMILY_WIDE")
    document = yaml.safe_load(path.read_text())
    document["family_id"] = "PANTHER:PTHR10256"
    path.write_text(yaml.safe_dump(document))
    row = module_family_function_findings(_module(), family_reviews_dir=tmp_path)[0]
    assert row["status"] == "FAMILY_REVIEW_ID_MISMATCH"
    assert row["severity"] == "error"


@pytest.mark.parametrize(
    "status,expected",
    [
        ("ACCEPTED", "FAMILY_SUPPORTED"),
        ("PROPOSED", "FAMILY_FUNCTION_PROPOSED"),
        ("REJECTED", "FAMILY_SCOPE_RESTRICTED"),
    ],
)
def test_pfam_curator_status_is_preserved(tmp_path, status, expected):
    path = tmp_path / "PF02431" / "PF02431-review.yaml"
    path.parent.mkdir()
    path.write_text(
        yaml.safe_dump(
            {
                "pfam_id": "PF02431",
                "proposed_annotations": [
                    {
                        "term": {"id": AMIDASE},
                        "status": status,
                        "relation": {"id": "RO:0002327", "label": "enables"},
                        "aspect": "molecular_function",
                        "rationale": "Member review.",
                    }
                ],
            }
        )
    )
    row = module_family_function_findings(
        _module("Pfam:PF02431"),
        family_reviews_dir=tmp_path / "panther",
        pfam_reviews_dir=tmp_path,
    )[0]
    assert row["status"] == expected
    assert row["severity"] == ("info" if status == "ACCEPTED" else "warning")


@pytest.mark.parametrize(
    "relation,expected,message_fragment",
    [
        ({"id": "RO:0002327", "label": "enables"}, "FAMILY_SUPPORTED", "ACCEPTED"),
        (
            {"id": "RO:0002326", "label": "contributes to"},
            "FAMILY_SCOPE_RESTRICTED",
            "contributes",
        ),
        (
            {"id": "RO:0002331", "label": "involved in"},
            "FAMILY_SCOPE_RESTRICTED",
            "RO:0002331",
        ),
        ({"label": "enables"}, "FAMILY_SCOPE_RESTRICTED", "missing"),
        (None, "FAMILY_SCOPE_RESTRICTED", "missing"),
    ],
)
def test_pfam_support_requires_an_explicit_enables_relation(
    tmp_path,
    relation,
    expected,
    message_fragment,
):
    """Contributes-to and ungrounded relations cannot establish independent activity."""
    path = tmp_path / "PF02431" / "PF02431-review.yaml"
    path.parent.mkdir()
    annotation = {
        "term": {"id": AMIDASE},
        "status": "ACCEPTED",
        "aspect": "molecular_function",
        "rationale": "Curated relation assessment.",
    }
    if relation is not None:
        annotation["relation"] = relation
    path.write_text(
        yaml.safe_dump(
            {
                "pfam_id": "PF02431",
                "proposed_annotations": [annotation],
            }
        )
    )
    row = module_family_function_findings(
        _module("Pfam:PF02431"),
        pfam_reviews_dir=tmp_path,
    )[0]
    assert row["status"] == expected
    assert row["severity"] == ("info" if expected == "FAMILY_SUPPORTED" else "warning")
    assert message_fragment in row["message"]


def test_real_pgrp_review_distinguishes_catalytic_and_receptor_subfamilies():
    rows = [
        module_family_function_findings(_module(family))[0]
        for family in (FAMILY, CATALYTIC, RECEPTOR)
    ]
    assert [row["status"] for row in rows] == [
        "FAMILY_SCOPE_RESTRICTED",
        "FAMILY_SUPPORTED",
        "FAMILY_CONFLICT",
    ]


def test_functionless_family_annoton_is_not_a_function_gap(tmp_path):
    doc = _module()
    del doc["module"]["annotons"][0]["function"]
    assert module_family_function_findings(doc, family_reviews_dir=tmp_path) == []
    doc["module"]["annotons"][0]["function"] = {"preferred_term": "unmapped activity"}
    assert (
        module_family_function_findings(doc, family_reviews_dir=tmp_path)[0]["status"]
        == "NO_FUNCTION_ID"
    )
