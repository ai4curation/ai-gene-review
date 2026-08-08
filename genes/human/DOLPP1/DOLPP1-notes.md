# DOLPP1 (Dolichyldiphosphatase 1) — review notes

UniProt: Q86YN1 (DOPP1_HUMAN). Gene symbol DOLPP1 (synonym LSFR2). HGNC:29565. GeneID 57171. Chromosome 9.
EC 3.6.1.43. Pharos target development level: **Tdark** (poorly characterized).

## Identity and family

- RecName "Dolichyldiphosphatase 1"; AltName "Dolichyl pyrophosphate phosphatase 1"; EC=3.6.1.43
  [file:human/DOLPP1/DOLPP1-uniprot.txt "RecName: Full=Dolichyldiphosphatase 1;" ... "EC=3.6.1.43;"].
- Belongs to the dolichyldiphosphatase family [file:human/DOLPP1/DOLPP1-uniprot.txt "Belongs to the dolichyldiphosphatase family."].
- Domain architecture: PAP2 / lipid-phosphatase (acid phosphatase / vanadium-dependent haloperoxidase) superfamily.
  UniProt DR records: CDD cd03382 "PAP2_dolichyldiphosphatase"; Pfam PF01569 "PAP2"; SMART SM00014 "acidPPc";
  InterPro IPR039667 "Dolichyldiphosphatase_PAP2", IPR000326 "PAP2/HPO"; Gene3D 1.20.144.10
  [file:human/DOLPP1/DOLPP1-uniprot.txt "CDD; cd03382; PAP2_dolichyldiphosphatase; 1."].
- Yeast/mouse ortholog is CWH8 / mouse Dolpp1 (Q9JMF7). Human isoform-1 mRNA originally submitted as
  "Dolichyl pyrophosphate phosphatase (human CWH8)" [file:human/DOLPP1/DOLPP1-uniprot.txt "Dolichyl pyrophosphate phosphatase (human CWH8)."].

## Molecular function

- Catalytic activity (ECO:0000250, by similarity to mouse Q9JMF7):
  a di-trans,poly-cis-dolichyl diphosphate + H2O = a di-trans,poly-cis-dolichyl phosphate + phosphate + H(+);
  RHEA:14385; EC=3.6.1.43
  [file:human/DOLPP1/DOLPP1-uniprot.txt "Reaction=a di-trans,poly-cis-dolichyl diphosphate + H2O = a di-"].
- FUNCTION: "Required for efficient N-glycosylation. Necessary for maintaining optimal levels of dolichol-linked
  oligosaccharides. Hydrolyzes dolichyl pyrophosphate at a very high rate and dolichyl monophosphate at a much
  lower rate. Does not act on phosphatidate (By similarity)."
  [file:human/DOLPP1/DOLPP1-uniprot.txt "Hydrolyzes dolichyl pyrophosphate at a very high rate and dolichyl"].
- The primary physiological substrate is dolichyl diphosphate (Dol-PP); Dol-P is a much weaker substrate; the
  enzyme does not act on phosphatidate, distinguishing it from the related PAP2 lipid phosphate phosphatases.
- Correct GO MF term: **GO:0047874 dolichyldiphosphatase activity** (def: "Catalysis of the reaction:
  a di-trans,poly-cis-dolichyl diphosphate + H2O = a di-trans,poly-cis-dolichyl phosphate + phosphate + H+"),
  verified in go.db; parent is GO:0120556 polyprenyl diphosphate phosphatase activity; sits under GO:0003674.
  NOTE: GO:0004582 is NOT this enzyme — it is "dolichyl-phosphate beta-D-mannosyltransferase activity" (verified go.db).

## Biological process

- Dol-PP is released into the ER after the lipid-linked oligosaccharide (LLO) Glc3Man9GlcNAc2-PP-Dol is
  transferred to nascent glycoproteins by oligosaccharyltransferase during N-linked glycosylation. DOLPP1
  dephosphorylates Dol-PP → Dol-P + Pi, recycling/regenerating the Dol-P glycan-carrier pool for another
  round of LLO synthesis. This is the "salvage" arm of dolichyl-phosphate synthesis.
- Reactome R-HSA-446199 "Synthesis of dolichyl-phosphate": "Dolichyl phosphate can be obtained either from
  direct phosphorylation of dolichol ... or a salvage reaction by de-phosphorylation of dolichyl diphosphate,
  released at the end of N-glycan biosynthesis (Cantagrel & Lefeber 2011)."
  [reactome/R-HSA-446199.md].
- PATHWAY: "Protein modification; protein glycosylation." [file:human/DOLPP1/DOLPP1-uniprot.txt
  "Protein modification; protein glycosylation."]. UniPathway UPA00378.
- GO BP terms in GOA: GO:0006487 protein N-linked glycosylation (the process DOLPP1 supports), and
  GO:0043048 dolichyl monophosphate biosynthetic process (Reactome TAS; the direct product of DOLPP1 is Dol-P).

## Subcellular location

- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane (ECO:0000250); Multi-pass membrane protein (ECO:0000250)
  [file:human/DOLPP1/DOLPP1-uniprot.txt "Endoplasmic reticulum membrane"].
- Four predicted TM helices (33-53, 100-120, 130-150, 162-182) [file:human/DOLPP1/DOLPP1-uniprot.txt
  "TRANSMEM        33..53"]. Keywords: Endoplasmic reticulum; Membrane; Transmembrane; Transmembrane helix; Hydrolase.
- Correct GO CC: GO:0005789 endoplasmic reticulum membrane.

## Isoforms

- Two isoforms by alternative splicing. Isoform 2 (Q86YN1-2) has residues 155-197 Missing (VSP_042210),
  which deletes TM helix 162-182 and adjacent sequence, likely disrupting the functional multi-pass
  architecture [file:human/DOLPP1/DOLPP1-uniprot.txt "VAR_SEQ         155..197"].

## Evidence status / caveats

- All human GO annotations are IBA / IEA / ISS / TAS. There are no human experimental (IDA/IMP/etc.)
  annotations. The UniProt FUNCTION and CATALYTIC ACTIVITY are propagated "By similarity" from mouse Q9JMF7,
  which is itself the WITH/FROM basis of the human ISS/IEA calls.
- PE 1 (protein level evidence) reflects proteomic detection, not functional assay.
- Cached publication PMID:15489334 is the MGC full-length cDNA project (large-scale sequencing); it does not
  characterize DOLPP1 function and should not be cited for functional claims.

## Annotation actions summary

- MF dolichyldiphosphatase activity (GO:0047874) x4 (IBA/IEA/TAS/ISS): core; ACCEPT the phylogenetic IBA as
  representative; keep the redundant IEA/ISS/TAS as ACCEPT (own core function, redundant is fine).
- CC endoplasmic reticulum membrane (GO:0005789) x4 (IBA is_active_in; IEA/TAS/ISS located_in): core location; ACCEPT.
- BP protein N-linked glycosylation (GO:0006487) x3 (IBA/IEA/ISS): core biological role; ACCEPT.
- BP dolichyl monophosphate biosynthetic process (GO:0043048) TAS Reactome: correct — Dol-P is the direct
  product; ACCEPT (captures the enzyme's product-forming role).
