# LtaS2 / YflE (UniProtKB:O34952) notes

## Identity
- UniProt O34952 = LTAS2_BACSU, gene `ltaS2`, synonym `yflE`, locus BSU07710.
- In the primary literature (Gründling & Schneewind 2007 PMID:17483484; Wörmann
  et al. 2011 PMID:21255105; Schirner et al. 2009 PMID:19229300) this protein is
  called **LtaS(BS)** / **YflE** and is the **major, housekeeping LTA synthase**.
  Schirner et al. renamed `yflE` as `ltaS`.
- Bona-fide polyglycerolphosphate LTA synthase; restores growth + LTA in an
  S. aureus ltaS depletion strain [PMID:17483484 "anhydrotetracycline-inducible
  expression of staphylococcal ltaS or B. subtilis yflE restored both LTA
  glycerol phosphate synthesis and bacterial growth"]. UniProt MISCELLANEOUS:
  "Restores staphylococcal growth after ltaS depletion".
- Mn2+-dependent; uses phosphatidylglycerol; active-site Thr nucleophile
  (orthologue mechanism PMID:19168632). PDB 2W8D = extracellular domain
  (residues 215/216-649).

## CMMMech cross-reference (data/records/thulium.yaml) — do NOT edit CMMMech
CMMMech grounds the B. subtilis thulium-biosorption mechanism to the four LtaS
paralogues. Three issues in its protein annotations for this entry (worth an
upstream note; the accession→record identity O34952=LtaS2 is correct):

1. **Synonym swapped.** CMMMech labels O34952 "LtaS2 / **YfnI**". UniProt and the
   literature have O34952 = ltaS2 = **yflE**; `yfnI` is the *other* entry
   (Q797B3). CMMMech has the yfnI/yflE synonyms reversed between O34952 and
   Q797B3.
2. **Locus tag wrong.** CMMMech gives "BSU07260" for O34952. UniProt:
   O34952 = **BSU07710**; BSU07260 is Q797B3.
3. **EC number wrong.** CMMMech asserts **EC 2.7.8.40** for all four paralogues.
   EC 2.7.8.40 is UDP-N-acetylgalactosamine-undecaprenyl-phosphate
   N-acetylgalactosaminephosphotransferase (an Aeromonas O-antigen enzyme),
   unrelated to LTA synthesis. UniProt assigns these proteins **EC 2.7.8.-**
   (no specific sub-number); the reaction is a glycerophosphotransferase.

The CMMMech record's overall biosorption claim is appropriately hedged (WT ~90%
vs LTA-defective ~74% Tm(III) removal; residual non-LTA binding; no Tm-specific
EXAFS/FTIR), so the mechanism framing is sound; only the per-protein identity
fields above are in error.
