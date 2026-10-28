# merA (Q3SJ73, Tbd_1341), Thiobacillus denitrificans ATCC 25259: notes

## Identity

- UniProtKB Q3SJ73 (Q3SJ73_THIDA), TrEMBL, PE 3 (inferred from homology), 541 aa,
  ordered locus Tbd_1341, reference proteome UP000008291.
- Name, EC 1.16.1.1 and the function text come from the PIRSF000350 (Mercury_reductase_MerA)
  rule and ARBA; there is no experimental characterisation of this protein.
- Family: PANTHER PTHR43014:SF2 (MERCURIC REDUCTASE); NCBIfam TIGR02053 MerA; InterPro IPR021179.

## Genomic context

The genome paper places Tbd_1341 as the last gene of a merRTPA cluster inside a larger
metal-resistance island: [PMID:16452431 "A second large gene cluster (encompassing genes on both the
forward and reverse strands) encodes proteins primarily associated with metal resistance (Tbd1324-Tbd1341)."]
and [PMID:16452431 "a Hg 2+ resistance system, merRTPA (Tbd1338-Tbd1341)"]. So Tbd_1341 is
the merA of a canonical MerR-regulated transport-plus-reductase operon (MerT, MerP uptake), as described
for mer loci in general: [PMID:12829275 "Loci conferring HgR in Gram-positive or Gram-negative bacteria
typically have at minimum a mercuric reductase enzyme (MerA) that reduces reactive ionic Hg(II) to volatile,
relatively inert, monoatomic Hg(0) vapor and a membrane-bound protein (MerT) for uptake of Hg(II) arranged
in an operon under control of MerR"].

## Sequence analysis

`merA-bioinformatics/RESULTS.md`: 61.2% identity to Tn501 MerA (P00392) over 539 aligned positions.
All three cysteine sets align: NmerA GMTCDHC (C13/C16), redox-active disulfide CVNVGC (C117/C122)
and the MerA-specific C-terminal pair (C538/C539). The C-terminal pair is the feature that separates MerA
from other class-I pyridine nucleotide-disulfide oxidoreductases, which mercurials inhibit:
[PMID:1531297 "the presence of these two moieties is not sufficient for catalytic Hg(II) reduction, as other
enzyme family members are potently inhibited by mercurials"] and [PMID:1531297 "both merA mutations result in a
total disruption of the Hg(II) detoxification pathway in vivo"]. The N-terminal NmerA domain is a
Hg(II) acquisition/delivery domain in Tn501: [PMID:16114877 "we show Tn501 NmerA to be a stable, soluble
protein that binds 1 Hg(2+)/domain and delivers it to the catalytic core at kinetically competent rates"].

## Annotation calls (summary)

- GO:0016152 mercury (II) reductase (NADP+) activity: ACCEPT (core).
- GO:0045340 mercury ion binding: ACCEPT (HMA domain plus C-terminal pair).
- GO:0050660 FAD binding, GO:0050661 NADP binding: ACCEPT / KEEP_AS_NON_CORE (cofactor and co-substrate).
- GO:0050787 detoxification of mercury ion: ACCEPT (mer operon context + conserved catalytic set).
- GO:0016491 oxidoreductase activity, GO:0046872 metal ion binding: MODIFY to the specific terms already present.
- GO:0003955 NAD(P)H dehydrogenase (quinone) activity: REMOVE. TreeGrafter propagation from the family-level
  PAINT node PTN002453100 (PTHR43014), whose only seed for this term is M. tuberculosis LpdA (P9WHH7), a
  quinone reductase. No quinone reductase activity has been reported for MerA proteins in the papers read here.
  Recorded as a source defect against GO_CENTRAL (PAINT node placement).
- GO:0016668 oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor: REMOVE. The donor/acceptor
  pairing is that of lipoamide dehydrogenase/glutathione reductase relatives; in MerA the cysteines are part of the enzyme,
  the substrate is Hg(II). GO:0016152 is under GO:0016723 (acting on metal ions, NAD or NADP as acceptor),
  not under GO:0016668 (OLS, 2026-10-28). Source defect against the family-wide PROSITE/InterPro IPR012999 mapping.

No `NEW` cytoplasm row is added: there is no localisation evidence for this protein beyond the
absence of signal/TM features and analogy with Tn501. Cytoplasm is used only in core_functions context text.

## CMMMech record check (data/records/metacinnabar.yaml)

CMMMech uses Q3SJ73 as a representative protein example for the MerA node of a T. thioparus metacinnabar
dissolution and Hg(0) volatilisation graph.

- **Organism mismatch (acknowledged by the record).** The experiments are on *T. thioparus* ATCC 8158, not
  *T. denitrificans*. The paper only amplified a 285-bp merA fragment: [PMID:26157421 "BLAST analysis of the merA
  fragment nucleotide sequence revealed a 98% sequence similarity to T. thioparus DSM 505 and 85% similarity to
  Thiobacillus denitrificans ATCC 25259, both containing putative mercuric reductase genes."] Q3SJ73 is a reasonable
  proxy at genus level. A UniProt REST query on 2026-10-28 (EC 1.16.1.1 / "mercuric reductase" in taxon 931,
  *T. thioparus*) returned no entry, so no closer UniProt representative was found. The paper also notes that
  Hg(II) reduction need not be MerA-dependent: [PMID:26157421 "Although T. thioparus may also have other strategies
  or proteins capable of Hg2+ reduction, PCR amplification using mer-specific primers and sequencing confirmed that
  T. thioparus possesses the merA gene."]
- **functional_role is stronger than the evidence.** "representative of the Thiobacillus mer operon that reduces
  solubilized Hg(II) to volatile elemental Hg(0) following metacinnabar dissolution" reads as an established
  mechanism. Neither organism has a merA mutant, expression or activity measurement, and Q3SJ73 itself is
  uncharacterised (PE 3). The defensible claim is "predicted mercuric reductase (homology, conserved catalytic
  cysteines, mer operon context); its involvement in Hg(0) production in the metacinnabar experiments is untested".
  The record's evidence explanation (supports: partial) already says this. Only functional_role overstates it.
- **Locus tag error.** functional_role gives "merA / B9G62_10060". UniProt gives OrderedLocusNames Tbd_1341
  (EMBL AAZ97294.1, CP000116), and the genome paper uses Tbd1341. A UniProt REST query for B9G62_10060 returned
  nothing on 2026-10-28. The locus tag should be Tbd_1341 (RefSeq protein WP_011311853.1). B9G62 may be
  a locus prefix from another assembly; I could not verify it.
- EC 1.16.1.1, the InterPro and Pfam lists, the taxon (NCBITaxon:292415) and the proteome (UP000008291) match the UniProt record.
- The causal-graph node text "NADPH-dependent flavoprotein mercuric reductase reducing cytoplasmic Hg(II)"
  is correct for the MerA family (Tn501) and is predicted for Q3SJ73.
