# POB3 Notes

## 2026-09-28 IBA and literature re-review

### IBA

GOA contains one IBA row for POB3: `GO:0035101 FACT complex`, with
`PANTHER:PTN002492356` in the WITH/FROM column. The cached PAINT export for
`PTHR45849 FACT COMPLEX SUBUNIT SSRP1` places the FACT-complex IBD on
`PTN002492356`, a eukaryotic node seeded by direct FACT-complex annotations from
S. cerevisiae POB3, fission yeast `pob3`, Drosophila `Ssrp`, Arabidopsis SSRP1,
and vertebrate SSRP1 descendants. The budding-yeast target is present among the
IBA donors because it helped seed the ancestral node; that is expected PAINT
behavior, not circularity. I kept the row as `ACCEPT` and marked the propagation
review `NO_FAILURE_CORE`.

### Cached literature

- Brewster et al. characterized Cdc68/Spt16 and Pob3 as the abundant CP complex
  and localized the function to the Spt16-Pob3 dimer [PMID:9705338].
- Wittmeyer et al. showed that purified Spt16 and Pob3 form a stable, abundant
  heterodimer that is nuclear/chromatin-associated and linked to DNA polymerase
  alpha/primase [PMID:10413469]; the preceding Pol alpha affinity study already
  identified both Spt16 and Pob3 as Pol1-binding proteins [PMID:9199353].
- Schlesinger and Formosa isolated `pob3` mutants and showed defects in both
  transcription and replication, including hydroxyurea sensitivity and delayed S
  phase progression [PMID:10924459].
- Formosa et al. showed that Nhp6-bound nucleosomes recruit Spt16-Pob3 to form
  SPN-nucleosomes with altered mobility and DNase I sensitivity; the same paper
  explicitly notes that yeast Pob3 lacks the HMG1 DNA-binding motif present in
  metazoan SSRP1 [PMID:11432837].
- Ruone/Rhoades/Formosa and later Rhoades/Ruone/Formosa established the
  two-step Nhp6 then Spt16-Pob3 nucleosome-reorganization mechanism in vitro
  [PMID:12952948, PMID:15082784], and Xin et al. refined the model by showing
  that yFACT increases nucleosomal DNA accessibility without obligatory
  H2A-H2B dimer displacement [PMID:19683499].
- VanDemark et al. mapped overlapping essential roles for the Spt16 N-terminal
  domain and Pob3 middle domain and connected yFACT to multiple histone contacts
  [PMID:18089575]. Hoffmann and Neumann later mapped Pob3's acidic C terminus as
  the major in vivo H2A-H2B contact surface, found the C-terminal NLS, and
  linked the CTD deletion to hydroxyurea sensitivity [PMID:26414936].
- The Pol II transcription annotations are grounded in the older elongation and
  initiation papers [PMID:14585989, PMID:15987999]. Martin et al. showed in 2018
  that FACT occupancy on S. cerevisiae chromatin is transcription-dependent and
  preferentially tracks RNAP-disrupted nucleosomes [PMID:30237209]; Pathak et
  al. connected FACT recruitment to histone H3 acetylation genome-wide
  [PMID:29695490].
- Shukla et al. extended Spt16/FACT biology to Pol III-transcribed loci, showing
  Spt16 enrichment near the 3' end of all Pol III genes and stress-responsive,
  gene-specific effects on downstream nucleosome positioning and Pol III output
  [PMID:33277439].

### Newer papers searched

Recent yeast FACT papers add useful mechanistic context but do not require new
GO assertions for POB3 beyond FACT complex membership, histone/nucleosome
binding, and participation in chromatin-based transcription and replication.
Byrd et al. tested fourteen `PMA1` 3'-end deletion alleles and found that one
modestly increased Spt16 occupancy while also retaining some Pol II and altering
nucleosome occupancy at the same 3' region [PMID:39103906]. Barman et al. used
Pob3/Spt16 TAP-MS in soluble and insoluble fractions to expand the FACT
interaction network and to show that San1-dependent regulation of Spt16 changes
associations with epigenetic, transcription, and repair factors [PMID:39855624].

### Curation decisions

- Retained the IBA `GO:0035101 FACT complex` as a sound conserved complex
  inference from `PANTHER:PTN002492356`.
- Switched the UniProt-keyword `GO:0006351 DNA-templated transcription` row to
  `ACCEPT`, because the broad process is a core FACT role and is already used in
  the transcription core function.
- Changed the generic `GO:0005515 protein binding` IPI rows without a histone
  WITH/FROM partner to `REMOVE` and the HHT2-backed rows to `MODIFY` toward
  `GO:0042393 histone binding`. The AP-MS and targeted interaction evidence is
  real, but the bare parent term is uninformative; the review captures the
  interpretable interactions as FACT complex membership, nucleosome binding,
  histone binding, replication, and transcription/chromatin organization.

## 2026-10-01 current-GOA refresh

- Forced `just fetch-gene yeast POB3 --force`. Current GOA has 33 rows. Ten rows were newly seeded from current IntAct, UniProt, ComplexPortal, and SGD data; nine older source rows disappeared from GOA and were retained as `retired: true`.
- Re-fetched the PTHR45849 PAINT cache. Current PAINT still has the `GO:0035101` FACT-complex IBD at `PANTHER:PTN002492356` with `taxon:2759`; no IBA action change was needed, and the `propagation_review.source_entities` entry now traces that PTN node per the IBA campaign convention.
- Reviewed newly seeded rows as one `REMOVE` and two `MODIFY` calls for generic `GO:0005515` protein-binding IntAct assertions and seven `ACCEPT` calls for current nucleus, chromosome, DNA-templated-replication, DNA replication-dependent chromatin assembly, and FACT-complex rows.
- Preserved nine no-longer-live source rows as retired: four old UniProt-keyword IEAs, four old generic protein-binding IPI rows, and the old ComplexPortal `GO:1902275` regulation of chromatin organization row.
- `just fetch-gene-pmids yeast POB3` confirmed all 28 PMID-backed references are cached, fetching full text for `PMID:32701054`. Web/PubMed searches for 2025-2026 `POB3`/`Pob3`/`FACT` found no newer direct yeast POB3 paper that changes the review beyond the already cached 2025 FACT TAP-MS paper.

## 2026-10-03 PR review follow-up

- Replaced the transcription core function's retired `GO:0006351
  DNA-templated transcription` process with `GO:0140673 transcription
  elongation-coupled chromatin remodeling`, and proposed a matching `NEW` row
  supported by Mason/Struhl, Martin/Howe, and Pathak/Govind.
- Removed the DNA-repair core function and demoted the retired UniProt-keyword
  `GO:0006281 DNA repair` row to `KEEP_AS_NON_CORE`; UniProt links FACT to
  repair-related chromatin transactions, but the cached yeast POB3 literature
  does not directly establish a separable DNA-repair core function.
- Changed the three `GO:0005515 protein binding` IPI rows with
  `UniProtKB:P61830`/HHT2 in WITH/FROM to `MODIFY` with `GO:0042393 histone
  binding` as the replacement, while leaving SPT16/RFA1 generic-binding rows as
  `REMOVE`.
- Clarified that the retired ComplexPortal `GO:1902275 regulation of chromatin
  organization` row is now superseded by current `GO:0006335
  DNA replication-dependent chromatin assembly`, and tightened the two broad SGD
  `GO:0006325 chromatin organization` rows so they describe the generic
  biochemical nucleosome-reorganization evidence rather than the narrower
  transcription or replication contexts.
