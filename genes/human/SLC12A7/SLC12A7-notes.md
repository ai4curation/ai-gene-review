# SLC12A7 (KCC4) curation notes

UniProt: Q9Y666 (S12A7_HUMAN). Protein: Solute carrier family 12 member 7 /
Electroneutral potassium-chloride cotransporter 4 (KCC4). 1083 aa, 12-TM
secondary active transporter, SLC12A / cation-chloride cotransporter (CCC)
family, K/Cl cotransporter subfamily. Gene on chr 5. Part of canonical-surfaceome
backfill batch 4 (SLC12 family).

## Core molecular function

- Electroneutral K+:Cl- cotransport (1:1 stoichiometry), activated by cell
  swelling (hypotonicity). Directly demonstrated for human KCC4 in Xenopus
  oocytes [PMID:10913127 "Both KCCs express minimal K(+)-Cl(-) cotransport under
  isotonic conditions, with significant activation by cell swelling under
  hypotonic conditions."]. Km(K+) ~17.5 mM [PMID:10913127 "K(m) values of
  approximately 25.5 and 17.5 mm for KCC1 and KCC4, respectively"].
- UniProt CATALYTIC ACTIVITY: K(+)(in) + chloride(in) = K(+)(out) + chloride(out)
  (Rhea:RHEA:72427), ECO:0000269|PubMed:10913127. GO term GO:0015379
  potassium:chloride symporter activity (verified via OLS: "K+(out) + Cl-(out) =
  K+(in) + Cl-(in)").
- Pharmacology: KCC4 less sensitive to bumetanide/furosemide than KCC1; uniquely
  sensitive to barium and trichlormethiazide; activated by NEM; inhibited by DIOA,
  DIDS; inhibited by WNK3 [PMID:21613606, UniProt ACTIVITY REGULATION].

## Structure / subunit

- Cryo-EM 2.9 A (PDB 7D99) [PMID:33310850]: homodimer with domain-swapped scissor
  helices; also forms heterodimer with SLC12A5 (KCC2). K+ and Cl- binding sites
  mapped (BINDING residues 131/132/429/432 K+; 135/429/433/434/589 Cl-). So KCC4
  is genuinely part of a protein-containing complex (obligate homodimer).

## Localization

- Plasma / cell membrane (multi-pass), direct EXP [PMID:10913127, UniProt
  SUBCELLULAR LOCATION "Cell membrane {ECO:0000269|PubMed:10913127}"].
- Apical plasma membrane IBA is a family-level (PAINT) call; KCC4's best
  characterized renal role is BASOLATERAL Cl- extrusion in proximal tubule
  (UniProt: "May be required for basolateral Cl(-) extrusion in the kidney and
  contribute to renal acidification (By similarity)"). Sub-membrane domain is
  cell-type dependent -> apical kept as non-core.

## Biological roles

- Cell volume homeostasis / regulatory volume decrease (swelling-activated).
- Renal: basolateral Cl- extrusion in proximal tubule, contributes to renal
  acidification (By similarity, UniProt).
- Inner ear: K+ recycling; KCC4-/- mice are deaf with outer/inner hair cell
  degeneration and loss of the organ of Corti; may mediate K+ uptake into
  Deiters' cells (UniProt FUNCTION, By similarity). "potassium ion import across
  plasma membrane" (GO:1990573) fits this cochlear uptake direction but KCC4's
  predominant physiological direction is efflux (K+/Cl- out) -> import kept
  non-core.

## Annotation notes

- GO:0032991 protein-containing complex, IDA, PMID:28246125: that paper is the
  ZMPSTE24/IFITM antiviral interactome; SLC12A7 is not discussed in the main
  text (likely a high-throughput AP-MS hit in Table S1). Root/uninformative CC
  term. KCC4's real complex is the homodimer (PMID:33310850). Marked
  over-annotated; homodimer captured in core_functions.in_complex.
- GO:0071333 cellular response to glucose stimulus, IEA (Ensembl ortholog of
  mouse Q9WVL3): over-propagated electronic transfer, not a core transporter
  function; marked over-annotated.
- Root/general terms entailed by the specific accepted MF GO:0015379 or the
  specific transport BPs -> TOO_GENERAL: GO:0015377 (parent MF), GO:0022857
  (root transporter activity), GO:0006811 monoatomic ion transport, GO:0055085
  transmembrane transport, GO:0006821 chloride transport.
- GO:0016020 membrane IEA -> MODIFY to GO:0005886 plasma membrane (transporter
  convention; location established by EXP).
</content>
</invoke>
