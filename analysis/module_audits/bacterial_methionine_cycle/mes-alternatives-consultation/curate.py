"""Curate source-bounded MesD/MesX and MesB gene reviews from immutable seeds."""

import copy
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = json.loads((HERE / "baseline.json").read_text())


def evidence(pmid, quote):
    text = (ROOT / f"publications/PMID_{pmid}.md").read_text()
    assert quote in text, (pmid, quote)
    return {"reference_id": "PMID:" + pmid, "supporting_text": quote}


def source(org, gene, quote, section):
    p = ROOT / f"genes/{org}/{gene}/{gene}-uniprot.txt"
    assert quote in p.read_text()
    return {
        "reference_id": f"file:{org}/{gene}/{gene}-uniprot.txt",
        "record_section": [section],
        "supporting_text": quote,
    }


def ref(d, pmid, statement, quote, notes):
    text = (ROOT / f"publications/PMID_{pmid}.md").read_text()
    meta = yaml.safe_load(text.split("---")[1])
    q = evidence(pmid, quote)
    d.setdefault("references", []).append(
        {
            "id": q["reference_id"],
            "title": meta["title"],
            "reference_review": {
                "relevance": "HIGH",
                "correctness": "VERIFIED",
                "review_notes": notes,
            },
            "findings": [{"statement": statement, "supporting_text": quote}],
        }
    )


def raw_ref(d, org, gene, statement):
    d.setdefault("references", []).append(
        {
            "id": f"file:{org}/{gene}/{gene}-uniprot.txt",
            "title": f"UniProtKB record for {gene}",
            "reference_review": {
                "relevance": "HIGH",
                "correctness": "VERIFIED",
                "review_notes": "Used for sequence/locus/domain identity. Submitter or ProtNLM protein names and ARBA-only cofactor predictions are not independent functional evidence.",
            },
            "findings": [{"statement": statement}],
        }
    )


def main():
    docs = {k: copy.deepcopy(v["review"]) for k, v in BASE["seeds"].items()}
    d = docs["ACIAD/ACIAD3523"]
    d["description"] = (
        "ACIAD3523 encodes MesD, a compact catalytic-barrel methionine synthase associated with the neighboring MesX protein. Native Acinetobacter baylyi ADP1 genetics supports methionine synthesis without added cobalamin. The protein lacks the N-terminal folate-binding barrel of canonical MetE. MesD-family evidence supports sulfur methyl transfer to homocysteine, with conserved catalytic zinc coordination; the physiological methyl donor and purified ADP1 reaction remain unidentified. Aerobic dependence was established in comparative MesD/MesX complementation rather than in an isolated ADP1 enzyme assay."
    )
    ev = [
        evidence(
            "33534785",
            "ACIAD3523 (UniProt:Q6F6Z8) is required for methionine synthesis in the absence of cobalamin, and so is the adjacent gene ACIAD3524.",
        ),
        evidence("33534785", "ACIAD3523 lacks the N-terminal folate-binding domain"),
        source("ACIAD", "ACIAD3523", "DR   Pfam; PF01717; Meth_synt_2; 1.", "DR:Pfam"),
    ]
    d["existing_annotations"][0]["review"] = {
        "summary": "MesD supports homocysteine methylation, but the canonical folate-triglutamate donor is not supported.",
        "action": "MODIFY",
        "reason": "Native ADP1 methionine auxotrophy and the exact MesD identity support the final homocysteine-methylation role. The single catalytic barrel lacks the folate-binding domain, and MesD/MesX comparative genetics establishes MetF-independent activity. The original electronic EC/family mapping incorrectly fixes the methyl donor. S-methyltransferase activity retains the supported chemistry without inventing the physiological donor or treating S. koreensis complementation as a purified ADP1 assay.",
        "proposed_replacement_terms": [
            {"id": "GO:0008172", "label": "S-methyltransferase activity"}
        ],
        "supported_by": ev,
    }
    zinc = [
        evidence(
            "33534785",
            "The zinc-binding residues are highly conserved in the MesA, MesB, and MesD families (Fig 4).",
        ),
        source(
            "ACIAD",
            "ACIAD3523",
            "DR   InterPro; IPR016456; Met_Synthase_cat.",
            "DR:InterPro",
        ),
    ]
    d["existing_annotations"][1]["review"] = {
        "summary": "Conserved zinc coordination supports the MesD catalytic homocysteine-activation site.",
        "action": "ACCEPT",
        "reason": "The target is the experimentally identified MesD-family prototype, and the primary comparative analysis identifies conserved zinc-binding residues and a zinc-containing homolog structure. This supports a catalytic-site inference for ADP1, not a measurement of native metal occupancy. Zinc is integral to the inferred reaction, so uncertainty about direct occupancy is stated explicitly rather than encoded as a peripheral-function decision. The ARBA-only UniProt cofactor note is not the evidence used.",
        "supported_by": zinc,
    }
    d["core_functions"] = [
        {
            "description": "MesD-family sulfur methyl transfer to homocysteine during methionine synthesis, with MesX required physiologically; ADP1 chemistry is inferred from native genetics and catalytic architecture, and its methyl donor remains unknown.",
            "molecular_function": {
                "id": "GO:0008172",
                "label": "S-methyltransferase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0071265", "label": "L-methionine biosynthetic process"}
            ],
            "supported_by": ev + zinc,
        }
    ]
    ref(
        d,
        "18319726",
        "Native ADP1 genetics distinguishes the methionine requirement of the gene then called metE from the dispensability of metH without coenzyme B12.",
        "the metE mutant, obtained in presence of coenzyme-B12, is auxotrophic for methionine.",
        "Full text read. Native ADP1 deletion phenotypes are direct target evidence; the historical metE label does not establish a folate donor. No purified MesD activity is claimed.",
    )
    ref(
        d,
        "18840283",
        "The native model/phenotype study identifies ACIAD3523 as the B12-independent methionine-synthesis route and notes that B12 availability gates MetH rescue.",
        "Since coenzyme-B12 is neither synthesized by A. baylyi nor provided in the experimental media, the ΔACIAD3523 mutant was unable to use the MetH enzyme to synthesize methionine.",
        "Full text read. This confirms target locus and growth-condition scope, not purified substrate chemistry. The older canonical metE name is revised by the later MesD analysis.",
    )
    ref(
        d,
        "33534785",
        "The exact ADP1 protein is designated MesD, a catalytic barrel lacking the canonical folate-binding domain; comparative S. koreensis assays establish aerobic MesD/MesX function without MetF.",
        "We will call these proteins MesD and MesX.",
        "Full text read, including ADP1 genetics discussion, S. koreensis fitness and heterologous complementation methods, functional-residue analysis and the speculative MesX discussion. Aerobic dependence and donor independence are comparative system evidence; the ADP1 physiological donor is not identified.",
    )
    raw_ref(
        d,
        "ACIAD",
        "ACIAD3523",
        "The record maps the 344-residue ACIAD3523 protein to the MetE-like catalytic barrel PF01717 and PTHR30519; that broad family assignment does not establish folate-dependent MetE chemistry.",
    )
    d["suggested_questions"] = [
        {
            "question": "What physiological methyl donor supplies ADP1 MesD, and does MesX deliver a methylated intermediate or generate a diffusible donor?"
        }
    ]
    d["suggested_experiments"] = [
        {
            "description": "Determine the methyl donor and MesX requirement with purified ADP1 proteins while testing aerobic dependence independently of cellular growth rescue.",
            "experiment_type": "biochemical mechanism",
        }
    ]

    d = docs["ACIAD/ACIAD3524"]
    d["description"] = (
        "ACIAD3524 encodes MesX, a member of the former DUF1852 family required for the MesD-associated, cobalamin-independent methionine-synthesis route in Acinetobacter baylyi ADP1. Native deletion causes methionine auxotrophy and expression of ACIAD3524 restores prototrophy. Related MesD/MesX pairs support aerobic methionine synthesis in heterologous complementation, but the molecular action of MesX remains unresolved. Methyl-donor generation or transfer is a hypothesis; independent oxidase activity, a bound methyl carrier, and a stable MesD–MesX catalytic complex have not been established."
    )
    ref(
        d,
        "18319726",
        "Native ADP1 loss and complementation directly establish a requirement for ACIAD3524 in methionine synthesis under the tested growth conditions.",
        "We have shown that the ACIAD3524 mutant is auxotrophic for methionine, whereas prototrophy is restored by complementation with ACIAD3524.",
        "Full text and complementation methods read. The construct uses the ADP1 coding sequence. Necessity and rescue do not identify the molecular work performed by MesX or prove autonomous methyltransferase activity.",
    )
    ref(
        d,
        "33534785",
        "ACIAD3524 is MesX/DUF1852; proposed methyl provision and oxidative chemistry are mechanistic hypotheses, not demonstrated activities.",
        "Instead, we predict that MesX provides methyl groups to MesD, either by covalently binding the methyl group, or by forming a methylated substrate that MesD can act on.",
        "Full text read. The aerobic complementation experiments use S. koreensis genes in E. coli. The section on MesX molecular function is explicitly predictive; it does not justify an oxidase or methyl-carrier GO assertion for ADP1.",
    )
    raw_ref(
        d,
        "ACIAD",
        "ACIAD3524",
        "Official InterPro IPR015004 and Pfam PF08908 identify the MesX family. No PANTHER cross-reference is present in the immutable record.",
    )
    d["references"][-1]["findings"][0]["supporting_text"] = (
        "DR   InterPro; IPR015004; MesX."
    )
    d["references"][-1]["findings"][0]["record_section"] = ["DR:InterPro"]
    d["existing_annotations"] = []
    d["suggested_questions"] = [
        {
            "question": "What molecular reaction or structural contribution does MesX perform, and is its role direct methyl provision, donor synthesis, or another enabling function?"
        },
        {
            "question": "Does ADP1 MesX form a stable functional complex with MesD, or supply a diffusible metabolite?"
        },
    ]
    d["suggested_experiments"] = [
        {
            "description": "Identify the product or intermediate generated by MesX and determine whether it supports MesD-dependent homocysteine methylation; distinguish a stable complex from metabolite supply.",
            "experiment_type": "biochemical mechanism",
        }
    ]

    d = docs["DEHMC/cbdbA481"]
    d["description"] = (
        "cbdbA481 encodes the compact MesB-type methionine synthase of Dehalococcoides mccartyi CBDB1. Purified untagged recombinant protein transfers a methyl group from methylcobalamin to homocysteine, forming methionine in anoxic assays. The enzyme lacks the folate-binding half of canonical MetE and does not use methyl-tetrahydrofolate triglutamate in the tested reaction. The physiological corrinoid donor remains unidentified: transfer from the AcsCD corrinoid iron-sulfur protein is a proposed route, not a demonstrated native transfer reaction. The protein does not rescue an E. coli metE deletion under the tested complementation conditions."
    )
    ev = [
        evidence(
            "32034217",
            "The enzymatic activity of purified core-MetECBDB was tested using methylcob(III)alamin as methyl donor and homocysteine as methyl acceptor.",
        ),
        evidence(
            "32034217",
            "the formation of methionine ([M\u2009+\u2009H]+ \u2009=\u2009150.0583\u2009m/z) during the enzymatic reaction was verified via liquid chromatography-mass spectrometry (LC-MS)",
        ),
        source(
            "DEHMC",
            "cbdbA481",
            "DR   EMBL; AJ965256; CAI82680.1; -; Genomic_DNA.",
            "DR:EMBL",
        ),
    ]
    d["existing_annotations"] = [
        {
            "term": {"id": "GO:0008172", "label": "S-methyltransferase activity"},
            "evidence_type": "IDA",
            "original_reference_id": "PMID:32034217",
            "qualifier": "enables",
            "review": {
                "summary": "Purified CBDB1 MesB directly methylates homocysteine using methylcobalamin in vitro.",
                "action": "NEW",
                "reason": "The exact cbdbA481/CAI82680 protein was produced untagged, purified, identified by peptide mass spectrometry and assayed with methylcobalamin and homocysteine. No-enzyme, no-homocysteine and E. coli crude-extract controls were negative, while methionine product was confirmed by LC-MS. GO0008172 captures the directly demonstrated sulfur methyl transfer without imposing folate, SAM or another untested physiological donor. Current narrower donor-specific GO terms do not match this reaction. This is an independent experimentally supported activity gap in a zero-row seed; no process annotation is added merely for coverage.",
                "supported_by": ev,
            },
        }
    ]
    d["core_functions"] = [
        {
            "description": "Catalyzes methylcobalamin-dependent sulfur methyl transfer to homocysteine, producing methionine in the purified anoxic assay. Native AcsCD donor coupling and complete native-cycle flux are unproven.",
            "molecular_function": {
                "id": "GO:0008172",
                "label": "S-methyltransferase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0071265", "label": "L-methionine biosynthetic process"}
            ],
            "supported_by": ev,
        }
    ]
    ref(
        d,
        "32034217",
        "Purified CBDB1 cbdbA481 protein catalyzes methionine formation from methylcobalamin and homocysteine with controlled substrate and enzyme omissions.",
        "The enzymatic activity of purified core-MetECBDB was tested using methylcob(III)alamin as methyl donor and homocysteine as methyl acceptor.",
        "Full text read, including untagged expression/purification, LC-MS identity/product verification, methylcobalamin assay controls, folate-negative assay, failed E. coli complementation and the hypothetical AcsCD route. Direct target biochemical evidence is distinct from a native physiological donor or flux experiment.",
    )
    d["references"][-1]["findings"].extend(
        [
            {
                "statement": "The folate-triglutamate control did not produce methionine with core-MetE, whereas canonical E. coli MetE did.",
                "supporting_text": "No L-methionine was formed in the presence of core-MetECBDB",
            },
            {
                "statement": "Direct methyl transfer from AcsCD/CoFeSP to MesB remains a hypothesis.",
                "supporting_text": "We speculate that the methyl group is directly transferred from the CoFeSP to the core-MetECBDB",
            },
        ]
    )
    ref(
        d,
        "33534785",
        "The characterized Dehalococcoides core synthase defines the MesB family, distinguished from aerobic MesD and canonical two-barrel MetE.",
        "MesB uses methylcobalamin, but not 5-methyl-THF, as a substrate in vitro",
        "Full text read. This primary comparative analysis contextualizes the direct CBDB1 enzyme study; its CoFeSP donor model remains a hypothesis.",
    )
    raw_ref(
        d,
        "DEHMC",
        "cbdbA481",
        "The current A0A916P3S8 record maps CBDB1 locus cbdbA481 to CAI82680.1 and 343 residues, matching the primary target. The ProtNLM name is not treated as functional evidence; no PANTHER assignment is present.",
    )
    d["suggested_questions"] = [
        {
            "question": "Which physiological corrinoid donor methylates CBDB1 MesB, and is AcsCD-to-MesB transfer direct or mediated by an unidentified participant?"
        },
        {
            "question": "Can a specific methylcobalamin:homocysteine S-methyltransferase GO term distinguish this reaction from folate-dependent methionine synthase activity?"
        },
    ]
    d["suggested_experiments"] = [
        {
            "description": "Establish the physiological methyl donor and test whether a defined corrinoid protein supplies methyl groups to MesB without an intervening folate reaction.",
            "experiment_type": "biochemical donor assignment",
        }
    ]

    for key, d in docs.items():
        d["status"] = "COMPLETE"
        for r in d.get("references", []):
            if r["id"].startswith("GO_REF:"):
                r["reference_review"] = {
                    "relevance": "LOW",
                    "correctness": "VERIFIED",
                    "review_notes": "Annotation-provenance method, not independent biological evidence. The original machine-sourced term and evidence payload are preserved while the assertion is reviewed against primary sources.",
                }
        p = ROOT / "genes" / key / (key.split("/")[1] + "-ai-review.yaml")
        p.write_text(yaml.safe_dump(d, sort_keys=False, width=100, allow_unicode=True))
    print(
        "Curated three gene reviews; two original payloads preserved; one direct MF proposal added."
    )


if __name__ == "__main__":
    main()
