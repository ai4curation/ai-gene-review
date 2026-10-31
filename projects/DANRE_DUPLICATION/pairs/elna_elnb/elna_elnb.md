---
title: "elna / elnb"
autolink_gene_symbols: false
---

# elna / elnb

[Back to pairs](../README.md)

**Bottom line:** MIXED. At the expression level this is a clean, well-established
partition: elnb is restricted to the teleost-specific bulbus arteriosus (BA) in three
teleosts, while elna keeps the broad expression of the single elastin of a
non-teleost fish. At the protein level, one rescue experiment suggests that elnb
also innovated: neither elna nor Polypterus eln mRNA rescues loss of elnb.
Recent work locates the new property in the material, not in a new kind of activity:
Elnb makes the BA matrix unusually soft. The expression partition is established. The
protein-level innovation is supported by one lab's non-rescue data and by sequence
divergence, and has not been tested by a cross-rescue driven from the elnb locus.

| | elna | elnb |
|---|---|---|
| UniProt | A0A8N1TQS2 (1164 aa; RefSeq NP_001073532) | A0A8M1NAS7 (2020 aa; RefSeq NP_001041529) |
| Human ortholog | ELN (PANTHER: least-diverged ortholog) | ELN (PANTHER: ortholog) |
| Review | [genes/DANRE/elna](../../../../genes/DANRE/elna/elna-ai-review.yaml) | [genes/DANRE/elnb](../../../../genes/DANRE/elnb/elnb-ai-review.yaml) |

**Accession note.** Both reviewed entries are unreviewed TrEMBL records, one of
several isoform entries per gene. They are the entries backed by the RefSeq NP
proteins. They are not the accessions in the PANTHER row (A0A8M6YT25 and
A0A8M6Z3N0). A0A8M6Z3N0 is a 2104-aa XP-backed elnb isoform, and a UniProt REST
lookup of A0A8M6YT25 on 2026-09-27 returned no record. The elnb entry (2020 aa) is
also shorter than the 2,041-aa full-length protein described in the mutant paper
[PMID:41712646 "compared to the full-length 2,041-amino acid protein in wild-type fish"].
These differences come from alternative exon usage in highly repetitive genes. They do
not affect the GO review, but the identity figure below depends on which isoforms are
compared.

## 1. Evidence the pair comes from the TGD

**PANTHER** (row in `panther_tgd_pairs.tsv`): call `unresolved`, duplication branch
`Teleostei|DANRE`, pair class 1:1, family PTHR24018 (ELASTIN). There are 0 gar
co-orthologs, because the PANTHER tree has no gar eln gene. There are 2 medaka
co-orthologs, and the medaka copies are also duplicated (`medaka_parallel_dup = yes`).
Without a gar gene PANTHER cannot place the duplication on the `Neopterygii|Teleostei`
branch. The medaka pattern is the same one that the `TGD_likely_parallel` rule
treats as supporting the TGD.

**The literature settles the TGD origin.** There are three lines of evidence:

- *Gene phylogeny with an outgroup.* Moriyama et al. placed the duplication after the
  gar split
  [PMID:26783159 "The resultant phylogenetic tree showed that elna and elnb were duplicated after the split of the spotted gar"].
- *Co-duplicated neighbours (synteny).* Because elastin is repetitive and hard to align,
  the same study used the flanking gene limk1. Its paralogs lie next to elna and elnb and
  were also duplicated after the gar split
  [PMID:26783159 "This led to the identification of LIM domain kinase (limk) 1a and 1b genes as neighbours of elna and elnb, respectively"]
  [PMID:26783159 "Taken together, these results indicate that genomic locus including eln and limk1 genes was duplicated in the 3R WGD."]
  The two zebrafish copies lie on chromosomes 15 and 21 in conserved synteny with
  human and mouse
  [PMID:35216218 "The elna and elnb zebrafish paralogs are located on different chromosomes (chr), chr 15 and chr 21, respectively, but they share conserved synteny among them and with their human and mouse orthologs"].
- *Genome survey.* A survey of 51 jawed fishes found one eln in every non-teleost
  genome, and elna plus elnb in teleosts, all in a conserved eln–septin–limk1 block
  [PMID:41465165 "All non-teleost genomes contain a single eln gene, whereas duplicated elna and elnb genes were found in teleosts"]
  [PMID:41465165 "All genomes examined were shown to contain a syntenic block comprising eln, septin4/septin5 and limk1"].
  The survey includes the gar, bowfin and bichir proteins
  [PMID:41465165 "the ray-finned species spotted gar, bowfin and gray bichir exhibited mainly KP domains"].

**What is established:** the duplication happened after teleosts split from holosteans
and before the zebrafish–medaka split, it involved a whole genomic block (eln plus
limk1), and a single eln exists in gar. That is the TGD signature. The PANTHER
`unresolved` call is an artefact of the gar gene being absent from the PANTHER tree.
**Not established:** no formal gar-bridge double-conserved-synteny analysis for this
locus was found. At least one early-branching teleost (tarpon) appears to have lost
elnb
[PMID:41465165 "except for the missing tarpon (Megalops cyprinoides) elnb linked to septin5 and limk1 on chromosome 3"].

## 2. Protein-level comparison

- **Identity.** A global alignment gives 33.4% identity over 2082 columns
  (annotation-comparison.md). For two long, low-complexity, glycine-rich elastins this
  figure is inflated by composition and should be read with caution. Needle alignments
  against human elastin show the asymmetry more clearly: Elna is about 37% identical to
  human ELN, and Elnb only about 18%
  [PMID:35216218 "They share approximately 37% identity and 41% similarity, whereas for Elnb, around 18% identity and 21% similarity were calculated."].
  Elna and Elnb are further apart from each other than Elna is from mammalian elastin
  [PMID:35216218 "The difference between Elna and Elnb is also very important, being even less close between each other than Elna and tropoelastins from both human and mouse"].
  PANTHER also marks elna as the least-diverged ortholog of ELN.
- **Domain architecture.** This is conserved in both copies: alternating hydrophobic and
  crosslinking domains and the crosslinking motifs
  [PMID:16982180 "All tropoelastins shared a predominant and characteristic alternating domain arrangement, as well as the fundamental crosslinking sequence motifs."].
  Elnb is larger
  [PMID:35216218 "Elna and Elnb are respectively 101 kilodaltons (kDa) with 57 exons and 173kDa with 59 exons"],
  has longer hydrophobic domains
  [PMID:35216218 "hydrophobic domains of Elnb are larger on average than those of other tropoelastins"],
  and is less hydrophobic overall than other fish and tetrapod elastins
  [PMID:41465165 "showed no significant difference with the tetrapods examined, except for the lower hydrophobicity of teleost ElnB"].
  The duplicated-exon block is present in both copies
  [PMID:17628459 "exons 20-31 in both zebrafish elastins"].
- **Biochemical and functional comparison.** No purified-protein comparison exists. The
  only protein-level test is in vivo rescue of an elnb morphant. elnb mRNA rescues it,
  but elna mRNA does not
  [PMID:26783159 "In contrast to this, injection of elnb MO and elna full-length mRNA did not rescue the elnb morphant phenotype"],
  and neither do two isoforms of Polypterus eln
  [PMID:26783159 "both of these Polypterus eln mRNAs did not rescue the elnb morphant phenotype"].
  The material property that differs is stiffness: Elnb confers the BA's low stiffness
  [PMID:41712646 "we demonstrate that the teleost-specific extracellular matrix gene elastin b confers the uniquely low stiffness of the BA"].

**Does each copy keep the ancestral molecular function?** At the level GO can express,
yes. Both are tropoelastins that make elastic matrix. elna keeps the ancestral-like
sequence. elnb makes a different kind of elastic matrix: softer, and more viscoelastic
[PMID:26783159 "with BA elastin showing a decreased elastic modulus and increased viscoelasticity"]. That is a quantitative change in a
material property, not a change in kind of activity.

## 3. Expression

- **Ancestral state.** Polypterus, a non-teleost with a myocardial conus instead of a
  BA, has one broadly expressed eln
  [PMID:26783159 "As expected, Polypterus had one elastin gene, and its expression was observed in various tissues including OFT, which is similar to that of zebrafish elna"].
  The BA itself is found only in teleosts
  [PMID:26783159 "only teleost species have BA"].
- **Zebrafish.** Both genes are expressed in most elastic tissues (head cartilage,
  outflow tract, ventral aorta, swim bladder wall). elnb (eln2) predominates in the BA
  [PMID:17112714 "In general, both genes were expressed and their gene products deposited in most of the elastic tissues examined, with the notable exception of the bulbus arteriosus in which eln2 expression and its gene product was predominant."]
  and is induced more strongly
  [PMID:17112714 "the upregulation of eln2 was much stronger than that of eln1"].
  By in situ hybridization, elnb starts in the BA at 3 dpf, while elna is broad
  [PMID:26783159 "In contrast, elna was expressed not only in the BA but also other tissues, such as the cranial skeleton and swim bladder"].
  elnb is the earliest, exclusive BA marker
  [PMID:39460530 "We have identified that elnb is the earliest, exclusive marker of the bulbus arteriosus"].
  In adults, elna is the prevalent elastin in the heart valves
  [PMID:37408270 "elastin a seems to be the prevalent isoform expressed in this specific structure"].
- **Other teleosts.** The pattern is conserved in medaka and stickleback
  [PMID:26783159 "We found that elnb expression patterns were restricted to the BA, while elna was observed in various tissues in both medaka"].
  In rainbow trout (which has two elna copies from the salmonid duplication) elnb is
  enriched in the bulbus
  [PMID:41465165 "the bulbar expression of elnb was 15 times higher than the ventricular levels in juvenile fish"].
  The partition is not absolute, however: the trout elna copies are also bulbus-enriched
  [PMID:41465165 "The expression of elna1 and elna2 was also significantly higher in the bulbus, and together their transcript levels were almost similar as the elnb levels."].

**Shared vs copy-specific.** Most elastic tissues are shared, with elna broader. The BA
is dominated by elnb, and the valves are dominated by elna. elna's breadth matches the
ancestral (Polypterus) state. elnb's restriction is derived, and its BA domain is new
because the organ is new.

## 4. Experimental evidence of function

**elnb**

- *Morphants* (translation-blocking MO) have a hypoplastic BA with less elastin
  [PMID:26783159 "The elnb morphants exhibited severe hypoplasia of the BA and decreased elastin accumulation, while elna morphants exhibited no obvious defect in BA morphology"],
  and ectopic cardiomyocytes in the BA
  [PMID:26783159 "Such ectopic cardiomyocyte formation in the BA was observed only in elnb morphants and not in elna morphants."].
  The contraction duration of the BA is also strongly reduced
  [PMID:26783159 "Elnb is likely a major contributor to BA elasticity"].
- *CRISPR embryos* (2016, apparently F0, screened by T7 assay) reproduced the ectopic
  cardiomyocytes
  [PMID:26783159 "We observed ectopic cardiomyocytes in the BA of elnb genetic mutant embryos similar to those of morpholino knockdown embryos"].
- *Germline mutant* (2026): the allele is a premature stop in exon 2, so it is a
  PTC/NMD-type allele
  [PMID:41712646 "This elnb mutant carries a premature stop codon that results in a truncated 81-amino acid Elnb protein"].
  The phenotype is more severe than in morphants
  [PMID:41712646 "Homozygous elnb mutants exhibited a more severe hypoplastic BA than elnb morphants and developed ectopic cardiomyocytes in the BA"],
  and the BA never develops its low stiffness
  [PMID:41712646 "Notably, this developmental decrease in extracellular stiffness in the BA was not observed in elnb mutant"].
  Stiffening the BA mechanically is sufficient to phenocopy the mutant
  [PMID:41712646 "this manipulation led to the formation of ectopic cardiomyocytes in the BA, phenocopying the elnb KD or KO condition"].
- *Rescue:* see section 2. It works with elnb mRNA and fails with elna or Polypterus eln
  mRNA.

**elna**

- *Morphants* have a swim bladder defect
  [PMID:26783159 "elna morphants exhibited a swim bladder defect, where elna expression level is relatively high"],
  a milder reduction of BA deformation that is shared with elnb
  [PMID:26783159 "the averaged contraction deformation distances were significantly reduced in elna and elnb morphant BA cells"],
  and no ectopic cardiomyocytes.
- *Germline mutant* sa12235 (ENU, PTC at Tyr88)
  [PMID:37408270 "This change leads to the loss of a tyrosine (Tyr88) for a stop codon at the very beginning of the protein sequence."].
  Embryos develop normally
  [PMID:37408270 "elnasa12235 embryo survival was not affected during the early stages of development of individuals (from 0 to 7 dpf)"],
  but adults have less valve elastin
  [PMID:37408270 "the valves of elnasa12235/+ and elnasa12235/sa12235 mutants were found to have a markedly diminished quantity of elastin"]
  and shorter lives
  [PMID:37408270 "Heterozygous (elnasa12235/+) and homozygous (elnasa12235/sa12235) mutants were found to have a significantly decreased life expectancy compared with their wild-type siblings."].
  The authors attribute survival to elnb elsewhere
  [PMID:37408270 "as elastin b is still expressed in the vessels and in the bulbus arteriosus"].
  That is an inference, not a test of compensation.

**Not done:** no elna;elnb double mutant, no RNA-less allele of either gene, and no test
of transcriptional adaptation (paralog upregulation) in either PTC mutant.

## 5. Fate classification

**MIXED: expression partition plus protein-level innovation in elnb.**

- *Expression level: PARTITION.* Confidence is high. The single ancestral-type gene is
  broadly expressed. elna keeps the broad domain. elnb became restricted to the BA, and
  this is conserved across zebrafish, medaka and stickleback. The authors themselves
  call this step subfunctionalization
  [PMID:26783159 "one of the two paralogues, elnb, was relaxed from constraints of transcriptional regulation and changed its expression pattern to be restricted to BA (subfunctionalization)"].
  Strictly, this is not a symmetric DDC split. elna lost little, and the BA domain is a
  new organ, so part of elnb's domain is new rather than a subset of an ancestral one.
- *Protein level: INNOVATION in elnb.* Confidence is moderate. The authors conclude
  [PMID:26783159 "These results indicate that the function of elnb is distinct from those of elna and ancestral eln; neofunctionalization likely occurred between these two paralogues."].
  Supporting evidence: the specific non-rescue by both elna and Polypterus eln, the
  greater sequence divergence of Elnb, and the direct stiffness data. Caveats: the
  rescues used ubiquitous mRNA injection into morphants, so protein dose and timing at
  the BA were not controlled; the result comes from a single lab; and the "new function"
  is best described as a changed material property (lower stiffness) of the same kind
  of activity.
- *Not BACKUP.* The copies have different single-mutant phenotypes (BA fate for elnb,
  valves for elna), and cross-rescue failed. *Not DOSAGE* either.

**What would change the call:** if elna coding sequence expressed from the elnb locus
rescued the elnb mutant, the protein-level innovation would collapse to a pure
expression partition (with elnb's divergence then neutral or quantitative). If an
elna;elnb double mutant showed BA or valve defects beyond the singles, that would
reveal partial overlap.

## 6. GO annotation consistency across the pair

From `annotation-comparison.md`:

- **GOA before review.** The two copies were identical: InterPro2GO IEA for
  GO:0005201 extracellular matrix structural constituent and GO:0031012 extracellular
  matrix, plus root ND placeholders. There are no IBA, ISO or experimental rows. PAINT
  has not propagated anything to either copy, and ZFIN has not curated the published
  phenotypes as GO.
- **Kept identical, because the biology is shared.** Both copies get the same changes:
  GO:0005201 MODIFY to GO:0030023 extracellular matrix constituent conferring
  elasticity, GO:0031012 ACCEPT, and the ND placeholders REMOVE. Both copies get NEW
  GO:0071953 elastic fiber and GO:0048251 elastic fiber assembly (elna by the
  sa12235 mutant's loss of valve elastin; elnb by loss of BA elastin). Both proteins make
  elastic matrix. The divergence in stiffness is a quantitative material difference that
  GO has no term for, so it is recorded in the text and not as an MF asymmetry.
- **Copy-specific, because the biology differs.** Only elnb gets NEW GO:0003232 bulbus
  arteriosus development (IMP, germline mutant plus morphant). This is justified by the
  expression partition and by the elnb-specific phenotype: elna morphants have no BA
  morphology defect. Elnb passes the participation test because it is the structural
  matrix whose low stiffness directs BA cell fate. The tetrapod comparator is human ELN,
  which carries GO:0003151 outflow tract morphogenesis (IMP).
- **Deliberately not added.** Valve and swim bladder process terms were not added for
  elna: the valve phenotype is adult degeneration rather than development, and the swim
  bladder phenotype is morphant-only. A smooth-muscle-differentiation term was not
  added for elnb, because Elnb acts on cell fate indirectly through matrix stiffness.
  Any future IBA from PTHR24018 would reasonably give both copies the elastin MF and
  location terms, but should not transfer the BA term.

## 7. Open questions

- Is the protein-level innovation real? This needs an elna CDS knock-in at the elnb
  locus, or a transgene driven by the elnb promoter, in the elnb germline mutant.
- Which Elnb sequence features (longer hydrophobic domains, hybrid domains, lower
  hydrophobicity) produce the low-stiffness matrix?
- Is there transcriptional adaptation? Is elna upregulated in elnb PTC mutants, or elnb
  in elna sa12235 mutants? What do elna;elnb double mutants show?
- How general is the partition? In trout the elna copies are also bulbus-enriched,
  and icefish lack bulbar elastin
  [PMID:41465165 "The crucial role played by ElnB in the development of bulbus seems to be absent in Antarctic icefish, lacking bulbar elastin"].
- Is elnb lost in tarpon, and if so, how is its BA built?

## References

- PMID:16982180, Chung et al. 2006 (two zebrafish tropoelastins; abstract only)
- PMID:17112714, Miao et al. 2007 (differential expression; abstract only)
- PMID:17628459, He et al. 2007 (comparative genomics of elastin; abstract only)
- PMID:26783159, Moriyama et al. 2016 (phylogeny, synteny, knockdown, rescue; full text)
- PMID:35216218, Hoareau et al. 2022 (review: sequence comparison, synteny)
- PMID:37408270, Hoareau et al. 2023 (elna sa12235 mutant)
- PMID:39460530, zebrafish arterial valve development, Cardiovasc Res 2025 (elnb as BA marker)
- PMID:41465165, Andersen & Østbye 2025 (eln genes in 51 jawed fishes; trout)
- PMID:41712646, Matsuki et al. 2026 (elnb germline mutant; BA stiffness)
- [annotation-comparison.md](annotation-comparison.md);
  PANTHER row from `../../panther_tgd_pairs.tsv`
