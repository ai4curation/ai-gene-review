# scsC (Dictyostelium discoideum, UniProtKB:Q55AI5, DDB_G0271842) notes

Started 2026-11-18, as a follow-up to the evolutionary reviews of the succinyl-CoA synthetase (SCS) beta family PTHR11815 and alpha family PTHR11117, and written after the reviews of the alpha subunit scsA and the G-type beta subunit scsB.

## Terms used in these notes

- SCS: succinyl-CoA synthetase (succinate--CoA ligase), an alpha/beta enzyme of the tricarboxylic acid cycle.
- A-type and G-type beta subunit: the beta subunit groups with animal SUCLA2 (ATP-specific enzyme) or with animal SUCLG2 (GTP-specific enzyme) in the family trees. The label is a statement of descent, not of measured nucleotide specificity.
- A daughter: the clade below PANTHER node PTN008330414, one of the two clades below the eukaryotic duplication node PTN000212530 of PTHR11815. It contains human SUCLA2 and yeast LSC2.
- Position 20: residue 20 of the mature beta subunit; Gln in pig GTP-specific SCS, Pro in E. coli SucC.
- RER: relative enrichment ratio of PMID:35602934, the abundance of a protein in purified mitochondria over whole-cell lysate, normalised to 47 reference mitochondrial proteins.

## Summary

- scsC encodes a 445-residue beta subunit of SCS. It is the A-type (SUCLA2-like) beta subunit of Dictyostelium by descent. The genome also has a G-type beta gene (scsB, Q869S7) and one alpha gene (scsA, P36967).
- No publication studies scsC as a gene product. There is no mutant, no recombinant protein and no assay assigned to this subunit.
- The only direct data on the protein are from one organelle-proteomics study, which finds it in Percoll-purified mitochondria (PMID:35602934).
- The Dictyostelium enzyme has been assayed, and what was purified uses GTP. That is the activity expected of the scsB-containing enzyme, not of an scsC-containing one. The ADP-forming activity of scsC is therefore an inference from descent and family rules that no measurement in this species supports or contradicts.

## UniProt record (entry version 125, sequence version 1)

- Reviewed entry SUCB1_DICDI, protein existence level 3 (inferred from homology). The entry cites only the two genome papers (PMID:12097910, PMID:15875012).
- Every functional statement carries the HAMAP rule MF_03220 as its evidence; none is experimental. [file:DICDI/scsC/scsC-uniprot.txt "The beta subunit provides nucleotide specificity of the enzyme and binds the substrate succinate, while the binding sites for coenzyme A and phosphate are found in the alpha subunit."]
- [file:DICDI/scsC/scsC-uniprot.txt "Reaction=succinate + ATP + CoA = succinyl-CoA + ADP + phosphate;"]
- [file:DICDI/scsC/scsC-uniprot.txt "Heterodimer of an alpha and a beta subunit. The beta subunit determines specificity for ATP."]
- [file:DICDI/scsC/scsC-uniprot.txt "Belongs to the succinate/malate CoA ligase beta subunit family. ATP-specific subunit beta subfamily."]
- Predicted features from the rule: transit peptide 1..17, chain 18..445, ATP-grasp domain 43..270, ATP at 80 and 87..89, Mg(2+) at 240 and 254, substrate shared with the alpha subunit at 305 and 362..364.
- Family cross-references: PANTHER PTHR11815:SF1, HAMAP MF_03220 (Succ_CoA_betaA_euk), InterPro IPR034723, Pfam PF08442 and PF00549.

## Literature search (2026-11-18)

The perplexity deep-research provider was not available in this environment (`just deep-research DICDI scsC --provider perplexity` reported "Provider 'perplexity' not available. Available: asta, openscientist, claude_code"), so no deep-research file exists for this gene. The search below was done by hand.

PubMed (E-utilities esearch), query and number of hits, run when this review was written:

- `scsC AND Dictyostelium`: 0
- `sucla2 AND Dictyostelium`: 0
- `"DDB_G0271842"`: 0
- `Q55AI5`: 0
- `succinyl-CoA synthetase AND Dictyostelium`: 9 (PMID:9344470, PMID:9099993, PMID:7669763, PMID:7771809, PMID:8016083, PMID:8060491, PMID:8240297, PMID:8384004, PMID:8448193)
- `succinate-CoA ligase AND Dictyostelium` and `succinate thiokinase AND Dictyostelium`: 7 each, all among the 9 above
- `Dictyostelium AND mitochondria AND proteome`: 10; `Dictyostelium AND mitochondrial AND proteomic`: 16. From these, PMID:35602934 and PMID:33923051 were read in full.

Europe PMC full-text search for `"Q55AI5" OR "SUCB1_DICDI"`: 0 hits.

A preparatory search for this review, made the same day, also ran `succinyl-CoA ligase AND Dictyostelium` (6 hits, among the 9), `succinyl CoA synthetase beta subunit AND Dictyostelium` (2 hits, PMID:8016083 and PMID:8240297, neither on a Dictyostelium beta gene), a PubMed query combining the enzyme names with `ATP-specific OR ADP-forming OR SUCLA2` (0 hits), and Europe PMC queries for `"scsC" AND "Dictyostelium"` (3 hits, none on this gene) and `"Dictyostelium discoideum" AND ("scsC" OR "scsB" OR "scsA")` (6 hits, one relevant, PMID:33923051, which names scsA only). I did not re-run those.

The dictyBase gene record lists two references for the gene, PMID:8448193 and PMID:7771809. Both are about the alpha subunit and the enzyme and predate the genome. The dictyBase curated summary says that scsC "is highly similar to known ADP-forming succinyl-CoA ligase beta subunits". That is a database description and not a literature search; it was read in the preparatory search and not re-read by me.

Result: no paper names, sequences, purifies, assays or mutates the Dictyostelium A-type beta subunit. The nine SCS papers concern the alpha subunit (p36) and the enzyme. One proteomics paper measures the scsC protein in mitochondria.

Not read: the full text of PMID:20013782 (2-D DIGE mitochondrial proteome, 96 proteins; the abstract does not name SCS). It could hold a second identification of the protein in mitochondria.

## What is known about the Dictyostelium enzyme (not assigned to scsC)

All of these papers are abstract-only in the cache.

- The purified enzyme uses GTP. [PMID:7771809 "We have previously shown that the enzyme purified from growing D. discoideum is a GTP-utilizing enzyme"]
- The partially purified alpha subunit is phosphorylated with GTP and little or not at all with ATP; crude preparations accept both. [PMID:8448193 "In crude sample preparations, p36 could be phosphorylated by both ATP or GTP"] [PMID:8448193 "Partially purified p36 retained its ability to be phosphorylated with GTP while exhibiting little or no phosphorylation with ATP"]
- A second laboratory also saw both nucleotides label the alpha subunit in crude mitochondrial fractions. [PMID:8384004 "p38 can be phosphorylated in vitro using either ATP or GTP as phosphoryl donors"]
- The enzyme is an alpha/beta dimer. [PMID:8240297 "Gel-filtration analyses indicate that SCS in our system behaves as a non-interacting alpha beta dimer"] This does not say which beta subunit.
- The alpha subunit has a cleaved 16-residue targeting sequence and is a single-copy gene. [PMID:7771809 "Direct amino acid sequence data indicate that the first 16 amino acids encoded by the cDNA comprise a mitochondrial targeting sequence"] [PMID:7771809 "In D. discoideum, the alpha subunit is a single copy gene that is developmentally regulated"]

What this means for scsC:

- The purified, GTP-using enzyme is what descent predicts for scsA with scsB. It is not evidence for scsC.
- Labelling of the alpha subunit by ATP in crude fractions is what an scsA/scsC enzyme would produce. It is not evidence for one either, because conversion of ATP to GTP by another enzyme in a crude fraction (for example nucleoside diphosphate kinase) would give the same result, and the abstracts do not separate the two.
- If an ATP-linked form exists, it was lost or inactivated during partial purification. Whether that happened is not known.

## Direct data on the scsC protein: mitochondrial proteome (PMID:35602934, full text and supplementary tables read)

I downloaded the supplementary tables of PMC9118663 from Europe PMC on 2026-11-18 and read the rows for Q55AI5 myself. The values are in the spreadsheets and not in the cached text, so they cannot be quoted.

- Design. [PMID:35602934 "From AX2 axenic cultures, we prepared mitochondria isolates—both crude and highly purified—through Percoll gradient ultracentrifugation"]
- Classification. [PMID:35602934 "we assessed the probability of a protein localizing to mitochondria by comparing its relative enrichment in mitochondrial preparations to a list of 47 authentic mitochondrial proteins that include components of electron transport chain complexes and enzymes in the citric acid cycle"] [PMID:35602934 "We chose an RER cutoff of 0.392"]
- Values for Q55AI5 (DDB_G0271842):
  - Table S2: enrichment ratios crude/lysate 0.781, pure/lysate 0.854, pure/crude 1.093. The pure/lysate value is the RER.
  - Table S4: RER 0.854, probability 1 of belonging to the mitochondrial cluster.
  - Table S7: listed in the compendium with discovery method "Proteomics" and class "Energy metabolism".
  - Table S1 and Table S5: TargetP-2.0 prediction mTP (mitochondrial targeting peptide). In Table S5 the row for Q55AI5 carries a dictyBase ID that belongs to another gene (DDB_G0282961), and the row with DDB_G0271842 carries another accession; the two columns of that table are offset by one row there. The UniProt accession, RER and prediction agree with Table S1 and Table S4.
  - Table S9 (RNA-seq of an earlier study, raw values at 0, 4, 8, 12, 16, 20 and 24 h of development): 108, 26, 53, 36, 20, 14, 14. The transcript falls in development.
  - Not among the 98 proteins selected for imaging (Table S6).
- Caveat. Table S3 lists Q55AI5 among the 47 reference proteins that define RER 1.0, as it does scsA (P36967) and scsB (Q869S7). The reference set was chosen from existing annotation, so the classification of Q55AI5 as mitochondrial is not independent of prior annotation. The measured enrichment is still a measurement on this protein, and it is well above the cutoff of 0.392.
- The same tables give RER 1.021 for scsA and 0.799 for scsB (from the scsB review, which read them directly). All three SCS subunits are in purified mitochondria of axenically growing AX2 cells.
- Limits: whole-organelle proteomics, no sub-mitochondrial resolution, no information on activity or on the partner of scsC.

A second proteome, PMID:33923051 (full text in the cache), reports only the alpha subunit among SCS subunits: [PMID:33923051 "succinate-CoA ligase (XP_636263.1)"]. The text does not contain scsC or its RefSeq accession XP_645537.1.

A lead that is not literature: the dictyBase developmental proteome viewer has an entry for scsC at all five life-cycle stages, at abundance similar to scsB and scsA. The preparatory search read it from the dictyBase site and did not resolve its publication, so it is not cited in the review.

## Evolutionary placement

- PANTHER PTHR11815, subfamily SF1. Path from the root: PTN000212531 (LUCA) > PTN000212530 (duplication) > PTN008330414 (the A daughter, 63 leaves), which holds human SUCLA2, yeast LSC2 and S. pombe SPCC1620.08.
- scsC is not below PTN000929335, the node where PAINT places the gain of GDP-forming activity and the loss of ADP-forming activity. Its paralog scsB is.
- PAINT annotations that reach this leaf (`interpro/panther/PTHR11815/PTHR11815-paint.tsv`): ADP-forming activity, tricarboxylic acid cycle, succinyl-CoA metabolic process and succinate-CoA ligase complex from the LUCA node PTN000212531; mitochondrion from the duplication node PTN000212530.
- Independent trees. [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "| Dictyostelium Q55AI5 (Pro) | A daughter | with SUCLA2 | 127 / 59 / 14 | with SUCLA2 |"] Q55AI5 is with SUCLA2 in 127 of 200 neighbor-joining bootstrap trees, with SUCLG2 in 59 and outside both in 14; the maximum-likelihood tree places it with SUCLA2.
- The maximum-likelihood clade that joins it to SUCLA2 has 24 sequences and ultrafast bootstrap 98, and is found in 33 of 200 neighbor-joining bootstrap trees. [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "| human SUCLA2 and the Dictyostelium Pro20 gene | 24: the 16 above, Monosiga A9UTU9 (Gly20), Dictyostelium Q55AI5, Phytophthora H3GTW5, Thalassiosira B8BS06, three Paramecium Pro20 genes and Plasmodium Q8ILE9; no Gln20 sequence | 98 to 98 | 33/200 |"]
- So the A-type placement of scsC agrees between PANTHER and the maximum-likelihood tree, and is only moderately supported by neighbor joining. It is weaker than for yeast LSC2 (197 of 200). scsC is not in the 16-sequence fungal and animal clade with ultrafast bootstrap 100.
- Pairwise identity does not help: scsC is 57.9% identical to its paralog scsB, 54.6% to human SUCLA2 and 52.8% to human SUCLG2 (`scsC-bioinformatics/RESULTS.md`).
- The family review of PTHR11815 rates the placement of ADP-forming activity at the LUCA node as needing pruning for leaves other than scsC, and says that the term holds for the A-type lineage. Its description of SF1 says "ADP-forming where assayed (S. cerevisiae, animal SUCLA2)". The Dictyostelium member is not assayed.

## Family-level evidence on nucleotide specificity

- Yeast, the closest assayed A-type enzyme: [PMID:9874242 "The yeast succinyl-CoA ligase was shown to utilize ATP but not GTP for succinyl-CoA synthesis"]
- Pigeon enzymes (abstract only): [PMID:9765290 "Two succinyl-CoA synthetases, one highly specific for GTP/GDP and the other for ATP/ADP, have been purified to homogeneity from pigeon liver and breast muscle"]
- Position 20 does not decide nucleotide use alone. [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "The residue therefore does not by itself decide nucleotide use for an unassayed subunit."] Blastocystis (full text): [PMID:18452512 "Although analysis of residues inside the nucleotide-binding site suggests that Blastocystis SCS is GTP-specific, we demonstrate that it is ATP-specific."] Thermus aquaticus SCS has Pro20 and prefers GTP (stated in the LSC2 analysis from PMID:22751660, which I did not read for this review).

## N-terminus and sub-mitochondrial location

Analysis in `scsC-bioinformatics/` (script `nterm_extension.py`, results in `results.yaml` and `RESULTS.md`).

- Six reference beta subunits (human SUCLA2, human, pig and mouse SUCLG2, yeast LSC2, E. coli SucC) place their mature start on Leu35 of Q55AI5. [file:DICDI/scsC/scsC-bioinformatics/RESULTS.md "Six of the seven references with a mature start place it on Leu35 of Q55AI5."]
- The 34 residues ahead of Leu35 are basic and have no acidic residue. [file:DICDI/scsC/scsC-bioinformatics/RESULTS.md "They contain 7 basic residues (Lys or Arg), no acidic residue (Asp or Glu), 9 Ser or Thr and 13 hydrophobic residues"]
- Position 20 of the mature subunit is Pro54.
- The transit peptide in the UniProt record is 1..17, from the family rule. It is half the length of the extension. [file:DICDI/scsC/scsC-bioinformatics/RESULTS.md "The transit peptide in the UniProt record (1..17) is half the length of the extension."] The cleavage site has not been measured, so this is an open point and not an error in the record.
- TargetP-2.0 predicts a mitochondrial targeting peptide (Table S1 and Table S5 of PMID:35602934). The paralog scsB is predicted OTHER in the same tables.

Reasoning for a mitochondrial matrix row (inferred by curator, added beside the three mitochondrion rows):

1. The protein is measured in Percoll-purified mitochondria (PMID:35602934).
2. Its function, as a subunit of the SCS step of the tricarboxylic acid cycle, acts on matrix metabolites.
3. Its only possible alpha partner, scsA, is a single-copy gene whose product has an experimentally determined cleaved presequence (PMID:7771809). A beta subunit that works with it is where the alpha subunit is.
4. It has no transmembrane feature in UniProt, a basic N-terminal extension in the position of the animal transit peptides, and a predicted targeting peptide from two sources (the HAMAP rule and TargetP-2.0).

Against: no sub-mitochondrial assay. `core_functions.locations` stays at mitochondrion, because the activity has not been shown in a sub-compartment.

## Decisions on the GOA rows (15 rows, no experimental row, one ND row)

- GO:0003674 molecular_function (ND, dictyBase 2015): ACCEPT, `nd_case: TRUE_GAP`. No literature on this gene product in this species identifies a molecular function; the IBA and IEA rows do not make the ND stale. I considered INFERABLE. The family and the reaction are clear from orthologs, but the nucleotide is not: the only purified enzyme of this species uses GTP, the A-type placement of scsC has moderate support, and the residue at position 20 does not decide nucleotide use. That is the subcase "the family is known but the specificity is not" of `projects/NO_DATA.md`, which goes with a BIOLOGY knowledge gap. The gap is the first entry of `knowledge_gaps`.
- GO:0004775 ADP-forming activity (IBA from the LUCA node PTN000212531, IEA from the HAMAP rule, Rhea and EC): ACCEPT both. The target is inside the clade that inherits the term and outside the loss node. There is no target-specific evidence of loss or divergence. The reason states that the activity is unassayed here and that the purified Dictyostelium enzyme uses GTP.
- GO:0005524 ATP binding and GO:0000287 magnesium ion binding (IEA): kept as non-core; substrate and cofactor binding that are part of the reaction.
- GO:0046872 metal ion binding (IEA, InterPro): TOO_GENERAL. The term is imprecise on its own and magnesium ion binding is asserted on the gene; the row's own evidence (an ATP-grasp fold signature) does not identify the metal, so MODIFY does not apply (maintainer ruling of 2026-11-14). Same decision as for scsB.
- GO:0003824 catalytic activity (IEA): TOO_GENERAL.
- GO:0006099 tricarboxylic acid cycle (IBA from the LUCA node, IEA) and GO:0006104 succinyl-CoA metabolic process (IBA): ACCEPT. The beta subunit binds succinate and the nucleotide, so it does part of the work of the step.
- GO:0005739 mitochondrion (IBA from PTN000212530, ISS from human SUCLA2 by dictyBase in 2005, IEA): ACCEPT under the root-organelle policy. The claim holds on the target itself (PMID:35602934).
- GO:0005737 cytoplasm (IEA from ARBA00026971): TOO_GENERAL. True of a mitochondrial protein under the GO definition and uninformative next to mitochondrion.
- GO:0042709 succinate-CoA ligase complex (IBA from the LUCA node): ACCEPT, as for scsB. The row's evidence stops at the nucleotide-neutral complex, and scsC has no row for a nucleotide-specific complex. No NEW row for GO:0009361 succinate-CoA ligase complex (ADP-forming) is proposed, and `core_functions.in_complex` uses GO:0042709: no measurement shows an ADP-forming complex that contains scsC. The scsB review names the GDP-forming complex in its core function because the enzyme-level assays agree with it; there is no such agreement for scsC.
- NEW GO:0005759 mitochondrial matrix (IC): see the section above. scsA and scsB carry the same proposed row.

## Curation gaps (not knowledge gaps)

- GOA has no experimental mitochondrion row for Q55AI5, although PMID:35602934 supplies high-throughput evidence that dictyBase could annotate (for scsA, scsB and scsC). All three were reference proteins of that study.
- scsC carries a no-data annotation for molecular function and scsB carries none, although neither subunit has been assayed.
- The family review of PTHR11815 describes SF1 as "ADP-forming where assayed (S. cerevisiae, animal SUCLA2)" and does not say that the Dictyostelium member is unassayed while the only enzyme data from that species are for a GTP-using preparation.
- The transit peptide of the UniProt record (1..17, from HAMAP MF_03220) is not anchored to a measurement. It is not reported as a source defect, because the true cleavage site is unknown.

## Open questions

See `knowledge_gaps` in the review: nucleotide specificity of a defined scsA/scsC heterodimer, whether an scsA/scsC enzyme exists in the cell and what share of the flux it carries, the mature N-terminus and sub-mitochondrial location, and whether scsC has the role in mitochondrial DNA maintenance described for animal SUCLA2.
