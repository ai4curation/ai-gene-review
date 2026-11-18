# mvd1 (Aspergillus fumigatus Af293) review notes

## 2026-11-18 manual review

UniProt Q4WNV9 (MVD1_ASPFU), ordered locus AFUA_4G07130, 404 residues, PE 3 (inferred from
homology). PANTHER PTHR10977:SF3. No deep-research provider keys are configured here, so no
provider file was generated; this review uses the UniProt record, the cached papers and the
searches below.

### Literature searches (Europe PMC, 2026-11-18)

- `"Aspergillus fumigatus" AND (mvd1 OR erg19 OR AFUA_4G07130)` (29 hits) and `"Aspergillus
  fumigatus" AND ("mevalonate diphosphate decarboxylase" OR "diphosphomevalonate decarboxylase" OR
  "mevalonate pyrophosphate decarboxylase")` (41 hits): no paper characterises the A. fumigatus
  protein. Hits are reviews, transcriptomics, PTM proteomics and terpene work.
- The two papers UniProt cites (PMID:16110826, PMID:22106303) are pathway context and do not
  name mvd1 in the cached text.
- The closest characterised ortholog is A. oryzae AoErg19 (Sun et al. 2019, PMID:31156588, full
  text cached). A 2025 review (PMID:40221522) lists Afu4g07130 as the single A. fumigatus ERG19
  (MVD1) [PMID:40221522 "In the pathogenic fungi A. fumigatus, C. neoformans and C. albicans there
  are single gene copies for ERG12, ERG8, ERG19 (MVD1), IDI1, and ERG20 (Table 1)"]. Its list of
  genes shown essential in A. fumigatus names erg10, erg12, erg8 and erg20 but not mvd1, so
  essentiality of mvd1 has not been reported.

### Evidence

- A. fumigatus pathway context: about 20 ergosterol genes [PMID:16110826 "About 20 genes are
  involved in the A. fumigatus ergosterol biosynthesis pathway."]; mevalonate is shared between
  ergosterol and the TAFC siderophore [PMID:22106303 "Here we demonstrate a link between TAFC and
  ergosterol biosynthetic pathways, which are both critical for virulence and treatment of fungal
  infections."]. Mvd1 acts downstream of the mevalonate branch point, on the ergosterol/isoprenoid
  side.
- A. oryzae AoErg19: complements S. cerevisiae erg19 and restores its ergosterol [PMID:31156588
  "Aoerg19/erg19 transformants can recover the ergosterol deficiency of the erg19 mutant"];
  overexpression lowers ergosterol [PMID:31156588 "Overexpression of Aoerg19 decreased the
  ergosterol content in A. oryzae, which may due to the feedback-mediated downregulation of
  Aoerg8."]; overexpression and RNAi strains are stress-sensitive and sporulate late.
- Localization: AoErg19 has no predicted targeting signal [PMID:31156588 "Bioinformatic analysis
  showed that there were no specific targeting signal sequences in the amino acid sequence of
  AoErg19"], yet its DsRed fusions, which are the overexpression constructs [PMID:31156588 "To
  construct the overexpression vector, the CDS of Aoerg19 was fused to DsRed at the C- and
  N-terminal of AoErg19 using fusion PCR"], co-localised with vacuolar markers. A soluble protein
  without a signal peptide would reach the vacuole lumen only through autophagy or degradation, so
  this result is more plausibly turnover of an overexpressed fusion than the working location of
  the enzyme. The S. cerevisiae ortholog, tagged at its chromosomal locus, is cytoplasmic
  (PMID:14562095), and mammalian MVD, the PAINT cytosol seed, is cytosolic (PMID:14972328). The
  cytosol rows are accepted. The question is open in Aspergillus and is flagged as a suggested
  experiment.

### PANTHER / PAINT

- Leaf PTN002590614, under PTN000104601 > PTN000104602 (all eukaryotes) > PTN000861730 >
  PTN000104603 > ... > PTN000104638 > PTN002250703 > PTN002590613. The same path as S. cerevisiae
  MVD1 and C. albicans MVD down to PTN000104638. No IRD/IKR (`just paint-losses ASPFU mvd1`).
- PTHR10977 has no fungal ergosterol IBD node (unlike PTHR43290 PTN000825284 for erg12 and
  PTHR31814 PTN001274236 for erg8), so A. fumigatus mvd1 is the only enzyme of the A. fumigatus
  mevalonate-to-IPP segment without an ergosterol biosynthesis row.

### Decisions

- Accept the GO:0004163, GO:0019287, cytosol and GO:0008299 rows.
- GO:0016831 carboxy-lyase activity: TOO_GENERAL (IPR005935 also covers phosphomevalonate
  decarboxylases).
- NEW GO:0006696 ergosterol biosynthetic process (ISS). Participation: Mvd1 catalyses the
  IPP-forming step of the mevalonate segment that GO and SGD place in ergosterol biosynthesis.
  Comparator check (positive): A. fumigatus erg12 and erg8 carry GO:0006696 by IBA, S. cerevisiae
  MVD1 by IDA/RCA, and C. albicans MVD by IEA. Experimental support is the A. oryzae ortholog's
  rescue of yeast erg19 ergosterol deficiency and the effect of AoErg19 overexpression on
  ergosterol.
