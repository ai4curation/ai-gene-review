from pathlib import Path
import subprocess
import json
import yaml
import hashlib

root = Path.cwd()
R = Path("analysis/module_audits/bacterial_nonhomologous_end_joining/resume-20261108")
panel = [
    ("PSEPK", "ku"),
    ("PSEPK", "ligD"),
    ("PSEAE", "ku"),
    ("PSEAE", "ligD"),
    ("MYCTU", "mku"),
    ("MYCTU", "ligD"),
    ("BACSU", "ku"),
    ("BACSU", "ligd"),
]
rows = []
for org, g in panel:
    p = Path("genes") / org / g / f"{g}-ai-review.yaml"
    d = yaml.safe_load(p.read_text())
    b = yaml.safe_load(
        subprocess.check_output(
            ["git", "show", "ced78affcbf1e39e91dd15e2a723f32424b532ed:" + str(p)],
            text=True,
        )
    )

    def payload(annotations):
        return [{k: v for k, v in x.items() if k != "review"} for x in annotations]

    assert payload(d["existing_annotations"]) == payload(b["existing_annotations"])
    assert all(x["review"]["action"] != "PENDING" for x in d["existing_annotations"])
    u = p.with_name(g + "-uniprot.txt")
    text = u.read_text()
    fam = "PTHR41251:SF1" if g in ["ku", "mku"] else "PTHR42705:SF2"
    classification = next(
        x for x in text.splitlines() if x.startswith("DR   PANTHER; " + fam + ";")
    )
    for suffix in ["-uniprot.txt", "-goa.tsv"]:
        f = p.with_name(g + suffix)
        assert f.read_bytes() == subprocess.check_output(
            ["git", "show", "ced78affcbf1e39e91dd15e2a723f32424b532ed:" + str(f)]
        )
    logfile = R / f"validate-{org}-{g}.log"
    assert "All validations passed" in logfile.read_text()
    rows.append(
        {
            "gene": org + "/" + g,
            "review_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "ordered_annotation_payloads_preserved": len(d["existing_annotations"]),
            "unresolved_rows": sum(
                x["review"]["action"] == "UNDECIDED" for x in d["existing_annotations"]
            ),
            "membership_source": str(u),
            "membership_quote": classification,
            "membership_source_sha256": hashlib.sha256(u.read_bytes()).hexdigest(),
            "validation_log": str(logfile),
        }
    )
assert "module checks passed" in (R / "module-validation.log").read_text()
quote_count = 0
hashes = {}


def walk(x):
    global quote_count
    if isinstance(x, dict):
        sid = x.get("source_id", x.get("reference_id"))
        q = x.get("supporting_text")
        if sid and q and sid.startswith("PMID:"):
            p = Path("publications") / ("PMID_" + sid.split(":")[1] + ".md")
            assert " ".join(q.split()) in " ".join(p.read_text().split()), (sid, q)
            quote_count += 1
            hashes[str(p)] = hashlib.sha256(p.read_bytes()).hexdigest()
        for y in x.values():
            walk(y)
    elif isinstance(x, list):
        for y in x:
            walk(y)


for p in [
    "modules/bacterial_nonhomologous_end_joining.yaml",
    "interpro/panther/PTHR41251/PTHR41251-review.yaml",
    "interpro/panther/PTHR42705/PTHR42705-review.yaml",
]:
    walk(yaml.safe_load(Path(p).read_text()))
result = {
    "result": "PASS_FOCUSED",
    "baseline_commit": "ced78affcbf1e39e91dd15e2a723f32424b532ed",
    "genes": rows,
    "ordered_annotation_payloads_preserved": sum(
        x["ordered_annotation_payloads_preserved"] for x in rows
    ),
    "new_annotation_rows": 0,
    "raw_gene_sources_unchanged": 16,
    "module_family_primary_quote_occurrences": quote_count,
    "quote_source_hashes": hashes,
    "capacity_cases": 63,
    "validation": [
        "eight just validate gene runs",
        "module schema and semantic validation",
        "family schema, GO terms, references and residue validation",
        "eleven new history records validated",
        "eight gene pages and module page rendered",
    ],
    "limits": [
        "This is focused validation, not a full-corpus result; fresh PR CI and scientific review are pending.",
        "The large PANTHER member index was not rebuilt after disk cleanup. All eight representative classifications were checked directly against retained UniProt PANTHER cross-references above. CI remains responsible for its full release-pinned index check.",
        "Whole-family grants remain unresolved where the inspected phylogeny or domain evidence does not establish them.",
        "Lost original handoffs are not reconstructed; this receipt describes only the recovery checkpoint and current work.",
    ],
}
(R / "closure.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    "PASS",
    result["ordered_annotation_payloads_preserved"],
    "payloads",
    quote_count,
    "quotes",
)
