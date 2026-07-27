#!/usr/bin/env python3
"""Emit ``ADIPOQ-ai-review.yaml`` with exactly one entry per GOA row.

Why a builder rather than hand-editing: the GOA TSV has **161** rows and the
``fetch-gene`` stub seeds only 103, because
``GOAValidator.seed_missing_annotations`` keys entries on
``(GO id, evidence, reference, negated, qualifier)`` and omits ``WITH/FROM``.
Restoring 58 per-partner rows by hand, and keeping their verdicts consistent,
is exactly the "fixed in N places, landed in N-1" failure this campaign keeps
hitting.  So the mapping is a table, the emission is mechanical, and coverage
is asserted rather than eyeballed.

**This file is the source of truth for the review YAML.**  Do not hand-edit the
emitted YAML; change the table here and re-run.  ``audit_review.py`` runs over
the *emitted file* (the artifact a reviewer greps), not over this source.

Design rules honoured:
  * dump through a SafeDumper with ``ignore_aliases -> True`` and assert no
    ``&id`` anchor survives, so every row is an independent object and raw text
    counts are meaningful (an alias silently *multiplies* a quote);
  * no prose constant spans rows whose ``action`` differs -- the action-specific
    clause is attached per action, never shared;
  * coverage is asserted against the TSV, and the script fails loudly.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA_TSV = GENE_DIR / "ADIPOQ-goa.tsv"
OUT = GENE_DIR / "ADIPOQ-ai-review.yaml"

RESULTS_REF = "file:human/ADIPOQ/ADIPOQ-bioinformatics/RESULTS.md"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # noqa: D102, ARG002
        return True


def st(ref, text, **kw):
    d = {"reference_id": ref, "supporting_text": text}
    d.update(kw)
    return d


# --------------------------------------------------------------------------
# shared prose, split so no constant spans differing actions
# --------------------------------------------------------------------------

SCREEN_PREMISE = (
    "This row comes from a systematic binary-interactome screen, not from a "
    "hypothesis-led experiment on adiponectin. IntAct records 286 interactions "
    "for Q15848 across only 7 publications, of which 171 are from the single "
    "HuRI dataset (PMID:32296183) and 196 are two-hybrid, logged under five "
    "sub-method names (two hybrid array, validated two hybrid, two hybrid prey "
    "pooling approach, two hybrid pooling, two hybrid bait and prey pooling "
    "approach) - which is why UniProt shows NbExp=3 on nearly every partner "
    "even though there is one experiment. 240 of 264 IntAct partners appear in "
    "exactly one publication, and no orthogonal biophysical assay (SPR, ITC, "
    "co-immunoprecipitation of endogenous protein) supports any of them."
)
SCREEN_TOPOLOGY = (
    "Adiponectin is synthesised with a cleaved signal peptide (SIGNAL 1..18) "
    "and its mature chain is secreted; two-hybrid requires both partners to "
    "reconstitute a transcription factor in the yeast nucleus, a compartment "
    "the native protein never enters. Its assembly into disulfide-linked "
    "hexamers and HMW multimers, and the hydroxylation/glycosylation those "
    "multimers depend on, also cannot occur in that assay."
)
SCREEN_OVERANN_TAIL = (
    "Marked as over-annotated rather than removed: an unreplicated screen hit "
    "is unmeasured, not refuted, and a bare protein binding term carries no "
    "functional information either way."
)

ROLE_CONFLATION_NOTE = (
    "Adiponectin is a secreted hormone: it does not itself carry out glucose "
    "or fatty-acid metabolism, it changes the rate at which responding cells "
    "do so, via AdipoR1/AdipoR2 and AMPK."
)

# --------------------------------------------------------------------------
# per-(term, evidence, reference) decisions.  GO:0005515 is handled separately.
# --------------------------------------------------------------------------

D: dict[tuple, dict] = {}


def dec(term, ev, ref, **kw):
    D[(term, ev, ref)] = kw


# ---- molecular function ---------------------------------------------------

_HORMONE_SUMMARY = (
    "Adiponectin is a bona fide adipocyte-derived endocrine hormone and this "
    "is its core molecular function."
)
_HORMONE_REASON = (
    "GO:0005179 is defined as the action of 'any substance formed in very "
    "small amounts in one specialized organ or group of cells and carried "
    "(sometimes in the bloodstream) to another organ or group of cells in the "
    "same organism, upon which it has a specific regulatory action'. "
    "Adiponectin is made only by adipocytes, circulates in plasma at 5-30 "
    "ug/ml, and acts on liver, skeletal muscle, macrophages, endothelium and "
    "kidney through AdipoR1, AdipoR2 and T-cadherin. The definition is met "
    "exactly, and this term - not the coarser signaling receptor binding, and "
    "not extracellular matrix or interaction-screen terms - is what the gene "
    "is for."
)
for ev, ref in [("IBA", "GO_REF:0000033"), ("IDA", "PMID:11222466"),
                ("IDA", "PMID:18703020"), ("IEA", "GO_REF:0000107"),
                ("ISS", "GO_REF:0000024")]:
    dec("GO:0005179", ev, ref, action="ACCEPT", summary=_HORMONE_SUMMARY,
        reason=_HORMONE_REASON)

D[("GO:0005179", "IBA", "GO_REF:0000033")]["reason"] += (
    " The IBA is self-referential - its WITH/FROM is "
    "MGI:MGI:106675|PANTHER:PTN008559544|UniProtKB:Q15848, i.e. it includes "
    "ADIPOQ itself - so it records a PAINT curator judging this function core "
    "rather than importing it from elsewhere. Both donor tokens resolve and "
    "both carry their own experimental evidence for the term (MGI:MGI:106675 "
    "= Q60994 ADIPO_MOUSE, IDA). Node PTN008559544 reaches exactly one human "
    "gene, ADIPOQ, checked against all 82 human GO:0005179 IBA rows.")
D[("GO:0005179", "IBA", "GO_REF:0000033")]["propagation_review"] = {
    "root_cause": "NO_FAILURE_CORE",
    "source_entities": [
        {"source_id": "MGI:MGI:106675",
         "comment": "mouse Adipoq (Q60994, Swiss-Prot); carries its own "
                        "IDA for this term"},
        {"source_id": "PANTHER:PTN008559544",
         "comment": "ancestral node; human reach is exactly ADIPOQ"},
        {"source_id": "UniProtKB:Q15848",
         "comment": "self-reference - the target gene is its own IBD seed"},
    ]}
D[("GO:0005179", "IDA", "PMID:11222466")]["supported_by"] = [
    st("PMID:11222466",
       "The adipocyte-derived plasma protein adiponectin suppressed "
       "macrophage-to-foam cell transformation")]
D[("GO:0005179", "IDA", "PMID:18703020")]["supported_by"] = [
    st("PMID:18703020",
       "APN up-regulated the expression of ABCA1 in human macrophages")]

_SRB = (
    "Adiponectin binds AdipoR1 and AdipoR2 (PMID:12802337) and T-cadherin "
    "(PMID:15210937), so the term is correct and experimentally well founded. "
    "It is worth being precise about how it relates to the gene's other "
    "molecular-function rows, because the two look redundant and are not: "
    "GO:0005102 signaling receptor binding is a BINDING term, whereas "
    "GO:0005179 hormone activity sits in the ACTIVITY branch, under GO:0048018 "
    "receptor ligand activity -> GO:0140677 molecular function activator "
    "activity -> GO:0098772 molecular function regulator activity. "
    "GO:0005102 is NOT among GO:0005179's is_a/part_of ancestors (verified "
    "against QuickGO and recorded under term_relations in "
    "ADIPOQ-bioinformatics/results.json). The two rows therefore state "
    "different things - that adiponectin physically engages a receptor, and "
    "that engaging it activates the receptor - and neither subsumes the other."
)
for ref in ["GO_REF:0000024", "PMID:12368907"]:
    dec("GO:0005102", "ISS", ref, action="ACCEPT",
        summary="Adiponectin binds its signalling receptors; kept as the "
                "general-grain statement of the core ligand function.",
        reason=_SRB)

dec("GO:0005125", "NAS", "PMID:12611609", action="KEEP_AS_NON_CORE",
    summary="Adiponectin has genuine cytokine-like actions on myeloid cells, "
            "but its defining molecular function is endocrine, not cytokine.",
    reason=(
        "GO:0005125 is defined as 'the activity of a soluble extracellular "
        "gene product that interacts with a receptor to effect a change in the "
        "activity of the receptor to control the survival, growth, "
        "differentiation and effector function of tissues and cells'. "
        "Adiponectin does act on macrophages and myelomonocytic progenitors "
        "(PMID:10961870), so the term is not wrong. It is retained as "
        "non-core because the evidence is NAS - an author statement in a "
        "review article, the only two annotations that reference carries in "
        "all of GOA - and because the gene's characterised identity is a "
        "circulating metabolic hormone rather than an immune mediator."))

dec("GO:0005201", "RCA", "PMID:28675934", action="REMOVE",
    summary="Adiponectin is a circulating hormone, not a structural component "
            "of the extracellular matrix; this row is a bulk computational "
            "block that converted matrisome detection into a structural role.",
    reason=(
        "Three independent grounds. (1) Provenance: PMID:28675934 is an ECM "
        "proteomics survey, and in GOA it assigns GO:0005201 by RCA to 41 "
        "entities, together with GO:0030020, GO:0030021 and GO:0030023 - the "
        "collagen tensile-strength terms - to 31, 8 and 4 more. That is a "
        "computational block over a matrisome protein list, not a measurement "
        "of adiponectin's contribution to matrix integrity. (2) The term's "
        "definition is 'the action of a molecule that contributes to the "
        "structural integrity of the extracellular matrix'; no such "
        "contribution has been reported for adiponectin, and UniProt places "
        "the mature protein in 'Secreted' with no matrix role. (3) The likely "
        "trigger is the collagen-like domain (residues 42-107), but UniProt's "
        "SUBUNIT is explicit that those repeats build adiponectin's own "
        "homotrimer: the low-molecular-weight trimers are assembled via "
        "non-covalent interactions of the collagen-like domains in a triple "
        "helix. They do not crosslink a matrix. This is a fold-to-function error "
        "arriving through a bulk RCA import rather than through the retired "
        "Swiss-Prot-keyword route. Adiponectin does adsorb to matrix in "
        "injured tissue, but that is binding, not being a structural "
        "constituent, and no GO row currently makes the binding claim."),
    propagation_review={
        "root_cause": "PROPAGATION_BAD",
        "failure_modes": ["ROLE_CONFLATION", "GRANULARITY_MISMATCH"],
        "source_entities": [
            {"source_id": "PMID:28675934",
             "comment": "bulk RCA block: 41 entities receive GO:0005201 "
                            "from this one ECM-proteomics reference"}]},
    supported_by=[st(RESULTS_REF,
                     "`GO:0005201` from **PMID:28675934 is a bulk `RCA` block**")])

dec("GO:0033691", "IDA", "PMID:19855092", action="REMOVE",
    summary="The cited paper shows that adiponectin IS sialylated; it does not "
            "show that adiponectin binds sialic acid. The annotation inverts "
            "the direction of the relationship.",
    reason=(
        "GO:0033691 is defined as 'Binding to a sialic acid'. PMID:19855092 is "
        "a post-translational-modification study: it maps sialylated O-linked "
        "glycans onto Thr residues of adiponectin's own variable domain and "
        "shows that removing them accelerates plasma clearance. Adiponectin is "
        "the glycoprotein carrying the sialic acid, not a lectin recognising "
        "it - the only receptor discussed is the hepatic asialoglycoprotein "
        "receptor, which binds desialylated adiponectin, i.e. the traffic runs "
        "the other way. UniProt encodes the same facts as CARBOHYD features at "
        "Thr-21 and Thr-22 with this exact reference, and a PTM comment, not "
        "as a binding activity. Adiponectin has no lectin domain: its two "
        "modules are a collagen-like repeat (42-107) and a C1q jelly-roll "
        "(108-244). This is the sole annotation PMID:19855092 carries in all "
        "of GOA. Note the row has already propagated: mouse Adipoq (Q60994) "
        "holds GO:0033691 only by IEA GO_REF:0000107 and ISO GO_REF:0000119, "
        "both orthology transfers from this human row, so correcting it here "
        "retracts the error in both species."),
    supported_by=[
        st("PMID:19855092",
           "sialylation occurs on previously unidentified O-linked glycans on "
           "Thr residues of the variable domain in human adiponectin"),
        st("PMID:19855092",
           "plasma clearance of desialylated adiponectin was accelerated "
           "compared with that of control adiponectin")])

dec("GO:0042802", "IEA", "GO_REF:0000107", action="ACCEPT",
    summary="Adiponectin self-associates into trimers, hexamers and HMW "
            "multimers; identical protein binding is correct and is the right "
            "grain for a homomultimer of variable stoichiometry.",
    reason=(
        "UniProt SUBUNIT: 'Homomultimer. Forms trimers, hexamers and 12- to "
        "18-mers.' The fundamental unit is a trimer built from a triple helix "
        "of the collagen-like domains plus hydrophobic contacts in the "
        "globular C1q domain; hexamers and HMW species follow from "
        "interchain disulfides at Cys-36 (mature Cys-22 numbering in "
        "PMID:14522956). GO:0042802 'Binding to an identical protein or "
        "proteins' is stoichiometry-neutral and therefore correct for all "
        "three forms."))

dec("GO:0042803", "IPI", "PMID:12021245", action="MODIFY",
    summary="Adiponectin's fundamental self-associated unit is a TRIMER, not a "
            "dimer; the parent term states the fact without the wrong "
            "stoichiometry.",
    reason=(
        "GO:0042803 is defined as 'Binding to an identical protein to form a "
        "homodimer'. No homodimeric adiponectin species has been described. "
        "UniProt SUBUNIT records trimers, hexamers and 12- to 18-mers, and "
        "the original characterisation of the human protein describes a "
        "collagen-like domain 'through which they form homo-trimers, which "
        "further combine to make oligomeric complexes'. Generalising to "
        "GO:0042802 identical protein binding, the direct parent, keeps "
        "everything the evidence supports and drops the dimer claim. The "
        "trimer itself is proposed separately as GO:0070207 protein "
        "homotrimerization, which is the term that actually states the "
        "stoichiometry."),
    proposed_replacement_terms=[
        {"id": "GO:0042802", "label": "identical protein binding"}],
    supported_by=[st("PMID:8947845",
                     "possessing a collagen-like domain through which they "
                     "form homo-trimers, which further combine to make "
                     "oligomeric complexes")])

# ---- cellular component ---------------------------------------------------

_EXTRA_SUMMARY = ("Adiponectin is a secreted plasma protein; the extracellular "
                  "region is its core location.")
_EXTRA_REASON = (
    "UniProt SUBCELLULAR LOCATION is 'Secreted' with experimental evidence, "
    "and TISSUE SPECIFICITY records that it is 'Synthesized exclusively by "
    "adipocytes and secreted into plasma'. Circulating concentrations are "
    "5-30 ug/ml. Multiple independent experimental rows agree."
)
for ev, ref in [("EXP", "PMID:8947845"), ("HDA", "PMID:27068509"),
                ("IBA", "GO_REF:0000033"), ("IDA", "PMID:10403784"),
                ("IDA", "PMID:11222466"), ("IDA", "PMID:15585515"),
                ("IDA", "PMID:17327472"), ("IEA", "GO_REF:0000044"),
                ("TAS", "Reactome:R-HSA-1183058"),
                ("TAS", "Reactome:R-HSA-8848663")]:
    dec("GO:0005576", ev, ref, action="ACCEPT", summary=_EXTRA_SUMMARY,
        reason=_EXTRA_REASON)
D[("GO:0005576", "EXP", "PMID:8947845")]["supported_by"] = [
    st("PMID:8947845",
       "The clone encodes a polypeptide of 244 amino acids with a secretory "
       "signal sequence at the amino terminus")]
D[("GO:0005576", "IBA", "GO_REF:0000033")]["reason"] += (
    " The IBA sits on node PTN008355511, whose human reach is ADIPOQ, C1QA, "
    "C1QB, C1QC, C1QTNF2, C1QTNF5, C1QTNF7, C1QTNF9 and C1QTNF9B. For a clade "
    "mixing the complement C1q chains with the CTRP adipokines the generic "
    "extracellular term is the correct least common ancestor - refining it "
    "would mean picking one donor's compartment over another's. All 15 donor "
    "tokens resolve and all 15 carry their own experimental evidence for the "
    "term, and the WITH/FROM includes UniProtKB:Q15848 itself.")
D[("GO:0005576", "IBA", "GO_REF:0000033")]["propagation_review"] = {
    "root_cause": "NO_FAILURE_CORE",
    "source_entities": [
        {"source_id": "PANTHER:PTN008355511",
         "comment": "C1q/CTRP family node; 9 human genes reached"},
        {"source_id": "UniProtKB:Q15848",
         "comment": "self-reference - target is its own IBD seed"},
        {"source_id": "UniProtKB:P02745", "comment": "human C1QA, own IDA"},
        {"source_id": "UniProtKB:P02746", "comment": "human C1QB, own IDA"},
        {"source_id": "UniProtKB:P02747", "comment": "human C1QC, own IDA"},
        {"source_id": "UniProtKB:Q3Y5Z3",
         "comment": "bovine ADIPOQ, own IDA"},
        {"source_id": "UniProtKB:Q9BXJ0",
         "comment": "human C1QTNF5, own IDA"},
        {"source_id": "MGI:MGI:106675",
         "comment": "mouse Adipoq (Q60994), own EXP/IDA"},
        {"source_id": "MGI:MGI:1916433",
         "comment": "mouse C1qtnf2 (Q9D8U4), own IDA"},
        {"source_id": "MGI:MGI:1925911",
         "comment": "mouse C1qtnf7 (Q8BVD7), own IDA"},
        {"source_id": "MGI:MGI:2385958",
         "comment": "mouse C1qtnf5 (Q8K479), own IDA/HDA"},
        {"source_id": "MGI:MGI:3045252",
         "comment": "mouse C1qtnf9 (Q4ZJN1), own IDA"},
        {"source_id": "RGD:1306716", "comment": "rat C1qa (P31720), own EXP"},
        {"source_id": "RGD:1306828", "comment": "rat C1qc (P31722), own EXP"},
        {"source_id": "RGD:2229", "comment": "rat C1qb (P31721), own IDA"},
        {"source_id": "RGD:628748",
         "comment": "rat Adipoq (F7FPS2, TrEMBL), own IDA"},
    ]}

dec("GO:0005783", "ISS", "GO_REF:0000024", action="KEEP_AS_NON_CORE",
    summary="Adiponectin transits and is assembled in the ER, but the ER is a "
            "biosynthetic waypoint rather than the site of its function.",
    reason=(
        "Adiponectin's multimer assembly, disulfide bonding and lysine "
        "hydroxylation/glycosylation occur in the endoplasmic reticulum before "
        "secretion, so the localisation is real and mechanistically important "
        "- UniProt PTM notes that hydroxylation and glycosylation of the "
        "collagen-domain lysines are 'critically involved in regulating the "
        "formation and/or secretion of HMW complexes'. It is non-core because "
        "the protein acts after secretion, on other cells."))

dec("GO:0009986", "IDA", "PMID:10982546", action="KEEP_AS_NON_CORE",
    summary="Adiponectin docks saturably on the surface of endothelial cells, "
            "which is where its receptors are; a real but secondary location.",
    reason=(
        "PMID:10982546 measured biotinylated adiponectin binding to human "
        "aortic endothelial cells by cell ELISA and found specific, saturable "
        "binding. For a secreted ligand, 'cell surface' records where it "
        "accumulates on the responding cell, which is a consequence of the "
        "receptor-binding function rather than a separate one."),
    supported_by=[st("PMID:10982546",
                     "Adiponectin specifically bound to HAECs in a saturable "
                     "manner and inhibited TNF-alpha-induced mRNA expression "
                     "of monocyte adhesion molecules")])

dec("GO:0031012", "HDA", "PMID:28675934", action="KEEP_AS_NON_CORE",
    summary="Adiponectin is reproducibly detected in tissue ECM preparations, "
            "which reflects adsorption of a circulating protein rather than "
            "matrix residency as its site of action.",
    reason=(
        "This is a high-throughput proteomics detection: PMID:28675934 assigns "
        "GO:0031012 by HDA to 135 entities. Adiponectin genuinely accumulates "
        "in injured vessel wall and on hepatocyte matrix, so the localisation "
        "is not spurious. It is non-core because adiponectin's function is "
        "executed on receptors at the cell surface, and because being "
        "recovered in a matrisome fraction is a much weaker statement than "
        "the structural claim GO:0005201 makes from the same reference."))

dec("GO:0140149", "TAS", "PMID:36399478", action="MARK_AS_OVER_ANNOTATED",
    summary="A MatrisomeDB database import: one reference gives this term to "
            "272 entities. The term's definition is about structural matrix "
            "glycoproteins, which adiponectin is not.",
    reason=(
        "PMID:36399478 is the MatrisomeDB 2.0 database-update paper. The "
        "reference-projection test returns 285 annotations over 274 distinct "
        "entities, of which GO:0140149 alone reaches 272, all assigned by "
        "GO_Central - one reference giving 272 entities one identical "
        "cellular-component term is a bulk import, not 272 traceable author "
        "statements. GO:0140149 is defined as 'the non-collagenous component "
        "of interstitial extracellular matrices, including glycoprotein like "
        "fibronectin and elastin', i.e. the structural non-collagenous "
        "compartment. Adiponectin is a 30 kDa circulating hormone that appears "
        "in matrisome fractions because it adsorbs to tissue, not because it "
        "builds interstitial matrix. Marked over-annotated rather than removed "
        "because its presence in ECM preparations is a real, reproducible "
        "observation and is already recorded by the GO:0031012 HDA row at the "
        "grain the data supports."),
    propagation_review={
        "root_cause": "PROPAGATION_BAD",
        "failure_modes": ["ROLE_CONFLATION"],
        "source_entities": [
            {"source_id": "PMID:36399478",
             "comment": "MatrisomeDB 2.0; 272 entities receive GO:0140149 "
                            "from this single reference"}]},
    supported_by=[st(RESULTS_REF,
                     "`GO:0140149` from **PMID:36399478 is a database "
                     "import**")])

# ---- biological process ---------------------------------------------------

_ADIPO_PATHWAY = (
    "GO:0033211 is defined as 'the series of molecular signals initiated by "
    "adiponectin binding to its receptor on the surface of a cell, and ending "
    "with the regulation of a downstream cellular process'. This is the gene's "
    "own pathway and its core biological process."
)
for ev, ref in [("IDA", "PMID:18703020"), ("ISS", "GO_REF:0000024")]:
    dec("GO:0033211", ev, ref, action="ACCEPT",
        summary="The adiponectin-activated signalling pathway is, by "
                "definition, this gene's core process.",
        reason=_ADIPO_PATHWAY)

_PDGFR = (
    "This is one of the few adiponectin activities with a directly measured "
    "molecular mechanism in human cells. PMID:12070119 showed that human "
    "adiponectin binds PDGF-BB itself and thereby blocks the ligand from "
    "reaching its receptor on human aortic smooth muscle cells, suppressing "
    "PDGF beta-receptor autophosphorylation. Ligand sequestration is a direct "
    "participation in the negative regulation of that pathway, not a "
    "downstream physiological consequence."
)
for ev, ref in [("IBA", "GO_REF:0000033"), ("IDA", "PMID:12070119"),
                ("IEA", "GO_REF:0000107")]:
    dec("GO:0010642", ev, ref, action="ACCEPT",
        summary="Adiponectin binds PDGF-BB and blocks its access to the "
                "receptor; a directly demonstrated, mechanistically explicit "
                "process.",
        reason=_PDGFR)
D[("GO:0010642", "IDA", "PMID:12070119")]["supported_by"] = [
    st("PMID:12070119",
       "Adiponectin specifically bound to (125)I-PDGF-BB and significantly "
       "inhibited the association of (125)I-PDGF-BB with HASMCs")]
D[("GO:0010642", "IBA", "GO_REF:0000033")]["propagation_review"] = {
    "root_cause": "NO_FAILURE_CORE",
    "source_entities": [
        {"source_id": "MGI:MGI:106675",
         "comment": "mouse Adipoq (Q60994); carries its own IDA for this term"},
        {"source_id": "PANTHER:PTN008559544",
         "comment": "human reach is exactly ADIPOQ; this is the only human "
                        "GO:0010642 IBA row in GOA"},
        {"source_id": "UniProtKB:Q15848", "comment": "self-reference"}]}

_FATCELL = (
    "Recombinant adiponectin blocks adipogenesis in bone-marrow stromal "
    "cultures through a COX-2/prostaglandin-dependent paracrine loop, "
    "establishing preadipocytes as direct adiponectin targets. Combined with "
    "the gene's identity as the adipocyte's own secreted product, this is a "
    "well-founded feedback function rather than an incidental phenotype."
)
for ev, ref in [("IBA", "GO_REF:0000033"), ("IDA", "PMID:12021245"),
                ("IEA", "GO_REF:0000107")]:
    dec("GO:0045599", ev, ref, action="ACCEPT",
        summary="Adiponectin restrains adipocyte differentiation in a "
                "paracrine negative-feedback loop.",
        reason=_FATCELL)
D[("GO:0045599", "IDA", "PMID:12021245")]["supported_by"] = [
    st("PMID:12021245",
       "Recombinant adiponectin blocked fat cell formation in long-term bone "
       "marrow cultures and inhibited the differentiation of cloned stromal "
       "preadipocytes")]
D[("GO:0045599", "IBA", "GO_REF:0000033")]["propagation_review"] = {
    "root_cause": "NO_FAILURE_CORE",
    "source_entities": [
        {"source_id": "MGI:MGI:106675", "comment": "mouse Adipoq (Q60994)"},
        {"source_id": "PANTHER:PTN008559544",
         "comment": "human reach is exactly ADIPOQ"},
        {"source_id": "UniProtKB:Q15848", "comment": "self-reference"}]}

# role-conflation MODIFYs: the hormone annotated to the process it regulates
_RC_SUM = ("Adiponectin regulates this process in responding cells; it does "
           "not carry it out.")
for ref in ["GO_REF:0000024", "PMID:12368907"]:
    dec("GO:0006006", "ISS", ref, action="MODIFY",
        summary=_RC_SUM,
        reason=(
            "GO:0006006 glucose metabolic process is a direct-participation "
            "term - 'the chemical reactions and pathways involving glucose'. "
            + ROLE_CONFLATION_NOTE +
            " PMID:12368907 is explicit that the effect is mediated by AMPK "
            "in the responding myocyte or hepatocyte, and that blocking AMPK "
            "abolishes it. GO:0010906 regulation of glucose metabolic process "
            "states what adiponectin does, and ADIPOQ already carries it, so "
            "this is a correction of grain rather than a loss of content."),
        proposed_replacement_terms=[
            {"id": "GO:0010906",
             "label": "regulation of glucose metabolic process"}],
        propagation_review={
            "root_cause": "TERM_SCOPING_PROBLEM",
            "failure_modes": ["ROLE_CONFLATION"],
            "source_entities": [
                {"source_id": "UniProtKB:Q60994",
                 "comment": "mouse Adipoq; holds GO:0006006 itself by "
                                "IDA/IMP, so the same conflation exists "
                                "upstream at MGI"}]})

for term, ev, ref in [("GO:0006635", "ISS", "GO_REF:0000024"),
                      ("GO:0006635", "ISS", "PMID:12368907"),
                      ("GO:0019395", "ISS", "GO_REF:0000024")]:
    dec(term, ev, ref, action="MODIFY",
        summary=_RC_SUM,
        reason=(
            "Adiponectin is not an enzyme of beta-oxidation and has no "
            "catalytic activity of any kind; it raises the rate of fatty-acid "
            "oxidation in muscle and liver by activating AMPK downstream of "
            "AdipoR1/AdipoR2. " + ROLE_CONFLATION_NOTE + " GO:0046321 "
            "positive regulation of fatty acid oxidation states the "
            "measured effect at the correct grain and preserves the direction, "
            "which the bare metabolic term does not."),
        proposed_replacement_terms=[
            {"id": "GO:0046321",
             "label": "positive regulation of fatty acid oxidation"}],
        propagation_review={
            "root_cause": "TERM_SCOPING_PROBLEM",
            "failure_modes": ["ROLE_CONFLATION"],
            "source_entities": [
                {"source_id": "UniProtKB:Q60994",
                 "comment": "mouse Adipoq; holds GO:0006635 (IMP) and "
                                "GO:0019395 (IDA) itself"}]})
D[("GO:0006635", "ISS", "PMID:12368907")]["supported_by"] = [
    st("PMID:12368907",
       "stimulation of glucose utilization and fatty-acid oxidation by Ad "
       "occurs through activation of AMPK")]

dec("GO:0050873", "ISS", "GO_REF:0000024", action="MODIFY",
    summary="Adiponectin promotes browning of adipose tissue; it does not "
            "itself undergo brown fat cell differentiation.",
    reason=(
        "GO:0050873 is the differentiation process itself - 'the process in "
        "which a relatively unspecialized cell acquires specialized features "
        "of a brown adipocyte'. Adiponectin is a secreted product of white "
        "adipocytes that acts on other cells; the reported effect is that "
        "cold-induced adiponectin recruits M2 macrophages via T-cadherin and "
        "thereby activates beige cells (PMID:26166748). GO:0090336 positive "
        "regulation of brown fat cell differentiation states that correctly "
        "and adds the direction. Note this is the same claim whose citation "
        "is disputed by PMID:24531262; the regulation term is used here "
        "because the ISS transfer is anchored on the browning result."),
    proposed_replacement_terms=[
        {"id": "GO:0090336",
         "label": "positive regulation of brown fat cell differentiation"}],
    propagation_review={
        "root_cause": "TERM_SCOPING_PROBLEM",
        "failure_modes": ["ROLE_CONFLATION"],
        "source_entities": [
            {"source_id": "UniProtKB:Q60994",
             "comment": "mouse Adipoq; GO:0050873 IDA from PMID:18492766, "
                            "a paper about a different adipokine in which "
                            "adiponectin serves as a differentiation marker"}]})

dec("GO:0038002", "IEA", "GO_REF:0000107", action="ACCEPT",
    summary="Adiponectin is carried in the bloodstream from adipocytes to "
            "distant target organs; this is the process form of its core "
            "hormone function.",
    reason=(
        "GO:0038002 is defined as signalling 'where an endocrine hormone is "
        "transported from the signal-producing cell to the receiving cell via "
        "the circulatory system (via blood, lymph or cerebrospinal fluid). The "
        "signaling cell and the receiving cell are often distant to each "
        "other.' Adiponectin is made only by adipocytes, circulates at 5-30 "
        "ug/ml and acts on liver, muscle, endothelium, macrophages and kidney. "
        "The definition is met exactly. Although the row is an Ensembl Compara "
        "projection, the conclusion is established by the human literature "
        "independently of the projection, so it is accepted as core rather "
        "than downgraded on evidence code alone."))

dec("GO:0009967", "ISS", "PMID:12368907", action="MODIFY",
    summary="Too general to be informative for a gene whose own signalling "
            "pathway has a dedicated GO term.",
    reason=(
        "GO:0009967 positive regulation of signal transduction says only that "
        "adiponectin turns some pathway up. The pathway in question has its "
        "own term, GO:0033211 adiponectin-activated signaling pathway, which "
        "ADIPOQ already carries by IDA and ISS. The generic term is not the "
        "least common ancestor of a heterogeneous donor set here - there is a "
        "single, named pathway - so replacing it loses nothing and gains "
        "specificity."),
    proposed_replacement_terms=[
        {"id": "GO:0033211", "label": "adiponectin-activated signaling pathway"}])

dec("GO:0006091", "TAS", "PMID:10095105", action="REMOVE",
    summary="The cited paper is a gene-structure report that performs no "
            "metabolic experiment, and the term is a direct-participation term "
            "for a protein with no catalytic activity.",
    reason=(
        "PMID:10095105 is 'Organization of the gene for gelatin-binding "
        "protein (GBP28)': it maps ADIPOQ to 3q27 by FISH and describes a "
        "16 kb, three-exon gene lacking a TATA box. It contains no assay of "
        "energy metabolism. The projection test shows this reference carries "
        "exactly one annotation in all of GOA - this one - so it is not a "
        "bulk import that swept ADIPOQ up; it is a single unsupported TAS, "
        "assigned by PINC. Separately, GO:0006091 'generation of precursor "
        "metabolites and energy' describes the reactions themselves, and "
        "adiponectin is a hormone that modulates them in other cells rather "
        "than performing them. Mouse Adipoq carries no counterpart row, so "
        "nothing depends on this one."),
    propagation_review={
        "root_cause": "SOURCE_BAD",
        "failure_modes": ["SOURCE_MISCITATION", "ROLE_CONFLATION"],
        "source_entities": [
            {"source_id": "PMID:10095105",
             "comment": "gene-structure paper; its only GOA annotation is "
                            "this row"}]})

# thermogenesis: the 2x2 cross-product
_THERMO_SHARED = (
    "GOA cites GO:0120162 (positive) and GO:0120163 (negative) regulation of "
    "cold-induced thermogenesis to the SAME two references, PMID:24531262 and "
    "PMID:26166748 - a full 2x2 cross-product. The same evidence cannot "
    "support a proposition and its negation. Reading the two papers assigns "
    "each to exactly one direction: PMID:24531262 (Diabetologia 2014) reports "
    "that Adipoq-knockout mice run HOTTER and express MORE UCP1, i.e. "
    "adiponectin SUPPRESSES thermogenesis; PMID:26166748 (Cell Metab 2015) "
    "reports that the cold-induced thermogenic program is IMPAIRED in "
    "adiponectin-knockout mice, i.e. adiponectin PROMOTES it. The same "
    "cross-product is present on mouse Adipoq (Q60994) as four IMP rows from "
    "the same two references, so the defect originates upstream at MGI and "
    "reaches human through these ISS transfers."
)
dec("GO:0120162", "ISS", "PMID:26166748", action="KEEP_AS_NON_CORE",
    summary="Correctly paired half of the cross-product: this reference does "
            "show adiponectin promoting cold-induced thermogenesis.",
    reason=(_THERMO_SHARED + " This row is the correctly paired one for the "
            "positive term and is retained. It is non-core because it is a "
            "whole-animal knockout phenotype several steps downstream of "
            "receptor engagement, and because the field has not reconciled it "
            "with the opposite result."),
    supported_by=[st("PMID:26166748",
                     "Chronic cold exposure-induced accumulation of M2 "
                     "macrophages, activation of beige cells, and thermogenic "
                     "program were markedly impaired in scWAT of adiponectin "
                     "knockout (ADN KO) mice")])
dec("GO:0120162", "ISS", "PMID:24531262", action="REMOVE",
    summary="Sign inversion: this reference reports that adiponectin SUPPRESSES "
            "thermogenesis, so it cannot support the positive-regulation term.",
    reason=(_THERMO_SHARED + " This particular row pairs the POSITIVE term "
            "with the paper that demonstrates suppression, and is therefore "
            "removable on the reference's own conclusion without adjudicating "
            "the underlying biological disagreement. The same paper correctly "
            "supports the GO:0120163 row, which is kept."),
    propagation_review={
        "root_cause": "SOURCE_BAD",
        "failure_modes": ["REGULATORY_SIGN_INVERSION", "SOURCE_MISCITATION"],
        "source_entities": [
            {"source_id": "UniProtKB:Q60994",
             "comment": "mouse Adipoq carries the identical cross-product: "
                            "GO:0120162 and GO:0120163 each by IMP from BOTH "
                            "PMID:24531262 and PMID:26166748"}]},
    supported_by=[st("PMID:24531262",
                     "This study demonstrates that adiponectin suppresses "
                     "thermogenesis")])
dec("GO:0120163", "ISS", "PMID:24531262", action="KEEP_AS_NON_CORE",
    summary="Correctly paired half of the cross-product: this reference does "
            "show adiponectin suppressing cold-induced thermogenesis.",
    reason=(_THERMO_SHARED + " This row is the correctly paired one for the "
            "negative term and is retained, non-core for the same reasons as "
            "its positive counterpart."),
    supported_by=[st("PMID:24531262",
                     "The CBTs of adiponectin knockout mice (Adipoq(-/-)) were "
                     "significantly higher than those of wild type (WT) mice")])
dec("GO:0120163", "ISS", "PMID:26166748", action="REMOVE",
    summary="Sign inversion: this reference reports that adiponectin PROMOTES "
            "cold-induced browning, so it cannot support the "
            "negative-regulation term.",
    reason=(_THERMO_SHARED + " This particular row pairs the NEGATIVE term "
            "with the paper that demonstrates enhancement, and is removable on "
            "the reference's own conclusion. The same paper correctly supports "
            "the GO:0120162 row, which is kept."),
    propagation_review={
        "root_cause": "SOURCE_BAD",
        "failure_modes": ["REGULATORY_SIGN_INVERSION", "SOURCE_MISCITATION"],
        "source_entities": [
            {"source_id": "UniProtKB:Q60994",
             "comment": "mouse Adipoq carries the identical cross-product: "
                            "GO:0120162 and GO:0120163 each by IMP from BOTH "
                            "PMID:24531262 and PMID:26166748"}]},
    supported_by=[st("PMID:26166748",
                     "Chronic cold exposure-induced accumulation of M2 "
                     "macrophages, activation of beige cells, and thermogenic "
                     "program were markedly impaired in scWAT of adiponectin "
                     "knockout (ADN KO) mice")])
for term in ("GO:0120162", "GO:0120163"):
    dec(term, "IEA", "GO_REF:0000107", action="KEEP_AS_NON_CORE",
        summary="Ensembl Compara projection of the mouse thermogenesis rows; "
                "retained at the same non-core grade as the ISS rows it "
                "mirrors.",
        reason=(_THERMO_SHARED + " The IEA rows are Compara projections from "
                "mouse Adipoq and inherit the same evidence. They are kept "
                "because each direction does have one correctly-cited paper "
                "behind it; the fix belongs upstream, where the four mouse IMP "
                "rows should become two."))

dec("GO:0071466", "ISS", "GO_REF:0000024", action="MARK_AS_OVER_ANNOTATED",
    summary="The underlying observation is that a drug INDUCES adiponectin, "
            "which makes adiponectin the output of the response rather than a "
            "participant in it.",
    reason=(
        "The mouse annotation this ISS transfers from is GO:0071466 IDA on "
        "Q60994 from PMID:19109165, 'The peroxisome proliferator-activated "
        "receptor gamma agonist rosiglitazone ameliorates murine lupus by "
        "induction of adiponectin'. The datum is that rosiglitazone raises "
        "adiponectin expression. Annotating ADIPOQ to 'cellular response to "
        "xenobiotic stimulus' therefore inverts the roles: adiponectin is what "
        "the responding adipocyte produces, not the machinery by which it "
        "detects or handles the xenobiotic. Marked over-annotated rather than "
        "removed because the transcriptional response is real and a curator "
        "reading only the expression change would reasonably reach for this "
        "term."),
    propagation_review={
        "root_cause": "SOURCE_BAD",
        "failure_modes": ["ROLE_CONFLATION"],
        "source_entities": [
            {"source_id": "UniProtKB:Q60994",
             "comment": "mouse Adipoq GO:0071466 IDA from PMID:19109165, a "
                            "rosiglitazone-induction study"}]})
dec("GO:0071466", "IEA", "GO_REF:0000107", action="MARK_AS_OVER_ANNOTATED",
    summary="Compara projection of the same rosiglitazone-induction datum; "
            "same role inversion as the ISS row.",
    reason=(
        "Ensembl Compara projection from mouse Adipoq, whose GO:0071466 IDA "
        "rests on PMID:19109165 showing that rosiglitazone induces adiponectin "
        "expression. The gene product is the output of the response, not a "
        "component of it."),
    propagation_review={
        "root_cause": "SOURCE_BAD",
        "failure_modes": ["ROLE_CONFLATION"],
        "source_entities": [
            {"source_id": "UniProtKB:Q60994",
             "comment": "mouse Adipoq GO:0071466 IDA from PMID:19109165"},
            {"source_id": "ensembl:ENSMUSP00000023593",
             "comment": "Compara protein id for mouse Adipoq, as emitted in "
                        "the GOA WITH/FROM"}]})

_ALBUMIN_REASON = (
    "GO:2000534 sits under GO:0097017 renal protein absorption, defined as "
    "proteins 'taken up from the collecting ducts, glomerulus and proximal and "
    "distal loops of the nephron'. PMID:18431508 measures something else "
    "entirely: it shows that adiponectin-knockout mice have podocyte foot-"
    "process effacement and increased albuminuria, and that adiponectin acting "
    "through AMPK reduces podocyte PERMEABILITY to albumin. The full text "
    "contains no measurement of tubular reabsorption; the words absorption, "
    "reabsorption and tubular do not appear in the extracted text at all. So "
    "adiponectin restores the glomerular filtration barrier - less albumin "
    "crosses it - rather than increasing uptake downstream. GO has no term for "
    "regulation of glomerular permeability to albumin, which is very likely "
    "why this one was chosen; that gap is filed under proposed_new_terms. "
    "Marked over-annotated rather than removed because the phenotype (less "
    "urinary albumin) is real and the term is the closest existing fit."
)
dec("GO:2000534", "IDA", "PMID:18431508", action="MARK_AS_OVER_ANNOTATED",
    summary="The paper measures podocyte permeability to albumin, not renal "
            "albumin absorption; the term names the wrong process.",
    reason=_ALBUMIN_REASON + (
        " Note also that the evidence code is IDA on the human gene while the "
        "experiments are an adiponectin-knockout mouse plus cultured "
        "podocytes; MGI records the same finding as IMP on mouse Adipoq, which "
        "is the more accurate code."),
    supported_by=[st("PMID:18431508",
                     "both adiponectin and AMPK activation reduced podocyte "
                     "permeability to albumin and podocyte dysfunction")])
dec("GO:2000534", "IEA", "GO_REF:0000107", action="MARK_AS_OVER_ANNOTATED",
    summary="Compara projection of the same mouse podocyte result; inherits "
            "the same process mismatch.",
    reason=_ALBUMIN_REASON,
    propagation_review={
        "root_cause": "TERM_SCOPING_PROBLEM",
        "failure_modes": ["ROLE_CONFLATION"],
        "source_entities": [
            {"source_id": "UniProtKB:Q60994",
             "comment": "mouse Adipoq GO:2000534 IMP from PMID:18431508"},
            {"source_id": "ensembl:ENSMUSP00000023593",
             "comment": "Compara protein id for mouse Adipoq, as emitted in "
                        "the GOA WITH/FROM"}]})

dec("GO:0050805", "IDA", "PMID:17327472", action="MARK_AS_OVER_ANNOTATED",
    summary="The cited experiment records renal sympathetic nerve firing and "
            "blood pressure, not transmission across a synapse.",
    reason=(
        "GO:0050805 is defined as reducing 'synaptic transmission, the process "
        "of communication from a neuron to a target (neuron, muscle, or "
        "secretory cell) across a synapse'. PMID:17327472 injected adiponectin "
        "intravenously and intracerebroventricularly into anaesthetised rats "
        "and measured renal sympathetic nerve activity and blood pressure, "
        "with the effect abolished by suprachiasmatic-nucleus lesions. That is "
        "efferent autonomic outflow, one level of organisation above synaptic "
        "transmission, and no synaptic measurement was made. GO has no term "
        "for regulation of sympathetic nervous system activity - a search of "
        "the ontology returns only developmental terms (GO:0048485, "
        "GO:0061549, GO:0097490-2, GO:1903045) - so there is nothing to MODIFY "
        "to; the gap is filed under proposed_new_terms. The blood-pressure "
        "half of the same experiment is already captured by the GO:0045776 "
        "row."),
    supported_by=[st("PMID:17327472",
                     "Both iv and LCV injections of adiponectin induced "
                     "dose-dependent suppressions of RSNA and b/p")])

dec("GO:0010906", "IDA", "PMID:17327472", action="ACCEPT",
    summary="Regulation of glucose metabolism is a genuine core action of "
            "adiponectin, though this particular reference is a poor citation "
            "for it.",
    reason=(
        "The term is right: suppression of hepatic glucose output is "
        "adiponectin's best-characterised metabolic effect (PMID:11748271, "
        "PMID:12368907), and this is the term the role-conflated GO:0006006 "
        "rows should be modified to. The citation is the weak part - "
        "PMID:17327472 measured renal sympathetic nerve activity and blood "
        "pressure in rats, and mentions glucose metabolism only as background "
        "in its first sentence. The full text is not available here, so per "
        "GO curation practice the curator's reading is not overruled; the "
        "concern is recorded in this reference's reference_review instead. "
        "Accepted on the strength of the term, with the citation flagged."))

# straightforward non-core downstream physiology
NONCORE = {
    "GO:0009749": ("Adipocyte adiponectin expression and secretion track "
                   "glucose availability.",
                   "A response-to-stimulus term transferred by ISS from mouse. "
                   "It describes the regulation of adiponectin rather than an "
                   "action of adiponectin, so it is retained only as "
                   "peripheral context."),
    "GO:0010745": ("Adiponectin suppresses the conversion of macrophages into "
                   "lipid-laden foam cells.",
                   "PMID:11222466 showed that adiponectin lowers class A "
                   "scavenger receptor expression and lipid uptake in human "
                   "monocyte-derived macrophages. Real and human, but this is "
                   "a downstream cellular consequence of receptor signalling, "
                   "not a molecular action of the protein."),
    "GO:0010804": ("Adiponectin blunts TNF signalling in endothelium.",
                   "Downstream physiology: adiponectin pretreatment suppresses "
                   "TNF-induced IkB-alpha phosphorylation and adhesion "
                   "molecule expression. Anti-TNF action is a well-established "
                   "adiponectin effect but is mediated through its own "
                   "receptor pathway."),
    "GO:0010875": ("Adiponectin raises ABCA1-dependent cholesterol efflux from "
                   "macrophages.",
                   "PMID:18703020 showed APN upregulates ABCA1, LXRalpha and "
                   "PPARgamma and increases apoA-I-mediated efflux in human "
                   "macrophages. A downstream transcriptional consequence of "
                   "adiponectin signalling."),
    "GO:0030336": ("Adiponectin restrains migration of vascular smooth muscle "
                   "and mesangial cells.",
                   "Transferred by ISS from mouse Adipoq, whose GO:0030336 IDA "
                   "comes from PMID:19460854 on PDGF-induced mesangial cell "
                   "migration. Mechanistically this is the same PDGF-BB "
                   "sequestration captured more precisely by GO:0010642 and "
                   "GO:1904753; kept as the general vascular-remodelling "
                   "statement."),
    "GO:0030853": ("Adiponectin inhibits granulocyte differentiation from "
                   "myelomonocytic progenitors.",
                   "PMID:10961870 showed adiponectin suppresses growth of "
                   "myelomonocytic progenitors and mature macrophage "
                   "functions. A haematopoietic effect well outside the gene's "
                   "metabolic core."),
    "GO:0032720": ("Adiponectin lowers macrophage TNF production.",
                   "PMID:10961870 found adiponectin inhibits "
                   "lipopolysaccharide-induced TNF production by cultured "
                   "macrophages. UniProt's FUNCTION records the same: "
                   "'Antagonizes TNF by negatively regulating its expression "
                   "in various tissues such as liver and macrophages'. "
                   "Downstream of receptor signalling."),
    "GO:0032757": ("HMW adiponectin induces IL-8 in PBMCs and microvascular "
                   "endothelial cells.",
                   "PMID:19524870 is a careful isoform-resolved study: HMW but "
                   "not LMW adiponectin induces chemokines. It is retained "
                   "because it is one of the clearest demonstrations that "
                   "adiponectin's inflammatory sign is multimer-dependent, and "
                   "it sits alongside the anti-inflammatory rows without "
                   "contradicting them."),
    "GO:0032869": ("Adipocytes and adiponectin-responsive tissues respond to "
                   "insulin.",
                   "ISS transfer from mouse. Adiponectin sensitises tissues to "
                   "insulin and its own expression is insulin-responsive; the "
                   "term is broad and peripheral to the gene's own activity."),
    "GO:0033034": ("Adiponectin promotes apoptosis of myelomonocytic cells.",
                   "PMID:10961870 observed subdiploid peaks and "
                   "oligonucleosomal DNA fragmentation in acute myelomonocytic "
                   "leukaemia lines treated with adiponectin. A cell-type-"
                   "restricted downstream effect."),
    "GO:0034115": ("Adiponectin reduces monocyte adhesion to endothelium.",
                   "PMID:10604883 showed adiponectin dose-dependently inhibits "
                   "TNF-induced THP-1 adhesion to human aortic endothelial "
                   "cells. Downstream of the NF-kB suppression captured by "
                   "GO:0043124."),
    "GO:0034383": ("Adiponectin influences clearance of LDL particles by "
                   "macrophages.",
                   "Derived from the same scavenger-receptor experiments in "
                   "PMID:11222466. A downstream lipid-handling consequence."),
    "GO:0034612": ("Adiponectin-treated endothelial cells respond differently "
                   "to TNF.",
                   "A response-to-stimulus term from PMID:10604883. It "
                   "describes the experimental setting - TNF challenge - "
                   "rather than an adiponectin activity, so it is kept only as "
                   "context."),
    "GO:0038002": ("Adiponectin is transported in the bloodstream from "
                   "adipocytes to distant target organs.",
                   "GO:0038002 is defined as signalling 'where an endocrine "
                   "hormone is transported from the signal-producing cell to "
                   "the receiving cell via the circulatory system'. That is "
                   "precisely adiponectin's mode of action and the definition "
                   "is met exactly. Recorded as non-core only because it "
                   "restates, as a process, the same fact that GO:0005179 "
                   "hormone activity states as the molecular function."),
    "GO:0043123": ("Hexameric and HMW adiponectin activate NF-kB, in contrast "
                   "to the trimer.",
                   "This is NOT a contradiction of the GO:0043124 negative row. "
                   "PMID:12087086 and PMID:14522956 show that hexamer and HMW "
                   "Acrp30 activate NF-kB in C2C12 myocytes while trimers and "
                   "the globular fragment do not, whereas PMID:10982546 shows "
                   "adiponectin suppressing TNF-INDUCED NF-kB in endothelium. "
                   "The sign depends on multimer state and cell type, and both "
                   "rows are correct."),
    "GO:0043124": ("Adiponectin suppresses TNF-induced NF-kB activation in "
                   "endothelial cells through cAMP/PKA.",
                   "PMID:10982546 showed adiponectin blocks TNF-induced "
                   "IkB-alpha phosphorylation without affecting JNK, p38 or "
                   "Akt, and that the effect is cAMP-dependent. UniProt "
                   "FUNCTION records it as 'Inhibits endothelial NF-kappa-B "
                   "signaling through a cAMP-dependent pathway'. Well founded "
                   "but downstream of receptor engagement."),
    "GO:0043407": ("Adiponectin dampens MAP kinase activation by growth "
                   "factors.",
                   "ISS transfer from mouse; mechanistically the same result "
                   "as the human GO:0070373 IDA row, where adiponectin "
                   "suppresses PDGF-BB-induced ERK phosphorylation. Kept at "
                   "the general grain."),
    "GO:0045650": ("Adiponectin inhibits macrophage differentiation.",
                   "From PMID:10961870's myelomonocytic experiments. A "
                   "haematopoietic effect, downstream and outside the core."),
    "GO:0045776": ("Adiponectin lowers blood pressure, at least partly via "
                   "reduced sympathetic outflow.",
                   "PMID:17327472 showed dose-dependent suppression of blood "
                   "pressure by both intravenous and intracerebroventricular "
                   "adiponectin in rats, abolished by suprachiasmatic-nucleus "
                   "lesions. A whole-organism physiological outcome, several "
                   "steps from the molecular function."),
    "GO:0048261": ("Adiponectin reduces scavenger-receptor-mediated uptake in "
                   "macrophages.",
                   "The same class A scavenger receptor result from "
                   "PMID:11222466, expressed as an endocytosis term. "
                   "Downstream."),
    "GO:0050765": ("Adiponectin suppresses macrophage phagocytosis via the C1q "
                   "receptor C1qRp.",
                   "PMID:10961870 showed adiponectin inhibits phagocytic "
                   "activity and that this was abrogated by anti-C1qRp "
                   "antibody, implicating CD93 as a receptor. Notable as one "
                   "of the few receptor-resolved adiponectin effects, but a "
                   "downstream immune process."),
    "GO:0050996": ("Adiponectin increases lipid catabolism in muscle and "
                   "liver.",
                   "The organism-level expression of the AMPK-driven "
                   "fatty-acid oxidation effect. Retained as the general "
                   "statement; the specific, direction-bearing term proposed "
                   "for the GO:0006635/GO:0019395 rows is GO:0046321."),
    "GO:0060621": ("Adiponectin reduces cholesterol uptake by macrophages.",
                   "The uptake half of the PMID:11222466 foam-cell result, "
                   "complementary to the GO:0010875 efflux row. Downstream."),
    "GO:0070373": ("Adiponectin suppresses growth-factor-induced ERK1/2 "
                   "signalling in vascular smooth muscle.",
                   "PMID:12070119 showed adiponectin 'strongly and "
                   "dose-dependently suppressed PDGF-BB-induced p42/44 "
                   "extracellular signal-related kinase (ERK) "
                   "phosphorylation'. Mechanistically downstream of the "
                   "PDGF-BB sequestration recorded by GO:0010642."),
    "GO:0071639": ("HMW adiponectin induces MCP-1 in PBMCs and microvascular "
                   "endothelial cells.",
                   "The MCP-1 half of PMID:19524870's isoform-dependent "
                   "chemokine result, alongside the IL-8 row. Kept for the "
                   "same reason: it documents the multimer dependence of "
                   "adiponectin's inflammatory sign."),
    "GO:0141163": ("Adiponectin raises cAMP and activates PKA in endothelial "
                   "cells.",
                   "PMID:10982546 attributed adiponectin's NF-kB suppression "
                   "to a cAMP-PKA-dependent pathway. This is the proximal "
                   "second-messenger step of one branch of adiponectin "
                   "signalling; it is kept non-core because the receptor-"
                   "proximal event is already covered by GO:0033211."),
    "GO:1904706": ("Adiponectin inhibits proliferation of vascular smooth "
                   "muscle cells.",
                   "PMID:12070119 showed physiological concentrations of "
                   "adiponectin suppress PDGF-BB-stimulated proliferation of "
                   "human aortic smooth muscle cells. A direct consequence of "
                   "PDGF-BB sequestration, and one of the better-supported "
                   "vascular effects."),
    "GO:1904753": ("Adiponectin inhibits migration of vascular smooth muscle "
                   "cells.",
                   "The migration half of the same PMID:12070119 experiment, "
                   "measured in a Boyden chamber. Downstream of PDGF-BB "
                   "binding."),
    "GO:2000590": ("Adiponectin inhibits PDGF-driven migration of mesangial "
                   "cells.",
                   "Transferred from mouse Adipoq, whose annotation rests on "
                   "PMID:19460854, 'Inhibitory effects of adiponectin on "
                   "platelet-derived growth factor-induced mesangial cell "
                   "migration'. The term names metanephric MESENCHYMAL cells, "
                   "the embryonic progenitors, whereas the assay used cultured "
                   "mesangial cells; GO has no mesangial cell migration term, "
                   "so this is the closest available fit rather than an error. "
                   "Mechanistically it is again PDGF antagonism."),
    "GO:2000584": ("Adiponectin dampens PDGF-alpha-receptor signalling "
                   "downstream of the receptor.",
                   "Worth stating precisely, because PMID:12070119 reports "
                   "that adiponectin reduced PDGF-AA-stimulated ERK "
                   "phosphorylation 'without affecting autophosphorylation of "
                   "PDGF alpha-receptor', and that adiponectin does not bind "
                   "PDGF-AA. So the alpha-receptor pathway is inhibited at a "
                   "post-receptor step, unlike the beta-receptor pathway where "
                   "ligand sequestration acts upstream. The term is about the "
                   "pathway, which includes downstream steps, so it stands - "
                   "but it should not be read as ligand sequestration."),
    "GO:2000467": ("Adiponectin increases glycogen synthase activity in "
                   "responding tissue.",
                   "ISS transferred from UniProtKB:Q8K3R4, which resolves to "
                   "rat Adipoq but is an UNREVIEWED TrEMBL entry rather than a "
                   "Swiss-Prot ortholog record - weaker support than the "
                   "mouse-derived rows, and worth noting. The effect itself is "
                   "consistent with adiponectin's insulin-sensitising action."),
    "GO:0050728": ("Adiponectin is broadly anti-inflammatory.",
                   "A general statement supported by the endothelial adhesion "
                   "molecule, TNF and macrophage results. Kept as the umbrella "
                   "term for a set of downstream immune effects, none of which "
                   "is the gene's molecular function."),
}
for term, (summ, rsn) in NONCORE.items():
    pass  # filled in below per (evidence, reference)

NONCORE_ROWS = [
    ("GO:0009749", "ISS", "PMID:12368907"),
    ("GO:0010745", "IDA", "PMID:11222466"),
    ("GO:0010804", "IDA", "PMID:10604883"),
    ("GO:0010875", "IDA", "PMID:18703020"),
    ("GO:0030336", "IEA", "GO_REF:0000107"),
    ("GO:0030336", "ISS", "GO_REF:0000024"),
    ("GO:0030853", "IDA", "PMID:10961870"),
    ("GO:0032720", "IDA", "PMID:10961870"),
    ("GO:0032757", "IDA", "PMID:19524870"),
    ("GO:0032869", "ISS", "GO_REF:0000024"),
    ("GO:0033034", "IDA", "PMID:10961870"),
    ("GO:0034115", "IDA", "PMID:10604883"),
    ("GO:0034383", "IDA", "PMID:11222466"),
    ("GO:0034612", "IDA", "PMID:10604883"),
    ("GO:0043123", "ISS", "GO_REF:0000024"),
    ("GO:0043124", "IDA", "PMID:10982546"),
    ("GO:0043407", "ISS", "GO_REF:0000024"),
    ("GO:0045650", "IDA", "PMID:10961870"),
    ("GO:0045776", "IDA", "PMID:17327472"),
    ("GO:0048261", "IDA", "PMID:11222466"),
    ("GO:0050728", "IEA", "GO_REF:0000107"),
    ("GO:0050728", "ISS", "GO_REF:0000024"),
    ("GO:0050728", "NAS", "PMID:12611609"),
    ("GO:0050765", "IDA", "PMID:10961870"),
    ("GO:0050996", "IEA", "GO_REF:0000107"),
    ("GO:0050996", "ISS", "GO_REF:0000024"),
    ("GO:0060621", "IDA", "PMID:11222466"),
    ("GO:0070373", "IDA", "PMID:12070119"),
    ("GO:0071639", "IDA", "PMID:19524870"),
    ("GO:0141163", "IDA", "PMID:10982546"),
    ("GO:1904706", "IDA", "PMID:12070119"),
    ("GO:1904753", "IDA", "PMID:12070119"),
    ("GO:2000467", "ISS", "GO_REF:0000024"),
    ("GO:2000584", "IEA", "GO_REF:0000107"),
    ("GO:2000584", "ISS", "GO_REF:0000024"),
    ("GO:2000590", "IEA", "GO_REF:0000107"),
    ("GO:2000590", "ISS", "GO_REF:0000024"),
]
for term, ev, ref in NONCORE_ROWS:
    summ, rsn = NONCORE[term]
    dec(term, ev, ref, action="KEEP_AS_NON_CORE", summary=summ, reason=rsn)

D[("GO:0070373", "IDA", "PMID:12070119")]["supported_by"] = [
    st("PMID:12070119",
       "Adiponectin strongly and dose-dependently suppressed PDGF-BB-induced "
       "p42/44 extracellular signal-related kinase (ERK) phosphorylation and "
       "PDGF beta-receptor autophosphorylation")]
D[("GO:1904706", "IDA", "PMID:12070119")]["supported_by"] = [
    st("PMID:12070119",
       "Physiological concentrations of adiponectin significantly suppressed "
       "both proliferation and migration of HASMCs stimulated with "
       "platelet-derived growth factor (PDGF)-BB")]
D[("GO:1904753", "IDA", "PMID:12070119")]["supported_by"] = [
    st("PMID:12070119",
       "Cell migration assay was performed using a Boyden chamber")]
D[("GO:2000584", "ISS", "GO_REF:0000024")]["supported_by"] = [
    st("PMID:12070119",
       "without affecting autophosphorylation of PDGF alpha-receptor")]
D[("GO:0032757", "IDA", "PMID:19524870")]["supported_by"] = [
    st("PMID:19524870",
       "induced a dose-dependent increase in production of monocyte "
       "chemoattractant protein-1 and interleukin-8 by PBMCs and MVECs")]
D[("GO:0071639", "IDA", "PMID:19524870")]["supported_by"] = [
    st("PMID:19524870",
       "LMW adiponectin at the same concentrations did not induce chemokine "
       "production in any of the cell types tested")]
D[("GO:0050765", "IDA", "PMID:10961870")]["supported_by"] = [
    st("PMID:10961870",
       "Suppression of phagocytosis by adiponectin is mediated by one of the "
       "complement C1q receptors, C1qRp")]
D[("GO:0043124", "IDA", "PMID:10982546")]["supported_by"] = [
    st("PMID:10982546",
       "Adiponectin suppressed TNF-alpha-induced IkappaB-alpha "
       "phosphorylation and subsequent NF-kappaB activation")]
D[("GO:0043123", "ISS", "GO_REF:0000024")]["supported_by"] = [
    st("file:human/ADIPOQ/ADIPOQ-deep-research-affinage.md",
       "Hexameric and higher molecular weight (HMW) isoforms of Acrp30 "
       "activate NF-\u03baB in C2C12 myocytes via phosphorylation and "
       "degradation of I\u03baB-alpha, whereas trimeric Acrp30 and globular "
       "domain (gAcrp30) do not",
       reference_section_type="RESULTS")]

D[("GO:0010804", "IDA", "PMID:10604883")]["supported_by"] = [
    st("PMID:10604883",
       "Physiological concentrations of adiponectin dose-dependently inhibited "
       "TNF-alpha-induced THP-1 adhesion and expression of VCAM-1, E-selectin, "
       "and ICAM-1 on HAECs")]

# core-grade metabolic BPs
_METCORE = {
    "GO:0042593": ("Maintenance of blood glucose is adiponectin's principal "
                   "systemic role.",
                   "Adiponectin lowers glucose by suppressing hepatic glucose "
                   "output and increasing peripheral glucose disposal; "
                   "knockout mice are glucose intolerant and adiponectin "
                   "replacement reverses insulin resistance. This is a core "
                   "organismal process for the gene."),
    "GO:0045721": ("Suppression of hepatic gluconeogenesis is adiponectin's "
                   "best-characterised metabolic action.",
                   "PMID:11748271 showed Acrp30 infusion reduces endogenous "
                   "glucose production by about 65% and halves hepatic PEPCK "
                   "and G6Pase mRNA without affecting peripheral glucose "
                   "uptake, glycolysis or glycogen synthesis. Regulation, not "
                   "participation, and therefore the correct grain."),
    "GO:0045923": ("Adiponectin increases fatty-acid metabolism in muscle and "
                   "liver.",
                   "The regulation-grade counterpart of the role-conflated "
                   "GO:0006635 and GO:0019395 rows, and the term those should "
                   "be read alongside. Supported by AMPK-dependent "
                   "stimulation of fatty-acid oxidation."),
    "GO:0046326": ("Adiponectin stimulates glucose uptake in muscle.",
                   "PMID:12368907 showed adiponectin stimulates glucose uptake "
                   "and lactate production in myocytes through AMPK, and "
                   "PMID:16622416 traced GLUT4 membrane translocation to "
                   "APPL1-Rab5. A core metabolic action, correctly expressed "
                   "as regulation."),
}
for term, ev, ref in [("GO:0042593", "ISS", "GO_REF:0000024"),
                      ("GO:0042593", "ISS", "PMID:12368907"),
                      ("GO:0045721", "ISS", "PMID:12368907"),
                      ("GO:0045923", "ISS", "PMID:12368907"),
                      ("GO:0046326", "ISS", "PMID:12368907")]:
    summ, rsn = _METCORE[term]
    dec(term, ev, ref, action="ACCEPT", summary=summ, reason=rsn)
D[("GO:0046326", "ISS", "PMID:12368907")]["supported_by"] = [
    st("PMID:12368907",
       "Ad stimulates phosphorylation of acetyl coenzyme A carboxylase (ACC), "
       "fatty-acid oxidation, glucose uptake and lactate production in "
       "myocytes")]
D[("GO:0045721", "ISS", "PMID:12368907")]["supported_by"] = [
    st("PMID:12368907",
       "reduction of molecules involved in gluconeogenesis in the liver, and "
       "reduction of glucose levels in vivo")]


# --------------------------------------------------------------------------
# GO:0005515 -- per-partner
# --------------------------------------------------------------------------

PARTNER_GENE = {}  # filled from results.json if available


def protein_binding_entry(partner: str, ref: str, gene: str | None) -> dict:
    label = f"{gene} ({partner})" if gene else partner
    if partner == "P01127":
        return dict(
            action="MODIFY",
            summary="This is not a screen hit: adiponectin was shown to bind "
                    "PDGF-BB directly, and growth factor binding says so.",
            reason=(
                "PMID:12070119 is a hypothesis-led study in human aortic "
                "smooth muscle cells. Adiponectin bound 125I-PDGF-BB and "
                "blocked its association with the cells, while having no "
                "effect on the binding of 125I-PDGF-AA or 125I-HB-EGF - i.e. "
                "the interaction was measured and shown to be selective. "
                "GO:0019838 growth factor binding ('binding to a growth "
                "factor, proteins or polypeptides that stimulate a cell or "
                "organism to grow or proliferate') states the informative "
                "content that bare protein binding discards, and it is the "
                "molecular event underlying this gene's GO:0010642, "
                "GO:0070373, GO:1904706 and GO:1904753 rows. UniProt's SUBUNIT "
                "records the same for the mouse protein and extends it to "
                "HBEGF and FGF2 with multimer-specific affinities, which "
                "remains By similarity for human."),
            proposed_replacement_terms=[
                {"id": "GO:0019838", "label": "growth factor binding"}],
            supported_by=[st("PMID:12070119",
                             "Adiponectin specifically bound to (125)I-PDGF-BB "
                             "and significantly inhibited the association of "
                             "(125)I-PDGF-BB with HASMCs")])
    if partner == "Q96A54":
        return dict(
            action="MODIFY",
            summary="The partner is adiponectin's own receptor AdipoR1; "
                    "signaling receptor binding is the informative term.",
            reason=(
                "ADIPOR1 is one of the two seven-transmembrane adiponectin "
                "receptors cloned by expression cloning in PMID:12802337, and "
                "the reciprocal row exists on ADIPOR1 (Q96A54 carries "
                "GO:0005515 IPI PMID:16622416 with UniProtKB:Q15848). "
                "Replacing bare protein binding with GO:0005102 signaling "
                "receptor binding records what the partnership is. One caveat "
                "worth stating: PMID:16622416 is primarily an APPL1 paper, and "
                "what it demonstrates about adiponectin is that 'APPL1 "
                "interacts with adiponectin receptors in mammalian cells and "
                "the interaction is stimulated by adiponectin' - a "
                "ligand-dependent effect on a receptor complex rather than a "
                "direct binding measurement. The direct adiponectin-AdipoR1 "
                "interaction is established by PMID:12802337 instead."),
            proposed_replacement_terms=[
                {"id": "GO:0005102", "label": "signaling receptor binding"}],
            supported_by=[
                st("PMID:16622416",
                   "APPL1 interacts with adiponectin receptors in mammalian "
                   "cells and the interaction is stimulated by adiponectin"),
                st("PMID:12802337",
                   "they serve as receptors for globular and full-length "
                   "adiponectin")])
    extra = ""
    if partner == "O43765":
        extra = (" This partner (SGTA) is the only one recorded in more than "
                 "two of the seven IntAct publications, appearing in "
                 "PMID:25910212, PMID:31515488 and PMID:32296183 - but all "
                 "three are two-hybrid interactome datasets from the same "
                 "methodological lineage, so the repetition is the same assay "
                 "run again rather than orthogonal validation. SGTA is a "
                 "cytosolic co-chaperone for mislocalised tail-anchored "
                 "proteins, a well-known source of promiscuous hits.")
    elif partner == "P42858":
        extra = (" This partner (HTT, huntingtin) is a 3142-residue cytosolic "
                 "scaffold and one of the most frequently reported hubs in "
                 "interactome datasets; the reference here is a "
                 "neurodegeneration-focused interactome (PMID:32814053, 20010 "
                 "annotations in GOA).")
    return dict(
        action="MARK_AS_OVER_ANNOTATED",
        summary=(f"Unreplicated interactome-screen hit ({label}); no "
                 f"orthogonal evidence and no plausible compartment in which "
                 f"secreted adiponectin could meet it."),
        reason=(SCREEN_PREMISE + " " + SCREEN_TOPOLOGY + extra + " " +
                SCREEN_OVERANN_TAIL),
        supported_by=[st(RESULTS_REF,
                         "There is **no orthogonal biophysical assay** "
                         "anywhere in the set")])


# --------------------------------------------------------------------------
# emit
# --------------------------------------------------------------------------

def read_goa():
    lines = GOA_TSV.read_text().splitlines()
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def build() -> dict:
    import json
    rj = HERE / "results.json"
    if rj.exists():
        for p in json.loads(rj.read_text())["intact_census"]["partner_detail"]:
            PARTNER_GENE[p["with_from_token"]] = p["gene"]

    rows = read_goa()
    anns = []
    missing = Counter()
    for r in rows:
        term, ev, ref = r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"]
        entry = {
            "term": {"id": term, "label": r["GO NAME"]},
            "evidence_type": ev,
            "original_reference_id": ref,
        }
        if r["QUALIFIER"]:
            entry["qualifier"] = r["QUALIFIER"]
        wf = [t for t in r["WITH/FROM"].split("|") if t]
        if wf:
            entry["supporting_entities"] = wf

        if term == "GO:0005515":
            partner = r["WITH/FROM"].replace("UniProtKB:", "")
            rev = protein_binding_entry(partner, ref, PARTNER_GENE.get(partner))
            if partner == "P01127":
                # Record the sequestered ligand machine-readably.  It is an
                # INPUT of the binding, not a substrate -- adiponectin has no
                # catalytic activity, so `substrates` would misdescribe it.
                entry["extensions"] = [{
                    "predicate": "RO:0002233",
                    "term": {"id": "UniProtKB:P01127",
                             "label": "PDGFB (platelet-derived growth factor "
                                      "subunit B)"}}]
        else:
            d = D.get((term, ev, ref))
            if d is None:
                missing[(term, ev, ref)] += 1
                continue
            rev = dict(d)
        entry["review"] = rev
        anns.append(entry)

    if missing:
        raise SystemExit("no decision for:\n" +
                         "\n".join(f"  {k}" for k in sorted(missing)))
    assert len(anns) == len(rows), f"{len(anns)} entries vs {len(rows)} GOA rows"
    return {"existing_annotations": anns}


DESCRIPTION = (
    "Adiponectin is a 244-residue, adipocyte-specific secreted protein and one "
    "of the most abundant hormones in human plasma, circulating at roughly "
    "5-30 ug/ml. After removal of an 18-residue signal peptide the mature "
    "chain comprises a short variable N-terminal segment, a collagen-like "
    "domain of 22 Gly-X-Y repeats (residues 42-107) and a C-terminal globular "
    "C1q domain (108-244), the architecture that places it in the C1q/TNF-"
    "related (CTRP) superfamily alongside the complement C1q chains. Three "
    "chains associate through a triple helix of their collagen-like domains "
    "and hydrophobic contacts within the globular heads to form the obligate "
    "trimer; trimers then join through interchain disulfide bonds into "
    "hexamers and 12- to 18-mer high-molecular-weight complexes. Extensive "
    "post-translational modification of the collagen domain - proline and "
    "lysine hydroxylation, glucosyl-galactosyl glycosylation of the "
    "hydroxylysines, and sialylation of O-linked glycans on N-terminal "
    "threonines - governs how much high-molecular-weight complex is assembled "
    "and secreted and how long the protein persists in blood.\n\n"
    "Oligomeric state determines which signal adiponectin delivers. Trimers "
    "preferentially activate AMP-activated protein kinase in skeletal muscle, "
    "whereas hexameric and high-molecular-weight species activate NF-kB and "
    "are the only forms that bind T-cadherin. Signalling runs through two "
    "seven-transmembrane receptors, AdipoR1 and AdipoR2, which are unrelated "
    "to G-protein-coupled receptors and recruit the adaptor APPL1, and through "
    "the GPI-anchored receptor T-cadherin. Downstream, AMPK and PPAR-alpha "
    "activation increase fatty-acid oxidation and glucose uptake in muscle and "
    "suppress gluconeogenic gene expression in liver, which is the basis of "
    "adiponectin's insulin-sensitising and glucose-lowering action; infusion "
    "reduces endogenous glucose production by around two thirds.\n\n"
    "Beyond metabolism, adiponectin acts on the vessel wall and on myeloid "
    "cells. It binds PDGF-BB directly and sequesters it from its receptor, "
    "suppressing smooth-muscle proliferation and migration; it blocks "
    "TNF-induced NF-kB activation and adhesion-molecule expression in "
    "endothelium through a cAMP/PKA-dependent route; it lowers scavenger-"
    "receptor-mediated lipid uptake and raises ABCA1-dependent cholesterol "
    "efflux in macrophages; and it restrains myelomonocytic proliferation and "
    "phagocytosis. These effects are not uniformly anti-inflammatory - "
    "high-molecular-weight adiponectin induces MCP-1 and IL-8 in peripheral "
    "blood mononuclear cells and microvascular endothelium while the "
    "low-molecular-weight form does not - so the sign of the response depends "
    "on multimer state and on the target cell. Plasma adiponectin falls with "
    "visceral obesity and insulin resistance, and rare variants that impair "
    "high-molecular-weight assembly or secretion cause autosomal dominant "
    "adiponectin deficiency."
)

REF_TITLES = {
    "GO_REF:0000024": "Manual transfer of experimentally-verified manual GO annotation data to orthologs by curator judgment of sequence similarity",
    "GO_REF:0000033": "Annotation inferences using phylogenetic trees",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000107": "Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara",
    "PMID:10095105": "Organization of the gene for gelatin-binding protein (GBP28).",
    "PMID:10403784": "The human apM-1, an adipocyte-specific gene linked to the family of TNF's and to genes expressed in activated T cells, is mapped to chromosome 1q21.3-q23, a susceptibility locus identified for familial combined hyperlipidaemia (FCH).",
    "PMID:10604883": "Novel modulator for endothelial adhesion molecules: adipocyte-derived plasma protein adiponectin.",
    "PMID:10961870": "Adiponectin, a new member of the family of soluble defense collagens, negatively regulates the growth of myelomonocytic progenitors and the functions of macrophages.",
    "PMID:10982546": "Adiponectin, an adipocyte-derived plasma protein, inhibits endothelial NF-kappaB signaling through a cAMP-dependent pathway.",
    "PMID:11222466": "Adipocyte-derived plasma protein, adiponectin, suppresses lipid accumulation and class A scavenger receptor expression in human monocyte-derived macrophages.",
    "PMID:12021245": "Paracrine regulation of fat cell formation in bone marrow cultures via adiponectin and prostaglandins.",
    "PMID:12070119": "Adipocyte-derived plasma protein adiponectin acts as a platelet-derived growth factor-BB-binding protein and regulates growth factor-induced common postreceptor signal in vascular smooth muscle cell.",
    "PMID:12368907": "Adiponectin stimulates glucose utilization and fatty-acid oxidation by activating AMP-activated protein kinase.",
    "PMID:12611609": "The role of the novel adipocyte-derived hormone adiponectin in human disease.",
    "PMID:15585515": "Adiponectin in chronic kidney disease is related more to metabolic disturbances than to decline in renal function.",
    "PMID:16622416": "APPL1 binds to adiponectin receptors and mediates adiponectin signalling and function.",
    "PMID:17327472": "Effects of adiponectin on the renal sympathetic nerve activity and blood pressure in rats.",
    "PMID:18431508": "Adiponectin regulates albuminuria and podocyte function in mice.",
    "PMID:18703020": "Adiponectin prevents atherosclerosis by increasing cholesterol efflux from macrophages.",
    "PMID:19524870": "Induction of chemokine expression by adiponectin in vitro is isoform dependent.",
    "PMID:19855092": "Sialic acid modification of adiponectin is not required for multimerization or secretion but determines half-life in circulation.",
    "PMID:24531262": "Adiponectin reduces thermogenesis by inhibiting brown adipose tissue activation in mice.",
    "PMID:25910212": "Widespread macromolecular interaction perturbations in human genetic disorders.",
    "PMID:26166748": "Adiponectin Enhances Cold-Induced Browning of Subcutaneous Adipose Tissue via Promoting M2 Macrophage Proliferation.",
    "PMID:27068509": "Extracellular matrix remodelling in response to venous hypertension: proteomics of human varicose veins.",
    "PMID:28675934": "Characterization of the Extracellular Matrix of Normal and Diseased Tissues Using Proteomics.",
    "PMID:31515488": "Extensive disruption of protein interactions by genetic variants across the allele frequency spectrum in human populations.",
    "PMID:32296183": "A reference map of the human binary protein interactome.",
    "PMID:32814053": "Interactome Mapping Provides a Network of Neurodegenerative Disease Proteins and Uncovers Widespread Protein Aggregation in Affected Brains.",
    "PMID:36399478": "MatrisomeDB 2.0: 2023 updates to the ECM-protein knowledge database.",
    "PMID:8947845": "Isolation and characterization of GBP28, a novel gelatin-binding protein purified from human plasma.",
    "Reactome:R-HSA-1183058": "Expression of Adiponectin",
    "Reactome:R-HSA-8848663": "ADIPOQ trimer binds ADIPOR dimers",
    # added by this review; titles copied from publications/PMID_*.md frontmatter
    "PMID:12802337": "Cloning of adiponectin receptors that mediate antidiabetic metabolic effects.",
    "PMID:15210937": "T-cadherin is a receptor for hexameric and high-molecular-weight forms of Acrp30/adiponectin.",
    "PMID:11748271": "Endogenous glucose production is inhibited by the adipose-derived protein Acrp30.",
    "PMID:12087086": "Oligomerization state-dependent activation of NF-kappa B signaling pathway by adipocyte complement-related protein of 30 kDa (Acrp30).",
    "PMID:12496257": "Structure-function studies of the adipocyte-secreted hormone Acrp30/adiponectin. Implications fpr metabolic regulation and bioactivity.",
    "PMID:14522956": "Role of disulfide bonds in Acrp30/adiponectin structure and signaling specificity. Different oligomers activate different signal transduction pathways.",
    "PMID:19109165": "The peroxisome proliferator-activated receptor gamma agonist rosiglitazone ameliorates murine lupus by induction of adiponectin.",
    "PMID:19460854": "Inhibitory effects of adiponectin on platelet-derived growth factor-induced mesangial cell migration.",
    "PMID:11479627": "The fat-derived hormone adiponectin reverses insulin resistance associated with both lipoatrophy and obesity.",
}

REF_REVIEWS = {
    "PMID:19855092": dict(
        relevance="HIGH", correctness="MISCITED",
        review_notes=(
            "The identifier resolves to the intended paper and the paper is "
            "sound. It is recorded as MISCITED because the annotation it "
            "supports, GO:0033691 sialic acid binding, inverts the paper's "
            "finding: the study characterises adiponectin as the CARRIER of "
            "sialylated O-linked glycans, not as a sialic-acid-binding "
            "protein. UniProt encodes the same reference correctly, as "
            "CARBOHYD features at Thr-21/Thr-22 and a PTM comment.")),
    "PMID:10095105": dict(
        relevance="LOW", correctness="MISCITED",
        review_notes=(
            "A gene-structure paper (FISH mapping to 3q27, three exons, no "
            "TATA box) cited as TAS for GO:0006091 generation of precursor "
            "metabolites and energy. It performs no metabolic experiment. "
            "This is its only annotation in all of GOA.")),
    "PMID:24531262": dict(
        relevance="HIGH", correctness="DISPUTED",
        review_notes=(
            "Correctly cited for GO:0120163 (adiponectin suppresses "
            "thermogenesis) and incorrectly cited for the opposite term "
            "GO:0120162. The scientific claim is also genuinely disputed: "
            "PMID:26166748 reports the opposite direction in the same "
            "knockout model. Both papers are attached to both terms in GOA and "
            "in MGI.")),
    "PMID:26166748": dict(
        relevance="HIGH", correctness="DISPUTED",
        review_notes=(
            "Mirror image of PMID:24531262: correctly cited for GO:0120162 "
            "(adiponectin promotes cold-induced browning) and incorrectly "
            "cited for GO:0120163. Also the second independent report of the "
            "adiponectin-T-cadherin interaction, which GO records nowhere.")),
    "PMID:17327472": dict(
        relevance="MEDIUM", correctness="MISCITED",
        review_notes=(
            "Supports GO:0045776 negative regulation of blood pressure "
            "directly. It is flagged because it also carries GO:0010906 "
            "regulation of glucose metabolic process, which the abstract "
            "mentions only as background, and GO:0050805 negative regulation "
            "of synaptic transmission, whereas the measurement is renal "
            "sympathetic nerve activity. Full text was not available, so the "
            "curator's reading of the glucose row is not overruled.")),
    "PMID:28675934": dict(
        relevance="MEDIUM", correctness="MISCITED",
        review_notes=(
            "A legitimate ECM proteomics survey, correctly supporting the "
            "GO:0031012 HDA detection row. Flagged because the same reference "
            "also drives a bulk RCA block assigning GO:0005201 extracellular "
            "matrix structural constituent to 41 entities, a structural claim "
            "the proteomics cannot support for a circulating hormone.")),
    "PMID:36399478": dict(
        relevance="LOW", correctness="MISCITED",
        review_notes=(
            "MatrisomeDB 2.0 is a database-update paper, not a study of "
            "adiponectin. In GOA it supplies GO:0140149 to 272 distinct "
            "entities, i.e. it is a bulk import rather than an author "
            "statement about this gene.")),
    "PMID:32296183": dict(
        relevance="LOW", correctness="VERIFIED",
        review_notes=(
            "HuRI, the human binary reference interactome. Correctly cited as "
            "the source of 56 of this gene's GO:0005515 rows; it carries "
            "85343 annotations across GOA. Its relevance to adiponectin's "
            "biology is low because the assay is nuclear two-hybrid and the "
            "protein is secreted.")),
    "PMID:12611609": dict(
        relevance="LOW", correctness="VERIFIED",
        review_notes=(
            "A review article, correctly cited as NAS. Carries exactly two "
            "annotations in GOA, both on this gene.")),
    "PMID:12070119": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "The strongest molecular-function evidence in this gene's record: "
            "direct, selective radioligand binding of human adiponectin to "
            "PDGF-BB in human cells, with the receptor-proximal consequence "
            "measured. Verified against the cached abstract.")),
    "PMID:16622416": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Correctly identified; the reciprocal GO:0005515 row exists on "
            "ADIPOR1. Two caveats. The paper's subject is APPL1, and what it "
            "shows about adiponectin is that ligand stimulates the "
            "APPL1-AdipoR1 association rather than measuring adiponectin-"
            "AdipoR1 binding directly. Separately, PubMed records an "
            "unflagged erratum (Nat Cell Biol 2006;8(6):642, "
            "doi:10.1038/ncb1422) with a NULL PubMed id, found only by reading "
            "CommentsCorrections/RefType and resolving the DOI at Crossref; "
            "its content could not be retrieved here, so nothing beyond the "
            "quoted abstract sentence rests on this reference.")),
    "PMID:12802337": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "The expression cloning of AdipoR1 and AdipoR2 and the primary "
            "basis for adiponectin's receptor-ligand function. Also carries an "
            "unflagged erratum with a NULL PubMed id (Nature 2004;431:1123, "
            "doi:10.1038/nature03091), discoverable only through "
            "CommentsCorrections plus Crossref.")),
    "PMID:15210937": dict(
        relevance="HIGH", correctness="VERIFIED",
        review_notes=(
            "Identifies T-cadherin as the receptor for hexameric and HMW "
            "adiponectin. Absent from GOA entirely: neither ADIPOQ nor CDH13 "
            "carries any annotation naming the other.")),
    "PMID:19109165": dict(
        relevance="LOW", correctness="MISCITED",
        review_notes=(
            "The source of mouse Adipoq's GO:0071466 IDA, which reaches human "
            "ADIPOQ by ISS and IEA. The paper shows that rosiglitazone INDUCES "
            "adiponectin; adiponectin is the output of the xenobiotic "
            "response, not a participant in it.")),
    "PMID:19460854": dict(
        relevance="MEDIUM", correctness="VERIFIED",
        review_notes=(
            "Source of the mouse rows behind human GO:0030336, GO:2000584 and "
            "GO:2000590. Correctly cited; note the assay is cultured mesangial "
            "cells while GO:2000590 names metanephric mesenchymal cells, "
            "because GO has no mesangial cell migration term.")),
}

CORE_FUNCTIONS = [
    {
        "description": (
            "Adipocyte-derived endocrine hormone. Adiponectin is secreted into "
            "plasma and acts on distant tissues through the seven-"
            "transmembrane receptors AdipoR1 and AdipoR2 and the GPI-anchored "
            "receptor T-cadherin, initiating the adiponectin-activated "
            "signalling pathway and, through AMPK and PPAR-alpha, raising "
            "fatty-acid oxidation and glucose uptake in muscle while "
            "suppressing hepatic gluconeogenesis."),
        "molecular_function": {"id": "GO:0005179", "label": "hormone activity"},
        "directly_involved_in": [
            {"id": "GO:0033211", "label": "adiponectin-activated signaling pathway"},
            {"id": "GO:0038002", "label": "endocrine signaling"},
            {"id": "GO:0042593", "label": "glucose homeostasis"},
            {"id": "GO:0045721", "label": "negative regulation of gluconeogenesis"},
            {"id": "GO:0046326",
             "label": "positive regulation of D-glucose import across plasma membrane"},
            {"id": "GO:0045923",
             "label": "positive regulation of fatty acid metabolic process"},
        ],
        "locations": [{"id": "GO:0005576", "label": "extracellular region"}],
        "supported_by": [
            st("PMID:12368907",
               "stimulation of glucose utilization and fatty-acid oxidation by "
               "Ad occurs through activation of AMPK"),
            st("PMID:12802337",
               "they serve as receptors for globular and full-length adiponectin"),
        ],
    },
    {
        "description": (
            "Growth-factor sequestration. Adiponectin binds PDGF-BB directly "
            "and selectively - it does not bind PDGF-AA - preventing the "
            "ligand from engaging its receptor on vascular smooth muscle "
            "cells and thereby suppressing PDGF beta-receptor "
            "autophosphorylation, ERK1/2 activation, proliferation and "
            "migration. This is the one adiponectin activity with a directly "
            "measured, ligand-level molecular mechanism in human cells."),
        "molecular_function": {"id": "GO:0019838", "label": "growth factor binding"},
        "directly_involved_in": [
            {"id": "GO:0010642",
             "label": "negative regulation of platelet-derived growth factor "
                      "receptor signaling pathway"},
        ],
        "locations": [{"id": "GO:0005576", "label": "extracellular region"}],
        "supported_by": [
            st("PMID:12070119",
               "Adiponectin specifically bound to (125)I-PDGF-BB and "
               "significantly inhibited the association of (125)I-PDGF-BB "
               "with HASMCs"),
        ],
    },
    {
        "description": (
            "Homomultimer assembly. Three adiponectin chains associate through "
            "a triple helix of their collagen-like domains and hydrophobic "
            "contacts in the globular C1q heads to form the obligate trimer; "
            "trimers then join through interchain disulfide bonds into "
            "hexamers and 12- to 18-mer high-molecular-weight complexes. The "
            "assembly state is functionally decisive - trimers activate AMPK "
            "in muscle, hexamers and HMW species activate NF-kB and are the "
            "only forms that bind T-cadherin - so self-association is part of "
            "the gene's function rather than incidental. GO:0042802 is a "
            "deliberately unspecific term, and it is used here because it is "
            "the most specific CORRECT molecular function available: "
            "GO:0042803 protein homodimerization activity names a "
            "stoichiometry adiponectin does not adopt, and GO:0070207 protein "
            "homotrimerization - the term that does state it - exists only in "
            "the biological process branch. A search of the ontology returns "
            "no molecular function term for homotrimerisation or "
            "homooligomerisation, so the imprecision is the ontology's, not "
            "the annotation's."),
        "molecular_function": {"id": "GO:0042802", "label": "identical protein binding"},
        "directly_involved_in": [
            {"id": "GO:0070207", "label": "protein homotrimerization"},
        ],
        "locations": [{"id": "GO:0005576", "label": "extracellular region"}],
        "supported_by": [
            st("PMID:8947845",
               "possessing a collagen-like domain through which they form "
               "homo-trimers, which further combine to make oligomeric complexes"),
            st("PMID:14522956",
               "Thus, trimeric and HMW/hexameric Acrp30 activate different "
               "signal transduction pathways"),
        ],
    },
]

NEW_ANNOTATIONS = [
    {
        "term": {"id": "GO:0070207", "label": "protein homotrimerization"},
        "evidence_type": "IDA",
        "original_reference_id": "PMID:8947845",
        "qualifier": "involved_in",
        "review": {
            "action": "NEW",
            "summary": "Adiponectin's obligate assembly unit is a homotrimer, "
                       "and GO has a term that states exactly this; nothing in "
                       "the current record captures the stoichiometry.",
            "reason": (
                "The gene's whole signalling logic runs through assembly state "
                "- trimers activate AMPK in skeletal muscle, hexamers and HMW "
                "complexes activate NF-kB and are the only species T-cadherin "
                "binds - yet GOA records self-association only as GO:0042802 "
                "identical protein binding (IEA) and GO:0042803 protein "
                "homodimerization activity, the latter naming a stoichiometry "
                "adiponectin does not adopt. GO:0070207 is defined as 'the "
                "formation of a protein homotrimer, a macromolecular structure "
                "consisting of three noncovalently associated identical "
                "subunits', which matches UniProt's SUBUNIT description of a "
                "non-covalent collagen-domain triple helix precisely. "
                "PMID:8947845 characterised the human plasma protein and "
                "described this architecture directly."),
            "supported_by": [
                st("PMID:8947845",
                   "possessing a collagen-like domain through which they form "
                   "homo-trimers, which further combine to make oligomeric "
                   "complexes"),
                st("PMID:14522956",
                   "substitution of Cys22 with alanine led exclusively to trimers"),
            ],
        },
    },
]

PROPOSED_TERMS = [
    {
        "proposed_name": "regulation of glomerular permeability to albumin",
        "proposed_definition": (
            "Any process that modulates the rate, frequency or extent at which "
            "albumin crosses the glomerular filtration barrier from blood into "
            "the urinary space."),
        "proposed_parent": {"id": "GO:0003093",
                            "label": "regulation of glomerular filtration"},
        "justification": (
            "GO can currently express changes in urinary albumin only as "
            "renal albumin ABSORPTION (GO:0097018 and its regulation terms "
            "GO:2000532-2000534), which sits under GO:0097017 renal protein "
            "absorption - uptake from the nephron lumen. That is a different "
            "process from permselectivity of the glomerular filtration "
            "barrier, and the mismatch has produced a real mis-annotation: "
            "PMID:18431508 shows adiponectin acting through AMPK to reduce "
            "podocyte permeability to albumin, with no measurement of tubular "
            "reabsorption anywhere in the paper, yet both human ADIPOQ and "
            "mouse Adipoq carry GO:2000534 positive regulation of renal "
            "albumin absorption. Podocyte-barrier biology is a large and "
            "active field (nephrin, podocin, slit diaphragm) that has no "
            "adequate GO process term for its central readout."),
        "supported_by": [
            st("PMID:18431508",
               "both adiponectin and AMPK activation reduced podocyte "
               "permeability to albumin and podocyte dysfunction"),
        ],
    },
    {
        "proposed_name": "regulation of sympathetic nervous system activity",
        "proposed_definition": (
            "Any process that modulates the frequency, rate or extent of "
            "efferent signalling by the sympathetic division of the autonomic "
            "nervous system to its target organs."),
        "proposed_parent": {"id": "GO:0044057",
                            "label": "regulation of system process"},
        "justification": (
            "Searching GO for 'sympathetic' returns only developmental terms "
            "(GO:0048485 sympathetic nervous system development, GO:0061549, "
            "GO:0097490, GO:0097491, GO:0097492, GO:1903045) and for "
            "'autonomic' only GO:0048483 and GO:1901166. There is no term for "
            "modulating sympathetic outflow, which is a standard, directly "
            "measurable physiological readout. In its absence, PMID:17327472's "
            "measurement of reduced renal sympathetic nerve activity was "
            "annotated to GO:0050805 negative regulation of synaptic "
            "transmission, a term about communication across an individual "
            "synapse, which the study did not assay."),
        "supported_by": [
            st("PMID:17327472",
               "Both iv and LCV injections of adiponectin induced "
               "dose-dependent suppressions of RSNA and b/p"),
        ],
    },
]

QUESTIONS = [
    {"question":
     "GOA and MGI both attach GO:0120162 (positive) and GO:0120163 (negative) "
     "regulation of cold-induced thermogenesis to BOTH PMID:24531262 and "
     "PMID:26166748 - a full 2x2 cross-product in which each paper supports "
     "only one direction. Mouse Adipoq carries four IMP rows over the same two "
     "references and human ADIPOQ four ISS/IEA rows derived from them. Can MGI "
     "reduce this to one correctly-cited row per direction, after which the "
     "human ISS and Compara rows will follow?"},
    {"question":
     "GO records no interaction between adiponectin and T-cadherin (CDH13, "
     "P55290) on either gene: CDH13 has 60 annotations and none names Q15848 "
     "in WITH/FROM, and ADIPOQ's 61 GO:0005515 partners do not include it. "
     "T-cadherin is the established receptor for hexameric and HMW adiponectin "
     "(PMID:15210937) and mediates the M2-macrophage recruitment in "
     "PMID:26166748. AdipoR2 (Q86V24) is likewise absent from both records "
     "while AdipoR1 has a reciprocal pair. Should the two missing receptors be "
     "curated?"},
    {"question":
     "GO:0045296 cadherin binding is defined as 'binding to cadherin, a type I "
     "membrane protein involved in cell adhesion'. T-cadherin is "
     "GPI-anchored, not a type I membrane protein, so the definition as "
     "written excludes the one cadherin that is a hormone receptor. Should the "
     "definition be broadened to the cadherin superfamily by domain content "
     "rather than by membrane topology?"},
    {"question":
     "GO:0033691 sialic acid binding on ADIPOQ (IDA, PMID:19855092) records "
     "that adiponectin IS sialylated, not that it binds sialic acid; the same "
     "reference is used correctly by UniProt as CARBOHYD features. Mouse "
     "Adipoq has acquired the term by IEA and ISO from this human row, so it "
     "is the sole origin. Can it be retracted in both species?"},
    {"question":
     "Adiponectin's activity is multimer-dependent in a way GO cannot "
     "currently express: trimers activate AMPK but not NF-kB, hexamers and HMW "
     "complexes do the reverse and alone bind T-cadherin, and HMW but not LMW "
     "induces MCP-1 and IL-8. Several annotations on this gene are "
     "isoform-specific in that sense while carrying no marker of it. Is there "
     "an annotation-extension convention for oligomeric state, analogous to "
     "the isoform field for splice variants?"},
    {"question":
     "UniProt's SUBUNIT states that LMW, MMW and HMW complexes bind HBEGF and "
     "that HMW binds FGF2, with distinct affinities, but tags the whole "
     "statement ECO:0000250|UniProtKB:Q60994 (By similarity from mouse). The "
     "one human measurement, PMID:12070119, found no effect of adiponectin on "
     "HB-EGF binding to smooth muscle cells. Is there direct human evidence "
     "for HBEGF and FGF2 binding, or should the human entry be qualified?"},
]

EXPERIMENTS = [
    {"description":
     "Resolve the cold-thermogenesis contradiction by comparing the two "
     "knockout lines head to head. PMID:24531262 and PMID:26166748 used "
     "different Adipoq-null alleles, different cold protocols (acute 4 C "
     "challenge versus chronic intermittent exposure) and different depots "
     "(interscapular BAT versus subcutaneous WAT beiging). Run both protocols "
     "on both lines in one facility with matched housing temperature and diet, "
     "reading UCP1, core temperature and indirect calorimetry, and stratify by "
     "circulating HMW fraction.",
     "hypothesis":
     "Adiponectin suppresses beta3-adrenergic BAT activation acutely while "
     "promoting chronic beiging of subcutaneous fat through T-cadherin on M2 "
     "macrophages, so the two results are depot- and timescale-specific rather "
     "than contradictory."},
    {"description":
     "Test directly whether adiponectin binds sialic acid, the claim GO:0033691 "
     "makes. Assay purified recombinant adiponectin against a sialylated "
     "glycan array and by surface plasmon resonance against free Neu5Ac and "
     "sialyllactose, with a Siglec ectodomain as positive control and "
     "desialylated adiponectin as an internal control.",
     "hypothesis":
     "Adiponectin shows no measurable sialic acid binding; the annotation "
     "originates from a post-translational modification of adiponectin itself, "
     "and the array will be negative at all concentrations."},
    {"description":
     "Establish the human interactome of adiponectin with an assay compatible "
     "with its topology. Perform secretome-scale extracellular interaction "
     "screening (for example AVEXIS or an equivalent avidity-based assay using "
     "eukaryotically expressed, multimerised ectodomain baits) against a "
     "library of human cell-surface and secreted proteins, and confirm hits by "
     "surface plasmon resonance with size-fractionated trimer, hexamer and HMW "
     "adiponectin.",
     "hypothesis":
     "None of the 59 unreplicated two-hybrid partners will reproduce, whereas "
     "AdipoR1, AdipoR2, T-cadherin, CD93 and PDGF-BB will, and several hits "
     "will be specific to the hexamer/HMW species."},
    {"description":
     "Separate ligand sequestration from receptor signalling in the vascular "
     "phenotype. Compare wild-type adiponectin with a C1q-domain point mutant "
     "that retains AdipoR binding but loses PDGF-BB binding (identified by "
     "alanine scanning guided by the 6U66 structure) for their ability to "
     "suppress PDGF-BB-driven proliferation and migration of human aortic "
     "smooth muscle cells.",
     "hypothesis":
     "The anti-proliferative effect depends on direct PDGF-BB sequestration "
     "rather than on AdipoR signalling, so the separation-of-function mutant "
     "will lose the vascular effect while retaining AMPK activation."},
    {"description":
     "Determine whether the podocyte effect is filtration or reabsorption, "
     "which decides between GO:2000534 and the proposed glomerular "
     "permeability term. Combine micropuncture or FITC-albumin two-photon "
     "imaging of the glomerular filtration barrier with megalin/cubilin-"
     "dependent proximal tubule uptake assays in adiponectin-treated and "
     "untreated Adipoq-null mice.",
     "hypothesis":
     "Adiponectin reduces trans-barrier albumin flux with no change in tubular "
     "reabsorptive capacity, confirming that the existing absorption term "
     "names the wrong process."},
]

KNOWLEDGE_GAPS = [
    {"gap_statement":
     "No structure of adiponectin bound to any of its three receptors exists. "
     "The three deposited structures (4DOU, 6U66, 6U6N) all cover only the "
     "globular C1q domain, residues 104-244, so neither the collagen-like "
     "domain nor any receptor complex has been resolved, and the structural "
     "basis of multimer-selective T-cadherin binding is unknown.",
     "gap_kind": ["BIOLOGY"],
     "dark_aspect": "RESIDUAL_SUBGAP",
     "status": "OPEN",
     "boundary":
     "The globular C1q domain fold is solved to 0.99 A (PDB 6U66, residues "
     "107-244), the trimer/hexamer/HMW ladder and its disulfide dependence are "
     "established, and the three receptors are identified.",
     "significance":
     "Multimer-selective receptor engagement is the central unexplained "
     "feature of adiponectin biology and the main obstacle to designing "
     "receptor-selective agonists.",
     "provenance": [
         st("file:human/ADIPOQ/ADIPOQ-uniprot.txt",
            "DR   PDB; 6U66; X-ray; 0.99 A; A/B/C=107-244.")]},
    {"gap_statement":
     "Whether the globular fragment of adiponectin, which is far more potent "
     "than the full-length protein in many assays, is actually generated in "
     "vivo in humans remains unresolved. It can be released from full-length "
     "adiponectin by neutrophil elastase in vitro, but whether it circulates "
     "at meaningful concentrations is disputed, and much of the receptor "
     "literature uses it as a surrogate.",
     "gap_kind": ["BIOLOGY"],
     "dark_aspect": "RESIDUAL_SUBGAP",
     "status": "OPEN",
     "boundary":
     "Neutrophil elastase can release the globular fragment from full-length "
     "adiponectin in vitro, and the fragment binds AdipoR1/AdipoR2 and "
     "activates AMPK; what is unresolved is whether it exists in human "
     "circulation at functionally relevant levels.",
     "significance":
     "A large fraction of the functional literature, and therefore of this "
     "gene's GO record, rests on globular adiponectin whose physiological "
     "existence is uncertain.",
     "provenance": [
         st("PMID:18431508",
            "although it remains controversial whether the globular fragment "
            "of adiponectin is generated in situ or circulates in vivo")]},
    {"gap_statement":
     "The sign of adiponectin's effect on inflammation is unresolved and "
     "appears to depend on multimer state and target-cell polarisation. HMW "
     "adiponectin induces MCP-1 and IL-8 in peripheral blood mononuclear cells "
     "and microvascular endothelium while LMW does not, and hexamer/HMW "
     "species activate NF-kB in myocytes, yet adiponectin suppresses "
     "TNF-induced NF-kB in endothelium. GOA carries both directions with no "
     "marker of the conditions that distinguish them.",
     "gap_kind": ["BIOLOGY", "ONTOLOGY"],
     "dark_aspect": "RESIDUAL_SUBGAP",
     "status": "OPEN",
     "boundary":
     "The multimer species are separable and individually assayable, and their "
     "divergent effects on AMPK, NF-kB and T-cadherin binding are reproducible; "
     "what is missing is a rule predicting the sign in a given cell type, and "
     "any way to record multimer state in a GO annotation.",
     "significance":
     "Both GO:0043123 and GO:0043124, and both GO:0050728 and the chemokine-"
     "induction rows, are simultaneously annotated; without a convention for "
     "recording multimer state the record cannot express what is actually "
     "known.",
     "provenance": [
         st("PMID:19524870",
            "LMW adiponectin at the same concentrations did not induce "
            "chemokine production in any of the cell types tested")]},
]


def full_document() -> dict:
    ann = build()["existing_annotations"]
    ann.extend(NEW_ANNOTATIONS)
    refs = []
    for rid in sorted(REF_TITLES):
        r = {"id": rid, "title": REF_TITLES[rid]}
        # Read the flag from the cached publication rather than hand-listing
        # it: a hand-maintained list drifts, and a STALE
        # full_text_unavailable: true suppresses evidence extraction.
        if rid.startswith("PMID:"):
            f = (GENE_DIR.parents[2] / "publications"
                 / f"PMID_{rid.split(':', 1)[1]}.md")
            if not f.exists():
                raise SystemExit(
                    f"missing {f}; run `just fetch-pmid {rid.split(':')[1]}`")
            fm = yaml.safe_load(f.read_text().split("---")[1])
            if fm.get("full_text_available") is False:
                r["full_text_unavailable"] = True
        if rid in REF_REVIEWS:
            r["reference_review"] = dict(REF_REVIEWS[rid])
        refs.append(r)
    return {
        "id": "Q15848",
        "gene_symbol": "ADIPOQ",
        "product_type": "PROTEIN",
        "status": "COMPLETE",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": DESCRIPTION,
        "references": refs,
        "existing_annotations": ann,
        "core_functions": CORE_FUNCTIONS,
        "proposed_new_terms": PROPOSED_TERMS,
        "suggested_questions": QUESTIONS,
        "suggested_experiments": EXPERIMENTS,
        "knowledge_gaps": KNOWLEDGE_GAPS,
    }


if __name__ == "__main__":
    doc = full_document()
    n_goa = len(read_goa())
    n_new = len(NEW_ANNOTATIONS)
    assert len(doc["existing_annotations"]) == n_goa + n_new, (
        f"{len(doc['existing_annotations'])} entries vs {n_goa} GOA rows "
        f"+ {n_new} NEW")
    txt = yaml.dump(doc, Dumper=NoAliasDumper, sort_keys=False,
                    default_flow_style=False, width=88, allow_unicode=True)
    assert "&id" not in txt, "YAML anchor survived; rows are sharing objects"
    OUT.write_text(txt)
    print(f"wrote {OUT}: {n_goa} GOA rows + {n_new} NEW = "
          f"{len(doc['existing_annotations'])} entries")
    sys.exit(0)
