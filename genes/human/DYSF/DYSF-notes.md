# DYSF manual review notes

## 2026-10-18 source-specific review

All 45 imported source assertions are preserved, including evidence codes, supporting entities and qualifiers. The decisions are 23 ACCEPT, 8 MODIFY, 12 KEEP_AS_NON_CORE and 2 UNDECIDED, with no NEW annotation. Two complementary core activities summarize phospholipid binding and calcium binding. No membrane-repair process annotation is manufactured from the absence of a term in the seed.

The normal Falcon research attempt returned an authentication failure (HTTP 403); the genuine configured Perplexity fallback returned HTTP 401 with insufficient quota. No provider report was created or fabricated. Manual assessment instead uses the preserved normal caches, independently recovered original sources and the [source guide](DYSF-source-guide.md). There was no preexisting DYSF review or notes file to overwrite.

The project-specific [CLINGEN policy](../../../projects/CLINGEN_MENDELIAN.md) retains biologically supported generic protein binding as KEEP_AS_NON_CORE when no evidence-backed specific replacement is warranted. This takes precedence over the generic skill's informational-REMOVE recommendation. Specific partner-class terms are used where supported, without requiring a purified interface or a demonstrated native pathway. Expected generic-binding advisories do not establish false biology.

## Biochemical activities and natural products

Purified human C2-domain studies support calcium binding and acidic-phospholipid binding. The seven-domain study distinguishes basal binding in EDTA from calcium enhancement; the alternative-exon-1 C2A study demonstrates different solution and membrane-associated calcium responses. Neither study makes every natural full-length product functionally equivalent. The earlier positive calcium-sensitive lipid-binding annotation is retained despite incomplete original access. [PMID:11959863](https://pubmed.ncbi.nlm.nih.gov/11959863/), [PMID:24239457](https://pmc.ncbi.nlm.nih.gov/articles/PMC5993433/), [PMID:24461013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3907215/)

All 15 official products are retained. The alternative N-terminal sequence VSP_035924 is shared by products O75923-8 through O75923-14. A fragment representing that class does not identify a unique full-length splice product. Only O75923-15 loses the displayed C-terminal membrane anchor. Historical dysferlin_v1 naming and transcript studies inform diversity but do not override the current official sequence reconstruction. [UniProt O75923](https://www.uniprot.org/uniprotkb/O75923/entry), [PMID:16896923](https://pubmed.ncbi.nlm.nih.gov/16896923/), [PMID:19221801](https://pubmed.ncbi.nlm.nih.gov/19221801/)

## Binding and localization

The human skeletal-muscle interactome used fragments and several validation methods. NEB, MYOM1, MYBPC1, TTN and SGCG have score-A target rows; MYOM2 has score D with positive proximity ligation. Positive IP is listed for MYOM1, whereas MYOM1/MYOM2 have negative colocalization observations. These assay differences remain explicit. The five independently established sarcomeric partner classes support cytoskeletal-protein-binding refinements. SGCG remains positive generic non-core binding because its transmembrane sarcoglycan/DGC membership does not by itself settle the narrower cytoskeletal-component class boundary. Neither choice transfers a partner's structural activity to dysferlin. [PMID:23414517 and supplement](https://pmc.ncbi.nlm.nih.gov/articles/PMC3610214/), [reproducible source audit](DYSF-bioinformatics/source-audit/RESULTS.md)

Endogenous human dysferlin associates with HDAC6 and FAM65B/RIPOR2 in differentiating fetal myogenic cells. This supports the HDAC6 partner-class refinement without assigning deacetylase activity to dysferlin. AHNAK/AHNAK2 associations remain positive with their detailed original-assay access limits. [PMID:24687993](https://pmc.ncbi.nlm.nih.gov/articles/PMC4062822/), [PMID:17185750](https://pubmed.ncbi.nlm.nih.gov/17185750/)

Full-length and mutant trafficking observations support surface and internal endosomal pools. Mouse C2C12 hosts, engineered constructs, indexed publisher Results and native observations are distinguished in the source guide. HPA assigns supported reliability specifically to plasma membrane; centriolar-satellite and midpiece entries are uncertain and are not upgraded by the overall assay score. Reactome's event input resolves to human O75923 residues 1–2080 in cytoplasmic vesicle membrane. None of these gene-level observations supplies the missing membrane anchor to O75923-15. [PMID:20595382](https://pmc.ncbi.nlm.nih.gov/articles/PMC2937879/), [PMID:26707827](https://doi.org/10.1111/tra.12370), [HPA](https://www.proteinatlas.org/ENSG00000135636-DYSF/subcellular), [Reactome R-HSA-5263633](https://reactome.org/content/detail/R-HSA-5263633)

## Contextual functions and remaining uncertainty

The immune study preserves the nonsignificant untreated human monocyte comparison alongside the positive TNF-treated comparison and the separate mouse J774 knockdown. These data support contextual immune annotations without a new receptor mechanism. [PMID:18276788](https://pmc.ncbi.nlm.nih.gov/articles/PMC2258254/)

The PAINT target path and literal IBD assertions are valid. The actual PANTHER geneinfo mapping and sequence establish PTHR45911, despite the different UniProt family pointer. The fly Mctp study demonstrates a presynaptic ER calcium-sensor role, while the rat Mctp1 study remains abstract-only. These donor results and ferlin/MCTP differences leave the two synaptic transfers unresolved; they do not demonstrate a target-specific loss, invalid node or circular evidence. Calcium IBA retains its legitimate target experimental grounding. [PMID:28485711](https://pmc.ncbi.nlm.nih.gov/articles/PMC5449185/), [PMID:26195140](https://pubmed.ncbi.nlm.nih.gov/26195140/), [source audit](DYSF-bioinformatics/source-audit/RESULTS.md)

Urinary-exosome Table 1 directly identifies DYSF by one unique peptide and one spectrum, with the source's manual and database-disambiguation safeguards. The EPS-urine main paper was read, but its target supplement was not recovered. Both positive high-throughput annotations remain non-core detection claims; no contamination conclusion follows from low peptide count or membrane topology. [PMID:19056867](https://pmc.ncbi.nlm.nih.gov/articles/PMC2637050/), [PMID:23533145](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/)

Existing shared publication bytes and their flags remain unchanged. Separately recovered originals are described as such, and fresh variants remain acquisition provenance. The portable analysis publishes only lossless machine-source responses and original supplementary data, not whole article bodies. It reproduces actual target joins and includes independent partner-class locators. No newly authored publication quotation is introduced.


## Follow-up: membrane repair and titin specificity

The participation/comparator audit supersedes the initial decision to omit a repair process. [PMID:24967968](https://pubmed.ncbi.nlm.nih.gov/24967968/) supplies human-cell repair evidence; [PMID:27226605](https://pubmed.ncbi.nlm.nih.gov/27226605/) supplies direct biochemical participation. Dysferlin contributes to the repair machinery rather than being the membrane lesion acted upon. The [saved-source audit](DYSF-bioinformatics/repair-audit/README.md) records the comparator, ancestry, redundancy and GO-CAM checks. GO:0001778 is added once and linked to the existing lipid-binding core. Bansal et al. (PMID:12736685) is HIGH relevance, with its mouse and abstract-only access scope retained.

The PMID:23414517 titin row now proposes GO:0031432, the verified child of GO:0008092. Other cytoskeletal partners retain their original class refinements. The fragment-interaction and tissue-proximity limits remain explicit.
