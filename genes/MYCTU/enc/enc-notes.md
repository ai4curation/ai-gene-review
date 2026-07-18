# Notes: Mycobacterium tuberculosis `enc` / CFP29 (I6WZG6, ENCAP_MYCTU, Rv0798c)

## Why this gene is in the corpus
The **second experimental seed** (with *T. maritima* Q9WZP2) of the GO:0140737
encapsulin-nanocompartment IBA propagation (PANTHER PTN002201532 / PTHR37165).
Reviewed as the cross-species counterpart to `THEMA/enc`.

## Identity
- **Type 1 encapsulin shell protein**, gene `enc`, locus **Rv0798c**.
- Originally identified as **CFP29 ("Culture Filtrate Protein 29")**, a 29 kDa
  secreted mycobacterial T-cell antigen. [PMID:9596740 "The 29-kDa antigen (CFP29)
  was purified from M. tuberculosis short-term culture filtrate"] The same 1998
  paper already noted it "forms a polymer with a high molecular mass" and has
  "62% identity to the bacteriocin Linocin from Brevibacterium linens" — the
  encapsulin identity in hindsight, but framed then as a secretome/vaccine antigen.
- Structurally recognized as the M. tuberculosis encapsulin (Mt-Enc) in 2014.
  [PMID:24855650]

## Core biology (with provenance)
- Forms an intracellular ~22 nm icosahedral proteinaceous nanocompartment
  (~2.5 nm walls) in situ and when expressed in E. coli. [UniProt FUNCTION,
  ECO:0000269|PMID:24855650, PMID:34751132]
- In an **operon with its principal cargo, the dye-decolorizing peroxidase DyP**;
  also encapsulates **BfrB** (ferritin) and **FolB**, all targeted via C-terminal
  extensions. [PMID:24855650 "we show by co-purification and electron microscopy
  that mycobacteria via Mt-Enc can encapsulate Mt-DyP, Mt-BfrB, and Mt-FolB"]
- Cargo enzymes are antioxidant → the nanocompartment is implicated in the
  **oxidative/nitrosative-stress response** and survival against host ROS =
  **virulence-associated**. [PMID:24855650; PMID:34751132 "Probably involved in
  protection against oxidative damage from the host immune response"]

## The live curation problem (contrast maritimacin)
Unlike the *T. maritima* maritimacin case — where the superseded "protease" identity
is GONE from GOA because kw2go (GO_REF:0000043) is retired — CFP29's superseded
"secreted antigen" identity **is still live in GOA** and EXP-backed:

- GO:0005576 extracellular region — **EXP (PMID:9596740)** + IEA (GO_REF:0000044,
  from the "Secreted" SubCell keyword).
- GO:0005886 plasma membrane — **EXP (PMID:9596740)** + IEA (GO_REF:0000044, from
  the "Cell membrane" keyword).

`GO_REF:0000044` is the UniProt **SubCell-location → GO CC** mapping — a *different,
still-active* pipeline from the retired kw2go — so these were not immunized away.

**Why not REMOVE:** the extracellular/membrane terms carry ECO:0000269 experimental
evidence (I have not read the PMID:9596740 full text), and the protein is
independently detected in **host-cell exosomes during infection** [UniProt,
ECO:0000269|PMID:20662102], so extracellular presence is genuine, not purely
artifactual.

**Why not core:** GO:0140737 is by definition intracellular, and UniProt itself now
attributes the culture-filtrate appearance to lysis: [UniProt SUBCELLULAR LOCATION
"Detected at low levels in short-term culture filtrate, the nanocompartment is very
stable and may survive cell lysis, explaining its apparent secretion (Probable)"].

**Decision:** GO:0140737 → ACCEPT (core, IDA+IBA; IEA redundant). GO:0005576 and
GO:0005886 (both EXP and IEA) → **KEEP_AS_NON_CORE** — genuine but secondary /
context-dependent, flagged for expert sign-off. Added a proposed **NEW** MF
(GO:0005198 structural molecule activity) to fill the MF gap, as for THEMA/enc.

## Relation to the SPKW project
Good complement to the maritimacin note in `projects/SPKW.md`: a **"superseded-identity"
keyword that was NOT immunized away** — it rides a still-active SubCell pipeline and
has EXP backing, so it requires an actual nuanced curation decision (KEEP_AS_NON_CORE)
rather than silent pipeline retirement.
