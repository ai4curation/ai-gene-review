# B3GLCT review notes

## 2026-09-30: identity, source review, and manual research

Human B3GLCT is HGNC:20207, UniProt Q6Y288 (B3GLT_HUMAN), a 498-residue protein. B3GALTL and B3GTL are historical gene symbols; the old name does not establish galactosyltransferase activity. The unchanged normal UniProt and GOA files were imported with a 14-annotation initialized seed. All 14 distinct GOA source tuples and their supporting entities are preserved; there are no isoform-specific or negated rows in this snapshot and no alternative-product block in UniProt.

The ordinary Falcon research command, including its perplexity-lite fallback option, failed without producing a report. These are manual notes, not provider output. An independent annotation audit agrees with the provisional 9 ACCEPT / 5 MODIFY decisions. Additional normal publication-cache retrieval and final biological review remain pending.

### Direct catalytic function

B3GLCT extends the O-fucose installed by POFUT2 on folded thrombospondin type 1 repeats (TSRs), using UDP-glucose to make Glc-beta-1,3-Fuc. Recombinant human enzyme and product characterization directly establish glucose transfer. The assay first fucosylates a TSR using POFUT2, then adds B3GLCT. [PMID:16899492, Sato et al.](https://pubmed.ncbi.nlm.nih.gov/16899492/), normal abstract: “transfer Glc to the
fucosylated TSR domain”. The complete normal abstract and UniProt entry have been read; complete experimental Methods for this paper have not.

The independent Kozma study distinguishes correctly folded fucosylated TSR acceptors from EGF repeats and unfucosylated modules. Its complete indexed PubMed abstract was read, but not its full Methods. [PMID:17032646](https://pubmed.ncbi.nlm.nih.gov/17032646/).

GO:0160265 specifies this glucosyltransferase chemistry. The seeded IBA GO:0008375 instead names acetylglucosaminyltransferase activity. The proposed modification is based on target-specific donor chemistry, not donor count. The recorded PAINT node is PTN000087478; its tree placement has not been independently reconstructed. The mixed Fringe-related family contains enzymes with different specificities, but family membership alone does not locate the evolutionary change. The official GO:0036066 definition includes extension of initially attached O-fucose, so B3GLCT directly participates in that process without being the enzyme that transfers the initial fucose.

### Location and pathway provenance

The Sato abstract supports ER residence and the C-terminal REEL retention signal. UniProt additionally records type II membrane topology, with a lumen-facing catalytic region. The curator's ER-membrane IDA is retained; lack of full topology Methods in the abstract is not contradictory evidence. All three normal Reactome caches were read in full. The defective-enzyme event R-HSA-6785565 describes loss of a normal reaction: its title does not negate the unnegated wild-type GOA activity or location. The broader R-HSA-5173214 pathway includes predicted substrate assignments, which are not all direct experiments.

### Substrate-dependent secretion and evidence limits

The 2015 study found that B3GLCT knockdown affected secretion of selected TSR-containing clients. Its POFUT2 refolding assay must not be reassigned to B3GLCT. [PMID:25544610](https://pmc.ncbi.nlm.nih.gov/articles/PMC4318717/). The 2020 study explicitly used mouse ADAMTSL2 in HEK293T cells and found that B3GLCT knockout did not reduce secretion, whereas POFUT2 knockout did. This limits the earlier ADAMTSL2 inference without disproving all client-specific effects or establishing universal dispensability. The proposed off-target explanation for the earlier siRNA result remains the authors' interpretation. [PMID:32913123](https://pmc.ncbi.nlm.nih.gov/articles/PMC7667967/). Selected Methods, Results and captions were inspected; no complete-paper or supplement review is claimed.

### Structural and disease context

The 2021 mutagenesis paper used structural modeling; the later 2026 report provides an experimental two-domain structure. The inactive N-terminal domain contributes substrate recognition, while the C-terminal domain catalyzes transfer. Neither finding makes the whole protein a pseudoenzyme. The PDB 12EM A1B1 assembly contains enzyme and TSR substrate, not two B3GLCT subunits, and does not cover all 498 canonical residues. Full 2026 Methods and coordinates have not been inspected. [PMID:34058199](https://pubmed.ncbi.nlm.nih.gov/34058199/), [PMID:42575440](https://pubmed.ncbi.nlm.nih.gov/42575440/), [PDB 12EM](https://www.rcsb.org/structure/12EM).

Biallelic disease association supports Peters plus syndrome context, not extra molecular activities. Mouse Adamts9 eye phenotypes and recombinant ADAMTS9 secretion experiments have distinct organism and construct scopes; no protease activity is assigned to B3GLCT. [PMID:18798333](https://pubmed.ncbi.nlm.nih.gov/18798333/), [PMID:27687499](https://pubmed.ncbi.nlm.nih.gov/27687499/). The proposed core is the ER glucosylation reaction. No new Notch-signaling, universal secretion, or general developmental-process assertion is proposed.


## 2026-09-30: recovered literature integration

The seven requested normal publication caches are now imported and their bytes verified. The complete abstracts and selected relevant Results, Discussion, Methods and captions were read. This is not a whole-paper, figure-image, supplement or coordinate review. The 14 original annotation tuples and supporting entities remain unchanged: 9 ACCEPT, 5 MODIFY, one catalytic core and no NEW annotations.

The Kozma abstract supports folded, fucosylated TSR specificity and excludes the tested EGF-like acceptor. Its soluble-enzyme description differs from the UniProt type II topology record. Full Kozma Methods remain unavailable; recombinant solubility does not settle endogenous topology. The ER-membrane IDA is retained with this limitation and a suggested question. [PMID:17032646](https://pubmed.ncbi.nlm.nih.gov/17032646/).

The 2015 glucose-dependent TSR stabilization result remains supported. Its ADAMTSL2 secretion finding receives a limited DISPUTED assessment because the later mouse-ADAMTSL2 knockout assay found secretion unchanged. Construct species is unresolved in the inspected 2015 Methods; the 2020 siRNA explanation remains an interpretation. The POFUT2 refolding assay is not reassigned to B3GLCT. [PMID:25544610](https://pubmed.ncbi.nlm.nih.gov/25544610/), [PMID:32913123](https://pubmed.ncbi.nlm.nih.gov/32913123/).

ADAMTS9 experiments used recombinant human fragments, separate from mouse eye phenotypes. The abstract names HEK293F, whereas the knockdown Methods name HEK293T; the earlier note reflects the abstract. No universal secretion requirement is inferred. [PMID:27687499](https://pubmed.ncbi.nlm.nih.gov/27687499/). The clinical series supports disease association without adding a molecular activity. [PMID:18798333](https://pubmed.ncbi.nlm.nih.gov/18798333/).

The 2026 structure resolves acceptor recognition by adjoining GT-A domains, with an inactive N-terminal domain and active C-terminal domain. UDP/Mn binding and chelation revise the 2021 metal-independence suggestion at finding level. The older mutagenesis remains informative. The enzyme is truncated, and printed residue boundaries are inconsistent; exact boundaries and resolution are unnecessary here. The proposed reaction geometry includes modeling. No whole-protein pseudoenzyme, second catalytic function, or Notch assertion is added. [PMID:34058199](https://pubmed.ncbi.nlm.nih.gov/34058199/), [PMID:42575440](https://pubmed.ncbi.nlm.nih.gov/42575440/).

The repeated Sato snippet on the activity IDA row was removed. Its core and ER-location snippets remain, alongside the earlier notes quotation. Every new supporting snippet is exact source text, with total quotations limited to 25 words per paper across the proposed review and notes. Independent final biological peer and canonical application remain pending at this entry.


## PR 3575 evidence-anchor follow-up

The exact-head review approved the biology and suggested a more informative localization excerpt. Expanded only the PMID16899492 ER-residence anchor to include the retention context; this supports ER residence while the existing reason separately qualifies membrane topology. Annotation actions, source tuples, references and the catalytic core are unchanged. The aggregate PMID16899492 quotation count across review and notes is 23 words; no additional quote is added here.
