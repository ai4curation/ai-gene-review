# SERINC1 manual deep-research synthesis

Date: 2026-07-18

## Scope and provenance

This synthesis was prepared manually from the reviewed human UniProt record
Q9NRX5, all 16 GOA rows (12 grouped review entries), and every cached primary
reference used for this review. The automated Falcon run failed with HTTP 402
(payment required), and its Perplexity-lite fallback failed with HTTP 401
(insufficient quota). Neither failed provider output was retained.

## Protein identity, topology, and localization

SERINC1 is a 453-residue, N-myristoylated multipass membrane protein in the
TDE1/SERINC family. Reviewed UniProt predicts 11 transmembrane helices and places
the human protein at the endoplasmic-reticulum membrane by similarity to rat
Serinc1. The rat experiment directly reported that "rat Serinc1 protein
co-localizes with lipid biosynthetic enzymes in endoplasmic reticulum membranes"
[PMID:16120614]. Human UniProt does not currently describe a plasma-membrane
pool, although the rat GO record carries a plasma-membrane IDA annotation.

## Core biochemical evidence

The direct functional study was performed with rat Serinc1 and other mammalian
SERINC-family proteins rather than endogenous human SERINC1. It found that the
family "facilitates the synthesis of two serine-derived lipids,
phosphatidylserine and sphingolipids" [PMID:16120614]. Full-text experiments
reported increased phosphatidylserine-synthase and serine-palmitoyltransferase
activities after Serinc1 expression, interaction with SPTLC1, and no increase in
free-serine uptake across the membrane. The mechanistic interpretation is an ER
membrane scaffold/adaptor and enzyme-activity enhancer, not an established
L-serine transmembrane transporter.

The current GO term GO:0010698, acetyltransferase activator activity, is too
specific for this evidence: serine C-palmitoyltransferase is an acyltransferase,
not an acetyltransferase. GO:0008047 enzyme activator activity is the appropriate
broader replacement. GO:0030674 protein-macromolecule adaptor activity captures
the proposed organization of serine-synthetic and lipid-biosynthetic enzymes.

## Physiological boundary

A Serinc1-null mouse study found that loss of the transcript in macrophages and
lymphocytes "did not significantly alter serine-derived lipid composition"
[PMID:28006656]. It also found no effect on the tested macrophage functions,
lymphocyte proliferation, viability, fertility, or autoimmune susceptibility.
This negative result does not refute the overexpression biochemistry, but it
shows that SERINC1 is dispensable in those contexts and suggests compensation by
other SERINC-family members.

## Human interaction-screen evidence

Two human systematic-interactome papers supply generic protein-binding
annotations. PMID:20195357 reports an mRNA-display interaction with PAX8;
PMID:32296183 reports yeast-two-hybrid interactions with FFAR3, GPR42, AQP9,
and GPX8. These datasets establish candidate binary contacts but do not assign a
SERINC1-specific molecular mechanism or connect the partners to serine-derived
lipid synthesis. Generic protein binding is therefore over-annotated relative
to the informative adaptor/enzyme-regulator functions.

## Evidence conclusion

SERINC1 is best described as an ER multipass membrane adaptor and broad enzyme
activity enhancer that promotes serine incorporation into phosphatidylserine
and sphingolipids. This human assignment is supported by mammalian orthology and
direct rat biochemistry; direct endogenous human biochemical validation remains
missing, and single-gene loss can be phenotypically buffered in mouse immune
cells.
