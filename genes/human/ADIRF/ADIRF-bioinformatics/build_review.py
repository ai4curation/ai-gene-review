#!/usr/bin/env python3
"""Build genes/human/ADIRF/ADIRF-ai-review.yaml from the GOA TSV.

Design constraints, each from a recorded failure elsewhere in this campaign:

* `existing_annotations` is built by iterating the GOA TSV, so the row count and
  the WITH/FROM contents match GOA **by construction** rather than by hand, and
  `source_entities` is derived from column 11.
* Every row is a freshly-constructed dict (no shared Python objects), and the
  dumper has `ignore_aliases -> True`, so no `&id`/`*id` anchor can be emitted.
  An anchor would silently multiply one `supporting_text` across N rows and all
  three repo checkers would report N successes.
* After dumping, the raw text is re-read and checked for (a) duplicate mapping
  keys via a strict loader, (b) `&id` anchors, and (c) raw-vs-parsed
  `reference_id` counts. A duplicate key is dropped by PyYAML on parse, so no
  check that walks the parsed tree can see it.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE
while REPO != REPO.parent and not (REPO / "genes").is_dir():
    REPO = REPO.parent
if not (REPO / "genes").is_dir():
    raise SystemExit(f"could not locate the repo root above {HERE}")
GENE_DIR = REPO / "genes" / "human" / "ADIRF"
GOA = GENE_DIR / "ADIRF-goa.tsv"
OUT = GENE_DIR / "ADIRF-ai-review.yaml"

N_GOA_ROWS = 11
BIOINF = "file:human/ADIRF/ADIRF-bioinformatics/RESULTS.md"
UNIPROT_FILE = "file:human/ADIRF/ADIRF-uniprot.txt"


def T(i, l):
    return {"id": i, "label": l}


def ST(ref, text, **kw):
    d = {"reference_id": ref, "supporting_text": text}
    d.update(kw)
    return d


# --------------------------------------------------------------------------
# per-row review content, keyed on (GO id, evidence, reference, qualifier)
# --------------------------------------------------------------------------

REVIEWS: dict[tuple, dict] = {}

REVIEWS[("GO:0005634", "IBA", "GO_REF:0000033", "is_active_in")] = dict(
    action="ACCEPT",
    summary=(
        "Accepted. This is the PAN-GO curator's core-function statement for ADIRF, and its "
        "WITH/FROM names ADIRF itself (UniProtKB:Q15847) as the IBD seed alongside the node, "
        "so it is a self-referential IBA recording a human curator's judgement rather than a "
        "transfer from another species. The nucleus is independently supported by the gene's "
        "own IDA and by HPA immunofluorescence, and it is where a factor acting upstream of "
        "PPARG and CEBPA would have to act."
    ),
    reason=(
        "PANTHER:PTN008674116 reaches seven mammalian ADIRF orthologues by IBA (human, "
        "chimpanzee, gorilla, dog, pig, cow, opossum) and every one of them lists "
        "UniProtKB:Q15847 as the seed, because human ADIRF is the only member of the family "
        "with any experimental annotation. Mouse and rat are absent from that list for a "
        "concrete reason: Muroidea have no ADIRF gene at all. I note but do not act on the "
        "fact that `is_active_in` asserts the molecular function is executed in the nucleus, "
        "which is a stronger claim than `located_in` for a protein whose molecular function "
        "is entirely unknown, and that HPA calls cytosol a main location alongside "
        "nucleoplasm. Both points are raised as questions for GO_Central rather than used to "
        "downgrade a curator's deliberate core-function call."
    ),
    supported_by=[
        ST("PMID:23239344",
           "Our data demonstrated that C10orf116 is highly expressed in adipose tissue and "
           "is localized primarily within the nucleus."),
        ST(BIOINF,
           "IBD seeds named in the WITH/FROM, with the `db` field read rather than flattened away: UniProtKB:Q15847 x14. The seed is the gene under review, so both IBA rows are **self-referential**: **True**."),
    ],
    propagation_review=dict(
        root_cause="NO_FAILURE_CORE",
        source_entities=[
            dict(source_id="PANTHER:PTN008674116",
                 source_label="PANTHER ancestral node for the ADIRF family",
                 source_status="SUPPORTS_TRANSFER",
                 comment=(
                     "A PANTHER internal tree node, not a protein. It reaches 7 mammalian "
                     "ADIRF orthologues by IBA, all seeded from human Q15847.")),
            dict(source_id="UniProtKB:Q15847",
                 source_label="human ADIRF (the gene under review; self-referential IBD seed)",
                 source_status="SUPPORTS_TRANSFER",
                 comment=(
                     "Self-referential: the seed is the target. Per campaign convention this "
                     "is valid and records a PAN-GO curator judging nuclear residence core, "
                     "not a circular chain. Q15847 carries its own IDA to GO:0005634.")),
        ],
    ),
)

REVIEWS[("GO:0045600", "IBA", "GO_REF:0000033", "involved_in")] = dict(
    action="ACCEPT",
    summary=(
        "Accepted. The PAN-GO curators selected positive regulation of fat cell "
        "differentiation as ADIRF's core biological process, seeded from the gene's own IDA. "
        "This is the best-supported process claim for the gene and is the one UniProt's "
        "FUNCTION line leads with."
    ),
    reason=(
        "Same self-referential node as the nucleus row: PANTHER:PTN008674116 plus "
        "UniProtKB:Q15847 as the IBD seed, propagating to seven mammalian orthologues. The "
        "term is correct for human ADIRF on its own experimental evidence, so the IBA adds "
        "curatorial weight rather than new evidence. Note the boundary the underlying "
        "experiment sets: it was ectopic expression in mouse 3T3-L1 preadipocytes, a lineage "
        "that has no ADIRF gene, so it shows ADIRF can promote adipogenic differentiation "
        "and not that adipogenesis requires it. That distinction is recorded as a knowledge "
        "gap rather than used to reject the term. Notably PAN-GO chose this term and not "
        "GO:0045944 from the same paper, which is why GO:0045944 is treated as non-core here."
    ),
    supported_by=[
        ST("PMID:23239344",
           "Over-expression studies in 3T3-L1 cells indicated that it up-regulates the "
           "levels of CCAAT/enhancer binding protein α (C/EBPα) and PPARγ and "
           "promotes adipogenic differentiation starting from the early stage of "
           "adipogenesis."),
        ST(UNIPROT_FILE,
           "CC   -!- FUNCTION: Plays a role in fat cell development; promotes adipogenic"),
    ],
    propagation_review=dict(
        root_cause="NO_FAILURE_CORE",
        source_entities=[
            dict(source_id="PANTHER:PTN008674116",
                 source_label="PANTHER ancestral node for the ADIRF family",
                 source_status="SUPPORTS_TRANSFER",
                 comment=(
                     "Internal tree node reaching 7 mammalian gene products by IBA. Six are "
                     "genuine ADIRF orthologues of 75-76 aa aligning over 73-76 of the 76 "
                     "human residues at 81.6-100% identity, so the transfer to human is "
                     "sound and no granularity problem arises for this gene. The seventh, "
                     "UniProtKB:A0A5F8H3S4 (Monodelphis domestica), is NOT an orthologue - a "
                     "447-aa tandem-repeat protein aligning over 62 of 76 residues at 15.8% "
                     "identity - and it receives both of this node's terms. That is a defect "
                     "in the node's membership, not in the transfer to human, and its root "
                     "cause is upstream of PAINT: opossum has a real ADIRF gene "
                     "(NCBI Gene 100020286) but UniProt's proteome for the species contains "
                     "no ADIRF-sized member of the family, so the tree was given the wrong "
                     "sequence. Raised in suggested_questions.")),
            dict(source_id="UniProtKB:Q15847",
                 source_label="human ADIRF (the gene under review; self-referential IBD seed)",
                 source_status="SUPPORTS_TRANSFER",
                 comment=(
                     "Self-referential seed carrying its own IDA to GO:0045600. Valid; "
                     "records a core-function judgement, not a circular transfer.")),
        ],
    ),
)

_CIRCULAR_PREAMBLE = (
    "InterPro's IPR034450 is a single-family signature whose entire curated basis is this "
    "gene: its InterPro description is written from human ADIRF's own papers, and it has "
    "exactly one reviewed Swiss-Prot member, human ADIRF itself. interpro2go maps IPR034450 "
    "to exactly two terms, GO:0045600 and GO:0005634. "
)

REVIEWS[("GO:0005634", "IEA", "GO_REF:0000120", "located_in")] = dict(
    action="ACCEPT",
    summary=(
        "Accepted as correct but redundant. The term is right - ADIRF has its own IDA to "
        "nucleus and a more specific HPA IDA to nucleoplasm - but this row carries no "
        "independent evidence, because both tokens in its WITH/FROM trace back to the same "
        "experiment the IDA row already records."
    ),
    reason=(
        _CIRCULAR_PREAMBLE
        + "The second WITH/FROM token, UniProtKB-SubCell:SL-0191, is UniProt's own Nucleus "
        "subcellular-location term, and UniProt's SUBCELLULAR LOCATION line attributes it to "
        "ECO:0000269|PubMed:23239344 - the same paper as the IDA row. So both routes into "
        "this row originate in PMID:23239344. Correct term, zero added information; ACCEPT "
        "rather than REMOVE because nothing false is asserted. The WITH/FROM names no ARBA "
        "rule id, so there was no rule to fetch at rest.uniprot.org/arba/ despite the "
        "GO_REF:0000120 reference."
    ),
    supported_by=[
        ST(UNIPROT_FILE,
           "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:23239344}."),
    ],
    propagation_review=dict(
        root_cause="EVIDENCE_CIRCULAR_OR_REDUNDANT",
        failure_modes=["CIRCULAR_PROPAGATION"],
        source_entities=[
            dict(source_id="InterPro:IPR034450",
                 source_label="InterPro family 'Adipogenesis regulatory factor'",
                 source_status="CIRCULAR_OR_REDUNDANT",
                 comment=(
                     "Family entry whose description and GO mapping derive from human "
                     "ADIRF's own literature, and whose only reviewed member is human ADIRF. "
                     "Mapping it back onto human ADIRF adds no evidence.")),
            dict(source_id="UniProtKB-SubCell:SL-0191",
                 source_label="UniProt subcellular location 'Nucleus'",
                 source_status="CIRCULAR_OR_REDUNDANT",
                 comment=(
                     "UniProt's own Nucleus annotation for Q15847 is attributed to "
                     "ECO:0000269|PubMed:23239344, the same paper behind the IDA row.")),
        ],
    ),
)

REVIEWS[("GO:0045600", "IEA", "GO_REF:0000002", "involved_in")] = dict(
    action="ACCEPT",
    summary=(
        "Accepted as correct but redundant. Pure InterPro2GO from IPR034450, a signature "
        "built from this gene's own papers, so for human ADIRF the row restates the IDA. The "
        "term is right; the route is circular. The same mapping over-reaches badly on other "
        "species, which is filed as an upstream question rather than acted on here."
    ),
    reason=(
        _CIRCULAR_PREAMBLE
        + "Measured over the whole propagation (withFrom=InterPro:IPR034450, fully "
        "paginated, 1512 annotations asserted complete): GO:0045600 reaches 723 gene "
        "products, of which only 130 are ADIRF-sized (60-90 aa) while 504 are larger than "
        "200 aa and therefore cannot be orthologues of a 76-aa protein, and 237 are "
        "non-vertebrate metazoans. Human ADIRF is not one of the mis-hit recipients, so this "
        "row's action turns on the human evidence alone and is ACCEPT. The upstream defect - "
        "an Ala/Gln-rich 76-aa signature matching long tandem-repeat proteins in molluscs, "
        "insects and nematodes and carrying a mammal-derived adipocyte term to them - is "
        "raised in suggested_questions for InterPro and GO."
    ),
    supported_by=[
        ST("PMID:23239344",
           "Over-expression studies in 3T3-L1 cells indicated that it up-regulates the "
           "levels of CCAAT/enhancer binding protein α (C/EBPα) and PPARγ and "
           "promotes adipogenic differentiation starting from the early stage of "
           "adipogenesis."),
        ST(BIOINF,
           "| GO:0045600 positive regulation of fat cell differentiation | 723 | 130 | 504 | 89 |"),
        ST(BIOINF,
           "Recipients that are both non-vertebrate and larger than 200 aa: **217**."),
    ],
    propagation_review=dict(
        root_cause="EVIDENCE_CIRCULAR_OR_REDUNDANT",
        failure_modes=["CIRCULAR_PROPAGATION"],
        source_entities=[
            dict(source_id="InterPro:IPR034450",
                 source_label="InterPro family 'Adipogenesis regulatory factor'",
                 source_status="CIRCULAR_OR_REDUNDANT",
                 comment=(
                     "For human ADIRF the mapping is circular: the entry's description cites "
                     "this gene's own papers and its only reviewed member is human ADIRF. "
                     "Separately, and not a reason to change this row, the same entry carries "
                     "GO:0045600 to 723 gene products of which 504 exceed 200 aa - a "
                     "composition-driven match on a low-complexity 76-aa sequence, quantified "
                     "in the bioinformatics results.")),
        ],
    ),
)

REVIEWS[("GO:0005515", "IPI", "PMID:32296183", "enables")] = dict(
    action="MARK_AS_OVER_ANNOTATED",
    summary=(
        "Marked as over-annotated. The interaction with IL18 is a single unreplicated "
        "yeast-two-hybrid hit from the HuRI systematic screen, its apparent triplicate "
        "support is one screen logged under three assay versions, and `protein binding` "
        "conveys nothing about what ADIRF does. No informative replacement term is proposed "
        "because no functional consequence of the interaction has ever been measured."
    ),
    reason=(
        "UniProt records NbExp=3 for this pair, but IntAct returns a single interaction "
        "record (EBI-11784632, MI-score 0.56) logged under three sub-methods - two hybrid "
        "array, two hybrid prey pooling approach, and validated two hybrid - and the source "
        "paper states it screened with a panel of three Y2H assay versions. So NbExp counts "
        "assay versions, not independent experiments. Neither ADIRF nor IL18 is named in the "
        "paper's text; the pair comes from the supplementary interaction list. There is no "
        "orthogonal assay and no follow-up literature linking the two proteins. "
        "Three checks that would have strengthened the case came back NEGATIVE and are "
        "reported as such rather than omitted: (1) the partner accession resolves to reviewed "
        "canonical Swiss-Prot IL18 at the full 193 aa, so there is no TrEMBL or partial-ORFeome "
        "substitution; (2) neither protein is a promiscuous hub - IL18 has 15 distinct IntAct "
        "partners and ADIRF has 4; (3) the interaction is not topologically impossible, because "
        "IL18 is a leaderless cytokine whose precursor UniProt describes as cytosolic and ADIRF "
        "is nucleoplasmic and cytosolic, so both could meet in the cytosol. The verdict "
        "therefore rests only on the absence of replication and the uninformativeness of the "
        "term, not on any argument that the observation is impossible."
    ),
    supported_by=[
        ST("PMID:32296183",
           "We screened this search space a total of nine times with a panel of three Y2H "
           "assay versions"),
        ST(UNIPROT_FILE,
           "CC       Q15847; Q14116: IL18; NbExp=3; IntAct=EBI-7162516, EBI-3910835;"),
    ],
)

REVIEWS[("GO:0005654", "IDA", "GO_REF:0000052", "located_in")] = dict(
    action="ACCEPT",
    summary=(
        "Accepted, and it is the most specific supported nuclear term for this gene. HPA's "
        "immunofluorescence for antibody HPA026810 has reliability 'Supported', and the same "
        "antibody has an unusually clean specificity control: it gives no signal in any mouse "
        "tissue, and mouse has no ADIRF gene."
    ),
    reason=(
        "GO:0005654 is a verified descendant of GO:0005634, so this row is a refinement of "
        "the nucleus rows rather than an independent claim, and it is the term core_functions "
        "should carry for the nuclear compartment. The antibody control is worth stating: "
        "PMID:31945134 used Sigma HPA026810 - the same antibody underlying this HPA call - "
        "for immunohistochemistry across mouse tissues and saw no ADIRF staining anywhere, "
        "which is the expected result for a species carrying a 43-kb deletion of the locus. "
        "An antibody that stains human tissue and is blank in the species lacking the gene is "
        "about as well controlled as a localisation reagent gets. "
        "Separately, HPA's own record gives TWO main locations, Nucleoplasm and Cytosol, and "
        "GOA imported only the nucleoplasm half; the missing GO:0005829 row is proposed as a "
        "NEW annotation below rather than treated as a defect in this row."
    ),
    supported_by=[
        ST("PMID:31945134",
           "Finally, mouse did not stain for LPHN2/ADGRL2 in lung non-vascular SMC or for "
           "ADIRF in any tissue."),
        ST(BIOINF,
           "HPA record for ADIRF (ENSG00000148671), IF reliability **Supported**, main "
           "subcellular locations **Nucleoplasm, Cytosol**."),
    ],
)

_EXOSOME_SHARED = (
    "ADIRF's presence outside the cell is independently real and better supported than the "
    "exosome-specific claim: it is measured in human serum by ELISA at microgram-per-millilitre "
    "concentrations across 139 patients (PMID:33737617) and detected as an intact protein by "
    "top-down mass spectrometry in lipoaspirate fluid (PMID:26719138). Neither is in GOA. "
    "That corroboration is why this row is kept rather than marked over-annotated. It supports "
    "the parent - GO:0070062 is a verified descendant of GO:0005576 extracellular region - and "
    "not the exosome mechanism, which requires release by multivesicular-body fusion and has "
    "never been tested for ADIRF. I did not propose GO:0005576 separately because this row "
    "already entails it. The protein has no signal peptide and no transmembrane segment, so "
    "the export route is unknown; that is filed as a knowledge gap."
)

REVIEWS[("GO:0070062", "HDA", "PMID:23533145", "located_in")] = dict(
    action="KEEP_AS_NON_CORE",
    summary=(
        "Kept as non-core. A real high-throughput detection in exosomes purified from "
        "expressed prostatic secretions in urine, but one of 1046 proteins given this single "
        "term from this one paper, with no ADIRF-specific validation - and the authors "
        "themselves caution that abundant contaminating proteins in such preparations must be "
        "verified before their presence is generalised."
    ),
    reason=(
        "The reference-projection test shows this PMID annotates 1046 distinct gene products "
        "with GO:0070062 and nothing else, all HDA, all assigned by UniProt. That is a bulk "
        "import, not 1046 independent findings; ADIRF is not mentioned anywhere in the "
        "paper's narrative and the row derives from a supplementary identification list. One "
        "count I could not reconcile and am recording rather than explaining away: the paper's "
        "text says close to 900 proteins were identified in the two pools, while GOA imported "
        "1046 entities from it, and the identifications live in a supplemental table absent "
        "from the cached text. "
        + _EXOSOME_SHARED
    ),
    supported_by=[
        ST("PMID:23533145",
           "Certainly the presence of high abundant contaminating proteins, in exosome "
           "preparations from cancer-related biofluids such as EPS-urine, must be taken into "
           "account and further verified before generalizing their presence to a clinical "
           "association with the cancerous condition."),
        ST("PMID:23533145",
           "in total, close to 900 proteins were identified in the two EPS-urine exosome "
           "pools"),
        ST("PMID:33737617",
           "cut-off value was determined as 18.7 µg/mL, with a sensitivity and "
           "specificity of 84.0% and 71.7%, respectively"),
    ],
)

REVIEWS[("GO:0070062", "HDA", "PMID:19056867", "located_in")] = dict(
    action="KEEP_AS_NON_CORE",
    summary=(
        "Kept as non-core. An independent high-throughput detection, this time in exosomes "
        "from normal human urine rather than a cancer-related biofluid, which is a useful "
        "corroboration of the other GO:0070062 row - but again one of over a thousand "
        "proteins from a single study, with no ADIRF-specific validation."
    ),
    reason=(
        "This row's value relative to the PMID:23533145 row is that the source material is "
        "healthy-donor urine, so the contaminating-tumour-protein caveat that the other "
        "paper raises about itself does not apply here. Against that, the paper is cached "
        "abstract-only (full_text_available: false), so I can characterise only what the "
        "abstract states, and the reference-projection test shows it annotates 1016 distinct "
        "gene products with GO:0070062 and no other term - a bulk import. ADIRF is a small, "
        "very abundant protein and both exosome preparations are from the urogenital tract "
        "where ADIRF is well expressed, so detection is expected on abundance grounds alone. "
        + _EXOSOME_SHARED
    ),
    supported_by=[
        ST("PMID:19056867",
           "Overall, the analysis identified 1132 proteins unambiguously, including 177 that "
           "are represented on the Online Mendelian Inheritance in Man database of "
           "disease-related genes, suggesting that exosome analysis is a potential approach "
           "to discover urinary biomarkers.",
           full_text_unavailable=True),
        ST("PMID:26719138",
           "adipogenesis regulatory factor, perilipin-1 fragments, and S100A6, along with "
           "their PTMs",
           full_text_unavailable=True),
    ],
)

REVIEWS[("GO:0005634", "IDA", "PMID:23239344", "located_in")] = dict(
    action="ACCEPT",
    summary=(
        "Accepted. Direct observation of nuclear localisation in the paper that first "
        "characterised the gene, independently corroborated by HPA immunofluorescence with a "
        "well-controlled antibody. Unlike the two process rows from the same paper, this one "
        "is a direct assay and IDA is the correct evidence code for it."
    ),
    reason=(
        "The abstract states the localisation directly. The full text is not available "
        "(full_text_available: false) so the method is not visible to me, but the result is "
        "corroborated by an independent antibody-based dataset and by UniProt's curated "
        "SUBCELLULAR LOCATION line. One caveat is recorded as a knowledge gap rather than "
        "used against the row: at 76 aa and 7855 Da ADIRF is far below the nuclear-pore "
        "passive-diffusion limit and has no annotated NLS, so nuclear presence is the default "
        "expectation for a protein this small and carries little information. The paper says "
        "'primarily within the nucleus', which implies enrichment rather than mere presence, "
        "and enrichment of a freely diffusible protein requires a retention mechanism that "
        "nobody has identified."
    ),
    supported_by=[
        ST("PMID:23239344",
           "Our data demonstrated that C10orf116 is highly expressed in adipose tissue and "
           "is localized primarily within the nucleus.",
           full_text_unavailable=True),
        ST(UNIPROT_FILE,
           "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:23239344}."),
    ],
)

REVIEWS[("GO:0045600", "IDA", "PMID:23239344", "involved_in")] = dict(
    action="ACCEPT",
    summary=(
        "Accepted as the term, with a correction to the evidence code: the supporting "
        "experiment is over-expression, so this should be IMP rather than IDA. This is "
        "ADIRF's only characterised biological role and the one UniProt's FUNCTION line leads "
        "with, but the experiment shows that ADIRF can promote adipogenic differentiation, "
        "not that adipogenesis requires it."
    ),
    reason=(
        "The abstract names the assay outright as over-expression in 3T3-L1 cells, and GO's "
        "IMP definition explicitly covers over-expression and ectopic expression of wild-type "
        "genes while IDA is reserved for a direct assay of the gene product's own activity or "
        "location. The mis-coding is therefore decidable from the abstract alone and needs no "
        "full text. I did not change the term, which is well supported. "
        "A second boundary on the interpretation, measured rather than assumed: 3T3-L1 is a "
        "mouse line, and ADIRF is absent from the entire Muroidea clade - 0 genes in mouse, "
        "rat and Muroidea in NCBI Gene against positive controls of 1, 1 and 30 for ADIPOQ, "
        "with the sister rodent clade Sciuridae retaining 9 ADIRF genes so the loss is "
        "localised rather than a query artefact. PMID:31945134 identifies the mechanism as a "
        "43-kb deletion removing the promoter and first exon. So the only functional "
        "experiments on this gene are gain-of-function in a background with no endogenous "
        "orthologue, murine adipogenesis demonstrably proceeds without any ADIRF, and no "
        "loss-of-function experiment exists in any system that has the gene. That does not "
        "make the term wrong - it bounds what it means - so the requirement claim is filed as "
        "a knowledge gap rather than asserted or used to reject the row."
    ),
    supported_by=[
        ST("PMID:23239344",
           "Over-expression studies in 3T3-L1 cells indicated that it up-regulates the "
           "levels of CCAAT/enhancer binding protein α (C/EBPα) and PPARγ and "
           "promotes adipogenic differentiation starting from the early stage of "
           "adipogenesis.",
           full_text_unavailable=True),
        ST("PMID:31945134",
           "The mouse locus corresponding to human ADIRF harbors a deletion of close to 43 kb "
           "(Fig 5A). This deletion is predicted to remove the promoter and first exon of "
           "ADIRF, a sequence that encodes the first 42 amino acids of the 76 amino acid gene "
           "product."),
        ST(BIOINF,
           "ADIRF absent from Muroidea: **True**; retained in the sister rodent clade "
           "Sciuridae: **True** (9 genes)."),
    ],
    knowledge_gaps=[
        dict(gap_statement=(
            "It is unknown whether ADIRF is required for adipocyte differentiation in any "
            "cell that expresses it endogenously. Every functional experiment on the gene is "
            "ectopic over-expression in mouse 3T3-L1 preadipocytes, and the mouse lineage "
            "carries a 43-kb deletion of the ADIRF locus, so the assay system has no "
            "endogenous orthologue and murine adipogenesis proceeds without any ADIRF."),
            boundary=(
                "Established: expressing human ADIRF in 3T3-L1 cells raises C/EBP-alpha and "
                "PPAR-gamma levels and accelerates adipogenic differentiation. Not "
                "established: any loss-of-function phenotype, in any species, in any cell "
                "that has the gene."),
            gap_kind=["BIOLOGY", "CURATION"],
            dark_aspect="RESIDUAL_SUBGAP",
            status="OPEN",
            significance=(
                "Distinguishes a sufficiency claim from a necessity claim for the gene's only "
                "annotated biological process, and explains why the gene has remained dark: "
                "the standard model organism for adipose biology cannot be used, and "
                "PMID:31945134 notes ADIRF has no clear paralogue that could substitute."),
            provenance=[
                ST("PMID:23239344",
                   "Over-expression studies in 3T3-L1 cells indicated that it up-regulates "
                   "the levels of CCAAT/enhancer binding protein α (C/EBPα) and "
                   "PPARγ and promotes adipogenic differentiation starting from the "
                   "early stage of adipogenesis.",
                   full_text_unavailable=True),
                ST("PMID:31945134",
                   "deletion of this segment (and loss of ADIRF expression) occurred in the "
                   "evolutionary predecessor to mouse, rat, and hamster."),
            ]),
    ],
)

REVIEWS[("GO:0045944", "IDA", "PMID:23239344", "involved_in")] = dict(
    action="KEEP_AS_NON_CORE",
    summary=(
        "Kept as non-core. The term is the UniProt curator's reading of the full text, which "
        "I do not overrule, but it rests on the same single over-expression experiment as the "
        "GO:0045600 row - so it is a mechanistic interpretation of one result rather than an "
        "independent finding, and the PAN-GO curators reviewing the same paper selected "
        "GO:0045600 and not this term as ADIRF's core process."
    ),
    reason=(
        "What the abstract reports is a change in the levels of C/EBP-alpha and PPAR-gamma, "
        "which does not by itself localise the effect to RNA polymerase II transcription. "
        "UniProt's curator, who read the full text I cannot see, wrote that ADIRF 'stimulates "
        "transcription initiation' of these factors, and per project policy an experimental "
        "call made from the full text is not overruled from an abstract - so the term stands "
        "and this is not a MODIFY. What keeps it non-core is that no mechanism has been "
        "established: ADIRF has no annotated DNA-binding activity, no measured promoter "
        "occupancy, and no identified cofactor, so whether it acts at Pol II transcription "
        "directly or several steps upstream is unknown. The evidence code has the same "
        "problem as the GO:0045600 row - the supporting experiment is over-expression, which "
        "GO codes as IMP, not IDA."
    ),
    supported_by=[
        ST("PMID:23239344",
           "Over-expression studies in 3T3-L1 cells indicated that it up-regulates the "
           "levels of CCAAT/enhancer binding protein α (C/EBPα) and PPARγ and "
           "promotes adipogenic differentiation starting from the early stage of "
           "adipogenesis.",
           full_text_unavailable=True),
        ST("PMID:23239344",
           "C10orf16 manifested the characteristics of an adipocyte lineage-specific nuclear "
           "factor that can modulate the master adipogenesis transcription factors early "
           "during differentiation.",
           full_text_unavailable=True),
    ],
    knowledge_gaps=[
        dict(gap_statement=(
            "The mechanism by which ADIRF increases C/EBP-alpha and PPAR-gamma expression is "
            "unknown. No DNA-binding activity, promoter occupancy, chromatin association or "
            "transcriptional cofactor has been reported for the protein, so it is not known "
            "whether it acts at transcription at all or at some earlier step whose output is "
            "a change in the levels of these factors."),
            boundary=(
                "Established: ectopic ADIRF raises C/EBP-alpha and PPAR-gamma levels, and "
                "the protein is nuclear. Not established: any direct molecular interaction "
                "with DNA, chromatin, a transcription factor or the Pol II machinery."),
            gap_kind=["BIOLOGY"],
            dark_aspect="MF_DARK",
            status="OPEN",
            significance=(
                "This is the gap that makes GO:0045944 uncertain in mechanism while leaving "
                "the process term defensible, and it is why no molecular_function is asserted "
                "for this gene anywhere in this review."),
            provenance=[
                ST("PMID:23239344",
                   "C10orf16 manifested the characteristics of an adipocyte lineage-specific "
                   "nuclear factor that can modulate the master adipogenesis transcription "
                   "factors early during differentiation.",
                   full_text_unavailable=True),
            ]),
    ],
)

# --------------------------------------------------------------------------
# NEW annotations (not in GOA)
# --------------------------------------------------------------------------

NEW_ROWS = [
    dict(
        term=T("GO:0005829", "cytosol"),
        evidence_type="IDA",
        original_reference_id="GO_REF:0000052",
        qualifier="located_in",
        review=dict(
            action="NEW",
            summary=(
                "Proposed as missing. The Human Protein Atlas gives ADIRF TWO main "
                "subcellular locations, Nucleoplasm and Cytosol, from the same "
                "immunofluorescence experiment at reliability 'Supported', but GOA imported "
                "only the nucleoplasm half. GO:0005829 is absent from ADIRF's entire GOA "
                "record."
            ),
            reason=(
                "This is a gap in the HPA import rather than a disagreement with it, and it "
                "was verified against a positive control so that a zero cannot be a broken "
                "query: GAPDH is also called Cytosol by HPA and does carry GO:0005829 in "
                "GOA, with the term id resolved through the same location-to-term mapping "
                "used for ADIRF. GO:0005829 is not a descendant of GO:0005634, so this adds "
                "genuinely new information rather than restating the nuclear rows. "
                "This row rests on the HPA immunofluorescence call alone, which is sufficient "
                "for it. It deliberately does NOT lean on the sub-diffusion-limit argument: at "
                "7855 Da ADIRF is below the nuclear-pore passive-diffusion limit, but that "
                "predicts BOTH compartments and so discounts both equally - it cannot be "
                "evidence for one of them. That argument therefore appears only in the "
                "knowledge gap asking whether nuclear enrichment is active. "
                "Proposed as located_in only - no claim is made that any ADIRF function is "
                "executed in the cytosol, and cytosol is deliberately absent from "
                "core_functions locations for that reason."
            ),
            supported_by=[
                ST(BIOINF,
                   "HPA record for ADIRF (ENSG00000148671), IF reliability **Supported**, "
                   "main subcellular locations **Nucleoplasm, Cytosol**."),
                ST(BIOINF,
                   "Terms expected from HPA's main locations: GO:0005654, GO:0005829. "
                   "Missing from ADIRF's GOA record entirely: **GO:0005829**."),
            ],
        ),
    ),
]

EXPECTED_ANNOTATIONS = N_GOA_ROWS + len(NEW_ROWS)

# --------------------------------------------------------------------------
# references
# --------------------------------------------------------------------------

REFERENCES = [
    dict(id="GO_REF:0000002",
         title="Gene Ontology annotation through association of InterPro records with GO terms",
         findings=[]),
    dict(id="GO_REF:0000033",
         title="Annotation inferences using phylogenetic trees",
         findings=[]),
    dict(id="GO_REF:0000052",
         title="Gene Ontology annotation based on curation of immunofluorescence data",
         findings=[]),
    dict(id="GO_REF:0000120",
         title="Combined Automated Annotation using Multiple IEA Methods",
         findings=[]),
    dict(id="PMID:19056867",
         title="Large-scale proteomics and phosphoproteomics of urinary exosomes.",
         full_text_unavailable=True,
         findings=[
             dict(statement=(
                 "Profiles the proteome of exosomes from normal human urine and identifies "
                 "1132 proteins; ADIRF is one of the 1016 gene products GOA annotates to "
                 "extracellular exosome from this study, from the supplementary "
                 "identification list rather than from any ADIRF-specific result."),
                 supporting_text=(
                     "Overall, the analysis identified 1132 proteins unambiguously, including "
                     "177 that are represented on the Online Mendelian Inheritance in Man "
                     "database of disease-related genes, suggesting that exosome analysis is "
                     "a potential approach to discover urinary biomarkers."),
                 full_text_unavailable=True),
             dict(statement=(
                 "Defines the vesicle population being sampled, which is what makes "
                 "GO:0070062 rather than a generic extracellular term the assigned "
                 "annotation."),
                 supporting_text=(
                     "Normal human urine contains large numbers of exosomes, which are 40- "
                     "to 100-nm vesicles that originate as the internal vesicles in "
                     "multivesicular bodies from every renal epithelial cell type facing the "
                     "urinary space."),
                 full_text_unavailable=True),
         ],
         reference_review=dict(
             relevance="MEDIUM",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified against the cached record. Correctly cited for a "
                 "high-throughput detection, but it is a bulk import annotating 1016 gene "
                 "products with a single term and it says nothing specific about ADIRF; "
                 "cached abstract-only. No retraction, erratum or correction found on the "
                 "PubMed record."),
         )),
    dict(id="PMID:23239344",
         title=("A Novel pro-adipogenesis factor abundant in adipose tissues and "
                "over-expressed in obesity acts upstream of PPARγ and C/EBPα."),
         full_text_unavailable=True,
         findings=[
             dict(statement=(
                 "The only functional characterisation of ADIRF in the nucleus, and the "
                 "source of three of the eleven GOA rows. The assay is explicitly "
                 "over-expression, which is why the two process rows should carry IMP rather "
                 "than IDA."),
                 supporting_text=(
                     "Over-expression studies in 3T3-L1 cells indicated that it up-regulates "
                     "the levels of CCAAT/enhancer binding protein α (C/EBPα) and "
                     "PPARγ and promotes adipogenic differentiation starting from the "
                     "early stage of adipogenesis."),
                 full_text_unavailable=True),
             dict(statement=(
                 "Direct observation of nuclear localisation, supporting the GO:0005634 IDA "
                 "row; this observation is a direct assay and IDA is correct for it."),
                 supporting_text=(
                     "Our data demonstrated that C10orf116 is highly expressed in adipose "
                     "tissue and is localized primarily within the nucleus."),
                 full_text_unavailable=True),
             dict(statement=(
                 "The authors' own summary of the inference, which is the basis for the "
                 "GO:0045944 annotation; note it is framed as characteristics rather than a "
                 "demonstrated mechanism."),
                 supporting_text=(
                     "C10orf16 manifested the characteristics of an adipocyte "
                     "lineage-specific nuclear factor that can modulate the master "
                     "adipogenesis transcription factors early during differentiation."),
                 full_text_unavailable=True),
         ],
         reference_review=dict(
             relevance="HIGH",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified against the cached record; note the source itself contains "
                 "the typo 'C10orf16' in the abstract, reproduced verbatim above. Cached "
                 "abstract-only, so claims here are bounded to what the abstract states; "
                 "UniProt's 'stimulates transcription initiation' wording comes from the full "
                 "text and is deferred to rather than re-derived. No retraction or erratum. "
                 "This paper is absent from the affinage record despite being the reference "
                 "behind three GOA rows."),
         )),
    dict(id="PMID:23533145",
         title=("In-depth proteomic analyses of exosomes isolated from expressed prostatic "
                "secretions in urine."),
         findings=[
             dict(statement=(
                 "The authors caution that abundant contaminating proteins in these "
                 "preparations require verification before their presence is generalised - "
                 "directly relevant to a small, very abundant protein like ADIRF being "
                 "detected in a urogenital-tract exosome preparation."),
                 supporting_text=(
                     "Certainly the presence of high abundant contaminating proteins, in "
                     "exosome preparations from cancer-related biofluids such as EPS-urine, "
                     "must be taken into account and further verified before generalizing "
                     "their presence to a clinical association with the cancerous "
                     "condition.")),
             dict(statement=(
                 "The paper's own protein count, which does not reconcile with the 1046 gene "
                 "products GOA annotates from it; the identifications are in a supplemental "
                 "table absent from the cached text, so the difference is recorded as "
                 "unresolved."),
                 supporting_text=(
                     "in total, close to 900 proteins were identified in the two EPS-urine "
                     "exosome pools")),
             dict(statement=(
                 "The authors note that proteins recovered in urine exosome preparations are "
                 "often simply abundant, or may exist in soluble form - a further reason the "
                 "exosome-specific claim is weaker than the extracellular one."),
                 supporting_text=(
                     "This evidence suggests that, proteins found in urine exosome "
                     "preparations are relatively abundant and thus also detected when the "
                     "whole fluid is analyzed, or alternatively, some of these proteins could "
                     "also exist as a soluble form.")),
         ],
         reference_review=dict(
             relevance="MEDIUM",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified; full text available and read. Correctly cited for the HDA "
                 "detection. ADIRF is not mentioned anywhere in the paper's text, so the "
                 "annotation rests on a supplementary list; the caveats quoted are the "
                 "authors' own. No retraction or erratum."),
         )),
    dict(id="PMID:32296183",
         title="A reference map of the human binary protein interactome.",
         findings=[
             dict(statement=(
                 "Establishes that the HuRI dataset screened with three Y2H assay versions, "
                 "which is why IntAct logs the single ADIRF-IL18 interaction under three "
                 "sub-methods and UniProt reports NbExp=3 for what is one screen."),
                 supporting_text=(
                     "We screened this search space a total of nine times with a panel of "
                     "three Y2H assay versions")),
         ],
         reference_review=dict(
             relevance="MEDIUM",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified; full text available. Correctly cited as the source of the "
                 "GO:0005515 IPI row. Neither ADIRF nor IL18 appears in the paper's text, so "
                 "the pair comes from the supplementary interaction list. The "
                 "reference-projection test is uninformative for this reference - 85,343 "
                 "annotations over 854 pages - and that is stated rather than a first-page "
                 "count being substituted. No retraction or erratum."),
         )),
    dict(id="PMID:31945134",
         title=("Tripartite factors leading to molecular divergence between human and murine "
                "smooth muscle."),
         findings=[
             dict(statement=(
                 "Identifies the genomic basis of ADIRF's absence in the mouse lineage: a "
                 "43-kb deletion removing the promoter and first exon, which encodes the "
                 "first 42 of the protein's 76 residues."),
                 supporting_text=(
                     "The mouse locus corresponding to human ADIRF harbors a deletion of "
                     "close to 43 kb (Fig 5A). This deletion is predicted to remove the "
                     "promoter and first exon of ADIRF, a sequence that encodes the first 42 "
                     "amino acids of the 76 amino acid gene product.")),
             dict(statement=(
                 "Places the loss in the common ancestor of mouse, rat and hamster, which "
                 "matches the independently measured absence of ADIRF across all of Muroidea."),
                 supporting_text=(
                     "deletion of this segment (and loss of ADIRF expression) occurred in the "
                     "evolutionary predecessor to mouse, rat, and hamster.")),
             dict(statement=(
                 "ADIRF is more abundant in arterial tissue than in the adipose tissue that "
                 "gave it its name - relevant because all eleven GOA rows are adipogenesis or "
                 "localisation and none is vascular."),
                 supporting_text=(
                     "The ADIRF gene is relatively highly expressed (over 700 RKMP in tibial "
                     "artery in GTEx [Release V6]) and more abundant in arterial than adipose "
                     "tissue where it was initially characterized.")),
             dict(statement=(
                 "Provides a specificity control for antibody Sigma HPA026810, the same "
                 "antibody behind HPA's immunofluorescence call and therefore behind the "
                 "GO:0005654 IDA row: it gives no signal in any mouse tissue, the species "
                 "lacking the gene."),
                 supporting_text=(
                     "Finally, mouse did not stain for LPHN2/ADGRL2 in lung non-vascular SMC "
                     "or for ADIRF in any tissue.")),
             dict(statement=(
                 "ADIRF has no clear paralogue, so no functional redundancy can compensate "
                 "for its absence in the mouse lineage - independently confirmed here, since "
                 "the only other human PTHR39227 entry, Q5TBU5, is an unreviewed TrEMBL "
                 "duplicate with the identical 76-aa sequence."),
                 supporting_text=(
                     "The chances that ADIRF could result in functional changes is increased "
                     "because it appears to encode a protein with no clear paralogs.")),
         ],
         reference_review=dict(
             relevance="HIGH",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified; full text available and read. This is the single most "
                 "consequential reference for interpreting ADIRF's annotations and it is "
                 "absent from GOA, from UniProt's reference list and from the affinage "
                 "record. One claim in it is NOT relied on, and is adjudicated on sequence "
                 "rather than on a symbol count: it also states ADIRF is absent from "
                 "zebrafish and lamprey. An earlier version of this review declined that on "
                 "the strength of an NCBI symbol/alias count, which is orthology asserted by "
                 "an annotation pipeline rather than measured, and is exactly the name-based "
                 "inference the rest of this analysis refuses. Aligning the actual RefSeq "
                 "proteins instead: NP_001373520.1 (Danio rerio) and XP_085644419.1 "
                 "(Trachurus japonicus) are both 81 aa and align over 71 of the 76 human "
                 "residues at 38.2% identity, passing the same coverage criterion used "
                 "throughout - with a chicken positive control, the 938-aa Cyprinus carpio "
                 "family member as a negative control that fails as expected, and only 1 of "
                 "30 composition-matched shuffles passing. So an ADIRF-like protein is "
                 "annotated in zebrafish and the paper's zebrafish claim is inconsistent with "
                 "current RefSeq annotation - though this review examined sequence, not "
                 "synteny, so it does not adjudicate the genomic-deletion argument the paper "
                 "actually makes. The mouse/rat/hamster claim, which is what this review does "
                 "rely on, is independently confirmed. No retraction or erratum."),
         )),
    dict(id="PMID:33737617",
         title=("Adipose most abundant 2 protein is a predictive marker for cisplatin "
                "sensitivity in cancers."),
         findings=[
             dict(statement=(
                 "Measures ADIRF/APM2 in human serum by ELISA at microgram-per-millilitre "
                 "concentrations in 139 patients, independently corroborating that the "
                 "protein reaches an extracellular fluid - a route absent from GOA."),
                 supporting_text=(
                     "cut-off value was determined as 18.7 µg/mL, with a sensitivity and "
                     "specificity of 84.0% and 71.7%, respectively")),
             dict(statement=(
                 "The authors treat secretion into the blood as a premise for their assay "
                 "design rather than demonstrating it, so this paper establishes that ADIRF "
                 "is present in serum but not how it gets there - and the protein has no "
                 "signal peptide or transmembrane segment."),
                 supporting_text=(
                     "To determine serum APM2 concentration as a potential biomarker of CDDP "
                     "sensitivity, as it is secreted into the blood stream, the APM2 serum "
                     "level was tested with ELISA in 71 HCC patients who were treated with "
                     "CDDP intra-arterial infusion")),
         ],
         reference_review=dict(
             relevance="MEDIUM",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified; full text available and read. Cited only for the measured "
                 "serum concentration, which is used to corroborate extracellular presence "
                 "and hence to keep rather than downgrade the GO:0070062 rows. The paper's "
                 "ERCC6L-upregulation claim rests on bioinformatic plus histological analysis "
                 "and is deliberately NOT used to support any annotation. No retraction or "
                 "erratum. Absent from the affinage record."),
         )),
    dict(id="PMID:26719138",
         title=("Lipoaspirate fluid proteome: A preliminary investigation by LC-MS "
                "top-down/bottom-up integrated platform of a high potential biofluid in "
                "regenerative medicine."),
         full_text_unavailable=True,
         findings=[
             dict(statement=(
                 "Detects intact ADIRF by top-down mass spectrometry in the acid-soluble "
                 "fraction of lipoaspirate fluid, a third independent extracellular detection "
                 "route and one from adipose tissue itself."),
                 supporting_text=(
                     "adipogenesis regulatory factor, perilipin-1 fragments, and S100A6, "
                     "along with their PTMs"),
                 full_text_unavailable=True),
         ],
         reference_review=dict(
             relevance="LOW",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified against the cached record; cached abstract-only, and the "
                 "quoted sentence is from the abstract. Corroborating only: a preliminary "
                 "two-sample study, cited for the fact of detection in an extracellular "
                 "adipose fluid and for nothing more. No retraction or erratum."),
         )),
    dict(id="PMID:19444912",
         title=("APM2 is a novel mediator of cisplatin resistance in a variety of cancer cell "
                "types regardless of p53 or MMR status."),
         full_text_unavailable=True,
         findings=[
             dict(statement=(
                 "The second phenotype attributed to ADIRF: over-expression confers cisplatin "
                 "resistance and silencing sensitises cancer cell lines. No molecular "
                 "mechanism is identified, and no GO annotation exists or is proposed for it, "
                 "because a drug-resistance phenotype is not a molecular function or a "
                 "biological process the gene participates in."),
                 supporting_text=(
                     "APM2 is a novel mediator of cisplatin resistance in a variety of cancer "
                     "cell types regardless of p53 or MMR status."),
                 full_text_unavailable=True),
         ],
         reference_review=dict(
             relevance="LOW",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified. One of the two references the affinage record returned, and "
                 "it checks out. Cited here to record why no GO annotation follows from it: "
                 "the cisplatin phenotype is downstream physiology in tumour cell lines, not "
                 "a function of the protein, and it is explicitly not proposed as a new term. "
                 "Cached abstract-only. No retraction or erratum."),
         )),
    dict(id="PMID:23467766",
         title=("Overexpression of C10orf116 promotes proliferation, inhibits apoptosis and "
                "enhances glucose transport in 3T3-L1 adipocytes."),
         full_text_unavailable=True,
         findings=[
             dict(statement=(
                 "A third over-expression study in the same mouse 3T3-L1 line, reporting "
                 "effects on proliferation, apoptosis and insulin-stimulated glucose uptake. "
                 "No GO annotation is proposed from it: it shares the interpretive limit of "
                 "PMID:23239344, being ectopic expression in a lineage with no ADIRF gene, "
                 "and the reported effects are cellular phenotypes rather than the protein's "
                 "own activity."),
                 supporting_text=(
                     "Overexpression of C10orf116 promotes proliferation, inhibits apoptosis "
                     "and enhances glucose transport in 3T3-L1 adipocytes."),
                 full_text_unavailable=True),
         ],
         reference_review=dict(
             relevance="LOW",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified. The second of the two affinage citations; it checks out. "
                 "InterPro cites this paper in its IPR034450 description, which is part of "
                 "why the InterPro2GO rows for this gene are circular. Cached abstract-only; "
                 "cited for scope rather than as support for any annotation. No retraction or "
                 "erratum."),
         )),
    dict(id="PMID:24052233",
         title=("Characterization of microRNA expression profiles in 3T3-L1 adipocytes "
                "overexpressing C10orf116."),
         full_text_unavailable=True,
         findings=[
             dict(statement=(
                 "A fourth study, again over-expression in mouse 3T3-L1. Cited to establish "
                 "the completeness of the claim that every functional experiment on ADIRF "
                 "used this one heterologous system; no annotation is drawn from it."),
                 supporting_text=(
                     "Characterization of microRNA expression profiles in 3T3-L1 adipocytes "
                     "overexpressing C10orf116."),
                 full_text_unavailable=True),
         ],
         reference_review=dict(
             relevance="LOW",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified. Cached abstract-only. Cited only to support the scope claim "
                 "that all ADIRF functional work is 3T3-L1 over-expression. No retraction or "
                 "erratum."),
         )),
    dict(id="PMID:36261012",
         title="Circadian lncRNA ADIRF-AS1 binds PBAF and regulates renal clear cell tumorigenesis.",
         findings=[
             dict(statement=(
                 "Concerns ADIRF-AS1, a distinct antisense lncRNA gene at the ADIRF locus, "
                 "not the ADIRF protein. Recorded to make the boundary explicit: 10 of the 37 "
                 "PubMed records matching ADIRF in title or abstract are about this lncRNA, "
                 "and none of ADIRF's eleven GOA rows cites any of them."),
                 supporting_text=(
                     "Circadian lncRNA ADIRF-AS1 binds PBAF and regulates renal clear cell "
                     "tumorigenesis.")),
         ],
         reference_review=dict(
             relevance="LOW",
             correctness="VERIFIED",
             review_notes=(
                 "Title verified; full text available. Deliberately included as a NEGATIVE "
                 "control on the review's scope rather than as evidence: it documents that "
                 "the locus/transcript confusion hazard was checked and that the GO record is "
                 "free of it. Nothing in this review's verdicts depends on it. Separately "
                 "noted: another ADIRF-AS1 paper, PMID:35937391, is a Retracted Publication, "
                 "and nothing here rests on it either."),
         )),
    dict(id="file:human/ADIRF/ADIRF-deep-research-affinage.md",
         title="Affinage mechanistic annotation for ADIRF (human)",
         findings=[],
         reference_review=dict(
             relevance="LOW",
             correctness="LOW_QUALITY",
             review_notes=(
                 "Recorded so the provider's performance on this gene is measurable, and "
                 "deliberately NOT cited as supporting_text for any annotation. Precision is "
                 "fine: gates_passed is True, both citations (PMID:19444912, PMID:23467766) "
                 "are real numeric PubMed ids rather than bioRxiv DOIs in a PMID-shaped "
                 "field, both resolve to papers genuinely about this gene under its former "
                 "names, and neither is retracted. Recall for annotation purposes is close to "
                 "zero: it returned none of the four PMIDs GOA cites - including "
                 "PMID:23239344, the reference behind three of the eleven rows and the only "
                 "nuclear characterisation of the protein - and it missed PMID:31945134 (the "
                 "43-kb Muroid deletion and the arterial expression data), which is the "
                 "single most consequential fact about this gene, and PMID:33737617 (serum at "
                 "microgram-per-millilitre). Marked LOW_QUALITY for one substantive "
                 "inaccuracy rather than for its citations: the narrative asserts that no "
                 "binding partner has been characterised, while a curated IL18 interaction "
                 "sits in the GO record it did not consult. Its empty molecular_activity, "
                 "localization, partners and complexes fields are, by contrast, correct for "
                 "this gene."),
         )),
    dict(id=BIOINF,
         title="ADIRF (Q15847) bioinformatics results",
         findings=[]),
    dict(id=UNIPROT_FILE,
         title="UniProtKB entry Q15847 (ADIRF_HUMAN)",
         findings=[]),
]

# --------------------------------------------------------------------------
# core functions, gaps, questions, experiments
# --------------------------------------------------------------------------

CORE_FUNCTIONS = [
    dict(
        description=(
            "Acts in the nucleus of cells of the adipocyte lineage to raise the expression of "
            "the master adipogenic transcription factors PPARG and CEBPA at early stages of "
            "preadipocyte differentiation, thereby promoting adipogenic differentiation. No "
            "molecular function is asserted: the protein is 76 residues with no domain, no "
            "resolved structure and no measured catalytic, nucleic-acid-binding or "
            "protein-binding activity beyond a single unreplicated two-hybrid hit, so how it "
            "produces this effect is unknown. The supporting experiment is ectopic expression "
            "in a mouse cell line whose lineage lacks the gene, so this records what ADIRF "
            "can do rather than a demonstrated requirement."
        ),
        directly_involved_in=[T("GO:0045600", "positive regulation of fat cell differentiation")],
        # Both nucleus and nucleoplasm are listed even though the second entails
        # the first: three separate GOA rows assert the parent explicitly (IDA,
        # IBA and IEA) while HPA's immunofluorescence supports the child, so each
        # is independently attested. Cytosol is deliberately absent -- see the
        # GO:0005829 row, which is proposed as located_in only.
        locations=[T("GO:0005634", "nucleus"), T("GO:0005654", "nucleoplasm")],
        supported_by=[
            ST("PMID:23239344",
               "Over-expression studies in 3T3-L1 cells indicated that it up-regulates the "
               "levels of CCAAT/enhancer binding protein α (C/EBPα) and PPARγ "
               "and promotes adipogenic differentiation starting from the early stage of "
               "adipogenesis.",
               full_text_unavailable=True),
            ST("PMID:23239344",
               "Our data demonstrated that C10orf116 is highly expressed in adipose tissue "
               "and is localized primarily within the nucleus.",
               full_text_unavailable=True),
        ],
    ),
]

KNOWLEDGE_GAPS = [
    dict(gap_statement=(
        "ADIRF has no known molecular function of any kind. It is a 76-residue protein whose "
        "UniProt feature table contains a single CHAIN 1..76 and nothing else - no domain, no "
        "signal peptide, no transmembrane segment, no active or binding site - with no "
        "resolved experimental structure, and no catalytic, nucleic-acid-binding or "
        "cofactor-binding activity has ever been measured."),
        boundary=(
            "Established: subcellular distribution (nucleoplasm and cytosol), a "
            "pro-adipogenic effect on ectopic expression, and one two-hybrid interaction with "
            "IL18. Not established: anything about what the polypeptide itself does at the "
            "molecular level."),
        gap_kind=["BIOLOGY"],
        dark_aspect="MF_DARK",
        status="OPEN",
        significance=(
            "This is why core_functions asserts a biological process and locations but no "
            "molecular_function or contributes_to_molecular_function, and why the only MF row "
            "in GOA is the uninformative GO:0005515. It also means there is no fold from "
            "which an activity could have been mis-inferred - the campaign's usual "
            "fold-to-activity propagation lead has nothing to find on this gene."),
        provenance=[
            ST(UNIPROT_FILE, "FT   CHAIN           1..76"),
        ]),
    dict(gap_statement=(
        "The route by which ADIRF reaches the extracellular space is unknown. The protein is "
        "measured in human serum at microgram-per-millilitre concentrations, detected as an "
        "intact species in lipoaspirate fluid, and recovered from two independent urinary "
        "exosome proteomes - yet it has no signal peptide and no transmembrane segment, so "
        "classical secretion is unavailable to it."),
        boundary=(
            "Established: the protein is present in serum, lipoaspirate fluid and exosome "
            "preparations. Not established: whether it is packaged into extracellular "
            "vesicles, released by an unconventional secretion pathway, or liberated from "
            "damaged cells; and whether serum ADIRF is vesicle-associated or free."),
        gap_kind=["BIOLOGY"],
        dark_aspect="CC_DARK",
        status="OPEN",
        significance=(
            "Determines whether GO:0070062 is the right extracellular term or whether a "
            "generic extracellular-region annotation is all the data support. The two "
            "existing GO:0070062 rows already entail GO:0005576, so no additional term was "
            "proposed; resolving this gap is what would justify keeping or refining them."),
        provenance=[
            ST("PMID:33737617",
               "cut-off value was determined as 18.7 µg/mL, with a sensitivity and "
               "specificity of 84.0% and 71.7%, respectively"),
            ST(UNIPROT_FILE, "FT   CHAIN           1..76"),
        ]),
    dict(gap_statement=(
        "ADIRF's function in vascular smooth muscle is entirely uncharacterised, despite "
        "artery being the tissue in which the gene is most abundant. Its GO record contains no "
        "vascular annotation of any kind."),
        boundary=(
            "Established: high arterial expression, and immunohistochemical detection in "
            "human vascular and non-vascular smooth muscle. Not established: any function, "
            "partner or process in that tissue."),
        gap_kind=["BIOLOGY", "CURATION"],
        dark_aspect="BP_DARK",
        status="OPEN",
        significance=(
            "The gene's name, its InterPro entry name, its PANTHER family name and all eleven "
            "of its GOA rows derive from the tissue where it was first found rather than the "
            "tissue where it is most abundant. No GO action is proposed because no functional "
            "vascular experiment exists to annotate; this is recorded so the asymmetry is "
            "visible to the next curator."),
        provenance=[
            ST("PMID:31945134",
               "The ADIRF gene is relatively highly expressed (over 700 RKMP in tibial artery "
               "in GTEx [Release V6]) and more abundant in arterial than adipose tissue where "
               "it was initially characterized."),
        ]),
    dict(gap_statement=(
        "Whether ADIRF is actively retained in the nucleus is unknown. At 76 residues and "
        "7855 Da it is far below the nuclear-pore passive-diffusion limit and has no annotated "
        "nuclear localisation signal, so its presence in the nucleus is the default "
        "expectation and carries little information; the reported enrichment there would "
        "require a retention mechanism that nobody has identified."),
        boundary=(
            "Established: the protein is detected in nucleoplasm and in cytosol by "
            "immunofluorescence, and described as localised primarily within the nucleus. Not "
            "established: whether nuclear accumulation is active, what would retain it, or "
            "whether the two compartments simply reflect free equilibration."),
        gap_kind=["BIOLOGY"],
        dark_aspect="CC_DARK",
        status="OPEN",
        significance=(
            "Bears directly on whether GO_Central's is_active_in GO:0005634 qualifier is the "
            "right one for this gene, which is raised as a question rather than acted on, and "
            "on why cytosol is proposed as located_in only and kept out of core_functions "
            "locations."),
        provenance=[
            ST("PMID:23239344",
               "Our data demonstrated that C10orf116 is highly expressed in adipose tissue "
               "and is localized primarily within the nucleus.",
               full_text_unavailable=True),
        ]),
]

QUESTIONS = [
    dict(question=(
        "Should the InterPro2GO mapping from IPR034450, or the signature itself, be "
        "restricted? Measured with a fully paginated QuickGO query "
        "(withFrom=InterPro:IPR034450, 1512 annotations, completeness asserted): GO:0045600 "
        "positive regulation of fat cell differentiation reaches 723 gene products, of which "
        "only 130 are ADIRF-sized (60-90 aa) while 504 exceed 200 aa and 237 are "
        "non-vertebrate metazoans - among them a 2304-aa Toxocara canis protein, a 1578-aa "
        "Melipona quadrifasciata protein and nine Mizuhopecten yessoensis proteins. The cause "
        "is that human ADIRF is a 76-aa low-complexity sequence whose three commonest residues "
        "are 43.4% of it, and PTHR39227 accordingly contains 556 members over 200 aa including "
        "39 fungal, 16 bacterial and 15 plant entries. Aligning human ADIRF against five "
        "genuine orthologues and twelve oversized recipients separates them cleanly on "
        "coverage: orthologues align over 75-76 of 76 residues, oversized members over 23-65, "
        "and the oversized members are tandem-repeat proteins with 11/22/33-residue periods. "
        "Note this is a signature-specific problem, not a general indictment of InterPro2GO: "
        "the mapping consists of exactly two terms and both are correct for the gene the entry "
        "was built from. There is a reciprocal half worth fixing at the same time: the "
        "family has 50 teleost members in UniProtKB and not one of them is ADIRF-sized, so its "
        "entire fish content is oversized spurious matches, while the genuine teleost ADIRF "
        "proteins - for example NP_001373520.1 in Danio rerio, 81 aa, aligning over 71 of the "
        "76 human residues - are annotated in RefSeq and absent from the family. The signature "
        "is thus simultaneously over-inclusive of unrelated repeat proteins and under-inclusive "
        "of real orthologues."),
        experts=["InterPro curators", "GO Central"]),
    dict(question=(
        "Should UniProtKB:A0A5F8H3S4 be removed from PANTHER subfamily PTHR39227:SF1, and is "
        "the Monodelphis domestica proteome missing its real ADIRF? PANTHER node "
        "PTN008674116 propagates both of human ADIRF's IBA terms - including is_active_in "
        "GO:0005634, which asserts the molecular function is executed there - to 7 gene "
        "products. Six are genuine orthologues of 75-76 aa aligning over 73-76 of the 76 "
        "human residues at 81.6-100% identity. The seventh, A0A5F8H3S4, is a 447-aa "
        "'Uncharacterized protein' built from a 22-residue tandem repeat at 85.4% "
        "periodicity whose three commonest residues are 52.1% of the sequence; it aligns "
        "over only 62 of 76 residues at 15.8% identity, inside the same band as the "
        "unambiguously spurious IPR034450 matches. Importantly the root cause looks to be "
        "upstream of PAINT rather than in the tree curation: NCBI Gene has a real 3-exon "
        "ADIRF gene for this species (GeneID 100020286, ADIPOQ control non-zero for the same "
        "taxon), but UniProt's Monodelphis proteome contains no ADIRF-sized member of the "
        "family, so the only candidate the HMM had to match was the repeat protein. The "
        "actionable items are therefore (a) whether the family HMM should admit a 447-aa "
        "tandem-repeat protein at all, and (b) whether the missing opossum ADIRF protein "
        "should be added to the reference proteome. Stated as a question rather than a "
        "finding about PAINT, whose placement of the six real orthologues is correct."),
        experts=["PANTHER curators", "GO Central", "UniProt proteomes"]),
    dict(question=(
        "Is GO:0045600's taxon constraint of only_in_taxon NCBITaxon:6072 (Eumetazoa) intended "
        "to admit invertebrates? The constraint machinery is demonstrably working - of the 723 "
        "recipients of GO:0045600 via IPR034450, zero are outside Metazoa, so the fungal, plant "
        "and bacterial family members are correctly excluded, and GO:0005634's Eukaryota "
        "constraint likewise excludes the bacterial and archaeal ones. But 237 recipients are "
        "invertebrate metazoans, and they pass the constraint. GO:0045444's definition is 'The "
        "process in which a relatively unspecialized cell acquires specialized features of an "
        "adipocyte, an animal connective tissue cell specialized for the synthesis and storage "
        "of fat' - so the question is whether an insect fat body cell or a mollusc storage cell "
        "satisfies that differentia. If not, the constraint may want tightening toward "
        "Vertebrata. Raised as a question because the answer determines whether the invertebrate "
        "annotations are a constraint problem or purely a signature problem."),
        experts=["GO Central", "GO taxon constraint working group"]),
    dict(question=(
        "Should the two PMID:23239344 process rows (GO:0045600 and GO:0045944) be recoded from "
        "IDA to IMP? The abstract states the assay as 'Over-expression studies in 3T3-L1 "
        "cells', and GO's IMP definition explicitly covers over-expression and ectopic "
        "expression of wild-type genes, whereas IDA is for a direct assay of the gene product's "
        "own activity or location. The GO:0005634 row from the same paper is a genuine direct "
        "observation and should stay IDA. Flagged rather than acted on because the review "
        "schema records term-level actions, not evidence-code corrections."),
        experts=["UniProt curators", "GO Central"]),
    dict(question=(
        "Is is_active_in the right qualifier for GO_Central's GO:0005634 IBA on a gene with no "
        "known molecular function? is_active_in asserts that the molecular function is executed "
        "in the nucleus, but ADIRF has no measured molecular function of any kind, and the "
        "Human Protein Atlas gives it two main locations - Nucleoplasm and Cytosol - from one "
        "immunofluorescence experiment at reliability Supported. At 7855 Da the protein is well "
        "below the nuclear-pore passive-diffusion limit and has no annotated NLS, so dual "
        "distribution is the physical expectation. The row was accepted as a deliberate "
        "core-function judgement by curators who read the same literature; the question is "
        "whether located_in would be the safer qualifier until a molecular function is known."),
        experts=["GO Central", "PAN-GO curators"]),
    dict(question=(
        "Should GOA import the cytosol half of HPA's ADIRF immunofluorescence call? HPA gives "
        "Nucleoplasm and Cytosol as co-equal main locations for ENSG00000148671 (antibody "
        "HPA026810, IF reliability Supported), but the GO_REF:0000052 row carries only "
        "GO:0005654, and GO:0005829 is absent from ADIRF's whole GOA record. Verified against a "
        "positive control - GAPDH is also called Cytosol by HPA and does carry GO:0005829 - so "
        "this is a gap in the import rather than a broken query. Proposed here as a NEW row."),
        experts=["HPA curators", "GOA curators"]),
    dict(question=(
        "Should UniProt entry Q15847 drop or qualify its two keyword-derived GO cross-references? "
        "The entry carries 'DR   GO; GO:0030154; P:cell differentiation; IEA:UniProtKB-KW.' and "
        "'DR   GO; GO:0006351; P:DNA-templated transcription; IEA:UniProtKB-KW.', neither of "
        "which is entailed by the gene's evidence. I fetched the relations rather than inferring "
        "them from labels: GO:0045944 is not a descendant of GO:0006351, and GO:0045600 is a "
        "descendant of neither GO:0030154 nor GO:0045444, because GO deliberately keeps "
        "regulation out of the is_a hierarchy. GO:0006351 is 'The synthesis of an RNA transcript "
        "from a DNA template', i.e. it says ADIRF performs transcription rather than regulating "
        "it. GOA no longer imports the Swiss-Prot keyword route - GO_REF:0000043 returns 0 human "
        "annotations against 139,714 for GO_REF:0000044 - so these claims are now invisible from "
        "GOA and there is no GO row to correct; it is a UniProt-side request only."),
        experts=["UniProt curators"]),
    dict(question=(
        "Should UniProt entry Q15847 add the arterial expression data and the two missing primary "
        "references? Its TISSUE SPECIFICITY line leads with adipose tissue, but PMID:31945134 "
        "reports over 700 RKMP in tibial artery in GTEx and states the gene is more abundant in "
        "arterial than adipose tissue. That paper is also the only source for the 43-kb Muroid "
        "deletion that explains why the gene has no mouse orthologue - highly relevant to anyone "
        "planning experiments - and PMID:33737617 provides the only quantitative measurement of "
        "the protein in a body fluid. Neither is in the entry's reference list."),
        experts=["UniProt curators"]),
    dict(question=(
        "Is ADIRF's real biology vascular rather than adipose, and if so what accounts for the "
        "adipose framing? The gene's approved name, its InterPro entry name, its PANTHER family "
        "name and all eleven of its GOA rows derive from its discovery as the second most "
        "abundant transcript in adipose tissue, but expression is higher in artery, and the one "
        "study that examined vascular smooth muscle found it there while noting its complete "
        "absence in mouse. No GO action is proposed because no vascular function has been "
        "assayed."),
        experts=["vascular smooth muscle biologists", "adipose tissue biologists"]),
]

EXPERIMENTS = [
    dict(hypothesis=(
        "ADIRF is required for, and not merely sufficient to accelerate, adipocyte "
        "differentiation in cells that express it endogenously."),
        description=(
            "CRISPR knockout and inducible degron-tagged depletion of ADIRF in a human "
            "preadipocyte model that expresses it endogenously (for example SGBS cells or "
            "primary human adipose-derived stromal cells), scoring differentiation by lipid "
            "accumulation and by PPARG and CEBPA induction. This is the experiment the entire "
            "existing literature lacks: every published functional result is ectopic "
            "expression in mouse 3T3-L1 cells, and the mouse lineage carries a 43-kb deletion "
            "of the ADIRF locus, so no loss-of-function has ever been tested in a background "
            "that has the gene. Reconstitution with the human protein should rescue."),
        experiment_type="loss-of-function genetics"),
    dict(hypothesis=(
        "ADIRF acts through a protein partner rather than through an intrinsic biochemical "
        "activity."),
        description=(
            "Proximity-dependent biotinylation (TurboID or BioID2) with ADIRF fused at each "
            "terminus, performed in parallel in differentiating human preadipocytes and in "
            "primary human vascular smooth muscle cells, with a size-matched inert bait as "
            "control. Because ADIRF is only 76 residues, run a free-tag control to subtract "
            "compartment background, and compare nuclear and cytosolic fractions separately. "
            "This directly targets the gene's largest gap - no molecular function of any kind "
            "is known - and the vascular arm addresses the tissue where the gene is most "
            "abundant but wholly unannotated."),
        experiment_type="proximity labelling proteomics"),
    dict(hypothesis=(
        "ADIRF associates with chromatin at the PPARG and CEBPA loci, as its GO:0045944 "
        "annotation implies."),
        description=(
            "CUT&RUN or ChIP-seq for endogenous ADIRF (or a knock-in epitope tag to avoid "
            "over-expression artefacts) in differentiating human preadipocytes, with matched "
            "input and an IgG control, asking whether the protein occupies the PPARG and CEBPA "
            "regulatory regions. A negative result would be informative: it would argue that "
            "ADIRF acts upstream of transcription rather than at it, and would justify "
            "generalising GO:0045944 to a term that does not assert action at Pol II."),
        experiment_type="chromatin occupancy"),
    dict(hypothesis=(
        "Nuclear enrichment of ADIRF is active rather than a consequence of free diffusion "
        "through the nuclear pore."),
        description=(
            "Compare the nucleocytoplasmic distribution of ADIRF-GFP with ADIRF fused to a "
            "tandem multimeric tag that raises the fusion above the passive-diffusion limit "
            "(for example ADIRF-3xGFP, roughly 90 kDa), alongside free GFP and free 3xGFP "
            "controls, and measure exchange by fluorescence loss in photobleaching. If "
            "nuclear enrichment persists for the oversized fusion, retention is active and a "
            "retention factor exists to be found; if it collapses, the observed distribution "
            "is equilibration and the GO nuclear annotations describe an accessible "
            "compartment rather than a functional site."),
        experiment_type="live-cell imaging"),
    dict(hypothesis=(
        "ADIRF reaches serum by unconventional secretion or in extracellular vesicles, not by "
        "release from damaged cells."),
        description=(
            "Fractionate conditioned medium from human adipocytes and vascular smooth muscle "
            "cells by size-exclusion chromatography and density gradient, and ask whether "
            "ADIRF co-migrates with CD9/CD63/TSG101-positive vesicles or with the free "
            "protein fraction; test protease protection with and without detergent to "
            "distinguish luminal cargo from surface-associated protein; and test brefeldin A "
            "insensitivity to exclude the classical pathway, which the absence of a signal "
            "peptide already predicts. Include a cell-death marker such as LDH release as the "
            "control that discriminates secretion from lysis. This decides whether GO:0070062 "
            "or a generic extracellular-region annotation is the supportable term."),
        experiment_type="secretion and vesicle biochemistry"),
    dict(hypothesis=(
        "The ADIRF-IL18 interaction reported by the HuRI two-hybrid screen occurs at native "
        "expression levels."),
        description=(
            "Test the interaction orthogonally: reciprocal co-immunoprecipitation of "
            "endogenous ADIRF and pro-IL18 from a cell type expressing both, in situ proximity "
            "ligation assay, and NanoBiT complementation with a non-interacting pair as "
            "negative control. Because pro-IL18 is cytosolic and ADIRF is cytosolic and "
            "nucleoplasmic the interaction is topologically possible, so this is a genuine "
            "open question rather than an implausible one - but the current annotation rests "
            "on a single screen logged under three assay versions and has never been "
            "replicated by any other method."),
        experiment_type="interaction validation"),
]


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------

class StrictLoader(yaml.SafeLoader):
    """SafeLoader that REJECTS duplicate mapping keys.

    PyYAML silently keeps the last occurrence of a duplicated key and discards
    the earlier one, so a duplicate destroys data *before* any checker that
    walks the parsed tree can run.
    """


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def build() -> dict:
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    assert len(rows) == N_GOA_ROWS, \
        f"expected {N_GOA_ROWS} GOA rows, got {len(rows)}"

    existing = []
    unmatched = []
    for r in rows:
        key = (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["QUALIFIER"])
        if key not in REVIEWS:
            unmatched.append(key)
            continue
        rv = dict(REVIEWS[key])  # fresh dict per row; no shared objects
        entry = {
            "term": T(r["GO TERM"], r["GO NAME"]),
            "evidence_type": r["GO EVIDENCE CODE"],
            "original_reference_id": r["REFERENCE"],
            "qualifier": r["QUALIFIER"],
        }
        # source_entities derived FROM the GOA WITH/FROM column, never by hand.
        wf = [t for t in r["WITH/FROM"].split("|") if t]
        if wf:
            entry["supporting_entities"] = wf
        pr = rv.get("propagation_review")
        if pr and wf:
            declared = [se["source_id"] for se in pr["source_entities"]]
            assert declared == wf, (
                f"source_entities drifted from GOA WITH/FROM for {key}: "
                f"declared={declared} goa={wf}")
        entry["review"] = {k: v for k, v in rv.items()}
        existing.append(entry)

    assert not unmatched, f"GOA rows with no review content: {unmatched}"
    assert len(existing) == len(rows), f"{len(existing)} reviews for {len(rows)} rows"

    existing.extend(NEW_ROWS)

    doc = {
        "id": "Q15847",
        "gene_symbol": "ADIRF",
        "aliases": ["APM2", "AFRO", "C10orf116", "apM-2"],
        "product_type": "PROTEIN",
        "status": "COMPLETE",
        "taxon": T("NCBITaxon:9606", "Homo sapiens"),
        "description": (
            "ADIRF (adipogenesis regulatory factor, formerly C10orf116, also known as APM2 "
            "and AFRO) is a 76-residue nuclear and cytosolic protein of vertebrates, "
            "originally identified as one of the most abundant transcripts in human adipose "
            "tissue. It is a small, alanine- and glutamine-rich polypeptide with no "
            "recognisable domain, no resolved structure and no known molecular activity: its "
            "only sequence feature is the mature chain itself. Introduced into preadipocytes "
            "it raises the levels of the master adipogenic transcription factors PPARG and "
            "CEBPA during the early phase of differentiation and accelerates adipogenic "
            "conversion, placing it upstream of the core adipogenic transcriptional program, "
            "though the mechanism by which it does so - and whether it acts at transcription "
            "directly - is unresolved. Immunofluorescence places the protein in both the "
            "nucleoplasm and the cytosol, a distribution consistent with its being far "
            "smaller than the nuclear-pore diffusion limit, and it is also recovered from "
            "extracellular fluids: it is "
            "present in human serum at microgram-per-millilitre concentrations and in "
            "urinary and prostatic exosome preparations, despite lacking any signal peptide "
            "or transmembrane segment. Expression is highest in arterial tissue and in "
            "adipose tissue, with additional expression in heart, cornea, liver, kidney and "
            "spleen, and the protein is detected in vascular and non-vascular smooth muscle. "
            "Elevated ADIRF is associated with obesity and, in tumour cells, with resistance "
            "to cisplatin. The gene is present across vertebrates: orthologues in teleost "
            "fish, birds and mammals all align across essentially the whole 76-residue "
            "protein. It was nonetheless lost in the ancestor of mice, rats and hamsters "
            "through a "
            "43-kilobase deletion that removed its promoter and first exon, and it has no "
            "paralogue, so rodent models of the standard kind cannot report on its function."
        ),
        "references": REFERENCES,
        "existing_annotations": existing,
        "core_functions": CORE_FUNCTIONS,
        "knowledge_gaps": KNOWLEDGE_GAPS,
        "suggested_questions": QUESTIONS,
        "suggested_experiments": EXPERIMENTS,
    }
    # references[].id must be unique -- a duplicated reference entry is a
    # generator bug, so assert on the generator's output rather than the file.
    ref_ids = [r["id"] for r in doc["references"]]
    assert len(ref_ids) == len(set(ref_ids)), \
        f"duplicate references: {[i for i in ref_ids if ref_ids.count(i) > 1]}"
    return doc


def _norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def check_file_quotes(parsed, problems: list[str]) -> int:
    """Verify every ``file:`` supporting_text against its target file.

    The repo's reference validator checks supporting_text verbatim only for
    ``PMID:`` references and skips ``file:`` ones entirely, so a fabricated or
    whitespace-mangled file quote ships silently.  Two were caught exactly this
    way while this review was being written, both invented rather than copied.
    """
    checked = 0

    def walk(node):
        nonlocal checked
        if isinstance(node, dict):
            ref, txt = node.get("reference_id"), node.get("supporting_text")
            if isinstance(ref, str) and ref.startswith("file:") and txt:
                target = REPO / "genes" / ref.split(":", 1)[1]
                if not target.exists():
                    target = REPO / ref.split(":", 1)[1]
                if not target.exists():
                    problems.append(f"file: reference target missing: {ref}")
                elif _norm(txt) not in _norm(target.read_text()):
                    problems.append(
                        f"file: quote is NOT verbatim in {ref}: {txt[:70]!r}")
                else:
                    checked += 1
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for e in node:
                walk(e)

    walk(parsed)
    return checked


def count_key(node, key: str) -> int:
    n = 0
    if isinstance(node, dict):
        for k, v in node.items():
            n += 1 if k == key else count_key(v, key)
    elif isinstance(node, list):
        for e in node:
            n += count_key(e, key)
    return n


def audit(raw: str) -> tuple[list[str], dict]:
    """Run every invariant against the EMITTED YAML, not against the builder.

    Detector and mutator must share a representation: a claim that is a single
    sentence in the Python source is line-wrapped by the dumper, so a check run
    over the generator cannot see what actually ships.
    """
    problems: list[str] = []

    if "&id" in raw or re.search(r"\*id\d+", raw):
        problems.append(
            "YAML anchors/aliases present; a shared object multiplies one "
            "supporting_text across rows and every checker then reports N successes")

    try:
        parsed = yaml.load(raw, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        problems.append(f"duplicate mapping key in emitted YAML: {exc}")
        parsed = yaml.safe_load(raw)

    # Raw-vs-parsed reconciliation. A duplicate mapping key is dropped by PyYAML
    # on parse, so the data is gone before any checker that walks the parsed
    # tree can run; only the raw text can see it.
    raw_ref_ids = len(re.findall(r"^\s*(?:-\s*)?reference_id:", raw, re.M))
    parsed_ref_ids = count_key(parsed, "reference_id")
    if raw_ref_ids != parsed_ref_ids:
        problems.append(
            f"raw vs parsed reference_id count mismatch: {raw_ref_ids} vs "
            f"{parsed_ref_ids} -- investigate; do not find a story that makes the "
            f"gap acceptable")

    n_rows = len(parsed["existing_annotations"])
    if n_rows != EXPECTED_ANNOTATIONS:
        problems.append(
            f"expected {N_GOA_ROWS} GOA rows + {len(NEW_ROWS)} NEW = "
            f"{EXPECTED_ANNOTATIONS} annotations, got {n_rows}")

    ref_ids = [r["id"] for r in parsed["references"]]
    dupes = sorted({i for i in ref_ids if ref_ids.count(i) > 1})
    if dupes:
        problems.append(f"duplicated references[].id (a generator bug): {dupes}")

    # Same term, same action -- GO:0005515 is exempt because per-partner
    # verdicts on protein-binding rows are legitimate and validator.py skips it.
    by_term: dict[str, set] = {}
    for a in parsed["existing_annotations"]:
        by_term.setdefault(a["term"]["id"], set()).add(a["review"]["action"])
    for term, actions in sorted(by_term.items()):
        if term != "GO:0005515" and len(actions) > 1:
            problems.append(f"{term} carries conflicting actions {sorted(actions)}")

    # Coverage, BOTH directions. An unwritten direction is not a passing one.
    accepted = {a["term"]["id"] for a in parsed["existing_annotations"]
                if a["review"]["action"] == "ACCEPT"}
    backed = {a["term"]["id"] for a in parsed["existing_annotations"]
              if a["review"]["action"] in ("ACCEPT", "NEW")}
    cf_terms: set[str] = set()
    for cf in parsed["core_functions"]:
        for slot in ("directly_involved_in", "locations", "substrates",
                     "anatomical_locations"):
            for t in cf.get(slot) or []:
                cf_terms.add(t["id"])
        for slot in ("molecular_function", "contributes_to_molecular_function",
                     "in_complex"):
            if cf.get(slot):
                cf_terms.add(cf[slot]["id"])
    if not accepted:
        problems.append("no ACCEPT rows at all -- the coverage checks below would "
                        "pass vacuously")
    if not cf_terms:
        problems.append("core_functions names no terms -- the coverage checks below "
                        "would pass vacuously")
    missing_cf = accepted - cf_terms
    if missing_cf:
        problems.append(f"ACCEPTed terms absent from core_functions: {sorted(missing_cf)}")
    unbacked = cf_terms - backed
    if unbacked:
        problems.append(f"core_functions terms with no ACCEPT/NEW row: {sorted(unbacked)}")

    # A hedge in prose must not be contradicted by a structured field. This
    # review states throughout that ADIRF has no known molecular function and
    # that no function is claimed to occur in the cytosol.
    for cf in parsed["core_functions"]:
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            if cf.get(slot):
                problems.append(
                    f"core_functions asserts {slot}={cf[slot]['id']} while the review "
                    f"states throughout that ADIRF has no known molecular function")
    if "GO:0005829" in cf_terms:
        problems.append(
            "cytosol appears in core_functions, but the cytosol row is proposed as "
            "located_in only, with no claim that any function occurs there")

    n_file_quotes = check_file_quotes(parsed, problems)
    if n_file_quotes == 0:
        problems.append("no file: quotes were checked -- check_file_quotes passed "
                        "vacuously, so its result proves nothing")

    stats = {
        "annotations": n_rows,
        "references": len(parsed["references"]),
        "reference_id_raw": raw_ref_ids,
        "reference_id_parsed": parsed_ref_ids,
        "file_quotes_checked": n_file_quotes,
        "actions": {a: sum(1 for x in parsed["existing_annotations"]
                           if x["review"]["action"] == a)
                    for a in sorted({x["review"]["action"]
                                     for x in parsed["existing_annotations"]})},
    }
    return problems, stats


def self_test() -> int:
    """Break each audit check in the direction it exists for, asserting the message."""
    base = OUT.read_text()

    def expect(mutated: str, fragment: str, label: str) -> None:
        problems, _ = audit(mutated)
        hits = [p for p in problems if fragment in p]
        if not hits:
            raise AssertionError(
                f"self-test {label}: expected a problem containing {fragment!r}, "
                f"got {problems!r}")
        print(f"  ok  {label}: {hits[0][:88]}...")

    # Each mutation asserts its anchor is present BEFORE replacing, so a target
    # that has drifted fails loudly instead of silently proving nothing.
    def mutate(old: str, new: str, label: str) -> str:
        assert old in base, f"self-test {label}: anchor {old[:50]!r} not in the file"
        return base.replace(old, new, 1)

    # A duplicated mapping key at the SAME indent: PyYAML keeps the last and
    # silently discards the first, so no checker that walks the parsed tree can
    # see the loss.
    expect(mutate("    - reference_id: PMID:23239344\n",
                  "    - reference_id: PMID:23239344\n"
                  "      reference_id: PMID:23239344\n",
                  "dup-key"),
           "duplicate mapping key", "audit/duplicate-key")

    expect(mutate("\n    action: ACCEPT\n", "\n    action: REMOVE\n", "conflict"),
           "conflicting actions", "audit/conflicting-actions")

    expect(mutate("supporting_text: HPA record for ADIRF (ENSG00000148671)",
                  "supporting_text: HPA record for ADIRF (ENSG99999999)",
                  "filequote"),
           "file: quote is NOT verbatim", "audit/file-quote")

    # Point the core_functions process term at an id no row backs.
    expect(mutate("  directly_involved_in:\n  - id: GO:0045600\n",
                  "  directly_involved_in:\n  - id: GO:0099999\n",
                  "cf-unbacked"),
           "core_functions terms with no ACCEPT/NEW row", "audit/cf-unbacked")

    # ... and the mirror: an ACCEPTed term missing from core_functions.
    expect(mutate("  locations:\n  - id: GO:0005634\n    label: nucleus\n",
                  "  locations:\n", "cf-missing"),
           "ACCEPTed terms absent from core_functions", "audit/cf-missing")

    # A molecular_function in core_functions must contradict the review's
    # standing hedge that ADIRF has none.
    expect(mutate("  directly_involved_in:\n",
                  "  molecular_function:\n    id: GO:0003674\n"
                  "    label: molecular_function\n  directly_involved_in:\n",
                  "mf-hedge"),
           "no known molecular function", "audit/mf-contradicts-hedge")

    # Happy direction: the shipped file must produce no problems. A check can be
    # wrong about success as easily as about failure.
    problems, stats = audit(base)
    if problems:
        raise AssertionError(f"self-test audit/happy: shipped file raised {problems!r}")
    print(f"  ok  audit/happy: shipped file clean ({stats['file_quotes_checked']} "
          f"file: quotes checked)")
    print()
    print("self-test passed. A passing self-test proves the guards I thought of fire;")
    print("it cannot tell me which guard I failed to write.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--audit-only", action="store_true",
                    help="audit the emitted YAML without regenerating it")
    ap.add_argument("--self-test", action="store_true",
                    help="break-test the audit checks against mutated copies")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    if not args.audit_only:
        doc = build()
        OUT.write_text(yaml.dump(doc, Dumper=NoAliasDumper, sort_keys=False,
                                 allow_unicode=True, width=100,
                                 default_flow_style=False))
        print(f"wrote {OUT}")

    problems, stats = audit(OUT.read_text())
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  -", p)
        return 1
    print("  all invariants held")
    return 0


if __name__ == "__main__":
    sys.exit(main())
