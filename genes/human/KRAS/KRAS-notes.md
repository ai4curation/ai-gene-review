# KRAS review notes

Initial review date: 2026-05-02

## Evidence summary

KRAS is a Ras-family small GTPase. UniProt describes human KRAS as binding GDP/GTP
and having intrinsic GTPase activity, with the catalytic reaction GTP + H2O -> GDP
+ phosphate. It cycles between GDP-bound inactive and GTP-bound active states and
is regulated by GEFs and GAPs [file:human/KRAS/KRAS-uniprot.txt, "Ras proteins
bind GDP/GTP and possess intrinsic GTPase activity"; "Alternates between an
inactive form bound to GDP and an active form bound to GTP"].

KRAS membrane localization is central to function. UniProt places KRAS at the cell
membrane, cytoplasmic side, endomembrane system, and cytosol [file:human/KRAS/KRAS-uniprot.txt,
"Cell membrane ... Lipid-anchor"; "Endomembrane system"; "Cytoplasm, cytosol"].
PDEdelta regulates correct localization of farnesylated KRAS and supports the cytosolic
trafficking pool [PMID:23698361 Small molecule inhibition of the KRAS-PDEdelta
interaction impairs oncogenic KRAS signalling, "Correct localization and signalling
by farnesylated KRAS is regulated by the prenyl-binding protein PDEδ"].

KRAS4A and KRAS4B differ in C-terminal targeting mechanisms. K-Ras4A is regulated by
lysine fatty acylation; SIRT2-mediated removal of lysine acylation promotes
endomembrane localization and ARAF interaction [PMID:29239724 SIRT2 and lysine fatty
acylation regulate the transforming activity of K-Ras4a, "SIRT2-mediated lysine
defatty-acylation promotes endomembrane localization of K-Ras4a"].

KRAS participates directly in Ras protein signal transduction. SOS1 facilitates
GDP-to-GTP exchange on KRAS [PMID:38188543 Studying early structural changes in SOS1
mediated KRAS activation mechanism, "SOS1 facilitates the exchange of GDP to GTP
thereby leading to activation of KRAS"]. GTP-bound RAS recruits RAF and promotes RAF
activation in the RAF-MEK-ERK cascade [Reactome:R-HSA-5673001 RAF/MAP kinase cascade,
"GTP-bound RAS recruits RAF"; PMID:33608534 KRAS interaction with RAF1 RAS-binding
domain and cysteine-rich domain provides insights into RAS-mediated RAF activation,
"Active RAS recruits RAF to the membrane where RAF dimerizes and becomes active"].
RAS-PI3Kalpha interaction also supports PI3K-AKT-mTOR signaling [PMID:39788953
Structural insights into isoform-specific RAS-PI3Kalpha interactions and the role of
RAS in PI3Kalpha activation, "activating PI3Kα and amplifying the PI3K-AKT-mTOR pathway"].

## Curation decisions

Core annotations are GTPase activity, G protein activity/GTP-GDP switch behavior, Ras
protein signal transduction, and MAPK cascade activation at membranes. Plasma membrane,
cytoplasmic side of plasma membrane, endomembrane system, cytosol/cytoplasm, Golgi,
ER, and mitochondrial outer membrane annotations were handled according to how directly
they support KRAS signaling versus trafficking or isoform/modification-specific biology.

Generic protein binding annotations were removed. They record real interactions in some
cases, but GO:0005515 does not describe KRAS function and is explicitly discouraged by
the project guidelines.

High-level phenotype/process annotations such as liver development, pregnancy, hormone
responses, response to gravity/isolation stress, and cell-type proliferation were marked
as over-annotated unless they had direct pathway support. Proliferation, TOR signaling,
and senescence were retained as non-core where they reflect plausible downstream outcomes
of KRAS effector signaling.

## Limitations

`just fetch-gene human KRAS` hit NCBI HTTP 429 errors for several PMIDs. I retried
PMID:20949621, PMID:22065586, PMID:35831509, and PMID:39043660 but the fetch still
failed. I updated their reference titles from accessible web/PubMed or structural
database metadata and marked findings as full-text unavailable where needed. These
failed cached publications should be refreshed later with `just fetch-gene-pmids human KRAS`
or targeted `just fetch-pmid` retries.
