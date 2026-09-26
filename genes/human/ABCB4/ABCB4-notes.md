# ABCB4 evidence review and source-access notes

## Scope and molecular synthesis

2026-09-26 UTC. Human ABCB4, UniProt P21439; 68 seeded GO assertions reviewed.
The original assertion objects, including both `negated: true` ceramide rows,
are preserved. An independent annotation-reviewer consultation inspected the
complete seed and challenged the substrate scope of those negative annotations.

ABCB4's core role is ATP-dependent PC flopping at the hepatocyte canalicular
membrane. PC moves from the cytosolic to the exoplasmic leaflet, then extracellular
bile salts extract it. This is distinct from transporting bile acids, chemically
metabolizing PC, or shuttling lipid through water in a soluble carrier pocket.
The core synthesis uses GO:0090554, GO:0016324 and GO:0045332. Existing broad ABC
transport, ATP binding/hydrolysis and membrane terms remain valid.

The genuine Falcon report completed successfully in 439.84 seconds and is retained
unchanged with its artifact. It was a source-discovery aid; its mechanistic models,
clinical recommendations and recent-paper summaries were not automatically
accepted as annotation evidence. No clinical treatment recommendation is made
in this review. The 2025 simulation paper PMID:40206349 is cached but does not
provide a new direct transport assay, and no annotation rests on it.

## Direct lipid transport and negative annotation scope

[PMID:8898203](https://pubmed.ncbi.nlm.nih.gov/8898203/) compares human MDR1 and MDR3
in polarized LLC-PK1 cells. The original full article was recovered from the
[Utrecht repository](https://dspace.library.uu.nl/items/0c2e8542-4357-4833-82b8-16f0a04fc782)
and its [PDF](https://dspace.library.uu.nl/bitstreams/3b524e2a-3227-4daf-96a6-2c346a76b5b0/download).
The repository download adds a cover page. Journal pages 511–512, Figures 3–4,
were rendered and visually inspected as well as read through extracted text.
Low-temperature assays suppress vesicular secretion; extracellular albumin
extracts lipid after transbilayer transport. The abstract states: "MDR3 cells
exclusively released a short-chain phosphatidylcholine."

Figure 4's negative MDR3 comparison concerns short-chain sphingomyelin and
glucosylceramide synthesized from a ceramide precursor. It contrasts sharply
with MDR1-dependent movement of those derivatives. It does **not** directly
measure free-ceramide movement. Live QuickGO definitions for GO:0099038 and
GO:0099040 concern ceramide, so both existing NOT assertions remain UNDECIDED.
Neither is misread as a positive claim, deleted, or converted into an invented
negative annotation for another lipid. PC selectivity alone cannot prove an
unbounded negative for every ceramide substrate and condition.

[PMID:34385322](https://pmc.ncbi.nlm.nih.gov/articles/PMC8379956/) provides purified
human ABCB4 proteoliposome transport and structural evidence. The full indexed
Results and Methods were accessible even though direct PMC navigation challenged
access and the supported cache refresh encountered HTTP 429. ATP-dependent
NBD-PC transport, discrimination against the tested NBD-PE, and substrate-pocket
structure corroborate PC floppase activity. The experiments use P21439-2; this
does not demonstrate that only isoform 2 is active. Original seeded isoform fields
are not changed. Canonical P21439 is 1,286 residues, whereas structural isoform 2
is shorter; residue numbering must not be transferred between them casually.

[PMID:31873305](https://pubmed.ncbi.nlm.nih.gov/31873305/) resolves an ATP-bound
human ABCB4 state with two ATP molecules. A structural snapshot is not itself
a leaflet-resolved transport assay. The independent cellular and purified flux
studies support the source's PC-floppase annotation.

The cached UniProt record also contains PE and SM Rhea reaction statements
attributed to PMID:8898203. They need reconciliation with the original MDR1/MDR3
comparison and are recorded as an expert question; the downloaded record is not
edited. Cell-medium PE/SM efflux in PMID:23468132 must also be distinguished from
purified transbilayer transport of those substrates.

## Indirect effects and regulation terminology

- [PMID:17523162](https://pubmed.ncbi.nlm.nih.gov/17523162/) measures human ABCB4
  lipid release with taurocholate and ATP-coupling mutants. PC availability also
  facilitates cholesterol diffusion; this supports a non-core positive effect
  on cholesterol transport, not direct cholesterol-transporter activity.
- [PMID:24045840](https://pmc.ncbi.nlm.nih.gov/articles/PMC3992575/) distinguishes
  reduced PC secretion from preserved expression and targeting. Taurocholate-
  stimulated cholesterol release increases in mutant cells, particularly Y403H;
  a blanket statement that all lipid export decreases would misstate the result.
- GO:0061092 and GO:2001140 are refined to direct phospholipid translocation.
  ABCB4 executes the step; the studies do not establish a separate regulator
  acting on another phospholipid translocator.
- Mouse Abcb4/P21440 has bile-acid-secretion IMP evidence from
  [PMID:8106172](https://pubmed.ncbi.nlm.nih.gov/8106172/). Its verified primary
  result is loss of biliary phospholipids. GO:0032782 specifically names bile-acid
  secretion. Human ABCB4's direct PC movement supports replacing the transferred
  process with GO:0045332 without asserting that the mouse paper contains no
  secondary bile-acid phenotype.
- Fenofibrate-response transfers trace to mouse IDA
  [PMID:8615769](https://pubmed.ncbi.nlm.nih.gov/8615769/), with independent human
  induction in [PMID:24122873](https://pmc.ncbi.nlm.nih.gov/articles/PMC4049334/).
  The latter's functional PC secretion experiments used rat hepatocytes.
  Drug-induced expression is contextual; ABCB4 is not thereby a fenofibrate
  receptor or transporter. Taurocholate-dependent cellular efflux is likewise
  retained as a non-core bile-acid response, not bile-acid export.

## Localization and interaction evidence

[PMID:23468132](https://pmc.ncbi.nlm.nih.gov/articles/PMC3622319/) Results/Figure 2
uses detergent-free fractionation of human ABCB4-expressing cells. The ABCB4
raft/nonraft ratio is 0.158: a positive minor raft pool, despite predominantly
nonraft distribution. Both raft annotations are KEEP_AS_NON_CORE. The title's
emphasis on nonrafts is not evidence that raft detection was absent.

The indexed Results of [PMID:24045840](https://pmc.ncbi.nlm.nih.gov/articles/PMC3992575/)
describe wild-type ABCB4 in cytoplasm and at the cell surface of HUH7 and HEK293
cells; Figure 3 compares mutant distributions. Cytoplasm is not synonymous with
soluble cytosol, and neither label can be rejected merely because the protein has
transmembrane domains. This intracellular pool is retained as non-core.

The [Human Protein Atlas ABCB4 subcellular page](https://www.proteinatlas.org/ENSG00000005471-ABCB4/subcellular)
was inspected on 2026-09-26. HPA049395 reports supported plasma-membrane staining
in A-549, Hep-G2 and U2OS, and supported additional cytosol staining in A-549.
The former agrees with dedicated membrane studies; the latter is retained as a
contextual antibody-based observation. No new nuclear/focal-adhesion annotation
is inferred from the other HPA signals.

The SL-0070 clathrin-vesicle mapping traces through rat Abcb4 **Q08201** to
[PMID:15159385](https://pubmed.ncbi.nlm.nih.gov/15159385/). The abstract foregrounds
BSEP, but the original full Results, "Distribution of HAX-1 in Rat Liver
Subcellular Fractions," explicitly includes MDR2 in the enriched clathrin-vesicle
fraction. The [indexed original article mirror](https://www.researchgate.net/publication/8547779_Identification_of_HAX-1_as_a_Protein_That_Binds_Bile_Salt_Export_Protein_and_Regulates_Its_Abundance_in_the_Apical_Membrane_of_Madin-Darby_Canine_Kidney_Cells)
made that section accessible. This resolves the initial access uncertainty and
supports a non-core trafficking location in the human ortholog. The antibody
C219 detects MDR1/MDR2; no human-specific fractionation is claimed.

[PMID:19674157](https://pubmed.ncbi.nlm.nih.gov/19674157/) reports RACK1 binding
to the ABCB4 linker in two-hybrid/pulldown experiments, but unsuccessful full-length
co-immunoprecipitation. Generic protein binding is removed as uninformative,
without denying the observed interaction or assigning RACK1's adapter function
to ABCB4.

[PMID:23533145](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/) is available in
the cache as full text. It catalogs exosomes from expressed prostatic secretions
in urine. ABCB4/P21439 does not appear in the article body; Supplemental Table 2
contains the protein-level data but was not retrieved through the challenged PMC
endpoint. The HDA row remains UNDECIDED, not rejected as wrong tissue or declared
proof of a dedicated extracellular function.

Other source-specific locations and activity perturbations are supported by
PMIDs 15258199, 21820390, 24594635, 24723470, 24806754 and 28012258. Pathogenic
ER retention is not promoted to a normal core location. Mouse Mdr2 in
PMID:7912658 is an ortholog, not human MDR3; its vesicle PC assay supports
conservation, with direct human experiments cited independently.

## Propagation, ontology, and coverage checks

Live QuickGO donor records and UniProt entries were read for mouse P21440 and
rat Q08201 on 2026-09-26. Mouse PC translocation traces to PMID:7912658; its
fenofibrate-response source is PMID:8615769. Intercellular canaliculus is
consistent with donor PMID:12068294 and independent human pseudocanalicular
imaging. The radixin paper's ABCC2 focus is not a basis for alleging wrong-gene
curation of its comparator proteins.

All 23 inferred rows have source-entity propagation assessments. IBA assessments
use their proximate PTN nodes; an experimentally characterized target among the
descendant evidence is valid, not circular. No PAINT node is rejected on donor
count or on the presence of the target in its own source list.

QuickGO confirms GO:0090554 is cytosolic-to-exoplasmic PC flopping, whereas
GO:0140345 specifies the opposite direction. GO:0120014 is aqueous-phase lipid
transfer requiring shielding of its hydrophobic region; both Reactome rows are
therefore refined to PC floppase activity. Reactome mutant-loss events remain
valid context for the corresponding normal membrane location and activity.

`gocams/index.tsv` had no ABCB4/P21439 match. No NEW process is needed. Broad
transport and narrower substrate terms already cover the direct function;
downstream disease phenotypes are not manufactured into additional processes.

Final draft counts: 44 ACCEPT, 12 KEEP_AS_NON_CORE, 8 MODIFY, 3 UNDECIDED,
1 REMOVE. The three unresolved rows are the two NOT ceramide assertions and the
exosome proteomic assignment. Validation and PR follow-up are recorded below.

## Validation — 2026-09-26 UTC

`just validate human ABCB4` passes. The sole advisory warning is intentional:
the genuine Falcon report is retained and assessed but no annotation uses it as
direct evidence in place of the primary literature. Gene history validation,
HTML rendering, and `git diff --check` pass. A semantic comparison with the
initial YAML confirms all 68 original source assertion objects, including both
NOT flags, are unchanged; all 23 inferred rows have propagation assessments.
The independent annotation reviewer inspected the completed draft and found no
blocking biological issue. No whole-repository validation rerun was needed for
this isolated content change beyond the campaign baseline and required PR CI.
