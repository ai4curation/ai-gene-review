# ALPHA-SCS1 (UniProtKB:P53399, SUCA1_TRIVA) notes

Trichomonas vaginalis hydrogenosomal succinyl-CoA synthetase alpha subunit 1.

Started 2026-11-18, as a follow-up to the evolutionary reviews of the succinyl-CoA synthetase (SCS) alpha family PTHR11117 and beta family PTHR11815. The partner beta subunit is reviewed in genes/TRIVA/Q03184.

The folder is named by the UniProt gene name ALPHA-SCS1 (`just fetch-gene TRIVA P53399 --alias ALPHA-SCS1`). The UniProt entry is for taxon 5722 (the species), strain ATCC 30001 / NIH-C1, not the genome strain G3 (taxon 412133).

## Terms used in these notes

- SCS: succinyl-CoA synthetase (succinate--CoA ligase, succinate thiokinase), an alpha/beta enzyme.
- ASCT: acetate:succinate CoA-transferase. It moves CoA from acetyl-CoA to succinate, giving acetate and succinyl-CoA.
- ASCT/SCS cycle: ASCT makes succinyl-CoA; SCS converts it back to succinate and makes ATP (or GTP) from ADP (or GDP) and phosphate.
- AP33: a 33 kDa protein described as a surface adhesin of T. vaginalis. The three ap33 genes are the three alpha-SCS genes.
- Paralogs: ALPHA-SCS2 (UniProtKB:P53400) and ALPHA-SCS3 (UniProtKB:P53401).

## Summary

- P53399 is the 309-residue precursor of one of three alpha subunits of the hydrogenosomal SCS. The alpha-SCS proteins were isolated from purified hydrogenosomes with an antibody, are soluble on carbonate extraction, and lack the first nine residues encoded by the genes (PMID:7808480, abstract only).
- No enzyme assay exists for the product of this gene or of either paralog. SCS activity is known for hydrogenosomal fractions, with ADP and with GDP (PMID:1898409, abstract only).
- T. vaginalis has no mitochondria, and its hydrogenosomes have no TCA cycle (PMID:22079833, full text). The enzyme works with ASCT in acetate formation and makes ATP by substrate-level phosphorylation.
- The only experimental GO row is hydrogenosome lumen (EXP, PMID:7808480). The mitochondrion and tricarboxylic acid cycle rows are electronic and are wrong for this protein.
- The same proteins were described as the adhesin AP33. Two independent localisation studies found alpha-SCS only in hydrogenosomes. The adhesin role is disputed and no annotation is proposed for it.

## UniProt record (entry SUCA1_TRIVA, sequence version 1, entry version 120 of 04-NOV-2026)

- Reviewed entry, 309 residues. Its only reference is PMID:7808480, for the genomic sequence, the protein sequence of residues 10-25 and the subcellular location.
- The only experimental statements are the location and the transit peptide: [file:TRIVA/ALPHA-SCS1/ALPHA-SCS1-uniprot.txt "SUBCELLULAR LOCATION: Hydrogenosome lumen {ECO:0000269|PubMed:7808480}."]. The feature table has TRANSIT 1..9 with note "Hydrogenosome" and the same evidence, and CHAIN 10..309.
- Everything else is text of HAMAP rule MF_03222: the catalytic activity [file:TRIVA/ALPHA-SCS1/ALPHA-SCS1-uniprot.txt "Reaction=succinate + ATP + CoA = succinyl-CoA + ADP + phosphate;"], the subunit statement [file:TRIVA/ALPHA-SCS1/ALPHA-SCS1-uniprot.txt "SUBUNIT: Heterodimer of an alpha and a beta subunit."], the active site (His262, tele-phosphohistidine intermediate) and the CoA-binding positions (Lys54, 107-109, and Tyr171 for the substrate shared with the beta subunit).
- The rule text is wrong for this protein in three places. The name ends in "mitochondrial". The FUNCTION comment says [file:TRIVA/ALPHA-SCS1/ALPHA-SCS1-uniprot.txt "Succinyl-CoA synthetase functions in the citric acid cycle"]. The PATHWAY comment places it in [file:TRIVA/ALPHA-SCS1/ALPHA-SCS1-uniprot.txt "Carbohydrate metabolism; tricarboxylic acid cycle; succinate"]. The record also has the keyword "Tricarboxylic acid cycle" and the UniPathway cross-reference UPA00223.
- The part of the rule text that describes the subunit is consistent with the family: [file:TRIVA/ALPHA-SCS1/ALPHA-SCS1-uniprot.txt "The alpha subunit of the enzyme binds the substrates coenzyme A and phosphate, while succinate binding and nucleotide specificity is provided by the beta subunit."]
- Sequence checked in the record: residues 1-9 are MLAGDFSRN and 10-25 are LHKPLLFIDKDTKVVI; residue 262 is His, 54 is Lys, 107-109 are Ile-Thr-Glu, 171 is Tyr.
- Family cross-references: PANTHER PTHR11117 and subfamily PTHR11117:SF2, whose label is "SUCCINATE--COA LIGASE [ADP_GDP-FORMING] SUBUNIT ALPHA, MITOCHONDRIAL"; NCBIfam TIGR01019 (sucCoAalpha); PROSITE PS01216 and PS00399; Pfam PF02629 (CoA_binding) and PF00549 (Ligase_CoA). The comment evidence cites HAMAP rule MF_03222, while the DR line lists HAMAP MF_01988.
- Locus cross-references: VEuPathDB TrichDB:TVAG_047890 and TrichDB:TVAGG3_0657380. See the next section: by sequence this is the locus of ALPHA-SCS2, not of this gene.

## Paralogs and related UniProt entries (UniProt REST, 2026-11-18)

Comparisons are my own position-by-position checks of the UniProt FASTA sequences (all 309 residues, no gaps). They are not stored in a committed analysis.

| Entry | Gene name or locus | Differences from P53399 | Notes |
|---|---|---|---|
| P53400 | ALPHA-SCS2 (reviewed) | 14 | identical to Q65ZG5 (ap33-2) and to A0A8U0WP19 (TVAG_047890, strain G3) |
| P53401 | ALPHA-SCS3 (reviewed) | 8 | identical to A2DUL5 (TVAG_165340, strain G3); 1 difference from O15569 (ap33-3; Ala263 against Ser) |
| O15568 | ap33-1 (unreviewed) | 1 (Ser248 in P53399, Phe in O15568) | identical to A0A8U0WPT0 |
| A0A8U0WPT0 | TVAG_318670 (strain G3) | 1 (Ser248 against Phe) | PANTHER leaf PTN000874239 |

- P53400 and P53401 differ from each other at 9 positions.
- Four of the differences between P53399 and each paralog are in the nine-residue presequence (positions 3, 4, 5 and 7): MLAGDFSRN in P53399, MLSSSFERN in P53400 and P53401. A fifth N-terminal difference, position 12 (Lys in P53399, Gln in the paralogs), is in the mature chain.
- All nine sequences compared have His at 262. All except P53399 have Phe at 248, so Ser248 is a strain difference or a sequencing difference.
- So ALPHA-SCS1, ALPHA-SCS2 and ALPHA-SCS3 correspond to ap33-1, ap33-2 and ap33-3, and to the strain G3 loci TVAG_318670, TVAG_047890 and TVAG_165340.
- UniProt names all nine entries "mitochondrial" from HAMAP rule MF_03222. The six unreviewed entries have the location "Hydrogenosome lumen" without the experimental evidence tag.
- Locus cross-references do not follow the sequences. The three reviewed entries, the three ap33 entries and A2DUL5 (TVAG_165340) all carry TrichDB:TVAG_047890. A0A8U0WPT0, the entry closest to P53399, carries TrichDB:TVAGG3_0662310. The reviewed entries are from another strain, so the cross-reference may be a similarity mapping to one locus and not an error. It matters when reading locus-level data: results reported for TVAG_318670 are the ones that correspond to this gene.
- UniProt assigns the protein sequence of residues 10-25 to ALPHA-SCS1 and ALPHA-SCS3 and of residues 10-14 to ALPHA-SCS2. The abstract of PMID:7808480 does not say which protein was sequenced.

## Literature search (2026-11-18)

`just deep-research TRIVA ALPHA-SCS1 --provider perplexity` failed: "Provider 'perplexity' not available. Available: asta, openscientist, claude_code". No deep-research file exists for this gene. The literature was searched by hand in PubMed and Europe PMC before this review was written; queries and number of hits:

- `Trichomonas vaginalis succinyl-CoA synthetase`: 20
- `(Trichomonas OR Tritrichomonas OR trichomonad) AND (succinate thiokinase OR "succinyl-CoA synthetase" OR "succinyl CoA synthetase" OR "succinate-CoA ligase")`: 21
- `Trichomonas vaginalis hydrogenosome (alpha-SCS OR "SCS alpha" OR "alpha-succinyl" OR SCSalpha)`: 4
- `Trichomonas vaginalis hydrogenosome proteome`: 19
- `Trichomonas vaginalis acetate:succinate CoA-transferase`: 5
- `AP33 Trichomonas vaginalis`: 18
- `"Trichomonas vaginalis" AND (TVAG_047890 OR TVAG_318670 OR TVAG_165340 OR "ALPHA-SCS1" OR "alpha-SCS1")`: 0 in PubMed, which indexes abstracts only
- Europe PMC full-text search: `TVAG_318670` 5 hits (PubMed ids 22419839, 32948226, 34944632, 32487244 and 23741475; only the last was read); `TVAG_047890` 5 hits; `TVAG_165340` 5 hits (among them 18676956, the import study below). Re-run on 2026-11-18 with the same counts. These are the positive control for the PubMed zero.
- `Trichomonas vaginalis (tricarboxylic acid cycle OR Krebs cycle OR citric acid cycle) hydrogenosome`: 2

Publications fetched for this review with `just fetch-pmid`: 23741475 and 17608941 (full text), and 9622355, 9846736 and 18676956 (abstract only). Already in the cache: 7808480, 1898409, 9501211, 1400232, 10669133, 31077495, 16515848, 18024431, 20085767, 3090435, 12603729 (abstract only) and 22079833 (full text).

Not found: an enzyme assay of the recombinant or purified product of this gene or of a defined alpha/beta pair; a paralog-specific knockout; a structure; interaction data for the T. vaginalis subunits.

## The genes and the protein (PMID:7808480, abstract only)

- [PMID:7808480 "The alpha-SCS of T. vaginalis is encoded by a multigene family composed of 3 similar genes that do not appear allelic."]
- [PMID:7808480 "Antibodies raised against recombinant T vaginalis alpha-SCS expressed in bacteria were used to isolate alpha-SCS proteins from purified hydrogenosomes."]
- [PMID:7808480 "Succinyl-coenzyme A synthetase is a hydrogenosomal enzyme which catalyzes the formation of ATP via substrate-level phosphorylation."]
- The abstract reports no enzyme assay. The identification as alpha-SCS rests on sequence similarity (more than 50% identity with the E. coli, Thermus and rat alpha subunits) and on isolation from hydrogenosomes.
- The antibody isolates "alpha-SCS proteins" as a group, so the location evidence is for the three paralogs together. UniProt attributes it to all three entries.

## Location

- Sub-compartment: [PMID:7808480 "These proteins partition into the soluble fraction of hydrogenosomes treated with sodium carbonate at high pH, consistent with a matrix localization in the organelle."]
- Processing: [PMID:7808480 "Amino-terminal sequencing of purified alpha-SCS proteins shows that mature proteins lack a short, leader sequence of 9 amino acids."]
- The organism has no mitochondria: [PMID:7808480 "is characterized by the absence of mitochondria and the presence of double membrane bound organelles called hydrogenosomes"]
- Immunolocalisation (PMID:10669133, abstract only): [PMID:10669133 "All antibodies labeled the hydrogenosome matrix as determined both by immunofluorescence and by immunogold staining."] and [PMID:10669133 "There was no labeling on the cell surface or in any other cell compartment."] One of the three monoclonal antibodies is against the alpha subunit; the abstract does not say that it separates the three alpha proteins.
- Trafficking (PMID:31077495, abstract only): [PMID:31077495 "α- and β-SCS are biotinylated in the cytosol and imported exclusively into the hydrogenosomes"]. The abstract does not say which alpha gene was tagged.
- Proteomics (PMID:23741475, full text): the strain G3 locus that corresponds to this gene, TVAG_318670, was detected in purified hydrogenosomes: [PMID:23741475 "The only exception observed was the α-SCS subunit (TVAG 318670), which was significantly upregulated at the proteomic level but downregulated with the EST approach under -Fe conditions."]
- Targeting signal (PMID:18676956, abstract only): [PMID:18676956 "SCSalpha lacking its N-terminal extension was efficiently imported into hydrogenosomes, indicating that this extension is not required for import of this major hydrogenosomal protein."] The presequence is removed but is not the only targeting signal. The abstract does not say which alpha gene was used. The Europe PMC full-text search finds this paper for TVAG_165340 (the ALPHA-SCS3 locus) and not for the two other loci, so the protein tested was probably not the product of this gene; that is a search hit, not a reading of the paper.
- The partner beta subunit is soluble in the same assay: [PMID:1400232 "The trichomonad protein partitions into the soluble fraction of hydrogenosomes treated with sodium carbonate at high pH, consistent with a matrix localization within the organelle."]

GO terms (QuickGO ontology service, 2026-11-18): GO:0034492 hydrogenosome lumen is part of GO:0042566 hydrogenosome. GO:0005739 mitochondrion is not an ancestor of either. P53399, P53400 and P53401 are the only three gene products with an experimental annotation to GO:0034492.

Sub-compartment decision: the lumen term is already on the entry with experimental evidence. Three lines agree (soluble on carbonate extraction; a cleaved N-terminal presequence; immunogold label over the matrix). No new location row is needed. The hydrogenosome is not one of the five root organelles of projects/ORGANELLES.md.

## Activity and nucleotide

- Organelle enzyme (PMID:1898409, abstract only): [PMID:1898409 "Succinate thiokinase activities, both ADP- and GDP-dependent, were shown to be hydrogenosomal in Tritrichomonas foetus and Trichomonas vaginalis."] and [PMID:1898409 "the 'small' enzyme was found in T. foetus whereas T. vaginalis contained a 'large' enzyme"].
- The abstract contrasts dimeric enzymes specific for one nucleotide with a [PMID:1898409 "single 'large' (tetrameric) enzyme which utilizes both nucleotides"] of Gram-negative bacteria. It does not say outright that the T. vaginalis large enzyme is one enzyme that uses both nucleotides; that reading is an inference.
- The 'large' enzyme does not agree with the "Heterodimer" statement of the UniProt rule as a description of the native enzyme.
- Organelle physiology (PMID:3090435, abstract only): [PMID:3090435 "fermented pyruvate to acetate, malate, H2, and CO2 in an anaerobic process dependent on ADP, Pi, Mg2+, and succinate"]. The physiological process is shown with ADP.
- The alpha subunit does not choose the nucleotide; in the family that is a property of the beta subunit. The three T. vaginalis beta subunits have Gly at position 20 of the mature chain, which is neither the Gln of GTP-specific enzymes nor the Pro of the plant and E. coli enzymes (genes/yeast/LSC2/LSC2-bioinformatics/RESULTS.md).
- Which alpha pairs with which beta is unknown: three alpha and three beta genes, no interaction data.

## Pathway: no TCA cycle; the ASCT/SCS cycle

- PMID:22079833 (hydrogenosome proteome, full text in the cache): [PMID:22079833 "Hydrogenosomes can generate ATP by substrate level phosphorylation but not via oxidative phosphorylation as mitochondria do."] and [PMID:22079833 "Hydrogenosomes also lack a trichloroacetic acid (TCA) cycle, cytochromes and members of complex I-IV"]. The authors wrote "trichloroacetic" where tricarboxylic is meant. The sentence is in the introduction and is about the organelle.
- PMID:23741475 (full text): [PMID:23741475 "The resulting succinyl-CoA serves as a substrate for ATP synthesis by succinate thiokinase"].
- The cycle (PMID:9501211, abstract only; the trichomonad statement is background): [PMID:9501211 "Hydrogenosome-containing anaerobic protists, such as the trichomonads, produce large amounts of acetate by an acetate:succinate CoA transferase (ASCT)/succinyl CoA synthetase cycle."]
- The partner enzyme (PMID:18024431, abstract only): [PMID:18024431 "It was shown that the CoA transferase activity is succinate-dependent."]
- Review (PMID:20085767, abstract only): [PMID:20085767 "reaction yields succinyl-CoA for ATP formation via succinyl-CoA synthetase"]
- Ancestry of the enzyme (PMID:16515848, abstract only): [PMID:16515848 "Our analyses of the Trichomonas vaginalis SCS sequences also confirmed the mitochondrial affiliation of these hydrogenosomal enzymes, in contrast to previous results."] The enzyme is of mitochondrial descent; descent is not location.

Process term decision.

- GO:0006099 tricarboxylic acid cycle is removed: there is no cycle in the organelle, and all sources of the row are electronic.
- GO:0006104 succinyl-CoA metabolic process is proposed as a new row. Participation test: the alpha subunit carries the phosphohistidine intermediate and binds CoA, so it does part of the chemistry of the conversion of succinyl-CoA. Comparator check, run in QuickGO by term id on 2026-11-18 for SCS alpha subunits: yeast LSC1 (P53598) carries GO:0006104 by IDA, rat Suclg1 (P13086) by IDA, mouse Suclg1 (Q9WUM5) by ISO; the T. vaginalis beta subunit Q03184 carries it by TreeGrafter IEA. The same query returned 27 rows for GO:0006099 on the same set of proteins, so the query can return positives. The term is not an ancestor or descendant of any term kept on this gene.
- GO:1901289 succinyl-CoA catabolic process (a child of GO:0006104) is carried by human SUCLG1 and yeast LSC1 from ComplexPortal. It is not proposed: no flux through the T. vaginalis enzyme has been measured, so the direction-neutral parent is as far as the evidence goes.
- No ATP-synthesis or acetate term is proposed. No SCS alpha subunit in the comparator set carries GO:0006754 ATP biosynthetic process or GO:0019413 acetate biosynthetic process (0 hits each, same query that returned positives for the other terms). The acetate is released by ASCT, not by SCS.
- GO has no term for the ASCT/SCS cycle and none for substrate-level phosphorylation. The definition of GO:0019654 pyruvate fermentation to acetate describes breakdown of acetate under a "fermentation to acetate" label, so it is not used.

## The AP33 adhesin claim

- The claim (PMID:9622355, abstract only): [PMID:9622355 "A database search revealed that AP33 had significant identity to the succinyl-CoA synthetase alpha-subunit of several different organisms and virtually 100% identity to the reported T. vaginalis subunit."] and [PMID:9622355 "Unlike commercially purchased enzyme, the recombinant proteins retained adhesive properties equal to the natural T. vaginalis AP33."]
- Binding domains (PMID:9846736, abstract only): [PMID:9846736 "two domains interactive with host cell surfaces were identified at distinct parts of AP33: one in the N-terminal half of the protein, and the other within 24 residues in the C-terminal third"]
- Antisense knock-down (PMID:17608941, full text): the antisense RNA [PMID:17608941 "decreases the amounts of endogenous transcripts of all three ap33 genes"]; [PMID:17608941 "the level of adherence by AS trichomonads was measured and found to be ~30% lower than wt and S-transfected parasites"]; [PMID:17608941 "decreased amounts of AP33 (α-SCS) did not affect overall trichomonal growth and multiplication"]. The sense primer in the Methods (5'-CATACGCATATGCTCGCAGGCGACTTCTC-3') encodes Met-Leu-Ala-Gly-Asp-Phe, the N-terminus of P53399 and ap33-1 and not of the two paralogs. That is my reading of the primer; the paper does not name the gene copy. This is the only genetic perturbation of the alpha-SCS genes found. It is not paralog-specific, it is partial, and the paper reports no measurement of SCS activity or of hydrogenosomal metabolism.
- Surface placement under high iron (PMID:12603729, abstract only): [PMID:12603729 "high-iron-grown organisms coexpressed adhesins on the surface and intracellularly in contrast with low-iron parasites"]
- Against: [PMID:10669133 "These results support the idea that these proteins are restricted to a hydrogenosomal function and do not play a role as adhesins at the plasma membrane surface."] and [PMID:31077495 "these results demonstrate that the α- and β-SCS subunits are targeted only to the hydrogenosomes, which argues against their putative moonlighting function"].
- Status: disputed. The adhesin reports come from one laboratory; two other laboratories found the protein only in hydrogenosomes. GOA has no adhesion or cell-surface term on any of the nine T. vaginalis alpha entries (QuickGO, 2026-11-18: their only biological process rows are GO:0006099). None is proposed.

## Iron regulation (PMID:23741475, full text)

- In the hydrogenosome proteome of cells grown with and without iron, Table 1 lists TVAG_047890 (the ALPHA-SCS2 locus) as lower and TVAG_318670 (the ALPHA-SCS1 locus) as higher under iron deficiency.
- [PMID:23741475 "acetate:succinate-CoA transferase (ASCT) and heterodimeric succinyl-CoA synthase (SCS), of which only the α subunit showed significant downregulation under -Fe conditions"]
- The paralogs respond differently to iron. Why three near-identical genes are kept is unknown.

## Position in the PANTHER tree (PANTHER release 19 tree service, read 2026-11-18)

- P53399 is not a leaf of the PANTHER tree of PTHR11117 and has no IBA row. Its four PANTHER-derived rows name PANTHER:PTN008961326, the duplication node that holds the three strain G3 leaves: PTN000874237 (A2DUL5, TVAG_165340), PTN000874238 (A0A8U0WP19, TVAG_047890) and PTN000874239 (A0A8U0WPT0, TVAG_318670). [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "| PTHR11117 (alpha) | PTN008961326 | duplication | 3 | Trichomonas vaginalis alpha subunits |"]
- Path from the root to the clade: PTN008961318 > PTN000122012 (LUCA) > PTN008512606 (Eubacteria) > PTN004231559 (horizontal transfer) > PTN000122014 (Eukaryota) > PTN007487682 (Bikonts, 84 leaves) > PTN002476581 (Excavates, 5 leaves) > PTN008961326. The sister of the Trichomonas clade inside PTN002476581 is PTN000874234 (Leishmania major Q4Q9M4 and Trypanosoma brucei Q582T6).
- Origin of each term in the PAINT file: GO:0004775, GO:0004776, GO:0006099 and GO:0009361 are IBD at PTN000122012; GO:0005739 is IBD at PTN000122014, e.g. [file:interpro/panther/PTHR11117/PTHR11117-paint.tsv "PTHR11117	PTN000122014	GO:0005739	C	IBD	false"].
- Node judgement. The root placement of the ADP-forming activity and of the complex is sound for this clade: the alpha subunit is conserved, with the phosphohistidine residue, and the organelle enzyme is ADP-dependent. The root placement of the GDP-forming activity is plausible for this clade because the organelle also has GDP-dependent activity. The mitochondrion placement at PTN000122014 and the TCA placement at the root do not hold for the Trichomonas clade; the family review proposes pruning at PTN008961326.
- The GO:0006099 row on P53399 has two sources besides the PANTHER node (UniRule UR000406071 and UniPathway UPA00223). A loss annotation in the PAINT tree would not remove them.

## Points for the family reviews

- No contradiction with interpro/panther/PTHR11117/PTHR11117-review.yaml, interpro/panther/PTHR11815/PTHR11815-review.yaml or genes/yeast/LSC2/LSC2-bioinformatics/RESULTS.md was found.
- The alpha family review says the abstracts it read do not state in so many words that T. vaginalis has no TCA cycle. The full text of PMID:22079833 states it for hydrogenosomes (with "trichloroacetic" printed for tricarboxylic).
- The family review gives the tree leaves and their identities to the reviewed entries. It does not record the correspondence to loci and to the ap33 names: P53399 = ap33-1 = TVAG_318670 (one residue different), P53400 = ap33-2 = TVAG_047890, P53401 = ap33-3 = TVAG_165340. UniProt cross-references all three reviewed entries to TVAG_047890.
- The path from PTN000122014 to the Trichomonas clade passes through PTN007487682 (Bikonts) and PTN002476581 (Excavates), which the family review does not name. The sister clade holds T. brucei Q582T6, one of the seeds of the mitochondrion IBD.
- The AP33 adhesin literature concerns the alpha subunits of this clade and is not mentioned in the alpha family review.
- The GDP-forming term stays plausible for this clade, as the family review says. Added caveats: the abstract of PMID:1898409 reports one 'large' enzyme in T. vaginalis and does not say that it uses both nucleotides, and the Gly20 residue of the beta subunits does not predict a nucleotide.
