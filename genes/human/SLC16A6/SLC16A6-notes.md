# SLC16A6 (MCT7, UniProt O15403) — curation notes

## Identity and family

- SLC16A6 encodes Monocarboxylate transporter 7 (MCT7), also historically called MCT6
  (nomenclature confusion: the original cloning paper denoted this gene "MCT6", and UniProt
  retains "MCT6" as an AltName while the current standard short name is MCT7).
  [file:human/SLC16A6/SLC16A6-uniprot.txt "RecName: Full=Monocarboxylate transporter 7"]
  [file:human/SLC16A6/SLC16A6-uniprot.txt "AltName: Full=Monocarboxylate transporter 6"]
- Member of the major facilitator superfamily (MFS), monocarboxylate porter family (TC 2.A.1.13);
  predicted 12-transmembrane topology with a large intracellular loop between TM6 and TM7, typical
  of SLC16/MCT transporters.
  [file:human/SLC16A6/SLC16A6-uniprot.txt "Belongs to the major facilitator superfamily."]
  [PMID:9425115 "All sequences were predicted to have 12 transmembrane (TM) helical domains with a large intracellular loop between TM6 and TM7."]
- 523 aa; InterPro IPR030766 (MCT7-specific), PANTHER PTHR11360:SF20 (MONOCARBOXYLATE TRANSPORTER 7),
  CDD cd17422 (MFS_MCT7). TCDB 2.A.1.13.15.
- Protein existence: evidence at protein level (detected by MS proteomics); Pharos class Tdark
  (understudied). Tissue-enhanced expression in choroid plexus, epididymis, retina (HPA); also liver
  and brain.
- This is a **sparsely characterized ("orphan") transporter**. Only ~5 primary papers bear directly
  on its function, and the two UniProt-cited references are abstract-only in our cache.

## Original cloning paper (PMID:9425115, abstract-only)

- Price, Jackson & Halestrap (1998) cloned four new human MCT homologues from cDNA, denoting them
  MCT3–MCT6; the sequence they called "MCT6" corresponds to the present SLC16A6/MCT7.
  [PMID:9425115 "the cloning and sequencing of four new full-length MCT-like sequences from human cDNA libraries, which we have denoted MCT3, MCT4, MCT5 and MCT6"]
- This paper is **sequence/family evidence only** — Northern blotting for tissue distribution plus
  topology prediction. It contains **no functional transport assay and no subcellular-localization
  experiment** for SLC16A6. The GOA TAS rows anchored to it (plasma membrane; monocarboxylic acid
  transmembrane transporter activity; monocarboxylic acid transport; membrane) are therefore
  predictions from family membership and predicted topology, not direct measurement — reasonable
  family-level calls but low evidence grade.
  [PMID:9425115 "Together these sequences constitute a new family of transporters"]

## Established function 1 — ketone body (β-hydroxybutyrate) export (strongest, human-protein-linked)

- Forward-genetic screen in zebrafish identified the *red moon* (rmn) mutant with fasting hepatic
  steatosis; the locus is **slc16a6a**, which the authors showed **encodes a transporter of the major
  ketone body β-hydroxybutyrate** required for hepatocyte secretion of ketone bodies during fasting.
  Loss of function diverts liver-trapped ketogenic carbon into triacylglycerol.
  [PMID:22302940 "a gene that we show encodes a transporter of the major ketone body β-hydroxybutyrate"]
- **Crucially, human SLC16A6 functionally rescues the zebrafish mutant**: "Restoring wild-type
  zebrafish slc16a6a expression or introducing human SLC16A6 in rmn mutant livers rescues the mutant
  phenotype." This cross-species rescue is **direct functional evidence that the human protein mediates
  β-hydroxybutyrate (ketone body) export**, not merely orthology inference.
  [PMID:22302940 "introducing human SLC16A6 in rmn mutant livers rescues the mutant phenotype"]
- Follow-up (PMID:30692937) reaffirmed that zebrafish slc16a6 mutants cannot export β-hydroxybutyrate,
  develop hepatic steatosis on ketogenic conditions, and that human SLC16A6 coding/non-coding variants
  are genome-wide significantly associated with human height; concluded the gene acts "through
  modulating transport of monocarboxylic acids in several tissues."
  [PMID:30692937 "cannot export the major ketone body β-hydroxybutyrate, diverting liver-trapped ketogenic carbon atoms to triacylglycerol"]
- Evidence grade: β-hydroxybutyrate is a monocarboxylic acid, so this supports GO:0008028 (monocarboxylic
  acid transmembrane transporter activity) and the more specific GO:0097253 (β-hydroxybutyrate
  transmembrane transporter activity). GO:0097253 is_a GO:0008028 (QuickGO ancestry verified). The
  human-protein rescue warrants proposing GO:0097253 as a NEW annotation.

## Established function 2 — facilitative taurine transport (mammalian ortholog, human-cell assays)

- Higuchi et al. (2022) reported mammalian **MCT7/Slc16a6 as a novel facilitative taurine transporter**.
  EGFP-tagged MCT7 expressed in human HEK293T and polarized Caco-2 cells caused rapid taurine
  reduction; taurine uptake and efflux were **pH-independent**, **non-saturable up to 200 mM** (low
  affinity), and **inhibited by monocarboxylates and acidic amino acids**. MCT7 localized to the
  **basolateral membrane** of polarized Caco-2 cells and enhanced transepithelial taurine permeation.
  [PMID:35257743 "these findings reveal that taurine is a novel substrate of MCT7 and that MCT7-mediated taurine transport might contribute to the efflux of taurine from cells"]
  [PMID:35257743 "We found that taurine uptake and efflux by MCT7 was pH-independent and that the uptake was not saturated in the presence of taurine excess of 200 mM"]
  [PMID:35257743 "MCT7 was localized at the basolateral membrane in polarized Caco-2 cells"]
- Transport is enhanced by the ancillary single-TM proteins **basigin/CD147 and embigin/GP70**, as for
  several MCTs.
  [PMID:35257743 "interactions of MCT7 with ancillary proteins basigin/CD147 and embigin/GP70 enhanced MCT7-mediated taurine transport"]
- A later review by the same group clarifies they "successfully identified taurine ... as new
  substrates for **rat** Slc16a6/MCT7", and that MCT7 function (unlike MCT6/MCT13) was **unaffected by
  extracellular chloride and potassium**, consistent with simple facilitative (uniport) transport.
  [PMID:39617467 "We successfully identified taurine, cephradine, and 5-carboxyfluorescein as new substrates for rat Slc16a6/MCT7, SLC16A13/MCT13, and SLC16A5/MCT6, respectively"]
- **Evidence-grade caveat:** the directly assayed construct in the mechanistic taurine work is the
  **rat ortholog** (Slc16a6/Q7TMR7), expressed in human cells. The human SLC16A6 taurine activity is
  therefore ISS-propagated (UniProtKB:Q7TMR7), well-grounded in mammalian experiment but **not a direct
  human-protein assay**. UniProt's curated FUNCTION reflects this ortholog work.
  [file:human/SLC16A6/SLC16A6-uniprot.txt "Monocarboxylate transporter selective for taurine. May"]
  [file:human/SLC16A6/SLC16A6-uniprot.txt "The transport is pH- and sodium-independent. Rather low-affinity, is"]

## Mechanism and localization (synthesis)

- MCT7 is a **facilitative (uniport), pH- and Na+-independent, low-affinity** polyspecific transporter.
  It is NOT a proton-coupled symporter like MCT1–4; do not assert H+ coupling.
  [file:human/SLC16A6/SLC16A6-uniprot.txt "The transport is pH- and sodium-independent. Rather low-affinity, is"]
- Substrate range spans at least β-hydroxybutyrate (a monocarboxylate/ketone body) and taurine (an
  amino-sulfonic acid); monocarboxylates and acidic amino acids compete, consistent with a broad
  monocarboxylate/organic-anion channel-like facilitator. Taurine (GO:0005368) sits on the sulfur-
  compound-transporter branch (QuickGO: is_a GO:1901682), distinct from the monocarboxylate branch, so
  the two substrate activities are genuinely different MF leaves.
- Localization: **basolateral plasma membrane** (shown in polarized Caco-2 cells; UniProt curated
  basolateral cell membrane from rat ISS). Consistent with an efflux role (e.g. hepatocyte ketone
  export to blood; basolateral taurine efflux in epithelia).
  [file:human/SLC16A6/SLC16A6-uniprot.txt "Basolateral cell membrane"]
- Ancillary subunits: forms functional complexes with BSG/CD147 or EMB/GP70.
  [file:human/SLC16A6/SLC16A6-uniprot.txt "Forms functional complexes with BSG/CD147 or EMB/GP70"]

## Interaction annotation (PMID:32814053, abstract-only)

- The GOA GO:0005515 (protein binding) IPI row cites a single high-throughput neurodegenerative-disease
  **interactome Y2H mapping** (Haenig et al. 2020), reporting SLC16A6–WFS1 (wolframin, O76024). This is
  an uninformative bare "protein binding" annotation from one HT screen (WFS1 is itself an ER membrane
  protein, a problematic Y2H bait/prey), with no functional characterization. Per the project
  protein-binding policy, bare GO:0005515 is removed as uninformative.

## Phosphorylation / PTM (not annotated functionally)

- Phosphoserines at S234/S237/S240/S247 (large-scale phosphoproteomics, PMID:17081983, 18669648) in the
  large intracellular TM6–TM7 loop. No functional consequence established.

## Review decisions summary

- **Core MF 1:** GO:0097253 β-hydroxybutyrate transmembrane transporter activity (NEW) — human rescue
  evidence (PMID:22302940). Parent GO:0008028 kept via existing IBA/TAS rows.
- **Core MF 2:** GO:0005368 taurine transmembrane transporter activity (ISS ACCEPT) — mammalian/rat
  experimental + human-cell assays (PMID:35257743), ISS to human.
- **Core location:** GO:0016323 basolateral plasma membrane (ACCEPT) / GO:0005886 plasma membrane (ACCEPT).
- **ACCEPT:** GO:0008028 (IBA, TAS), GO:0015718 monocarboxylic acid transport (TAS), GO:0015734 taurine
  transmembrane transport (IEA, inferred from accepted MF), GO:0005886 (IBA, TAS), GO:0016323 (IEA, ISS).
- **TOO_GENERAL (term entailed by a more specific asserted term):** GO:0015849 organic acid transport
  (ancestor of asserted GO:0015718), GO:0016020 membrane ×2 (which membrane? — entailed by plasma
  membrane), GO:0022857 transmembrane transporter activity (entailed by GO:0008028), GO:0055085
  transmembrane transport (entailed by GO:0015734).
- **REMOVE:** GO:0005515 protein binding (bare, uninformative; protein-binding policy).
