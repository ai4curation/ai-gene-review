# AVR4 (Fulvia fulva / Cladosporium fulvum; UniProt Q00363) — curation notes

## 2026-10-02 — initial review

Sources: UniProt record, GOA (10 rows), falcon deep research, cached publications
(PMID:30148881 full text; others abstract only), plus six PubMed-verified papers added
and cached via `just fetch-gene-pmids` (17849712, 17153926, 14769793, 12736265,
27401545, 9090881).

### Identity / structure
- Secreted 135-aa precursor; signal peptide 1-18, propeptide 19-29, CBM14
  (invertebrate chitin-binding type-2) domain 47-111 (UniProt).
- "AVR4 contains an invertebrate (inv) chitin-binding domain (ChBD). Binding of AVR4 to
  chitin was confirmed experimentally." [PMID:12736265]
- Crystal structure with (GlcNAc)6 at 1.95 Å (PDB 6BN0) [PMID:30148881 "we solved the
  crystal structure of CfAvr4 in complex with chitohexaose [(GlcNAc)6] at 1.95Å
  resolution"].

### Intrinsic function: wall chitin shielding
- "interaction of Avr4 with chitin is specific, because it does not interact with other
  cell wall polysaccharides" ... "In vitro, Avr4 protects chitin against hydrolysis by
  plant chitinases" ... "In situ fluorescence studies showed that Avr4 also binds to cell
  walls of C. fulvum during infection of tomato" [PMID:17153926].
- Non-binding mutants (W100A, D102A) fail to protect T. viride germlings from chitinases
  [PMID:30148881 "mutations in the ChBD of CfAvr4 that decrease or abolish its affinity
  for (GlcNAc)6 also reduce the protein's ability to protect fungal germlings against
  chitinases"].
- Virulence: "silencing of the Avr4 gene in C. fulvum decreases its virulence on tomato"
  [PMID:17849712].
- Proposed binding mode on walls: "it is plausible that the protein rests as a monomer on
  the solvent-exposed surface of these microfibrils, thus creating a protective layer
  against endochitinases" [PMID:30148881]. This is shielding, not soluble-PAMP
  sequestration (contrast ECP6).

### Avirulence: Cf-4 recognition
- AVR4 triggers HR in Cf-4 tomato [PMID:10998185; PMID:16167771; PMID:25902074].
- Recognition separable from chitin binding: "mutations in residues within the ChBD that
  decrease or abolish the protein's affinity for (GlcNAc)6 do not individually affect
  recognition by Cf-4 if they do not perturb the stability of the protein"
  [PMID:30148881].
- Virulent strains make protease-sensitive isoforms [PMID:9090881; PMID:12736265 "These
  natural Cys to Tyr mutant AVR4 proteins did retain their chitin binding ability"].

### GO term decisions
- GO:0140320 PAMP receptor decoy activity — definition is "Binding and sequestering PAMP
  ligands in order to prevent them from binding and activating to the host PAMP receptor"
  (QuickGO). Not tested in PMID:30148881 (full text read). MARK_AS_OVER_ANNOTATED.
  Only 5 annotations in GOA (Mg3LysM, a chitinase-like Chi, MGG_08054, AVR4).
- GO:0140403 suppression of host innate immune response (IMP) — evidence is chitinase
  protection; MODIFY to GO:0141177 "symbiont-mediated evasion of recognition by host
  innate immune effector" (def: symbiont mitigates effects of host innate immune
  effectors with direct activity against the symbiont, e.g. AMPs, complement). GO:0141177
  currently has 0 annotations in GOA; plant chitinases fit the definition.
- GO:0080185 / GO:0140404 rows: KEEP_AS_NON_CORE (recognition outcome).
- NEW locations: GO:0140593 host apoplast; GO:0009277 fungal-type cell wall.
- Ontology oddity: GO:0080185 (activation of plant HR) has GO:0140403 (suppression of host
  innate immune response) among its is_a ancestors (QuickGO ancestors query). Raised as a
  suggested question.

### Project-relevant observation
- AVR4 vs ECP6: both chitin-binding effectors, but distinct mechanisms. AVR4 currently
  carries the decoy (sequestration) MF that better fits ECP6; the evasion-of-host-effector
  process term (GO:0141177) is the better representation of AVR4's counter-defence.
