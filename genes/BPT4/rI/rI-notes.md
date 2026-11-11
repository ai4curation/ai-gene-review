# Curation Notes: Bacteriophage T4 `rI` (Lysis inhibition regulator / Antiholin RI, P13304)

## Overview
- **Gene symbol:** `rI` (gpRI)
- **UniProt ID:** `P13304` (`RI_BPT4`)
- **Length:** 97 amino acids
- **Function:** Periplasmic antiholin that directly binds the periplasmic C-terminal domain of holin T (`t`) in a 2:2 heterotetramer (`T2-RI2`) to block holin oligomerization and delay host cell lysis (lysis inhibition, LIN) upon superinfection.

## Biological Role and Mechanism
- Historically, RI was proposed to possess an N-terminal signal-anchor-release (SAR) domain that tethered it transiently to the inner membrane before release into the periplasm and degradation by DegP (`PMID:17693511`).
- Subsequent biochemical and genetic work demonstrated that RI actually possesses a canonical Sec-translocated, signal peptidase I-cleavable N-terminal signal peptide (residues 1-24), releasing a mature 73-residue soluble periplasmic protein (`PMID:34456892`).
- In the periplasm, mature RI binds the periplasmic globular domain of holin T (`t`) in a `T2-RI2` heterotetrameric complex, inhibiting holin triggering and pore formation (`PMID:17693511`, `PMID:34456892`, PubMed 16166524, PubMed 31611409).
- Structural and biochemical studies indicate that the `T2-RI2` complex can bind periplasmic double-stranded DNA ejected by superinfecting T-even phages, stabilizing the inhibited state as the primary superinfection signal for lysis inhibition (LIN) (PubMed 31611409).

## Review of Existing GO Annotations
- `GO:0140678` (molecular function inhibitor activity, IEA, GO_REF:0000120): **ACCEPT**. Directly captures RI's core molecular function as an antiholin that binds and inhibits the pore-forming activity of holin T.
- `GO:0044229` (host cell periplasmic space, IEA, GO_REF:0000044 & EXP, `PMID:34456892`): **ACCEPT**. Both annotations are well supported; RI is cleaved by signal peptidase and functions as a soluble periplasmic protein that engages the periplasmic domain of holin T (`PMID:34456892`).
- `GO:0020002` (host cell plasma membrane, IDA, `PMID:17693511`): **KEEP_AS_NON_CORE**. The uncleaved precursor and signal-peptidase-defective RI remain associated with the *E. coli* inner membrane, and mature periplasmic RI is recruited to the inner membrane through its high-affinity complex with the integral inner-membrane holin T (`PMID:17693511`, `PMID:34456892`).
- `GO:0003677` (DNA binding, IEA, GO_REF:0000043): **KEEP_AS_NON_CORE**. Crystallographic and functional studies (PubMed 31611409) show that the holin-antiholin (`T-RI`) complex binds periplasmic dsDNA from superinfecting phages as a LIN signal, though dsDNA binding is a property of the assembled `T-RI` interface rather than the primary standalone function of free RI.
- `GO:0031640` (killing of cells of another organism, IEA, GO_REF:0000043): **MODIFY** to `GO:0039639` (suppression by virus of host cell lysis in response to superinfection). RI does not kill host cells; rather, it inhibits holin T to prevent premature host cell lysis when superinfection occurs.
