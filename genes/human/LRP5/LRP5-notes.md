# LRP5 review notes

## Record and molecular architecture

The reviewed human product O75197 is a 1,615-residue precursor and type-I
single-pass membrane protein. UniProt places the signal peptide at residues
1-31, the extracellular region at 32-1384, the transmembrane helix at
1385-1407, and the cytoplasmic tail at 1408-1615
[file:human/LRP5/LRP5-uniprot.txt, "FT   SIGNAL          1..31"; "FT   TOPO_DOM        32..1384"; "FT   TRANSMEM        1385..1407"; "FT   TOPO_DOM        1408..1615"].
The original human cloning paper likewise reports that the osteoblast-library
cDNA "encoded a 1,615 amino acids protein designated as LR3"
[PMID:9790987]. No normal alternative products are curated in the current
reviewed UniProt record. The internally deleted product discussed below is a
tumor-associated aberrant splice product, not evidence for a normal LRP5
isoform.

## Canonical Wnt coreceptor mechanism

The strongest LRP5-specific mechanistic source is the Axin study. LRP5 alone
did not activate the canonical reporter in fibroblasts but acted synergistically
with Wnt; Wnt caused Axin membrane translocation and enhanced Axin-LRP5 binding.
The authors conclude that "the binding of Axin to LRP-5 is an important part of
the Wnt signal transduction pathway" [PMID:11336703]. This supports a
ligand-dependent coreceptor function and cytoplasmic recruitment mechanism, not
constitutive receptor signaling by wild-type LRP5.

CAPRIN2 provides an additional activation mechanism: "Caprin-2 facilitates
LRP5/6 phosphorylation by glycogen synthase kinase 3, and thus enhances the
interaction between Axin and LRP5/6" [PMID:18762581]. This paper treats LRP5
and LRP6 jointly, so it should not be used to claim an LRP5-specific complex
beyond the reported LRP5/6 binding and phosphorylation assays.

Sclerostin/SOST is a directly supported extracellular antagonist. It binds "the
extracellular domain of the Wnt coreceptors LRP5 and LRP6" and disrupts
Wnt-induced Frizzled-LRP complex formation [PMID:15908424]. APCDD1 is another
reported inhibitor that "can interact in vitro with WNT3A and LRP5"
[PMID:20393562]; this is in-vitro interaction evidence and should not imply a
constitutive complex in every tissue.

## Bone biology and variant directionality

Human LRP5 signaling dosage is strongly linked to bone mass. In human
mesenchymal stem cells, "Both hMSC-LRP5(WT) and hMSC-LRP5(T253) showed enhanced
osteoblast differentiation and inhibited adipogenesis in vitro, and the
opposite effect was observed in hMSC-LRP5(T244)" [PMID:17680723]. The same
study reports mineralized-bone formation by wild-type and activating T253 cells
after implantation. These direction-specific results are important: the
activating allele promotes osteoblast differentiation and suppresses adipocyte
differentiation, whereas the inactivating allele has the opposite effects.

Damaging human LRP5 variants are also associated with osteoporosis and abnormal
glucose metabolism, but that small patient study explicitly concludes that
"Further studies are needed to establish the role of LRP5 in glucose and lipid
metabolism" [PMID:19673927]. Common-variant studies associate selected alleles
with BMD, cholesterol, blood pressure, or calcium-intake interactions
[PMID:18721193; PMID:20146170; PMID:20630166]. These are association studies,
not evidence that lipid homeostasis, blood-pressure control, or glucose
catabolism are core biochemical functions of LRP5.

## Retinal Norrin signaling

Human genetic evidence links LRP5 to both dominant and recessive familial
exudative vitreoretinopathy (FEVR). One study identifies LRP5 as "a Wnt
coreceptor" at the EVR1 locus [PMID:15024691], while another found homozygous
R570Q, R752G, and E1367K variants in three recessive families
[PMID:15346351]. The ligand-system paper establishes that Norrin-FZD4 signaling
requires an LRP component but does not distinguish LRP5 from LRP6 in its
accessible abstract [PMID:15035989]. LRP5-specific functional support comes
from variant assays: "single missense mutations in LRP5 and FZD4 caused a
moderate level of reduction" in Norrin-dependent signaling
[PMID:17955262]. Thus retinal vascular roles are well supported, but effects
must remain allele- and assay-specific.

## Variant, construct, and assay boundaries

The internally deleted LRP5 product from hyperparathyroid tumors strongly
activated WNT3-dependent transcription and was DKK1-insensitive
[PMID:18044981]. Reactome specifies an in-frame deletion of residues 666-809
[Reactome:R-HSA-5339711]. This aberrant tumor product should not be described
as a normal isoform or generalized to wild-type receptor activity.

Candidate polycystic-liver and ADPKD-associated variants reduced canonical Wnt
reporter activation [PMID:24706814; PMID:25920554]. These sources inform variant
effects and disease context, not a core cystogenesis function. The accessible
PMID:25920554 cache does not contain the full text needed to check the seeded
endoplasmic-reticulum localization experiment.

The early LR3 transfection study reported that full-length receptor or its
ectodomain increased NIH 3T3 proliferation, while the intracellular domain did
not [PMID:9790987]. This is an ectopic assay and does not make mitogenesis a
universal output of LRP5.

BioPlex 2.0 and 3.0 are proteome-scale affinity-purification mass-spectrometry
resources [PMID:28514442; PMID:33961781]. Their LRP5-SOST rows are candidate
cell-line co-associations; targeted binding and functional evidence comes from
PMID:15908424.

## Citation hazards identified during reference review

- PMID:11029007 experimentally characterizes LRP6 in Xenopus and mentions LRP5
  only as an Arrow homolog; it does not directly establish LRP5 pathway activity.
- PMID:11433302 explicitly identifies LRP6/Arrow as the DKK1-binding receptor
  component, not LRP5.
- PMID:12121999 reports that several Wnt-FZD fusions activated TOPFlash with
  "LRP6, but not LRP5" in 293T cells. This is a negative, construct-specific
  LRP5 result, not positive pathway evidence.
- PMID:12857724 identifies a rat PC12 WNT7A-FZD5-LRP6 complex and does not assay
  LRP5 in the accessible record.
- PMID:18350154 reports that knockdown of "either LRP6, LRP5, or both proteins
  has no influence" on anthrax toxin entry in human HeLa cells. It contradicts
  a positive LRP5 toxin-transporter assignment.
- PMID:20093360 reconstitutes an FZD8-WNT3A-LRP6 complex; the experiment is not
  an LRP5 complex assay.
- PMID:21471202 demonstrates a direct sclerostin-LRP4 interaction. It is a
  paralog-specific LRP4 paper and cannot support LRP5-SOST binding.
- Reactome:R-NUL-1458902 describes Xenopus CK1gamma phosphorylation of LRP6,
  not localization or phosphorylation of human LRP5.

These explicit boundaries are based on the cached titles/abstracts or full
text, not on an inference from paper titles alone.
