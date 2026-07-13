#!/usr/bin/env python3
"""First-pass curation for pyoverdine NRPS genes mis-bucketed by "non-ribosomal"."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "siderophore_biosynthesis_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_nonribosomal_peptide_synthetase_spillovers.tsv"
)


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0002049": {"id": "GO:0002049", "label": "pyoverdine biosynthetic process"},
    "GO:0003824": {"id": "GO:0003824", "label": "catalytic activity"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0008610": {"id": "GO:0008610", "label": "lipid biosynthetic process"},
    "GO:0009239": {"id": "GO:0009239", "label": "enterobactin biosynthetic process"},
    "GO:0009366": {"id": "GO:0009366", "label": "enterobactin synthetase complex"},
    "GO:0019290": {"id": "GO:0019290", "label": "siderophore biosynthetic process"},
    "GO:0031177": {"id": "GO:0031177", "label": "phosphopantetheine binding"},
    "GO:0043041": {
        "id": "GO:0043041",
        "label": "amino acid activation for nonribosomal peptide biosynthetic process",
    },
    "GO:0044550": {"id": "GO:0044550", "label": "secondary metabolite biosynthetic process"},
    "GO:0047527": {"id": "GO:0047527", "label": "2,3-dihydroxybenzoate-serine ligase activity"},
    "GO:0071766": {"id": "GO:0071766", "label": "Actinobacterium-type cell wall biogenesis"},
    "GO:0097429": {
        "id": "GO:0097429",
        "label": "amino acid ligation activity by nonribosomal peptide synthase",
    },
    "GO:0140414": {
        "id": "GO:0140414",
        "label": "phosphopantetheine-dependent carrier activity",
    },
    "GO:1904091": {"id": "GO:1904091", "label": "non-ribosomal peptide synthetase activity"},
}


GENE_INFO = {
    "pvdJ": {
        "accession": "Q88F78",
        "aliases": ["PP_4220"],
        "description": (
            "pvdJ encodes a large non-ribosomal peptide synthetase subunit "
            "of ferribactin/pyoverdine assembly in Pseudomonas putida KT2440. The "
            "protein has repeated adenylation, condensation, and phosphopantetheine "
            "carrier domains and is best interpreted as part of the pyoverdine "
            "siderophore assembly line rather than a translation factor."
        ),
        "locations": [],
        "questions": [
            "Which amino acid substrate is selected by each KT2440 PvdJ adenylation module?",
            "Does KT2440 PvdJ form a stable assembly with PvdL, PvdI, and PvdD or a transient NRPS handoff complex?",
        ],
    },
    "pvdI": {
        "accession": "Q88F77",
        "aliases": ["PP_4221"],
        "description": (
            "pvdI encodes a cytosolic multimodular non-ribosomal peptide synthetase "
            "subunit of ferribactin/pyoverdine assembly in Pseudomonas putida KT2440. "
            "Its adenylation, condensation, and phosphopantetheine carrier domains "
            "support pyoverdine siderophore peptide assembly, while enterobactin "
            "annotations are over-transfers from other NRPS systems."
        ),
        "locations": ["GO:0005829"],
        "questions": [
            "Which residues are incorporated by the KT2440 PvdI modules?",
            "How does PvdI physically coordinate with PvdL, PvdJ, and PvdD during ferribactin/pyoverdine precursor assembly?",
        ],
    },
    "pvdL": {
        "accession": "Q88F56",
        "aliases": ["PP_4243"],
        "description": (
            "pvdL encodes a very large non-ribosomal peptide synthetase subunit of "
            "ferribactin/pyoverdine assembly in Pseudomonas putida KT2440. Its "
            "multiple adenylation, condensation, and phosphopantetheine carrier "
            "domains, plus an FAAL/FAAC-like region, support an initiation/assembly "
            "role in pyoverdine siderophore biosynthesis rather than lipid "
            "biosynthesis or Actinobacterium-type cell-wall biogenesis."
        ),
        "locations": [],
        "questions": [
            "What starter unit and amino acid substrates are selected by the KT2440 PvdL modules?",
            "Is KT2440 PvdL membrane-associated like the P. aeruginosa PvdL assembly hub, and does that organization control handoff to PvdI, PvdJ, and PvdD?",
        ],
    },
}


FALCON_REF = "file:PSEPK/pvdD/pvdD-deep-research-falcon.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def lines(path: Path) -> list[str]:
    return read_text(path).splitlines()


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def falcon_text(*needles: str) -> str | None:
    return optional_first_line(ROOT / "genes" / "PSEPK" / "pvdD" / "pvdD-deep-research-falcon.md", *needles)


def product_line(gene: str) -> str | None:
    return optional_first_line(gene_file(gene, "uniprot.txt"), "DE   SubName:")


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    uniprot = gene_file(gene, "uniprot.txt")
    goa = gene_file(gene, "goa.tsv")
    asta = gene_file(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    if term_id and goa.exists():
        for line in lines(goa):
            if term_id in line:
                add_unique(items, support(file_id(gene, "goa.tsv"), line))
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    for marker in (
        "DR   InterPro; IPR010071; AA_adenyl_dom.",
        "DR   InterPro; IPR001242; Condensation_dom.",
        "DR   InterPro; IPR010060; NRPS_synth.",
        "DR   InterPro; IPR020806; PKS_PP-bd.",
        "DR   InterPro; IPR006162; Ppantetheine_attach_site.",
        "DR   InterPro; IPR040097; FAAL/FAAC.",
        "DR   Pfam; PF00501; AMP-binding;",
        "DR   Pfam; PF00668; Condensation;",
        "DR   Pfam; PF00550; PP-binding;",
        "KW   Phosphopantetheine",
    ):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(uniprot, marker)))
    for marker in (
        "  protein_description:",
        "  protein_family:",
        "  protein_domains:",
    ):
        add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, marker)))
    add_unique(items, support(FALCON_REF, falcon_text("PvdL/PvdI/PvdJ/PvdD in canonical systems")))
    add_unique(items, support(FALCON_REF, falcon_text("NRPSs are large modular enzymes")))
    add_unique(items, support(FALCON_REF, falcon_text("Pyoverdine synthesis begins in the cytoplasm")))
    add_unique(items, support(FALCON_REF, falcon_text("PvdI/PvdJ/PvdD explore the cytoplasm")))
    return items


def replacement(term_id: str, label: str | None = None) -> dict[str, str]:
    if label:
        return {"id": term_id, "label": label}
    return TERM[term_id]


def review_for(gene: str, term_id: str) -> dict:
    if term_id == "GO:0003824":
        return {
            "summary": "True only in an uninformative sense; this NRPS subunit is better captured by non-ribosomal peptide synthetase activity.",
            "action": "MODIFY",
            "reason": (
                f"{gene} is annotated in UniProt as a non-ribosomal peptide synthetase/ferribactin synthase subunit "
                "with AMP-binding, condensation, and carrier-domain signatures. The pyoverdine pathway synthesis "
                "evidence supports a specific NRPS activity rather than generic catalytic activity."
            ),
            "supported_by": evidence_for(gene, term_id),
            "proposed_replacement_terms": [replacement("GO:1904091")],
        }
    if term_id == "GO:0005737":
        return {
            "summary": "Broad but directionally correct localization for a soluble bacterial NRPS; cytosol is preferred and already present.",
            "action": "MODIFY",
            "reason": (
                "The pyoverdine NRPS assembly stage is cytoplasmic. Because the review also has a cytosol row, "
                "the broader cytoplasm term should be replaced by GO:0005829."
            ),
            "supported_by": evidence_for(gene, term_id),
            "proposed_replacement_terms": [replacement("GO:0005829")],
        }
    if term_id == "GO:0005829":
        return {
            "summary": "Appropriate localization for a pyoverdine NRPS subunit acting during cytoplasmic precursor assembly.",
            "action": "ACCEPT",
            "reason": "Pyoverdine synthesis begins in the cytoplasm, and homologous imaging evidence places PvdI/PvdJ/PvdD in the cytoplasm.",
            "supported_by": evidence_for(gene, term_id),
        }
    if term_id == "GO:0009239":
        return {
            "summary": "Incorrect specific siderophore family. This gene belongs to pyoverdine/ferribactin assembly, not enterobactin biosynthesis.",
            "action": "MODIFY",
            "reason": (
                f"{gene} is a ferribactin/pyoverdine NRPS-family subunit in KT2440. The enterobactin process term is an "
                "over-transfer from another siderophore NRPS system; the appropriate specific process is pyoverdine biosynthesis."
            ),
            "supported_by": evidence_for(gene, term_id),
            "proposed_replacement_terms": [replacement("GO:0002049")],
        }
    if term_id == "GO:0009366":
        return {
            "summary": "Incorrect complex term. Pyoverdine NRPSs are not the enterobactin synthetase complex.",
            "action": "REMOVE",
            "reason": (
                "The local evidence supports a pyoverdine/ferribactin NRPS assembly line. GO lacks a pyoverdine-specific "
                "synthetase complex term, so the enterobactin-specific complex should be removed rather than generalized."
            ),
            "supported_by": evidence_for(gene, term_id),
        }
    if term_id == "GO:0031177":
        return {
            "summary": "Directionally correct but under-specific for the carrier-domain chemistry of NRPS proteins.",
            "action": "MODIFY",
            "reason": (
                f"{gene} has phosphopantetheine carrier-domain evidence. The functional carrier-activity term better "
                "captures thiotemplate intermediate tethering than generic phosphopantetheine binding."
            ),
            "supported_by": evidence_for(gene, term_id),
            "proposed_replacement_terms": [replacement("GO:0140414")],
        }
    if term_id == "GO:0043041":
        return {
            "summary": "Accurate but sub-process-level context for adenylation modules within NRPS catalysis.",
            "action": "KEEP_AS_NON_CORE",
            "reason": (
                "Amino acid activation is part of the NRPS thiotemplate mechanism, but the core biological process for "
                f"{gene} is ferribactin/pyoverdine siderophore assembly."
            ),
            "supported_by": evidence_for(gene, term_id),
        }
    if term_id == "GO:0044550":
        return {
            "summary": "Too broad for a pyoverdine siderophore NRPS subunit.",
            "action": "MODIFY",
            "reason": (
                f"{gene} is better represented by siderophore/pyoverdine biosynthetic process terms. Broad secondary "
                "metabolite biosynthesis obscures the specific pathway context."
            ),
            "supported_by": evidence_for(gene, term_id),
            "proposed_replacement_terms": [replacement("GO:0019290")],
        }
    if term_id == "GO:0047527":
        return {
            "summary": "Wrong substrate/product and wrong siderophore family; this is an enterobactin/EntF-like over-transfer.",
            "action": "MODIFY",
            "reason": (
                f"{gene} is a ferribactin/pyoverdine NRPS subunit, not a 2,3-dihydroxybenzoate-serine ligase for "
                "enterobactin. The appropriate molecular function is a general NRPS amino acid ligation activity."
            ),
            "supported_by": evidence_for(gene, term_id),
            "proposed_replacement_terms": [replacement("GO:0097429")],
        }
    if term_id == "GO:0008610":
        return {
            "summary": "Misleading process call. PvdL may use fatty-acyl starter chemistry, but the product pathway is pyoverdine siderophore biosynthesis.",
            "action": "MODIFY",
            "reason": (
                "The FAAL/FAAC-like region does not make pvdL a lipid-biosynthesis gene in this context. Its product name "
                "and NRPS architecture support ferribactin/pyoverdine assembly."
            ),
            "supported_by": evidence_for(gene, term_id),
            "proposed_replacement_terms": [replacement("GO:0002049")],
        }
    if term_id == "GO:0071766":
        return {
            "summary": "Incorrect taxonomic/pathway transfer for a Pseudomonas pyoverdine NRPS subunit.",
            "action": "REMOVE",
            "reason": (
                "Actinobacterium-type cell wall biogenesis is not a supported process for P. putida KT2440 pvdL. "
                "The local evidence points to ferribactin/pyoverdine assembly, not an Actinobacterium-type cell wall route."
            ),
            "supported_by": evidence_for(gene, term_id),
        }
    if term_id == "GO:0002049":
        return {
            "summary": "Pyoverdine biosynthesis is added as the specific pathway context for this ferribactin/pyoverdine NRPS subunit.",
            "action": "NEW",
            "reason": (
                f"{gene} has a ferribactin synthase/pyoverdine NRPS product identity and domain architecture, while the "
                "pathway-level pyoverdine NRPS evidence places PvdL/PvdI/PvdJ/PvdD in pyoverdine precursor assembly."
            ),
            "supported_by": evidence_for(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def has(data: dict, term_id: str) -> bool:
    return any(row.get("term", {}).get("id") == term_id for row in data.get("existing_annotations", []))


def ensure_new(data: dict, gene: str, term_id: str, qualifier: str) -> None:
    if has(data, term_id):
        return
    data.setdefault("existing_annotations", []).append(
        {
            "term": TERM[term_id],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": qualifier,
            "review": review_for(gene, term_id),
        }
    )


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    seen = {ref.get("id") for ref in refs}
    for ref_id, title in [
        (file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene} ({GENE_INFO[gene]['accession']})"),
        (file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene} ({GENE_INFO[gene]['accession']})"),
        (file_id(gene, "deep-research-asta.md"), f"Asta retrieval report for {gene} ({GENE_INFO[gene]['accession']})"),
        (
            FALCON_REF,
            "Falcon deep research report for pvdD and pyoverdine NRPS pathway context",
        ),
    ]:
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)


def core_functions_for(gene: str) -> list[dict]:
    core = [
        {
            "description": (
                "Multimodular non-ribosomal peptide synthetase activity used in ferribactin/pyoverdine "
                "siderophore precursor assembly"
            ),
            "molecular_function": TERM["GO:1904091"],
            "directly_involved_in": [TERM["GO:0002049"], TERM["GO:0019290"]],
            "supported_by": evidence_for(gene, "GO:0003824"),
        },
        {
            "description": (
                "Phosphopantetheine-dependent carrier-domain activity that tethers pathway intermediates "
                "during NRPS assembly"
            ),
            "molecular_function": TERM["GO:0140414"],
            "directly_involved_in": [TERM["GO:0002049"]],
            "supported_by": evidence_for(gene, "GO:0031177"),
        },
    ]
    locations = [TERM[term_id] for term_id in GENE_INFO[gene]["locations"]]
    if locations:
        for item in core:
            item["locations"] = locations
    return core


def curate_gene(gene: str) -> None:
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(read_text(path))
    data["status"] = "DRAFT"
    data["aliases"] = GENE_INFO[gene]["aliases"]
    data["description"] = GENE_INFO[gene]["description"]
    ensure_references(data, gene)
    for row in data.setdefault("existing_annotations", []):
        row["review"] = review_for(gene, row["term"]["id"])
    ensure_new(data, gene, "GO:0002049", "involved_in")
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": q, "experts": []} for q in GENE_INFO[gene]["questions"]]
    data["suggested_experiments"] = [
        {
            "experiment_type": "biochemical assay",
            "description": (
                f"Clone and assay individual {gene} adenylation modules or module pairs against candidate "
                "pyoverdine/ferribactin substrate amino acids."
            ),
            "hypothesis": f"{gene} adenylation modules select defined residues in the KT2440 pyoverdine precursor.",
        },
        {
            "experiment_type": "protein interaction study",
            "description": (
                f"Measure {gene} interaction with PvdL, PvdI, PvdJ, and PvdD by co-immunoprecipitation, "
                "cross-linking mass spectrometry, or bacterial two-hybrid assays under iron limitation."
            ),
            "hypothesis": f"{gene} participates in a coordinated pyoverdine NRPS assembly line.",
        },
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    note_lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass curation for the translation/RNA-processing NRPS spillover batch.",
        "",
        "Asta was run for this gene and returned fast retrieval, but the useful gene-specific content was mainly the UniProt-derived target context; most retrieved papers were generic database/annotation resources rather than pyoverdine NRPS papers. The curation therefore uses Asta for provenance plus UniProt/domain evidence and the previously generated pyoverdine NRPS pathway report for mechanistic context.",
        "",
        "Key evidence:",
    ]
    seen: set[tuple[str, str]] = set()
    for item in evidence_for(gene, "GO:0003824"):
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        note_lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
        if len(seen) >= 10:
            break
    note_lines.extend(
        [
            "",
            "Curation implications:",
            "- Treat the gene as a pyoverdine/ferribactin NRPS subunit, not as translation/RNA-processing despite the word `non-ribosomal`.",
            "- Replace generic catalytic activity with NRPS activity where possible.",
            "- Replace phosphopantetheine binding with phosphopantetheine-dependent carrier activity.",
            "- Route broad secondary-metabolite or wrong-family siderophore terms to pyoverdine/siderophore biosynthesis.",
            "",
        ]
    )
    gene_file(gene, "notes.md").write_text("\n".join(note_lines), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    obj = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        obj["description"] = description
    return obj


def participant(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def nrps_annoton(gene: str, role: str, include_location: bool = True) -> dict:
    item = {
        "id": f"{gene.lower()}_pyoverdine_nrps",
        "label": f"{gene}: pyoverdine/ferribactin NRPS subunit",
        "participant": participant(gene),
        "function": descriptor("GO:1904091"),
        "processes": [descriptor("GO:0002049"), descriptor("GO:0019290")],
        "role_description": role,
    }
    if include_location:
        item["locations"] = [descriptor("GO:0005829")]
    return item


def add_or_replace_concept(concepts: list[dict], concept: dict) -> None:
    term_id = concept.get("term", {}).get("id")
    if term_id and any(item.get("term", {}).get("id") == term_id for item in concepts):
        return
    concepts.append(concept)


def write_module() -> None:
    data = yaml.safe_load(read_text(MODULE_PATH))
    data["description"] = (
        "Boundary/partial module for Pseudomonas putida KT2440 siderophore and pyoverdine "
        "biosynthesis. It includes the ppu00975/ppu01053 precursor and carrier-activation "
        "boundary genes plus the PvdL/PvdI/PvdJ/PvdD ferribactin/pyoverdine NRPS assembly "
        "genes routed out of the translation/RNA-processing bucket."
    )
    evidence = data.setdefault("evidence", [])
    existing_sources = {item.get("source_id") for item in evidence}
    new_evidence = [
        {
            "source_id": f"file:{BATCH_TSV}",
            "title": "PSEPK translation/RNA NRPS spillover batch",
            "statement": (
                "The batch records pvdD, pvdJ, pvdI, and pvdL as non-ribosomal peptide synthetase "
                "spillovers from the translation/RNA-processing bucket and routes them to siderophore "
                "biosynthesis context."
            ),
        },
        {
            "source_id": "file:PSEPK/pvdD/pvdD-deep-research-falcon.md",
            "title": "pvdD Falcon pyoverdine NRPS pathway context",
            "statement": (
                "The pvdD pathway report summarizes the canonical PvdL/PvdI/PvdJ/PvdD pyoverdine NRPS "
                "assembly line, cytoplasmic synthesis, and terminal PvdD context."
            ),
        },
    ]
    for item in new_evidence:
        if item["source_id"] not in existing_sources:
            evidence.append(item)
            existing_sources.add(item["source_id"])

    concepts = data["module"].setdefault("concepts", [])
    for concept in [
        descriptor("GO:1904091", "General NRPS activity used for PvdL/PvdI/PvdJ/PvdD assembly subunits."),
        descriptor("GO:0097429", "General amino acid ligation activity for pyoverdine NRPS modules."),
        descriptor("GO:0140414", "Carrier-domain activity for phosphopantetheine-dependent NRPS intermediates."),
    ]:
        add_or_replace_concept(concepts, concept)

    parts = data["module"].setdefault("parts", [])
    parts = [part for part in parts if part.get("node", {}).get("id") != "pyoverdine_ferribactin_nrps_assembly"]
    parts.append(
        {
            "order": 6,
            "role": "Pyoverdine/ferribactin NRPS assembly",
            "node": {
                "id": "pyoverdine_ferribactin_nrps_assembly",
                "label": "Pyoverdine/ferribactin NRPS assembly",
                "module_type": "BIOLOGICAL_PROCESS",
                "description": (
                    "PvdL, PvdI, PvdJ, and PvdD are the large NRPS assembly-line proteins for the "
                    "ferribactin/pyoverdine precursor. KT2440-specific residue assignments remain unresolved, "
                    "but product identity, domain architecture, and Pseudomonas pyoverdine pathway evidence "
                    "support routing these genes to pyoverdine/siderophore biosynthesis rather than translation."
                ),
                "annotons": [
                    nrps_annoton("pvdL", "Initiation/early ferribactin NRPS subunit with multiple A/C/PCP modules and FAAL/FAAC-like starter-unit context.", include_location=False),
                    nrps_annoton("pvdI", "Ferribactin/pyoverdine NRPS subunit with repeated A/C/PCP modules for internal peptide assembly."),
                    nrps_annoton(
                        "pvdJ",
                        "Ferribactin/pyoverdine NRPS subunit with repeated A/C/PCP modules for later peptide assembly.",
                        include_location=False,
                    ),
                    nrps_annoton("pvdD", "Terminal pyoverdine NRPS subunit; existing review supports cytosolic assembly and terminal thioesterase context."),
                ],
            },
        }
    )
    data["module"]["parts"] = sorted(parts, key=lambda part: part.get("order", 999))
    module_notes = (
        "This module is deliberately scoped as a boundary/partial siderophore module. The ppu00975/ppu01053 "
        "members cover precursor, tailoring, carrier-activation, and chorismate-boundary chemistry; the added "
        "PvdL/PvdI/PvdJ/PvdD node records the main ferribactin/pyoverdine NRPS assembly machinery that was "
        "misrouted to translation/RNA processing by the string 'non-ribosomal'. Exact KT2440 module substrate "
        "assignments remain open."
    )
    data["module"]["notes"] = module_notes
    data["notes"] = module_notes
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENE_INFO:
        curate_gene(gene)
        write_notes(gene)
    write_module()
    print("Curated translation/RNA NRPS spillovers: pvdJ, pvdI, pvdL; extended siderophore module")


if __name__ == "__main__":
    main()
