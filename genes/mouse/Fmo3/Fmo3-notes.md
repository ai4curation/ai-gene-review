# Fmo3 (Mouse) Curation Notes — UniProtKB:P97501 (MGI:1100496)

## 1. Gene Overview & Orthology
- **Gene symbol**: `Fmo3` (`MGI:1100496`), encoding mouse dimethylaniline monooxygenase [N-oxide-forming] 3 / flavin-containing monooxygenase 3 (`UniProtKB:P97501`, 534 aa, sequence version 1).
- **Subfamily & Family**: Member of `PANTHER:PTHR23023` (`DIMETHYLANILINE MONOOXYGENASE`) and subfamily `PANTHER:PTHR23023:SF44` (`FLAVIN-CONTAINING MONOOXYGENASE 3`).
- **Orthology**: 1:1 ortholog of human `FMO3` (`UniProtKB:P31513`, `file:human/FMO3/FMO3-ai-review.yaml`), sharing 79% amino acid sequence identity and conserved FAD-binding (starting at residue 9) and NADP+ pyrophosphate-binding (starting at residue 191) Rossmann-fold motifs (`PMID:9344459`).

## 2. Molecular Function, Metaorganismal TMAO Pathway & Sexual Dimorphism in *Mus*
- **Trimethylamine N-Oxygenation (`GO:0034899`, `EC 1.14.13.148`, `RHEA:21316`)**:
  - Recombinant mouse Fmo3 expressed in *E. coli* catalyzes NADPH-dependent sulfoxidation of methimazole that is >85% competitively inhibited by trimethylamine (TMA) and thioacetamide, as well as by thiourea, thiobenzamide, and N,N-dimethylaniline (`PMID:9344459`).
  - In vivo, hepatic Fmo3 is the principal host enzyme converting portal-delivered, gut-microbiota-derived TMA into circulating trimethylamine N-oxide (TMAO); antisense oligonucleotide knockdown or transgenic overexpression of `Fmo3` in mice directly alters plasma TMAO levels, platelet responsiveness, and carotid artery thrombosis potential (`PMID:29981269`).
- **Lineage-Specific Male Hepatic Repression & Chemosensory Evolution (`PMID:9344459`, `PMID:23177478`)**:
  - Whereas human `FMO3` and rat `Fmo3` are expressed in adult liver in both sexes, *Mus musculus* (and closely related *Mus domesticus* and *Mus spretus*) evolved androgen/testosterone-dependent transcriptional silencing of hepatic `Fmo3` in males at puberty (4-5 weeks of age), resulting in >1,000-fold higher hepatic `Fmo3` mRNA in adult females than in adult males (`PMID:9344459`, `PMID:23177478`).
  - Consequently, adult female mice oxidize gut-derived TMA to urinary TMAO, whereas adult male mice excrete >1,000-fold higher urinary TMA (~5 mM), which activates trace amine-associated receptor 5 (`Taar5`) in the olfactory epithelium to serve as a species-specific social attractant for mice and an aversive allomone toward predatory rats (`PMID:23177478`).
- **Taurine Biosynthesis vs Fmo1 (`PMID:32156684`, `PMID:23177478`)**:
  - Comparative NMR profiling of male and female mouse urine in `PMID:23177478` directly demonstrated that while TMA and TMAO show reciprocal >20-fold sex differences due to male hepatic `Fmo3` silencing, urinary taurine and creatine levels are identical between male and female mice (`"The levels of other major metabolites, including creatine and taurine, were similar between males and females"`). This in vivo evidence corroborates Veeravalli et al. (`PMID:32156684`), who showed that FMO1 (`Fmo1`), rather than FMO3, is the primary physiological hypotaurine monooxygenase in mammals.

## 3. Paralogous `ISO` Transfers from Rat `Fmo1` (`RGD:619761`) in GOA
- Three MGI `ISO` (`GO_REF:0000096`) annotations on mouse `Fmo3` cite `RGD:619761` in `with_or_from`. However, `RGD:619761` is rat **`Fmo1`** (`UniProtKB:P36365`), whereas rat `Fmo3` is `RGD:628602` (`UniProtKB:Q9EQ76`):
  1. `GO:0004499` (`N,N-dimethylaniline monooxygenase activity`, `ISO` `RGD:619761`) — `ACCEPT` (the activity itself is true for mouse Fmo3 and experimentally supported by `PMID:9344459`), with `propagation_review` flagging `PARALOG_TRANSFER` / `WRONG_WITH_FROM`.
  2. `GO:0006805` (`xenobiotic metabolic process`, `ISO` `RGD:619761`) — `ACCEPT` (the process is true for mouse Fmo3 and supported by `PMID:9344459`), with `propagation_review` flagging `PARALOG_TRANSFER` / `WRONG_WITH_FROM`.
  3. `GO:0016597` (`amino acid binding`, `ISO` `RGD:619761`) — `REMOVE` (false paralog transfer from rat `Fmo1`; Fmo3 is a flavin-dependent amine/sulfide monooxygenase, not an amino acid binding protein).

## 4. Summary of GOA Annotation Review Decisions
- **`ACCEPT` (Core)**:
  - `GO:0034899` `trimethylamine monooxygenase activity` (IEA, ISO `UniProtKB:P31513`).
  - `GO:0004499` `N,N-dimethylaniline monooxygenase activity` (IBA `PTN000545689`, 3 IEA rows, ISO `RGD:619761`).
  - `GO:0050660` `flavin adenine dinucleotide binding` (IBA `PTN009058586`, IEA).
  - `GO:0050661` `NADP binding` (IBA `PTN000545689`, IEA).
  - `GO:0006805` `xenobiotic metabolic process` (IEA, ISO `RGD:619761`).
  - `GO:0005789` `endoplasmic reticulum membrane` (IBA `PTN000545689`, IEA) and `GO:0005783` `endoplasmic reticulum` (IEA; kept as `ACCEPT` per root organelle policy `projects/ORGANELLES.md`).
- **`KEEP_AS_NON_CORE`**:
  - `GO:0047638` `albendazole monooxygenase activity` (IEA, ISO `UniProtKB:P31513`).
  - `GO:0047822` `hypotaurine monooxygenase activity` (IEA, ISO `UniProtKB:P31513`) and `GO:0042412` `taurine biosynthetic process` (IBA `PTN000545693`, IEA, ISO `UniProtKB:P31513`).
- **`MODIFY`**:
  - `GO:0004497` `monooxygenase activity` (IEA) -> `GO:0034899`, `GO:0004499`.
  - `GO:0016491` `oxidoreductase activity` (IEA) -> `GO:0034899`, `GO:0004499`.
  - `GO:0016020` `membrane` (IEA) -> `GO:0005789` (`endoplasmic reticulum membrane`).
- **`REMOVE`**:
  - `GO:0016597` `amino acid binding` (ISO `RGD:619761`).
