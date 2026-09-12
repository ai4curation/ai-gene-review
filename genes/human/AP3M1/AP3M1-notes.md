# AP3M1 (human, Q9Y2T2) — curation notes

Reviewer journal for the PAINT/affinage wave-B review. Provenance is inline as
`[PMID:NNNN "verbatim quote"]`. Everything asserted here is either quoted, computed in
`AP3M1-bioinformatics/`, or fetched from a named API during this session.

---

## 1. Identity check

`AP3M1-uniprot.txt` is `ID   AP3M1_HUMAN             Reviewed;         418 AA.` with
`AC   Q9Y2T2; Q5JQ12; Q9H5L2;` — the expected accession, not a merged redirect. The record
names the protein "AP-3 complex subunit mu-1" with alternative names "AP-3 adaptor complex
mu3A subunit", "Mu-adaptin 3A", "Mu3A-adaptin". Single MHD domain, residues 176–417
(`FT   DOMAIN          176..417` / `/note="MHD"`), 418 aa, no catalytic features, no
active-site or binding features annotated.

PANTHER family from the UniProt DR line: `PTHR10529` "AP COMPLEX SUBUNIT MU". This is a
*single* family spanning every AP medium subunit — the local
`interpro/panther/PTHR10529/PTHR10529-entries.csv` contains AP1M1, AP1M2, AP2M1, AP3M1,
AP3M2 and AP4M1 as human members — which is the structural reason several IBA rows on this
gene carry AP-1/AP-2-flavoured terms (§5).

InterPro matches (fetched from the InterPro API for Q9Y2T2, `count 7`): IPR001392
(Clathrin adaptor, mu subunit), IPR011012 (Longin-like domain superfamily), IPR018240
(Clathrin adaptor, mu subunit, conserved site), IPR022775 (AP complex, mu/sigma subunit),
IPR028565 (Mu homology domain), IPR036168 (AP-2 complex subunit mu, C-terminal
superfamily), IPR050431 (Adaptor complexes medium subunit). Exactly the seven listed on the
UniProt DR lines — the two lists agree, which matters for the ARBA analysis in §7.

## 2. Which AP-3 is this? AP-3A, not AP-3B

AP-3 is a heterotetramer. UniProt:
`AP3B1 or AP3B2), a medium adaptin (mu-type subunit AP3M1 or AP3M2) and` — i.e. two of the
four subunits come in ubiquitous and neuronal isoforms. Simpson et al. named them when they
characterised the complex: [PMID:9151686 "p47 exists as two isoforms: p47A, which is
expressed ubiquitously, and p47B, which is specifically expressed in neuronal tissues"]
(p47A = mu3A = AP3M1; p47B = mu3B = AP3M2).

The ComplexPortal web service (queried this session) makes the pairing explicit. AP3M1 is a
subunit of exactly the two **ubiquitous** variants:

| complex | name | subunits |
|---|---|---|
| CPX-5051 | Ubiquitous AP-3 Adaptor complex, sigma3a variant | AP3B1, AP3D1, **AP3M1**, AP3S1 |
| CPX-5052 | Ubiquitous AP-3 Adaptor complex, sigma3b variant | AP3B1, AP3D1, **AP3M1**, AP3S2 |
| CPX-5053 | Neuronal AP-3 Adaptor complex, sigma3b variant | AP3B2, AP3D1, AP3M2, AP3S2 |
| CPX-5055 | Neuronal AP-3 Adaptor complex, sigma3a variant | AP3B2, AP3D1, AP3M2, AP3S1 |

UniProt cross-references Q9Y2T2 to CPX-5051 and CPX-5052 only
(`DR   ComplexPortal; CPX-5051; Ubiquitous AP-3 Adaptor complex, sigma3a variant.`). The
delta subunit AP3D1 is shared by all four, which is the pivot for §6: every mouse phenotype
that GOA transfers onto AP3M1 comes from the *mocha* (`Ap3d1`) allele, and a delta-null
removes the neuronal complex as well as the ubiquitous one.

GO has no term for either variant: `GO:0030123` "AP-3 adaptor complex" has **no children**
(QuickGO `/children` returned none). Recorded as a proposed new term.

## 3. What the medium subunit does: YxxΦ cargo recognition

This is the part of AP3M1's biology that GOA does not capture at all, and it is the
best-evidenced thing about the protein.

The general principle was established for the family: [PMID:9151686 "The presence of a μ
subunit in the complex indicates that it plays a role in the sorting of proteins containing
tyrosine-based signals (Ohno et al."] and, in the same paper,
[PMID:9151686 "and recently μ3 has also been shown to bind such sequences (Dell Angelica et
al."].

Direct evidence on mu3A itself, four independent lines:

1. **TGN38 YQRL.** [PMID:9118953 "Like other members of the medium-chain family, the p47A
   chain is capable of interacting with the tyrosine-based sorting signal YQRL from
   TGN38."] p47A is AP3M1.
2. **Combinatorial specificity.** [PMID:9748267 "We have analyzed the selectivity of
   interaction between YXXO signals and the mu1, mu2, and mu3 (A or B) subunits of the AP-1,
   AP-2, and AP-3 complexes, respectively, by screening a combinatorial XXXYXXO library
   using the yeast two-hybrid system."] and [PMID:9748267 "each medium subunit favored
   specific sets of residues at the X and O positions; these preferences were consistent
   with the proposed roles of the different adaptor complexes in rapid endocytosis and
   lysosomal targeting."]
3. **Selectivity for a lysosomal membrane protein.** [PMID:9794796 "we show that the
   cytosolic domain of lgp120 interacts almost exclusively with mu3A."] lgp120 is LAMP1.
   The same paper reports the AP-4 medium subunit behaving differently
   [PMID:9794796 "We also show that the newly identified mu-adaptin-related protein 2 (mu4)
   only interacts weakly with tyrosine-based sorting motifs."]
4. **Structure.** The 2024 human AP-3 cryo-EM series (PDB 9C58–9C5C, all cross-referenced
   from Q9Y2T2 with chain M = 1–418) resolves a LAMP1 YQTI peptide in the mu3 pocket:
   [PMID:39705307 "There is also clear density for the LAMP1 cargo motif in the μ3-CTD
   tyrosine cargo-binding pocket, unambiguously showing that this complex represents the
   cargo-engaged state of AP-3 (Fig."]

Note how well 3 and 4 agree: Stephens & Banting's lgp120 tail and Begley's LAMP1 peptide are
the same YQTI motif on the same protein, twenty-six years apart.

A fifth, independent line comes from virology: [PMID:29028839 "Here, we show that HRSV
Matrix (M) protein interacts with the cellular adaptor protein complex 3 specifically via
its medium subunit (AP-3Mu3A)."] with the motif identified —
[PMID:29028839 "This novel interaction is further substantiated by the presence of a known
tyrosine-based adaptor protein MU subunit sorting signal sequence, YXXФ: where Ф is a bulky
hydrophobic residue, which is conserved across the related RSV M proteins."]

**GOA carries none of this.** The only molecular function on AP3M1 in the GOA file is
`GO:0035615` (IBA, seeded from AP-1/AP-2 donors) plus `GO:0031267` and 23 bare
`GO:0005515` rows. The obvious comparator is the paralogue: human AP2M1 (Q96CW1) carries
`GO:0005048` "signal sequence receptor activity" with **IDA** evidence from PMID:8918456
(QuickGO, queried this session), which is exactly the mu-chain YxxΦ activity. So GO already
has a term and a curation precedent for this on the sister subunit, and AP3M1 simply lacks
the row. That is the main `NEW` recommendation of this review.

### Bioinformatics: is the pocket actually there?

Rather than assert conservation, I measured it — `AP3M1-bioinformatics/cargo_pocket.py`,
results in `AP3M1-bioinformatics/RESULTS.md`. The script downloads the structures and
sequences live, asserts that PDB 9C5B chain M matches Q9Y2T2 at every one of its 418
author-numbered positions and that 1BXX chain A matches Q96CW1 at all 256 of its modelled
positions (so both are in UniProt numbering), then computes heavy-atom contacts at 4.5 Å.

- 9C5B chain M (AP3M1) vs the LAMP1 `SHAGYQTI` peptide: **10 contacts** — E178, Y180, F181,
  V389, L392, F402, K403, G404, V405, K406.
- 1BXX chain A (AP2M1) vs the TGN38 `DYQRLN` peptide: **14 contacts** — F174, L175, D176,
  K203, V401, R402, Y403, L404, V418, I419, K420, W421, V422, R423.
- 9 of AP3M1's 10 contacts sit on alignment columns that are also AP2M1 pocket positions.
  The site is the same site.
- But AP3M1 is identical to AP2M1 at only **5 of the 14** pocket columns (D182, V389, L392,
  K403, V405), while aligning to a residue at all 14. The substitutions include
  AP2M1 W421 → AP3M1 G404 and AP2M1 R402 → AP3M1 N390. Structurally conserved, chemically
  divergent — which is precisely what Ohno's combinatorial screen found functionally.
- Mouse Ap3m1 (Q9JKC8) is identical to human AP3M1 at **14 of 14** of these positions, so
  the ISS/IEA transfers GOA makes from mouse are not crossing a diverged cargo site.

These are encoded as machine-checkable `residue_claims` on the `GO:0035615` row.

## 4. Is AP-3 a clathrin adaptor? No — and three GOA rows assume it is

This is the single biggest curation issue on the gene. The GOA file asserts clathrin three
times: `GO:0030131` "clathrin adaptor complex" (IEA, InterPro2GO), `GO:0035615`
"clathrin-cargo adaptor activity" (IBA), and `GO:0035654` "clathrin-coated vesicle cargo
loading, AP-3-mediated" (NAS, ComplexPortal).

The history: Simpson's group described AP-3 as a non-clathrin coat
[PMID:9151686 "The AP-3 complex is not clathrin associated (Simpson et al."], and UniProt
still records that view (`not clathrin-associated. The complex is associated with the
Golgi`). Dell'Angelica then reported the opposite [PMID:9545220 "In vitro binding assays
showed that mammalian AP-3 did associate with clathrin by interaction of the appendage
domain of its beta3 subunit with the amino-terminal domain of the clathrin heavy chain."]
— note that this is a **beta3** activity, not a mu3A one. The 2024 structural review of the
field states the dispute as unresolved: [PMID:39705307 "AP-3 has been reported to have both
clathrin-dependent (21, 22) and -independent functions (23–25) and is found to only
partially colocalize with clathrin in vivo (26, 27)."]

The 2026 cryo-ET reconstitution settles the coat question: [PMID:42139345 "By demonstrating
that AP3:ARF1 can generate carriers without using a clathrin lattice, we explain the
clathrin independence of AP3-mediated trafficking."] and the same paper places the complex
[PMID:42139345 "Mammalian AP3 (subunits δ, β3, μ3, and σ3) (Fig."] … on early/tubular
endosomes.

Ontology check (QuickGO, this session): `GO:0030131` "clathrin adaptor complex" (def: "A
membrane coat adaptor complex that links clathrin to a membrane") has exactly **two**
children, `GO:0030121` (AP-1) and `GO:0030122` (AP-2). `GO:0030123` (AP-3) is **not** among
its descendants — its ancestors are `GO:0030119` AP-type membrane coat adaptor complex,
`GO:0030117`, `GO:0048475`, `GO:0098796`, `GO:0005737`. GO itself therefore places AP-3
outside the clathrin adaptor complexes, and the term definition says so:
`GO:0030123` def "…AP-3 does not appear to associate with clathrin in all organisms."

So the InterPro2GO row `GO:0030131` asserts, of AP3M1, membership in a class the ontology
explicitly does not put AP-3 in. The mapping fires because IPR001392 is "Clathrin adaptor,
mu subunit" — a family signature covering *all* AP medium subunits, AP-3 and AP-4 included.
That is a demonstrably wrong domain→complex mapping, which is the one licensed use of
`REMOVE` on an IEA row. (The same InterPro pair also yields `GO:0006886` and `GO:0016192`,
which are generically true and stay.)

`GO:0035615`'s definition is "Bringing together a cargo protein with clathrin, responsible
for the formation of endocytic vesicles" — wrong on both counts for AP-3 (no clathrin
lattice; not endocytic). Its parent `GO:0140312` "cargo adaptor activity" is the right level
and is the proposed replacement.

`GO:0035654`'s own definition already hedges ("in some organisms, links clathrin"). Its
grandparent `GO:0035459` "vesicle cargo loading" carries the same assertion without the
clathrin commitment, so that is the proposed replacement, with a request for a
clathrin-neutral AP-3-specific child.

## 5. The five IBAs — nodes, seeds, and where the AP-1/AP-2 leakage is

`just fetch-panther-paint PTHR10529` produced
`interpro/panther/PTHR10529/PTHR10529-paint.tsv` (10 nodes, 18 node-level annotations).
Every donor below was resolved against UniProt this session (`xref:` lookups) or against
`PTHR10529-entries.csv`.

| GOA row | IBD node | seeds (resolved) |
|---|---|---|
| GO:0030123 AP-3 adaptor complex | PTN002237676 | SGD:S000000492 = P38153 yeast **Apm3** (AP-3 mu); dictyBase:DDB_G0277901 = Q9GPF1 *Dictyostelium* **apm3** (AP-3 mu) |
| GO:0005802 trans-Golgi network | PTN000055849 | AT1G60780 = O22715 Arabidopsis **AP1M2**; AT4G24550 = Q9SB50 Arabidopsis **AP4M**; SGD:S000001011 = P38700 yeast **Apm2**; E2RED8 dog **AP4M1**; O00189 human **AP4M1** |
| GO:0006896 Golgi to vacuole transport | PTN000055849 | SGD:S000000492 yeast **Apm3**; SGD:S000001011 yeast **Apm2**; SGD:S000006180 = Q00776 yeast **Apm1** (AP-1 mu); O00189 human **AP4M1** |
| GO:0035615 clathrin-cargo adaptor activity | PTN000055849 | FB:FBgn0024833 = O62531 *Drosophila* **AP-1mu**; FB:FBgn0263351 = O62530 *Drosophila* **AP-2mu**; dictyBase:DDB_G0289247 = Q54HS9 *Dictyostelium* **apm1** (AP-1 mu) |
| GO:0098884 postsynaptic NT-receptor internalization | PTN002575745 | MGI:MGI:1929212 = Q9JKC8 **mouse Ap3m1** (the target's own orthologue) |

Two nodes matter. **PTN002237676** is the AP-3 mu clade node: both its seeds are genuine
AP-3 mu subunits, and AP3M1 is the human AP-3 mu subunit. That IBA is exactly right.
**PTN000055849** is a deep node ancestral to the whole medium-subunit family (its
annotations reach AP3M1 *and* AP4M1), and three of the five IBAs hang off it.

`GO:0035615` is the leakage case the family predicts. Every seed is an AP-1 or AP-2 medium
subunit — the two complexes that really are clathrin adaptors — and the term is then
inherited by AP-3 and AP-4 mu subunits, which are not. The current PAINT slice
(IBD dated 20260828) also lists `UniProtKB:Q9Y6Q5` = human **AP1M2** as a seed; the GOA
WITH/FROM predates that and lists three. Either way the seed set is 100% AP-1/AP-2. Human
AP4M1 (O00189) carries the same `GO:0035615` IBA, and AP4M1's own experimental record
(QuickGO, this session) contains no clathrin activity at all.

Note also what the PAINT curators *did* fence off: `PTN000242370` (the AP-2 mu clade) carries
an **IRD** (negated) for `GO:0005802`, and `PTN002575694` (the stonin clade) carries an IRD
for `GO:0006896`. So the node placements have been actively curated; the objection to
`GO:0035615` is that the clathrin-specific child was placed at a node whose descendants
include two non-clathrin coats, not that nobody was paying attention.

## 6. The mouse *Ap3m1* record, and what GOA transfers from it

Five GOA rows on AP3M1 are `IEA` via GO_REF:0000107 (Ensembl Compara) with
`UniProtKB:Q9JKC8|ensembl:ENSMUSP00000117346`, and two more are `ISS` via GO_REF:0000024
with `UniProtKB:Q9JKC8`. Q9JKC8 is mouse Ap3m1 (UniProt lookup). Querying QuickGO for
Q9JKC8 (31 annotations) gives the experimental originals:

| transferred term | mouse evidence | paper |
|---|---|---|
| GO:0035651 AP-3 adaptor complex binding | IDA (MGI) | PMID:19010779 |
| GO:0008089 anterograde axonal transport | IMP (UniProt) | PMID:21998198 |
| GO:0048490 anterograde synaptic vesicle transport | IMP (UniProt) | PMID:21998198 |
| GO:0098884 postsynaptic NT-receptor internalization | IDA ×3 (SynGO) | PMID:27568566 |
| GO:0098837 postsynaptic recycling endosome | IDA ×3 (SynGO) | PMID:27568566 |

**PMID:21998198** (Larimore et al., MBoC 2011) is the source of both "anterograde" rows. Its
AP-3 genetics are entirely the *mocha* delta allele: [PMID:21998198 "the AP-3–deficient
allele mocha (Ap3d1mh/mh; Kantheti et al."], and the phenotype is
[PMID:21998198 "PI4KIIα was targeted to processes in wild-type primary cultured cortical
neurons and PC12 cells but failed to reach neurites in cells lacking either AP-3 or
BLOC-1."]. Searching the cached full text, the strings `Ap3m1`, `mu3A` and `AP3M` do not
occur; `μ3` occurs twice, both in the introductory sentence naming the heterotetramer's
subunits. So mu3A is never perturbed or assayed — the evidence is complex-level, and since
delta is shared by the ubiquitous and the neuronal complex (§2), the phenotype cannot even
be assigned to AP-3A. Kept, but as non-core, with `SOURCE_WEAK_OR_INFERRED`.

That reading is reinforced by the genetics that *do* separate the two complexes:
[PMID:15537701 "Neurons express adaptor (AP)-3 complexes assembled with either ubiquitous
(beta3A) or neuronal-specific (beta3B) beta3 isoforms."],
[PMID:15537701 "beta3B-containing AP-3 complexes were preferentially targeted to neuronal
processes."] and [PMID:15537701 "Consistently, beta3B deficiency compromised synaptic zinc
stores assessed by Timm's staining and the synaptic vesicle targeting of membrane proteins
involved in zinc uptake (ZnT3 and ClC-3)."] — with the ubiquitous complex going the other
way: [PMID:15537701 "Surprisingly, despite the lack of neurological symptoms,
beta3A-deficient mouse brain possessed significantly increased synaptic zinc stores and
synaptic vesicle content of ZnT3 and ClC-3."]. The synaptic-vesicle cargo job belongs
mostly to the neuronal complex, which does not contain AP3M1.

**PMID:27568566** (Steinmetz et al., Cell Reports 2016) is the one paper that studies mu3A
itself in neurons, in mouse: [PMID:27568566 "As expected, immunohistochemistry localized μ3
to a number of endosomal compartments within pyramidal neurons (Fig."] and
[PMID:27568566 "Knockdown of μ3A prevented"] synaptic scaling. Two caveats worth recording:
the sufficiency experiments are overexpression, and the paper's own conclusion is that the
effect is AP-3-independent ("excess μ3A acts independently of the AP-3A complex"). Kept as
non-core; SynGO curators read the full text and I am not second-guessing the IDA.

**PMID:19010779** (Salazar et al., JBC 2009) cross-linked and affinity-purified AP-3 and
identified associated proteins by MS. Finding mu3A in a purified AP-3 preparation is
complex *membership*, which AP3M1 already asserts through `GO:0030123 part_of`; re-stating
it as the molecular function "AP-3 adaptor complex binding" types an obligate subunit as an
external ligand of its own complex. Marked as over-annotated rather than removed.

## 7. The other electronic rows

`GO:0005737` cytoplasm comes from `ARBA:ARBA00026971`. Fetching
`https://rest.uniprot.org/arba/ARBA00026971` returns a rule with **2388** condition sets and
a single output annotation, `GO:0005737`. Only two of those condition sets mention any
signature AP3M1 carries, and neither can fire for this protein: one requires IPR011012
**AND** taxon *Saccharomyces*; the other requires IPR022775 **AND** IPR016635 **AND**
IPR027156, and AP3M1's complete InterPro match list (§1, seven entries, cross-checked
against the InterPro API) contains neither IPR016635 nor IPR027156. So the row cannot be
reproduced from the rule's published conditions. This repo has already documented the same
pattern for ARBA00027853 (`ARBA00027853-review.yaml`). The annotation itself is harmless and
true — AP-3 is a cytosolic coat — so it is kept as non-core, with the reproducibility problem
recorded rather than used as grounds for removal (the API may not expose everything the
production pipeline uses).

`GO:1904115` axon cytoplasm is GO_REF:0000108 — a logical inter-ontology inference whose
`supporting_entities` is the GO term `GO:0008089`. It is only as good as that row, which is
the *mocha*-derived one. Kept as non-core, flagged as inherited.

## 8. Reference-projection checks (QuickGO, paginated by entity)

| reference | annotations | distinct entities |
|---|---|---|
| PMID:10024875 (TAS ×2, PINC) | 2 | 1 — only AP3M1 |
| PMID:9151686 (NAS, ComplexPortal) | 17 | 14 |
| PMID:9545220 (NAS, ComplexPortal) | 38 | 22 |
| PMID:23247405 (NAS ×4, ComplexPortal) | 178 | 48 |
| PMID:17897319 (HDA) | 246 | 242 |
| PMID:22511774 (IPI ×2) | 53 | 7 |
| PMID:19116314 (IPI) | 10 | 4 |
| PMID:19010779 (mouse IDA) | 35 | 26 |

`PMID:17897319` is a 242-entity placental-lysosome membrane proteome
[PMID:17897319 "We report on additional 86 proteins that were significantly enriched in the
lysosomal membrane fraction."]; a cytosolic coat co-purifying with that fraction is
expected and non-core. `PMID:22511774` and `PMID:19116314` project over 7 and 4 entities
respectively — small, complex-scoped, and consistent with the papers' claims
([PMID:22511774 "BLOC-2, AP-3, and AP-1 coimmunoprecipitated with Rab38 and Rab32 from MNT-1
melanocytic cell extracts."]). Neither is a mass projection.

`PMID:10024875` deserves a note: the two TAS rows exist on AP3M1 and on no other protein in
GOA, even though the paper is about beta3A mutations in Hermansky-Pudlak syndrome. The
reason the curator chose mu3A is in the abstract — [PMID:10024875 "These differential
effects are consistent with the preferential interaction of the AP-3 mu 3A subunit with
tyrosine-based signals involved in lysosomal targeting."] — so the process row
(`GO:0006622`) is well placed. The location row (`GO:0005764` lysosome) is not: the paper
shows AP-3 sorts cargo *to* lysosomes [PMID:10024875 "The AP-3 deficiency results in
increased surface expression of the lysosomal membrane proteins CD63, lamp-1, and lamp-2,
but not of nonlysosomal proteins."], which is a process, not residence in the organelle.

## 9. The bare `protein binding` rows

Twenty-three `GO:0005515` IPI rows. Twenty-two come from six high-throughput interactome
papers — HuRI/Y2H (PMID:25416956, PMID:32296183), BioPlex AP-MS (PMID:28514442,
PMID:33961781), a neurodegeneration Y2H map (PMID:32814053) and the SLC interactome
(PMID:40355756) — with partners AGTRAP, ARNT2, CRMP1, DVL3, FRMD6, HLA-DMB, HTT, IL36RN,
RSPH14, SIPA1L2, SLC12A4, SPAG16, TRIM9, TRIM23. None has functional follow-up naming
AP3M1, and none of them is an AP-3 subunit or a known AP-3 cargo whose sorting was traced.
The UniProt `NbExp` values on these pairs (2–13) are replicate counts inside those same
datasets, not independent studies. All marked over-annotated; a bare `protein binding` row
adds nothing that the informative MF row proposed in §3 does not say better.

The twenty-third (`UniProtKB:Q04671` = OCA2, PMID:19116314, assigned by UniProt rather than
IntAct) is a genuine low-throughput result, but the abstract is all the cache has and the
motifs assayed are **dileucine**, not tyrosine: [PMID:19116314 "The two dileucine signals
physically interact in a differential manner with cytoplasmic adaptors known to function in
trafficking other proteins to melanosomes."]. Acidic dileucine signals are read by the
sigma3/delta hemicomplex, not by the mu3A tyrosine pocket
([PMID:39705307 "This closed form of the complex occludes the two known binding sites for
transmembrane cargo: tyrosine-based YxxΦ motifs (where x is any amino acid and Φ is a bulky,
hydrophobic amino acid) on the μ subunit (12, 13)"] — the dileucine site is on sigma). With
the full text unavailable I cannot tell which construct was used, so this stays as an
over-annotated bare binding row rather than being converted to a cargo-recognition MF.

The two `GO:0031267` rows (RAB38 P57729, RAB32 Q13637; PMID:22511774) are the melanocyte
co-immunoprecipitation above. Real, but a complex-level co-IP in a specialised cell type;
kept as non-core.

## 10. Affinage record

`AP3M1-deep-research-affinage.md` has `self_evaluation_pairwise: loss`, `faith_pct: 50.0`,
`n_discoveries: 1`, `citation_count: 1`, and `.affinage.log` reports the trust gate tripped.
Its entire content is one 2017 proteomics correlation — [PMID:29032074 "We identified 48
such rate-limiting interactions and experimentally confirmed our predictions on the
interactions of AP3B1 with AP3M1 and GTF2E2 with GTF2E1."] — i.e. that AP3B1 depletion
lowers AP3M1 abundance. That is a real and correctly-cited observation about complex
stoichiometry, and it is the only thing in the record; its own summary concedes "no further
mechanistic detail for AP3M1 has been characterized in the available corpus", which is
plainly false for this gene.

**What affinage missed** (every one of these was found by independent Europe PMC search):
the entire YxxΦ literature (PMID:9118953, PMID:9748267, PMID:9794796, PMID:11071885), both
AP-3 cryo-EM papers (PMID:39705307, PMID:42139345) — the first of which is cross-referenced
straight from the UniProt record via PDB 9C58–9C5C — the clathrin-association dispute
(PMID:9545220 vs PMID:9151686), the HPS2 cargo phenotype (PMID:10024875), the mu3A neuronal
paper (PMID:27568566), the beta3A/beta3B genetic dissection (PMID:15537701), and the HRSV
matrix interaction (PMID:29028839) that UniProt itself cites as reference [6]. Marked
`LOW_QUALITY` / `relevance: LOW` in `references`.

## 11. Things that stayed open

- Is human AP3M1 associated with any disease? Searches on `"AP3M1" AND (mutation OR variant
  OR patient)` (143 hits) returned no Mendelian AP3M1 disorder; the human AP-3 diseases are
  HPS2 (`AP3B1`) and HPS10 (`AP3D1`). AP3M1 shares a bidirectional CpG-island promoter with
  adenosine kinase [PMID:14575525 "These mutants should prove useful in elucidating the role
  of AP-3 mu3A in vesicle-mediated protein sorting--a process that is altered in
  Hermansky-Pudlak syndrome."], which is a plausible reason large ADK-region deletions could
  take AP3M1 with them, but no human case has been reported.
- Whether mu3A and mu3B genuinely partition with beta3A and beta3B respectively, or "mix and
  match", was an open question when AP-3 was characterised and I found nothing settling it
  for human cells.
- Whether the residual clathrin association of AP-3 (beta3 hinge, PMID:9545220) has any
  in-cell function, given that carrier formation does not need a clathrin lattice
  (PMID:42139345).
