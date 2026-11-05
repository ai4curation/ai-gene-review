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

### The underlying biosorption paper
The experimental grounding for that record is Moriwaki et al. 2013
[PMID:22684329 "The maximum adsorption capacities for Tm(III) by WT and ∆LTA
powders were 43 and 37 mg g(-1), respectively"], who compared freeze-dried cell
powders of B. subtilis 168 wild type and an LTA-defective strain and concluded
[PMID:22684329 "These results indicate that rare earth ions are adsorbed to
functional groups, such as phosphate and carboxyl groups, of lipoteichoic
acid"]. Two cautions for anyone reading the CMMMech record against this paper:

- The cached record is **abstract only**. The abstract gives maximum capacities
  (43 vs 37 mg/g for Tm(III)) and states only that [PMID:22684329 "Removal (in
  percent) of Tm(III), La(III), and Eu(III) from aqueous solution by WT powder
  was greater than by ∆LTA powder"]. The ~90% / ~74% removal figures that
  CMMMech reports are not in the abstract; they presumably come from the full
  text, and should be checked there before being repeated.
- The abstract does not say which gene the LTA-defective strain is mutated in,
  so this paper does not by itself attribute the lost adsorption to O34952
  rather than to another of the four paralogues. The attribution to LtaS2 rests
  on LtaS2 being the major vegetative synthase (PMID:21255105, PMID:19229300),
  not on anything stated in PMID:22684329.

The adsorption itself is a property of the LTA polymer, not an activity of this
enzyme, so nothing from this paper is used as support for any annotation in the
review; it is recorded here as the provenance of the CMMMech record.
