# MOCS1 (human) review notes

UniProt: Q9NZB8 (MOCS1_HUMAN). HGNC:7190. Gene on chr 6. All quotes below are grounded in
the local files `genes/human/MOCS1/MOCS1-uniprot.txt`, `genes/human/MOCS1/MOCS1-goa.tsv`, and
cached `publications/PMID_*.md`.

## Summary of biology

MOCS1 encodes the enzyme(s) that catalyse the **first step of molybdenum cofactor (Moco)
biosynthesis**: conversion of GTP to cyclic pyranopterin monophosphate (cPMP, "precursor Z").
It is a **bicistronic / alternatively-spliced gene** producing two functionally distinct
products, MOCS1A and MOCS1B, that together carry out this two-part reaction
[file:human/MOCS1/MOCS1-uniprot.txt "Isoform MOCS1A and isoform MOCS1B probably form a complex
that catalyzes the conversion of 5'-GTP to cyclic pyranopterin"].

- **MOCS1A** (N-terminal region, aa 1–383) = **GTP 3',8-cyclase**, EC 4.1.99.22 /
  GO:0061798. It is a **radical-SAM enzyme** binding **two [4Fe-4S] clusters** (one 4Fe-4S–
  S-AdoMet cluster, one binding the GTP-derived substrate). It makes
  (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate.
  [file:human/MOCS1/MOCS1-uniprot.txt "MOCS1A catalyzes the cyclization of\nGTP to (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate"]
  [file:human/MOCS1/MOCS1-uniprot.txt "Binds 2 [4Fe-4S] clusters."]
- **MOCS1B** (C-terminal region, aa 414–636) = **cyclic pyranopterin monophosphate synthase**,
  EC 4.6.1.17 / GO:0061799. It converts (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate
  to cPMP. Belongs to the MoaC family.
  [file:human/MOCS1/MOCS1-uniprot.txt "MOCS1B\ncatalyzes the subsequent conversion of (8S)-3',8-cyclo-7,8-\ndihydroguanosine 5'-triphosphate to cPMP"]

Domain architecture (UniProt FT): TRANSIT 1..21 Mitochondrion; REGION 1..383 = MOCS1A;
DOMAIN 64..277 Radical SAM core; REGION 414..636 = MOCS1B; ACT_SITE 606 "For MOCS1B activity".
[file:human/MOCS1/MOCS1-uniprot.txt "In the N-terminal section; belongs to the radical SAM\nsuperfamily. MoaA family."]
[file:human/MOCS1/MOCS1-uniprot.txt "In the C-terminal section; belongs to the MoaC family."]

## Subcellular localization

UniProt subcellular location: mitochondrial matrix for isoforms MOCS1A, MOCS1B, 9, 8; but
isoform 2 = cytosol and isoform 3 = cytoplasm (aggregates).
[file:human/MOCS1/MOCS1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform MOCS1A]: Mitochondrion matrix"]
[file:human/MOCS1/MOCS1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]: Cytoplasm, cytosol"]

- PMID:31996372 (Mayr, Röper, Schwarz 2020, J Biol Chem) established that MOCS1A/MOCS1B
  proteins localize to the **mitochondrial matrix**, with a novel maturation mechanism: type
  I splice variants either go to the mitochondrial matrix (exon 1a) or stay cytosolic (exon
  1b); MOCS1AB variants are targeted to mitochondria independently of exon 1, and within
  mitochondria MOCS1AB is proteolytically cleaved to release matrix MOCS1B.
  [PMID:31996372 "type I splice variants (MOCS1A) either localize\nto the mitochondrial matrix (exon 1a) or remain cytosolic (exon 1b)"]
  [PMID:31996372 "Within mitochondria, MOCS1AB underwent proteolytic cleavage resulting in\nmitochondrial matrix localization of the MOCS1B domain."]
- The cytosol IDA (GO:0005829, HPA GO_REF:0000052) and IEA cytoplasm/cytosol annotations are
  consistent with the cytosolic isoforms (2/3) and with the pre-import/cytosolic pool, so they
  are retained as non-core relative to the matrix site of catalysis.
- Mitochondrion HTP (GO:0005739, PMID:34800366) is a high-throughput mitochondrial proteome
  study; consistent with the matrix localization but non-core (general term, HTP).

## Molecular function evidence

- **GTP 3',8'-cyclase (GO:0061798, MOCS1A)** — EC 4.1.99.22, verified in vitro.
  UniProt CATALYTIC ACTIVITY [Isoform MOCS1A]: GTP + AH2 + SAM = (8S)-3',8-cyclo-7,8-
  dihydroguanosine 5'-triphosphate + 5'-deoxyadenosine + L-methionine + A + H(+),
  EC=4.1.99.22, Evidence ECO:0000269|PubMed:31996372.
  [file:human/MOCS1/MOCS1-uniprot.txt "EC=4.1.99.22 {ECO:0000269|PubMed:31996372}"]
  GOA has an EXP annotation to GO:0061798 with PMID:31996372.
- **cyclic pyranopterin monophosphate synthase (GO:0061799, MOCS1B)** — EC 4.6.1.17.
  PMID:23627491 (Hover et al. 2013, J Am Chem Soc; full text available) directly assays the
  **human homolog MOCS1B**, showing it converts 3',8-cH2GTP to cPMP with Km 0.79 µM.
  [PMID:23627491 "The isolated \n3',8-cH2GTP was converted to cPMP by MoaC or its human homologue, MOCS1B, with \nhigh specificities (Km < 0.060 μM and 0.79 ± 0.24 μM for MoaC and MOCS1B, \nrespectively)"]
  GOA EXP GO:0061799 with PMID:23627491, plus IGI (PMID:29368224, with E. coli MoaC
  UniProtKB:P0A738) and IMP (PMID:15180982) support the same activity.
- **4Fe-4S cluster binding (GO:0051539)** — PMID:15180982 (Hänzelmann et al. 2004) characterized
  MOCS1A as an oxygen-sensitive Fe-S protein binding two [4Fe-4S] clusters, each ligated by
  three cysteines; all conserved cysteines are essential for precursor-Z synthesis in vivo.
  [PMID:15180982 "MOCS1A could \nbe reconstituted in vitro under anaerobic conditions to yield a form containing \ntwo [4Fe-4S](2+) clusters."]
  [PMID:15180982 "A redox-active [4Fe-4S](2+,+) cluster is ligated by an N-terminal \nCX(3)CX(2)C motif as is the case with all other AdoMet-dependent radical enzymes"]
  UniProt COFACTOR [Isoform MOCS1A] Name=[4Fe-4S] cluster, Note "Binds 2 [4Fe-4S] clusters."
  GOA IEA GO:0051539 is well supported; GO:0051536 (parent) and GO:0046872 (metal ion binding)
  are broader/redundant parents.
- **S-adenosyl-L-methionine binding (GO:1904047)** — not in the GOA snapshot's core rows but in
  the UniProt DR block (IEA:Ensembl). SAM is a cosubstrate of the radical-SAM MOCS1A reaction;
  UniProt has BINDING 86 and BINDING 127 to S-adenosyl-L-methionine. Included in core_functions
  as a supporting activity of MOCS1A.
  [file:human/MOCS1/MOCS1-uniprot.txt "/ligand=\"S-adenosyl-L-methionine\""]

## Biological process / disease

- **Mo-molybdopterin cofactor biosynthetic process (GO:0006777)** — the pathway MOCS1 initiates.
  Strong experimental (IMP/IDA) and mutational support; this is the core BP.
  UniProt: PATHWAY "Cofactor biosynthesis; molybdopterin biosynthesis."
  [file:human/MOCS1/MOCS1-uniprot.txt "The first step, the conversion of GTP to cyclic pyranopterin"]
  IMP annotations to GO:0006777 rest on patient-mutation studies:
  - PMID:9731530 (Reiss et al. 1998, Nat Genet) — first identification of MOCS1 as the
    disease gene; mutations in both ORFs (moaA/moaC homologs) in MoCo-deficient patients.
    [PMID:9731530 "Mutations can be found in the majority of \nMoCo-deficient patients that confirm the functional role of both ORFs"]
  - PMID:9921896 (Reiss et al. 1998, Hum Genet) — genomic structure and mutational spectrum;
    MOCODA type A. [PMID:9921896 "the first two enzymes \nrequired in the MoCo biosynthesis pathway, MOCS1 A and MOCS1 B, in a single \ntranscript"]
  - PMID:16021469 (Leimkühler et al. 2005) — ten novel MOCS1/MOCS2 mutations.
  - PMID:29368224 (Mayr et al. 2018) — mild MoCD case; c.1338delG truncates MOCS1B; residual
    MOCS1B via translation re-initiation; functional confirmation of MOCS1B activity.
    [PMID:29368224 "Functional studies of both proteins confirmed activity of MOCS1B"]
  - PMID:12754701 (Reiss & Johnson 2003, Hum Mutat; review) — TAS for GO:0006777.
- **GO:0032324 molybdopterin cofactor biosynthetic process** (ARBA IEA) — a valid but slightly
  broader/legacy sibling of GO:0006777; kept as non-core to avoid redundancy.
- Disease: **Molybdenum cofactor deficiency type A (MOCODA, MIM:252150)** — autosomal recessive,
  loss of all molybdoenzyme activities (sulfite oxidase, xanthine dehydrogenase, aldehyde
  oxidase); neonatal intractable seizures, severe neurodegeneration, early death. cPMP
  (fosdenopterin/DrugBank DB16628) replacement is a treatment.
  [file:human/MOCS1/MOCS1-uniprot.txt "Molybdenum cofactor deficiency, type A (MOCODA) [MIM:252150]"]

## Annotation-review decisions (rationale)

- Core MFs: GO:0061798 (MOCS1A) and GO:0061799 (MOCS1B) accepted (EXP/IMP/IGI/IBA). The
  bare "catalytic activity" (GO:0003824, IEA) is an uninformative parent → MARK_AS_OVER_ANNOTATED.
- Fe-S: GO:0051539 (4Fe-4S) accepted as core supporting MF; GO:0051536 (Fe-S cluster binding)
  and GO:0046872 (metal ion binding) are redundant parents → KEEP_AS_NON_CORE.
- Core BP: GO:0006777 accepted. GO:0032324 → KEEP_AS_NON_CORE (redundant broader).
- Localization: mitochondrial matrix (GO:0005759, IDA PMID:31996372) is the core catalytic
  site. cytosol/cytoplasm/mitochondrion (IEA/IDA/HTP/TAS) kept as non-core (isoform-specific
  cytosolic pool, or general/high-throughput terms).
- No experimental annotation is REMOVEd. IEA-only redundant-parent rows are kept as
  non-core or flagged as over-annotated rather than removed, per policy (they are not
  clearly wrong).
</content>
</invoke>
