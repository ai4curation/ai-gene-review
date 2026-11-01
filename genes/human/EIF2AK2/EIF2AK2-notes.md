# EIF2AK2 (PKR) curation notes

UniProt: P19525 (E2AK2_HUMAN), 551 aa. HGNC symbol EIF2AK2; synonyms PKR, PRKR, p68 kinase.

Deep research was attempted with `just deep-research human EIF2AK2 --provider perplexity`; no
provider was available in this environment (`ERROR - Provider 'perplexity' not available.
Available: claude_code`). These notes are therefore hand-written from the cached UniProt record
and the cached publications, with provenance for every assertion.

## Domain architecture and activation

Two N-terminal dsRNA-binding domains (DRBM 1, residues 9-77; DRBM 2, residues 100-167) and a
C-terminal protein kinase domain (267-538) with the proton acceptor at Asp414 and ATP-binding
residues 273-281/296 [file:human/EIF2AK2/EIF2AK2-uniprot.txt "Contains 2 dsRNA-binding domain
(DRBM) (PubMed:9736623). The N-terminus contains the catalytic domain dimerization. The
C-terminus binds EIF2S1/EIF2-alpha"]. The dsRNA-binding region was mapped to the N-terminal half
by deletion analysis, with two short arginine/lysine-rich motifs required for binding
[PMID:1351683 "Deletions in either of two 12-amino-acid-long and arginine- or lysine-rich regions
abrogated binding to dsRNA."].

PKR is made as a latent kinase and is switched on by dsRNA-driven dimerization and activation-loop
autophosphorylation [file:human/EIF2AK2/EIF2AK2-uniprot.txt "Initially produced in an inactive
form and is activated by binding to viral dsRNA, which causes dimerization and
autophosphorylation in the activation loop and stimulation of function."]. Autophosphorylation
spans Ser, Thr and Tyr residues [file:human/EIF2AK2/EIF2AK2-uniprot.txt "Autophosphorylated on
several Ser, Thr and Tyr residues."], and site-specific tyrosine autophosphorylation (Y101, Y162,
Y293) is itself required for efficient activation [PMID:16373505 "Site-specific tyrosine
phosphorylation is essential for efficient dsRNA-binding, dimerization, kinase activation and
eIF2alpha phosphorylation of PKR."]. Crystal structures of the isolated kinase domain show a
back-to-back dimer plus a front-to-front interface formed by activation-segment exchange, giving a
mechanism for *trans* autophosphorylation [PMID:31246429 "The kinase protomers interact via the
known back-to-back interface as well as a front-to-front interface that is formed by exchange of
activation segments."]. PKR is an interferon-stimulated gene [file:human/EIF2AK2/EIF2AK2-uniprot.txt
"By type I interferons."].

## Core activity: eIF2alpha Ser51 kinase

The founding characterisation already established the two defining properties — dsRNA binding and
eIF2alpha phosphorylation leading to initiation block [PMID:1695551 "On activation by dsRNA in the
presence of ATP, the kinase becomes autophosphorylated and can catalyze the phosphorylation of the
alpha subunit of eIF2, which leads to an inhibition of the initiation of protein synthesis."], and
the cloned cDNA encodes a canonical Ser/Thr kinase catalytic domain [PMID:1695551 "the catalytic
domain characteristic of serine/threonine kinases"].

Substrate recognition is structurally defined: eIF2alpha docks on the C-terminal catalytic lobe
while dimerization is mediated by the N-terminal lobe, and binding locally unfolds the Ser51
acceptor site so it reaches the catalytic cleft [PMID:16179258 "The structures reveal that
eIF2alpha binds to the C-terminal catalytic lobe while catalytic-domain dimerization is mediated
by the N-terminal lobe."]. UniProt records the same interaction and its consequence
[file:human/EIF2AK2/EIF2AK2-uniprot.txt "Interacts with EIF2S1/EIF-2ALPHA; this interaction
induces a conformational change in EIF2S1 and its phosphorylation by EIF2AK2"], and the
eIF2S1-binding region is annotated at residues 379-496.

PKR is one of the four human eIF2alpha kinases and is placed by UniProt in the GCN2 subfamily
[file:human/EIF2AK2/EIF2AK2-uniprot.txt "Belongs to the protein kinase superfamily. Ser/Thr
protein kinase family. GCN2 subfamily."].

## Antiviral role

The UniProt curated summary ties the kinase activity directly to the integrated stress response
and to a broad antiviral range [file:human/EIF2AK2/EIF2AK2-uniprot.txt "Inhibits viral
replication via the integrated stress response (ISR): EIF2S1/eIF-2-alpha phosphorylation in
response to viral infection converts EIF2S1/eIF-2-alpha in a global protein synthesis inhibitor,
resulting to a shutdown of cellular and viral protein synthesis, while concomitantly initiating
the preferential translation of ISR-specific mRNAs, such as the transcriptional activator ATF4"].

HCV is the best-documented case in the cached literature. PKR is activated by HCV infection, and
knockdown raises viral titre ~10-fold while transient PKR expression suppresses replication in a
kinase-dependent manner [PMID:19189853 "Compared to a control cell HCV replication was
significantly elevated in a PKR-knockdown cell, giving rise to a 10-fold higher viral titer, and
was less sensitive to IFNalpha treatment."]. An independent knockdown study reaches the same
conclusion but shows PKR is not strictly required for the antiviral effect of high-dose IFN-alpha
[PMID:19840259 "Although the extent of suppression was significantly lower in stable PKR knockdown
than control cells using a low concentration (2.5-5 U/ml) of IFN-alpha, even 10 U/ml IFN-alpha
suppressed the replication of subgenomic replicon by >98% in both cells."].

PKR also amplifies IFN-beta induction, and the mechanism is translational rather than a separate
adapter activity: eIF2alpha phosphorylation lowers IkB-alpha protein despite higher mRNA, and
cycloheximide rescues IFN-beta induction after PKR knockdown [PMID:22948139 "we observed increased
mRNA but decreased protein levels for the inhibitor of NF-kB signaling, IkB-a, that correlated
with PKR activation and eIF-2a phosphorylation"], [PMID:22948139 "These results suggest that an
eIF-2a-dependent translation inhibition mechanism is sufficient to explain the PKR-mediated
amplification of IPS-1-dependent IFN-b induction by foreign RNA."]. This matters for curation: the
NF-kB and interferon-induction phenotypes are downstream of the one catalytic activity.

A second antiviral output is phosphorylation of the NFAR/ILF3 proteins on Thr188 and Thr315, which
retains them on ribosomes and impedes viral replication [PMID:21123651 "Activation of the
dsRNA-activated protein kinase PKR by viral RNA enabled phosphorylation of NFAR1 and NFAR2 on Thr
188 and Thr 315"].

Viruses counter PKR at every level: HCV E2 contains a PKR/eIF2alpha phosphorylation-site mimic and
inhibits the kinase [PMID:10390359 "E2 inhibited the kinase activity of PKR and blocked its
inhibitory effect on protein synthesis and cell growth."]; the same pseudosubstrate also inhibits
PERK [PMID:12610133 "Here we report the inhibition of a second eIF2alpha kinase by E2, and these
results are consistent with a pseudosubstrate mechanism of inhibition of eIF2alpha kinases."].
UniProt lists vaccinia K3L and E3, HSV-1 US11, HCMV TRS1, HHV-8 v-IRF2 and bunyavirus NSs among
the inhibitors.

## Non-eIF2alpha substrates and signalling outputs

All of these rest on the same kinase activity acting on a different substrate; none is a separate
molecular function.

- **MKK6/MAP2K6 (p38 pathway).** MKK6, but not MKK3 or MKK4, gains affinity for PKR after
  poly(rI:rC) and is efficiently phosphorylated by PKR in vitro [PMID:15229216 "In vitro kinase
  assays revealed that MKK6 was efficiently phosphorylated by PKR, and this could be inhibited by
  2-aminopurine."]. The output is p38 MAPK activation [PMID:15229216 "Our results indicate that the
  interaction of MKK6 and PKR provides a mechanism for regulating p38 MAPK activation in response
  to dsRNA stimulation."].
- **TRAF2/5/6 and NF-kB.** PKR carries two TRAF-interacting motifs in its kinase domain, the
  interaction is dimerization-dependent, and NF-kB activation by PKR fails in TRAF2/TRAF5-deficient
  cells [PMID:15121867 "we show that the binding between PKR and TRAFs is functionally relevant, as
  observed by the absence of NF-kappa B activity upon PKR expression in cells genetically deficient
  in TRAF2 and TRAF5 or after expression of TRAF dominant negative molecules."].
- **PP2A B56alpha/PPP2R5A.** PKR phosphorylates B56alpha, which raises PP2A holoenzyme activity
  [PMID:10866685 "An in vitro dephosphorylation assay showed that when B56alpha was phosphorylated
  by PKR, the activity of PP2A trimeric holoenzyme was increased."]. PKR is the kinase here, not a
  phosphatase regulatory subunit — relevant to the GO:0019888 row below.
- **p53 via RAX/PACT.** PKR activity is required for RAX/PACT-driven p53-dependent G1 arrest
  [PMID:22214662 "co-expression of p53, RAX/PACT and the dominantnegative PKR(K296R) mutant
  inhibits RAX/PACT-induced, p53-dependent G1 growth arrest"].
- **CDK1 Tyr-4.** UniProt records tyrosine-kinase activity on CDK1 after DNA damage
  [file:human/EIF2AK2/EIF2AK2-uniprot.txt "also has tyrosine-protein kinase activity and
  phosphorylates CDK1 at 'Tyr-4' upon DNA damage, facilitating its ubiquitination and proteasomal
  degradation (PubMed:20395957)"].
- **GSK-3beta/tau.** PKR inhibitors or siRNA attenuate GSK-3beta activation and tau
  phosphorylation in neuroblastoma cells exposed to tunicamycin or Abeta [PMID:21029237 "In SH-SY5Y
  cell cultures, tunicamycin and Ab(1-42) activate PKR, GSK-3b and induce tau phosphorylation and
  all these processes are attenuated by PKR inhibitors or PKR siRNA."].
- **Osteoblast differentiation.** A kinase-dead K296R mutant in MC3T3-E1 osteoblasts grew faster,
  lost ALP activity and failed to form bone nodules [PMID:16216244 "The PKR-K/R mutant cells
  exhibited up-regulated cell growth and had low alkaline phosphatase (ALP) activity. The PKR-K/R
  mutant cells were not able to form bone nodules in vitro."]. This is the basis of the human
  GO:0033689 IMP row, but the cells are mouse.

## Negative regulators

NPM1 binds PKR and inhibits its activation, and is itself a PKR substrate [PMID:12882984 "Kinase
assays demonstrated that recombinant NPM inhibited PKR activation in a dose-dependent manner. In
addition, purified recombinant NPM was phosphorylated by activated PKR."]. NCK1 binds the inactive
kinase and limits its activation by dsRNA [PMID:18835251 "Interestingly, we found that Nck-1
interacts with the inactive form of PKR, independently of its Src homology domains."]. MPT
synthase (MOCS2B) and the ATAC subunit MBIP together suppress *latent* PKR autophosphorylation, so
that eIF2B is not sequestered and initiation proceeds [PMID:26705305 "MPT synthase and ATAC
directly interacted with PKR and suppressed latent autophosphorylation of PKR and its downstream
phosphorylation of JNK and eukaryotic initiation factor 2a (eIF2a)."]. p58IPK/DNAJC3 inhibits PKR
and PERK, and the same study shows it also inhibits GCN2 [PMID:25329545 "The protein p58IPK ... is
known to inhibit the eIF2a kinases PKR (dsRNA-dependent protein kinase/eIF2a kinase 2) and PERK
and hence prevent or delay eIF2a phosphorylation"].

## Localisation

UniProt records cytoplasm, nucleus and perinuclear cytoplasm, with no membrane location
[file:human/EIF2AK2/EIF2AK2-uniprot.txt "Cytoplasm, perinuclear region"]. Nuclear PKR is not an
artefact: in acute leukaemia cell lines nuclear p-T451 PKR exists in several post-translationally
modified forms and is catalytically active and stress-responsive [PMID:21072047 "Biochemical
analysis demonstrated that nuclear PKR is an active kinase that can respond to stress."], and
nuclear localisation is elevated in several malignancies
[file:human/EIF2AK2/EIF2AK2-uniprot.txt "Nuclear localization is elevated in acute leukemia,
myelodysplastic syndrome (MDS), melanoma, breast, colon, prostate and lung cancer patient samples
or cell lines as well as neurocytes from advanced Creutzfeldt- Jakob disease patients."]. The
assays behind these rows (immunofluorescence, nuclear fractionation) do not resolve a
sub-nuclear compartment, so `nucleus` is as precise as the evidence supports.

The single `GO:0016020 membrane` HDA row comes from an NK-cell membrane proteome whose authors
state that most of their 1843 identifications are not integral membrane proteins
[PMID:19946888 "The remaining species were largely involved in cellular processes and molecular
functions that could be predicted to be transiently associated with membranes."]. PKR has no
transmembrane segment in UniProt. Treated as an over-annotation.

## Inflammasome: a disputed claim

PKR was reported to be broadly required for inflammasome activation, interacting with NLRP3,
NLRP1, NLRC4 and AIM2 [PMID:22801494 "PKR inactivation by genetic deletion or pharmacological
inhibition severely impaired inflammasome activation in response to double-stranded RNA, ATP,
monosodium urate, adjuvant aluminium, rotenone, live Escherichia coli, anthrax lethal toxin, DNA
transfection and Salmonella typhimurium infection."]. This did not replicate: using macrophages
from two independent PKR-deficient mouse strains, PKR was needed for iNOS induction but
dispensable for caspase-1 activation and IL-1beta secretion [PMID:23401008 "However, PKR was
dispensable for caspase-1 activation, processing of pro-IL-1b/IL-18 and secretion of IL-1b induced
by stimuli that trigger the activation of NLRP3, NLRC4 and AIM2."]. The neutral GO term
(`regulation of NLRP3 inflammasome complex assembly`) is retained as non-core with the dispute
recorded; a directional term would not be defensible.

## Basis of the mouse ISS/IEA rows

The ISS rows transferred from mouse Eif2ak2 (UniProtKB:Q03963) trace to two experimental mouse
papers (checked in QuickGO): cytokine/chemokine production, stress-activated MAPK and
non-canonical NF-kB rows come from PMID:20038207, where PKR-deficient mice infected with RSV had
"significantly lower levels of several innate inflammatory cytokines and chemokines"
[PMID:20038207 "Our data showed that bronchoalveolar lavage (BAL) fluid from infected PKR(-/-)
mice had significantly lower levels of several innate inflammatory cytokines and chemokines."];
the three haematopoietic rows come from PMID:23403623. None of these is a core function of the
protein, but none is an unsupported electronic guess either.

## Disease

De novo EIF2AK2 variants cause a dominant leukoencephalopathy with developmental delay and
episodic neurologic regression (LEUDEN, MIM 618877) [PMID:32197074 "De novo EIF2AK1 and EIF2AK2
Variants Are Associated with Developmental Delay, Leukoencephalopathy, and Neurologic
Decompensation"], and other variants cause dystonia 33 (DYT33, MIM 619687)
[file:human/EIF2AK2/EIF2AK2-uniprot.txt "Dystonia 33 (DYT33) [MIM:619687]"]. Both phenotypes are
consistent with dysregulated ISR signalling in the CNS and parallel the EIF2AK1/EIF2B
leukoencephalopathies in the same project cohort.

## Curation decisions taken

- Core: dsRNA binding (GO:0003725) and eIF2alpha kinase activity (GO:0004694) in the cytosol,
  driving negative regulation of cytoplasmic translation and defence against viruses.
- Generic kinase rows (`protein kinase activity`, `kinase activity`) are MODIFYed to the specific
  activity the cited paper assayed: GO:0004694 where the substrate is eIF2alpha, GO:0004674 where
  it is another Ser/Thr substrate or autophosphorylation.
- `GO:0019888 protein phosphatase regulator activity` (TAS, PMID:10866685) is a lateral
  mis-classification: PKR phosphorylates B56alpha, so the molecular function is kinase activity and
  the PP2A effect is a downstream consequence. MODIFY to GO:0004674.
- `GO:0034198 cellular response to amino acid starvation` is marked over-annotated. The cited
  paper's stresses are ER stress, hypothermia and prolonged culture, and its amino-acid-starvation
  sensor is GCN2, not PKR [PMID:25329545 "whereas GCN2 is the kinase that is activated following
  cold-shock/hypothermic culturing of mammalian cells, PERK and GCN2 have overlapping functions"].
  The companion row is an unvetted ARBA rule.
- The 59 bare `GO:0005515 protein binding` IPI rows are REMOVEd per the repository protein-binding
  policy, except the eIF2alpha (P05198) rows, which are MODIFYed to
  `GO:0031369 translation initiation factor binding`, and the `GO:0042802 identical protein
  binding` row, MODIFYed to `GO:0042803 protein homodimerization activity`. Removal does not say
  the interactions are false.
