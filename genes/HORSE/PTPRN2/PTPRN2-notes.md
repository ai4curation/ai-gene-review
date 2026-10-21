# PTPRN2 notes


## 2026-09-08 paired review

Selected accession A0A9L0T4W6; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/PTPRN2/PTPRN2-notes.md). [Sequence comparison](PTPRN2-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

The 1996 cloning report states that recombinant IAR/PTPRN2 has phosphatase activity, but its abstract does not name the substrate. Later human cell work explicitly distinguishes lack of phosphoprotein-substrate activity from phosphoinositide phosphatase activity and tests the effect of a catalytic-domain mutant on migration and metastasis. Vesicle accumulation, insulin/neurotransmitter release, and membrane phosphoinositide regulation are not interchangeable with protein tyrosine dephosphorylation. Conversely, a biological-process annotation can describe regulation through another enzyme: losing intrinsic protein phosphatase activity alone does not refute all participation in protein dephosphorylation. The exact experimental annotation therefore remains unresolved while the inappropriate electronic intrinsic protein-phosphatase terms can be challenged.

Sources: [PMID:8798755](https://pubmed.ncbi.nlm.nih.gov/8798755/), [PMID:26620550](https://pubmed.ncbi.nlm.nih.gov/26620550/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research: `just deep-research-falcon HORSE PTPRN2 --fallback perplexity-lite` failed (Falcon "Failed to authenticate"; Perplexity HTTP 401 insufficient quota), so no horse deep-research file exists. The review uses primary literature cached in `publications/`.

### Identity of the benchmark accession (alternative gene model)

[compare_horse_models_rereview.py](PTPRN2-bioinformatics/compare_horse_models_rereview.py) produced [RESULTS-rereview.md](PTPRN2-bioinformatics/RESULTS-rereview.md) and `results-rereview.json`. Findings:

- Horse PTPRN2 (Ensembl ENSECAG00000012762) has eight TrEMBL models, all in PANTHER PTHR46106:SF5. The canonical model in the UniProt gene-centric reference proteome is **A0A9L0RAE3** (1054 aa, PTPRN2-205). The benchmark **A0A9L0T4W6** (976 aa, PTPRN2-208, ENSECAT00000094767) is a non-canonical model.
- A0A9L0T4W6 keeps the signal peptide, the IA-2 luminal domain, the TM helix (568-592) and the catalytic loop HCSDGAGRSG (Cys897 = human Cys945). Its last coding exon (ENSECAE00000523854) is an alternative terminal exon. That exon replaces the 47 C-terminal residues conserved in human, mouse and the seven other horse models with 56 unrelated residues. The replaced stretch maps to human 969-1015, i.e. the final 37 residues of the PTP-like domain (human domain 745-1005) plus the cytoplasmic tail. The model also lacks 87 residues upstream of the catalytic motif compared with the canonical model.
- The earlier RESULTS.md description ("deletion of human residues 989-1003") is a pairwise-alignment artifact. The true change is the C-terminal replacement. RESULTS.md is left unchanged and marked DISPUTED in reference_review.

### Evolutionary basis for transfer

- Rat phogrin (Ptprn2, Q63475) and human Q92932 are both in PTHR46106:SF5 with the horse protein, so subfamily-level transfer is justified. Rat phogrin biochemistry [PMID:20097759 "We report here that phogrin is able to dephosphorylate specific inositol phospholipids, including phosphatidylinositol (PI) 3-phosphate and PI 4,5-diphosphate but not PI 3,4,5-trisphosphate."] shows Cys-dependent PIPase activity and no activity on phosphoproteins or pNPP [PMID:20097759 "In the absence of detectable ability to dephosphorylate phosphoproteins or p -nitrophenyl phosphate (pNPP)"]. The effect on insulin secretion needs the catalytic Cys [PMID:20097759 "Insulin secretion was not decreased by overexpression of phogrin(C934S)-myc, indicating that the effect of phogrin on insulin secretion depends on its enzymatic activity."].
- Mouse Ptprn2 knockouts: fewer DCVs and less insulin secretion [PMID:21732083 "insulin content, insulin secretion and the number and half-life of DCV"]. IA-2beta also sits on synaptic vesicles [PMID:19361477 "IA-2beta is present in both DCV and SV"]. Behavioural and lifespan phenotypes of the double knockout are downstream organismal effects and were not annotated.
- The horse accession carries no IBA rows. Human PTPRN2 gets regulation of secretion, secretory granule and synapse by IBA from PTN000439769 / PTN000439772, so the subfamily-level terms are PAINT-sanctioned.

### Annotation decisions

- GO:0004725 and GO:0008138 (protein phosphatase activities, IEA): REMOVE. The subfamily lost phosphoprotein activity.
- GO:0016787 hydrolase activity: MODIFY to GO:0052866 phosphatidylinositol phosphate phosphatase activity (verified is_a hydrolase activity in OLS). This changes the previous UNDECIDED. The caveat that this exact model's C-terminus is altered is stated in the reason.
- GO:0030141 secretory granule: MODIFY to GO:0032127 dense core granule membrane.
- GO:0030658 transport vesicle membrane and GO:0045202 synapse: MODIFY to GO:0030672 synaptic vesicle membrane. OLS confirms GO:0030672 sits under both, and that secretory granule membrane is not under transport vesicle membrane.
- NEW GO:0051046 regulation of secretion (ISS, subfamily orthology; matches the PAINT IBA on human).

### Relative to review next

A0A9L0T4W6 is a non-canonical alternative gene model. The canonical product of the same horse gene, A0A9L0RAE3, has no review. Suggested folder: `genes/HORSE/PTPRN2__A0A9L0RAE3`. The PANTHER family review (interpro/panther/PTHR46106) also places the horse protein in SF5, so there is no subfamily disagreement. But it uses the non-canonical A0A9L0T4W6 as the horse representative and repeats the "989-1003 deletion" description. No module in modules/ includes PTPRN2; `modules/beta_cell_glucose_stimulated_insulin_secretion.yaml` is the closest pathway context.
