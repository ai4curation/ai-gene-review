#!/usr/bin/env python
"""Feasibility-spike converter: GapMind ``.steps`` -> module ``ModuleReview`` YAML.

This is a **mining feasibility spike**, not a production importer. Its only job
is to show how much of a GapMind amino-acid biosynthesis pathway definition can
be mechanically lifted into the ``modules/`` ``ModuleReview`` schema, and where a
human (or deep-research pass) still has to fill in judgement.

GapMind ``.steps`` grammar (see https://github.com/morgannprice/PaperBLAST/tree/master/gaps):

* ``stepId<TAB>description<TAB>query<TAB>query...`` -- a step, where each query is
  one of ``EC:x.x.x.x``, ``hmm:PFxxxxx`` / ``hmm:TIGRxxxxx``, ``uniprot:ID``,
  ``curated:DB::ID`` (positive exemplars), ``term:...`` (name synonyms), or
  ``ignore:...`` / ``ignore_other:...`` (negative exemplars -- explicitly NOT the step).
* ``ruleName: a b c`` -- a rule combining steps/rules conjunctively. The SAME rule
  name may appear on several lines; those alternatives are an OR (variant set).
* ``import other.steps:stepA stepB`` -- pull step definitions from a sibling file.
* ``all: ...`` -- the top-level rule defining the pathway backbone.

Mapping decisions:

* step -> ``ModuleAnnoton`` inside a ``REACTION`` ``ModuleNode``. EC-bearing steps
  use an ``ANY_WITH_FUNCTION`` selector; HMM-only steps use a ``FAMILY`` selector
  with the Pfam/TIGRFam id and ``representative_members`` taken from the positive
  exemplars.
* single-definition rule -> a ``METABOLIC_PATHWAY`` ``ModuleNode`` with ordered ``parts``.
* multi-definition rule -> a ``ModuleVariantSet`` (``selection: EXACTLY_ONE``,
  ``axis: route``) -- this is how GapMind's alternative routes (e.g. the three
  ways isoleucine makes 2-oxobutanoate) land in the schema.
* EC numbers are grounded against the ModelSEED reactions table to attach
  ModelSEED/KEGG/MetaCyc cross-references as ``EvidenceItem``s.

Deliberate non-goals / honesty notes:

* **GO molecular-function term ids are never guessed.** EC/Pfam/KEGG ids are
  carried verbatim as ``EvidenceItem.source_id`` provenance; assigning the GO MF
  term is left to the human/deep-research review (per repo "never guess identifiers").
* The output is a ``status: DRAFT`` stub meant to be reviewed, not published.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml

RULE_RE = re.compile(r"^([A-Za-z0-9_]+):\s+(.+)$")
IMPORT_RE = re.compile(r"^import\s+(\S+\.steps):\s*(.+)$")


@dataclass
class Step:
    """A single GapMind step (one enzymatic/transport function)."""

    step_id: str
    description: str
    ec_numbers: list[str] = field(default_factory=list)
    hmms: list[str] = field(default_factory=list)
    exemplars: list[str] = field(default_factory=list)  # positive uniprot:/curated: ids
    comment: str = ""
    source_file: str = ""


@dataclass
class ParsedSteps:
    """Parsed contents of one ``.steps`` file (after import resolution)."""

    pathway_id: str
    header_comment: str
    steps: dict[str, Step]
    # rule name -> list of alternative definitions; each definition is a list of step/rule ids
    rules: dict[str, list[list[str]]]
    rule_order: list[str]


def _classify_query(step: Step, token: str) -> None:
    """Sort one query token into the right bucket on ``step``."""
    if token.startswith("EC:"):
        step.ec_numbers.append(token[3:])
    elif token.startswith("hmm:"):
        step.hmms.append(token[4:])
    elif token.startswith("uniprot:"):
        step.exemplars.append(token[len("uniprot:") :])
    elif token.startswith("curated:"):
        step.exemplars.append(token[len("curated:") :])
    # term:, ignore:, ignore_other: are intentionally dropped from the structured
    # output (synonyms / negative exemplars are provenance noise for a module sketch).


def parse_steps_file(path: Path) -> ParsedSteps:
    """Parse a GapMind ``.steps`` file, resolving ``import`` directives from siblings.

    >>> p = parse_steps_file(Path("cache/gapmind/aa/his.steps"))
    >>> p.pathway_id
    'his'
    >>> p.steps["hisG"].ec_numbers
    ['2.4.2.17']
    >>> p.rules["all"][0][:3]
    ['prs', 'hisG', 'hisI']
    """
    pathway_id = path.stem
    steps: dict[str, Step] = {}
    rules: dict[str, list[list[str]]] = {}
    rule_order: list[str] = []
    header_lines: list[str] = []
    pending_comment: list[str] = []
    seen_first_step = False

    for raw in path.read_text().splitlines():
        line = raw.rstrip("\n")
        if not line.strip():
            pending_comment = []
            continue
        if line.startswith("#"):
            text = line.lstrip("#").strip()
            if seen_first_step:
                pending_comment.append(text)
            else:
                header_lines.append(text)
            continue

        imp = IMPORT_RE.match(line)
        if imp:
            seen_first_step = True
            imported = _resolve_import(path.parent, imp.group(1), imp.group(2).split())
            for s in imported:
                steps.setdefault(s.step_id, s)
            pending_comment = []
            continue

        if "\t" in line:
            seen_first_step = True
            fields = line.split("\t")
            step = Step(
                step_id=fields[0].strip(),
                description=fields[1].strip() if len(fields) > 1 else fields[0].strip(),
                comment=" ".join(pending_comment),
                source_file=path.name,
            )
            for tok in fields[2:]:
                _classify_query(step, tok.strip())
            steps[step.step_id] = step
            pending_comment = []
            continue

        rule = RULE_RE.match(line)
        if rule:
            seen_first_step = True
            name, body = rule.group(1), rule.group(2)
            rules.setdefault(name, []).append(body.split())
            if name not in rule_order:
                rule_order.append(name)
            pending_comment = []

    return ParsedSteps(
        pathway_id=pathway_id,
        header_comment=" ".join(header_lines),
        steps=steps,
        rules=rules,
        rule_order=rule_order,
    )


def _resolve_import(directory: Path, filename: str, step_ids: list[str]) -> list[Step]:
    """Load specific step definitions from a sibling ``.steps`` file."""
    sibling = directory / filename
    if not sibling.exists():
        # Honest fallback: emit placeholder steps so the backbone stays intact.
        return [
            Step(step_id=sid, description=f"{sid} (imported, definition unavailable)",
                 comment=f"Imported from {filename}; source file not cached.")
            for sid in step_ids
        ]
    other = parse_steps_file(sibling)
    out = []
    for sid in step_ids:
        if sid in other.steps:
            s = other.steps[sid]
            s.comment = (s.comment + f" [imported from {filename}]").strip()
            out.append(s)
        else:
            out.append(Step(step_id=sid, description=f"{sid} (imported)",
                            comment=f"Imported from {filename}; step not found."))
    return out


# --------------------------------------------------------------------------- #
# ModelSEED grounding
# --------------------------------------------------------------------------- #

def load_modelseed_ec_index(reactions_tsv: Path) -> dict[str, list[dict[str, str]]]:
    """Build an ``EC -> [{modelseed, kegg, metacyc, name}]`` index from ModelSEED.

    Only non-obsolete reactions are indexed.
    """
    index: dict[str, list[dict[str, str]]] = {}
    with reactions_tsv.open() as fh:
        header = fh.readline().rstrip("\n").split("\t")
        col = {name: i for i, name in enumerate(header)}
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if f[col["is_obsolete"]] == "1":
                continue
            ecs = f[col["ec_numbers"]]
            if not ecs or ecs == "null":
                continue
            aliases = f[col["aliases"]]
            entry = {
                "modelseed": f[col["id"]],
                "name": f[col["name"]],
                "kegg": _alias(aliases, "KEGG"),
                "metacyc": _alias(aliases, "MetaCyc"),
            }
            for ec in ecs.replace("|", ";").split(";"):
                ec = ec.strip()
                if ec:
                    index.setdefault(ec, []).append(entry)
    return index


def _alias(aliases: str, db: str) -> str:
    """Pull the first id for ``db`` out of a ModelSEED pipe-delimited alias string."""
    for block in aliases.split("|"):
        if block.startswith(f"{db}:"):
            ids = block[len(db) + 1 :].strip()
            return ids.split(";")[0].strip()
    return ""


# --------------------------------------------------------------------------- #
# YAML emission
# --------------------------------------------------------------------------- #

def _function_evidence(step: Step, seed_index: dict) -> list[dict]:
    """Mined provenance for a step: EC, HMM, and ModelSEED/KEGG/MetaCyc xrefs."""
    ev: list[dict] = []
    for ec in step.ec_numbers:
        item: dict = {"source_id": f"EC:{ec}", "statement": step.description}
        hits = seed_index.get(ec, [])
        if hits:
            h = hits[0]
            extra = [f"ModelSEED:{h['modelseed']}"]
            if h["kegg"]:
                extra.append(f"KEGG:{h['kegg']}")
            if h["metacyc"]:
                extra.append(f"MetaCyc:{h['metacyc']}")
            item["notes"] = "ModelSEED grounding: " + ", ".join(extra) + f" ({h['name']})"
        ev.append(item)
    for hmm in step.hmms:
        prefix = "Pfam" if hmm.startswith("PF") else "NCBIfam"
        ev.append({"source_id": f"{prefix}:{hmm}", "statement": f"HMM for {step.description}"})
    return ev


def _annoton_for_step(step: Step, seed_index: dict) -> dict:
    """Build a ModuleAnnoton dict from a step."""
    func: dict = {"preferred_term": step.description}
    fn_ev = _function_evidence(step, seed_index)
    if fn_ev:
        func["evidence"] = fn_ev

    if step.ec_numbers:
        participant: dict = {
            "selector_type": "ANY_WITH_FUNCTION",
            "required_function": {"preferred_term": step.description},
        }
    elif step.hmms:
        hmm = step.hmms[0]
        prefix = "Pfam" if hmm.startswith("PF") else "NCBIfam"
        family: dict = {
            "preferred_term": step.description,
            "term": {"id": f"{prefix}:{hmm}", "label": step.description},
        }
        if step.exemplars:
            family["representative_members"] = [
                {"preferred_term": ex} for ex in step.exemplars[:5]
            ]
        participant = {"selector_type": "FAMILY", "family": family}
    else:
        participant = {
            "selector_type": "ANY_WITH_FUNCTION",
            "required_function": {"preferred_term": step.description},
        }

    annoton: dict = {
        "id": f"{step.step_id}_activity",
        "label": f"{step.step_id}: {step.description}",
        "participant": participant,
        "function": func,
    }
    if step.comment:
        annoton["notes"] = step.comment
    return annoton


def _step_node(step: Step, seed_index: dict) -> dict:
    """A REACTION node wrapping a single step's annoton."""
    return {
        "id": f"{step.step_id}_step",
        "label": step.description,
        "module_type": "REACTION",
        "annotons": [_annoton_for_step(step, seed_index)],
    }


def _expand_name(name: str, parsed: ParsedSteps, seed_index: dict, depth: int = 0) -> dict:
    """Expand a step-or-rule name into a ModuleNode (recursing through rules)."""
    if name in parsed.steps:
        return _step_node(parsed.steps[name], seed_index)

    # It's a rule.
    definitions = parsed.rules.get(name, [])
    if len(definitions) > 1:
        # OR -> variant set wrapped in a node.
        variants = []
        for i, defn in enumerate(definitions, 1):
            variants.append({
                "id": f"{name}_route{i}",
                "label": f"{name} route {i}: " + " + ".join(defn),
                "module_type": "METABOLIC_PATHWAY",
                "parts": [
                    {"order": j + 1, "node": _expand_name(s, parsed, seed_index, depth + 1)}
                    for j, s in enumerate(defn)
                ],
            })
        return {
            "id": f"{name}_node",
            "label": f"{name} (alternative routes)",
            "module_type": "METABOLIC_PATHWAY",
            "variant_sets": [{
                "id": f"{name}_variants",
                "label": f"Alternative routes to {name}",
                "axis": "route",
                "selection": "EXACTLY_ONE",
                "variants": variants,
            }],
        }

    # Single definition -> ordered sub-pathway.
    defn = definitions[0] if definitions else []
    return {
        "id": f"{name}_node",
        "label": name,
        "module_type": "METABOLIC_PATHWAY",
        "parts": [
            {"order": j + 1, "node": _expand_name(s, parsed, seed_index, depth + 1)}
            for j, s in enumerate(defn)
        ],
    }


def build_module(parsed: ParsedSteps, seed_index: dict, full_name: str) -> dict:
    """Assemble a full ModuleReview document from a parsed pathway."""
    backbone = parsed.rules.get("all", [[]])[0]
    parts = []
    for order, name in enumerate(backbone, 1):
        parts.append({"order": order, "role": name, "node": _expand_name(name, parsed, seed_index)})

    metacyc_ids = re.findall(r"metacyc:([A-Za-z0-9\-]+)", parsed.header_comment, re.IGNORECASE)
    evidence = [{
        "source_id": "GapMind:aa",
        "title": "GapMind for amino acid biosynthesis",
        "statement": parsed.header_comment or f"GapMind {full_name} biosynthesis pathway definition.",
        "url": f"https://papers.genomics.lbl.gov/cgi-bin/gapView.cgi?gdb=NCBI&set=aa&path={parsed.pathway_id}",
    }]
    for mc in metacyc_ids:
        evidence.append({"source_id": f"MetaCyc:{mc}", "statement": "Underlying MetaCyc pathway cited by GapMind."})

    return {
        "id": f"MODULE:gapmind_{parsed.pathway_id}_biosynthesis",
        "title": f"{full_name} biosynthesis (GapMind-derived DRAFT)",
        "description": (
            f"Auto-converted DRAFT module for {full_name} biosynthesis, mined from the "
            f"GapMind amino-acid pathway definition '{parsed.pathway_id}.steps' and grounded "
            "against ModelSEED. Generated by a feasibility-spike importer; GO molecular-function "
            "term assignments and biological prose are intentionally left for human/deep-research "
            "review and must not be treated as curated."
        ),
        "status": "DRAFT",
        "evidence": evidence,
        "module": {
            "id": f"gapmind_{parsed.pathway_id}",
            "label": f"{full_name} biosynthesis",
            "module_type": "METABOLIC_PATHWAY",
            "parts": parts,
        },
        "notes": (
            "MINED DRAFT -- not curated. Source: GapMind .steps (PaperBLAST, Price/Arkin LBL). "
            "Steps map to annotons; GapMind OR-rules map to EXACTLY_ONE variant_sets; EC numbers "
            "grounded to ModelSEED/KEGG/MetaCyc. 'ignore'/'term' GapMind tokens were dropped."
        ),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("steps_file", type=Path, help="path to a GapMind .steps file")
    ap.add_argument("--name", default=None, help="full pathway/amino-acid name for titles")
    ap.add_argument("--modelseed", type=Path,
                    default=Path(__file__).parent / "cache/modelseed/reactions.tsv")
    ap.add_argument("-o", "--out", type=Path, default=None)
    args = ap.parse_args()

    parsed = parse_steps_file(args.steps_file)
    seed_index = load_modelseed_ec_index(args.modelseed) if args.modelseed.exists() else {}
    full_name = args.name or parsed.pathway_id
    module = build_module(parsed, seed_index, full_name)

    text = yaml.dump(module, sort_keys=False, allow_unicode=True, width=100)
    if args.out:
        args.out.write_text(text)
        print(f"wrote {args.out} ({len(text)} bytes); ModelSEED EC index: {len(seed_index)} ECs")
    else:
        print(text)


if __name__ == "__main__":
    main()
