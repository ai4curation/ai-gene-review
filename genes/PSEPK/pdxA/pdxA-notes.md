# pdxA review notes (P. putida KT2440, Q88QT5, PP_0402)

Step 4 of the DXP-dependent de novo PLP module
(`modules/pyridoxal_5_phosphate_biosynthesis.yaml`).

## Provenance

- Sources: reviewed UniProt record (all functional statements HAMAP
  MF_00536-derived, PE 3), the OpenScientist deep-research file, and the
  E. coli ortholog literature (PMID:12896974, PMID:15026039; abstract-only).
- No experimental study of PP_0402 itself was found by the deep-research run
  [file:PSEPK/pdxA/pdxA-deep-research-openscientist.md "A directed PubMed
  search during this investigation returned **no experimental study of the
  *P. putida* PP_0402 protein specifically**"].
- No IBA rows: QuickGO shows PAINT IBA only on PANTHER reference proteomes
  (E. coli P19624 carries the PTN002408757 IBAs), so their absence here says
  nothing about node placement.

## Function

- Reaction: [file:PSEPK/pdxA/pdxA-uniprot.txt "Catalyzes the NAD(P)-dependent
  oxidation of 4-(phosphooxy)-L-threonine (HTP) into
  2-amino-3-oxo-4-(phosphooxy)butyric acid which spontaneously decarboxylates
  to form 3-amino-2-oxopropyl phosphate (AHAP)."]
- Orthology: [file:PSEPK/pdxA/pdxA-deep-research-openscientist.md "Q88QT5 is
  **61.9 % identical (gap-free in the core)** to the *E. coli* PdxA"]
  (provider's alignment; not re-run).

## Curation decisions (2026-11 completion)

- Fixed action/reason mismatches in the earlier draft: `GO:0042823` was
  KEEP_AS_NON_CORE while arguing for the de novo child; it is now MODIFY ->
  `GO:0036001`, and the separate NEW `GO:0036001` row was dropped because the
  MODIFY replacement carries it. `GO:0046872` metal ion binding was
  MARK_AS_OVER_ANNOTATED while arguing redundancy; it is now TOO_GENERAL.
- Cytoplasm kept KEEP_AS_NON_CORE (location as context), consistent with the
  E. coli PdxA and the PdxJ/PdxH location rows of this pathway.
- Removed the reference to the GOA tsv (never support).
- Actions mirror genes/ECOLI/pdxA term by term.
