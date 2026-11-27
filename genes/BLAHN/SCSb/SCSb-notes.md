# SCSb (Blastocystis sp. subtype 1, strain ATCC 50177 / NandII, UniProtKB:B3FHP0) notes

Started 2026-11-18, as a follow-up to the evolutionary reviews of the succinyl-CoA synthetase (SCS) beta family PTHR11815 and alpha family PTHR11117.

## Terms used in these notes

- SCS: succinyl-CoA synthetase (succinate--CoA ligase), an alpha/beta enzyme.
- MLO / MRO: mitochondrion-like or mitochondrion-related organelle, the names the Blastocystis literature uses for its double-membrane organelle.
- ASCT: acetate:succinate CoA-transferase.
- Position 20: residue 20 of the mature beta subunit (Gln in pig GTP-specific SCS, Pro in E. coli SucC). Mature numbering of B3FHP0 is precursor numbering minus 14.
- Gatekeeper lysines: Lys46 and Lys114 of the mature subunit, at the entrance of the nucleotide site.
- A daughter and G daughter: the two clades below the PANTHER duplication node PTN000212530 (human SUCLA2 and human SUCLG2).

## Summary

- SCSb encodes the 416-residue precursor of the beta subunit of the Blastocystis SCS. The recombinant alpha/beta enzyme is ATP-specific, with no detectable activity with GTP, in two independent studies of the same strain (PMID:18452512, PMID:27478903).
- The subunit has Gln at position 20, which was expected to mark GTP specificity. In crystal structures of the nucleotide-binding domain Gln20 hydrogen-bonds the adenine base (PMID:31282474, abstract).
- The alpha subunit was located in the organelle by confocal microscopy. The beta subunit was not detected: both antibodies failed. Its location is inferred from a predicted presequence, the alpha subunit and the co-purifying complex (PMID:18452512).
- Blastocystis has no complete tricarboxylic acid cycle. The proposed role of SCS is ATP formation from succinyl-CoA made by ASCT. That role has not been measured in the organism.
- There is no mutant, knockdown or inhibitor study of the gene.

## UniProt record (entry SUCB_BLAHN, sequence version 1)

- Reviewed entry, protein existence level 1. Its only reference is PMID:18452512. The seven PDB entries of PMID:31282474 (6NO0 to 6NO6, residues 16-253) are cross-referenced, but that paper is not cited as a reference.
- [file:BLAHN/SCSb/SCSb-uniprot.txt "KM=68 uM for ATP {ECO:0000269|PubMed:18452512};"]
- [file:BLAHN/SCSb/SCSb-uniprot.txt "Reaction=succinate + ATP + CoA = succinyl-CoA + ADP + phosphate;"]
- [file:BLAHN/SCSb/SCSb-uniprot.txt "SUBCELLULAR LOCATION: Hydrogenosome {ECO:0000269|PubMed:18452512}."] with the note [file:BLAHN/SCSb/SCSb-uniprot.txt "Note=Found in the matrix of the mitochondrion-like organelles (MLO) of"]. The words "matrix" and "lumen" do not occur in the cached full text of PMID:18452512, and the paper never calls the organelle a hydrogenosome (checked by text search of publications/PMID_18452512.md; supplementary figures not read).
- The FUNCTION comment says the enzyme [file:BLAHN/SCSb/SCSb-uniprot.txt "functions in the citric acid cycle"] and carries PubMed:18452512 as experimental evidence beside the HAMAP rule MF_03219. The paper says the opposite for this organism (below).
- Features: TRANSIT 1..14 (predicted), CHAIN 15..416, ATP, Mg(2+) and substrate binding residues from the HAMAP rule, and two SITE features at 60 and 128, "Important for substrate specificity", from PMID:18452512 by curator inference. No transmembrane or signal feature.
- Residue numbering, checked against the sequence in the record: Gln34 is "Gln20" of the mature subunit; Lys60 and Lys128 are "Lys46" and "Lys114"; Val127 is "Val113"; Leu241 is "Leu227". PMID:18452512 names the two lysines by the pig numbering, as replacements of [PMID:18452512 "Glu 42 β to Lys and Asp 110 β to Lys"]. Arg13 is two residues before the predicted cleavage site.
- Family cross-references: PANTHER PTHR11815:SF10 (label "SUCCINATE--COA LIGASE [GDP-FORMING] SUBUNIT BETA, MITOCHONDRIAL", which is wrong for this ATP-specific member; the family review already records that SF10 is the root subfamily and holds ADP-forming members), Pfam PF08442 ATP-grasp_2 and PF00549 Ligase_CoA.

## Literature search (2026-11-18)

`just deep-research BLAHN SCSb --provider perplexity` failed: "Provider 'perplexity' not available. Available: asta, openscientist, claude_code". No deep-research file exists for this gene. The search below was done by hand in PubMed; query and number of hits:

- `Blastocystis succinyl-CoA synthetase`: 6 (PMID:33174373, PMID:31282474, PMID:27478903, PMID:18757809, PMID:18694756, PMID:18452512)
- `Blastocystis AND (succinate thiokinase OR "succinate-CoA ligase" OR "succinyl CoA synthetase" OR SCS)`: the same 6
- `(SCSb OR "SCS beta" OR "SCS-beta" OR "succinyl-CoA synthetase beta") AND Blastocystis`: 1 (PMID:18694756)
- `Blastocystis AND (ATP-specific OR "nucleotide specificity" OR gatekeeper)`: 4 (PMID:33174373, PMID:31282474, PMID:27478903, PMID:18452512)
- `Blastocystis AND ("acetate:succinate CoA-transferase" OR ASCT OR "tricarboxylic acid cycle" OR "substrate-level phosphorylation")`: 4 (PMID:31282474, PMID:18757809, PMID:18452512, PMID:18403202)
- `Blastocystis AND (mitochondrion-like organelle OR mitochondria-related organelle OR hydrogenosome) AND (proteome OR metabolism OR biochemical)`: 10, of which PMID:18757809, PMID:18694756 and PMID:18403202 were used
- `Blastocystis[Title] AND genome[Title]`: 6, of which PMID:21439036 (subtype 7 genome) and PMID:28892507 (subtype 1 genome) were searched for SCS

Seven publications were added to the cache with `just fetch-pmid` (27478903, 33174373, 18403202, 21439036 and 28892507 with full text; 18694756 and 18757809 abstract only). PMID:31282474 is abstract only. PMID:18452512 is cached with full text.

Not found: any knockout, knockdown or inhibitor study of SCS in Blastocystis; any direct localisation of the beta subunit in subtype 1; any sub-organellar fractionation; any measurement of flux through SCS in the organism.

## Activity and nucleotide specificity

PMID:18452512 (Hamblin et al. 2008; full text read; strain NandII, the strain of this entry):

- The subunits were expressed without their presequences: [PMID:18452512 "Succinyl-CoA synthetase genes were amplified from cDNA without their targeting sequences for protein expression"]
- Sequence predicted a GTP-specific enzyme: [PMID:18452512 "Primary sequence analysis of the Blastocystis SCS suggested that the enzyme is GTP-specific because of the presence of glutamine at the equivalent position to Gln 20 β in pig GTP-specific SCS"]
- The assay showed the opposite: [PMID:18452512 "the recombinant Blastocystis SCS showed no detectable activity with GTP"] and [PMID:18452512 "The enzyme therefore has specificity for ATP rather than GTP, in contrast to our initial sequence analysis predictions"]
- Kinetics: [PMID:18452512 "The Blastocystis SCS has a KM of 68 μM for ATP"]; [PMID:18452512 "the Blastocystis SCS Kcat is only 133 min−1 in comparison with the E. coli SCS Kcat of 2684 min−1"]
- Conclusion on position 20: [PMID:18452512 "the appearance of Gln at position 20 in Blastocystis SCS coupled with its ATP specificity indicates that it is not this residue that dictates nucleotide specificity"]. The concluding remarks of the paper write "Glu 20" where Gln 20 is meant; that sentence is not quoted anywhere in the review.
- Mechanism proposed from a homology model, docking and molecular dynamics, not from an experiment: [PMID:18452512 "The rim surrounding the binding site in Blastocystis SCS thus acts as an electrostatic gatekeeper that prevents GTP from orienting in the bound conformation."]

PMID:27478903 (Vashisht et al. 2017; full text read; subunits amplified [PMID:27478903 "from Blastocystis hominis strain NandII cDNA"]):

- Second assay of the wild-type enzyme: [PMID:27478903 "The Km of wild-type Blastocystis SCS for ATP was 145 ± 47 μM, and it showed a kcat/Km value of 96 M–1 s–1 but no detectable activity with GTP"]
- Mutagenesis of the gatekeeper lysines: [PMID:27478903 "we have designed a gatekeeper mutant (ED) by changing Lys46 to Glu and Lys114 to Asp in Blastocystis"]; [PMID:27478903 "our gatekeeper mutant enzyme (ED) showed both ATP and GTP specificity but with a clear preference for GTP (Km = 143 ± 17 μM) over ATP (Km = 230 ± 34 μM)"]
- Combined with the binding-site mutant (Val113Leu and Leu227Phe): [PMID:27478903 "a complete reversal of nucleotide specificity was obtained with GTP, but no detectable activity was obtained with ATP"]

PMID:31282474 (Huang et al. 2019; abstract only; crystal structures of residues 16-253, the nucleotide-binding domain without the alpha subunit):

- [PMID:31282474 "The crystal structures show that the enzyme is specific for ADP/ATP because of interactions between the nucleotide and the binding site."]
- [PMID:31282474 "Nucleotide-specificity is provided by hydrogen-bonding interactions between the adenine base and Gln20β, Gly111β and Val113β."]
- [PMID:31282474 "It is the different conformations of the backbone at Gln20β, of the side chain of Gln20β and of the linker that make the enzyme ATP-specific."]
- [PMID:31282474 "Although the K46βE/K114βD double mutant of Blastocystis hominis SCS binds GTP better than ATP according to kinetic assays, only the complex with Mg2+-ADP was obtained."]

The two accounts of the mechanism differ. The kinetic work assigns exclusion of GTP to the two surface lysines; the structural abstract assigns ATP specificity to the binding site. Neither is taken as superseding the other here: the double mutant prefers GTP in kinetics, which the structural paper itself reports, and the full text of the structural paper was not read. The mechanism is recorded as unresolved.

PMID:33174373 (Vashisht et al. 2021) concerns the Plasmodium falciparum beta subunit refolded with the Blastocystis alpha subunit and has no data on B3FHP0. Context only: [PMID:33174373 "electrostatic interactions at the gatekeeper region alone are insufficient to alter the substrate specificity of PfSCS"]

## Complex

- [PMID:18452512 "Affinity purification of the expressed proteins showed the co-purification of the α–β complex"]
- [PMID:18452512 "These results clearly indicate that the two Blastocystis subunits interact as expected"]
- The alpha subunit is B3FHT4 (gene SCSa). The complex was shown with recombinant tagged proteins from E. coli; the native enzyme has not been purified.

## Location

- Prediction: [PMID:18452512 "both predict a mitochondrial localization for both subunits."] (Mitoprot and TargetP).
- Experiment, alpha subunit only, on isolate DMP/02-328, which is subtype 4 while this entry is from subtype 1 strain NandII [PMID:18452512 "Subtyping of Blastocystis sp. DMP/02–328 indicated that this strain is subtype 4 (Stensvold et al., 2007) whereas Blastocystis sp. NandII is subtype 1."], with an antiserum against pig SCS alpha: [PMID:18452512 "Confocal microscopy showed the pig anti-SCSα colocalized with Mitotracker orange, a mitochondrion-specific stain"]
- Beta subunit: [PMID:18452512 "Unfortunately, neither the anti-pig-SCSβ antibody nor the anti-Neocallimastix-SCSβ antibody recognized Blastocystis SCSβ. However, given the presence of a typical targeting signal and the presence of the alpha subunit in the mitochondria, the beta subunit is likely to be localized to the mitochondria as well."]
- The GOA row `GO:0042566 hydrogenosome, EXP, PMID:18452512` on this entry is therefore an inference by the authors, not an assay of this protein. The alpha entry B3FHT4 carries the same row; there the experiment is on the alpha subunit, but of a subtype 4 isolate.
- A second study (abstract only; the abstract does not state the strain): [PMID:18694756 "are located within double-membrane surrounded-compartments known as mitochondria-like organelles (MLOs)."] The sentence lists beta-SCS among the proteins located there by electron microscopy. The abstract does not name the antibody or the sub-compartment.

What kind of organelle it is:

- [PMID:18403202 "The Blastocystis organelles have metabolic properties of aerobic and anaerobic mitochondria and of hydrogenosomes."]
- Mitochondrial characters: cristae, membrane potential, an organellar genome, complexes I and II [PMID:18403202 "an incomplete tricarboxylic acid cycle as well as a mitochondrial genome"].
- Hydrogenosomal character: [PMID:18403202 "iron-only [FeFe] hydrogenase that we show localizes to the organelles"], but [PMID:18403202 "Although at present we have no direct evidence of hydrogen production by the Blastocystis MLOs"]; in subtype 7 organelle fractions [PMID:18757809 "Hydrogenase activity was not detected under the conditions used in this study."]
- [PMID:18694756 "As there is no evidence for hydrogen production by this organism, we suggest that MLOs are more likely anaerobic mitochondria."]
- The SCS paper says of the organelle that it is [PMID:18452512 "unlikely to be a mitosome as per definition"] and otherwise writes "mitochondria-like organelles" and "mitochondria".
- GO has GO:0005739 mitochondrion, GO:0042566 hydrogenosome ("participates in ATP and molecular hydrogen formation"; not a kind or part of mitochondrion) and GO:0032047 mitosome. A QuickGO search on 2026-11-18 found no term for a mitochondrion-related organelle as a class, but the usage comment of GO:0005739 says that gene products in the mitochondrion-related organelles of anaerobic or microaerophilic organisms are to be annotated to GO:0032047 mitosome or GO:0042566 hydrogenosome, and the review it cites lists Blastocystis [PMID:24316280 "mitochondrion-related organelles (MROs), such as mitosomes, hydrogenosomes, and mithochondrion-like organelles"]. UniProt maps "mitochondrion-like organelle" to its subcellular location Hydrogenosome (SL-0145).
- QuickGO, 2026-11-18: experimental annotations to GO:0042566 or GO:0005739 (with descendants) in Blastocystis (taxon 12968 and descendants): two, both hydrogenosome from PMID:18452512, on B3FHP0 and B3FHT4.

Decision (revised in the follow-up of 2026-11-18, to follow the usage comment of GO:0005739 and to agree with the review of the alpha subunit SCSa). The protein is in the organelle; that is not in doubt. GO:0042566 hydrogenosome is used for the core location and both hydrogenosome rows are accepted, because that is the term GO directs for mitochondrion-related organelles that are not mitosomes; the limits are that hydrogen production has not been shown and that the organelle has mitochondrial characters. The TreeGrafter mitochondrion row is marked as over-annotated, not removed. The earlier decision (mitochondrion as core location, hydrogenosome rows non-core, and a suspected term defect asking UniProt to consider mitochondrion) did not consider the usage comment and was withdrawn; the UniProt defect now concerns only the matrix note. No sub-compartment row is added: the presequence is predicted and its cleavage is not shown, and no assay resolves a sub-compartment for either subunit.

## Process

- [PMID:18452512 "suggests that Blastocystis does not use a normal TCA cycle."]
- [PMID:18452512 "our EST analyses indicate that only the latter half of the TCA cycle is present"]
- [PMID:18452512 "The end-product of this pathway is succinate and SCS is not part of this route."] (the route is malate dismutation, which runs from malate to succinate).
- [PMID:18403202 "No ESTs were found corresponding to mitochondrial citrate synthase, aconitase, isocitrate dehydrogenase, or α-ketoglutarate dehydrogenase"]
- Subtype 7 genome: [PMID:21439036 "An incomplete oxidative phosphorylation chain, a partial Krebs cycle, amino acid and fatty acid metabolisms and an iron-sulfur cluster assembly are all predicted to occur in these organelles."]
- Proposed role: [PMID:18452512 "ASCT allows acetyl-CoA to be used as a CoA donor to form succinyl-CoA from succinate. SCS then conserves the high-energy potential of the succinyl-CoA thioester bond by forming ATP from ADP and Pi."]
- [PMID:18452512 "in the absence of a classic mitochondrial electron transport chain, it is likely to be one of the main ATP producing enzymes in this parasite"]
- Expression: [PMID:18452512 "This indicates that SCS is highly expressed and likely plays an important role in the overall metabolism of this parasite."] (from EST abundance).
- Enzyme activities in organelle fractions of subtype 7, not assigned to a gene (abstract only): [PMID:18757809 "which cumulatively are responsible for recycling CoA and generating ATP"]
- The assay of the recombinant enzyme ran toward succinyl-CoA formation; the proposed direction in the cell is the reverse. GO:0006104 succinyl-CoA metabolic process covers both. GO:0006099 tricarboxylic acid cycle is the acetyl-oxidising cycle and is not supported for this organism.
- QuickGO search on 2026-11-18 found no GO term for substrate-level phosphorylation, and none for an ASCT/SCS cycle. No new process annotation is proposed: the shuttle is a proposal for this organism, not a measurement.
- The subtype 1 genome paper (PMID:28892507) was searched for succinyl-CoA synthetase, SCS, ASCT, Krebs and TCA in the cached full text: no hits in the main text.

## Place in the family trees

- B3FHP0 is in the InterPro member list of PTHR11815:SF10 and is not a leaf of the PAINT tree, so it has no IBA rows. Five GOA rows name PANTHER:PTN000212530, the eukaryotic duplication node, in WITH/FROM: the three TreeGrafter rows (GO:0005739, GO:0006104, GO:0042709) and the two combined rows (GO:0004775, GO:0006099). Read here as the node where TreeGrafter grafted the sequence; that reading is inferred from the pattern of the rows, not from TreeGrafter documentation.
- A graft at PTN000212530 is above both daughters and above PTN000929335, where PAINT places the gain of GDP-forming and the loss of ADP-forming activity. B3FHP0 therefore receives neither GO:0004776 nor the NOT annotation for GO:0004775, which agrees with the assays.
- Of the terms it receives, only GO:0005739 has its PAINT origin at PTN000212530; GO:0004775, GO:0006099, GO:0006104 and GO:0042709 originate at the LUCA root PTN000212531 (interpro/panther/PTHR11815/PTHR11815-review.yaml).
- Sequence trees: [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "| Blastocystis B3FHP0 (Gln) | not in tree | with SUCLA2 | 73 / 68 / 59 | outside both |"]. The deep placement is unresolved, and the Gln20 of Blastocystis does not group with the SUCLG2 Gln20 clade.
- The gene's own paper: [PMID:18452512 "only one type of SCSβ was found among the Blastocystis ESTs"] and its trees [PMID:18452512 "fail to resolve the position of Blastocystis within the eukaryotes"].
- Alpha partner B3FHT4 (QuickGO, 2026-11-18): GO:0004775 and GO:0042566 by EXP from PMID:18452512, and TreeGrafter IEAs through PTN000874228 that include GO:0004776 succinate-CoA ligase (GDP-forming) activity, GO:0009361 and GO:0005739. The GDP-forming row on the alpha entry is contradicted by the assays; it is outside this review and is noted for the alpha family review.

## Points for the family reviews

1. The beta family review says no node can be named for B3FHP0. The TreeGrafter graft node PTN000212530 is in the WITH/FROM of its rows.
2. GO:0006099 fails for B3FHP0 and B3FHT4 as it does for the Trichomonas clade. Both are InterPro members and not leaves, so a PAINT loss cannot stop the TreeGrafter and UniRule rows.
3. The Blastocystis localisation experiment was on the alpha subunit only, in a subtype 4 isolate, and the paper does not use the word hydrogenosome for this organelle.
4. PMID:18452512 says of its own trees [PMID:18452512 "In both trees, alpha-proteobacteria are sister to eukaryotes, indicating the mitochondrial ancestry of this protein."] The PANTHER beta tree groups eukaryotes with Archaea. The paper's trees are in supplementary figures that were not read; not adjudicated.
5. PMID:18452512 says several organisms, including "an Aspergillus", [PMID:18452512 "all have two SCSβ isoforms"]. LSC2 RESULTS.md finds almost no SUCLG2-type gene in Dikarya. The Aspergillus statement rests on a supplementary tree that was not read; a lead to check.
6. PMID:18452512 describes E. coli SCS as a case [PMID:18452512 "where both ATP and GTP can bind but GTP is preferred"], and PMID:27478903 writes of [PMID:27478903 "a higher affinity for GTP"]. LSC2 RESULTS.md says E. coli SCS prefers ADP, citing PMID:22751660. Not adjudicated here.
