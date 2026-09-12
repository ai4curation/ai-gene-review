# AP3M2 (mu3B-adaptin) — curation notes

UniProt **P53677** (`AP3M2_HUMAN`, "AP-3 complex subunit mu-2", 418 aa, chromosome 8,
HGNC:570). Verified the accession returns the intended protein rather than a merged
record: the fetched entry is `ID   AP3M2_HUMAN             Reviewed;         418 AA.`
with `GN   Name=AP3M2;`. PANTHER family **PTHR10529** "AP COMPLEX SUBUNIT MU"
(`DR   PANTHER; PTHR10529; AP COMPLEX SUBUNIT MU; 1.`).

GOA snapshot: **26 rows**, of which 4 IBA, 2 ISS, 11 IEA, 4 NAS, 1 TAS — and **no
experimental rows at all**. So this review is almost entirely a propagation audit.
A live QuickGO pull for `P53677` at review time returned the same 26 rows as the
cached `AP3M2-goa.tsv`, so the snapshot is current.

One snapshot divergence worth flagging but not actionable: the UniProt record's own
`DR   GO` block lists `GO:0006897; P:endocytosis; IBA:GO_Central` and the entry says
`DR   PAN-GO; P53677; 5 GO annotations based on evolutionary models.`, whereas GOA
carries only 4 IBAs and no `GO:0006897`. The PTHR10529 PAINT slice fetched for this
review carries no `GO:0006897` IBD node either. No row was added for it: the review
follows GOA.

---

## 1. What the protein is

AP3M2 is one of two mammalian **mu3 medium subunits** of the heterotetrameric AP-3
adaptor. UniProt states the composition explicitly:

> `CC       Adaptor protein complex 3 (AP-3) is a heterotetramer composed of two`
> `CC       large adaptins (delta-type subunit AP3D1 and beta-type subunit AP3B1 or`
> `CC       AP3B2), a medium adaptin (mu-type subunit AP3M1 or AP3M2) and a small`
> `CC       adaptin (sigma-type subunit APS1 or AP3S2). {ECO:0000250}.`
> — `file:human/AP3M2/AP3M2-uniprot.txt` (quoted line-by-line: a `file:` supporting_text must sit on one physical line)

The two mu3 paralogues define the two AP-3 isoforms. AP-3A is the ubiquitous complex
(beta3A/AP3B1 + mu3A/AP3M1); AP-3B is the neuronal complex (beta3B/AP3B2 +
mu3B/AP3M2), with the delta and sigma3 subunits shared. Nakatsu et al. state the
pairing and, importantly, that it is **obligate**:

- [PMID:15492041 "In contrast, μ3B is exclusively expressed in neurons and forms the neuron-specific AP-3B complex along with β3B, another neuron-specific subunit"]
- [PMID:15492041 "indicating that β3B can assemble with only μ3B and not μ3A to constitute the neuron-specific AP-3B"]

ComplexPortal encodes exactly this: `CPX-5053` "Neuronal AP-3 Adaptor complex, sigma3b
variant" and `CPX-5055` "…sigma3a variant" both list AP3D1 + AP3B2 + **AP3M2** +
AP3S2/AP3S1. Both ComplexPortal records are cross-referenced from the UniProt entry.
This matters for the review because every ComplexPortal `NAS` row on AP3M2 is a
complex-level statement projected onto the subunit.

The historical literature calls the protein **p47B**. Pevsner et al. cloned it from rat
and reported the expression pattern that gave rise to the "neuron-specific" framing
[PMID:8076832 "Rat p47B mRNA is detected exclusively in brain and spinal cord, and may participate in nervous system-specific functions such as biogenesis or recycling of synaptic vesicles."].
Simpson et al. restated it when naming AP-3
[PMID:9151686 "p47 exists as two isoforms: p47A, which is expressed ubiquitously, and p47B, which is specifically expressed in neuronal tissues (Pevsner et al., 1994)."].

### But human AP3M2 is not neuron-restricted

The "exclusively brain and spinal cord" statement is a 1994 rodent Northern blot. The
human gene behaves differently. Human Protein Atlas (fetched live, see
`AP3M2-bioinformatics/RESULTS.md` §5) reports **RNA tissue specificity: Low tissue
specificity**, **RNA tissue distribution: Detected in all**, with single-cell
enrichment in **melanocytes (103.5 nCPM)** and spermatogenic cell types rather than in
neurons; the single-nuclei brain data show **low cell-type specificity**. The UniProt
entry agrees (`DR   HPA; ENSG00000070718; Low tissue specificity.`;
`DR   Bgee; ENSG00000070718; Expressed in endothelial cell and 186 other cell types or tissues.`).
The tissue-level expression *cluster* is still "Brain & retina - Neuronal signaling", so
the gene is brain-weighted without being brain-restricted.

The pigment-cell enrichment is not an artefact of one atlas. Zebrafish `ap3m2` is
required for lysosome-related-organelle biogenesis in iridophores
[PMID:41950095 "Key regulators, including Rab32a, Ap3m2, and Hps5, are essential for crystal formation, with gene knockouts causing reduced crystal number, altered morphology, and distinct maturation defects."]
and `ap3m2` was one of the candidates in the transparent zebrafish *pinky* mutant
[PMID:23639161 "The molecular analysis results in several candidate genes, hps1, ap3m2 and rabggta, implicated in the Hermansky-Pudlak syndrome (HPS) genes associated with HPS in pk."].
Human cell work outside neurons also exists: AP3M2 knockdown reduces IL-6 secretion in
iPSC-derived astrocytes [PMID:30371777 "Knockdown of AP3M2, CNN2, GSTP1, NPC1, NPC2, PSAP and SORL1 reduced interleukin-6 levels in astrocytes."]
and reduces viability of colorectal-cancer lines [PMID:39488930 "The Knockdown of AP3M2 significantly reduced the viability of three CRC cell lines HCT-116, CACO2, and HT29."].
I did **not** convert any of this into annotation actions — the zebrafish gene's
orthology to human AP3M2 rather than AP3M1 was not established here, and the human
knockdown phenotypes are not mechanistically resolved. It is recorded as a knowledge
gap instead.

---

## 2. What AP-3B does

### 2.1 It buds synaptic vesicles from endosomes — and that is the mu3B-specific job

The decisive paper is Blumstein et al. 2001, which **affinage did not return** (see §6):

- [PMID:11588176 "In the presence of GTPgammaS both ubiquitous and neuronal forms of AP-3 can bind to purified synaptic vesicles. However, only the neuronal form of AP-3 can produce synaptic vesicles from endosomes in vitro."]
- [PMID:11588176 "We also identified that the expression of neuronal AP-3 is limited to varicosities of neuronal-like processes and is expressed in most axons of the brain."]

It builds on the original AP-3 coat reconstitution
[PMID:9590176 "Depletion of AP3 from brain cytosol inhibits small vesicle formation from PC12 endosomes in vitro."; PMID:9590176 "We conclude that AP3 coating is involved in at least one pathway of small vesicle formation from endosomes."]
and is confirmed in vivo by the mu3B knockout
[PMID:15492041 "Thus, these results indicate that AP-3B is involved in the biogenesis of synaptic vesicles in hippocampus in vivo."].

Nakatsu et al. also draw the distinction that the GO terms in GOA get wrong:

> [PMID:15492041 "There are two distinct pathways for synaptic vesicle formation: endocytosis or recycling from the plasma membrane and budding from the endosomal membrane"]

and place AP-3B on the second of the two
[PMID:15492041 "Although we and others have shown the implication of AP-3B in the biogenesis of synaptic vesicles from endosomes in vitro (Faundez et al., 1998; Blumstein et al., 2001), its physiological role has remained uncertain."].

GO has a term for exactly this: **GO:0016182 synaptic vesicle budding from endosome**,
"Budding of synaptic vesicles during the formation of constitutive recycling vesicles
from early endosomes" (QuickGO). Mouse `Ap3d1` already carries it with IMP and IDA from
PMID:11588176. Human AP3M2 carries neither it nor anything under it; instead it carries
two terms on the *endocytic* branch — GO:0016183 synaptic vesicle coating (whose
definition is "The formation of clathrin coated pits in the presynaptic membrane
endocytic zone…") and GO:0048488 synaptic vesicle endocytosis ("…the synaptic vesicle
membrane constituents are retrieved from the presynaptic membrane on the axon terminal
after neurotransmitter secretion by exocytosis"). Checked with QuickGO: GO:0016183
`is_a` GO:0048488 and both sit under GO:0006897 endocytosis, whereas GO:0016182 does
not. Both rows are therefore MODIFY → GO:0016182.

### 2.2 The in vivo phenotype is a selective GABAergic defect

The mu3B knockout is the only gene-specific in vivo evidence that exists:

- seizures — [PMID:15492041 "mu3B-/- mice suffered from spontaneous epileptic seizures."]
- selective transmitter defect — [PMID:15492041 "However, the K+-evoked release of GABA, but not of glutamate, was impaired in μ3B−/−ΔNeo mice at 8 wk old or over (Fig. 4, A and B)."]
- the cargo — [PMID:15492041 "The amount of VGAT protein was decreased significantly in synaptosomal lysates from the hippocampus of μ3B−/−ΔNeo mice (Fig. 4, C and D) despite the fact that the amounts of VGLUT1 and VGLUT2, and other synaptic vesicle proteins such as synaptophysin, synaptotagmin, VAMP2, rabphilin-3A, and Rab3A (Fig. 4 C) were unchanged."]
- ultrastructure at both synapse types — [PMID:15492041 "The density of synaptic vesicles in excitatory terminals was lower in μ3B−/−ΔNeo mice than in wild-type mice at the age of 4–16 wk (Fig. 3, A, B, and E)."]

This is why GO:0098982 GABA-ergic synapse is graded as core while GO:0098978
glutamatergic synapse is kept as non-core: both compartments show a vesicle-density
phenotype, but only the inhibitory one shows a functional transmitter defect.

Human genetics has not (yet) matched the mouse: a 190-patient screen found
[PMID:17293072 "Although neither missense nor nonsense mutations were detected, we identified 21 sequence variations, of which 16 variations were novel."].
The obligate partner *AP3B2*, by contrast, causes DEE48
[PMID:41948612 "Loss-of-function variants in AP3B2, a neuronal adaptor protein required for synaptic vesicle formation, cause a severe early-onset neurodevelopmental epilepsy known as Developmental and Epileptic Encephalopathy 48 (DEE48)."].
Mouse `Ap3m2` is also the positional candidate at an alcohol-preference/withdrawal QTL
[PMID:24923803 "Functional validation studies in Ap3m2 knockout mice confirmed these relationships."] —
recorded as context, not annotated.

### 2.3 Where AP-3 acts: endosomes, not the TGN

This was a genuine controversy and it was settled by immuno-EM:

- [PMID:15051738 "The adaptor protein (AP) 3 adaptor complex has been implicated in the transport of lysosomal membrane proteins, but its precise site of action has remained controversial. Here, we show by immuno-electron microscopy that AP-3 is associated with budding profiles evolving from a tubular endosomal compartment that also exhibits budding profiles positive for AP-1."]
- [PMID:15051738 "Based on these data, we propose that AP-3 defines a novel pathway by which lysosomal membrane proteins are transported from tubular sorting endosomes to lysosomes."]

GO's own definition of the complex agrees: GO:0030123 is "A heterotetrameric AP-type
membrane coat adaptor complex that consists of beta3, delta, mu3 and sigma3 subunits
and is found associated with endosomal membranes" (QuickGO). AP-3 is also seen on
early/recycling endosome tubules in pigment cells
[PMID:23247405 "Packaging of the tyrosinases into transport vesicles at early/recycling endosome-associated tubules is dependent on ubiquitous adaptor protein complex (AP)-1 and AP-3, and biogenesis of lysosome-related organelles complex (BLOC)-1 and BLOC-2."].

The earlier literature that put AP-3 "at the Golgi" was itself hedged
[PMID:9151686 "Our earlier study indicated that some of the complex is associated with the TGN (Simpson et al., 1996), and the more peripheral labeling may represent a post-TGN compartment."],
and UniProt still records `SUBCELLULAR LOCATION: Golgi apparatus. Cytoplasmic vesicle
membrane`. So Golgi is kept (non-core) while the IBA-derived `is_active_in
trans-Golgi network` is modified to early endosome — see §4.

### 2.4 The molecular function: YxxPhi cargo recognition by the mu subunit

The mu subunits of AP complexes are the tyrosine-signal-recognition arm
[PMID:9151686 "The presence of a μ subunit in the complex indicates that it plays a role in the sorting of proteins containing tyrosine-based signals (Ohno et al., 1995; Dell'Angelica et al., 1997)."].
**mu3B itself was directly assayed** — this is the one molecular-function experiment on
this protein anywhere in the literature I found:

> [PMID:9748267 "We have analyzed the selectivity of interaction between YXXO signals and the mu1, mu2, and mu3 (A or B) subunits of the AP-1, AP-2, and AP-3 complexes, respectively, by screening a combinatorial XXXYXXO library using the yeast two-hybrid system."]
> [PMID:9748267 "Other than for this common preference, each medium subunit favored specific sets of residues at the X and O positions; these preferences were consistent with the proposed roles of the different adaptor complexes in rapid endocytosis and lysosomal targeting."]

and the structural mechanism is now solved for the human AP-3 holocomplex
[PMID:39705307 "AP-3 is conformationally flexible upon initial recruitment to the membrane yet is rigidified upon engagement with tyrosine cargo."],
with the cargo being the LAMP1 tail
[PMID:39705307 "Cryo-EM structure of AP-3 bound to Arf1 and LAMP1 cargo peptide on a lipid nanodisc."].
Note that mu3 is not the only cargo arm: the sigma3/delta hemicomplex carries the
dileucine site [PMID:39705307 "Instead, packing of β3 into the σ3 dileucine cargo-binding pocket keeps the μ3-CTD distal from the Arf1-δ interface."],
and Nakatsu's candidate VGAT signal is a dileucine, not a YxxPhi
[PMID:15492041 "Notably, we have identified a potential di-leucine signal, one of the well-characterized sorting signals recognized by AP complexes (Bonifacino and Traub, 2003), in the cytoplasmic tail of VGAT (unpublished data)."].
So mu3B contributes one of two cargo-recognition sites in the complex, which is why
`contributes_to` is the right qualifier in `core_functions`.

**GO has no term for this.** Searching QuickGO for "sorting signal binding",
"tyrosine-based sorting", "dileucine" and "YXXphi" returns exactly one relevant
molecular-function term, **GO:0089710 endocytic targeting sequence binding**, whose
definition is explicitly committed to internalisation: "Binding to a endocytic signal
sequence, a specific peptide sequence, of 4-6 amino acids with an essential tyrosine
(Y), found on cytoplasmic tails of some cell surface membrane proteins, which directs
internalization by clathrin-coated pits." Its only ancestors are GO:0005515 /
GO:0005488 / GO:0003674, so there is no non-endocytic sibling to fall back on. That the
motif's recognition by a mu subunit is not an endocytic-only activity is shown directly
[PMID:11139587 "This chimera was targeted to the endosomal-lysosomal system without being internalized from the plasma membrane."].
Recorded under `proposed_new_terms`.

---

## 3. Bioinformatics (see `AP3M2-bioinformatics/RESULTS.md`)

Everything below is recomputed live by `AP3M2-bioinformatics/analyze.py`; nothing is
hardcoded, and wrong accessions raise rather than pass silently (the first run caught
my own use of P53676 — rat Ap3m1, not human).

**Paralogy.** AP3M2's closest human paralogue is AP3M1 at **84.2%** identity; identity
to the clathrin-adaptor medium subunits is AP1M1 29.7%, AP1M2 31.6%, AP2M1 29.1%, and
to AP4M1 24.5%. The AP-3 pair is a clean, well-separated subfamily. This is the
quantitative form of the objection in §4 to a family-root IBD seeded only by AP-1/AP-2
donors.

**Is the cargo site intact in mu3B?** Defined empirically from **PDB 9C5B**, the human
AP-3 holocomplex on a nanodisc with the LAMP1 cytoplasmic tail bound (SIFTS maps chain
M to Q9Y2T2/AP3M1 1-418 and chain Y to P11279/LAMP1 406-417; modelled peptide
`SHAGYQTI`, carrying the GYQTI YxxPhi motif). Nine mu3A residues have a heavy atom
within 4.0 A of the cargo: Y180, F181, V389, L392, F402, K403, G404, V405, K406.
**AP3M2 is identical at 8 of the 9**, the ninth being a conservative V405I. No
deletions. There is therefore no residue-level evidence that the neuronal paralogue has
lost cargo recognition — encoded as `residue_claims` on the molecular-function row.

**A second, independent AP-3 cargo complex.** The PANTHER family metadata names
**PDB 4IKN** as PTHR10529's representative structure: the *rat* mu3A C-terminal domain
bound to the TGN38 tail (`DYQRL`) — a different species and a different cargo from 9C5B.
Ten rat mu3A residues contact the peptide, and projected onto human AP3M1 **nine of them
are exactly the 9C5B set**; the tenth is D182, which falls just outside the 4.0 Å cutoff
in 9C5B. Human AP3M2 carries the same residue as rat mu3A at 9 of the 10. So the site is
not an artefact of one structure, one cargo or one species, and mu3B matches mu3A across
it. (D182 is one of only **two** positions at which every human mu paralogue matches mu2 in
the outgroup comparison below — the other is mu2 V401, which maps to V389 and is itself a
contact in both AP-3 structures. `analyze.py` computes that count rather than my asserting
it; every other mu2 contact position has at least one paralogue that diverges.)

**Outgroup and alignment check.** The classical AP-2 pocket from **PDB 1BXX** (rat mu2 +
TGN38 `DYQRLN`) gives 13 contact residues. Both AP-3 mu subunits have diverged sharply
from it — AP3M2 matches mu2 at 4/13 and AP3M1 at 5/13, versus AP1M1 10/13, AP1M2 9/13
and AP4M1 11/13 — most strikingly mu2 W421 → **G404** in both mu3 proteins. Yet all 13
positions still align with no deletion, and projecting them onto AP3M1 lands on **9 of
the 9** positions 9C5B observes contacting LAMP1. The two routes agree, so the
cross-family alignment is not drifting, and the reading is that AP-3 recognises
tyrosine cargo through the structurally equivalent site with a diverged residue
complement — which is precisely what Ohno et al. reported functionally
[PMID:9748267 "each medium subunit favored specific sets of residues at the X and O positions"].

**mu3 linker amphipathic helix.** Begley et al. report a membrane-inserting amphipathic
helix in the mu3 linker [PMID:39705307 "Both helices follow a heptad-repeat sequence, have a clear hydrophobic face, and have a high predicted hydrophobic moment, all of which are common features of AH domains."].
Scanning the 45 residues preceding each protein's own UniProt MHD boundary with an
Eisenberg hydrophobic-moment window, AP3M2 139-156 (`ILRTVVNTITGSTNVGDQ`) scores
<uH> = 0.487 against AP3M1 0.450, AP1M1 0.433, AP1M2 0.373, AP2M1 0.227 and AP4M1
0.161, with AP3M2 and AP3M1 the only two proteins whose best window also has positive
mean hydrophobicity. Consistent with mu3B retaining the mu3 membrane-insertion feature.
This is a prediction, not an observation, and is reported as such.

**Isoform 2.** `P53677-2` combines VAR_SEQ 268-273 (`NLVAIP -> KCCLGM`) with VAR_SEQ
274-418 (`Missing`), i.e. it truncates at residue 273 of 418 and so removes the
C-terminal half of the MHD (176-417) — the half that carries every one of the nine
cargo-contacting positions above. Worth noting because the four IntAct interactions in
the UniProt record (FGFR3, HRAS, MEOX2, SPRED1) are all on the **-2** isoform with
`NbExp=3`, which is replicate counts within one dataset, not three studies. No GO row
depends on them and none was added.

---

## 4. Propagation audit

### 4.1 The PANTHER family and its nodes

`just fetch-panther-paint PTHR10529` →
`interpro/panther/PTHR10529/PTHR10529-paint.tsv`, 10 nodes / 18 node-level
annotations. PTHR10529 is broad: `PTHR10529-entries.csv` lists AP-1 mu, AP-2 mu, AP-3
mu, AP-4 mu **and stonins** (STON1 Q9Y6Q2, STON2 Q8WXE9, Drosophila stoned-B) among its
60 reviewed members. The node structure that matters:

| node | IBD terms | seeds (resolved) |
|---|---|---|
| `PTN000055849` | GO:0005802 C, GO:0035615 F, GO:0006896 P | family root — see below |
| `PTN000055848` | GO:0030121 (AP-1 complex) | AP-1 mu clade |
| `PTN000242370` | GO:0030122 (AP-2 complex), GO:0005829; **IRD on GO:0005802** | AP-2 mu clade |
| `PTN000242612` | GO:0030124 (AP-4 complex), GO:0006605, GO:0090160 | AP-4 mu clade |
| `PTN002237676` | **GO:0030123 (AP-3 complex)** | APM3 (yeast), apm3 (Dicty) |
| `PTN002575694` | GO:0030100, GO:0048488; **IRD on GO:0006896** | stonin clade (Bilateria) |
| `PTN008307226` | GO:0008021 | — |

AP3M2 receives IBAs from exactly two of these — `PTN002237676` (the AP-3 clade) and
`PTN000055849` (the family root) — and receives no AP-1/AP-2/AP-4 complex term, so the
complex-membership propagation is clean. The leakage is entirely at the root node.

Donors resolved through `xref:<db>-<id>` UniProt searches (fetch size 5; the only
multi-hit was AT4G24550 → Q9SB50 Swiss-Prot plus two TrEMBL isoforms):

| WITH/FROM id | resolves to |
|---|---|
| `SGD:S000000492` | P38153 yeast **APM3** — AP-3 mu |
| `SGD:S000001011` | P38700 yeast **APM2** — "Adaptin medium chain homolog" |
| `SGD:S000006180` | Q00776 yeast **APM1** — AP-1 mu-1-I |
| `FB:FBgn0024833` | O62531 *Drosophila* **AP-1mu** |
| `FB:FBgn0263351` | O62530 *Drosophila* **AP-2mu** |
| `dictyBase:DDB_G0277901` | Q9GPF1 *Dictyostelium* **apm3** — AP-3 mu |
| `dictyBase:DDB_G0289247` | Q54HS9 *Dictyostelium* **apm1** — AP-1 mu |
| `AGI_LocusCode:AT1G60780` | O22715 *Arabidopsis* **AP1M2** |
| `AGI_LocusCode:AT4G24550` | Q9SB50 *Arabidopsis* **AP4M** |
| `UniProtKB:O00189` | human **AP4M1** |
| `UniProtKB:E2RED8` | dog **AP4M1** |
| `UniProtKB:Q9Y6Q5` | human **AP1M2** |

### 4.2 GO:0035615 clathrin-cargo adaptor activity — the clearest defect

The `PTN000055849` IBD for GO:0035615 is seeded by `FB:FBgn0024833` (fly AP-1mu),
`FB:FBgn0263351` (fly AP-2mu), `UniProtKB:Q9Y6Q5` (human AP1M2) and
`dictyBase:DDB_G0289247` (Dicty AP-1 mu). **All four donors are AP-1 or AP-2 medium
subunits** — the two clathrin adaptors — and there is no AP-3 or AP-4 donor at all.
The term's definition is doubly committed: "Bringing together a cargo protein with
clathrin, responsible for the formation of **endocytic vesicles**" (QuickGO). AP-3 is
neither: UniProt says `Part of the AP-3 complex, an adaptor-related complex which is not
clathrin-associated` and Peden showed its budding profiles arise from endosomes, not
the plasma membrane. (AP-3 does contact clathrin — [PMID:9545220 "In vitro binding assays showed that mammalian AP-3 did associate with clathrin by interaction of the appendage domain of its beta3 subunit with the amino-terminal domain of the clathrin heavy chain."] — but that is the beta3 subunit and it does not make AP-3 an endocytic coat.)
→ MODIFY to **GO:0140312 cargo adaptor activity**, the immediate parent (QuickGO
ancestors of GO:0035615 include GO:0140312, GO:0030674, GO:0060090), which keeps the
adaptor claim and drops the clathrin/endocytosis commitments.

This is not an AP3M2 quirk. Querying QuickGO for the same term on the other two human
non-clathrin medium subunits returns the identical row on both:

```
AP3M1  GO:0035615  IBA  GO_REF:0000033  FB:FBgn0024833|FB:FBgn0263351|PANTHER:PTN000055849|dictyBase:DDB_G0289247
AP4M1  GO:0035615  IBA  GO_REF:0000033  FB:FBgn0024833|FB:FBgn0263351|PANTHER:PTN000055849|dictyBase:DDB_G0289247
```

Same node, same four AP-1/AP-2 donors, same clathrin-committed molecular function on
three human genes whose complexes are not clathrin coats. Fixing it at the node would fix
all three. The residue analysis in
§3 is attached here so it is clear the modification is a scoping fix and *not* a
loss-of-function argument.

### 4.3 GO:0005802 trans-Golgi network and GO:0006896 Golgi to vacuole transport

Both also come from the root node. The TGN IBD is seeded only by AP-1 mu (AT1G60780,
plus yeast APM2) and AP-4 mu (AT4G24550, E2RED8, O00189) — no AP-3 donor — and the
PAINT curator has already placed an **IRD on GO:0005802 at the AP-2 clade**
(`PTN000242370`), showing the compartment is understood to be subfamily-specific within
this family. Mammalian AP-3's compartment is the tubular sorting endosome (§2.3).
→ MODIFY to **GO:0005769 early endosome**.

GO:0006896 does have a real AP-3 donor (yeast APM3), and in fungi AP-3 genuinely runs
the Golgi→vacuole ALP route. But that is the fungal route; the metazoan AP-3 route runs
endosome→lysosome, which is the finding of PMID:15051738. → MODIFY to **GO:0008333
endosome to lysosome transport** ("The directed movement of substances from endosomes
to lysosomes", QuickGO). Note this is the same node whose GO:0006896 assertion the
PAINT curators already blocked with an IRD one clade over (`PTN002575694`, stonins).

### 4.4 GO:0030123 AP-3 adaptor complex — sound

`PTN002237676` is seeded by yeast APM3 and Dicty apm3, both bona fide AP-3 mu subunits,
and AP3M2 sits squarely inside the AP-3 mu clade (84% identical to AP3M1). AP3M2 is not
among its own donors, which is expected — the gene has no experimental GO row of any
kind. ACCEPT, `NO_FAILURE_CORE`.

### 4.5 The Ensembl-Compara IEA block (GO_REF:0000107) and the two ISS rows

Seven rows transfer from mouse `Q8R2R9` (Ap3m2) and one from rat `P53678` (Ap3m2).
Resolved both via UniProt REST (`Q8R2R9` = *Mus musculus* Ap3m2, `P53678` = *Rattus
norvegicus* Ap3m2, both Swiss-Prot, both PTHR10529). Pulling the donors' own GO records
from QuickGO shows what each transfer actually rests on:

| human row | mouse/rat source annotation |
|---|---|
| GO:0048488, GO:0098978, GO:0098982 | Ap3m2 IMP **and** IDA, SynGO, **PMID:15492041** (the mu3B knockout) |
| GO:0008089, GO:0048490 (IEA **and** ISS) | Ap3m2 IMP, UniProt, **PMID:21998198** |
| GO:0035651 | Ap3m2 IDA, MGI, PMID:19010779 |
| GO:0008021 | rat Ap3m2 EXP/IDA, SynGO, PMID:33376223 |

Two of these do not survive inspection of the cited paper.

**PMID:21998198 does not perturb Ap3m2.** The cached full text (24,083 words) contains
zero occurrences of "Ap3m2", "mu3B", "μ3B" or "AP-3B"; "μ3" appears once, in the generic
sentence naming the complex's four subunits. Every mouse allele in the study is
BLOC-1 or the delta subunit: [PMID:21998198 "other BLOC-1–deficient mice muted (Mutedmu/mu) and pallid (Pldnpa/pa) and the AP-3–deficient allele mocha (Ap3d1mh/mh; Kantheti et al., 1998; Huang et al., 1999; Zhang et al., 2002; Li et al., 2003)."].
Because `mocha` removes the shared delta subunit it ablates **both** AP-3A and AP-3B, so
the result cannot be assigned to the mu3B-containing complex. The biology is real and
AP-3 is genuinely required for cell-body-to-neurite cargo delivery
[PMID:21998198 "Our findings indicate a novel vesicle transport mechanism requiring BLOC-1 and AP-3 complexes for cargo sorting from neuronal cell bodies to neurites and nerve terminals."],
so the four affected rows (GO:0008089 IEA + ISS, GO:0048490 IEA + ISS) are kept as
non-core rather than removed, with `SOURCE_WEAK_OR_INFERRED` recorded. I am **not**
asserting the mouse annotation is wrong — I did not see what the UniProt curator saw
beyond this text — only that the evidence behind the human transfer is complex-level.
GO:1904115 axon cytoplasm is a GOC logical inference *from* GO:0008089
(`WITH/FROM = GO:0008089`) and inherits the same status.

**PMID:33376223 names AP-3 as an SV visitor, not a resident.** The rat `is_active_in
GO:0008021` rests on an SV-fraction proteome whose authors write
[PMID:33376223 "This may explain the presence of endosomal-related proteins (e.g., Stx7, AP3) or proteins of the AZ (e.g., Piccolo, Bassoon) in the SV proteome."].
Their per-protein dataset (Dataset S1) is not in the cached text, so I cannot see
AP3M2's own rank or resident/visitor call. Kept as non-core with the caveat recorded;
Blumstein's independent in vitro result that neuronal AP-3 binds purified synaptic
vesicles is the reason it is kept at all.

**GO:0035651 AP-3 adaptor complex binding** is a role conflation at the term level:
AP3M2 is a *constitutive subunit* of AP-3, which GO expresses as `part_of GO:0030123`
(already present twice on this gene), not as an enzyme-style "binding" of its own
complex. The mouse IDA is abstract-only in our cache (`full_text_available: false`), so
I make no claim about what the mouse experiment showed;
`MARK_AS_OVER_ANNOTATED` applies to the human transfer only.

### 4.6 GO:0030131 clathrin adaptor complex (InterPro2GO) — a real mis-mapping

The InterPro API gives `IPR001392` "Clathrin adaptor, mu subunit" → GO:0006886,
GO:0016192 and **GO:0030131**. GO:0030131 is "A membrane coat adaptor complex that
links clathrin to a membrane". QuickGO's ancestor list for GO:0030123 is
`GO:0005575, GO:0005622, GO:0005737, GO:0016020, GO:0030117, GO:0030119, GO:0030123,
GO:0032991, GO:0048475, GO:0098796, GO:0110165` — **GO:0030131 is not in it**. So in
GO's own structure the AP-3 complex is not a clathrin adaptor complex, and this is not
a case of an IEA being harmlessly broader: it is a different branch. The mapping is
calibrated on mu1/mu2 and over-reaches to the mu3/mu4 members of the same InterPro
family. → MODIFY to GO:0030123. The other two InterPro2GO terms (GO:0006886,
GO:0016192) are correct for the whole family and are accepted.

### 4.7 ARBA00026971 (GO:0005737 cytoplasm) cannot be reproduced

`https://rest.uniprot.org/arba/ARBA00026971` returns a rule with **2,388 condition
sets** conferring a single annotation, GO:0005737. Filtering those sets for any of
AP3M2's seven InterPro signatures (IPR001392, IPR011012, IPR018240, IPR022775,
IPR028565, IPR036168, IPR050431, confirmed via the InterPro API for P53677) or for
PTHR10529 leaves exactly two:

- one pairing `IPR011012` with taxon `Saccharomyces` — AP3M2 is human, so this fails;
- one pairing `IPR022775` with `IPR016635` and `IPR027156` — IPR016635 is "Adaptor
  protein complex, sigma subunit" and IPR027156 is "AP-2 complex subunit sigma";
  AP3M2 is a mu subunit and has neither, so this fails too.

No condition set of the rule as the API serves it is satisfied by this protein. (The
record returns no meaningful version string, so an earlier revision may have had a set
that did fire; the finding is about the rule as it now stands.) The *claim* is
nonetheless true (AP-3 is a cytosolic coat that cycles on and off membranes), so the
row is kept as non-core rather than removed, with the provenance defect recorded in
`propagation_review`. This is the same pattern as the repo's earlier ARBA00027853
finding.

---

## 5. Action summary and rationale index

| # | term | ev | action |
|---|---|---|---|
| 1 | GO:0005737 cytoplasm | IEA ARBA | KEEP_AS_NON_CORE (§4.7) |
| 2 | GO:0005769 early endosome | NAS | ACCEPT (§2.3) |
| 3 | GO:0005794 Golgi apparatus | IEA SubCell | KEEP_AS_NON_CORE (§2.3) |
| 4 | GO:0005802 trans-Golgi network | IBA | MODIFY → GO:0005769 (§4.3) |
| 5 | GO:0006886 intracellular protein transport | IEA InterPro | KEEP_AS_NON_CORE (§4.6) |
| 6 | GO:0006896 Golgi to vacuole transport | IBA | MODIFY → GO:0008333 (§4.3) |
| 7 | GO:0008021 synaptic vesicle | IEA | KEEP_AS_NON_CORE (§4.5) |
| 8-9 | GO:0008089 anterograde axonal transport | IEA, ISS | KEEP_AS_NON_CORE (§4.5) |
| 10 | GO:0016183 synaptic vesicle coating | NAS | MODIFY → GO:0016182 (§2.1) |
| 11 | GO:0016192 vesicle-mediated transport | IEA InterPro | KEEP_AS_NON_CORE (§4.6) |
| 12 | GO:0030119 AP-type membrane coat adaptor complex | TAS | MODIFY → GO:0030123 |
| 13-14 | GO:0030123 AP-3 adaptor complex | IBA, NAS | ACCEPT (§4.4) |
| 15 | GO:0030131 clathrin adaptor complex | IEA InterPro | MODIFY → GO:0030123 (§4.6) |
| 16 | GO:0030659 cytoplasmic vesicle membrane | IEA SubCell | ACCEPT |
| 17 | GO:0035615 clathrin-cargo adaptor activity | IBA | MODIFY → GO:0140312 (§4.2) |
| 18 | GO:0035651 AP-3 adaptor complex binding | IEA | MARK_AS_OVER_ANNOTATED (§4.5) |
| 19 | GO:0035654 cc-vesicle cargo loading, AP-3-mediated | NAS | ACCEPT (§2.4, §9) |
| 20 | GO:0036465 synaptic vesicle recycling | NAS | ACCEPT (§2.1) |
| 21 | GO:0048488 synaptic vesicle endocytosis | IEA | MODIFY → GO:0016182 (§2.1) |
| 22-23 | GO:0048490 anterograde synaptic vesicle transport | IEA, ISS | KEEP_AS_NON_CORE (§4.5) |
| 24 | GO:0098978 glutamatergic synapse | IEA | KEEP_AS_NON_CORE (§2.2) |
| 25 | GO:0098982 GABA-ergic synapse | IEA | ACCEPT (§2.2) |
| 26 | GO:1904115 axon cytoplasm | IEA GOC | KEEP_AS_NON_CORE (§4.5) |
| NEW | GO:0061534 GABA secretion, neurotransmission | ISS | NEW (§2.2) |

The TAS row (#12) deserves a word. PMID:8076832 is the 1994 cloning paper; it predates
the identification of AP-3 by three years and its own claim is homology-level
[PMID:8076832 "These three proteins share approx. 80% amino acid (aa) identity to each other and have 27-30% aa identity to rat AP50 and mouse AP47, the medium-chain subunits of adaptor complexes associated with clathrin-coated vesicles."].
The parent term it carries is correct — GO:0030119's definition explicitly covers AP-3,
"Any of several heterotetrameric complexes that link clathrin (or another coat-forming
molecule, as hypothesized for AP-3 and AP-4) to a membrane surface" — but the specific
complex identity has been known since 1997 [PMID:9151686] and is what should be
asserted.

---

## 6. What affinage missed

The affinage record (`gates_passed`, `self_evaluation_pairwise: win`, `faith_pct:
100.0`, 6 citations) describes the right protein and gets the LRO/pigment-cell angle —
which turned out to be more useful than expected, given the HPA melanocyte enrichment.
But it returned **none of the papers this review actually rests on**. Missing:

- **PMID:11588176** Blumstein 2001 — the only paper that isolates the *neuronal* AP-3
  function, and the single most important reference for AP3M2;
- **PMID:15492041** Nakatsu 2004 — the mu3B knockout itself, already in GOA via the
  mouse ortholog, and the source of the GABAergic phenotype;
- **PMID:9748267** Ohno 1998 — the only direct molecular-function assay of mu3B;
- **PMID:9590176** Faundez 1998, **PMID:15051738** Peden 2004, **PMID:39705307**
  Begley 2024, **PMID:9151686**, **PMID:9118953**, **PMID:15537701**.

The pattern is the one this campaign keeps hitting: the decisive papers are titled for
the *complex* ("AP-3", "AP-3B", "adaptor medium chains") or for the *partner*
(AP3B2/DEE48), not for the gene symbol, and a symbol-anchored search does not reach
them. Affinage did return the two 2024-2026 papers that *are* titled "AP3M2" — the CRC
knockdown and the zebrafish iridophore work — which is consistent with its gates
measuring precision rather than recall. Everything above was recovered by hand from
Europe PMC (which 503'd intermittently and needed a retry loop), from QuickGO donor
records, and from the PAINT slice.

## 7. Open questions

- Is human AP3M2 functionally neuronal at all? The rodent restriction (PMID:8076832) is
  not reproduced by human expression atlases, which put its highest single-cell signal
  in melanocytes and spermatogenic cells. Either the paralogue's tissue distribution
  changed in the primate lineage, or the protein has an unrecognised role in
  lysosome-related-organelle biogenesis in pigment cells, as the zebrafish knockout
  suggests.
- Does mu3B-containing AP-3B select different cargo from mu3A? Ohno's library screen
  says the YxxPhi preferences of mu3A and mu3B differ, but no mu3B-specific cargo has
  been identified; VGAT, the best candidate, is proposed to use a dileucine signal,
  which is read by sigma3/delta rather than by mu3.
- Is the AP-3B complex ever assembled without beta3B? Nakatsu's immunoblot says beta3B
  is destabilised in mu3B-null brain, implying strict interdependence, but the reverse
  experiment (mu3B stability in AP3B2-null neurons) was not found here — and it matters
  for interpreting DEE48.
- Which complex does the alcohol-preference QTL act through? PMID:24923803 maps
  regulatory variation upstream of Ap3m2 rather than coding change, so the phenotype may
  be a dosage effect on AP-3B assembly.

---

## 8. Validation record

Counts below are printed by `AP3M2-bioinformatics/reconcile_goa.py`, not asserted by
hand. That script is the GOA-to-YAML reconciliation the campaign brief requires: it
checks that every line of `AP3M2-goa.tsv` maps to exactly one `existing_annotations`
entry with the same term, evidence code, reference and normalised WITH/FROM set, that
the only extra entry is the `NEW` row, and that every `propagation_review`'s
`source_entities` are exactly the row's `supporting_entities`, in order, each with a
comment.

```
GOA tsv rows            : 26
YAML reviewed rows      : 26
YAML NEW rows           : 1
rows with propagation_review: 21
rows with supporting_entities: 21
action counts           : {'KEEP_AS_NON_CORE': 11, 'ACCEPT': 7, 'MODIFY': 7,
                           'MARK_AS_OVER_ANNOTATED': 1, 'NEW': 1}
OK: GOA and review reconcile exactly
```

- `just validate human AP3M2` → `✓ Valid (with 1 warnings)`. The single warning is that
  no annotation cites the affinage file in `supported_by`. That is deliberate: the
  campaign brief forbids quoting an affinage sentence as `supporting_text` for a
  mechanistic claim, and there is no non-mechanistic row here where the file would be
  the right source. The record is still adjudicated in `references` with
  `relevance: LOW` / `correctness: LOW_QUALITY` and an explanation. The campaign's own
  model review, `genes/human/AGT`, carries the identical warning with `status: COMPLETE`.
- `checkquotes.py` → `checked 80 quotes: 0 failures, 0 skipped`.
- `uv run python -m ai_gene_review.validation.gene_residue_claims` →
  `352 pass, 0 fail, 0 unresolved` over 20 gene reviews, AP3M2's five claims among them.
- Duplicate-key scan of the YAML → none. `cache/go/terms.csv` → no deletions relative to
  the merge base, no duplicate ids.

---

## 9. Changes made across the three bot review rounds

**The third clathrin-committed term.** The first draft modified `GO:0035615` and
`GO:0030131` because each commits AP-3 to clathrin, and then accepted `GO:0035654`
*"**clathrin-coated vesicle** cargo loading, AP-3-mediated"* without comment. That reads
as selective, and the objection does apply to the wording: the definition's clause is
"transported by a clathrin-coated vesicle". The distinction that makes ACCEPT right
anyway is about what each term picks out and what alternatives exist.

| term | what it is | non-clathrin alternative in GO |
|---|---|---|
| GO:0035615 | a term *about* clathrin adaptors, into which AP-3 was swept by a family-root IBD | yes — GO:0140312, its immediate parent |
| GO:0030131 | a complex class AP-3 is not in (GO:0030123 is not a descendant) | yes — GO:0030123 itself |
| GO:0035654 | a term created *for* AP-3; its definition names the AP-3 heterotetramer | **no** — generalising to GO:0035459 discards the AP-3 identity to drop an adjective |

So the remedy for GO:0035654 belongs to the ontology, not to this gene: drop
"clathrin-coated" from the name and definition and re-parent it directly under GO:0035459
vesicle cargo loading, leaving its current parent GO:0035652 for the AP-1/AP-2 adaptors.
Both of those ids and labels were checked against QuickGO rather than written from memory
— `GO:0035652` is "clathrin-coated vesicle cargo loading", not obsolete, with ancestors
`GO:0006810, GO:0008150, GO:0035459, GO:0035652, GO:0051179, GO:0051234`, and its
children are exactly `GO:0035653` and `GO:0035654`, both `is_a`. That last lookup is the
one that establishes the relation the proposal turns on: GO:0035654 currently sits
*beneath* GO:0035652, so the proposal moves it up one level to sit alongside it. (Both `proposed_new_terms` entries are really ontology *change* requests, and
`ProposedOntologyTerm` has no field that says so; each justification now states it
explicitly, and the schema gap is worth an issue of its own.) That is now the second
entry in `proposed_new_terms`, and the ONTOLOGY knowledge gap names both defects as two
faces of the same legacy framing. The structural work states the point plainly
[PMID:39705307 "our findings that AP-3 contains multiple AH domains and can co-opt Arf1 for homodimerization suggests that a clathrin-independent tubular coat for AP-3 is likely."].

**Cross-review inconsistency with AP3B2 — not resolved here.**
`genes/human/AP3B2/AP3B2-ai-review.yaml` ACCEPTs both `GO:0016183` (same ComplexPortal
NAS, same PMID:15537701) and `GO:0048488` (same Ensembl route), and puts GO:0016183 in
its core functions. This review modifies both to `GO:0016182` for the obligate partner of
the same complex, so the repository now carries two opposite calls on the same assertion.

Worth recording that AP3B2's own summary for GO:0016183 reads *"mediating the formation
of synaptic vesicle precursors from endosomal membranes"* — which is the definition of
**GO:0016182**, not of GO:0016183 ("the formation of clathrin coated pits in the
presynaptic membrane endocytic zone"). The two reviews therefore agree on the biology and
differ only on which term expresses it; the AP3B2 row's prose argues for the term this
review proposes. I did not edit AP3B2: it is neither this gene's folder nor a donor in
any of its rows, and the campaign brief limits edits to those. Filed instead as
[issue #3027](https://github.com/ai4curation/ai-gene-review/issues/3027).

**Two actions retuned.** `GO:0006886` and `GO:0016192` were ACCEPT while their own
reasons called them broad, harmless IEA parents; since `ACCEPT` means "retain as
representing the core function", both moved to `KEEP_AS_NON_CORE` with
`root_cause: NO_FAILURE_NON_CORE`. Counts are now 11 / 7 / 7 / 1 / 1.

**One suggestion declined.** The bot suggested adding `qualifier: involved_in` to the NEW
row for consistency with the seeded rows. Declined: the annotation-reviewer skill is
explicit that the gene-product-to-term relationship type "plays no role in review
reasoning, and any such value you encounter in a YAML row is likewise inert; never add,
edit, or argue from it." The seeded rows carry qualifiers because the GOA seeder copied
them, which is not a reason to author one. The NEW row's `reason` was instead reworded to
stop leaning on the word `involved_in`, and now argues the point directly.

**Round 3: a denominator corrected.** The `WHOLLY_DARK` gap first said "21 of the 26 rows
carry a WITH/FROM". Counted from the tsv, it is **20** — the six without are the five
ComplexPortal NAS rows and the ProtInc TAS row — and the 21st `propagation_review` in the
file belongs to the proposed NEW row. So the finding is **13 of 20**, not 13 of 21, which
makes it slightly stronger. Also added to `RESULTS.md` §1: the pairwise identity matrix is
computed per ordered pair, so where several alignments score equally the two directions
can pick different ones and the matrix is very slightly asymmetric (largest
cell-vs-transpose difference 0.6 percentage points, none of it in the AP3M2 row the review
cites). The history record's `details` was rewritten to the final numbers; `docs/history.md`
freezes only `target.slug` and `target.path`, so `details` is editable in place.
