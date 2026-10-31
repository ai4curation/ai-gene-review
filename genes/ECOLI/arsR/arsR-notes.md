# arsR (P37309, b3501) notes

## Provenance of research

- `just deep-research ECOLI arsR --provider falcon` was attempted once on
  2026-10-19 and failed (recipe exited with code 1; falcon is currently failing
  with an Edison HTTP 403 auth error). It was not retried and no
  `-deep-research-*.md` file was created. This review is grounded in the
  UniProt record, the GOA rows and primary literature cached in `publications/`
  (found with PubMed E-utilities searches for E. coli ArsR).
- All cached papers except PMID:41562852 and PMID:27917165 are abstract-only.

## Identity

- 117 aa ArsR/SmtB-family (HTH_ARSR, PF01022, PS50987) winged-helix protein,
  first gene of the chromosomal arsRBC operon at ~78 min [file:ECOLI/arsR/arsR-uniprot.txt].
- UniProt function (by similarity): "Transcriptional repressor for the arsEFG operon"
  and "The repressive effect of ArsE is alleviated by oxyions of +III oxidation
  state of arsenic, antimony, and bismuth" [file:ECOLI/arsR/arsR-uniprot.txt].
- Sequence (UniProt SQ) contains the motif ELCVCDLC with Cys32, Cys34 and Cys37,
  the same positions identified as the As(III)-binding thiolates in the
  plasmid R773 ArsR (see below). Other cysteines: Cys91, Cys108, Cys116.

## Operon and physiology

- Chromosomal ars operon identified by arsenite-inducible lacZ fusion; three
  cistrons arsR, arsB, arsC; mutants "approximately 10- to 100-fold more
  sensitive to sodium arsenate and arsenite exposure than wild-type E. coli"
  [PMID:7721697 "we have identified an Escherichia coli operon whose expression is induced by cellular exposure to sodium arsenite"].
- luxAB fusions: "the operon was rapidly induced by sodium arsenite and
  negatively regulated by the trans-acting arsR gene product"; transcribed as a
  ~2100 nt mRNA [PMID:8764681].

## Biochemistry of ArsR

- Purified ArsR binds the chromosomal ars promoter (gel shift); DNase I footprint
  "spans 33 nucleotides in the promoter region, including the putative -35
  promoter element"; blaM fusions show "ArsR is a trans-acting repressor that
  regulates expression of the chromosomal ars operon"; chromosomal and R773
  repressors cross-regulate each other's promoters [PMID:8576202].
- Homodimer: "dimers retained the ability to bind to the ars promoter and to
  respond to inducer, whereas monomeric ArsRs did neither"; an ~80-residue core
  suffices for "dimerization, repression, and metal recognition" [PMID:9188467].
- Metal-sensing mechanism (R773 plasmid ArsR, a close homologue; the
  chromosomal ArsR was shown to be functionally interchangeable at the promoter
  level in PMID:8576202): As(III) is bound as AsS3 by Cys32, Cys34, Cys37;
  "binding to only two, the Cys-32 and Cys-34 thiolates, is required to produce
  the conformational change that results in release of the repressor from the
  DNA and induction" [PMID:8621591]. Applying this to the K-12 protein is an
  inference from the conserved cysteine motif, not a direct K-12 measurement.

## Broader regulation (preliminary)

- Shotgun proteomics of AW3110 (deltaarsRBC) +/- arsR complementation suggests ArsR
  influences proteins beyond the ars operon and proposes an activator role
  [PMID:41562852 "These findings challenge the classical view of ArsR as a repressor"].
  This is indirect (protein abundance, no binding sites shown); not used for GO.

## Synthetic biology use

- E. coli ArsR / Pars is widely used in arsenite whole-cell biosensors; compared
  with C. violaceum ArsR, the E. coli system shows weaker repression
  [PMID:27917165]. Low relevance for function.

## Annotation decisions (summary)

- MF: DNA-binding TF activity (IEA) and DNA binding (IDA) are correct but general;
  refine to GO:0141096 ligand-modulated transcription repressor activity and
  GO:0000976 transcription cis-regulatory region binding respectively.
- BP: GO:0006355 (IBA/IEA/IDA) and GO:0006351 (EXP) refined to GO:0045892
  negative regulation of DNA-templated transcription. ArsR does not carry out
  transcription; GO:0006351 is not appropriate even with acts_upstream_of_or_within.
- BP: GO:0046685 response to arsenic-containing substance accepted.

## PGAP

- PGAP names WP_000008957.1 from BlastRule NBR009015 ("As(III)-sensing
  metalloregulatory transcriptional repressor ArsR"), which carries no GO;
  matched NF007528/NF033788/NF013209 carry GO:0003700 and GO:0006355 but PGAP
  passes GO only from the naming model, so the protein has no PGAP GO. This is a
  recall failure for at least GO:0003700 and GO:0006355 (both true, though general).
