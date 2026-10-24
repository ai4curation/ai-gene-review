# AP2S1 (sigma2-adaptin, AP17) — research notes

UniProt **P53680** (`AP2S1_HUMAN`), 142 aa, 17.0 kDa, PE 1 (evidence at protein level).
Verified against the fetched record: `ID   AP2S1_HUMAN             Reviewed;         142 AA.` and
`AC   P53680; B2R4Z4; O75977; Q6PK67;` — the expected accession, not a merged redirect.
PANTHER **PTHR11753** "ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY"; InterPro IPR027156 (APS2,
the AP-2-sigma-specific entry), IPR000804 (clathrin small-chain signature), IPR016635
(AP complex small subunit), IPR011012 (longin-like domain superfamily).
Two isoforms: P53680-1 (canonical) and P53680-2 (VSP_017352, residues 52-89 missing).

---

## 1. What the protein is

AP2S1 is the small (sigma) subunit of the heterotetrameric AP-2 clathrin adaptor, the
principal cargo-selection module of clathrin-mediated endocytosis (CME) at the plasma
membrane. The complex is `α + β2 + μ2 + σ2`; UniProt states it directly:

> `CC       of two large adaptins (alpha-type subunit AP2A1 or AP2A2 and beta-type`
> [`file:human/AP2S1/AP2S1-uniprot.txt`]

AP-2 assembles hierarchically from two hemicomplexes, α/σ2 and β2/μ2, and σ2 is the
obligate partner of the α trunk. The two cargo-binding sites are non-overlapping and sit
on different subunits: μ2 reads tyrosine-based YxxΦ signals, while the acidic dileucine
signal is read by the α/σ2 pair [PMID:42234739 "AP-2 is composed of two large subunits (α
and β2), a medium subunit (μ2), and a small subunit (σ2) that assemble hierarchically from
hemicomplexes (α/σ2 and β2/μ2) before forming the final heterotetramer"].

## 2. The subunit-level molecular function: sigma2 builds the dileucine pockets

This is the point that most of AP2S1's GO record misses, and it is settled structurally.
Kelly et al. co-crystallised the 200 kDa AP2 core with the CD4 dileucine peptide and found
that **the leucines bind sigma2 itself**:

> [PMID:19140243 "The major recognition events are the two leucine residues binding in hydrophobic pockets on σ2."]

> [PMID:19140243 "binds in two adjacent hydrophobic pockets on the small σ2 subunit that are lined by a number of hydrophobic residues"]

The pockets were mapped by mutagenesis, with binding measured against motifs displayed on
PtdIns(4,5)P2 liposomes:

> [PMID:19140243 "Mutation of a number of these to hydrophilic residues (σ2L65S, σ2V88D, σ2V98S or σ2L103S), or filling in the pocket by replacement of σ2A63 or σ2N92 with tryptophan, strongly inhibited binding of recombinant AP2 core complexes to different dileucine motifs"]

> [PMID:19140243 "The KD for wild-type AP2 binding to the CD4 dileucine motif was 0.85 μM, whilst the σ2V88 and σ2L103 mutations reduced binding to below detectable levels."]

The specificity control matters: the same mutant cores bound PtdIns(4,5)P2 and the TGN38
YxxΦ motif normally, so the defect is in the dileucine site rather than in folding
[PMID:19140243 "In contrast, the binding of wild-type and mutant AP2 cores to PtdIns4,5P2 and to YxxΦ was unaffected"].

The basic L-4 patch is shared between subunits, and this is where Arg15 sits:

> [PMID:19140243 "A double mutant in σ2R15 and αR21 decreased binding to the dileucine motif by around an order of magnitude"]

**Ontology gap.** There is no GO molecular function for acidic dileucine
(`[DE]xxxL[LI]`) sorting-signal binding. The nearest term, GO:0089710 *endocytic targeting
sequence binding*, is defined as "Binding to a endocytic signal sequence, a specific
peptide sequence, of 4-6 amino acids with an essential tyrosine (Y), found on cytoplasmic
tails of some cell surface membrane proteins, which directs internalization by
clathrin-coated pits" — i.e. it is the YxxΦ term, which belongs to μ2, not σ2. Verified by
QuickGO term lookup plus keyword searches for "dileucine" (0 hits), "sorting motif
binding", "internalization signal binding" and "leucine motif"; none returns a suitable MF.
This is recorded as a `proposed_new_terms` entry and an ONTOLOGY knowledge gap, and it is
the reason sigma2's one genuinely subunit-level activity cannot currently be expressed in
GO.

## 3. Residue check (bioinformatics, `AP2S1-bioinformatics/`)

`check_sigma2_pockets.py` fetches every sequence live from UniProt and hardcodes no result.
Findings (`RESULTS.md`, `results.json`):

- All eight literature positions carry the stated residue in human P53680:
  **R15, A63, L65, V88, N92, N97, V98, L103**. Nothing is lost or substituted.
- Kelly's structure is of a species-mixed AP2 core — its Methods give the construct as
  `1-621 mouse α-adaptin; 1-591 human β2-adaptin; 1-435 rat μ2-adaptin, 1-143 mouse
  σ2-adaptin`, so the sigma2 chain crystallised is the **mouse** protein (P62743), and the
  residue numbering transfers to human only if the orthologues match. They do: human
  P53680, rat P62744 and mouse P62743 are **identical over the full 142-residue chain**,
  so the transfer is exact and needs no alignment step. Checked, not assumed.
- MAFFT L-INS-i alignment of the eight human sigma subunits (AP2S1, AP1S1, AP1S2, AP1S3,
  AP3S1, AP3S2, AP4S1, AP5S1): **R15 is invariant in all eight**, confirming Nesbit's
  statement [PMID:23222959 "which is evolutionarily conserved in all AP2σ2 subunit orthologues and human AP sigma subunit paralogues"].
  Restricted to the AP-1 to AP-4 sigmas (the scope of Kelly's own conservation claim),
  15R, 63A, 65L, 88V and 98V are invariant — again matching the paper
  [PMID:19140243 "most of which are conserved in all σ subunits from APs 1-4 in species from yeast to mammals"].
- One position is **AP2S1-specific among the AP-1 to AP-4 sigmas: N92**, where every other
  paralogue carries D. N97 (3/7) and L103 (3/7) are also variable. So the pocket is mostly
  a family-wide feature with a small AP-2-specific rim — consistent with AP-2 showing
  broader dileucine tolerance than AP-1/AP-3
  [PMID:19140243 "the increased tolerance of AP2 for alterations in residues adjacent to the L"].

These are encoded as eight `RETAINED` residue claims with `method: STRUCTURE`, `anchor`
mouse P62743 (the chain in the co-crystal) and `target` human P53680, both stated as
UniProt positions rather than alignment columns. All eight pass
`ai_gene_review.validation.gene_residue_claims` with no unresolved checks.

## 4. Disease: FHH3 and the Arg15 hotspot

Heterozygous missense mutations at Arg15 — and only at Arg15 in the original series —
cause familial hypocalciuric hypercalcaemia type 3:

> [PMID:23222959 "missense mutations of AP2 σ subunit (AP2S1) affecting Arg15, which forms key contacts with dileucine-based motifs of CCV cargo proteins, result in familial hypocalciuric hypercalcemia type 3 (FHH3), an extracellular calcium homeostasis disorder affecting the parathyroids, kidneys and bone"]

> [PMID:23222959 "AP2S1 mutations decreased the sensitivity of CaSR-expressing cells to extracellular calcium and reduced CaSR endocytosis"]

The mechanism runs through the dileucine site: CaSR carries a variant dileucine motif
(RHQPLL, residues 1009-1014) in its cytoplasmic tail, and removing it phenocopies the
AP2S1 mutation. A 2025 study made the motif dependence explicit
[PMID:40510119 "we demonstrate that a dileucine endocytic motif is required for directing CaSR to dynamic spatiotemporal pathways by interacting with the adaptor protein-2 σ-subunit, which is mutated in hypercalcemic patients"].

Follow-up genetics and mouse work:

- 17/65 further FHH probands carried Arg15 mutations, all three alleles acting
  dominant-negatively [PMID:26082470 "All three FHH3-causing AP2σ2 mutations impaired CaSR signal transduction in a dominant-negative manner."]
- An exome survey found a second class of AP2σ variants away from Arg15
  [PMID:29325022 "the Thr112Met, Met117Ile and Glu142Lys variants, located in the AP2σ α4-α5 helical region that forms an interface with AP2α, impaired CaSR-mediated intracellular calcium (Cai2+) signalling"]
- Knock-in mice reproduce the human disease and show the mutation damages complex assembly
  as well as cargo binding
  [PMID:33729479 "Co-immunoprecipitation studies showed that the AP2S1 p.Arg15Leu mutation impaired protein-protein interactions between AP2σ2 and the other AP2 subunits, and also with the CaSR."]
  Homozygotes die perinatally [PMID:33729479 "Homozygous (Ap2s1L15/L15) mice invariably died perinatally."]
- An independent ENU allele that deletes 17 conserved residues is embryonic lethal when
  homozygous, establishing that the subunit is essential
  [PMID:29479578 "However, homozygous Ap2s1del17/del17 mice were non-viable and died between embryonic days 3.5 and 9.5"],
  while heterozygotes are haplosufficient with normal calcium handling.

Note the asymmetry worth keeping in mind when reading the GO record: AP2S1 loss is
embryonic-lethal and CME-wide, yet the human disease caused by the Arg15 alleles is a
narrow calcium-homeostasis phenotype. Nesbit's own explanation is that Arg15 mutation is
specific for recognition of the CaSR motif rather than a general loss of adaptor function.

## 5. The two assembly chaperones — and what the IPI rows really mean

Eight `GO:0005515 protein binding` IPI rows sit on AP2S1. Seven cite AAGAB (Q6PD74,
`AAGAB_HUMAN`, alpha- and gamma-adaptin-binding protein p34) and one cites CCDC32 (Q9BV29,
`CCD32_HUMAN`; former symbol C15orf57).

**AAGAB.** All seven rows come from proteome-scale interactome screens. The
reference-projection test (QuickGO by `reference=`, full pagination, entities counted not
annotations) gives, per reference: PMID:25416956 1,570 entities; PMID:28514442 2,324;
PMID:29892012 449; PMID:32296183 746; PMID:33961781 4,757; PMID:35271311 1,394;
PMID:40205054 1,815. These are catalogue depositions, not seven independent statements
about sigma2. UniProt does record `NbExp=12` for the pair, which is replication of the
measurement — but the focused mechanistic study shows the association is **not** a direct
sigma2 activity:

> [PMID:31353312 "Interestingly, while the σ2 subunit itself did not associate with AAGAB in co-IP, it interacted with AAGAB when the α subunit was co-expressed"]

> [PMID:31353312 "We observed that the σ2 subunit interacted stoichiometrically with AAGAB and the α subunit"]

So what exists is an α:σ2:AAGAB assembly intermediate, not a σ2–AAGAB binding activity.
The same paper independently confirms AP2S1's requirement in CME
[PMID:31353312 "the uptake of the cargo reporter was abolished in AAGAB KO cells or cells deficient in AP2S1, which encodes the σ2 subunit of AP2 adaptor"].

**CCDC32.** Only two entities carry PMID:33859415, so this row is a focused finding rather
than a projection. The cached record is abstract-only and names the gene by its old symbol
[PMID:33859415 "We also show that C15orf57 encodes a protein that binds the AP2 complex, localizes to clathrin-coated pits and enables efficient transferrin uptake."];
UniProt's curated SUBUNIT line, written from the full text, says the interaction is direct.
The 2026 structural study then shows precisely how CCDC32 engages sigma2 — through a
canonical dileucine cargo motif, i.e. the very site described in §2:

> [PMID:42234739 "CCDC32 contains two other binding sites for the α/σ2 core, a canonical dileucine cargo motif and an α-helical domain that mimics an intramolecular interaction in the α subunit."]

> [PMID:42234739 "In addition, two amphipathic helices in CCDC32 bind to the α/σ2 heterodimer."]

Both partners therefore point back to the same molecular activity, and neither can be
expressed as an informative GO MF today. The bare `protein binding` rows are marked
over-annotated with that reasoning rather than being converted to a term that does not fit.

## 6. The IBA: node PTN000204281

One IBA row, `GO:0016192 vesicle-mediated transport`, GO_REF:0000033. The GOA WITH/FROM
carries the node plus eleven gene donors. The local PAINT slice
(`interpro/panther/PTHR11753/PTHR11753-paint.tsv`, refreshed and unchanged from main)
shows the family has exactly one PTN node with two IBD assertions:

| node | term | seeds in slice | date |
|---|---|---|---|
| PTN000204281 | GO:0043231 intracellular membrane-bounded organelle (C) | 13 | 20260528 |
| PTN000204281 | GO:0016192 vesicle-mediated transport (P) | 10 | 20260828 |

(AP2S1 receives only the GO:0016192 one; there is no GO:0043231 IBA on the gene, and
UniProt's `DR   PAN-GO; P53680; 1 GO annotation based on evolutionary models.` agrees that
exactly one PAN-GO annotation exists.) The slice's GO:0016192 seed list has ten entries
against the eleven gene donors in GOA/QuickGO — GOA additionally carries `FB:FBgn0043012`,
which is present in the node's GO:0043231 seed list. I note the difference rather than
explaining it; both are current PAINT/GOA products and neither changes the verdict.

Donors resolved (UniProt cross-reference lookups; QuickGO checked for the transferred term
on each):

| WITH/FROM | resolves to | what it is | evidence behind it |
|---|---|---|---|
| `CGD:CAL0000182525` | Q59QC5 | *C. albicans* APS3, AP-3 sigma | GO:0006896 Golgi-to-vacuole IMP PMID:20870878 |
| `FB:FBgn0039132` | AP-1sigma (B8A403 among 4 TrEMBL entries) | *Drosophila* AP-1 sigma | GO:0016192 NAS PMID:11598180 |
| `FB:FBgn0043012` | Q9VDC3 | *Drosophila* AP-2 sigma | **GO:0035615 IMP PMID:20226669** |
| `MGI:MGI:1098244` | P61967 | mouse Ap1s1 | GO:0042147 IMP PMID:24928897 |
| `MGI:MGI:1889383` | Q9DB50 | mouse Ap1s2 | **GO:0016192 IMP PMID:24928897**; GO:0016182 IDA/IMP PMID:20203623 |
| `PomBase:SPAP27G11.06c` | Q9P7N2 | *S. pombe* vas2, AP-1 sigma-1 | GO:0042147 and GO:0099638 IDA PMID:19624755 |
| `RGD:620188` | P62744 | rat Ap2s1 — the direct ortholog | GO:0098884 IDA/EXP PMID:17289840 |
| `SGD:S000003561` | P47064 | *S. cerevisiae* APS3, AP-3 sigma | GO:0006896 IMP PMID:9335339 |
| `SGD:S000004160` | P35181 | *S. cerevisiae* APS1, AP-1 sigma-1 | GO:0006896 IMP PMID:17003107 |
| `UniProtKB:P53680` | AP2S1 — **the target itself** | human sigma2 | GO:0048488 IDA/IMP PMID:11102472 |
| `WB:WBGene00000157` | Q19123 | *C. elegans* aps-2, AP-2 sigma | GO:0072583 IMP PMID:25303366 |

`WB:WBGene00000157` is not a UniProtKB accession, so it is not a key in
`PTHR11753-entries.csv` (which in any case holds only 46 representative members and no
*C. elegans* entry). It was resolved instead through UniProt's own WormBase cross-reference
line, `DR   WormBase; F02E8.3; CE07018; WBGene00000157; aps-2.` on Q19123 — a lookup a
database actually performs, not a name match.

**Reading of the node.** The seeds span AP-1, AP-2 and AP-3 sigma subunits across fungi,
flies, nematodes, rodents and human, and their experimental evidence is in *different*
vesicle pathways: Golgi-to-vacuole for the AP-3 seeds, endosome-to-Golgi retrieval for the
AP-1 seeds, endocytosis for the AP-2 seeds. The last common ancestor of that set does
vesicle-mediated transport and nothing more specific, which is exactly the term the curator
placed. This is the case the taxonomy calls out explicitly: `GRANULARITY_MISMATCH` applies
only when donors agree and a finer term was available; here they do not agree in pathway, so
the parent is the correct LCA and there is no failure. Human AP2S1 sits inside the clade
(PANTHER assigns it to PTHR11753) and shows no loss or divergence — its dileucine pocket is
intact (§3) and it has its own experimental CME evidence. No IRD or IKR exists anywhere in
this family's slice. Verdict: **`NO_FAILURE_CORE`**, `ACCEPT`.

The target's own accession appearing among the donors is correct and expected: AP2S1's
GO:0048488 IDA/IMP is one of the descendant evidences the PAINT curator used to place the
IBD. It is marked `SUPPORTS_TRANSFER`, never `CIRCULAR_OR_REDUNDANT`.

## 7. Reference projection: what the 97 rows actually are

Ninety-seven GOA rows reduce to a small term set. Counts, produced by script from the tsv:

| term | evidence | rows |
|---|---|---|
| GO:0005829 cytosol | TAS | **31** |
| GO:0005886 plasma membrane | TAS 22 / ISS 1 / IEA 1 | **24** |
| GO:0005515 protein binding | IPI | **8** |
| GO:0036020 endolysosome membrane | TAS | **5** |
| GO:0030122 AP-2 adaptor complex | TAS 2 / NAS 1 / IEA 1 | **4** |
| everything else | — | 1 each |

The parent brief anticipated "many cargo-specific process rows (receptor endocytosis of X,
Y, Z…)". **That is not what this record contains.** All 60 Reactome rows are
*cellular component* rows — cytosol, plasma membrane, endolysosome membrane, endocytic
vesicle membrane — carried by 47 distinct reaction stable ids. Counted from the tsv: 60
Reactome rows, 14 GO_REF rows and 23 PMID rows, and all 60 Reactome rows carry aspect
`cellular_component`. Reactome contributed no process term at all to AP2S1. The cargo-specific pathways (Nef-mediated CD4 down-regulation,
MHC class II, WNT5A/FZD4, LDL clearance, AMPA receptor trafficking…) appear only as the
*references* of compartment rows.

Projection counts (QuickGO by reference, fully paginated, distinct **entities** counted):

- `Reactome:R-HSA-8868648` "SYNJ hydrolyze PI(4,5)P2 to PI(4)P" → 101 entities, 58 of them
  getting GO:0005829; the largest of the set is `R-HSA-8868658` "HSPA8-mediated ATP
  hydrolysis promotes vesicle uncoating" at 104 entities.
  `R-HSA-8868230`, `-8868236`, `-8868651`, `-8868658`…`-8871194` are the
  same shape. These are participant-compartment assignments for every protein in a CME
  reaction, not statements about AP2S1.
- `PMID:12121421` (Boll 2002, the μ2/FDNPVY paper) → 7 entities; the five AP-2 subunits
  AP2A1, AP2A2, AP2B1, AP2M1 and AP2S1 each receive the *identical* triple
  {GO:0030122, GO:0035615, GO:0072583} as TAS. One reference, one complex-level statement,
  five copies. The paper's experiments are entirely on μ2
  [PMID:12121421 "We show that recognition of the FDNPVY signal is mediated by a binding site in the mu2-subunit that is distinct from the site for the more general YppØ sorting signal"].
  The conclusions are right for sigma2 anyway, but the evidence for them lives elsewhere
  (§2), so those rows are accepted while naming their real grounding.
- The four ComplexPortal NAS references (PMID:12086608, PMID:29184887, PMID:31671891,
  PMID:15941406) give **14 entities each**: the four AP-2 ComplexPortal objects
  (CPX-5149/5150/5152/5153, human and mouse α1/α2 variants) plus the five human and five
  mouse subunit accessions. Complex-level annotation distributed to components — a sound
  practice, but again one statement, not fourteen.
- `PMID:25898166` (CALM/PICALM) → 11 entities for GO:0045334.
- `PMID:10753805` (Pearse 2000 review) → **1 entity**. This is the outlier: three TAS terms
  (GO:0030100, GO:0030122, GO:0048268) placed on AP2S1 alone and on no other protein in GO.
  The cached record is abstract-only, and the abstract concerns the clathrin cage, the μ2
  subunit and the α-appendage; the sigma subunit is not mentioned.
- `PMID:11102472` (SynGO) → 4 entities for GO:0048488: AP2S1, AP2B1 (human and rat) and
  AP2M1. See §8.

## 8. The SynGO synaptic-vesicle rows

Three rows (NAS, IDA, IMP) give `GO:0048488 synaptic vesicle endocytosis` from Morgan et al.
2000. The paper identifies a DLL clathrin-assembly motif and works with AP-2 purified from
bovine brain plus a peptide from the **β2** subunit (`examined a DLL-containing peptide from
the b2 subunit of AP-2`), microinjected into squid giant presynaptic terminals
[PMID:11102472 "Microinjection of these peptides into squid giant presynaptic terminals reversibly blocked synaptic transmission and inhibited synaptic vesicle endocytosis by preventing coated pit formation at the plasma"].
Sigma2 is never assayed separately; the assayed object is the intact complex, of which
sigma2 is an obligate subunit. That is a legitimate complex-level annotation and no reason
to overrule the curator — but it is not evidence of a sigma2-specific synaptic role, and
synaptic vesicle endocytosis is one tissue-specific instance of the general CME function
rather than the core function of a ubiquitously expressed adaptor subunit
(`DR   HPA; ENSG00000042753; Low tissue specificity.`). Hence `KEEP_AS_NON_CORE`.

The same reasoning covers GO:0098884 (postsynaptic neurotransmitter receptor
internalization, ComplexPortal NAS), which has real experimental grounding on the rat
ortholog [rat P62744 carries GO:0098884 IDA/EXP from PMID:17289840, "Molecular determinants
for the interaction between AMPA receptors and the clathrin adaptor complex AP-2"], and the
two GOC term-relationship IEAs it and GO:0048488 generate (GO:0098793 presynapse from
GO:0048488; GO:0098794 postsynapse from GO:0098884).

## 9. The endolysosome-membrane rows — the one clear defect

Five TAS rows place AP2S1 in `GO:0036020 endolysosome membrane`, from
`R-HSA-2130486`, `R-HSA-2130725`, `R-HSA-6784729`, `R-HSA-6784738` and `R-HSA-8855130`.
Reading the cached Reactome entries makes the mechanism plain — these are reactions in
which a *clathrin-coated vesicle entity* is relocated to a downstream compartment while
keeping its full subunit roster:

- `R-HSA-2130486` "Uncoating of clathrin-coated vesicles and fusion with endosomes"
- `R-HSA-6784729` "PCSK9:LDLR:Clathrin-coated vesicle transport from plasma membrane to endolysosome"
- `R-HSA-8855130` "VLDLR:PCSK9:Clathrin-coated vesicle translocates from the plasma membrane to lysosomal membrane"

The first of these is literally the step at which AP-2 leaves. Three independent lines say
the assertion is wrong:

1. **Ontology.** GO's own closure places the AP-2 adaptor complex within the coated pit,
   plasma membrane and clathrin-coated endocytic vesicle (GO:0030122's ancestors include
   GO:0005905, GO:0005886, GO:0045334, GO:0030669, GO:0030666). GO:0036020 is *not* among
   them; its ancestry runs through lysosome and late-endosome membrane.
2. **UniProt.** The record states the opposite of residence in a downstream vesicle:
   `CC       internalizing CCVs and to disengage from sites of endocytosis seconds`
   [`file:human/AP2S1/AP2S1-uniprot.txt`], and lists only `Cell membrane` and
   `Membrane, coated pit` as locations.
3. **Mechanism.** AP-2 membrane recruitment requires PtdIns(4,5)P2, a plasma-membrane lipid;
   Reactome's own `R-HSA-8868648` has synaptojanin hydrolysing it to drive uncoating.

Hence `REMOVE` ×5. This is a database compartment-inheritance artefact, not a curator
judgement being overruled, and no experimental annotation is touched.

By contrast `GO:0030669` (clathrin-coated endocytic vesicle membrane, `R-HSA-5138459`
"WNT5A:FZD4 is endocytosed") and `GO:0030666` (endocytic vesicle membrane, `R-HSA-416639`)
are kept: both are ancestors of GO:0030122 in GO's own structure, so they are entailed by
complex membership rather than contradicted by it.

## 10. The Pearse 2000 TAS trio

`PMID:10753805` uniquely supplies GO:0030100, GO:0030122 and GO:0048268 on AP2S1.

- GO:0030122 AP-2 adaptor complex — correct, and supported many other ways. `ACCEPT`.
- GO:0048268 clathrin coat assembly — real at the complex level, but the clathrin-engaging
  element of AP-2 is the β2 hinge/clathrin box, not sigma2; sigma2 participates only as an
  obligate subunit. `KEEP_AS_NON_CORE`.
- GO:0030100 regulation of endocytosis — definition "Any process that modulates the
  frequency, rate or extent of endocytosis" (QuickGO). AP-2 does not modulate CME; it is the
  cargo-selection machinery that executes it. Annotating core machinery as a regulator is
  role conflation, and the correct term, GO:0072583, is already on the gene from three
  better-grounded rows. `MODIFY` → GO:0072583.

## 11. Other biology, and what is *not* core

- **ARF6 / non-clathrin route.** UniProt cites PubMed:19033387 for a role in maintaining
  post-endocytic trafficking through the ARF6-regulated non-clathrin pathway. No GOA row
  encodes this; it is noted but not proposed as a NEW term, because the cached record is
  abstract-only and the study is on the complex.
- **APP degradation / late-endosome-to-lysosome fusion.** AP2S1 knockdown lowers APP and Aβ
  via enhanced LE-lysosome fusion, and the authors state the effect is *not* endocytic
  [PMID:36412210 "This effect was unrelated to endocytosis but involved lysosomal degradation."].
  This is a single-laboratory finding that would, if generalised, be a second and quite
  different function. It is recorded as a knowledge gap rather than annotated: the paper
  localises APP, not AP2S1, to the late endosome, and it does not argue that sigma2 acts
  there. It is also, notably, *not* what the five Reactome GO:0036020 rows assert — those
  come from coated-vesicle compartment inheritance and predate the paper.
- **Behaviour.** Zebrafish `ap2s1` supports acoustically evoked habituation learning
  [PMID:38550987 "Here, we show that multiple AP2 subunits regulate acoustically evoked behavior selection and habituation learning in zebrafish."].
  Non-human, complex-level, and well downstream of the molecular function; not annotated.
- **Phosphorylation.** UniProt records `MOD_RES 140 /note="Phosphoserine"` from a
  large-scale study (PubMed:18691976). A PTM the protein carries is not an activity and
  generates no annotation.

## 12. What affinage missed

The affinage record is good — trust gates clear, `self_evaluation_pairwise: win`,
`faith_pct: 100.0` — and it correctly centres the narrative on Arg15, the dileucine motif,
CaSR endocytosis and the mouse models. Two limits:

1. **It never cites the structure paper.** Its citation list is
   PMID:23222959, 29479578, 33729479, 36412210, 9040778, 9767099 and one bioRxiv id
   (`PMID:bio_10.1101_2024.07.22.24310683`, non-numeric — a preprint, which I did not use).
   The claim it repeats from Nesbit — that Arg15 "forms key contacts with the dileucine
   motif" — traces to **PMID:19140243** (Kelly et al. 2008, *Nature*), which affinage does
   not list. That paper is the only source for the pocket residues, the KD measurements and
   the YxxΦ specificity control, i.e. for everything in §2 and §3. The parent brief cited
   `PubMed:18497731` for this structure; that PMID resolves to an unrelated FAAH gene-variant
   paper, and the correct id was found by an exact-title search on Europe PMC.
2. **It missed both assembly chaperones as mechanism.** AAGAB (PMID:31353312) and CCDC32
   (PMID:42234739) are the two proteins that explain the eight `protein binding` IPI rows,
   and neither appears in the record. Both were found by independent Europe PMC searches on
   "AP2 dileucine" and "sigma2 dileucine" rather than on the gene symbol — the predicted
   failure mode, where the decisive paper is titled for the partner.

Its `mechanism_profile` GO ids (GO:0060090, GO:0038024, GO:0005768, GO:0005764) were not
imported. GO:0038024 *cargo receptor activity* is defined for proteins that "span
membranes"; sigma2 is a peripheral cytosolic subunit, so the id is wrong for this protein,
and the lysosome/endosome localisations are the same over-reach as §9.

## 13. Summary of judgements

- Core: sigma2 is the cargo-recognition small subunit of AP-2; with the α trunk it forms the
  acidic-dileucine binding site, and through it AP-2 selects `[DE]xxxL[LI]`-bearing
  transmembrane cargo into clathrin-coated pits at the plasma membrane.
- One IBA, `NO_FAILURE_CORE`, correct at the LCA.
- Five `REMOVE`s, all the same Reactome compartment-inheritance artefact.
- One `MODIFY` (regulator→executor).
- Eight bare `protein binding` rows marked over-annotated, with the real activity identified
  and proposed as a new term.
- Two NEW rows: `GO:0005905 clathrin-coated pit` (the defining location of AP-2, curated by
  UniProt from PubMed:33859415 and directly imaged in PMID:15941406, yet absent from GOA)
  and `GO:0055074 calcium ion homeostasis` (the FHH3 role, asserted by UniProt and supported
  by human genetics plus the knock-in mouse, also absent from GOA — added as a downstream
  organism-level role, deliberately not as a core function).

### 13a. The NEW term I decided *not* to add

`GO:0002031 G protein-coupled receptor internalization` looks like the obvious missing
term: Nesbit's experiment measures exactly that, on AP2S1, in human cells. But its GO
ancestry runs through `GO:0045744 negative regulation of G protein-coupled receptor
signaling pathway` and `GO:0009968 negative regulation of signal transduction` (QuickGO
ancestor closure). Annotating AP2S1 to it would therefore assert that sigma2 negatively
regulates GPCR signalling — and the FHH3 data say the opposite direction: loss of AP2σ2
function *reduces* CaSR signalling, giving a rightward EC50 shift
[PMID:23222959 "This revealed that expression of all three mutant AP2σ2s led to a rightward shift in the concentration–response curves"],
consistent with a separate line of work showing CaSR signals from internalized endosomal
compartments [PMID:40510119 "From early endosomes, internalized CaSR is targeted to spatially distinct pathways involving early-to-recycling and late endosomes, to direct compartment-specific signals and regulate GPCR forward trafficking."].
Adding the term would import a sign-inverted regulatory claim through the ontology's own
closure. Recorded as an ONTOLOGY knowledge gap instead of annotated.
