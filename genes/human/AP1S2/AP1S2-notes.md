# AP1S2 (sigma-2 / sigma1B adaptin) — curation notes

UniProt **P56377** (`AP1S2_HUMAN`), 157 aa, sequence version 1, reviewed. The accession returned
by the live UniProt fetch is the one requested, so this is not a merged-accession mix-up.
X-linked (Xp22), HGNC:560, PANTHER **PTHR11753** "ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY".
GOA snapshot has 50 rows: 24 Reactome TAS, 7 ComplexPortal NAS, 6 IntAct IPI, 6 InterPro2GO IEA,
3 UniProt-SubCell IEA, 1 ARBA IEA, 1 HPA IDA, 1 PINC TAS, 1 GO_Central IBA.

## 1. What the protein is

AP1S2 is one of three vertebrate sigma1 isoforms (sigma1A/AP1S1, sigma1B/AP1S2, sigma1C/AP1S3)
that can occupy the small-subunit slot of the heterotetrameric AP-1 clathrin adaptor. UniProt:
`Adaptor protein complex 1 (AP-1) is a heterotetramer composed of two large adaptins (gamma-type subunit AP1G1 and beta-type subunit`
… `AP1B1), a medium adaptin (mu-type subunit AP1M1 or AP1M2) and a small adaptin (sigma-type subunit AP1S1 or AP1S2 or AP1S3)`
[`file:human/AP1S2/AP1S2-uniprot.txt`]. The GO definition of GO:0030121 already encodes this
heterogeneity — "In at least humans, the AP-1 complex can be heterogeneric due to the existence
of multiple subunit isoforms encoded by different genes (gamma1 and gamma2, mu1A and mu1B, and
sigma1A, sigma1B and sigma1C)" (QuickGO `/ontology/go/terms/GO:0030121/complete`).

The protein was first described by Takatsu et al. as a sigma1A paralogue that pairs with the
large gamma adaptins: "gamma2-adaptin is capable of interacting not only with the sigma1 chain
(called as sigma1A in this paper), the small chain of the AP-1 complex, but also with a novel
sigma1-like protein, designated as sigma1B, which shows an 87% amino acid identity to sigma1A"
[PMID:9733768]. My own alignment reproduces that number exactly — 87.3% over aligned columns
(`AP1S2-bioinformatics/RESULTS.md`), which is a useful check that the accessions being compared
are the intended ones.

## 2. Which claims are sigma1B-specific and which are AP-1-generic

This is the central question for this gene, because most of the GOA rows are complex-level or
family-level projections. The sigma1B-specific evidence is:

- **Assembly into AP-1, and only AP-1.** HA-tagged human sigma1B stably expressed in M1
  fibroblasts co-precipitates gamma1, beta1 and mu1 but not AP-2, AP-3 or AP-4 subunits:
  "all three sigma1-HA isoforms are incorporated into AP-1 complexes containing gamma1, beta1,
  and mu1 subunits but not into complexes including the alphaC subunit of AP-2, the beta3A
  subunit of AP-3, or the epsilon subunit of AP-4" [PMID:21097499]. The same paper shows sigma1B
  pairs with both gamma isoforms: "the gamma1 isoform was incorporated into AP-1 complexes
  containing either sigma1A, sigma1B, or sigma1C, the gamma2 isoform was incorporated into AP-1
  complexes containing sigma1A or sigma1B, but not sigma1C" [PMID:21097499]. This is direct
  human evidence for GO:0030121 and against any AP-2/AP-3/AP-4 assignment.
- **Cargo-signal recognition by the gamma1-sigma1B hemicomplex.** "all AP-1 hemicomplexes
  containing gamma1 (gamma1-sigma1A, gamma1-sigma1B, and gamma1-sigma1C) interact with similar
  avidities with the Nef, tyrosinase, and LIMP-II signals" — and the gamma2-containing ones are
  signal-selective: "the gamma2-sigma1A and gamma2-sigma1B hemicomplexes displayed
  signal-dependent interactions" [PMID:21097499]. So sigma1B is not a passive spacer; it is one
  of the two subunits that form the `(D/E)XXXL(L/I)` binding site.
- **Isoform-specific partner binding.** In yeast-three-hybrid gamma1/sigma1 hemicomplex assays,
  "Rabex-5 binds sigma1B, not sigma1A" and the RabGAP5 RUN domain "binds sigma1B, not sigma1A"
  [PMID:27411398]. This is a genuinely sigma1B-private molecular activity, and it is the
  mechanism by which AP-1/sigma1B opposes the AP-1/sigma1A-ArfGAP1-Rabex-5 complex and damps
  Rab5/Vps34-driven MVB maturation.
- **Tissue-restricted, mostly neuronal biology.** "Expression levels of sigma1B and sigma1C are
  highly variable and tissue specific, with most tissues expressing sigma1A and only one of the
  other isoforms" and "These data demonstrate that sigma1B is not required for ubiquitous,
  'house-keeping' functions of AP-1, but mediates tissue-specific AP-1 functions"
  [PMID:20203623].

The AP-1-generic claims are everything sourced to a pan-AP-1 reagent: the Reactome pathway
reactions, the ComplexPortal projections from PMID:15377783 and PMID:23247405, and the
InterPro2GO family mappings. Those are discussed row by row in the review.

## 3. Residue-level check on the cargo-binding site

Mattera et al. give the sigma-side residue numbers for sigma1A, sigma2 and sigma3A but not for
sigma1B. I mapped them (`AP1S2-bioinformatics/sigma_cargo_site.py`, live UniProt fetch, global
BLOSUM62 alignment, run captured in `sigma_cargo_site.out`):

| sigma1A anchor (P61966) | AP1S2 (P56377) | verdict |
|---|---|---|
| R15 | **R14** | RETAINED (corroborative only for AP-1) |
| A63 | **A62** | RETAINED (abolishing substitution in sigma1A) |
| V88 | **V87** | RETAINED (abolishing substitution in sigma1A) |
| L101 | **L100** | RETAINED (corroborative only for AP-1) |
| I103 | **I102** | RETAINED (abolishing substitution in sigma1A) |

A caveat the bot review correctly pressed on: in AP-1 the sigma-side Arg15 is *not* the
load-bearing basic residue. Mattera et al. state that "interaction with γ1-σ1A depends mainly on
γ1 Arg 15" and list "σ1A Arg 15 and Leu 101 , which can be substituted with relatively little
impact on the ability of γ1-σ1A to recognize (D/E) XXX L(L/I) signals" [PMID:21097499]. So R14
and L100 are corroborative. The positions that carry the argument are the three whose sigma1A
counterparts abolish binding outright: the γ1-σ1A interaction "was abolished only by V88D and
I103S (for Nef) and also by A63D (for tyrosinase)" [PMID:21097499], mapping to AP1S2 V87, I102
and A62. A62 is the one specific to the tyrosinase signal, which is also the signal on which the
γ2-σ1B hemicomplex diverges from γ1-σ1B. This is recorded in the `role` and
`comment` of the R14 residue claim.

All five sigma1A positions whose substitution abolishes or weakens dileucine-signal binding
("the loss of signal binding by the sigma2 V88D or L103S substitutions and the homologous
sigma1A V88D and I103S and sigma3A V94D and L109S substitutions" [PMID:21097499]) are present in
AP1S2. The one difference versus sigma2 (L103 -> I102) is the Leu/Ile difference that
distinguishes the whole AP-1 sigma1 subfamily; sigma1A, which was shown to bind all three test
signals, carries Ile there too. **There is no residue-level argument that sigma1B has lost the
cargo-signal site**, and this is recorded as `residue_claims` on the GO:0035615 row so that the
"fold without function" mirror error is closed off explicitly.

The same script shows human AP1S2 and mouse Ap1s2 (Q9DB50) are **100.0% identical over all 157
human residues**, with the mouse protein differing only by a 3-residue insertion at mouse
143-145. That is the justification for treating the mouse sigma1B knockout literature as
sequence-similarity evidence for human AP1S2 rather than as an untransferable mouse result.

## 4. The mouse sigma1B knockout — what it actually shows

- **Synaptic vesicle reformation from endosomes.** "Synaptic vesicle reformation in cultured
  neurons from sigma1B-deficient mice is reduced upon stimulation, and large endosomal
  intermediates accumulate" [PMID:20203623]. Quantitatively: "Within the first 10 s after
  depleting stimulation, only 46.5% of the exocytosed vesicles become re-available for release
  in sigma1B-deficient neurons compared with 94% in the isogenic controls" [PMID:20203623].
- **AP-1 is presynaptic, inside the SV cluster.** "Such short mean distances between AP-1 and
  synaptophysin (58.8±6.8 nm for WT and 48.4±5.5 nm for 'ko') indicate the localization of AP-1
  within the SV cluster" and "no or very little co-localization was observed between AP1 and the
  post-synaptic marker, Homer, both in WT and knockout boutons; thus supporting a predominantly
  pre-synaptic localization of AP-1" [PMID:20203623]. Note the caveat the authors themselves
  give: the localisation was done with an anti-gamma1 antibody, not an isoform-specific one,
  because "None of them could be unambiguously localized by IFM to either TGN or endosomes,
  indicating that the C-terminal domains of membrane-bound complexes are masked"
  [PMID:20203623].
- **The accumulating compartment is an early endosome.** "The sigma1B(-/-) 'bulk' endosomes
  proved to be classic early endosomes with an increase in the phospholipid phosphatidylinositol
  3-phosphate (PI-3-P)" and "sigma1B deficiency induced alterations in the endosomal proteome
  reveals two major functions: SV protein storage and sorting into endolysosomes"
  [PMID:25128028].
- **Endosome maturation is regulated, not just cargo-sorted.** "AP-1/sigma1A and AP-1/sigma1B
  regulate maturation of these early endosomes into multivesicular body late endosomes, thereby
  controlling synaptic vesicle protein transport into a degradative pathway", with the sign of
  the sigma1B contribution being negative: "Formation of AP-1/sigma1A-ArfGAP1-Rabex-5 complexes
  is prevented by sigma1B binding of Rabex-5 and the amount of endosomal Rabex-5 is reduced"
  [PMID:27411398].
- **A non-neuronal cargo.** In adipose tissue, "sigma1B-specific binding of sortilin requires the
  sortilin DxxD-x12-DSxxxL motif" and "sigma1B deficiency does not lead to a block of sortilin
  transport out of a specific organelle, but the fraction that reaches lysosomes is reduced"
  [PMID:24928897]. Note that the motif quoted is itself a dileucine-type signal, which ties this
  cargo directly to the hemicomplex binding site mapped in section 3.
- **Behaviour.** "The sigma1B-deficient mice have reduced motor coordination and severely
  impaired long-term spatial memory" [PMID:20203623].

## 5. Human disease

Loss-of-function AP1S2 variants cause an X-linked intellectual disability syndrome that has been
described three times under different names. Tarpey et al. found "two nonsense mutations and one
consensus splice-site mutation in the AP1S2 gene on Xp22 in three families" [PMID:17186471];
Saillour et al. mapped Fried syndrome to the same gene, "A mutation in the third intron of AP1S2
was found in all affected male subjects in this large French family" [PMID:17617514]; Cacciagli
et al. identified the Pettigrew syndrome mutation, "The AP1S2 c.426+1 G>T mutation segregates
with the disease in the Pettigrew syndrome family and results in loss of 46 amino acids in the
clathrin adaptor complex small chain domain that spans most of the AP1S2 protein sequence", and
concluded that the separately named disorders "are all the same syndrome with recognition
complicated by highly variable expressivity" [PMID:23756445].

The important cell-biological observation for curation is Borck et al.'s negative result: "no
major alteration of the stability, subcellular localization, and function of the AP-1 complex was
observed in fibroblasts derived from a patient carrying an AP1S2 mutation", which they attribute
to "functional redundancy among AP-1 sigma subunits (sigma1A, sigma1B, and sigma1C)" with "the
phenotype observed in our patients results from a subtle and brain-specific defect of the
AP-1-dependent intracellular protein traffic" [PMID:18428203]. This is why the AP-1-generic,
ubiquitous-trafficking process terms sit awkwardly on this gene: the ubiquitous AP-1 functions
survive loss of sigma1B.

MIM 300629 (gene) / 304340 (phenotype); Orphanet lists Fried syndrome (85335), the
Dandy-Walker/basal-ganglia/seizures syndrome (1568) and the hypotonia/dysmorphism/aggression
syndrome (85329) — the same condition under three registry entries, consistent with
[PMID:23756445].

## 6. The IBA and its PANTHER node

The single IBA row is GO:0016192 vesicle-mediated transport, `WITH/FROM` naming node
`PANTHER:PTN000204281` plus eleven gene-level donors. The family PAINT slice
(`interpro/panther/PTHR11753/PTHR11753-paint.tsv`, fetched for this review) carries exactly two
IBD rows, both on that same node:

```
PTHR11753  PTN000204281  GO:0043231  C  IBD  (13 seeds, incl. UniProtKB:P56377 and UniProtKB:P61966)
PTHR11753  PTN000204281  GO:0016192  P  IBD  (10 seeds)
```

I resolved every GO:0016192 seed through UniProt xref lookup and then queried each donor's own GO
record (`.scratch/resolve_donors.py`; QuickGO `annotation/search`):

| donor | resolves to | own GO:0016192 evidence |
|---|---|---|
| MGI:MGI:1889383 | Q9DB50 `AP1S2_MOUSE` (sigma1B) | IDA + IMP PMID:20203623, IMP PMID:24928897 |
| MGI:MGI:1098244 | P61967 `AP1S1_MOUSE` (sigma1A) | IMP PMID:24928897, TAS PMID:9714600 |
| UniProtKB:P53680 | `AP2S1_HUMAN` (sigma2) | IDA + IMP PMID:11102472 |
| RGD:620188 | P62744 `AP2S1_RAT` | IDA/EXP PMID:17289840 |
| PomBase:SPAP27G11.06c | Q9P7N2 `AP1S1_SCHPO` (vas2) | IDA PMID:19624755 |
| SGD:S000004160 | P35181 `AP1S1_YEAST` (APS1) | IMP PMID:17003107 |
| SGD:S000003561 | P47064 `AP3S_YEAST` (APS3) | IMP PMID:9335339 |
| CGD:CAL0000182525 | Q59QC5 `APS3_CANAL` | IMP PMID:20870878 |
| FB:FBgn0043012 | Q9VDC3 (Dm `AP-2sigma`) | IMP PMID:20226669 on the UniProt-keyed record; NAS PMID:11598180 at the FlyBase gene level |
| FB:FBgn0039132 | Dm `AP-1sigma` (four TrEMBL accessions for one gene) | IMP PMID:22389401 at the FlyBase gene level; the UniProt accessions carry only ISS/IEA |
| WB:WBGene00000157 | `aps-2` (*C. elegans* AP-2 sigma) — no UniProt xref hit and not an accession, so `PTHR11753-entries.csv` cannot resolve it; resolved instead through the GO API `bioentity/gene/WB:WBGene00000157/function` endpoint | GO:0016192 only IEA + IBA — no experimental grounding |

Three things follow.

1. **The node is deep and pan-family.** Its seeds span Arabidopsis, Dictyostelium, budding and
   fission yeast, Candida, fly, worm, rat, mouse and human, and they are sigma subunits of AP-1,
   AP-2, AP-3 *and* AP-4. GO:0016192 is the correct last common ancestor term for that set: the
   donors do not agree on a compartment or a destination, so a more specific child would be
   wrong, not merely bolder. This is not a `GRANULARITY_MISMATCH`.
2. **The target is squarely inside the inheriting clade.** AP1S2 is a PTHR11753 member
   (`PTHR11753-entries.csv` lists `P56377,AP-1 complex subunit sigma-2,…,AP1S2,157`), and it has
   its own experimental grounding through the 100%-identical mouse orthologue. There is no IRD or
   IKR anywhere in the family slice.
3. **The second IBD is informative even though no IBA row carries it.** The GO:0043231 IBD on the
   same node lists `UniProtKB:P56377` — AP1S2 itself — among its seeds. No GO:0043231 IBA appears
   in this GOA snapshot for AP1S2 (QuickGO returns 22 GO:0043231 annotations for P56377, all
   Reactome TAS or ComplexPortal NAS, none IBA); the IBD row is dated 20260528 against the
   20250902 IBA row, so the likeliest reading is simply that the GOA snapshot predates it. I do
   not assert more than that.

Nothing here justifies challenging the IBA. Verdict: `NO_FAILURE_CORE`.

## 7. Reference projection: the ComplexPortal NAS rows

Seven rows are ComplexPortal NAS, and they are the weakest evidence on the gene. ComplexPortal
maintains `CPX-5048` "Ubiquitous AP-1 Adaptor complex, sigma1b variant"
[`file:human/AP1S2/AP1S2-uniprot.txt`], and annotations made on that complex object are projected
onto every subunit including AP1S2. Running the reference-projection test
(`.scratch/refproj.py`, QuickGO paginated by `reference=`, counting entities not annotations):

- **PMID:23247405** → 178 annotations over **48 distinct gene products** and only 5 distinct
  terms (GO:0005765, GO:0005769, GO:0016192, GO:0060155, GO:1903232). One projection, 48 ways.
- **PMID:15377783** → 36 annotations over **18 distinct gene products**, 3 terms.
- **PMID:9733768** → 19 annotations over 9 gene products, 10 terms (a normal, non-projected
  citation pattern).

PMID:23247405 is a *Small GTPases* "extra view" commentary by Bultema & Di Pietro on their own
primary paper, i.e. a genuine NAS. Its AP-1 experiments are RNAi and immunofluorescence in MNT-1
melanocytes using pan-AP-1 reagents, and it does not distinguish sigma isoforms. Two of the five
projected terms do not survive reading it:

- **GO:0060155 platelet dense granule organization.** The only platelet sentence in the paper is
  an explicit prediction about Rab38, not a result about AP-1: "it is likely that the cooperation
  between Rab38 and the ubiquitous transport machinery uncovered in melanocytes also functions in
  the biogenesis of other LROs, such as platelet dense granules and lamellar bodies"
  [PMID:23247405]. Nothing in the paper places AP-1 — let alone the sigma1B variant — in
  megakaryocytes.
- **GO:1903232 melanosome assembly.** AP-1 involvement in melanosomal cargo traffic is real, but
  the paper's own AP-1 depletion result is negative for the mechanism it is cited for:
  "Depletion of AP-1 has no effect on either Rab32 or Rab38 membrane association"
  [PMID:23247405]. And the isoform question is untouched — sigma1B is a tissue-restricted isoform
  [PMID:20203623] and there is no evidence it is the sigma in melanocyte AP-1.

By contrast **GO:0005769 early endosome** from the same projection is independently correct for
sigma1B — the sigma1B-specific literature places AP-1/sigma1B on early endosomes
[PMID:25128028, PMID:27411398] — so that row is accepted on the biology even though its cited
reference is weak. This is the useful distinction: a weak reference is not the same as a wrong
term.

PMID:15377783 (Heldwein et al., AP-1 core crystal structure) is likewise a complex-level
citation: the structure contains "the intact medium and small chains, micro1 and sigma1"
[PMID:15377783] — the crystallised small chain is sigma1A, not sigma1B. The projected terms
(GO:0030121, GO:0032588) are nonetheless correct for AP1S2 on other grounds, so the right action
is to keep them while recording that the reference is complex-level.

## 8. The IPI rows

Six `GO:0005515 protein binding` IPI rows, all IntAct-assigned. Resolving the partners:

- Five rows name **AP1G1** (`UniProtKB:O43747` or its isoform `O43747-2`) — the gamma-1 adaptin,
  which is sigma1B's direct structural partner in the AP-1 core and the other half of the
  dileucine-binding site. UniProt curates it: `P56377; O43747: AP1G1; NbExp=4; IntAct=EBI-1054374, EBI-447609;`
  [`file:human/AP1S2/AP1S2-uniprot.txt`]. `NbExp=4` counts IntAct experiments, not four
  independent studies. This interaction is corroborated by orthogonal, non-high-throughput work
  [PMID:9733768, PMID:21097499].
- One row names **MAB21L2** (`UniProtKB:Q9Y586`, "Protein mab-21-like 2"), from the HuRI binary
  interactome map [PMID:32296183]. UniProt records `P56377; Q9Y586: MAB21L2; NbExp=5; IntAct=EBI-1054374, EBI-6659161;`
  [`file:human/AP1S2/AP1S2-uniprot.txt`]. No follow-up connects MAB21L2 to AP-1 or to membrane
  traffic; a Europe PMC search for AP1S2 with MAB21L2 returns no mechanistic study. Reproducible
  in one assay format, uncharacterised in function.

None of the six cached interactome papers mentions AP1S2 anywhere in its cached text — the pairs
live in supplementary tables — so the quotable evidence for these rows is the UniProt
`CC -!- INTERACTION` block, not the papers' narratives. I say that explicitly rather than
manufacturing a quote.

## 9. The ARBA row

GO:0005737 cytoplasm, `WITH/FROM ARBA:ARBA00026971`. I fetched the rule
(`https://rest.uniprot.org/arba/ARBA00026971`): 2388 condition sets, conditions of type
`FunFam id` (3285), `InterPro id` (689), `taxon` (231) and `PANTHER id` (97); the rule's only
annotation is GO:0005737. Scanning every condition set against AP1S2's actual signature
complement — InterPro IPR000804, IPR011012, IPR016635, IPR022775, IPR044733 (InterPro REST for
P56377), FunFam `3.30.450.60:FF:000009` (UniProt `DR FunFam`), PANTHER PTHR11753 — finds only
two sets that mention anything AP1S2 has:

- set 26: `IPR011012` **AND** taxon *Saccharomyces* — AP1S2 is human, so this cannot fire.
- set 289: `IPR016635` **AND** `IPR022775` **AND** `IPR027156` — and IPR027156 is "AP-2 complex
  subunit sigma", which AP1S2 does not match (its family signature is IPR044733 "AP-1 complex
  subunit sigma").

The rule's FunFam conditions include `3.30.450.60:FF:000003/4/7/8/10/11` but **not** AP1S2's
`FF:000009`. So the published rule, as fetched today, contains no condition set AP1S2 satisfies.
I record this as a source-trace failure rather than as a reason to drop the term: "cytoplasm" is
biologically true for a peripheral-membrane coat subunit on the cytoplasmic face of Golgi and
vesicle membranes, it is just uninformative next to the cytosol and Golgi rows that are already
present.

## 10. What affinage missed

The affinage record (`self_evaluation_pairwise: tie`, trust gate tripped — logged as
`LOW_QUALITY` in `references[]`) describes the correct protein and its narrative is, as far as I
could check it, faithful to the papers it cites. Its ten citations are all numeric PMIDs; none is
a bioRxiv id. What it did not return:

- **PMID:21097499** (Mattera et al. 2011) — the single most useful paper for GO purposes, because
  it is the only *human* experiment that shows sigma1B assembling into AP-1 (and not into AP-2/3/4)
  and the only one that tests gamma1-sigma1B for cargo-signal binding. It is titled for the signal
  class, not for the gene, which is exactly the affinage blind spot. Found by searching the
  mechanism keyword ("dileucine" + "hemicomplex") rather than the symbol.
- **PMID:17360967**, **PMID:14691137** — the earlier hemicomplex papers that establish the
  gamma/sigma1 site in the first place.
- **PMID:9733768** — the paper that named sigma1B, already in GOA as the TAS source for
  GO:0030119, but absent from the affinage citation list.
- **PMID:23247405** and **PMID:15377783** — the two ComplexPortal NAS sources, i.e. seven of the
  50 GOA rows. Affinage never looks at the annotation set, so it cannot flag a projection.

Affinage also under-weights the one negative human result (PMID:18428203, patient fibroblasts
show no AP-1 defect), mentioning it only as a 2008 "Medium"-confidence row; that result is
central to deciding that the ubiquitous AP-1 process terms are non-core for this isoform.

**Searches run** (Europe PMC REST, `resultType=lite`): `AP1S2` (1122 hits), `"sigma1B" AND
adaptor` (9), `"Fried syndrome"` (29), `"Pettigrew syndrome"` (43), `"sigma1B-adaptin"` (1),
`AP1S2 AND zebrafish` (74), `AP1S2 AND (dendritic OR spine OR neuron)` (285), `(AP1S2 OR
"sigma1B") AND knockout` (214), `AP1S2 AND sortilin` (36), `dileucine AND (sigma1 OR "sigma
subunit") AND adaptor` (30), `"hemicomplex" AND dileucine` (68).

**Negative search results worth recording.** There is no AP1S2/ap1s2 zebrafish model in the
literature I could find: the zebrafish AP-1 work is on *ap1g1* (PMID:37108275) and on gamma1
morphants, not on the sigma1B subunit. Likewise I found no study of dendritic spine morphology in
sigma1B-deficient neurons — the mouse work is presynaptic (SV pools, boutons, active-zone
docking) [PMID:20203623], and the only postsynaptic statement is the negative one, that AP-1 does
not colocalise with Homer. Both are recorded as knowledge gaps rather than being filled in with a
plausible-sounding claim.

## 11. Curation decisions in one paragraph

Core: AP1S2 is a subunit of the AP-1 clathrin adaptor (GO:0030121, GO:0030119, GO:0030117) and
contributes to its cargo-adaptor activity (GO:0035615), with the sigma-side dileucine-signal
residues intact; it acts in vesicle-mediated transport and intracellular protein transport at the
TGN/endosome interface (GO:0016192, GO:0006886, GO:0015031); it localises to the Golgi/TGN, to
cytoplasmic vesicle membranes, and to early endosomes (GO:0005794, GO:0000139, GO:0032588,
GO:0030659, GO:0005769). Non-core: the generic compartments (cytosol, cytoplasm), the lysosomal
membrane rows (a coat modelled at the point of uncoating, not a residence), and the
clathrin-coated pit row (the pit term's definition does cover TGN and endosomal pits, so it is
kept rather than removed). Over-annotated: platelet dense granule organization and melanosome
assembly, both ComplexPortal projections of a commentary onto an isoform it never resolved. New:
the sigma1B-specific endosomal synaptic-vesicle biology (GO:0036466, GO:0016182), the Rabex-5
adaptor activity (GO:0030674) and the regulation of endosome maturation (GO:2000641), all coded
ISS from the 100%-identical mouse orthologue rather than IMP on human.
