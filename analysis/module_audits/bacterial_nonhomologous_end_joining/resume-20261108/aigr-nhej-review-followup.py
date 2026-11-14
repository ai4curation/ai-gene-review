from pathlib import Path
from copy import deepcopy
import yaml
import json
import hashlib

r = Path("analysis/module_audits/bacterial_nonhomologous_end_joining")
suc = r / "root-mku-endbinding-successor-20261107"
suc.mkdir(exist_ok=False)
p = Path("genes/MYCTU/mku/mku-ai-review.yaml")
before = p.read_bytes()
d = yaml.safe_load(before)
payloads = [
    {k: v for k, v in a.items() if k != "review"} for a in d["existing_annotations"]
]
base = deepcopy(d["core_functions"][0])
assert base["molecular_function"]["id"] == "GO:0003690"
base["molecular_function"] = {"id": "GO:0045027", "label": "DNA end binding"}
base["description"] = (
    "Recognition of exposed duplex DNA termini provides the end-specific Ku activity that recruits and organizes the end-joining machinery. The direct target evidence distinguishes linear duplex ends from closed circular duplex and single-stranded DNA."
)
d["core_functions"].insert(1, base)
for a in d["existing_annotations"]:
    if a["term"]["id"] == "GO:0003677":
        assert a["review"]["action"] == "MODIFY"
        a["review"]["proposed_replacement_terms"].append(
            {"id": "GO:0045027", "label": "DNA end binding"}
        )
        a["review"]["reason"] = (
            "Refine the true DNA-binding genus to both supported descendants: duplex DNA binding (GO:0003690) and DNA end binding (GO:0045027). These are sibling specificity claims, not an assumed ancestor relation. The primary-linked target biochemical statement distinguishes linear duplex ends from closed circular duplex and single-stranded DNA; no general single-stranded binding claim is inferred."
        )
assert [
    {k: v for k, v in a.items() if k != "review"} for a in d["existing_annotations"]
] == payloads
p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
(suc / "change.json").write_text(
    json.dumps(
        {
            "supersedes_review_hash_in": "myctu-review-20261107/handoff.json",
            "before_sha256": hashlib.sha256(before).hexdigest(),
            "after_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "changes": [
                "Add independently supported DNA-end-binding core, retaining duplex-binding core",
                "Refine DNA-binding genus to both supported sibling descendants",
            ],
            "ordered_payloads_preserved": len(payloads),
            "new_annotation_rows": 0,
            "validation_pending": True,
        },
        indent=2,
    )
    + "\n"
)
p = Path("genes/MYCTU/mku/mku-notes.md")
p.write_text(
    p.read_text()
    + "\n\n## 2026-11-07 — module conformance follow-up\n\nThe NHEJ module uses DNA end binding (GO:0045027). The target UniProt primary-linked statement distinguishes linear duplex ends from circular duplex DNA and ssDNA, supporting this specific core alongside duplex binding. Added the end-binding core and the second supported replacement for generic DNA binding; no annotation payload or raw source changed. The earlier consultation seal remains an immutable historical snapshot; root-mku-endbinding-successor-20261107 records the successor.\n"
)
p = Path("interpro/panther/PTHR42705/PTHR42705-review.yaml")
d = yaml.safe_load(p.read_text())
for n in d["node_assessments"]:
    if n["asserted_term"]["id"] == "GO:0006269":
        n["asserted_term"]["label"] = "DNA replication, synthesis of primer"
p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
p = Path("modules/bacterial_nonhomologous_end_joining.yaml")
d = yaml.safe_load(p.read_text())
d["evidence"][0]["statement"] = (
    "Defines DNA-end joining without a homologous repair template; this does not imply that POL nucleotide incorporation is template-independent."
)
s = (Path("publications") / "PMID_17938628.md").read_text()
meta = yaml.safe_load(s.split("---", 2)[1])
q = "an NHEJ system that depends on a dedicated DNA ligase, LigD, and the DNA-end-binding protein Ku"
assert " ".join(q.split()) in " ".join(s.split())
d["evidence"].append(
    {
        "source_id": "PMID:17938628",
        "title": meta["title"],
        "statement": "The accessible abstract of this historical review corroborates the Ku-LigD framework in mycobacteria and other genera; it is not used to assert universal bacterial presence or ancestry.",
        "supporting_text": q,
    }
)
d["module"]["parts"][1]["node"]["label"] = "Conditional Ku/LigD DNA-end processing"
d["module"]["knowledge_gaps"].append(
    {
        "gap_statement": "AP beta-elimination products depend on substrate geometry. A 3-prime phospho-alpha,beta-unsaturated aldehyde end is not equivalent to a simple 3-prime phosphate.",
        "boundary": "AP-lyase and ligase capacity alone does not establish repair of arbitrary AP-bearing ends. Test the experimentally supported short5-prime-overhang/recessed-end substrates separately from blocked3-prime-PUA products; do not assume PE phosphatase removes the aldehyde block.",
        "gap_kind": ["BIOLOGY"],
    }
)
lookup = {}
for org, gene in [
    ("PSEPK", "ku"),
    ("PSEPK", "ligD"),
    ("PSEAE", "ku"),
    ("PSEAE", "ligD"),
    ("MYCTU", "mku"),
    ("MYCTU", "ligD"),
    ("BACSU", "ku"),
    ("BACSU", "ligd"),
]:
    g = yaml.safe_load(
        (Path("genes") / org / gene / f"{gene}-ai-review.yaml").read_text()
    )
    lookup["UniProtKB:" + g["id"]] = (g["gene_symbol"], org)


def walk(x):
    if isinstance(x, dict):
        for member in x.get("representative_members", []):
            acc = member.get("term", {}).get("id")
            if acc in lookup:
                symbol, org = lookup[acc]
                member["preferred_term"] = f"{symbol} ({org})"
        for v in x.values():
            walk(v)
    elif isinstance(x, list):
        for v in x:
            walk(v)


walk(d)
p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
print("Wrote module/family follow-up and explicit mku successor")
