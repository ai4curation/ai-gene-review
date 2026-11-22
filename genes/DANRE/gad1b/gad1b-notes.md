# gad1b notes (Danio rerio, glutamate decarboxylase 1b, GAD67; UniProt Q7ZUS3)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison/Falcon 402 Payment Required; OpenAI key invalid). Not
attempted, per instructions. Literature searched by hand in Europe PMC (see `../gad1a/gad1a-notes.md`
for the queries). Pair analysis in `../gad1a/gad1a-bioinformatics/RESULTS.md`; paralog notes in
`../gad1a/gad1a-notes.md`.

Accession Q7ZUS3 (TrEMBL, RefSeq NP_919400, 587 aa), ZFIN:ZDB-GENE-030909-3 (formerly gad1 /
gad67), Ensembl ENSDARG00000027419, chr6. 8 GOA rows: IBA/IEA plus one ZFIN IEP for GABA
biosynthetic process from PMID:9634146.

### Nomenclature
- Older zebrafish papers use "GAD67", "gad67" or "gad1" for this gene. The sequenced Martin et al.
  1998 GAD67 cDNA (AF017266) is 99.6% identical to Gad1b vs 90.9% to Gad1a (probe_identity.py in
  gad1a-bioinformatics). Mueller & Guo used a probe from AF017266:
  [PMID:19673006 "GAD67 (zfin: gad1; nucleotides 151–1964 of GenBank accession number AF017266)"]
  (AF017266 is only 696 nt, so the coordinates quoted cannot be right as written, but the accession
  is clear).
- The old probe names map to gad1b:
  [PMID:26896392 "A mixture of two probes to gad1b (previously called gad67, probes used to be called gad67a and gad67b) and one probe to gad2 (previously called gad65) was used to label GABAergic cells [61, 62]."]

### Expression
- Martin et al. 1998 (abstract): [PMID:9634146 "In the caudal hindbrain, only GAD67 was detected (in neurons with large-caliber axons)."]
  [PMID:9634146 "Immunohistochemistry for gamma-aminobutyric acid (GABA) revealed that GABA is produced at all sites of GAD expression, including the novel cells in the caudal hindbrain."]
- Pan-GABAergic marker of choice: [PMID:42466317 "At 5 dpf, as shown previously, gad1b expression occupies all regions of the larval brain (Figure 4A)."]
- Locus coeruleus: [PMID:24374659 "Also in this case, expression analysis of individual gad isoforms revealed that only gad1b is expressed in the locus coeruleus (Table2)."]
  (Filippi et al. compared gad1b with gad2, not with gad1a.)
- Lateral-line efferent neurons: [PMID:41950195 "Efferent neurons showed robust expression of gad2 and gad1b (but not gad1a [Fig 4B]), encoding for enzymes required for the synthesis of GABA [35,36]."]
- Public data (RESULTS.md): 84 TPM in 5-day whole larvae (gad1a 4 TPM); 88 Bgee calls, mostly in situ
  in brain nuclei, retina, spinal interneurons, Kolmer-Agduhr neurons and Purkinje cells; 247 ZFIN
  records from 69 publications.

### Function
- Morphants (translation-blocking MO): craniofacial defects not seen in the mutant:
  [PMID:30200754 "A gad1b MO injected at the 1-4 cell stage caused severe morphological defects in head development"]
  [PMID:30200754 "The craniofacial phenotype in gad1b morphants is surprising because genetic knockouts of gad1b do not cause craniofacial defects"]
- CRISPR null allele gav2303 (10-bp deletion, exon 4), abnormal brain activity like PTZ:
  [PMID:30200754 "The gad1bgav2303/gav2303 allele used in these studies harbored a 10 bp deletion in exon 4 and was a functional null mutation."]
  [PMID:30200754 "The electrophysiological traces of the cMO morphants were comparable to those obtained from larvae null for gad1b and wild-type fish exposed to PTZ, which causes seizures in zebrafish."]
  Full characterization "submitted" (VanLeuven et al.); a 2024 preprint on reduced GABA and tectal
  connectivity exists but has no PMID and was not used. PMID:42610151 cites earlier 2D seizure
  imaging of gad1b null mutants.
- Splice MO (intron 8 retention) raises locomotor activity:
  [PMID:34650032 "Firstly, interference with gad1b, Gad or GABA-A-Rs results in an increased locomotor activity similar to what we find after foxp2 impairment, thus we demonstrate that GABAergic signalling influences locomotor activity in zebrafish."]
- No enzyme assay of zebrafish Gad1b; activity inferred (catalytic residues kept, 82.7% identical to
  human GAD1). Mammalian: [PMID:17384644 "GAD67 is constitutively active and is responsible for basal GABA production."]
- Transcriptional adaptation (gad1a upregulation in gad1b mutants) has not been measured.

### Annotation decisions
- IEP GABA biosynthetic process (PMID:9634146): ACCEPT. The GAD67 cDNA of that paper is gad1b by
  sequence, and GABA co-localizes with GAD expression. The process term is right; the evidence is
  expression-based.
- IBA/IEA MF rows: ACCEPT. Cytoplasm: ACCEPT. Presynaptic active zone (IBA): KEEP_AS_NON_CORE (ZFIN
  curates Gad1b-antibody staining at presynaptic active zones in adult cerebellum from Bae et al. 2009,
  PMID:19371731, abstract only in cache, so not quoted).
- No NEW rows: the mutant/morphant phenotypes (seizure-like activity, locomotion) are downstream
  consequences of GABA deficiency, not processes Gad1b performs.
