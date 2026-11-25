---
title: "col1a1a / col1a1b"
autolink_gene_symbols: false
---

# col1a1a / col1a1b

[Back to pairs](../README.md)

**Bottom line:** DOSAGE, with a minor expression partition. The duplicate did become a
distinct subunit of the same complex: col1a1b encodes the teleost alpha3(I) chain,
which is built into type I collagen alongside alpha1(I) (col1a1a) and alpha2(I). But
no evidence shows that alpha3(I) adds a property that alpha1(I) lacks. The two
chains are co-expressed almost everywhere and occur at about equal amounts in adult
bone, skin and scales. Genetically they behave as partly interchangeable doses of
one "alpha1-like" chain: either single heterozygote is normal, but the double
heterozygote has fragile bones. The split is asymmetric. col1a1a is dose-limiting
(its null is lethal) and alone supplies the fin-fold actinotrichia, while col1a1b
is dispensable (its null is viable), evolves faster, and has been lost in several
teleost lineages. The expression and genetic facts are established. That alpha3(I)
is a quantitatively supplementary chain, and not a functional innovation, is an
inference from the absence of any copy-specific phenotype or property.

| | col1a1a | col1a1b |
|---|---|---|
| UniProt | Q6U1J5 (1447 aa; RefSeq NP_954684) | Q6PEI9 (1449 aa; RefSeq NP_958886) |
| Chain | alpha1(I) | alpha3(I) (teleost-specific; synonym col1a3) |
| Human ortholog | COL1A1 (literature; the PANTHER table lists COL3A1, see section 1) | COL1A1 (literature; the PANTHER table lists COL3A1) |
| Review | [genes/DANRE/col1a1a](../../../../genes/DANRE/col1a1a/col1a1a-ai-review.yaml) | [genes/DANRE/col1a1b](../../../../genes/DANRE/col1a1b/col1a1b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER** (row in `panther_tgd_pairs.tsv`): call `TGD_tree`, duplication branch
`Neopterygii|Teleostei`, pair class 1:1, family PTHR24023 (COLLAGEN ALPHA). There is
1 gar co-ortholog, shared by both copies, and there are 2 medaka co-orthologs, with no
parallel medaka duplication. This is the strongest PANTHER call: one gar gene, and the
duplication placed after the gar split and before the zebrafish–medaka split. The
table's `human_orthologs` column gives COL3A1 for both copies, not COL1A1. We read
this as a quirk of PANTHER's orthology assignment within the large fibrillar collagen
family: both the literature phylogeny and the synteny place the pair with COL1A1
(below). It has no bearing on the TGD call.

**Literature.**

- *Phylogeny.* The cloned zebrafish alpha3(I) groups with alpha1(I), consistent with
  a duplication in the ray-finned fish genome duplication
  [PMID:14738308 "Results obtained with the newly isolated sequences of the zebrafish showed that the alpha3(I) chain is phylogenetically close to the alpha1(I) chain and support the hypothesis that the alpha3(I) chain arose from a duplication of the alpha1(I) gene."]
  [PMID:14738308 "The duplication might occur during the duplication of the actinopterygian genome, soon after the divergence of actinopterygians and sarcopterygians"].
  Trout sequences give the same answer
  [PMID:11358497 "Finally, phylogenetic analyses revealed that proalpha3(I) had diverged from proalpha1(I)."].
- *Synteny.* Both loci share synteny with human and mouse COL1A1, but only a few
  flanking genes are shared, and the two zebrafish regions are arranged differently
  [PMID:26876635 "Alignment of the genomic regions surrounding the zebrafish col1a1a and col1a1b genes with the regions flanking the human/murine COL1A1 locus revealed a shared synteny"]
  [PMID:26876635 "However, the number of the syntenic genes flanking human/mouse COL1A1 and zebrafish col1a1a and col1a1b is limited and also their location and arrangement are different."].
  The authors attribute the duplication to the TGD
  [PMID:26876635 "The similarity between α1(I) and α3(I) suggested that the genes for both proteins probably originated from the duplication of an ancestor α(I) coding gene during the whole genome duplication event that occurred ~320 mya at the basis of teleost evolution"].
- *A dissenting data point.* Protein chemistry detected an alpha3(I) chain in white
  sturgeon, a non-teleost
  [PMID:1617936 "The present study, however, has revealed the occurrence of alpha 3(I) in a chondrostean fish, white sturgeon."],
  and Kimura dated the duplication
  [PMID:1617936 "near the time of the adaptive radiation of bony fish"].
  That identification was chromatographic. A later sequence survey could not find an
  alpha3(I) sequence in another sturgeon
  [PMID:34430038 "Of interest, Kimura [31] found it to be present in the sturgeon Acipenser transmontanus, whereas we were unable to find such a sequence for Acipenser schrenckii using the online protein search tools."].

**What is established:** alpha3(I) is an alpha1(I) paralog, and the PANTHER tree places
the duplication on the teleost stem with a single gar gene. **Not established:** no
double-conserved-synteny (gar bridge) analysis has been published for this locus. The
sturgeon report has not been resolved at the sequence level. Sturgeons have their own
polyploidy, so a sturgeon "alpha3" could be an independent duplicate; that is our
inference, not a published test.

## 2. Protein-level comparison

- **Identity.** A global alignment gives 76.3% identity and 82.7% similarity
  (annotation-comparison.md). The paper reports 78% for the procollagens
  [PMID:26876635 "Amino acid (AA) sequence alignments revealed that zebrafish proα1(I) and proα3(I) chains share 78% of AA identity and the same theoretical molecular weight (137 kDa) and isoelectric point (5.4) (Table 1)."].
  col1a1a is slightly closer to human COL1A1 than col1a1b is
  [PMID:26876635 "Moreover, zebrafish proα1(I) shows 77% and 76% conserved AA with human and murine proα1(I) chains respectively, while proα3(I) has 75% identity with both of them."].
  Across ray-finned fishes, alpha3(I) is the fastest-evolving type I chain
  [PMID:34430038 "with the α3 (I) sequence evolving the fastest, followed by the α2 (I) chain"].
- **Domain architecture.** Both have the complete fibrillar procollagen layout (signal
  peptide, VWFC domain in the N-propeptide, uninterrupted Gly-X-Y helix, NC1
  C-propeptide; UniProt features), with nearly the same length. The cross-linking
  lysines are conserved in zebrafish
  [PMID:26876635 "All the Lys/Hyl residues involved in human/mouse collagen type I cross-links are conserved in zebrafish with the exception of the α2(I) Lys/Hyl 933 that is substituted by an arginine."].
- **Differences that could matter for chain assembly.**
  - alpha3(I) lacks one inter-chain cysteine of the C-propeptide
    [PMID:26876635 "Interestingly, in proα3 this latter domain, crucial for chain association in the trimer, lacks one of the 4 conserved cysteine residues involved in inter-chain bonds (Cys63 of the proα1(I) C-propeptide)"].
    This is confirmed on the UniProt sequences: col1a1a C1265 corresponds to col1a1b
    S1267 ([bioinformatics check](../../../../genes/DANRE/col1a1b/col1a1b-bioinformatics/RESULTS.md)).
    The same Cys/Ser difference separates alpha1(I) from alpha3(I) across fishes
    [PMID:34430038 "We observed the residue at the 1264th position to be Cys (C) in α1 (I) and Ser (S) in α3 (I)"].
  - Its chain recognition region is more divergent
    [PMID:26876635 "Also, the chain recognition region is more divergent in proα3 than in proα1 when compared to mammalian proα1"].
    The authors suggest these changes may affect stoichiometry
    [PMID:26876635 "The lack of zebrafish α3 chain Cys63, that is known to participate in inter chain bounds, may have implication for chain stoichiometry."].
  - The helix is richer in Gly-Gly
    [PMID:26876635 "In zebrafish α3(I) the number of GG + GGG repeats is about two-fold higher than in zebrafish α1(I)"].
    In trout this was proposed to loosen the helix of skin collagen
    [PMID:11358497 "The small number of Gly-Pro-Pro and the large number of Gly-Gly in proalpha3(I) was assumed to partially loosen the triple-helical structure of skin collagen"].
- **Biochemical comparison.** There is no cross-rescue and no purified-chain assay. In
  zebrafish, collagen from bone, skin and scales, which contain different alpha3(I)
  shares, has the same melting temperature
  [PMID:26876635 "For the first time we were able to determine the temperature stability of zebrafish collagen type I that was characterized by apparent Tm ~35 °C in all three analyzed tissues."].
  So no alpha3-dependent change in stability has been detected in zebrafish.

**Does each copy keep the ancestral molecular function?** Yes. Both are structural type
I collagen chains built into the same trimer, and dominant glycine substitutions in
either gene damage bone collagen
[PMID:30082390 "The functional similarity between α1(I) and α3(I) is further illustrated by the fact that glycine substitutions in both genes can cause severe skeletal phenotypes, arguing for a dominant-negative effect on type I bone collagen and thus incorporation of a substantial amount of both α1(I) and α3(I) into the type I collagen triple helix."].
The protein-level change is in *how* alpha3(I) takes part in the complex: it has
changed assembly signals and fills one of the two "alpha1" positions. It does not do
a different kind of thing.

## 3. Expression

- **Ancestral state.** No gar or other non-teleost expression data were found. In
  tetrapods, the single COL1A1 supplies both alpha1 chains of the (alpha1)2alpha2
  trimer
  [PMID:26876635 "In tetrapods collagen type I is a trimer mainly composed of two α1 chains and one α2 chain, encoded by COL1A1 and COL1A2 genes, respectively."].
- **Zebrafish: shared domains.** The three type I collagen genes have the same time
  course, peaking at the onset of bone formation
  [PMID:26876635 "The expression profiles of all three type I collagen genes were highly similar, with a peak in relative expression between 3 and 4 dpf (Fig. 3a,b), corresponding with the onset of bone formation in zebrafish embryos28."].
  They share the same tissues: osteoblasts, tendon and ligament fibroblasts,
  myosepta and epidermis
  [PMID:26876635 "All three type I collagen genes are expressed in mesenchymal cells that have entered final differentiation."]
  [PMID:26876635 "At every time point, expression of all three genes could be detected in the epidermis."].
  The authors conclude the genes are co-regulated
  [PMID:26876635 "Our data demonstrated a co-regulation and interdependence of the three collagen type I genes during embryonic and larval zebrafish development."].
- **Zebrafish: copy-specific domain.** Only col1a1a is expressed in the fin fold and
  pectoral fin margin
  [PMID:26876635 "Interestingly, only col1a1a was shown to be expressed in the median fin fold and in the apical ectodermal ridge of the pectoral fin at 48, 72 and 96 hpf (Fig. 4a,b)."],
  which the authors link to actinotrichia made of alpha1(I) homotrimers
  [PMID:26876635 "Given the absence of col1a1b and col1a2 expression, our findings also support the presence of α1(I) homotrimers in actinotrichia."].
- **Protein level, by tissue.** At the protein level all three chains are present at
  roughly 1:1:1 in adult tissues
  [PMID:26876635 "Even though in adult bone, skin and scales equal amounts of α1(I), α3(I) and α2(I) chains are present"].
  The alpha3/alpha1 ratio is higher in skin and scales than in bone
  [PMID:26876635 "SRM and spectral counting mass spectrometry data shows a statistically significant higher α3(I)/α1(I) ratio in external (skin and scales) versus internal (bone) tissues pointing out to a tissue-specific collagen composition."].
  In trout, alpha3(I) is in skin collagen but not in muscle collagen
  [PMID:11358497 "The subunit compositions of skin and muscle type I collagens from rainbow trout were found to be alpha1(I)alpha2(I)alpha3(I) and [alpha1(I)](2)alpha2(I), respectively."].
- **Other teleosts.** alpha3 is common but not universal. Kimura's survey found
  [PMID:3677606 "The skin collagen seems to exist as an alpha 1 alpha 2 alpha 3 heterotrimer in many teleosts and as an (alpha 1)2 alpha 2 heterotrimer in some teleosts."],
  including species that lack it altogether
  [PMID:26876635 "A first teleost group, including ayu, flying fish and saury, missed this chain"].
  Sequence searches also miss it in some cyprinids and in herring
  [PMID:34430038 "This chain is, however, apparently absent from two of the five genera of cyprinids (Cypriniformes: Cyprinidae), and from herring, Clupea harengus (Clupeiformes: Clupeidae)."].

**Shared vs copy-specific.** Almost everything is shared. col1a1a has one extra domain
(fin fold and actinotrichia). col1a1b has no domain of its own; its only distinctive
feature is a quantitative bias toward skin and scales at the protein level. Whether
the fin-fold domain was ancestral and lost by col1a1b (a partition) cannot be told
without a non-teleost reference. Actinotrichia are a fish fin structure, so this is
plausible but untested.

## 4. Experimental evidence of function

All germline data come from one study that crossed the two paralogs
[PMID:30082390 "We systematically analyzed skeletal phenotypes in a large set of zebrafish models carrying different mutations in the zebrafish type I collagen-encoding genes col1a1a, col1a1b, and col1a2 (Table 1)."].
The null alleles are ENU nonsense alleles from the Zebrafish Mutation Project
[PMID:30082390 "The col1a1asa1748, col1a1bsa12931, col1a2sa17981, bmp1asa2416, and plod2sa1768 mutant zebrafish were generated by the zebrafish mutation project"],
i.e. PTC/NMD-type alleles. Each removes its chain from bone collagen
[PMID:30082390 "Two zebrafish knockout mutants with a premature stop-codon mutation in either col1a1a or col1a1b show absence of α1(I) and α3(I), respectively, in the vertebral bone"]
[PMID:30082390 "Accordingly, in col1a1b−/− mutants, no tryptic peptides of α3(I) could be detected, confirming decay of mutant col1a1b mRNA transcripts."].

**col1a1a**

- *Null (sa1748), homozygous:* lethal
  [PMID:30082390 "Eventually, all genotypes containing a homozygous knockout of col1a1a [loss of α1(I)] were found to be lethal by the age of 3 mo."].
  Larvae lack actinotrichia
  [PMID:30082390 "Upon detailed examination of the finfold, these actinotrichia were found to be absent in col1a1a−/− mutant larvae (Fig. 5D)."]
  and do not inflate the swim bladder
  [PMID:30082390 "These larvae lacked the presence of an inflated swim bladder"].
- *Morphants* disrupt actinotrichia
  [PMID:21420398 "Morpholino knockdown in zebrafish embryos demonstrated that the two collagens and lh1 are essential for actinotrichia and fin fold morphogenesis."].
- *Dominant helix glycine alleles* (chihuahua, dmh13, dmh14) cause osteogenesis
  imperfecta-like skeletal disease
  [PMID:14623232 "Heterozygous chihuahua fish have phenotypic similarities to human osteogenesis imperfecta"]
  [PMID:28835471 "Both the dmh13 and dmh14 mutants carry mutations in the col1a1a gene (G1093R; G1144E)"].

**col1a1b**

- *Null (sa12931), homozygous:* viable, with mild bone changes
  [PMID:30082390 "Fish with a complete loss of α3(I), but intact α1(I) did not show significant alterations of bone morphology (SI Appendix, Fig. S7), although some fish showed evidence of fractures (Fig. 1 and Table 2) and increased TMD throughout the vertebral column, indicating an impaired bone quality."].
- *Dominant helix glycine allele* dmh29 has the most severe phenotype among the helix
  alleles tested in these paralogs
  [PMID:30082390 "with col1a1bdmh29/+ fish displaying the most severe skeletal phenotype with kyphoscoliosis and shorter, thicker, and overmineralized vertebral bodies and frequent rib fractures"].
  So alpha3(I) is not a minor or optional component of the bone collagen that is
  actually made.

**Both copies together**

- *Single heterozygotes are normal, the double heterozygote is not:*
  [PMID:30082390 "However, both qualitative and quantitative assessment of µCT scans of the vertebral column of heterozygous col1a1a+/− or col1a1b+/− zebrafish mutants revealed no skeletal abnormalities"]
  [PMID:30082390 "Hence, we generated a double-heterozygous knockout mutant (col1a1a+/−;col1a1b+/−), which displays a mild skeletal phenotype, with a low frequency of spontaneous fractures (calluses in the ribs), scoliosis and localized compression, fusions, and mild malformation of the vertebral bodies in some of the mutant fish"].
- *The col1a1b null worsens the col1a1a heterozygote:*
  [PMID:30082390 "Homozygous mutant col1a1b−/− mutants [loss of α3(I)] were present by the age of 3 mo, however at reduced numbers if combined with heterozygous loss of col1a1a (col1a1a+/−;col1a1b−/−)."]
- *Authors' interpretation:* redundancy plus a dosage asymmetry
  [PMID:30082390 "arguing for interchangeability and functional redundancy between α1(I) and the homologous α3(I)"]
  [PMID:30082390 "This suggests a gene/protein dosage effect, where α1(I) is more abundant than α3(I), as hypothesized in our previous work (19)."].

**Not done:** there is no cross-rescue or allele swap, no RNA-less allele, and no test
of transcriptional adaptation (for example, col1a1a up in col1a1b PTC mutants). The
normal single heterozygotes could partly reflect upregulation of the paralog. There
are no data on skin or scale collagen in the col1a1b null, although that is where
alpha3(I) is relatively enriched.

## 5. Fate classification

**DOSAGE, with a minor expression partition (col1a1a-only fin fold). No evidence of
protein-level innovation.**

- *Protein level: DOSAGE (shared function, stoichiometric).* Confidence is moderate.
  Both chains keep the ancestral structural activity and are built into the same type
  I trimer, at similar amounts in adult tissues. Genetically they behave as one pooled
  "alpha1-type" dose: either chain alone can be halved without effect, but halving
  both causes bone fragility. This is the dosage/stoichiometry fate that the
  heterotrimer hypothesis predicts. The duplicate became a new *subunit identity*
  within the complex. Its changed assembly signals (lost inter-chain cysteine,
  divergent recognition region) plausibly steer it into alpha1alpha2alpha3 trimers.
  But no property of those trimers is known that (alpha1)2alpha2 lacks. Zebrafish
  collagens with different alpha3 shares have the same thermal stability. The trout
  suggestion that alpha3 loosens the skin collagen helix is untested in zebrafish.
- *The split is asymmetric.* col1a1a keeps the full ancestral role: it is
  dose-limiting, its null is lethal, and it can form homotrimers. col1a1b is the
  junior copy: dispensable, faster-evolving, and lost in several teleost lineages. This
  fits the quantitative subfunctionalization (hypofunctionalization) pattern described
  in the [background](../../DANRE_DUPLICATION-background.md), more than a new
  function.
- *Expression level: minor PARTITION.* Confidence is moderate for the observation and
  low for the interpretation. col1a1b is absent from the fin fold, where col1a1a builds
  actinotrichia. Without non-teleost expression data it is unknown whether col1a1b
  lost this domain.
- *Not INNOVATION.* There is no copy-specific phenotype of col1a1b, no tissue where it
  acts alone, and no measured new property. *Not pure BACKUP.* The copies are not
  equivalent (lethal vs viable nulls; fin fold col1a1a-only), and both are needed at
  full dose together.

**What would change the call:**
- If collagen lacking alpha3(I) (col1a1b-/- skin or scales) showed a measurable change
  in stability, cross-linking or fibril structure, the protein-level call would move
  toward innovation (a specialized skin/scale chain).
- If a col1a1a CDS knocked into col1a1b fully restored col1a1b-/- skin and bone, pure
  dosage would be confirmed.
- If col1a1a were upregulated in col1a1b PTC mutants, the apparent dispensability of
  alpha3(I) would be partly an artefact of transcriptional adaptation.

## 6. GO annotation consistency across the pair

From `annotation-comparison.md`:

- **GOA before review.** The asymmetry was large: 27 rows on col1a1a, 9 on col1a1b.
  Every IBA and IEA row is identical between the copies. The difference is entirely
  experimental. col1a1a carries ZFIN IMP rows from many alleles (chihuahua, dmh13,
  dmh14, tt281, sa1748, a morpholino). col1a1b has a single IMP row (dmh29, skeletal
  system development), and none from PMID:30082390 or PMID:26876635, which study it
  directly. Most of the asymmetry therefore reflects which copy was studied (col1a1a
  is the chihuahua locus), not biology.
- **Mis-attached evidence.** Two col1a1a "skeletal system development" IMP rows from
  PMID:30082390 are supported by genotypes that carry no col1a1a allele:
  ZDB-GENO-180503-7 = col1a1b^dmh29/+ and ZDB-GENO-180503-8 = col1a2^dmh15/+ (ZFIN
  genotype pages). They are marked REMOVE on col1a1a. The term stays through the
  col1a1a-allele rows, and the dmh29 evidence belongs on col1a1b. This is raised as a
  suggested question for ZFIN.
- **Kept identical, because the biology is shared.**
  - MF GO:0030020 (IBA) ACCEPT on both; the broader GO:0005201 (IEA) ACCEPT on both.
  - GO:0030199 collagen fibril organization ACCEPT on both.
  - GO:0031012 extracellular matrix and GO:0005576 extracellular region ACCEPT on both.
  - GO:0001501 skeletal system development ACCEPT on both, each on its own alleles.
  - GO:0043588 skin development and GO:0048705 skeletal system morphogenesis (IBA)
    KEEP_AS_NON_CORE on both.
  - NEW GO:0005584 collagen type I trimer (IDA, PMID:26876635) on both. This is the
    annotation that captures the pair's biology: two paralogous chains of one complex.
    Human COL1A1 carries the same term. By definition GO:0005584 covers any trimer of
    alpha(I) chains, so the teleost alpha1alpha2alpha3 form needs no new term.
- **Removed from both.** The GO:0005737 cytoplasm IBA (PTN002771199) is removed on
  both. Its only source is a col1a1a IDA that rests on a col1a1 mRNA in situ used as a
  keratinocyte marker (PMID:19757382). That IDA is MARK_AS_OVER_ANNOTATED on col1a1a.
- **Copy-specific, because the biology differs.** The fin terms stay on col1a1a only.
  GO:0033333 fin development and GO:0033334 fin morphogenesis are ACCEPT, and
  pectoral fin development and fin regeneration are non-core. This matches the
  col1a1a-only fin-fold expression and the loss of actinotrichia in the col1a1a null.
  They should not be propagated to col1a1b. The chihuahua bone-quality terms (bone
  mineralization, bone remodeling, regulation of ossification, which is MODIFIED to
  ossification) remain col1a1a-only as non-core IMP. They are allele-specific
  observations, and nothing suggests col1a1b lacks the same roles, but no one has
  assayed them in col1a1b. They are left as a study-effort asymmetry rather than
  copied over.
- **Deliberately not added.** No col1a1b-specific process term, and no skin- or
  scale-specific term. The alpha3(I) enrichment in skin and scales is quantitative.
  No NEW IMP was added to col1a1b from the null or double-heterozygote data, because
  its skeletal system development row already covers them. IBA from PTHR24023
  correctly treats both copies as equivalent for MF and location. No IBA process term
  here is copy-specific.

## 7. Open questions

- What trimers actually exist in each tissue: alpha1alpha2alpha3 only, or a mix with
  (alpha1)2alpha2 and (alpha3)2alpha2? The authors could not exclude a mix
  [PMID:26876635 "Due to the co-migration of α1(I) either with α1(II) or α3(I) chains it was impossible to determine exact ratios between these chains and hence make assumptions about the stoichiometry of chain association of embryonic collagen type I."].
- Does alpha3(I) change skin or scale collagen properties? Compare thermal stability,
  cross-links and fibril diameter in col1a1b-/- versus wild-type skin and scales.
- Is there transcriptional adaptation? Is col1a1a upregulated in col1a1b PTC mutants,
  and vice versa? An RNA-less col1a1b allele would test this.
- Allele swap: can col1a1a CDS at the col1a1b locus replace alpha3(I), and can
  alpha3(I) build actinotrichia if expressed in the fin fold?
- Why has alpha3(I) been lost in some teleosts (ayu, flying fish, saury, some
  cyprinids, herring), and do those species compensate with more alpha1(I)?
- What is the gar col1a1 expression pattern, including in fin-fold-like structures?
  This is needed to decide whether col1a1b lost an ancestral fin domain.

## References

- PMID:1617936, Kimura 1992 (alpha3 in bony fish, including sturgeon; abstract only)
- PMID:3677606, Kimura et al. 1987 (alpha3 in teleost skin collagen; abstract only)
- PMID:11358497, Saito et al. 2001 (trout type I collagen primary structure; abstract only)
- PMID:14623232, Fisher et al. 2003 (chihuahua; abstract only)
- PMID:14738308, Morvan-Dubois et al. 2003 (phylogeny locating zebrafish alpha3(I); abstract only)
- PMID:21420398, Durán et al. 2011 (actinotrichia collagens; abstract only)
- PMID:26876635, Gistelinck et al. 2016 (expression, chain composition, sequence comparison; full text)
- PMID:28835471, Henke et al. 2017 (dominant dmh alleles in col1a1a and col1a1b; full text)
- PMID:30082390, Gistelinck et al. 2018 (null and dominant alleles of both copies, double heterozygotes; full text)
- PMID:34430038, Harvey et al. 2021 (collagen I sequences across ray-finned fishes; full text)
- [annotation-comparison.md](annotation-comparison.md);
  [col1a1b C-propeptide cysteine check](../../../../genes/DANRE/col1a1b/col1a1b-bioinformatics/RESULTS.md);
  PANTHER row from `../../panther_tgd_pairs.tsv`
