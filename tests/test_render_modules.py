"""Tests for module HTML rendering."""

from ai_gene_review.render_modules import (
    collect_anchor_map,
    collect_module_stats,
    evidence_url,
    output_path_for_module,
    render_all_modules,
    render_module,
)


MODULE_YAML = """id: MODULE:test
title: Test module
description: A small test module.
status: DRAFT
module:
  id: test_module
  label: Test module
  module_type: METABOLIC_PATHWAY
  concepts:
    - preferred_term: test pathway
      term:
        id: GO:0008150
        label: biological_process
  parts:
    - order: 1
      role: first step
      node:
        id: first_step
        label: First step
        module_type: REACTION
        annotons:
          - id: first_activity
            label: First activity
            participant:
              selector_type: PROTEIN_COMPLEX
              protein_complex:
                preferred_term: test complex
                active_units:
                  - id: catalytic_unit
                    label: Catalytic unit
                    participant:
                      selector_type: FAMILY
                      family:
                        preferred_term: test enzyme family
                        representative_members:
                          - preferred_term: test representative enzyme
                    role: catalytic subunit
            function:
              preferred_term: catalytic activity
              term:
                id: GO:0003824
                label: catalytic activity
  variant_sets:
    - id: route_axis
      label: Route variants
      axis: route
      selection: EXACTLY_ONE
      variants:
        - id: route_a
          label: Route A
          module_type: REACTION
        - id: route_b
          label: Route B
          module_type: REACTION
  connections:
    - source: first_activity
      target: route_a
      connection_type: PRECEDES
"""


def test_collect_module_stats():
    import yaml

    data = yaml.safe_load(MODULE_YAML)
    stats = collect_module_stats(data)

    assert stats["nodes"] == 4
    assert stats["parts"] == 1
    assert stats["variant_sets"] == 1
    assert stats["variants"] == 2
    assert stats["annotons"] == 1
    assert stats["connections"] == 1


def test_collect_anchor_map():
    import yaml

    data = yaml.safe_load(MODULE_YAML)
    anchors = collect_anchor_map(data)

    assert anchors["first_step"] == "#node-first_step"
    assert anchors["first_activity"] == "#annoton-first_activity"


def test_evidence_url_maps_doi_source_id():
    assert evidence_url({"source_id": "DOI:10.1016/j.tcb.2023.08.005"}) == (
        "https://doi.org/10.1016/j.tcb.2023.08.005"
    )


def test_output_path_for_module(tmp_path):
    modules_dir = tmp_path / "modules"
    yaml_path = modules_dir / "generic" / "test.yaml"
    output_dir = tmp_path / "pages" / "modules"

    assert output_path_for_module(yaml_path, output_dir, modules_dir) == (
        output_dir / "generic" / "test.html"
    )


def test_render_module_page(tmp_path):
    modules_dir = tmp_path / "modules"
    yaml_path = modules_dir / "generic" / "test.yaml"
    yaml_path.parent.mkdir(parents=True)
    yaml_path.write_text(MODULE_YAML)
    output_dir = tmp_path / "pages" / "modules"

    output_path, warnings = render_module(
        yaml_path,
        output_dir=output_dir,
        modules_dir=modules_dir,
    )

    assert warnings == []
    assert output_path == output_dir / "generic" / "test.html"
    assert output_path.exists()

    html = output_path.read_text()
    assert "Test module" in html
    assert "Route variants" in html
    assert "First activity" in html
    assert "data-tree-search" in html
    assert 'href="#annoton-first_activity"' in html
    assert "Active units" in html
    assert "Representative Members" in html


def test_render_all_modules_with_index(tmp_path):
    modules_dir = tmp_path / "modules"
    yaml_path = modules_dir / "generic" / "test.yaml"
    yaml_path.parent.mkdir(parents=True)
    yaml_path.write_text(MODULE_YAML)
    output_dir = tmp_path / "pages" / "modules"

    output_paths, warnings = render_all_modules(
        modules_dir=modules_dir,
        output_dir=output_dir,
    )

    assert warnings == []
    assert output_dir / "generic" / "test.html" in output_paths
    assert output_dir / "index.html" in output_paths
    assert (output_dir / "index.html").exists()
    assert "Test module" in (output_dir / "index.html").read_text()
