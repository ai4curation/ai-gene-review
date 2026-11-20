# GFER: selected evidence and construct scope

The [review](GFER-ai-review.yaml) and [source guide](GFER-source-guide.md) distinguish current judgments from the dated originals and prior review in the [compact archive](GFER-context-archive.json). Exact excerpt offsets and source grades are in [source evidence](GFER-source-evidence.yaml).

## Redox relay and constructs

[PMID:20593814](https://pubmed.ncbi.nlm.nih.gov/20593814/), selected Methods/Results: long/short human reagents contain C154A/C165A despite being called wild type. Oxygen, cytochrome-c and DTT assays have distinct scope; no natural-product-specific kinetic assignment follows automatically.

[PMID:22224850](https://pubmed.ncbi.nlm.nih.gov/22224850/), all four original main-text pages/captions: human 65–205 retains C71/C74; 81–205 lacks that distal shuttle. Principal reconstitution measures cytochrome-c reduction; oxygen/small-substrate discussion cites earlier work. Supplementary methods were not inspected.

[PMID:21383138](https://pubmed.ncbi.nlm.nih.gov/21383138/), selected genuine PMC Results/Methods: human recognition/redox experiments use C154A/C165A long and C74A/C85A short backgrounds. Yeast Erv1 import tests are separate. The normal cache omits these sections despite its full-text flag.

[PMID:23676665](https://pubmed.ncbi.nlm.nih.gov/23676665/), selected human-cell Results/Methods and Figure4 caption: association, substrate competition and coupled oxidation/import support the pathway. Main text reports mitochondrial ALR; supplemental localization images and construct sequences remain uninspected. No figure pixels or SI were read for these studies.

## Interaction evidence

| Raw context | Partner | Actual inspected support | Interpretation limit |
|---|---|---|---|
| 0 | BNIPL / Q7Z465 | PMID12681488 full abstract: Y2H, pull-down, co-IP | Full methods/product mapping unavailable; tentative bridge model |
| 1 | CHCHD4 / Q8N4Q1 | PMID23676665 selected original human-cell association | Partner folding function is not transferred to GFER |
| 2 | PLEKHF2 / Q9H8W4 | PMID25416956 original sheet2G row1933, GeneIDs2671/79666, two screens; three IntAct rows | Positive pair does not establish GFER trafficking |
| 3 | nsp10 / P0DTD1-PRO_0000449628 | PMID32353859 source-specific IntAct pull-down record | Association need not be binary; original target table uninspected |
| 4 | nsp10 / P0DTD1-PRO_0000449628 | PMID33060197 source-specific IntAct pull-down record | No infected-cell mechanism inferred |
| 5 | nsp10 / P0DTD1-PRO_0000449628 | PMID36217030 original Table1, sheetS1 row107: nsp10/Y2H/GeneID2671/GFER | Direct screen pair, distinct from the pull-down records |

The processed viral partner is nsp10, residues4254–4392, not every enzyme in the polyprotein. Its stimulation of other enzymes does not make nsp10 their catalyst. All six positive interactions are preserved; generic-label removals do not reject them.

CHCHD4's [reviewed official FUNCTION](https://rest.uniprot.org/uniprotkb/Q8N4Q1.json), accession-relative `/comments/0/texts/0/value`, states: “Functions as a chaperone”. Its complete sibling `/comments/0/texts/0/evidences` array is retained in source evidence, with the original response hash/pointer. This establishes partner class; selected PMID23676665 supplies the interaction evidence. The surrounding paragraph's other citations were not all independently read.

## Compartment and donor evidence

[MitoCoP, PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/), original TableS1 A row463/B row417: group5152 includes P55789 and P55789-2, with Class1 subtractive/importomics and Cluster1 spatial support. This is experimental inclusion, but neither unique-product nor IMS resolution.

[HPA](https://www.proteinatlas.org/ENSG00000127554-GFER/subcellular) metadata reports enhanced mitochondrial and cytosolic staining; mitochondrial examples include HPA041227/U2OS and HPA063553/A-549/MCF-7. Image pixels were not examined. [UniProt P55789](https://www.uniprot.org/uniprotkb/P55789/entry) assigns long-product IMS and short-product cytoplasmic/secreted pools; this does not manufacture isoform-specific GOA fields or a newly verified secretion assay.

Rat liver regeneration is within liver development: GO:0097421 is_a GO:0001889. [PMID:24880092](https://pubmed.ncbi.nlm.nih.gov/24880092/) abstract reports reduced proliferation plus increased apoptosis after rat knockdown; [PMID:8058770](https://pubmed.ncbi.nlm.nih.gov/8058770/) abstract reports positive recombinant rat125-residue ALR in a canine hepatotrophic assay. Full protocols remain unavailable. [PMID:7708779](https://pubmed.ncbi.nlm.nih.gov/7708779/) is the verified linked correction; its contents are unknown. The actual Tetrapoda IBD remains valid. The unresolved issue is regenerative participation versus general survival dependence, not adulthood, donor count or lack of direct human testing.

## Additional primary support

[PMID:19397338](https://pubmed.ncbi.nlm.nih.gov/19397338/): engineered human ALR oxidizes reduced MIA40 through the distal cysteine pair. Different substrates in the short/long cytochrome-c comparisons prevent a simple natural-product ranking.

[PMID:19409522](https://pubmed.ncbi.nlm.nih.gov/19409522/): human wild-type cDNA improves patient-cell respiratory activity. This corroborates the mitochondrial relay but is not a direct import-rate or enzyme assay. Yeast variant tests are separate.
