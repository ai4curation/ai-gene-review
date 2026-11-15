"""Bounded round-two corrections with atomic writes and a 256 MiB headroom floor."""

import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]
GENES = ["ECTOL/phaZ", "PSEPK/phaZ", "PSEAE/phaG", "ECTOL/phaC1", "ECTOL/phaC2"]
CURATED = [f"genes/{g}/{g.split('/')[1]}-ai-review.yaml" for g in GENES] + [
    "interpro/panther/PTHR43194/PTHR43194-review.yaml",
    "interpro/panther/PTHR43798/PTHR43798-review.yaml",
    "modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml",
]
NOTES = [f"genes/{g}/{g.split('/')[1]}-notes.md" for g in GENES]
HEAD = "a1f8a9620cd7877401982cae2e89135b2d5de0f4"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic(path, content):
    assert shutil.disk_usage(ROOT).free > 256 * 1024 * 1024, (
        "Headroom below authorized floor"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    data = content.encode() if isinstance(content, str) else content
    with tempfile.NamedTemporaryFile(
        dir=path.parent, prefix=".mcl-r2-", delete=False
    ) as stream:
        temporary = Path(stream.name)
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def replace_once(text, old, new):
    assert text.count(old) == 1, old[:100]
    return text.replace(old, new, 1)


def node_replace(text, node, term, **changes):
    start = text.index("- node_id: PANTHER:" + node + "\n")
    while (
        f"    id: GO:{term}\n"
        not in text[
            start : text.find("\n- node_id:", start + 1)
            if "\n- node_id:" in text[start + 1 :]
            else text.index("\nterm_assessments:", start)
        ]
    ):
        start = text.index("- node_id: PANTHER:" + node + "\n", start + 1)
    ends = [
        p
        for p in [
            text.find("\n- node_id:", start + 1),
            text.find("\nterm_assessments:", start + 1),
        ]
        if p >= 0
    ]
    end = min(ends)
    block = text[start:end]
    if "assessment" in changes:
        old = yaml.safe_load(block)[0]["assessment"]
        block = replace_once(
            block, "  assessment: " + old, "  assessment: " + changes["assessment"]
        )
    if "reason" in changes:
        a = block.index("  assessment_reason:")
        b = block.index("  supported_by:", a)
        block = (
            block[:a]
            + "  assessment_reason: >-\n    "
            + changes["reason"]
            + "\n"
            + block[b:]
        )
    if "support" in changes:
        block += changes["support"]
    return text[:start] + block + text[end:]


def main():
    assert (
        subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
        == HEAD
    )
    assert not (HERE / "baseline.json").exists()
    documents = {
        p: {
            "sha256": sha(ROOT / p),
            "text": (ROOT / p).read_text(),
            "document": yaml.safe_load((ROOT / p).read_text()),
        }
        for p in CURATED
    }
    old_artifacts = {
        str(p.relative_to(ROOT)): sha(p)
        for p in sorted(AUDIT.rglob("*"))
        if p.is_file() and HERE not in p.parents and "__pycache__" not in p.parts
    }
    protected = {}
    for gene in GENES:
        for p in (ROOT / "genes" / gene).iterdir():
            if (
                p.is_file()
                and str(p.relative_to(ROOT)) not in CURATED + NOTES
                and p.suffix != ".html"
            ):
                protected[str(p.relative_to(ROOT))] = sha(p)
    for family in ("PTHR43194", "PTHR43798"):
        for p in (ROOT / "interpro/panther" / family).iterdir():
            if p.is_file() and not p.name.endswith("-review.yaml"):
                protected[str(p.relative_to(ROOT))] = sha(p)
    for pmid in (
        "40434073",
        "20693992",
        "36689471",
        "17170116",
        "41055782",
        "10713430",
        "12200450",
    ):
        p = ROOT / "publications" / f"PMID_{pmid}.md"
        protected[str(p.relative_to(ROOT))] = sha(p)
    baseline = {
        "head": HEAD,
        "documents": documents,
        "notes": {
            p: {"sha256": sha(ROOT / p), "text": (ROOT / p).read_text()} for p in NOTES
        },
        "protected_sources": protected,
        "prior_audit_artifacts": old_artifacts,
    }
    atomic(HERE / "baseline.json", json.dumps(baseline, indent=2) + "\n")
    edits = {p: row["text"] for p, row in documents.items()}
    shared = (
        "The two family PAINT slices carry the same PTN000863140 hydrolase assertion and date. "
        "Retain positive hydrolase anchors including human EPHX2 P34913 and P. aeruginosa Q9HZR3. "
        "The ancestral node is absent from both available family reference trees, so its complete descendant scope is not independently resolved. "
        "An alpha/beta-hydrolase fold alone does not establish universal hydrolysis in transferase branches. "
        "UNRESOLVED concerns placement and extent, not denial of the seeded activities or a newly inferred loss."
    )
    for family in ("PTHR43194", "PTHR43798"):
        path = f"interpro/panther/{family}/{family}-review.yaml"
        edits[path] = node_replace(
            edits[path],
            "PTN000863140",
            "0016787",
            assessment="UNRESOLVED",
            reason=shared,
        )
    path = "interpro/panther/PTHR43194/PTHR43194-review.yaml"
    mf = (
        "The verified 17-leaf bacterial node includes BioH, PhaG, RhlA and RsbQ. BioH supplies positive pimelyl-ACP methyl ester hydrolysis evidence. "
        "PhaG acyl transfer and RsbQ signaling do not directly test this exact secondary substrate reaction. "
        "The Bacillus BioW route and PAO1 dedicated BioH requirement distinguish physiological pathway roles but do not constitute a purified RsbQ or PhaG methyl-ester negative. "
        "TOO_DEEP concerns ancestral gain placement; current topology and different roles do not independently establish that gain boundary. Retain UNRESOLVED without inventing a loss or a universal SF5 grant."
    )
    bp = (
        "The verified node includes BioH-positive proteins, PhaG/RhlA and Bacillus subtilis RsbQ O07015 in SF3. "
        "The review PMID40434073 identifies the Bacillus BioW route and absence of BioC/BioH; primary PMID20693992 tests Bacillus BioW in E. coli bioC/bioH deletion backgrounds. "
        "Together with native PAO1 BioH dependence in PMID36689471, these establish a physiological scope concern for transferring the BioH pathway role to PhaG or RsbQ. "
        "That BP boundary is distinct from possible secondary methyl-ester chemistry. The available evidence does not distinguish a later BioH gain from a lineage-specific change, and does not assay every SF3 member. "
        "Retain UNRESOLVED ancestral placement while explicitly preserving this pathway boundary; do not restore a categorical SF3 catalytic exclusion."
    )
    support = (
        "\n  - reference_id: PMID:40434073\n"
        "    supporting_text: B. subtilis lacks the genes encoding those proteins.\n"
        "  - reference_id: PMID:20693992\n"
        "    supporting_text: expression of the BioW pimeloyl-CoA synthetase of Bacillus subtilis in a ΔbioC ΔbioH strain\n"
    )
    edits[path] = node_replace(edits[path], "PTN002455972", "0090499", reason=mf)
    edits[path] = node_replace(
        edits[path], "PTN002455972", "0009102", reason=bp, support=support
    )
    references = (
        "- id: PMID:40434073\n"
        "  title: 'Fatty acid synthesis and utilization in gram-positive bacteria: insights from Bacillus subtilis.'\n"
        "- id: PMID:20693992\n  title: Biotin synthesis begins by hijacking the fatty acid synthetic pathway.\n"
    )
    edits[path] = replace_once(
        edits[path],
        "review_status: COMPLETE\n",
        references + "review_status: COMPLETE\n",
    )

    path = "genes/ECTOL/phaZ/phaZ-ai-review.yaml"
    start = edits[path].index("- term:\n    id: GO:0046464")
    end = edits[path].index("- term:\n    id: GO:0047372", start)
    block = edits[path][start:end]
    block = block.replace(
        "    action: MARK_AS_OVER_ANNOTATED\n", "    action: MODIFY\n", 1
    )
    a, b = block.index("    reason:"), block.index("    supported_by:")
    block = (
        block[:a]
        + (
            "    reason: >-\n"
            "      Native GPo1 genetics and complementation support intracellular PHA mobilization. PHA ester bonds lack a glycerol backbone, so the propagated acylglycerol process is not the demonstrated process. Laterally replace it with GO:0042620 to retain the supported polyester-metabolic participation already represented in the core. This does not claim a purified product distribution, native monoacylglycerol catabolism, or absence of secondary lipid chemistry.\n"
            "    proposed_replacement_terms:\n    - id: GO:0042620\n      label: poly(3-hydroxyalkanoate) metabolic process\n"
        )
        + block[b:]
    )
    edits[path] = edits[path][:start] + block + edits[path][end:]
    definition = (
        "Catalysis of the hydrolysis of ester bonds in medium-chain-length poly(3-hydroxyalkanoate),\n"
        "    yielding 3-hydroxyalkanoate monomers and oligomers."
    )
    for path in (
        "genes/ECTOL/phaZ/phaZ-ai-review.yaml",
        "genes/PSEPK/phaZ/phaZ-ai-review.yaml",
    ):
        marker = "- proposed_name: medium-chain-length poly(3-hydroxyalkanoate) depolymerase activity\n"
        a = edits[path].index("  proposed_definition:", edits[path].index(marker))
        b = edits[path].index("  justification:", a)
        edits[path] = (
            edits[path][:a]
            + "  proposed_definition: "
            + definition
            + "\n"
            + edits[path][b:]
        )
    path = "genes/PSEPK/phaZ/phaZ-ai-review.yaml"
    a = edits[path].index(
        "  justification:", edits[path].index("- proposed_name: medium-chain-length")
    )
    b = edits[path].index("  proposed_parent:", a)
    edits[path] = (
        edits[path][:a]
        + (
            "  justification: >-\n"
            "    GO:0050527 represents the supported hydroxyoctanoate reaction inferred from closely related KT2442 enzyme assays and resolved size-one/two products. Acceptance of additional aliphatic and aromatic mcl-PHA substrates does not make that narrower activity false. This broader proposal captures substrate scope not expressed by the C8 term; it is not an assertion that GO:0050527 is invalid. Pure-HO polymer testing and exact KT2442-to-KT2440 construct equivalence remain unestablished.\n"
        )
        + edits[path][b:]
    )
    for gene in ("phaC1", "phaC2"):
        path = f"genes/ECTOL/{gene}/{gene}-ai-review.yaml"
        old = f"    - reference_id: file:ECTOL/{gene}/{gene}-uniprot.txt\n"
        edits[path] = replace_once(
            edits[path], old, old + '      record_section: ["CC:FUNCTION"]\n'
        )
    path = "genes/PSEAE/phaG/phaG-ai-review.yaml"
    old = "      native forward kinetics or universal necessity follows.\n"
    addition = "      The untagged UniProt CC FUNCTION is not an independent PAO1 purified-activity measurement; the catalytic inference relies on sequence-linked PAO1 genetics and the explicitly homologous P. putida reverse-transfer assay in PMID12200450. Historical IC is preserved here as source payload; its evidence-code adjudication remains separate.\n"
    edits[path] = replace_once(edits[path], old, old + addition)
    path = "modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml"
    a = edits[path].index("  - gap_statement: GO0050527 specifies")
    b = edits[path].index("  - gap_statement:", a + 1)
    edits[path] = edits[path][:a] + edits[path][b:]
    for path, text in edits.items():
        assert text != documents[path]["text"], path
        yaml.safe_load(text)
        atomic(ROOT / path, text)
    notes = {
        "ECTOL/phaZ": "Laterally refine the propagated acylglycerol process row to GO0042620, supported by native GPo1 polyester turnover. Preserve source payload/order, membrane UNDECIDED and the secondary-MAG uncertainty. Normalize the existing proposed activity definition without asserting a purified GPo1 oligomer distribution.",
        "PSEPK/phaZ": "Clarify that the supported C8-specific GO0050527 inference and broader mcl-PHA proposal can coexist: broader substrate acceptance does not falsify the narrower reaction. Product-resolved LC-MS is attributed to PMID17170116 through its documented external full-text reading, not to PMID41055782. Exact strain/construct and pure-polymer limitations remain.",
        "PSEAE/phaG": "The untagged UniProt FUNCTION statement is not independent PAO1 purified-activity evidence. The catalytic inference rests on PAO1 genetics/identity plus the explicit P. putida reverse-transfer assay; historical NEW IC payload remains untouched, with code adjudication separately unresolved.",
        "ECTOL/phaC1": "Add CC:FUNCTION metadata to the existing curated UniProt quotation; no function, action, source text or ordered annotation payload changes.",
        "ECTOL/phaC2": "Add CC:FUNCTION metadata to the existing curated UniProt quotation; no function, action, source text or ordered annotation payload changes.",
    }
    for gene, note in notes.items():
        path = f"genes/{gene}/{gene.split('/')[1]}-notes.md"
        atomic(
            ROOT / path,
            baseline["notes"][path]["text"].rstrip()
            + "\n\n## 2026-11-07 — PR6194 second review follow-up\n\n"
            + note
            + "\n",
        )
    # Use the repository's exact history filename/session generator, atomically
    # persisting its returned record to obey this task's disk-write constraint.
    spec = importlib.util.spec_from_file_location(
        "repo_history_helper", ROOT / "scripts/new_history.py"
    )
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    histories = []
    for path in CURATED:
        target = Path(path)
        if path.startswith("genes/"):
            kind, organism, slug = "gene", target.parts[1], target.parts[2]
            args = ["--kind", kind, "--organism", organism, "--slug", slug]
        elif path.startswith("modules/"):
            args = ["--kind", "module", "--slug", target.stem]
        else:
            args = ["--kind", "other", "--slug", target.parent.name, "--path", path]
        args += [
            "--actor-name",
            "codex",
            "--agent-tool",
            "codex",
            "--event",
            "EDIT",
            "--outcome",
            "changed",
            "--summary",
            "Address bounded PR6194 second-review scientific consistency",
            "--pr",
            "6194",
            "--details",
            "Read-only review adjudication followed by scoped corrections documented in analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/review-followup/round2-implementation. Preserve ordered annotation payloads/NEW lifecycle and raw PAINT/source bytes. No invented loss, universal substrate grant or membrane-negative claim. No render or full validation in this phase.",
        ]
        record, generated_path = helper.build_record(helper.parse_args(args))
        assert not generated_path.exists()
        atomic(generated_path, yaml.dump(record, sort_keys=False, allow_unicode=True))
        histories.append(str(generated_path))
    atomic(HERE / "histories.json", json.dumps(histories, indent=2) + "\n")
    print(
        json.dumps(
            {
                "curated_files": len(CURATED),
                "notes": len(NOTES),
                "histories": len(histories),
                "headroom_bytes": shutil.disk_usage(ROOT).free,
            }
        )
    )


if __name__ == "__main__":
    main()
