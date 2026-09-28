# rum1 (P40380) curation notes

## Identity

- *Schizosaccharomyces pombe* 972h-, SPBC32F12.09, protein p25^rum1 / Rum1 ("replication uncoupled from mitosis").
  230 aa, predicted ~25 kDa. PE 1 (evidence at protein level).
- Domain: Rum1 (IPR062409 / PF30839), a lineage-specific family. The only CKI in fission yeast
  [PMID:32361273 "In the core of this G1 arrest lies the only CKI in fission yeast, Rum1, and the anaphase-promoting complex/cyclosome (APC/C) activator Ste9."].
- Not related in sequence to metazoan Cip/Kip (p27/p21); it is the functional homologue of budding-yeast Sic1, with
  limited sequence similarity confined to an ~80-residue cyclin-binding/CDK-inhibitory region
  [PMID:9472012 "we have mapped the cyclin interacting domain and Cdk inhibitory domain to a region of about 80 amino acids in p25rum1 that has significant homology to the C-terminal domain of p40SIC1"].
  UniProt FT: residues 67-147 "CDK inhibitory and cyclin-binding"; 101-230 "Required for activity as a cdc2 kinase inhibitor";
  three MobiDB-lite disordered regions (1-25, 43-118, 188-230).
- UniProt FUNCTION summary: regulator of G1 progression; inhibitor of the cdc2 mitotic kinase; determines the length of
  pre-Start G1; prevents mitosis in early G1; required for pheromone-induced G1 arrest; adapter promoting cdc13 proteolysis
  in G1; degraded at G1/S after phosphorylation by cig1-associated cdc2. SUBUNIT: interacts with cdc13, cig2 and pop1.
  IntAct: cdc13 (NbExp=5), cdc2 (2), cig2 (2). SUBCELLULAR LOCATION: nucleus (PMID:16823372).
- Phosphosites (UniProt MOD_RES): Thr58, Thr62 by cdc2 (PMID:9430640); Thr13, Ser19 by MAPK (PMID:12135491).
  MUTAGEN T58A/T62A: stabilised protein, small colonies with elongated cells (G1 delay), polyploidisation.

## Core biology

### Molecular function: stoichiometric inhibitor of Cdc2-B-cyclin complexes

- Founding biochemistry: [PMID:8521500 "p25rum1 from the fission yeast S. pombe is shown to act as a specific in vitro inhibitor of the p34cdc2/p56cdc13 mitotic kinase."]
- Direct interaction with the holoenzyme: [PMID:8598285 "Biochemical experiments indicate that Ruml potently inhibits Cdc2 phosphorylation of histone H1 or a Cdc18 fusion protein by directly interacting with the Cdc2/cyclin B complex."]
  (note the OCR-style "Ruml" spelling in the cached abstract).
- Cyclin selectivity (from the deep-research synthesis of the 1995 Cell paper): 2.6 nM Rum1 completely inhibited Cdc13-associated
  kinase, reduced Cig2-associated activity by ~60 %, and did not inhibit Cig1-associated kinase even at 26 nM
  [file:SCHPO/rum1/rum1-deep-research-falcon.md "In vitro, 2.6 nM Rum1 completely inhibited Cdc13-associated kinase, reduced Cig2-associated activity by about 60%, and did not inhibit Cig1-associated activity even at 26 nM."].
  Consistent with [PMID:9430640 "The CDK-cyclin complex cdc2-cig1, which is insensitive to p25(rum1 )inhibition, seems to be the main kinase that phosphorylates p25(rum1)."]
- Binding is to the cyclin subunit: [PMID:9303310 "In vitro binding data indicate that p25rum1 has specificity for the B-cyclin p56cdc13 component of the CDK and can bind the cyclin even in the absence of the cyclin destruction box."]
  and it binds both B-cyclins in vivo: [PMID:9614176 "it binds both cdc13p and cig2p and is specifically required for cdc13p proteolysis"].
- Bacterially produced Rum1 is fully active, i.e. no activating modification is needed
  [PMID:9614176 "Bacterially produced rum1p is fully active as an inhibitor of cdc13p–cdc2p kinase ( Correa-Bordes and Nurse, 1995 )"].
- Family-level statement: [PMID:9472012 "p25rum1 and p40SIC1 are specific inhibitors of p34(cdc2/CDC28) kinase complexes with B-type cyclins that play a central role in the regulation of the G1 phase of the cell cycle."]

### G1 function: Start timing, size control, ordering of S and M

- Discovery paper: [PMID:8121488 "It influences three aspects of G1 regulation: determination of the length of G1, dependence of S phase upon completion of mitosis, and restraint of mitosis until G1 is finished."]
- Pre-Start form of Cdc2: [PMID:7593289 "Here we present genetic data suggesting that rum1 maintains p34cdc2 in a pre-Start G1 form, inhibiting its activity until the cell achieves the critical mass required for Start, and find that in the absence of rum1 p34cdc2 has increased Start activity in vivo."]
- Size threshold (PomBase's basis for GO:0031568): [PMID:9552380 "In opposition to these cyclins the rum1 inhibitor, a protein present exclusively in G1, prevents premature activation of the cdc2/cig2 and the cdc2/cdc13 complexes until cells have reached the critical cell size required to pass Start and initiate a new cell cycle."]
- Anti-mitosis safeguard in G1: [PMID:8521500 "early G1 cells contain p25rum1, which associates with and inhibits the mitotic kinase, and maintains p56cdc13 mitotic B cyclin at a low level, ensuring that these cells do not undergo a premature lethal entry into mitosis"].
- Re-replication on overexpression (the "rum" phenotype): [PMID:8521500 "A high level of p25rum1 in G2 cells inhibits the p34cdc2/p56cdc13 kinase that removes the block preventing a further S phase and leads to repeated rounds of DNA replication."]
  Mechanistically via Cdc18: [PMID:8598285 "Overexpression of Ruml under conditions that promote re-replication of the genome induces a striking accumulation of Cdc18 protein by a largely post-transcriptional mechanism."]
  and Sic1 does the same, arguing that it is a CDK-level effect: [PMID:8598285 "Overexpression of SIC1, an unrelated cyclin-dependent kinase inhibitor from budding yeast, causes a similar accumulation of Cdc18 and also leads to re-replication."]
- Genetic link to Cdc18: [PMID:8598285 "We found that the ruml+ gene efficiently suppresses the lethality of a conditional cdc18 mutant."]

### Cdc13 destruction in G1

- [PMID:9303310 "Here we show that p25rum1 associates with the CDK p34cdc2/p56cdc13 during G1 in normally cycling cells and is required for the rapid proteolysis of p56cdc13."]
- Cyclosome (APC/C) dependence and Rum1 specificity for Cdc13 (not Cig2):
  [PMID:9614176 "Proteolysis of both cig2p and cdc13p B-cyclins in pheromone was shown to require the cyclosome by the lack of proteolysis in cells defective for the nuc2p cyclosome subunit (Figure 5 )."]
  [PMID:9614176 "rum1p mediates cdc13p turnover, whereas cig2p turnover can occur in a rum1 -independent manner, indicating that rum1p is specifically required for cdc13p degradation by the cyclosome"]
- The adaptor model is explicitly a proposal: [PMID:9614176 "We propose that rum1p acts as an adaptor targeting cdc13p for degradation by the cyclosome."]
  The 2020 model instead routes the effect through CDK inhibition relieving Ste9 phosphorylation:
  [PMID:32361273 "As Rum1 accumulates, this eventually results in the sustained inactivation of CDK complexes."]
  [PMID:32361273 "either the deletion of rum1 or the mutation of the B56 binding motif impairs the dephosphorylation of Ste9 to a similar extent"].
  Either way Rum1 positively regulates APC/C-dependent Cdc13 destruction; the specific term GO:1905786 is also used by PomBase for srw1/ste9.

### Pheromone- and starvation-induced G1 arrest, mating

- [PMID:9614176 "Here we show that rum1 + is required for this pheromone-induced G1 arrest."]
- [PMID:9614176 "rum1p is required to maintain this G 1 arrest and specifically inhibits the cdc13p-cdc2p kinase"]
- Not confined to pheromone: [PMID:9614176 "the rum1 function is not confined to pheromone response, being required in other situations with a prolonged G 1 phase, such as the extended G 1 in a wee1–50 mutant or after nitrogen starvation"]
- rum1 null cells are sterile because they cannot arrest in G1: [PMID:9614176 "mutants such as rum1 Δ and nuc2–663 that fail to arrest in G1 under mating conditions are sterile"].
- Nutrient coupling via mRNA stability (UniProt INDUCTION, PMID:14653990, not cached).

### Regulation of Rum1 itself (substrate side)

- Periodic accumulation: [PMID:9430640 "p25(rum1) begins to accumulate at anaphase, persists in G1 and is destroyed during S phase."]
- Phosphodegron: [PMID:9430640 "Phosphorylation of p25(rum1 )by cdc2-cyclin complexes at residues T58 and T62 is important to target the protein for degradation."]
  [PMID:9430640 "Mutation of one or both of these residues to alanine causes stabilization of p25(rum1) and induces a cell cycle delay in G1 and polyploidization due to occasional re-initiation of DNA replication before mitosis."]
- Kinase: Cdc2-Cig1 [PMID:9303310 "the rapid disappearance of p25rum1 requires the activity of the CDK p34cdc2/cig1p and that this same CDK phosphorylates p25rum1 in vitro"].
- E3: SCF-Pop1/Pop2 (Cdc4-like F-box/WD40) [PMID:9203581 "We propose that Pop1 functions as a recognition factor for Rum1 and Cdc18, which are subsequently ubiquitinated and targeted to the 26S proteasome for degradation."]
  [PMID:9653157 "Cells lacking sud1(+) accumulate high levels of Cdc18 and the CDK inhibitor Rum1, because they cannot degrade these two key cell cycle regulators."]
  [PMID:32361273 "Under rich conditions, phosphorylation of Rum1 leads to its degradation by the SCFPop1/Pop2 (Skp1-Cullin1-F-box)"].
- MAPK phosphorylation of Thr13/Ser19 reduces inhibitory potency without abolishing binding
  [PMID:12135491 "phosphorylation of p25(rum1) by MAPK revealed markedly reduced Cdc2 kinase inhibitor ability of the protein"].
- PP2A-B56^Par1 counteracts CDK phosphorylation and stabilises Rum1 during nitrogen starvation; Rum1 carries two
  candidate LxxIxE SLiMs flanking T58/T62 and binds Par1 directly in vitro
  [PMID:32361273 "Rum1 comprises two potential PP2A-B56-SLiMs."]
  [PMID:32361273 "the interaction between Par1 and Rum1 was much stronger (Figure 6C)"]
  [PMID:32361273 "Therefore, we conclude that Rum1 is the most likely a direct substrate of PP2A-B56Par1."]
  and the rum1 BM1AA (I42A E44A) motif mutant phenocopies par1 deletion
  [PMID:32361273 "this mutant failed to accumulate Rum1 in the cell, even though the mRNA levels were similar to those of the WT strain"].

### Localisation

- Nucleus by genome-wide YFP tagging (HDA) [PMID:16823372 "we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein"];
  UniProt SUBCELLULAR LOCATION cites the same study, and the IEA (GO_REF:0000044) row is derived from it.
- The deep-research report notes that the endogenous protein is too scarce for quantitative imaging and treats localisation
  as unresolved; the nuclear assignment is nonetheless consistent with Rum1's nuclear CDK targets and nuclear SCF-mediated turnover.

## Curation decisions

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0004861 CKI activity (x6) | EXP/IDA 8521500, 8121488, 8598285, 9303310, 9430640, 9552380 | ACCEPT | Core MF; direct in vitro inhibition of Cdc2-Cdc13 (and partial Cdc2-Cig2). 9552380 is a review that summarises the group's primary data. |
| GO:0005515 with cdc13 (9303310, 9472012, 9614176) | IPI | MODIFY -> GO:0030332 cyclin binding | Rum1 binds the B-cyclin subunit; the cyclin-interacting region is mapped. |
| GO:0005515 with cig2 (9614176) | IPI | MODIFY -> GO:0030332 | Direct binding shown by Stern & Nurse; Cig2-Cdc2 partially inhibited. |
| GO:0005515 with cdc2 (9303310) | IPI | MODIFY -> GO:0019901 protein kinase binding | Association with the Cdc2 holoenzyme; the functional consequence is GO:0004861 (same paper). |
| GO:0005515 with par1 (32361273) | IPI | MODIFY -> GO:0019903 protein phosphatase binding | SLiM-mediated docking of PP2A-B56; substrate-side regulatory input, non-core. |
| GO:0005634 nucleus | HDA 16823372; IEA GO_REF:0000044 | ACCEPT | ORFeome YFP localisation; the IEA row is the UniProt SubCell mapping of the same result. |
| GO:0007089 traversing start control point | IMP 8121488 | MODIFY -> GO:2000134 | GO:0007089 is_a GO:1900087 positive regulation of G1/S transition; Rum1's contribution to Start is inhibitory. PomBase also annotates the negative regulator par1 to this term, so this is a term-placement issue flagged in suggested_questions rather than a curation error. |
| GO:0031568 G1 size-control checkpoint signaling (x3) | IMP 8121488, 9552380; EXP 9614176 | ACCEPT | PomBase's term for the pre-Start G1 delay, also used for cdc2, cig2, wee1, srw1 and par1. GO:0000751 (pheromone G1 arrest) has no PomBase annotations, so the pheromone row is kept under the same convention. |
| GO:0032436 positive regulation of proteasomal Ub-dependent catabolic process | EXP 9614176 | MODIFY -> GO:1905786 | The proteolysis is explicitly cyclosome (APC/C)-dependent; PomBase uses GO:1905786 for srw1/ste9. |
| GO:0045930 negative regulation of mitotic cell cycle | IDA 9303310 | ACCEPT | General but apt for the G1 restraint of the mitotic kinase (mitosis from G1 is not a G2/M transition); G1/S aspect covered by GO:2000134. |
| GO:1903464 negative regulation of mitotic cell cycle DNA replication | IMP 8521500 | ACCEPT | Abstract shows the re-replication gain-of-function; the negative-regulation statement reflects the pre-Start restraint of CDK-driven S phase. Curator had full text. |
| GO:1903467 negative regulation of mitotic DNA replication initiation | IDA 11937031 | ACCEPT | Abstract does not mention Rum1 (presumably used as the CDK inhibitor showing Cdc2-dependence of Drc1 phosphorylation); biology is correct, deferred to curator. |
| GO:2000134 negative regulation of G1/S transition (x4) | IGI 7593289 (cdc2); IMP 8521500, 8598285, 9430640 | ACCEPT | Core BP. |

## Open questions

- Is the Cdc13-destruction effect direct (adaptor to APC/C) or indirect (CDK inhibition -> Ste9 dephosphorylation)? No
  in vitro reconstitution exists; the 2020 data favour the indirect route.
- GO:0007089 sits under positive regulation of G1/S; should PomBase's use of it for negative regulators (rum1, par1) be
  re-examined, or should the term be moved to a neutral parent?
- Exact stoichiometry/structure of the Rum1-Cdc13-Cdc2 complex is unknown (no structure; three disordered regions).

## Comparators

- yeast/SIC1 (complete review): same actions on GO:0004861, MODIFY of bare protein-binding rows, ACCEPT of G1/S rows.
- human/CDKN1B (complete review): MODIFY protein binding -> cyclin binding (GO:0030332) for cyclin partners and
  -> protein kinase binding (GO:0019901) for CDK partners; this review follows the same pattern.
- modules/g1_s_transition.yaml cites rum1 as the fission-yeast CKI exemplar (SCF-dependent CKI destruction).
