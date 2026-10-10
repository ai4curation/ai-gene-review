# FoxB (Sp-FoxB / Spfkh1, Q9XZM6) — curation notes

## Identity
- UniProt Q9XZM6 (TrEMBL, 360 aa), "Winged helix transcription factor Forkhead-1", gene name
  fkh1 (EMBL AAD34014.1), GeneID 373496. The RX citation is the original cloning paper
  [PMID:10433970 "Spfkh1 is a Strongylocentrotus purpuratus transcription factor that contains a
  winged helix DNA binding domain."], which places the gene in forkhead Class II
  [PMID:10433970 "this gene falls into Class II of the winged helix transcription factors."];
  Class II of the old Kaufmann/Knochel scheme corresponds to the FoxB subclass.
- Mapping to the GRN gene: NCBI Gene 373496 (the GeneID cross-referenced from this UniProt entry,
  checked with eutils esummary on 2026-10-03) carries the alias "FoxB". Minokawa et al. 2004
  re-examined the expression of "SpFoxb" as one of four regulatory genes [PMID:15183312
  "Re-examination of the expression pattern of SpFoxb reveals domains of expression not previously
  reported for this gene"], i.e. the gene was already known in 2004, consistent with it being one
  of the three fox genes known before the genome survey [PMID:17081512 "This genome includes 22
  fox genes, only three of which were previously known."]. Garfield et al. 2012 analysed the
  "FoxB" upstream cis-regulatory region [PMID:23017024 "Patterns of variation in the
  cis-regulatory regions of six of the genes examined (CyIIa, CyIIIa, Endo16, FoxB, AN, and HE)
  are consistent with directional selection."], matching the cis-regulatory region sequenced by
  David et al. 1999. Confidence that fkh1/Q9XZM6 is the foxb node of the Davidson skeletogenic GRN:
  HIGH (GeneID alias + the single Class II / FoxB forkhead gene in the genome + continuity of the
  Spfkh1 -> SpFoxb -> Sp-foxb naming in the Caltech papers).
- Domains (UniProt DR): Fork_head IPR001766 (Pfam PF00250, PROSITE PS50039, residues 13-107);
  PANTHER PTHR11829 (family), subfamily SF377. No GO-CAM contains this gene
  (`gocams/index.tsv` has no STRPU rows).

## Molecular features (David et al. 1999, abstract only in cache)
- Single ORF encoding DNA-binding domain, NLS and transactivation domain [PMID:10433970 "Spfkh1
  is transcribed in one open reading frame that contains the DNA binding domain, nuclear
  localization signal and transactivation domain."]; 40.7 kDa, pI 9.96.
- Promoter region contains many predicted TF binding sites, including sites for Wnt/beta-catenin
  and hedgehog pathway effectors [PMID:10433970 "Included among these are binding sites for
  factors downstream of the Wnt/beta-catenin and hedgehog signaling pathways, implicating these
  pathways in both regulation of Spfkh1 and specification of endoderm."]. This 1999 inference of an
  endodermal role was made before the GRN work placed the gene in the skeletogenic lineage.

## Place in the skeletogenic (micromere/PMC) GRN
- foxb is a late-tier regulatory gene of the skeletogenic micromere lineage, downstream of the
  double-negative-gate outputs tbr and alx1 [PMID:18413610 "The tbr and alx1 genes also provide
  inputs into the additional skeletogenic differentiation genes dri and foxb."]. Nam & Davidson
  2012 describe the same wiring [PMID:22238426 "The final tier of regulators of skeletogenesis,
  foxO , foxB , and deadringer , are activated by the inputs that have become available."].
- Oliveri et al. 2008 originally proposed a feed-forward (Ets1 > Alx1 > target) regulation of
  Sp-foxb together with the biomineralization genes msp130 and msp103L; Shashikant et al. 2018
  recall this [PMID:29558892 "a feedforward mechanism originally proposed by Oliveri and
  co-workers to account for the regulation of Sp-msp130, Sp- msp103L, and Sp-foxb [11] may
  control a large fraction of the effector genes in the PMC GRN"].
- Output: FoxB is listed among the regulatory-state components whose products are required as
  drivers of the skeletogenic differentiation gene batteries (perturbation data in Oliveri 2008
  Table S1, not in the cached text) [PMID:18413610 "these differentiation genes require as drivers
  products of all of the now familiar components of the skeletogenic regulatory state ( alx1 ,
  ets1 , tbr , tel , erg , hex , foxb , dri ) and in addition a factor that is at this stage
  ubiquitously present, Hnf6 ( 42 )."]. These differentiation genes are the biomineral genes
  [PMID:18413610 "the activation of the sets of genes ( 22 ) that actually constitute the
  skeletal biomineral and cause the cells to execute the many cell biology functions required for
  skeletal deposition."].
- Expression: the GRN papers describe foxb as transcribed in the micromere/skeletogenic lineage
  (Oliveri 2008 Figs. 2, 3, 6). Minokawa 2004 reports additional expression domains
  [PMID:15183312 "Re-examination of the expression pattern of SpFoxb reveals domains of
  expression not previously reported for this gene"], but the cached record is abstract-only, so
  the later (oral ectoderm/stomodaeal, endodermal) domains mentioned in the orchestrator's brief
  cannot be quoted from the cache and are not asserted in the review.

## PMC epithelial-mesenchymal transition (Lytechinus variegatus)
- Saunders & McClay 2014 knocked down 13 skeletogenic TFs in L. variegatus [PMID:24598159 "To
  observe regulatory control of EMT directly, we used the sea urchin Lytechinus variegatus"] and
  found foxb required for PMC EMT [PMID:24598159 "Three TFs highest in the GRN specified and
  activated EMT (alx1, ets1, tbr) and the 10 TFs downstream of those (tel, erg, hex, tgif, snail,
  twist, foxn2/3, dri, foxb, foxo) were also required for EMT."], specifically in the apical
  constriction sub-circuit [PMID:24598159 "apical constriction is controlled by a complex forward
  cascade that feeds into five terminal TFs: tel, hex, foxn2/3, foxb and foxo."].
- This is the Lv orthologue, so it is recorded here and in suggested_questions rather than as an
  S. purpuratus NEW annotation.

## Curation decisions (2026-10-03)
- IBA rows (0000981, 0000978, 0005634, 0006357) accepted: family-level winged-helix DNA binding
  and nuclear TF function are consistent with the cloning paper and GRN role.
- IEA generic rows (0003677, 0003700, 0006355) MODIFY to the specific RNA pol II terms already on
  the gene / proposed; 0043565 and 0005634 (IEA) accepted.
- IBA 0030154 cell differentiation MODIFY -> GO:0070169; IBA 0009653 kept as non-core.
- NEW: GO:0045944 (IMP, Oliveri 2008) and GO:0070169 (IMP, Oliveri 2008), both minimal and
  resting on the perturbation data summarised in Oliveri 2008.
- Not proposed: EMT terms (Lv data only), endoderm terms (1999 in silico promoter inference only),
  activator MF GO:0001228 (no reporter/site-mutation evidence for FoxB itself).
