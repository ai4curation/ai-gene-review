# NtR (Q9W288) Cys-loop hallmark residue comparison (re-review, 2026-10-20)

Script: `compare_motifs_rereview.py` (UniProt REST + MAFFT L-INS-i). Raw output: `compare_motifs_rereview.out`.
References: Dmel nAChRalpha2 P17644 (the only other model-organism member of PANTHER 19.0 subfamily PTHR18945:SF430), Dmel nAChRbeta1 P04755, human CHRNA7 P36544.

## PANTHER placement

PANTHER 19.0 classification files place Q9W288 in PTHR18945:SF430 (ACETYLCHOLINE RECEPTOR SUBUNIT ALPHA-LIKE 2-RELATED) together with nAChRalpha2 P17644; the UniProt cross-reference still gives PTHR36695:SF12 (AGAP008648-PA). The IBA rows on NtR descend from PTHR18945 PAINT nodes (PTN001054635, PTN000435923, PTN000434994, PTN001054960, PTN001825467).

## Findings

1. Cys-loop disulfide retained: NtR C337 and C351 align with the nAChRalpha2 C169-C183 Cys-loop pair, but the conserved FPFD motif inside the loop is replaced (NtR NWPSE versus FPFD in all three references).
2. Loop C vicinal cysteines absent: the nAChRalpha2 C243-C244 and CHRNA7 vicinal Cys pair, which defines acetylcholine-binding alpha subunits, aligns with NtR M412-M413 (within KGMMQK), with no cysteine pair anywhere in the NtR sequence after the signal peptide.
3. M2 selectivity ring absent: all three references share the GEK motif at the intracellular end of M2 (nAChRalpha2 SGEKIALCISILLS), which forms the cation-selective intermediate ring; the aligned NtR segment is STRRSSLILIALLIAAW (GEK aligns with RSS) and has no GEK or glutamate at this position.
4. Overall identity with nAChRalpha2 is low (85 identical aligned residues over about 580 positions, roughly 15%).

## Interpretation

The data support membership in the Cys-loop ligand-gated channel superfamily (Cys-loop, ligand-binding domain, four hydrophobic segments), but NtR lacks both the principal acetylcholine-binding determinant of alpha subunits and the cation-selectivity motif conserved across nAChRs. These are target-specific divergences from the ancestral nAChR state assumed by the PAINT nodes. They do not prove NtR cannot assemble with nAChR subunits, but they argue against transferring acetylcholine gating, cation/calcium selectivity or cholinergic synaptic roles from the subfamily.
