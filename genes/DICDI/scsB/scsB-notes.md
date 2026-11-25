# scsB (Dictyostelium discoideum, UniProtKB:Q869S7, DDB_G0274449) notes

Started 2026-11-18, as a follow-up to the evolutionary reviews of the succinyl-CoA synthetase (SCS) beta family PTHR11815 and alpha family PTHR11117.

## Terms used in these notes

- SCS: succinyl-CoA synthetase (succinate--CoA ligase), an alpha/beta enzyme of the tricarboxylic acid cycle.
- G-type and A-type beta subunit: the beta subunit groups with animal SUCLG2 (GTP-specific enzyme) or with animal SUCLA2 (ATP-specific enzyme) in the family trees. The label is a statement of descent, not of measured nucleotide specificity.
- Position 20: residue 20 of the mature beta subunit; Gln in pig GTP-specific SCS, Pro in E. coli SucC.
- RER: relative enrichment ratio of PMID:35602934, the abundance of a protein in purified mitochondria over whole-cell lysate, normalised to 47 reference mitochondrial proteins.

## Summary

- scsB encodes a 420-residue beta subunit of SCS. It is the G-type (SUCLG2-like) beta subunit of Dictyostelium by descent. The genome also has an A-type beta gene (scsC, Q55AI5) and one alpha gene (scsA, P36967).
- No publication studies scsB as a gene product. There is no mutant, no recombinant protein and no assay assigned to this subunit.
- The only direct data on the protein are from one organelle-proteomics study, which finds it in Percoll-purified mitochondria (PMID:35602934).
- The Dictyostelium enzyme has been assayed and uses GTP, but the assays are on the enzyme and its alpha subunit, and both beta subunits are present in mitochondria of growing cells. The GDP-forming activity of scsB is therefore an inference from descent and family rules that agrees with the enzyme-level assays.

## UniProt record (entry version 139)

- Reviewed entry SUCB2_DICDI, protein existence level 3 (inferred from homology). The entry cites only the two genome papers.
- Every functional statement carries the HAMAP rule MF_03221 as its evidence; none is experimental. [file:DICDI/scsB/scsB-uniprot.txt "GTP-specific succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of GTP"]
- [file:DICDI/scsB/scsB-uniprot.txt "Heterodimer of an alpha and a beta subunit. The beta subunit determines specificity for GTP."]
- [file:DICDI/scsB/scsB-uniprot.txt "This protein may be expected to contain an N-terminal transit peptide but none has been predicted."] The record has a CHAIN 1..420 and no TRANSIT feature.
- Predicted binding residues from the rule: GTP at 46, 78..80 and 135; Mg(2+) at 232 and 246; substrate shared with the alpha subunit at 297 and 354..356.

## Literature search (2026-11-18)

The perplexity deep-research provider was not available in this environment (`just deep-research DICDI scsB --provider perplexity` reported "Provider 'perplexity' not available"), so no deep-research file exists for this gene. The search below was done by hand.

PubMed (E-utilities esearch), query and number of hits:

- `scsB AND Dictyostelium`: 0
- `"DDB_G0274449"`: 0
- `Q869S7`: 0
- `SUCLG2 AND Dictyostelium`: 0
- `succinyl-CoA synthetase AND Dictyostelium`: 9 (PMID:9344470, PMID:9099993, PMID:7669763, PMID:7771809, PMID:8016083, PMID:8060491, PMID:8240297, PMID:8384004, PMID:8448193)
- `succinate-CoA ligase AND Dictyostelium`, `succinate thiokinase AND Dictyostelium`, `succinyl-CoA ligase AND Dictyostelium`: 7, 7 and 6, all among the 9 above
- `"succinyl-CoA synthetase" AND Dictyostelium AND beta`: 2 (PMID:8016083, PMID:8240297); neither concerns a Dictyostelium beta gene
- `Dictyostelium AND mitochondria AND proteome` and `Dictyostelium AND mitochondrial AND proteomic`: 10 and 16 hits, from which PMID:35602934 and PMID:33923051 were read in full

The first, second, fourth and fifth queries were re-run when this review was written and gave the same counts.
Europe PMC full-text searches for `"Q869S7"`, `"SUCB2_DICDI"` and `"scsB" AND Dictyostelium` gave no paper on this gene.
The dictyBase gene page could not be read by machine, so its curated literature list was not checked.

Result: no paper names, sequences, purifies or mutates the Dictyostelium G-type beta subunit. The nine SCS papers concern the alpha subunit (p36) and the enzyme.

## What is known about the Dictyostelium enzyme (not assigned to scsB)

All five papers below are abstract-only in the cache.

- The purified enzyme uses GTP. [PMID:7771809 "We have previously shown that the enzyme purified from growing D. discoideum is a GTP-utilizing enzyme"]
- The partially purified alpha subunit is phosphorylated with GTP and little or not at all with ATP; crude preparations accept both. [PMID:8448193 "In crude sample preparations, p36 could be phosphorylated by both ATP or GTP"] [PMID:8448193 "Partially purified p36 retained its ability to be phosphorylated with GTP while exhibiting little or no phosphorylation with ATP"]
- A second laboratory also saw both nucleotides label the alpha subunit in crude mitochondrial fractions. [PMID:8384004 "p38 can be phosphorylated in vitro using either ATP or GTP as phosphoryl donors"]
- GDP is a substrate and GTP is formed. [PMID:8240297 "Dephosphorylation of p36 is induced by relatively high levels of GDP and is coincident with the formation of GTP"]
- The enzyme is an alpha/beta dimer. [PMID:8240297 "Gel-filtration analyses indicate that SCS in our system behaves as a non-interacting alpha beta dimer"] This is the only statement that the assayed enzyme has a beta subunit; it does not say which.
- Low GDP stimulates phosphoenzyme formation, interpreted as allosteric regulation. [PMID:8060491 "Low concentrations of GDP stimulate phosphoenzyme formation by either GTP, or succinyl-CoA and P(i)"] [PMID:8240297 "We propose that GDP functions as an allosteric regulator of SCS"]
- The alpha subunit has a cleaved 16-residue targeting sequence and is a single-copy gene. [PMID:7771809 "Direct amino acid sequence data indicate that the first 16 amino acids encoded by the cDNA comprise a mitochondrial targeting sequence"] [PMID:7771809 "In D. discoideum, the alpha subunit is a single copy gene that is developmentally regulated"]

Why these assays cannot be assigned to scsB: the purified enzyme was not characterised at the level of its beta subunit in any abstract, and the A-type beta subunit scsC is in the same mitochondria (next section). Labelling by ATP in crude fractions has at least two explanations that the abstracts do not separate: an scsC-containing ADP-forming enzyme, or conversion of ATP to GTP by another enzyme in the fraction.

## Direct data on the scsB protein: mitochondrial proteome (PMID:35602934, full text and supplementary tables read)

- Design. [PMID:35602934 "From AX2 axenic cultures, we prepared mitochondria isolates—both crude and highly purified—through Percoll gradient ultracentrifugation"] [PMID:35602934 "We performed tandem mass tag (TMT) liquid chromatography-mass spectrometry (LC-MS) on both mitochondria isolates and included AX2 whole-cell lysate as the control"]
- Classification. [PMID:35602934 "we assessed the probability of a protein localizing to mitochondria by comparing its relative enrichment in mitochondrial preparations to a list of 47 authentic mitochondrial proteins that include components of electron transport chain complexes and enzymes in the citric acid cycle"] [PMID:35602934 "We chose an RER cutoff of 0.392"]
- Values for Q869S7 (DDB_G0274449), read from the supplementary spreadsheets, which are not part of the cached text: Table S2, the three enrichment ratios are 0.651, 0.799 and 1.228 (the 0.799 value is the RER); Table S4, RER 0.799 and probability 1 of belonging to the mitochondrial cluster; Table S7, listed in the compendium with discovery method "Proteomics" and class "Energy metabolism"; Table S1 and Table S5, TargetP-2.0 prediction OTHER.
- The same tables give RER 1.021 for scsA (P36967) and 0.854 for scsC (Q55AI5), both predicted to have a mitochondrial targeting peptide. All three SCS subunits are therefore in purified mitochondria of axenically growing AX2 cells.
- Caveat. Table S3 lists Q869S7 among the 47 reference proteins that define RER 1.0, chosen from existing annotation. The classification of Q869S7 as mitochondrial is therefore not independent of prior annotation. The measured enrichment is still a measurement on this protein, and it is well above the cutoff of 0.392.
- Table S9 (RNA-seq of an earlier study, raw values at 0, 4, 8, 12, 16, 20 and 24 h of development): 212, 387, 246, 183, 127, 63, 54. The transcript falls late in development, as the alpha transcript does.
- Q869S7 is not among the 81 proteins imaged by microscopy.
- Limits: whole-organelle proteomics, no sub-mitochondrial resolution.

A second proteome, PMID:33923051 (full text read for the scsA review), reports only the alpha subunit among SCS subunits.

## Evolutionary placement

- PANTHER PTHR11815, read from the PANTHER treeinfo service on 2026-11-18. Path from root to leaf: PTN000212531 (LUCA) > PTN000212532 (Archaea-Eukaryota) > PTN000212530 (duplication) > PTN002483419 (Eukaryota, the G daughter) > PTN000929335 (Unikonts) > PTN000929353 (Dictyostelium) > leaf PTN000212642 (Q869S7). The nodes PTN000212532, PTN000929353 and PTN000212642 are not in `genes/yeast/LSC2/LSC2-bioinformatics/results.yaml`; they come from the live service only.
- PAINT annotations that reach this leaf (`interpro/panther/PTHR11815/PTHR11815-paint.tsv`): tricarboxylic acid cycle, succinyl-CoA metabolic process, succinate-CoA ligase complex and ADP-forming activity at the LUCA node PTN000212531; mitochondrion at the duplication node PTN000212530; gain of GDP-forming activity and loss of ADP-forming activity at PTN000929335.
- Trees built independently of PANTHER (neighbor joining and maximum likelihood on one 64-sequence panel and alignment, so independent of PANTHER but not of each other). [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "| Dictyostelium Q869S7 (Gln) | G daughter, under PTN000929335 | with SUCLG2 | 10 / 182 / 8 | with SUCLG2 |"] Q869S7 is with SUCLG2 in 182 of 200 neighbor-joining bootstrap trees and in all three maximum-likelihood runs.
- [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "PTN000929335 is the node that holds the experimentally characterised GTP-specific enzymes (pig and human SUCLG2); it is not the limit of Gln20."]
- [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "the assays are on the enzyme and are not assigned to the Gln20 beta gene Q869S7"]
- Subfamily label. Q869S7 is in PTHR11815:SF10, the root subfamily, which is named GDP-forming but also holds ADP-forming bacterial SucC. The subfamily name is therefore not evidence of GDP specificity.

## Family-level evidence on nucleotide specificity

- Pig GTP-specific SCS (abstract only): [PMID:16481318 "interactions of the guanine base with a glutamine residue (Gln-20beta) and with backbone atoms provide the specificity"] and [PMID:16481318 "GTP is bound in the ATP-grasp domain"].
- Pigeon enzymes (abstract only): [PMID:9765290 "Two succinyl-CoA synthetases, one highly specific for GTP/GDP and the other for ATP/ADP, have been purified to homogeneity from pigeon liver and breast muscle"].
- Gln at position 20 is not sufficient. E. coli Pro20-to-Gln (abstract only): [PMID:10353839 "had a Km(app) for GTP that was more than 5 times lower than that of wild-type SCS, whereas parameters for the other substrates remained unchanged"]. Blastocystis (full text): [PMID:18452512 "Although analysis of residues inside the nucleotide-binding site suggests that Blastocystis SCS is GTP-specific, we demonstrate that it is ATP-specific."]

## N-terminus and sub-mitochondrial location

Analysis in `scsB-bioinformatics/` (script `nterm_extension.py`, results in `results.yaml` and `RESULTS.md`).

- Six reference beta subunits (human, pig and mouse SUCLG2, human SUCLA2, yeast LSC2, E. coli SucC) place their mature start on Leu27 of Q869S7. [file:DICDI/scsB/scsB-bioinformatics/RESULTS.md "Six of the seven references place their mature start on Leu27 of Q869S7."]
- The 26 residues ahead of Leu27 are basic and have no acidic residue. [file:DICDI/scsB/scsB-bioinformatics/RESULTS.md "They contain 4 basic residues (Lys or Arg), no acidic residue (Asp or Glu), 3 Ser or Thr and 12 hydrophobic residues"]
- Position 20 of the mature subunit is Gln46, the residue UniProt lists as a GTP-binding residue.
- The alignment does not show that the extension is cleaved. TargetP-2.0 classifies the protein as OTHER (Table S1 and Table S5 of PMID:35602934) and UniProt says no transit peptide is predicted.

Reasoning for a mitochondrial matrix row (inferred by curator, added beside the three mitochondrion rows):

1. The protein is measured in Percoll-purified mitochondria (PMID:35602934).
2. Its function, as a subunit of the SCS step of the tricarboxylic acid cycle, acts on matrix metabolites.
3. Its only possible alpha partner, scsA, is a single-copy gene whose product has an experimentally determined cleaved presequence, and the enzyme is a soluble alpha/beta dimer (PMID:7771809, PMID:8240297). A beta subunit in that dimer is where the alpha subunit is.
4. It has no transmembrane feature in UniProt and a basic N-terminal extension in the position of the animal transit peptide.

Against: no sub-mitochondrial assay, and no predicted presequence. `core_functions.locations` stays at mitochondrion, because the activity has not been shown in a sub-compartment.

## Decisions on the GOA rows (16 rows, no experimental row, no ND row)

- GO:0004776 GDP-forming activity (IBA from PTN000929335, IEA): accepted as the core activity. The node placement holds for this leaf in the PANTHER tree and in the neighbor-joining and maximum-likelihood trees of the LSC2 analysis (one panel, two methods). The gene assignment is by descent; the enzyme-level assays agree.
- NOT GO:0004775 ADP-forming activity (IBA, loss at PTN000929335): accepted. The family review rates the loss as supported. No assay of a Dictyostelium scsA/scsB heterodimer with ADP exists, so the negative rests on descent and on the pigeon and pig G-type enzymes, and it agrees with the partially purified Dictyostelium enzyme not using ATP.
- GO:0005524 ATP binding (IEA from the ATP-grasp fold signatures): MODIFY to GO:0005525 GTP binding, a lateral correction, as in the human SUCLG2 review. The signatures are named for the fold. The nucleotide is inferred, not measured, for this protein, and the action is kept consistent with the accepted NOT ADP-forming row.
- GO:0005525 GTP binding and GO:0000287 magnesium ion binding (IEA, UniRule): kept as non-core; substrate and cofactor binding that are part of the reaction.
- GO:0046872 metal ion binding (IEA, InterPro): TOO_GENERAL. The term is imprecise on its own and magnesium ion binding is asserted on the gene; the row's own evidence (an ATP-grasp fold signature) does not identify the metal, so MODIFY does not apply. The sibling reviews of E. coli sucC and human SUCLA2 used MODIFY to GO:0000287 for the same row; the choice here follows the maintainer ruling of 2026-11-14 that MODIFY needs the row's own evidence, and does not make those reviews defective.
- GO:0003824 catalytic activity (IEA): TOO_GENERAL.
- GO:0006099 tricarboxylic acid cycle and GO:0006104 succinyl-CoA metabolic process (IBA from the LUCA node, IEA): accepted. The beta subunit binds succinate and the nucleotide, so it does part of the work of the step.
- GO:0005739 mitochondrion (IBA from PTN000212530, ISS from mouse Suclg2 by dictyBase in 2005, IEA): accepted under the root-organelle policy. The claim holds on the target itself (PMID:35602934).
- GO:0042709 succinate-CoA ligase complex (IBA from the LUCA node): accepted. The row's evidence stops at the nucleotide-neutral complex, because the LUCA node has ADP- and GDP-forming descendants, and the term is specific enough to keep. The sibling reviews (human SUCLG2 and SUCLA2, yeast LSC2, S. pombe SPCC1620.08, E. coli sucC) mark this row TOO_GENERAL; each of those genes has an existing annotation to a nucleotide-specific complex and scsB has none. No NEW row for GO:0045244 is proposed: it is a child of a term the gene carries and would rest on the same inference as the GDP-forming activity. GO:0045244 is named in `core_functions.in_complex`.
- NEW GO:0005759 mitochondrial matrix (IC): see the section above.

## Curation gaps (not knowledge gaps)

- GOA has no experimental mitochondrion row for Q869S7, although PMID:35602934 supplies high-throughput evidence that dictyBase could annotate (for scsB, scsC and scsA).
- scsC (Q55AI5) carries a no-data annotation for molecular function, while scsB carries none; neither subunit has been assayed.
- GO:0045244 succinate-CoA ligase complex (GDP-forming) is not annotated on scsB.
- In `interpro/panther/PTHR11815/PTHR11815-review.yaml`, the assessment of the loss of ADP-forming activity at PTN000929335 lists the affected subfamilies SF11 and SF12; Q869S7, which is below that node, is in SF10.
- scsC (Q55AI5) has no review in this repository yet.

## Open questions

See `knowledge_gaps` in the review: nucleotide specificity of a defined scsA/scsB heterodimer, division of labour between scsB and scsC, the mature N-terminus and import route, and the phenotype of a mutant.
