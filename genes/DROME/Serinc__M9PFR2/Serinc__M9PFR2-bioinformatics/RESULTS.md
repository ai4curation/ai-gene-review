# Serinc isoform F (M9PFR2): mapping the DmSERINC structure onto this accession

Input: `serinc_isoforms_and_TMS1.fasta` (UniProt REST; the six FlyBase Serinc products
PA Q9VV58, PB M9PI80, PC M9PCT1, PD M9PFH8, PE M9PFW5, PF M9PFR2, plus yeast TMS1 Q12116).
Script: `compare_isoformF_rereview.py`; raw output in `compare_isoformF_rereview_output.txt`.

The question this analysis answers: the only experimental study of the fly protein
(Pye et al. 2020, PMID:31907454; PDB 6SP2) numbers its residues according to **isoform A**
(Q9VV58 — all 18 residues named in that paper sit at the stated positions in isoform A, and
at none of the other isoforms' positions). M9PFR2 is a different splice product of the same
gene, so how much of the characterised protein does this accession actually contain?

## Result

- Isoforms A and F are identical over residues 1-365. Isoform A then carries three extra
  residues in the cytosolic loop between TM8 and TM9, after which the two sequences realign
  (A *n* = F *n*-3) and stay identical up to **A419 = F416**.
- From there they diverge completely: isoform A ends with
  `KPHSEIELFNGNEASMWVKIVSSWLGVFIYGWSLAAPIVLTNRDFS` (A420-465) and isoform F with an
  unrelated `NNFLFPQTSFGNRAVQRQRGFHVGQDRLQLAGCLHLWLEPCSAHCSYQSRL` (F417-467).
- Isoform F therefore retains **17 of the 18 structurally named DmSERINC residues**: both
  disulphides (C71-C95, C238-C299), the whole membrane-cytosol-interface pocket
  (Y42, Q136, W140, K143, Y395→F392, H401→F398) and the inter-subdomain hydrophilic cleft
  except one residue (Q181, Y282, Y285, S289, F177, T414→F411, W418→F415). The exception is
  the invariant **Lys438, which lies in the isoform-A-specific C-terminus and has no
  counterpart in isoform F**.
- UniProt's Phobius annotation gives isoform A nine transmembrane helices, the last at
  439-459; isoform F has eight, the last at 396-416. The divergent isoform-F C-terminus is
  not predicted to be membrane-spanning. In the cryo-EM structure the final helix TM10
  belongs to subdomain B, so the substitution is not a trivial tail swap.

## Consequences for annotation

- The lipid-binding groove of subdomain B is "formed by TM5, 7, 8 and the C-terminal end of
  TM4" (PMID:31907454) — all of it inside the region isoform F shares with isoform A. The
  acyl chain seen in the cryo-EM map, and the phosphatidylserine-sensitive HDX region, are
  therefore expected to be present in isoform F.
- Subdomain B as a whole (TM5, TM6, TM7, TM10) is **not** intact in isoform F, and the
  extracellular cleft loses Lys438. Any claim about isoform F's lipid handling is an
  inference from the shared region, not a measurement.
- Global identity between isoform F and yeast TMS1 (Q12116) is low; the earlier run in
  `genes/DROME/Serinc/Serinc-bioinformatics/` measured 141 identical positions for isoform C
  over a global alignment. Yeast-specific localization or phenotypes are not transferable.

## Limits

- No experiment has used isoform F. Whether it is translated at a meaningful level, and
  whether the alternative C-terminus changes folding, oligomerisation or targeting, is
  untested.
- Phobius helix counts are predictions; the cryo-EM structure resolves ten helices for
  isoform A where Phobius predicts nine.
