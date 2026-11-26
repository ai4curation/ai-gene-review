# AK1 (human, P00568) review notes

## 2026-11-26: first review

### Sources and their limits

- `just fetch-gene human AK1` gave 29 GOA rows, the UniProt record and the Reactome entries.
- Deep research: the default provider (falcon) and the perplexity-lite fallback are not
  configured in this environment ("Provider 'falcon' not available. Available: asta,
  openscientist, claude_code"). `just deep-research-asta human AK1` ran, but
  `AK1-deep-research-asta.md` is a keyword retrieval whose 20 papers are unrelated to AK1
  (IgAN subtyping, plant transcriptomes, database papers). It is kept verbatim as provider
  output and is not used as evidence for anything in the review. An OpenScientist
  deep-research run was started with `just deep-research-openscientist human AK1`; see the
  end of this file for its outcome.
- Literature search of my own, PubMed, 2026-11-26. Queries: "adenylate kinase deficiency
  hemolytic anemia AK1"; "adenylate kinase[Title] AND (erythrocyte OR red cell) AND (deficiency
  OR mutation OR variant)"; "(adenylate kinase 1 OR AK1) AND (knockout OR deficient) AND
  (muscle OR heart OR energetic)"; "AK1beta / myristoylat*"; "adenylate kinase AND (sperm
  flagellum OR outer dense ...)"; "human adenylate kinase 1 AND (crystal structure OR NMR OR
  Ap5A)"; "adenylate kinase deficiency AND Japan ...". Hits were cached with `just
  fetch-pmid`. Most of the older papers are abstract-only in the cache; three case reports
  (PMID:34321014, PMID:35509045, PMID:40016400) and two others have full text.

### What AK1 is

- The major cytosolic adenylate kinase: 194 residues, N-acetylated, monomeric
  [PMID:183954 "Human adenylate kinase (isoenzyme AK-1-1) from skeletal muscle is a single
  polypeptide chain of 194 amino-acid residues with an acetylmethionine at the N-terminus
  and a lysine at the C-terminus."].
- Reaction ATP + AMP = 2 ADP, reversible [Reactome:R-HSA-74220 "Cytosolic adenylate kinase 1
  (AK1) catalyzes the reversible reactions of AMP and dAMP with ATP to form ADP and dADP
  respectively, plus ADP"]. dAMP is a poor substrate by affinity: UniProt records KM 2.4 mM
  for AMP and 18.1 mM for dAMP from PMID:21080915.
- AK7 and AK8 are more efficient AMP kinases per enzyme than AK1, which is nevertheless "the
  major cytosolic isoform" [PMID:21080915 "proved to be more efficient in AMP phosphorylation
  as compared with the major cytosolic isoform AK1"].
- Broad in vitro phosphotransferase activity, including NDP kinase activity, was reported for
  several AKs in the AK9 paper [PMID:23416111 "A number of previously characterized adenylate
  kinases were also tested and found to possess a broad phosphotransferase activity similar
  to AK9."]. The cached record is the abstract only; it gives no rates for AK1. The sibling
  review of CMPK1 marks the same row from the same paper MARK_AS_OVER_ANNOTATED (dedicated NME
  NDP kinases exist); I follow it for consistency.
- Thiamine triphosphate synthesis, which UniProt lists "at a very low rate" by similarity to
  chicken AK1, is not a physiological role in mouse [PMID:12379473 "AK1 knockout mice have
  normal ThTP levels in skeletal muscle, heart, brain, liver and kidney, demonstrating that
  AK1 is not responsible for ThTP synthesis in those tissues."]. No GOA row claims it.

### Physiology from the Ak1 knockout mouse

- Skeletal muscle: contraction is maintained but costs more ATP [PMID:11101510 "A maintained
  contractile performance of AK1-deficient muscles was associated with higher ATP turnover
  rate and larger amounts of ATP consumed per contraction."]; other phosphotransfer routes are
  up-regulated. Conclusion of the authors: [PMID:11101510 "AK1-catalyzed phosphotransfer is
  essential in the maintenance of cellular energetic economy, enabling skeletal muscle to
  perform at the lowest metabolic cost."]
- Heart: [PMID:11006295 "In hearts with a null mutation of the AK1 gene, which encodes the
  major AK isoform, total AK activity and beta-phosphoryl transfer was reduced by 94% and
  36%, respectively."]; normal at rest, compromised under hypoxia [PMID:11006295 "under
  hypoxia AK1-knockout hearts display compromised energetics and impaired cardioprotective
  signaling"].
- Muscle remodelling in the knockout: more glycolytic phosphotransfer and, in fast-twitch
  muscle, doubled intermyofibrillar mitochondrial volume [PMID:12562761].
- AMP signalling: contraction-induced AMPK phosphorylation is blunted without AK1
  [PMID:16195390 "AMPK phosphorylation with contractions was clearly increased in WT muscles
  (4.0 +/- 1.1 above resting values), but did not change noticeably with AK deficiency"].
  This is AK1 making the AMP signal; it is not AK1 regulating AMPK directly.
- K-ATP channel metabolic sensing depends on AK phosphotransfer [PMID:11390963 "Adenylate
  kinase associates with the K(ATP) channel complex, anchoring cellular phosphotransfer
  networks and facilitating delivery of mitochondrial signals to the membrane environment."]
- None of the cached knockout abstracts reports red-cell indices. Whether the Ak1 knockout
  mouse has haemolytic anaemia is a gap I could not close from the cache (question put to
  OpenScientist, below).

### Isoforms and locations

- AK1beta: an alternative first exon gives a membrane-bound isoform [PMID:10557075 "The
  AK1beta protein differs from cytoplasmic AK1 by having 18 extra amino acids at the
  N-terminus. The extra residues in AK1beta provide a consensus signal for N-terminal
  myristoylation; as expected, AK1beta was shown to localize to the plasma membrane."]. It
  is p53-inducible in mouse and human cells (same abstract). In mouse brain both isoforms
  are neuronal and AK1beta couples to K-ATP channels in transfected cells [PMID:14977170].
- The reviewed UniProt entry P00568 lists no alternative products. My isoform script finds
  the human AK1beta sequence as the unreviewed entry Q5T9B7 (210 aa, RefSeq NP_001305051.1):
  an 18-residue N-terminus MGCCSSSDPRREDDLRAR replaces Met1-Glu2, with a myristoylation
  consensus (bioinformatics RESULTS section 5). Recorded as a `functional_isoforms` entry
  with a MISSING_ISOFORM source defect for UniProt. Residues in AK1beta are canonical + 16;
  every residue number in this review is canonical P00568 numbering.
- Sperm flagellum (mouse): [PMID:16790685 "AK1 was first seen in condensing spermatids and
  was associated with the outer microtubular doublets and outer dense fibers of sperm."] The
  human GOA rows for sperm flagellum and outer dense fiber are Ensembl Compara transfers of
  this mouse result. No human data found.
- Extracellular AK1: secreted from C2C12 myotubes [PMID:18446060] and present in human
  serum, where it interconverts circulating ADP [PMID:22637533 "This phosphotransfer
  reaction was diminished markedly in serum from knockout mice lacking the major AK isoform,
  AK1, and in human serum immunodepleted of AK1."]. Interesting, but I did not propose an
  extracellular-space annotation: the release route is unknown and one immunodepletion
  experiment is thin support for a location row. Left as a suggested question.

### Adenylate kinase deficiency (MONDO:0012967, MIM 612631)

Reported alleles, all checked against NM_000476.3 by `01_variant_consequences.py`
(numbering identical to P00568; see RESULTS section 1):

| Allele | Protein | Genotype in report | Source |
|---|---|---|---|
| c.382C>T | p.Arg128Trp | one allele found | PMID:2542324 |
| c.491A>G | p.Tyr164Cys | homozygous | PMID:9432020 |
| c.319C>T | p.Arg107Ter | homozygous | PMID:10233365 |
| c.118G>A / c.190G>A | p.Gly40Arg / p.Gly64Arg | compound heterozygous | PMID:12649162 |
| c.418_420del | p.Asp140del (= p.Asp141del) | homozygous | PMID:12649162 |
| c.138del ("delG138") | p.Val47SerfsTer45 | homozygous | PMID:15315793 |
| c.289C>T | p.Arg97Trp | not stated in cache | PMID:28211224 (title only in cache); table in PMID:40016400 |
| c.71A>G / c.413G>A | p.Gln24Arg / p.Arg138His | compound heterozygous | PMID:30918013 |
| c.301C>A | p.Gln101Lys | homozygous | PMID:34321014 |
| c.223dup / c.413G>A | p.Met75AsnfsTer19 / p.Arg138His | compound heterozygous | PMID:35509045 |
| c.518T>G | p.Val173Gly (computed; cache has title only) | not stated in cache | PMID:37782390 |
| c.464del | p.Lys155ArgfsTer39 | homozygous (plus thalassaemia trait) | PMID:40016400 |

- Functional data on recombinant human enzymes [PMID:17662886 "Four mutant enzymes
  (Gly40Arg, Gly64Arg, Arg128Trp, Asp140del) were severely affected in activity, displaying
  a catalytic efficiency of four orders of magnitude lower than the wild-type; one
  (Tyr164Cys) was grossly perturbed in protein stability."]. This matches the structural
  split my scripts find: the first four are at the nucleotide or the LID arginine network,
  Tyr164 is buried (rSASA 0.01) and 11.8 A from the ligand.
- Arg128Trp in the chicken enzyme: [PMID:2542324 "The mutant chicken AK1 expressed in
  Escherichia coli showed a reduced catalytic activity as well as a decreased solubility"].
- Arg97Trp is a hypomorph in vitro, not a null [PMID:43093599 "R97W exhibited an
  approximately 89% reduction in catalytic efficiency and markedly decreased binding
  affinities for Mg2+·ATP, AMP, and Mg2+·ADP."], with a more open NMP domain; my centroid
  measurements on the deposited NMR ensembles (8X1G vs 7X7S) agree (NMP-LID 23.4 vs 18.9 A).
  It is also the most frequent disease allele in gnomAD (40 alleles, no homozygotes).
- Inheritance and dosage: carriers have about half-normal activity and are well
  [PMID:9432020 "Her parents and brother had approximately 50% normal AK activity"]. gnomAD:
  pLI 0.009, LoF o/e 0.54, 31 observed high-confidence LoF variants (98 alleles) and no LoF homozygote. So:
  recessive loss of function; no hint of dominant-negative or gain of function, and the
  enzyme is a monomer.
- Clinical picture across reports: chronic non-spherocytic haemolytic anaemia from the
  neonatal period (jaundice, splenomegaly, transfusion need in the severe cases), with
  psychomotor impairment in some families (Arg107Ter siblings, PMID:10233365; the Chinese
  compound heterozygote, PMID:35509045) and not in others (PMID:12649162 "In neither case
  was psychomotor impairment observed."). Splenectomy helped one patient (PMID:28211224,
  title).

### The open question: is AK1 loss sufficient for haemolysis?

- Against simple sufficiency: [PMID:6308059 "A child with hemolytic anemia was found to have
  severe erythrocyte adenylate kinase (AK) deficiency, but an equally enzyme-deficient
  sibling had no evidence of hemolysis."] and [PMID:1646049 "These additional biochemical
  defects in the AK-deficient RBC further support the concept that AK deficiency per se may
  not cause hemolytic anemia."] Both predate molecular diagnosis; the genotypes of those
  families are unknown.
- For causality: every molecularly characterised family has biallelic damaging AK1
  variants, the recombinant enzymes are defective [PMID:17662886 "The altered properties
  displayed by the mutant enzymes support the cause-effect relationship between AK1 mutations
  and hemolytic anemia."], and severity is not obviously tied to residual activity (a
  patient with 44% activity and an altered enzyme had haemolysis, PMID:6305188).
- The red cell has residual ADP-forming capacity without AK1 (about 1/2,000 of normal),
  attributed to AK2 or guanylate kinase [PMID:6308059]. How the cell's adenine nucleotide
  pool behaves with that residue, and why it fails in most but not all deficient people, is
  not established. This is a BIOLOGY knowledge gap in the review and the hypothesis sent to
  OpenScientist (`AK1-hypotheses/ak1-sole-erythrocyte-adenylate-kinase/`).

### Annotation decisions worth a note

- GO:0050145 (NMP kinase) and GO:0019205: parents of AMP kinase activity; TOO_GENERAL, as in
  the CMPK1 and yeast ADK1 reviews.
- GO:0004550 (NDP kinase), IDA and IEA: MARK_AS_OVER_ANNOTATED, same judgement as CMPK1.
  Not REMOVE: I have not read the full text and the activity was measured.
- GO:0009142 (NTP biosynthetic process): kept. The reverse adenylate kinase reaction makes
  ATP from two ADP, which is the physiologically important direction in working muscle; the
  row does not depend on the NDP kinase side activity.
- Sperm flagellum / outer dense fiber: KEEP_AS_NON_CORE on mouse evidence.
- No NEW rows. Candidate "plasma membrane" for AK1beta rests on mouse and transfected-cell
  data and belongs to the isoform (recorded there). Candidate process terms such as energy
  homeostasis would restate necessity evidence from the knockout; the catalysed step is
  already covered by ADP biosynthetic process and nucleotide interconversion.
- PAINT: `just paint-losses human AK1` reports no IRD/IKR on the lineage. The family review
  (PTHR23359) already scopes AMP kinase activity onto SF59; I added AK1 detail there.
- GO-CAM: `gocams/index.tsv` has no model containing UniProtKB:P00568, so there is no GO-CAM
  review to write.
- Module: AK1 is already the human representative of the `adenylate_kinase_activity`
  annoton in `modules/purine_nucleotide_interconversion.yaml`.

### Not done / could not do

- Full text of the older primary papers (PMID:2542324, 9432020, 10233365, 12649162,
  15315793, 17662886, 28211224, 37782390) is not in the cache; genotype and assay details
  beyond the abstracts were not verified.
- ClinVar-only variants (p.Arg132His, p.Lys56Ter, c.44-5_48delinsC) have no publication I
  could find; they are placed structurally but not used as evidence of pathogenic mechanism.

### OpenScientist runs (2026-11-26)

- `just deep-research-openscientist human AK1`: ran for the full two hours allowed here and
  was stopped by the session's background-job limit before any report was written. No
  `AK1-deep-research-openscientist.md` exists; nothing from it is used.
- `just gene-hypothesis-research openscientist human AK1 --focus-type free-text --slug
  ak1-sole-erythrocyte-adenylate-kinase ...` (hypothesis: AK1 is the only quantitatively
  significant adenylate kinase of the mature red cell, so its loss alone is sufficient to
  shorten red cell survival; to be tested against red cell proteome copy numbers and Ak1
  knockout mouse haematology). Also stopped by the same limit with no report; the empty
  output directory was removed so it does not look like a finished run. The question stays
  open and is recorded as a knowledge gap on the core function.
- The gene-review checklist (`lcv`) could not be filled: the tool installs from a
  repository this session cannot reach.
