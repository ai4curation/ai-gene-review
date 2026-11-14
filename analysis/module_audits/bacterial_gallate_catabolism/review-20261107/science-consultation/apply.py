"""Bounded Gallate follow-up, with atomic writes and a pre-edit archive."""

import copy
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]
MOD = "modules/bacterial_gallate_catabolism.yaml"
PMID_FILE = "analysis/module_audits/bacterial_gallate_catabolism/review-20261107/publisher-evidence.md"
ONTOLOGY = "analysis/module_audits/bacterial_gallate_catabolism/burkholderia-consultation.ontology.json"
PSEPK = [
    f"genes/PSEPK/{g}/{g}-ai-review.yaml"
    for g in ("galA", "galB", "galC", "galD", "galP")
]
CAND = "genes/BURL3/Bcep18194_C7570/Bcep18194_C7570-ai-review.yaml"
LIGK = "genes/SPHSK/ligK/ligK-ai-review.yaml"
CURATED = PSEPK + [CAND, LIGK, MOD]
OTHER_NOTES = [
    f"genes/BURL3/{g}/{g}-notes.md" for g in ("Bcep18194_C7569", "Bcep18194_C7572")
]
NOTES = (
    [p.replace("-ai-review.yaml", "-notes.md") for p in CURATED[:-1]]
    + OTHER_NOTES
    + ["modules/bacterial_gallate_catabolism-notes.md"]
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic(path, text):
    assert shutil.disk_usage(ROOT).free > 256 * 1024 * 1024, "Insufficient headroom"
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=path.parent, prefix=".gallate-", delete=False
    ) as stream:
        stream.write(text.encode())
        stream.flush()
        os.fsync(stream.fileno())
        temporary = stream.name
    os.replace(temporary, path)


def top_section(text, name):
    start = text.index(name + ":\n")
    following = re.search(r"^\w[^\n]*:\s*", text[start + len(name) + 2 :], re.M)
    end = start + len(name) + 2 + following.start() if following else len(text)
    return start, end


def replace_ref(text, reference_id, new):
    start = text.index("- id: " + reference_id + "\n", text.index("references:\n"))
    candidates = [
        x
        for x in (text.find("\n- id:", start + 1), top_section(text, "references")[1])
        if x >= 0
    ]
    end = min(candidates)
    return (
        text[:start]
        + yaml.safe_dump([new], sort_keys=False, allow_unicode=True, width=100).rstrip()
        + "\n"
        + text[end:].lstrip("\n")
    )


def append_ref(text, reference):
    _, end = top_section(text, "references")
    return (
        text[:end]
        + yaml.safe_dump([reference], sort_keys=False, allow_unicode=True, width=100)
        + text[end:]
    )


def replace_annotation(text, term, new):
    start = text.index("- term:\n    id: " + term + "\n")
    candidates = [
        x
        for x in (
            text.find("\n- term:", start + 1),
            top_section(text, "existing_annotations")[1],
        )
        if x >= 0
    ]
    end = min(candidates)
    return (
        text[:start]
        + yaml.safe_dump([new], sort_keys=False, allow_unicode=True, width=100).rstrip()
        + "\n"
        + text[end:].lstrip("\n")
    )


def main():
    assert not (HERE / "baseline.json").exists()
    assert (
        subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
        == "f852d88b3b0cfe9f4658d879171b446a90dd6f1c"
    )
    coverage = yaml.safe_load((AUDIT / "coverage-evidence.yaml").read_text())
    reviews = [r["review_path"] for r in coverage["proteins"]]
    protected = {}
    for path in reviews:
        for source in (ROOT / path).parent.iterdir():
            if source.is_file() and not source.name.endswith(
                ("-ai-review.yaml", "-notes.md", ".html")
            ):
                protected[str(source.relative_to(ROOT))] = sha(source)
    cited_pmids = {
        n
        for path in reviews + [MOD]
        for n in re.findall(r"PMID:(\d+)", (ROOT / path).read_text())
    }
    for pmid in cited_pmids:
        path = ROOT / "publications" / f"PMID_{pmid}.md"
        assert path.is_file()
        protected[str(path.relative_to(ROOT))] = sha(path)
    prior = {
        str(p.relative_to(ROOT)): sha(p)
        for p in AUDIT.rglob("*")
        if p.is_file() and HERE not in p.parents and "__pycache__" not in p.parts
    }
    before = {
        p: {
            "sha256": sha(ROOT / p),
            "text": (ROOT / p).read_text(),
            "document": yaml.safe_load((ROOT / p).read_text()),
        }
        for p in sorted(set(reviews + [MOD]))
    }
    baseline = {
        "head": "f852d88b3b0cfe9f4658d879171b446a90dd6f1c",
        "documents": before,
        "notes": {
            p: {"sha256": sha(ROOT / p), "text": (ROOT / p).read_text()} for p in NOTES
        },
        "protected_sources": protected,
        "prior_artifacts": prior,
    }
    atomic(HERE / "baseline.json", json.dumps(baseline, indent=2) + "\n")
    old_module = before[MOD]["document"]
    archived = {
        "source_head": baseline["head"],
        "source_sha256": before[MOD]["sha256"],
        "optional_part": old_module["module"]["parts"][0],
        "connection": old_module["module"]["connections"][0],
        "reason": "Move transport outside the consistent intracellular chemical boundary; retain GalP gene review and source evidence as adjacent context.",
    }
    assert archived["optional_part"]["node"]["id"] == "gallate_outer_membrane_entry"
    atomic(HERE / "galp-model-archive.json", json.dumps(archived, indent=2) + "\n")
    ref = {
        "id": "file:" + PMID_FILE,
        "title": "Scoped publisher transport and strain evidence for PMID:21219457",
        "findings": [
            {
                "statement": "The sequenced gal cluster differs between KTGAL and KT2440 only in the GalT-restoring cytosine deletion; other cluster genes provide an exact sequence bridge, without establishing native KT2440 gallate uptake.",
                "supporting_text": "identical to that of the wild-type strain",
            }
        ],
        "reference_review": {
            "relevance": "HIGH",
            "correctness": "VERIFIED",
            "review_notes": "Bounded publisher Results excerpts and separate interpretation; acquisition URL, source lines190/229 and capture/excerpt hashes are in adjacent publisher-provenance.json. Original PMID cache remains abstract-only.",
        },
    }
    for path in PSEPK:
        text = before[path]["text"]
        doc = before[path]["document"]
        original = copy.deepcopy(
            next(r for r in doc["references"] if r["id"] == "PMID:21219457")
        )
        original["reference_review"]["review_notes"] += (
            " Reproducible transport and strain excerpts with acquisition hashes are recorded in file:"
            + PMID_FILE
            + "."
        )
        text = replace_ref(text, "PMID:21219457", original)
        local_ref = copy.deepcopy(ref)
        if path.endswith("/galP-ai-review.yaml"):
            local_ref["findings"].append(
                {
                    "statement": "At 10 micromolar gallate, galP disruption lowered whole-cell uptake from 7.4 to 4.2 nmol per minute per mg protein without abolishing growth; this is a KTGAL phenotype, not isolated-channel selectivity.",
                    "supporting_text": "uptake of 10\u2003µM GA",
                }
            )
            support = {
                "reference_id": "file:" + PMID_FILE,
                "supporting_text": "uptake of 10\u2003µM GA",
            }
            for term in ("GO:0015288", "GO:0055085"):
                row = copy.deepcopy(
                    next(
                        a
                        for a in doc["existing_annotations"]
                        if a["term"]["id"] == term
                    )
                )
                row["review"]["supported_by"].append(support)
                text = replace_annotation(text, term, row)
            a, b = top_section(text, "core_functions")
            core = copy.deepcopy(doc["core_functions"])
            core[0]["supported_by"].append(support)
            text = (
                text[:a]
                + "core_functions:\n"
                + yaml.safe_dump(core, sort_keys=False, allow_unicode=True, width=100)
                + text[b:]
            )
        text = append_ref(text, local_ref)
        yaml.safe_load(text)
        atomic(ROOT / path, text)
    path = CAND
    text = before[path]["text"]
    row = copy.deepcopy(
        next(
            a
            for a in before[path]["document"]["existing_annotations"]
            if a["term"]["id"] == "GO:0019748"
        )
    )
    row["review"]["action"] = "UNDECIDED"
    row["review"]["summary"] = (
        "The candidate gallate-pathway role does not resolve classification as secondary metabolism."
    )
    row["review"]["reason"] = (
        "GO:0019748 explicitly includes unicellular utilization and acquisition of unusual nutrients, so carbon-source catabolism does not demonstrate that this term is false. Family placement, gal-cluster context and native strain 383 growth support inferred participation in gallate catabolism, but do not independently resolve the secondary-metabolism classification or an ancestral gain/loss placement. GO:0019396 is not a descendant of GO:0019748; withdraw the unsupported lateral replacement and retain uncertainty on this original claim. The existing gallate-process core remains a qualified inference, with exact hydratase intermediate unresolved."
    )
    row["review"].pop("proposed_replacement_terms")
    row["review"]["supported_by"].append(
        {
            "reference_id": "file:" + ONTOLOGY,
            "supporting_text": "utilization and acquisition of unusual nutrients.",
        }
    )
    text = replace_annotation(text, "GO:0019748", row)
    text = append_ref(
        text,
        {
            "id": "file:" + ONTOLOGY,
            "title": "Archived official QuickGO definitions for the Burkholderia consultation",
            "findings": [
                {
                    "statement": "The secondary-metabolism definition permits unusual-nutrient utilization in unicellular organisms; it does not itself resolve this unassayed candidate's classification.",
                    "supporting_text": "utilization and acquisition of unusual nutrients.",
                }
            ],
        },
    )
    atomic(ROOT / path, text)
    text = before[LIGK]["text"]
    a = text.index("- question: Should GO split GO:0047443")
    b = text.index("  experts:", a)
    text = (
        text[:a]
        + "- question: Would a CHA-aldolase synonym or clearer label for GO:0047443 make its already-included CHA cleavage reaction easier to recognize without creating a redundant activity term?\n"
        + text[b:]
    )
    atomic(ROOT / LIGK, text)
    text = before[MOD]["text"]
    a = text.index(
        "    - order: 1\n      role: optional outer-membrane substrate entry"
    )
    b = text.index("    - order: 2\n", a)
    text = text[:a] + text[b:]
    a = text.index("    - source: gallate_outer_membrane_entry\n")
    b = text.index("    - source: gallate_dioxygenation\n", a)
    text = text[:a] + text[b:]
    text = text.replace(
        "RraA-like fold finally cleaves CHA to pyruvate and oxaloacetate. An\n  outer-membrane porin encoded with the pathway genes can optionally support\n  substrate entry. Upstream reactions",
        "RraA-like fold finally cleaves CHA to pyruvate and oxaloacetate. Envelope\n  transport by GalP and GalT is adjacent context; this intracellular reaction\n  module assumes gallate availability and does not model a complete uptake route. Upstream reactions",
    )
    text = text.replace("GalB, GalC, optional GalP porin)", "GalB, GalC)")
    a = text.index("  Boundary. GalP is optional")
    b = text.index("\n\n  Grounding.", a)
    text = (
        text[:a]
        + "  Boundary. The required mechanism begins with intracellular gallate and ends at pyruvate plus oxaloacetate.\n  Both GalP outer-membrane access and GalT inner-membrane transport remain adjacent context. The GalP review\n  is retained as a transport comparator, with KTGAL uptake contribution and unresolved isolated-channel selectivity.\n  Complete extracellular gallate utilization additionally requires compatible envelope delivery; no direct\n  GalP-to-cytoplasmic-dioxygenase delivery edge is asserted. GalR regulation, sphingomonad 3-O-methylgallate\n  routes (DesZ, LigAB, LigM O-demethylation), and metabolism of terminal products are also adjacent context.\n  The LigU/LigJ mechanism panel combines directly assayed KA1 LigU with SYK-6 enzymes. It demonstrates\n  compatible reaction chemistry, not a complete native gallate route in either strain. A same-strain SYK-6\n  LigU identity remains to be verified; no accession is inferred from the orf1 name alone."
        + text[b:]
    )
    text = text.replace("batch (PTHR34596, NCBIfam NF009904", "batch (NCBIfam NF009904")
    text = text.replace(
        "That batch also listed\n  the nicotinate-cluster porin NicP (Q88FY7) as a GalP-step representative; it is not adopted because NicP has no\n  role in gallate catabolism.",
        "The adjacent porin comparison distinguishes\n  gallate-cluster GalP from nicotinate-cluster NicP (Q88FY7); neither is a catalytic-module representative.",
    )
    text = text.replace(
        "      GalP remains optional. Inner-membrane uptake by KTGAL GalT is known but lies outside this module's\n      intracellular chemical boundary.",
        "      GalP and GalT are adjacent transport context outside the intracellular chemical boundary.\n      The model does not assert complete extracellular-to-cytoplasmic delivery.",
    )
    for pmid in ("31075306", "38064205"):
        start = text.index("  - id: PMID:" + pmid + "\n", text.index("references:\n"))
        end = text.index("\n  - id:", start + 1)
        block = text[start:end]
        assert block.count("relevance: HIGH") == 1
        text = (
            text[:start]
            + block.replace("relevance: HIGH", "relevance: MEDIUM")
            + text[end:]
        )
    # Module references use an indented sequence; keep existing entries verbatim.
    module_ref = copy.deepcopy(ref)
    module_ref["reference_review"]["relevance"] = "MEDIUM"
    module_ref["findings"].append(
        {
            "statement": "GalP whole-cell uptake contribution and GalT adaptation are transport context, not an additional intracellular reaction.",
            "supporting_text": "uptake of 10\u2003µM GA",
        }
    )
    a, b = top_section(text, "references")
    text = (
        text[:b]
        + "".join(
            "  " + line if line.strip() else line
            for line in yaml.safe_dump(
                [module_ref], sort_keys=False, allow_unicode=True, width=100
            ).splitlines(True)
        )
        + text[b:]
    )
    yaml.safe_load(text)
    atomic(ROOT / MOD, text)
    for path in NOTES:
        if path.startswith("modules/"):
            note = "This follow-up supersedes the earlier optional-entry boundary: GalP and GalT are both adjacent transport context. The removed optional GalP part and input edge are archived exactly in review-20261107/science-consultation/galp-model-archive.json. All intracellular parts and chemical connections are unchanged. The KA1/SYK-6 panel is explicitly synthetic, not proof of one native route. The production compiler still does not enforce reaction identity; the historical coverage checker and receipts are preserved and require an additive update for the six catalytic atoms. Publisher transport/strain evidence is now reproducible in review-20261107/publisher-evidence.md with separate hashed provenance."
        elif "BURL3" in path:
            note = "Family/domain and cluster evidence plus whole-strain growth support a qualified gallate-process core, not a target-specific pathway assay or exact intermediate assignment. An inferred core does not mandate a manufactured NEW annotation merely to remove a coverage warning. All three BURL3 candidates use this policy. C7570's original secondary-metabolism classification is now UNDECIDED because the GO definition permits unusual nutrients but target evidence does not resolve that classification; its prior lateral replacement was withdrawn. No new rows or loss claims were added."
        elif "/ligK/" in path:
            note = "Replace the obsolete GO0047443 split-term question with a synonym/label clarification: the official definition already includes CHA cleavage, and the redundant proposal remains retired. All original annotations and NEW lifecycle remain unchanged."
        else:
            note = (
                "The existing KTGAL-versus-KT2440 strain bridge now cites bounded publisher Results excerpts and acquisition hashes in "
                + PMID_FILE
                + ". GalP uptake is a whole-cell KTGAL contribution, not isolated-channel selectivity; GalT restoration does not demonstrate uptake by unadapted KT2440. No source annotation or action changed. GalP remains a reviewed comparator outside the intracellular chemical module."
            )
        atomic(
            ROOT / path,
            baseline["notes"][path]["text"].rstrip()
            + "\n\n## 2026-11-07 — PR6158 boundary and provenance follow-up\n\n"
            + note
            + "\n",
        )
    spec = importlib.util.spec_from_file_location(
        "history_helper", ROOT / "scripts/new_history.py"
    )
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    targets = CURATED + [p.replace("-notes.md", "-ai-review.yaml") for p in OTHER_NOTES]
    histories = []
    for path in targets:
        target = Path(path)
        args = (
            ["--kind", "module", "--slug", target.stem]
            if path.startswith("modules/")
            else [
                "--kind",
                "gene",
                "--organism",
                target.parts[1],
                "--slug",
                target.parts[2],
            ]
        )
        args += [
            "--actor-name",
            "codex",
            "--agent-tool",
            "codex",
            "--summary",
            "Clarify Gallate chemical boundary and evidence provenance",
            "--event",
            "EDIT",
            "--outcome",
            "changed",
            "--pr",
            "6158",
            "--details",
            "Bounded changes and exact supersessions are recorded in analysis/module_audits/bacterial_gallate_catabolism/review-20261107/science-consultation. Preserve original annotation payloads/NEW lifecycle and source caches; move GalP to adjacent context; withdraw unresolved C7570 lateral classification; retain explicit synthetic-panel and compiler limits. No render or full validation in this phase.",
        ]
        record, out = helper.build_record(helper.parse_args(args))
        assert not out.exists()
        atomic(ROOT / out, yaml.dump(record, sort_keys=False, allow_unicode=True))
        histories.append(str(out))
    atomic(HERE / "histories.json", json.dumps(histories, indent=2) + "\n")
    print(
        json.dumps(
            {
                "curated": len(CURATED),
                "notes": len(NOTES),
                "histories": len(histories),
                "protected": len(protected),
                "prior_artifacts": len(prior),
            }
        )
    )


if __name__ == "__main__":
    main()
