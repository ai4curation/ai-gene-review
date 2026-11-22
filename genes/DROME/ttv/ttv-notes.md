# ttv-PC review notes

The native 299-residue PC isoform matches full-length residues 462–760 and preserves the C-terminal catalytic-site region. The N-terminal glycosyltransferase domain and membrane anchor are absent. Broad activity is not refuted solely from shortening because exostosins possess two chemically distinct domains. [PMID:36593275](https://pubmed.ncbi.nlm.nih.gov/36593275/) and [PMID:36402845](https://pubmed.ncbi.nlm.nih.gov/36402845/) characterize this division and describe important complex/construct qualifications. The structural studies describe domain-specific chemistry and important expression/activity limitations for isolated constructs; neither assays native fly PC. All five IEAs and the single GO prediction remain UNC pending direct exact-isoform evidence; no wrong-input assertion is made.

## Provider research assessment

The Falcon synthesis integrates fly EXT genetics, morphogen distribution and human EXT1 rescue. These strongly support the full-length Ttv gene function. Its ER/Golgi and copolymerase conclusions do not specifically establish activity or targeting of the native 299-residue PC product, which lacks the N-terminal domain and anchor. The retained C-terminal architecture and primary EXT domain studies support keeping the exact-product glycosyltransferase question open.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files and prediction-evidence folders were not opened. The earlier sections above are left unchanged.

### Identity
- The benchmark accession D5SHU8 is **ttv-PC** (FlyBase FBpp0305368, transcript ttv-RC, 299 aa). It is an **N-terminally truncated alternative product** of the ttv gene, not the canonical protein. The canonical, reviewed product is **Q9V730 (EXT1_DROME)**: 760 aa, encoded by ttv-PA and ttv-PB. A 772-aa PD product also exists. [file:DROME/ttv/ttv-flybase.txt "ttv-PC FBpp0305368 34.4 299 9.71 D5SHU8 NP_001260972 AGB93504"]
- D5SHU8 is 100% identical to Q9V730 residues 462-760. Compared with the canonical product it is missing the cytoplasmic tail and the type II signal-anchor helix (TRANSMEM 7-25), the whole N-terminal GT47/GT-B (GlcA-transferase) domain, and the UDP-GlcNAc binding residue at 437. It keeps the C-terminal GT64/GT-A domain, including the DxD motif (D581/D583 in Ttv numbering, D120/D122 in D5SHU8), Asp670 and R713. [file:DROME/ttv/ttv-bioinformatics/rereview/RESULTS-rereview.md]
- PE 2: supported only at the transcript level (a cDNA, MIP20656p).

### Evolutionary grounding
- PANTHER: D5SHU8, Q9V730 and human EXT1 (Q16394) are all in PTHR48261:SF3 (EXOSTOSIN GLYCOSYLTRANSFERASE 1). Sotv (Q9Y169) and human EXT2 (Q93063) are in SF5 (UniProt PANTHER cross-references, fetched 2026-10-20). Human EXT1 is therefore the subfamily-matched comparator. Over the human EXT1 GT-A region, identity is 60.4% to Ttv and 42.0% to Sotv.
- Human EXT1-EXT2 structures (PMID:36593275): the active sites are EXT1 GT-B (GlcA-T) and EXT2 GT-A (GlcNAc-T). EXT1 GT-A is "weakly active", and mutating it had only minor effects. Single EXT1 GT-A or GT-B domains gave no secreted protein. In PMID:36402845, mutating the EXT1 GT-A DxD reduced GlcNAc-T activity, so the two groups partly disagree on whether EXT1 GT-A contributes. In both studies, any activity of this domain was seen only inside the full-length heterodimer.
- In ttv-PC, the residues aligned to the EXT2 uridine-stacking Tyr and phosphate-binding Arg are I24 and A26. This follows the EXT1-type pattern, not the active EXT2 pattern (about ±4 residues of loop alignment uncertainty).
- PAINT gives Q9V730 IBA rows for acetylglucosaminyltransferase and glucuronosyltransferase activity. D5SHU8 has no IBA rows, most likely because of isoform coverage. This is not read as a curator's decision.

### Annotation decisions (5 IEA rows)
- GO:0005789 ER membrane (SubCell/ARBA): **REMOVE**. The ARBA type II signal-anchor topology is contradicted by the sequence, which has no anchor helix.
- GO:0016020 membrane (InterPro): **MARK_AS_OVER_ANNOTATED**. There is no anchor, and membrane association through partners is undemonstrated.
- GO:0016757 glycosyltransferase activity (InterPro): **MARK_AS_OVER_ANNOTATED**. This is a weakly active EXT1-type GT-A domain without luminal targeting.
- GO:0009101 glycoprotein biosynthetic process, GO:1901135 carbohydrate derivative metabolic process: **MARK_AS_OVER_ANNOTATED**. These roles are true of the gene through full-length Ttv, not this isoform.
- These rows were previously all UNDECIDED. The re-review uses the human EXT1 GT-A domain data, which are subfamily-matched (SF3), and the absence of a signal anchor to argue against transferring them to this product.
- core_functions are left empty because no function is established for the ttv-PC product. The gene-level function (Ttv-Sotv heparan sulfate co-polymerase, ER/Golgi) belongs in a review of Q9V730.

### Relative and modules
- Next relative: **Q9V730 ttv (same_gene_canonical)**. There is no review for it in the repo; its folder would be genes/DROME/ttv__Q9V730.
- The family review interpro/panther/PTHR48261/PTHR48261-review.yaml lists D5SHU8 as the SF3 representative. It agrees with the subfamily placement, but the canonical Q9V730 or human EXT1 would be a better representative for SF3.
- Module: modules/dmel_glycosaminoglycan_biosynthesis.yaml (it uses UniProtKB:Q9V730 for ttv).
