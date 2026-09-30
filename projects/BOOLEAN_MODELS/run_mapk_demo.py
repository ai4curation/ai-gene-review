#!/usr/bin/env python
"""BOOLEAN_MODELS demo: translate the MAPK cascade modules to Boolean networks,
calibrate their wiring against two external sources (BBM-070 / Grieco 2013 and
SIGNOR-EGF), and compare dynamics with biodivine-aeon.

Run from the repository root (biodivine-aeon is installed ephemerally):

    uv run --with biodivine-aeon python projects/BOOLEAN_MODELS/run_mapk_demo.py

Writes:
    projects/BOOLEAN_MODELS/out/<module>.bnet          translated modules
    projects/BOOLEAN_MODELS/out/erk_cascade.sbml       SBML-qual export (via aeon)
    projects/BOOLEAN_MODELS/out/erk_cascade_pre_calibration.bnet  counterfactual (loops cut)
    projects/BOOLEAN_MODELS/RESULTS.md                 generated report

Nothing in the report is hand-written: every number is computed here.
"""

from __future__ import annotations

import sys
from collections import Counter
from importlib.metadata import version as _pkg_version
from pathlib import Path

import biodivine_aeon as ba

from ai_gene_review.module_boolean import (
    BooleanModel,
    SignedEdge,
    SignedEdgeDiff,
    diff_signed_edges,
    find_paths,
    iter_mapping_pairs,
    load_mapping,
    module_file_to_boolean,
    parse_bnet_file,
    path_sign,
    project_edges,
    signor_signed_edges,
)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "projects" / "BOOLEAN_MODELS" / "out"
REPORT = ROOT / "projects" / "BOOLEAN_MODELS" / "RESULTS.md"
MODULES = ["erk_cascade", "p38_cascade", "jnk_cascade", "jak_stat_signaling"]
BBM = ROOT / "models" / "boolean" / "bbm-070-mapk-cancer-cell-fate"
SIGNOR = ROOT / "models" / "boolean" / "signor"

# Counterfactual: the ERK module *before* its feedback loops were closed (the
# wiring the calibration originally found, PR history). Expressed as logic
# overrides on the module's own element ids; the DUSP step is additionally
# reduced to a free input by fixing it in the scenario.
PRE_CALIBRATION_LOGIC = {
    "raf_map3k": "ras_active",  # drop ERK -| RAF
    "ras_gef_step": "adaptor_recruitment",  # drop ERK output -| SOS
}


def md_table(header: list[str], rows: list[list[str]]) -> str:
    out = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join("---" for _ in header) + "|",
    ]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# 1. Translate modules
# ---------------------------------------------------------------------------


def translate() -> dict[str, BooleanModel]:
    OUT.mkdir(parents=True, exist_ok=True)
    models: dict[str, BooleanModel] = {}
    for stem in MODULES:
        bn = module_file_to_boolean(ROOT / "modules" / f"{stem}.yaml")
        (OUT / f"{stem}.bnet").write_text(bn.to_bnet() + "\n")
        models[stem] = bn
    aeon_bn = ba.BooleanNetwork.from_file(str(OUT / "erk_cascade.bnet"))
    (OUT / "erk_cascade.sbml").write_text(aeon_bn.to_sbml())
    return models


# ---------------------------------------------------------------------------
# 2. Calibration against external sources
# ---------------------------------------------------------------------------


def classify_right_only(
    edge: SignedEdge, module_edges: set[SignedEdge], module_symbols: set[str]
) -> str:
    """Explain an external-only edge in module terms."""
    hidden = module_symbols - {edge.source, edge.target}
    sign = path_sign(module_edges, edge.source, edge.target, hidden)
    if sign == edge.sign:
        return "collapsed path (module expresses it via intermediate tiers)"
    # feedback: the source is downstream of the target in the module
    down = path_sign(module_edges, edge.target, edge.source, hidden)
    if down is not None:
        return "feedback loop absent from module"
    return "cross-talk / lumping artefact"


def calibrate(
    models: dict[str, BooleanModel],
    mapping_path: Path,
    external_edges: set[SignedEdge],
    label: str,
) -> str:
    mapping = load_mapping(mapping_path)
    external_map = dict(iter_mapping_pairs(mapping["external"]))
    ext = project_edges(external_edges, external_map)
    lines = [f"### {label}", ""]
    for stem, bn in models.items():
        section = mapping.get("modules", {}).get(stem)
        if not section:
            continue
        module_map = dict(iter_mapping_pairs(section))
        cur = project_edges(bn.edges, module_map)
        module_symbols = set(module_map.values())
        # restrict the external side to symbols this module maps, so a p38 edge is not
        # reported as missing from the ERK module
        ext_edges = {
            e
            for e in ext.edges
            if e.source in module_symbols and e.target in module_symbols
        }
        diff: SignedEdgeDiff = diff_signed_edges(cur.edges, ext_edges)
        lines.append(
            f"**{stem}** — {len(cur.edges)} module edges, {len(ext_edges)} {label} edges on the "
            f"{len(module_symbols)} shared symbols: agree **{len(diff.agree)}**, sign conflicts "
            f"**{len(diff.sign_conflict)}**, module-only **{len(diff.left_only)}**, "
            f"{label}-only **{len(diff.right_only)}**."
        )
        lines.append("")
        rows: list[list[str]] = []
        for e in sorted(diff.agree, key=str):
            rows.append([f"`{e}`", "agree", ""])
        for le, re_ in sorted(diff.sign_conflict, key=lambda p: str(p[0])):
            rows.append([f"`{le}` vs `{re_}`", "sign conflict", ""])
        ext_ids_for_symbol: dict[str, set[str]] = {}
        for ext_id, sym in external_map.items():
            ext_ids_for_symbol.setdefault(sym, set()).add(ext_id)
        unmapped_ext = set(ext.unmapped_ids)
        for e in sorted(diff.left_only, key=str):
            missing = [
                sym for sym in (e.source, e.target) if not ext_ids_for_symbol.get(sym)
            ]
            if missing:
                rows.append(
                    [
                        f"`{e}`",
                        "module-only",
                        f"{', '.join(missing)} has no counterpart in {label} (see mapping notes)",
                    ]
                )
                continue
            reading = (
                f"absent from {label} (both ends mapped, no route; see mapping notes)"
            )
            # (a) the source expresses the same edge through intermediates that are not mapped
            routes = [
                (sign, interior)
                for src in sorted(ext_ids_for_symbol.get(e.source, ()))
                for tgt in sorted(ext_ids_for_symbol.get(e.target, ()))
                for sign, interior in find_paths(external_edges, src, tgt, unmapped_ext)
                if sign == e.sign
            ]
            if routes:
                reading = (
                    f"collapsed path in {label} via unmapped intermediates "
                    f"({' -> '.join(routes[0][1])})"
                )
            if not routes:
                # (c) the source routes it through *mapped* intermediates only, along a
                # route the module also wires (BBM-070: v_ERK -> v_RSK -| v_SOS, with RSK
                # mapped to ERK_OUTPUT and the module carrying ERK -> ERK_OUTPUT -| SOS)
                mapped_ext = set(external_map)
                for src in sorted(ext_ids_for_symbol.get(e.source, ())):
                    for tgt in sorted(ext_ids_for_symbol.get(e.target, ())):
                        for sign, interior in find_paths(
                            external_edges, src, tgt, mapped_ext
                        ):
                            syms = {external_map[v] for v in interior}
                            if (
                                sign == e.sign
                                and interior
                                and path_sign(cur.edges, e.source, e.target, syms)
                                == e.sign
                            ):
                                via = ", ".join(
                                    f"{external_map[v]} ({v})" for v in interior
                                )
                                reading = (
                                    f"{label} routes it via {via}, a route the module also "
                                    f"wires; the module additionally asserts this direct edge"
                                )
                                routes = [(sign, interior)]
                                break
                        if routes:
                            break
                    if routes:
                        break
            if not routes:
                # (b) the source reaches the target from a *different* mapped symbol via
                # unmapped intermediates (BBM-070 routes DUSP1 from ERK through MSK and CREB)
                other = [
                    (sym, interior)
                    for sym, ids in sorted(ext_ids_for_symbol.items())
                    if sym != e.source and sym in module_symbols
                    for src in sorted(ids)
                    for tgt in sorted(ext_ids_for_symbol.get(e.target, ()))
                    for sign, interior in find_paths(
                        external_edges, src, tgt, unmapped_ext
                    )
                    if sign == e.sign and interior
                ]
                if other:
                    sym, interior = other[0]
                    reading = (
                        f"{label} reaches {e.target} from {sym} via unmapped intermediates "
                        f"({' -> '.join(interior)})"
                    )
            rows.append([f"`{e}`", "module-only", reading])
        for e in sorted(diff.right_only, key=str):
            rows.append(
                [
                    f"`{e}`",
                    f"{label}-only",
                    classify_right_only(e, cur.edges, module_symbols),
                ]
            )
        lines.append(md_table(["edge", "status", "reading"], rows))
        lines.append("")
        # external regulators of mapped tiers that the module does not name
        partial = sorted(
            {
                e
                for e in ext.partial
                if (e.target in module_symbols) and e.source not in module_symbols
            },
            key=str,
        )
        if partial:
            lines.append(
                f"External regulators of {stem} tiers not named by the module ({len(partial)}): "
                + ", ".join(f"`{e}`" for e in partial)
            )
            lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 3. Dynamics with biodivine-aeon
# ---------------------------------------------------------------------------


def aeon_from_model(
    model: BooleanModel, scenario: dict[str, bool]
) -> ba.BooleanNetwork:
    fixed = model.with_inputs(scenario)
    return ba.BooleanNetwork.from_bnet(fixed.to_bnet()).infer_valid_graph()


def project_attractor(
    stg: ba.AsynchronousGraph, attractor: ba.ColoredVertexSet, names: list[str]
) -> dict[str, str]:
    """Per-variable value in an attractor: '1', '0', or '*' (oscillates)."""
    vs = attractor.vertices()
    out: dict[str, str] = {}
    for n in names:
        hi = not vs.intersect(stg.mk_subspace({n: True}).vertices()).is_empty()
        lo = not vs.intersect(stg.mk_subspace({n: False}).vertices()).is_empty()
        out[n] = "1" if hi and not lo else "0" if lo and not hi else "*"
    return out


def attractors_of(
    bn: ba.BooleanNetwork, names: list[str]
) -> list[tuple[str, dict[str, str]]]:
    """Attractors projected onto ``names``; identical projections are merged with a count."""
    stg = ba.AsynchronousGraph(bn)
    projected: Counter[tuple[str, tuple[tuple[str, str], ...]]] = Counter()
    for a in ba.Attractors.attractors(stg):
        kind = (
            "fixed point"
            if a.is_singleton()
            else f"complex attractor ({a.vertices().cardinality():,} states)"
        )
        projected[(kind, tuple(sorted(project_attractor(stg, a, names).items())))] += 1
    result = []
    for (kind, items), n in projected.items():
        label = kind if n == 1 else f"{n} {kind}s (identical on the shown variables)"
        result.append((label, dict(items)))
    return result


def dynamics(models: dict[str, BooleanModel]) -> str:
    lines = []
    erk = models["erk_cascade"]
    names = [
        "ras_gef_step",
        "ras_active",
        "raf_map3k",
        "mek_map2k",
        "erk_mapk",
        "erk_output",
        "mapk_negative_regulation",
    ]
    scenarios = {
        "no stimulus": {"adaptor_recruitment": False, "rasgap_step": False},
        "adaptor recruited": {"adaptor_recruitment": True, "rasgap_step": False},
        "adaptor recruited + constitutive RasGAP": {
            "adaptor_recruitment": True,
            "rasgap_step": True,
        },
        "adaptor recruited + constitutive DUSP": {
            "adaptor_recruitment": True,
            "rasgap_step": False,
            "mapk_negative_regulation": True,
        },
    }
    lines.append("### 3a. The curated ERK module as translated (feedback loops closed)")
    lines.append("")
    lines.append(
        "Inputs are the stimulus (adaptor recruitment) and the GAP tier; the DUSP step is ERK-induced, "
        "so it is a variable here and fixed only in the 'constitutive DUSP' scenario."
    )
    lines.append("")
    rows = []
    for label, scen in scenarios.items():
        for kind, proj in attractors_of(aeon_from_model(erk, scen), names):
            rows.append([label, kind] + [proj[n] for n in names])
    lines.append(md_table(["scenario", "attractor"] + names, rows))
    lines.append("")

    lines.append("### 3b. BBM-070 (Grieco 2013) under sustained EGFR stimulus")
    lines.append("")
    bbm = parse_bnet_file(BBM / "model.bnet")
    bbm_names = [
        "v_SOS",
        "v_RAS",
        "v_RAF",
        "v_MEK1_2",
        "v_ERK",
        "v_RSK",
        "v_Proliferation",
        "v_Apoptosis",
        "v_Growth_Arrest",
    ]
    bbm_scenarios = {
        "no input": {
            "v_EGFR_stimulus": False,
            "v_FGFR3_stimulus": False,
            "v_TGFBR_stimulus": False,
            "v_DNA_damage": False,
        },
        "EGFR stimulus": {
            "v_EGFR_stimulus": True,
            "v_FGFR3_stimulus": False,
            "v_TGFBR_stimulus": False,
            "v_DNA_damage": False,
        },
    }
    rows = []
    for label, scen in bbm_scenarios.items():
        for kind, proj in attractors_of(aeon_from_model(bbm, scen), bbm_names):
            rows.append([label, kind] + [proj[n] for n in bbm_names])
    lines.append(md_table(["scenario", "attractor"] + bbm_names, rows))
    lines.append("")

    lines.append("### 3c. Counterfactual: the ERK module with its feedback loops cut")
    lines.append("")
    lines.append(
        "Model file: [`out/erk_cascade_pre_calibration.bnet`](out/erk_cascade_pre_calibration.bnet)."
    )
    lines.append("")
    lines.append(
        "This is the wiring the module had before the calibration (no ERK -| RAF, no ERK output -| SOS, "
        "DUSP as a free input). Overrides applied (prototype `update_rule` values on the module's own ids):"
    )
    lines.append("")
    for var, rule in PRE_CALIBRATION_LOGIC.items():
        lines.append(f"- `{var}, {rule}`")
    lines.append(
        "- `mapk_negative_regulation` made a free input again (rule and incoming edge dropped; "
        "0, or 1 in the constitutive-DUSP scenario)"
    )
    lines.append("")
    # DUSP becomes a free input again (rule and incoming edge dropped), so the
    # committed file is exactly the model the table below simulates.
    pre = erk.with_logic(PRE_CALIBRATION_LOGIC).as_inputs("mapk_negative_regulation")
    (OUT / "erk_cascade_pre_calibration.bnet").write_text(pre.to_bnet() + "\n")
    pre_scenarios = {
        label: {
            **scen,
            "mapk_negative_regulation": scen.get("mapk_negative_regulation", False),
        }
        for label, scen in scenarios.items()
    }
    rows = []
    for label, scen in pre_scenarios.items():
        for kind, proj in attractors_of(aeon_from_model(pre, scen), names):
            rows.append([label, kind] + [proj[n] for n in names])
    lines.append(md_table(["scenario", "attractor"] + names, rows))
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def main() -> int:
    models = translate()
    bbm_edges = parse_bnet_file(BBM / "model.bnet").edges
    signor_edges = signor_signed_edges(SIGNOR / "SIGNOR-EGF.tsv")
    aeon_versions = _pkg_version("biodivine-aeon")

    parts = [
        "---",
        'title: "Boolean models — MAPK demo results"',
        "maturity: SCOPING",
        "tags: [PIPELINE]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# Boolean models — MAPK demo results",
        "",
        "Generated by [`run_mapk_demo.py`](run_mapk_demo.py); do not edit by hand. Part of",
        "[BOOLEAN_MODELS](../BOOLEAN_MODELS.md).",
        "",
        "## 1. Translation",
        "",
    ]
    rows = []
    for stem, bn in models.items():
        rows.append(
            [
                f"`modules/{stem}.yaml`",
                str(len(bn.variables)),
                str(len(bn.edges)),
                ", ".join(f"`{i}`" for i in bn.inputs),
                f"[`out/{stem}.bnet`](out/{stem}.bnet)",
            ]
        )
    parts.append(
        md_table(
            [
                "module",
                "variables",
                "signed edges",
                "inputs (no incoming edge)",
                "bnet",
            ],
            rows,
        )
    )
    parts.append("")
    parts.append(
        "The ERK translation is also exported as SBML-qual via biodivine-aeon: "
        "[`out/erk_cascade.sbml`](out/erk_cascade.sbml)."
    )
    parts.append("")
    parts.append("```")
    parts.append((OUT / "erk_cascade.bnet").read_text().strip())
    parts.append("```")
    parts.append("")
    parts.append("## 2. Calibration of wiring against external sources")
    parts.append("")
    parts.append(
        "Edges are compared on the shared symbols of the reviewed mappings "
        "(`models/boolean/*/mapping_to_modules.yaml`). `->` activates, `-|` inhibits."
    )
    parts.append("")
    parts.append(
        calibrate(models, BBM / "mapping_to_modules.yaml", bbm_edges, "BBM-070")
    )
    parts.append(
        calibrate(
            models,
            SIGNOR / "SIGNOR-EGF.mapping_to_modules.yaml",
            signor_edges,
            "SIGNOR-EGF",
        )
    )
    parts.append(
        "## 3. Dynamics (asynchronous attractors, biodivine-aeon "
        + str(aeon_versions)
        + ")"
    )
    parts.append("")
    parts.append("`1`/`0`: stable in the attractor; `*`: oscillates.")
    parts.append("")
    parts.append(dynamics(models))
    REPORT.write_text("\n".join(parts) + "\n")
    print(f"wrote {REPORT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
