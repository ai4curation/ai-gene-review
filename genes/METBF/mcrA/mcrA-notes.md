# mcrA (P07962, MCRA_METBF) — Methanosarcina barkeri Fusaro MCR alpha

Part of the cross-clade MCR review (`projects/ARCHAEA/mcrA-across-clades.md`);
Methanosarcinales representative alongside M. acetivorans.

## Literature search

No deep-research provider key is configured (checked 2026-11-13); hand-written notes
from the UniProt-cited papers and PubMed searches for M. barkeri Fusaro physiology.

## Evidence

- Crystal structure (PDB 1E6Y, 1.6 A): active site almost identical to Methanothermobacter
  MCR; four of the five modified residues present [PMID:11023796 "four of the five
  modified amino acid residues of MCR from M. thermoautotrophicum, namely a thiopeptide,
  an S-methylcysteine, a 1-N-methylhistidine and a 5-methylarginine were also present"].
  The missing one is 2-methylglutamine.
- Didehydroaspartate present [PMID:27467699 "in MCR of phylogenetically distantly related
  Methanosarcina barkeri"].
- Substrates: H2/CO2, methanol, acetate [PMID:11929975 "The mutant was unable to grow on
  methanol/H(2)/CO(2), H(2)/CO(2), or acetate ... but showed wild-type growth rates with
  methanol as sole substrate."] (wild type grows on all).
- Residue comparison: Tyr444 (P11558 numbering, coenzyme M contact) is Phe464 here, as
  in M. acetivorans; otherwise conserved.

## Review decisions (2026-11-13)

- IEA/ISS rows ACCEPT.
- GO:0015948 -> MODIFY to all three supported children: GO:0019386 (CO2), GO:0019387
  (methanol), GO:0019385 (acetate). Same rule applied to METAC in the harmonization.
- NEW (IDA, PMID:11023796): GO:0044674 complex, GO:0046906 tetrapyrrole binding.
