# pdxH review notes (E. coli K-12, P0AFI7)

Step 6 (terminal oxidation) of the DXP-dependent de novo PLP module; seed of
PTHR10851 PAINT nodes PTN008507293 (GO:0004733), PTN000091366 (GO:0042823) and
PTN000091428 (cytosol). The PTHR10851 family review uses yeast PDX3 as its
reference protein.

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Sources: the
  reviewed UniProt record and cached publications PMID:7860596, 9693059,
  11786019, 7696318, 15858270, 16562115 (abstract-only), PMID:34019876 (full
  text) and PMID:18304323 (cytosol proteome).
- `just paint-losses ECOLI pdxH`: no IRD/IKR on the lineage (the family's only
  IRD, PTN000852082, is in Actinomycetales).

## Function

- [PMID:7860596 "In the presence of molecular oxygen, the PdxH enzyme uses PNP
  or PMP as a substrate (Km = 2 and 105 microM and kcat = 0.76 and 1.72 s-1 for
  PNP and PMP, respectively) and produces hydrogen peroxide."]
- [PMID:7860596 "Comparison of kcat/Km values suggests that PNP rather than PMP
  is the in vivo substrate of E. coli PdxH oxidase."]
- Hydride to FMN: [PMID:11786019 "A hydrogen atom is removed from C4' during the
  oxidation and a pair of electrons is transferred to tightly bound FMN."]
- Both routes: [PMID:34019876 "responsible for the last step of PLP
  biosynthesis and is also involved in the PLP salvage pathway."]
- PLP allosteric "arginine cage" at the subunit interface (PMID:34019876).
- PMID:7696318 reported a monomer for the MBP-fusion-derived protein, contradicted
  by later homodimer findings [PMID:9693059 "Both the holo- and apoenzymes were
  homodimers."]; marked DISPUTED in reference_review.

## Curation decisions

- GO:0004733 (all five rows) ACCEPT; its definition covers PMP and PNP oxidation.
- FMN binding ACCEPT (catalytic prosthetic group), consistent with PDX3 and PNPO.
- GO:0042823 ACCEPT (both routes) plus GO:0036001 (IMP) ACCEPT and NEW
  GO:0009443 salvage; GO:0008615 -> MODIFY to GO:0042823 (PdxH does not build
  the pyridoxine ring); GO:0042816 TOO_GENERAL.
- GO:0016491 and GO:0016638 -> MODIFY to GO:0004733.
- PLP binding (allosteric) KEEP_AS_NON_CORE; homodimerization and
  protein-containing complex KEEP_AS_NON_CORE; cytosol rows KEEP_AS_NON_CORE
  (consistent with PdxJ).
- Phosphate ion binding (IDA, crystal) MARK_AS_OVER_ANNOTATED: in vitro ligand
  of unknown relevance.
- Riboflavin binding (IDA, PMID:15858270) -> MODIFY to FMN binding: the bound
  flavin is FMN and GO:0010181 is not a descendant of GO:1902444. Full text not
  seen; possibly a term-selection error upstream, not recorded as a source
  defect without the full text.
