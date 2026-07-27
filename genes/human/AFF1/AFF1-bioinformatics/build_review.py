#!/usr/bin/env python3
"""Build genes/human/AFF1/AFF1-ai-review.yaml from the GOA TSV plus per-row verdicts.

Why a builder rather than hand editing:

* `supporting_entities` and `propagation_review.source_entities` are derived FROM
  the GOA `WITH/FROM` column, so they cannot drift out of agreement with GOA.  Hand
  maintained source lists have drifted on every gene in this campaign that tried it.
* Row order, evidence code, reference and qualifier are copied from the TSV, and the
  build asserts one verdict exists per TSV row and that no verdict is unused.
* Reference titles are taken from the seeded stub or from the cached
  `publications/PMID_*.md` frontmatter -- never written from memory.
* Every `supporting_text` is verified against its source **before** the file is
  written, and the build fails if it verified zero `file:` quotes (the vacuity hole:
  `file:` quotes are skipped by the repo validator, so they are the one place an
  invented quotation survives every automated gate).
* Dumped with aliases disabled, so each row is an independent object and raw-text
  counts are meaningful.

Run: uv run python build_review.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
GOA = GENE_DIR / "AFF1-goa.tsv"
OUT = GENE_DIR / "AFF1-ai-review.yaml"
STUB_TITLES_FROM = OUT  # the seeded stub is the title source of record


class Fail(Exception):
    pass


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip().lower()


def source_path(ref: str) -> Path:
    if ref.startswith("PMID:"):
        return REPO / "publications" / f"PMID_{ref.split(':', 1)[1]}.md"
    if ref.startswith("file:"):
        rel = ref.split(":", 1)[1]
        p = REPO / "genes" / rel
        return p if p.exists() else REPO / rel
    raise Fail(f"no source path scheme for {ref}")


def title_from_cache(pmid: str) -> str:
    p = source_path(pmid)
    if not p.exists():
        raise Fail(f"no cached publication for {pmid}; run `just fetch-pmid "
                   f"{pmid.split(':')[1]}`")
    text = p.read_text()
    m = re.search(r"^title:\s*(.*(?:\n  .*)*)", text, re.M)
    if not m:
        raise Fail(f"{p} has no `title:` in its frontmatter")
    return re.sub(r"\s+", " ", m.group(1)).strip().strip("'\"")


class Q:
    """A quotation, verified against its source at construction time."""

    checked_pmid = 0
    checked_file = 0

    def __init__(self, ref: str, text: str) -> None:
        p = source_path(ref)
        if not p.exists():
            raise Fail(f"quote cites a source that does not exist: {ref} -> {p}")
        body = p.read_text()
        if norm(text) not in norm(body):
            raise Fail(f"NOT VERBATIM: {ref}\n  {text!r}")
        if ref.startswith("file:"):
            # A `file:` quote must also lie inside ONE physical line, or a UniProt
            # `CC       ` continuation prefix ends up inside the quoted span and
            # nothing in CI would notice.
            if not any(text in ln for ln in body.splitlines()):
                raise Fail(f"`file:` quote crosses a line boundary (invisible to "
                           f"every repo gate): {ref}\n  {text!r}")
            Q.checked_file += 1
        else:
            Q.checked_pmid += 1
        self.ref, self.text = ref, text

    def d(self) -> dict:
        return {"reference_id": self.ref, "supporting_text": self.text}


def sb(*qs: Q) -> list[dict]:
    """Fresh dicts every time, so no two rows can share one object (which would be
    emitted as a YAML alias and verified N times as one quote)."""
    return [q.d() for q in qs]


def term(tid: str, label: str) -> dict:
    return {"id": tid, "label": label}


# ---------------------------------------------------------------------------
# quotations used by the review
# ---------------------------------------------------------------------------

U = "file:human/AFF1/AFF1-uniprot.txt"

Q_SUBUNIT = Q(U, "composed of EAF1, EAF2, CDK9, MLLT3/AF9, AFF (AFF1 or AFF4), the P-TEFb")
Q_SUBCELL = Q(U, "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000305}.")
Q_RP_SEC = Q(U, "RP   IDENTIFICATION IN THE SEC COMPLEX.")
Q_RP_NMR = Q(U, "RP   STRUCTURE BY NMR OF 738-779 IN COMPLEX WITH MLLT3.")

Q_KD = Q("PMID:23260655", "The affinity for AF4 is extremely high (KD = 0.17 ± 0.05 nM)")
Q_PEPTIDE = Q("PMID:23260655",
              "we titrated a peptide derived from the AF9 interaction motif of AF4 "
              "(residues 761 to 774) into the AF9 AHD")
Q_ORDERED = Q("PMID:23260655",
              "1H-15N heteronuclear NOE experiments show that AF4 residues 761-775 "
              "are ordered in the complex whereas the remainder is flexible")
Q_HYDROPHOBIC = Q("PMID:23260655",
                  "aliphatic residues, which are conserved in each of the AF9 binding "
                  "partners, form an integral part of the hydrophobic core of the complex")

Q_ELL_AFF1 = Q("PMID:20159561",
               "Furthermore, the ELL and AFF4-containing complexes also consist of "
               "additional MLL partners, AFF1, ENL, and AF9")
Q_NO_DOT1 = Q("PMID:20159561",
              "we find that Dot1 is not associated with AFF1, AFF4 or the ELL "
              "complexes indicating that ENL is part of at least two distinct complexes")
Q_AFF1_NOT_AFF4 = Q("PMID:20159561",
                    "We observed that the reduction of the AFF4 homologue AFF1 does "
                    "not alter ELL1 and P-TEFb stability in these cells")

Q_SEC_PURIFIED = Q("PMID:22547686",
                   "We previously purified the AFF1- and AFF4-containing super "
                   "elongation complex (SEC) as a major regulator of development and "
                   "cancer pathogenesis.")
Q_CTD_KINASE = Q("PMID:22547686",
                 "The SEC family members demonstrate high levels of polymerase II "
                 "(Pol II) C-terminal domain kinase activity")

Q_LEC = Q("PMID:22195968",
          "Eleven-nineteen lysine-rich leukemia (ELL) participates in the super "
          "elongation complex (SEC) with the RNA polymerase II (Pol II) CTD kinase "
          "P-TEFb.")

Q_MED26 = Q("PMID:21729782",
            "Reactivation of paused Pol II correlates with recruitment of "
            "super-elongation complexes (SECs) containing ELL/EAF family members, "
            "P-TEFb, and other proteins")

Q_JAGER = Q("PMID:22190034",
            "we report the use of affinity tagging and purification mass spectrometry "
            "to determine systematically the physical interactions of all 18 HIV-1 "
            "proteins and polyproteins with host proteins in two different human cell "
            "lines (HEK293 and Jurkat)")

Q_PARSTA = Q("PMID:41062835",
             "Upon DNA damage, PARP1 binds to and PARylates AFF1 in a region targeted "
             "by the E3 ligase Siah1, preventing AFF1 ubiquitination and promoting its "
             "stability. This stabilization supports efficient transcriptional "
             "recovery after DNA damage.")
Q_DEPLETION = Q("PMID:41062835", "AFF1 depletion impairs DNA repair and survival")

Q_ACETYL = Q("PMID:31611376",
             "we show that site-specific acetylation of super elongation complex (SEC) "
             "subunit AFF1 by p300 reduces its interaction with other SEC components "
             "and impairs P-TEFb-mediated C-terminal domain phosphorylation of RNA "
             "polymerase II both in vitro and in vivo")
Q_REEXPRESS = Q("PMID:31611376",
                "Reexpression of wild-type AFF1, but not an acetylation mimic mutant, "
                "restores SEC component recruitment and target gene expression in AFF1 "
                "knockdown cells.")
Q_SEC_OR = Q("PMID:31611376",
             "Human SEC was described as a megadalton complex containing elongation "
             "factors P-TEFb (a heterodimer of CyclinT1 and CDK9) and ELL in "
             "association with AFF1 or AFF4, AF9 or ENL, and EAF1/2")

Q_PTEFB = Q("PMID:24367103",
            "we show that the AF4/FMR2 family member 1 (AFF1) is bound to CDK9-CycT "
            "and is present in all major P-TEFb complexes and that the tripartite "
            "CDK9-CycT-AFF1 complex is transferred as a single unit within the P-TEFb "
            "network")
Q_TAT_CYCT1 = Q("PMID:24367103",
                "By increasing the affinity of the HIV-encoded transactivating (Tat) "
                "protein for CycT1, AFF1 facilitates Tat's extraction of P-TEFb from "
                "7SK snRNP and the formation of Tat-SECs for HIV transcription.")

Q_KD_ALP = Q("PMID:28955517",
             "siRNA-mediated depletion of AFF1 led to more intense staining of "
             "alkaline phosphatase (ALP), an early marker of osteoblastic differentiation")
Q_OE_ALP = Q("PMID:28955517",
             "We found that overexpression of AFF1 decreased the ALP activity and "
             "mineralization of MSCs")
Q_CHIP_DKK1 = Q("PMID:28955517",
                "we performed an anti-AFF1 ChIP assay, which demonstrated that AFF1 "
                "bound to the promoter region of DKK1")
Q_RESCUE = Q("PMID:28955517",
             "Depletion of DKK1 significantly abolished the inhibition of ALP activity "
             "triggered by AFF1 overexpression")
Q_INVIVO = Q("PMID:28955517",
             "Mice implanted with AFF1-overexpressing MSCs showed much less bone tissue")
Q_OPPOSITE = Q("PMID:28955517",
               "depletion of AFF4 significantly reduced the alkaline phosphatase (ALP) "
               "activity and extracellular matrix mineralization, indicating that it "
               "had an opposite effect on osteogenic differentiation compared with AFF1")
Q_NOT_TOGETHER = Q("PMID:28955517",
                   "Although AFF1 and AFF4 are components of SECs, they may be "
                   "independently localized and are not found together in a single SEC.")

Q_MOUSE_AF4 = Q("PMID:17135274",
                "We demonstrate that mouse Af4 functions as a positive regulator of "
                "Pol II transcription elongation factor b (P-TEFb) kinase")
Q_GAL4 = Q("PMID:8555498",
           "both LAF-4 and AF-4 had domains that activated transcription strongly when "
           "fused to the GAL4 DNA-binding domain")
Q_ROBOTIC = Q("PMID:12629167",
              "Genetic and physical mapping of the disease locus led to the "
              "identification of a missense mutation in a highly conserved region of "
              "Af4, a putative transcription factor that has been previously implicated "
              "in leukemogenesis.")
Q_ROBOTIC_HEDGE = Q("PMID:12629167",
                    "We demonstrate that Af4 is specifically expressed in Purkinje "
                    "cells, and we hypothesize that the expression of mutant Af4 leads "
                    "to neurodegeneration.")
Q_PFWT = Q("PMID:15269783",
           "we have developed a peptide, designated PFWT, which disrupts the AF4-AF9 "
           "interaction in vitro and in vivo")
Q_IGF1 = Q("PMID:20007461",
           "Chromatin immunoprecipitation confirmed that Igf-1 is a direct and the "
           "first validated target of the AF4 transcriptional regulatory complex")

# ---------------------------------------------------------------------------
# per-row verdicts, keyed on (term, evidence, reference) -- a stable entity triple
# ---------------------------------------------------------------------------

NODE = "PANTHER:PTN000829417"

DONOR_LABELS = {
    "PANTHER:PTN000829417": "PANTHER family node (AF4/FMR2 family; 79 recipient gene products, human reach = AFF1/AFF2/AFF3/AFF4)",
    "UniProtKB:P51825": "human AFF1 itself (self-referential IBD seed)",
    "MGI:MGI:1100819": "mouse Aff1 (O88573) - the 1:1 ortholog",
    "MGI:MGI:106927": "mouse Aff3 (P51827) - paralog",
    "MGI:MGI:1202294": "mouse Aff2 (O55112) - paralog",
    "FB:FBgn0041111": "Drosophila lilli (Q9VQI9) - the single fly family member, co-orthologue of all four vertebrate AFFs",
    "ARBA:ARBA00026330": "ARBA automatic rule",
    "InterPro:IPR043640": "InterPro AF4/FMR2 C-terminal homology domain signature",
    "InterPro:IPR007797": "InterPro AF4/FMR2 family signature",
    "UniProtKB-SubCell:SL-0191": "UniProt SubCell keyword Nucleus (derived from the entry's own ECO:0000305 SUBCELLULAR LOCATION line)",
}

DONOR_STATUS = {
    "PANTHER:PTN000829417": ("SUPPORTS_TRANSFER",
        "an internal PANTHER tree node, not a protein; its human reach is exactly the four AFF paralogues, all of which belong to SEC-family complexes"),
    "UniProtKB:P51825": ("CIRCULAR_OR_REDUNDANT",
        "the target itself; a self-referential IBD records a PAINT curator judging the function core rather than a chain of inference, so it neither adds nor removes support"),
    "MGI:MGI:1100819": ("SUPPORTS_TRANSFER",
        "the true ortholog, and it carries its own IDA to positive regulation of DNA-templated transcription (PMID:9365243)"),
    "MGI:MGI:106927": ("SUPPORTS_TRANSFER",
        "a paralog rather than the ortholog, which is legitimate for IBA but means no ortholog-strength inference rests on this token; it carries its own IDA and IMP rows"),
    "MGI:MGI:1202294": ("SUPPORTS_TRANSFER",
        "a paralog; its experimental evidence in this subtree is GO:0007611 learning or memory IMP (PMID:11923441), a descendant of the propagated term"),
    "FB:FBgn0041111": ("SUPPORTS_TRANSFER",
        "the single fly family member, with its own experimental annotation in every subtree it is cited for"),
    "ARBA:ARBA00026330": ("SUPPORTS_TRANSFER", "automatic rule, not a gene product"),
    "InterPro:IPR043640": ("SUPPORTS_TRANSFER", "family-specific signature, not a gene product"),
    "InterPro:IPR007797": ("SUPPORTS_TRANSFER", "family-specific signature, not a gene product"),
    "UniProtKB-SubCell:SL-0191": ("CIRCULAR_OR_REDUNDANT",
        "this token derives from the entry's own SUBCELLULAR LOCATION line, which is itself ECO:0000305 curator inference, so it is not an independent witness"),
}


def prop(root_cause: str, failure_modes: list[str] | None,
         tokens: list[str]) -> dict:
    srcs = []
    for t in tokens:
        if t not in DONOR_LABELS:
            raise Fail(f"no label registered for WITH/FROM token {t}")
        status, comment = DONOR_STATUS[t]
        srcs.append({"source_id": t, "source_label": DONOR_LABELS[t],
                     "source_status": status, "comment": comment})
    d: dict[str, Any] = {"root_cause": root_cause}
    if failure_modes:
        d["failure_modes"] = list(failure_modes)
    d["source_entities"] = srcs
    return d


VERDICTS: dict[tuple[str, str, str], dict] = {}


def verdict(key: tuple[str, str, str], **kw) -> None:
    if key in VERDICTS:
        raise Fail(f"duplicate verdict registered for {key}")
    VERDICTS[key] = kw


# --- row 1 -----------------------------------------------------------------
verdict(("GO:0006355", "IBA", "GO_REF:0000033"),
    summary=(
        "Accepted as a correct family-level statement. All four protein donors "
        "(mouse Aff1, mouse Aff2, mouse Aff3, Drosophila lilli) carry their own "
        "experimental annotations in this subtree, so the chain is not empty of "
        "experimental evidence and no source-weakness objection survives measurement. "
        "The unsigned parent is the right level here rather than lazy curation: the "
        "family is heterogeneous in DIRECTION - human AFF1 activates DKK1 while mouse "
        "Aff2 carries negative regulation of gene expression by IMP - so a signed "
        "child would be false for part of the clade."),
    action="ACCEPT",
    reason=(
        "AFF1 regulates transcription as the scaffolding subunit of the super "
        "elongation complex, and the gene independently holds the specific, "
        "polymerase-resolved descendants of this term from human experiments. This "
        "row is the family-level generalisation of that, and it is a verified "
        "ancestor of GO:0032786 which the human IMP rows already assert, so it adds "
        "nothing false. One of the five WITH/FROM tokens is the target itself, which "
        "records a PAINT curator judging transcriptional regulation to be AFF1's core "
        "function."),
    supported_by=sb(Q_SEC_PURIFIED, Q_CHIP_DKK1),
    propagation_review=prop("NO_FAILURE_CORE", None,
        ["FB:FBgn0041111", "MGI:MGI:106927", "MGI:MGI:1100819", NODE,
         "UniProtKB:P51825"]))

# --- row 2 -----------------------------------------------------------------
verdict(("GO:0003712", "IBA", "GO_REF:0000033"),
    summary=(
        "Accepted as the family's molecular function. The donor, Drosophila lilli, "
        "holds this exact term by IMP (PMID:11171404), so this is a transfer from an "
        "experimentally annotated family member rather than a family-level guess. The "
        "term's own definition permits action \"either on its own or as part of a "
        "complex\", which is what AFF1 does: it modulates transcription of specific "
        "gene sets from within SEC."),
    action="ACCEPT",
    reason=(
        "AFF1 has no catalytic domain and no sequence-specific DNA-binding domain - "
        "901 of its 1210 residues (74.5%) carry a Disordered feature, computed from "
        "the UniProt feature table rather than estimated - so a coregulator activity "
        "is exactly the right class of molecular function for it. Human evidence: it "
        "occupies the DKK1 promoter and sets DKK1 output in both directions in "
        "mesenchymal stromal cells. Recorded in core_functions under "
        "contributes_to_molecular_function, because the coregulatory output is "
        "delivered by the assembled complex."),
    supported_by=sb(Q_CHIP_DKK1, Q_ACETYL),
    propagation_review=prop("NO_FAILURE_CORE", None,
        ["FB:FBgn0041111", NODE]))

# --- row 3 -----------------------------------------------------------------
GO0006368 = term("GO:0006368", "transcription elongation by RNA polymerase II")
verdict(("GO:0006354", "IBA", "GO_REF:0000033"),
    summary=(
        "The essence is right and the polymerase is under-specified. This row is "
        "self-referential - the WITH/FROM cites AFF1 itself alongside the node - so it "
        "records a PAINT curator judging transcription elongation to be AFF1's core "
        "function, which this review agrees with. But the same node asserts, of the "
        "same 79 recipient gene products, GO:0032783 super elongation complex, a term "
        "whose definition is explicitly about \"RNA polymerase II transcription "
        "elongation\". A polymerase-agnostic process term and a Pol II-specific "
        "complex term cannot both be maximally precise."),
    action="MODIFY",
    reason=(
        "Every characterised SEC substrate is RNA polymerase II: SEC-family complexes "
        "are assayed as Pol II CTD kinases, the p300 study measures Pol II CTD "
        "phosphorylation specifically, and AFF1 already holds the Pol II-resolved "
        "regulatory term GO:0032968 by IMP from human knockdown. There is no evidence "
        "of AFF1 acting on RNA polymerase I or III. GO:0006368 was verified by "
        "fetching its is_a/part_of closure to be a genuine descendant of GO:0006354, "
        "so this is a one-step refinement that asserts nothing new about the "
        "polymerase beyond what the gene's other rows already say."),
    proposed_replacement_terms=[dict(GO0006368)],
    supported_by=sb(Q_CTD_KINASE, Q_ACETYL),
    propagation_review=prop("NO_FAILURE_CORE", ["GRANULARITY_MISMATCH"],
        [NODE, "UniProtKB:P51825"]))

# --- row 4 -----------------------------------------------------------------
verdict(("GO:0050877", "IBA", "GO_REF:0000033"),
    summary=(
        "Kept, but not as a core function. Both experimental donors reach this term "
        "from below: Drosophila lilli and mouse Aff2 each carry GO:0007611 learning or "
        "memory by IMP, a descendant, and PAINT generalised to the organ-system parent "
        "rather than transferring the specific term - which is the conservative and "
        "correct move, since neither learning nor memory has been assayed for human "
        "AFF1. There is no human AFF1 nervous-system experiment at all."),
    action="KEEP_AS_NON_CORE",
    reason=(
        "AFF1's own nervous-system link is a mouse phenotype: the robotic allele "
        "carries a missense change in a conserved region of Af4 and the mice show "
        "region-specific Purkinje-cell loss with ataxia, with Igf-1 identified by ChIP "
        "as a target - attributed by those authors to \"the AF4 transcriptional "
        "regulatory complex\" rather than to Af4 alone. Stated at the strength the "
        "papers state it: the 2003 study is explicit that the causal step is "
        "hypothesised rather than demonstrated. That evidence is real but it is (i) "
        "mouse, (ii) a dominant missense allele in which Af4 accumulates, so a "
        "gain-of-function rather than a loss of function, and (iii) downstream of the "
        "same transcription-elongation activity captured by the core rows. The "
        "discriminator against core function 3, which uses similar "
        "tissue-specific-output language and is nevertheless kept as core, is the "
        "evidence and not the tissue-specificity: the DKK1 axis rests on direct human "
        "loss- AND gain-of-function in the relevant cell type with a mapped "
        "intermediate whose removal abolishes the effect, whereas this row has no "
        "human data at all and its mouse support is a dominant gain-of-function allele "
        "with no identified mechanism. MARK_AS_OVER_ANNOTATED is a defensible reading "
        "on the same facts and a curator may prefer it; KEEP_AS_NON_CORE is chosen "
        "because the term is not wrong - PAINT deliberately generalised from two "
        "independent learning-or-memory IMPs rather than transferring them, which is "
        "sound practice - and over-annotated would mis-describe a correct conservative "
        "call as an over-reach. Note for upstream curation: mouse Aff1 is NOT among this row's donors and MGI has annotated no "
        "nervous-system term to it, so the claim reaches human AFF1 through its "
        "paralogues while the ortholog's own relevant phenotype is uncaptured."),
    supported_by=sb(Q_ROBOTIC, Q_ROBOTIC_HEDGE, Q_IGF1),
    propagation_review=prop("NO_FAILURE_NON_CORE", None,
        ["FB:FBgn0041111", "MGI:MGI:1202294", NODE]))

# --- row 5 -----------------------------------------------------------------
verdict(("GO:0032783", "IBA", "GO_REF:0000033"),
    summary=(
        "Accepted as a core cellular component. Unusually, the term's own definition "
        "names the family - a SEC contains \"a transcription factor of the ELL family, "
        "an EAF protein, and an AFF family protein or distant relative\" - so reading "
        "the definition supports this propagation rather than undermining it. The "
        "donor, Drosophila lilli, holds the term by IPI from PMID:22195968. All four "
        "human AFF paralogues receive it from this node, and that is right: AFF1 and "
        "AFF4 occupy SEC, AFF2 and AFF3 the biochemically isolated SEC-L2 and SEC-L3 "
        "variants."),
    action="ACCEPT",
    reason=(
        "SEC membership is AFF1's central, best-corroborated fact: UniProt curates it "
        "from two references, it is reproduced by direct purification in human cells, "
        "and a point change in AFF1 alone is sufficient to disassemble the complex. "
        "The IBA and the independent human IDA agree, so this is corroboration rather "
        "than duplication."),
    supported_by=sb(Q_SUBUNIT, Q_ELL_AFF1, Q_SEC_OR),
    propagation_review=prop("NO_FAILURE_CORE", None,
        ["FB:FBgn0041111", NODE]))

# --- row 6 -----------------------------------------------------------------
verdict(("GO:0005634", "IEA", "GO_REF:0000120"),
    summary=(
        "Accepted. The location is correct and is independently established by the "
        "IDA row from PMID:41062835 and by nuclear immunofluorescence of both AF4 and "
        "its mouse ortholog. Worth recording about the provenance rather than the "
        "conclusion: GO_REF:0000120 asserts agreement between independent automatic "
        "pipelines, and one of its three tokens - UniProtKB-SubCell:SL-0191 - derives "
        "from this entry's own SUBCELLULAR LOCATION line, which is itself ECO:0000305 "
        "curator inference, so the three witnesses are not fully independent."),
    action="ACCEPT",
    reason=(
        "A nuclear transcription-elongation scaffold has to be nuclear, and the "
        "experimental row for the same term makes this one redundant rather than "
        "load-bearing. Not flagged as a defect: the conclusion is right and the "
        "combinatorial reference is behaving as designed."),
    supported_by=sb(Q_SUBCELL),
    propagation_review=prop("NO_FAILURE_CORE", None,
        ["ARBA:ARBA00026330", "InterPro:IPR043640",
         "UniProtKB-SubCell:SL-0191"]))

# --- row 7 -----------------------------------------------------------------
GO0006355 = term("GO:0006355", "regulation of DNA-templated transcription")
verdict(("GO:0010468", "IEA", "GO_REF:0000002"),
    summary=(
        "Sound but one level too coarse. This comes from InterPro2GO via IPR007797, "
        "the AF4/FMR2 family signature. PAINT gives that same family GO:0006355 - one "
        "level more specific - so two automatic pipelines assign different "
        "granularities to the same family from the same evidence base, and "
        "GO:0010468 was verified to be a genuine ancestor of GO:0006355, making it "
        "strictly redundant on this gene."),
    action="MODIFY",
    reason=(
        "The argument is upstream, about the mapping, not about this gene. Every "
        "characterised member of the AF4/FMR2 family regulates transcription "
        "specifically, not gene expression at some unspecified step - none has a "
        "reported role in translation, RNA stability or any other post-transcriptional "
        "layer, and the family's defining biochemistry is occupancy of a "
        "transcription-elongation complex. So IPR007797 supports the more precise term "
        "for every protein it matches, and the mapping is what should move. On THIS "
        "gene the row is redundant either way - today it is an ancestor of the "
        "GO:0006355 the gene already holds by IBA, and after the refinement it would "
        "duplicate that row exactly - so no gene-level redundancy is removed by the "
        "change, and the family-wide precision gain is the whole of the case for it."),
    proposed_replacement_terms=[dict(GO0006355)],
    supported_by=sb(Q_SEC_PURIFIED),
    propagation_review=prop("NO_FAILURE_CORE", ["GRANULARITY_MISMATCH"],
        ["InterPro:IPR007797"]))

# --- rows 8 and 10: AF9 -----------------------------------------------------
GO0030674 = term("GO:0030674", "protein-macromolecule adaptor activity")
AF9_REASON_SHARED = (
    "AF9 is a verified partner by every available standard: five orthogonal detection "
    "methods in IntAct (NMR, circular dichroism, gel filtration, pull-down, tagged "
    "co-immunoprecipitation) across two publications, a deposited NMR structure "
    "(PDB 2LM0), and a dissociation constant of 0.17 nM - an order of magnitude "
    "tighter than AF9's other known ligands measured in the same experiment. So the "
    "problem with the row is not the partner, it is that bare protein binding records "
    "nothing about what the interaction accomplishes. What it accomplishes is "
    "bridging: AFF1 contacts AF9 through residues 761-774 and the P-TEFb kinase module "
    "through a separate region, and a single acetyl-mimic substitution in AFF1 is "
    "sufficient to lose SEC assembly and Pol II CTD phosphorylation. That is adaptor "
    "activity as GO defines it - bringing two or more macromolecules into contact so "
    "they can act in a coordinated way.")

verdict(("GO:0005515", "IPI", "PMID:21729782"),
    summary=(
        "Replace with an informative molecular function. The partner is MLLT3/AF9 "
        "(P42568), captured here in the MED26 study's co-purification of SEC with "
        "Mediator; the reference-projection test returns 26 annotations over 17 "
        "entities, all GO:0005515, so this is one interaction network rather than a "
        "targeted binary assay. Judged per partner rather than per gene: this row and "
        "the PMID:23260655 row name the same partner and get the same verdict, while "
        "the HIV-1 Tat row is decided separately."),
    action="MODIFY",
    reason=AF9_REASON_SHARED + (
        " This row contributes the in-cell half of that case: AFF1 and AF9 co-purify "
        "with Mediator on chromatin, which is where the bridging matters. Recorded for "
        "a curator's eye rather than as an objection: the same reference set led "
        "UniProt to assign GO:0060090 molecular adaptor activity to AF9 itself. That "
        "is not double counting - AF9's AHD is the hub competed for by Dot1L, BCoR and "
        "hPC3, while AFF1 is the hub joining P-TEFb to the ELL/EAF module - but the "
        "symmetry is worth checking."),
    proposed_replacement_terms=[dict(GO0030674)],
    supported_by=sb(Q_MED26, Q_REEXPRESS))

verdict(("GO:0005515", "IPI", "PMID:23260655"),
    summary=(
        "Replace with an informative molecular function. Same partner as the "
        "PMID:21729782 row, MLLT3/AF9 (P42568), and this is the reference that "
        "quantifies it. The paper is titled for AF9, not AFF1 - a reminder that the "
        "only direct molecular measurement on human AFF1 sits under a partner's title. "
        "What was assayed is stated plainly: a 14-residue AFF1 peptide, not the "
        "full-length protein. For a coupled folding-and-binding motif that is the "
        "biologically meaningful unit rather than a truncation artefact, since AFF1's "
        "residues are disordered until they fold into AF9's hydrophobic core."),
    action="MODIFY",
    reason=AF9_REASON_SHARED + (
        " This row contributes the quantitative and structural half: sub-nanomolar "
        "affinity by fluorescence anisotropy against MBP-AF9 AHD, a solved complex, "
        "and heteronuclear NOE data showing that only AFF1 residues 761-775 order on "
        "binding."),
    proposed_replacement_terms=[dict(GO0030674)],
    supported_by=sb(Q_KD, Q_PEPTIDE, Q_ORDERED, Q_HYDROPHOBIC, Q_RP_NMR))

# --- row 9: Tat ------------------------------------------------------------
verdict(("GO:0005515", "IPI", "PMID:22190034"),
    summary=(
        "Kept as a real but non-core host-pathogen interaction. The partner is HIV-1 "
        "Tat (P04608), from a systematic affinity-purification survey of all 18 HIV-1 "
        "proteins; the projection test returns 183 annotations over 104 distinct "
        "entities, all GO:0005515. Expanding the IntAct records rather than trusting "
        "UniProt's NbExp=3: the three records come from ONE publication, logged as two "
        "sub-methods in two cell lines (HEK293T and Jurkat) at MI-score 0.56. So "
        "NbExp=3 is again counting sub-methods, not independent experiments."),
    action="KEEP_AS_NON_CORE",
    reason=(
        "The interaction is not screen noise: AFF1's role in Tat-dependent HIV "
        "transactivation is independently established, and the two-cell-line "
        "replication is part of that study's design. But it is not a core cellular "
        "function of AFF1, and the molecular detail is genuinely open - the "
        "corroborating study's stated mechanism is that AFF1 raises Tat's affinity for "
        "cyclin T1, which does not establish a direct AFF1-Tat contact, and AFF1 has "
        "no Tat co-structure (2LM0, its only PDB entry, is the AF9 complex). Bare "
        "protein binding is uninformative, but no better molecular-function term exists "
        "for a virus-host bridging role, so this is kept rather than modified."),
    supported_by=sb(Q_JAGER, Q_TAT_CYCT1))

# --- row 11 ----------------------------------------------------------------
verdict(("GO:0000785", "IDA", "PMID:41062835"),
    summary=(
        "Accepted. This reference's cached record is abstract-only, so the direct "
        "assay is not visible here and the review defers to the curator, who read the "
        "full text. The call is corroborated from two independent directions: AFF1 "
        "occupies the DKK1 promoter by ChIP in mesenchymal stromal cells, and IntAct "
        "holds a ChIP record placing AFF1 at the MYC gene."),
    action="ACCEPT",
    reason=(
        "Chromatin association follows from what AFF1 does - SEC acts on paused "
        "polymerase at promoters - and it is separately measured. Verified rather than "
        "assumed: GO:0000785 is not an is_a/part_of descendant of GO:0005634, so the "
        "chromatin and nucleus rows are two independent location claims and neither "
        "makes the other redundant."),
    supported_by=sb(Q_CHIP_DKK1, Q_PARSTA))

# --- row 12 ----------------------------------------------------------------
verdict(("GO:0003711", "IMP", "PMID:41062835"),
    summary=(
        "Accepted, and it is already the most specific term available - GO:0003711 has "
        "no children, so there is no polymerase-resolved elongation-factor-activity "
        "term to refine to. Recorded because GO's evidence codes do not distinguish "
        "it: the evidence is a knockdown, so this establishes that AFF1 is REQUIRED "
        "for the activity, not that AFF1 alone is sufficient to supply it."),
    action="ACCEPT",
    reason=(
        "The stimulation of polymerase elongation is delivered by the assembled "
        "complex - the CTD kinase is CDK9, not AFF1 - so core_functions records this "
        "under contributes_to_molecular_function rather than as an activity AFF1 "
        "carries out alone. The independent basis for AFF1's specific contribution is "
        "the acetyl-mimic experiment: re-expressing wild-type but not acetylation-mimic "
        "AFF1 restores SEC recruitment and target-gene expression, so a change in AFF1 "
        "alone controls whether the elongation activity is delivered. Verified rather "
        "than assumed: GO:0003712 is NOT an ancestor of GO:0003711, so this row and "
        "the coregulator row are different claims rather than a general/specific pair, "
        "and both stand. The divergence between the row's GOA qualifier (enables) and "
        "where core_functions puts the term (contributes_to_molecular_function) is "
        "deliberate, not an inconsistency: strictly, contributes_to is the correct GOA "
        "qualifier for an activity delivered by an assembled complex, but ActionEnum "
        "offers no qualifier-change action, and MODIFY would wrongly imply the TERM is "
        "wrong when only the qualifier is imprecise. So the row is ACCEPTed as-is and "
        "the nuance is carried by the core_functions slot; a qualifier correction is "
        "raised with UniProt in suggested_questions instead."),
    supported_by=sb(Q_DEPLETION, Q_REEXPRESS, Q_CTD_KINASE))

# --- row 13 ----------------------------------------------------------------
verdict(("GO:0005634", "IDA", "PMID:41062835"),
    summary=(
        "Accepted. This is the experimental nuclear localisation for AFF1; note that "
        "UniProt's own SUBCELLULAR LOCATION line is ECO:0000305 curator inference, so "
        "before this reference the nuclear call rested on inference plus older "
        "immunofluorescence rather than on a curated experimental annotation."),
    action="ACCEPT",
    reason=(
        "Uncontested and corroborated by the IEA row for the same term and by nuclear "
        "immunofluorescence of AF4 and of mouse Af4."),
    supported_by=sb(Q_SUBCELL, Q_PARSTA))

# --- row 14 ----------------------------------------------------------------
verdict(("GO:0006974", "IDA", "PMID:41062835"),
    summary=(
        "Accepted. The projection test on this reference was run precisely because "
        "AFF1 is a complex subunit and a complex-level phenotype can become gene-level "
        "evidence on every subunit: fully paginated, PMID:41062835 yields 8 "
        "annotations over 2 distinct gene products, with six terms on AFF1 alone and "
        "only the damage-site location shared with PARP1. The phenotype does not "
        "spread across a complex, so this is the benign shape."),
    action="ACCEPT",
    reason=(
        "Independently corroborated from the opposite direction by the p300 study, "
        "which shows AFF1 acetylation is dynamically induced by genotoxic stress and "
        "shuts SEC down. Two laboratories, two modifications, one coherent picture: "
        "AFF1 abundance and modification state are the switch for transcriptional "
        "shutdown and restart around DNA damage."),
    supported_by=sb(Q_PARSTA, Q_DEPLETION, Q_ACETYL))

# --- row 15 ----------------------------------------------------------------
verdict(("GO:0032783", "IDA", "PMID:20159561"),
    summary=(
        "Accepted as a core cellular component, after checking what molecule the "
        "experiment used. This paper is titled for AFF4 and most of it works with "
        "MLL-AFF1 and other MLL-fusion constructs, which would be the wrong basis for "
        "a wild-type annotation. This row is not that: its basis is the Flag-AFF4 and "
        "Flag-ELL1/2/3 purifications, which recover endogenous AFF1 as a component. "
        "Wild-type protein, native levels."),
    action="ACCEPT",
    reason=(
        "SEC membership is AFF1's core cellular component and this is the direct human "
        "biochemical demonstration of it. The reference-projection test returns a "
        "single annotation on a single entity, so there is no projection concern. The "
        "same paper independently records that AFF1 and AFF4 are not "
        "interchangeable - depleting AFF1 does not destabilise ELL1 or P-TEFb, whereas "
        "depleting AFF4 does - which is why this review treats the paralogues "
        "separately throughout."),
    supported_by=sb(Q_ELL_AFF1, Q_AFF1_NOT_AFF4, Q_SUBUNIT))

# --- row 16 ----------------------------------------------------------------
GO0032968 = term("GO:0032968",
                 "positive regulation of transcription elongation by RNA polymerase II")
verdict(("GO:0032786", "IMP", "PMID:41062835"),
    summary=(
        "Correct but redundant with its own child. GO:0032968 was verified by fetching "
        "its is_a/part_of closure to be a descendant of GO:0032786, and the SAME "
        "reference supplies both by IMP - so these two rows are a parent/child pair "
        "from one experiment, not two independent findings. AFF1's substrate is RNA "
        "polymerase II, so the polymerase-agnostic parent carries no information the "
        "child does not."),
    action="MODIFY",
    reason=(
        "Collapse onto the Pol II-resolved child that the same reference already "
        "provides. Every measurement behind these rows is Pol II-specific: SEC-family "
        "complexes are assayed as Pol II CTD kinases and the acetylation study "
        "measures Pol II CTD phosphorylation. There is no evidence for AFF1 acting on "
        "RNA polymerase I or III, so nothing is lost. Deliberately NOT claimed: that "
        "GO:0032968 sits under GO:0006368; it does not - GO links them by "
        "positively_regulates and keeps regulation out of the is_a hierarchy, and both "
        "closures were fetched to check."),
    proposed_replacement_terms=[dict(GO0032968)],
    supported_by=sb(Q_DEPLETION, Q_CTD_KINASE))

# --- row 17 ----------------------------------------------------------------
verdict(("GO:0032968", "IMP", "PMID:41062835"),
    summary=(
        "Accepted as a core biological process, and it is the term the parent row "
        "should collapse onto. AFF1 knockdown lowers transcriptional recovery after "
        "DNA damage, and AFF1's contribution to Pol II CTD phosphorylation is "
        "separately demonstrated by the acetyl-mimic experiment."),
    action="ACCEPT",
    reason=(
        "This is the polymerase-resolved statement of AFF1's central activity and it "
        "is supported from both directions - loss of AFF1 lowers elongation output, "
        "and restoring wild-type but not acetylation-mimic AFF1 recovers it. The "
        "evidence is knockdown-based, so it establishes requirement; the sufficiency "
        "arm comes from the rescue rather than from this row."),
    supported_by=sb(Q_DEPLETION, Q_ACETYL, Q_REEXPRESS))

# --- row 18 ----------------------------------------------------------------
verdict(("GO:0090734", "IDA", "PMID:41062835"),
    summary=(
        "Accepted, deferring to the curator on an assay this review cannot see - the "
        "cached record for this reference is abstract-only. The abstract does establish "
        "the biochemical basis for a damage-site location: PARP1, which localises to "
        "DNA lesions, binds and PARylates AFF1. The projection test shows this is the "
        "only term of the seven that PMID:41062835 gives to a second entity, and that "
        "entity is PARP1 itself - consistent with a shared recruitment rather than a "
        "complex-wide projection."),
    action="ACCEPT",
    reason=(
        "A damage-induced location for a transcription-elongation scaffold is exactly "
        "what the transcription-restart mechanism requires, and it is recorded in "
        "core_functions as a location of the DNA-damage-response function rather than "
        "of the constitutive SEC function, since it is stress-induced. Verified rather "
        "than assumed: GO:0090734 is not an is_a/part_of descendant of GO:0000785, so "
        "this and the chromatin row are separate claims."),
    supported_by=sb(Q_PARSTA))

# --- row 19 ----------------------------------------------------------------
verdict(("GO:0006354", "EXP", "PMID:22547686"),
    summary=(
        "Same term and same granularity issue as the IBA row, and given the same "
        "action for consistency. This is the human experimental row for AFF1's "
        "participation in transcription elongation, from the study that biochemically "
        "isolated the SEC family; the reference-projection test returns one annotation "
        "on one entity, so there is no projection concern."),
    action="MODIFY",
    reason=(
        "The very reference behind this row is what makes the polymerase specific: it "
        "reports that the SEC family members are Pol II C-terminal domain kinases. "
        "GO:0006368 was verified to be an is_a/part_of descendant of GO:0006354 before "
        "being proposed, so this is a one-step refinement toward the polymerase the "
        "experiment actually used."),
    proposed_replacement_terms=[dict(GO0006368)],
    supported_by=sb(Q_SEC_PURIFIED, Q_CTD_KINASE))

# --- row 20 ----------------------------------------------------------------
GO0032783 = term("GO:0032783", "super elongation complex")
verdict(("GO:0008023", "IDA", "PMID:22195968"),
    summary=(
        "Correct but one level less specific than the same curator's own reading of "
        "the same paper. UniProt's reference table for PMID:22195968 records its "
        "contribution as identification in the SEC complex, yet the annotation landed "
        "on the generic parent. The reference-projection test makes the pattern exact. "
        "Twenty-two gene products receive one of the two terms, 11 human and 11 "
        "Drosophila. All 10 recipients of the specific GO:0032783 are Drosophila, and "
        "ALL ELEVEN human recipients - AFF1, AFF4, CDK9, ELL, ELL2, ELL3, EAF1, EAF2, "
        "MLLT1, MLLT3 and ICE2 - got only the generic GO:0008023. The split is not "
        "purely clade-based: Drosophila Ell is the twelfth parent-only recipient, so "
        "10 of the 11 fly subunits were refined and none of the 11 human ones was."),
    action="MODIFY",
    reason=(
        "GO:0032783 was verified to be an is_a/part_of descendant of GO:0008023, and "
        "the specific term is already established for AFF1 by an independent human IDA, "
        "so this refinement asserts nothing new about the gene. What makes it worth "
        "acting on is the route the specific term took to get here: Drosophila lilli's "
        "GO:0032783 IPI comes from THIS paper, and that fly annotation is the donor of "
        "human AFF1's GO:0032783 IBA. So the specific term reached AFF1 by "
        "phylogenetic inference from a fly protein annotated in the same experiment "
        "that annotated the human protein one level up. Fixing it at the reference "
        "would retract the detour for all eleven human recipients at once; that "
        "recommendation is stated once, in suggested_questions, rather than repeated "
        "per gene."),
    proposed_replacement_terms=[dict(GO0032783)],
    supported_by=sb(Q_RP_SEC, Q_LEC, Q_ELL_AFF1))

# ---------------------------------------------------------------------------
# NEW rows
# ---------------------------------------------------------------------------

NEW_ROWS = [
    {
        "term": term("GO:0045668", "negative regulation of osteoblast differentiation"),
        "qualifier": "involved_in",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:28955517",
        "review": {
            "summary": (
                "Proposed as a new annotation. AFF1's best-characterised "
                "gene-specific human function has no representation in GOA at all. In "
                "human mesenchymal stromal cells, siRNA depletion of AFF1 increases "
                "alkaline phosphatase staining, mineralisation and Runx2/SP7/BGLAP "
                "expression, while lentiviral overexpression decreases them and "
                "reduces ectopic bone formation in vivo. AFF1 occupies the DKK1 "
                "promoter, sets DKK1 levels in both directions, and knocking DKK1 down "
                "abolishes the effect of AFF1 overexpression - so the intermediate is "
                "identified, not merely correlated."),
            "action": "NEW",
            "reason": (
                "Both directions were tested, which matters because GO's evidence "
                "codes do not distinguish them: the knockdown arm shows AFF1 is "
                "REQUIRED to restrain osteogenesis and the overexpression arm shows "
                "raising AFF1 is SUFFICIENT to suppress it. IMP is the right code for "
                "both, since the assays are siRNA depletion and ectopic expression "
                "rather than direct measurement at native levels. Sign matters here "
                "for a family reason: the same paper shows AFF4 has the OPPOSITE "
                "effect, so a term transferred between the two paralogues in either "
                "direction would invert the biology. Two caveats recorded rather than "
                "smoothed over - the paper carries a 2020 Correction (PMID:32257529) "
                "whose content is not stated in any retrievable record, and one "
                "sentence in its overexpression section says \"AFF1-depleted\" where "
                "the surrounding figure describes overexpressing cells; the claims "
                "above rest only on the unambiguous sentences."),
            "supported_by": sb(Q_KD_ALP, Q_OE_ALP, Q_CHIP_DKK1, Q_RESCUE, Q_INVIVO,
                               Q_OPPOSITE),
        },
    },
]

# ---------------------------------------------------------------------------
# assembly
# ---------------------------------------------------------------------------

def read_goa() -> list[dict]:
    if not GOA.exists():
        raise Fail(f"missing {GOA}; run `just fetch-gene human AFF1`")
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise Fail(f"{GOA} has no data rows")
    return rows


def existing_titles() -> dict[str, str]:
    """Reference titles from the seeded stub -- never written from memory."""
    if not STUB_TITLES_FROM.exists():
        return {}
    doc = yaml.safe_load(STUB_TITLES_FROM.read_text()) or {}
    out = {}
    for r in doc.get("references") or []:
        t = r.get("title")
        if r.get("id") and t and not t.startswith("TODO"):
            out[r["id"]] = t
    return out


def build() -> dict:
    rows = read_goa()
    titles = existing_titles()

    anns: list[dict] = []
    used: set[tuple[str, str, str]] = set()
    for i, r in enumerate(rows, start=1):
        key = (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"])
        if key not in VERDICTS:
            raise Fail(f"GOA row {i} has no verdict: {key}")
        used.add(key)
        v = VERDICTS[key]
        toks = [t.strip() for t in (r.get("WITH/FROM") or "").split("|") if t.strip()]
        ann: dict[str, Any] = {
            "term": term(r["GO TERM"], r["GO NAME"]),
            "qualifier": r["QUALIFIER"],
            "evidence_type": r["GO EVIDENCE CODE"],
            "original_reference_id": r["REFERENCE"],
        }
        if toks:
            ann["supporting_entities"] = list(toks)
        review: dict[str, Any] = {"summary": v["summary"], "action": v["action"]}
        if v.get("reason"):
            review["reason"] = v["reason"]
        if v.get("proposed_replacement_terms"):
            review["proposed_replacement_terms"] = [
                dict(t) for t in v["proposed_replacement_terms"]]
        if v.get("supported_by"):
            review["supported_by"] = [dict(x) for x in v["supported_by"]]
        if v.get("propagation_review"):
            pr = v["propagation_review"]
            # Build source_entities FROM the GOA field, and assert the set matches.
            got = {s["source_id"] for s in pr["source_entities"]}
            if got != set(toks):
                raise Fail(
                    f"row {i} ({key[0]}): propagation source set {sorted(got)} does "
                    f"not equal the GOA WITH/FROM set {sorted(toks)}")
            review["propagation_review"] = yaml.safe_load(
                yaml.safe_dump(pr))  # deep copy, no shared objects
        ann["review"] = review
        anns.append(ann)

    unused = set(VERDICTS) - used
    if unused:
        raise Fail(f"verdicts registered for rows that are not in the GOA TSV: "
                   f"{sorted(unused)}")

    for nr in NEW_ROWS:
        anns.append(yaml.safe_load(yaml.safe_dump(nr)))

    if len(anns) != len(rows) + len(NEW_ROWS):
        raise Fail("annotation count does not equal GOA rows plus NEW rows")

    # ---- references -------------------------------------------------------
    ref_ids = [
        "GO_REF:0000002", "GO_REF:0000033", "GO_REF:0000120",
        "PMID:8555498", "PMID:12629167", "PMID:15269783", "PMID:17135274",
        "PMID:20007461", "PMID:20159561", "PMID:21729782", "PMID:22190034",
        "PMID:22195968", "PMID:22547686", "PMID:23260655", "PMID:24367103",
        "PMID:28955517", "PMID:31611376", "PMID:41062835",
        "file:human/AFF1/AFF1-uniprot.txt",
        "file:human/AFF1/AFF1-bioinformatics/RESULTS.md",
        "file:human/AFF1/AFF1-deep-research-affinage.md",
    ]
    if len(set(ref_ids)) != len(ref_ids):
        raise Fail("duplicate reference id in the reference list")

    GO_REF_TITLES = {
        "GO_REF:0000002": "Gene Ontology annotation through association of InterPro "
                          "records with GO terms",
        "GO_REF:0000033": "Annotation inferences using phylogenetic trees",
        "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
    }
    FILE_TITLES = {
        "file:human/AFF1/AFF1-uniprot.txt":
            "UniProt entry P51825 (AFF1_HUMAN)",
        "file:human/AFF1/AFF1-bioinformatics/RESULTS.md":
            "AFF1 (P51825) annotation-provenance analysis",
        "file:human/AFF1/AFF1-deep-research-affinage.md":
            "Affinage mechanistic annotation for AFF1 (human)",
    }
    REVIEW_NOTES = {
        "PMID:41062835": (
            "PubMed-verified; supplies 7 of the 20 GOA rows. The cached record is "
            "abstract-only (full_text_available: false), so this review characterises "
            "only what the abstract states and defers to the curator on the direct "
            "assays. The reference-projection test (fully paginated) returns 8 "
            "annotations over 2 distinct entities, with the functional terms confined "
            "to AFF1, so it is not a complex-level projection. No retraction, erratum "
            "or expression of concern in its PubMed CommentsCorrections, and Crossref "
            "reports no update-to/updated-by relation."),
        "PMID:23260655": (
            "PubMed-verified; titled for AF9 but it holds the only quantitative "
            "binding measurement on human AFF1. What was assayed is a 14-residue AFF1 "
            "peptide (residues 761-774) against MBP-AF9 AHD, which the review states "
            "explicitly rather than presenting it as full-length protein."),
        "PMID:20159561": (
            "PubMed-verified; titled for AFF4. Checked which molecule underlies the "
            "AFF1 row: the GO:0032783 IDA rests on Flag-AFF4/Flag-ELL purifications "
            "recovering endogenous AFF1, not on the paper's MLL-AFF1 fusion "
            "constructs. Also the strongest available refutation of the claim that "
            "AFF1 recruits DOT1L."),
        "PMID:28955517": (
            "PubMed-verified. Carries an unflagged 2020 Correction (PMID:32257529) "
            "whose content is not stated in its abstract or its PMC record, and one "
            "sentence in the overexpression section says \"AFF1-depleted\" where the "
            "figure describes overexpressing cells; both are recorded in the notes and "
            "the claims used avoid that sentence. LOW_QUALITY is not the right flag - "
            "the experiments are sound and bidirectional - but the correction is "
            "unresolved."),
        "PMID:17135274": (
            "PubMed-verified, and cited here ONLY for what it actually shows: a mouse "
            "Af4 result. It carries an unflagged 2023 Erratum (PMID:37777189), and its "
            "DOT1L-recruitment claim rests on an ENL co-immunoprecipitate that "
            "PMID:20159561 reports was misinterpreted. Nothing in this review asserts "
            "DOT1L recruitment by AFF1."),
        "PMID:22190034": (
            "PubMed-verified. A systematic AP-MS survey of all 18 HIV-1 proteins; the "
            "projection test returns 183 annotations over 104 entities, all "
            "GO:0005515, so it is a screen rather than a targeted assay. The AFF1-Tat "
            "records are 3 IntAct entries from this one publication across two cell "
            "lines."),
        "PMID:24367103": (
            "PubMed-verified. Cached abstract-only, so nothing is asserted about its "
            "figures. Cited for the constitutive CDK9-CycT-AFF1 association and for "
            "the Tat/CycT1 mechanism, and used to note that raising Tat's affinity for "
            "cyclin T1 does not establish a direct AFF1-Tat contact."),
        "PMID:15269783": (
            "PubMed-verified. Cited only to record that the PFWT peptide is a synthetic "
            "inhibitor modelled on AFF1's AF9-binding domain, so its cellular effects "
            "are properties of the peptide and no GOA row rests on it - the "
            "peptide-pharmacology hazard checked and found absent from this gene's "
            "annotation set."),
        "PMID:8555498": (
            "PubMed-verified, and titled for the paralog LAF-4/AFF3 - which is why no "
            "AFF1-keyed search surfaces it. It reports that AF-4 as well as LAF-4 has "
            "a domain that transactivates when fused to the GAL4 DNA-binding domain. "
            "Not used to support a term: the molecule assayed is a GAL4 chimera, so it "
            "shows a region can activate when artificially tethered, not that AFF1 "
            "does so natively. GOA uses this reference for AFF3's nucleus IDA and not "
            "at all for AFF1."),
        "PMID:22547686": (
            "PubMed-verified; cached abstract-only. Supplies AFF1's only EXP-coded row "
            "and, importantly for two MODIFY calls, states that the SEC family members "
            "are RNA polymerase II CTD kinases and that AFF2/AFF3 occupy the SEC-L2 "
            "and SEC-L3 variants."),
        "PMID:22195968": (
            "PubMed-verified; cached abstract-only. UniProt's own reference table "
            "records its contribution as identification in the SEC complex, which is "
            "the basis for refining the GO:0008023 row. Its projection profile is what "
            "revealed that the same reference gave the specific complex term to 10 "
            "Drosophila recipients and only the generic parent to all 11 human ones."),
        "PMID:31611376": (
            "PubMed-verified, full text available. The acetyl-mimic rescue experiment "
            "here is the cleanest evidence that the bridging function is AFF1's own "
            "rather than an emergent property of SEC, and it is why "
            "GO:0030674 is placed in molecular_function while the elongation-factor "
            "and coregulator terms are placed in "
            "contributes_to_molecular_function."),
        "PMID:21729782": (
            "PubMed-verified. Source of one AFF1-AF9 protein-binding row via SEC "
            "co-purification with Mediator; the projection test returns 26 annotations "
            "over 17 entities, all GO:0005515, i.e. an interaction network."),
        "PMID:12629167": (
            "PubMed-verified. Mouse; and a gain-of-function model - the robotic allele "
            "stabilises Af4 rather than removing it - which is why the nervous-system "
            "row is kept as non-core rather than promoted."),
        "file:human/AFF1/AFF1-deep-research-affinage.md": (
            "Adjudicated and deliberately not used as evidence anywhere in this "
            "review; recorded here so the judgement lives in the repository. Its "
            "gates_passed: True and faith_pct: 100.0 concern PRECISION - the 23 "
            "citations are all well-formed numeric PMIDs with no preprint ids in "
            "PMID-shaped fields. Recall was measured, not estimated: of the 7 PMIDs "
            "that AFF1's GOA rows actually cite, affinage returned 0, including the "
            "2026 paper behind 7 of the 20 rows (computed in RESULTS.md section G). "
            "Four substantive defects: two cited papers carry unflagged corrections "
            "(PMID:28955517 -> PMID:32257529; PMID:17135274 -> PMID:37777189); the "
            "claim that AFF1 recruits DOT1L is contradicted by PMID:20159561; a stated "
            "hypothesis in PMID:12629167 is reported as demonstrated causation; and a "
            "result PMID:20007461 attributes to \"the AF4 transcriptional regulatory "
            "complex\" is attributed to Af4 alone. LOW_QUALITY refers to this record "
            "as a source, not to the underlying papers."),
        "PMID:20007461": (
            "PubMed-verified. Mouse Purkinje cells; cited only as the tissue-specific "
            "downstream consequence supporting the non-core nervous-system call."),
    }
    RELEVANCE = {
        "PMID:41062835": "HIGH", "PMID:23260655": "HIGH", "PMID:20159561": "HIGH",
        "PMID:31611376": "HIGH", "PMID:28955517": "HIGH", "PMID:22547686": "HIGH",
        "PMID:22195968": "HIGH", "PMID:24367103": "HIGH",
        "PMID:21729782": "MEDIUM", "PMID:22190034": "MEDIUM",
        "PMID:17135274": "MEDIUM", "PMID:12629167": "MEDIUM",
        "PMID:20007461": "MEDIUM", "PMID:8555498": "MEDIUM",
        "PMID:15269783": "LOW",
        "GO_REF:0000002": "LOW", "GO_REF:0000033": "HIGH", "GO_REF:0000120": "LOW",
        "file:human/AFF1/AFF1-uniprot.txt": "HIGH",
        "file:human/AFF1/AFF1-bioinformatics/RESULTS.md": "HIGH",
        "file:human/AFF1/AFF1-deep-research-affinage.md": "LOW",
    }
    CORRECTNESS = {
        "PMID:17135274": "DISPUTED",
        "PMID:28955517": "DISPUTED",
        "file:human/AFF1/AFF1-deep-research-affinage.md": "LOW_QUALITY",
    }

    refs = []
    for rid in ref_ids:
        if rid.startswith("PMID:"):
            title = titles.get(rid) or title_from_cache(rid)
        elif rid.startswith("GO_REF:"):
            title = titles.get(rid) or GO_REF_TITLES[rid]
        else:
            title = FILE_TITLES[rid]
        entry: dict[str, Any] = {"id": rid, "title": title}
        rr: dict[str, Any] = {"relevance": RELEVANCE[rid],
                              "correctness": CORRECTNESS.get(rid, "VERIFIED")}
        if rid in REVIEW_NOTES:
            rr["review_notes"] = REVIEW_NOTES[rid]
        elif rid.startswith("GO_REF:"):
            rr["review_notes"] = (
                "A GO reference, not a publication; cited because GOA rows point at "
                "it. Its WITH/FROM tokens were resolved individually and are recorded "
                "per row.")
        else:
            rr["review_notes"] = (
                "Machine-fetched project artifact; every quotation from it was "
                "verified with an exact-substring check that also requires the span to "
                "lie inside one physical line, because the repo's reference validator "
                "skips file: quotes entirely.")
        entry["reference_review"] = rr
        if rid in {"PMID:41062835", "PMID:24367103", "PMID:22547686",
                   "PMID:22195968", "PMID:21729782", "PMID:22190034",
                   "PMID:17135274", "PMID:12629167", "PMID:20007461",
                   "PMID:21030982", "PMID:8555498", "PMID:15269783"}:
            entry["full_text_unavailable"] = True
        refs.append(entry)

    # ---- core functions ---------------------------------------------------
    core_functions = [
        {
            "description": (
                "AFF1 is the scaffolding subunit of one branch of the super elongation "
                "complex. It binds the CDK9-cyclin T (P-TEFb) kinase module "
                "constitutively and, through a short motif that folds only on binding, "
                "grips the AF9 ANC1-homology domain with sub-nanomolar affinity, "
                "joining P-TEFb to the AF9/ENL and ELL/EAF modules. Holding those "
                "modules together is what the complex needs from AFF1: a single "
                "acetylation-mimicking substitution in AFF1 loses SEC assembly and, "
                "with it, P-TEFb-dependent phosphorylation of the RNA polymerase II "
                "C-terminal domain, so paused polymerase is not released into "
                "productive elongation."),
            "supported_by": sb(Q_KD, Q_ORDERED, Q_HYDROPHOBIC, Q_REEXPRESS, Q_ACETYL,
                               Q_PTEFB, Q_SUBUNIT, Q_ELL_AFF1),
            "molecular_function": dict(GO0030674),
            "contributes_to_molecular_function": term(
                "GO:0003711", "transcription elongation factor activity"),
            "directly_involved_in": [
                dict(GO0006368),
                dict(GO0032968),
            ],
            "locations": [
                term("GO:0005634", "nucleus"),
                term("GO:0000785", "chromatin"),
            ],
            "in_complex": dict(GO0032783),
        },
        {
            "description": (
                "AFF1 is the point at which transcription is switched off and back on "
                "around DNA damage, and it is switched by post-translational "
                "modification of AFF1 itself rather than by changing its partners. "
                "Early after genotoxic exposure p300 acetylates AFF1, which loosens "
                "its contacts with the other SEC subunits and lowers polymerase II "
                "C-terminal domain phosphorylation genome-wide; PARP1 then binds AFF1 "
                "and poly(ADP-ribosyl)ates it in the region the E3 ligase Siah1 "
                "targets, blocking its ubiquitination and stabilising it, which "
                "supports the resumption of transcription. Cells lacking AFF1 repair "
                "DNA and survive genotoxic stress poorly."),
            "supported_by": sb(Q_PARSTA, Q_DEPLETION, Q_ACETYL, Q_REEXPRESS),
            "directly_involved_in": [
                term("GO:0006974", "DNA damage response"),
                dict(GO0032968),
            ],
            "locations": [
                term("GO:0090734", "site of DNA damage"),
                term("GO:0000785", "chromatin"),
            ],
            "in_complex": dict(GO0032783),
        },
        {
            "description": (
                "In mesenchymal stromal cells AFF1 restrains the osteoblast programme "
                "by driving transcription of DKK1, the secreted Wnt antagonist. Its "
                "level sets the outcome in both directions: depleting AFF1 raises "
                "alkaline phosphatase, mineralisation and Runx2/SP7/BGLAP, while "
                "raising AFF1 suppresses them and reduces ectopic bone formation in "
                "vivo, and removing DKK1 abolishes the effect of excess AFF1 - so "
                "DKK1 is the operative intermediate rather than a correlate. This is a "
                "tissue-specific output of the same elongation activity rather than a "
                "separate biochemistry, and it is one of the places where AFF1 and its "
                "closest paralogue AFF4 act in opposite directions."),
            "supported_by": sb(Q_KD_ALP, Q_OE_ALP, Q_CHIP_DKK1, Q_RESCUE, Q_INVIVO,
                               Q_OPPOSITE),
            "directly_involved_in": [
                term("GO:0045668", "negative regulation of osteoblast differentiation"),
                dict(GO0006355),
            ],
            "contributes_to_molecular_function": term(
                "GO:0003712", "transcription coregulator activity"),
            "locations": [
                term("GO:0000785", "chromatin"),
            ],
        },
    ]

    # ---- assemble ---------------------------------------------------------
    doc: dict[str, Any] = {
        "id": "P51825",
        "gene_symbol": "AFF1",
        "product_type": "PROTEIN",
        "status": "COMPLETE",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": (
            "AFF1 (also called AF4, and the founding member of the AF4/FMR2 family) is "
            "a large nuclear protein, about three-quarters of whose 1210 residues are "
            "intrinsically disordered, that works as a scaffold rather than as an "
            "enzyme or a sequence-specific DNA-binding factor. It is the subunit that holds together one branch of "
            "the super elongation complex: it is constitutively bound to the "
            "CDK9-cyclin T kinase P-TEFb and is present in every major P-TEFb "
            "assembly, and a short motif in its middle folds onto the ANC1-homology "
            "domain of AF9 with sub-nanomolar affinity, tying P-TEFb to the AF9/ENL "
            "and ELL/EAF modules on chromatin. Through that complex AFF1 promotes the "
            "release of promoter-paused RNA polymerase II into productive elongation, "
            "which depends on P-TEFb phosphorylating the polymerase C-terminal domain. "
            "Its own abundance and modification state make it a control point rather "
            "than a passive strut: p300 acetylation loosens the complex and shuts "
            "transcription down soon after DNA damage, while PARP1-dependent "
            "poly(ADP-ribosyl)ation protects AFF1 from Siah1-directed ubiquitination "
            "and supports transcriptional restart, and cells short of AFF1 repair DNA "
            "and survive genotoxic stress poorly. Its gene-specific outputs include "
            "the Wnt antagonist DKK1, through which AFF1 restrains osteoblast "
            "differentiation in mesenchymal stromal cells - the opposite of what its "
            "closest paralogue AFF4 does there. AFF1 is also the most frequent partner "
            "fused to KMT2A/MLL by the t(4;11)(q21;q23) translocation of infant acute "
            "lymphoblastic leukaemia; the resulting chimera is a distinct oncoprotein, "
            "and its properties are not simply those of the wild-type protein."),
        "existing_annotations": anns,
        "core_functions": core_functions,
        "references": refs,
    }

    doc["proposed_new_terms"] = [
        {
            "proposed_name": "transcriptional restart after DNA damage",
            "proposed_definition": (
                "The resumption of RNA polymerase II transcription following the "
                "transcriptional shutdown that DNA damage induces, once lesions have "
                "been repaired or bypassed."),
            "proposed_parent": term("GO:0006974", "DNA damage response"),
            "justification": (
                "GO has no term for this process. Verified on a working endpoint "
                "rather than inferred from an empty search: a control query for "
                "\"super elongation complex\" returns GO:0032783 first, five phrasings "
                "of the restart concept return nothing relevant, and none of the 96 "
                "is_a/part_of descendants of GO:0006974 has \"recover\", \"restart\" or "
                "\"resum\" in its name. The consequence is visible in this gene's "
                "record: the one process that PMID:41062835 and PMID:31611376 jointly "
                "describe - AFF1 acetylation shutting SEC down early after genotoxic "
                "stress, AFF1 PARylation stabilising it for recovery - has to be "
                "expressed as an unrelated pair of terms, GO:0006974 plus GO:0032968, "
                "which loses the fact that AFF1 is the switch for both halves. The "
                "field treats recovery as a distinct, separately assayed phase of the "
                "damage response, so a child of GO:0006974 would let it be annotated "
                "as one process."),
            "supported_by": sb(Q_PARSTA, Q_ACETYL),
        },
    ]

    doc["suggested_questions"] = [
        {"question": (
            "PAINT/UniProt curation, stated once for all affected genes: "
            "PMID:22195968 gives GO:0032783 super elongation complex to 10 Drosophila "
            "recipients and only the generic parent GO:0008023 to all eleven of its "
            "human recipients - AFF1, AFF4, CDK9, ELL, ELL2, ELL3, EAF1, EAF2, MLLT1, "
            "MLLT3 and ICE2 - even though UniProt's own reference table records the "
            "paper's contribution as \"IDENTIFICATION IN THE SEC COMPLEX\". The "
            "consequence is a detour: Drosophila lilli's GO:0032783 IPI from this paper "
            "is the donor of human AFF1's GO:0032783 IBA, so the specific term reaches "
            "the human gene by phylogenetic inference from a fly protein annotated in "
            "the same experiment. Would GOA consider refining the human rows at the "
            "reference, which would fix eleven gene products in one edit? Note the "
            "split is not purely clade-based - Drosophila Ell also received only the "
            "parent - so this is a per-annotation gap rather than a rule about "
            "clades."),
         "experts": ["GOA/UniProt curators", "GO Central PAINT curators"]},
        {"question": (
            "PANTHER node PTN000829417 assigns, to the same 79 recipients, both "
            "GO:0032783 - whose definition is explicitly about RNA polymerase II "
            "elongation - and the polymerase-agnostic GO:0006354. Since every "
            "characterised SEC substrate is Pol II, would PAINT consider moving the "
            "process term to GO:0006368 transcription elongation by RNA polymerase II "
            "at the node, which would refine all four human AFF paralogues at once? "
            "Separately, InterPro2GO gives the same family GO:0010468 via IPR007797 "
            "while PAINT gives GO:0006355, so the two pipelines differ by one level on "
            "the same family."),
         "experts": ["GO Central PAINT curators", "InterPro2GO curators"]},
        {"question": (
            "MGI curation gap: the AFF1-specific nervous-system literature is a mouse "
            "phenotype - the robotic allele stabilises Af4 and causes Purkinje-cell "
            "loss with ataxia (PMID:12629167), with Af4 regulating Igf-1 in Purkinje "
            "cells (PMID:20007461) - yet mouse Aff1 carries no nervous-system term, and "
            "human AFF1's GO:0050877 IBA therefore rests on the paralogues Aff2 and "
            "lilli instead of on the ortholog. Would MGI consider annotating the "
            "robotic phenotype?"),
         "experts": ["MGI curators"]},
        {"question": (
            "Do AFF1 and AFF4 ever occupy the same super elongation complex? "
            "PMID:28955517's discussion states they \"are not found together in a "
            "single SEC\" and UniProt models them as alternative occupants of one slot "
            "(\"AFF (AFF1 or AFF4)\"), but IntAct records an AFF1-AFF4 physical "
            "association across 8 records and 2 distinct publications at MI-score 0.6, "
            "and PMID:20159561's Flag-AFF4 purification recovers endogenous AFF1. If "
            "they are genuinely mutually exclusive, GO cannot currently say so - "
            "GO:0032783 has no children and ComplexPortal's seven AFF1-containing "
            "entries all list AFF1 and AFF4 together."),
         "experts": ["transcription elongation biologists", "ComplexPortal curators"]},
        {"question": (
            "UniProt: would a FUNCTION comment be considered for P51825? The entry "
            "currently has none, despite a solved partner complex, a measured "
            "dissociation constant, a curated SUBUNIT line and a 2026 primary paper on "
            "its role in transcriptional recovery. The SUBCELLULAR LOCATION line is "
            "also still ECO:0000305 curator inference although an experimental IDA now "
            "exists (PMID:41062835). Third item, raised here because ActionEnum has no "
            "qualifier-change action so it cannot be expressed on the row itself: "
            "GO:0003711 transcription elongation factor activity is annotated with the "
            "enables qualifier, but the activity is delivered by the assembled SEC and "
            "the evidence is an AFF1 knockdown, so contributes_to would be the "
            "strictly correct qualifier. The term is right; only the qualifier "
            "overstates AFF1's independence."),
         "experts": ["UniProt curators"]},
        {"question": (
            "Is AFF1's molecular adaptor role better modelled on AFF1, on AF9, or on "
            "both? UniProt assigned GO:0060090 molecular adaptor activity to AF9 "
            "(P42568) from PMID:23260655, and this review proposes GO:0030674 for AFF1 "
            "from the same interaction plus the acetyl-mimic rescue. Both proteins are "
            "hubs, but for different ligand sets, and a curator's view on whether "
            "adaptor activity should be annotated reciprocally would be useful."),
         "experts": ["GO Central curators", "UniProt curators"]},
    ]

    doc["suggested_experiments"] = [
        {"hypothesis": (
            "AFF1-containing and AFF4-containing super elongation complexes are "
            "mutually exclusive assemblies rather than one complex carrying both."),
         "description": (
            "Sequential immunodepletion followed by quantitative mass spectrometry: "
            "deplete AFF1 from nuclear extract to exhaustion, then ask whether the "
            "remaining ELL/EAF/P-TEFb/AF9 pool still contains AFF4 at "
            "near-stoichiometric levels, and repeat in the opposite order. Pair it with "
            "single-molecule two-colour photobleaching on complexes purified through a "
            "third subunit (ELL2 or EAF1) to count AFF1 and AFF4 copies per particle. "
            "This distinguishes genuine co-occupancy from an average over two "
            "populations, which is what a bulk co-immunoprecipitation cannot do and "
            "which is why the current evidence is contradictory."),
         "experiment_type": "biochemistry"},
        {"hypothesis": (
            "The bridging function of AFF1 is separable from its abundance, so the "
            "transcriptional-restart phenotype after DNA damage is caused by loss of "
            "SEC assembly rather than by loss of AFF1 protein per se."),
         "description": (
            "Knock in, at the endogenous locus, the acetylation-mimic and "
            "acetylation-defective AFF1 alleles used in PMID:31611376 together with a "
            "PARylation-site mutant of the Siah1-targeted region from PMID:41062835, "
            "then measure recovery of nascent transcription after UV or "
            "camptothecin by TT-seq alongside AFF1 protein levels and SEC composition. "
            "The informative outcome is a separation: an allele that keeps normal AFF1 "
            "abundance but fails to recover transcription would show the defect is "
            "assembly, not dosage."),
         "experiment_type": "genetics"},
        {"hypothesis": (
            "AFF1 and AFF4 direct SEC to non-overlapping gene sets, and the osteogenic "
            "sign inversion between them follows from that target split rather than "
            "from different biochemistry."),
         "description": (
            "In one human mesenchymal stromal cell background, perform paired "
            "degron-mediated acute depletion of AFF1 and of AFF4 with TT-seq and "
            "Pol II PRO-seq readouts, plus ChIP-seq for each paralogue. Then swap the "
            "AF9-binding motifs between them and ask whether target selection follows "
            "the motif or the rest of the protein. A negative control is built in: if "
            "the two depletions converge on the same genes, the differential "
            "osteogenesis result requires another explanation."),
         "experiment_type": "genomics"},
        {"hypothesis": (
            "AFF1 contacts HIV-1 Tat directly, rather than only raising Tat's affinity "
            "for cyclin T1 within a ternary complex."),
         "description": (
            "Measure binding of recombinant Tat to purified AFF1 fragments by "
            "isothermal titration calorimetry and NMR chemical-shift perturbation, "
            "with and without cyclin T1 present, and attempt a co-structure of the "
            "AFF1 region that is not the AF9-binding motif. AFF4-Tat-P-TEFb structures "
            "exist and AFF1 has none, so the honest current position is that the "
            "GO:0005515 row rests on affinity purification and a functional "
            "requirement, not on a mapped contact."),
         "experiment_type": "structural_biology"},
        {"hypothesis": (
            "The transactivation activity reported for an AF-4 GAL4 fusion in 1996 "
            "reflects a function the native protein performs at its own target "
            "promoters."),
         "description": (
            "The original result used a GAL4-DNA-binding-domain chimera, so it shows a "
            "region can activate when artificially tethered and cannot show what AFF1 "
            "does natively - which is why no GO term is proposed from it here. Test it "
            "properly by tethering the same region with a catalytically dead dCas9 to "
            "endogenous AFF1 target promoters identified by ChIP-seq, and by deleting "
            "that region at the endogenous locus and measuring nascent transcription of "
            "those same promoters."),
         "experiment_type": "genetics"},
    ]

    doc["knowledge_gaps"] = [
        {"gap_statement": (
            "Whether AFF1 and AFF4 can occupy the same super elongation complex is "
            "unresolved, and the evidence points both ways. UniProt models them as "
            "alternative occupants of one slot and PMID:28955517's discussion states "
            "they are not found together, but IntAct records an AFF1-AFF4 association "
            "across 8 records and 2 distinct publications at MI-score 0.6 and "
            "PMID:20159561's AFF4 purification recovers endogenous AFF1."),
         "boundary": (
            "What is settled is that the two paralogues are not functionally "
            "interchangeable: depleting AFF1 does not destabilise ELL1 or P-TEFb "
            "whereas depleting AFF4 does, their SEC target genes are reported as "
            "largely non-overlapping, and in mesenchymal stromal cells they act in "
            "opposite directions on osteogenesis. What is not settled is complex "
            "stoichiometry, which bulk co-immunoprecipitation cannot decide because it "
            "averages over populations."),
         "gap_kind": ["BIOLOGY"],
         "dark_aspect": "CC_DARK",
         "status": "OPEN",
         "significance": (
            "It determines whether GO:0032783 needs paralogue-specific children. No "
            "such children are proposed here, because proposing terms for a "
            "distinction the evidence does not settle would be an over-annotation of "
            "the opposite sign."),
         "provenance": sb(Q_SUBUNIT, Q_NOT_TOGETHER, Q_AFF1_NOT_AFF4)},
        {"gap_statement": (
            "AFF1's subnuclear distribution is described inconsistently. Older "
            "immunofluorescence reports discrete punctate compartments ('AF4 bodies') "
            "where AF4 and AF9 co-localise, while PMID:28955517's discussion describes "
            "AFF1 as diffuse and reserves nuclear speckles for AFF4. GOA reflects the "
            "uncertainty by giving AFF1 no subnuclear term at all, while AFF4 has "
            "nucleoplasm and nuclear body and AFF2 has nuclear speck."),
         "boundary": (
            "Nuclear localisation itself is settled, by IDA and by immunofluorescence "
            "in several cell types. Chromatin association is settled, by ChIP at DKK1 "
            "and at MYC. What is unresolved is whether AFF1 concentrates in a defined "
            "subnuclear body."),
         "gap_kind": ["BIOLOGY"],
         "dark_aspect": "CC_DARK",
         "status": "OPEN",
         "significance": (
            "No subnuclear term is proposed for AFF1 here. The absence of one in GOA "
            "appears to be appropriate caution rather than a coverage gap."),
         "provenance": sb(Q_SUBCELL, Q_NOT_TOGETHER)},
        {"gap_statement": (
            "Whether AFF1 has any molecular function outside a super elongation "
            "complex is unknown. Every measurement on the protein is made either "
            "within SEC or on a short peptide from it, and its only solved structure "
            "is 42 residues bound to a partner; 901 of its 1210 residues (74.5%) are "
            "annotated as disordered, most of it with no assigned interaction."),
         "boundary": (
            "The SEC-dependent activity is well established and quantified. What is "
            "unmapped is the function of the large disordered regions outside the "
            "AF9-binding motif and the Siah1/PARylation region - including the nine "
            "MS-detected phosphosites and one acetylation site, none of which has an "
            "assigned consequence."),
         "gap_kind": ["BIOLOGY"],
         "dark_aspect": "MF_DARK",
         "status": "OPEN",
         "significance": (
            "This is why GO:0030674 is proposed as the molecular function rather than "
            "anything narrower, and why the elongation-factor and coregulator terms "
            "are recorded as contributions to a complex."),
         "provenance": sb(Q_RP_NMR, Q_ORDERED)},
        {"gap_statement": (
            "What the wild-type AFF1 protein contributes to t(4;11) leukaemogenesis, "
            "as distinct from the MLL-AFF1 chimera, is not established. The chimera is "
            "a different molecule with its own composition, and the peptide inhibitor "
            "PFWT that kills t(4;11) cells is a synthetic reagent modelled on AFF1's "
            "AF9-binding domain rather than the gene product."),
         "boundary": (
            "The AF9-binding motif itself is mapped and quantified on wild-type AFF1. "
            "What is not separable from the current data is which leukaemia phenotypes "
            "require the remaining wild-type allele's own activity."),
         "gap_kind": ["BIOLOGY"],
         "dark_aspect": "BP_DARK",
         "status": "OPEN",
         "significance": (
            "No GOA row for AFF1 rests on the fusion or on the peptide, which is the "
            "correct state; this gap records why no leukaemia process term is proposed "
            "here."),
         "provenance": sb(Q_PFWT, Q_KD)},
    ]

    return doc


class NoAliasDumper(yaml.SafeDumper):
    """Never emit anchors/aliases: an alias multiplies one quote across N rows so
    every gate verifies the same string N times and reports N successes."""

    def ignore_aliases(self, data: Any) -> bool:  # noqa: D102
        return True


def main() -> int:
    doc = build()
    text = yaml.dump(doc, Dumper=NoAliasDumper, sort_keys=False,
                     allow_unicode=True, width=100, default_flow_style=False)
    if "&id" in text or re.search(r"\*id\d+", text):
        raise Fail("an anchor or alias survived the dump")
    OUT.write_text(text)

    if Q.checked_file == 0:
        raise Fail("verified zero `file:` quotes -- since the repo validator skips "
                   "them entirely, a build that checks none has no coverage where "
                   "coverage matters most")
    if Q.checked_pmid == 0:
        raise Fail("verified zero PMID quotes")
    print(f"wrote {OUT.relative_to(REPO)}")
    print(f"verified {Q.checked_pmid} PMID quotes and {Q.checked_file} file: quotes "
          f"before writing")
    n = len(doc["existing_annotations"])
    print(f"{n} annotation entries ({n - len(NEW_ROWS)} GOA rows + "
          f"{len(NEW_ROWS)} NEW)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
