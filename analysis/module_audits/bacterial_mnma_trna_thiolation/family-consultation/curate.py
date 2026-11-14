"""Apply manually adjudicated family reviews; original inputs are archived separately."""

import copy
import csv
import json
import re
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
PRE = A.parent / "preflight"
ROOT = A.parents[3]
labels = {
    r["curie"]: r["label"] for r in csv.DictReader((ROOT / "cache/go/terms.csv").open())
}
taxa = {
    r["curie"]: r["label"]
    for r in csv.DictReader((ROOT / "cache/ncbitaxon/terms.csv").open())
}
obo = (ROOT / "interpro/panther/panther.obo").read_text()
pnames = dict(re.findall(r"^id: (PANTHER:PTHR[^\n]+)\nname: ([^\n]+)", obo, re.M))
for x in json.loads((A / "term-scope.json").read_text())["results"]:
    labels[x["id"]] = x["name"]
GENES = [
    ("ECOLI", "iscS", "P0A6B7"),
    ("PSEPK", "iscS", "Q88PK8"),
    ("BACSU", "iscS1", "O34599"),
    ("THET2", "TT_C0087", "Q72LH2"),
    ("THET2", "TT_C1373", "Q72HV9"),
    ("ECOLI", "mnmA", "P25745"),
    ("PSEPK", "mnmA", "Q88FR9"),
    ("BACSU", "mnmA", "O35020"),
    ("THET2", "mnmA", "Q72GX1"),
    ("ECOLI", "tusA", "P0A890"),
    ("PSEPK", "tusA", "Q88L21"),
    ("ECOLI", "tusB", "P45530"),
    ("PSEPK", "PP_3995", "Q88FT7"),
    ("ECOLI", "tusC", "P45531"),
    ("PSEPK", "PP_3994", "Q88FT8"),
    ("ECOLI", "tusD", "P45532"),
    ("PSEPK", "tusD", "Q88FT9"),
    ("ECOLI", "tusE", "P0AB18"),
    ("PSEPK", "tusE", "Q88FT6"),
]
PROTEINS = {}
for org, g, acc in GENES:
    path = f"genes/{org}/{g}/{g}-ai-review.yaml"
    d = yaml.safe_load((ROOT / path).read_text())
    assert d["id"] == acc
    PROTEINS[acc] = {
        "id": "UniProtKB:" + acc,
        "label": g,
        "gene_symbol": g,
        "organism": d["taxon"]["label"],
        "gene_review": path,
    }


def term(go):
    return {"id": go, "label": labels[go]}


def support(ref, quote):
    return {"reference_id": ref, "supporting_text": quote}


def sf(f, n, members, description):
    ident = f"PANTHER:{f}:SF{n}"
    return {
        "subfamily_id": ident,
        "label": pnames[ident],
        "description": description,
        "representative_members": [
            copy.deepcopy(PROTEINS[a]) if a in PROTEINS else {"id": "UniProtKB:" + a}
            for a in members
        ],
    }


def assessment(go, scope, reason, supports, subfamilies=None):
    x = {
        "assessed_term": term(go),
        "scope": scope,
        "scope_reason": reason,
        "supported_by": supports,
    }
    if subfamilies:
        x["applicable_subfamilies"] = [
            {"id": s, "label": pnames[s]} for s in subfamilies
        ]
    return x


def refs(d):
    ids = set()

    def walk(v):
        if isinstance(v, dict):
            if "reference_id" in v:
                ids.add(v["reference_id"])
            for z in v.values():
                walk(z)
        elif isinstance(v, list):
            for z in v:
                walk(z)

    walk(d)
    existing = {x["id"] for x in d.get("references", [])}
    for ref in sorted(ids - existing):
        if ref.startswith("PMID:"):
            raw = (
                ROOT / "publications" / ("PMID_" + ref.split(":")[1] + ".md")
            ).read_text()
            title = yaml.safe_load(raw.split("---", 2)[1])["title"]
        else:
            title = ref.removeprefix("file:")
        d.setdefault("references", []).append({"id": ref, "title": title})


def save(f, d):
    refs(d)
    d["review_status"] = "COMPLETE"
    d["reviewed_by"] = "codex"
    d["review_date"] = "2026-11-07"
    path = ROOT / f"interpro/panther/{f}/{f}-review.yaml"
    path.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))


sulfur = support("PMID:16387657", "IscS transfers the persulfide\nsulfur to TusA.")
relay = support(
    "PMID:16387657",
    "TusE binds TusBCD complex and stimulates sulfur transfer from\nTusA to TusD.",
)
tusd = support(
    "PMID:16472754", "only Cys78, in the TusD\nsubunit, participates in sulfur transfer"
)
yrvo = support("PMID:25825430", "YrvO is able to transfer sulfur directly to MnmA.")
tt = support(
    "PMID:31801798",
    "These results suggest direct persulfide transfer from the cysteine desulfurases to MnmA during s2U formation.",
)
critical = support(
    "PMID:39660893",
    "These apparent differences in experimental findings need to be investigated and clarified in future studies.",
)
# Preserve current Isc6175 review; change only universal process scope and directly related prose.
f = "PTHR11601"
d = yaml.safe_load((ROOT / f"interpro/panther/{f}/{f}-review.yaml").read_text())
for a in d["term_assessments"]:
    if a["assessed_term"]["id"] == "GO:0016226":
        a["scope"] = "UNRESOLVED"
        a.pop("applicable_subfamilies", None)
        a["scope_reason"] = (
            "IscS, NifS and NFS1 are established sulfur donors for Fe-S assembly, but SF34 also contains the directly characterized Bacillus subtilis YrvO/iscS1 (O34599), a cognate MnmA sulfur donor. This shared classification does not establish a native Fe-S assembly role for every SF34 member. The positive IscS/NFS1 evidence and eukaryotic PAINT node remain valid; no YrvO negative native Fe-S assay or loss branch is asserted. Exact target function and partner evidence are required."
        )
        a["supported_by"].append(yrvo)
d["summary"] += (
    " The same SF34 also includes the dedicated Bacillus YrvO/iscS1 donor for MnmA-mediated U34 thiolation; the common desulfurase reaction does not make sulfur acceptor partnerships interchangeable."
)
d["coherence_reason"] += (
    " In particular, the YrvO–MnmA partnership differs from the housekeeping IscS relay, so Fe-S-process participation cannot be licensed from SF34 alone."
)
d["notes"] += (
    " The 2026-11-07 MnmA consultation preserves all original node assessments, PAINT payloads and unrelated chemistry judgments. PR5077 is an older overlapping review and was not substituted for this curated baseline."
)
save(f, d)
# Reuse all four published PR5078 Tus review structures and every assertion payload.
configs = {
    "PTHR34874": (
        "TusD/YchN family with a sulfur-relay TusD branch",
        "P45532",
        "Q88FT9",
        "TusD is the persulfide-bearing subunit of the heterohexameric TusBCD sulfur-transfer complex. The distinct YchN branch shares ancestry but is not thereby assigned the TusD-specific U34 role.",
        tusd,
    ),
    "PTHR37010": (
        "TusE terminal sulfur-relay carriers",
        "P0AB18",
        "Q88FT6",
        "TusE associates with TusBCD and the MnmA–tRNA complex during wobble-uridine thiolation. Its relay role does not establish autonomous tRNA thiolation or interchangeable binding to every MnmA homolog.",
        relay,
    ),
    "PTHR37526": (
        "TusB sulfur-relay complex subunits",
        "P45530",
        "Q88FT7",
        "TusB contributes the structure of the TusBCD complex used in bacterial U34 thiolation. Covalent sulfur carriage is localized to TusD in the characterized complex, rather than inferred for every subunit.",
        tusd,
    ),
    "PTHR38780": (
        "TusC sulfur-relay complex subunits",
        "P45531",
        "Q88FT8",
        "TusC contributes to the TusBCD complex that transfers sulfur toward MnmA. Its structural contribution is distinct from the experimentally assigned sulfur-bearing TusD cysteine.",
        tusd,
    ),
}
for f, (preferred, anchor, target, summary, evidence) in configs.items():
    d = yaml.safe_load((PRE / f"PR5078-{f}-review.yaml").read_text())
    d["preferred_name"] = preferred
    d["summary"] = summary
    d["coherence_reason"] = (
        "The reviewed PAINT clade and extant functional evidence support the stated relay or complex role. Family-wide scope, where retained, concerns that role; it does not assert the same upstream donor, complete pathway, autonomous catalysis or obligate essentiality in every bacterium."
    )
    d["reference_protein"] = copy.deepcopy(PROTEINS[anchor])
    for s in d["subfamilies"]:
        if any(x["id"] == "UniProtKB:" + anchor for x in s["representative_members"]):
            s["representative_members"].append(copy.deepcopy(PROTEINS[target]))
    for n in d["node_assessments"]:
        n["evidence"] = "IBD"
        n["assessment_reason"] = (
            "The official tree places this original assertion on the "
            + (
                "whole TusE/TusB/TusC family clade"
                if f != "PTHR34874"
                else (
                    "shared YchN/TusD clade for cytosolic localization"
                    if n["asserted_term"]["id"] == "GO:0005829"
                    else "TusD descendant clade, separate from YchN"
                )
            )
            + ". The characterized E. coli protein and conserved family architecture support inheritance of this claim. Target absence from a sampled tree is not a loss, and supporting descendants are not counted as a proxy for node validity."
        )
        if n["asserted_term"]["id"] != "GO:0005829":
            n["supported_by"].append(evidence)
    for a in d["term_assessments"]:
        a["scope_reason"] += (
            " The official tree/MSA and primary E. coli relay evidence were inspected; exact KT2440 membership is independently supported by its UniProt record. This scope does not license arbitrary cross-species pairing or autonomous sulfur transfer by structural subunits."
        )
        if a["assessed_term"]["id"] != "GO:0005829":
            a["supported_by"].append(evidence)
    d["notes"] = (
        d.get("notes", "")
        + " Imported from PR5078 head4477f7e8948736e948949285b68a94d347e2d9af, whose exact original bytes are preserved in the preflight. Every original node identity, term, seed, taxon and PAINT date is retained. Mechanical donor-count explanations were replaced with clade/role reasoning. The original primary Tus papers are abstract-only in the normal cache; positive claims are explicit in those abstracts and corroborated by later full primary/review sources. No experimental-negative claim is based on inaccessible full text. Target membership does not prove a sampled target leaf exists."
    )
    save(f, d)
# MnmA/MTU1 family: preserve every raw node including the unresolved tick loss.
f = "PTHR11933"
d = {
    "family_id": "PANTHER:" + f,
    "family_name": pnames["PANTHER:" + f],
    "preferred_name": "MnmA/MTU1-related PP-loop sulfurtransferases",
    "summary": "MnmA and mitochondrial MTU1 activate tRNA wobble uridine and install sulfur at C2. Their donor partnerships, C5-modified substrate preferences and cofactor requirements differ. The family tree also contains an SF6 ThiI-AANH-like branch outside the principal MnmA/MTU1 node, so the family label does not establish the same reaction for all members.",
    "functional_coherence": "MOSTLY_COHERENT",
    "coherence_reason": "SF5 contains experimentally supported bacterial MnmA and mitochondrial MTU1, whereas the additional SF6 branch lacks a demonstrated MnmA assignment in this audit. D-type and C-type MnmAs share SF5; iron-sulfur dependence and compatible donors cannot be inferred from that identifier.",
    "reference_protein": PROTEINS["P25745"],
    "subfamilies": [
        sf(
            f,
            5,
            ["P25745", "Q88FR9", "O35020", "Q72GX1", "O75648"],
            "Bacterial MnmA and mitochondrial MTU1; common U34 sulfur chemistry but different substrate and partner contexts.",
        ),
        sf(
            f,
            6,
            ["O67046"],
            "Official tree branch outside the main MnmA/MTU1 node; membership is verified, exact U34 activity remains unestablished here.",
        ),
    ],
    "node_assessments": [],
    "term_assessments": [],
    "notes": "All eight original PAINT rows are preserved verbatim in the immutable raw slice. The MSA verifies E. coli D99/C102/C199 and Bacillus D101/C104/C200 in corresponding columns; Thermus Q72GX1 is not a sampled tree/MSA leaf and its three-cysteine primary result is target-specific. No universal residue-dependent activity rule is authored. GO0103016 and GO0061708 are sibling reactions, not interchangeable labels. The mite IRD and its source IBD are retained without inventing a molecular-loss explanation.",
}
rows = list(
    csv.DictReader(
        (ROOT / f"interpro/panther/{f}/{f}-paint.tsv").open(), delimiter="\t"
    )
)
for r in rows:
    go = r["go_id"]
    negative = r["negated"] == "true"
    n = {
        "node_id": "PANTHER:" + r["node"],
        "asserted_term": term(go),
        "evidence": r["evidence"],
        "paint_snapshot": r["date"],
        "seeds": [{"id": s} for s in r["seeds"].split("|")],
        "assessment": "UNRESOLVED" if negative else "SOUND",
        "assessment_reason": "",
    }
    if negative:
        n["negated"] = True
        n["assessment_reason"] = (
            "The original IRD stops the bacterial sulfurtransferase-complex IBD for the sampled Ixodes B7P8A5 branch. It does not assert absence of U34 thiolation. The residue or biochemical basis of this specific complex-association loss was not recovered; the raw loss remains recorded and is not converted into a broad family exclusion."
        )
    else:
        n["assessment_reason"] = {
            "GO:0016783": "The principal SF5 node includes bacterial MnmA and mitochondrial MTU1; both catalyze sulfur transfer. The separate SF6 branch is outside this node, so the assertion is not treated as a whole-family grant.",
            "GO:0002143": "The principal MnmA/MTU1 clade unites bacterial and mitochondrial U34 C2 thiolation; differing sulfur donors and C5 substituents do not negate this shared process.",
            "GO:0005739": "The eukaryotic MTU1 branch supports mitochondrial localization; bacterial SF5 members lie outside this node and are not assigned an organelle.",
            "GO:1990799": "The eukaryotic MTU1 branch supports the mitochondrial version of U34 thiolation. This contextual claim is not transferred to bacterial SF5 proteins.",
            "GO:0061708": "This chordate branch carries the taurino-substrate reaction grounded in human TRMU. It is distinct from the bacterial reaction and is not generalized to SF5.",
            "GO:0103016": "The sampled fungal branch carries the uridine reaction. Independent bacterial MnmA assays support the same activity elsewhere without changing this original node or inventing an ancestral gain.",
            "GO:1990228": "The bacterial MnmA branch participates in sulfurtransferase assemblies with cognate sulfur donors. The term does not require a universal TusABCDE composition; Bacillus YrvO/MnmA provides a different compatible assembly.",
        }[go]
    if r["taxon"] != "taxon:":
        tid = r["taxon"].replace("taxon:", "NCBITaxon:")
        n["node_taxon"] = {
            "id": tid,
            "label": taxa.get(
                tid,
                {"NCBITaxon:6945": "Acari", "NCBITaxon:451864": "Dikarya"}[tid]
                if tid in ["NCBITaxon:6945", "NCBITaxon:451864"]
                else tid,
            ),
        }
    n["supported_by"] = [
        support(f"file:interpro/panther/{f}/{f}-paint.tsv", "\t".join(r.values()))
    ]
    d["node_assessments"].append(n)
for go in ["GO:0016783", "GO:0002143"]:
    d["term_assessments"].append(
        assessment(
            go,
            "SUBFAMILY_ONLY",
            "The original PTN000232426 assertion covers the MnmA/MTU1 SF5 clade. SF6 is outside that node and lacks independently established exact MnmA activity here; this is a scope limit, not a negative assay. Compatible donor pairing and native compartment remain target-specific.",
            [yrvo, tt],
            ["PANTHER:PTHR11933:SF5"],
        )
    )
for go in ["GO:0103016", "GO:0061708", "GO:0005739", "GO:1990799", "GO:1990228"]:
    reason = {
        "GO:0103016": "Bacterial MnmA and the fungal PAINT clade positively support this reaction, but human MTU1 carries the chemically distinct taurino-substrate sibling. SF5 cannot separate them, and SF6 exact chemistry is unestablished. Exact positive members retain activity; no secondary-substrate absence is asserted.",
        "GO:0061708": "Human/chordate MTU1 supports the taurino-substrate activity; that specific reaction is not established for every bacterial or fungal member of the same SF5.",
        "GO:0005739": "The genuine eukaryotic localization node is narrower than SF5, which also includes bacterial proteins. No universal subfamily organelle grant is appropriate.",
        "GO:1990799": "The eukaryotic MTU1 process node is narrower than the mixed bacterial/eukaryotic SF5 classification.",
        "GO:1990228": "Bacterial MnmA forms functional sulfur-transfer assemblies, but neither a universal complex composition nor a complete family/subfamily association scope is resolved. Preserve the original IBD and mite IRD as distinct node assertions.",
    }[go]
    supports = (
        [yrvo, tt]
        if go in ["GO:0103016", "GO:1990228"]
        else [
            d["node_assessments"][
                next(
                    i
                    for i, n in enumerate(d["node_assessments"])
                    if n["asserted_term"]["id"] == go
                )
            ]["supported_by"][0]
        ]
    )
    d["term_assessments"].append(assessment(go, "UNRESOLVED", reason, supports))
d["notes"] += (
    " Full2021 and2024 E. coli primary studies disagree about the physiological Fe-S requirement; the critical2025 review explicitly identifies the unresolved discrepancy. C-type Thermus biochemical cofactor dependence is positive evidence and is retained. No universal Fe-S-binding grant is added."
)
d["term_assessments"][2]["supported_by"].append(critical)
save(f, d)
# TusA/YedF: no normal PAINT slice exists after a genuine fetch.
f = "PTHR33279"
d = {
    "family_id": "PANTHER:" + f,
    "family_name": pnames["PANTHER:" + f],
    "preferred_name": "TusA/YedF-related sulfur carriers",
    "summary": "Small sulfur-carrier proteins include the TusA relay component that accepts persulfide sulfur from IscS and delivers it toward the TusBCD/MnmA pathway. Related YedF and archaeal proteins occur in the same family; exact sulfur-trafficking roles require partner and pathway evidence.",
    "functional_coherence": "MOSTLY_COHERENT",
    "coherence_reason": "Shared sulfur-carrier architecture does not specify a single acceptor pathway. The normal PAINT acquisition resolved tree nodes but no node-level assertions, so no ancestral claim is invented.",
    "reference_protein": PROTEINS["P0A890"],
    "subfamilies": [
        sf(
            f,
            2,
            ["P0A890", "Q88L21"],
            "TusA members with positive bacterial relay evidence.",
        ),
        sf(
            f,
            6,
            ["P0AA31"],
            "YedF-related proteins; exact native pathway need not be the Tus relay.",
        ),
        sf(
            f,
            18,
            ["Q58397"],
            "Archaeal sulfur-carrier-related members; exact pathway not assigned here.",
        ),
    ],
    "term_assessments": [
        assessment(
            "GO:0097163",
            "UNRESOLVED",
            "E. coli TusA is a directly established persulfide carrier and KT2440 TusA has conserved membership and pathway context. The actual tree also contains YedF and archaeal branches whose complete functional scope was not resolved; their unknown role is not a negative sulfur-carrier claim.",
            [sulfur],
        ),
        assessment(
            "GO:0002143",
            "UNRESOLVED",
            "The E. coli TusA relay role is established; the exact U34 process is not licensed for every TusA/YedF-family member or every same-label subfamily member without cognate partner context.",
            [sulfur, relay],
        ),
    ],
    "notes": "A normal fetch-panther-paint PTHR33279 attempt completed with96 resolved nodes and zero node-level annotations; no fabricated slice or node assessment is supplied. The official tree contains P0A890 but not Q88L21. UniProt supports the latter classification independently; lack of sampled ancestry is not evidence of a loss.",
}
save(f, d)
# SufS/CsdA-related PLP family is functionally broader than its official label.
f = "PTHR43586"
e = support(
    "file:" + str((A / "A0R5M7-uniprot.json").relative_to(ROOT)),
    "Catalyzes a C-S bond cleavage, converting hercynylcysteine sulfoxide to 2-sulfenohercynine",
)
s = support(
    "file:" + str((A / "Q59072-uniprot.json").relative_to(ROOT)),
    "Converts O-phospho-L-seryl-tRNA(Cys) (Sep-tRNA(Cys)) to L-cysteinyl-tRNA(Cys) (Cys-tRNA(Cys))",
)
d = {
    "family_id": "PANTHER:" + f,
    "family_name": pnames["PANTHER:" + f],
    "preferred_name": "SufS/CsdA-related PLP-dependent enzymes",
    "summary": "This PLP-enzyme family includes group-II cysteine desulfurases, EgtE hercynylcysteine sulfoxide lyase and SepCysS aminoacyl-tRNA conversion enzymes. Thermus HB27 SufS supplies sulfur to MnmA in a purified cysteine-fed reaction, while other members have different physiological substrates and partners.",
    "functional_coherence": "HETEROGENEOUS",
    "coherence_reason": "Experimentally supported alternative chemistry occurs even within SF8: Thermus SufS and mycobacterial EgtE share the same official subfamily. SepCysS lies in SF3. Positive alternate activities do not prove a lack of secondary cysteine desulfuration, but they prevent an unqualified family-wide or SF8-wide role grant.",
    "reference_protein": PROTEINS["Q72HV9"],
    "subfamilies": [
        sf(
            f,
            8,
            ["Q72HV9", "A0R5M7"],
            "Includes Thermus cysteine desulfurase and mycobacterial EgtE; the chloroplastic label does not describe every member.",
        ),
        sf(f, 3, ["Q59072"], "SepCysS converts phosphoseryl-tRNA to cysteinyl-tRNA."),
        sf(
            f,
            25,
            ["P77444"],
            "Canonical bacterial SufS members with cysteine-desulfurase chemistry; partner function still requires context.",
        ),
    ],
    "node_assessments": [],
    "term_assessments": [
        assessment(
            "GO:0031071",
            "UNRESOLVED",
            "The newly fetched root IBD spans a heterogeneous PLP family, including EgtE and SepCysS lineages. Its established SufS/CsdA positive seeds remain valid, and Thermus SufS has direct donor chemistry. Current evidence does not justify assigning cysteine desulfuration to every descendant or defining a universal loss site; alternate substrate activity is not itself a negative assay.",
            [tt, e, s],
        ),
        assessment(
            "GO:0002143",
            "UNRESOLVED",
            "The purified Thermus SufS–MnmA pairing demonstrates a U34 sulfur-delivery capacity. It does not establish native donor exclusivity, a universal SF8 MnmA partner or U34 participation for other SufS/CsdA/EgtE/SepCysS members.",
            [tt],
        ),
    ],
    "notes": "The official label and classification are preserved, including the surprising chloroplastic SF8 name. Q72HV9 is absent from the sampled tree and reviewed-member CSV but is classified by the official UniProt record; a missing target leaf is not a negative loss trace. No new IRD/IKR or residue-based discrimination is invented.",
}
r = list(
    csv.DictReader(
        (ROOT / f"interpro/panther/{f}/{f}-paint.tsv").open(), delimiter="\t"
    )
)[0]
d["node_assessments"] = [
    {
        "node_id": "PANTHER:" + r["node"],
        "asserted_term": term(r["go_id"]),
        "evidence": r["evidence"],
        "paint_snapshot": r["date"],
        "seeds": [{"id": z} for z in r["seeds"].split("|")],
        "assessment": "UNRESOLVED",
        "assessment_reason": "The official tree places this IBD at the whole family root, spanning canonical desulfurases and experimentally characterized alternate PLP chemistries. Positive seed chemistry is retained, but a safe universal scope and any specific loss/pruning branch are unresolved. Neither a short seed list nor a different primary substrate is used as evidence of functional loss.",
        "supported_by": [
            support(f"file:interpro/panther/{f}/{f}-paint.tsv", "\t".join(r.values())),
            e,
            s,
        ],
    }
]
save(f, d)
print("Wrote eight scoped family reviews")
