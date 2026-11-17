"""Pilot C: is the cerebellum-development module switched on in the right order?

Extends pathway satisfiability to a developmental module. A metabolic module
is asked "can this run here?"; a developmental one is a sequence, so the
question is asked per developmental stage: is each step's gene expressed, in
that step's own anatomical context, at that stage? The answer is a step x stage
matrix that should show a staggered wave in module order, not a block.

Oracle: mouse Bgee 15.2 stage-resolved present calls (REST API; in situ from
MGI GXD plus RNA-seq/Affymetrix), for the OMA mouse ortholog of each human
module participant. Stages are placed on one days-post-conception axis from
MmusDv (start/end in dpc, days, weeks or months post birth; birth = 19.5 dpc;
UBERON stage ids through MmusDv xrefs) and a stage counts toward a bin (BINS)
only if its whole interval lies inside it, so broad stages (life cycle,
organogenesis stage, infant stage P4-P23) are not used. A call counts toward a step only if its anatomical entity lies
inside the step's declared context, develops into it, or is a cerebellar
sample containing it: calls on structures broader than the cerebellum (brain,
hindbrain) never count, because Bgee propagates calls up the anatomy.

Three variants:
  declared_strict  the module YAML's own context (nearest node with one); a
             call must lie inside the context, develop into it, or (for a
             cell type) lie inside the cell type's CL location
  declared   as declared_strict, plus whole-cerebellar samples that contain
             the context (weakest; blind to whether the context exists yet)
  territory  declared context plus the cerebellar territory (cerebellum, its
             rhombic-lip precursor, rhombomere 1, midbrain-hindbrain boundary,
             metencephalon), for steps that act before the cerebellum exists

The engine (``ai_gene_review.module_logic``) decides step satisfiability; this
script only supplies the stage-specific predicate.

Outputs: ``results/cerebellum_timing.yaml``, ``results/cerebellum_timing.md``,
``data/cerebellum_stage_calls_mouse.tsv``.

Usage (from repo root):
    uv run python projects/BGEEDB_EXPRESSION/scripts/cerebellum_timing.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Optional

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import bgee_common as bc  # noqa: E402
from ai_gene_review.module_logic import (  # noqa: E402
    compile_module_file,
    iter_atoms,
    step_id,
    unsatisfied_steps,
)

MODULE = bc.REPO / "modules" / "cerebellum_development.yaml"
BIRTH_DPC = 19.5
# (label, start dpc inclusive, end dpc exclusive). Analysis parameters chosen to
# bracket the module's phases in mouse; they are not results.
BINS = [
    ("E8-E10.5", 8.0, 10.5),
    ("E10.5-E14", 10.5, 14.0),
    ("E14-birth", 14.0, BIRTH_DPC),
    ("P0-P7", BIRTH_DPC, BIRTH_DPC + 7),
    ("P7-P21", BIRTH_DPC + 7, BIRTH_DPC + 21),
    ("adult", BIRTH_DPC + 21, 10_000.0),
]
CEREBELLUM = "UBERON:0002037"
TERRITORY = {
    "UBERON:0002037",  # cerebellum
    "UBERON:0006215",  # rhombic lip
    "UBERON:0005499",  # rhombomere 1
    "UBERON:0003052",  # midbrain-hindbrain boundary
    "UBERON:0001895",  # metencephalon
}


# ---------------------------------------------------------------------------
# Module walk: annoton -> step order, step id, nearest declared context
# ---------------------------------------------------------------------------


def _context_ids(node: dict) -> list[str]:
    ctx = node.get("context") or {}
    ids = []
    for key in ("anatomical_locations", "cell_types"):
        for d in ctx.get(key) or []:
            tid = (d.get("term") or {}).get("id")
            if tid:
                ids.append(tid)
    return ids


def annoton_contexts(path: Path) -> dict[str, dict]:
    doc = yaml.safe_load(path.read_text())
    module = doc["module"]
    out: dict[str, dict] = {}

    def walk(node: dict, inherited: list[str], step: Optional[tuple[int, str]]) -> None:
        here = _context_ids(node) or inherited
        for ann in node.get("annotons") or []:
            out[ann["id"]] = {"context": here, "step_order": step[0] if step else None,
                              "step": step[1] if step else None, "node": node.get("id")}
        for part in node.get("parts") or []:
            child = part.get("node") or {}
            walk(child, here, step or (part.get("order"), child.get("id")))
        for vs in node.get("variant_sets") or []:
            for var in vs.get("variants") or []:
                walk(var, here, step)

    walk(module, _context_ids(module), None)
    return out


# ---------------------------------------------------------------------------
# Stage axis
# ---------------------------------------------------------------------------


def stage_axis() -> dict[str, tuple[float, float]]:
    """Stage id -> (start, end) in days post conception.

    MmusDv gives start/end in dpc, days, weeks or months post birth; days post
    birth win for postnatal stages (TS27 has start_dpc 19 but start_dpb 0). A
    Theiler stage with only a start ends where the stage that follows it
    begins. UBERON stage ids that Bgee uses (``neonate stage``) are resolved
    through MmusDv xrefs (UBERON:0007221 -> TS27, P0-P3).
    """
    dv = bc.parse_obo(bc.ontology_file("mmusdv.obo"))

    def to_dpc(p: dict, side: str) -> Optional[float]:
        for key, scale in ((f"{side}_dpb", 1.0), (f"{side}_wpb", 7.0), (f"{side}_mpb", 30.4)):
            if key in p:
                return BIRTH_DPC + scale * float(p[key])
        if f"{side}_dpc" in p:
            return float(p[f"{side}_dpc"])
        return None

    start = {sid: to_dpc(t["props"], "start") for sid, t in dv.items() if sid.startswith("MmusDv:") and not t.get("obsolete")}
    start = {k: v for k, v in start.items() if v is not None}
    follows: dict[str, str] = {}
    for sid, t in dv.items():
        for pred, obj in t["rel"]:
            if pred == "immediately_preceded_by":
                follows[obj] = sid
    axis: dict[str, tuple[float, float]] = {}
    for sid, st in start.items():
        end = to_dpc(dv[sid]["props"], "end")
        if end is None and sid in follows and follows[sid] in start:
            end = start[follows[sid]]
        if end is None:
            end = st + 1.0 if st < BIRTH_DPC else 10_000.0
        axis[sid] = (st, end)
        for x in dv[sid]["xref"]:
            if x.startswith("UBERON:"):
                axis.setdefault(x, (st, end))
    return axis


def bin_of(interval: tuple[float, float]) -> Optional[str]:
    """The bin that wholly contains a stage interval (None if it straddles bins)."""
    st, end = interval
    for label, lo, hi in BINS:
        if lo <= st < hi and end <= hi + 1e-6:
            return label
    return None


# ---------------------------------------------------------------------------
# Context matching
# ---------------------------------------------------------------------------


def match(entity: str, context: list[str], anat: bc.Anatomy, allow_containing: bool = True) -> Optional[str]:
    """How a call on ``entity`` relates to a step's context, or None.

    ``allow_containing`` admits a whole-cerebellum (or cerebellar-part) sample
    that contains the context. It is the weakest match, and it ignores whether
    the context structure exists at that stage (an adult cerebellum sample
    "contains" the transient external granule layer), so the strict variant
    turns it off.
    """
    for c in context:
        if anat.within(entity, c) or anat.precursor_of(entity, c):
            return "within"
        if c.startswith("CL:") and any(anat.within(entity, loc) for loc in anat.locations(c)):
            return "colocated"
    cerebellar = anat.within(entity, CEREBELLUM) or anat.precursor_of(entity, CEREBELLUM)
    if cerebellar and allow_containing:
        for c in context:
            if anat.within(c, entity) or (c.startswith("CL:") and any(anat.within(loc, entity) for loc in anat.locations(c))):
                return "cerebellar sample containing context"
    return None


def main() -> None:
    anat = bc.load_anatomy()
    axis = stage_axis()
    contexts = annoton_contexts(MODULE)
    circuit = compile_module_file(MODULE)
    atoms = list(iter_atoms(circuit))

    # human symbol -> human Ensembl (UniProt DR Bgee) -> mouse ortholog (Bgee/OMA)
    mouse_of: dict[str, list[tuple[str, str]]] = {}
    for a in atoms:
        for sym in a.gene_symbols:
            ens = bc.bgee_gene_id(bc.REPO / "genes" / "human" / sym / f"{sym}-uniprot.txt")
            mouse_of[sym] = bc.orthologs(ens, 9606, 10090) if ens else []

    stage_rows = []
    calls_by_gene: dict[str, list[tuple[str, str, str, str, float, str]]] = {}
    for sym, orths in mouse_of.items():
        rows = []
        for mid, mname in orths:
            for c in bc.stage_calls(mid, 10090):
                anat_id = c["condition"]["anatEntity"]["id"]
                st = c["condition"].get("devStage", {})
                sid = st.get("id", "")
                if sid not in axis:
                    continue
                score = float(c["expressionScore"]["expressionScore"])
                b = bin_of(axis[sid])
                if b is None:
                    continue
                rows.append((anat_id, c["condition"]["anatEntity"]["name"], sid, b, score,
                             "|".join(c.get("dataTypesWithData", []))))
                stage_rows.append([sym, mid, mname, anat_id, c["condition"]["anatEntity"]["name"], sid, st.get("name", ""),
                                   axis[sid][0], axis[sid][1] if axis[sid][1] < 10_000 else "", b, score,
                                   "|".join(c.get("dataTypesWithData", []))])
        calls_by_gene[sym] = rows
    with (bc.DATA / "cerebellum_stage_calls_mouse.tsv").open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["human_symbol", "mouse_gene", "mouse_symbol", "entity", "entity_name", "stage", "stage_name",
                    "stage_start_dpc", "stage_end_dpc", "bin", "score", "data_types"])
        for r in sorted(stage_rows, key=lambda r: (r[0], r[7], r[3])):
            w.writerow(r)

    def expressed(sym: str, ctx: list[str], b: str, lenient: bool = True) -> tuple[bool, Optional[str]]:
        best = None
        for anat_id, name, _sid, bb, score, _dt in calls_by_gene.get(sym, []):
            if bb != b:
                continue
            how = match(anat_id, ctx, anat, allow_containing=lenient)
            if how and (best is None or score > best[1]):
                best = (f"{name} ({how})", score)
        return (best is not None), (best[0] if best else None)

    def any_call(sym: str, b: str) -> bool:
        return any(bb == b for _a, _n, _s, bb, _sc, _d in calls_by_gene.get(sym, []))

    variants = {
        "declared_strict": (lambda ctx: ctx, False),
        "declared": (lambda ctx: ctx, True),
        "territory": (lambda ctx: list(dict.fromkeys(ctx + sorted(TERRITORY))), True),
    }
    result: dict = {"bgee_release": bc.BGEE_RELEASE, "module": "modules/cerebellum_development.yaml",
                    "bins_dpc": [{"bin": b, "start": lo, "end": (hi if hi < 10_000 else None)} for b, lo, hi in BINS],
                    "orthologs": {s: [f"{m} {n}" for m, n in o] for s, o in mouse_of.items()},
                    "variants": {}}
    for vname, (widen, lenient) in variants.items():
        atom_ctx = {a.node_id: widen(contexts.get(a.node_id, {}).get("context", [])) for a in atoms}
        genes = {}
        for a in atoms:
            info = contexts.get(a.node_id, {})
            for sym in a.gene_symbols:
                row = {}
                for b, _lo, _hi in BINS:
                    ok, why = expressed(sym, atom_ctx[a.node_id], b, lenient)
                    row[b] = ("IN_CONTEXT: " + why) if ok else ("ELSEWHERE" if any_call(sym, b) else "NO_CALL")
                genes[sym] = {"step_order": info.get("step_order"), "step": info.get("step"),
                              "context": [f"{c} {anat.name(c)}" for c in contexts.get(a.node_id, {}).get("context", [])],
                              "by_stage": row}
        steps = {}
        for b, _lo, _hi in BINS:
            def holds(atom, b=b, lenient=lenient):
                return any(expressed(s, atom_ctx[atom.node_id], b, lenient)[0] for s in atom.gene_symbols)
            failing = {step_id(s) for s in unsatisfied_steps(circuit, holds)}
            for ch in circuit.children:
                steps.setdefault(step_id(ch), {})[b] = step_id(ch) not in failing
        onsets = {}
        for sid, row in steps.items():
            first = next((b for b, _lo, _hi in BINS if row[b]), None)
            onsets[sid] = first
        order = [step_id(ch) for ch in circuit.children]
        idx = {b: i for i, (b, _lo, _hi) in enumerate(BINS)}
        onset_idx = [idx[onsets[s]] if onsets[s] else None for s in order]
        known = [(i, o) for i, o in enumerate(onset_idx) if o is not None]
        concordant = sum(1 for x in range(len(known)) for y in range(x + 1, len(known)) if known[x][1] < known[y][1])
        discordant = sum(1 for x in range(len(known)) for y in range(x + 1, len(known)) if known[x][1] > known[y][1])
        ties = sum(1 for x in range(len(known)) for y in range(x + 1, len(known)) if known[x][1] == known[y][1])
        result["variants"][vname] = {
            "steps_satisfied_by_stage": steps,
            "step_onset": onsets,
            "onset_order_pairs": {"concordant": concordant, "discordant": discordant, "tied": ties},
            "genes": genes,
        }

    (bc.RESULTS / "cerebellum_timing.yaml").write_text(yaml.safe_dump(result, sort_keys=False, width=120))

    lines = ["---", 'title: "Cerebellum development module x mouse Bgee developmental expression"', "species: [human]", "---", "",
             "# Cerebellum development module x mouse Bgee developmental expression", "",
             "Generated by `scripts/cerebellum_timing.py`; do not edit. Bgee 15.2 stage-resolved present calls "
             "for the OMA mouse ortholog of each module participant. ✔ = expressed in the step's context at that "
             "stage; · = expressed only elsewhere at that stage; blank = no call at that stage.", ""]
    for vname, v in result["variants"].items():
        lines += [f"## Variant: {vname}", "", "### Steps satisfiable per stage (module_logic engine)", "",
                  "| step | " + " | ".join(b for b, _, _ in BINS) + " | onset |", "|---" * (len(BINS) + 2) + "|"]
        for sid, row in v["steps_satisfied_by_stage"].items():
            lines.append(f"| {sid} | " + " | ".join("✔" if row[b] else "" for b, _, _ in BINS) + f" | {v['step_onset'][sid] or '—'} |")
        p = v["onset_order_pairs"]
        lines += ["", f"Step-onset order vs module order: {p['concordant']} concordant, {p['discordant']} discordant, "
                  f"{p['tied']} tied pairs.", "", "### Genes", "",
                  "| step | gene | context | " + " | ".join(b for b, _, _ in BINS) + " |", "|---" * (len(BINS) + 3) + "|"]
        for sym, g in sorted(v["genes"].items(), key=lambda kv: (kv[1]["step_order"] or 0, kv[0])):
            cells = []
            for b, _, _ in BINS:
                val = g["by_stage"][b]
                cells.append("✔" if val.startswith("IN_CONTEXT") else "·" if val == "ELSEWHERE" else "")
            lines.append(f"| {g['step_order']} {g['step']} | {sym} | {'; '.join(g['context'])} | " + " | ".join(cells) + " |")
        lines.append("")
    (bc.RESULTS / "cerebellum_timing.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
