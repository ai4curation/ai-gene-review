# Suppressed-evidence candidates: references whose findings were never extracted

Generated while removing 80 stale `full_text_unavailable: true` flags (the PR that added
`ai-gene-review audit-fulltext-flags`). Every row below carried that flag while its cached
publication reports `full_text_available: true` — so the flag discouraged extracting evidence that
was available all along.

**39 of 79 also have zero `findings`**, which is the signature: the flag did not merely
mislabel the reference, it suppressed the extraction. Those are the curation candidates below.
Removing the flag (already done) does **not** re-extract the evidence — that is a reading task, not a
mechanical one.

Re-check the current state at any time with `just audit-fulltext-flags`.

## Zero findings — highest priority

| gene review | PMID | title |
|---|---|---|
| `genes/DESVH/Q726C4/Q726C4-ai-review.yaml` | [24639670](https://pubmed.ncbi.nlm.nih.gov/24639670/) | Exploring the role of CheA3 in Desulfovibrio vulgaris Hildenborough mo |
| `genes/ECOLI/rbsD/rbsD-ai-review.yaml` | [18304323](https://pubmed.ncbi.nlm.nih.gov/18304323/) | Protein abundance profiling of the Escherichia coli cytosol. |
| `genes/human/CD28/CD28-ai-review.yaml` | [12028592](https://pubmed.ncbi.nlm.nih.gov/12028592/) | The regulation of protein synthesis and translation factors by CD3 and |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [11953320](https://pubmed.ncbi.nlm.nih.gov/11953320/) | Regulation of the ubiquitin-conjugating enzyme hHR6A by CDK-mediated p |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [11980914](https://pubmed.ncbi.nlm.nih.gov/11980914/) | Human Speedy: a novel cell cycle regulator that enhances proliferation |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [15107404](https://pubmed.ncbi.nlm.nih.gov/15107404/) | Liver tumors escape negative control of proliferation via PI3K/Akt-med |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [16061792](https://pubmed.ncbi.nlm.nih.gov/16061792/) | Association of the human papillomavirus type 16 E7 oncoprotein with th |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [16326706](https://pubmed.ncbi.nlm.nih.gov/16326706/) | Shp-1 mediates the antiproliferative activity of tissue inhibitor of m |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [16431923](https://pubmed.ncbi.nlm.nih.gov/16431923/) | The nucleocapsid protein of severe acute respiratory syndrome-coronavi |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [17053782](https://pubmed.ncbi.nlm.nih.gov/17053782/) | C-terminal phosphorylation controls the stability and function of p27k |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [17418410](https://pubmed.ncbi.nlm.nih.gov/17418410/) | HIF-2alpha promotes hypoxic cell proliferation by enhancing c-myc tran |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [17698606](https://pubmed.ncbi.nlm.nih.gov/17698606/) | SCAPER, a novel cyclin A-interacting protein that regulates cell cycle |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [18177895](https://pubmed.ncbi.nlm.nih.gov/18177895/) | Role of intrinsic flexibility in signal transduction mediated by the c |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [19150984](https://pubmed.ncbi.nlm.nih.gov/19150984/) | Identification and functional analysis of a novel cyclin e/cdk2 substr |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [20871633](https://pubmed.ncbi.nlm.nih.gov/20871633/) | p38 phosphorylates Rb on Ser567 by a novel, cell cycle-independent mec |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [21092281](https://pubmed.ncbi.nlm.nih.gov/21092281/) | HTLV-I p30 inhibits multiple S phase entry checkpoints, decreases cycl |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [21423803](https://pubmed.ncbi.nlm.nih.gov/21423803/) | Role of T198 modification in the regulation of p27(Kip1) protein stabi |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [21952639](https://pubmed.ncbi.nlm.nih.gov/21952639/) | NIRF constitutes a nodal point in the cell cycle network and is a cand |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [22810586](https://pubmed.ncbi.nlm.nih.gov/22810586/) | Interpreting cancer genomes using systematic host network perturbation |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [22940584](https://pubmed.ncbi.nlm.nih.gov/22940584/) | The molecular basis for substrate specificity of the nuclear NIPP1:PP1 |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [23082202](https://pubmed.ncbi.nlm.nih.gov/23082202/) | The stomatin-like protein SLP-1 and Cdk2 interact with the F-Box prote |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [23184662](https://pubmed.ncbi.nlm.nih.gov/23184662/) | Phosphorylation of eukaryotic elongation factor 2 (eEF2) by cyclin A-c |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [23781148](https://pubmed.ncbi.nlm.nih.gov/23781148/) | Overexpression of DOC-1R inhibits cell cycle G1/S transition by repres |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [24358021](https://pubmed.ncbi.nlm.nih.gov/24358021/) | Polycomb protein SCML2 regulates the cell cycle by binding and modulat |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [24670654](https://pubmed.ncbi.nlm.nih.gov/24670654/) | Cell-cycle-regulated activation of Akt kinase by phosphorylation at it |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) | A proteome-scale map of the human interactome network. |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [28514442](https://pubmed.ncbi.nlm.nih.gov/28514442/) | Architecture of the human interactome defines protein communities and  |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [29997244](https://pubmed.ncbi.nlm.nih.gov/29997244/) | LuTHy: a double-readout bioluminescence-based two-hybrid technology fo |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [31467278](https://pubmed.ncbi.nlm.nih.gov/31467278/) | Maximizing binary interactome mapping with a minimal number of assays. |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | Dual proteome-scale networks reveal cell-specific remodeling of the hu |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [34591612](https://pubmed.ncbi.nlm.nih.gov/34591612/) | A protein interaction landscape of breast cancer. |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [34591642](https://pubmed.ncbi.nlm.nih.gov/34591642/) | A protein network map of head and neck cancer reveals PIK3CA mutant dr |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/) | OpenCell: Endogenous tagging for the cartography of human cellular org |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [37398436](https://pubmed.ncbi.nlm.nih.gov/37398436/) | AI-guided pipeline for protein-protein interaction drug discovery iden |
| `genes/human/CDK2/CDK2-ai-review.yaml` | [40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) | Multimodal cell maps as a foundation for structural and functional gen |
| `genes/human/CHAMP1/CHAMP1-ai-review.yaml` | [29656893](https://pubmed.ncbi.nlm.nih.gov/29656893/) | DNA Repair Network Analysis Reveals Shieldin as a Key Regulator of NHE |
| `genes/human/CHAMP1/CHAMP1-ai-review.yaml` | [29789392](https://pubmed.ncbi.nlm.nih.gov/29789392/) | FAM35A associates with REV7 and modulates DNA damage responses of norm |
| `genes/human/CHAMP1/CHAMP1-ai-review.yaml` | [36044844](https://pubmed.ncbi.nlm.nih.gov/36044844/) | CHAMP1 binds to REV7/FANCV and promotes homologous recombination repai |
| `genes/human/KCTD12/KCTD12-ai-review.yaml` | [32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | A reference map of the human binary protein interactome. |

## Findings present despite the stale flag — lower priority

The flag was wrong but did not stop the work.

| gene review | PMID | findings |
|---|---|---|
| `genes/ANOGA/PGRPLD/PGRPLD-ai-review.yaml` | [29489896](https://pubmed.ncbi.nlm.nih.gov/29489896/) | 5 |
| `genes/ANOGA/PGRPLD/PGRPLD-ai-review.yaml` | [31907025](https://pubmed.ncbi.nlm.nih.gov/31907025/) | 1 |
| `genes/DANRE/dph2/dph2-ai-review.yaml` | [20559380](https://pubmed.ncbi.nlm.nih.gov/20559380/) | 1 |
| `genes/DANRE/dph2/dph2-ai-review.yaml` | [24422557](https://pubmed.ncbi.nlm.nih.gov/24422557/) | 1 |
| `genes/DANRE/dph2/dph2-ai-review.yaml` | [29590073](https://pubmed.ncbi.nlm.nih.gov/29590073/) | 1 |
| `genes/DANRE/dph2/dph2-ai-review.yaml` | [32576952](https://pubmed.ncbi.nlm.nih.gov/32576952/) | 1 |
| `genes/DANRE/dph2/dph2-ai-review.yaml` | [34154323](https://pubmed.ncbi.nlm.nih.gov/34154323/) | 1 |
| `genes/DANRE/dph2/dph2-ai-review.yaml` | [37675463](https://pubmed.ncbi.nlm.nih.gov/37675463/) | 1 |
| `genes/DANRE/dph2/dph2-ai-review.yaml` | [38671004](https://pubmed.ncbi.nlm.nih.gov/38671004/) | 1 |
| `genes/METEA/sucB/sucB-ai-review.yaml` | [19440302](https://pubmed.ncbi.nlm.nih.gov/19440302/) | 1 |
| `genes/MYCTU/clpP2/clpP2-ai-review.yaml` | [35507665](https://pubmed.ncbi.nlm.nih.gov/35507665/) | 1 |
| `genes/PSEPK/tolC/tolC-ai-review.yaml` | [35682576](https://pubmed.ncbi.nlm.nih.gov/35682576/) | 1 |
| `genes/human/ABRAXAS1/ABRAXAS1-ai-review.yaml` | [39009827](https://pubmed.ncbi.nlm.nih.gov/39009827/) | 1 |
| `genes/human/AIPL1/AIPL1-ai-review.yaml` | [38439910](https://pubmed.ncbi.nlm.nih.gov/38439910/) | 1 |
| `genes/human/AIPL1/AIPL1-ai-review.yaml` | [41465493](https://pubmed.ncbi.nlm.nih.gov/41465493/) | 1 |
| `genes/human/ANKZF1/ANKZF1-ai-review.yaml` | [37158785](https://pubmed.ncbi.nlm.nih.gov/37158785/) | 1 |
| `genes/human/ANKZF1/ANKZF1-ai-review.yaml` | [38388640](https://pubmed.ncbi.nlm.nih.gov/38388640/) | 1 |
| `genes/human/ARF1/ARF1-ai-review.yaml` | [36269825](https://pubmed.ncbi.nlm.nih.gov/36269825/) | 1 |
| `genes/human/ATG2A/ATG2A-ai-review.yaml` | [38622126](https://pubmed.ncbi.nlm.nih.gov/38622126/) | 1 |
| `genes/human/ATG2B/ATG2B-ai-review.yaml` | [30952800](https://pubmed.ncbi.nlm.nih.gov/30952800/) | 1 |
| `genes/human/ATG2B/ATG2B-ai-review.yaml` | [38622126](https://pubmed.ncbi.nlm.nih.gov/38622126/) | 1 |
| `genes/human/BCL2L13/BCL2L13-ai-review.yaml` | [26146385](https://pubmed.ncbi.nlm.nih.gov/26146385/) | 2 |
| `genes/human/BCL2L13/BCL2L13-ai-review.yaml` | [34193180](https://pubmed.ncbi.nlm.nih.gov/34193180/) | 1 |
| `genes/human/BCL2L13/BCL2L13-ai-review.yaml` | [36589739](https://pubmed.ncbi.nlm.nih.gov/36589739/) | 2 |
| `genes/human/BCL2L13/BCL2L13-ai-review.yaml` | [37660127](https://pubmed.ncbi.nlm.nih.gov/37660127/) | 1 |
| `genes/human/BCL2L13/BCL2L13-ai-review.yaml` | [38494498](https://pubmed.ncbi.nlm.nih.gov/38494498/) | 1 |
| `genes/human/BCL2L13/BCL2L13-ai-review.yaml` | [39175772](https://pubmed.ncbi.nlm.nih.gov/39175772/) | 2 |
| `genes/human/BNIP3L/BNIP3L-ai-review.yaml` | [38992176](https://pubmed.ncbi.nlm.nih.gov/38992176/) | 1 |
| `genes/human/CALCOCO1/CALCOCO1-ai-review.yaml` | [18722177](https://pubmed.ncbi.nlm.nih.gov/18722177/) | 1 |
| `genes/human/CALCOCO1/CALCOCO1-ai-review.yaml` | [25422592](https://pubmed.ncbi.nlm.nih.gov/25422592/) | 1 |
| `genes/human/CALCOCO1/CALCOCO1-ai-review.yaml` | [38822137](https://pubmed.ncbi.nlm.nih.gov/38822137/) | 1 |
| `genes/human/CALCOCO1/CALCOCO1-ai-review.yaml` | [39871880](https://pubmed.ncbi.nlm.nih.gov/39871880/) | 1 |
| `genes/human/DPT/DPT-ai-review.yaml` | [20551380](https://pubmed.ncbi.nlm.nih.gov/20551380/) | 1 |
| `genes/human/DPT/DPT-ai-review.yaml` | [25037231](https://pubmed.ncbi.nlm.nih.gov/25037231/) | 1 |
| `genes/human/DPT/DPT-ai-review.yaml` | [27068509](https://pubmed.ncbi.nlm.nih.gov/27068509/) | 1 |
| `genes/human/DPT/DPT-ai-review.yaml` | [27559042](https://pubmed.ncbi.nlm.nih.gov/27559042/) | 1 |
| `genes/human/DPT/DPT-ai-review.yaml` | [28675934](https://pubmed.ncbi.nlm.nih.gov/28675934/) | 1 |
| `genes/worm/atf-4/atf-4-ai-review.yaml` | [23692540](https://pubmed.ncbi.nlm.nih.gov/23692540/) | 3 |
| `genes/worm/csr-1/csr-1-ai-review.yaml` | [19123269](https://pubmed.ncbi.nlm.nih.gov/19123269/) | 1 |
| `genes/worm/lbp-8/lbp-8-ai-review.yaml` | [30713071](https://pubmed.ncbi.nlm.nih.gov/30713071/) | 1 |
