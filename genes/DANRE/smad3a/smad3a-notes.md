# smad3a notes (Danio rerio, SMAD family member 3a; UniProt Q8AY15)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random sample)

**Deep research:** not available for this gene (Edison/Falcon returned 402 Payment Required;
the OpenAI key is invalid). Not attempted, per instructions. No `-deep-research-*.md` file
exists. The literature search below was done by hand (Europe PMC queries "smad3a AND
zebrafish", "smad3b AND zebrafish", "(smad3a OR smad3b) AND (mutant OR morpholino OR
knockout OR crispr) AND zebrafish"; relevant papers cached with `fetch-pmid`).

Accession: Q8AY15 (TrEMBL, 425 aa) holds all 31 GOA rows, including the ZFIN experimental rows.
Paralog: smad3b (Q8AY16). Human ortholog SMAD3 (P84022).

### TGD origin
- PANTHER: `TGD_tree`, Neopterygii|Teleostei, 1:1, PTHR13703 (SMAD); one gar co-ortholog, two
  medaka co-orthologs (projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv).
- Synteny/phylogeny in several teleosts [PMID:27703851 "confirmed that smad3a/3b most likely originated from the teleost-specific WGD"]
- [PMID:27703851 "Teleost SMAD3 genes could be clearly divided into two well-conserved clusters, i.e., smad3a and smad3b, whereas spotted gar SMAD3 occupied a separate clade."]
- Note that the synteny paper considers smad3b the copy in the ancestral neighbourhood
  [PMID:27703851 "Thus, the teleost smad3b gene was more likely to be the ancestor SMAD3 gene and smad3a derived from genome duplication."]
  (In a WGD both copies are equally "ancestral"; this is about which one kept more of the flanking gene order.)

### Protein (my analysis: smad3a-bioinformatics/RESULTS.md)
- smad3a vs smad3b 94.1%; smad3a vs human SMAD3 96.9%; smad3a vs gar SMAD3 (W5N932) 96.3%.
- All annotated functional residues of human SMAD3 conserved in smad3a (Zn site, K40/K41,
  linker phosphosites, K378, SSVS C-terminus). smad3a is the conservative copy; smad3b carries
  most linker changes and S418N.
- Longer smad3b branch in teleosts [PMID:27703851 "Moreover, the branch length of smad3b cluster was longer than smad3a"]
- Human-zebrafish conservation used to model human variants
  [PMID:36926042 "Human and zebrafish smad3a share 97% identify and total conservation of V244 (Figure 3A)."]

### Expression
- Maternal and ubiquitous early [PMID:28687631 "First, we showed that the smad3a gene is maternally expressed, and its transcripts are ubiquitously distributed during early embryonic development"]
- Stronger in new somites [PMID:21159776 "Although smad genes were expressed in most cells, we found that smad3a and smad4 expressions were stronger in the newly formed somites where myf5 was highly expressed."]
- Circadian, unlike smad3b [PMID:29940038 "In contrast to Smad3a, another zebrafish paralog of Smad3, Smad3b, did not show any time- or light-dependent expression pattern"]
- Clock1a controls the smad3a promoter [PMID:28687631 "Mechanistically, Clock1a activates the smad3a promoter via its E-box1 element (CAGATG)."]
- Upregulated in regenerating heart [PMID:33816481 "Similarly, the gene expressions of TGF-β receptors alk5a, alk5b, and cofactor smad3a were also dramatically upregulated in the ablated hearts (Figures 1E–G′)."]
- Bgee: highest in presomitic/paraxial mesoderm, somite, caudal fin, retina (RESULTS.md).
- Dick et al. 2000 cloned "smad3" before smad3b was described
  [PMID:10767528 "while smad3 shows a spatially restricted zygotic expression pattern"]. The
  abstract does not use the a/b names; I infer (not verified) that this is smad3a, since
  smad3b was described as novel in 2002 (PMID:12112463).

### Function
- Dominant-negative forms of each paralog (and Smad2) block mesendoderm induction
  [PMID:18025082 "We generated potent and specific dominant-negative forms of zebrafish Smad2, Smad3a, and Smad3b by mutating multiple amino acids."]
  [PMID:18025082 "Thus, our data reveal that Nodal signaling and mesendoderm induction depend on Smad2/3"]
- smad3a, not smad3b, activates the myf5 promoter when overexpressed; ChIP shows Smad3a on myf5 SBEs
  [PMID:21159776 "Using a luciferase assay to detect myf5 promoter activity when smad2 , smad3a , smad3b , or smad4 mRNAs were overexpressed, we found that excessive smad2 and smad3a showed enhanced myf5 promoter activity but not excessive smad3b or smad4 mRNA."]
  [PMID:21159776 "However, two PCR products with 218 bp containing SBE1 and SBE2 were found in embryos injected with either pHis-Smad3a or pHis-Smad4"]
- smad3a mRNA rescues clock1a morphant mesoderm/scl markers
  [PMID:28687631 "These effects were largely compromised by co-injection of smad3a- mRNA."]
- Constitutively active Smad3a and Smad3b both raise cardiomyocyte proliferation (70% vs 31%)
  [PMID:29196619 "whereas both caSmad3a and caSmad3b expression resulted in a 70% (±18% s.e.m.) and 31% (±12% s.e.m.) increase in EdU incorporation, respectively"]
- Smad3 reporter responds to both; both knockdowns alter neural differentiation
  [PMID:25286120 "Reporter fluorescence is activated in phospho-Smad3 positive cells and is responsive to both Smad3 isoforms, Smad3a and 3b."]
  [PMID:25286120 "Similarly, smad3a and 3b knock-down alter neural differentiation showing that both paralogues play a positive role in neural differentiation."]
- Double knockout needed for an aortic phenotype; DKO viable
  [PMID:42584512 "We found an increased diameter of the ventral aorta in smad3a-/-;smad3b-/- double knockout (smad3a/b DKO) zebrafish larvae"]
  [PMID:42584512 "Smad3a/b DKO survive normally to adulthood"]
  [PMID:40066353 "Since many of the zebrafish ohnologues have redundant functionality, they would need to both be targeted to elicit the desired phenotype in zebrafish, as we experienced for the smad3a/b and smad6a/b genes."]
  Single-mutant phenotypes are not given in the cached text (Vanhooydonck 2026 is abstract only).

### GOA experimental rows: notes
- PMID:28887217 (Eaf1/2) is abstract-only. Two IMP rows carry the eaf1 morpholino
  (ZDB-MRPHLNO-090820-4 resolves to "MO1-eaf1" on ZFIN) in WITH. Could not see which smad3a
  manipulation was scored. Deferred to the curator for TGF-beta signalling; cell-fate terms kept as
  non-core.
- PMID:16890162 (Tob1a) abstract: [PMID:16890162 "Although Tob1a can also inhibit the transcriptional activity of the Nodal effector Smad3, its role in limiting dorsal development is executed primarily by antagonizing the beta-catenin signal."]
  Generic protein binding: removed as uninformative (the interaction is not disputed).
- BMP signaling pathway (ARBA IEA): SMAD3 is a TGF-beta/activin/nodal R-SMAD; marked over-annotated.
