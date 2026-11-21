# SUCLG2 (A0A9P6TY68), Actinomortierella ambigua: review notes

Started 2026-11-18. Follow-up to the evolutionary reviews of the succinyl-CoA synthetase (SCS) beta family PTHR11815 and alpha family PTHR11117.

## Folder name

The UniProt entry has a gene name, SUCLG2, supplied by the submitter [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-uniprot.txt "GN   Name=SUCLG2 {ECO:0000313|EMBL:KAG0251593.1};"]. The organism has no five-letter UniProt mnemonic of its own; the entry name is A0A9P6TY68_9FUNG, and other fungal entries with the pooled mnemonic 9FUNG carry the same gene symbol. The folder is therefore `genes/9FUNG/SUCLG2__A0A9P6TY68/`, following `genes/9EURY/mcrA__A0A284VQI9`. Fetched with `just fetch-gene 9FUNG A0A9P6TY68 --alias SUCLG2__A0A9P6TY68`.

## What the entry is

- Unreviewed TrEMBL entry, 409 residues, sequence version 1, existence level "inferred from homology".
- A gene model (ORF name DFQ27_008652, EMBL KAG0251593.1) from the draft genome of strain BC1065.
- Every functional statement in the record comes from HAMAP rule MF_03219 or from signature matches. Nothing in it is experimental.
- UniProt flags the sequence as preliminary [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-uniprot.txt "The sequence shown here is derived from an EMBL/GenBank/DDBJ"].

## Literature: there is none on this gene

The only paper attached to the entry is the genome paper, PMID:33364917 (Vandepol et al. 2020), cached with full text. I searched the cached text for "succin", "mitochond" and "tricarbox": no occurrence. The paper says nothing about this gene or about SCS.

What the paper does say that matters here:

- The strain is not called A. ambigua outright [PMID:33364917 "Actinomortierella. sp. aff ambigua BC1065 was isolated from decaying wood and fungivorous millipedes (Macias et al. 2019)."]. UniProt and NCBI file the genome under Actinomortierella ambigua.
- Gene models are automatic predictions [PMID:33364917 "Genomes were annotated with funannotate v1.7.0, which used a combination of evidence from ab initio gene prediction and protein alignments to produce a predicted gene set"].
- Coverage is low [PMID:33364917 "The average depth of genome coverage was 14.8X (8.5X-38.5X)."].

### Search log (2026-11-18)

Searches were run for the dossier of this review and are recorded here as reported; I did not rerun them.

PubMed:

1. `Actinomortierella ambigua`: 0 results.
2. `"Mortierella ambigua"`: 1 result (PMID:26539035, new species records from Korean soil; not about this gene).
3. `(Mortierella OR Mortierellomycota OR Mortierellaceae OR Actinomortierella OR Linnemannia OR Podila) AND (succinyl-CoA synthetase OR succinate-CoA ligase OR succinate thiokinase OR succinyl-CoA ligase)`: 0 results.
4. `DFQ27_008652 OR KAG0251593 OR A0A9P6TY68`: 2 results, both false hits on the digits (PMID:41444267, PMID:26464626).
5. `(SUCLG2 OR "GTP-specific succinyl-CoA synthetase") AND (fungi OR fungus OR fungal)`: 6 results, none on a fungal G-type gene (PMID:42815872, PMID:42810054, PMID:36906258, PMID:28709933, PMID:26241189, PMID:25708514). The last two use a construct named SUCLG2 in Candida glabrata metabolic engineering; abstracts only, no assay of nucleotide specificity.
6. `(succinyl-CoA synthetase OR succinate-CoA ligase) AND (Mucoromycota OR Mucoromycotina OR zygomycete OR "early-diverging fungi" OR Basidiobolus OR Rozella OR chytrid)`: 2 results (PMID:16515848, PMID:8257282), both on the hydrogenosomal enzyme of Neocallimastix.

Europe PMC full text:

7. `"A0A9P6TY68"`: 0. 8. `"DFQ27_008652"`: 0. 9. `"KAG0251593"`: 0.
10. `"Actinomortierella ambigua"`: 6 results (microbiome surveys and comparative-sequence papers; seen by title only for five; none on SCS).
11. `"Actinomortierella" AND ("succinyl-CoA synthetase" OR "succinate-CoA ligase" OR "succinyl-CoA ligase")`: 1 result (PMID:41683920, a bioinformatics paper on another protein family; title only, not read).
12. `("Mortierella" OR "Mortierellomycota") AND (SCS names) AND ("GTP-specific" OR "SUCLG2" OR "nucleotide specificity")`: 0.

Result: no paper describes this gene, this protein, or the succinyl-CoA synthetase of any Mortierellomycota species.

### Deep research

`just deep-research 9FUNG SUCLG2__A0A9P6TY68 --provider perplexity` was run once on 2026-11-18 and failed: "Provider 'perplexity' not available. Available: asta, openscientist, claude_code". No deep-research file exists for this gene and none was written by hand.

## Why UniProt calls the protein ADP-forming

Checked in the UniRule REST service on 2026-11-18.

- The entry is annotated by UniRule UR000405968 (HAMAP MF_03219, "Succ_CoA_beta_euk"). Its one condition set is: HAMAP hit MF_00558, taxon Eukaryota, not a fragment, and no hit to MF_03220 or MF_03221. It is the fallback rule for eukaryotic beta subunits that match neither dedicated profile, and it names the protein ADP-forming, EC 6.2.1.5.
- The GDP-forming rule UR000405912 (MF_03221) has two condition sets, one requiring taxon Metazoa and one requiring taxon Amoebozoa. The ATP-specific rule UR000406065 (MF_03220) has the same two taxon limits. The UniRule system therefore cannot name a fungal beta subunit GDP-forming. The fallback has no taxon limit below Eukaryota and catches only subunits that miss both dedicated profiles: Linnemannia elongata A0A197JV50 hits only MF_00558 and has the same double annotation as this entry (GO:0004775 from the UniRule, GO:0004776 from TreeGrafter), while Lobosporangium transversale A0A1Y2H5W1 hits MF_03221, is excluded from the fallback, is named "Succinate-CoA ligase subunit beta" with EC 6.2.1.- by RuleBase RU361258 and carries GO:0004776 with no GO:0004775 row (UniProt REST, 2026-11-18). So this entry falls to the fallback because it misses the MF_03221 profile, not because of the taxon limits of the dedicated rules.
- This entry lists only MF_00558 among its HAMAP hits [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-uniprot.txt "DR   HAMAP; MF_00558; Succ_CoA_beta; 1."], so it did not reach the MF_03221 profile either. I did not find out why (profile scores not inspected).
- So the ADP-forming name, EC number and GO:0004775 row are the default of a catch-all rule. They are not a judgement that this protein uses ADP.
- UniProt also warns that the rule did not fit fully [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-uniprot.txt "Lacks conserved residue(s) required for the propagation of"]. From the alignment, the likely residue is Ala344, where E. coli SucC has Val323 [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/RESULTS.md "The third residue of the substrate motif is Ala344, where E. coli SucC has Val323."]. UniProt does not say which residue failed.

## Where the GO rows come from

All nine rows are IEA. There is no IBA, no experimental row, no ND row and no NOT row.

- The protein is not a leaf of the PAINT tree of PTHR11815. PAINT terms reach it through TreeGrafter, which names PTN000929336 in WITH/FROM. That is the graft point, not the node where PAINT placed the annotation.
- In the PANTHER release 19 tree PTN000929336 is labelled Metazoa-Choanoflagellida (39 leaves) and lies below PTN008982083 (Opisthokonts, 40 leaves), which lies below PTN000929335 (Unikonts, 42 leaves). The first two are in `genes/yeast/LSC2/LSC2-bioinformatics/results.yaml` on the path to the Xanthomonas leaf; the full path from the root was walked for the dossier.
- A fungal protein grafted at a Metazoa-Choanoflagellida node is odd; the expected position is at or above the Opisthokont node. It makes no difference to the inherited terms, because every PAINT annotation the protein receives sits at PTN000929335 or higher.
- PAINT sources (`interpro/panther/PTHR11815/PTHR11815-paint.tsv`): GO:0004776 IBD at PTN000929335; GO:0006104, GO:0042709 and GO:0006099 IBD at the root PTN000212531; GO:0005739 IBD at the duplication node PTN000212530.
- PAINT also has a loss of GO:0004775 (IKR, NOT) at PTN000929335. TreeGrafter emitted no NOT row for this protein, and the UniRule row asserts GO:0004775 positively. GOA therefore gives this protein both the ADP-forming and the GDP-forming term.

## Phylogenetic position

- UniProt puts the entry in PANTHER subfamily SF10, the root subfamily, which is functionally mixed. Its name says GDP-forming, but SF10 also holds bacterial SucC, so the name is not evidence.
- `genes/yeast/LSC2/LSC2-bioinformatics/results.yaml` lists A0A9P6TY68 in the fungal census (group Mortierellomycota, context `DINV[Q]RFE`, closest reference SUCLG2). It was not one of the five fungal Gln20 genes placed in the trees.
- Those five genes group with human SUCLG2 [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "All five group with human SUCLG2 in 200 of 200 neighbor-joining bootstrap trees and in all three maximum-likelihood runs, inside a clade of 14 Gln20 sequences with animal SUCLG2 (ultrafast bootstrap 91 to 96)."].
- New here: A0A9P6TY68 is 80.3% and 78.5% identical to two of the five [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/RESULTS.md "A0A9P6TY68 is 80.3% identical to Linnemannia elongata A0A197JV50 and 78.5% identical to Lobosporangium transversale A0A1Y2H5W1"], and closer to human SUCLG2 than to its own second beta subunit [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/RESULTS.md "A0A9P6TY68 is more similar to human SUCLG2 (56.9%) than to the second beta subunit of its own genome, A0A9P6Q632 (52.5%)"].
- No tree contains A0A9P6TY68 itself. Its assignment to the SUCLG2-type lineage rests on TreeGrafter, on pairwise identity and on the five tested relatives.
- The organism has one alpha subunit and two beta subunits [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/RESULTS.md "Actinomortierella ambigua has three succinyl-CoA synthetase entries in UniProt: one alpha subunit (A0A9P6PU00) and two beta subunits (A0A9P6TY68 and A0A9P6Q632)."]. This fits the family review: Mortierellomycota keep a G-type gene next to an A-type gene.

## "Gln20" is Gln34 in this entry

Position 20 of the mature beta subunit is residue 34 of A0A9P6TY68 [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/RESULTS.md "Gln34 of A0A9P6TY68 aligns with Pro20 of E. coli SucC, Gln58 of pig SUCLG2 (P53590) and Gln57 of human SUCLG2 (Q96I99)."].

The residue is not an argument for nucleotide specificity:

- In the pig GTP-specific enzyme it reads the guanine base [PMID:16481318 "interactions of the guanine base with a glutamine residue (Gln-20beta) and with backbone atoms provide the specificity"].
- The Blastocystis enzyme has the same residue and is ATP-specific [PMID:18452512 "the appearance of Gln at position 20 in Blastocystis SCS coupled with its ATP specificity indicates that it is not this residue that dictates nucleotide specificity"].
- In E. coli SCS the Pro20-to-Gln mutant gains GTP affinity without losing ATP use [PMID:10353839 "had a Km(app) for GTP that was more than 5 times lower than that of wild-type SCS, whereas parameters for the other substrates remained unchanged"].

## Decisions on the rows

Basis for every row: no experiment on this protein or on any Mortierellomycota SCS. Rows are judged on descent and on what each electronic source rests on.

- GO:0004776 GDP-forming (TreeGrafter): ACCEPT, core. The term is inherited from the PAINT gain at PTN000929335. To dispute it I would have to dispute the node or show that this protein diverged; what I found supports membership of the clade. The activity is unmeasured and the review says so.
- GO:0004775 ADP-forming (UniRule): MODIFY to GO:0004776. This is a lateral correction, not a refinement. The row is the default of the fallback rule; by descent the protein belongs to the clade where PAINT records loss of ADP-forming activity. I did not use REMOVE: no assay excludes ADP use, the Blastocystis case shows that a Gln20 subunit can be ATP-specific, and the E. coli enzyme uses both nucleotides. I considered UNDECIDED. I chose MODIFY because the review accepts the gain at the node, and the loss is the same judgement at the same node; accepting one and withholding a view on the other would be inconsistent. A source defect (check request) is recorded on the rule.
- GO:0005524 ATP binding (InterPro2GO + UniRule): MODIFY to GO:0005525 GTP binding, the same lateral correction, following the human SUCLG2 and Dictyostelium scsB reviews. Weaker here than there, because no enzyme of this lineage of fungi has been assayed.
- GO:0003824 catalytic activity: TOO_GENERAL. The signature is shared with ATP-citrate synthase, so the row's own evidence does not support the specific ligase term (not MODIFY).
- GO:0000287 magnesium ion binding: KEEP_AS_NON_CORE. Both Mg ligand positions of the rule are conserved.
- GO:0006099, GO:0006104: ACCEPT. Root-node IBDs; the organism encodes the alpha subunit.
- GO:0042709 complex: ACCEPT. The row's evidence stops at the nucleotide-neutral complex and the gene has no GDP-forming complex row. I did not add GO:0045244 as NEW: no complex of this protein has been observed.
- GO:0005739 mitochondrion: ACCEPT under the root-organelle policy. Both sources stop at the organelle: the HAMAP rule's location line and the PAINT IBD at the duplication node, seeded from both daughter clades. The claim holds by descent. No sub-compartment row added: only one line (the function, a TCA cycle enzyme acting on matrix metabolites) points to the matrix. A presequence is not established; the 14-residue N-terminal extension has two Arg and no acidic residue [file:9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/RESULTS.md "The 14 residues contain two basic residues (Arg5, Arg13) and no acidic residue."], which is compatible with a presequence but was not tested with a predictor, and the start codon of an automatic gene model from a low-coverage draft is itself uncertain.

No NEW rows. No ND rows exist and none is proposed.

## Gene model

The N-terminus is unverified. Follow-up of 2026-11-18: the N-termini of the two closest ortholog models were compared (RESULTS.md, section 4). Residues 9 to 13 (ASQVR) are shared with both; the Linnemannia model A0A197JV50 (402 residues) starts one residue before that motif, so its seven-residue difference lies entirely at the N-terminus and only residues 1 to 8 (MPIQRGIV) are specific to this model; the Lobosporangium model A0A1Y2H5W1 (439 residues) has a 40-residue leader with seven basic and no acidic residues that this model lacks. A `gene_model_issues` entry (WRONG_START_SITE, SUSPECTED, ortholog comparison) is now recorded, with the suggested question and the localisation knowledge gap reworded. No genomic or transcript sequence was examined.

## Points for the family reviews

1. `interpro/panther/PTHR11815/PTHR11815-review.yaml`, GO:0004776 term assessment, says "The unassayed Gln20 members outside the node (Paramecium, early-diverging fungi) are open." For early-diverging fungi this needs rewording. They are not leaves of the tree, but TreeGrafter grafts A0A9P6TY68 below PTN000929335 and it already receives the GDP-forming IEA. By the family review's own criterion (membership of the clade below PTN000929335) the Mortierellomycota genes are members, although unassayed. Only this one protein was checked.
2. GOA gives this protein both GO:0004775 (UniRule fallback) and GO:0004776 (TreeGrafter), because the HAMAP G-type and A-type rules are limited to Metazoa and Amoebozoa. The same conflict is expected for other fungal SF10 Gln20 entries; they were not checked one by one. This belongs in a rule review of UR000405968.
3. The PAINT loss of GO:0004775 at PTN000929335 does not reach grafted sequences as a NOT row, so it cannot stop the UniRule row.
4. The TreeGrafter graft point of a fungal protein is a Metazoa-Choanoflagellida node. No effect on the inherited terms.
5. Nothing contradicts the PTHR11117 review or the numbers in the LSC2 RESULTS.md.

## Not done

- No tree with A0A9P6TY68 in it.
- No targeting-sequence prediction.
- The Europe PMC hits for "Actinomortierella ambigua" were seen by title only.
- HAMAP profile scores were not inspected.
