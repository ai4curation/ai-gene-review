# Msed_1700 (A4YHF3): ASD versus MCR paralog comparison

Script: `compare_asd_mcr.py` (run `uv run python compare_asd_mcr.py > results.txt`).
It fetches sequences and cross-references live from UniProt REST, so numbers can change
with UniProt releases. Raw output from the 2026-10-15 run is in `results.txt`.

## Questions

1. Is Msed_1700 closer to the true archaeal aspartate-semialdehyde dehydrogenases (ASDs)
   or to the malonyl-CoA reductases (MCRs) derived from them?
2. Does Msed_1700 keep the catalytic cysteine and histidine of the family?
3. Which proteins does UniProt name EC 1.2.1.75 in archaea, and do they split into MCR-type
   and ASD-type by conserved-domain (CDD) subfamily models?

## Results (2026-10-15 run)

Global pairwise identity to A4YHF3 (BLOSUM62, gap open -10, extend -0.5; identities over
the shorter sequence):

| Comparator | Identity |
|---|---|
| A4YEN2 Msed_0709, M. sedula MCR | 38.8% |
| Q96YK1 STK_21710, S. tokodaii MCR (structure 4DPK) | 40.5% |
| Q971Y6 STK_12420 (ST1242), S. tokodaii asd | 69.0% |
| Q57658 MJ0205, M. jannaschii ASD (structure 1YS4) | 44.3% |

Msed_1700 is far closer to the S. tokodaii asd gene product (ST1242) than to either MCR.
ST1242 is the RefSeq NP_377174 protein that Alber et al. 2006 assigned as the true asd of
S. tokodaii from its cluster with aspartokinase and threonine synthase (the NCBI GenPept
record for NP_377174 carries locus_tag ST1242, 350 aa).

Catalytic residues: positions aligned to S. tokodaii MCR Cys153 and His248 (the
nucleophile and acid/base of PMID:23325803) are Cys150 and His242 in Msed_1700. These match
UniProt's PIRSR active-site features (ACT_SITE 150 acyl-thioester intermediate; ACT_SITE
242 proton acceptor). Both residues are conserved in all five proteins, as expected for
the shared mechanism, so they do not discriminate ASD from MCR.

CDD subfamily models. Of the 40 archaeal UniProt entries named EC 1.2.1.75, 19 carry only
MCR-type models (cd23940 ASADH_C_MCR and/or cd24150 ASADH_MCR_N), 17 carry only ASD-type
models (cd18130 ASADH_C_arch_fung_like and/or cd02315 ScASADH_like_N), and 4 carry none.
Msed_1700 and ST1242 are in the ASD-type group; Msed_0709 and STK_21710 are in the MCR-type
group.

## Interpretation

- The sequence data place Msed_1700 with the archaeal/fungal ASDs, consistent with its
  genomic context (Msed_1698 threonine synthase, Msed_1699 aspartokinase).
- About 17 of the 40 archaeal entries named "malonyl CoA reductase" (EC 1.2.1.75) are
  probably true ASDs. The UniProt naming rule ARBA00067001 is conditioned only on FunFam
  3.40.50.720:FF:000411 plus the taxon Archaea, and that FunFam covers both paralogs.
- **Correction to the Msed_0709 notes:** NCBIfam TIGR00978 (asd_EA) and NF006416 are
  present on both Msed_0709 and Msed_1700 in current UniProt (A4YEN2 entry version 101).
  TIGR00978 therefore does not discriminate the paralogs. The CDD models do: cd23940 and
  cd24150 for MCR, and cd18130 and cd02315 for ASD.
- No experimental data exist for Msed_1700 itself. These are homology and context
  inferences.
