from pathlib import Path
import yaml
import re
import hashlib

R = Path("analysis/module_audits/bacterial_nonhomologous_end_joining/resume-20261108")
R.mkdir(exist_ok=True)
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
pa_old = "The primer extension and gap filling reactions were performed in the presence of 100 μ m dNTPs"
pa_new = "The kinetic profile of the 3-nucleotide gap filling with dNMPs highlighted the same themes, especially faster gap closure on the 5′-phosphate DNA"
bs_old = "57 nM BsuLigD and either 300 μM ddCTP, 10 μM dCTP or 10 μM CTP"
bs_new = "Altogether the results imply that BsuLigD fills the gap restoring the original (repaired) nucleotide"


def quote(n, q):
    s = (Path("publications") / f"PMID_{n}.md").read_text()
    assert " ".join(q.split()) in " ".join(s.split()), (n, q)
    return {"reference_id": "PMID:" + n, "supporting_text": q}


quote("20018881", pa_new)
quote("26826709", bs_new)
receipt = []
for org, gene in panel:
    p = Path("genes") / org / gene / f"{gene}-ai-review.yaml"
    before = p.read_bytes()
    d = yaml.safe_load(before)
    payloads = [
        {k: v for k, v in a.items() if k != "review"} for a in d["existing_annotations"]
    ]

    def clean(x):
        if isinstance(x, dict):
            if x.get("supporting_text") == pa_old:
                x["supporting_text"] = pa_new
            if x.get("supporting_text") == bs_old:
                x["supporting_text"] = bs_new
            if isinstance(x.get("supported_by"), list):
                x["supported_by"] = [
                    s
                    for s in x["supported_by"]
                    if not any(
                        t in s.get("supporting_text", "")
                        for t in ["synthesized by Genewiz", "polymerase buffer (50 mM"]
                    )
                ]
            for k, v in list(x.items()):
                if k in {
                    "reason",
                    "summary",
                    "description",
                    "statement",
                    "notes",
                } and isinstance(v, str):
                    x[k] = re.sub(r"\bGO(\d{7})\b(?![-_])", r"GO:\1", v)
                    x[k] = re.sub(r"\bPMID(\d+)\b(?![-_])", r"PMID:\1", x[k])
                else:
                    clean(v)
        elif isinstance(x, list):
            for y in x:
                clean(y)

    clean(d)
    changes = [
        "Replace functional methods-only quotes with result statements; retain construct provenance in reference findings and notes."
    ]
    if org == "MYCTU" and gene == "ligD":
        old_description = d["description"]
        d["description"] = (
            "LigD is a multifunctional DNA double-strand-break repair enzyme of Mycobacterium tuberculosis H37Rv. Its polymerase, phosphoesterase and ATP-dependent ligase modules remodel and seal DNA ends in cooperation with Ku. The polymerase binds broken-end intermediates, supports end synapsis and extends DNA across a break using deoxyribonucleotides or ribonucleotides. Its RNA-synthesis activity can also initiate short primers on single-stranded DNA templates. The phosphoesterase and ligase modules provide complementary end-healing and strand-sealing activities."
        )
        for a in d["existing_annotations"]:
            if a["term"]["id"] == "GO:0000287":
                a["review"].update(
                    action="UNDECIDED",
                    summary="The curated magnesium-binding assignment cannot be independently resolved from the accessible primary text.",
                    reason="The two original IDA assertions are retained unchanged as source claims. Accessible abstracts establish metal-dependent LigD chemistry but do not identify the metal as magnesium, and the curated UniProt cofactor statement concerns manganese. A magnesium-containing assay buffer and a CDC1551 construct-synthesis statement do not establish magnesium binding by the H37Rv target. The relevant full-text metal evidence was not recovered; use UNDECIDED rather than infer the ion identity or reject the curator.",
                )
                a["review"].pop("supported_by", None)
        changes.append(
            "Move construct-specific commentary into notes and mark unresolved magnesium evidence UNDECIDED without altering the two source IDA rows."
        )
    elif org == "MYCTU" and gene == "mku":
        old_description = d["description"]
        d["description"] = (
            "Mku is the homodimeric DNA-end-binding factor of the Mycobacterium tuberculosis H37Rv nonhomologous end-joining system. It recognizes exposed double-stranded DNA termini, recruits LigD and stimulates ligation of broken ends. Mku also associates with UvrD1 in a DNA-unwinding complex; UvrD1 supplies the helicase activity. These interactions organize the processing and joining of DNA breaks."
        )
        d["core_functions"] = [
            x
            for x in d["core_functions"]
            if x.get("molecular_function", {}).get("id") != "GO:0003690"
        ]
        assert (
            sum(
                x.get("molecular_function", {}).get("id") == "GO:0045027"
                for x in d["core_functions"]
            )
            == 1
        )
        changes.append(
            "Use the demonstrated DNA-end-binding activity as the Ku recognition core and retain duplex-binding annotation rows."
        )
    else:
        old_description = None
    if (org, gene) in [("BACSU", "ku"), ("PSEAE", "ku"), ("PSEAE", "ligD")]:
        for c in d["core_functions"]:
            if c.get("molecular_function", {}).get("id") in [
                "GO:0140078",
                "GO:0051575",
            ]:
                c.pop("directly_involved_in", None)
                c["description"] = (
                    c["description"].split(";")[0].rstrip(".")
                    + ". This measured substrate-dependent chemistry is not assigned a general native NHEJ or base-excision-repair role."
                )
        changes.append(
            "Separate measured AP/dRP lyase capabilities from unproven native process assignments."
        )
    if org == "PSEAE" and gene == "ku":
        for a in d["existing_annotations"]:
            if a["review"].get("summary", "").strip() == "P.":
                a["review"]["summary"] = (
                    "Ku promotes DNA-end joining by recruiting LigD and stimulating its ligation activity."
                )
    if org == "PSEPK" and gene == "ku":
        row = next(
            a for a in d["existing_annotations"] if a["term"]["id"] == "GO:0006303"
        )
        sources = [
            quote(
                "12215643",
                "bacterial Ku specifically recruits DNA ligase to DNA ends and stimulates DNA ligation.",
            ),
            quote(
                "25942369",
                "Both the absence of LigD or Ku resulted in characteristic spectra of stationary-phase mutations that differed from each other and also from the wild-type spectrum.",
            ),
            quote(
                "36475478",
                "we investigated the effect of removal or overproduction of NHEJ-associated P. putida KT2440 enzymes on mutations generated upon repair of Cas9-mediated DSBs",
            ),
        ]
        row["review"]["supported_by"].extend(sources)
        row["review"]["reason"] += (
            " PMID:12215643 supports conserved bacterial recruitment, not a native KT2440 assay. PMID:25942369 supplies P. putida mutation-spectrum evidence and explicitly allows Ku- and LigD-independent pathways. PMID:36475478 reports native KT2440 perturbations; the recovered English full text gives the locus-specific dependence. The earlier secondary deep-research statement is superseded by these bounded primary findings."
        )
        for n in ["12215643", "25942369", "36475478"]:
            if not any(x["id"] == "PMID:" + n for x in d["references"]):
                meta = yaml.safe_load(
                    (Path("publications") / f"PMID_{n}.md")
                    .read_text()
                    .split("---", 2)[1]
                )
                d["references"].append({"id": "PMID:" + n, "title": meta["title"]})
        changes.append(
            "Restore and distinguish three primary sources behind the original NHEJ assessment; retain the newer native-pathway limits."
        )
    for a in d["existing_annotations"]:
        if a.get("retired") and a["review"]["action"] == "NEW":
            a["review"]["summary"] = (
                "Supported biological claim retained as an inactive historical proposal because the existing-row refinement already represents it."
            )
            if a["term"]["id"] == "GO:0045027":
                a["review"]["reason"] = (
                    "Linear duplex-end recognition is supported by the target HAMAP statement and characterized bacterial Ku proteins. The generic DNA-binding row already proposes this same supported end-binding term. This historical authored proposal is therefore retired to avoid an additional redundant assertion; retirement does not mean the activity is false. Its source payload remains intact."
                )
            else:
                a["review"]["reason"] = (
                    "The target LigD domain architecture and bacterial end-joining biochemistry support the NHEJ function, while native KT2440 repair can proceed without LigD at the tested sites. Existing DNA-repair and recombination rows already refine to this process. Retire this historical authored proposal to avoid a duplicate assertion, while retaining its source payload and the limits of the native evidence."
                )
    assert [
        {k: v for k, v in a.items() if k != "review"} for a in d["existing_annotations"]
    ] == payloads, (org, gene)
    p.write_text(yaml.safe_dump(d, sort_keys=False, width=100, allow_unicode=True))
    notes = p.with_name(gene + "-notes.md")
    s = notes.read_text()
    s = re.sub(r"\bGO(\d{7})\b(?![-_])", r"GO:\1", s)
    s = re.sub(r"\bPMID(\d+)\b(?![-_])", r"PMID:\1", s)
    s += (
        "\n\n## 2026-11-08 — recovery PR review follow-up\n\n"
        + " ".join(changes)
        + " Original annotation payloads and raw-source files remain unchanged.\n"
    )
    if old_description:
        s += (
            "\nConstruct and assay context retained from the prior description: "
            + old_description
            + "\n"
        )
    notes.write_text(s)
    receipt.append(
        {
            "gene": org + "/" + gene,
            "before_sha256": hashlib.sha256(before).hexdigest(),
            "after_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "ordered_payloads_preserved": len(payloads),
            "changes": changes,
        }
    )
# Workflow constraints are not biological knowledge gaps.
p = Path("modules/bacterial_nonhomologous_end_joining.yaml")
d = yaml.safe_load(p.read_text())
gaps = d["module"].get("knowledge_gaps", [])
d["module"]["knowledge_gaps"] = [
    x
    for x in gaps
    if not x["gap_statement"].startswith("Family membership does not establish")
]
for x in gaps:
    if x["gap_statement"].startswith("Family membership does not establish"):
        d["notes"] += " " + x["gap_statement"] + " " + x["boundary"]
p.write_text(yaml.safe_dump(d, sort_keys=False, width=100, allow_unicode=True))
(R / "review-followup.yaml").write_text(
    yaml.safe_dump(
        {
            "pr": 6205,
            "genes": receipt,
            "limitations": [
                "Full-corpus validation and renewed scientific review remain pending.",
                "Original retired NEW payloads remain inactive; no duplicate active annotation was added.",
            ],
        },
        sort_keys=False,
    )
)
print("Updated eight reviews; all ordered annotation payloads preserved.")
