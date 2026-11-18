# Q03184 (Trichomonas vaginalis hydrogenosomal succinyl-CoA synthetase beta subunit, SUCB_TRIVA) notes

Started 2026-11-18, as a follow-up to the evolutionary reviews of the succinyl-CoA synthetase (SCS) beta family PTHR11815 and alpha family PTHR11117.

The UniProt entry has no gene name, so the folder is named by the accession. The locus tag of the same gene in the genome strain G3 is TVAG_259190.

## Terms used in these notes

- SCS: succinyl-CoA synthetase (succinate--CoA ligase, succinate thiokinase), an alpha/beta enzyme.
- ASCT: acetate:succinate CoA-transferase. It moves CoA from acetyl-CoA to succinate, giving acetate and succinyl-CoA.
- ASCT/SCS cycle: ASCT makes succinyl-CoA; SCS converts it back to succinate and makes ATP (or GTP) from ADP (or GDP) and phosphate.
- Position 20: residue 20 of the mature beta subunit (Pro in E. coli SucC, Gln in pig GTP-specific SCS). The mature chain of Q03184 starts at residue 10, so mature position n is precursor position n + 9. Mature position 20 is Gly29 of the precursor.
- A daughter and G daughter: the two clades below the PANTHER duplication node PTN000212530 (human SUCLA2 and human SUCLG2).
- AP51: a 51 kDa protein described as a surface adhesin of T. vaginalis. The ap51 genes are the beta-SCS genes.

## Summary

- Q03184 is the 407-residue precursor of a beta subunit of the hydrogenosomal SCS. The protein was purified from hydrogenosomes, its N-terminus was sequenced, and it is soluble on carbonate extraction (PMID:1400232).
- T. vaginalis has no mitochondria. Its hydrogenosomes have no TCA cycle (PMID:22079833, full text).
- The enzyme works with ASCT: it turns the succinyl-CoA made by ASCT back into succinate and makes ATP by substrate-level phosphorylation.
- Hydrogenosomes have both ADP-dependent and GDP-dependent succinate thiokinase activity (PMID:1898409). No assay is assigned to this gene product or to either of the two other beta genes.
- No recombinant enzyme, kinetic constants, knockout, knockdown or structure were found for any T. vaginalis beta-SCS gene.
- The same protein was described as the adhesin AP51-1. Two later studies found the beta subunit only in hydrogenosomes. The adhesin role is disputed and no annotation is proposed for it.

## UniProt record (entry SUCB_TRIVA, sequence version 1, entry version 129)

- Reviewed entry, 407 residues, protein existence level 1 (direct protein sequencing). Its only reference is PMID:1400232, for the gene sequence, the protein sequence of residues 10-21 and the subcellular location.
- The only experimental statements are the location and the transit peptide: [file:TRIVA/Q03184/Q03184-uniprot.txt "SUBCELLULAR LOCATION: Hydrogenosome {ECO:0000269|PubMed:1400232}."]. The feature table has TRANSIT 1..9 with note "Hydrogenosome" and the same evidence, and CHAIN 10..407.
- Everything else is text of HAMAP rule MF_03219: the catalytic activity [file:TRIVA/Q03184/Q03184-uniprot.txt "Reaction=succinate + ATP + CoA = succinyl-CoA + ADP + phosphate;"], the cofactor [file:TRIVA/Q03184/Q03184-uniprot.txt "Note=Binds 1 Mg(2+) ion per subunit. {ECO:0000255|HAMAP-Rule:MF_03219};"], the subunit statement [file:TRIVA/Q03184/Q03184-uniprot.txt "SUBUNIT: Heterodimer of an alpha and a beta subunit."] and the binding-site features.
- The rule text is wrong for this protein in two places. The FUNCTION comment says [file:TRIVA/Q03184/Q03184-uniprot.txt "Succinyl-CoA synthetase functions in the citric acid cycle"], and the PATHWAY comment places it in [file:TRIVA/Q03184/Q03184-uniprot.txt "Carbohydrate metabolism; tricarboxylic acid cycle; succinate"]. The record also has the keyword "Tricarboxylic acid cycle" and the UniPathway cross-reference UPA00223. The organism has no such cycle (below).
- N-terminus, checked against the sequence in the record: MLSSSFARN | FNILEWQSKEIC... The mature protein starts at Phe10. Residue 29 is Gly (context NVAA[G]INL).
- Family cross-references: PANTHER PTHR11815:SF10, whose label is "SUCCINATE--COA LIGASE [GDP-FORMING] SUBUNIT BETA, MITOCHONDRIAL". The label is wrong for this protein on location, and unsupported on nucleotide. The family review already records that SF10 is the root subfamily and does not delimit the GDP-forming clade. Other signatures: HAMAP MF_00558, NCBIfam TIGR01016 (sucCoAbeta), Pfam PF08442 (ATP-grasp_2) and PF00549 (Ligase_CoA).

## Related UniProt entries (UniProt REST, 2026-11-18; comparisons are my own position-by-position checks of the FASTA sequences, not stored)

- A2EBX0 (TVAG_259190, strain G3, unreviewed, 407 residues) is the same gene in the genome strain. It differs from Q03184 at one residue: Asn256 in Q03184, Ser in A2EBX0. UniProt names A2EBX0 "Succinate--CoA ligase [ADP-forming] subunit beta, mitochondrial" and gives it SUBCELLULAR LOCATION Mitochondrion, both from HAMAP rule MF_03219.
- A2FVK7 (TVAG_144730) and A2D987 (TVAG_183500), 409 residues each, are the two other beta genes of strain G3. UniProt names both "mitochondrial" as well.
- Q6LC42 (gene name ap51-1, EMBL U87093, 403-residue fragment) is identical to residues 5-407 of Q03184. So the "AP51-1" of the adhesin literature is this gene product.

## Literature search (2026-11-18)

`just deep-research TRIVA Q03184 --provider perplexity` failed: "Provider 'perplexity' not available. Available: asta, openscientist, claude_code". No deep-research file exists for this gene. The literature was searched by hand in PubMed before this review was written; queries and number of hits:

- `Trichomonas vaginalis succinyl-CoA synthetase`: 20
- `(Trichomonas OR Tritrichomonas OR trichomonad) AND (succinate thiokinase OR "succinyl-CoA synthetase" OR "succinate-CoA ligase" OR "succinyl coenzyme A synthetase")`: 22
- `Trichomonas vaginalis acetate:succinate CoA-transferase`: 5
- `Trichomonas vaginalis AP51 adhesin succinyl`: 3
- `Trichomonas vaginalis AP51`: 12
- `Trichomonas vaginalis hydrogenosome proteome`: 19
- `Trichomonas vaginalis hydrogenosome (tricarboxylic acid cycle OR Krebs cycle OR citric acid cycle)`: 2
- `Trichomonas vaginalis succinate thiokinase`: 15
- `TVAG_259190 OR "SUCB_TRIVA"`: 0

Twelve publications were added to the cache with `just fetch-pmid`: 22079833 (full text), and 10669133, 31077495, 8410536, 9466942, 3090435, 18024431, 16515848, 20085767, 1602965, 12603729 and 19105955 (abstract only). PMID:1400232, PMID:1898409, PMID:9501211 and PMID:7808480 were already cached, all abstract only. The full text of PMID:1400232 exists only as scanned page images and was not read.

Not found: an enzyme assay of the recombinant or purified product of this gene; assignment of ADP or GDP use to one of the three beta genes; a knockout or knockdown of any beta-SCS gene; a structure.

## The gene and the protein (PMID:1400232, abstract only)

- [PMID:1400232 "We cloned a gene encoding the beta subunit of the hydrogenosomal protein succinyl-coenzyme A synthetase (beta-SCS) and isolated the protein from Trichomonas vaginalis."]
- [PMID:1400232 "has 43% amino acid identity (65% similarity) with beta-SCS from Escherichia coli"]
- [PMID:1400232 "The protein is encoded by a multigene family composed of at least three members."]
- The abstract describes no enzyme assay of the cloned gene product. The identification as beta-SCS rests on sequence similarity and on isolation of the protein from hydrogenosomes.

## Location

- Organelle and sub-compartment, on this gene product: [PMID:1400232 "The trichomonad protein partitions into the soluble fraction of hydrogenosomes treated with sodium carbonate at high pH, consistent with a matrix localization within the organelle."]
- Processing: [PMID:1400232 "Amino-terminal sequencing of beta-SCS purified from T. vaginalis hydrogenosomes shows that the mature protein lacks the first nine amino acids encoded in the gene."]
- The organism has no mitochondria: [PMID:1400232 "an unusual organelle found exclusively in certain anaerobic eukaryotes that lack mitochondria"]; [PMID:7808480 "is characterized by the absence of mitochondria and the presence of double membrane bound organelles called hydrogenosomes"]; [PMID:8410536 "Trichomonas vaginalis is a primitive protist that lacks mitochondria and peroxisomes."]
- Biogenesis: [PMID:8410536 "appear to be synthesized as larger precursors that contain an 8- or 9-amino acid amino-terminal extension, respectively"]. The same abstract reports that the leader is required for association with the organelle in an in vitro import assay, without saying which protein was used.
- Immunolocalisation (PMID:10669133, abstract only): [PMID:10669133 "All antibodies labeled the hydrogenosome matrix as determined both by immunofluorescence and by immunogold staining."] and [PMID:10669133 "There was no labeling on the cell surface or in any other cell compartment."] The antibody is against "the beta subunit"; the abstract does not say that it separates the three beta proteins.
- Trafficking (PMID:31077495, abstract only): [PMID:31077495 "α- and β-SCS are biotinylated in the cytosol and imported exclusively into the hydrogenosomes"]. The abstract does not say which beta gene was tagged.
- The alpha partners behave the same way: [PMID:7808480 "These proteins partition into the soluble fraction of hydrogenosomes treated with sodium carbonate at high pH, consistent with a matrix localization in the organelle."] The three alpha entries P53399, P53400 and P53401 carry GO:0034492 hydrogenosome lumen with an experimental code from that paper (QuickGO, 2026-11-18; they are the only three experimental annotations to the term).

GO terms (QuickGO ontology service, 2026-11-18): GO:0042566 hydrogenosome is not a descendant of GO:0005739 mitochondrion; its ancestors run through intracellular membrane-bounded organelle to cytoplasm. It has two part_of children, GO:0034492 hydrogenosome lumen ("The volume enclosed by the hydrogenosome membrane.") and GO:0046859 hydrogenosomal membrane.

Sub-compartment decision: four lines agree that the protein is in the lumen (soluble on carbonate extraction; a cleaved N-terminal presequence; immunogold label over the matrix; import from the cytosol only into hydrogenosomes). A new row for GO:0034492 is proposed beside the two hydrogenosome rows, as a curator inference. The hydrogenosome is not one of the five root organelles of projects/ORGANELLES.md; the policy is applied by analogy.

## Activity and nucleotide

- Organelle enzyme (PMID:1898409, abstract only): [PMID:1898409 "Succinate thiokinase activities, both ADP- and GDP-dependent, were shown to be hydrogenosomal in Tritrichomonas foetus and Trichomonas vaginalis."] and [PMID:1898409 "the 'small' enzyme was found in T. foetus whereas T. vaginalis contained a 'large' enzyme"]. The abstract contrasts dimeric enzymes specific for one nucleotide with a "single 'large' (tetrameric) enzyme which utilizes both nucleotides" of Gram-negative bacteria. It does not say outright that the T. vaginalis large enzyme is one enzyme using both nucleotides; that reading is an inference.
- Organelle physiology (PMID:3090435, abstract only): [PMID:3090435 "fermented pyruvate to acetate, malate, H2, and CO2 in an anaerobic process dependent on ADP, Pi, Mg2+, and succinate"]. The succinate requirement was half-saturated at [PMID:3090435 "5 microM succinate for T. vaginalis"]; the authors attribute it to the CoA transferase and say that the exact mechanism remained to be elucidated.
- [PMID:7808480 "Succinyl-coenzyme A synthetase is a hydrogenosomal enzyme which catalyzes the formation of ATP via substrate-level phosphorylation."]
- [PMID:31077495 "α- and β-subunits of succinyl-CoA synthetase (SCS) catalyze key steps of energy metabolism in Trichomonas vaginalis hydrogenosomes"]

## Pathway: no TCA cycle; the ASCT/SCS cycle

- PMID:22079833 (hydrogenosome proteome, full text read in the cache): [PMID:22079833 "Hydrogenosomes can generate ATP by substrate level phosphorylation but not via oxidative phosphorylation as mitochondria do."] and [PMID:22079833 "Hydrogenosomes also lack a trichloroacetic acid (TCA) cycle, cytochromes and members of complex I-IV"]. The authors wrote "trichloroacetic" where tricarboxylic is meant; the abbreviation and the context leave no doubt. The sentence is in the introduction and is about the organelle.
- The same paper lists SCS among the energy-metabolism proteins of the proteome: [PMID:22079833 "succinate thiokinase (SCS), adenylate kinase (AK)"]. The locus tags are in a table and supplementary tables that are not in the cached text, so TVAG_259190 was not confirmed individually.
- [PMID:22079833 "The human pathogen Trichomonas vaginalis lacks conventional mitochondria and instead contains divergent mitochondrial-related organelles."]
- The cycle (PMID:9501211, abstract only; the experiments are on trypanosomatids and the trichomonad statement is background): [PMID:9501211 "Hydrogenosome-containing anaerobic protists, such as the trichomonads, produce large amounts of acetate by an acetate:succinate CoA transferase (ASCT)/succinyl CoA synthetase cycle."]
- The partner enzyme (PMID:18024431, abstract only): [PMID:18024431 "is present in the hydrogenosomes where it functions as the T. vaginalis acetate:succinate CoA-transferase (TvASCT)"]; [PMID:18024431 "It was shown that the CoA transferase activity is succinate-dependent."]
- Review (PMID:20085767, abstract only): [PMID:20085767 "reaction yields succinyl-CoA for ATP formation via succinyl-CoA synthetase"]
- [PMID:8410536 "Hydrogenosomes are the site of fermentative oxidation of pyruvate, coupled to ATP production via substrate level phosphorylation."]
- Ancestry of the enzyme (PMID:16515848, abstract only): [PMID:16515848 "Our analyses of the Trichomonas vaginalis SCS sequences also confirmed the mitochondrial affiliation of these hydrogenosomal enzymes, in contrast to previous results."] The enzyme is of mitochondrial descent; the organelle it now sits in is classed separately in GO.

Process term decision. GO:0006099 tricarboxylic acid cycle is not supported: there is no cycle in the organelle. GO:0006104 succinyl-CoA metabolic process is true and names no pathway. No new process term is proposed:

- GO has no term for the ASCT/SCS cycle and none for substrate-level phosphorylation (QuickGO term search, 2026-11-18).
- GO:0019654 pyruvate fermentation to acetate does not fit. Its definition reads "The anaerobic chemical reactions and pathways resulting in the breakdown of acetate, yielding energy in the form of ATP." (QuickGO, 2026-11-18), which describes breakdown of acetate under a "fermentation to acetate" label.
- Participation test: the acetate is released by ASCT, not by SCS. SCS regenerates the succinate acceptor and conserves the energy.
- Comparator check, run by term id for eleven SCS beta subunits (human SUCLA2 and SUCLG2, yeast LSC2, E. coli SucC, T. brucei Q38AM2, Neocallimastix P53587, Blastocystis B3FHP0, Q03184, and three others) with a positive control for each term: no SCS beta subunit carries GO:0006754 ATP biosynthetic process, GO:0019413 acetate biosynthetic process or any term under GO:0006083 acetate metabolic process, including the T. brucei subunit that works in the same cycle. GO:1901289 succinyl-CoA catabolic process is carried by three of them from ComplexPortal; it is a child of GO:0006104 and nothing measured on this protein shows the direction, so it is not proposed.

## The AP51 adhesin claim

- The claim: [PMID:1602965 "Four trichomonad surface proteins (adhesins) with molecular masses of 65,000 daltons (65 kDa; AP65), 51 kDa (AP51), 33 kDa (AP33), and 23 kDa (AP23) mediate the interaction of T. vaginalis with epithelial cells."]
- The genes (PMID:9466942, abstract only): [PMID:9466942 "The ap51-1 and ap51-3 genes each encoded for 407 amino acids while ap51-2 encoded 408 amino acids"]; [PMID:9466942 "Northern analysis showed transcriptional regulation by iron of only the ap51-1 and ap51-3 genes but not ap51-2"]; [PMID:9466942 "the ap51 genes had partial homology to the beta-subunit of succinyl-CoA synthetase, reinforcing the idea that molecular mimicry may play a role in host parasitism by T. vaginalis"]. The UniProt entry for ap51-1 (Q6LC42) is identical to Q03184 over all of its 403 residues, so "partial homology" understates it: ap51-1 is this gene.
- Surface placement under high iron (PMID:12603729, abstract only): [PMID:12603729 "high-iron-grown organisms coexpressed adhesins on the surface and intracellularly in contrast with low-iron parasites"]
- Heme binding (PMID:19105955, abstract only): [PMID:19105955 "AP51 and AP65, besides serving as adhesion molecules, could also act as heme- and hemoglobin-binding proteins"]
- Against: [PMID:10669133 "These results support the idea that these proteins are restricted to a hydrogenosomal function and do not play a role as adhesins at the plasma membrane surface."] and [PMID:31077495 "these results demonstrate that the α- and β-SCS subunits are targeted only to the hydrogenosomes, which argues against their putative moonlighting function"].
- Status: disputed. GOA has no adhesion term on Q03184 or on Q6LC42 (QuickGO, 2026-11-18). None is proposed. All of these papers were read as abstracts only.

## Position in the PANTHER tree (PANTHER release 19 treeinfo service, read 2026-11-18)

- Q03184 is an InterPro member of PTHR11815:SF10 and is not a leaf of the PAINT tree. It has no IBA row. Its four TreeGrafter rows name PANTHER:PTN000929413, which is the leaf for the same gene in strain G3 (A2EBX0, TVAG_259190). The two other beta genes are the leaves PTN000929414 (A2FVK7) and PTN000929415 (A2D987).
- Path from the root to that leaf: PTN000212531 (LUCA) > PTN000212532 (Archaea-Eukaryota) > PTN000212530 (duplication) > PTN002483419 (Eukaryota; the G daughter) > PTN007541286 (Bikonts) > PTN004310558 (Excavates) > PTN008982090 (duplication; the three Trichomonas leaves) > PTN000929413.
- Origin of each grafted term, from the PAINT file: GO:0004775, GO:0006099, GO:0006104 and GO:0042709 are IBD at the root PTN000212531; GO:0005739 is IBD at the duplication node PTN000212530, e.g. [file:interpro/panther/PTHR11815/PTHR11815-paint.tsv "PTHR11815	PTN000212530	GO:0005739	C	IBD	false"].
- The leaf is outside PTN000929335, the node where PAINT places the gain of GDP-forming and the loss of ADP-forming activity. So the gene inherits the ADP-forming term from the root and no GDP-forming term.
- Sequence trees do not resolve where the Trichomonas genes belong: [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "| Trichomonas vaginalis, 3 genes (Gly) | G daughter | with SUCLG2 | 25 / 122 / 53 | outside both |"]. Membership of the PANTHER G daughter should not be read as orthology to SUCLG2.
- Node judgement. The root placement of the ADP-forming activity, the metabolite-level process and the complex is sound for this clade: the organelle enzyme is ADP-dependent. The mitochondrion placement at PTN000212530 and the TCA placement at the root do not hold for the Trichomonas clade, which is what the family review proposes to prune at PTN008982090.
- The GO:0006099 row on Q03184 has three sources besides TreeGrafter (InterPro IPR005809, UniRule UR000405968 and UniPathway UPA00223). A loss annotation in the PAINT tree would not remove them.

## Points for the family reviews

- The full text of PMID:22079833 states that hydrogenosomes lack a TCA cycle. The PTHR11815 and PTHR11117 reviews say the abstracts they read do not state this in so many words; this sentence fills that gap for the organelle.
- UniProt names the three genome-strain leaves A2EBX0, A2FVK7 and A2D987 "mitochondrial" and gives them a Mitochondrion location from HAMAP rule MF_03219. This is a second source of the wrong location for the Trichomonas clade, beside the PAINT IBA.
- In the alpha tree (PTHR11117), PTN000874238 is the leaf A0A8U0WP19 (TVAG_047890) inside the clade PTN008961326. The reviewed alpha entry P53400 is grafted to that leaf, and P53399 and P53401 to the clade node. This agrees with the family review.
- The AP51 adhesin literature concerns the beta subunits of this family and is not mentioned in the family reviews.
