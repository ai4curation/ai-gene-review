"""Tests for the GO-CAM ETL (fetch/cache/index)."""

import json
from pathlib import Path

import pytest

from ai_gene_review.etl.gocam import (
    INDEX_COLUMNS,
    GoCamActivityRow,
    build_gene_index,
    cache_gocam_model,
    iter_activity_rows,
    list_production_models,
    load_cached_model,
    minerva_json_to_model,
    model_to_yaml,
    normalize_gocam_id,
    src_path,
)

FIXTURE = Path(__file__).parent / "input" / "gocam" / "568b0f9600000284.json"


@pytest.fixture
def minerva_raw() -> dict:
    """Low-level Minerva JSON for a real production model (offline fixture)."""
    return json.loads(FIXTURE.read_text())


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("gomodel:568b0f9600000284", "568b0f9600000284"),
        ("http://model.geneontology.org/568b0f9600000284", "568b0f9600000284"),
        ("568b0f9600000284", "568b0f9600000284"),
        ("GO_CAM:gomodel:568b0f9600000284", "568b0f9600000284"),
        ("  568b0f9600000284  ", "568b0f9600000284"),
    ],
)
def test_normalize_gocam_id(raw, expected):
    assert normalize_gocam_id(raw) == expected


def test_src_path_layout():
    assert (
        src_path("gomodel:568b0f9600000284", cache_dir=Path("gocams")).as_posix()
        == "gocams/568b0f9600000284/568b0f9600000284-src.yaml"
    )


def test_minerva_json_to_model(minerva_raw):
    model = minerva_json_to_model(minerva_raw)
    assert model.id == "gomodel:568b0f9600000284"
    assert model.activities
    # taxon is carried through from the model annotations
    assert model.taxon == "NCBITaxon:6239"


def test_iter_activity_rows(minerva_raw):
    model = minerva_json_to_model(minerva_raw)
    rows = list(iter_activity_rows(model))
    assert rows, "expected at least one annoton"
    assert all(isinstance(r, GoCamActivityRow) for r in rows)
    assert all(r.model_id == "568b0f9600000284" for r in rows)
    # Every annoton must have an enabling gene product and a molecular function.
    assert all(r.gene_product for r in rows)
    assert all(r.molecular_function for r in rows)
    # The tir-1 signaling-adaptor annoton is present with its labels resolved.
    tir1 = [r for r in rows if r.gene_product == "WB:WBGene00006575"]
    assert tir1, "expected the tir-1 annoton"
    assert tir1[0].molecular_function == "GO:0035591"
    assert tir1[0].mf_label == "signaling adaptor activity"
    assert tir1[0].biological_process == "GO:0140367"


def test_model_to_yaml_roundtrips(minerva_raw, tmp_path):
    model = minerva_json_to_model(minerva_raw)
    text = model_to_yaml(model)
    assert "id: gomodel:568b0f9600000284" in text
    # Writing through cache_gocam_model and reloading yields an equivalent model.
    out = src_path(model.id, cache_dir=tmp_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    reloaded = load_cached_model(model.id, cache_dir=tmp_path)
    assert reloaded is not None
    assert reloaded.id == model.id
    assert len(reloaded.activities) == len(model.activities)


def test_build_gene_index(minerva_raw, tmp_path):
    model = minerva_json_to_model(minerva_raw)
    out = src_path(model.id, cache_dir=tmp_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(model_to_yaml(model))

    index = build_gene_index(cache_dir=tmp_path)
    assert index.exists()
    lines = index.read_text().strip().splitlines()
    header = lines[0].split("\t")
    assert header == INDEX_COLUMNS
    assert len(lines) - 1 == len(model.activities)
    # tir-1 gene product appears in the index body.
    assert any(line.startswith("WB:WBGene00006575\t") for line in lines[1:])


def test_load_cached_model_absent(tmp_path):
    assert load_cached_model("gomodel:doesnotexist", cache_dir=tmp_path) is None


# --- integration (network) ---------------------------------------------------


@pytest.mark.integration
@pytest.mark.vcr_skip  # the production index is ~660KB; don't commit it as a cassette
def test_list_production_models_integration():
    models = list_production_models()
    # The production set is ~2k models; assert it is in a sane range.
    assert 1500 < len(models) < 5000
    assert all(m["id"] for m in models)


@pytest.mark.integration
def test_cache_and_index_one_model_integration(tmp_path):
    # Fetch a single known production model directly (no large index download).
    out = cache_gocam_model("568b0f9600000284", cache_dir=tmp_path)
    assert out.exists()
    assert out == src_path("568b0f9600000284", cache_dir=tmp_path)

    index = build_gene_index(cache_dir=tmp_path)
    assert index.exists()
    assert len(index.read_text().strip().splitlines()) >= 2

    # Re-caching without force is a no-op (file already present).
    mtime = out.stat().st_mtime
    cache_gocam_model("568b0f9600000284", cache_dir=tmp_path)
    assert out.stat().st_mtime == mtime
