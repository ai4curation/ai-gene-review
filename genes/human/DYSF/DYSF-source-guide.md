# DYSF source and evidence guide

This guide identifies the evidence actually examined and separates ordinary publication-cache contents from independently recovered originals. It is a locator, not an additional biological experiment. All 45 imported assertions remain intact; 15 products, two core activities and zero NEW annotations are represented. All support is reference-only, with no newly authored publication excerpts.

## Biochemical and product evidence

| Source | Actual evidence and access | Limits |
|---|---|---|
| [PMID:11959863](https://doi.org/10.1074/jbc.M201858200) | Authentic complete abstract positively reports calcium-sensitive phospholipid binding and a mutant effect. | Publisher/JBC attempts did not recover full original text. Detailed unseen construct/figure claims are not asserted. |
| [PMID:24239457](https://pmc.ncbi.nlm.nih.gov/articles/PMC5993433/) | Complete operative Methods/Results: bacterial expression of human canonical C2A 1–125 and alternative C2Av1 1–126 fragments; calcium/lipid assays; full-length surface experiments. | C2Av1 Cys2Ala and tag/protease handling are construct details. Surface experiments shown are in mouse C2C12; the corresponding HEK293 result is data not shown. Alternative exon 1 is a sequence class, not a unique complete natural isoform. |
| [PMID:24461013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3907215/) | Protein-expression, ITC and liposome Methods plus corresponding Results were read. Human AF075575.1-derived isolated C2 domains show calcium binding and acidic-lipid binding, including EDTA baseline and calcium enhancement. | No intact-product repair assay or equivalence across all 15 products follows from these isolated domains. |
| [UniProt O75923](https://www.uniprot.org/uniprotkb/O75923/entry) | All 15 official FASTAs were independently reconstructed from the displayed sequence and stated variation features. | VSP_035924 occurs in products 8–14; only product 15 lacks the canonical membrane anchor. Historical naming in [16896923](https://pubmed.ncbi.nlm.nih.gov/16896923/) and [19221801](https://pubmed.ncbi.nlm.nih.gov/19221801/) was checked at abstract scope. |

## Interactions and partner classes

[PMID:23414517](https://pmc.ncbi.nlm.nih.gov/articles/PMC3610214/) was read at full operative Methods/Results scope, with the [genuine supplementary archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3610214/supplementaryFiles). The public [source audit](DYSF-bioinformatics/source-audit/RESULTS.md) reproduces the exact six target-pair rows and source-specific validation fields. File `2044-5040-3-3-S1.xls` is internally named `Table S2`; rows 399, 402, 403, 405, 469 and 1137 identify MYBPC1, MYOM1, NEB, TTN, MYOM2 and SGCG, respectively. The independent bait file `S2.xls`, internally `Table S1`, gives DYSF L2–I485 at row 12. These mismatched source labels are preserved.

The [IntAct query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id:O75923?format=tab27) contains 101 records. Publication-and-partner joins select 34 records; all 68 participant reference checksums match saved sequences. The complete record identifiers, taxa, roles and feature strings are in the replay output. These checks authenticate reference participants, not complete experimental inserts or unique natural isoforms. Human Y2H libraries, mouse co-IP and human biopsy proximity imaging remain separate. Negative colocalization does not itself negate a positive interaction assay.

Independent official partner-class links and the exact current definitions of [GO:0008092](https://www.ebi.ac.uk/QuickGO/term/GO:0008092) and [GO:0042826](https://www.ebi.ac.uk/QuickGO/term/GO:0042826) are included in RESULTS.md and the saved inputs. Class refinements do not assign the partner's activity to dysferlin. SGCG's membrane/DGC role remains distinguished from an established actin-, microtubule- or intermediate-filament structural component.

[PMID:24687993](https://pmc.ncbi.nlm.nih.gov/articles/PMC4062822/) was independently recovered and read through human-cell differentiation, endogenous co-IP and operative assay Methods. Positive dysferlin/HDAC6 and dysferlin/FAM65B-RIPOR2 associations are separate from the deacetylase assay. The effective normal cache remains abstract-only. [PMID:17185750](https://doi.org/10.1096/fj.06-6628com) remains abstract-only despite bounded original attempts; its positive reported AHNAK interaction and official AHNAK/AHNAK2 records support preservation with detailed assay limits. Empty IntAct joins for these sources do not establish absence.

## Location and contextual evidence

| Source | Actual scope | Interpretation boundary |
|---|---|---|
| [10196375](https://pubmed.ncbi.nlm.nih.gov/10196375/), [10496277](https://pubmed.ncbi.nlm.nih.gov/10496277/) | Complete authentic abstracts support surface-membrane association. | No full-paper or isoform-specific detail was inferred. |
| [20595382](https://pmc.ncbi.nlm.nih.gov/articles/PMC2937879/) | Full operative Methods/Results in C2C12 support surface localization and an early/late endocytic itinerary for full-length and mutant tagged constructs. | Host is mouse. Gift-construct provenance is not complete natural-human-product authentication; accelerated mutant trafficking is distinct from exclusivity. |
| [26707827](https://doi.org/10.1111/tra.12370) | Authentic abstract and independently indexed publisher Results support PM/Rab7-endosome observations in the specified transfected-cell contexts. | Complete Methods and figure pixels were unavailable. Rab7 late endosomes are mostly separate from LAMP1 structures; no wholesale lysosomal relabeling is made. |
| [17363620](https://pubmed.ncbi.nlm.nih.gov/17363620/), [17554076](https://pubmed.ncbi.nlm.nih.gov/17554076/) | Complete abstracts provide myogenic trafficking and human placental context. | Used as corroboration, with no unseen full-text claim. |
| [HPA subcellular page](https://www.proteinatlas.org/ENSG00000135636-DYSF/subcellular), [XML](https://www.proteinatlas.org/ENSG00000135636.xml) | HPA017071 target metadata were inspected, including Rh30 plasma-membrane staining. Plasma membrane is supported; centriolar satellite and midpiece are uncertain. | Overall approved reliability does not upgrade uncertain locations. No image pixels were independently scored; U2OS lacks staining in the saved record. |
| [Reactome R-HSA-5263633](https://reactome.org/content/detail/R-HSA-5263633) | The exact input [R-HSA-5263626](https://reactome.org/content/detail/R-HSA-5263626) resolves to human O75923 residues 1–2080 in cytoplasmic vesicle membrane. | This is a curated assembly/pathway state, not a new measured transport rate or purified interaction. The [11532985 abstract](https://pubmed.ncbi.nlm.nih.gov/11532985/) provides independent muscle association context. |
| [18276788](https://pmc.ncbi.nlm.nih.gov/articles/PMC2258254/) | Independently recovered complete operative Methods/Results distinguish human patient monocytes, TNF treatment, tissue observations and mouse J774 knockdown. | Untreated human phagocytosis was not significantly increased. No direct receptor/Rho mechanism is assigned from the proposed model. |
| [19056867](https://pmc.ncbi.nlm.nih.gov/articles/PMC2637050/) | Original Table 1 and Methods identify DYSF with one unique peptide/one spectrum in pooled human urine; linked NHLBI data identify NP_003485. | Gene-level detection does not discriminate all products or establish active extracellular function. The effective cache is abstract-only; the separately read original supplies the target table. |
| [23533145](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/) | Full main Methods/Results describe human EPS-urine exosome enrichment and proteomics. | The valid DYSF supplementary row was not recovered: small XML/HTML/error responses are not spreadsheets. The positive curated assertion is retained with independent urinary-exosome corroboration. |

## Propagation sources

The replay verifies the 194-entry [PTHR45911 tree](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR45911), [alignment](https://www.pantherdb.org/services/oai/pantherdb/familymsa?family=PTHR45911), exact 2,080-residue target sequence and [whole IBD source](https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf). The current [geneinfo lookup](https://pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList=O75923&organism=9606) and UniProt family pointer disagree; this is resolved by target identity, not by changing an imported PTN. Both imported nodes are on the target path. The normal PTHR12546 lookup output is retained as private acquisition provenance and is not substituted for the verified target tree.

PTN002473508 grounds calcium binding, with legitimate target experimental evidence among its descendants. PTN000413636 grounds the two unresolved synaptic assertions. Rat RGD:1305199 resolves to Mctp1: its [26195140 abstract](https://pubmed.ncbi.nlm.nih.gov/26195140/) supports neuronal vesicle/presynaptic observations, but the full original was not obtained. Fly FBgn0034389 resolves to Mctp; the [28485711 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC5449185/) was read for presynaptic ER localization, release/homeostatic phenotypes and neuronal rescue. These are donor experiments, not human DYSF experiments. MCTP/ferlin differences raise specialization uncertainty without proving loss or invalid ancestry. The mouse dysferlin donor [Q9ESD7](https://www.uniprot.org/uniprotkb/Q9ESD7/entry) is an ortholog with experimental location annotation, independently corroborated by target trafficking sources. Its [12736685 source](https://pubmed.ncbi.nlm.nih.gov/12736685/) was checked at complete abstract scope: mouse muscle shows dysferlin-associated membrane patches and vesicle accumulation; full operative original text was not independently read.

Electronic contexts were checked against the actual target FunFam/InterPro features, lineage and relevant ARBA condition groups: [ARBA00089298](https://rest.uniprot.org/arba/ARBA00089298.json), [ARBA00089297](https://rest.uniprot.org/arba/ARBA00089297.json), [ARBA00089681](https://rest.uniprot.org/arba/ARBA00089681.json), [ARBA00087396](https://rest.uniprot.org/arba/ARBA00087396.json) and [ARBA00033481](https://rest.uniprot.org/arba/ARBA00033481.json). Only matching branches are claimed. InterPro IPR006614/IPR012560/IPR012561 legitimately map a broad membrane term; refinement uses independently supported PM and internal-vesicle pools. GO_REF entries describe methodology and are individually assessed as LOW biological relevance, rather than treated as target experiments.

## Effective publication-cache inventory

The table below is generated from the actual selected cache headers. A true flag means text is present in that cache, not that every paragraph or supplement was examined. A false flag does not erase a separately recovered original described above. Existing repository publication bytes take precedence over fresh variants and are preserved exactly.

| PMID | Effective full-text flag | SHA-256 |
|---|---|---|
| [10196375](https://pubmed.ncbi.nlm.nih.gov/10196375/) | false | `84229925ae2356a720a7aa71c58f21cd4f173c5b7fc422a26f4debb8783f79f5` |
| [10496277](https://pubmed.ncbi.nlm.nih.gov/10496277/) | false | `6a9a9b97761b0ca488be0599947d510733ea168f3f7e172420b4e456ee41096a` |
| [11532985](https://pubmed.ncbi.nlm.nih.gov/11532985/) | false | `727f882b261652b26f47c82422c8a0846e0318709bc209de6342139ee3bd60a1` |
| [11959863](https://pubmed.ncbi.nlm.nih.gov/11959863/) | false | `f06f57d129aacbfda8edd2536e0b3f203573496d6681fc838c850febd57a6503` |
| [12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/) | false | `cb557e6a5792e0109ba453095626b5b8053e45e9073a672b399f276d640b65eb` |
| [16896923](https://pubmed.ncbi.nlm.nih.gov/16896923/) | false | `7fefe481c2e0155de7f35b8cf0687253fe653dfcb6a2710befe2da6335a07192` |
| [17185750](https://pubmed.ncbi.nlm.nih.gov/17185750/) | false | `9895f71f8271c0d17ec74ffebe367c222156bc3afa5937eac5803260e650f8b9` |
| [17363620](https://pubmed.ncbi.nlm.nih.gov/17363620/) | false | `6adc90f9aefd7ea8495fd01338050fc94fd42113acf8002f2fd2966b4f5ae2c3` |
| [17554076](https://pubmed.ncbi.nlm.nih.gov/17554076/) | false | `2233abb1b93c41b69344d32f318ce48620edef4f28992c6bae9c37374a1e84b5` |
| [18276788](https://pubmed.ncbi.nlm.nih.gov/18276788/) | false | `1ed4cdaf974df5fb9d6d64faa234591b2833d7451805b40625bddca27fa0a8ca` |
| [19056867](https://pubmed.ncbi.nlm.nih.gov/19056867/) | false | `90ceb930bcd3ba708af5c0630dfcc028133affae4b73bd0409c758d54b43f2c4` |
| [19221801](https://pubmed.ncbi.nlm.nih.gov/19221801/) | false | `4d7cad37f142b709e9c947dea0d55e632be5c6f633fb6a53e11ee8b5045d2ee4` |
| [20595382](https://pubmed.ncbi.nlm.nih.gov/20595382/) | true | `7149f7809db9d8f79aefac39968c96a2974c05221e39aa1f6e43c6b100cf486c` |
| [23414517](https://pubmed.ncbi.nlm.nih.gov/23414517/) | true | `0d08e0c6a78953ef41a9c8dc98c07dc7a7b14bc963fa55b306bed11b983d1cae` |
| [23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/) | true | `f347293c23617bd56d83e1ae9bc3ad8a65e540fdbf4aff13bd0e918ec598a17e` |
| [24239457](https://pubmed.ncbi.nlm.nih.gov/24239457/) | true | `24aa88323c0058c04dc24a1847846c52ea99a9fb9c1ae9a8d66551d3c31b7b96` |
| [24461013](https://pubmed.ncbi.nlm.nih.gov/24461013/) | true | `e05971faedb09f1718b311decf303f3bde21f99ca75d872638cfa8de797dfa6c` |
| [24687993](https://pubmed.ncbi.nlm.nih.gov/24687993/) | false | `90b864283b905164800a21c5b120c16926acd7e042bec9fa584f7f4561320df9` |
| [26195140](https://pubmed.ncbi.nlm.nih.gov/26195140/) | false | `2968817035e345b196f115dffd7d82131fb6a93ca6e4f5916173c9aa75f20de3` |
| [26707827](https://pubmed.ncbi.nlm.nih.gov/26707827/) | false | `c27ddff9927b85c2aeaafc01da0fd2ad0acc6af7af39aa3f16355b69bfe93572` |
| [28485711](https://pubmed.ncbi.nlm.nih.gov/28485711/) | true | `ace6fb4adfdd002a068aeee7e8fd1f1def73a3942cdf730f265b9855bd1ad8e9` |

The source audit includes exact input URLs, hashes, a locked dependency and executed saved outputs. Reference-only links from the review distinguish primary support, computed source joins and this locator guide. The normal research-provider failures are documented in the notes; they are not represented as completed research reports.


## Follow-up source access

[PMID:24967968](https://pubmed.ncbi.nlm.nih.gov/24967968/): normal full-text cache; Results on patient myoblasts and Methods on cell origin/laser injury were read. The human comparison uses one patient and an unmatched control; mechanistic lysosome experiments use mouse cells.

[PMID:27226605](https://pmc.ncbi.nlm.nih.gov/articles/PMC4938179/): normal cache is abstract-only; the original PMC HTML Results and Methods were read independently. The experiment measures lipid mixing, including an inner-leaflet control, rather than directly measuring wound closure. The soluble human construct is reported as residues 1–1965; no current natural-product identity is assigned.

The [repair audit](DYSF-bioinformatics/repair-audit/README.md) preserves the current ontology and comparator query results. No newly authored quotation or machine-cache flag change was introduced.
