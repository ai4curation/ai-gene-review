# sox9a (Q9DFH2) curation notes

## 2026-09-27 — initial review (DANRE_DUPLICATION project, pair sox9a/sox9b)

### Identity and origin
- One of two zebrafish co-orthologs of tetrapod SOX9; alias jellyfish (jef).
  [PMID:12397114 "We show that two alleles of jef contain mutations in sox9a, one of two zebrafish orthologs of the human transcription factor SOX9."]
- Duplicated chromosome segments: [PMID:11180959 "Genetic mapping showed that these two loci reside on chromosome segments that were apparently duplicated in a large-scale genomic duplication event in ray fin fish phylogeny."]
- PANTHER v19 calls the pair `TGD_or_lineage` (duplication on Teleostei|DANRE, one gar co-ortholog, one medaka co-ortholog), see projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv.

### Protein
- HMG box 107-175 (UniProt). Region identity script: `sox9a-bioinformatics/` (HMG box 98.6% identical to Sox9b and human SOX9; whole protein 61.3% vs Sox9b, 70.2% vs human SOX9). Sox9a is the less diverged copy relative to human SOX9.
- Both proteins bind DNA and transactivate: [PMID:11180959 "Both Sox9a and Sox9b proteins bind to the HMG consensus DNA sequences in vitro."]
- ChIP of tagged Sox9a: [PMID:25568117 "ChIP-PCR assay verified 11 of 21 genes for Atoh1a and 11 of 18 genes for Sox9a as reproducible targets"]

### Function
- Cartilage: [PMID:12397114 "These studies show that jef (sox9a) is essential for both morphogenesis of condensations and overt cartilage differentiation."]
- Stacking vs number: [PMID:15689370 "Chondrocytes failed to stack in sox9a mutants, failed to attain proper numbers in sox9b mutants and failed in both morphogenetic processes in double mutants."]
- Glia: [PMID:20023158 "We have shown that in the zebrafish hindbrain, sox9a is necessary for the generation of both OLPs and GS-positive astroglia, supporting a phylogenetically conserved role."]
- Otic: redundancy with sox9b / dlx3b / dlx4b [PMID:12668634 "Removal of dlx3b, dlx4b and sox9a genes together also blocks ear development, although a few residual cells form an otic epithelium."]
- Heart: not required [PMID:23775563 "Knock down of sox9a expression did not cause cardiac malformations, or defects in epicardium development."]
- Gonad: [PMID:15939378 "In adult testes, amh and sox9a were expressed in presumptive Sertoli cells."]
- Deep research (sox9a-deep-research-falcon.md, arrived during review) cites Lin et al. 2021 (Aquaculture and Fisheries, doi:10.1016/j.aaf.2019.12.009, no PMID found in Europe PMC) with CRISPR sox9a frameshift alleles that lose neurocranial and most arch cartilage; not independently verified here.

### Annotation decisions
- REMOVE protein binding (IPI, Ewsa co-IP): uninformative; also the anti-SOX9 antibody was commercial, so the copy detected is unclear.
- cytoplasm (IMP, PMID:12397114) x2: MARK_AS_OVER_ANNOTATED. The paper's observation is about nuclear retention of unspliced sox9a *transcript* after splice-blocking MO, not protein. Sun et al. 2013 (PMID:24263104) reports a cytoplasmic Sox9a protein pool in juvenile gonad, so not removed outright.
- heart development (IBA): MARK_AS_OVER_ANNOTATED for sox9a (paralog-partitioned function; donor is sox9b; sox9a MO had no cardiac effect). Added propagation_review.
- NEW GO:0001228 (transcription activator activity) on both copies, from PMID:11180959.
- Otic, fin, glial, placode terms: KEEP_AS_NON_CORE. Cartilage/chondrocyte: ACCEPT (core).
