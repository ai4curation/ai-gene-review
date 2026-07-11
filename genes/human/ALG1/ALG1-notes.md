# ALG1 (Q9BT22) review notes

Human ALG1 = chitobiosyldiphosphodolichol beta-mannosyltransferase (EC 2.4.1.142; RHEA:13865),
a.k.a. beta-1,4-mannosyltransferase / GDP-Man:GlcNAc2-PP-dolichol mannosyltransferase / MT-1.
HGNC:18294. CAZy GT33 (glycosyltransferase group 1 family, GT33 subfamily). 464 aa, chromosome 16.

## Core biology (verified)

- Catalyzes the FIRST mannose-addition step of dolichol-linked oligosaccharide (LLO / DLO) assembly:
  transfer of the first mannose from GDP-mannose onto the chitobiose core (GlcNAc2-PP-dolichol),
  forming Man1GlcNAc2-PP-dolichol, on the cytoplasmic (cytosolic) face of the ER membrane.
  [file UniProt Q9BT22 FUNCTION: "Catalyzes, on the cytoplasmic face of the endoplasmic reticulum,
  the addition of the first mannose residues to the dolichol-linked oligosaccharide chain, to produce
  Man1GlcNAc(2)-PP-dolichol core oligosaccharide."]
  [PMID:26931382 "encodes an ER localized β1,4 mannosyltransferase that catalyzes the transfer of the
  first of nine Man moieties onto the growing DLO"]
- Man1GlcNAc2-PP-dolichol is the substrate for ALG2, the next enzyme (UniProt FUNCTION).
- CATALYTIC ACTIVITY (UniProt / RHEA:13865): an N,N'-diacetylchitobiosyl-diphospho-dolichol +
  GDP-alpha-D-mannose = beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-dolichol +
  GDP + H+. EC 2.4.1.142. Direct enzymatic evidence from PMID:14973778 (patient fibroblast extracts,
  [14C]GlcNAc2-PP-dolichol + GDP-mannose assay).
- Subcellular location: ER membrane, single-pass membrane protein. Topology (PMID:35136180): short
  lumenal N-terminus (1-2), one TM helix (3-23), then a large cytoplasmic catalytic region — consistent
  with acting on the cytoplasmic face. GOA also carries "cytoplasmic side of ER membrane" (GO:0098554, ISS).

## Disease

- Deficiency causes ALG1-CDG (congenital disorder of glycosylation type Ik / CDG-Ik; MIM:608540),
  a severe autosomal-recessive multisystem disorder: developmental delay, hypotonia, epilepsy,
  microcephaly, dysmorphism, coagulation/hematologic and immune involvement; high early mortality.
  [PMID:14973778, PMID:26931382]
- Diagnostic biomarker: xeno-tetrasaccharide NeuAc-Gal-GlcNAc2 (PMID:26931382).
- Originally described by 3 groups in 2004 (Schwarz PMID:14973778; Kranz PMID:14973782;
  Grubenmann PMID:14709599). PMID:26931382 tripled the case count (39 new patients, 26 new mutations).

## Annotation review reasoning

- MF GO:0004578 (chitobiosyldiphosphodolichol beta-mannosyltransferase activity) is the exact,
  correct MF — supported by IDA (PMID:14973778), TAS (Reactome), IEA (RHEA/EC). ACCEPT all.
- GO:0000030 (mannosyltransferase activity) IBA + IEA is the correct-branch parent; less specific
  than GO:0004578. MODIFY -> GO:0004578 (too general).
- GO:0016757 (glycosyltransferase activity) IEA (InterPro Glyco_trans_1) is a very general
  grandparent — over-annotation given the specific term is available. MARK_AS_OVER_ANNOTATED.
- BP: GO:0006488 (dolichol-linked oligosaccharide biosynthetic process) IDA + TAS — core, ACCEPT.
  GO:0006487 (protein N-linked glycosylation) IDA x2 (acts_upstream_of_positive_effect) — core,
  ACCEPT. GO:0009101 (glycoprotein biosynthetic process) IBA — correct but more general parent of
  N-linked glycosylation; KEEP (accept as broader).
- CC: GO:0005789 (ER membrane) TAS/IEA/ISS — core location, ACCEPT. GO:0005783 (ER) IBA — broader
  correct location, ACCEPT. GO:0098554 (cytoplasmic side of ER membrane) ISS — correct catalytic
  face, ACCEPT. GO:0016020 (membrane) HDA (PMID:19946888 NK-cell membrane proteome) — correct but
  uninformatively general; MARK_AS_OVER_ANNOTATED.

## Refs used
- PMID:14973778 (Schwarz 2004) — CDG-Ik discovery, enzymatic + complementation; abstract-only cache.
- PMID:26931382 (Ng 2016) — 39-patient clinical/molecular series; full text cached.
- PMID:19946888 (Ghosh 2010) — NK-cell membrane proteome (basis of the HDA membrane annotation).
- Reactome R-HSA-446218 / R-HSA-446193 / R-HSA-4549382 — pathway TAS annotations.
- file:human/ALG1/ALG1-uniprot.txt — UniProt Q9BT22 FUNCTION / SUBCELLULAR LOCATION / CATALYTIC ACTIVITY.

## Provenance notes
- No falcon deep research (provider out of credits, HTTP 402). Grounded in UniProt, GOA, cached PMIDs
  and Reactome only.
