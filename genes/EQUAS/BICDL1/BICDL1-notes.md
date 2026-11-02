# BICDL1 (donkey, A0A9L0JLY3) notes

DONKEY40 cohort review. Evidence: donkey UniProt TrEMBL record (PE 4, predicted; no comment lines), donkey
GOA (2 TreeGrafter IEA rows), human Swiss-Prot Q6ZP65 fetched to `BICDL1-bioinformatics/`, and a
donkey-human pairwise comparison (`BICDL1-bioinformatics/RESULTS.md`). No cached publications exist for this
gene; human BICDL1 functional text is itself transferred from mouse Bicdl1/BICDR-1 (A0JNT9, ECO:0000250).
No deep-research provider call was made.

## Sequence

- 573 aa vs human 573 aa; 95.99% identity over 524 paired residues, 91.45% coverage of each
  [file:EQUAS/BICDL1/BICDL1-bioinformatics/RESULTS.md "with 95.99% identity across 524 paired residues"].
- The donkey model lacks human residues 255-303 (inside the long central coiled coil) and instead contains
  donkey 389-436, which matches the extra exon of human isoform 2 [human UniProt VAR_SEQ 436 "T ->
  TGSRRLDDDSLEEQIRQTSEDSRALRELMEGERGKLRQSLEELQRLH SQ (in isoform 2)"; donkey alignment shows
  SSRRIDDDSLEEQIRQTSEDSRALRELMEGERGKLRQSLEELQRLHSQ]. So the donkey entry is an alternative splice form;
  its effect on adaptor length/dynein recruitment is unknown.
- CC1 box (dynein light intermediate chain binding motif) conserved [RESULTS.md "MOTIF (CC1 box): human
  [113, 114, 115, 116, 117] AARLG -> donkey [114, 115, 116, 117, 118] AARLG."]. C-terminal BICDL1/2-like
  domain (Rab6-binding region in the family) present (donkey 489-541, Pfam PF27654).
- PANTHER PTHR32123:SF12 BICD FAMILY-LIKE CARGO ADAPTER 1.

## Function (transferred)

- Activating dynein adaptor: links dynein to cargo, converts dynein to a processive motor with dynactin,
  recruits two dyneins [human UniProt "Acts as an adapter protein linking the dynein motor complex to various
  cargos and converts dynein from a non-processive to a highly processive motor in the presence of
  dynactin"].
- Rab6 vesicles: pericentrosomal accumulation of Rab6 secretory vesicles, restricting anterograde secretion
  in early neuronal differentiation; regulator of neurite outgrowth [human UniProt "Regulates the secretory
  vesicle transport by controlling the accumulation of Rab6-containing secretory vesicles in the
  pericentrosomal region"].
- Binds RAB6A/B, KIF1C; tripartite complex with dynein and dynactin.

## Decisions

- GO:0047496 vesicle transport along microtubule (TreeGrafter): ACCEPT (core).
- GO:0055107 Golgi to secretory granule transport (TreeGrafter): KEEP_AS_NON_CORE. Rab6 constitutive
  secretory vesicles are not classical secretory granules, and BICDL1 restrains rather than drives their
  anterograde delivery; human carries the same term by ISS.
- NEW GO:0140660 cytoskeletal motor activator activity (ISS from human/mouse).

## ProtNLM2 GO predictions

- GO:0034452 dynactin binding: COR. GO:0005813 centrosome: COR. GO:0031267 small GTPase binding: COR
  (Rab6). GO:0031175 neuron projection development: COR (human ISS same term; mechanism is negative
  regulation of neuritogenesis). All absent from donkey GOA; all ultimately rest on mouse experiments.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Re-examined every annotation, the description and the core functions without using any ProtNLM2 output.
The ProtNLM2 section above was not used as evidence.

### Deep research

`just deep-research-falcon EQUAS BICDL1 --fallback perplexity-lite` failed: falcon timed out and the
perplexity-lite fallback also failed (recipe exit code 1). No deep-research file exists. Instead I read
the primary literature directly:
- PMID:20360680 (Schlager et al. 2010, mouse BICDR-1; full text cached by `just fetch-pmid`).
- PMID:29420470 (Urnavicius et al. 2018, BICDR1-dynein-dynactin reconstitution and cryo-EM; already cached).

### Identity of the benchmark accession (alternative gene model)

New analysis in `BICDL1-bioinformatics/compare_isoforms_rereview.py`, written up in `RESULTS-rereview.md`.
The existing RESULTS.md and alignment were left unchanged.
- All five donkey BICDL1 UniProt entries come from one Ensembl gene, ENSEASG00005007623. Ensembl canonical
  is ENSEAST00005058854, which is ENSEASP00005061163 = A0A9L0K8K5 (626 aa). The benchmark A0A9L0JLY3 is
  the non-canonical transcript ENSEAST00005044452.
- A0A9L0JLY3 is the only donkey product that lacks the central coiled-coil segment (human Q6ZP65 ~256-303,
  `KMLSDRKREL...`). That segment is present in human and mouse Swiss-Prot and in all other donkey models.
  The benchmark also includes the human isoform-2-type exon. Its length (573 aa) equals human canonical
  only by coincidence.
- The CC1 box (AARLG, donkey 114) and the C-terminal BICDL1/2-like / Rab6-binding region are retained.
  Mouse BICDR-1 382-577 binds Rab6-GTP [PMID:20360680 "a C-terminal region of BICDR-1, amino acids
  382–577, interact with constitutively active GTPase-deficient Rab6A-Q72R"]. So the core activities
  are expected to transfer, but the spacing between the dynein-binding and cargo-binding regions may differ.
- A0A9L0I4K1 (574 aa) has the human/mouse canonical architecture (SEG_CORE present, alt exon absent).

### Evolutionary grounding

- Donkey, human Q6ZP65 and mouse A0JNT9 are all in PANTHER PTHR32123:SF12 (BICD FAMILY-LIKE CARGO ADAPTER 1)
  according to the UniProt cross-references.
- PAINT (`interpro/panther/PTHR32123/PTHR32123-paint.tsv`) places both IBDs on PTN001281025 (Deuterostomia).
  GO:0047496 is seeded by ZFIN and GO:0055107 by MGI:1922915. No MF or CC term is propagated at that
  node, so the MF/CC NEW rows rest on direct mouse experiments plus SF12 membership, not on the PAINT node.
- The experimental evidence for the whole subfamily is from mouse (in cells) and from in vitro
  reconstitution. The human Swiss-Prot functional text is ECO:0000250 from mouse.
- No PANTHER family review YAML exists under interpro/panther/PTHR32123 (only metadata, entries and PAINT
  files), so there is no subfamily-placement disagreement to report.

### Decisions (changes from previous version)

- GO:0047496 vesicle transport along microtubule: ACCEPT (unchanged). Support is now PMID:20360680.
- GO:0055107 Golgi to secretory granule transport: KEEP_AS_NON_CORE (unchanged), with a revised rationale.
  The earlier argument that Rab6 carriers "are not secretory granules" was weakened: the carriers contain
  NPY-GFP, a dense-core cargo [PMID:20360680 "most of the centrosomal BICDR-1-positive vesicles contain
  NPY-GFP"]. The term is kept as non-core because BICDR-1 mainly retains the carriers pericentrosomally.
- NEW GO:0140660 cytoskeletal motor activator activity: retained. The reference is changed to PMID:29420470
  ["both BICDR1 and HOOK3 preferentially recruit two"].
- NEW GO:0031267 small GTPase binding: added, because of the GTP-dependent Rab6A binding by the C-terminal
  region shown in PMID:20360680. It is a core MF that defines the adaptor's cargo.
- NEW GO:0005813 centrosome: retained, now supported by the endogenous-staining quote from PMID:20360680.
- Description corrected: KIF1C binds the N-terminal region (1-353), not the C-terminus [PMID:20360680
  "an N-terminal region of BICDR-1, amino acids 1–353, interact with the C-terminal tail domain of Kif1C"].
  The description now also states that the product is a non-canonical splice form.
- Not added: negative regulation of neuron projection development. This is a downstream cellular phenotype
  of overexpression and knockdown (the zebrafish morphant data are organismal), not process participation.
  Also not added: dynactin binding or dynein complex binding. These are subsumed by the motor-activator
  activity, and adding them would be redundant.

### Relative

The benchmark is an alternative gene model, and the same-gene canonical product (Ensembl canonical
A0A9L0K8K5) has no review. The next relative is therefore that canonical product (same_gene_canonical),
in the folder genes/EQUAS/BICDL1__A0A9L0K8K5. The closest experimentally characterised ortholog is mouse
Bicdl1 A0JNT9 (same SF12 subfamily, PAINT seed MGI:1922915). It also has no review in the repo.

### Modules

Searched `modules/` for BICDL1, Q6ZP65 and PTHR32123: no hits.

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0031267 small GTPase binding, GO:0005813 centrosome) on this accession. GOA already carries the same terms on
another product of the same gene, reviewed in `genes/EQUAS/BICDL1__A0A9L0K8K5/`. GOA propagates gene-level
annotations to one representative product per gene, so adding them to a second product fills a
convention rather than a curation gap. The rows were withdrawn under the rule applied across the
ProtNLM2 re-review cohorts, first raised in the review of PR #5303. The gene-level function is unchanged.

## 2026-10-23 — PR #5309 review follow-up

Core-function terms left after the 2026-10-21 withdrawal of the NEW rows (GO:0031267 small GTPase
binding, GO:0005813 centrosome). The PR reviewer preferred dropping them from core_functions. For
consistency with the convention accepted in the parallel cohort PRs #5305 (MESK2) and #5308 (FTSH12),
a core-function term is kept when its core_functions supported_by cites direct evidence independent of
the withdrawn row (primary literature or a PAINT IBD row), and dropped only when no such evidence exists.
The withdrawal rule is about not duplicating a gene-level GOA row on a second product; core_functions
summarise the gene product's function, which the primary evidence still supports.

- GO:0031267: kept; already supported by PMID:20360680 (C-terminal region binds GTP-locked Rab6A-Q72R and
  not GDP-locked Rab6A-T27N).
- GO:0005813: kept; added PMID:20360680 "specifically localized around the γ-tubulin-labelled centrosome"
  (endogenous BICDR-1) to the first core function.

The 2026-10-21 "Decisions" bullets that describe these as added NEW rows are superseded by the withdrawal
section; no annotation row for either term remains in the review.
