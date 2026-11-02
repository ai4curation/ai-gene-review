# HSPD1 evidence notes

[PMID:1346131](https://pubmed.ncbi.nlm.nih.gov/1346131/) reconstitutes mammalian Hsp60/Hsp10 substrate folding with MgATP; [PMID:25918392](https://pubmed.ncbi.nlm.nih.gov/25918392/), DOI [10.1073/pnas.1411718112](https://doi.org/10.1073/pnas.1411718112), solves the human type I chaperonin complex. These establish the distinction from the cytosolic type II TRiC/CCT system, independently of an AI review or ARBA.

Horse F6Z587 has 541 residues versus 573 for human P10809, with an internal deletion of human 171–202. The N-terminal mitochondrial precursor and annotated ATP-binding positions are conserved. Broad ATP binding and mitochondrial targeting remain reasonable inferences, but full ATP-dependent folding competence is uncertain for this model. The existing horse ARBA GO:0005832 TRiC-complex annotation is wrong at family/complex level regardless of whether this deletion preserves Hsp60 activity.

[PMID:17823127](https://pubmed.ncbi.nlm.nih.gov/17823127/) shows that cytosolic Hsp60 can promote death or survival in different apoptotic systems, with different caspase-3 interactions. Do not remove opposing apoptotic-direction annotations solely because they share a reference. Immune responses to extracellular preparations require their own preparation/contamination and receptor-dependence controls; those rows remain UNDECIDED rather than being accepted as a universal Hsp60 cytokine activity or rejected from localization alone.

A completed human Falcon report has been inspected. The selected horse record is unreviewed; the initial literature search did not identify a targeted horse HSPD1 mechanistic experiment warranting a separate horse Edison report.

## Human structural research

The completed Falcon report identifies [PMID:32317635](https://pubmed.ncbi.nlm.nih.gov/32317635/), [DOI:10.1038/s41467-020-15698-8](https://doi.org/10.1038/s41467-020-15698-8), which establishes active single- and double-ring human Hsp60–Hsp10 assemblies. It also identifies [PMID:31444388](https://pubmed.ncbi.nlm.nih.gov/31444388/), [DOI:10.1038/s41598-019-48762-5](https://doi.org/10.1038/s41598-019-48762-5), on impaired client refolding by disease variants. These primary identities were independently verified. ATP turnover and productive folding are distinct readouts, strengthening the caution about the selected horse deletion. The earlier manual synthesis is retained as separately labeled primary-source analysis.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all seven GOA rows, the description and core functions for F6Z587 without opening any ProtNLM2 file. Deep research: `just deep-research HORSE HSPD1 --provider falcon` failed twice on 2026-10-20 ("Edison API request failed: Failed to authenticate"); no horse deep-research file was created. I used the human falcon report context already summarised above, the human Swiss-Prot record and cached primary papers (PMID:1346131, PMID:25918392, PMID:32317635 full text, PMID:31444388, PMID:23636703).

New analysis (no existing bioinformatics file overwritten): `HSPD1-bioinformatics/compare_gene_models_rereview.py` -> `RESULTS-rereview.md`, `results-rereview.json`, `alignments-rereview.txt`; inputs `A0A9L0S8L8-rereview.fasta`, `A0A9L0TMN1-rereview.fasta` (UniProt REST) and `ensembl_gene_rereview.json` (Ensembl REST lookup of ENSECAG00000008968), fetched 2026-10-20.

### Identity of the benchmark accession (alternative gene model)

- F6Z587 (541 aa; ENSECAT00000009419 / ENSECAP00000007167) is an exon-skipping alternative model of horse HSPD1. It omits the 96-bp coding exon at chr18:72882811-72882906 that is present in the Ensembl canonical transcript ENSECAT00000137290 [file:HORSE/HSPD1/HSPD1-bioinformatics/RESULTS-rereview.md]. The skip removes human P10809 residues 171-202 (VATISANGDKEIGNIISDAMKKVGRKGVITVK) in frame.
- In mature numbering the gap is 145-176, entirely within the first segment of the intermediate hinge domain [PMID:32317635 "an equatorial ATP-binding domain (residues 1–137, 411–526), an intermediate hinge domain (residues 138–191, 375–411), and an apical domain (residues 192–374)"]. Transit peptide, equatorial ATP-binding residues and the apical domain are retained; 527/541 paired residues are identical to human.
- Human P10809 has no equivalent isoform (its isoform 2 is a different C-terminal truncation).
- The canonical horse product is A0A9L0S8L8 (587 aa; ENSECAP00000072491): every human residue (559/573 identical) plus a 14-aa N-terminal extension MKAHLTKRNSASSE before the MLRLP start. UniProt gives it the PAINT IBA rows (GO_Central) that F6Z587 lacks. A third model, A0A9L0TMN1 (474 aa), is C-terminally truncated.

### Evolutionary grounding

- PANTHER PTHR45633 (Cpn60/GroEL; includes the divergent yeast Tcm62 in SF33). Horse F6Z587 has no subfamily in the local member index. Human P10809 is in SF17 in the PANTHER 19.0 human file, whereas mouse, rat, cow, chicken, frog, zebrafish, fly, worm and yeast HSP60 orthologs are all in SF3. This looks like a subfamily-HMM boundary quirk rather than a real split, since P10809 and MGI:96242 seed the same PAINT nodes.
- PAINT: protein folding (GO:0006457) IBD at PTN000143677 (GroEL, M. tuberculosis GroEL1/2, yeast HSP60, human); mitochondrial matrix and protein-folding chaperone binding at PTN000143509; UPRmt and IMS import at PTN000143510 (Opisthokonta); immune-regulation terms at PTN002900230 (Euteleostomi, seeded by human and mouse). Horse HSPD1 is inside all of these clades (the canonical model receives them as IBA).
- The CCT/TRiC complex is never propagated to PTHR45633. Type II chaperonins are a different family (TCP-1).

### Decisions

- GO:0005524 ATP binding: ACCEPT. The equatorial site is intact and mapped residues are identical.
- GO:0005759 mitochondrial matrix: ACCEPT. The transit peptide is retained, and the location is an IBD at PTN000143509.
- GO:0005832 chaperonin-containing T-complex (ARBA): REMOVE. This is the wrong chaperonin type.
- GO:0006457, GO:0042026, GO:0140662 (folding/refolding/ATP-dependent chaperone): UNDECIDED. These are the gene's core function, but this product lacks 32/54 residues of the first hinge-domain segment. Even point variants that destabilise the nucleotide-triggered cycle abolish folding [PMID:31444388 "and DLS results suggest that the D3G and V72I complexes fall apart when treated"]. I have no expression evidence for the skip transcript. The earlier review had the same actions; the reasoning now rests on the exon structure and domain mapping.
- GO:0009409 response to cold (ISS from chicken Q5ZL72): changed UNDECIDED -> KEEP_AS_NON_CORE. The donor experiment is now resolved: PMID:23636703 reports Hsp60 mRNA induction in cold-stressed chicken heart [PMID:23636703 "the mRNA levels of Hsps (70, 60, 40, and 27) increased significantly"]. This is a gene-level stress-induction observation and matches the human review.
- No NEW rows. The IBA-supported terms carried by the canonical model (UPRmt, immune-regulation terms) belong to A0A9L0S8L8 and depend on a functional chaperonin.
- Core function: written at the gene level, with an explicit caveat that the competence of the F6Z587 product is unresolved.

### Family review / modules

- interpro/panther/PTHR45633/PTHR45633-review.yaml lists F6Z587 as a representative member under "Benchmark members without resolved subfamily placement". It does not mention the exon skip, and an exon-skipped model is a weak representative for the GO:0140662 assessment. There is also a disagreement: modules/mitochondrial_upr.yaml says "HSP-60 and HSPD1 are in PTHR45633:SF17", but the PANTHER 19.0 files put worm hsp-60 (P50140) in SF3 and only human P10809 in SF17.
- Modules: modules/mitochondrial_upr.yaml (HSPD1 as UPRmt chaperone output); modules/cct_chaperonin_folding.yaml (group II comparator, relevant to the CCT REMOVE).
- Relative to review next: horse A0A9L0S8L8, the full-length canonical product of the same gene (same_gene_canonical). It has no review. Its folder would be genes/HORSE/HSPD1__A0A9L0S8L8, because genes/HORSE/HSPD1 is keyed to F6Z587.
