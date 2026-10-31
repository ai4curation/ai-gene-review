---
title: "sox9a / sox9b"
autolink_gene_symbols: false
---

# sox9a / sox9b

[Back to pairs](../README.md)

**Bottom line:** PARTITION (subfunctionalization) at the expression level. The
two copies split the ancestral SOX9 expression domains and developmental roles.
The proteins keep a near-identical HMG box and, as far as has been tested, the
same molecular function. Some domains are still shared and partly redundant (ear,
parts of the craniofacial skeleton and fin). No innovation has been shown: the
copy-specific sox9b roles (pancreaticobiliary ducts, heart, retina) match known
roles of the single mammalian Sox9. No cross-rescue experiment has been done, so
"same protein function" is inferred, not tested.

| | sox9a | sox9b |
|---|---|---|
| UniProt | Q9DFH2 | Q9DFH1 |
| Human ortholog | SOX9 | SOX9 |
| Review | [genes/DANRE/sox9a](../../../../genes/DANRE/sox9a/sox9a-ai-review.yaml) | [genes/DANRE/sox9b](../../../../genes/DANRE/sox9b/sox9b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER row** (`panther_tgd_pairs.tsv`, PANTHER v19):

| tgd_call | duplication_branch | pair_class | family | family_name | gene_a | gene_b | human_orthologs_a | human_orthologs_b | gar_coorthologs | gar_a | gar_b | medaka_coorthologs | medaka_parallel_dup |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TGD_or_lineage | Teleostei\|DANRE | 1:1 | PTHR45803 | SOX100B | sox9a | sox9b | SOX9(LDO) | SOX9(O) | 1 | 1 | 1 | 1 | (empty) |

- **What the tree says.** PANTHER places the duplication on the
  `Teleostei|DANRE` branch. Both copies share one spotted gar co-ortholog and one
  medaka co-ortholog, and there is no parallel medaka duplication. On the tree
  alone, this cannot tell a TGD with loss of one medaka copy from a
  zebrafish-only duplication.
- **Medaka has two copies after all.** Medaka does have two Sox9 genes; the
  second was cloned later, and mapping supports co-orthology:
  [PMID:15818483 "Sequence analysis, phylogenetic data, linkage mapping as well as expression pattern all together suggest that the medaka Sox9a and Sox9b are co-orthologs."]
  So PANTHER's single medaka co-ortholog more likely reflects gene-model or tree
  resolution than true loss.
- **Synteny (zebrafish).** The two zebrafish loci lie on duplicated chromosome
  segments:
  [PMID:11180959 "Genetic mapping showed that these two loci reside on chromosome segments that were apparently duplicated in a large-scale genomic duplication event in ray fin fish phylogeny."]
- **Phylogeny and synteny across teleosts.** A larger study found separate
  Sox9a and Sox9b clades, only in teleosts:
  [PMID:27196604 "An exclusive Sox9 phylogeny was generated and clearly showed three main clades, corresponding to Sox9, Sox9a and Sox9b, and only the teleost species exhibited the duplicate copies"]
  and
  [PMID:27196604 "We observed Sstr2 as the common genetic marker of the Sox9 single and duplicate copies in all the vertebrate groups analyzed, and Rasd1 and Adap1 as the specific markers of Sox9a and Sox9b in almost all the teleost groups analyzed."]
- **Established:** the pair came from a teleost-lineage duplication. Duplicated
  syntenic segments are shared across teleosts, and two copies are present in
  zebrafish, medaka and stickleback.
- **Not established here:** a gar-bridge (double-conserved synteny) analysis of
  this locus. The cached literature has no gar SOX9 expression or synteny study.

## 2. Protein-level comparison

- **Identity.** 61.3% overall identity (annotation-comparison.md). A region-wise
  analysis (`genes/DANRE/sox9a/sox9a-bioinformatics/RESULTS.md`) found:
  - the HMG box is 98.6% identical between Sox9a, Sox9b and human SOX9;
  - divergence lies mainly C-terminal to the HMG box (52.3% identity between the
    copies there);
  - Sox9b is 55 aa shorter than Sox9a and more diverged from human SOX9 (56.8%
    vs 70.2% overall);
  - both copies keep the same extreme C-terminus.
- **Domains.** Both have Sox_N and the HMG box (UniProt/InterPro) and are in the
  same PANTHER subfamily (PTHR45803:SF1).
- **Biochemistry.** Both bind DNA and carry a transactivation domain:
  - [PMID:11180959 "Both Sox9a and Sox9b proteins bind to the HMG consensus DNA sequences in vitro."]
  - [PMID:11180959 "We tested different domains for transactivation potential and identified a potential activation domain located in the middle of both Sox9a and Sox9b."]
- **Shared target in vivo.** Both copies regulate the same cartilage target
  where they are expressed:
  [PMID:19210963 "After the sox9 gene duplication event, regulatory elements controlling the expression of sox9 co-orthologs apparently partitioned in a tissue-specific fashion, but the Sox9 proteins encoded by sox9a and sox9b retained the ability to regulate col11a2, presumably by binding to regulatory sites for the col11a2 gene."]
- **Candidate sites of protein divergence.** Coevolution analysis points to the
  dimerization and transactivation domains:
  [PMID:27196604 "We also suggest that DIM and TADs are candidates for functional modulation and variability of the Sox9 single and duplicate copies (Sox9a and Sox9b) in vertebrates"]
  This is a sequence-based hypothesis, not a measured difference.
- **Not tested.** No cross-rescue (sox9a coding sequence in the sox9b domain, or
  the reverse) and no quantitative side-by-side transactivation assay. Both
  copies are inferred to keep the ancestral molecular function; there is no
  evidence that either copy lost it.

## 3. Expression

- **Distinct, with overlap.** The two patterns are distinct but overlap in
  places:
  - [PMID:11180959 "During embryogenesis, sox9a and sox9b expression patterns are distinct but overlap in some regions of the brain, head skeleton, and fins."]
  - [PMID:11180959 "In the adults, sox9a is expressed in many tissues including brain, muscle, fin, and testis, whereas sox9b expression is restricted to previtellogenic oocytes of the ovary."]
- **Together they cover the mammalian pattern.** The sum of the two patterns
  resembles the single-copy mouse gene:
  [PMID:19210963 "The expression patterns of sox9a and sox9b overlap in some regions and are gene-specific in other domains, and the sum of their expression patterns is similar to the mouse Sox9 expression pattern"]
- **Pharyngeal arches.**
  [PMID:19210963 "wild-type pharyngeal arches express both sox9a and sox9b, with sox9a in the mesenchyme and sox9b in the epithelium"]
- **Pectoral girdle.** Mainly sox9a:
  [PMID:19210963 "In the wild-type pectoral apparatus, sox9a is expressed strongly in the scapulocoracoid of the pectoral girldle but was weaker in the blade of the fin bud and did not appear in the cleithrum of the pectoral girdle."]
- **Gonad.** Expression is complementary:
  [PMID:15939378 "testes expressed amh and sox9a, but not cyp19a1a, while ovaries expressed cyp19a1a and sox9b, but not amh."]
- **Digestive organs.** sox9b only:
  [PMID:22719264 "As in wild-type, sox9a expression appears to be excluded from the digestive organs in sox9bfh313 mutants, suggesting that sox9a expression does not compensate for the reduction of Sox9b function in these mutants."]
- **Heart.** sox9b is expressed in the myocardium:
  [PMID:23775563 "In these experiments, it was apparent that sox9b is expressed in myocardial cells, especially in the ventricle."]
- **Hindbrain glial progenitors.** Both copies:
  [PMID:20023158 "although sox9a was delayed relative to sox9b , both genes were expressed in rhombomere centres"]
- **Different upstream regulation in the otic region.**
  [PMID:12668634 "Expression of sox9a but not dlx3b, dlx4b or sox9b requires Fgf3 and Fgf8."]
- **Other teleost lineages.** Stickleback and medaka comparisons disagree on
  *when* the partition happened:
  - Stickleback vs zebrafish: [PMID:14579386 "Most expression domains appear to have been partitioned between Sox9a and Sox9b before the divergence of stickleback and zebrafish lineages, but some ancestral expression domains were distributed differentially in each lineage."]
  - Medaka vs zebrafish: [PMID:15818483 "We conclude that Sox9 regulatory subfunctions were not partitioned before divergence of the teleosts and evolved to lineage-specific expression domains."]
  Both agree that the split is partly lineage-specific.
- **Pre-duplication state.** No gar or other non-teleost fish expression data are
  cached. The "ancestral" pattern is therefore inferred from mouse, which is
  itself a derived single-copy state.

## 4. Experimental evidence of function

**sox9a**
- **Alleles.** Classic *jellyfish* alleles are an ENU splice-site mutation and a
  retroviral insertion into the DNA-binding domain:
  [PMID:12397114 "A retrovirus insertion into sox9a disrupted its DNA-binding domain."]
- **Phenotype.** Cartilage differentiation and condensation morphogenesis fail:
  [PMID:12397114 "These studies show that jef (sox9a) is essential for both morphogenesis of condensations and overt cartilage differentiation."]
- **Glia.** Required in the hindbrain; sox9b partly compensates:
  [PMID:20023158 "residual expression of glial markers in these mutants is probably due to the sox9b co-orthologue, which has an overlapping expression profile."]
- **Heart.** Not required:
  [PMID:23775563 "Knock down of sox9a expression did not cause cardiac malformations, or defects in epicardium development."]
- **Retina.** Not required:
  [PMID:19210963 "In contrast, sox9a mutant retinas had no obvious defects, even though sox9a is expressed in the inner nuclear layer at 68 hpf"]

**sox9b**
- **Allele caveat.** The original b971 allele is a multi-gene deletion:
  [PMID:22719264 "the chromosomal deletion which underlies the b971 lesion removes eleven other genes, greatly limiting the use of this allele to study the function of Sox9b."]
  b971 phenotypes were supported by morpholino phenocopy:
  [PMID:19210963 "Because the morpholino knock down of sox9b phenocopies the sox9b971 defects, the phenotype observed in sox9b971 at this developmental stage is due solely to loss of sox9b function"]
  The later point mutant fh313 truncates the protein before the HMG box (a PTC
  allele) and confirms the ductal roles:
  [PMID:22719264 "Strikingly, sox9b(fh313) homozygous mutants survive to adulthood and exhibit cholestasis associated with hepatic and pancreatic duct proliferation, cyst formation, and fibrosis."]
- **Endocrine progenitors.**
  [PMID:22537488 "Finally, we show that sox9b is essential for endocrine cell formation from the pancreatic ducts and for beta cell regeneration."]
- **Heart.**
  - [PMID:23775563 "Furthermore, sox9b is required for PE, epicardium, and valve formation."]
  - A cardiomyocyte-restricted dominant-negative construct was also used:
    [PMID:30224706 "We generated a dominant-negative sox9b (dnsox9b) to inhibit sox9b target gene expression and used the Gal4/UAS system to drive dnsox9b specifically in cardiomyocytes."]
    A truncated HMG-box dominant negative could also block Sox9a, so this
    experiment alone does not show copy specificity. The morpholino data above do.
- **Retina.**
  [PMID:19210963 "Considering the expression pattern of sox9b, the expression of candidate genes in sox9b mutants, and the phenotype observed in the retina of sox9b mutants, we conclude that sox9b is essential for retinal development."]
- **Dosage sensitivity.**
  [PMID:18784347 "Loss of a single copy of the sox9b gene in sox9b(+/-) heterozygotes increased sensitivity to jaw malformation by TCDD."]
- **Conflicting cartilage result.** A 2021 CRISPR study (Lin et al.,
  *Aquaculture and Fisheries*, doi:10.1016/j.aaf.2019.12.009) is not indexed in
  PubMed or Europe PMC. It is known here only through the deep-research summary
  (`genes/DANRE/sox9b/sox9b-deep-research-falcon.md`), and has not been verified
  from the paper itself. That summary reports that sox9b frameshift mutants had
  grossly normal maxillary, mandibular and pectoral-fin cartilage. This conflicts
  with the b971 and morpholino cartilage phenotypes. Possible explanations are
  transcriptional adaptation in PTC alleles, the extra genes removed by b971
  (including sox8), and phenotypes (chondrocyte number) that gross staining would
  miss. These remain untested.

**Double mutants and redundancy**
- **Additive or synergistic.**
  [PMID:15689370 "The double mutant phenotype is additive or synergistic."]
- **Ear.** [PMID:15689370 "Ears are somewhat reduced in each single mutant but are mostly absent in the double mutant."]
- **Chondrocytes.** Each copy has its own role:
  [PMID:15689370 "Chondrocytes failed to stack in sox9a mutants, failed to attain proper numbers in sox9b mutants and failed in both morphogenetic processes in double mutants."]
- **Otic placode**, together with dlx3b/dlx4b:
  [PMID:12668634 "These cells fail to form if sox9b function is also blocked."]
- **No cross-regulation or compensation found.** Overexpressing Sox9b did not
  change sox9a levels:
  [PMID:27565026 "However, over expression of neither full length nor truncated Sox9b affected sox9a expression levels"]
  and sox9a is not induced in sox9b mutant digestive organs (quote in section 3).
  Neither result tests transcriptional adaptation in the CRISPR alleles
  specifically.

## 5. Fate classification

**PARTITION (subfunctionalization), at the expression level.** Confidence:
moderate to high for partition as the dominant fate. Low for any claim about
protein-level divergence.

**Evidence for partition**
- The authors of the key double-mutant study reached this conclusion:
  [PMID:15689370 "Analysis of mutant phenotypes strongly supports the interpretation that ancestral gene functions partitioned spatially and temporally between Sox9 co-orthologs."]
- Each copy has single-mutant phenotypes in its own domains:
  [PMID:15689370 "Distinct subsets of the craniofacial skeleton, otic placode and pectoral appendage express each gene, and are defective in each single mutant."]
- Together, the two expression patterns approximate that of mouse Sox9 (section 3).

**Why not innovation**
- The sox9b-only roles (pancreaticobiliary ducts, heart valves/epicardium,
  retina) are all known SOX9 roles in mammals, so they are partitioned ancestral
  functions, not new ones. For the ducts, sox9b was chosen because it mirrors
  mouse Sox9:
  [PMID:22719264 "We first show that zebrafish sox9b recapitulates the expression pattern of mouse Sox9 in the pancreaticobiliary ductal system"]
- Oocyte-restricted adult expression of sox9b could be a lineage-specific
  domain. Without gar data it cannot be called neofunctionalization.

**Why not backup or dosage**
- Single mutants of each copy have strong, non-overlapping phenotypes.
- Redundancy is limited to overlap domains (ear, some craniofacial and fin
  elements). There it is positively supported by double-mutant synergy, not
  inferred from mild single mutants.
- The TCDD heterozygote result shows that sox9b dosage matters in the jaw. This
  is dosage sensitivity within a partitioned domain, not dosage retention of the
  whole pair.

**Level of the claim**
- **Expression level:** established.
- **Protein level:** not established. The HMG box is conserved and the two
  copies share col11a2 regulation (section 2), but divergence outside the HMG box
  (larger in Sox9b) is untested.

**What would change the classification**
- A failed cross-rescue: sox9a coding sequence failing to replace sox9b in
  ducts or heart would add a protein-level component (MIXED).
- Gar expression data showing sox9b domains (e.g. oocyte) absent from the
  pre-duplication gene would add innovation for those domains.
- Confirmation that CRISPR sox9b nulls have normal cartilage because of paralog
  upregulation would make the cartilage domain a case of compensatory
  redundancy.

## 6. GO annotation consistency across the pair

See [annotation-comparison.md](annotation-comparison.md).

- **Kept consistent (shared biology):**
  - Molecular function: RNA polymerase II cis-regulatory DNA binding and
    DNA-binding transcription factor activity (IBA, ACCEPT on both).
  - Nucleus.
  - Chondrocyte differentiation and positive regulation of chondrocyte
    differentiation (IBA, ACCEPT on both).
  - Cartilage development (IMP, ACCEPT on both).
  - Otic vesicle and placode formation, inner ear development (KEEP_AS_NON_CORE
    on both).
  - Embryonic pectoral fin morphogenesis (both).
  - Negative regulation of transcription and morphogenesis of an epithelium (IBA,
    KEEP_AS_NON_CORE on both).
  - The same NEW term, GO:0001228 DNA-binding transcription activator activity,
    RNA polymerase II-specific, is proposed for both copies from one paper that
    assayed both proteins (PMID:11180959). The shared molecular function is thus
    annotated identically.
- **Justified asymmetries (expression partition):**
  - sox9b only: pancreas development and hepaticobiliary system development
    (ACCEPT, copy-specific core), endocrine pancreas and type B cell
    differentiation, heart valve / proepicardium / epicardium, retina, and liver
    regeneration (MODIFY from the generic "regeneration" to GO:0097421).
  - sox9a has none of these annotations, and the evidence supports that absence
    (no sox9a expression in digestive organs; no cardiac or retinal phenotype
    after sox9a loss).
  - sox9a only: cartilage morphogenesis (jellyfish stacking phenotype) and
    astrocyte differentiation. These rest on sox9a being the copy that was tested.
    Chondrocyte stacking is genuinely sox9a-specific. Gliogenesis may be shared,
    since sox9b is expressed in the same progenitor domains.
- **IBA propagation:**
  - PAINT propagates heart development (PTN002910118) to both copies. The only
    zebrafish donor is sox9b, and sox9a knockdown had no cardiac effect.
    Therefore: KEEP_AS_NON_CORE on sox9b, MARK_AS_OVER_ANNOTATED on sox9a (with a
    propagation_review of functional divergence / tissue mismatch). This is the
    expected failure mode of IBA for a partition-fate pair: correct at the
    ancestral node, over-applied to the copy that lost the domain.
  - Oligodendrocyte differentiation (IBA) likewise has sox9a as donor. It is kept
    on sox9b as non-core because sox9b is co-expressed in glial progenitor
    domains and there is no evidence of loss.
- **Artefacts of which copy was studied:**
  - Chromatin binding (IDA, ChIP of tagged Sox9a) is on sox9a only, but it
    reflects a shared HMG-box property.
  - The Ewsa "protein binding" IPI on sox9a used a commercial anti-SOX9
    antibody. The copy precipitated is uncertain, and the annotation was removed
    as uninformative.
  - Pigment-cell annotations on sox9b (melanocyte, iridophore; b971 allele,
    abstract-only paper) were left UNDECIDED.
  - Cytoplasm on sox9a was marked over-annotated: the cited evidence concerns
    nuclear retention of unspliced transcript, not protein location.

## 7. Open questions

- **Cross-rescue.** Does Sox9a protein expressed from sox9b regulatory elements
  rescue sox9b-specific duct, heart and retina phenotypes? This is the missing
  test of protein-level equivalence.
- **Conflicting cartilage alleles.** Why do CRISPR sox9b frameshift alleles
  reportedly spare gross cartilage while b971 and morphants do not? Is sox9a or
  sox8 upregulated in the PTC alleles (transcriptional adaptation)?
- **Ancestral state.** What is the expression of the single gar SOX9, which would
  give a true pre-duplication reference? In particular, does it cover the
  oocyte-restricted sox9b adult domain?
- **Protein-level divergence.** Is the C-terminal divergence in Sox9b (the
  transactivation region) functionally significant, e.g. for transactivation
  strength or partner choice?

## References

All quotes above are checked with `scripts/check_quotes.py` against the cached
`publications/PMID_*.md` files. Other sources:

- Gene reviews: `genes/DANRE/sox9a/sox9a-ai-review.yaml`, `genes/DANRE/sox9b/sox9b-ai-review.yaml`.
- Region identity analysis: `genes/DANRE/sox9a/sox9a-bioinformatics/RESULTS.md`.
- Annotation table: `annotation-comparison.md` (generated).
- Deep research: `genes/DANRE/sox9a/sox9a-deep-research-falcon.md` and
  `genes/DANRE/sox9b/sox9b-deep-research-falcon.md`. These are the only source
  for the Lin et al. 2021 CRISPR result, which has no PMID.
