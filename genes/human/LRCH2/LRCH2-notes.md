# LRCH2 literature notes

## Evidence overview

Human LRCH2 is a poorly characterized LRR/CH-domain protein. The strongest
LRCH2-specific mechanistic study in the seeded set is PMID:32203420. Its cached
record is abstract-only and describes a family-wide analysis of Rho regulators
[PMID:32203420, “Through a family-wide characterization of substrate specificities,
interactomes and localization, we reveal at the systems level how RhoGEFs and
RhoGAPs contextualize and spatiotemporally control Rho signalling.”]. Inspection
of the publisher-hosted article PDF confirms that expressed LRCH2 recruits DOCK8
to the cell periphery, that LRCH2 leucine-rich repeats mediate the interaction,
and that an LRCH2 CH-domain fragment has cytochalasin-sensitive actin association.
Those experiments used expressed constructs in MDCK and HEK293T cells. They do not
show direct actin binding by purified LRCH2, DOCK8 GEF regulation, an endogenous
stable complex, or a physiological cellular consequence.

The other seeded LRCH2-DOCK8 annotations come from interaction maps. BioPlex 2.0
is explicitly an affinity-purification mass-spectrometry resource
[PMID:28514442, “Here we present BioPlex 2.0 (Biophysical Interactions of
ORFeome-derived complexes), which uses robust affinity purification-mass
spectrometry methodology to elucidate protein interaction networks and co-complexes
nucleated by more than 25% of protein-coding genes from the human genome, and
constitutes, to our knowledge, the largest such network so far.”]. BioPlex 3.0
likewise generated cell-line-specific AP-MS networks [PMID:33961781, “Through
affinity-purification mass spectrometry, we have created two proteome-scale,
cell-line-specific interaction networks.”]. PMID:24255178 is abstract-only and
does not expose the LRCH2-DOCK8 pair in its cached narrative. These datasets
corroborate co-association but cannot establish direct binding, GEF inhibition,
immune-cell function, or one constitutive LRCH2-DOCK8 complex.

## Paralogs, species, and CH-domain boundaries

LRCH paralogs are functionally distinct. LRCH1 restricts DOCK8 GEF activity by
competing with Cdc42 for its catalytic DHR-2 domain [PMID:28028151, “Next, we identified that LRCH1 competes with Cdc42 for binding to the catalytic DHR-2 domain of DOCK8 and restricts the GEF activity of DOCK8.”]. Functions reported for other
LRCH paralogs must not be assigned to LRCH2. PMID:32203420 supports a physical and
localization relationship between LRCH2 and DOCK8, but not the LRCH1 inhibitory
mechanism.

The evolutionary study identifies four human proteins that combine LRR and CH
domains [PMID:20805893, “In human, only four highly-related proteins (hLRCH1-4)
simultaneously harbor these two motifs.”]. Its functional experiments concern the
single Drosophila dLRCH, which stabilizes the cortex during cell division
[PMID:20805893, “Taking advantage of the existence of a single LRCH gene in flies,
dLRCH, we explored its function in cultured cells, and show that dLRCH act to
stabilize the cell cortex during cell division.”]. Fly cortical-blebbing,
spindle-positioning, fertility, stress, and Moesin findings are family context,
not direct human LRCH2 evidence. A CH domain is compatible with an actin-associated
role, but domain presence alone does not prove direct F-actin binding.

## Human disease and expression boundaries

PMID:35351988 reported a hemizygous LRCH2 p.Lys258Glu substitution in a single
family [PMID:35351988, “In Family I, the unique missense mutation (p.Lys258Glu)
was found in the LRCH2 gene inherited in an X-linked manner. p.Lys258Glu occurs
in the evolutionarily invariant site of the leucine-rich repeat domain of LRCH2.”].
The same study reported LRCH2 expression in Schwann-lineage cells and relative
predominance over its paralogs in developing cerebellar cortex
[PMID:35351988, “The LRCH2 gene for Family I patients (in which congenital
cerebellar hypoplasia was associated with demyelinating polyneuropathy) is
expressed in Schwann and precursor Schwann cells and predominantly over its
paralogous genes in the developing cerebellar cortex.”]. This is candidate-gene
evidence based on one family, conservation, and expression analysis, without direct
variant functional validation. It does not establish LRCH2 as a definitive disease
gene or reveal its normal molecular activity.

## Isoforms and open questions

The reviewed UniProt record lists two splice isoforms, Q5VUJ6-1 and Q5VUJ6-2.
The four seeded DOCK8 rows are assigned to canonical LRCH2 and do not demonstrate
an isoform-specific mechanism. UniProt/IntAct separately lists an isoform-2 contact
with TEX11 isoform 3, but this is outside the seeded GOA set and no functional
consequence was established here.

Key open questions are whether endogenous LRCH2 directly binds actin, whether its
DOCK8 interaction changes nucleotide-exchange activity or localization in a native
cell type, whether DOCK6/7 interactions occur physiologically, and whether the two
endogenous LRCH2 isoforms differ in tissue distribution or partner specificity.
