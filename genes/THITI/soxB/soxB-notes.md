# soxB (U5TVQ7, Thiobacillus thioparus) review notes

## Entry identity

- UniProtKB U5TVQ7 (U5TVQ7_THITI) is an unreviewed TrEMBL entry, 325 aa, flagged
  `Fragment` with NON_TER at both ends. It comes from a soxB PCR amplicon of
  *T. thioparus* strain NZ (EMBL KC542803), deposited by a soil-microcosm study that
  designed soxB primers for nonfilamentous chemolithotrophic sulfur oxidisers
  [PMID:24646185 "We have developed a molecular approach based on primer design
  targeting the soxB functional gene of nonfilamentous chemolithotrophic SOB that
  allows assessment of both abundance and diversity"]. That paper is an ecology study.
  It contains no biochemistry on this protein.
- The UniProt submitter name "Sulfate thioesterase/sulfate thiohydrolase" is taken
  from the EMBL record (ECO:0000313), and so is the gene name. PANTHER places the
  fragment in PTHR11575:SF42 "SULFUR OXIDATION PROTEIN SOXB". This placement and the
  homology analysis below agree that it is a genuine SoxB.
- No deep-research provider output exists (no API keys). These notes are manual
  literature research.

## Bioinformatics (file:THITI/soxB/soxB-bioinformatics/RESULTS.md)

- The fragment aligns to residues ~153-470 of *Paracoccus pantotrophus* SoxB
  (A0AAE6TS95; 50.3% identity) and ~148-465 of *Thermus thermophilus* HB27 SoxB
  (Q72IT0; 38.9% identity), whose crystal structures define the Mn site.
- Of the seven PDB-derived Mn(2+) ligands of Q72IT0, the four that fall inside the
  fragment are conserved histidines (U5TVQ7 H27, H131, H154, H156). D47, H49 and D143
  lie upstream of the fragment and cannot be assessed.
- The N-terminal Tat signal peptide is outside the fragment. Periplasmic location
  therefore rests on homology, not on this sequence.

## SoxB biology (homologs)

- SoxB is the Sox component that hydrolyses sulfate off the SoxY carrier cysteine.
  It has a dimanganese site [PMID:19535341 "SoxB contains a di-manganese(II) site and
  is proposed to catalyze the release of sulfate from a protein-bound cysteine
  S-thiosulfonate"]. The T. thermophilus structures include complexes with the
  substrate analogue thiosulfate and with product sulfate [PMID:19535341 "Structures
  were also determined for SoxB in complex with the substrate analogue thiosulfate
  and in complex with the product sulfate"].
- The reaction is ENZYME EC 3.1.6.20, S-sulfosulfanyl-L-cysteine sulfohydrolase
  (S-sulfosulfanyl-L-cysteinyl-[SoxY protein] + H2O = S-sulfanyl-L-cysteinyl-[SoxY
  protein] + sulfate + H+; ExPASy ENZYME, checked 2026-10-28). The bond cleaved is
  the S-S bond between the sulfane and sulfone sulfur atoms. GO has no term for this
  reaction. The closest existing parent is GO:0016828 "hydrolase activity, acting on
  sulfur-sulfur bonds".
- In *P. pantotrophus*, SoxB is required in the reconstituted system [PMID:10940005
  "Purified SoxXA, SoxYZ, and SoxB are essential for thiosulfate or sulfite-dependent
  cytochrome c reduction in vitro"]. It has a Tat signal peptide [PMID:10940005 "The
  putative signal peptide contained a twin arginine motif (see Fig. 7 ) characteristic
  of periplasmic proteins"]. It is homologous to 5'-nucleotidase [PMID:10940005 "The
  soxB gene product predicts a protein of a molecular mass of 61,897 Da which is 20.7%
  identical to 5′-nucleotidase of Escherichia coli"].
- In *Allochromatium vinosum*, genetics showed SoxB is required in vivo [PMID:16995898
  "Gene inactivation and complementation experiments proved these proteins to be
  indispensable for thiosulphate oxidation to sulphate"]. Meyer et al. describe SoxB
  as a component of the periplasmic complex and found soxB in *Thiobacillus*
  [PMID:17991026 "The soxB gene encodes the SoxB component of the periplasmic
  thiosulfate-oxidizing Sox enzyme complex"].
- *T. thioparus* DSM 505T (= ATCC 8158T) has soxXYZAB but no soxCD [PMID:28127420
  "Numerous Kelly-Friedrich pathway genes (soxXYZAB) were present but the remaining
  of the conserved soxTRS-VW-XYZABCDEFGH genes being absent"]. The authors assign
  SoxB its canonical role [PMID:28127420 "Finally soxB encodes a hydrolase that
  removes the terminal sulfone group as sulfate"]. Without SoxCD, the sulfane sulfur
  is not oxidised on SoxY, as in *A. vinosum*.
- The same paper is agnostic about whether Sox acts in *T. thioparus* at all. Batch
  cultures show tetrathionate as an intermediate, the Kelly-Trudinger signature, and
  the authors write [PMID:28127420 "If soxXYZAB genes are being expressed then they
  may be required as a functional part of the Kelly-Trudinger pathway. The action of
  Sox proteins (if any)"] ... "remains poorly understood". This supports keeping all
  process claims for U5TVQ7 at the homology level.

## Annotation decisions (summary)

- GO:0016787 hydrolase activity (InterPro2GO): correct but general. MODIFY to
  GO:0016828 hydrolase activity, acting on sulfur-sulfur bonds. A specific term
  (EC 3.1.6.20) is listed under proposed_new_terms.
- GO:0009166 nucleotide catabolic process (InterPro2GO from IPR006179/IPR036907):
  REMOVE. The mapping is a family-level over-propagation from the 5'-nucleotidase
  members. SoxB's substrate is the SoxY-bound sulfonate, and no nucleotidase activity
  has been reported for any SoxB. Recorded as an InterPro2GO source defect (CHECK).
- GO:0030288 outer membrane-bounded periplasmic space (TreeGrafter): ACCEPT. SoxB is a
  Tat-exported periplasmic Sox component in a Gram-negative bacterium. The PAINT IBD
  node PTN008520763 is seeded by E. coli UshA/CpdB, which are themselves periplasmic.
- NEW GO:0030145 manganese ion binding (IC). Two lines of evidence: the dimanganese
  site of characterised SoxB, and conservation of all four Mn ligands covered by the
  fragment.
- NEW GO:0019417 sulfur oxidation (IC), added after the PR review (#5628). SoxB
  catalyses a step of the pathway, so it passes the participation test. Process terms
  searched in QuickGO on 2026-10-28 (children of GO:0006790 sulfur compound metabolic
  process, plus searches for "thiosulfate", "sulfur oxidation", "sulfite oxidation",
  "tetrathionate", "polythionate", "sulfane"):
  - GO:0019416 thiosulfate oxidation: defined as thiosulfate to tetrathionate with
    cytochrome c as acceptor (Tsd/TQO). Rejected, not the SoxB step.
  - GO:0019418 sulfide oxidation (sulfide to sulfite or sulfate): not established for
    SoxB. Rejected.
  - GO:0019414 aerobic respiration, using sulfur or sulfate as electron donor: the
    definition includes thiosulfate, but it frames the process as respiration, SoxB
    transfers no electrons, and nothing is annotated to it. Rejected.
  - GO:0044273 sulfur compound catabolic process: "breakdown" fits an oxidative energy
    pathway poorly. Rejected.
  - GO:0006790 sulfur compound metabolic process: true but uninformative; it is the
    parent of the chosen term.
  - GO:0019417 sulfur oxidation (no children): its definition says elemental sulfur,
    but the comparator check shows it is the Sox-system term in practice. SoxA carries
    it by IDA in five species (O33434 P. pantotrophus from PMID:10940005, D7A6E5,
    Q08IS0, Q8KDM7, Q8RLX0), assigned by UniProt. Chosen. The definition mismatch is
    raised as a suggested question.
  The inference is by homology only: U5TVQ7 is a fragment from strain NZ, no
  T. thioparus SoxB has been assayed, and the type-strain genome paper is unsure
  whether Sox acts in this organism. Even the structurally characterised
  T. thermophilus SoxB (Q72IT0) carries only the same three IEA rows.

## CMMMech claim check (data/records/metacinnabar.yaml; not edited)

- `functional_role` gives EC 3.12.1.1. That EC is trithionate hydrolase (GO:0047401),
  not the SoxB reaction. The correct EC is 3.1.6.20.
- `functional_role` says SoxB catalyses "thiosulfate cleavage during sulfur-oxidizing
  mobilization of mercury from metacinnabar". This is stronger than the evidence:
  1. The metacinnabar study (PMID:26157421) used *T. thioparus* ATCC 8158 and contains
     no mention of sox genes. The evidence block in CMMMech correctly says partial
     support.
  2. U5TVQ7 is from a different strain (NZ, a soil isolate), and it is a fragment.
  3. SoxB does not cleave free thiosulfate. It hydrolyses sulfate from the SoxY-bound
     S-thiosulfonate after SoxAX has attached thiosulfate to SoxY.
  4. Any link from SoxB to HgS dissolution is an inference: thiosulfate/sulfide
     oxidation by the culture. It is not a measured SoxB function.
- The node description "Periplasmic Sox-pathway thiosulfohydrolase driving
  chemolithoautotrophic sulfur/sulfide oxidation" is acceptable at the homology level.
  "sulfide oxidation" is not established for SoxB itself.
