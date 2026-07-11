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
