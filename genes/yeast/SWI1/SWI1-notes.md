# SWI1 curation notes

## 2026-09-29 - IBA source alignment

- Rechecked the four SWI1 IBA rows against the current `PTHR13964` PAINT snapshot.
  `PTN000359478` still carries `GO:0006357` regulation of transcription by RNA polymerase
  II and `GO:0005634` nucleus, and the transfers remain valid for S. cerevisiae Swi1.
- Preserved the existing `REMOVE` decision for `GO:0000976` transcription cis-regulatory
  region binding. The PAINT row is seeded by human ARID5B/MRF2 evidence from a different
  subfamily at the Opisthokont ARID/SWI1-family node, whereas yeast Swi1's ARID is weak
  and nonspecific and Swi1 is better captured as a SWI/SNF scaffold that contributes to
  nucleosome engagement.
- `PTN002303792` still carries `GO:0016514` SWI/SNF complex on the fungal Swi1 node with
  Candida, S. pombe, and S. cerevisiae descendant evidence, so the complex-membership IBA
  was kept as core.
- Converted the legacy `GO:0005515` protein binding IPI rows to `REMOVE`. These
  interactions are biologically real but are represented more informatively as SWI/SNF
  complex membership, RNA polymerase II-specific DNA-binding transcription factor binding,
  and nucleosome binding.
- Searched 2025+ PubMed for `SWI1`, `YPL016W`, `ADR6`, and `GAM3` with
  `Saccharomyces cerevisiae`. The only exact hits were PMID:40004101, a yeast-prion paper
  touching Swi1's N-terminal prion-forming region, and PMID:40768430, a Colletotrichum
  CgSwi1 virulence paper; neither changes the propagated SWI/SNF annotation calls.

## 2026-10-01 - current-GOA refresh

Forced a current GOA refresh and reviewed all 29 live source rows. The refresh
seeded three live rows not present as exact rows in the prior review: the
InterPro2GO `GO:0003677` DNA-binding row, the ComplexPortal `GO:0016514`
SWI/SNF-complex row from PMID:28249159, and a second exact PMID:11865042
`GO:0061629` transcription-factor-binding row for Hap4
(`SGD:S000001592`). The DNA-binding row was kept as non-core because Swi1 has a
weak, nonspecific ARID domain but functions in intact SWI/SNF as a nucleosome
engagement and activator-recruitment subunit. The two direct SWI/SNF-complex and
activator-binding rows were accepted.

Fourteen older exact rows no longer appear in the live GOA feed and are
preserved as `retired: true`: the older GO_REF:0000120 DNA-binding row; three
UniProt-keyword GO_REF:0000043 transcription, zinc-ion-binding, and
metal-ion-binding rows; and ten aggregate `GO:0005515` protein-binding IPI
rows. The protein-binding assertions were already marked `REMOVE` because
SWI/SNF complex membership, Pol II activator binding, and the proposed
nucleosome-binding function capture those interactions at higher specificity.

The current `PTHR13964` PAINT cache still places `GO:0006357`, `GO:0005634`,
and the over-broad `GO:0000976` cis-regulatory-region-binding assertion at
`PANTHER:PTN000359478`. It still places the accepted `GO:0016514` SWI/SNF
complex assertion at the fungal Swi1 node `PANTHER:PTN002303792`. The IBA
action calls therefore remain unchanged.

PMID:39235627 was checked as a newer direct 2024 publication. Its Ino2
activation-domain mapping strengthens the core activator-binding interpretation
for Swi1 without changing the GO term selection.
