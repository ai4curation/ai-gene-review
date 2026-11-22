# Sur (Q9VL32, CG5772, FBgn0028675) - manual literature review

No deep-research API was available; this summary was compiled by hand from cached
publications (publications/PMID_*.md), a PubMed search
(`(dSUR OR "sulfonylurea receptor") AND Drosophila`, 16 hits), and the UniProt record.

## Identity and family

- Sur is the single Drosophila sulfonylurea receptor, a 2223-aa ABCC-family protein with two
  ABC transmembrane domains and two nucleotide-binding domains [file:DROME/Sur/Sur-uniprot.txt
  "Belongs to the ABC transporter superfamily. ABCC family"].
- Cloned as Dsur, "highly related to the vertebrate SUR family", with a 1.7 kb insert lacking
  homology to known genes; only one Dsur gene in the genome [PMID:10506204 "Studies of the
  Drosophila genome support that only a single Dsur gene is present"].
- Local motif scan: Walker A motifs intact in both NBDs; NBD1 Walker B has D (degenerate),
  NBD2 Walker B retains the catalytic E, as in mammalian SURs
  [file:DROME/Sur/Sur-bioinformatics/RESULTS.md].

## Molecular function

- Mammalian SURx are channel-regulatory subunits: "SURx alone is electrophysiologically inert"
  and require Kir6.2 [PMID:10506204].
- Dsur alone in Xenopus oocytes: "When Dsur alone is expressed in Xenopus oocytes
  glibenclamide-sensitive potassium channel activity occurs" [PMID:10506204]. Whether this
  reflects endogenous oocyte Kir subunits or intrinsic channel activity is unresolved (abstract
  only available).
- No transported substrate has been demonstrated for Sur. A sulfonylurea-binding site in fly larval
  vesicles (glibenclamide KD 44.9 nM) was measured but not assigned to the Sur protein
  [PMID:15262279].
- The Kir partner in vivo is not established; corpora cardiaca cells co-express Sur and an inward
  rectifier ("Ir") [PMID:15372035 "CC cells express Drosophila cognates of sulphonylurea receptor
  (Sur) and potassium channel (Ir)"].

## Expression

- Embryonic dorsal vessel (heart) and tracheal system [PMID:10506204].
- Adult heart; Tinman directly regulates cardiac expression through an intronic enhancer, with
  Pannier [PMID:16882722]; Tinman/Pannier/MEF2 overexpression expands Sur expression
  [PMID:26225919 "In approximately 20% of the embryos, we observed ectopic accumulation of Hand or
  Sur transcripts"].
- Adult brain insulin-producing cells [PMID:20195385 "In situ hybridization of whole mount adult
  brains reveals IPC-specific dSur expression"] and larval corpora cardiaca [PMID:15372035].
- Expression declines with age in the heart [PMID:16882722; PMID:17574126].

## Physiology (perturbation evidence)

- Heart: knockdown reduces protection against hypoxic stress and pacing-induced failure
  [PMID:16882722 "dSUR plays a protective role against hypoxic stress and pacing-induced heart
  failure"].
- Cdc42-Tinman cardiac pathway: dSUR mRNA reduced; dSUR named as potential effector
  [PMID:21690310 "We also identified K(+) channels, encoded by dSUR and slowpoke, as potential
  effectors of the Cdc42-Tinman interaction"]. Full text (PMC3216339, read via PubMed) reports
  qPCR down-regulation of the two K+ channel genes and a structural cardiac phenotype in
  Cdc42/channel transheterozygotes (genetic interaction, not mechanism).
- Infection: dSUR RNAi increases susceptibility to flock house virus [PMID:18026101].
- Sleep: neuronal RNAi shortens early-night sleep [PMID:22105623]; head transcriptome of
  knockdowns [PMID:28676676].
- Chitin: a complete loss-of-function has normal cuticle and chitin [PMID:23441090 "cuticle
  architecture is normal and chitin amounts are not diminished in the cuticle of these animals,
  indicating that Sur is dispensable for chitin synthesis"].
