# ACTR1B (beta-centractin / Arp1B) — review notes

Human ACTR1B, UniProt P42025 (`ACTY_HUMAN`), 376 aa, chromosome 2q11.1-q11.2.
The second of the two human Arp1 (centractin) paralogs; the other is ACTR1A
(alpha-centractin, P61163, also 376 aa).

Reviewed as part of the PAINT + affinage campaign. A sibling agent reviewed
**ACTR1A** in parallel; the point of the exercise was to see whether ACTR1B's
annotations are (a) correctly shared with ACTR1A because both are genuine
dynactin Arp1 subunits, (b) transferred from ACTR1A and false for ACTR1B, or
(c) right for ACTR1B but by a different route. The answer differs per row and
is recorded below.

---

## 1. The central question: is ACTR1B *documented* in dynactin, or assumed?

**Documented, directly, in human, and it does not depend on paralogy at all.**

The founding paper raised **isoform-specific antibodies precisely because the
existing anti-alpha-centractin reagents did not work on beta**, then used 2D
gels to separate the two:

> [PMID:7696711 "As antibodies previously raised against alpha-centractin reacted only poorly with beta-centractin, new antibodies were produced and combined with two-dimensional gel electrophoresis to discriminate the two isoforms."]

and reported both isoforms inside the 20S complex, with no free pool of either:

> [PMID:7696711 "Both isoforms were found predominantly in the cytosolic fraction as a part of a previously identified 20S complex (referred to as the dynactin complex) with no evidence for a free pool of either isoform."]

> [PMID:7696711 "The isoforms were found in a constant ratio of approximately 15:1 (alpha:beta) in the dynactin complex."]

So the identification of beta-centractin in dynactin was made with reagents
designed *not* to cross-react with alpha. This is the opposite of a paralog
transfer.

Modern interaction proteomics agrees and adds the whole roster. Querying IntAct
for P42025 (`ws/interaction/findInteractionWithFacet`, 146 binary records, 87
unique partners) returns ACTR1B partnered with **every** dynactin subunit
except DCTN2's absent paralogs: DCTN1, DCTN2, DCTN3, DCTN4, DCTN5, DCTN6,
ACTR10 (Arp11), CAPZA1, CAPZA2, CAPZB — **and ACTR1A itself**
(PMID:28514442 BioPlex 2.0, PMID:33961781 BioPlex 3.0, both anti-tag coIP).
Two consequences:

- ACTR1B contacts both ends of the filament (CAPZ at the barbed end, Arp11 at
  the pointed end) plus the shoulder (DCTN1/DCTN2) and the pointed-end complex
  (DCTN4/5/6), i.e. it sits in a fully assembled dynactin, not a subcomplex.
- Because ACTR1B co-purifies with **ACTR1A**, the two paralogs are in the *same*
  filament. At a 15:1 alpha:beta ratio over the 8 filament protomers, that
  implies roughly one beta protomer in every second dynactin particle — a
  genuinely sub-stoichiometric subunit of a hetero-oligomeric filament, not a
  separate beta-only dynactin.

A 2025 result closes the loop using the same trick the 1994 paper used — a
paralog-specific antibody. The study that solved the human dynactin structure probed
its effector's binding with **anti-Arp1b**:

> [PMID:40186871 "These Dre1 variants were tested in co-transfection assays for binding to multiple dynactin subunits (p150glued, p50-dynamitin [DCTN2], Arp1b) as well as to dynein"]

> [PMID:40186871 "Eluates were immunoblotted with anti-p150glued, anti-p50-dynamitin, anti-dynein 74 kDa, anti-Arp1b, anti-FHL2, anti-Strep, and anti-GAPDH antibodies."]

Both of those are Methods sentences, so the *result* is carried separately:

> [PMID:40186871 "A single substitution in CR1, in which phenylalanine 195 was changed to proline or to alanine (F195P or F195A) and which is predicted to disrupt the strand fold, decreased binding of endogenous dynactin subunits and dynein to the transfected Dre1 variants"]

Binding can only be *decreased* from a baseline, and a conservative F195Y
replacement "did not affect Dre1 binding to dynactin" — so the endogenous subunits
assayed do bind wild-type Dre1. Arp1b is one of the three, detected with a
paralog-specific antibody. Hence: **endogenous beta-centractin is among the dynactin
subunits recovered on Dre1** — a modern, human, paralog-resolved result independent
of AP-MS, thirty years after the 2D-gel work. The per-subunit bands live in Figure
2D, which the cached text does not render, so the claim is made at exactly that
strength and no further.

Note the irony: those authors chose **anti-Arp1b** as their representative
Arp1-filament readout while depositing a structure that models all eight protomers as
alpha. (Missed on my first pass because the paper spells it `Arp1b`, lower-case b,
and my context grep used `Arp1B`; the PR reviewer caught it.)

## 2. Where the two paralogs are, and are not, distinguishable

**Not distinguishable by tissue.** The founding paper's Northerns:

> [PMID:7696711 "Comparisons of Northern blots of human tissues indicated that alpha-centractin and beta-centractin mRNAs are equally distributed in all populations of mRNA examined, whereas the expression of gamma-centractin appears to be tissue specific."]

Note the tissue-restricted isoform is *gamma*, not beta. HPA agrees for ACTR1B
[file:human/ACTR1B/ACTR1B-uniprot.txt "DR   HPA; ENSG00000115073; Low tissue specificity."]
and P61163's entry carries the same `Low tissue specificity` call. So the common
shorthand that ACTR1B is a tissue-restricted variant of ACTR1A is wrong.

**Distinguishable by abundance within the complex** — 15:1 (above).

**Distinguishable by requirement in cells.** BioGRID-ORCS CRISPR-screen hit
frequency differs about 2.8-fold:
[file:human/ACTR1B/ACTR1B-uniprot.txt "DR   BioGRID-ORCS; 10120; 197 hits in 1155 CRISPR screens."]
versus `DR   BioGRID-ORCS; 10121; 557 hits in 1172 CRISPR screens.` in the
UniProt P61163 flat file (17.1% vs 47.5% of screens). ORCS pools essentiality
with other phenotypes so this is a soft signal, but it points the same way as
the stoichiometry: alpha is the workhorse, beta is dispensable in most lines.

**Distinguishable structurally — but only as absence of data.** See §4.

**Not distinguishable by disease genetics.** ACTR1B was screened alongside
ACTR1A and DCTN1-6 in inherited peripheral neuropathy and came up empty:
> [PMID:26662454 "No variants of disease significance were identified in this study suggesting the dynactin genes are unlikely to be a common cause of IPNs."]

## 2b. The QuickGO queries behind the load-bearing claims

Three claims here rest on QuickGO rather than on a file in the repo, so the exact
queries are recorded for reproducibility. All run **2026-07-26** against
`https://www.ebi.ac.uk/QuickGO/services`.

1. **"ACTR1A carries none of the four Reactome granule/extracellular annotations"**
   — corroborates the four REMOVEs; the topological argument stands without it:
   ```
   /annotation/search?geneProductId=UniProtKB:P42025&limit=200
   /annotation/search?geneProductId=UniProtKB:P61163&limit=200
   ```
   Totals 21 and 43. On ACTR1B but not ACTR1A: `GO:0005576` (x2 TAS), `GO:0034774`,
   `GO:1904813`, `GO:0016020`. On ACTR1A but not ACTR1B: `GO:0005875`, `GO:0005938`,
   `GO:0016192`. Everything else — including all three IBAs and the centrosome
   IEA+IDA pair — is identical between the paralogs.

2. **"GO:0106006 IBA reaches only five human proteins, and PTN007551901 delivers it
   to exactly ACTR1A and ACTR1B"** — load-bearing for the MODIFY:
   ```
   /annotation/search?goId=GO:0106006&taxonId=9606&geneProductType=protein&evidenceCode=ECO:0000318&limit=200
   ```
   5 hits: HIP1 and HIP1R (`PTN000045135|SPAC688.11`), DCTN2
   (`PTN000394123|SPCC11E10.03`), ACTR1A and ACTR1B (`PTN007551901|SPBC1347.12`).
   The same query on `GO:0030473` returns 4 hits and shows the *other* node,
   `PTN000233666`, on both centractins — which is how the two-node structure was found.

3. **Per-donor evidence for each propagated term** (used throughout section 3):
   ```
   /annotation/search?geneProductId=UniProtKB:<ACC>&goId=<GO_ID>&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100
   ```
   run for every WITH/FROM accession x term pair, collecting `goEvidence`. Also
   ```
   /annotation/search?goId=GO:0140660&taxonId=9606&geneProductType=protein&limit=50
   ```
   which returns **zero hits** — the basis for the annotation-gap claim.

## 3. WITH/FROM resolution, and what each donor carries itself

Every accession in GOA column 11 was resolved, and each donor was then queried
in QuickGO for **its own** evidence for the propagated term
(`/annotation/search?geneProductId=...&goId=...&goUsage=descendants`).
Experimental codes counted: EXP IDA IPI IMP IGI IEP HTP HDA HMP HGI HEP.

| Token | Resolves to | Status |
|---|---|---|
| `PomBase:SPBC1347.12` | O94630 `ARP1_SCHPO`, *S. pombe* arp1 | Swiss-Prot |
| `SGD:S000001171` | P38696 `ARP1_YEAST`, *S. cerevisiae* ARP1/ACT5 | Swiss-Prot |
| `UniProtKB:F2Z5G5` | `ACTZ_PIG`, *Sus scrofa* ACTR1A | Swiss-Prot |
| `UniProtKB:Q5BBX7` | ANIA_01953 / AN1953, *Aspergillus nidulans* | **TrEMBL, "Uncharacterized protein"** |
| `WB:WBGene00013168` | *C. elegans* arp-1 / Y53F4B.22 | **2 TrEMBL accessions** (`x-total-results: 2`): Q9NA98 and U4PR70, both unreviewed, both named "Actin" |
| `PANTHER:PTN000233666` | PANTHER tree node, not a protein | family/ortholog node |
| `PANTHER:PTN007551901` | PANTHER tree node, not a protein | node restricted to the two human centractins (see §5) |

Two caveats recorded rather than hidden: **Q5BBX7 is unreviewed and its protein
name is "Uncharacterized protein"**, so its *name* is worthless as evidence —
but its *annotations* are not (it carries an IMP, below). And WBGene00013168 maps
to two TrEMBL accessions; the second, U4PR70, has **zero** GO annotations, so the
worm support rests entirely on Q9NA98.

`source_entities` in the review YAML were generated **from GOA column 11 by
construction**, not typed by hand, and re-verified afterwards by diffing every
`propagation_review.source_entities` list against the WITH/FROM field of the
matching GOA row: 8 propagation reviews, 0 mismatches, counts equal on every row.
(For the four Reactome rows, which have an empty WITH/FROM, the reaction id is
used as the source entity.)

Per-donor evidence for each propagated term:

**GO:0005869 dynactin complex** — every resolvable donor carries its own
experimental annotation:
- O94630 pombe arp1: IPI (PMID:25736293, with SPCC11E10.03 = Jnm1) + NAS
- P38696 yeast ARP1: IDA (PMID:9658168) + IPI (PMID:18245366)
- F2Z5G5 pig ACTR1A: IPI (PMID:33734450)
- Q9NA98 worm arp-1: IDA (PMID:20964796)
- U4PR70: nothing at all
- and human ACTR1A itself carries the same IBA **plus** TAS PMID:7696711

**GO:0030473 nuclear migration along microtubule** —
- Q5BBX7 *A. nidulans*: **IMP, PMID:10467007** — the strongest donor. That paper
  cloned the gene and identified it as Arp1:
  > [PMID:10467007 "We have cloned one of the genes, nudK, and determined that it encodes the actin-related protein Arp1, which is a component of the dynactin complex. This provides the first evidence that dynactin is involved in nuclear migration in A. nidulans."]
- O94630 pombe arp1: IMP + NAS for the descendant GO:0030989
- F2Z5G5 pig ACTR1A: IDA for the descendant GO:0030989, assigned by
  **ComplexPortal** from PMID:36071160 (Chaaban & Carter, the dynein-dynactin-
  BICDR1 cryo-EM/single-molecule paper). This donor row looks wrong:
  GO:0030989 is defined as "Oscillatory movement of the nucleus involved in
  meiosis I. This oscillatory movement is led by an astral microtubule array
  emanating from the **spindle pole body**..." — a structure pig cells do not
  have, from a paper that assayed reconstituted motility on microtubules, not
  meiosis. Flagged in `suggested_questions`. It does not invalidate the parent
  term GO:0030473, whose own definition is organism-neutral.
- human ACTR1A: IBA only.

**GO:0106006 cytoskeletal protein-membrane anchor activity** — only two tokens,
and only one is a protein:
- O94630 pombe arp1: **EXP, PMID:25736293** (single experimental donor)
- F2Z5G5 pig ACTR1A and human ACTR1A: IBA only.

## 4. Residues: does beta-centractin retain the ATP site and the polymerisation interface?

Arp1 genuinely is actin-like and genuinely polymerises — unlike the ARP11/ACTR10
capping subunit — so canonical actin annotations are not automatically suspect
here:

> [PMID:12857853 "but Arp1 has a vanishingly low critical concentration for polymerization"]

but its filament is a defined-length, non-dynamic ruler rather than a treadmilling
polymer:

> [PMID:12857853 "Interestingly, the filaments formed by pure, isolated Arp1"]
> [PMID:12857853 "other dynactin components provide a ruler activity that governs Arp1 assembly."]

so terms about filament *dynamics* would not transfer even though *polymerisation*
does. No such term is in GOA for ACTR1B, so nothing needed removing on that basis.

I tested residue retention rather than assuming it —
`ACTR1B-bioinformatics/analyze.py`, results in
[file:human/ACTR1B/ACTR1B-bioinformatics/RESULTS.md]. Method: derive the contact
residues **from the structure of human dynactin itself** (PDB 9B85, the 2025
cryo-EM structure obtained by *Chlamydia* Dre1 affinity purification), not from
conventional actin by analogy, then test retention in ACTR1B by alignment.

The structure is itself the key negative finding:

- All **8** Arp1 filament protomers of 9B85 (chains A-G, I) are modelled as
  **ACTR1A**, each with a bound **ADP**; the ninth filament position is
  conventional beta-actin (chain H) and the pointed-end cap is ACTR10.
- **PDBe maps 0 PDB entries to P42025.** ACTR1B is in no deposited structure at
  all. Its filament incorporation is a biochemical fact, not a structural one —
  and at 3.0-5.0 A local resolution in the filament
  [PMID:40186871 "the local resolution of the Arp1 filament ranged from 3 to 5 Å"]
  two 90%-identical paralogs could not have been told apart anyway.

Retention results (contacts within 4.0 A; PDB 9B85 chain A is 1:1 with P61163
1-376 by SIFTS, asserted at runtime):

| | nucleotide site (18 res.) | Arp1-Arp1 interface (37 res.) |
|---|---|---|
| ACTR1B (P42025) | **17/18** | **32/37** |
| pig ACTR1A (donor) | 17/18 (1 gap) | 37/37 |
| pombe arp1 (donor) | 13/18 | 20/37 |
| yeast ARP1 (donor) | 10/18 | 20/37 |
| beta-actin | 11/18 | 16/37 |
| ACTR10 / Arp11 | 6/18 | 10/37 |

All 6 divergent positions are conservative, none is a gap, and all 6 are
**conserved in mouse Actr1b (Q8R5C5)**, so they are fixed features of the beta
paralog rather than human noise. At 4 of the 6 the ACTR1B residue is
*independently* present in another Arp1 orthologue or in conventional actin.

The single nucleotide-site difference is the most informative one:
**position 215, ACTR1A K -> ACTR1B R** — and pombe arp1, yeast ARP1, worm arp-1,
*A. nidulans* AN1953 **and beta-actin all have Arg there** (beta-actin R210).
ACTR1B carries the ancestral/consensus residue and ACTR1A is the outlier. The
beta-centractin nucleotide site is therefore intact, and if anything more
canonical than alpha's. That makes the loss of `GO:0005524 ATP binding` from
GOA a defect (see §6), not a correction.

One asymmetry worth an experiment rather than a conclusion: the Arp1-Arp1
interface is **37/37 invariant** between human and pig alpha-centractin at 90.3%
overall identity, yet ACTR1B differs at 5/37 at essentially the same overall
identity (90.4%). The interface is under strict purifying selection along the
alpha orthologue lineage but is diverging at roughly the background rate between
the paralogs — consistent with relaxed constraint on a sub-stoichiometric
protomer that never has to tile the whole filament. All 5 changes are
conservative (V45M, Y197L, S207T, I213V, I268V), so this does not argue against
incorporation; it is a hypothesis, recorded in `suggested_experiments`.

## 5. The molecular-function row is the real defect: GO:0106006

`contributes_to GO:0106006 cytoskeletal protein-membrane anchor activity`,
IBA, dated 2026-04-16, WITH/FROM `PANTHER:PTN007551901|PomBase:SPBC1347.12`.

Three findings, in order of weight.

**(a) The node is centractin-specific and single-sourced.** Asking QuickGO which
human proteins hold GO:0106006 by IBA returns exactly 5: HIP1 and HIP1R (from
`PTN000045135`/pombe SPAC688.11), DCTN2 (from `PTN000394123`/pombe
SPCC11E10.03), and **ACTR1A + ACTR1B from `PTN007551901`/pombe SPBC1347.12**.
So `PTN007551901` is the Arp1/centractin node, and the entire experimental basis
for the human annotation is one *S. pombe* paper. HIP1/HIP1R are the paradigm
users of this term (they bridge F-actin to clathrin and plasma-membrane lipids);
the dynactin subunits arrived here from a different kind of experiment.

**(b) The donor paper shows a process requirement, not a bridging activity —
and explicitly puts the membrane-binding elsewhere.** PMID:25736293 identified
three pombe dynactin subunits and found them needed for cortical dynein
anchoring, but the cortical receptor binds dynein *without* dynactin, and what
the dynactin subunits were shown to do was microtubule regulation:

> [PMID:25736293 "Cortical factor Num1 (also known as Mcp5), which was also required for dynein anchoring, bound to dynein independently of dynactin."]
> [PMID:25736293 "Whereas Num1 suppressed the sliding of dynein foci along the cortex, Arp1, Mug5 and Jnm1 were involved in the regulation of shrinkage and bundling of microtubules."]

That is a fission-yeast **meiotic-prophase** context, and it supports
"required for cortical anchoring", not "is the molecule that anchors".

**(c) GO:0106006's own differentia is not met.** Its definition is *"The binding
activity of a molecule that brings together a cytoskeletal protein or protein
complex and a plasma membrane lipid or membrane-associated protein, in order to
maintain the localization of the cytoskeleton at a specific **cortical membrane**
location."* Arp1 does have a documented membrane-skeleton partner — but on
**intracellular** membranes at the Golgi, not the cortex:

> [PMID:11461920 "Here, we demonstrate that Arp1 binds directly to the Golgi-associated betaIII spectrin isoform."]
> [PMID:11461920 "We hypothesize that the interaction between betaIII spectrin and Arp1 recruits dynein and dynactin to intracellular membranes and provides a direct link between the microtubule motor complex and its membrane-bounded cargo."]

confirmed in the 2025 human-dynactin paper's own framing:

> [PMID:40186871 "Dynactin binds MTs anchored at the GA as well as to βIII spectrin on GA membranes through its Arp1 subunit."]

So the term is *near*-right in kind and wrong in the compartment clause. And note
that this spectrin work is alpha-directed ("Centractin (ARP1)", PMID:8991093;
PMID:11461920) — extending it to beta would itself be a paralog transfer, so I
did **not** propose `spectrin binding` for ACTR1B.

**What Arp1 demonstrably does provide** is the backbone the rest of the complex
is built on. UniProt says so for both fungal donors — P38696: *"ARP1 forms the
backbone filament of the dynactin rod structure and serves as the scaffold for
the remaining subunits"* — which is verbatim the definition of `GO:0140378
protein complex scaffold activity`: *"A structural molecule activity of a
protein-containing complex component that serves to hold the complex together.
Protein complex scaffolds are integral members of complexes."* So there are two defensible structural MFs. **MODIFY -> GO:0005200 structural
constituent of cytoskeleton** is listed first, on precedent: it is the term
conventional beta-actin carries, *S. cerevisiae* ARP1 holds it by its own **IDA**
(PMID:9658168), and **ACTR10/Arp11 -- the capping subunit of this very filament --
already holds it by IBA with the `enables` qualifier**. `GO:0140378 protein complex
scaffold activity` is offered second: its definition is tighter but it has no
precedent in this family. Decisive for the ordering: the term is attached to the
*shared* node `PTN007551901`, so one node cannot deliver a different structural MF
to each paralog — and the independent ACTR1A review converged on GO:0005200. PAINT
should receive one actionable recommendation, not two competing ones.

A collateral observation reinforcing the choice: UniProt's cross-reference block for
P42025 still lists
[file:human/ACTR1B/ACTR1B-uniprot.txt "DR   GO; GO:0005200; F:structural constituent of cytoskeleton; IBA:GO_Central."]
which is **absent from current GOA for both paralogs**, while GO:0106006 sits at a
*different* PANTHER node and is dated 2026-04-16. Whatever the edit history, the
present state is that the two human centractins carry a membrane-anchor MF and no
structural MF, even though *S. cerevisiae* ARP1 holds GO:0005200 with its own
**IDA** (PMID:9658168, verified in QuickGO) — i.e. the term GOA dropped from these two
genes is the one an orthologue holds experimentally.

Also: the qualifier should become `enables`, not `contributes_to`. Scaffold
activity is the subunit's own activity; `contributes_to` is for complex-level
activities the subunit cannot perform alone.

## 6. The nucleotide MF was lost as collateral — and the right ligand is ADP, not ATP

UniProt still shows
[file:human/ACTR1B/ACTR1B-uniprot.txt "DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW."]
and the `ATP-binding` / `Nucleotide-binding` keywords are on the entry, but the
term is absent from the current GOA download. This is the GO_REF:0000043
Swiss-Prot-keyword pipeline retirement, which removed keyword-derived
annotations wholesale — not a judgement about ACTR1B.

But the term to restore is **`GO:0043531 ADP binding`, not `GO:0005524 ATP binding`**.
ATP binding by Arp1 has never been shown. The paper that purified native Arp1 and
characterised its polymerisation says so in as many words:

> [PMID:10074429 "is predicted to bind ATP and possibly polymerize"]

What *has* been observed is ADP: entity 10 of PDB 9B85 is ADENOSINE-5'-DIPHOSPHATE,
present in all eight Arp1 protomers (chains A-G, I), while the single
conventional-actin protomer (chain H) carries AMP-PNP instead. Combined with the
residue retention from §4 — 17/18 nucleotide contacts conserved, the single change
being to the residue five other family members carry — `GO:0043531` is proposed as a
`NEW` row with **ISS** evidence (inferred from the ADP-bound ACTR1A protomers, since
ACTR1B is in no structure). The with/from is the sequence accession `UniProtKB:P61163`
alone; the PDB entry is cited as a reference rather than placed in with/from. If a
curator objects even to ADP, the fallback is the parent `GO:0000166 nucleotide
binding`, still better than the present state of no nucleotide MF at all. The
independent ACTR1A review reached the same ADP-over-ATP conclusion from the same
coordinates.

The same paper also bounds the polymerisation claim in the other direction: Arp1
filaments annealed over time but never reached conventional actin-filament length, so
no filament-dynamics term is proposed for either paralog.

## 7. The Reactome neutrophil-granule rows: a paralog-pair argument

ACTR1B carries four annotations ACTR1A does not:
`GO:0005576 extracellular region` (x2), `GO:0034774 secretory granule lumen`,
`GO:1904813 ficolin-1-rich granule lumen` — all TAS from
`Reactome:R-HSA-6798748` "Exocytosis of secretory granule lumen proteins" and
`R-HSA-6800434` "Exocytosis of ficolin-rich granule lumen proteins", i.e. the
Neutrophil degranulation pathway, whose membership derives from Rorvig et al.'s
neutrophil granule proteomics (Reactome's own summation cites
"Rorvig et al. 2009, 2013").

ACTR1B has no signal peptide and no transmembrane segment (the P42025 FT table
contains only CHAIN, MOD_RES and VARIANT features), and its UniProt
SUBCELLULAR LOCATION is
[file:human/ACTR1B/ACTR1B-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytoskeleton. Cytoplasm, cytoskeleton,"]
only. A cytosolic actin-fold protein with no free pool cannot be topologically
inside a granule lumen or secreted.

The decisive argument is the paralog pair. **ACTR1B and ACTR1A are in the same
complex, with alpha at 15x the abundance.** If beta-centractin were genuinely a
granule-lumen cargo, alpha-centractin would necessarily be one too — and it
carries none of these four annotations. The asymmetry can only be detection
stochasticity in a granule proteome, so it is not evidence of localisation for
either. Same argument applies to `GO:0016020 membrane` (HDA, PMID:19946888),
which ACTR1B has and ACTR1A does not; that paper concedes the point about its own
list:

> [PMID:19946888 "The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes."]

Conversely `GO:0070062 extracellular exosome` (HDA, PMID:23533145) is on **both**
paralogs from the same urine-EV proteome — consistent, but a bulk EV shotgun
proteome of ~900 proteins with no orthogonal validation, so over-annotated
rather than removable.

## 8. The five `GO:0005515 protein binding` rows

Resolved partner by partner via IntAct, since GOA collapses the two
PMID:12857853 rows in the review stub but they are two different experiments:

| Reference | Partner | IntAct method | Call |
|---|---|---|---|
| PMID:12857853 | Q14203 DCTN1 (p150Glued) | **density sedimentation** + western blot, both partners neutral | co-complex, not direct |
| PMID:12857853 | Q9QZB7 mouse Actr10 (Arp11) | **pull down** | real direct dynactin-internal contact; mouse partner (UniProt marks it `Xeno`) |
| PMID:26638075 | Q14203 DCTN1 | proximity-dependent biotinylation (BioID) | proximity, dynactin co-membership |
| PMID:33961781 | Q14203 DCTN1 | anti-tag coIP (BioPlex 3.0) | co-complex |
| PMID:32814053 | P42858 HTT | **two-hybrid array + two-hybrid pooling + validated two hybrid, all from this one publication** | screen hit, not independently replicated |

The DCTN1 rows deserve a caution: p150 does not contact the Arp1 filament
directly, it is held in the shoulder and reaches the filament via the four p50
subunits —

> [PMID:33734450 "The unique architecture of the shoulder securely houses the p150 subunit and positions the four identical p50 subunits in different conformations to bind dynactin's filament."]

and DCTN1 is not even modelled in 9B85. So `enables protein binding` from a
co-sedimentation/AP-MS pair of dynactin subunits records complex co-membership,
which `part_of GO:0005869` already states far more informatively. Kept as
non-core rather than removed, since IPI is experimental and the partners are real.

The HTT row is different. UniProt reports `P42025; P42858: HTT; NbExp=3`, which
reads like triplicate independent support, but all three IntAct records come from
**PMID:32814053 alone** (three Y2H variants in one systematic
neurodegeneration-focused screen). HTT's documented route to dynactin in the
literature is via HAP1 to p150Glued, not via Arp1. Marked over-annotated.

## 9. Redundant parents

- `GO:0005815 microtubule organizing center` (IEA, ARBA) is a strict ancestor of
  `GO:0005813 centrosome`, which ACTR1B has by IDA (PMID:21399614).
- `GO:0005856 cytoskeleton` (IEA, SubCell SL-0090) is a strict ancestor of
  `GO:0005869 dynactin complex` — verified from the QuickGO ancestor list for
  GO:0005869, which contains GO:0005856, GO:0015629 (actin cytoskeleton) and
  GO:0005875 (microtubule associated complex).
- `GO:0005737 cytoplasm` (IDA, LIFEdb GFP fusion) is an ancestor of the cytosol
  row.

None is wrong; all three are true-but-uninformative and kept as non-core.

That GO:0005869 sits under GO:0015629 *actin cytoskeleton* is also the reason a
`structural constituent of cytoskeleton` framing for Arp1 is not a category
error: the ontology already classifies dynactin as part of the actin
cytoskeleton.

## 10. Curation recommendations issued

1. `GO:0106006` -> `GO:0005200 structural constituent of cytoskeleton` (alternative:
   `GO:0140378 protein complex scaffold activity`), qualifier `contributes_to` ->
   `enables`. Affects **both** ACTR1A and ACTR1B via PANTHER node `PTN007551901`;
   stated once, naming both genes.
2. Re-code the `GO:0005869` TAS PMID:7696711 row as **IDA**. The cited paper is
   not a review — it made isoform-specific antibodies and ran 2D gels on
   cytosolic fractions. TAS understates the strongest evidence ACTR1B has.
   Applies to ACTR1A's row from the same paper too.
3. Restore a nucleotide MF lost to the GO_REF:0000043 retirement, as `GO:0043531 ADP
   binding` rather than `GO:0005524 ATP binding` — ADP is what is modelled in all eight
   Arp1 protomers of 9B85, whereas ATP binding by Arp1 is still only predicted.
4. Retire the four Reactome granule-lumen/extracellular rows.
5. Fix the pig ACTR1A `GO:0030989` IDA (ComplexPortal, PMID:36071160) —
   spindle-pole-body-defined meiotic term on a mammalian in vitro motility paper.
6. `GO:0140660 cytoskeletal motor activator activity` currently has **zero human
   annotations** (QuickGO, taxonId=9606, protein). Dynactin is the textbook
   cytoskeletal motor activator; this is an annotation gap for the whole complex.

## 11. Things the affinage record got right, and its limits

`self_evaluation_pairwise: win`, trust gates clear. Its central claim — ACTR1B as a stoichiometric minor
subunit of 20S dynactin at ~1:15 versus alpha, with no free pool, from
PMID:7696711 — checks out verbatim against the abstract (§1); the direction of
the ratio is quoted the other way round in the source (15:1 alpha:beta) but the
biology is identical. Its own `molecular_activity` grounding
(`GO:0005198 structural molecule activity`) points the same way as the GO:0140378
conclusion reached here independently, one level more general.

Its two low-confidence findings are abundance-change observations in proteomic
comparisons — beta-centractin altered on platelet GPVI activation
(PMID:20107233), down-regulated in dendritic cells pulsed with
high-metastatic-potential HCC lysates (PMID:17619203, PMID:17925177). These are
differential-abundance correlations, not function, and none of them assays
ACTR1B. Not used for any annotation.

`PE 1: Evidence at protein level` for ACTR1B: the protein is detected repeatedly
by MS (RN 5-9 of the UniProt entry, including direct protein sequencing of
residues 239-255). What is missing is *functional/biochemical* dissection of
beta-centractin specifically — no beta-selective knockdown, no beta-only
dynactin reconstitution, no beta-specific phenotype.
