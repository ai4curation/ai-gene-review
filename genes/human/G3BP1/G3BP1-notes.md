# G3BP1 (human, Q13283) — curation notes

Reviewed for the [Stress Granule Assembly project](../../../projects/STRESS_GRANULES.md),
issue [#3953](https://github.com/ai4curation/ai-gene-review/issues/3953). G3BP1 is one of
the two core nucleators the project page flagged as unreviewed.

## Provenance of this file

No deep-research provider was reachable from the environment this review was run in:
`just deep-research human G3BP1 --provider perplexity` failed with
`Provider 'perplexity' not available. Available: claude_code`, and
`just deep-research-claude-code human G3BP1` failed with `Not logged in`. Per CLAUDE.md
this file holds the research record instead; it is **not** a provider artifact and must not
be renamed to `G3BP1-deep-research-*.md`. If a provider becomes available later, generate a
real deep-research file alongside this one rather than replacing it.

All 55 PMIDs cited in `G3BP1-goa.tsv` were present in `publications/`; nothing needed
fetching. 30 of the 55 are full text, 25 abstract-only — relevant where noted below.

## What G3BP1 is

466 aa (Q13283, sequence version 1). Architecture, from the UniProt feature table:

| Region | Residues | Role |
|---|---|---|
| NTF2 domain | 11–133 | dimerisation; binds the GIM motif of CAPRIN1/USP10/UBAP2L |
| acidic disordered region | 142–225 | autoinhibitory; phosphoregulated (Ser149) |
| disordered | 255–329 | linker |
| RRM | 340–415 | RNA binding |
| RG-rich (RGG) | 410–466 | RNA binding, 40S association, protein crosslinking |

The NTF2 domain is the best-characterised part structurally — 23 PDB entries cover
residues 1–139 (`3Q90`, `4FCJ`, `5FW5`, `6TA7`, `8TH1`, `9IVQ`, …). There is no structure of
a nucleotide-binding module, because there is no nucleotide-binding module (see the
helicase section).

## Core mechanism: an RNA-dependent condensate switch

Three back-to-back 2020 *Cell* papers converged on the same mechanism, and this is the
claim the review treats as G3BP1's core function.

- G3BP1 is the central node of the stress-granule protein–RNA network and acts as a
  switch: [PMID:32302571 "The central node of this network is G3BP1, which functions as a
  molecular switch that triggers RNA-dependent LLPS in response to a rise in intracellular
  free RNA concentrations."] (Yang et al.; note the cached `title:` for this PMID is the
  Yang "tunable switch" paper, not Guillén-Boixet).
- The switch is a conformational one, gated by autoinhibition:
  [PMID:32302572 "We show that, under non-stress conditions, G3BP adopts a compact
  auto-inhibited state stabilized by electrostatic intramolecular interactions between the
  intrinsically disordered acidic tracts and the positively charged arginine-rich region.
  Upon release from polysomes, unfolded mRNAs outcompete G3BP auto-inhibitory interactions,
  engendering a conformational transition that facilitates clustering of G3BP through
  protein-RNA interactions."] (Guillén-Boixet et al.)
- And it is the RNA-binding capacity of the network's nodes, not sequence specificity,
  that decides whether condensation happens: [PMID:32302570 "Protein-interaction networks
  can be viewed as interconnected complexes (nodes) of RNA-binding domains (RBDs), whose
  integrated RNA-binding capacity determines whether LLPS occurs upon RNA influx."]
  (Sanders et al.; abstract only in cache.)

This is exactly `GO:0140693 molecular condensate scaffold activity` ("Binding and bringing
together two or more macromolecules in contact, permitting those molecules to organize as a
molecular condensate"), which GOA already carries by IDA from all three papers plus
PMID:34739333 and PMID:36692217. It is the core MF in this review.

Genetic requirement is independent and strong:
[PMID:27022092 "We now show that cells lacking both G3BP1 and G3BP2 cannot form SGs in
response to eukaryotic initiation factor 2α phosphorylation or eIF4A inhibition, but are
still SG-competent when challenged with severe heat or osmotic stress."] — note the
stress-specific caveat, which is why `GO:0034063` is right but "essential for all stress
granules" would not be. Paralog redundancy with G3BP2 was shown earlier:
[PMID:23279204 "Although single knockdown of either G3BP1 or G3BP2 in 293T cells partially
reduced the number of SG-positive cells induced by arsenite, the knockdowns of both genes
significantly reduced the number."]

Mechanistic sub-parts:

- 40S recruitment via the RGG: [PMID:27022092 "G3BP interacts with 40S ribosomal subunits
  through its RGG motif, which is also required for G3BP-mediated SG formation."] This
  grounds `GO:0043024 ribosomal small subunit binding` (IDA) and explains how stalled
  preinitiation complexes get into granules.
- Opposed NTF2-domain partners: [PMID:27022092 "Caprin1/USP10 binding to G3BP is mutually
  exclusive: Caprin binding promotes, but USP10 binding inhibits, SG formation."] Both
  partners use the same pocket: [PMID:36279435 "The crystal structures of the nuclear
  transport factor 2-like (NTF2L) domain of G3BP1 in complex with the G3BP1-interacting
  motif (GIM) of Caprin-1 and USP10 show that both GIMs bind to the same hydrophobic pocket
  of G3BP1."]
- Disassembly is ubiquitin-triggered, with G3BP1 as the target rather than the actor:
  [PMID:34739333 "Specifically in the setting of heat shock, disassembly required
  ubiquitination of G3BP1, the central protein within the stress granule RNA-protein
  network."] — that paper traces the route onward through FAF2 to p97/VCP but does not
  identify the E3 ligase (it never mentions TRIM21). The ligase was named later:
  [PMID:36692217 "TRIM21 catalyzes K63-linked ubiquitination of the SG core protein, G3BP1
  (G3BP stress granule assembly factor 1), and G3BP1 ubiquitination can effectively inhibit
  LLPS, in vitro."] Either way G3BP1 is the substrate of the disassembly machinery, not a
  participant in it, so it is **not** annotated to `GO:0035617 cytoplasmic stress granule
  disassembly` — per CLAUDE.md, being the thing a process acts on is not participation. The
  same paper supplies a clean dissociation showing this is specific to disassembly:
  [PMID:34739333 "2, F and G and movie S2), indicating that assembly of stress granules is
  independent of ubiquitination of G3BP1."]

## Second role: priming cytosolic nucleic-acid sensors

G3BP1 uses the same multivalent-scaffold chemistry on the innate-immune sensors.

- cGAS: [PMID:30510222 "G3BP1 enhanced DNA binding of cGAS by promoting the formation of
  large cGAS complexes. G3BP1 deficiency led to inefficient DNA binding by cGAS and
  inhibited cGAS-dependent interferon (IFN) production."] UniProt adds that this is
  condensation-linked (`CC FUNCTION`, citing PubMed:34779554 — not in GOA, so not reviewed
  here).
- RIG-I: [PMID:30804210 "we overexpress G3BP1 with RIG-I in HEK293T cells and found that
  G3BP1 significantly enhances RIG-I-induced ifn-b mRNA synthesis."] with the interaction
  mapped to the RGG and direct dsRNA binding by the same region.

Both support the `GO:0032481` rows and the `GO:0051607` row. Treated as a second core
function, since the UniProt curators describe it as essential
(`CC FUNCTION`: "Plays an essential role in innate immunity by promoting CGAS and RIGI
activity") and because it is a distinct output of the same activity, not a pleiotropic
side-effect.

## The helicase annotations are wrong

`GO:0003678` (DNA helicase), `GO:0003724` (RNA helicase), `GO:0033677` (DNA/RNA helicase)
and `GO:0016887` (ATP hydrolysis) trace, through every one of their 12 rows, to a single
1999 report: [PMID:9889278 "Human DNA helicase VIII (HDH VIII) was isolated in the course
of a systematic study of the DNA unwinding enzymes present in human cells. From a HeLa cell
nuclear extract a protein with an Mrof 68 kDa in SDS-PAGE was isolated, characterised and
micro-sequenced."] and [PMID:9889278 "Microsequencing of the polypeptide showed that this
enzyme corresponds to G3BP, an element of the Ras pathway which binds specifically to the
GTPase-activating protein."]

The propagation chain is worth laying out, because all of it is one paper:

| Row | Evidence | Where it comes from |
|---|---|---|
| IDA ×3 (FlyBase) | PMID:9889278 | the paper itself |
| TAS ×2 (PINC) | PMID:9889278 | the paper itself |
| EXP (UniProt, `GO:0016887`) | PMID:9889278 | the paper itself |
| IEA ×2 (UniProt) | `EC:3.6.4.12`, `EC:3.6.4.13` | UniProt EC numbers, whose only evidence is `ECO:0000269|PubMed:9889278` |
| IEA (RHEA, `GO:0016887`) | `RHEA:13065` | the `CC CATALYTIC ACTIVITY` line, same evidence tag |
| IBA ×3 (GO_Central) | `PANTHER:PTN002581351` | `WITH/FROM` is `PTN002581351|UniProtKB:Q13283` — the node's only descendant evidence is Q13283's own IDA |

Per `projects/IBA_REVIEW.md`, the target appearing in its own `WITH/FROM` is normally a
marker of genuine experimental grounding, and short donor lists are not weak. The problem
here is narrower and specific: PTN002581351 has no descendant evidence *other than* the
target's own 1999 IDA, so the IBA adds no independent support and stands or falls with that
paper. Compare the SG-assembly IBA on the same gene, at node PTN000074905, whose
`WITH/FROM` spans fly, fission yeast, budding yeast and both human paralogs — that is what
a well-seeded node looks like.

A QuickGO census of all 11 reviewed members of PTHR10693 (part 2 of
[`G3BP1-bioinformatics/RESULTS.md`](G3BP1-bioinformatics/RESULTS.md)) makes that concrete
and checkable rather than merely asserted:

- Helicase terms occur in **exactly one subfamily, SF21** — the G3BP1 orthologs (human,
  mouse, cattle, orangutan).
- **Q13283 is the only member of the family, in any species, with experimental evidence for
  any helicase term.** Mouse G3bp1 carries 12 helicase rows, cattle 7, orangutan 5 — and
  every one of them is ISO, ISS, IBA, IEA or RCA. The 1999 human paper is the sole
  experimental seed for the whole family.
- The paralogous SF10 subfamily (G3BP2 in human, mouse and orangutan) has **none**, and
  neither do the fungal (`nxt3`, `BRE5`), nematode (`gtbp-1`) or plant members.

So the claim entered the family through one report and spread by propagation, rather than
being independently observed anywhere. A genuinely ancestral enzymatic activity would not
look like this.

The 1999 result has not been independently reproduced in the 27 years since, and the
protein has none of the machinery the activity requires. A reproducible check is in
[`G3BP1-bioinformatics/RESULTS.md`](G3BP1-bioinformatics/RESULTS.md): G3BP1 has zero hits
for Walker A/P-loop, Walker B, DExD/H box, SF2 motif VI, SF2 motif III and the Q motif;
none of its 19 domain/family signatures names a helicase or a RecA/AAA/P-loop ATPase; and
no nucleotide-binding or ATP binding-site feature is annotated. The same test flags all
four positive controls (DDX3X, EIF4A3, BLM, UPF1) and neither of the two fold-matched
negative controls (NUTF2 for the NTF2 domain, HNRNPA1 for the RRM+RGG half) — i.e. G3BP1's
architecture does not score positive by accident. The annotated domains also tile the whole
protein, leaving no room for the two ~200-residue RecA-like lobes an ATP-dependent helicase
needs.

The parsimonious reading is that the HeLa nuclear-extract fraction contained a genuine
helicase alongside abundant G3BP1, and microsequencing identified the wrong one of the two —
microsequencing says which protein is in the band, not which carries the activity. All 12
rows are therefore `REMOVE`, and a `source_defects` entry asks UniProt to retire the two EC
numbers, the `ATP-dependent DNA helicase VIII` alternate name, and the helicase sentences in
`CC FUNCTION` / `CC CATALYTIC ACTIVITY` / `CC COFACTOR`.

One thing that is **not** evidence for the helicase: InterPro `IPR012677`
"Nucleotide-bd_a/b_plait_sf" on the entry. That is the α/β-plait fold shared by RRMs; it
describes single-stranded nucleic-acid binding and fold ancestry, not ATP hydrolysis.

## The Ras connection is a name, not a function

`GO:0007265 Ras protein signal transduction` is a single TAS row from the paper that named
the gene: [PMID:8649363 "G3BP physically associates with the SH3 domain of GAP, which
previously had been shown to be essential for Ras signaling."] and
[PMID:8649363 "G3BP coimmunoprecipitates with GAP only when cells are in a proliferating
state, suggesting a recruitment of a GAP-G3BP complex when Ras is in its activated
conformation."] — note "suggesting". The term's definition requires "An intracellular
signaling cassette in which a small monomeric GTPase of the Ras subfamily relays a signal";
binding the SH3 domain of a GAP does not show that G3BP1 relays anything. Nothing in the
intervening 30 years established a step. UniProt itself now carries the RASA1 interaction as
`By similarity` only (`CC SUBUNIT`: "Binds to the SH3 domain of Ras GTPase-activating
protein (RASA1) in proliferating cells (By similarity)"), i.e. not from a human experiment.
There is a residual thread — HRAS-dependent dephosphorylation gates recruitment to granules
(UniProt `CC SUBCELLULAR LOCATION`, citing PubMed:37672657) — so the term is not flatly
false, which is why this is `MARK_AS_OVER_ANNOTATED` rather than `REMOVE`.

## The endoribonuclease claim

PMID:11604510 reported G3BP1 as a phosphorylation-dependent endoribonuclease
["G3BP exclusively cleaves between cytosine and adenine (CA) after a specific interaction
with RNA through the carboxyl-terminal RRM-type RNA binding motif."]. UniProt hedges it
("May also act as a phosphorylation-dependent sequence-specific endoribonuclease in vitro"),
and — importantly for this review — **GOA carries no endoribonuclease term for G3BP1**
(`GO:0004521` is absent from the GOA file). So there is nothing to review, and proposing it
as `NEW` would be wrong: the activity has the same single-paper, never-reproduced,
no-catalytic-residues profile as the helicase, and a 2010 secondary source still describes
it only as attributed [PMID:20180778 "G3BP1 is also an RNA-binding protein with
endoribonuclease activity that is recruited to 'stress granules' after stress stimuli."].
Recorded instead as a `suggested_questions` entry. The same paper's Ser149 result is real
and is why the `GO:0005634 nucleus` rows are kept (non-core):
["A G3BP mutant in which this serine is changed to alanine remains exclusively cytoplasmic,
whereas a glutamate for serine substitution that mimics the charge of a phosphorylated
serine is translocated to the nucleus."]

## ComplexPortal rows

Four rows come from ComplexPortal and are complex-level claims propagated to the subunit.
UniProt lists both complexes: `CPX-21432` "CAPRIN1-G3BP1, stress granules assembly
regulating complex" and `CPX-26721` "G3BP1-USP10, deubiquitinase complex".

- `GO:0016579 protein deubiquitination` (IDA, PMID:34469731) — from `CPX-26721`. The
  catalysis is USP10's; G3BP1 has no DUB domain, so `GO:0004843 cysteine-type deubiquitinase
  activity` would be wrong for it. The cached full text of PMID:34469731 (Garshott et al.,
  iRQC) is entirely about RNF10 and USP10 acting on 40S uS3/uS5 and never mentions G3BP. I
  considered and rejected reading that as a wrong-gene source defect: the row is a
  *complex-level* assertion projected onto a member, not a claim that G3BP1 was assayed in
  that paper, and the projection is substantively defensible — G3BP1's RGG region is what
  holds the complex on its substrate [PMID:27022092 "Thus, G3BP associates preferentially to
  40S ribosomal subunits rather than 80S ribosomes, and both Caprin1 and USP10 are bound to
  40S-associated G3BP."]. Substrate presentation is doing part of the work, so
  `involved_in` survives the CLAUDE.md participation test. Kept as non-core.
- `GO:0062030 negative regulation of cytoplasmic stress granule assembly` (IDA,
  PMID:27022092) — the USP10-bound state is assembly-incompetent; consistent with how the
  project page records USP10's own rows (kept as non-core).
- `GO:0062029` / `GO:0140694` (NAS, PMID:36279435) — from `CPX-21432`. `GO:0140694
  membraneless organelle assembly` is a strict ancestor of `GO:0034063`, which this review
  accepts, so it is `TOO_GENERAL`.

## Localisation rows

- `GO:0010494 cytoplasmic stress granule` (9 rows) and `GO:0005829 cytosol` (5 rows,
  including `is_active_in`) — accepted. The cytosol row matters mechanistically: the
  autoinhibited switch sits in the cytosol and the condensate forms from there.
- `GO:0005737 cytoplasm` — correct but less specific than the cytosol rows the gene already
  carries; `MODIFY`.
- `GO:0005634 nucleus` — real but minor (Ser149-phospho form, resting cells); non-core.
- `GO:0043204 perikaryon` — `ISS`/`IEA` from mouse P97855 via `UniProtKB-SubCell:SL-0197`.
  Plausible (G3BP1 is abundant in neurons and figures in neuronal granule biology) but
  nothing human-specific; non-core.
- `GO:0005925 focal adhesion` — a single HDA row from a 905-protein focal-adhesion proteome
  whose authors explicitly flag that half their list may be background:
  [PMID:21423176 "More importantly, we show that protein abundance of half (459/905) the FA
  proteome is altered by myosinII activity and half remain constant as core FA components or
  non-specific contaminants."]. G3BP1 is not named anywhere in the cached text (the
  identification is in uncached supplementary tables), and no follow-up localises G3BP1 to
  adhesions. An abundant cytosolic condensate protein in an isolated-adhesion preparation is
  what co-isolating background looks like. `MARK_AS_OVER_ANNOTATED`.

## RNA-binding rows

- `GO:0003729 mRNA binding` (IBA at the well-seeded PTN000074904 node, plus IEA from mouse)
  — accepted; this is the informative term.
- `GO:0003723 RNA binding` — two HDA rows from mRNA interactome capture
  [PMID:22658674 "we describe a systematic, unbiased, and comprehensive approach, termed
  "interactome capture," to define the mRNA interactome of proliferating human HeLa cells."]
  and [PMID:22681889 "We developed a photoreactive nucleotide-enhanced UV crosslinking and
  oligo(dT) purification approach to identify the mRNA-bound proteome"]. Both assays select
  poly(A) mRNA, so they support the more specific `GO:0003729`; `MODIFY`.
- `GO:0003676 nucleic acid binding` — IEA from `InterPro:IPR035979`; same `MODIFY`.

The 2020 mechanism is specifically about *unfolded, protein-free* RNA, so
`GO:0003727 single-stranded RNA binding` would also be defensible. Not proposed: G3BP1
already carries `GO:0003729`, and adding a second RNA-binding term would be redundant
coverage rather than new information.

## Protein binding

71 of the 139 rows are bare `GO:0005515` IPI rows. Per the protein-binding policy these are
all `REMOVE` — uninformative, not false. Worth noting what they consist of: 34 of the 71 are
SARS-CoV-2-era rows recording the viral N protein's capture of G3BP1 to dismantle stress
granules (PMID:33495715, PMID:34035218, PMID:34400613, PMID:34901782 and others), which is a
real and well-studied phenomenon — it just belongs to N, not to a `protein binding`
annotation on G3BP1. The functionally informative partner interactions (CAPRIN1, USP10,
UBAP2L, CGAS, RIGI, 40S) are already captured by better terms elsewhere in this review.

## Not proposed as NEW

Applying the CLAUDE.md `NEW` bar:

- `GO:0035617 cytoplasmic stress granule disassembly` — G3BP1 is the ubiquitinated substrate
  that VCP extracts, not a participant. VCP carries this term; G3BP1 should not.
- `GO:0004521 RNA endonuclease activity` — single unreproduced paper, no catalytic residues;
  see above.
- `GO:0003727 single-stranded RNA binding` — redundant with `GO:0003729`.
- `GO:0034198 cellular response to amino acid starvation` and similar stress-response
  parents — G3BP1 responds to many stresses through one mechanism already captured by
  `GO:0034063`; enumerating stressors would be over-annotation.
- Nothing is proposed for the mTORC1/astrin link (PMID:23953116) or the autophagy-receptor
  link (PMID:36692217): in both, G3BP1 is the cargo or the scaffold being acted on.

## Open questions recorded in the review

1. Does anything reproduce an ATP-dependent unwinding activity for recombinant G3BP1, or
   should the EC numbers be retired outright?
2. Is the Ser149-phospho nuclear pool functional, and is the CA-specific endoribonuclease
   activity real?
3. Does GO want a term for "condensate-scaffold-mediated sensor activation", given that
   G3BP1 uses one activity on both mRNA and cGAS?
