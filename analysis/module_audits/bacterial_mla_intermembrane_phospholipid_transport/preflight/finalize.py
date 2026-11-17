from pathlib import Path
import hashlib
import json
import difflib

P = Path(".cache/module-audit-logs/mla-preflight-20261107")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


snap = json.loads((P / "main-snapshot.json").read_text())
prs = json.loads((P / "open-pr-files.json").read_text())
prefixes = [
    str(Path(k).parent) + "/" for k in [*snap["reviews"], *snap["families"]]
] + ["modules/bacterial_mla_intermembrane_phospholipid_transport"]
hits = []
for pr in prs:
    hit = [x for x in pr["files"] if any(x.startswith(pre) for pre in prefixes)]
    if hit:
        hits.append(
            {
                "number": pr["number"],
                "url": pr["url"],
                "head": pr["headRefOid"],
                "files": hit,
            }
        )
(P / "expanded-overlap.json").write_text(
    json.dumps(
        {
            "open_pr_count": len(prs),
            "largest_pr_files": max(len(x["files"]) for x in prs),
            "hits": hits,
        },
        indent=2,
    )
    + "\n"
)
u = json.loads((P / "uniprot-PA4453.json").read_text())["results"][0]
r = json.loads((P / "6HSY-entity1.json").read_text())
target = u["sequence"]["value"]
construct = r["entity_poly"]["pdbx_seq_one_letter_code_can"]
seq_match = difflib.SequenceMatcher(
    None, target, construct, autojunk=False
).find_longest_match()
assert seq_match.size == 193
identity = {
    "PSEAE_ttg2D": {
        "accession": "Q9HVW4",
        "locus": "PA4453",
        "species": u["organism"],
        "precursor_length": len(target),
        "pdb": "6HSY/entity1",
        "construct_length": len(construct),
        "identical_segment_length": seq_match.size,
        "uniprot_interval_1based": [seq_match.a + 1, seq_match.a + seq_match.size],
        "construct_interval_1based": [seq_match.b + 1, seq_match.b + seq_match.size],
        "construct_prefix": construct[: seq_match.b],
        "construct_suffix": construct[seq_match.b + seq_match.size :],
        "limit": "Exact mature segment identity; construct additions and precursor signal segment are not full-length identity. Native PAO1 cargo preparation is separately reported in33837253.",
    },
    "BORPE_reference_panel": [],
}
for locus, role in zip(range(3757, 3762), ["mlaF", "mlaE", "mlaD", "mlaA", "mlaC"]):
    d = json.loads((P / f"uniprot-{locus}.json").read_text())["results"][0]
    identity["BORPE_reference_panel"].append(
        {
            "locus": f"BP{locus}",
            "role": role,
            "accession": d["primaryAccession"],
            "species": d["organism"]["scientificName"],
            "taxon": d["organism"]["taxonId"],
            "length": d["sequence"]["length"],
            "classifications": [
                x["id"]
                for x in d["uniProtKBCrossReferences"]
                if x["database"] == "PANTHER"
            ],
            "seed_suggestion": f"BORPE BP{locus} --uniprot-id {d['primaryAccession']}",
        }
    )
identity["BORPE_assay_bridge"] = {
    "primary": "PMID:36518166",
    "native_strain": "B213",
    "supplement": "36518166-supp-els.txt TableS1",
    "quote": "SmR derivative of Tohama I",
    "loci": "Figure1A assigns BP3757–BP3761 to F/E/D/A/C",
    "confidence": "Reference-lineage/locus bridge, not complete experimental strain sequence equality",
    "limitations": [
        "No B213-specific UniProt entry found; the official strain:B213 query returned no entries, which is not evidence of biological absence.",
        "No complete B213 target sequence comparison established.",
        "Native perturbation directly tests MlaF; remaining four role assignments are conserved architecture/operon inference.",
        "No identifiable MlaB homolog reported; this does not imply unknown substitutes are impossible.",
    ],
}
(P / "identity-proof.json").write_text(json.dumps(identity, indent=2) + "\n")
# Short source-exact quotes; findings and bounds are manually adjudicated.
rows = []


def add(pmid, kind, file, url, scope, statement, quote):
    text = (P / file).read_text()
    assert quote in text, (pmid, quote)
    rows.append(
        {
            "source_id": "PMID:" + pmid,
            "kind": kind,
            "source_file": file,
            "source_sha256": sha(P / file),
            "url": url,
            "access_scope": scope,
            "finding": statement,
            "supporting_text": quote,
        }
    )


add(
    "36459067",
    "REVIEW",
    "PMC10212509.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC10212509/",
    "Full XML; structural sections, directionality and outlook read",
    "Summarizes measured lipid binding and complete/partial reconstitution. Retrograde is best supported in the characterized systems; alternative direction proposals are not equal-strength native demonstrations. Extended Bacteroides MlaD tunnel is explicitly speculative, not a verified MlaA/C-independent realizer.",
    "the retrograde mode is the most widely accepted",
)
add(
    "38802775",
    "REVIEW",
    "PMC11131202.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC11131202/",
    "Full XML; organization, physiology and MlaA sections read",
    "Documents species-dependent phenotypes and operon organization. Do not treat the review’s broad six-component/retrograde language as proof of every lineage; primary Bordetella data and MlaB exceptions qualify it.",
    "mlaA mutants of N. gonorrhoea FA1090",
)
add(
    "35850151",
    "REVIEW",
    "PMC12981311-full.html.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC12981311/",
    "Complete HTML acquired; introduction, envelope boundary, Section5.1 and linked transport concepts read; XML500 retained",
    "Separates ferry transport from bridge/tunnel systems and shared folds from substrate specificity. Occurrence in diderms does not make all MCE-containing proteins Mla phospholipid transporters.",
    "The Mla system uses a ferry-like mechanism",
)
add(
    "31420510",
    "PERSPECTIVE",
    "PMC6717313.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC6717313/",
    "Full XML; Mla and directional-evidence discussion read; source calls itself Perspective",
    "Useful historical critical synthesis rather than a fourth primary assay or an unqualified review label. Contrasts genetics, lipid binding and inference from incomplete transfer systems.",
    "This Perspective aims to address recent work",
)
add(
    "34873038",
    "PRIMARY",
    "PMC8685716-html.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC8685716/",
    "Complete authentic PMC HTML after XML500; results and nanodisc transfer logic read",
    "E. coli MlaC↔MlaFEDB spontaneous exchange is bidirectional, but ATP enhances carrier-to-complex transfer and suppresses reverse exchange. This supports energetic retrograde bias, not anterograde powered transport.",
    "such anterograde movement is instead abolished by ATP hydrolysis",
)
add(
    "39080293",
    "PRIMARY",
    "PMC11289387.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC11289387/",
    "Full XML; interaction structure, WT transfer controls and assay strain methods read",
    "E. coli K12 BW25113 cellular background and reconstituted transfer support MlaC/D interface function. Liposome reporter movement is distinct from native whole-cell net flux. The inherited quote calling the label phosphatidyl glycerol (PE) needs scientific correction using the actual NBD-PE caption.",
    "lipids are transferred from the MlaA proteoliposome to the MlaFEDB proteoliposome",
)
add(
    "40168124",
    "PRIMARY",
    "PMC12002339.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC12002339/",
    "Full XML; native-MS loading results and protein context read",
    "OmpF3–MlaA enhances MlaC lipid loading and forms a transient complex; PG selectivity/enrichment is characterized. This is OM-to-carrier interface evidence, not independent reconstitution of all six components.",
    "significant enrichment of PG over PE",
)
add(
    "32602838",
    "PRIMARY",
    "PMC7367683.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC7367683/",
    "Full XML; MlaFB interface and functional rescue read",
    "E. coli MlaB supports MlaF stability/assembly. Overexpressed MlaF can compensate a missing B under the tested conditions; neither universal B necessity nor universal dispensability follows.",
    "can be rescued by overexpression of either WT MlaB or MlaF",
)
add(
    "36518166",
    "PRIMARY",
    "PMC9743053.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC9743053/",
    "Full XML, Figure1 visually inspected and authentic Supplementary TableS1 read",
    "B213 native MlaF/OMPLA genetics and cell-surface PE readout support asymmetry maintenance and retrograde consistency, not measured directional transport. Combined perturbation gives the clearest phenotype; growth depends on context. Five-gene F/E/D/A/C organization lacks an identifiable B.",
    "we were not able to identify an MlaB homologue",
)
add(
    "33837253",
    "PRIMARY",
    "PMC8035174.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC8035174/",
    "Full XML; structure, lipid cargo, native PAO1 preparation and methods read",
    "PAO1 Ttg2D/PA4453 carries two diacyl phospholipids or cardiolipin; both heterologous structure and native periplasmic cargo preparation are distinguished. Do not infer drug export or a directly measured complete transport direction from permeability phenotypes.",
    "In addition, a P. aeruginosa PAO1 mutant lacking ttg2D",
)
add(
    "30638443",
    "PRIMARY",
    "PMC6365058.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC6365058/",
    "Full XML; strain, complex assembly and directional assays read",
    "ATCC17978 native genetics and heterologously expressed complex support Mla components; membrane-fractionation/isotope evidence was interpreted as anterograde. Subsequent32880370 challenges both fractionation and strain confounding, so do not use it as settled direction proof.",
    "Transposon mutagenesis and subsequent chromosomal deletions of mla genes were performed in Acinetobacter baumannii ATCC 17978.",
)
add(
    "32880370",
    "PRIMARY",
    "PMC7500953.txt",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC7500953/",
    "Full XML; strain comparison, fractionation critique and OMV pulse-chase results read",
    "Contrasting ATCC17978 stocks reveal an obgE background confound and lack of anterograde deficit in tested mutants. OMV pulse-chase is a proxy rather than purified directional transfer; corrective evidence substantially weakens the earlier anterograde interpretation.",
    "no mla mutants, regardless of lab origin, exhibited a decrease in anterograde transport",
)
add(
    "28388411",
    "PRIMARY",
    "main-PMID_28388411.md",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC5467742/",
    "Full publication cache at pinned origin/main; direct-binding results and discussion model distinguished",
    "Direct biolayer interferometry demonstrates MlaC binding to purified MlaFEDB and MlaA–OmpF. The lipid-handoff sentence in the inherited module is a discussion model rather than a measured transfer result. Retain binding evidence and cite later direct transfer studies for lipid movement.",
    "using biolayer interferometry",
)
(P / "source-ledger.json").write_text(json.dumps(rows, indent=2) + "\n")
(P / "access-clarifications.json").write_text(
    json.dumps(
        {
            "PMC8685716": "XML retrieval failed, but subsequent HTML is genuine complete article; source-access-2 full_body_present false only describes XML-parser result, not final access.",
            "PMC12981311": "XML failed; complete HTML successful. Review is2022, author manuscript deposited2026; do not misdate it.",
            "36518166": "First PMC PDF request returned1817byte non-PDF; Elsevier and EuropePMC supplementZIP yielded genuine supplement, extracted and read.",
            "31235958": "Only immutable main abstract read; do not claim full primary access.",
            "2026_preprints": [
                "10.64898/2026.05.15.725309 PA MlaC–MlaD conformational switch, discovery abstract only; not peer-reviewed final support.",
                "10.64898/2026.08.28.747810 C. jejuni MlaC monomer/dimer and proposed RND coupling; discovery full web excerpts only, no exact accession bridge or demonstrated RND lipid-transfer interface.",
            ],
            "Bacteroides": "Extended MlaD prediction from2022review remains an unverified mechanistic comparator, not a positive complete panel.",
        },
        indent=2,
    )
    + "\n"
)
print("WROTE", len(rows), "source judgments; scope overlap", hits)
