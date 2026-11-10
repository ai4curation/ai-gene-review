# imuA (CC_3213, Q9A3J1) curation notes

Caulobacter crescentus ImuA, first gene of the SOS-regulated imuA-imuB-dnaE2 operon.

- No provider deep research is available for this gene; `just deep-research` was not run
  in this session and no `-deep-research-*.md` file exists. The review is built from the
  two cached primary papers plus the UniProt record, both read in full where available.
- The operon is SOS regulated: a LexA-binding site sits 66 bp upstream of imuA.
  [PMID:15886391, "The operon containing imuA, imuB and dnaE2 presents this typical LexA-binding sequence 66 bp upstream from the imuA start codon, indicating that this operon is SOS regulated."]
- imuA, imuB and dnaE2 are induced together after UV damage.
  [PMID:15886391, "The results shown in Figure 5 demonstrate that imuA, imuB and dnaE2 expression levels are increased similarly in response to UV damage."]
- An imuA in-frame deletion is extremely sensitive to mitomycin C and the phenotype is
  complemented by the wild-type allele.
  [PMID:15886391, "Both the UV and the mit C sensitivity phenotypes of imuA could be complemented by vector pMR3213, containing the wild-type imuA allele."]
- The imuA promoter is a confirmed LexA-dependent SOS promoter.
  [PMID:18083815, "which was confirmed by site-directed mutagenesis studies of the imuA promoter"]
- Strain note: the genetics are in NA1000, a derivative of the sequenced CB15 strain that
  Q9A3J1 represents. GOA makes the same association (EXP row from PMID:18083815).
- ImuA has no demonstrated molecular activity. CB15 ImuA carries InterPro IPR017026
  (Inducible mutagenesis protein A) and has no PANTHER assignment, unlike P. putida ImuA
  (Q88I84), which InterPro places in IPR047610 and PANTHER PTHR35369:SF3. The two ImuA
  InterPro families are distinct entries; this is recorded in the PTHR35369 family review.

## 2026-11-07 comparative consultation

The statements above that no ImuA molecular activity is known are now scoped to Caulobacter. PMID:38591662 directly demonstrates DNA-stimulated ATP hydrolysis, DNA binding and ImuB interaction for purified Myxococcus ImuA. The ImuB construct in that study is N-terminally truncated. Those experiments establish a testable mechanism in a comparator; they do not identify the Caulobacter catalytic residues or demonstrate these activities in Q9A3J1. The target retains a process-only core synthesis with an explicit molecular-function knowledge gap. No ATPase, DNA-binding, recombinase or nucleotide-binding annotation is manufactured from the P-loop fold.

PMID:15886391 uses NA1000, a CB15 derivative. Its in-frame imuA deletion and complementation support a genuine protein requirement rather than an untested polar effect. The mutagenesis and survival assays place ImuA in the accessory machinery, but do not identify which physical step it performs. The historical NEW TLS row remains present and active; its reason now distinguishes genetic pathway inference from a direct lesion-bypass assay.

The SOS-response row is ACCEPT: its role is not merely being expressed by an SOS promoter. GO:0009432 describes an error-prone microbial damage response, and the independent genetic evidence establishes ImuA as a core effector in that response. PMID:18083815 is still abstract-only in the unchanged local cache; the quoted promoter evidence is flagged accordingly.

A genuine Falcon deep-research request failed with HTTP403 authentication on this date. No provider report was fabricated. Sources were the full cached 2005 primary, cached 2008 abstract, full 2024 comparator and frozen UniProt record. There are no IBA rows in this three-gene panel; no PAINT node placement or lineage loss is inferred. The lack of a PANTHER cross-reference on this ImuA is a family-mapping gap, not justification to reuse the Pseudomonas ImuA selector.
