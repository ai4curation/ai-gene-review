# GLIPR2 review notes

## 2026-07-18: data acquisition

- `just fetch-gene human GLIPR2` retrieved UniProt Q9H4G4 and 13 grouped GOA annotations.
- `just fetch-gene-pmids human GLIPR2` confirmed that all six GOA-cited PMIDs were cached.
- Required automated research was attempted with Falcon and the configured
  Perplexity fallback. Falcon/Edison failed with HTTP 402 (payment required), and
  Perplexity-lite failed with HTTP 401 (insufficient quota). No provider-named
  deep-research file was created manually. The review therefore uses the cached
  primary literature, UniProt, QuickGO term definitions, and the local PANTHER
  propagation table.

## Protein identity and topology

GLIPR2 encodes the 154-aa Golgi-associated plant pathogenesis-related protein 1
(GAPR-1), a compact CAP/SCP-domain protein. Unlike most CAP-superfamily members,
it has no signal peptide and is not routed through the secretory pathway. The
original localization study states that it "localizes to the cytosolic site of
the endomembrane system in mammalian cells" and identifies myristoylation plus
electrostatic/protein interactions as the basis of strong Golgi-membrane
association [PMID:11865038, "Here we report the identification of a novel family
member that localizes to the cytosolic site of the endomembrane system in
mammalian cells."] [PMID:11865038, "Myristoylation, together with protein-protein
or electrostatic interactions at physiological pH owing to the highly basic pI
of GAPR-1 (pI 9.4) could explain the strong membrane association of GAPR-1."]

The protein forms homodimers in vitro and in vivo, and negatively charged lipids
favor a dimer conformation that tethers liposomes [PMID:15123429, "Here we report
that GAPR-1 may form dimers in vitro and in vivo, as determined by yeast
two-hybrid screening, biochemical and biophysical assays."] [PMID:22560898, "In
the presence of negatively charged lipids, GAPR-1 caused a rapid and stable
tethering of liposomes."]

## Core molecular function: inhibition of autophagy-initiating class III PI3K

The Tat-BECN1 study identified endogenous GLIPR2 as a BECN1-binding protein and
showed that knockdown increases autophagic flux. It further proposed that
Golgi-bound GLIPR2 tethers inactive BECN1 at the Golgi [PMID:23364696, "Taken
together, our data indicate that GAPR-1 is a beclin 1-interacting protein that
negatively regulates autophagy."] [PMID:23364696, "Thus, GAPR-1 may function to
tether beclin 1 in the Golgi apparatus (where it is inactive in autophagy), and
the Tat–beclin 1 peptide may promote the release of beclin 1 from the Golgi,
resulting in enhanced early autophagosome formation."]

The later definitive study used three independent CRISPR GLIPR2-null HeLa lines,
wild-type rescue, multiple flux assays, purified proteins, and Glipr2-null mice.
It showed that GLIPR2 directly binds the ATG14-containing class III
phosphatidylinositol 3-kinase complex I (PtdIns3K-C1), lowers its membrane
association and lipid kinase activity, and restrains basal macroautophagy
[PMID:33222586, "GLIPR2 binds to purified PtdIns3K-C1 and inhibits its in vitro
lipid kinase activity."] [PMID:33222586, "Thus, using four independent assays, we
demonstrate that GLIPR2 negatively regulates autophagy in cultured cells."]
[PMID:33222586, "Taken together, these data reveal increased autophagic flux and
PtdIns3K-C1 activity in glipr2-/-mice, providing evidence that GLIPR2 functions
as a negative regulator of autophagy in vivo."]

QuickGO defines GO:0141039, phosphatidylinositol 3-kinase inhibitor activity, as
"Binds to and decreases the activity of a phosphatidylinositol 3-kinase
(PI3K)." The purified-complex result meets this definition directly. The core
biological-process term is GO:0016242, negative regulation of macroautophagy.

## Context-dependent cellular phenotypes

In HK-2 human proximal-tubule cells, forced GLIPR2 expression increased
phospho-ERK1/2, EMT markers, and migration; a non-myristoylated construct lacked
these effects [PMID:23516513, "The GLIPR-2-transfected HK-2 cells had an increased
level of phospho-ERK1/2."] [PMID:23516513, "However, p-ERK1/2 and EMT markers did
not change in the non-myr GLIPR-2-transfected HK-2 cells."] A second study in
human hepatocellular-carcinoma lines combined overexpression and knockdown and
found that loss of GLIPR2 attenuated hypoxia-associated ERK activation, EMT,
migration, and invasion [PMID:24204846, "These results revealed that suppression
of GLIPR-2 expression in human HCC cells attenuated ERK1/2 activation and EMT-like
process following by migration and invasion in response to hypoxia."] These are
valid direct annotations but are disease/cell-culture contexts rather than the
best definition of the protein's core biochemical function.

An abstract-only study reports that IRAK1 phosphorylation of GAPR-1 promotes its
interaction with TMED7 and enhances TLR4-induced type-I-interferon/IL10 output
[PMID:26678074, "The phosphorylation of GAPR-1 promoted its interaction with
TRAM-TRIF dependent inhibitor TMED7, and impaired TMED7-mediated disruption of
the TRAM-TRIF complex to trigger IFN-β and the IL10 secretion."] This mechanism
is relevant but the full text was unavailable, so no new GO annotation is
proposed from it.

## PAINT propagation assessment

The local PANTHER table `interpro/panther/PTHR10334/PTHR10334-paint.tsv` shows:

- extracellular region (GO:0005576) at the very broad PTN000036124 node, seeded
  by multiple secreted CAP-family proteins; and
- molecular adaptor activity (GO:0060090) at the same broad node, seeded solely
  by mouse Glipr1l1 (MGI:MGI:1916536), a sperm/acrosomal paralog.

PTHR10334 spans 107 subfamilies and more than 36,000 proteins across animals,
plants, fungi, and other taxa. Direct evidence makes GLIPR2 a clear topology
exception: it is cytosolic and Golgi-membrane-associated rather than secreted.
The extracellular IBA and InterPro-derived IEA should therefore be removed.

The Glipr1l1-seeded adaptor propagation is not evidence for GLIPR2. Nevertheless,
GLIPR2 has a directly demonstrated, more informative molecular activity:
inhibition of PtdIns3K-C1. The broad adaptor annotation is therefore modified to
GO:0141039 rather than simply retained from an unrelated paralog.

## Exosome proteomics

Three HDA annotations report GLIPR2 in neural-stem-cell, urinary, and
prostate-secretion exosome preparations. These are compatible with occasional
packaging of a Golgi peripheral-membrane protein into extracellular vesicles,
but they do not overturn the direct cytosolic Golgi topology or establish that
exosomes are the protein's core site of action. They are retained as non-core.

## Evidence boundary

The PI3K/autophagy mechanism is supported by direct purified-protein assays,
human-cell knockout/rescue, and mouse knockout phenotypes. The following remain
unresolved: the exact endogenous compartment in which GLIPR2 inhibits
PtdIns3K-C1; whether it also inhibits PtdIns3K-C2; whether Golgi dispersion is a
cause or consequence of autophagy; how the autophagy mechanism relates to
ERK/EMT and TLR4-interferon phenotypes; and whether lipid/metal-dependent
amyloid-like assemblies observed in vitro have a physiological role.

Two recent yeast overexpression studies provide useful but limited context:
human GAPR-1 forms dynamic reversible inclusions, and its known BECN1-binding
surface suppresses co-expressed human BECN1 condensates [PMID:34298062,
"These cytosolic inclusions are dynamic and reversible organelles that gradually
increase during time of overexpression and decrease after promoter shut-off."]
[PMID:36586462, "Surprisingly, co-expression of hGAPR-1-GFP and hBeclin 1-mCherry
results in a strong reduction of hBeclin 1 condensates."] Because both proteins
were overexpressed in *Saccharomyces cerevisiae*, these results do not establish
an endogenous condensate mechanism in human cells.
