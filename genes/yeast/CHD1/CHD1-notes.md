# CHD1 curation notes

## 2026-10-01 current-GOA and IBA re-review

Reviewed *Saccharomyces cerevisiae* **CHD1/YER164W** after a forced UniProt/GOA
refresh. Chd1 is the conserved SNF2-family ATP-dependent chromatin remodeler that
slides nucleosomal DNA and spaces nucleosomes during transcription-coupled chromatin
reassembly; its yeast activity is directly supported by the foundational in vitro
work on purified Chd1p [PMID:10811623 "Biochemical experiments using Chd1p purified
from yeast showed that it reconfigures the structure of nucleosome core particles"]
and by later domain, genome-wide and structural papers.

### Source refresh

- The old review had **65** rows; live GOA now has **66** rows. The refreshed review
  has **82** rows: 65 active, 17 explicitly `retired: true`.
- `just fetch-gene yeast CHD1 --force` backfilled qualifiers and exact IBA donor
  sets for the live rows, added 17 live GOA rows that were missing from the old
  review, and left 17 historical source rows no longer present as exact current GOA
  assertions.
- The stale rows retained as retired are:
  - 9 old non-`GO:0005515` rows: the pre-refresh `GO:0000123`, keyword/ARBA/RHEA
    electronic rows for nucleotide binding, DNA binding, ATP binding, nucleus,
    chromatin organization, DNA-templated transcription, hydrolase activity and
    nucleosome organization.
  - 8 exact generic `GO:0005515 protein binding` IPI rows from older interactome
    screens: PMIDs 12242279, 14759368, 16429126, 16554755, 19536198, 20489023,
    21179020 and 37968396. These now all use `REMOVE`, because the bare protein
    binding term does not add an informative molecular function for a well
    characterized ATP-dependent remodeler.
- All 17 newly seeded live rows were reviewed. The new experimental/electronic rows
  restored SAGA/SLIK membership, ATP binding, nuclear/chromosomal localization,
  RNA Pol I/II transcription termination and elongation, ATP hydrolysis, and five
  IGI rows for `GO:2000104 negative regulation of DNA-templated DNA replication`;
  the latter were kept as non-core genetic-context phenotypes rather than core
  Chd1 process annotations.
- The obsolete/broad experimental `GO:0008094 ATP-dependent activity, acting on DNA`
  row from PMID:10811623 was changed to `MODIFY`, with replacement
  `GO:0140658 ATP-dependent chromatin remodeler activity`, because the
  Chd1-specific assay is ATP-dependent nucleosome remodeling rather than generic
  activity on naked DNA.

### IBA / PAINT review

All eight live IBA rows were checked against `interpro/panther/PTHR45623`.

- `PTN002473914` carries the Chd1-family IBD assertions for `GO:0000785 chromatin`,
  `GO:0005634 nucleus`, `GO:0003677 DNA binding`, `GO:0003682 chromatin binding`,
  `GO:0016887 ATP hydrolysis activity`, `GO:0042393 histone binding`,
  `GO:0140658 ATP-dependent chromatin remodeler activity` and `GO:0006338
  chromatin remodeling`. Budding-yeast Chd1 (`SGD:S000000966`) is inside this
  clade and appears in the PAINT evidence for all rows except the histone-binding
  row, where the placement is supported by mouse CHD paralogs.
- `PTN001326511` is the narrower eukaryotic Chd1-family node for
  `GO:0034728 nucleosome organization`; it is seeded by `SGD:S000000966`, so the
  IBA is explicitly target-grounded.
- Self appearance in `WITH/FROM` was retained as expected PAINT descendant
  evidence, not circularity. No target-specific loss was found for the inherited
  chromatin/nucleus/remodeling/DNA-binding/ATPase/nucleosome-organization calls.
  `GO:0042393 histone binding` was retained as non-core, because histone/nucleosome
  binding is a reasonable inherited property but is less direct than
  nucleosome-dependent ATPase/remodeler activity.

### Literature checked

Cached deep-research reports from Falcon and Perplexity agreed on the central
biology: Chd1 is a nuclear, monomeric chromatin remodeler that couples ATP
hydrolysis at SHL2 to nucleosome sliding and helps re-establish nucleosome
organization across active gene bodies after RNA Pol II passage.

Cached primary references read during the pass included:

- PMID:10811623 for ATP-dependent chromatin remodeling by purified budding-yeast
  Chd1.
- PMID:21623345 for the C-terminal SANT/SLIDE DNA-binding domain required for
  DNA/nucleosome binding and remodeling.
- PMID:21940898 and PMID:26861626 for the Isw1/Chd1 nucleosome-spacing role in
  genome-wide nucleosome organization.
- PMID:22922743, PMID:23468649 and PMID:25395991 for Chd1 recruitment to active
  transcribed regions and its role in transcription-coupled chromatin structure.
- PMID:33174727 for ATP-dependent remodeling and nucleosome unwrapping.
- PMID:34520455 for the non-core but valid role at sites of double-strand breaks.

The newer PubMed search for 2024-2026 Chd1/yeast papers found several mechanistic
or structural studies. The most curation-relevant hit was the peer-reviewed 2025
Nucleic Acids Research paper showing a direct interaction between the Chd1 CHCT
domain and the Paf1C subunit Rtf1 (PMID:40867051), updating the 2024 bioRxiv
preprint already summarized in the Falcon report. Also found but not action
changing were the 2025 abstract-only Chd1 exit-DNA unwrapping cryo-EM paper
(PMID:40453884) and a 2025 structural paper on Chd1 remodeling intermediates
(PMID:41439750). All reinforce the ATP-dependent chromatin-remodeler/nucleosome
spacing model and did not motivate additional GO assertions.

### Remaining uncertainty

`GO:0140002 histone H3K4me3 reader activity` remains `UNDECIDED`. Pray-Grant
et al. reported H3K4 methylation recognition for budding-yeast Chd1, but later
biochemical/structural studies argue that the yeast chromodomains lack the
aromatic cage used by human CHD1 and that Chd1 localization is mediated through
elongation factors rather than direct H3K4me3 reading. That is a real primary
literature conflict, not an IBA propagation issue, so the existing uncertainty was
left in place.
