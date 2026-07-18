# Notes: Thermotoga maritima `enc` (Q9WZP2, ENCAP_THEMA)

## Why this gene is in the corpus
Selected as the **primary experimental source seeding the IBA annotations** to
GO:0140737 (encapsulin nanocompartment). QuickGO shows 5 IBA annotations to that
term, all propagating from PANTHER family node PTN002201532 with a with/from panel
of two experimental leaves: `Q9WZP2` (*T. maritima*, this gene) and `I6WZG6`
(*M. tuberculosis*). Q9WZP2 is the far richer anchor — 1 IDA + 7 EXP annotations
vs. the *M. tuberculosis* leaf's single IDA — and is the prototypical/model
encapsulin.

## Identity
- **Type 1 encapsulin shell protein**; gene `enc`; ordered locus TM_0785 / TM0785.
- 265 aa; HK97-like fold (viral capsid–derived). PANTHER family PTHR37165
  ("Encapsulin nanocompartment").
- AltNames of historical interest: **Maritimacin**, **Thermotoga bacteriocin** —
  it was first described as a thermostable protease/"bacteriocin" before being
  recognized as an encapsulin shell.

## Core biology (with provenance)
- Forms a **T=1 icosahedral proteinaceous shell**: 60 monomers = 12 pentamers,
  ~23–24 nm diameter, 2.0–2.5 nm thick walls. N-terminus inside, C-terminus
  outside. [PMID:19172747 "60 copies of the monomer assemble into a thin,
  icosahedral shell with a diameter of 240 angstroms"] (founding 3.1 Å crystal
  structure; this is the IDA anchor for the CC term).
- **Encapsulates a ferritin-like cargo protein (Flp)** targeted to the shell
  interior via a C-terminal targeting peptide binding conserved interior sites;
  implicated in oxidative-stress response / iron storage. [PMID:19172747 "The
  interior of this nanocompartment is lined with conserved binding sites for
  short polypeptide tags present as C-terminal extensions of enzymes involved in
  oxidative-stress response"] Empty intact shells can be isolated without cargo
  (UniProt FUNCTION, ECO:0000269).
- **Flavoprotein**: binds FMN near the 3-fold axis channel — established
  independently by three structural/biochemical studies. [PMID:34815415 "The
  encapsulin from Thermotoga maritima is a flavoprotein with a symmetry matched
  ferritin-like cargo protein"]; corroborated [PMID:33953921] and [PMID:35119930].
- **Fe(2+) flux**: iron ions may pass through the 5-fold and dimer channels of the
  shell (Probable). [UniProt FUNCTION, ECO:0000305|PMID:33953921]
- **Model scaffold for bioengineering**: minimal peptide cargo-loading tag
  [PMID:27224728]; pore engineering for mass transport [PMID:30376298];
  artificial metabolons [PMID:33769792]; engineered protein cages [PMID:35119930].

## Historical / uncertain: protease ("maritimacin") activity
UniProt retains a second FUNCTION: "Protease that exhibits activity toward
chymotrypsin and trypsin substrates" (chymotrypsin/trypsin-like, Ca/Co-activated,
pH opt ~7.1, T opt 90–93 °C) [ECO:0000269|PMID:11210524, PMID:9872409], but flags
"**Probably does not have antibacterial activity**" and the shell-protein
reinterpretation [ECO:0000305|PMID:19172747]. UniProt keyword xrefs therefore carry
GO:0008233 (peptidase activity), GO:0006508 (proteolysis), GO:0006826 (iron ion
transport) as keyword-derived IEAs. **None of these three are in the GOA seed**
(GOA only carries GO:0140737), so they are not part of `existing_annotations`.
These are candidates for scrutiny: the "maritimacin protease" characterization
predates the encapsulin reinterpretation and may reflect a distinct or artefactual
activity rather than the physiological function of the shell protein.

## GOA situation (the curation story)
All 10 GOA annotations point to the **same term**, GO:0140737, differing only in
evidence/qualifier:
- 1 IDA (PMID:19172747, `located_in`) — founding structure, the anchor.
- 7 EXP/ECO:0000269 (`located_in`) — cargo-loading & structural studies.
- 1 IBA (GO_REF:0000033, `is_active_in`) — phylogenetic; **this gene is its own
  experimental seed**.
- 1 IEA (GO_REF:0000120 / ARBA, `located_in`) — redundant electronic.
This is heavy redundancy on a single, well-supported cellular-component term. All
are correct; the shell protein legitimately *is* / localizes to the nanocompartment.
The missing piece in GOA is a **molecular function** — the protein's core role is
structural (it constitutes the shell), best captured by GO:0005198 structural
molecule activity, which I add in `core_functions`.
