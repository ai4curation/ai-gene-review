# SECISBP2 (Q96T21) review notes

Gene: SECISBP2 (SBP2), HGNC:30972, human, UniProt Q96T21 (854 aa). Also known as SBP2.

## Core biology

SECISBP2 = Selenocysteine insertion sequence-binding protein 2. Essential trans-acting
factor for co-translational selenocysteine (Sec) incorporation into selenoproteins.

- UniProt FUNCTION: "mRNA-binding protein that binds to the SECIS (selenocysteine
  insertion sequence) element present in the 3'-UTR of mRNAs encoding selenoproteins and
  facilitates the incorporation of the rare amino acid selenocysteine"
  [file:human/SECISBP2/SECISBP2-uniprot.txt].
- Mechanism (from same FUNCTION block): "SECISBP2 (1) specifically binds the SECIS
  sequence once the 80S ribosome encounters an in-frame UGA codon and (2) contacts the
  RPS27A/eS31 of the 40S ribosome before ribosome stalling. (3) GTP-bound EEFSEC then
  delivers selenocysteinyl-tRNA(Sec) to the 80S ribosome ... (4) After GTP hydrolysis,
  EEFSEC dissociates ..., selenocysteinyl-tRNA(Sec) accommodates, and peptide bond
  synthesis and selenoprotein elongation occur" [file:human/SECISBP2/SECISBP2-uniprot.txt].
- Domain architecture: L7Ae/L30-family RNA-binding domain. UniProt DR lines list
  Pfam PF01248 Ribosomal_L7Ae; InterPro IPR040051 SECISBP2; SUPFAM SSF55315 L30e-like.
  The functional C-terminal half (residues ~409-854) contains a Sec-insertion domain (SID)
  and an RNA-binding domain (RBD) [PMID:35709277, "the functional C-terminal half of human
  SBP2 (residues 409–854), which is composed of a Sec-insertion domain (SID) and an
  RNA-binding domain (RBD)"].

## Structural / functional evidence

PMID:35709277 (Hilal et al., Science 2022; full text available) — cryo-EM of the mammalian
"selenosome" decoding the Sec UGA codon. Directly establishes SECIS binding and the role in
Sec incorporation:
- "A complex between the noncoding Sec-insertion sequence (SECIS), SECIS-binding protein 2
  (SBP2), and 40S ribosomal subunit enables Sec-specific elongation factor eEFSec to
  deliver Sec."
- "the RBD of SBP2 adopts an L7Ae protein fold and binds to the conserved kink-turn motif
  of the SECIS."
- "The RBD of SBP2 binds to the SECIS base, whereas the N-terminal part of the SID latches
  onto the 40S through contacts with the rRNA and eS31."
- Ribosome contact: "The subsequent segment (residues 441–446) forms a parallel β-strand
  that leans against the C terminus of eS31" (eS31 = RPS27A). This supports
  ribonucleoprotein complex binding (40S/eS31) and RNP-complex membership (selenosome).
- Disease variants rationalized structurally: E679D, C691R.

PMID:17332014 (Cléry et al., NAR 2007; full text available) — SELEX + footprinting defining
SBP2 RNA-binding specificity for SECIS/K-turn motifs. Supports mRNA 3'-UTR (SECIS) binding:
- "By binding to SECIS elements located in the 3'-UTR of selenoprotein mRNAs, the protein
  SBP2 plays a key role in the assembly of the selenocysteine incorporation machinery."
- "SBP2 contains an L7Ae/L30 RNA-binding domain similar to that of protein 15.5K/Snu13p,
  which binds K-turn motifs."

PMID:16962588 (Lu et al., FEBS Lett 2006; abstract only) — SelK characterization; shows SBP2
binds the SelK SECIS: "human SBP2 bound to the SelK SECIS element through the conserved
non-Watson-Crick base pair quartet but not the AAT motif." SelK SECIS is in the 3'UTR:
"selenium incorporation into SelK was dependent on the 3'UTR of SelK mRNA." Supports
GO:0003730 mRNA 3'-UTR binding (SECIS).

PMID:22658674 (Castello et al., Cell 2012; abstract only) — mRNA interactome capture (HeLa,
UV crosslink). High-throughput identification of SBP2 as an mRNA-binding protein
(GO:0003723 RNA binding, HDA). General; corroborates RNA-binding but not SECIS-specific.

PMID:19467292 (Oliéric et al., Biochimie 2009; abstract only) — SBP2 is an intrinsically
disordered protein: "ca. 70% of the SBP2 sequence is disordered, whereas the RNA binding
domain appears to be folded and functional." This is the DisProt source (DP00420). NOTE: the
GOA GO:0003677 "DNA binding" EXP annotation cites this DisProt paper, but the paper is about
intrinsic disorder and RNA binding, NOT DNA binding. SBP2 is not a characterized DNA-binding
protein; treat GO:0003677 as over-annotation (EXP → MARK_AS_OVER_ANNOTATED, do not REMOVE).

## Localization

- Isoform 1 (full length): Nucleus. UniProt SUBCELLULAR LOCATION [Isoform 1]: Nucleus
  {ECO:0000305}. NLS motif at 380-387 (FT MOTIF). Also cytoplasmic/ribosome-associated in
  the literature (acts co-translationally at the ribosome; shuttling reported).
- Isoform 2 (mtSBP2): Mitochondrion {ECO:0000269|PubMed:19004874}; contains a transit
  peptide at positions 1-15 [file:human/SECISBP2/SECISBP2-uniprot.txt]. Mitochondrial
  localization is thus isoform-2-specific (per PMID:19004874, cited by UniProt).
- HPA IDA: nucleoplasm (GO:0005654).

## Interactions (high-throughput Y2H; bare "protein binding")

UniProt INTERACTION block [file:human/SECISBP2/SECISBP2-uniprot.txt]:
- Q92567-2 FAM168A (PMID:32296183, HuRI reference interactome, Luck et al.)
- Q08379 GOLGA2 (PMID:25416956, Rolland et al. interactome)
- P42858 HTT (PMID:32814053, neurodegeneration interactome)
These are systematic binary interactome (Y2H) hits, uncharacterized functionally, no
biological role established for SBP2. GO:0005515 "protein binding" IPI is uninformative →
MARK_AS_OVER_ANNOTATED (policy: never REMOVE bare protein-binding IPI).

## Disease

THMA1 (Thyroid hormone metabolism, abnormal, 1; MIM 609698): "A disorder associated with a
reduction in type II iodothyronine deiodinase activity" [file:human/SECISBP2/SECISBP2-uniprot.txt];
caused by SECISBP2 variants (PMID:16228000 first patients incl. variant R540Q; PMID:29882503
additional patient). Multisystem selenoprotein deficiency (thyroid, growth, myopathy,
photosensitivity, azoospermia) reflects loss of translation of many selenoproteins.

## Reactome

UniProt DR: Reactome R-HSA-2408557 "Selenocysteine synthesis."

## Annotation decisions summary

- GO:0035368 SECIS binding (IDA PMID:35709277) — ACCEPT (core MF).
- GO:0001514 selenocysteine incorporation (IDA PMID:35709277) — ACCEPT (core BP).
- GO:0003730 mRNA 3'-UTR binding (IDA PMID:16962588, PMID:17332014) — ACCEPT; SECIS is in
  the 3'-UTR, so this is the same SECIS-binding role at a slightly more general MF term.
- GO:0035368 / GO:0001514 / GO:0003730 IBA/IEA duplicates — KEEP_AS_NON_CORE or ACCEPT (they
  restate the experimentally supported core; not independent evidence).
- GO:0043021 RNP complex binding (IBA) — KEEP_AS_NON_CORE (SBP2 binds 40S/eS31, supported by
  PMID:35709277).
- GO:1990904 ribonucleoprotein complex (IBA part_of) — KEEP_AS_NON_CORE (selenosome RNP).
- GO:0003723 RNA binding (HDA PMID:22658674) — KEEP_AS_NON_CORE (general parent of SECIS
  binding; high-throughput).
- GO:0005634 nucleus (IEA), GO:0005654 nucleoplasm (IDA) — KEEP_AS_NON_CORE (isoform 1
  localization; SBP2 acts at cytoplasmic ribosomes).
- GO:0005739 mitochondrion (IBA is_active_in, IEA located_in) — KEEP_AS_NON_CORE; isoform-2
  (mtSBP2)-specific per PMID:19004874, not the canonical Sec-incorporation site.
- GO:0005515 protein binding IPI ×3 — MARK_AS_OVER_ANNOTATED (uninformative Y2H).
- GO:0003677 DNA binding (EXP PMID:19467292) — MARK_AS_OVER_ANNOTATED; source paper is about
  intrinsic disorder/RNA binding, no DNA-binding function established.

## Core functions

1. SECIS-element binding (GO:0035368 SECIS binding; also GO:0003730 mRNA 3'-UTR binding) via
   its L7Ae/L30 RBD.
2. Selenocysteine incorporation / UGA recoding (GO:0001514) — assembly of the selenosome on
   the 40S ribosome to enable EEFSEC-mediated Sec-tRNA(Sec) delivery.
</content>
</invoke>
