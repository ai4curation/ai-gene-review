---
title: "vcla / vclb"
autolink_gene_symbols: false
---

# vcla / vclb

[Back to pairs](../README.md)

**Bottom line:** MIXED. The two vinculin proteins are conserved and behave the same in the one
side-by-side cell assay. Only vclb substitutes Y822 (to F), and its effect in vivo is unknown. The
copies differ mainly in where they are expressed. vclb is the main copy in the embryonic heart,
epicardium, endocardium and endothelium. Loss of vclb alone disorganizes the coronary vessels and kills
juveniles, so in that domain the relationship is a PARTITION. Loss of vcla alone, even
maternal-zygotic, has no visible phenotype. Losing both copies adds mild vascular leakage and
lethality before adulthood.

vcla nonsense mutants that degrade their mRNA upregulate vclb mRNA by transcriptional adaptation. That
response is triggered by mutant mRNA decay, not by loss of Vcla protein. It shows that the vclb locus
responds, not that Vclb protein makes up for Vcla. A Western blot of another vcla nonsense allele found
no rise in vinculin protein. So "backup" is possible for vcla but has not been shown at the protein
level.

| | vcla | vclb |
|---|---|---|
| UniProt | B3DI32 (TrEMBL; metavinculin-type isoform, 1131 aa) | A0A0S2I7K2 (TrEMBL; vinculin-type isoform, 1066 aa) |
| Human ortholog | VCL | VCL |
| Chromosome | 13 | 12 |
| ZFIN | ZDB-GENE-050506-61 | ZDB-GENE-131017-1 |
| Review | [genes/DANRE/vcla](../../../../genes/DANRE/vcla/vcla-ai-review.yaml) | [genes/DANRE/vclb](../../../../genes/DANRE/vclb/vclb-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR46180 (VINCULIN) | VCL(LDO) / VCL(O) | 1 (same gar gene for both) | 2 | (blank) |

This is the strictest call the project uses. PANTHER places the duplication after the split from gar
and before the split between zebrafish and medaka. Both zebrafish copies share one gar co-ortholog, and
medaka also keeps two copies.

**Literature.** The paper that first described the pair attributes it to the teleost duplication. It
does not give a synteny or gene-tree analysis:
[PMID:28767718 "Zebrafish are members of the teleost family, which have undergone an additional genome duplication event compared to other vertebrates [43]."]
[PMID:28767718 "The first isoform, vinculin a (vcla) present on chromosome 13, was well annotated, while its paralog vinculin b (vclb) on chromosome 12 was not (as of assembly Zv9)."]

**Status.** TGD origin is supported by the PANTHER gene tree (a `TGD_tree` call with a single gar
co-ortholog). I found no published double-conserved synteny analysis with gar for this pair. The
statement is therefore tree-based, and that is what the project's strictest criterion requires. Which
medaka copy is orthologous to which zebrafish copy was not checked.

## 2. Protein-level comparison

- **Identity.** 81.4% identity and 87.6% similarity over 1131 alignment columns
  ([annotation-comparison.md](annotation-comparison.md)). Part of that difference comes from the
  isoforms in the two entries. The vcla entry B3DI32 includes the 68-residue metavinculin insert (59
  of 68 positions align, 46 identical); the vclb entry has none of it
  ([RESULTS.md](../../../../genes/DANRE/vcla/vcla-bioinformatics/RESULTS.md)). Against human vinculin
  of the matching isoform, the identities are vcla 85.4% (to metavinculin) and vclb 86.0% (to
  vinculin). The published figures are:
  [PMID:28767718 "Both zebrafish vcla and vclb show a high sequence conservation at the protein level (87% and 86% identical amino acids respectively) with mammalian vcl (Fig 1A)."]
- **Binding regions are conserved in both copies.**
  - The D1 head domain: [PMID:28767718 "The key residue of which mutation perturbs all of these interactions, A50, is fully conserved [47,48]."]
  - The proline-rich loop: [PMID:28767718 "The loop regions in vinculin A and B are a little less conserved across the higher vertebrate homologs, but the proline rich sequences, containing binding sites for VASP [49], vinexin [50], and Arp2/3 [51] are fully conserved, indicating that these interactions are conserved as well (Fig 1B and 1D)."]
  - The tail: [PMID:28767718 "Especially Helices 3–5 which mediate paxillin and F-actin binding (Fig 1E) [52,53] are almost completely identical."]
- **The one known protein difference: Y822F in vclb.** My alignment confirms F at the aligned position
  822 in vclb and Y in vcla.
  [PMID:28767718 "The one notable difference between zebrafish vinculin A and B is the change of the otherwise conserved Y at position 822 to F in vinculin B."]
  In mammalian cells, phosphorylation of Y822 was needed for vinculin to bind beta-catenin at
  junctions:
  [PMID:28767718 "The phosphorylation of this tyrosine was found to be crucial for the interaction of vinculin to β-catenin and localization to cell-cell junctions in MCF10A cells, although it is localized outside of the β-catenin interacting domain [58]."]
- **Side-by-side cell assay.** The two GFP-tagged proteins localize the same way in MDCK cells. Both
  depend on the vinculin-binding site of alpha-catenin to reach junctions:
  [PMID:28767718 "In α-catenin rescued cells, both vinculin A and vinculin B localize to integrin-based Focal Adhesion structures, as well as to the punctate Focal Adherens Junctions as evidenced by colocalization with α-catenin"]
  [PMID:28767718 "Here it is apparent that both vinculin A and vinculin B are now excluded from Focal Adherens Junctions and Linear Adherens Junctions (arrows), but are still present in Focal Adhesions (arrows)."]
  [PMID:28767718 "Curiously, the 822F residue in zebrafish vinculin B does not perturb its localization to cell-cell junctions."]
  The authors note a limit of this assay: the MDCK cells still contain their own vinculin.
  [PMID:28767718 "Alternatively, the fact that endogenous vinculin was depleted in experiments performed by Bays et al. but was still present in our cells, may have rescued the junctional localization of Y822F vinculin or zebrafish vinculin B."]
- **Authors' conclusion:**
  [PMID:28767718 "In conclusion, from the currently available data, both vinculin proteins in zebrafish appear to function comparably to the single vinculin protein present in higher vertebrates and can be regarded as functionally redundant."]

**Does each copy keep the ancestral molecular function?** Probably yes, for talin and alpha-catenin
engagement and actin linkage. The evidence is sequence conservation plus the MDCK localization assay.
No binding assay, cross-rescue or coding-sequence swap has been done in zebrafish. Whether Vclb binds
beta-catenin is open, because of F822.

## 3. Expression

- **Heart.** vclb is the main copy. vcla is low in whole-heart arrays but is present in the myocardium.
  - [PMID:30635353 "A recent report showed that vclb is the predominant vcl gene expressed in the embryonic heart (Cheng et al., 2016)."]
  - [PMID:30635353 "The microarray data show that tln1 and apbb1ip are expressed at high levels in embryonic hearts (Fig. S1 A), but vcla is expressed at low levels (data not shown); no probe for vclb was included in the array."]
  - [PMID:27578788 "By contrast, cardiac muscle development is relatively normal, probably owing to redundancy with Vcla, a vinculin paralog that is expressed in the myocardium but not epicardium."]
  - vclb is expressed in the atrioventricular canal:
    [PMID:30635353 "Interestingly, the expression pattern of tln1, vclb, and appb1ip closely resembled that of itga5 and itgb1b, with noticeable expression in the AVC in 56-hpf hearts (Fig."]
- **Endothelium: mainly vclb.**
  [PMID:36314606 "As vinculinb is most prominently expressed in zebrafish ECs (Lawson et al., 2020), we generated a vascular restricted transgenic line, Tg(fli1ep:vinculinb-eGFP)uq2al, whereby Vinculinb is tagged with eGFP at the C terminus."]
  [PMID:36314606 "Live imaging of the main axial artery, the dorsal aorta (DA), revealed Vinculinb localisation at cell-cell junctions and at FAs in wild-type embryos (Fig."]
- **Notochord sheath: both copies.** vcla transcripts are enriched there, and a vclb knock-in reporter
  also marks sheath focal adhesions. vclb is broadly expressed in the surrounding muscle and vessels.
  - [PMID:38697108 "We found a significant enrichment of transcripts for focal adhesion proteins including, vcla, pxna, zyx, tln2a, and ptk2ab (Figure 4B)."]
  - [PMID:38697108 "We generated a TgKI(vclb-mScarlet) transgenic KI line and observed in cross-sections localization of Vinculin+ puncta on the basal membrane of cells expressing TP1:VenusPest, indicating the assembly of focal adhesions in new segments (Figure 4C)."]
  - [PMID:38697108 "Live-imaging approaches using the TgKI(vclb-mScarlet) proved challenging due to the widespread expression profile of Vinculin in the surrounding tissues, such as the axial musculature and vasculature."]
- **Whole embryos.** In a Western blot using an antibody that detects both copies, most vinculin
  protein at 5 dpf comes from vcla (section 4).
- **Metavinculin.** The vcla gene can make the metavinculin splice form (B3DI32 carries the insert). No
  such exon was found in vclb cDNA at 1 dpf, though the vclb genomic annotation was incomplete:
  [PMID:28767718 "This extra exon is indeed annotated for vinculin A in the Zv9 genome database, but full annotation of the vinculin B genomic region spanning this exon was missing."]
  [PMID:28767718 "We did not detect the extra exon in the cDNA of vinculin A or B extracted from whole 1dpf embryo lysates, corroborating a recent article on vinculin B function in zebrafish [40]."]
- **The pre-duplication state.** Mammals have a single VCL gene that is expressed broadly, including
  in heart and muscle, where it is also made as metavinculin. I found no data on gar vinculin
  expression. The ancestral state is therefore inferred from tetrapods and has not been measured.

The picture is broad overlap (notochord sheath, cell culture behaviour) with a clear bias: vclb
dominates in heart and endothelium, and vcla dominates in total embryonic protein and may be the source
of metavinculin. There are no published in situ comparisons of the two copies side by side outside the
heart.

## 4. Experimental evidence of function

**Alleles used**

| Gene | Allele | Lesion | Type | Source |
|---|---|---|---|---|
| vcla | hu10818 | 8-bp deletion, stop at codon 160 (TALEN) | PTC; transcript still present in cDNA | PMID:28767718 |
| vcla | bns241 (Δ13) | frameshift | PTC with mutant mRNA decay; shows transcriptional adaptation | PMID:30944477 |
| vcla | sa14599 | point nonsense (ENU) | PTC without mRNA decay; no transcriptional adaptation | PMID:30944477 |
| vcla | bns300 (exon22_ins1) | insertion in last exon | NMD-insensitive position | PMID:30944477 |
| vcla | bns605 | 72.44-kb deletion of the locus | RNA-less; no transcriptional adaptation | PMID:36427314 |
| vclb | gene trap | insertional trap | loss of function (details in full text only) | PMID:27578788 |
| vclb | hu11202 | 7-bp deletion, stop at codon 22 | PTC | PMID:28767718 |
| vclb | bns247 | 16-bp deletion | frameshift (PTC expected; not characterized for mRNA decay) | PMID:30635353 |
| vcla | morpholino ZDB-MRPHLNO-100114-3 | splice-blocking, zygotic vcla only | knockdown | PMID:19800866, PMID:26954676 |

Allele sources:
[PMID:28767718 "The vcla Δ8B mutation results in a frameshift that creates a premature stopcodon at amino acid position 160."]
[PMID:28767718 "This frameshift mutation generates a premature stopcodon at position 22 (Fig 4D) and is the vclb mutant allele we describe from here on, unless otherwise specified, and is designated as vclbhu11202."]
[PMID:36427314 "In addition, we generated an RNA-less allele of vcla (a 72.44-kb deletion that removes the vcla locus; fig. S3, C and D) and found that it does not display TA (fig. S3E)."]
[PMID:30635353 "We generated a vclb allele carrying a 16-bp deletion (vclbbns247; Fig."]
[PMID:28767718 "Moreover, the splice-site morpholino that was used, only targeted the zygotic vinculin A isoform, keeping maternally supplied mRNA and vinculin B intact."]

**vcla**

- Maternal-zygotic mutants have no phenotype:
  [PMID:28767718 "To rule out possible effects of maternally contributed mRNA or protein of vcla to early development, the offspring was grown to adulthood, then incrossed to generate Maternal Zygotic (MZ) vcla embryos."]
  [PMID:28767718 "Taken together, the results show that vcla is not essential for zebrafish development or adult life."]
- The other vcla PTC alleles are also phenotypically wild type under the dissecting microscope:
  [PMID:30944477 "hbegfaΔ7, hbegfasa18135, hbegfafull locus del., vclaΔ13, vclasa14599, vclaexon22_ins1, alcamaΔ10, and alcamapromoter-less mutants do not exhibit any obvious defects under a dissecting microscope."]
- Morpholino phenotypes (heart failure, poor contractility, altered repolarization) were not
  reproduced by the mutants. The mutant authors consider the morpholino effects most likely
  non-specific:
  [PMID:26954676 "Finally, we found that targeted gene knock-down of vinculin, similar to Paxillin and FAK ablation, results in severe ventricular contractile dysfunction in zebrafish embryos [5] (S4A–S4D Fig)."]
  [PMID:28767718 "While we cannot fully exclude the latter, the most likely explanation is that the reported effects of the used vinculin A morpholinos are non-specific."]
- A dominant-negative vinculin head domain, cloned from vcla and expressed in endocardium, blocks
  valve morphogenesis. This blocks vinculin in general, not vcla specifically:
  [PMID:30635353 "To generate the DN Vinculin transgene, the first 774 bp of the vcla coding sequence was amplified by PCR using the following primers"]

**vclb**

- Gene-trap mutants have coronary vessel and epicardial defects and die as juveniles:
  [PMID:27578788 "The mutant shows overproliferation of epicardium-derived cells and disorganization of coronary vessels, and they eventually die off at juvenile stages."]
  [PMID:27578788 "Mechanistically, Vclb deficiency results in the release of another cytoskeletal protein, paxillin, from the Vclb complex and the upregulation of ERK and FAK phosphorylation in epicardium and endocardium, causing disorganization of endothelial cells and pericytes during coronary vessel development."]
- Other PTC alleles also fail to reach adulthood, but valve development is normal:
  [PMID:30635353 "These mutants did not survive to adulthood, a finding consistent with other recent studies of vclb function (Cheng et al., 2016; Han et al., 2017; unpublished data)."]
  [PMID:30635353 "However, we found that vclb mutants did not exhibit strong delays in AV EC migration and valve formation"]
- The hu11202 allele could in principle allow restart of translation after the stop codon:
  [PMID:28767718 "In contrast, for vclb a potential truncated protein could start at M26 in exon 1, leaving the possibility for a functional vinculin protein."]

**Both copies**

- In MZvcla; Zvclb double mutants, vinculin protein is undetectable at 5 dpf. The embryos develop,
  with mild, transient cardiac edema and normal skeletal muscle:
  [PMID:28767718 "By westernblotting using an antibody that recognizes both zebrafish vinculin A and B proteins (S5 Fig) we detect a very strong reduction in vinculin protein levels in the vcla-/- mutants, while there is no vinculin protein detectable in the vcla-/-vclb-/- double mutants (Fig 5A)."]
  [PMID:28767718 "While no lethality was observed, we did notice that vcla-/-vclb-/- double mutants began to develop cardiac edemas around 3 dpf that arbitrarily classified by eye in mild (54%) and severe (34%) cases (Fig 5B and 5C)."]
  [PMID:28767718 "The chance of developing the cardiac phenotype seemed to be gene dose dependent, as only 13% of vcla-/-vclb+/- mutants and 24% of vcla mutants developed mild cardiac edemas, while the incidence of severe edemas was also lower (19% and 17% for vcla-/-vclb+/- and vcla mutants respectively) compared to vcla-/-vclb-/- double mutants."]
  [PMID:28767718 "Statistical testing did not show significance of the observed differences (S7 Fig)."]
- No double mutants survive to adulthood. vcla-/-;vclb+/- fish are recovered at roughly Mendelian
  ratios:
  [PMID:28767718 "Remarkably, during fin clipping no vcla-/-vclb-/- fish were detected (172 adults screened out of three different pairings), while the remaining vcla-/- and vcla-/-vclb+/- siblings roughly show a Mendelian distribution."]
- Vascular phenotypes need loss of both copies, or of vcla plus one vclb allele. Small molecules leak
  from the vessels:
  [PMID:36260739 "Our analysis shows that vcla−/−;vclb+/−and vcl full-KO embryos exhibited increased perivascular dextran levels"]
  [PMID:36260739 "we observed vascular leakage specifically for small molecules, 10 kDa, in vinculin knockout zebrafish, whereas the vasculature still acted as a barrier for larger molecules"]
  [PMID:36260739 "The genetic ablation of both vinculin isoforms delays sprouting angiogenesis during early vascular development (34)."]
  Endothelial junctional fingers need vinculin, and expressing vinculin in endothelium rescues them:
  [PMID:35417696 "Furthermore, genetic deletion of vinculin prevents finger formation, a junctional defect that could be rescued by transient endothelial expression of vinculin."]
  The Kotini abstract does not name the rescue construct's paralog. The later paper says the same
  Han alleles were used:
  [PMID:36260739 "The vclahu10818; vclbhu11202 zebrafish lines (38) were crossed into the transgenic Tg(fli1a:EGFP)ƴ1line, which labels all endothelial cells (45) as described in (34)."]
- Maternal contribution. Maternal vcla is removed in the MZ design. Maternal vclb is not removed in any
  double mutant, but the authors infer it is small:
  [PMID:28767718 "Moreover, the very low expression of vinculin B at day 5 indicates that indeed very little if any vinculin protein is present due to maternal contribution in the early stages of development of the vcla-/-vclb-/- double mutants."]
- Cardiomyocyte maturation. Vinculin is reported to be essential for myofilament maturation. The
  abstract does not say which copy or alleles were used, so I cannot assign this to either gene:
  [PMID:31495694 "Here, we first show that the forces of the contracting heart regulate the localization and activation of the cytoskeletal protein vinculin (VCL), which we find to be essential for myofilament maturation."]

**Compensation and transcriptional adaptation: what is shown**

- **vcla PTC mutants that degrade their mRNA raise vclb mRNA.**
  [PMID:30944477 "hbegfa, vcla, hif1ab, vegfaa, egfl7 and alcama zebrafish mutants exhibit increased mRNA levels of a paralogue or family member (hereafter referred to as ‘adapting gene’), namely hbegfb, vclb, epas1a and epas1b, vegfab, emilin3a and alcamb, respectively"]
- **The response follows mutant mRNA decay, not the loss of protein.**
  - A vcla PTC allele without mRNA decay does not adapt:
    [PMID:30944477 "Notably, while analyzing various mutant alleles, we found that unlike hbegfaΔ7 and vclaΔ13, two other PTC bearing alleles, hbegfasa18135 and vclasa14599, do not display transcriptional adaptation (Fig."]
    [PMID:30944477 "To investigate the reason for this difference, we examined mutant mRNA levels and observed limited or no decrease in the hbegfasa18135 and vclasa14599 alleles (Fig."]
  - NMD was tested genetically in vcla:
    [PMID:30944477 "To investigate the role of the mRNA surveillance machinery in transcriptional adaptation, we genetically inactivated Upf1, a key non-sense mediated decay (NMD) factor6, in hbegfaΔ7, vegfaa and vclaΔ13 zebrafish mutants."]
  - The last-exon allele was tested. Its figure panel falls in the range the paper lists for alleles
    without adaptation. I read this from the figure-legend layout; the text does not state it for
    vcla:
    [PMID:30944477 "f, qPCR analysis of vcla and vclb mRNA levels in vcla wt and last exon (exon 22) mutant zebrafish."]
    [PMID:30944477 "In the context of the zebrafish studies, we identified several mutant alleles which do not display transcriptional adaptation (Extended Data Fig. 3d-f), indicating that a DNA lesion by itself is not sufficient to trigger transcriptional adaptation, or that specific DNA lesions are required."]
  - The RNA-less vcla allele does not adapt (PMID:36427314, quoted in the allele list above).
  - Destroying vcla mRNA with Cas13d, without any DNA lesion, also raises vclb:
    [PMID:40128410 "Kushawah et al (2020) have previously shown that Cas13d can degrade specific mRNAs in zebrafish embryos and that vclb mRNA levels increase after the cleavage of vcla mRNA, similar to our observations in vcla mutant zebrafish that display mutant mRNA decay (El-Brolosy et al, 2019)."]
  - Heterozygotes also adapt:
    [PMID:30944477 "Moreover, we found that vcla, hif1ab and egfl7 heterozygous animals also display transcriptional adaptation, albeit less pronounced than that observed in the homozygous mutants (Extended Data Fig."]
  - Antisense transcripts at the vclb locus go down:
    [PMID:30944477 "Notably, we also observed a downregulation of anti-sense transcripts at the hbegfb and vclb loci in hbegfaΔ7 and vclaΔ13 mutants, respectively (Extended Data Fig."]
- **The effect is inherited, which affects controls.** Wild-type offspring of vcla PTC heterozygotes
  have raised vclb, with H3K4me3 at the vclb promoter. Offspring of RNA-less heterozygotes do not:
  [PMID:36427314 "Notably, we observed increased mRNA levels of the adapting genes, alcamb, vclb, emilin2a/emilin3a, and adh1a3, in the wild-type offspring from intercrosses of alcama, vcla, egfl7, and aldh1a2 heterozygous zebrafish, respectively (Fig."]
  [PMID:36427314 "We thus performed ChIP coupled with quantitative polymerase chain reaction (qPCR) (ChIP-qPCR) at this stage and observed the enrichment of H3K4me3 at the promoter of the adapting gene vclb in second-generation (F2) wild-type embryos from F1 vcla+/+ incrosses compared with wild types (Fig."]
  [PMID:36427314 "We also analyzed wild-type offspring from vcla RNA-less allele heterozygous intercrosses and observed no increased expression of the adapting gene when compared with embryos obtained from AB incrosses (fig. S3F)."]
- **Protein-level compensation was looked for once and not found.** The test used a different PTC
  allele, hu10818, and whole posterior-body lysates:
  [PMID:28767718 "This result strongly indicates that mutation of the vcla gene leads to loss of most of the functional vinculin protein in zebrafish embryos and that this is not compensated for by increased expression of vinculin B."]
  [PMID:28767718 "First of all, we did not find evidence for upregulated expression of vinculin B in the vcla mutants (Fig 5A)."]

**What the compensation data do not show**

- They do not show that Vclb protein performs Vcla's work. No study has compared a vcla RNA-less
  homozygote with a PTC homozygote for a phenotype. The only published RNA-less vcla data are
  expression data.
- The hu10818 allele was not tested for mRNA decay or vclb upregulation. The El-Brolosy alleles were
  not tested by Western blot. The two observations, more vclb mRNA and no more vinculin protein, come
  from different alleles and different labs. They have not been reconciled.
- vclb mutants have not been tested for vcla upregulation.

## 5. Fate classification

**MIXED: a conserved protein with an expression-biased PARTITION. Backup of vcla by vclb is possible
but not demonstrated. Confidence: moderate.**

**Established**

- Both proteins keep the vinculin binding regions and localize the same way to focal adhesions and to
  alpha-catenin-dependent adherens junctions (section 2).
- vclb has an essential role that vcla does not cover: coronary and epicardial development and juvenile
  survival. vcla is not expressed in the epicardium, so this fits an expression partition, not a
  protein difference (PMID:27578788).
- vcla is dispensable on its own, even in maternal-zygotic mutants (PMID:28767718).
- Losing both copies produces phenotypes that neither single mutant has: undetectable vinculin,
  vascular leakage, delayed sprouting, and death of all double mutants before adulthood. The
  vcla-/-;vclb+/- genotype already leaks. So the copies share work in the embryonic vasculature and
  their doses add up there (PMID:36260739).
- vcla PTC alleles cause decay-dependent transcriptional adaptation of vclb. RNA-less vcla alleles do
  not (PMID:30944477, PMID:36427314).

**Inferred, not shown**

- That vclb *protein* compensates for loss of vcla. The strongest direct test, a Western blot, was
  negative. Transcriptional adaptation is a response of the locus to mRNA decay and is sequence-guided.
  It would happen whether or not Vclb could do Vcla's job. The El-Brolosy paper uses it to explain
  phenotype masking in general, but for vcla no masked phenotype has been uncovered.
- That the two proteins are fully interchangeable. This rests on the MDCK assay, done in cells that
  still had their own vinculin, and on sequence. F822 in vclb is untested in vivo.
- That the vcla-biased expression reflects a real vcla specialization, such as metavinculin in muscle.
  This is suggested by the metavinculin exon being annotated only at vcla, but it has not been shown.

**Why not the other fates**

- *Innovation.* Nothing shows a function absent from single-copy vertebrate vinculin. Coronary
  vessels, epicardium, endothelial junctions and heart are all places where vinculin acts in mammals.
  With no gar data, a teleost gain cannot be claimed.
- *Pure backup.* This is ruled out by the lethal vclb single mutant.
- *Pure dosage.* A dosage effect exists in the vasculature, but it cannot explain the copy-specific
  vclb lethality.

**What would change the call**

- A vcla RNA-less homozygote with a cardiac, muscle or vascular phenotype that PTC alleles lack would
  make masking real and support a backup component.
- Rescue of vclb mutant coronary defects by vcla expressed from vclb regulatory elements would confirm
  a pure expression partition. Failure to rescue, for example because of F822 and beta-catenin, would
  add a protein-level component.
- Gar vinculin expression in the epicardium and endothelium would anchor the ancestral state.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** Every IEA and IBA row is present on both copies and was reviewed with the
same wording. This covers:

- molecular function: actin filament binding, actin binding, alpha-catenin binding;
- cell adhesion;
- location: focal adhesion, adherens junction, cell-cell contact zone, cytoskeleton, plasma membrane,
  and the non-core muscle locations myofibril and sarcolemma.

Each copy has its own IDA for adherens junction from the same MDCK assay (PMID:28767718). Both copies
therefore appear among the PAINT descendant evidence for the adherens junction IBA, which is expected
and not circular. The same-node IBA is right for this pair: the protein is conserved and both copies
behave the same in the one direct test. The same "over-annotated" calls were made on both copies:
structural molecule activity (a vague parent of the linker function) and perinuclear region. For
consistency, I added the same NEW term to both copies: GO:0061028 establishment of endothelial barrier,
as IGI from the double-mutant leakage data (PMID:36260739). The in vivo evidence needs loss of both
copies.

**Asymmetric, and correctly so.**

- Coronary vasculature morphogenesis and heart development (IMP) are on vclb only. The vclb single
  mutant defines them, and vcla is not expressed in the epicardium. I did not propagate them to vcla.
- Beta-catenin binding (IBA) was accepted for vcla and left UNDECIDED for vclb. The PAINT node is sound,
  but vclb carries F at Y822, a residue whose phosphorylation mammalian work links to this particular
  interaction. This is the one row where same-node IBA propagation may overstate the pair's
  equivalence. Before marking it, I checked the substitution directly
  (propagation_review, residue claim SUBSTITUTED).

**Asymmetries that come from which copy was studied or which construct was used, not from biology.**

- All the vcla-only biological process IMPs rest on reagents rather than vcla-specific biology:
  - heart contraction and sarcomere organization rest on a zygotic vcla morpholino. I marked them
    UNDECIDED because the mutants contradict them but the possibility of masking has not been
    excluded.
  - membrane repolarization rests on the same kind of morpholino evidence. I marked it
    MARK_AS_OVER_ANNOTATED, because it is a downstream readout and vinculin does no work in
    repolarization.
  - atrioventricular valve morphogenesis rests on a DN head domain cloned from vcla. I marked it
    KEEP_AS_NON_CORE. The DN blocks vinculin generally, vclb is the copy expressed in the heart, and
    vclb single mutants have no strong valve defect.

  None of these was added to vclb.
- The vcla focal-adhesion IDA/IMP rows come from a cardiac antibody study (PMID:26954676) whose antibody
  does not tell the paralogs apart. The location is correct for both copies anyway. vclb has the
  equivalent location through its IBA and IEA rows, and endothelial Vinculinb-eGFP marks focal
  adhesions (PMID:36314606).

**Should be copy-specific:** coronary vasculature and epicardial roles (vclb).

**Should be shared:** vinculin molecular function; focal adhesion and adherens junction location; cell
adhesion; endothelial barrier. Cardiac contractility and myofibril maturation should also be shared if
the Fukuda 2019 data (paralog not stated in the abstract) turn out to come from double mutants.

## 7. Open questions

- Does a vcla RNA-less homozygote, alone or with one vclb allele, show cardiac or muscle phenotypes
  that PTC alleles hide? This is the decisive test of whether transcriptional adaptation of vclb
  actually masks anything.
- Does the rise in vclb mRNA in vcla bns241 mutants give more Vclb protein, measured with a
  paralog-specific tag in tissues where the copies overlap?
- Is vcla upregulated in vclb PTC mutants, and does it explain why their cardiac muscle is "relatively
  normal"?
- Does Vclb (F822) bind beta-catenin? Does an F822Y vclb knock-in change junction behaviour?
- Which copy makes metavinculin in adult heart and skeletal muscle?
- Which allele and which copies did Fukuda et al. 2019 use for the myofilament-maturation phenotype?

## References

PMID:19800866, PMID:24952909, PMID:26954676, PMID:27578788, PMID:28767718, PMID:30635353,
PMID:30944477, PMID:31495694, PMID:35417696, PMID:36260739, PMID:36314606, PMID:36427314,
PMID:38697108, PMID:40128410. Also the files `panther_tgd_pairs.tsv`,
[annotation-comparison.md](annotation-comparison.md) and
[vcla-bioinformatics/RESULTS.md](../../../../genes/DANRE/vcla/vcla-bioinformatics/RESULTS.md).
