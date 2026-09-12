# LRCH1 literature notes

## Evidence overview

LRCH1 is a cytoplasmic leucine-rich-repeat/calponin-homology-domain protein whose
best-supported proximal mechanism is inhibition of DOCK8-dependent Cdc42 activation
during chemokine-guided T-cell migration. The decisive study reports that “LRCH1
competes with Cdc42 for interaction with DOCK8 and restrains T cell migration” and
that chemokine-triggered PKCα phosphorylation releases DOCK8 from LRCH1 for
leading-edge recruitment [PMID:28028151, “Using two screening systems, we found
that LRCH1 competes with Cdc42 for interaction with DOCK8 and restrains T cell
migration. In response to chemokine stimulation, PKCα phosphorylates DOCK8 at its
three serine sites, promoting DOCK8 separation from LRCH1 and translocation to the
leading edge to guide T cell migration.”]. The paper combines human screening/cell
systems with mouse primary cells and experimental autoimmune encephalomyelitis;
its EAE protection/severity findings therefore remain mouse disease context
[PMID:28028151, “Importantly, Dock8 mutant mice or Lrch1 transgenic mice were
protected from MOG (35-55) peptide-induced experimental autoimmune encephalomyelitis
(EAE), whereas Lrch1-deficient mice displayed a more severe phenotype.”].

Independent human evidence supports the migration phenotype. In peripheral CD4+
T cells from an ulcerative-colitis study, LRCH1 manipulation did not alter the
assayed differentiation/cytokine outputs, while LRCH1 inhibited CXCL12-directed
migration [PMID:32210709, “Up or down regulation of LRCH1 did not affect the
differentiation of CD4+ T cells, and the related cytokines expression. Moreover,
LRCH1 inhibited migratory capacity of CD4+ T cells toward CXCL12 by PKCα.”]. Lower
LRCH1 expression in active-UC mucosa and PBMCs was inversely correlated with disease
activity, but this is an association rather than proof that LRCH1 initiates UC
[PMID:32210709, “LRCH1 expression was highly decreased in colonic mucosa and PBMCs
from patients with A-UC, and negatively correlated with disease activity.”].

## Additional immune contexts

LRCH1 also restrains LAT-dependent CD8+ T-cell signaling in a study dominated by
mouse mechanistic and in-vivo experiments: the abstract reports direct LAT binding,
reduced LAT phosphorylation/GRB2 interaction, and increased LAT endocytosis
[PMID:32727906, “Here we have demonstrated that LRCH1 (leucine-rich repeats and
calponin homology domain containing 1) directly binds LAT, reduces LAT phosphorylation
and interaction with GRB2, and also promotes the endocytosis of LAT.”]. The explicitly
human experiment used engineered glypican-3 CAR T cells in vitro, where LRCH1 knockout
improved migration and proliferation [PMID:32727906, “Furthermore, knockout of LRCH1
in human chimeric antigen receptor (CAR) T cells that recognize the liver
tumor-associated antigen glypican-3 could improve CAR T cell migration and
proliferation in vitro.”]. The cached record is abstract-only, so assay-level details
beyond those statements should not be inferred.

In NK-92 cells, LRCH1 knockout increased tumor-contact cytotoxicity and Src/Lck
activation [PMID:32173150, “Further experiments revealed that LRCH1 knockout
enhanced the activation of Src and Lck kinase which are important for natural killer
cell cytotoxicity.”]. Primary human NK cells showed increased IFN-γ and TNF-α after
LRCH1 knockout [PMID:32173150, “Importantly, human primary natural killer cells
exhibited a similar increase in the production of IFN-γ and TNF-α when LRCH1 was
knocked out.”]. This abstract-only paper does not demonstrate direct LRCH1 binding
to Src or Lck, and most mechanistic evidence is confined to the NK-92 cell line.

Rat primary-microglia knockdown increased inflammatory cytokine production in a
spinal-cord-injury study [PMID:32631435, “LRCH1 knockdown increased the production
of pro-inflammatory cytokines such as IL-1β, TNF-α, and IL-6 after in vitro priming
with lipopolysaccharide and adenosine triphosphate.”]. The authors explicitly used
primary microglia and a rat SCI model [PMID:32631435, “To elucidate the significance
of LRCH1 to microglial functions, we applied lentivirus-induced LRCH1 knockdown in
primary microglia culture and tested the role of LRCH1 in microglia-mediated
inflammatory reaction both in vitro and in a rat SCI model.”]. This supports a
species- and injury-context hypothesis, not an established human microglial core
function.

## DOCK7, cytoskeletal, and complex boundaries

PMID:29467281 supplies focused evidence for LRCH1 association with DOCK7 and a useful
negative boundary: “no interaction between LRCH1 and MYO6 was observed, although
LRCH1 did co‐immunoprecipitate DOCK7” [PMID:29467281, “Although other LRCH family
members such as LRCH1 were identified in the MYO6 and DOCK7 BioID data sets, no
interaction between LRCH1 and MYO6 was observed, although LRCH1 did
co‐immunoprecipitate DOCK7”]. The same paper's MYO6-linker,
DISP-complex, and septin-remodeling mechanism is mapped to LRCH3. It must not be
transferred to LRCH1, and the LRCH1-DOCK7 co-IP alone does not establish that LRCH1
inhibits DOCK7 or forms a constitutive stable complex.

Proteome-scale studies underlying other GOA/IntAct rows corroborate DOCK8 or DOCK7
contacts but do not define a shared biochemical activity. They should remain
screen-level evidence, with partner identity and tested DOCK8 isoform retained as
provenance rather than interpreted as LRCH1 isoform-specific biology
(PMID:24255178; PMID:25416956; PMID:31515488; PMID:33961781; PMID:35271311;
PMID:40205054).

A Drosophila study found that the single fly dLRCH stabilizes the mitotic cell cortex
[PMID:20805893, “Taking advantage of the existence of a single LRCH gene in flies,
dLRCH, we explored its function in cultured cells, and show that dLRCH act to
stabilize the cell cortex during cell division.”]. It also establishes that human
LRCH1-4 share the combined LRR/CH architecture [PMID:20805893, “In human, only four
highly-related proteins (hLRCH1-4) simultaneously harbor these two motifs.”]. The
fly cortex, spindle-positioning, fertility, and stress-robustness phenotypes are
family-level evolutionary context, not direct functions of human LRCH1. Likewise,
the presence of a calponin-homology domain does not by itself establish direct actin
binding by human LRCH1.

## Isoforms and remaining uncertainties

The reviewed UniProt record lists three alternatively spliced products (Q9Y2L9-1,
Q9Y2L9-2, and Q9Y2L9-3). None of the focused functional papers establishes that the
DOCK8-Cdc42, LAT, DOCK7, or immune phenotypes are unique to one endogenous LRCH1
isoform. A screened DOCK8 isoform records the partner construct that was tested, not
an LRCH1 isoform-specific function. IntAct lists TMEM14A/TMEM14B contacts for
Q9Y2L9-3, but these were not among the seeded GO annotations and no functional
mechanism was established here.

Open questions include whether LRCH1 regulates DOCK7 nucleotide-exchange activity,
whether the LAT and DOCK8 mechanisms share an endogenous membrane-recruitment step,
how the LRR and CH regions contribute independently, and which immune-cell contexts
operate in unmanipulated human tissue.
