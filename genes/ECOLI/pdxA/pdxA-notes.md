# pdxA review notes (E. coli K-12, P19624)

Reviewed as the experimental exemplar of step 4 of the DXP-dependent de novo
PLP module (`modules/pyridoxal_5_phosphate_biosynthesis.yaml`) and the seed of
PAINT node PTN002408757 (PTHR30004).

## Provenance of this review

- No deep-research provider was available in this environment (no provider API
  keys), so no `-deep-research-<provider>.md` file exists or was fabricated.
  The review was built from the reviewed UniProt record and the cached
  publications below.
- Literature checked (all abstract-only in the cache): PMID:12896974
  (crystal structure), PMID:15026039 (product identification), PMID:2670894
  and PMID:1537800 (genetics), PMID:10225425 (PdxA/PdxJ reconstitution).
  PMID:24561554 and PMID:24627523 are proteome-scale Y2H papers (full text
  cached; PdxA is only in supplementary tables).
- The 1998 JACS paper (Cane et al., DOI:10.1021/ja9742085, UniProt Ref.5)
  carries the kinetics and metal data but has no PMID and is not cached.

## Function

- PdxA oxidizes HTP with NAD(P)+; the product decarboxylates to AHAP.
  [file:ECOLI/pdxA/pdxA-uniprot.txt "Catalyzes the NAD(P)-dependent oxidation
  of 4-(phosphooxy)-L-threonine (HTP) into 2-amino-3-oxo-4-(phosphooxy)butyric
  acid which spontaneously decarboxylates to form 3-amino-2-oxopropyl phosphate
  (AHAP)."]
- AHAP is the released product. [PMID:15026039 "confirms that AHAP is the
  product of the PdxA-catalyzed reaction"]
- Structure: tight homodimer, active site at the interface, one Zn2+ per site.
  [PMID:12896974 "A Zn2+ ion is bound within each active site, coordinated by
  three conserved histidine residues from both monomers."]
- Metal promiscuity. [file:ECOLI/pdxA/pdxA-uniprot.txt "Can use ions such as
  Zn(2+), Mg(2+) or Co(2+)."]
- PdxA + PdxJ + DXP make PNP; PNP, not pyridoxine, is the first vitamer.
  [PMID:10225425 "The first vitamin B6 vitamer synthesised is PNP, and not
  pyridoxine."]

## Curation decisions

- `GO:0042823` rows (IBA, IEA, two IMP) -> MODIFY to `GO:0036001` de novo PLP
  biosynthesis: PdxA acts only in the de novo route. Same call on PSEPK pdxA
  and both pdxJ orthologs. PdxH keeps `GO:0042823` because it also serves
  salvage.
- `GO:0008615` pyridoxine biosynthetic process rows -> ACCEPT. GO has no PNP
  biosynthesis term; this is the term used for the PNP-forming branch. Caveat
  recorded: free pyridoxine is not the product (PMID:10225425).
- Zn/Mg/Co ion binding and NAD binding -> KEEP_AS_NON_CORE (cofactors);
  generic metal ion binding -> TOO_GENERAL.
- `GO:0042802` identical protein binding (two Y2H IPI rows) -> MODIFY to
  `GO:0042803` protein homodimerization activity, which the protein carries by
  IDA (crystal structure); that row is KEEP_AS_NON_CORE.
- `just paint-losses ECOLI pdxA`: no IRD/IKR on the lineage.
- Cytoplasm KEEP_AS_NON_CORE (location as context), the same treatment as the
  cytosol rows of PdxJ (fixed by the P. putida TreeGrafter re-review) and PdxH.
