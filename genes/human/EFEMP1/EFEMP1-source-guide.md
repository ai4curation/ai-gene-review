# EFEMP1 source and assay guide

This guide links the underlying evidence and distinguishes measured observations from interpretation. The review YAML contains the decisions; this guide is not an independent primary source. The [evidence extract](EFEMP1-evidence/README.md) reproduces selected records from hash-identified raw inputs without bundling full articles. Reference access flags describe operative access, not simply the normal publication cache's `full_text_available` metadata.

## Direct functional studies

**Human matrix contribution — PMID:35998264.** The [original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9772001/) was available in the independently fetched full publication cache, including the human cell experiments. A separate XML retrieval failed and is not treated as evidence. Methods specify human ARPE-19 loss/rescue and tagged human constructs in human production cells; the tag is inserted after the signal peptide. Results show altered collagen VI matrix organization, extracellular MMP2 activity and C55R mutant behavior. Wild-type partial rescue and mutant failure support matrix contribution. No purified collagen-binding assay, EFEMP1 protease chemistry or equivalence among natural products is inferred. Selected Methods and all operative Results were read; supplements were not claimed as inspected.

**EGFR association — PMID:19804359.** The [institutional record](https://epub.ub.uni-muenchen.de/17739/) supplies the [publisher PDF](https://epub.ub.uni-muenchen.de/17739/1/bc.2009.140.pdf), SHA256 `5adb48b843728739ec551b36328bd6c2bed6c690101307528a6161c2301bb800`. Selected Methods/Results and PDF page 4 figures 4–7 establish human FG/L3.6pl lysate co-immunoprecipitation, the no-antibody control, reduced association after EGF treatment, and signaling after purchased human EFEMP1. The supplier product is not identified by an accession or construct sequence. An 823-base cDNA check addresses the Arg345 region, not the full assayed protein. The paper contains inconsistent receptor phosphosite labels; no harmonized residue claim is made. Normal cached text remains abstract-only despite this separate original access.

**Chondrogenesis and secretion — PMID:20005202.** A [public research-report PDF](https://mhlw-grants.niph.go.jp/system/files/2010/103081/201025005A/201025005A0022.pdf) contains the article on physical pages 2–7, journal pages 1116–1121. PDF SHA256 is `e8354cc8fbbf70c4c198eed1e6e807d62989812647445782de1e0f1c8bf37529`. The article was read through page-specific OCR with visual checks of Methods/Figure 1. Human IMAGE clone 6083389 was expressed with a C-terminal triple-FLAG tag in mouse ATDC5 cells; purified human protein was produced using Sf9 cells. Stable-expression and extracellular-addition assays suppress differentiation endpoints. The construct is not assigned to a current natural product. The study's proposed TIMP3/ADAM mechanism is an interpretation, not a measured intermediate.

**Cloning and TIMP3 sources — PMID:10601734 and PMID:15123717.** Verified abstracts support fibulin-3 cloning/extracellular distribution and the TIMP3 interaction, respectively. Full original bodies were not recovered. The historical 487-residue cloning sequence is not reconciled to the current 493-residue reference. The microscopy statement in the cloning abstract concerns fibulin-4. The TIMP3 abstract's disease-associated deposits are not a complete normal-compartment experiment or proof of an enzymatic mechanism.

## Proteomics and compartment evidence

| Source | Actual access and target evidence | Limit retained |
|---|---|---|
| [PMID:20551380](https://pubmed.ncbi.nlm.nih.gov/20551380/) | Original human aorta Methods and Tables I–III; FBLN3_HUMAN target fields reproduced in `records.json` | Sequential extraction and peptide detection do not resolve natural products or mechanical strength |
| [PMID:25037231](https://pubmed.ncbi.nlm.nih.gov/25037231/) | Original Methods and Additional File 2; EFEMP1 physical row 43 in complete-data and matrisome sheets | Mixed accession group and multiple tissue contexts are preserved; no isoform-specific assignment |
| [PMID:27068509](https://pubmed.ncbi.nlm.nih.gov/27068509/) | Human normal/varicose saphenous-vein Methods/Results; recovered supplement contains figures | EFEMP1-specific protein table unavailable; broad extracellular location has separate human evidence |
| [PMID:28675934](https://pubmed.ncbi.nlm.nih.gov/28675934/) | Human breast/omental ECM-enrichment Methods, filtering and Discussion in the independently fetched full text | Target supplementary row unavailable; no invented peptide count or direct mechanical assay |
| [PMID:16502470](https://pubmed.ncbi.nlm.nih.gov/16502470/) | Human colostrum abstract | Full body/target table unavailable; broad extracellular pool retained with curator deference and independent evidence |
| [PMID:23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/) | Main original vesicle-preparation and proteomics methods | Target Supplementary Table 2 unavailable; the nominal XLSX route served a challenge, so exosome association remains unresolved |
| [PMID:36399478](https://pubmed.ncbi.nlm.nih.gov/36399478/) | MatrisomeDB original Methods/Results and supplementary workbooks | No target compartment row in the recovered supplement; location is corroborated by independent matrix/elastic-fiber evidence |

[HPA EFEMP1 subcellular data](https://www.proteinatlas.org/ENSG00000115380-EFEMP1/subcellular) report mitochondria with location-specific **enhanced** reliability; the [XML](https://www.proteinatlas.org/ENSG00000115380.xml) overall reliability is **supported**. The antibody/cell-line records include additional nuclear pools in some contexts. These are positive observations, not a demonstrated mitochondrial biochemical role. Images were not independently scored. The extracellular signal sequence is not used as a topological disproof of this pool.

The [elastic-fiber review](https://www.cambridge.org/core/journals/expert-reviews-in-molecular-medicine/article/elastic-fibres-in-health-and-disease/82C47BA5781BD354DC48CFEABE8D5A5A) (PMID:23962539) explicitly discusses fibulin-3 association and tissue-specific mouse defects. Its fibulin-4/5 binding mechanisms remain separate. Current [elastic-fiber GO relationships](https://www.ebi.ac.uk/QuickGO/term/GO:0071953) support the broader non-collagenous interstitial matrix context. They do not establish the distinct basement-membrane compartment.

## Interaction records and source-specific scope

`records.json` retains the complete fields of every matching current IntAct/MINT record for the 46 imported source/partner joins. Its `source_index` is zero-based and paired with literal PMID/partner identifiers, so row numbering is never the sole evidence key. The two current-query absences are not treated as negative experiments:

- **PMID:18985028, NS5A processed chain.** Original Methods identify genotype-1b HCV constructs and human-library/HEK293T assays. Supplementary Table SI physical row 375 is EFEMP1–NS5A with positive co-affinity purification; row 180 is a separate NS3 pair. The last column denotes liver expression. NS5A is not NS5B polymerase. Headers and both target rows are reproduced from the original XLS member.
- **PMID:19275936, ECM1.** The verified abstract explicitly reports human foreskin-library Y2H, in vitro/in vivo co-immunoprecipitation and human-skin colocalization with EFEMP1. The complete original body was not recovered. Matrix-binding class is supported; a purified interface is not claimed.

For PMID:12620389, 16189514, 16713569 and 32814053, abstracts plus literal source-specific interaction records were available, but original bodies were not recovered. PMID:25416956, 25910212 and 26871637 have incomplete accessible main-text sections; their database records provide exact pair/variant/feature evidence, without a claim to unseen complete Methods or inserts. Selected operative text was also read for PMID:21653829, 31515488 and 32296183. HuRI's heterologous binary-assay context remains explicit.

The [source-linked partner-class table](EFEMP1-evidence/partner-classes.yaml) accompanies the literal records. Important distinctions are:

- **ARAF:** sufficient-binding regions 66–155, 2–314 and 2–350 are N-terminal regulatory segments. Binding to a kinase protein does not require its active site and does not assign kinase activity to EFEMP1.
- **HOXA1:** one sufficient-binding feature is 1–110; the parent-sequence checksum is a separate statement. A verified transcription-factor class does not transfer transcriptional activity to EFEMP1.
- **Q86UY0/TXNDC5:** the literal 360-residue parent matches its database checksum. Its residues 17–360 equal reviewed [Q8NBS9](https://www.uniprot.org/uniprotkb/Q8NBS9/entry) residues 89–432; its first 16 residues differ. All three CGHC motifs and two complete C-terminal thioredoxin domains remain. Protein-disulfide-isomerase class is an inference from conserved sequence and official annotation, not an enzyme assay of the historical clone.
- **Q6FHY5/MEOX2:** the literal 303-residue sequence equals current [P50222](https://www.uniprot.org/uniprotkb/P50222/entry) with canonical Q81 deleted; the homeobox remains. The old identifier is preserved.
- **RIC8A-4:** deletion of reference residue 209 retains the verified chaperone class; separately recorded 111–530 sufficient-binding regions do not become full-length construct proof.
- **MSRB3-2:** the 185-residue product retains the MsrB domain and catalytic cysteine (canonical C158 maps to product-2 C151), supporting enzyme-class binding.
- **ANAPC11-2:** the 196-residue product replaces canonical residues 38–84, covering much of the RING domain. Canonical E3-ligase class is not automatically transferred, and catalytic inactivity is not asserted.
- **KRTAP/LCE proteins:** keratin association or cornified-envelope membership does not establish the cytoskeletal-component definition. **BAG4/BAG5:** an HSP70 co-chaperone/nucleotide-exchange role alone does not establish the direct unfolded-substrate-binding chaperone class. Positive generic pairs remain non-core, without requiring an EFEMP1 client-folding mechanism.
- **HTT:** the recorded sufficient-binding region is 1–546, with polyglutamine features; this does not establish an EFEMP1 neurodegeneration or transport function.

## Propagation, models and source identity

The portable extract records the exact target path and two literal IBD assertions from PTN000620536. The current family is PTHR24039, while the older PTHR24050 pointer remains unchanged in the machine source. The target MSA sequence matches Q12805 exactly; this authenticates the reference sequence, not an experimental insert. Current matrix-location IBD donors differ from the imported GOA snapshot and are retained separately. Experimental descendant records include human fibrillin and worm fibulin evidence; donor paper bodies were not claimed as independently read. No relevant NOT/IRD was found on the target path. Node placement, rather than donor count, grounds the transfer.

The current [InterPro IPR001881](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR001881/) and [IPR018097](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR018097/) mappings support calcium-binding EGF modules. This is domain inference, not a measured EFEMP1 calcium affinity. Current ARBA00084594 and ARBA00096893 rule bodies were inspected, but complete triggering conditions were not reconstructed from the target snapshot. Independently supported elastic-fiber location is retained; the narrower basement-membrane assignment remains unresolved.

The exact Reactome chains are:

- [R-HSA-1592387](https://reactome.org/content/detail/R-HSA-1592387) input DefinedSet 2395327 → `hasMember` 2161393.
- [R-HSA-2161282](https://reactome.org/content/detail/R-HSA-2161282) input complex 2396077 → complex 2395337 → DefinedSet 2395327 → `hasMember` 2161393.

Entity 2161393 identifies mature human Q12805 residues 18–493 in the extracellular region. Set membership supports the modeled location; it is not a purified physical-interaction assay.

## Verified citation mismatch and remaining uncertainty

For PMID:25406291, complete operative Methods/Results and Discussion describe FBN1/FBN2/FBN3 and MAGP1 in developing human eyes. Methods specify fibrillin antibodies, not EFEMP1. The three IEP removals are based on that verified target distinction, not a title-only inference. The publication identifier and original annotation fields remain unchanged.

The three unresolved assertions concern visual perception, the target-specific exosome measurement, and the specific basement-membrane compartment. Human retinal disease, secretion and general matrix detection do not by themselves settle these narrower claims. Positive observations and source provenance remain intact.
