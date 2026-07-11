#!/usr/bin/env python3
"""First-pass curation for the PSEPK envelope/secreted protease QC split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_DIR = ROOT / "genes" / "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0004222": {"id": "GO:0004222", "label": "metalloendopeptidase activity"},
    "GO:0004252": {"id": "GO:0004252", "label": "serine-type endopeptidase activity"},
    "GO:0005509": {"id": "GO:0005509", "label": "calcium ion binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0005886": {"id": "GO:0005886", "label": "plasma membrane"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0008233": {"id": "GO:0008233", "label": "peptidase activity"},
    "GO:0008236": {"id": "GO:0008236", "label": "serine-type peptidase activity"},
    "GO:0008237": {"id": "GO:0008237", "label": "metallopeptidase activity"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0016020": {"id": "GO:0016020", "label": "membrane"},
    "GO:0016485": {"id": "GO:0016485", "label": "protein processing"},
    "GO:0042597": {"id": "GO:0042597", "label": "periplasmic space"},
    "GO:0046872": {"id": "GO:0046872", "label": "metal ion binding"},
    "GO:0080164": {"id": "GO:0080164", "label": "regulation of nitric oxide metabolic process"},
    "GO:0098552": {"id": "GO:0098552", "label": "side of membrane"},
}


DESCRIPTIONS = {
    "qmcA": "qmcA encodes a predicted membrane SPFH/band-7 stomatin-like protein; current evidence supports membrane localization but not a confident catalytic peptidase role.",
    "PP_0759": "PP_0759 encodes a signal-peptide-bearing M48-family membrane metalloendopeptidase candidate.",
    "pmbA": "pmbA encodes a cytosolic TldD/PmbA/U62-family regulatory metallopeptidase candidate.",
    "PP_1232": "PP_1232 encodes a periplasmic BepA-family M48 metalloprotease/chaperone candidate for beta-barrel outer-membrane protein quality control.",
    "PP_1499": "PP_1499 encodes a QEGLA/MATCAP-domain protein linked by annotation to flavohemoglobin and nitric-oxide metabolic regulation, with weak generic metallopeptidase evidence.",
    "PP_4113": "PP_4113 encodes a signal-peptide-bearing S8/S53-family serine endopeptidase candidate.",
    "PP_4924": "PP_4924 encodes a large membrane-associated S8 subtilase/furin-like serine endopeptidase candidate with calcium-binding repeats.",
    "PP_5112": "PP_5112 encodes a signal-peptide-bearing M16 processin-like metallopeptidase candidate.",
    "PP_5115": "PP_5115 encodes an M16-family zinc/metallopeptidase candidate.",
    "PP_5116": "PP_5116 encodes an M16-domain metalloprotease candidate with only metal-binding GOA evidence.",
    "PP_5455": "PP_5455 encodes a low-information M15A C-terminal-domain protein; current evidence does not establish an autonomous peptidase function.",
    "PP_5604": "PP_5604 encodes an S8-family subtilisin-like serine endopeptidase candidate.",
}


def lines(path: Path) -> list[str]:
    return path.read_text().splitlines()


def first(path: Path, contains: str) -> str | None:
    for line in lines(path):
        if contains in line:
            return line.rstrip()
    return None


def required(path: Path, contains: str) -> str:
    value = first(path, contains)
    if value is None:
        raise ValueError(f"Missing {contains!r} in {path}")
    return value


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def ref(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict], item: dict) -> None:
    if item not in items:
        items.append(item)


def accession(gene: str) -> str:
    return required(GENE_DIR / gene / f"{gene}-uniprot.txt", "AC   ").split()[1].rstrip(";")


def support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    refs: list[dict[str, str]] = []
    goa = GENE_DIR / gene / f"{gene}-goa.tsv"
    if term_id and goa.exists():
        refs.extend(ref(file_id(gene, "goa.tsv"), line.rstrip()) for line in lines(goa) if term_id in line)
    uni = GENE_DIR / gene / f"{gene}-uniprot.txt"
    patterns = []
    if term_id:
        patterns.append(f"DR   GO; {term_id};")
    patterns.extend([
        "DE   RecName:",
        "DE   SubName:",
        "CC   -!- FUNCTION:",
        "CC   -!- COFACTOR:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   PANTHER;",
        "DR   Pfam;",
        "DR   InterPro;",
        "FT   SIGNAL",
        "FT   TRANSMEM",
        "FT   ACT_SITE",
        "FT   BINDING",
        "FT   DOMAIN",
    ])
    for pattern in patterns:
        line = first(uni, pattern)
        if line:
            refs.append(ref(file_id(gene, "uniprot.txt"), line))
    asta = GENE_DIR / gene / f"{gene}-deep-research-asta.md"
    if asta.exists():
        for pattern in ["  uniprot_accession:", "  protein_description:", "  protein_family:", "  protein_domains:"]:
            line = first(asta, pattern)
            if line:
                refs.append(ref(file_id(gene, "deep-research-asta.md"), line))
    out: list[dict[str, str]] = []
    for item in refs:
        add_unique(out, item)
    return out


def load(gene: str) -> dict:
    return yaml.safe_load((GENE_DIR / gene / f"{gene}-ai-review.yaml").read_text())


def write(gene: str, data: dict) -> None:
    (GENE_DIR / gene / f"{gene}-ai-review.yaml").write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120)
    )


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    existing = {r["id"] for r in refs}
    for entry in [
        {"id": file_id(gene, "goa.tsv"), "title": f"QuickGO GOA annotations for {gene} ({accession(gene)})", "findings": []},
        {"id": file_id(gene, "uniprot.txt"), "title": f"UniProtKB entry for {gene} ({accession(gene)})", "findings": []},
        {"id": file_id(gene, "deep-research-asta.md"), "title": f"Asta retrieval report for {gene} ({accession(gene)})", "findings": []},
    ]:
        if entry["id"] not in existing and (GENE_DIR / gene / entry["id"].split("/")[-1]).exists():
            refs.append(entry)
            existing.add(entry["id"])


def finish(data: dict, gene: str) -> None:
    data["status"] = "DRAFT"
    data["description"] = DESCRIPTIONS[gene]
    data.setdefault("proposed_new_terms", [])
    data.setdefault("suggested_questions", [])
    data.setdefault("suggested_experiments", [])


def has(data: dict, term_id: str) -> bool:
    return any(a.get("term", {}).get("id") == term_id for a in data.get("existing_annotations") or [])


def set_review(data: dict, gene: str, term_id: str, action: str, summary: str) -> None:
    matched = False
    for ann in data.get("existing_annotations") or []:
        if ann.get("term", {}).get("id") == term_id:
            ann["review"] = {"summary": summary, "action": action, "supported_by": support(gene, term_id)}
            matched = True
    if not matched:
        raise ValueError(f"{gene} lacks expected term {term_id}")


def ensure_new(data: dict, gene: str, term_id: str, qualifier: str, summary: str, reason: str) -> None:
    if has(data, term_id):
        return
    data.setdefault("existing_annotations", []).append({
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "review": {"summary": summary, "action": "NEW", "reason": reason, "supported_by": support(gene, term_id)},
        "qualifier": qualifier,
    })


def core(desc: str, mf: str, processes: list[str] | None = None, locations: list[str] | None = None, refs: list[dict[str, str]] | None = None) -> dict:
    item = {"description": desc, "molecular_function": TERM[mf], "supported_by": refs or []}
    if processes:
        item["directly_involved_in"] = [TERM[p] for p in processes]
    if locations:
        item["locations"] = [TERM[l] for l in locations]
    return item


def base(gene: str) -> dict:
    data = load(gene)
    ensure_references(data, gene)
    finish(data, gene)
    return data


def curate_qmcA() -> None:
    gene = "qmcA"
    data = base(gene)
    for term in ["GO:0005886", "GO:0016020", "GO:0098552"]:
        if has(data, term):
            set_review(data, gene, term, "ACCEPT", "Membrane localization is consistent with SPFH/band-7 stomatin-like domain evidence.")
    data["core_functions"] = []
    data["suggested_questions"] = [{"question": "Does qmcA have a direct protease-related function, or is it an SPFH/band-7 membrane scaffold in KT2440?"}]
    write(gene, data)


def curate_m48(gene: str, bepA: bool = False) -> None:
    data = base(gene)
    set_review(data, gene, "GO:0004222", "ACCEPT", "M48-family metalloprotease domain evidence supports metalloendopeptidase activity.")
    for term in ["GO:0008233", "GO:0008237"]:
        if has(data, term):
            set_review(data, gene, term, "MARK_AS_OVER_ANNOTATED", "Correct but less informative than M48 metalloendopeptidase activity.")
    if has(data, "GO:0008270"):
        set_review(data, gene, "GO:0008270", "KEEP_AS_NON_CORE", "Zinc binding is cofactor context for the M48 metalloprotease.")
    if has(data, "GO:0046872"):
        set_review(data, gene, "GO:0046872", "KEEP_AS_NON_CORE", "Metal ion binding is cofactor context for the M48 metalloprotease.")
    if has(data, "GO:0006508"):
        set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context for the M48 metalloprotease.")
    if has(data, "GO:0051603"):
        set_review(data, gene, "GO:0051603", "KEEP_AS_NON_CORE", "This obsolete protein-catabolic-process child term is retained only as imported GOA context, not as authored core function.")
    for term in ["GO:0016020", "GO:0042597"]:
        if has(data, term):
            set_review(data, gene, term, "ACCEPT", "Membrane/periplasmic localization is consistent with the signal peptide and envelope M48 context.")
    locs = [t for t in ["GO:0016020", "GO:0042597"] if has(data, t)]
    processes = ["GO:0006508"] if has(data, "GO:0006508") else None
    data["core_functions"] = [
        core(
            "Envelope M48-family metalloendopeptidase activity" + (" with BepA beta-barrel assembly quality-control context." if bepA else "."),
            "GO:0004222",
            processes,
            locs or None,
            support(gene, "GO:0004222"),
        )
    ]
    if bepA:
        data["suggested_questions"] = [{"question": "Which outer-membrane beta-barrel substrates are quality-controlled by PP_1232/BepA in KT2440?"}]
    write(gene, data)


def curate_pmbA() -> None:
    gene = "pmbA"
    data = base(gene)
    for term in ["GO:0005737", "GO:0005829"]:
        if has(data, term):
            set_review(data, gene, term, "ACCEPT", "Cytoplasmic/cytosolic localization is consistent with PmbA/U62-family soluble protease context.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is conservative process context for PmbA/U62 metallopeptidase activity.")
    set_review(data, gene, "GO:0008237", "ACCEPT", "TldD/PmbA/U62-family evidence supports metallopeptidase activity.")
    locs = [t for t in ["GO:0005829", "GO:0005737"] if has(data, t)]
    data["core_functions"] = [core("Cytosolic PmbA/U62-family metallopeptidase activity.", "GO:0008237", ["GO:0006508"], locs or None, support(gene, "GO:0008237"))]
    write(gene, data)


def curate_pp1499() -> None:
    gene = "PP_1499"
    data = base(gene)
    set_review(data, gene, "GO:0080164", "ACCEPT", "The specific nitric-oxide metabolic regulation annotation matches the flavohemoglobin-expression-modulating product description.")
    ensure_new(data, gene, "GO:0008237", "enables", "Generic metallopeptidase activity is supported by UniProt protease/metalloprotease keywords and MATCAP/QEGLA domain context, but substrate specificity is unresolved.", "GOA returned only the process row for this protein.")
    ensure_new(data, gene, "GO:0006508", "involved_in", "Proteolysis is conservative context for the generic metallopeptidase annotation.", "GOA returned only the nitric-oxide regulatory process row.")
    data["core_functions"] = [core("QEGLA/MATCAP-domain metallopeptidase candidate with unresolved substrate specificity.", "GO:0008237", ["GO:0006508"], None, support(gene, "GO:0008237"))]
    data["suggested_questions"] = [{"question": "How does PP_1499 mechanistically modulate flavohemoglobin or nitric-oxide metabolism in KT2440?"}]
    write(gene, data)


def curate_s8(gene: str, large: bool = False) -> None:
    data = base(gene)
    set_review(data, gene, "GO:0004252", "ACCEPT", "S8/S53 subtilase-family evidence supports serine-type endopeptidase activity.")
    if has(data, "GO:0008236"):
        set_review(data, gene, "GO:0008236", "MARK_AS_OVER_ANNOTATED", "Correct broad serine-peptidase class but less informative than serine-type endopeptidase activity.")
    if has(data, "GO:0006508"):
        set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is appropriate process context for the S8-family protease.")
    if has(data, "GO:0016485"):
        set_review(data, gene, "GO:0016485", "ACCEPT", "Protein processing is plausible context for the large subtilase/furin-like enzyme.")
    if has(data, "GO:0005509"):
        set_review(data, gene, "GO:0005509", "KEEP_AS_NON_CORE", "Calcium binding is domain/cofactor context for the large subtilase.")
    if has(data, "GO:0016020"):
        set_review(data, gene, "GO:0016020", "ACCEPT", "Membrane localization is consistent with the predicted large secreted/membrane-associated subtilase.")
    processes = [t for t in ["GO:0006508", "GO:0016485"] if has(data, t)]
    locs = ["GO:0016020"] if has(data, "GO:0016020") else None
    data["core_functions"] = [core("S8/S53-family serine-type endopeptidase activity.", "GO:0004252", processes or None, locs, support(gene, "GO:0004252"))]
    if large:
        data["suggested_questions"] = [{"question": "What extracellular or membrane-associated substrate is processed by PP_4924 in KT2440?"}]
    write(gene, data)


def curate_m16(gene: str, signal: bool = False, weak: bool = False) -> None:
    data = base(gene)
    if has(data, "GO:0046872"):
        set_review(data, gene, "GO:0046872", "KEEP_AS_NON_CORE", "Metal binding is cofactor context for M16 metallopeptidase activity.")
    if has(data, "GO:0008237"):
        set_review(data, gene, "GO:0008237", "ACCEPT", "M16-family domains and UniProt metalloprotease evidence support metallopeptidase activity.")
    else:
        ensure_new(data, gene, "GO:0008237", "enables", "M16 peptidase product/domain evidence supports metallopeptidase activity.", "Fetched GOA contained only metal-binding context.")
    if has(data, "GO:0006508"):
        set_review(data, gene, "GO:0006508", "ACCEPT", "Proteolysis is conservative process context for M16 metallopeptidase activity.")
    else:
        ensure_new(data, gene, "GO:0006508", "involved_in", "Proteolysis is conservative process context for M16 metallopeptidase activity.", "Fetched GOA contained only metal-binding context.")
    data["core_functions"] = [core(("Signal-peptide-bearing " if signal else "") + "M16-family metallopeptidase activity.", "GO:0008237", ["GO:0006508"], None, support(gene, "GO:0008237"))]
    if weak:
        data["suggested_questions"] = [{"question": f"Does {gene} encode an active M16 metalloprotease and what is its physiological substrate?"}]
    write(gene, data)


def curate_pp5455() -> None:
    gene = "PP_5455"
    data = base(gene)
    data["core_functions"] = []
    data["suggested_questions"] = [{"question": "Does PP_5455 have an active peptidase role, or is it only a non-catalytic M15A C-terminal-domain protein?"}]
    write(gene, data)


def main() -> None:
    curate_qmcA()
    curate_m48("PP_0759")
    curate_pmbA()
    curate_m48("PP_1232", bepA=True)
    curate_pp1499()
    curate_s8("PP_4113")
    curate_s8("PP_4924", large=True)
    curate_m16("PP_5112", signal=True)
    curate_m16("PP_5115")
    curate_m16("PP_5116", weak=True)
    curate_pp5455()
    curate_s8("PP_5604")
    print("Curated periplasmic/membrane/secreted protease QC split")


if __name__ == "__main__":
    main()
