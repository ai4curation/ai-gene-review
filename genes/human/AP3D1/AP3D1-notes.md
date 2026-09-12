# AP3D1 (human, O14617) — curation notes

Working notes for the GO annotation review of human AP3D1, the delta subunit
("delta-adaptin") of the heterotetrameric AP-3 adaptor complex. 1153 aa,
UniProt O14617 (`AP3D1_HUMAN`, entry version 224, sequence version 1), PANTHER
`PTHR22781:SF12`, InterPro family `IPR017105`.

Identity check: `AP3D1-uniprot.txt` line 1 reads `ID   AP3D1_HUMAN             Reviewed;        1153 AA.`
and the accession line begins `AC   O14617;`, so the fetch did not land on a
merged or redirected entry.

---

## 1. What the protein is

AP-3 is one of five heterotetrameric adaptor protein (AP) complexes. UniProt
states the subunit composition directly:

> [file:human/AP3D1/AP3D1-uniprot.txt "Adaptor protein complex 3 (AP-3) is a heterotetramer composed of two"]
> [file:human/AP3D1/AP3D1-uniprot.txt "large adaptins (delta-type subunit AP3D1 and beta-type subunit AP3B1 or"]
> [file:human/AP3D1/AP3D1-uniprot.txt "AP3B2), a medium adaptin (mu-type subunit AP3M1 or AP3M2) and a small"]

Two points follow that matter for every row in this review.

**Delta is the only large subunit that is not duplicated.** The beta slot is
filled by AP3B1 (ubiquitous, "AP-3A") or AP3B2 (neuronal, "AP-3B"), the mu slot
by AP3M1/AP3M2, the sigma slot by AP3S1/AP3S2 — but there is a single delta.
Falcón-Pérez and Dell'Angelica put it plainly
[PMID:17349999 "Two forms of AP-3 have been characterized: a ubiquitous form, containing the δ, β3A, μ3A and σ3(A/B) subunits, and a brain-specific form, containing β3B and μ3B in addition to the common δ and σ3(A/B) subunits"],
and the HPS10 paper draws the clinical consequence
[PMID:26744459 "AP3D1 codes for the AP3δ subunit of the complex, which is essential for both forms. In contrast, the AP3β3A subunit, affected in HPS2 patients, is substituted by AP3β3B in the neuron-specific heterotetramer."].
This is the reason AP3D1 loss is neurologically severe while AP3B1 loss (HPS2)
is not, and it is the reason the **synaptic-vesicle GO terms legitimately belong
on AP3D1 even though they are properties of the neuronal AP-3B complex** — delta
is in both complexes. Every SV row below is graded on that basis, not waved
through.

**Delta is required for complex stability.** Retroviral reconstitution of
patient cells restores the complex
[PMID:26744459 "AP3 complex formation and the degranulation defect in patient T cells were restored by retroviral reconstitution."],
and in mouse *mocha* fibroblasts
[PMID:22521722 "The absence of δ-adaptin causes destabilization of the AP3 complex in mouse mocha fibroblasts and mislocalization of VAMP7."].
So an AP3D1-null phenotype is an AP-3-null phenotype; nothing in the literature
separates "delta lost" from "AP-3 lost", which is a real limit on how much of
the AP-3 phenotype can be attributed to delta *as a subunit* rather than to the
complex.

Domain architecture (UniProt FT): eleven HEAT repeats spanning residues 34–585
(the N-terminal trunk / adaptin fold, Pfam `PF01602 Adaptin_N`), two long
disordered regions 629–696 and 726–920 with three coiled-coil segments, then the
C-terminal ear/appendage. `PF06375 AP3D1` and `IPR010474`
("AP-3 complex subunit delta domain, metazoa") are delta-specific signatures;
`PF26171 Mu_AP3` / `IPR058898` is the recently added Mu C-terminal domain.
Seven phosphoserines cluster in the first disordered region (S632, S634, S636,
S658, S688) and more in the second (S758, S759, ...). No catalytic residues,
no active site: this is a scaffold/adaptor, and no pseudo-enzyme argument
applies.

Disease: HPS10, OMIM 617050
[file:human/AP3D1/AP3D1-uniprot.txt "recessive disorder characterized by oculocutaneous albinism, bleeding"].

---

## 2. Three residue-level interfaces mapped on human delta

This is the part of AP3D1 biology that is genuinely delta-specific rather than
complex-level, and all three have been mapped **on the human protein**, so no
cross-species inference is needed to state them — only to test conservation.

### 2a. ARF1 — delta is the primary site, not beta-3

The 1998 in-vitro work established that ARF1 controls AP-3 membrane recruitment
[PMID:9679139 "we demonstrate that membrane association of the recently described AP-3 adaptor is regulated by ARF1"],
but it did not say which subunit. Two recent structural papers answer that, and
the answer is delta.

Begley, Aragon and Baker reconstituted human AP-3 and compared hemicomplexes
[PMID:39705307 "it is apparent that the δ-σ3 complex binds nearly as well as the full complex, with binding of the β3-μ3 hemicomplex barely above background levels in the Arf1GTP state"],
concluding
[PMID:39705307 "This suggests that the primary Arf1 binding site on AP-3 is on δ"]
— explicitly contrasted with AP-1, where the equivalent primary site is on beta-1.
Membrane engagement starts there
[PMID:39705307 "this state represents the initial engagement of AP-3 with the membrane via the δ-Arf1 interface"],
and the interface is mutable
[PMID:39705307 "Mutation of conserved interface residues in δ reduced binding to Arf1 in a pull-down assay"].
Their PDB depositions 9C58/9C59/9C5B/9C5C map to O14617 residues 1–617 (UniProt
`DR   PDB;` lines), confirming human numbering.

Kaufman et al. then resolved the coat itself by cryo-ET and named the residues.
Two ARF1 sites on delta:
[PMID:42139345 "The positively charged residues in β3 (K125/R132/R167/K194) and δ (H157/K159/R187/R163) occupy similar positions on either subunit."],
and a cellular test
[PMID:42139345 "Mutations in AP3D1 that abolish interaction with ARF1 sites relocalize δ-WT-SG to the cytosol."],
[PMID:42139345 "These data indicate that δ requires both ARF1 interfaces for correct membrane recruitment"].
Site 1 is F77/M110/L111 and site 2 is H157/K159/R163/R187 (from the mutant
constructs `δF77S, δM110S, δL111S` and `δH157D, δK159D, δR187D, δR163D`).

All seven positions carry exactly those residues in O14617 (checked against the
sequence in `AP3D1-uniprot.txt`; see §6).

### 2b. VAMP7 — a delta-hinge cargo receptor

Kent et al. solved the complex of the delta hinge with the VAMP7 longin domain
(PDB 4AFI; UniProt maps chain A/B to **O14617 residues 680–729**)
[PMID:22521722 "We show that the linker of the δ-adaptin subunit of AP3 binds the VAMP7 longin domain and determines the structure of their complex."]
[PMID:22521722 "Mutation to serine of residues Ile702 and Val704 (mut1) and of Leu709 and Leu713 (mut2) in the δ-adaptin, which play key roles in the VAMP7:δ-adaptin interface"].
The interaction requires VAMP7 to be in a cis-SNARE complex
[PMID:22521722 "The binding of VAMP7 to δ-adaptin requires the VAMP7 SNARE motif to be engaged in SNARE complex formation and hence AP3 must transport VAMP7 when VAMP7 is part of a cis-SNARE complex."].

Bowman et al. showed the interface is required *in vivo* in melanocytes
[PMID:33886957 "Sorting requires either recognition of VAMP7 by the AP-3δ subunit of AP-3 or of STX13 by the pallidin subunit of BLOC-1, but not both."].

I702/V704/L709/L713 are all present in O14617 at those positions (§6).

**Consequence for the review:** AP3D1 currently has *no* informative molecular
function in GOA — only `GO:0005515 protein binding` (IPI, CLN3) and, oddly,
`GO:0035651 AP-3 adaptor complex binding`. Two real, structurally defined,
subunit-level MFs are missing: `GO:0031267 small GTPase binding` (ARF1) and
`GO:0000149 SNARE binding` (VAMP7). Both are added as `NEW` rows. There is
precedent in the family: AP1G1 and AP3M1 both carry `GO:0031267` by IPI.

### 2c. An amphipathic helix — recorded but NOT asserted

Begley et al. report two amphipathic helices, one on delta and one on mu3, and
propose AP-3 contributes to membrane deformation. Kaufman et al. hedge:
[PMID:42139345 "Our AP3:ARF1 coat structure also suggests that there is an additional array of amphipathic helices is contributed by μ3 and possibly by δ."]
"Possibly" is not evidence. `GO:0180020 membrane bending activity` is therefore
**not** proposed; it goes in `knowledge_gaps` and `suggested_experiments`.

---

## 3. The clathrin question

Three GOA rows depend on AP-3 being a clathrin adaptor: `GO:0035654
clathrin-coated vesicle cargo loading, AP-3-mediated` (NAS, PMID:9545220) and
`GO:0016183 synaptic vesicle coating` (NAS, PMID:15537701). Both fail, for
different reasons.

**The clathrin contact was never delta's.** Dell'Angelica et al. localised it
precisely
[PMID:9545220 "In vitro binding assays showed that mammalian AP-3 did associate with clathrin by interaction of the appendage domain of its beta3 subunit with the amino-terminal domain of the clathrin heavy chain."].
That is AP3B1/AP3B2, a different protein in a different PANTHER family
(PTHR11134). Nothing in that paper puts delta on clathrin.

**And the clathrin contact is not functionally required.** The complex was
introduced as *non*-clathrin-associated
[PMID:9151686 "two proteins related to two of the adaptor subunits of clathrincoated vesicles, p47 (mu3) and beta-NAP (beta3B), are part of an adaptor-like complex not associated with clathrin"];
acute chemical-genetic clathrin inactivation spares AP-3 budding
[PMID:23761069 "These findings indicate that AP-3-clathrin association is dispensable for endosomal AP-3 vesicle budding and suggest that endosomal AP-3-clathrin interactions differ from those by which AP-1 and AP-2 adaptors productively engage clathrin in vesicle biogenesis."];
and the 2026 coat structure closes it
[PMID:42139345 "By demonstrating that AP3:ARF1 can generate carriers without using a clathrin lattice, we explain the clathrin independence of AP3-mediated trafficking."].
The GO term `GO:0030123 AP-3 adaptor complex` definition itself already hedges
("AP-3 does not appear to associate with clathrin in all organisms").

So `GO:0035654` is MODIFY → `GO:0035459 vesicle cargo loading` (its own parent;
the cargo-loading claim survives, the clathrin-coat framing does not).

`GO:0016183 synaptic vesicle coating` is a separate error. Its definition is
*"The formation of clathrin coated pits in the presynaptic membrane endocytic
zone"* — clathrin-mediated endocytosis at the presynaptic plasma membrane. AP-3
does not act there; the source paper (Seong et al.) is about β3A/β3B AP-3
complexes controlling synaptic-vesicle protein content, i.e. endosomal budding.
MODIFY → `GO:0016182 synaptic vesicle budding from endosome`, which is what the
source actually supports.

Caveat kept honest: AP-3 *does* colocalise partially with clathrin
[PMID:15051738 "AP-3 colocalizes with clathrin, but to a lesser extent than does AP-1."]
and in melanocytes AP-3 sits on clathrin-coated buds
[PMID:16162817 "AP-3 and AP-1 localize in melanocytes primarily to clathrin-coated buds on tubular early endosomes near melanosomes."].
The claim being rejected is the *functional* one (AP-3 loads cargo into a
clathrin coat), not colocalisation.

---

## 4. The PANTHER family and the ten IBAs

`DR   PANTHER; PTHR22781; DELTA ADAPTIN-RELATED` and `PTHR22781:SF12; AP-3
COMPLEX SUBUNIT DELTA-1`. The family slice was fetched with
`just fetch-panther-paint PTHR22781` →
`interpro/panther/PTHR22781/PTHR22781-paint.tsv`.

### 4a. The family cannot leak from the other adaptins

All nine reviewed members in `PTHR22781-entries.csv` are AP-3 **delta**
subunits, in `PTHR22781:SF12`, spanning human, mouse, bovine, *Drosophila*
(garnet), *Dictyostelium*, *S. cerevisiae* (APL5), *Eremothecium*, *S. pombe*
(apl5) and *Arabidopsis*. I checked the paralogs directly against the UniProt
REST records: AP3B1, AP1B1 and AP4B1 are all `PTHR11134` (ADAPTOR COMPLEX
SUBUNIT BETA FAMILY MEMBER); AP1G1, AP2A1 and AP4E1 are all `PTHR22780`
(ADAPTIN, ALPHA/GAMMA/EPSILON). **None of the AP-1/AP-2/AP-4 large subunits and
none of the beta subunits is in PTHR22781**, so the leakage route the review
brief asked about does not exist for these ten IBAs. This is the single most
important structural fact about this IBA set and it makes all ten cleaner than
the usual case.

### 4b. Two IBD nodes, both correctly placed

```
PTHR22781  PTN000513025  GO:0010008  C  IBD  MGI:MGI:107734|UniProtKB:O14617      taxon:2759   (Eukaryota)
PTHR22781  PTN000513025  GO:0030123  C  IBD  SGD:S000006116|dictyBase:DDB_G0279537 taxon:2759
PTHR22781  PTN000513025  GO:0006623  P  IBD  SGD:S000006116                        taxon:2759
PTHR22781  PTN000513025  GO:0006896  P  IBD  SGD:S000006116                        taxon:2759
PTHR22781  PTN000513028  GO:0043195  C  IBD  MGI:MGI:107734                        taxon:33213  (Bilateria)
PTHR22781  PTN000513028  GO:0098830  C  IBD  MGI:MGI:107734                        taxon:33213
PTHR22781  PTN000513028  GO:0016182  P  IBD  MGI:MGI:107734|RGD:1308659            taxon:33213
PTHR22781  PTN000513028  GO:0048490  P  IBD  MGI:MGI:107734                        taxon:33213
PTHR22781  PTN000513028  GO:0048499  P  IBD  MGI:MGI:107734                        taxon:33213
PTHR22781  PTN000513028  GO:0098943  P  IBD  MGI:MGI:107734                        taxon:33213
```

Exactly ten IBD rows, exactly the ten IBAs in GOA. No IRD or IKR anywhere in the
slice, so PAINT records no loss event in this family.

`PTN000513025` is the **Eukaryota** (taxon:2759) node: the pan-eukaryotic
delta-adaptin. `PTN000513028` is the **Bilateria** (taxon:33213) node, and every
term on it is neuronal. Human AP3D1 descends from both, so it is inside both
inheriting clades — there is no question of the target sitting outside.

The division of labour between the two nodes is exactly right, and it is worth
saying why: the neuronal terms are *not* placed at Eukaryota (yeast has no
synaptic vesicles) and the complex/compartment terms are *not* restricted to
Bilateria. A PAINT curator who had simply propagated everything from the mouse
experiments would have produced ten Bilateria-level rows; instead the four terms
with yeast/Dictyostelium grounding sit at the deeper node.

### 4c. Donor resolution (via UniProt `xref:` lookups, `size=5`)

| WITH/FROM id | UniProt | status | protein |
|---|---|---|---|
| `MGI:MGI:107734` | O54774 | Swiss-Prot | mouse Ap3d1 |
| `RGD:1308659` | B5DFK6 | TrEMBL (5 hits, all rat Ap3d1) | rat Ap3d1 |
| `SGD:S000006116` | Q08951 | Swiss-Prot (1 hit) | yeast APL5 |
| `dictyBase:DDB_G0279537` | Q54WN0 | Swiss-Prot (1 hit) | *Dictyostelium* ap3d1 |
| `UniProtKB:O14617` | O14617 | Swiss-Prot | **human AP3D1 — the target itself** |

Every donor is an AP-3 delta ortholog. No paralog, no homonym.

O14617 appearing in its own `GO:0010008` WITH/FROM is **correct and expected**,
not circular: human AP3D1 carries an IDA for endosome membrane
(PMID:16162817), and that IDA is one of the descendant evidences the PAINT
curator used to place the IBD. It is a marker that experimental grounding exists
on the target itself.

### 4d. What each donor actually has (QuickGO, per donor × term)

Queried `…/annotation/search?geneProductId=UniProtKB:<acc>&goId=<GO>` for all
five donors × ten terms. Every IBD seed resolves to a real experimental
annotation on the donor:

- `GO:0030123` — yeast APL5 IMP+IPI PMID:9250663 (the screen that defined the
  four-subunit yeast AP-3); *Dictyostelium* IDA PMID:18634783.
- `GO:0006623` — yeast APL5 IMP PMID:17895371 (scNcr1p vacuolar targeting
  perturbed in AP-3-deficient yeast).
- `GO:0006896` — yeast APL5 IMP PMID:9335339 (the ALP pathway; "AP-3 complex is
  essential for cargo-selective transport to the yeast vacuole").
- `GO:0010008` — mouse Ap3d1 IDA PMID:16162817; human AP3D1 IDA PMID:16162817.
- `GO:0043195` — mouse Ap3d1 IDA PMID:20089890.
- `GO:0098830` — mouse Ap3d1 IDA PMID:19144828.
- `GO:0016182` — mouse Ap3d1 IDA+IMP PMID:11588176; rat Ap3d1 IDA+IMP PMID:22539861.
- `GO:0048490` — mouse Ap3d1 IMP PMID:21998198.
- `GO:0048499` — mouse Ap3d1 IMP PMID:15860731.
- `GO:0098943` — mouse Ap3d1 IDA+IEP+IMP PMID:24217640.

No `SOURCE_STALE_OR_MISSING`; nothing traced to a propagated-only annotation.

### 4e. The one node-level scoping problem: `GO:0006896`

`GO:0006896 Golgi to vacuole transport` is placed at the Eukaryota node on the
strength of the yeast ALP pathway alone (Cowles et al.): in *S. cerevisiae*
AP-3 buds ALP and Vam3p **from the late Golgi** to the vacuole
[PMID:9335339 "A screen for factors specifically involved in transport of alkaline phosphatase (ALP) from the Golgi to the vacuole/lysosome has identified Ap16p and Ap15p of the yeast AP-3 complex."].

In mammals the demonstrated AP-3 exit site is not the Golgi. Peden et al.
[PMID:15051738 "we show by immuno-electron microscopy that AP-3 is associated with budding profiles evolving from a tubular endosomal compartment that also exhibits budding profiles positive for AP-1"]
[PMID:15051738 "Based on these data, we propose that AP-3 defines a novel pathway by which lysosomal membrane proteins are transported from tubular sorting endosomes to lysosomes."];
melanocytes agree (PMID:16162817, above); and the 2026 coat paper frames it the
same way
[PMID:42139345 "The AP3 complex mediates cargo sorting and carrier assembly for the trafficking of transmembrane proteins from endosomes to lysosomes."].

So the *process* is conserved (deliver cargo to the lytic compartment) but the
donor compartment is not. This is a `TERM_SCOPING_PROBLEM` /
`COMPARTMENT_OR_COMPLEX_MISMATCH`, handled as MODIFY → `GO:0008333 endosome to
lysosome transport`, keeping `GO:0006623 protein targeting to vacuole` (which
is compartment-agnostic and whose lysosomal child `GO:0006622` is proposed as a
human-specific NEW row; `GO:0006622 is_a GO:0006623` confirmed via the QuickGO
ancestors endpoint).

Honesty note: Peden's own framing is that the site "has remained
controversial", and Kantheti's 1998 abstract still describes AP-3 as
"associated with coated vesicles budding from the trans-Golgi network". The
MODIFY is therefore a refinement toward the better-supported mammalian route,
not a claim that no TGN pool exists — and that residual uncertainty is recorded
in `knowledge_gaps`.

---

## 5. The ARBA rows: one bad term, two irreproducible

Eight GOA rows come from `GO_REF:0000117` / `GO_REF:0000120` with an `ARBA…`
condition. I fetched each rule from `https://rest.uniprot.org/arba/<id>` and
evaluated its condition sets against AP3D1's complete signature complement
(the six InterPro entries, three Pfam, one SMART, one SUPFAM, the PANTHER
family, and the three FunFams `1.25.10.10:FF:000785`, `1.25.10.10:FF:000808`,
`3.30.450.50:FF:000001` from the UniProt `DR` lines; cross-checked against the
InterPro API `entry/all/protein/UniProt/O14617`, which returns 14 matches and
agrees with the record).

| Rule | GO term | condition sets | satisfied by AP3D1 |
|---|---|---|---|
| ARBA00028708 | GO:0005794 Golgi apparatus | 146 | 1 — `FunFam 3.30.450.50:FF:000001 + taxon Eukaryota` |
| ARBA00027179 | GO:0006886 intracellular protein transport | 53 | 1 — `FunFam 3.30.450.50:FF:000001` |
| ARBA00033548 | GO:0007041 lysosomal transport | 9 | 1 — `FunFam 3.30.450.50:FF:000001 + taxon Craniata` |
| ARBA00028306 | GO:0010008 endosome membrane | 27 | 1 — `FunFam 3.30.450.50:FF:000001 + taxon Eukaryota` |
| **ARBA00092758** | **GO:0010496 intercellular transport** | 99 | 1 — `FunFam 3.30.450.50:FF:000001` (no taxon guard) |
| ARBA00028845 | GO:0016050 vesicle organization | 33 | 1 — `FunFam 3.30.450.50:FF:000001 + taxon Euarchontoglires` |
| ARBA00028739 | GO:0032502 developmental process | 893 | **0** |
| ARBA00029167 | GO:0072657 protein localization to membrane | 26 | **0** |

Two observations.

**`GO:0010496 intercellular transport` is simply wrong.** Its definition is
*"The movement of substances between cells."* AP3D1 is a cytosolic coat subunit
acting on intracellular membranes; nothing in the literature has it moving
material between cells. The rule fires on the single AP3D1-specific FunFam
`3.30.450.50:FF:000001` — whose CATH FunFam name in the UniProt record is
literally "AP-3 complex subunit delta-1, putative" — with no taxon guard, so
the same evidence that correctly yields "lysosomal transport" and "endosome
membrane" here also yields "between cells". This is the only REMOVE among the
electronic rows that rests on a positive biological argument rather than on
mere generality.

**Two rules cannot be reproduced from their own published condition sets.**
ARBA00028739 (893 sets) and ARBA00029167 (26 sets) both annotate AP3D1 but no
set is satisfiable by it: neither carries `PTHR22781`, and ARBA00029167's sets
are all FunFam-based with none of AP3D1's three. I am *not* claiming the
annotations are therefore wrong — only that the published rule cannot be shown
to produce them, which is the same provenance gap already recorded in this
repository for ARBA00027853. `GO:0072657` is independently supported (mouse
IMP PMID:16760431), so it stands; `GO:0032502 developmental process` is a
root-adjacent term carrying no information and is marked over-annotated.

The remaining six ARBA terms are all true of AP3D1 and are kept, most of them
as non-core parents.

---

## 6. Bioinformatics — are the delta interfaces family features?

`AP3D1-bioinformatics/delta_interfaces.py` (uv project; fetches live from
UniProt into a disposable `cache/`, aligns with MAFFT `--auto`). Panel = the
nine reviewed `PTHR22781` members from the committed InterPro slice, plus four
out-of-family human controls: AP3B1 (PTHR11134), AP1G1, AP2A1, AP4E1
(PTHR22780). The script asserts `len(O14617) == 1153` and asserts each claimed
residue before aligning, so a silently-changed sequence fails rather than
producing a wrong table.

Identity to human AP3D1 at the site positions (`delta_interfaces.tsv`):

| site | positions | PTHR22781 members | out-of-family controls |
|---|---|---|---|
| ARF1 site 1 | F77, M110, L111 | mouse 3/3, bovine 3/3, fly 3/3, *S. cerevisiae* 3/3, *Eremothecium* 3/3, *S. pombe* 3/3, *Dictyostelium* 2/3, *Arabidopsis* 2/3 | AP3B1 1/3, AP1G1 1/3, AP2A1 1/3, AP4E1 1/3 |
| ARF1 site 2 | H157, K159, R163, R187 | mouse 4/4, bovine 4/4, fly 2/4, *Eremothecium* 2/4, *S. pombe* 2/4, *Arabidopsis* 2/4, yeast 1/4, *Dictyostelium* 1/4 | AP3B1 1/4, AP1G1 1/4, AP2A1 1/4, AP4E1 3/4 |
| VAMP7 hinge | I702, V704, L709, L713 | mouse 4/4, bovine 4/4, fly 3/4, *Dictyostelium* 3/4, yeast 1/4, *S. pombe* 1/4, *Arabidopsis* 1/4, *Eremothecium* 0/4 | AP3B1 0/4, AP1G1 1/4, AP2A1 0/4, AP4E1 0/4 |

Readings:

- **ARF1 site 1 is an ancient delta feature.** Fully conserved from budding
  yeast to human inside the family, essentially absent from the other adaptin
  large subunits. That is consistent with Begley et al.'s observation that the
  delta site is the analogue of the AP-1 gamma / COPI site while the *primary*
  site differs between complexes.
- **ARF1 site 2 is the basic patch and it is mammal-tight, deeper-taxon-loose.**
  4/4 in mouse and bovine, 1–2/4 outside vertebrates. This matches the paper's
  own wording — "highly conserved among multicellular eukaryotes" is a weaker
  claim than "universal", and the data say so. AP4E1 scoring 3/4 is expected:
  the equivalent basic patch is a general ARF1-contact feature of adaptin large
  subunits, not delta-private.
- **The VAMP7 hinge is metazoan-enriched and delta-private.** 0/4 or 1/4 in all
  four out-of-family human controls, 1/4 or less in the three fungi, 3–4/4 in
  metazoa and *Dictyostelium*. It sits inside `IPR010474`, whose InterPro name
  is "AP-3 complex subunit delta domain, metazoa", so the two independent
  signals agree.

Caveat recorded in `RESULTS.md`: the hinge lies in a MobiDB-lite disordered
region (UniProt REGION 629–696 / 726–920 flank it), so column assignment there
is less reliable than in the HEAT trunk. The 4/4 mouse and bovine results do not
depend on that, because both proteins align 1:1 with human through residue 713
— mouse and bovine native positions come out identical to human's for all
eleven residues, which is what the `residue_claims` use.

**How the residue claims are used.** The Bilateria node `PTN000513028` is seeded
by mouse Ap3d1 (and rat, for `GO:0016182`). The claims record, in checkable
form, that human retains every mouse residue at these interfaces — i.e. there is
no target-specific evidence of divergence that would undercut the transfer. They
are `RETAINED` claims with `anchor = UniProtKB:O54774` and `target =
UniProtKB:O14617`, method `MSA`.

---

## 7. The GOA rows, and what affinage missed

59 GOA rows (counted by `AP3D1-bioinformatics/goa_reconcile.py`, which also
proves every GOA row maps to exactly one YAML entry with identical normalized
`supporting_entities`): IEA 29, IBA 10, NAS 8, IMP 3, HDA 2, TAS 2, ISS 2, IPI
1, IDA 1, IC 1.

### Rows needing a positive argument

- **`GO:1990742 microvesicle` (IEA from mouse O54774) — REMOVE.** The GO term
  means *"An extracellular vesicle released from the plasma membrane and ranging
  in size from about 100 nm to 1000 nm."* The mouse donor annotation (IDA+IMP,
  PMID:16760431) uses "microvesicle" in the Faundez-lab sense of small
  **intracellular** AP-3/BLOC-1 vesicles carrying LAMP1, PI4KIIα and VAMP7-TI
  [PMID:16760431 "we show that the BLOC-1 complex resides on microvesicles that also contain AP-3 subunits and membrane proteins that are known AP-3 cargoes"].
  A vesicle carrying LAMP1 and PI4KIIα from a cell homogenate is not an
  extracellular vesicle. The defect is on the donor side
  (`source_status: SOURCE_BAD`); mouse Ap3d1 has no review in this repository,
  so there is nothing to fix upstream here, but it is flagged.
- **`GO:0016020 membrane` (HDA, PMID:19946888) — MARK_AS_OVER_ANNOTATED.**
  Reference-projection test: QuickGO `reference=PMID:19946888`, paginated fully,
  gives **1142 distinct entities**. An NK-cell membrane proteome that produced
  1142 annotations is a survey, not a localisation claim about AP3D1.
  (`GO:0005765 lysosomal membrane`, PMID:17897319, projects to 242 entities —
  kept, but non-core: AP-3 is a peripheral coat that cycles onto membranes, and
  its productive site is the tubular sorting endosome upstream of lysosomes.)
- **`GO:0035651 AP-3 adaptor complex binding` (IEA from mouse O54774) —
  MARK_AS_OVER_ANNOTATED.** The mouse source is IDA from PMID:19010779, a
  crosslinking/MS study that co-isolated AP-3 with BLOC-1, BLOC-2, HOPS,
  clathrin and PI4KIIα. The term is for proteins that *bind* AP-3 from outside;
  AP3D1 **is** AP-3, and `GO:0030123 … part_of` already states that. Applying a
  binding term to a constituent subunit inverts the part/whole relation.
- **`GO:0140916 zinc ion import into lysosome` (IMP, PMID:17349999) — MODIFY →
  `GO:0061462 protein localization to lysosome`.** The experiment is
  AP3D1-specific and sound — the siRNA targeted delta
  [PMID:17349999 "For AP-3 protein complex knockdown, the target was the δ subunit of the complex."]
  and depleted the complex
  [PMID:17349999 "targeting of the AP-3 δ subunit effectively depleted the endogenous AP-3 complex"].
  But AP-3 is not the zinc importer; ZnT2/ZnT3 are, and the paper's own result
  is that GFP-ZnT2 expression *rescues* the AP-3-depleted phenotype. AP-3
  delivers the transporter; the transporter moves the zinc. Role conflation.

### What affinage missed

The affinage record (`self_evaluation_pairwise: win`, `faith_pct: 100.0`, 11
citations, trust gates clear per `.affinage.log`) is accurate about this protein
— no symbol collision, the narrative is about AP-3 delta throughout — and its
recent-cargo material (IFNGR1/OPTN PMID:33627378, DRAM2 PMID:42059423, RNF13,
TGFβ2, the zebrafish *crasher* mutant PMID:35816398) is genuinely useful
context. But it is precision-not-recall, exactly as expected, and it missed
every paper this review actually turned on:

- the **mocha** mouse (PMID:9697856), despite the brief naming it — affinage
  cites two 2009 mocha follow-ups but not the 1998 identification;
- **garnet** / the discovery of delta-adaptin (PMID:9303295) and the AP-3
  characterisation (PMID:9151686);
- the entire **structural** literature: PMID:34688652, PMID:39705307,
  PMID:42139345, PMID:22521722 — i.e. both the ARF1 and the VAMP7 interfaces,
  which are the only subunit-level molecular functions AP3D1 has;
- the **clathrin** papers (PMID:9545220, PMID:15051738, PMID:23761069);
- every **PAINT donor** paper (PMID:9250663, PMID:9335339, PMID:17895371,
  PMID:11588176, PMID:20089890, PMID:19144828, PMID:21998198, PMID:15860731,
  PMID:22539861, PMID:24217640, PMID:18634783);
- **BLOC-1/AP-3** (PMID:16760431, PMID:33886957).

Pattern: the missed papers are titled for the complex ("AP-3", "AP3"), for a
partner (VAMP7, BLOC-1, clathrin, ARF1) or for a mutant name (mocha, garnet) —
never for the gene symbol. Searching Europe PMC on `"delta-adaptin" OR "AP3D1"`,
`mocha mouse AP-3 adaptin`, `"AP-3" AND clathrin`, `"AP-3" AND ARF1`,
`"BLOC-1" AND "AP-3"` and `garnet Drosophila delta-adaptin pigment granule`
recovered all of them.

---

## 8. Synthesis

AP3D1 is the single, non-redundant large "delta" adaptin of AP-3. Within the
complex it does three things that are demonstrably delta's rather than AP-3's in
general: it carries the primary ARF1-GTP binding site (two interfaces,
F77/M110/L111 and H157/K159/R163/R187) that recruits and holds the complex on
the membrane; it contributes, with sigma-3, the dileucine cargo pocket; and its
hinge (residues 680–729) is a dedicated receptor for the longin domain of
SNARE-engaged VAMP7. With ARF1 dimers it polymerises into spiralling arches that
tubulate the donor membrane into a carrier — without clathrin. Because delta is
shared by the ubiquitous AP-3A and the neuronal AP-3B complexes, its loss
removes both, which is why *mocha* mice and HPS10 patients combine the
melanosome/platelet-dense-granule/lysosome phenotypes of HPS with a severe
neurological phenotype that AP3B1 loss (HPS2) lacks.

Core: AP-3 complex membership, cargo-adaptor activity (contributed), ARF1
binding, VAMP7/SNARE binding, coat assembly on endosomal membranes, and
protein targeting from endosomes to lysosomes. Non-core: everything
cell-type-specific downstream of that one sorting step — melanosome, platelet
dense granule, synaptic vesicle, otolith, glutamatergic synapse — real, but
tissue context rather than evolved molecular role.

## 9. Open questions

1. Does delta's N-terminal amphipathic helix actually deform membranes, or only
   bind them? Both structural papers stop short.
2. Is there a mammalian TGN pool of AP-3 that does Golgi→lysosome transport as
   in yeast, or is the endosomal exit site the whole story?
3. The ~300-residue disordered region 726–920, heavily phosphorylated, has no
   assigned function. Does phosphorylation gate ARF1 binding or cargo capture?
4. Why does BLOC-1 regulate AP-3 in a brain-region-specific way (PMID:20089890),
   given that both complexes are ubiquitous?
5. HPS10 patients have hearing loss as a presenting feature in at least one
   family (PMID:36445457) and mocha mice have otoconial deficits
   (PMID:15109702); AP-3 is required for Vangl2 trafficking and inner-ear planar
   cell polarity (PMID:31268833). Which AP-3 cargo is the cochlear one?
