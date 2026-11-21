# DeepTMHMM2: human membrane-topology audit

Audited 2026-11-04. [Preprint v1](https://doi.org/10.64898/2026.08.24.746435): *DeepTMHMM2 enables accurate prediction of transmembrane protein topology and subcellular location*.

## 2026-11-12: topology flags on 205 additional proteins

The [expanded pilot](../genes/human/SPTLC2/SPTLC2-bioinformatics/deeptmhmm2-benchmark/flag-pilot-2026-11-12/RESULTS.md)
ran all additional locally reviewed human FRR:0004 and lipid-droplet candidates,
plus three controls, in 12.33 minutes on CPU (5.21 GiB peak RSS). The expanded
checker generated 45 flags on 32 proteins, all manually triaged. It recovered
existing annotation distinctions, identified model counterexamples, and exposed
complex-role, membrane-context and local-geometry questions. A human/chloroplast
check and a residue-overlap INTRAMEM/TM check were added during the pilot. Five
diagnostic predictions reproduced exactly with the upstream CLI. This run changes
no gene reviews and emits no GO NOT assertions.

## 2026-11-05: expanded local execution

The [31-protein follow-up panel](../genes/human/SPTLC2/SPTLC2-bioinformatics/deeptmhmm2-benchmark/panel-2026-11-05/RESULTS.md)
now runs all 23 audited S20 candidates locally and adds EGFR, CFTR, TOMM40, CALR,
SPTLC1, GAPDH, INS and COX4I1. This is 29 newly run proteins plus the original
SPTLC2/DPM1 controls. Two API passes took 49.70 and 49.30 seconds of inference;
the unmodified CLI took 183.80 seconds including startup/export. Peak RSS was
5.24 GiB for the API and 4.99 GiB for the CLI on the M1 Max CPU.

The API reproduces all 23 S20 feature predictions. The additional controls recover
CFTR's 12 helices, TOMM40's 19-strand barrel, and appropriate broad topology for the
other six controls. Known non-spanning false predictions for TOMM22, SUN2 and
CYP46A1 recur. API and CLI agree on all broad classes and selected membrane labels,
but two exact boundaries and one rounded membrane score differ. A three-protein
diagnostic reproduces all differences by enabling the CLI's CPU autocast policy
in the API. No curated annotation changes were made from this follow-up run.

## Outcome

The supplement is useful for finding incorrect membrane-spanning descriptions and overlooked primary literature. The focused audit covered all **23 existing human reviews** matched to S20, changed **16 review YAML files**, and appended evidence and limitations to all 23 gene notes. Changes cover 58 annotation-review blocks (37 action changes), five biological descriptions, the COQ8B core-function location, and three UniProt source-defect records. Annotation identifiers, original evidence codes, original reference IDs and qualifiers were preserved. No new annotation rows were added.

Three corrections have direct primary support:

- **SPTLC2:** the human SPT structure describes amphipathic/complex-mediated anchoring and no membrane-spanning region in SPTLC2. Correct the single-pass description while retaining ER membrane and cytoplasmic-face localization. [PMID:33558761](https://pubmed.ncbi.nlm.nih.gov/33558761/)
- **DHRS3:** cysteine scanning identifies an N-terminal interfacial amphipathic helix in the ER cytoplasmic leaflet and lipid-droplet monolayer. Correct the multi-pass description. [PMID:30104359](https://pubmed.ncbi.nlm.nih.gov/30104359/)
- **LPCAT1:** the paper cited for topology explicitly reports monotopic insertion. Correct the review's contradictory single-pass type II rationale. [PMID:21498505](https://pubmed.ncbi.nlm.nih.gov/21498505/)

These conflicts are recorded in `references[].reference_review.source_defects` for the cached UniProt descriptions. They have not been submitted upstream. The downloaded UniProt records themselves remain untouched.

**COQ8B** supplies an additional location refinement: human COQ8B-HA protease-protection and carbonate-extraction experiments support peripheral association with the matrix face of the inner mitochondrial membrane. All three broad mitochondrial-membrane rows and the core-function location were refined accordingly. This evidence is on COQ8B itself. [PMID:29194833](https://pubmed.ncbi.nlm.nih.gov/29194833/)

The audit also corrected location actions under the repository's organelle policy: retain informative root organelle terms alongside membrane subcompartments, refine generic membrane terms where supported, and use consistent actions for the same location regardless of overlapping evidence. These policy changes are not discoveries attributable to the predictor.

## Decisions across the 23 proteins

IF means interfacial and RE means reentrant. The author evidence labels are reproduced as source data, not adopted as our confidence grades. Exact coordinates are in the TSVs and gene notes; they were not independently mapped onto every structure.

| Gene | Author category | Our assessment | Review YAML edited |
|---|---|---|---|
| [ACSL4](../genes/human/ACSL4/ACSL4-notes.md) | Element | Retain; homolog-based candidate | No; notes only |
| [ADCK2](../genes/human/ADCK2/ADCK2-notes.md) | ? | Qualify inference; topology unresolved | Yes |
| [ATG2A](../genes/human/ATG2A/ATG2A-notes.md) | Peripheral | Retain; segment unvalidated | No; notes only |
| [COQ5](../genes/human/COQ5/COQ5-notes.md) | Element | Retain topology; retain root organelle | Yes |
| [COQ7](../genes/human/COQ7/COQ7-notes.md) | Element | Retain topology; retain root organelle | Yes |
| [COQ8B](../genes/human/COQ8B/COQ8B-notes.md) | Peripheral | Refine location from direct human evidence | Yes |
| [CYP46A1](../genes/human/CYP46A1/CYP46A1-notes.md) | No | Reject predicted topology change | Yes |
| [DHRS3](../genes/human/DHRS3/DHRS3-notes.md) | Element | Correct topology from direct experiment | Yes |
| [DPM1](../genes/human/DPM1/DPM1-notes.md) | Peripheral | Retain tethering mechanism; retain root ER | Yes |
| [GPAM](../genes/human/GPAM/GPAM-notes.md) | Element | Retain structural correction; retain root organelle | Yes |
| [LPCAT1](../genes/human/LPCAT1/LPCAT1-notes.md) | Peripheral | Correct conflicting topology rationale | Yes |
| [LPCAT4](../genes/human/LPCAT4/LPCAT4-notes.md) | ? | Qualify topology; retain root ER | Yes |
| [NDUFA12](../genes/human/NDUFA12/NDUFA12-notes.md) | Element | Retain peripheral placement; consistent actions | Yes |
| [PKMYT1](../genes/human/PKMYT1/PKMYT1-notes.md) | Element | Retain targeting mechanism; refine broad term | Yes |
| [PNPLA2](../genes/human/PNPLA2/PNPLA2-notes.md) | Element | Retain; correct interpretation of supplement | No; notes only |
| [PNPLA3](../genes/human/PNPLA3/PNPLA3-notes.md) | Peripheral | Qualify topology; refine broad membrane | Yes |
| [RDH5](../genes/human/RDH5/RDH5-notes.md) | ? | Retain pending direct topology resolution | No; notes only |
| [SPRY1](../genes/human/SPRY1/SPRY1-notes.md) | Peripheral | Retain; paralog hypothesis | No; notes only |
| [SPRY2](../genes/human/SPRY2/SPRY2-notes.md) | Peripheral | Retain; insertion geometry unproven | No; notes only |
| [SPTLC2](../genes/human/SPTLC2/SPTLC2-notes.md) | Element | Correct topology from human structure | Yes |
| [STOML1](../genes/human/STOML1/STOML1-notes.md) | Element | Qualify topology; refine location | Yes |
| [SUN2](../genes/human/SUN2/SUN2-notes.md) | ? | Reject predicted topology change | No; notes only |
| [TOMM22](../genes/human/TOMM22/TOMM22-notes.md) | No | Reject predicted topology change; refine broad terms | Yes |

## Limits that affect interpretation

- **False non-spanning calls exist.** Preserve established transmembrane topology for TOMM22, SUN2 and CYP46A1. The supplement itself marks TOMM22/CYP46A1 as `No` and acknowledges the missed SUN2 helix.
- **A homolog is not a residue-level experiment on the human target.** ACSL4 uses ACSL3 evidence; COQ5 uses a yeast structure; STOML1 uses stomatin; SPRY1 uses SPRY2. LPCAT1/2 results cannot directly settle LPCAT4 topology.
- **PNPLA2 requires particular care.** S20 describes a PNPLA5 basic patch, but the cited primary study distinguishes that mechanism from the hydrophobic targeting region in human ATGL/PNPLA2. Its 345–354 prediction overlaps the experimentally studied region without defining its full extent or geometry. [PMID:23741432](https://pubmed.ncbi.nlm.nih.gov/23741432/)
- **ADCK2 remains an inference.** Retain its provisional inner-membrane IC proposal, but distinguish evidence of mitochondrial protection and predicted membrane contact from evidence of bilayer spanning. The alternative topology calls are not independent experiments. Human fractionation and insertion mapping would resolve the remaining ambiguity.
- **RDH5 remains unresolved in this audit.** The available cached disease-variant abstract does not resolve the topology literature. Preserve experimental annotations rather than inferring a paralog error from the supplement. LPCAT4 and PNPLA3 descriptions likewise should not promote predicted insertion models to established topology.
- **Mechanism and compartment are different questions.** The model's coarse `Globular` category can include membrane-associated proteins. In the tested code, non-TM predictions have membrane-type assignments suppressed. Blank organelle output therefore does not refute ER association; predicted transit-peptide boundaries and strings such as `Cytoplasmic` or `Nucleus matrix` in S20 are not sufficient evidence for new organelle annotations.

## Usefulness and whether to run all human proteins

Use DeepTMHMM2 as a **topology discrepancy screen** alongside sequence, structural and experimental evidence. It can help distinguish a membrane-spanning anchor, a one-leaflet insertion and complex-mediated membrane association. It does not establish a substrate, catalytic activity, physiological pathway or new molecular function by itself. Here, its main value was finding literature-backed topology corrections and clarifying localization inferences.

A whole-human run is technically plausible, but should be a separate screening dataset with explicit confidence and conflict flags. This audit does not justify automatically rewriting GO annotations across the proteome. A useful next expansion would prioritize membrane-associated proteins with discordant topology annotations, then adjudicate against experimental structures and topology assays. If generating a proteome-wide dataset, pin the UniProt release and accession/isoform set, retain full topology strings and scores, document handling of very long proteins, and benchmark a length-stratified sample first.

The supplied workbook has **48 S20 candidates**, of which 23 match our reviews; it is not a complete precomputed human proteome. S17 is a curated experimental set; S18/S19 describe unresolved regions. No complete downloadable human-proteome prediction release was identified in the paper, code and supplement sources checked during this exploration. This is a search result, not proof that none exists elsewhere.

The local two-protein benchmark measured **0.63–1.36 seconds per protein** after loading on this M1 Max CPU and about **5 GiB process RAM**, with approximately **2.55 GiB weights**. The authors report approximately **65 minutes on an RTX 8000** for the human proteome excluding titin. Neither number supplies a reliable whole-proteome CPU estimate; long proteins, batching and startup matter. See the [benchmark, raw outputs and API correction](../genes/human/SPTLC2/SPTLC2-bioinformatics/deeptmhmm2-benchmark/RESULTS.md). This audit used S20 predictions for the 23-gene comparison; only SPTLC2 and DPM1 were rerun locally in the earlier benchmark.

## Reproducible source extraction

The subsequent local panel expanded execution to **31 proteins**, including all
23 reviewed S20 candidates and eight controls; results and API/CLI comparisons are
in the [benchmark report](../genes/human/SPTLC2/SPTLC2-bioinformatics/deeptmhmm2-benchmark/RESULTS.md).
The [topology flagging pilot](DEEPTMHMM2/TOPOLOGY_FLAGS.md) combines these predictions
with source topology, retained lipid-droplet claims and existing FRR:0004 scope.
It produced 21 advisory flags on 14 proteins, separating corroborated conflicts,
predictor counterexamples and context checks. It makes no new GO assertions.

Files:

- [s20.tsv](DEEPTMHMM2/s20.tsv): all 48 author rows, preserved verbatim with source row numbers.
- [reviewed-human.tsv](DEEPTMHMM2/reviewed-human.tsv): the 23 accession-matched rows.
- [audit.yaml](DEEPTMHMM2/audit.yaml): our decisions, reasoning and primary-reference identifiers, separated from the author claims.
- [source.json](DEEPTMHMM2/source.json): workbook SHA-256 and source/version metadata.
- [extract_s20.py](DEEPTMHMM2/extract_s20.py): standard-library extraction and accession join against existing review headers.

Reproduce from the supplied workbook:

```bash
python projects/DEEPTMHMM2/extract_s20.py ~/Downloads/media-1.xlsx
```

The companion `media-2.pdf` was inspected as the 18-page supplementary text; it contains methods and benchmarks rather than a complete human prediction table. Its SHA-256 is `bef4702c636aef17267db0bb2bf3aaf77768838b0f361adae6009a38fb69d938`.

## Validation

- All 23 original reviews passed `just validate human GENE` before editing.
- All 16 changed review YAML files passed the same full command after editing, including the COQ8B core-location refinement. The seven untouched YAML files retain their passing baseline result; their new audit notes do not alter schema content.
- Existing unrelated warnings remain (including protein-binding policy, pre-existing COQ8B kinase/NOT consistency, and older quote/support issues). Comparison with baseline found **no newly introduced warnings**. Per-gene exit status and warning counts are in [validation.tsv](DEEPTMHMM2/validation.tsv).
- All **24 new audit history records** (23 genes plus this project) passed `just validate-history`.
- `just paint-losses human GPAM` and `just paint-losses human LPCAT4` found no IRD/IKR lineage loss. These checks supported preserving the existing root-organelle inheritance; no new phylogenetic placement was asserted.
- Re-extraction reproduced the source TSVs and metadata byte for byte. Checks confirmed 48 source rows, 23 unique matched genes, unchanged machine-sourced annotation fields and annotation counts, and three source-defect records grounded in the cached source text and cited papers.
- `git diff --check` passed. No model retraining or proteome-wide execution was performed in this audit.
