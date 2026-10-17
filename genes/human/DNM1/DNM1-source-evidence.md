# DNM1 source evidence

This guide identifies the original assays behind the annotation decisions. Article access and an assay's species, construct and measured endpoint are separate questions. Cached full-text flags are preserved as downloaded; a recovered supplement or author copy does not retroactively change those flags.

## Mechanochemical core

| Source | Original evidence used | Limits |
| --- | --- | --- |
| [19084269](https://pubmed.ncbi.nlm.nih.gov/19084269/) | Nanotube closure/fission, GTP versus GTPγS and nonleak measurements; Results on nucleotide-dependent closure | The human reagent chain follows the cited [17170701](https://pubmed.ncbi.nlm.nih.gov/17170701/) purification Methods; current natural splice product is unresolved |
| [20428113](https://pubmed.ncbi.nlm.nih.gov/20428113/) | Human engineered GG fragment, transition-state dimer and assembly-stimulated hydrolysis | Residues 6–320 plus 726–750 are not a natural isoform |
| [30069048](https://pubmed.ncbi.nlm.nih.gov/30069048/) | Human deletion-polymer structure and separately sequence-verified human dynamin-1–GFP cellular assays | ΔPRD residues 1–748 are shared by products 1 and 3; [30377313](https://pubmed.ncbi.nlm.nih.gov/30377313/) corrects exchanged figure labels, not a retraction |
| [16648839](https://pubmed.ncbi.nlm.nih.gov/16648839/) | Separately recovered supplementary purification Methods and legends | Rat-brain reagent and selected human baculovirus confirmation; normal cache is abstract-only; no claim that every measurement used human protein |
| [21927000](https://pubmed.ncbi.nlm.nih.gov/21927000/) | Separately recovered supplementary construct/purification Methods and solution captions | Human ΔPRD and engineered assembly mutants distinguished; normal cache is abstract-only |
| [21962517](https://pubmed.ncbi.nlm.nih.gov/21962517/), [20700106](https://pubmed.ncbi.nlm.nih.gov/20700106/) | Selected original crosslinking, assembly, lipid-binding and mutant-control experiments | Engineered dimer/tetramer probes do not define every native oligomeric state |
| [26302298](https://pubmed.ncbi.nlm.nih.gov/26302298/) | Author original, Extended Data Figure 2 and analytical-ultracentrifugation Methods | Main crystal is DNM3; actual human DNM1 control constructs are separately identified |

The core uses [GO:0061791](https://www.ebi.ac.uk/QuickGO/term/GO:0061791), rather than requiring the twist-specific wording of GO:1990606. Typed is_a/part_of paths were checked for GO:0099050, GO:0006898 and GO:0016185, and for GO:0005905 and GO:0098793. No selected term is an ancestor of another selected term in those groups. GDP/GTP binding and self-association remain components of this integrated activity.

## Partner and assay distinctions

| Sources | Load-bearing observation and limitation |
| --- | --- |
| [15703209](https://pubmed.ncbi.nlm.nih.gov/15703209/) | Purified SNX9–DNM1 binding and SH3/PRD dependency. Full SNX9 stimulates assembly; the isolated SH3 domain does not reproduce that full effect. Endogenous DNM2 co-IP is a separate experiment. |
| [15252009](https://pubmed.ncbi.nlm.nih.gov/15252009/), [16234328](https://pubmed.ncbi.nlm.nih.gov/16234328/) | Original author-posted Methods/Results identify human DNM1 constructs and SH3-dependent FBP17/NOSTRIN capture. Lysate capture is not a purified affinity assay; rat DNM2 NOSTRIN co-IP is not relabeled DNM1. |
| [18353773](https://pubmed.ncbi.nlm.nih.gov/18353773/) | [Institutional original](https://opus.bibliothek.uni-augsburg.de/opus4/files/112695/112695.pdf), Methods and Figure 7: human DNM1/SNX33 co-IP and loss with SH3 deletion. Endogenous DNM2 pull-down is distinct. |
| [10206341](https://pubmed.ncbi.nlm.nih.gov/10206341/), [17474147](https://pubmed.ncbi.nlm.nih.gov/17474147/) | Cached abstracts plus exact IntAct records preserve NCK1 domain/capture evidence and GRB2 SH3 156–215 binding to a DNM1 780–792 peptide. No full-paper access claim. |
| [9922133](https://pubmed.ncbi.nlm.nih.gov/9922133/), [21706016](https://pubmed.ncbi.nlm.nih.gov/21706016/) | Abstract access and curated GRB2 records; independent domain evidence supports the narrower gene-level binding classification. The 9922133 abstract refers generally to SH3 proteins, not specifically to GRB2 in every assay. |
| [24282027](https://pubmed.ncbi.nlm.nih.gov/24282027/) | Human LRRK2 1–500 Y2H and human full-length co-IP, with separate mouse constructs. The kinase-binding refinement does not claim DNM1 is a kinase or that the interaction activates LRRK2. |
| [12791276](https://pubmed.ncbi.nlm.nih.gov/12791276/), [16432212](https://pubmed.ncbi.nlm.nih.gov/16432212/) | Original Hsc70/auxilin and NOS3 association experiments. Hsc70 is purified bovine reagent; human HEK NOS3 co-IP and purified DNM1 nitrosylation are distinguished. No unsupported specific HSP90-binding function is inferred. |
| [17500595](https://pubmed.ncbi.nlm.nih.gov/17500595/), [29949766](https://pubmed.ncbi.nlm.nih.gov/29949766/), [37871017](https://pubmed.ncbi.nlm.nih.gov/37871017/) | Human HTT 1–450 and SPG11 C-terminal Y2H constructs, controls and retesting; SPG11 1943–2443 is not the whole protein. |
| [21900206](https://pubmed.ncbi.nlm.nih.gov/21900206/) | Original Y2H Methods accessed, but exact DNM1–DNM2 supplementary row not independently recovered. Other maps corroborate the pair without pretending to authenticate this particular source row. |
| [31980649](https://pubmed.ncbi.nlm.nih.gov/31980649/), [33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | Quantitative capture and BioPlex AP-MS, with original tagging/cell/filtering Methods. Protein groups and cellular capture do not establish direct contact. Narrow refinements use independent domain evidence for the same pair. |
| [35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/), [40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) | Exact primary OpenCell CSV and 2025 AP-MS graph, reproduced in the [analysis folder](DNM1-bioinformatics/README.md). Reciprocal bait direction and accession ambiguity are retained; graph edges are not inferred from an embedding or complex-assembly table. |

The current [Reactome reaction](https://reactome.org/content/detail/R-HSA-3928654) links input entity [177488](https://reactome.org/ContentService/data/query/177488) to human Q05193 residues 1–864 at the plasma membrane. This establishes source identity/location; being listed as an input is not itself evidence that DNM1 catalyzes every reaction step.

## Location, RNA capture and propagation

The [Baltz original-author thesis](https://refubium.fu-berlin.de/bitstream/handle/fub188/9034/Dissertation_Baltz.pdf?sequence=1), PDF page 147, lists DNM1 in class III with L1 and H1 unavailable, L2 −2.38, mean 2.38 and iBAQ 3.94. The original Methods use UV crosslinking and denaturing oligo-dT capture; class III means only one of three labeling experiments qualifies. DNM1 is absent from the individual PAR-CLIP validation panel. The extract records this evidence without upgrading it to a demonstrated native RNA-regulatory mechanism.

[19706678](https://pubmed.ncbi.nlm.nih.gov/19706678/) measures WT/K44A dynamin-1 effects on Caspr2 uptake and EEA1 endosomal morphology in rat hippocampal neurons. [10944110](https://pubmed.ncbi.nlm.nih.gov/10944110/) combines human-expressed dynamin with rat cardiac membranes. [17257598](https://pubmed.ncbi.nlm.nih.gov/17257598/) separates rat purified protein, human DNM1 lysate capture and Swiss3T3 endocytic imaging. [9238017](https://pubmed.ncbi.nlm.nih.gov/9238017/) provides rat nerve-terminal localization and synaptic co-IP. None of these is described as an isoform-matched human neuronal knockout.

All seven source IBA rows have a matching term/node IBD assertion and target descent in the saved PAINT tree. Target self-evidence and short donor lists are not treated as circularity or weak support. Some donor identifier aliases do not resolve in the current tree export; this is recorded as a reconstruction limit, not a target-specific loss of function. Exact current donor GOA records were checked for fly P27619, mouse P39053, rat P21575 and human DNM2. Fly microtubule binding is supported by the original cytoskeletal fractionation/identification in [11076973](https://pubmed.ncbi.nlm.nih.gov/11076973/); the synaptic-vesicle donor source [15014125](https://pubmed.ncbi.nlm.nih.gov/15014125/) remains abstract-only. No assertion that every donor's complete Methods were read is made.

The ARBA rules were inspected, but some FunFam/compound conditions remain unresolved. The review does not claim a fully reconstructed target rule firing where that was not established. Experimental biochemistry, official domains, reaction identities and conserved target placement supply independent biological support. [21307259](https://pubmed.ncbi.nlm.nih.gov/21307259/) supports mouse LRRK2-domain capture context; [19781630](https://pubmed.ncbi.nlm.nih.gov/19781630/) remains abstract-only for the exact localization assay.

The two unresolved assertions are source-specific exosome detection in [23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/) and literal clathrin-cage assembly from [35220002](https://pubmed.ncbi.nlm.nih.gov/35220002/). The latter directly measures mouse vesicle size and pit geometry, with human rescue of fluorescence uptake kinetics; it does not show human rescue of EM size or a direct clathrin-cage assembly assay. Neither uncertainty warrants rejection of the established membrane-scission core.

## Access inventory

The table below preserves each cited publication cache's actual metadata, separately from the source-specific access notes above. A full-text cache is not a claim that every section or figure was read. The review uses six short exact quotations once each; all other source supports are reference-only.

| PMID | Cache full_text_available | Extraction metadata | Canonical source |
| --- | --- | --- | --- |
| [10074457](https://pubmed.ncbi.nlm.nih.gov/10074457/) | false | not supplied | Genuine normal fetch |
| [10206341](https://pubmed.ncbi.nlm.nih.gov/10206341/) | false | not supplied | Protected main cache |
| [10521508](https://pubmed.ncbi.nlm.nih.gov/10521508/) | false | not supplied | Protected main cache |
| [10944110](https://pubmed.ncbi.nlm.nih.gov/10944110/) | true | html | Genuine normal fetch |
| [12791276](https://pubmed.ncbi.nlm.nih.gov/12791276/) | false | not supplied | Genuine normal fetch |
| [15252009](https://pubmed.ncbi.nlm.nih.gov/15252009/) | false | not supplied | Genuine normal fetch |
| [15703209](https://pubmed.ncbi.nlm.nih.gov/15703209/) | true | html | Genuine normal fetch |
| [16234328](https://pubmed.ncbi.nlm.nih.gov/16234328/) | false | not supplied | Protected main cache |
| [16432212](https://pubmed.ncbi.nlm.nih.gov/16432212/) | true | html | Protected main cache |
| [16648839](https://pubmed.ncbi.nlm.nih.gov/16648839/) | false | not supplied | Genuine normal fetch |
| [17474147](https://pubmed.ncbi.nlm.nih.gov/17474147/) | false | not supplied | Protected main cache |
| [17500595](https://pubmed.ncbi.nlm.nih.gov/17500595/) | true | xml | Protected main cache |
| [18353773](https://pubmed.ncbi.nlm.nih.gov/18353773/) | false | not supplied | Protected main cache |
| [19084269](https://pubmed.ncbi.nlm.nih.gov/19084269/) | true | xml | Genuine normal fetch |
| [19706678](https://pubmed.ncbi.nlm.nih.gov/19706678/) | false | not supplied | Protected main cache |
| [20428113](https://pubmed.ncbi.nlm.nih.gov/20428113/) | true | xml | Genuine normal fetch |
| [20700106](https://pubmed.ncbi.nlm.nih.gov/20700106/) | true | html | Genuine normal fetch |
| [21706016](https://pubmed.ncbi.nlm.nih.gov/21706016/) | false | not supplied | Protected main cache |
| [21900206](https://pubmed.ncbi.nlm.nih.gov/21900206/) | false | not supplied | Protected main cache |
| [21927000](https://pubmed.ncbi.nlm.nih.gov/21927000/) | false | not supplied | Genuine normal fetch |
| [21962517](https://pubmed.ncbi.nlm.nih.gov/21962517/) | true | xml | Genuine normal fetch |
| [22681889](https://pubmed.ncbi.nlm.nih.gov/22681889/) | false | not supplied | Protected main cache |
| [23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/) | true | xml | Protected main cache |
| [24282027](https://pubmed.ncbi.nlm.nih.gov/24282027/) | true | xml | Protected main cache |
| [26302298](https://pubmed.ncbi.nlm.nih.gov/26302298/) | false | not supplied | Genuine normal fetch |
| [29949766](https://pubmed.ncbi.nlm.nih.gov/29949766/) | true | xml | Protected main cache |
| [30069048](https://pubmed.ncbi.nlm.nih.gov/30069048/) | true | xml | Genuine normal fetch |
| [31980649](https://pubmed.ncbi.nlm.nih.gov/31980649/) | true | xml | Protected main cache |
| [33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | true | html | Protected main cache |
| [35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/) | true | html | Protected main cache |
| [37871017](https://pubmed.ncbi.nlm.nih.gov/37871017/) | true | xml | Protected main cache |
| [40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) | true | xml | Protected main cache |
| [8101525](https://pubmed.ncbi.nlm.nih.gov/8101525/) | false | not supplied | Genuine normal fetch |
| [8910402](https://pubmed.ncbi.nlm.nih.gov/8910402/) | false | not supplied | Genuine normal fetch |
| [9362482](https://pubmed.ncbi.nlm.nih.gov/9362482/) | false | not supplied | Genuine normal fetch |
| [9765310](https://pubmed.ncbi.nlm.nih.gov/9765310/) | false | not supplied | Genuine normal fetch |
| [9922133](https://pubmed.ncbi.nlm.nih.gov/9922133/) | false | not supplied | Protected main cache |
| [17170701](https://pubmed.ncbi.nlm.nih.gov/17170701/) | true | html | Genuine normal fetch |
| [17257598](https://pubmed.ncbi.nlm.nih.gov/17257598/) | false | not supplied | Genuine normal fetch |
| [19781630](https://pubmed.ncbi.nlm.nih.gov/19781630/) | false | not supplied | Genuine normal fetch |
| [21307259](https://pubmed.ncbi.nlm.nih.gov/21307259/) | false | not supplied | Protected main cache |
| [30377313](https://pubmed.ncbi.nlm.nih.gov/30377313/) | false | not supplied | Genuine normal fetch |
| [35220002](https://pubmed.ncbi.nlm.nih.gov/35220002/) | true | xml | Genuine normal fetch |
| [9238017](https://pubmed.ncbi.nlm.nih.gov/9238017/) | false | not supplied | Genuine normal fetch |
| [11076973](https://pubmed.ncbi.nlm.nih.gov/11076973/) | true | xml | Protected main cache |
| [15014125](https://pubmed.ncbi.nlm.nih.gov/15014125/) | false | not supplied | Genuine normal fetch |
