# AP3S2 (sigma-3B) — review notes

Working notes for the GO annotation review of human AP3S2 / UniProtKB:P59780.
Inline provenance throughout; every quoted string is verbatim from the cached
source named beside it.

---

## 0. Identity and provenance checks

`AP3S2-uniprot.txt` is the expected record and not a merged redirect:
`ID   AP3S2_HUMAN             Reviewed;         193 AA.`, `AC   P59780;`,
`DE   RecName: Full=AP-3 complex subunit sigma-2;` with
`DE   AltName: Full=AP-3 complex subunit sigma-3B;`. Gene `AP3S2`, HGNC:571,
chromosome 15 (`DR   Proteomes; UP000005640; Chromosome 15.`), 193 residues,
22,017 Da. PANTHER family from the record itself:
`DR   PANTHER; PTHR11753; ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY; 1.`

Two flags on the record set the tone for the whole review. The protein has been
seen — `PE   1: Evidence at protein level;` and the keyword block carries
`Proteomics identification` — but it is pharmacologically and functionally dark:
`DR   Pharos; P59780; Tdark.`, `DR   HPA; ENSG00000157823; Low tissue
specificity.`, and `DR   BioGRID-ORCS; 10239; 20 hits in 1154 CRISPR screens.`
(1.7 % of screens; not a commonly essential gene).

A small defect in the UniProt SUBUNIT line is worth reporting upstream: it reads
`a small adaptin (sigma-type subunit APS1 or AP3S2)`. `APS1` is the *yeast* AP-1
sigma gene name; the intended human symbol is **AP3S1**. The biology is right,
the symbol is a typo.

Every functional statement in the UniProt record is `{ECO:0000250}` — inferred
by similarity. The FUNCTION and SUBUNIT blocks and the entire SUBCELLULAR
LOCATION block carry that code. The single experimentally-sourced CC line is
`CC   -!- TISSUE SPECIFICITY: Present in all adult tissues examined.`
`{ECO:0000269|PubMed:9118953}`. So UniProt itself asserts nothing experimental
about this protein beyond its expression breadth.

**GOA shape.** 25 rows: 1 IBA, 2 ISS, 13 IEA, 8 NAS, **1 experimental (IDA)**.
Counted by `AP3S2-bioinformatics/check_goa_reconciliation.py`, which also
reports that 16 of the 25 rows carry a `WITH/FROM` and therefore require a
`propagation_review`.

The one experimental row is `GO:0030123 AP-3 adaptor complex / IDA /
PMID:9118953`. QuickGO records its `assignedBy` as **FlyBase**, which is
surprising for a human gene product from a human paper but is what the record
says; the identical row sits on AP3S1 (Q92572). Both are correct: Dell'Angelica
et al. identified *both* sigma-3 paralogs in that paper.

---

## 1. What is known about the sigma-3B protein itself

This is the question the review turns on, so it is worth separating
sigma-3B-specific evidence from AP-3-complex evidence.

### 1a. It is a real, expressed human protein, cloned and blotted in 1997

Two groups cloned it independently in the same year, and both raised antibodies.

Dell'Angelica et al. [PMID:9118953]: *"We have identified two closely related
human proteins (sigma3A and sigma3B) that are homologous to the small chains,
sigma1 and sigma2, of clathrin-associated adaptor complexes."* Expression was
measured at both RNA and protein level: *"Northern and Western blot analyses
demonstrate that the products of both the sigma3A and sigma3B genes are
expressed in a wide variety of tissues and cell lines."*

Simpson et al. [PMID:9151686] cloned the same protein from ESTs — *"Although
neither clone is full length (R23892 encodes amino acids 79–193 of σ3A, and
R87391 encodes amino acids 85–193 of σ3B)"* — noting *"The mouse and human σ3B
protein sequences are 100% identical in the region of overlap."* Their Northern
panel agrees with Dell'Angelica's: *"Fig. 4 shows that δ, β3A, σ3A, and σ3B are
all expressed ubiquitously"*, and *"although there are two isoforms of σ3, they
have similar expression patterns."*

So the ubiquitous-expression claim is not inherited: it was measured on sigma-3B
itself, twice, in 1997, by Northern and by Western blot.

### 1b. It is a constituent of the AP-3 heterotetramer

Dell'Angelica et al. state it directly: *"sigma3A and sigma3B are components of
a large complex, named AP-3, that also contains proteins of apparent molecular
masses of 47, 140 and 160 kDa."* That is the basis of the one IDA row.

Simpson et al.'s co-immunoprecipitation is complex-level but sigma-3B-informed:
they used *"the δ, σ3A, and σ3B antibodies described above"*, and report *"The
σ3 antibodies bring down these four subunits as well, although the signal from
δ, β3, and μ3 is weaker than with the other two antibodies, and one of the σ3
isoforms appears to be preferentially immunoprecipitated."* The σ3 signal in
their δ and β3 immunoprecipitates *"appears as a doublet, presumably because
there are two isoforms of the protein"* — i.e. both sigma-3A and sigma-3B are in
AP-3 preparations from brain cytosol.

Modern human protein-level corroboration comes from the BioPlex AP-MS
interactomes, which I read out of IntAct (`findInteractions/P59780`, 26 records).
AP3S2 co-purifies with **AP3M1** (Q9Y2T2; three records, from PMID:28514442,
PMID:33961781 and PMID:40205054) and **AP3M2** (P53677; two records, from
PMID:28514442 and PMID:33961781) — the two mu-3 paralogs — and with the AP-3
dileucine cargo **RNF13** (O43567; two records, from the same two studies).
These are spoke-expanded affinity-purification hits, not direct-binding
measurements, but they are human, endogenous-scale and sigma-3B-specific, and
they place sigma-3B in complexes containing either mu-3 paralog.

### 1c. Nothing else

Beyond membership and expression, there is no sigma-3B-specific functional
literature. Concretely:

- Europe PMC `TITLE_ABS:"sigma3B"` returns **1** hit: PMID:9118953.
  `TITLE_ABS:"sigma-3B"` returns 0.
- PubMed `AP3S2[TIAB]` returns 19 records; on inspection all 19 are genetic
  association, transcriptomic-signature or fusion-transcript papers, not studies
  of the protein.
- Even the one survey of AP-3 subunit expression in tumours
  [PMID:17125464] skips it: *"Using RT-PCR we demonstrated more than twofold
  decrease in the levels of mRNA of AP3D1, AP3B1, AP3M1, and AP3S1"* — four
  subunits, sigma-3B not among them.
- Every solved AP-3 structure is built on the paralog. The 2024 cryo-EM core
  [PMID:39705307] and the 2026 AP3:ARF1 coat [PMID:42139345] both used sigma-3A;
  the latter states its constructs as *"AP3D1(1–1203) (Homo sapiens) and
  AP3S1(1–193) (H. sapiens) were cloned into the pFL vector"*.
- There is no knockout, knockdown, patient allele or biochemical assay reported
  for AP3S2 that I could find.

The one real exception is section 3 below, which affinage did not surface and
which is the single most important paper for this gene.

---

## 2. What is inherited from the AP-3 complex

AP-3 is well characterised, and AP3S2 inherits all of it as a constituent.

**Pathway.** *"Adaptor protein complex-3 (AP-3) mediates cargo sorting from
endosomes to lysosomes and lysosome-related organelles"* [PMID:39705307].
Signal-mediated: *"A heterotetrameric complex termed AP-3 is involved in
signal-mediated protein sorting to endosomal-lysosomal organelles"*
[PMID:9545220].

**Recruitment and coat assembly.** Human AP-3 is constitutively open and is
recruited by Arf1 through delta; in pull-downs *"the δ-σ3 complex binds nearly
as well as the full complex, with binding of the β3-μ3 hemicomplex barely above
background levels in the Arf1GTP state"* [PMID:39705307]. On membranes AP3:ARF1
builds tubular carriers: *"AP3:ARF1 spontaneously remodels membranes containing
cargo and the phosphoinositide PI(3,5)P2 into tubular structures coated in
spiraling rows of AP3 arches and ARF1 dimers"* [PMID:42139345].

**Clathrin: the position has reversed.** The 1998 paper behind the GOA row
`GO:0035654` reported association — *"In vitro binding assays showed that
mammalian AP-3 did associate with clathrin by interaction of the appendage domain
of its beta3 subunit with the amino-terminal domain of the clathrin heavy
chain"* [PMID:9545220] — and by 2013 that was the consensus: *"While it was
initially suspected that AP-3 may be clathrin-independent, subsequent research
has shown that AP-3 and AP-1 act as clathrin-binding adaptor proteins"*
[PMID:23247405]. The 2026 reconstitution settles it the other way: *"AP3 does
not copurify with clathrin-coated vesicles"*, and *"By demonstrating that
AP3:ARF1 can generate carriers without using a clathrin lattice, we explain the
clathrin independence of AP3-mediated trafficking"* [PMID:42139345]. This has
direct consequences for two annotations and for the choice of molecular-function
term (sections 6 and 8).

**Lysosome-related organelles.** In melanocytes, *"Packaging of the tyrosinases
into transport vesicles at early/recycling endosome-associated tubules is
dependent on ubiquitous adaptor protein complex (AP)-1 and AP-3"*, and across
LROs, *"Hermansky-Pudlak Syndrome (HPS) patients and the corresponding animal
models have abnormal melanosomes, platelet dense granules and lamellar bodies of
lung type II epithelial cells"*, with *"Mutations in subunits of AP-3, BLOC-1,
BLOC-2 and BLOC-3 underlie many forms of HPS"* [PMID:23247405]. This is the basis
of the ComplexPortal NAS rows for melanosome assembly and platelet dense granule
organization — real AP-3 biology, in specialised cell types.

A 2026 paper makes the dense-granule half of that concrete and ties it to the
signal the sigma subunit reads. *"Transmembrane protein 163 (TMEM163), a zinc
transporter, is drastically reduced in platelets of AP-3-, BLOC-1-, and
BLOC-2-deficient Hermansky-Pudlak syndrome mice and patients"*, and *"A conserved
N-terminal acidic dileucine motif (LEDRGL69L70) in TMEM163 is essential for
interactions with BLOC-1 and AP-3 but dispensable for binding with AP-1, AP-2 and
BLOC-2"*; the authors conclude that *"our findings established TMEM163 as a cargo
protein sequentially sorted by AP-3 and BLOC-1 via a shared dileucine-based
sorting signal, which is essential for its proper trafficking to platelet dense
granules"* [PMID:41985787]. The study works with AP3B1 and does not test which
subunit contacts the motif, so it is complex-level for AP3S2 — but it is current
primary evidence that AP-3 cargo selection runs through an acidic dileucine
signal, which is the site the sigma chain supplies.

**Neurons.** Neuronal AP-3 uses a beta-3 isoform: *"Neurons express adaptor
(AP)-3 complexes assembled with either ubiquitous (beta3A) or neuronal-specific
(beta3B) beta3 isoforms"*, and loss of the neuronal form damages synaptic vesicle
cargo loading: *"beta3B deficiency compromised synaptic zinc stores assessed by
Timm's staining and the synaptic vesicle targeting of membrane proteins involved
in zinc uptake (ZnT3 and ClC-3)"* [PMID:15537701]. Note that the isoform variable
in that paper is **beta-3, not sigma-3**; it says nothing about which sigma
paralog is in either complex.

---

## 3. Does the sigma subunit read the dileucine signal? Yes — and sigma-3B was tested

The merged `genes/human/AP1S1/` and `genes/human/AP1S3/` reviews worked this out
for AP-1: dileucine signals bind a composite site on the large/small subunit
interface, the pockets are on sigma, and GO has no term for it. Most of that
reasoning transfers to AP-3, and one part of it does not.

**What transfers.** The composite-site mechanism is stated for all three
complexes at once: *"signals, on the other hand, do not bind to any single AP
subunit but to combinations of γ-σ1, α-σ2, and δ-σ3 subunits, as demonstrated by
the use of yeast three-hybrid (Y3H) and in vitro binding assays"*
[PMID:21097499]. The residue-level map transfers too: *"This is evidenced by the
loss of signal binding by the σ2 V88D or L103S substitutions and the homologous
σ1A V88D and I103S and σ3A V94D and L109S substitutions"* [PMID:21097499]. And
the 2024 AP-3 cryo-EM structure sees that pocket directly, occluded in the
autoinhibited state: *"Surprisingly, the dileucine cargo-binding site on σ3 is
occupied by the N-terminal extension of β3"* [PMID:39705307].

**What sigma-3B-specific evidence exists — the paper affinage missed.** Janvier
et al. [PMID:14691137] tested the AP-3 delta-sigma3 hemicomplex in a yeast
three-hybrid assay with **both** sigma-3 paralogs cloned separately (*"μ3A and
σ1A (EcoRI–SalI), and σ2, σ3A, σ3B, and σ4 (BamHI–XhoI) were cloned into
pGAD424"*). The result: *"yeast three-hybrid analyses showed that the cytosolic
tail of LIMP-II interacted with γ1–σ1A, δ–σ3A, and δ–σ3B"*, and the specificity
was confirmed by alanine scanning: *"Of 12 residues that were mutated, only three
were essential for interactions with γ1–σ1A, δ–σ3A, and δ–σ3B, the
leucine-isoleucine pair and the glutamate residue at position −4"*. Their
conclusion: *"These observations reveal a novel mode of recognition of sorting
signals involving the gamma/delta and sigma subunits of AP-1 and AP-3."*

This is the only assay in the literature that puts sigma-3B in a functional
readout, and it is a clean one: a delta-sigma3B hemicomplex binds a genuine
lysosomal dileucine signal with the same three-residue requirement as
delta-sigma3A and gamma1-sigma1A.

**Confirmed by sequence.** `AP3S2-bioinformatics/sigma_dileucine_pocket.py`
fetches the sequences live and aligns them. AP3S2 retains both pocket residues
at the same native positions as AP3S1: **Val94** and **Leu109**. The paralogs
differ at 31 of 193 positions overall (83.9 % identity), but only 4 of those 31
lie in the 46-residue window spanning both anchors ± 15 residues, and none at an
anchor (V113M, N118Y, A121Q, M123V, all C-terminal to Leu109). The alignment also
independently reproduces Mattera's cross-complex equivalences: sigma-2 V88/L103
and sigma-1A V88/I103 both map onto AP3S2 V94/L109.

**Where the AP-1 reasoning does *not* transfer.** The AP1S1 and AP1S3 reviews
record the complex-level activity as `GO:0035615 clathrin-cargo adaptor
activity`. That term's definition is *"Bringing together a cargo protein with
clathrin, responsible for the formation of endocytic vesicles"* — clathrin in the
definition, endocytic vesicles in the definition. Neither holds for AP-3
(section 2, clathrin; PMID:39705307, endosome→lysosome). Using GO:0035615 for
AP3S2 would import a contradicted mechanism. The honest available term is
`GO:0030674 protein-macromolecule adaptor activity` ("An adaptor activity that
brings together two or more macromolecules in contact, permitting those molecules
to function in a coordinated way"), recorded as a `contributes_to`, with the
missing dileucine-binding term written up as an ontology gap.

The second AP1S3 proposal — `assembly chaperone binding`, for the AAGAB
interaction — also does not transfer. AAGAB is described as *"the assembly
chaperone for AP1 and AP2 adaptor complexes"*, and AP-3 is not among them; I
found no AAGAB-AP3S2 evidence and assert none.

---

## 4. The IBA: node PTN000204281 in PTHR11753

One IBA row: `GO:0016192 vesicle-mediated transport / IBA / GO_REF:0000033`,
with eleven gene-product donors plus `PANTHER:PTN000204281`.

The committed PAINT slice `interpro/panther/PTHR11753/PTHR11753-paint.tsv`
carries two IBD assertions on that node: `GO:0043231 intracellular
membrane-bounded organelle` (C, 13 seeds, slice dated 20260528) and
`GO:0016192 vesicle-mediated transport` (P, 10 seeds, slice dated 20260828).
Only the second propagates to AP3S2 in the current GOA release, consistent with
`DR   PAN-GO; P59780; 1 GO annotation based on evolutionary models.`

`AP3S2-bioinformatics/resolve_withfrom.py` resolves all ten seeds (one through
the GO API, because WormBase gene ids are absent from UniProt's xref index):

| seed | protein | complex |
|---|---|---|
| CGD:CAL0000182525 | Q59QC5 APS3_CANAL | **AP-3** |
| SGD:S000003561 | P47064 AP3S_YEAST (APS3) | **AP-3** |
| SGD:S000004160 | P35181 AP1S1_YEAST (APS1) | AP-1 |
| PomBase:SPAP27G11.06c | Q9P7N2 AP1S1_SCHPO (vas2) | AP-1 |
| MGI:MGI:1098244 | P61967 AP1S1_MOUSE | AP-1 |
| MGI:MGI:1889383 | Q9DB50 AP1S2_MOUSE | AP-1 |
| FB:FBgn0039132 | *D. melanogaster* AP-1sigma | AP-1 |
| RGD:620188 | P62744 AP2S1_RAT | AP-2 |
| UniProtKB:P53680 | AP2S1_HUMAN | AP-2 |
| WB:WBGene00000157 | Q19123, *C. elegans* aps-2 | AP-2 |

Three things follow, and they all point the same way.

1. **AP3S2 is inside the inheriting clade, trivially and by the seeds.** It is a
   sigma subunit of an AP complex, and two of the ten seeds are AP-3 sigma
   orthologs (budding-yeast APS3 and Candida APS3). The node is not an
   AP-1/AP-2 inference being stretched across to AP-3.
2. **The generality of the term is correct, not a granularity failure.** The
   seeds span AP-1 (TGN/endosome), AP-2 (plasma membrane) and AP-3
   (endosome/lysosome). Donors that disagree about destination make the parent
   term the correct least common ancestor; `GO:0016192` is general because the
   family is.
3. **The one apparent donor/seed mismatch is a release artefact, not a defect.**
   The IBA row carries `FB:FBgn0043012` (*D. melanogaster* AP-2sigma, Q9VDC3),
   which is not in the current `GO:0016192` seed list but *is* a seed of the same
   node's `GO:0043231` IBD, whose slice line is three months older. The tree
   contains the gene; the two lines were regenerated at different times.

No target-specific evidence of loss or divergence exists to argue against the
node placement: the fold is intact, the dileucine pocket is intact (section 3),
there are no NOT rows, and the protein is expressed in all tissues examined.
Verdict: `NO_FAILURE_CORE`.

---

## 5. The ISS/IEA rows: the donor is mouse Ap3s2, not AP3S1

Worth stating plainly because it is easy to assume otherwise for a
near-dark paralog: **no row in AP3S2's GOA cites AP3S1 as a donor.** Resolved
donors, from `withfrom_resolved.tsv`:

- `UniProtKB:Q8BSZ2` = **AP3S2_MOUSE**, `Ap3s2`, reviewed, 193 aa — the true
  one-to-one mouse ortholog. It is the `WITH/FROM` of both ISS rows
  (`GO:0008089`, `GO:0048490`) and of three Ensembl-Compara IEA rows
  (`GO:0008089`, `GO:0048490`, `GO:0035651`).
- `UniProtKB:A0A0G2K302` = rat `Ap3s2`, unreviewed — the `WITH/FROM` of the
  `GO:0008021 synaptic vesicle` IEA.

So the transfer is a straightforward vertebrate ortholog transfer, and an
unusually strong one: the alignment shows **human and mouse AP3S2 are
byte-for-byte identical proteins**, both 193 aa, 100 % identity, no gaps
(`sigma_dileucine_pocket.py`). There is no sequence-level reason to discount any
of these rows.

The interesting question is instead what the mouse annotations themselves rest
on. QuickGO on Q8BSZ2 gives `GO:0008089 IMP PMID:21998198` and `GO:0048490 IMP
PMID:21998198` (assigned by UniProt), and `GO:0035651 IDA PMID:19010779`
(assigned by MGI). Reading PMID:21998198 (Larimore et al., full text cached): the
genetic perturbation is the **delta** subunit — *"Synaptosome fractions from
control brains (lanes 1–8) and AP-3–deficient mocha (Ap3d1mh/mh) brains"* — and
the sigma detection is with a pan-σ3 antibody: *"antibodies against synaptic
vesicle markers (SV2, synaptophysin), AP-3–dependent synaptic vesicle cargoes
(PI4KIIα, VAMP7, ZnT3), and AP-3 σ3 subunit"*. Recall from PMID:9151686 that σ3
antibodies see both isoforms as a doublet.

That does not make the mouse IMPs wrong — AP-3 is a complex and its subunits
participate in what it does — but it fixes their grade: they are **complex-level
claims about neuronal AP-3, recorded on the sigma-3B gene product**, not
sigma-3B-specific results. The human rows inherit exactly that. Combined with
the fact that `GO:0008089 anterograde axonal transport` is defined as *"The
directed movement of organelles or molecules along microtubules from the cell
body toward the cell periphery in nerve cell axons"* — a microtubule-motor
process in which a coat adaptor participates by packaging cargo, not by moving
it — these are `KEEP_AS_NON_CORE`, not `ACCEPT` as core, and certainly not
`REMOVE`.

`GO:1904115 axon cytoplasm` is a GO_REF:0000108 inter-ontology inference off
`GO:0008089`; it stands or falls with it, and gets the same grade.

**`GO:0035651 AP-3 adaptor complex binding` is a different matter.** The
definition is *"Binding to an AP-3 adaptor complex"*. AP3S2 is not a binder of
AP-3; it is a constituent of it, which the same GOA record already states
correctly and experimentally (`part_of GO:0030123`, IDA). An `enables
AP-3-complex-binding` row on a core subunit of that complex conflates part-of
with binding. The mouse source is an MGI IDA from a cross-linking/AP-MS study
[PMID:19010779] whose abstract describes *"purification of cross-linked AP-3
complexes and mass spectrometric identification of associated proteins"* — an
experiment in which a subunit inevitably appears. I do not second-guess the MGI
curator's reading of that paper, but the human IEA transfer of it is
uninformative and mis-typed relative to the part_of row, so:
`MARK_AS_OVER_ANNOTATED`.

**`GO:0008021 synaptic vesicle` (is_active_in, IEA from rat).** The rat source is
a SynGO EXP/IDA from PMID:33376223, "Hidden proteome of synaptic vesicles in the
mammalian brain". The authors themselves flag AP-3 in that dataset as a
non-resident: *"This may explain the presence of endosomal-related proteins
(e.g., Stx7, AP3) or proteins of the AZ (e.g., Piccolo, Bassoon) in the SV
proteome."* A proteomic detection that the source paper attributes to visitor
proteins or preparation carry-over is a reproducible-but-uncharacterised hit:
`MARK_AS_OVER_ANNOTATED`, not `REMOVE` (the detection is real) and not `ACCEPT`.

---

## 6. Term-definition problems found by reading definitions rather than labels

Three GOA rows say something different from what their label suggests.

- **`GO:0016183 synaptic vesicle coating`** is defined as *"The formation of
  clathrin coated pits in the presynaptic membrane endocytic zone, triggered by
  the presence of high concentrations of synaptic vesicle components."* That is
  clathrin-coated-pit formation at the **presynaptic plasma membrane**. AP-3's
  role in synaptic vesicle biogenesis is at **endosomes**, and the cited paper
  [PMID:15537701] is about synaptic vesicle cargo content in beta-3 isoform
  knockouts, not about presynaptic pit formation. `GO:0016182 synaptic vesicle
  budding from endosome` ("Budding of synaptic vesicles during the formation of
  constitutive recycling vesicles from early endosomes") is the term the
  evidence actually supports → `MODIFY`.
- **`GO:0035654 clathrin-coated vesicle cargo loading, AP-3-mediated`** is
  defined as *"Formation of a macromolecular complex between proteins of the AP-3
  adaptor complex and proteins and/or lipoproteins that are going to be
  transported by a clathrin-coated vesicle."* The cargo-loading half is exactly
  what sigma-3B does; the clathrin-coated-vesicle half is the claim PMID:42139345
  overturns. `GO:0035459 vesicle cargo loading` ("The formation of a
  macromolecular complex between the coat proteins and proteins and/or
  lipoproteins that are going to be transported by a vesicle") keeps the right
  part and drops the wrong one → `MODIFY`.
- **`GO:0006896 Golgi to vacuole transport`** (InterPro2GO from IPR027155, the
  APS3 signature) describes the fungal ALP pathway, where AP-3 really does run
  Golgi→vacuole. In mammals the characterised itinerary is endosome→lysosome/LRO
  [PMID:39705307, PMID:23247405]. `GO:0008333 endosome to lysosome transport` →
  `MODIFY`.

By contrast, **`GO:0030123 AP-3 adaptor complex` is exactly right**, and its
definition says so by name: *"In at least humans, the AP-3 complex can be
heterogeneric due to the existence of multiple subunit isoforms encoded by
different genes (beta3A and beta3B, mu3A and mu3B, and sigma3A and sigma3B)."*

**The ARBA rule behind the GO:0030123 IEA checks out.** `ARBA00033921` fires on
`FunFam 3.30.450.60:FF:000001` **and** `taxon = Primates`. FunFam signatures are
named for whole families, so the rule looked like a candidate over-generalisation
— but `arba_funfam_specificity.py` shows the signature partitions cleanly: of the
eight reviewed human AP-complex sigma subunits, only AP3S1 and AP3S2 carry
FF:000001 (AP1S1/AP1S3 → FF:000005, AP1S2 → FF:000009, AP2S1 → FF:000004, AP4S1
→ FF:000010, AP5S1 → none). Zero non-AP-3 subunits would be mis-called. Note
that the panel is deliberately wider than PTHR11753: the family's complete human
membership is the seven proteins from AP1S1 to AP4S1, and AP5S1 was added so the
rule is not tested only on the family it was built from. Suspicion tested and
refuted; the row stands.

---

## 7. Disease and expression

The gene's visibility in the literature comes entirely from a GWAS locus label.
Kooner et al. [PMID:21874001] identified six new T2D loci in South Asians,
including one tagged by rs2028299 at 15q26. The paper is careful about what that
means: *"At 15q26, rs2028299 is nearest AP3S2, encoding a clathrin associated
adaptor complex expressed in adipocytes, pancreatic islets and other tissues,
which may be involved in vesicle transport and sorting."* It then names two
reasons to doubt AP3S2 is the effector: *"SNP rs2028299 is associated with
expression of C15orf38, encoding a member of an uncharacterised family of
proteins"*, and *"Amongst the other genes at this locus, PLIN1 is also a possible
candidate for the association with T2D."*

Two further observations. First, the description in that sentence — "a clathrin
associated adaptor complex" — is the pre-2026 view and is not accurate for AP-3.
Second, the C15orf38 eQTL is interesting rather than incidental here, because
UniProt lists a readthrough product among AP3S2's alternative products:
`CC         IsoId=Q7Z6K5-2; Sequence=External;` under `Name=C15orf38-AP3S2`. A
locus whose lead variant controls C15orf38 expression and which produces a
C15orf38-AP3S2 readthrough transcript is not a locus from which AP3S2 protein
function can be read off.

The remaining AP3S2 literature is of the same kind: replication studies of
rs2028299 in other populations, transcriptomic signature panels, and one fusion
report (AP3S2-NTRK3 in melanoma, where the oncogenic driver is the NTRK3 kinase
and AP3S2 supplies 5′ sequence). None of it is evidence about AP-3 sigma-3B's
molecular function, and none of it enters the review as support.

---

## 8. Assessment of the affinage record and what it missed

`AP3S2-deep-research-affinage.md`: `self_evaluation_pairwise: win`,
`faith_pct: 100.0`, `n_discoveries: 3`, `citation_count: 2`, and `.affinage.log`
reports `trust gates clear`. The record is about the right protein (sigma-3B /
AP-3, P59780) with no symbol collision, and its two numbered citations
(PMID:9118953, PMID:39256512) are both real and both about AP3S2. Its narrative
is accurate as far as it goes and honest about its own limits: *"Beyond its role
as an AP-3 subunit, no further mechanistic detail of AP3S2's own activity has
been characterized in the available corpus."*

But the corpus was small, and the gates measure precision rather than recall.
What it missed:

- **PMID:14691137** — the only paper that assays sigma-3B functionally
  (delta-sigma3B binds the LIMP-II dileucine signal). It is titled for the
  hemicomplexes and for HIV-1 Nef, so a symbol-driven search does not reach it.
  This is the single most consequential omission.
- **PMID:21097499** — the residue map of the sigma dileucine pocket, including
  the sigma-3A V94/L109 substitutions that make the paralogy argument testable.
- **PMID:39705307** and **PMID:42139345** — the AP-3 structures, and with them
  the reversal of the clathrin question that decides two annotations and the
  choice of MF term.
- **PMID:21998198**, **PMID:19010779**, **PMID:33376223** — the mouse and rat
  source annotations that the human ISS/IEA rows transfer from. None can be
  graded without reading them.
- **PMID:41985787** — a 2026 primary paper establishing an AP-3 cargo selected
  through an acidic dileucine motif and required for platelet dense granule
  trafficking; it is titled for TMEM163, so again unreachable from the symbol.
- **PMID:21874001** — the T2D GWAS that is the reason the symbol appears in the
  literature at all, and which argues against AP3S2 being the effector gene.

Its `mechanism_profile` grounding was not imported, per the brief. Two of its
three suggestions are defensible and were re-derived independently
(`GO:0005794 Golgi apparatus`; an adaptor-activity MF, though I chose
`GO:0030674` over its `GO:0060090` for specificity); the third, `partners:
NTRK3`, is a fusion-transcript artefact and not a partner of the protein.
Recorded as `relevance: MEDIUM`, `correctness: VERIFIED` with that caveat noted.

---

## 9. Where this leaves the review

- The one experimental row (`GO:0030123`, IDA) is correct and is the gene's
  anchor. `ACCEPT`.
- The IBA is sound at the node and general for the right reason.
  `NO_FAILURE_CORE`, `ACCEPT`.
- The ISS/IEA ortholog transfers are mechanically impeccable (identical
  sequences) but carry complex-level, neuron-context claims.
  `KEEP_AS_NON_CORE`, with `MARK_AS_OVER_ANNOTATED` for the two that are
  mis-typed or source-flagged (`GO:0035651`, `GO:0008021`).
- Three rows have the wrong term for the right biology and get `MODIFY`
  (`GO:0016183`, `GO:0035654`, `GO:0006896`).
- The one genuinely missing annotation is the activity the gene demonstrably
  performs — binding an acidic dileucine sorting signal as part of a
  delta-sigma3B hemicomplex — and GO has no term for it. It goes in
  `proposed_new_terms` and `knowledge_gaps`, not as a `NEW` row.
- Everything else about this protein is dark, and the `knowledge_gaps` section is
  the honest deliverable: what distinguishes sigma-3B from sigma-3A is unknown,
  and nobody has looked.
