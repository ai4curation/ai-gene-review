#!/usr/bin/env python3
"""Reproducible ChatGEM + COBRApy curation audit on BiGG GEMs (iMM904 / iML1515).

Cross-checks genome-scale metabolic models (GEMs) against curated gene reviews
in `genes/<species>/` and metabolic pathway modules in `modules/`.

Usage:
    # Default: S. cerevisiae iMM904 vs genes/yeast/
    uv run --no-project --with cobra --with pyyaml python \
        projects/YEAST_METABOLIC_ENGINEERING/run_yeast_gem_audit.py

    # Second organism test: E. coli iML1515 vs genes/ECOLI/
    uv run --no-project --with cobra --with pyyaml python \
        projects/YEAST_METABOLIC_ENGINEERING/run_yeast_gem_audit.py \
        --model-id iML1515 --genes-dir genes/ECOLI --out-dir /tmp/ecoli_gem_out
"""

from __future__ import annotations

import argparse
import ast
import gzip
import re
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any

import cobra
from cobra.flux_analysis import pfba
import yaml


class NoAliasDumper(yaml.SafeDumper):
    """YAML SafeDumper that never emits anchor/alias references."""

    def ignore_aliases(self, data: Any) -> bool:
        return True


# Core 10 target genes in YEAST_METABOLIC_ENGINEERING.md + 6 key paralogs
TARGET_GENES = [
    "PDC1",
    "ADH1",
    "ADH2",
    "GPD1",
    "GPD2",
    "HXK1",
    "HXK2",
    "GLK1",
    "PFK1",
    "PFK2",
    "PYC1",
    "PYC2",
    "TDH1",
    "TDH2",
    "TDH3",
    "ZWF1",
]

CURATED_MODULES = [
    "alcoholic_fermentation.yaml",
    "glycerol_metabolism.yaml",
    "emp_glycolysis.yaml",
    "pentose_phosphate_pathway.yaml",
    "pyruvate_metabolism.yaml",
]


def load_bigg_model(model_id: str, model_path: Path | None = None) -> cobra.Model:
    """Load a BiGG model from a local .json/.json.gz path, /tmp cache, or BiGG HTTPS."""
    target = model_path or Path(f"/tmp/{model_id}.json.gz")
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://bigg.ucsd.edu/static/models/{model_id}.json.gz"
        req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            target.write_bytes(resp.read())
    if str(target).endswith(".gz"):
        with gzip.open(target, "rt", encoding="utf-8") as fh:
            return cobra.io.from_json(fh.read())
    return cobra.io.load_json_model(str(target))


def parse_uniprot_metadata(uniprot_path: Path) -> dict[str, Any]:
    """Extract OrderedLocusNames and EC numbers from a cached UniProt flat file."""
    loci: list[str] = []
    ec_numbers: set[str] = set()
    if not uniprot_path.exists():
        return {"loci": loci, "ec_numbers": []}
    with uniprot_path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("GN   "):
                for part in line.split(";"):
                    if "OrderedLocusNames=" in part:
                        raw = part.split("OrderedLocusNames=")[1].split("{")[0].strip()
                        loci.extend(x.strip() for x in raw.split(",") if x.strip())
            if "EC=" in line:
                for match in re.findall(
                    r"EC=([0-9]+\.[0-9\-]+\.[0-9\-]+\.[0-9\-]+)", line
                ):
                    ec_numbers.add(match)
    return {"loci": loci, "ec_numbers": sorted(ec_numbers)}


def classify_gpr_ast(reaction: cobra.Reaction) -> str:
    """Classify a COBRApy reaction GPR using its AST rather than string splitting."""
    body = reaction.gpr.body
    if body is None:
        return "NO_GPR"
    if isinstance(body, ast.Name):
        return "SINGLE_GENE"

    has_and = False
    has_or = False
    for node in ast.walk(body):
        if isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.And):
                has_and = True
            elif isinstance(node.op, ast.Or):
                has_or = True
    if has_and and has_or:
        return "MIXED_AND_OR"
    if has_and:
        return "COMPLEX_AND"
    if has_or:
        return "ISOZYME_OR"
    return "SINGLE_GENE"


def eval_gpr_ast_eflux(
    node: ast.AST | None,
    expr_map: dict[str, float],
    default_missing: float = 1.0,
) -> float:
    """Evaluate effective reaction capacity from a GPR AST node (And=min, Or=sum)."""
    if node is None:
        return default_missing
    if isinstance(node, ast.Expression):
        return eval_gpr_ast_eflux(node.body, expr_map, default_missing)
    if isinstance(node, ast.Name):
        return float(expr_map.get(node.id, default_missing))
    if isinstance(node, ast.BoolOp):
        vals = [eval_gpr_ast_eflux(v, expr_map, default_missing) for v in node.values]
        if isinstance(node.op, ast.And):
            return min(vals)
        if isinstance(node.op, ast.Or):
            return sum(vals)
    raise ValueError(f"Unsupported GPR AST node: {ast.dump(node)}")


def chatgem_buggy_eflux_parser(gpr_str: str, expr_map: dict[str, float]) -> float:
    """Reproduce the regex/stack GPR evaluation bug in ChatGEM 46._automatic_E_flux.py."""
    if not gpr_str.strip():
        return 1.0
    tokens = [t.strip() for t in re.split(r"\(|\)", gpr_str) if t.strip()]
    stack: list[float] = []
    for token in tokens:
        if "and" in token and "or" not in token:
            genes = [g.strip() for g in token.split("and") if g.strip()]
            vals = [expr_map.get(g, 0.0) for g in genes]
            if vals:
                stack.append(min(vals))
        elif "or" in token and "and" not in token:
            genes = [g.strip() for g in token.split("or") if g.strip()]
            vals = [expr_map.get(g, 0.0) for g in genes]
            if vals:
                stack.append(sum(vals))
        else:
            if token in expr_map:
                stack.append(expr_map[token])
    return max(stack) if stack else 0.0


def audit_proteome_alignment(
    model: cobra.Model, genes_dir: Path
) -> dict[str, Any]:
    """Compare all reviewed genes in `genes_dir` against `model`."""
    gene_folders = sorted(
        p.name for p in genes_dir.iterdir() if p.is_dir() and not p.name.startswith(".")
    )
    category_counts: Counter[str] = Counter()
    class_changes: list[dict[str, Any]] = []
    aligned_count = 0

    for symbol in gene_folders:
        rev_path = genes_dir / symbol / f"{symbol}-ai-review.yaml"
        uni_path = genes_dir / symbol / f"{symbol}-uniprot.txt"
        if not rev_path.exists() or not uni_path.exists():
            continue

        uni_meta = parse_uniprot_metadata(uni_path)
        matched_loci = [loc for loc in uni_meta["loci"] if loc in model.genes]
        if not matched_loci:
            continue

        aligned_count += 1
        locus = matched_loci[0]
        model_gene = model.genes.get_by_id(locus)

        with rev_path.open(encoding="utf-8") as fh:
            rev_doc = yaml.safe_load(fh) or {}

        gem_ecs: set[str] = set()
        gpr_classes: set[str] = set()
        rxn_summaries: list[dict[str, Any]] = []
        for rxn in sorted(model_gene.reactions, key=lambda r: r.id):
            gpr_cls = classify_gpr_ast(rxn)
            gpr_classes.add(gpr_cls)
            ecs = rxn.annotation.get("ec-code", [])
            if isinstance(ecs, str):
                ecs = [ecs]
            gem_ecs.update(ecs)
            rxn_summaries.append(
                {
                    "id": rxn.id,
                    "name": rxn.name,
                    "reaction": rxn.reaction,
                    "gpr": rxn.gene_reaction_rule,
                    "gpr_class": gpr_cls,
                    "ec": sorted(ecs),
                    "compartments": sorted(rxn.compartments),
                }
            )

        uni_ecs = set(uni_meta["ec_numbers"])
        has_complex_and = bool(gpr_classes & {"COMPLEX_AND", "MIXED_AND_OR"})

        if not gem_ecs and uni_ecs:
            category = "MODEL_MISSING_EC"
        elif gem_ecs and not uni_ecs:
            category = "UNIPROT_MISSING_EC"
        elif not gem_ecs and not uni_ecs:
            category = "BOTH_NO_EC"
        elif gem_ecs == uni_ecs:
            category = "EXACT_MATCH"
        else:
            gem_top = {e.split(".")[0] for e in gem_ecs if e and e[0].isdigit()}
            uni_top = {e.split(".")[0] for e in uni_ecs if e and e[0].isdigit()}
            if gem_top == uni_top:
                category = "SAME_CLASS_EC_DIFF"
            elif "7" in uni_top and ("3" in gem_top or "1" in gem_top):
                category = "EC7_TRANSLOCASE_RECLASS"
            elif has_complex_and and uni_ecs.issubset(gem_ecs):
                category = "COMPLEX_SUBUNIT_EC_PROPAGATION"
            else:
                category = "CLASS_CHANGE"

        category_counts[category] += 1

        if category == "CLASS_CHANGE":
            core_mfs: list[str] = []
            for cf in rev_doc.get("core_functions", []) or []:
                mf = cf.get("molecular_function") or cf.get(
                    "contributes_to_molecular_function"
                )
                if isinstance(mf, dict) and mf.get("label"):
                    core_mfs.append(str(mf["label"]))

            removed_terms: list[dict[str, str]] = []
            for ann in rev_doc.get("existing_annotations", []) or []:
                review_block = ann.get("review") or {}
                if review_block.get("action") == "REMOVE":
                    term = ann.get("term") or {}
                    label = str(term.get("label", ""))
                    if label == "protein binding":
                        continue
                    removed_terms.append(
                        {
                            "id": str(term.get("id", "")),
                            "label": label,
                            "reason": str(
                                review_block.get("reason")
                                or review_block.get("summary")
                                or ""
                            ),
                        }
                    )

            class_changes.append(
                {
                    "gene_symbol": symbol,
                    "locus_tag": locus,
                    "review_status": str(rev_doc.get("status", "UNKNOWN")),
                    "gem_ec": sorted(gem_ecs),
                    "uniprot_ec": sorted(uni_ecs),
                    "has_complex_and": has_complex_and,
                    "core_molecular_functions": core_mfs,
                    "non_binding_removed_terms_count": len(removed_terms),
                    "removed_terms": removed_terms[:4],
                    "reactions": [
                        {
                            "id": r["id"],
                            "name": r["name"],
                            "ec": r["ec"],
                            "gpr": r["gpr"],
                        }
                        for r in rxn_summaries[:5]
                    ],
                }
            )

    return {
        "model_id": model.id,
        "genes_dir": str(genes_dir),
        "total_review_folders": len(gene_folders),
        "total_model_genes": len(model.genes),
        "aligned_reviewed_genes": aligned_count,
        "category_counts": dict(category_counts.most_common()),
        "class_change_count": len(class_changes),
        "class_changes": class_changes,
    }


def audit_target_cohort_and_modules(
    model: cobra.Model, genes_dir: Path, modules_dir: Path
) -> dict[str, Any]:
    """Audit the 16 central-carbon target/paralog genes and 5 curated modules."""
    module_gene_map: dict[str, list[str]] = {}
    for mod_file in CURATED_MODULES:
        mod_path = modules_dir / mod_file
        if not mod_path.exists():
            continue
        text = mod_path.read_text(encoding="utf-8")
        for sym in TARGET_GENES:
            if re.search(rf"\b{re.escape(sym)}\b", text):
                module_gene_map.setdefault(sym, []).append(mod_file.replace(".yaml", ""))

    cohort_rows: list[dict[str, Any]] = []
    for sym in TARGET_GENES:
        rev_path = genes_dir / sym / f"{sym}-ai-review.yaml"
        uni_path = genes_dir / sym / f"{sym}-uniprot.txt"
        uni_meta = parse_uniprot_metadata(uni_path)
        loci = [loc for loc in uni_meta["loci"] if loc in model.genes]
        locus = loci[0] if loci else (uni_meta["loci"][0] if uni_meta["loci"] else "")

        with rev_path.open(encoding="utf-8") as fh:
            rev = yaml.safe_load(fh) or {}

        core_mfs: list[str] = []
        core_locs: list[str] = []
        core_complexes: list[str] = []
        for cf in rev.get("core_functions", []) or []:
            mf = cf.get("molecular_function") or cf.get(
                "contributes_to_molecular_function"
            )
            if isinstance(mf, dict) and mf.get("label"):
                core_mfs.append(f"{mf.get('id')} ({mf.get('label')})")
            for loc in cf.get("locations", []) or []:
                if isinstance(loc, dict) and loc.get("label"):
                    core_locs.append(f"{loc.get('id')} ({loc.get('label')})")
            ic = cf.get("in_complex")
            if isinstance(ic, dict) and ic.get("label"):
                core_complexes.append(f"{ic.get('id')} ({ic.get('label')})")

        action_counts = Counter(
            (a.get("review") or {}).get("action", "NONE")
            for a in (rev.get("existing_annotations") or [])
        )

        mg = model.genes.get_by_id(locus)
        rxns = []
        gem_comps: set[str] = set()
        gem_ecs: set[str] = set()
        for r in sorted(mg.reactions, key=lambda x: x.id):
            gem_comps.update(r.compartments)
            ecs = r.annotation.get("ec-code", [])
            if isinstance(ecs, str):
                ecs = [ecs]
            gem_ecs.update(ecs)
            rxns.append(
                {
                    "id": r.id,
                    "name": r.name,
                    "reaction": r.reaction,
                    "gpr": r.gene_reaction_rule,
                    "gpr_class": classify_gpr_ast(r),
                    "ec": sorted(ecs),
                    "compartments": sorted(r.compartments),
                }
            )

        cohort_rows.append(
            {
                "gene_symbol": sym,
                "uniprot_id": rev.get("id"),
                "locus_tag": locus,
                "review_status": rev.get("status"),
                "action_counts": dict(action_counts),
                "curated_modules": sorted(set(module_gene_map.get(sym, []))),
                "curated_core_mf": core_mfs,
                "curated_locations": sorted(set(core_locs)),
                "curated_complex": sorted(set(core_complexes)),
                "uniprot_ec": uni_meta["ec_numbers"],
                "gem_ec": sorted(gem_ecs),
                "gem_compartments": sorted(gem_comps),
                "gem_reactions": rxns,
            }
        )

    return {"target_genes_count": len(cohort_rows), "target_genes": cohort_rows}


def configure_anaerobic_glucose_medium(model: cobra.Model) -> None:
    """Configure standard anaerobic glucose fermentation medium with sterol/FA supplements."""
    model.reactions.EX_glc__D_e.lower_bound = -10.0
    model.reactions.EX_o2_e.lower_bound = 0.0
    for ex_id in [
        "EX_ergst_e",
        "EX_zymst_e",
        "EX_hdcea_e",
        "EX_ocdca_e",
        "EX_ocdcea_e",
        "EX_ocdcya_e",
    ]:
        if ex_id in model.reactions:
            model.reactions.get_by_id(ex_id).lower_bound = -0.05


def audit_fba_vs_pfba_routing(model: cobra.Model) -> dict[str, Any]:
    """Compare standard FBA vs pFBA and quantify central-carbon routing artifacts."""
    key_rxns = [
        "HEX1",
        "GLUK",
        "PGI",
        "G6PI",
        "G6PI3",
        "PFK",
        "FBA",
        "PFK_3",
        "FBA3",
        "TALA",
        "TKT1",
        "TKT2",
        "G6PDH2r",
        "GND",
        "GAPD",
        "PGK",
        "PGM",
        "ENO",
        "PYK",
        "PYRDC",
        "ALCD2ir",
        "G3PD1ir",
        "G3PD1irm",
        "G3PDm",
        "G3PT",
        "GLYCDy",
        "DHAK",
        "EX_etoh_e",
        "EX_glyc_e",
        "EX_succ_e",
        "EX_co2_e",
    ]

    results: dict[str, Any] = {}
    for condition in ["aerobic_glucose", "anaerobic_glucose"]:
        with model:
            if condition == "anaerobic_glucose":
                configure_anaerobic_glucose_medium(model)
            fba_sol = model.optimize()
            pfba_sol = pfba(model)

            with model:
                model.reactions.PFK_3.bounds = (0.0, 0.0)
                fba_no_s17bp = model.optimize()
                pfba_no_s17bp = pfba(model)

                rxn_comparison: dict[str, dict[str, float]] = {}
                for rid in key_rxns:
                    if rid in model.reactions:
                        rxn_comparison[rid] = {
                            "standard_fba": round(float(fba_sol.fluxes[rid]), 4),
                            "pfba": round(float(pfba_sol.fluxes[rid]), 4),
                            "fba_after_closing_PFK_3": round(
                                float(fba_no_s17bp.fluxes[rid]), 4
                            ),
                            "pfba_after_closing_PFK_3": round(
                                float(pfba_no_s17bp.fluxes[rid]), 4
                            ),
                        }

                results[condition] = {
                    "growth_rate_standard_fba": round(
                        float(fba_sol.objective_value), 4
                    ),
                    "growth_rate_pfba": round(
                        float(pfba_sol.fluxes["BIOMASS_SC5_notrace"]), 4
                    ),
                    "growth_rate_after_closing_PFK_3": round(
                        float(fba_no_s17bp.objective_value), 4
                    ),
                    "total_abs_flux_standard_fba": round(
                        float(fba_sol.fluxes.abs().sum()), 2
                    ),
                    "total_abs_flux_pfba": round(
                        float(pfba_sol.fluxes.abs().sum()), 2
                    ),
                    "reactions": rxn_comparison,
                }
    return results


def run_knockout_and_repair_experiments(model: cobra.Model) -> dict[str, Any]:
    """Run single/double paralog knockouts before and after curation-guided repairs."""
    single_ko_results: list[dict[str, Any]] = []
    for sym in TARGET_GENES:
        matched = [g for g in model.genes if g.name == sym]
        if not matched:
            continue
        gene = matched[0]
        with model:
            wt_aero = model.optimize()
            gene.knock_out()
            ko_aero = model.optimize()
        with model:
            configure_anaerobic_glucose_medium(model)
            wt_anaero = model.optimize()
            gene.knock_out()
            ko_anaero = model.optimize()

        single_ko_results.append(
            {
                "gene_symbol": sym,
                "locus_tag": gene.id,
                "aerobic_wt_growth": round(float(wt_aero.objective_value), 4),
                "aerobic_ko_growth": round(float(ko_aero.objective_value), 4),
                "aerobic_growth_pct": round(
                    100.0
                    * float(ko_aero.objective_value)
                    / float(wt_aero.objective_value),
                    1,
                ),
                "aerobic_ko_etoh_flux": round(float(ko_aero.fluxes["EX_etoh_e"]), 4),
                "anaerobic_wt_growth": round(float(wt_anaero.objective_value), 4),
                "anaerobic_ko_growth": round(float(ko_anaero.objective_value), 4),
                "anaerobic_growth_pct": round(
                    100.0
                    * float(ko_anaero.objective_value)
                    / float(wt_anaero.objective_value),
                    1,
                ),
                "anaerobic_ko_etoh_flux": round(
                    float(ko_anaero.fluxes["EX_etoh_e"]), 4
                ),
            }
        )

    # Repair Experiment A: GPD1 (YDL022W) & GPD2 (YOL059W) anaerobic glycerol synthesis
    gpd_experiment: dict[str, Any] = {}
    with model:
        configure_anaerobic_glucose_medium(model)
        wt_fba = model.optimize()
        wt_pfba = pfba(model)
        gpd_experiment["unmodified_anaerobic_wt"] = {
            "growth": round(float(wt_fba.objective_value), 4),
            "standard_fba_G3PD1ir_flux": round(float(wt_fba.fluxes["G3PD1ir"]), 4),
            "standard_fba_G3PT_flux": round(float(wt_fba.fluxes["G3PT"]), 4),
            "standard_fba_GLYCDy_catabolic_loop": round(
                float(wt_fba.fluxes["GLYCDy"]), 4
            ),
            "standard_fba_DHAK_catabolic_loop": round(float(wt_fba.fluxes["DHAK"]), 4),
            "pfba_G3PD1ir_flux": round(float(wt_pfba.fluxes["G3PD1ir"]), 4),
            "G3PD1irm_flux": round(float(wt_pfba.fluxes["G3PD1irm"]), 4),
            "EX_glyc_e_secretion": round(float(wt_pfba.fluxes["EX_glyc_e"]), 4),
            "EX_etoh_e_secretion": round(float(wt_pfba.fluxes["EX_etoh_e"]), 4),
            "EX_succ_e_secretion": round(float(wt_pfba.fluxes["EX_succ_e"]), 4),
        }

        for rxn_id in ["GLYCDy", "G3PDm", "FRDcm", "FRDm", "GLUSx", "THRA"]:
            if rxn_id in model.reactions:
                model.reactions.get_by_id(rxn_id).bounds = (0.0, 0.0)

        orig_gpr_outcomes = {}
        for label, ko_ids in [
            ("WT", []),
            ("gpd1_KO", ["YDL022W"]),
            ("gpd2_KO", ["YOL059W"]),
            ("gpd1_gpd2_double_KO", ["YDL022W", "YOL059W"]),
        ]:
            with model:
                for gid in ko_ids:
                    model.genes.get_by_id(gid).knock_out()
                sol = pfba(model)
                orig_gpr_outcomes[label] = {
                    "growth": round(float(sol.fluxes["BIOMASS_SC5_notrace"]), 4),
                    "G3PD1ir_flux": round(float(sol.fluxes["G3PD1ir"]), 4),
                    "G3PT_flux": round(float(sol.fluxes["G3PT"]), 4),
                    "EX_glyc_e_flux": round(float(sol.fluxes["EX_glyc_e"]), 4),
                    "EX_etoh_e_flux": round(float(sol.fluxes["EX_etoh_e"]), 4),
                }
        gpd_experiment["original_gpr_after_loop_closure"] = orig_gpr_outcomes

        model.reactions.G3PD1ir.gene_reaction_rule = "YDL022W or YOL059W"
        repaired_gpr_outcomes = {}
        for label, ko_ids in [
            ("WT", []),
            ("gpd1_KO", ["YDL022W"]),
            ("gpd2_KO", ["YOL059W"]),
            ("gpd1_gpd2_double_KO", ["YDL022W", "YOL059W"]),
        ]:
            with model:
                for gid in ko_ids:
                    model.genes.get_by_id(gid).knock_out()
                sol = pfba(model)
                repaired_gpr_outcomes[label] = {
                    "growth": round(float(sol.fluxes["BIOMASS_SC5_notrace"]), 4),
                    "G3PD1ir_flux": round(float(sol.fluxes["G3PD1ir"]), 4),
                    "G3PT_flux": round(float(sol.fluxes["G3PT"]), 4),
                    "EX_glyc_e_flux": round(float(sol.fluxes["EX_glyc_e"]), 4),
                    "EX_etoh_e_flux": round(float(sol.fluxes["EX_etoh_e"]), 4),
                }
        gpd_experiment["repaired_gpr_G3PD1ir_YDL022W_or_YOL059W"] = (
            repaired_gpr_outcomes
        )

    # Repair Experiment B: DAL3 (YIR032C) & DUR1,2 (YBR208C) on allantoin sole N source
    dal3_experiment: dict[str, Any] = {}
    with model:
        model.reactions.EX_nh4_e.lower_bound = 0.0
        model.reactions.EX_alltn_e.lower_bound = -10.0
        wt_orig = model.optimize()
        with model:
            model.genes.YBR208C.knock_out()
            dur_ko_orig = model.optimize()
        with model:
            model.genes.YIR032C.knock_out()
            dal3_ko_orig = model.optimize()

        dal3_experiment["original_iMM904_bacterial_hydrolase_EC_3_5_3_19"] = {
            "UGLYCH_reaction": model.reactions.UGLYCH.reaction,
            "wt_growth": round(float(wt_orig.objective_value), 4),
            "dur1_2_KO_growth": round(float(dur_ko_orig.objective_value), 4),
            "dur1_2_KO_urea_secretion": round(float(dur_ko_orig.fluxes["EX_urea_e"]), 4),
            "dal3_KO_growth": round(float(dal3_ko_orig.objective_value), 4),
        }

        model.reactions.UGLYCH.reaction = "urdglyc_c --> glx_c + urea_c"
        wt_fixed = model.optimize()
        with model:
            model.genes.YBR208C.knock_out()
            dur_ko_fixed = model.optimize()
        with model:
            model.genes.YIR032C.knock_out()
            dal3_ko_fixed = model.optimize()

        dal3_experiment["repaired_yeast_ureidoglycolate_lyase_EC_4_3_2_3"] = {
            "UGLYCH_reaction": model.reactions.UGLYCH.reaction,
            "wt_growth": round(float(wt_fixed.objective_value), 4),
            "dur1_2_KO_growth": round(float(dur_ko_fixed.objective_value), 4),
            "dur1_2_KO_urea_secretion": round(
                float(dur_ko_fixed.fluxes["EX_urea_e"]), 4
            ),
            "dal3_KO_growth": round(float(dal3_ko_fixed.objective_value), 4),
        }

    # Repair Experiment C: BNA3 (YJL060W) vs BNA7 (YDR428C) & prokaryotic ASPOcm/QULNS removal
    bna_experiment: dict[str, Any] = {}
    with model:
        model.objective = "NNDPR"
        wt_nndpr_unmod = model.optimize().objective_value
        with model:
            model.genes.YJL060W.knock_out()
            bna3_ko_nndpr_unmod = model.optimize().objective_value
        with model:
            model.reactions.EX_o2_e.lower_bound = 0.0
            anaero_nndpr_unmod = model.optimize().objective_value

        bna_experiment["unmodified_iMM904_with_prokaryotic_ASPOcm_QULNS"] = {
            "aerobic_wt_NNDPR_max": round(float(wt_nndpr_unmod), 4),
            "aerobic_bna3_KO_NNDPR_max": round(float(bna3_ko_nndpr_unmod), 4),
            "anaerobic_wt_NNDPR_max": round(float(anaero_nndpr_unmod), 4),
        }

        model.reactions.ASPOcm.bounds = (0.0, 0.0)
        model.reactions.QULNS.bounds = (0.0, 0.0)
        wt_eu_only = model.optimize().objective_value
        with model:
            model.genes.YJL060W.knock_out()
            bna3_ko_wrong_gpr = model.optimize().objective_value
        with model:
            model.reactions.EX_o2_e.lower_bound = 0.0
            anaero_eu_only = model.optimize().objective_value

        bna_experiment[
            "after_removing_prokaryotic_ASPOcm_QULNS_with_original_FKYNH_GPR"
        ] = {
            "aerobic_wt_NNDPR_max": round(float(wt_eu_only), 4),
            "aerobic_bna3_KO_NNDPR_max": round(float(bna3_ko_wrong_gpr), 4),
            "anaerobic_wt_NNDPR_max": round(float(anaero_eu_only), 4),
        }

        model.reactions.FKYNH.gene_reaction_rule = "YDR428C"
        with model:
            model.genes.YJL060W.knock_out()
            bna3_ko_repaired = model.optimize().objective_value
        with model:
            model.genes.YDR428C.knock_out()
            bna7_ko_repaired = model.optimize().objective_value

        bna_experiment["after_reassigning_FKYNH_to_BNA7_YDR428C"] = {
            "aerobic_wt_NNDPR_max": round(float(wt_eu_only), 4),
            "aerobic_bna3_KO_NNDPR_max": round(float(bna3_ko_repaired), 4),
            "aerobic_bna7_KO_NNDPR_max": round(float(bna7_ko_repaired), 4),
            "anaerobic_wt_NNDPR_max": round(float(anaero_eu_only), 4),
        }

    return {
        "single_gene_knockouts": single_ko_results,
        "gpd1_gpd2_anaerobic_redox_experiment": gpd_experiment,
        "dal3_dur1_2_allantoin_experiment": dal3_experiment,
        "bna3_bna7_nad_biosynthesis_experiment": bna_experiment,
    }


def run_ast_eflux_comparison(model: cobra.Model) -> dict[str, Any]:
    """Compare ChatGEM's regex E-Flux parser vs AST E-Flux and evaluate condition regimes."""
    test_expr = {
        "YGR240C": 0.8,
        "YMR205C": 0.2,
        "YDL022W": 0.15,
        "YOL059W": 0.95,
        "YFR053C": 0.1,
        "YGL253W": 0.9,
        "YCL040W": 0.15,
        "YKL060C": 0.0,
    }

    parser_tests = []
    for label, gpr_str in [
        ("PFK heterooctamer (AND)", "YGR240C and YMR205C"),
        ("Cytosolic GPD isozymes (OR)", "YDL022W or YOL059W"),
        ("Hexokinase isozymes (3-way OR)", "YFR053C or YGL253W or YCL040W"),
        (
            "Nested complex with isozyme subunits ((A or B) and C)",
            "(YFR053C or YGL253W) and YMR205C",
        ),
        (
            "Alternative complexes ((A and B) or (C and D))",
            "(YGR240C and YMR205C) or (YDL022W and YOL059W)",
        ),
    ]:
        rxn = cobra.Reaction("TEST")
        rxn.gene_reaction_rule = gpr_str
        ast_val = eval_gpr_ast_eflux(rxn.gpr.body, test_expr, default_missing=0.0)
        buggy_val = chatgem_buggy_eflux_parser(gpr_str, test_expr)
        parser_tests.append(
            {
                "case": label,
                "gpr": gpr_str,
                "correct_ast_capacity": round(ast_val, 4),
                "chatgem_regex_capacity": round(buggy_val, 4),
                "discrepancy": round(abs(ast_val - buggy_val), 4),
            }
        )

    regimes = {
        "aerobic_high_glucose": {
            "YGL253W": 1.00,
            "YFR053C": 0.12,
            "YCL040W": 0.15,
            "YGR192C": 1.00,
            "YJR009C": 0.45,
            "YJL052W": 0.10,
            "YLR044C": 1.00,
            "YLR134W": 0.10,
            "YGR087C": 0.02,
            "YOL086C": 1.00,
            "YMR303C": 0.05,
            "YDL022W": 0.25,
            "YOL059W": 0.30,
        },
        "anaerobic_glucose_fermentation": {
            "YGL253W": 1.00,
            "YFR053C": 0.10,
            "YCL040W": 0.15,
            "YGR192C": 1.00,
            "YJR009C": 0.50,
            "YJL052W": 0.10,
            "YLR044C": 1.00,
            "YLR134W": 0.15,
            "YGR087C": 0.02,
            "YOL086C": 1.00,
            "YMR303C": 0.01,
            "YDL022W": 0.20,
            "YOL059W": 0.95,
        },
        "hyperosmotic_stress_glucose": {
            "YGL253W": 0.80,
            "YFR053C": 0.40,
            "YCL040W": 0.30,
            "YGR192C": 0.90,
            "YJR009C": 0.45,
            "YJL052W": 0.55,
            "YLR044C": 0.85,
            "YLR134W": 0.10,
            "YGR087C": 0.02,
            "YOL086C": 0.85,
            "YMR303C": 0.05,
            "YDL022W": 1.00,
            "YOL059W": 0.15,
        },
        "aerobic_ethanol_respiration": {
            "YGL253W": 0.15,
            "YFR053C": 0.85,
            "YCL040W": 0.75,
            "YGR192C": 0.70,
            "YJR009C": 0.40,
            "YJL052W": 0.65,
            "YLR044C": 0.20,
            "YLR134W": 0.05,
            "YGR087C": 0.05,
            "YOL086C": 0.20,
            "YMR303C": 1.00,
            "YDL022W": 0.30,
            "YOL059W": 0.10,
        },
    }

    regime_summaries = {}
    for reg_name, expr in regimes.items():
        hxk_tot = expr["YGL253W"] + expr["YFR053C"] + expr["YCL040W"]
        tdh_tot = expr["YGR192C"] + expr["YJR009C"] + expr["YJL052W"]
        pdc_tot = expr["YLR044C"] + expr["YLR134W"] + expr["YGR087C"]
        adh_tot = expr["YOL086C"] + expr["YMR303C"]
        gpd_tot = expr["YDL022W"] + expr["YOL059W"]

        regime_summaries[reg_name] = {
            "HEX1_capacity_sum": round(hxk_tot, 3),
            "HEX1_dominant_isoform": (
                f"HXK2 ({100*expr['YGL253W']/hxk_tot:.1f}%)"
                if expr["YGL253W"] >= expr["YFR053C"]
                else f"HXK1 ({100*expr['YFR053C']/hxk_tot:.1f}%)"
            ),
            "GAPD_capacity_sum": round(tdh_tot, 3),
            "GAPD_dominant_isoform": f"TDH3 ({100*expr['YGR192C']/tdh_tot:.1f}%)",
            "PYRDC_capacity_sum": round(pdc_tot, 3),
            "PYRDC_dominant_isoform": f"PDC1 ({100*expr['YLR044C']/pdc_tot:.1f}%)",
            "ALCD2_capacity_sum": round(adh_tot, 3),
            "ALCD2_dominant_isoform": (
                f"ADH1 ({100*expr['YOL086C']/adh_tot:.1f}%)"
                if expr["YOL086C"] >= expr["YMR303C"]
                else f"ADH2 ({100*expr['YMR303C']/adh_tot:.1f}%)"
            ),
            "G3PD1ir_repaired_capacity_sum": round(gpd_tot, 3),
            "G3PD1ir_dominant_isoform": (
                f"GPD2 ({100*expr['YOL059W']/gpd_tot:.1f}%)"
                if expr["YOL059W"] >= expr["YDL022W"]
                else f"GPD1 ({100*expr['YDL022W']/gpd_tot:.1f}%)"
            ),
        }

    return {
        "gpr_parser_benchmark": parser_tests,
        "condition_specific_isozyme_shares": regime_summaries,
    }


def dump_yaml(data: Any, path: Path) -> None:
    """Write YAML without anchors/aliases."""
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--model-id",
        type=str,
        default="iMM904",
        help="BiGG model ID to load (e.g., iMM904, iML1515)",
    )
    parser.add_argument(
        "--model",
        type=Path,
        default=None,
        help="Optional local path to model .json/.json.gz",
    )
    parser.add_argument(
        "--genes-dir",
        type=Path,
        default=Path("genes/yeast"),
        help="Directory containing curated gene review folders",
    )
    parser.add_argument(
        "--modules-dir",
        type=Path,
        default=Path("modules"),
        help="Directory containing curated metabolic module YAML files",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("projects/YEAST_METABOLIC_ENGINEERING/out"),
        help="Directory for structured YAML outputs",
    )
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    model = load_bigg_model(args.model_id, args.model)

    print(
        f"Loaded {model.id}: {len(model.reactions)} reactions, "
        f"{len(model.metabolites)} metabolites, {len(model.genes)} genes"
    )

    proteome_audit = audit_proteome_alignment(model, args.genes_dir)
    dump_yaml(proteome_audit, args.out_dir / "proteome_ec_gpr_alignment.yaml")
    print(
        f"1. Proteome alignment written: {proteome_audit['aligned_reviewed_genes']} "
        f"reviewed genes aligned ({proteome_audit['class_change_count']} CLASS_CHANGE)"
    )

    if model.id == "iMM904":
        cohort_audit = audit_target_cohort_and_modules(
            model, args.genes_dir, args.modules_dir
        )
        dump_yaml(cohort_audit, args.out_dir / "target_genes_audit.yaml")
        print(
            f"2. Target cohort audit written: {cohort_audit['target_genes_count']} genes"
        )

        routing_audit = audit_fba_vs_pfba_routing(model)
        dump_yaml(routing_audit, args.out_dir / "fba_vs_pfba_routing.yaml")
        print("3. Standard FBA vs pFBA routing audit written")

        ko_repair_audit = run_knockout_and_repair_experiments(model)
        dump_yaml(ko_repair_audit, args.out_dir / "knockout_and_repair_experiments.yaml")
        print("4. Knockout and curation-guided repair experiments written")

        eflux_audit = run_ast_eflux_comparison(model)
        dump_yaml(eflux_audit, args.out_dir / "ast_eflux_conditions.yaml")
        print("5. AST E-Flux condition benchmark written")


if __name__ == "__main__":
    main()
