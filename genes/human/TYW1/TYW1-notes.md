# TYW1 (Q9NV66) curation notes

Session 2026-10-18, RADICAL_SAM project, reviewed together with the paralog TYW1B.

## Sources

- The asta deep-research file is retrieval-only and returned no TYW1-specific primary
  papers (all 20 hits are database/genome papers). Falcon failed (403). Primary literature
  was found through PubMed and cached with `just fetch-gene-pmids human TYW1`.
- No other wybutosine pathway genes (TRMT5, TYW2/TRMT12, TYW3, LCMT2/TYW4, TYW5) and no
  yeast TYW1 review exist in the repo, so there is nothing to align with.

## Biology

- Yeast: TYW1 is one of four genes needed for yW. [PMID:16642040 "TYW1 is an
  iron-sulfur (Fe-S) cluster protein responsible for the tricyclic formation."]
- Archaeal structure: TYW1 makes the tricyclic ring from m1G37. [PMID:17727881 "TYW1
  catalyzes the second step to form the tricyclic ring structure, by cyclizing
  N(1)-methylguanosine."] The model has SAM and two [4Fe-4S] clusters, and yeast
  mutagenesis supports it (abstract-only).
- Second substrate is pyruvate. [PMID:22026549 "only incubation with pyruvate resulted in
  formation of 4-demethylwyosine"] C1 leaves as CO2 [PMID:36326713].
- Auxiliary cluster: P. abyssi TYW1 binds a second [4Fe-4S] cluster through an extra
  cysteine motif, and this cluster binds pyruvate [PMID:23043105 "these additional
  cysteines are involved in the coordination of a second [4Fe-4S] cluster displaying a
  free coordination site that interacts with pyruvate"]. P. abyssi Cys45/58/71 align to
  human TYW1 C381/C394/C407 (file:human/TYW1B/TYW1B-bioinformatics/RESULTS.md).
- Flavodoxin domain: eukaryotic TYW1 is an FMN flavoenzyme [PMID:34184886 "eukaryal
  homologues contain a flavin binding domain in addition to the radical SAM domain"],
  shown for yeast Tyw1 (FMN co-purifies; NAD(P)H is enough for activity).
- Human evidence (direct): TYW1-knockout hESCs have no OHyW [PMID:38706838 "OHyW was
  completely undetectable in TYW1-knockout hESCs"]. Patient compound-heterozygous variants
  (R206C, R389Q) make the protein less stable and lower OHyW by more than 50%. In HeLa
  immunostaining, WT TYW1 is cytoplasmic, not nuclear [PMID:38706838 "both wild-type (WT)
  and two variants of TYW1 showed clear localization in cytoplasm but not nucleus"].
  Loss lowers UUU-codon translation.
- Disease: biallelic TYW1 variants cause primary microcephaly with cerebral palsy and
  intellectual disability. Tyw1-/- mice have neural proliferation and migration defects
  [PMID:34077496]. This is pleiotropic downstream biology, so no BP terms were added.
- In HEK293T pull-downs, TYW1 is a client of the human CIA targeting complex (MMS19/MIP18),
  consistent with a cytosolic Fe-S protein [PMID:28178521]. The MS identification may not
  tell TYW1 from TYW1B apart, so it is not used as primary support.
- Yeast TYW1 is induced by Yap5 under high iron [PMID:21917924]. This is yeast-specific
  regulation and is not annotated.

## Decisions

- GO:0003824 catalytic activity: MODIFY to GO:0102521 (project rule).
- GO:0051536: MODIFY to GO:0051539. GO:0051539: ACCEPT (two clusters, radical SAM and
  auxiliary).
- GO:0008033 tRNA processing: MODIFY to GO:0031591 wybutosine biosynthetic process (an
  is_a descendant via tRNA modification, already carried by IBA).
- GO:0010181 FMN binding: ACCEPT (flavodoxin domain; shown for the yeast ortholog).
- GO:0031591 IBA and GO:0102521 IEA: ACCEPT (human KO evidence supports them).
- NEW GO:0005737 cytoplasm (PMID:38706838 immunostaining). GOA has no CC row.
- GO:1904047 SAM binding is not in GOA. It goes in core_functions only, with no NEW row
  (it is a cofactor/cosubstrate entailment of the radical SAM activity).

## Open questions

- Was the TYW1 CRISPR knockout in hESCs (PMID:38706838) specific to TYW1, given that
  TYW1B is 95.7% identical? If it was, TYW1B does not make up for TYW1 loss in hESCs.
- Does human TYW1 sit at the ER membrane like yeast Tyw1 (the N-terminal hydrophobic
  segment)?
