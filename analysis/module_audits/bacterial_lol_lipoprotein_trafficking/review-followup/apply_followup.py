import copy
import json
from pathlib import Path
import yaml

R = Path.cwd()
A = R / "analysis/module_audits/bacterial_lol_lipoprotein_trafficking/review-followup"
B = json.loads((A / "baseline.json").read_text())
D = copy.deepcopy(B["reviews"])
changes = {}


def doc(org, g):
    return D[f"genes/{org}/{g}/{g}-ai-review.yaml"]


def mark(org, g, s):
    changes.setdefault(f"genes/{org}/{g}/{g}-ai-review.yaml", []).append(s)


def row(d, term):
    return next(x for x in d["existing_annotations"] if x["term"]["id"] == term)


parent = {"id": "GO:0140318", "label": "protein transporter activity"}
definition = "Directly binding a mature lipoprotein and promoting incorporation of its lipid anchor into the bacterial outer membrane."
justification = "GO:0140318 provides the protein-binding and delivery genus. GO:0140598 requires movement with cargo between locations, whereas GO:0140306 specifies release from the inner membrane; neither describes terminal lipid-anchor insertion. GO:0032977 membrane insertase activity requires a transmembrane-domain-containing protein client, unlike the lipid-anchored lipoprotein substrate here. The proposed definition does not require a separate soluble donor because a bifunctional carrier can also perform the terminal step. Gene-specific support and assay limitations remain in the core function and supporting evidence."
for org, g in [
    ("ECOLI", "lolB"),
    ("ACIAD", "lolB"),
    ("PSEPK", "lolB"),
    ("FLAJ1", "Fjoh_1066"),
    ("CAUVC", "CC_3705"),
]:
    d = doc(org, g)
    t = next(
        t
        for t in d["proposed_new_terms"]
        if t["proposed_name"] == "outer-membrane lipoprotein insertion activity"
    )
    t.update(
        proposed_definition=definition,
        proposed_parent=copy.deepcopy(parent),
        justification=justification,
    )
    mark(
        org,
        g,
        "Unify insertion proposal definition and parent; distinguish membrane insertase client chemistry without imposing a separate donor on bifunctional carriers.",
    )
for org in ["ACIAD", "PSEPK"]:
    d = doc(org, "lolB")
    v = row(d, "GO:0009279")["review"]
    v["action"] = "MODIFY"
    v["summary"] = (
        "Refine the supported outer-membrane location to its periplasm-facing leaflet."
    )
    v["reason"] = (
        "The LolB-specific "
        + (
            "TIGR00548 signature and predicted signal peptide/lipidated mature cysteine"
            if org == "ACIAD"
            else "HAMAP MF_00233 assignment, secretion signal and lipidated mature cysteine"
        )
        + " support an anchored, periplasm-facing receptor. Its conserved acceptance of periplasmic LolA cargo and terminal lipid-anchor insertion place the functional domain on the periplasmic side of the outer membrane (GO:0031241), a supported refinement of GO:0009279. This combines target architecture with the E. coli transfer mechanism; it is not a direct "
        + ("ADP1" if org == "ACIAD" else "KT2440")
        + " topology experiment."
    )
    v["proposed_replacement_terms"] = [
        {"id": "GO:0031241", "label": "periplasmic side of cell outer membrane"}
    ]
    for c in d["core_functions"]:
        for loc in c.get("locations", []):
            if loc["id"] == "GO:0009279":
                loc.update(
                    id="GO:0031241", label="periplasmic side of cell outer membrane"
                )
    if org == "PSEPK":
        v["supported_by"] += [
            {
                "reference_id": "file:PSEPK/lolB/lolB-uniprot.txt",
                "record_section": ["FT:SIGNAL"],
                "supporting_text": "SIGNAL          1..17",
            },
            {
                "reference_id": "file:PSEPK/lolB/lolB-uniprot.txt",
                "record_section": ["FT:LIPID"],
                "supporting_text": "LIPID           18",
            },
        ]
    v["supported_by"].append(
        {
            "reference_id": "PMID:9384574",
            "supporting_text": "When the Lpp-LolA complex was incubated with a water-soluble LolB derivative, Lpp was transferred from LolA to LolB.",
        }
    )
    mark(
        org,
        "lolB",
        "Refine outer-membrane annotation and core location to periplasmic side using target architecture and conserved cargo acceptance.",
    )
# Explicit row-specific reasons replace shared role-independent caveats.
reasons = {
    "lolA": {
        "GO:0030288": "The cleavable secretion signal, curated periplasmic location and LolA-specific HAMAP MF_00240/TIGR00547 assignment support a soluble protein in the outer membrane-bounded periplasm. This location is inferred for Q88FS9, not measured by target fractionation.",
        "GO:0042597": "The target is a soluble carrier in a diderm periplasm. Refine the generic periplasmic-space term to its outer membrane-bounded descendant GO:0030288, already carried by this protein; the cleavable secretion signal and curated location support the specificity.",
        "GO:0042953": "Q88FS9 is a curated LolA carrier. The target function statement and the E. coli soluble cargo-complex experiment support conserved carriage of mature lipoproteins across the periplasm; the carrier itself moves cargo and therefore performs transport work.",
        "GO:0044874": "The target LolA function statement specifies inner-to-outer membrane lipoprotein delivery. Conserved carrier activity supplies the periplasmic transport step of this destination-specific localization process; the supporting E. coli experiment is an ortholog assay, not a KT2440 measurement.",
        "GO:0140598": "Retain the historical carrier proposal: the specific Q88FS9 HAMAP MF_00240/TIGR00547 assignment and curated function support carriage, and E. coli LolA forms soluble complexes with outer-membrane-directed lipoproteins. This supports the conserved binding-and-carriage function without assigning measured target kinetics.",
    },
    "lolB": {
        "GO:0015031": "Protein transport is correct but broader than the supported substrate-specific process GO:0042953, already represented by the historical proposal. The curated Q88PX4 function and the E. coli LolA-to-LolB transfer experiment support conserved terminal lipoprotein delivery, rather than rejection of transport.",
        "GO:0044874": "The curated Q88PX4 function explicitly places LolB in incorporation of lipoproteins into the outer membrane after LolA release. That terminal delivery step supports the destination-specific localization process by conserved-function inference.",
        "GO:0042953": "Retain the historical lipoprotein-transport proposal: Q88PX4 is the curated LolB terminal receptor, and LolA-to-LolB cargo transfer is experimentally demonstrated for E. coli. LolB itself performs terminal cargo acceptance and insertion. GO:0042953 and GO:0044874 are not ancestors or descendants of one another in the checked is_a/part_of ancestry, so the retained row is not a hierarchical duplicate.",
    },
    "lolD": {
        "GO:0005524": "ATP binding is substrate engagement in the core LolD catalytic cycle, not a peripheral function or an ancestor of ATP hydrolysis. Q88KY4 has the specific LolD ATPase assignment and conserved nucleotide-binding machinery; the assembled E. coli system supplies mechanistic ortholog support.",
        "GO:0005886": "The curated Q88KY4 location places LolD on the inner membrane through its association with LolC/LolE. The ATPase is the peripheral cytoplasmic subunit of this membrane complex, not itself a transmembrane permease.",
        "GO:0016020": "Refine membrane to the supported plasma-membrane location GO:0005886 already carried by the protein. LolD associates peripherally with the inner-membrane LolC/LolE complex; no transmembrane topology is implied for this ATPase.",
        "GO:0016887": "Q88KY4 is the HAMAP MF_01708/TIGR02211 LolD nucleotide-binding ATPase in the lolCDE locus. ATP hydrolysis is the energy-supplying catalytic activity of the assembled release machinery, established in the E. coli system and inferred for the matched KT2440 protein.",
        "GO:0022857": "Correct the mechanistic assignment to contribution to lipoprotein releasing activity GO:0140306. LolD supplies ATP hydrolysis for extraction from the outer leaflet of the inner membrane, not cargo passage across the bilayer. The coupled contribution is represented in core_functions while the original source payload remains intact.",
        "GO:0044873": "Refine lipoprotein localization to GO:0044874 lipoprotein localization to outer membrane, the destination-specific child already carried by the protein. The LolD-powered release step supplies the outer-membrane delivery pathway.",
        "GO:0044874": "The curated target LolD assignment places Q88KY4 in the matched LolCDE release complex. ATP-driven release supplies outer-membrane-destined lipoproteins to LolA and is a step of their localization to the outer membrane, without requiring LolD itself to reside there.",
        "GO:0042953": "Retain the historical transport proposal: the curated Q88KY4 LolD ATPase supplies energy directly to lipoprotein release in LolCDE. LolD therefore performs transport work through ATP-driven cargo release, not terminal membrane insertion. GO:0042953 and GO:0044874 are not ancestors or descendants of one another in the checked ancestry.",
        "GO:0089705": "Refine protein localization to outer membrane to the supported lipoprotein-specific descendant GO:0044874 already carried by the target. This identifies the demonstrated cargo class of LolCDE without asserting that LolD acts on every outer-membrane protein.",
        "GO:0140306": "Retain the historical release proposal as a coupled contribution: the LolD ATPase dimer supplies ATP hydrolysis, while LolC/LolE recognize and extract cargo. Positive assembled-complex architecture and target LolD identity support core contributes_to semantics, not autonomous release by isolated Q88KY4.",
    },
}
for g, rr in reasons.items():
    for term, reason in rr.items():
        row(doc("PSEPK", g), term)["review"]["reason"] = reason
for g, acc, locus in [("lolC", "Q88KY5", "PP_2154"), ("lolE", "Q88KY3", "PP_2156")]:
    d = doc("PSEPK", g)
    role = g[-1].upper()
    for x in d["existing_annotations"]:
        term = x["term"]["id"]
        texts = {
            "GO:0005886": f"{acc} has four predicted transmembrane helices and LolC/E-specific TIGR02212/IPR011925 signatures, supporting integral inner-membrane location. The {locus} locus identifies the {g} paralog; the shared PTHR30489:SF0 assignment alone does not distinguish LolC from LolE.",
            "GO:0016020": "Refine membrane to plasma membrane GO:0005886, the supported descendant already carried by the target. Its four predicted transmembrane helices and inner-membrane LolCDE role support this specificity.",
            "GO:0042953": f"The target {g} locus and LolC/E-specific signatures support a membrane subunit of the lipoprotein-release complex. E. coli reconstitution establishes that the assembled machinery performs cargo release to LolA; this is a conserved complex-dependent transport contribution, not isolated {role}-subunit transport.",
            "GO:0044874": f"The {g} subunit contributes to release of outer-membrane-destined lipoproteins from the inner membrane. This is the first transport step of outer-membrane localization, supported by matched target identity and the ortholog complex mechanism; it does not locate {g} in the outer membrane.",
            "GO:0098797": f"The target membrane topology and {locus} identity within the lolCDE locus support membership in the inner-membrane release complex. The E. coli structural complex contains LolC/LolE and the LolD ATPase dimer, supporting this assembly inference.",
            "GO:0140306": f"Retain the historical proposal as contribution to the complete recognition-and-release activity of assembled LolCDE. Positive structural evidence places membrane subfunctions in the LolC/LolE heterodimer and ATP hydrolysis in LolD. Target {g} identity supports the coupled role; shared family membership alone or isolated-subunit autonomy is not assumed.",
        }
        x["review"]["reason"] = texts[term]
for g in ["lolA", "lolB", "lolC", "lolD", "lolE"]:
    mark(
        "PSEPK",
        g,
        "Replace copied cross-gene and repeated generic caveats with annotation-specific reasoning; keep shared ortholog scope in notes and source assessments.",
    )
# Source relation: broad positive within relation is compatible, but less precise than supported participation.
d = doc("FLAJ1", "Fjoh_2111")
v = d["existing_annotations"][0]["review"]
v["reason"] = (
    "PMID:40050408 identifies the target as native UW101 LolA1; deletion/complementation and reduced outer-membrane GldJ/GldK abundance establish a trafficking role. Specific LolA architecture supports an inferred carrier mechanism, not purified target transfer kinetics. The source relation acts_upstream_of_or_within_positive_effect includes participation within the process and is compatible with these data, so the biological transport claim remains ACCEPT. For this mechanistic synthesis, involved_in would express the inferred carrier role more precisely; the source-relation check below does not edit the immutable qualifier or relabel ECO:0007744 as a target IDA assay. GO:0044874 is independently supported as destination-specific localization in the core summary, but is not a descendant replacement for GO:0042953. Keeping both supported process concepts in the core does not itself require manufacturing an additional annotation row. Gliding and T9SS defects remain downstream consequences, not new autonomous functions."
)
v["source_defects"] = [
    {
        "defect_type": "WRONG_QUALIFIER",
        "resource": "CACAO",
        "slot": "Qualifier",
        "requested_change": "CHECK",
        "asserted_value": "acts_upstream_of_or_within_positive_effect",
        "corrected_value": "involved_in",
        "confidence": "SUSPECTED",
        "explanation": "Consider the more precise involved_in relation for the combined native trafficking phenotype and specific LolA carrier architecture. The existing broad relation includes within and is not demonstrably false. This is a request to review relation precision, not a confirmed error, a change to the source evidence code, or a claim of purified target transport kinetics.",
        "supported_by": copy.deepcopy(v["supported_by"][:2]),
        "report_status": "NOT_REPORTED",
    }
]
mark(
    "FLAJ1",
    "Fjoh_2111",
    "Retain compatible broad source claim; explicitly distinguish inferred direct participation and supported core localization from annotation-row completeness, with a suspected source relation-precision CHECK.",
)
# Preserve source payloads and lifecycle before writing.
for n, why in changes.items():
    old = B["reviews"][n]
    d = D[n]
    assert [
        {k: v for k, v in x.items() if k != "review"}
        for x in old["existing_annotations"]
    ] == [
        {k: v for k, v in x.items() if k != "review"} for x in d["existing_annotations"]
    ]
    p = R / n
    p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
    org = p.parts[-3]
    g = p.parts[-2]
    notes = p.parent / f"{g}-notes.md"
    prior = A / "prior-notes" / f"{org}-{g}.md"
    before = (
        prior.read_text()
        if prior.exists()
        else (notes.read_text() if notes.exists() else "")
    )
    prior.parent.mkdir(exist_ok=True)
    if not prior.exists():
        prior.write_text(before)
    shared = (
        " Target KT2440 roles are conserved-function inferences from specific identity/architecture and ortholog experiments; no cited E. coli assay is represented as a measurement of this target."
        if org == "PSEPK"
        else ""
    )
    notes.write_text(
        before
        + "\n\n## PR6188 follow-up (2026-11-07)\n\n"
        + " ".join(why)
        + shared
        + " Original annotation payloads, qualifiers and proposal lifecycle are unchanged. See analysis/module_audits/bacterial_lol_lipoprotein_trafficking/review-followup/decisions.md for source and ontology adjudication.\n"
    )
(A / "changed-genes.json").write_text(
    json.dumps([{"path": n, "changes": w} for n, w in changes.items()], indent=2) + "\n"
)
print("changed", len(changes))
