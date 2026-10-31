# DPAGT1 (GPT / Q9H3H5) review notes

Human UDP-N-acetylglucosamine--dolichyl-phosphate N-acetylglucosaminephosphotransferase
(GlcNAc-1-P transferase, GPT). HGNC:2995. EC 2.7.8.15. 408 aa, 10-TM polytopic ER
membrane protein. Deep research (falcon) unavailable — provider out of credits (HTTP 402).
Review grounded in DPAGT1-uniprot.txt, DPAGT1-goa.tsv, and cached publications.

## Core biology (verified)
- Catalyses the FIRST and COMMITTED step of dolichol-linked oligosaccharide (LLO)
  assembly for N-linked glycosylation. On the cytosolic face of the ER membrane it
  transfers GlcNAc-1-P from UDP-GlcNAc onto dolichyl phosphate (Dol-P), yielding
  GlcNAc-PP-dolichol (Dol-PP-GlcNAc).
  [PMID:29459785 "catalyzes the first and committed step of N-linked glycosylation on the cytosolic face of endoplasmic reticulum (ER) membrane"]
  [PMID:30388443 "It catalyzes the transfer of an N-acetyl-D-glucosamine-1-phosphoryl unit (GlcNAc-1-P) from UDP-N-acetyl glucosamine (UDP-GlcNAc) onto dolichyl phosphate (Dol-P)"]
- Mg2+-dependent; homodimer; 10 TM helices; inhibited competitively by tunicamycin
  (structural analog / competitor of UDP-GlcNAc). PDB structures 5LEV/5O5E/6BW5/6BW6/6FM9/6FWZ.
  [PMID:29459785 "Magnesium is a required cofactor for GPT"]
- GO MF term used by GOA and for core_functions: GO:0003975
  "UDP-N-acetylglucosamine-dolichyl-phosphate N-acetylglucosaminephosphotransferase activity"
  (label confirmed current in local go.db).
- BP: GO:0006488 dolichol-linked oligosaccharide biosynthetic process (IDA PMID:29459785);
  GO:0006487 protein N-linked glycosylation (IMP PMID:19549906).
- CC: GO:0005789 endoplasmic reticulum membrane; multi-pass.

## Disease
- DPAGT1-CDG / CDG type Ij (CDG1J, MIM:608093) — GPT activity reduced to ~10% in patient
  fibroblasts, Y170C etc. [PMID:12872255]
- Congenital myasthenic syndrome 13 (CMS13/CMSTA2, MIM:614750), limb-girdle with tubular
  aggregates. [UniProt DISEASE; Reactome R-HSA-4549334; PMID:30388443]

## Annotation-specific notes
- GO:0003976 (UDP-N-acetylglucosamine-LYSOSOMAL-ENZYME N-acetylglucosaminephosphotransferase
  activity), IDA, PMID:6289658, assigned by MGI. This is the activity of the DISTINCT
  lysosomal-enzyme-targeting GlcNAc-1-phosphotransferase (GNPTAB/GNPTG; the I-cell disease
  / mucolipidosis II-III enzyme). PMID:6289658 (Varki et al.) is entirely about I-cell
  disease / pseudo-Hurler polydystrophy heterozygote assays of that lysosomal enzyme, NOT
  about DPAGT1's dolichol-P GlcNAc transferase. DPAGT1 transfers GlcNAc-1-P to a lipid
  (dolichyl phosphate), not to lysosomal-enzyme mannose-6-phosphate recognition markers.
  This is a wrong-function annotation (different enzyme). Marked MARK_AS_OVER_ANNOTATED
  (per policy, not REMOVE for an experimental annotation) — it is not DPAGT1's function.
- GO:0005515 protein binding (IPI, PMID:32814053, with UniProtKB:P42858 = HTT) — bare
  "protein binding" from a large-scale neurodegeneration Y2H/interactome screen; single
  HTT interaction, no functional MF. MARK_AS_OVER_ANNOTATED (uninformative per curation
  guidelines; do not REMOVE an IPI).
- GO:0042802 identical protein binding (ISS, GO_REF:0000024, from P24140) — supported by
  homodimer biology (UniProt SUBUNIT: Homodimer; PMID:29459785/30388443 crystallized as
  homodimer). ACCEPT as non-core (structural/quaternary, not the catalytic core function).
- GO:0016780 "phosphotransferase activity, for other substituted phosphate groups" (IEA
  InterPro) — correct but a parent/less-specific class of GO:0003975. MODIFY -> GO:0003975.
- GO:0016020 membrane (IBA/IEA/ISS/IDA) — correct but generic; ER membrane (GO:0005789) is
  the informative term. Keep as accept/non-core; ER membrane is core CC.
- GO:0043231 intracellular membrane-bounded organelle (IDA PMID:12872255) — very generic
  CC, subsumed by ER membrane. KEEP_AS_NON_CORE.


## 2026-10-18 — Source-preserving augmentation

The earlier review was approved at PR [2012](https://github.com/ai4curation/ai-gene-review/pull/2012), head `2c35594b374ed473c9640c99ea76d9bbfe1160a0`, and merged as `b112b563467825fa9422721824f5f7cb221263b4`. Its original notes above remain unchanged. A shallow local history boundary at PR 3214 was not the DPAGT1 review event; the remote path history and exact approved blobs establish the earlier provenance. Prior approval is retained without treating the INITIALIZED status or merge alone as completion of the present audit.

The 26 historical source identities are retained. Ordinary current fetching supplies three additional source objects: a separate P24140 ISS ER-membrane donor, a Golgi IEA transfer and an InterPro membrane mapping. Only the old membrane/IEA/GO_REF:0000120 identity is absent from the current snapshot and is marked retired as source lifecycle; its positive membrane-to-ER biological refinement remains. The genuine current GOA replaces the machine snapshot, while the [historical snapshot](source-snapshots/DPAGT1-goa-before-2026-10-18-augmentation.tsv) is byte-exact. The [provenance record](DPAGT1-source-provenance.yaml) supplies hashes, source mapping and acquisition details. There are 29 reviewed source objects and no new authored annotation.

The two former core blocks describe the same enzyme step and are consolidated. DPAGT1 transfers GlcNAc-1-phosphate to dolichyl phosphate; downstream enzymes extend the glycan and transfer it to protein. GO:0006488 is already within protein N-linked glycosylation, and GO-CAM 65c57c3400000687 models the target performing this step. The E-cadherin study (PMID:19549906, Methods and Results/Figures 1–4) measures human-cell glycan and junctional effects after DPAGT1 perturbation; it does not turn DPAGT1 into a direct protein-glycan transferase or a separate adhesion enzyme.

The earlier treatment of GO:0003976 is superseded by examination of the full 1982 original. Its Methods (pp. 718–720), Results/Figure 1 and Discussion (pp. 720–725) assay alpha-methylmannoside and endogenous glycoprotein acceptors in human cell extracts. This is the lysosomal phosphomannosyl-targeting reaction, distinct from the Dol-P acceptor reaction of DPAGT1. The historical source row remains intact with REMOVE and a MISCITED reference assessment. The experiments are not claimed false, and the 1982 paper is not claimed to have identified modern GNPT genes. The author-hosted [complete original PDF](https://cmm.ucsd.edu/research/labs/varki/_files/publications/a014.pdf) makes this distinction inspectable.

The positive HTT yeast two-hybrid records are retained as non-core binding, superseding the older genericity-only over-annotation rationale. The tested HTT fragment/modifications and the absence of demonstrated native ER function remain explicit. Self-association is refined to homodimerization, but the two structural papers disagree about the Cys106 intersubunit disulfide: PMID:30388443 favors predominantly noncovalent dimers under its tested conditions. The finding-level assessment preserves both valid catalytic studies.

The 400-residue historical clone in PMID:9451016 is traceable through the primary [CAB04787.1 ENA record](https://www.ebi.ac.uk/ena/browser/view/CAB04787.1). It corresponds to canonical residues 9–408, with the documented clone Leu25/current Arg33 difference, rather than being inferred from a structural model ending at residue 400. The natural 301-residue product is not equivalent to a full-length experimental construct. In PMID:30388443, elevated purified activity of some clinical variants coexists with exon-trap splicing defects; disease association does not imply every mutant has reduced intrinsic turnover. PMID:22742743 also cautions that tunicamycin rescue can reflect inhibitor buffering, including by catalytically inactive constructs.

The new Golgi source remains UNDECIDED. Its mouse donor is traceable to an MGI IPI annotation citing PMID:36074821, but target-specific supplementary evidence could not be inspected. Main-text LYSET–GNPTAB experiments do not by themselves settle DPAGT1 attribution, and established ER residence does not exclude a Golgi pool. No new process or localization is invented to fill this uncertainty.

The [source evidence guide](DPAGT1-source-evidence.md) distinguishes actual original reads from abstract-only and unavailable supplementary material. Genuine Falcon and fallback attempts failed authentication/quota checks; no provider report was authored or substituted. Previously cached source text, prior histories and the original UniProt record remain unchanged. The only newly reproduced source excerpt is the nine-word noncovalent-dimer anchor in the finding assessment; historical quotations remain a separate inventory and are not represented as collectively below 25 words per source.


## HTT interaction evidence anchor (2026-10-18)

The non-core protein-binding row now includes a short target-specific excerpt from the existing UniProt interaction record. It identifies DPAGT1 and HTT alongside the reported experiment count. The three public IntAct records and the original automated Y2H Methods remain the evidence for the assay interpretation described in the [source guide](DPAGT1-source-evidence.md). The earlier fly-screen excerpt is retained as general study context; it does not identify the target pair by itself. Table S2 was not separately recovered, and no target-specific mammalian or native ER interaction is claimed.

This follow-up reproduces four additional words from the existing UniProt source once. It preserves all prior quoted passages and their separately recorded historical totals; it adds no publication quotation or biological assertion.
