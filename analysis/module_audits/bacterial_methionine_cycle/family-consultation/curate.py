"""Apply bounded manual family judgments to the captured original documents."""

import copy
import csv
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = json.loads((HERE / "baseline.json").read_text())
TERMS = {
    x["id"]: x["name"]
    for x in json.loads((HERE / "go-terms.json").read_text())["results"]
}


def support(name, quote):
    path = (HERE / name).resolve()
    assert quote in path.read_text(), (name, quote)
    return {
        "reference_id": "file:" + str(path.relative_to(ROOT)),
        "supporting_text": quote,
    }


def pub(pmid, quote):
    assert quote in (ROOT / "publications" / f"PMID_{pmid}.md").read_text()
    return {"reference_id": "PMID:" + pmid, "supporting_text": quote}


def add_ref(d, evidence):
    for s in evidence:
        rid = s["reference_id"]
        if not any(r["id"] == rid for r in d.setdefault("references", [])):
            title = rid.removeprefix("file:").split("/")[-1]
            if rid.startswith("PMID:"):
                text = (ROOT / "publications" / ("PMID_" + rid[5:] + ".md")).read_text()
                title = yaml.safe_load(text.split("---")[1])["title"]
            d["references"].append({"id": rid, "title": title})


def set_node(d, go, reason, evidence, assessment=None):
    for n in d["node_assessments"]:
        if n["asserted_term"]["id"] == go:
            n["assessment_reason"] = reason
            if assessment:
                n["assessment"] = assessment
            n["supported_by"] = evidence
    add_ref(d, evidence)


def append_raw(d, family, go, reason, evidence, assessment="SOUND"):
    rows = list(
        csv.DictReader(
            (ROOT / "interpro/panther" / family / (family + "-paint.tsv")).open(),
            delimiter="\t",
        )
    )
    r = next(
        r
        for r in rows
        if r["go_id"] == go
        and not any(
            n["node_id"] == "PANTHER:" + r["node"] and n["asserted_term"]["id"] == go
            for n in d["node_assessments"]
        )
    )
    n = {
        "node_id": "PANTHER:" + r["node"],
        "asserted_term": {"id": go, "label": TERMS[go]},
        "evidence": r["evidence"],
        "negated": r["negated"] == "true",
        "paint_snapshot": r["date"],
        "seeds": [{"id": s} for s in r["seeds"].split("|")],
        "assessment": assessment,
        "assessment_reason": reason,
        "supported_by": evidence,
    }
    tax = r["taxon"].removeprefix("taxon:")
    labels = {
        "2": "Bacteria",
        "6072": "Eumetazoa",
        "71275": "rosids",
        "117571": "Euteleostomi",
    }
    if tax:
        n["node_taxon"] = {"id": "NCBITaxon:" + tax, "label": labels[tax]}
    d["node_assessments"].append(n)
    add_ref(d, evidence)


def main():
    docs = {
        Path(p).name.split("-")[0]: copy.deepcopy(x["document"])
        for p, x in BASE["reviews"].items()
    }
    d = docs["PTHR11964"]
    ev = [
        support(
            "P0A817-uniprot.json",
            "Catalyzes the formation of S-adenosylmethionine (AdoMet) from methionine and ATP.",
        ),
        support("Q88D60-uniprot.json", "Belongs to the AdoMet synthase family"),
    ]
    for go in ["GO:0004478", "GO:0006556"]:
        set_node(
            d,
            go,
            "The official tree places the assertion at the common MetK/MAT ancestor. Conserved AdoMet-synthase architecture and experimentally curated E. coli catalysis support ancestral SAM formation across the catalytic family; the KT2440 assignment is HAMAP-supported orthology, not a native assay. Regulatory MAT beta subunits are not being inferred from this catalytic family.",
            ev,
        )
    for t in d["term_assessments"]:
        t["scope_reason"] = (
            "Conserved catalytic MetK/MAT architecture and the ancestral PAINT placement support SAM synthesis. Curated E. coli chemistry independently anchors the reaction; this does not impose universal oligomer stoichiometry or cellular regulation."
        )
        t["supported_by"] = ev
    append_raw(
        d,
        "PTHR11964",
        "GO:0048269",
        "The stored PAINT gain is restricted to the vertebrate subtree, not the bacterial root. This preserves the distinct eukaryotic MAT-complex annotation and does not transfer its beta-subunit architecture to bacterial MetK.",
        [support("PTHR11964-tree.json", "PTN002633074")],
    )
    d["coherence_reason"] = (
        "The catalytic family conserves ATP-dependent SAM formation. Isozyme regulation and oligomer composition vary; these differences do not change the net core reaction."
    )

    d = docs["PTHR23420"]
    d["subfamilies"][0]["description"] = (
        "Contains canonical bacterial/fungal AhcY/SAH1 enzymes and additional members within the AHCYL loss subtree; SF0 alone is not a catalytic discriminator."
    )
    positive = [
        support(
            "P23526-uniprot.json",
            "Catalyzes the hydrolysis of S-adenosyl-L-homocysteine to form adenosine and homocysteine (PubMed:10933798).",
        ),
        support("A0A140FWS3-uniprot.json", "MF_00563"),
    ]
    negative = [
        support(
            "Q80SW1-uniprot.json",
            "recombinant AHCYL1 expressed in bacteria shows no hydrolase activity, nor does it affect the enzyme activity of AHCY",
        ),
        support("PTHR23420-tree.json", "PTN001158976"),
    ]
    d["coherence_reason"] = (
        "Canonical AhcY/SAH1/AHCY enzymes hydrolyze SAH, whereas AHCYL regulators have a directly supported activity loss. The IKR subtree includes SF0 as well as SF2/SF3, so SF0 alone cannot encode the catalytic boundary."
    )
    set_node(
        d,
        "GO:0004013",
        "The ancestral hydrolytic reaction is supported by canonical AHCY enzymes, conditional on the existing descendant IKR at PTN001158976. The loss is not ignored: its subtree includes SF0 members as well as SF2/SF3. The positive ancestor and negative descendant describe different evolutionary scopes.",
        positive + negative,
    )
    set_node(
        d,
        "GO:0033353",
        "Canonical hydrolases directly recycle homocysteine. The root also includes nonhydrolytic AHCYL regulators, and the hydrolase IKR is term-specific: it does not automatically stop this process annotation. A universal cycle-participation placement is unresolved; regulatory or SAH-sensor functions are not themselves proof of chemical recycling.",
        positive + negative,
        "UNRESOLVED",
    )
    append_raw(
        d,
        "PTHR23420",
        "GO:0004013",
        "The raw IKR stops ancestral hydrolase activity on the AHCYL-related subtree. Directly curated mouse AHCYL1 recombinant assays show no hydrolase activity, and the official topology places the rat/human/mouse AHCYL members inside this subtree. The subfamily labels are not treated as the loss boundary; SF0 also occurs below this node. No residue position or independent catalytic-loss mechanism is invented.",
        negative,
        "LOSS_SUPPORTED",
    )
    for t in d["term_assessments"]:
        t["scope"] = "UNRESOLVED"
        t.pop("applicable_subfamilies", None)
        t["scope_reason"] = (
            "Canonical catalytic members are positive, but the formerly listed SF0 includes descendants of the experimentally supported AHCYL loss node. Use target-specific catalytic evidence and the PAINT loss boundary, not a whole SF0 or family grant. The loss remains machine-readable in node_assessments."
        )
        t["supported_by"] = positive + negative
    add_ref(d, positive + negative)

    d = docs["PTHR46832"]
    ev = [
        support(
            "P0AF12-uniprot.json",
            "Catalyzes the irreversible cleavage of the glycosidic bond in both 5'-methylthioadenosine (MTA) and S-adenosylhomocysteine (SAH/AdoHcy)",
        ),
        support(
            "Q9KXN0-uniprot.json",
            "Catalyzes the hydrolysis of futalosine (FL) to dehypoxanthine futalosine (DHFL) and hypoxanthine, a step in the biosynthesis of menaquinone (MK, vitamin K2).",
        ),
    ]
    for go in ["GO:0008782", "GO:0008930"]:
        set_node(
            d,
            go,
            "The official ancestral node includes both the Pfs/MTAN SF1 branch and the experimentally characterized futalosine-hydrolase SF2 branch. E. coli Pfs directly supports the stated reaction, but MqnB chemistry does not establish universal SAH/MTA turnover. Its alternate substrate alone also does not demonstrate a secondary-activity loss or locate a pruning point.",
            ev,
            "UNRESOLVED",
        )
    for t in d["term_assessments"]:
        t["scope"] = "UNRESOLVED"
        t.pop("applicable_subfamilies", None)
        t["scope_reason"] = (
            "E. coli Pfs is a directly supported positive and SF1 is the canonical Pfs/MTAN lineage. SF2 MqnB has different primary chemistry, but absent secondary SAH/MTA activity has not been demonstrated for every member. Production SUBFAMILY_ONLY would enforce a negative on all other subfamilies, so the inherited exclusionary scope is withdrawn rather than manufacture that negative. Use source-qualified Pfs representatives."
        )
        t["supported_by"] = ev
    add_ref(d, ev)

    d = docs["PTHR45833"]
    d["summary"] = (
        "Canonical MetH/MTR proteins remethylate homocysteine using a cobalamin intermediate and methyl-tetrahydrofolate, with a separate reductive-reactivation module. This PANTHER family also contains a distinct SF2 lineage with homocysteine-methyltransferase and methylenetetrahydrofolate-reductase domains; family membership alone therefore does not specify the complete MetH reaction."
    )
    d["functional_coherence"] = "MOSTLY_COHERENT"
    d["coherence_reason"] = (
        "The official tree separates canonical MetH SF1 from SF2 YitJ/MetF-like domain fusions. Q748M7 retains an official SF2 assignment; O06745 has a PANTHER-tree versus current UniProt assignment disagreement, preserved without remapping. Shared homocysteine-binding architecture is not proof of the same methyl donor or complete B12-dependent mechanism."
    )
    ev = [
        support(
            "P13009-uniprot.json",
            "Subsequently, remethylates the cofactor using methyltetrahydrofolate",
        ),
        support(
            "Q748M7-uniprot.json",
            "BIFUNCTIONAL HOMOCYSTEINE S-METHYLTRANSFERASE_5,10-METHYLENETETRAHYDROFOLATE REDUCTASE",
        ),
        support("Q748M7-uniprot.json", "PF02219"),
    ]
    set_node(
        d,
        "GO:0008705",
        "The root includes canonical MetH SF1 and structurally distinct SF2 methyltransferase/reductase fusions. Canonical MetH has direct curated support for folate-to-homocysteine methyl transfer, but the SF2 architecture does not establish that complete reaction. Scope remains unresolved, without inferring a loss from a different primary function or guessing a gain/pruning node.",
        ev,
        "UNRESOLVED",
    )
    for t in d["term_assessments"]:
        if t["assessed_term"]["id"] == "GO:0008705":
            t["scope"] = "UNRESOLVED"
            t["scope_reason"] = (
                "The family includes SF2 homocysteine-methyltransferase/MTHFR fusions as well as canonical multi-domain MetH SF1. Use complete MetH architecture and target reaction evidence to qualify a representative; family membership alone cannot guarantee the folate-dependent reaction."
            )
            t["supported_by"] = ev
    add_ref(d, ev)

    d = docs["PTHR30519"]
    d["subfamilies"][0]["description"] = (
        "Includes canonical full-length MetE (MET6, met26) and shorter architectures in the official alignment; SF0 does not establish two-barrel architecture or folate-donor specificity."
    )
    d["preferred_name"] = "MetE-related methionine synthase domains and core synthases"
    d["summary"] = (
        "Canonical two-barrel MetE proteins transfer a methyl group from polyglutamylated methyl-tetrahydrofolate to zinc-activated homocysteine. Related single catalytic barrels include folate-independent core methionine synthases, including MesD, whose activity requires MesX and oxygen in characterized bacterial systems. Isolated N-terminal MetE-like barrels also occur. Domain composition and partner context distinguish these functions; a family label does not identify the methyl donor."
    )
    d["coherence_reason"] = (
        "The family includes full-length MetE, C-terminal-only core synthases such as the MesD exemplar Q6F6Z8 and inferred KT2440 Q88JF1, and N-terminal-only Q88E31. These are different architectures, not interchangeable full MetE enzymes. No split partnership between the two KT2440 proteins is established."
    )
    ev = [
        pub(
            "33534785",
            "5-methyl-THF is not the methyl donor for MesD, that MesD requires both MesX and oxygen for activity",
        ),
        pub("33534785", "We will call these proteins MesD and MesX."),
        support("Q6F6Z8-uniprot.json", "PTHR30519"),
        support("Q88JF1-uniprot.json", "Meth_synt_2"),
        support("Q88E31-uniprot.json", "Meth_synt_1"),
    ]
    set_node(
        d,
        "GO:0003871",
        "Canonical full-length MetE provides a positive folate-dependent anchor. The wider family contains experimentally characterized MesD architecture with a different donor requirement and isolated domains. The downloaded PANTHER tree does not contain the exact Q6F6Z8/Q88JF1 target leaves, so no unsupported MesD pruning node is assigned; a universal ancestral placement is unresolved.",
        ev,
        "UNRESOLVED",
    )
    ev2 = ev + [
        support(
            "go-terms.json",
            "Catalysis of the reaction: (6S)-5-methyl-5,6,7,8-tetrahydrofolate + L-homocysteine = (6S)-5,6,7,8-tetrahydrofolate + L-methionine.",
        )
    ]
    ev2.append(
        support(
            "../ecoli-canonical-consultation/16618097-substrate-scope.md",
            "neither a substrate nor an inhibitor",
        )
    )
    set_node(
        d,
        "GO:0008705",
        "The prior reason incorrectly treated this GO definition as requiring cobalamin. It specifies the monoglutamate folate reaction, not a cofactor. The Introduction of PMID16618097 explicitly reports that monoglutamate is neither substrate nor inhibitor for canonical E. coli MetE, citing earlier biochemistry; its own assays use triglutamate. This supports a member-specific substrate correction without settling every plant seed or placing a loss node. Folate-independent core synthases cannot receive this reaction from family identity. The former categorical pruning recommendation is withdrawn; precise ancestral substrate scope remains unresolved.",
        ev2,
        "UNRESOLVED",
    )
    set_node(
        d,
        "GO:0071265",
        "Full-length MetE and characterized MesD both participate in methionine biosynthesis, but the family also includes isolated domains whose productive partners are not uniformly established. Presence of one barrel does not prove autonomous synthesis or a particular split complex; retain uncertainty at the universal node rather than excluding known positive enzymes.",
        ev,
        "UNRESOLVED",
    )
    for t in d["term_assessments"]:
        t["scope"] = "UNRESOLVED"
        t["scope_reason"] = (
            "Canonical MetE is positive, but directly characterized MesD-family proteins do not require folate and exact Q6F6Z8 is assigned to this PANTHER family. Q88JF1 is a MesD-like catalytic-barrel target; Q88E31 is a different N-terminal-only protein. Neither family identity nor a hypothetical split partnership establishes the canonical polyglutamate-folate reaction."
        )
        t["supported_by"] = ev
    append_raw(
        d,
        "PTHR30519",
        "GO:0009507",
        "The raw chloroplast gain is confined to the rosid subtree and is retained independently of the bacterial catalytic-boundary correction. It is not transferred to bacterial family members.",
        [support("PTHR30519-tree.json", "PTN008625098")],
    )
    add_ref(d, ev2)

    d = {
        "family_id": "PANTHER:PTHR35799",
        "family_name": "S-RIBOSYLHOMOCYSTEINE LYASE",
        "preferred_name": "LuxS S-ribosylhomocysteine lyase",
        "summary": "LuxS cleaves S-ribosylhomocysteine to homocysteine and 4,5-dihydroxypentane-2,3-dione (DPD). Together with Pfs this regenerates homocysteine after SAH nucleosidase cleavage. DPD gives rise to AI-2-related molecules, but signal detection and a population-dependent response require additional cellular machinery and are not established by LuxS membership alone.",
        "functional_coherence": "COHERENT",
        "coherence_reason": "The bacterial family conserves LuxS catalytic architecture and the ancestral S-ribosylhomocysteine lyase reaction. Quorum sensing is a separate context-dependent process, not a universal consequence of DPD production.",
        "reference_protein": {
            "id": "UniProtKB:P45578",
            "gene_symbol": "luxS",
            "organism": "Escherichia coli",
            "gene_review": "genes/ECOLI/luxS/luxS-ai-review.yaml",
        },
        "subfamilies": [
            {
                "subfamily_id": "PANTHER:PTHR35799:SF1",
                "label": "S-RIBOSYLHOMOCYSTEINE LYASE",
                "description": "Canonical bacterial LuxS enzymes.",
                "representative_members": [
                    {
                        "id": "UniProtKB:P45578",
                        "gene_symbol": "luxS",
                        "organism": "Escherichia coli",
                        "gene_review": "genes/ECOLI/luxS/luxS-ai-review.yaml",
                    }
                ],
                "diverged_from_family": False,
            }
        ],
        "node_assessments": [],
        "references": [],
    }
    ev = [
        support(
            "P45578-uniprot.json",
            "Catalyzes the transformation of S-ribosylhomocysteine (RHC) to homocysteine (HC) and 4,5-dihydroxy-2,3-pentadione (DPD)",
        ),
        support("P45578-uniprot.json", "Belongs to the LuxS family"),
    ]
    for go, reason in [
        (
            "GO:0043768",
            "The bacterial root encompasses the conserved LuxS catalytic family. The experimentally curated E. coli anchor supports the exact reaction; the inference rests on conserved enzyme architecture and node scope, not the number of donor records.",
        ),
        (
            "GO:0005829",
            "The bacterial LuxS clade comprises soluble enzymes of intracellular activated-methyl-cycle chemistry. Cytosolic placement is consistent with the conserved architecture and the directly annotated E. coli anchor; this is a family-level inference rather than a localization assay in every taxon.",
        ),
    ]:
        append_raw(d, "PTHR35799", go, reason, ev)
    d["term_assessments"] = [
        {
            "assessed_term": {"id": "GO:0043768", "label": TERMS["GO:0043768"]},
            "scope": "FAMILY_WIDE",
            "scope_reason": "Conserved LuxS catalysis and the bacterial ancestral placement support the exact lyase reaction. No specific AI-2 chemical form, receptor or signaling response is implied.",
            "supported_by": ev,
        },
        {
            "assessed_term": {"id": "GO:0009372", "label": TERMS["GO:0009372"]},
            "scope": "UNRESOLVED",
            "scope_reason": "DPD production can supply an AI-2 precursor, but quorum sensing additionally requires signal detection and a population-dependent response. Metabolic LuxS function alone does not establish that process in every family member.",
            "supported_by": [
                support(
                    "go-terms.json",
                    "detecting the concentration of these molecules, and triggering a signal transduction pathway when a certain threshold is reached.",
                )
            ],
        },
    ]
    add_ref(d, d["term_assessments"][1]["supported_by"])
    docs["PTHR35799"] = d
    for family, d in docs.items():
        old_notes = d.get("notes", "")
        d["notes"] = (
            str(old_notes)
            + "\n2026-11-07 bounded bacterial-cycle consultation: official tree and MSA snapshots, current term definitions, exact target domain assignments and source-specific limits are documented in analysis/module_audits/bacterial_methionine_cycle/family-consultation/README.md. Original PAINT identities, seed lists and dates are preserved; newly represented raw rows are additive. Family-wide capacity must not substitute for the evidence-qualified target role."
        )
        d["review_status"] = "COMPLETE"
        d["reviewed_by"] = "codex"
        d["review_date"] = "2026-11-07"
        path = ROOT / "interpro/panther" / family / (family + "-review.yaml")
        path.write_text(
            yaml.safe_dump(d, sort_keys=False, width=100, allow_unicode=True)
        )
    print("Wrote", len(docs), "family reviews")


if __name__ == "__main__":
    main()
