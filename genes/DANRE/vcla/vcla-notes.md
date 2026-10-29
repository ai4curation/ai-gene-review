# vcla notes (Danio rerio, vinculin a; UniProt B3DI32)

## 2026-09-28 — session log

**Deep research:** FAILED for this gene (Edison/Falcon returned 402 Payment Required; the OpenAI key is
invalid). Not retried, per instructions. No `-deep-research-*.md` file exists; literature research below
was done manually from cached publications and Europe PMC searches.

Accession: B3DI32 (TrEMBL, 1131 aa) holds the ZFIN experimental and IBA GOA rows for vcla. It is the
metavinculin-type isoform (carries the metavinculin insert; see `vcla-bioinformatics/RESULTS.md`).

### Identity and TGD origin
- PANTHER call `TGD_tree` (Neopterygii|Teleostei, 1:1, PTHR46180), one gar co-ortholog, two medaka
  co-orthologs (projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv).
- Paralog vclb on chr12; vcla on chr13 [PMID:28767718 "The first isoform, vinculin a (vcla) present on chromosome 13, was well annotated, while its paralog vinculin b (vclb) on chromosome 12 was not (as of assembly Zv9)."]
- [PMID:28767718 "Both zebrafish vcla and vclb show a high sequence conservation at the protein level (87% and 86% identical amino acids respectively) with mammalian vcl (Fig 1A)."]

### Protein
- Key D1 residue conserved [PMID:28767718 "The key residue of which mutation perturbs all of these interactions, A50, is fully conserved [47,48]."]
- Only notable difference: vclb Y822F [PMID:28767718 "The one notable difference between zebrafish vinculin A and B is the change of the otherwise conserved Y at position 822 to F in vinculin B."]
- My alignment (vcla-bioinformatics): vcla B3DI32 contains the metavinculin insert; Y822 retained in vcla.

### Localization
- vcla-GFP in MDCK: focal adhesions + adherens junctions via alpha-catenin VBS [PMID:28767718 "In α-catenin rescued cells, both vinculin A and vinculin B localize to integrin-based Focal Adhesion structures, as well as to the punctate Focal Adherens Junctions as evidenced by colocalization with α-catenin"]
- Excluded from junctions with alpha-catenin-dVBS [PMID:28767718 "Here it is apparent that both vinculin A and vinculin B are now excluded from Focal Adherens Junctions and Linear Adherens Junctions (arrows), but are still present in Focal Adhesions (arrows)."]
- Notochord sheath: vcla transcripts enriched [PMID:38697108 "We found a significant enrichment of transcripts for focal adhesion proteins including, vcla, pxna, zyx, tln2a, and ptk2ab (Figure 4B)."]

### Expression vs vclb
- Heart: vcla low, vclb predominant [PMID:30635353 "The microarray data show that tln1 and apbb1ip are expressed at high levels in embryonic hearts (Fig. S1 A), but vcla is expressed at low levels (data not shown); no probe for vclb was included in the array."]
- But Cheng 2016: vcla expressed in myocardium, not epicardium [PMID:27578788 "probably owing to redundancy with Vcla, a vinculin paralog that is expressed in the myocardium but not epicardium"]

### Mutants
- Han 2017 vcla hu10818 (Δ8, PTC at 160). MZvcla viable, no defects [PMID:28767718 "Taken together, the results show that vcla is not essential for zebrafish development or adult life."]
- Western: no vclb protein compensation [PMID:28767718 "This result strongly indicates that mutation of the vcla gene leads to loss of most of the functional vinculin protein in zebrafish embryos and that this is not compensated for by increased expression of vinculin B."]
- Double (MZvcla; Zvclb) mutants: mild transient cardiac edema, normal skeletal muscle; no adult double mutants [PMID:28767718 "Remarkably, during fin clipping no vcla-/-vclb-/- fish were detected (172 adults screened out of three different pairings), while the remaining vcla-/- and vcla-/-vclb+/- siblings roughly show a Mendelian distribution."]
- Han consider the vcla MO phenotypes (Vogel 2009) most likely non-specific [PMID:28767718 "While we cannot fully exclude the latter, the most likely explanation is that the reported effects of the used vinculin A morpholinos are non-specific."]
- Morpholino (ZDB-MRPHLNO-100114-3) phenotypes: contractile dysfunction (PMID:19800866, PMID:26954676), repolarization (PMID:24952909). These are the basis of the IMP rows for heart contraction, sarcomere organization, repolarization. Disputed by mutants; see review.

### Transcriptional adaptation (TA)
- El-Brolosy 2019: vclaΔ13 (bns241) upregulates vclb [PMID:30944477 "hbegfa, vcla, hif1ab, vegfaa, egfl7 and alcama zebrafish mutants exhibit increased mRNA levels of a paralogue or family member (hereafter referred to as ‘adapting gene’), namely hbegfb, vclb, epas1a and epas1b, vegfab, emilin3a and alcamb, respectively"]
- vclasa14599 (PTC without mRNA decay) no TA [PMID:30944477 "Notably, while analyzing various mutant alleles, we found that unlike hbegfaΔ7 and vclaΔ13, two other PTC bearing alleles, hbegfasa18135 and vclasa14599, do not display transcriptional adaptation"]
- NMD dependence tested with upf1 in vcla [PMID:30944477 "To investigate the role of the mRNA surveillance machinery in transcriptional adaptation, we genetically inactivated Upf1, a key non-sense mediated decay (NMD) factor6, in hbegfaΔ7, vegfaa and vclaΔ13 zebrafish mutants."]
- vcla heterozygotes also adapt [PMID:30944477 "Moreover, we found that vcla, hif1ab and egfl7 heterozygous animals also display transcriptional adaptation, albeit less pronounced than that observed in the homozygous mutants"]
- Antisense at vclb locus down [PMID:30944477 "Notably, we also observed a downregulation of anti-sense transcripts at the hbegfb and vclb loci in hbegfaΔ7 and vclaΔ13 mutants, respectively"]
- RNA-less vcla allele (72.44-kb locus deletion) does NOT display TA; wild-type offspring of PTC heterozygotes show inherited vclb upregulation (Jiang 2022) [PMID:36427314 "In addition, we generated an RNA-less allele of vcla (a 72.44-kb deletion that removes the vcla locus; fig. S3, C and D) and found that it does not display TA (fig. S3E)."] [PMID:36427314 "Notably, we observed increased mRNA levels of the adapting genes, alcamb, vclb, emilin2a/emilin3a, and adh1a3, in the wild-type offspring from intercrosses of alcama, vcla, egfl7, and aldh1a2 heterozygous zebrafish, respectively"]
- Cas13d cleavage of vcla mRNA also raises vclb [PMID:40128410 "Kushawah et al (2020) have previously shown that Cas13d can degrade specific mRNAs in zebrafish embryos and that vclb mRNA levels increase after the cleavage of vcla mRNA, similar to our observations in vcla mutant zebrafish that display mutant mRNA decay (El-Brolosy et al, 2019)."]
- Key point: TA is triggered by mutant mRNA decay, not by loss of protein. It shows the vclb locus responds to vcla transcript decay; it does not by itself show that Vclb protein substitutes functionally. Han's Western (different PTC allele, hu10818) found no rise in total vinculin protein.

### Double mutant vascular phenotypes (both copies)
- [PMID:36260739 "Our analysis shows that vcla−/−;vclb+/−and vcl full-KO embryos exhibited increased perivascular dextran levels (Fig."] -- small-molecule leakage; vcla-/-;vclb+/- already affected (dose).
- Kotini 2022 (abstract only): vinculin deletion prevents junctional finger formation in ISVs, rescued by endothelial vinculin [PMID:35417696 "Furthermore, genetic deletion of vinculin prevents finger formation, a junctional defect that could be rescued by transient endothelial expression of vinculin."]

### Heart valve (GOA IMP)
- DN construct derived from vcla head domain [PMID:30635353 "To generate the DN Vinculin transgene, the first 774 bp of the vcla coding sequence was amplified by PCR using the following primers"]. It blocks vinculin binding partners generally; it does not show which endogenous copy acts. vclb mutants had no strong valve delay.

### Decisions summary
- MF (actin filament binding, alpha/beta-catenin binding): accept (IBA/IEA, domain conservation).
- CC focal adhesion, adherens junction, cell-cell contact zone, cytoskeleton: accept.
- MO-based BP (heart contraction, sarcomere organization): UNDECIDED (morpholino vs mutant conflict; Fukuda 2019 reports VCL essential for cardiomyocyte myofilament maturation but abstract does not name paralog/allele).
- Repolarization: MARK_AS_OVER_ANNOTATED.
- AV valve morphogenesis: KEEP_AS_NON_CORE (DN evidence speaks to vinculin, not specifically vcla).
- NEW: establishment of endothelial barrier (GO:0061028), IGI with vclb (PMID:36260739).
