# SLC12A6 (KCC3) curation notes

UniProt: Q9UHW9 (S12A6_HUMAN). Gene: SLC12A6 / KCC3. Human, 1150 aa, multi-pass
plasma-membrane protein. Member of the SLC12A / cation-chloride cotransporter
(CCC) family, K/Cl cotransporter (KCC) subfamily (paralogs KCC1/SLC12A4,
KCC2/SLC12A5, KCC4/SLC12A7).

## Core biology

- **Molecular function: electroneutral K+:Cl- symporter (GO:0015379).** Mediates
  obligately coupled 1:1 K+ and Cl- cotransport; electroneutral; secondary active,
  driven by the K+ (and Cl-) electrochemical gradients. Catalytic reaction
  (UniProt RHEA:72427): `K(+)(in) + chloride(in) = K(+)(out) + chloride(out)`.
  Kinetics: KM(K+) 9.5 mM, KM(Cl-) 51 mM (isoform 1); KM(Rb+) 10.7 mM, KM(Cl-)
  7.3 mM [PMID:16048901]. NH4+ can substitute at the K+ site [PMID:12657561].
- **Activation by cell swelling.** All N-terminal isoforms are activated by
  hypotonic cell swelling and inactive under isotonic conditions
  [PMID:16048901 "All five NH(2)-terminal isoforms are activated by cell swelling (hypotonic conditions), with no activity under isotonic conditions."].
  Also activated by N-ethylmaleimide, inhibited by DIOA/bumetanide/furosemide
  [PMID:10600773].
- **Phospho-regulation (WNK-SPAK/OSR1).** Inhibited by phosphorylation at Thr-991
  and Thr-1048 by OXSR1/OSR1 and STK39/SPAK downstream of WNK kinases; hypotonic
  dephosphorylation activates transport [PMID:19665974; PMID:34031912]. This is
  the structural basis of the KCC3b N-terminus occluding the intracellular
  vestibule in the phospho-mimetic state [PMID:34031912].
- **Process roles the protein itself performs:** K+ and Cl- transmembrane
  transport, chloride/potassium ion homeostasis (sets [Cl-]i), and cell volume
  homeostasis / regulatory volume decrease [PMID:19665974; PMID:16048901].
- **Localization:** plasma (cell) membrane, basolateral in polarized epithelia
  (proximal tubule) [PMID:16048901, PMID:12368912, PMID:17893295]. UniProt:
  "Cell membrane ... Basolateral cell membrane". NOT apical — the family-level IBA
  apical PM annotation does not fit KCC3.
- **Structure/subunit:** homodimer with a domain-swap at the scissor helices;
  heterodimer with KCC2/SLC12A5 [PMID:33199848, PMID:34031912, PMID:33310850].
- **Interactors:** STK39/SPAK (Q9UEW8) binds and phospho-regulates KCC3
  [PMID:24655550 "interacts with K-Cl co-transporter 3 (KCC3)"; PMID:40355756];
  CKB (brain creatine kinase) binds the C-terminus [PMID:18566107]. → protein
  kinase binding (GO:0019901) is the informative MF for the STK39 IPI rows.

## Disease (necessity, not GO process participation)

Loss-of-function / truncating variants cause Andermann syndrome (ACCPN,
MIM:218000): peripheral neuropathy with agenesis of the corpus callosum
[PMID:12368912, PMID:16606917, PMID:17893295]. Dominant variants cause
Charcot-Marie-Tooth type 2II (CMT2II, MIM:620068) [PMID:27485015, PMID:31439721,
PMID:35733399]. KCC3 is required for PNS axon maintenance, but the gene product's
biochemical job is K-Cl cotransport; disease reflects loss of that activity, not
participation in a distinct "nervous system development" process (no NEW BP
proposed on necessity alone).

## Annotation-review decisions (summary)

- GO:0015379 potassium:chloride symporter activity (IBA/IDA×7/IEA/TAS×2) → all
  ACCEPT (core MF). IBA WITH/FROM includes Q9UHW9 itself = experimental grounding
  on target, expected, not circular.
- GO:0005515 protein binding (IPI ×2, interactor Q9UEW8=STK39/SPAK, a protein
  kinase) → MODIFY → GO:0019901 protein kinase binding.
- GO:0005886 plasma membrane (EXP/IDA/IEA/ISS/TAS) → ACCEPT (core location).
- GO:0016323 basolateral plasma membrane (IEA/ISS) → ACCEPT (documented polarity).
- GO:0016324 apical plasma membrane (IBA) → MARK_AS_OVER_ANNOTATED: KCC3 is
  basolateral; apical is a family-level over-propagation contradicted for KCC3.
- GO:0016020 membrane (IEA/NAS) → MODIFY → GO:0005886 plasma membrane.
- GO:0006884 cell volume homeostasis (IDA) → ACCEPT (core process).
- GO:0055064 chloride ion homeostasis (ISS) → ACCEPT; GO:0055075 potassium ion
  homeostasis (ISS) → KEEP_AS_NON_CORE (K+ served by many pathways; KCC3 is a
  major Cl- exit route per PMID:19665974).
- GO:1902476 chloride transmembrane transport (TAS), GO:0071805 potassium ion
  transmembrane transport (IBA/IDA×2) → ACCEPT.
- GO:0071476 cellular hypotonic response (TAS) → ACCEPT; GO:0071477 cellular
  hypotonic salinity response (IDA) → MODIFY → GO:0071476 (assay was osmotic
  hypotonic swelling, not a low-salt/salinity-specific response).
- GO:1990573 potassium ion import across plasma membrane (IDA) → MODIFY →
  GO:0071805 (KCC3 physiologically effluxes K-Cl; "import" over-specifies
  direction for an electroneutral, bidirectional cotransporter).
- Root/general terms entailed by the specific accepted terms → TOO_GENERAL:
  GO:0006811 monoatomic ion transport (IDA/IEA), GO:0015377 chloride:monoatomic
  cation symporter activity (IEA), GO:0022857 transmembrane transporter activity
  (IEA), GO:0055085 transmembrane transport (IEA), GO:0006821 chloride transport
  (IBA; entailed by GO:1902476).
- GO:0001525 angiogenesis (NAS, PMID:10187864) → MARK_AS_OVER_ANNOTATED: rests
  only on VEGF up-regulation of KCC3 mRNA in endothelium; regulation-by /
  expression is not participation in angiogenesis.
