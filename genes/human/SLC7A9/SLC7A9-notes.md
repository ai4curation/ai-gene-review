# SLC7A9 (b0,+AT1 / BAT1) — curation notes

UniProt: P82251 (BAT1_HUMAN). HGNC: SLC7A9. 487 aa, multi-pass membrane protein,
APC (amino acid-polyamine-organocation) superfamily, LeuT fold. Gene on chr 19.

## Core biology (verified)

SLC7A9/b0,+AT is the **catalytic light chain** of a heteromeric amino acid
transporter (HAT). It is **disulfide-linked to the heavy chain SLC3A1 (rBAT)** —
NOT to 4F2hc/SLC3A2 (the heavy chain used by the LAT/y+LAT light chains). The
interchain disulfide is b0,+AT Cys144 ↔ rBAT Cys114
[PMID:32494597 full text, "Besides the disulfide bond between rBAT-Cys114 and b0,+AT-Cys144"];
UniProt FT DISULFID 144 "Interchain (with C-114 in SLC3A1)".

- **Mechanism:** system b0,+, a **Na+-independent, electrogenic, obligatory
  antiporter (exchanger)**. It mediates influx of extracellular **L-cystine and
  cationic (dibasic) amino acids (Arg, Lys, ornithine)** in exchange for efflux of
  intracellular **neutral amino acids**, 1:1 stoichiometry
  [PMID:8663357 abstract, "System bo, +-like showed a 1:1 stoichiometry of exchange, and the hetero-exchange dibasic (inward) with neutral (outward) amino acids were favored in oocytes"]
  [PMID:32494597 full text, "The b0,+AT-rBAT heterodimer mediates the Na+-independent electrogenic obligatory exchange of extracellular cationic amino acids and cystine with intracellular neutral amino acids"].
  High affinity for extracellular cationic AAs and cystine; lower affinity for
  intracellular neutral AAs (UniProt FUNCTION; KM = 41 µM cystine, 85 µM Arg, 90 µM Leu).
  The exchange is driven by the high intracellular concentration of neutral AAs and the
  intracellular reduction of cystine to cysteine [PMID:8663357].
- **Localization:** apical (brush border) plasma membrane of epithelial cells in
  renal proximal tubule and small intestine. Expressed as heterodimers with rBAT
  that coprecipitate from kidney brush-border membranes
  [PMID:12167606 abstract, "rBAT and b(0,+)AT were solely expressed as heterodimers of identical size and that both proteins coprecipitated"].
  "a decreasing expression gradient of heterodimeric rBAT-b(0,+)AT along the proximal
  tubule is responsible for virtually all apical cystine reabsorption" [PMID:12167606].
- **Physiological role:** apical reabsorption of cystine and dibasic amino acids in
  kidney and intestine. The counter-substrate (neutral AA efflux) is the driving arm.
- **Oligomeric state:** minimal functional unit is a single b0,+AT-rBAT heterodimer;
  the assembly exists as a **heterotetramer (dimer of heterodimers)** mediated by rBAT
  [PMID:16825196 abstract, "system b0,+ is a heterotetramer [b0,+ AT-rBAT]2"; "a single heterodimer is the functional unit of systems b0,+ and xC-"]
  [PMID:32817565 abstract, "a heterotetrameric protein assembly composed of two heavy and light chain subunits ... mediated via dimerization of the heavy chain subunits and does not include participation of the light chain subunits"].
  rBAT dictates oligomerization and traffics/stabilizes the complex to the plasma membrane.

## Structure

Cryo-EM structures of human b0,+AT-rBAT: 6LI9/6LID (PMID:32494597, 2.3–2.7 Å,
inward-open, +Arg and apo) and 6YUP/6YV1 (PMID:32817565). b0,+AT adopts the LeuT
fold (TM1-5 / TM6-10 inverted repeats); substrate pocket formed by TM1, TM6, TM10.
Arg bound in pocket 1 (H-bonds to Ile43, Gly45, Gly47 on TM1; Trp230, Asp233, Gln237
on TM6). Alanine mutagenesis: W230A, D233A, W235A, W383A, Y386A abolish transport;
Q237A, S379A partial [PMID:32494597 full text]. The complex has NO α-glucosidase
activity despite rBAT ECD homology to maltases
[PMID:32494597 full text, "the complex has no α-glucosidase activity when compared with the positive control isomaltase of Saccharomyces cerevisiae"].

## Disease

Loss-of-function causes **cystinuria (CSNU, MIM 220100), non-type I / type B**
(Orphanet Cystinuria type B). SLC7A9 mutations → non-type I; SLC3A1 → type I.
Impaired renal/intestinal reabsorption of cystine and dibasic AAs; cystine's low
solubility causes urinary tract calculi [PMID:10471498; UniProt DISEASE].
Many characterized missense variants reduce or abolish transport (e.g. A182T, V170M,
R333W, A354T, A382T, P482L) or destabilize the complex/dimer (P52L, G259R)
[PMID:32494597 full text; PMID:16609684].

## Substrate precision note

b0,+AT transports **L-cystine** (the oxidized disulfide dimer; ChEBI:35491), the
primary physiological high-affinity substrate (KM 41 µM) — distinct from L-cysteine
monomer. UniProt lists exchange half-reactions for both cystine and cysteine against
Arg(in), but the physiological/GO substrate term is cystine (GO:0015184 L-cystine
transmembrane transporter activity). Do not conflate with cysteine. GOA correctly uses
cystine terms.

## Annotation review orientation

- Core MF: **GO:0180009** broad specificity neutral L-amino acid:basic L-amino acid
  antiporter activity (EXP/IDA); **GO:0015184** L-cystine transmembrane transporter
  activity. GO:0106439 (Lys:Arg antiporter, EXP) and GO:0015175 (neutral L-AA
  transporter) are supported facets.
- Core CC: apical plasma membrane (GO:0016324) / brush border membrane (GO:0031526);
  functional unit is the b0,+AT-rBAT transmembrane transporter complex (GO:1902495,
  ComplexPortal CPX-8184).
- Generic/root transporter and transport terms (GO:0022857, GO:0015171, GO:0015297,
  GO:0003333, GO:0006865, GO:0055085, GO:1902475) are true but entailed by the specific
  terms → TOO_GENERAL.
- GO:0016020 membrane (IEA) → MODIFY → plasma membrane (GO:0005886).
- GO:0005886 plasma membrane rows: apical plasma membrane is asserted → TOO_GENERAL
  (keep, true, but subsumed by the apical/brush-border rows).
- GO:0005515 protein binding (3 IPI rows: SLC3A1 ×2, CREB3 ×1): bare protein binding →
  REMOVE per protein-binding policy. The functional SLC3A1 interaction is captured by
  GO:0046982 (heterodimerization) and GO:1902495 (complex). CREB3 (O43889-2) is a
  high-throughput Y2H hit (PMID:25910212), no functional characterization.
- GO:0042605 peptide antigen binding (ISS from Q9N1R6): "Binding to an antigen peptide"
  (OLS) — an MHC/immune-type function with no basis in any b0,+AT literature; demonstrably
  wrong similarity mapping → REMOVE.
- GO:0046982 protein heterodimerization activity (IDA): real (disulfide heterodimer with
  rBAT) but not the transport core → KEEP_AS_NON_CORE.
- GO:0065003 protein-containing complex assembly (TAS PMID:10799513): b0,+AT assembles
  with rBAT (and in vitro with 4F2hc) → KEEP_AS_NON_CORE.

IBA rows (GO:0003333, GO:0005886, GO:0015175, GO:0015184, GO:0015811, PTN000208507 /
PTN000268381): the SLC7 light-chain family node; b0,+AT is squarely within the HAT
light-chain clade and carries its own EXP annotations (appears in its own WITH/FROM for
PTN000268381, which is expected, not circular). Node placement sound; judge each term on
specificity.

No PAINT loss concerns expected for a well-conserved transporter core; the IBA terms are
all supported by direct human experimental data.
