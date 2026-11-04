# Selected GBE1 source evidence

These locators expose the target-level evidence behind the review. They describe selected original text and tables; they do not imply full figure, supplementary-image or raw-data inspection.

| Source | Target evidence and original locator | Limit |
| --- | --- | --- |
| [PMID:8613547](https://doi.org/10.1172/JCI118517) | Original Methods “Transient transfection in COS-7 cells” and “Enzyme assay”; Table III compares wild-type and variant human constructs with mock controls. | Coupled activity assay; historical clones were not aligned to the current sequence. |
| [PMID:26199317](https://doi.org/10.1093/hmg/ddv280) | Selected Methods and Results distinguish engineered human 38–700 protein, observed noncatalytic sugar contacts and modeled active-site binding. | A fragment is not a natural product; modeling is not observed active-site substrate occupancy. |
| [PMID:24837458](https://doi.org/10.1042/BSR20140053) | Results/Fig. 4A text reports tagged GBE1–STBD1 co-immunoprecipitation. | The later recruitment/deprivation experiments concern other enzymes. |
| [PMID:36217029](https://pubmed.ncbi.nlm.nih.gov/36217029/) | Supplementary Table 1B, worksheet row 102: GBE1/Q04446–NSP16, HIS3=1, GFP=0. Methods describe sequence-confirmed yeast two-hybrid retesting. | No target pair in the inspected orthogonal N2H table; no infected-cell function. |

The viral partner [P0DTD1, PRO_0000449633](https://www.uniprot.org/uniprotkb/P0DTD1/entry) is the NSP16 mature chain at residues 6799–7096. Its RNA cap methyltransferase class supports enzyme binding, without transferring catalysis to GBE1. [STBD1/O95210](https://www.uniprot.org/uniprotkb/O95210/entry) is a glycogen cargo receptor; that identity does not make it a signaling receptor.

## Urinary-vesicle identifications

The [NHLBI original protein table](https://esbl.nhlbi.nih.gov/UrinaryExosomes/) identifies GBE1/NP_000149 with one peptide (table row 449). Its legend assigns source 2 to [PMID:19056867](https://pubmed.ncbi.nlm.nih.gov/19056867/). The historical unversioned RefSeq accession is not a sequence-resolved modern isoform claim.

The original [PMID:23533145 supplement](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/) SI Table 2, row 842, identifies Q04446/GBE1: one protein and unique-peptide counts PCa1/PCa2/NC1/NC2 = 0/0/2/2. Methods describe two analyses per clinical pool. These are not independent donor replicates; contamination and preparation purity remain limits, and zero counts do not establish disease-specific absence.

## Actual Reactome target roles

[3322005](https://reactome.org/content/detail/R-HSA-3322005), [3322016](https://reactome.org/content/detail/R-HSA-3322016) and [3322057](https://reactome.org/content/detail/R-HSA-3322057) each use catalyst 71577 → physical entity 71576 → reference 55670, human Q04446 residues 1–702 in cytosol. [3322077](https://reactome.org/content/detail/R-HSA-3322077) explicitly contains these normal reactions.

[3878762](https://reactome.org/content/detail/R-HSA-3878762) is a FailedReaction: catalyst 9631892 → set 3878772 → F257L/R515C GBE1 members. It links normalReaction 3322016. [3878781](https://reactome.org/content/detail/R-HSA-3878781) is the disease pathway containing that event. Failed mutant catalysis is kept separate from normal target activity.
