# SCSa (Blastocystis sp. subtype 1, strain ATCC 50177 / NandII, UniProtKB:B3FHT4) notes

Started 2026-11-18, as a follow-up to the evolutionary reviews of the succinyl-CoA synthetase (SCS) alpha family PTHR11117 and beta family PTHR11815. The partner subunit is reviewed in `genes/BLAHN/SCSb/` (B3FHP0).

## Terms used in these notes

- SCS: succinyl-CoA synthetase (succinate--CoA ligase), an alpha/beta enzyme.
- MLO / MRO: mitochondrion-like or mitochondrion-related organelle, the names the Blastocystis literature uses for its double-membrane organelle.
- ASCT: acetate:succinate CoA-transferase.
- Graft node: the node of the PANTHER tree named in the WITH/FROM column of a TreeGrafter IEA, for a sequence that is not itself a leaf of the tree.

## Summary

- SCSa encodes the 318-residue precursor of the alpha subunit of the Blastocystis SCS. With the beta subunit SCSb (B3FHP0) it forms an enzyme that is ATP-specific, with no detectable activity with GTP, in two independent preparations from the same strain (PMID:18452512, PMID:27478903).
- The alpha subunit also forms an active, ADP-forming enzyme with the beta subunit of Plasmodium falciparum (PMID:33174373). It is the half of the enzyme that does not choose the nucleotide.
- The alpha subunit is the subunit that was located in the cell: an antiserum against pig SCS alpha colocalises with MitoTracker in the organelle of Blastocystis (PMID:18452512). The cells used were a subtype 4 isolate, not the subtype 1 strain of this entry.
- Blastocystis has no complete tricarboxylic acid cycle. The proposed role of SCS is ATP formation from succinyl-CoA made by ASCT. That role has not been measured in the organism.
- No assay of the alpha subunit alone exists (CoA binding, phosphorylation of the active-site histidine), and there is no mutant, knockdown or inhibitor study of the gene.

## UniProt record (entry SUCA_BLAHN, sequence version 1)

- Reviewed entry, protein existence level 1. Its only literature reference is PMID:18452512; the second reference is the genome submission.
- [file:BLAHN/SCSa/SCSa-uniprot.txt "Reaction=succinate + ATP + CoA = succinyl-CoA + ADP + phosphate;"]
- [file:BLAHN/SCSa/SCSa-uniprot.txt "Note=kcat is 133 min(-1) with ATP as substrate."]
- [file:BLAHN/SCSa/SCSa-uniprot.txt "SUBCELLULAR LOCATION: Hydrogenosome {ECO:0000269|PubMed:18452512}."] with the note [file:BLAHN/SCSa/SCSa-uniprot.txt "Note=Found in the matrix of the mitochondrion-like organelles (MLO) of"]. The words "matrix" and "lumen" do not occur in the cached full text of PMID:18452512 (text search of publications/PMID_18452512.md, 0 hits; supplementary figures not read). The word "hydrogenosome" occurs in the paper only in general statements about targeting signals and other organisms, never as the name of the Blastocystis organelle.
- The SUBUNIT comment [file:BLAHN/SCSa/SCSa-uniprot.txt "Heterodimer of an alpha and a beta subunit."] carries only the HAMAP rule MF_03222, although the paper shows co-purification of the two tagged subunits. The stoichiometry is not reported in the paper.
- The FUNCTION comment says the enzyme [file:BLAHN/SCSa/SCSa-uniprot.txt "functions in the citric acid cycle"] and carries PubMed:18452512 as experimental evidence beside the HAMAP rule. The PATHWAY comment places it in the tricarboxylic acid cycle with the same paper as curator inference. The paper says the opposite for this organism (below).
- Features, all from the HAMAP rule or a predictor, none experimental: TRANSIT 1..18, CHAIN 19..318, ACT_SITE 271 (tele-phosphohistidine intermediate), CoA binding at 38..41, 64 and 117..119, substrate binding at 181. No transmembrane or signal-peptide feature.
- Checked against the sequence in the record: residue 271 is His (in the motif GHAGA). Residue 17 is Arg and residue 18 Ala, so with cleavage after residue 18 the Arg is two positions before the site, as the paper says: the leader has [PMID:18452512 "arginine at position −2 from the putative cleavage site"]. The forward primer of the expression construct (methods of the paper) encodes SSTARVW, residues 19 to 25, so the recombinant protein began at residue 19, the first residue of the UniProt CHAIN. The cleavage site itself has not been determined.
- Family cross-references: PANTHER PTHR11117:SF2, NCBIfam TIGR01019 (sucCoAalpha), Pfam PF02629 CoA_binding and PF00549 Ligase_CoA, PROSITE PS01216 and PS00399. The HAMAP cross-reference line names MF_01988, while the evidence tags of the comments name MF_03222.

## Literature search (2026-11-18)

`just deep-research BLAHN SCSa --provider perplexity` failed: "Provider 'perplexity' not available. Available: asta, openscientist, claude_code". No deep-research file exists for this gene. The search was done by hand in PubMed; query and number of hits:

- `Blastocystis succinyl-CoA synthetase`: 6 (PMID:33174373, PMID:31282474, PMID:27478903, PMID:18757809, PMID:18694756, PMID:18452512)
- `Blastocystis AND (succinate thiokinase OR "succinate-CoA ligase" OR "succinyl-CoA ligase" OR SCSalpha OR "SCS alpha")`: 5, all among the six above
- `Blastocystis AND (mitochondrion-related organelle OR mitochondria-like organelle OR hydrogenosome) AND (proteome OR metabolism OR "tricarboxylic acid")`: 17, of which PMID:18757809, PMID:18694756 and PMID:18403202 were used
- `Blastocystis AND (acetate:succinate CoA-transferase OR ASCT OR "substrate-level phosphorylation")`: 3
- `Blastocystis AND ("tricarboxylic acid cycle" OR "Krebs cycle" OR "citric acid cycle")`: 5
- `Blastocystis AND (succinate OR "succinyl-CoA") AND (enzyme OR kinetics OR structure)`: 8 (adds PMID:33163680 and PMID:21790804, not examined)

Depth of reading. PMID:18452512, PMID:27478903, PMID:33174373, PMID:18403202 and PMID:21439036 are cached with full text; the first was read in full and the others were read for the passages on the enzyme, the alpha subunit, the organelle and the cycle. PMID:31282474, PMID:18694756, PMID:18757809 and PMID:24316280 are abstract only. PMID:24316280 was added to the cache for this review with `just fetch-pmid`; the others were already cached. The subtype 1 genome paper (PMID:28892507) has no statement on the enzyme (see the SCSb notes) and is not cited.

Not found: any assay of the isolated alpha subunit; any fractionation of the organelle; any localisation in the strain of this entry; any knockout, knockdown or inhibitor study of SCS in Blastocystis; any measurement of flux through SCS in the organism; any report of the native mass or stoichiometry of the enzyme.

## Activity and nucleotide specificity

PMID:18452512 (Hamblin et al. 2008; full text read; sequences from strain NandII, the strain of this entry):

- The subunits were expressed together without their presequences: [PMID:18452512 "Succinyl-CoA synthetase genes were amplified from cDNA without their targeting sequences for protein expression"]
- [PMID:18452512 "the recombinant Blastocystis SCS showed no detectable activity with GTP, but a rate of 0.028 nmol s−1 with ATP"]
- [PMID:18452512 "The enzyme therefore has specificity for ATP rather than GTP"]
- The assay ran toward succinyl-CoA: [PMID:18452512 "Blastocystis SCS enzyme kinetics measured in the direction of succinyl-CoA formation"]. Formation of ATP was not measured.
- Kinetics: [PMID:18452512 "The Blastocystis SCS has a KM of 68 μM for ATP"]; [PMID:18452512 "the Blastocystis SCS Kcat is only 133 min−1 in comparison with the E. coli SCS Kcat of 2684 min−1"]. The authors note the same drop for recombinant pig enzyme, so the low rate may be a property of the preparation.
- Homology model on pig SCS: [PMID:18452512 "the sequence identities of the alpha and beta subunits were 70% and 49%"]. The alpha subunit is the more conserved of the two.

PMID:27478903 (Vashisht et al. 2017; full text in the cache):

- [PMID:27478903 "SCSα and SCSβ genes were separately amplified from Blastocystis hominis strain NandII cDNA using primers listed in Table S1."]
- [PMID:27478903 "The SCSα subunits of Blastocystis were expressed as a soluble protein and further purified by Ni-NTA affinity chromatography as described previously."] The beta subunit came from inclusion bodies, and both were denatured and refolded together.
- Second assay of the wild-type enzyme: [PMID:27478903 "The Km of wild-type Blastocystis SCS for ATP was 145 ± 47 μM, and it showed a kcat/Km value of 96 M–1 s–1 but no detectable activity with GTP"]
- [PMID:27478903 "The SCSα subunit has the binding site for coenzyme A (CoA), while the SCSβ subunit has the nucleotide binding site."] This is a statement from the model and from other enzymes of the family, not an assay of CoA binding by B3FHT4.
- Every mutation in the paper is in the beta subunit; the alpha subunit is the unchanged partner of each mutant.

PMID:33174373 (Vashisht et al. 2021; full text in the cache):

- [PMID:33174373 "Despite multiple efforts, it was not possible to clone the PfSCSα subunit; hence the Blastocystis SCSα subunit (having >60% identity with PfSCSα) was chosen to generate the refolded PfSCS enzyme."]
- [PMID:33174373 "Refolding of the chimeric subunits (SCSα from Blastocystis and SCSβ from P. falciparum) to a functional enzyme successfully validated that swapping of SCS subunits among different organisms is feasible."]
- [PMID:33174373 "Interestingly, the Blastocystis SCSα subunit did provide the CoA binding site essential for the enzyme activity."] An interpretation by the authors: the chimera is active, and no control without an alpha subunit or assay of CoA binding was found in the text.
- The chimera is ADP-forming, and the specificity follows the beta subunit, here that of P. falciparum. This agrees with the premise of the alpha family review that the alpha subunit is nucleotide-agnostic.

PMID:31282474 (Huang et al. 2019; abstract only) reports structures of the nucleotide-binding domain of the beta subunit. The abstract has nothing on the alpha subunit and is cited only for that fact.

## Complex

- [PMID:18452512 "The pCDF duet vector added a 6XHis tag to the N-terminus of SCSα and a S tag to the C-terminus of SCSβ"]
- [PMID:18452512 "Affinity purification of the expressed proteins showed the co-purification of the α–β complex"]
- [PMID:18452512 "These results clearly indicate that the two Blastocystis subunits interact as expected"]
- [PMID:18452512 "The SCS complex was further purified by size exclusion"]. No native mass or stoichiometry is given, so alpha/beta heterodimer and alpha2/beta2 tetramer are not distinguished. GO:0009361 is defined as a heterodimeric complex.
- The complex was shown with recombinant tagged proteins from E. coli; the native enzyme has not been purified.

## Location

- Prediction: [PMID:18452512 "both predict a mitochondrial localization for both subunits."] (Mitoprot and TargetP).
- Western blot: [PMID:18452512 "This antibody produced a strong cross-reacting band of approximately 32 kDa on a Western blot of Blastocystis whole-cell lysate"]. The legend gives 32.5 kDa against a predicted 31.5 kDa, which is the size of the protein without the presequence (the precursor is 33.4 kDa). This fits a processed protein and does not show processing.
- Microscopy: [PMID:18452512 "Confocal microscopy showed the pig anti-SCSα colocalized with Mitotracker orange, a mitochondrion-specific stain"]
- The cells were not the strain of this entry. Only DNA and cDNA of NandII were used; the lysate came [PMID:18452512 "from strain DMP/02-328"], the methods for the immunolocalisation name the same isolate, and [PMID:18452512 "this strain is subtype 4 (Stensvold et al., 2007) whereas Blastocystis sp. NandII is subtype 1"]. The antiserum was raised against the pig protein. The experimental location row on B3FHT4 therefore rests on the orthologous protein of another subtype detected with a heterologous antiserum.
- The experiment was on the alpha subunit; the antibodies against the beta subunit failed (see the SCSb notes).
- The assay cannot resolve a compartment within the organelle.
- Beta subunit, abstract only, strain not stated in the abstract: electron microscopy places beta-SCS in the organelles [PMID:18694756 "are located within double-membrane surrounded-compartments known as mitochondria-like organelles (MLOs)."]

What kind of organelle it is, and which GO term names it:

- [PMID:18403202 "Blastocystis has mitochondrion-like organelles with cristae, a transmembrane potential and DNA."]
- [PMID:18403202 "Although complexes I and II of the electron transport chain (ETC) are present, we found no evidence for complexes III and IV or F1Fo ATPases."]
- [PMID:18403202 "iron-only [FeFe] hydrogenase that we show localizes to the organelles"], but [PMID:18403202 "Although at present we have no direct evidence of hydrogen production by the Blastocystis MLOs"]; in subtype 7 organelle fractions [PMID:18757809 "Hydrogenase activity was not detected under the conditions used in this study."]
- [PMID:18694756 "As there is no evidence for hydrogen production by this organism, we suggest that MLOs are more likely anaerobic mitochondria."]
- The SCS paper: [PMID:18452512 "Its presence suggests that the organelle is indeed involved in energy metabolism and therefore unlikely to be a mitosome as per definition"]
- GO terms (QuickGO, 2026-11-18): GO:0005739 mitochondrion, "notably the site of tissue respiration"; GO:0042566 hydrogenosome, "A spherical, membrane-bounded organelle found in some anaerobic protozoa, which participates in ATP and molecular hydrogen formation."; GO:0032047 mitosome. There is no term for a mitochondrion-related organelle as a class. Hydrogenosome is not a kind or part of mitochondrion in GO.
- The usage comment on GO:0005739 (QuickGO, 2026-11-18) says that organisms with mitochondrion-related organelles "do not have mitochondria", and: "To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)"
- The review the comment cites lists Blastocystis among those organisms (abstract): [PMID:24316280 "mitochondrion-related organelles (MROs), such as mitosomes, hydrogenosomes, and mithochondrion-like organelles, which are found in a wide range of anaerobic/microaerophilic eukaryotes that include several medically important parasitic protists such as Entamoeba histolytica, Giardia intestinalis, Trichomonas vaginalis, Cryptosporidium parvum, Blastocystis hominis"]. The misspelling is in the source.

Decision. The protein is in the organelle; that is not in doubt. By GO's own usage comment a location in the organelle of an MRO-bearing organism goes to mitosome or hydrogenosome, and the organelle of Blastocystis makes ATP and has the hydrogenase, so it is not a mitosome. The hydrogenosome rows are therefore accepted, and hydrogenosome is used as the location of the core function. The TreeGrafter mitochondrion row is marked as over-annotated: it is inherited from the eukaryotic node, GO does not class the hydrogenosome under mitochondrion, and the same organelle is already recorded by the experimental row. It is not removed, because the organelle is a mitochondrial derivative with a genome, cristae and complexes I and II, some authors call it an anaerobic mitochondrion, and hydrogen production has not been shown.

This differs from the SCSb review written earlier the same day, which accepts mitochondrion, keeps hydrogenosome as non-core and uses mitochondrion as the core location. That review did not have the usage comment on GO:0005739 or PMID:24316280. Reconciled in the follow-up of 2026-11-18: the SCSb review now marks its mitochondrion row as over-annotated, accepts both hydrogenosome rows and uses hydrogenosome as the core location, as here.

Sub-compartment. No row is added.
- Lines that point to the lumen: a predicted cleavable presequence (prediction; cleavage not shown); a band on the blot at the size of the processed protein; the alpha subunit is soluble when expressed in E. coli (PMID:27478903) and has no predicted transmembrane segment.
- Against adding GO:0034492 hydrogenosome lumen: all of these are indirect, none is a sub-organelle assay, and the root-organelle policy (projects/ORGANELLES.md) covers five organelles and not the hydrogenosome. The Trichomonas alpha subunits carry GO:0034492 from isolation out of purified hydrogenosomes; that is a comparator, not evidence here.
- UniProt's note says matrix and cites the paper with an experimental tag; the paper does not say so. Recorded as a source defect (check requested).

## Process

- [PMID:18452512 "suggests that Blastocystis does not use a normal TCA cycle."]
- [PMID:18452512 "our EST analyses indicate that only the latter half of the TCA cycle is present"]
- [PMID:18452512 "This pathway runs in the opposite direction compared with the TCA cycle and uses fumarate as an electron sink."]
- [PMID:18452512 "The end-product of this pathway is succinate and SCS is not part of this route."]
- [PMID:18403202 "No ESTs were found corresponding to mitochondrial citrate synthase, aconitase, isocitrate dehydrogenase, or α-ketoglutarate dehydrogenase"]
- Subtype 7 genome: [PMID:21439036 "An incomplete oxidative phosphorylation chain, a partial Krebs cycle, amino acid and fatty acid metabolisms and an iron-sulfur cluster assembly are all predicted to occur in these organelles."]
- Proposed role: [PMID:18452512 "ASCT allows acetyl-CoA to be used as a CoA donor to form succinyl-CoA from succinate. SCS then conserves the high-energy potential of the succinyl-CoA thioester bond by forming ATP from ADP and Pi."]
- Enzyme activities in organelle fractions of subtype 7, not assigned to a gene (abstract only): [PMID:18757809 "which cumulatively are responsible for recycling CoA and generating ATP"]
- Expression: [PMID:18452512 "This indicates that SCS is highly expressed and likely plays an important role in the overall metabolism of this parasite."] (from EST abundance).
- GO:0006099 tricarboxylic acid cycle is defined as the cycle in which the acetyl group of acetyl-CoA is oxidised. It is not supported for this organism. The action is REMOVE, as on the beta subunit: the row is electronic, and the paper on this enzyme, read in full, says the enzyme is outside the route that the remaining enzymes form. The absence of the first half of the cycle rests on transcript and genome surveys, so the source defects ask for a check.
- GO:0006104 succinyl-CoA metabolic process names the metabolite and no pathway or direction. The beta entry carries it as a TreeGrafter IEA; the alpha entry does not, because PAINT has no such term on the alpha tree. Comparator check (QuickGO by gene product and term id, 2026-11-18; the query returns positives): S. cerevisiae LSC1 P53598 carries GO:0006104 by IDA (PMID:9874242), S. pombe O13750 by ISS, Dictyostelium scsA P36967 by TAS, yeast LSC2 P53312 by IDA and IBA, B3FHP0 by IEA; E. coli SucD P0AGE9 and human SUCLG1 P53597 do not. So alpha subunits do carry the term, on the strength of an assay of the enzyme. The alpha subunit does part of the work of the reaction (it binds CoA and carries the phosphohistidine), so the participation test is met. Proposed as a NEW row with the assay of PMID:18452512.
- Looked up and not proposed: GO:1901289 succinyl-CoA catabolic process (direction in the cell not measured), GO:0006754 ATP biosynthetic process (ATP formation by this enzyme not measured), GO:0019413 acetate biosynthetic process (ASCT makes the acetate). GO has no term for substrate-level phosphorylation or for the ASCT/SCS cycle.

## Place in the family tree

- B3FHT4 is in the InterPro member list of PTHR11117:SF2 [file:interpro/panther/PTHR11117/PTHR11117-entries.csv "B3FHT4,Succinate--CoA ligase [ADP-forming] subunit alpha"] and is not a leaf of the PAINT tree, so it has no IBA rows. Its five PANTHER-derived rows name PANTHER:PTN000874228 in WITH/FROM, read here as the node where TreeGrafter grafted the sequence.
- PANTHER tree service (`treeinfo?family=PTHR11117`, read 2026-11-18): PTN000874228 is a speciation node labelled Alveolata-Stramenopiles with 7 leaves (Plasmodium falciparum Q8IIR8; Paramecium tetraurelia A0DYX8, A0CWN3, A0DQC4, A0BIZ5; Thalassiosira pseudonana B8C013; Phytophthora ramorum H3G957). Path from the root: PTN008961318 > PTN000122012 (LUCA) > PTN008512606 (Eubacteria) > PTN004231559 (horizontal transfer) > PTN000122014 (Eukaryota) > PTN007487682 (Bikonts) > PTN008316325 (SAR/HA supergroup) > PTN000874228.
- No PAINT annotation sits at PTN000874228. The terms come from the two origin nodes above it: [file:interpro/panther/PTHR11117/PTHR11117-paint.tsv "PTHR11117	PTN000122012	GO:0004776	F	IBD	false"], likewise GO:0004775, GO:0006099 and GO:0009361 at PTN000122012, and [file:interpro/panther/PTHR11117/PTHR11117-paint.tsv "PTHR11117	PTN000122014	GO:0005739	C	IBD	false"].
- GO:0004776 succinate-CoA ligase (GDP-forming) activity. The node placement is defensible for the family (alpha family review): an alpha subunit contributes to GDP-forming activity where its genome supplies a GDP-accepting beta subunit. Blastocystis does not: [PMID:18452512 "only one type of SCSβ was found among the Blastocystis ESTs"], and the enzyme made with that subunit has no detectable activity with GTP in two preparations. The family review already lists B3FHT4 as a member exception. A PAINT loss cannot stop this row, because B3FHT4 is not a leaf.
- None of the seven leaves below the graft node has an assayed enzyme that I know of; the P. falciparum enzyme (beta subunit with the Blastocystis alpha subunit) is ADP-forming (PMID:33174373). I did not look for the P. falciparum alpha leaf's partner data beyond that paper.
- Same-genome entries: UniProt also has unreviewed A0A196S6H2 (403 aa) and A0A196SK01 (211 aa) for taxon 478820 in PTHR11117. They were not aligned here; no claim about a paralog is made.

## Points for the family reviews and the coordinator

1. Graft node. The alpha family review says of B3FHT4 that "no PAINT node is named". The TreeGrafter graft node is PTN000874228 (Alveolata-Stramenopiles, 7 leaves), below PTN000122014. PTN000874228, PTN007487682 and PTN008316325 are not yet in the family review or in the LSC2 results file.
2. GO:0004776 exception. A second preparation (PMID:27478903) confirms no detectable activity with GTP, and the chimera of PMID:33174373 shows the Blastocystis alpha subunit working with a foreign beta subunit whose specificity the enzyme takes. Both strengthen the member exception; the family review cites only PMID:18452512.
3. GO:0006099. The term fails for B3FHT4 and B3FHP0 as for the Trichomonas clade, and for Blastocystis the full text states it. Neither is a leaf, so a PAINT loss cannot stop the TreeGrafter and UniRule rows.
4. GO:0005739. B3FHT4 receives mitochondrion as a TreeGrafter IEA through the eukaryotic node. The usage comment on GO:0005739 directs locations in mitochondrion-related organelles to hydrogenosome or mitosome, and the review it cites lists Blastocystis. The family review mentions B3FHT4 under this node only as "not a leaf".
5. The localisation in PMID:18452512 was done on a subtype 4 isolate with an antiserum against the pig protein. The family review's wording "located in a mitochondrion-like organelle in PMID:18452512" is accurate for the organism and not for the NandII protein itself.
6. Inconsistency, since reconciled in favour of this review (follow-up of 2026-11-18): the SCSb review originally accepted GO:0005739 and kept GO:0042566 as non-core; this review accepts GO:0042566 and marks GO:0005739 as over-annotated, because of the GO usage comment, which the SCSb review did not consider.
7. Not a knowledge gap, recorded here: GO has no grouping term for mitochondrion-related organelles; TreeGrafter IEAs on grafted sequences are outside the reach of PAINT losses.
