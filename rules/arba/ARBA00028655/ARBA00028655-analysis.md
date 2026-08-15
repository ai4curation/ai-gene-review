# ARBA00028655 analysis — GO:0006661 "phosphatidylinositol biosynthetic process"

Companion analysis for `ARBA00028655-review.yaml`.

- Rule created: 2021-10-20; last modified: 2025-12-15
- Consequent: a single GO annotation, **GO:0006661 phosphatidylinositol biosynthetic process** (aspect P)
- Antecedent: **25 alternative condition sets** (OR-ed), built from InterPro entries, CATH FunFams and taxon constraints
- Verdict in one line: **2 of 25 condition sets are biochemically correct; under 1% of the annotations the rule actually emits are defensible.**

All ontology facts below were checked against QuickGO/OLS on 2026-08-15. All census
numbers below come from the reproducible script in `scripts/census_arba00028655.py`,
run on 2026-08-15.

---

## 1. The ontology-branch argument

GO:0006661 is defined as:

> The chemical reactions and pathways resulting in the formation of phosphatidylinositol,
> any glycophospholipid in which the sn-glycerol 3-phosphate residue is esterified to the
> 1-hydroxyl group of 1D-myo-inositol.

Two structural facts about the ontology decide this review.

**(a) GO:0006661 is effectively a leaf.** Its only children are the regulation terms
(`regulation of`, `positive regulation of`, `negative regulation of` phosphatidylinositol
biosynthetic process). There is no "phosphoinositide" sub-branch beneath it. So an
annotation to GO:0006661 is a commitment to the specific claim that the protein
participates in forming the unphosphorylated PI molecule itself — it is not a safe,
vague umbrella.

**(b) The phosphoinositide branch is a SIBLING, not a descendant.** QuickGO ancestor
closure (is_a + part_of) for **GO:0046854 phosphatidylinositol phosphate biosynthetic
process** is:

```
GO:0046474 glycerophospholipid biosynthetic process
GO:0046486, GO:0006650, GO:0006644, GO:0008654, GO:0045017, GO:0008610,
GO:0006629, GO:0019637, GO:0006793, GO:0090407, GO:0009058, GO:0044238,
GO:0008152, GO:0009987, GO:0008150
```

**GO:0006661 does not appear in that list.** The two terms first meet at
GO:0046474 glycerophospholipid biosynthetic process. Therefore annotating a PI 3-/4-/5-kinase
to GO:0006661 is not an over-broad annotation that a curator could later refine downward;
it is a **wrong-branch (MISMATCHED)** annotation whose true term lies in a parallel subtree.
The same holds a fortiori for the phosphatases (whose process is dephosphorylation /
turnover, GO:0046856), for the GPI enzymes (GO:0006506), and for DPM1 (GO:0180047).

The commissioned deep research reaches the same conclusion independently, noting that
"[t]he ontology's separate phosphorylation, signaling, and GPI terms are strong evidence
that GO:0006661 should not be used as a generic parent for every reaction involving a
PI-containing molecule", and that "outright incorrect" here "means that the protein's
established molecular function lies in a chemically different process, not merely that a
more specific child term is preferable"
(`ARBA00028655-deep-research-falcon.md`).

Relevant term labels verified 2026-08-15 (QuickGO):

| Term | Label | Obsolete |
|---|---|---|
| GO:0006661 | phosphatidylinositol biosynthetic process | no |
| GO:0046854 | phosphatidylinositol phosphate biosynthetic process | no |
| GO:0036092 | phosphatidylinositol-3-phosphate biosynthetic process | no |
| GO:0046856 | phosphatidylinositol dephosphorylation | no |
| GO:0006506 | GPI anchor biosynthetic process | no |
| GO:0180047 | dolichol phosphate mannose biosynthetic process | no |
| GO:0035014 | phosphatidylinositol 3-kinase regulator activity (MF) | no |

Note: the deep-research report refers to GO:0046854 as "phosphatidylinositol
phosphorylation". That is a superseded label; the current primary label of GO:0046854 is
"phosphatidylinositol phosphate biosynthetic process". The report's reasoning is
unaffected.

---

## 2. Census methodology

`scripts/census_arba00028655.py` (run: `uv run python rules/arba/ARBA00028655/scripts/census_arba00028655.py`)
does the following, with nothing hardcoded:

1. Query the QuickGO annotation search API for
   `goId=GO:0006661 & goUsage=exact & evidenceCode=ECO:0000256 & reference=GO_REF:0000117`.
2. Keep only rows whose `withFrom` connected xrefs name **ARBA00028655** (this is what
   attributes an annotation to this specific rule rather than to ARBA in general).
3. QuickGO paging is capped, so sample `limit=100` over pages `[1, 5, 10, 15, 20, 25, 30, 35, 40, 45]`,
   i.e. a spread of ~1,000 accessions across the result set rather than the first page only.
4. Resolve the sampled accessions to UniProt `protein_name` in batches of 100 via the
   UniProtKB REST search endpoint, and count names.

The human subset was obtained by the same QuickGO query restricted to `taxonId=9606`.

**Caveat.** The name counts are a stratified sample of 1,000 of 4,782 annotations, not a
full enumeration, and protein names are UniProt's recommended names (so TrEMBL entries may
carry submitted or predicted names such as "Lateral signaling target protein 2 homolog").
The composition is nevertheless overwhelming and not sensitive to sampling.

---

## 3. Census output (run 2026-08-15)

**4,782** annotations total carry GO:0006661 / ECO:0000256 / GO_REF:0000117 with
ARBA00028655 in `withFrom`.

Sample of 1,000 accessions, resolved protein names:

| n | % | Protein name | Actual biochemistry | GO:0006661 correct? |
|---:|---:|---|---|---|
| 638 | 63.8 | Phosphatidylinositol-3,5-bisphosphate 3-phosphatase (myotubularin family) | PI(3,5)P2 → PI5P; PI3P → PI | no — dephosphorylation |
| 86 | 8.6 | 1-phosphatidylinositol 4-kinase | PI → PI4P | no — kinase |
| 79 | 7.9 | Lateral signaling target protein 2 homolog | myotubularin-related (LST2/MTMR-like) | no |
| 35 | 3.5 | Synaptojanin-1 | PI(4,5)P2 → PI4P (5-phosphatase + SAC) | no |
| 26 | 2.6 | Phosphatidylinositol-3-phosphatase SAC1 | PI4P → PI | no — dephosphorylation |
| 15 | 1.5 | Myotubularin-related protein 2 | PI3P/PI(3,5)P2 phosphatase | no |
| 15 | 1.5 | Synaptojanin-2 | phosphoinositide 5-phosphatase | no |
| 13 | 1.3 | Myotubularin-related protein 7 | phosphoinositide phosphatase | no |
| 12 | 1.2 | Myotubularin | PI3P → PI | no |
| 12 | 1.2 | Phosphatidylinositol 3,4,5-trisphosphate 5-phosphatase | PIP3 → PI(3,4)P2 | no |
| 11 | 1.1 | Polyphosphoinositide phosphatase (FIG4) | PI(3,5)P2 5-phosphatase | no |
| **8** | **0.8** | **CDP-diacylglycerol--inositol 3-phosphatidyltransferase (CDIPT/PIS)** | **CDP-DAG + myo-inositol → PI** | **YES** |
| 8 | 0.8 | Membrane-associated phosphatidylinositol transfer protein 2 (PITPNM2) | lipid transfer, PH/DDHD | no |
| 7 | 0.7 | INPPL1 (SHIP2) | PIP3 5-phosphatase | no |
| 7 | 0.7 | INPP5F | phosphoinositide phosphatase | no |
| 4 | 0.4 | PITPNM1 | lipid transfer | no |
| 4 | 0.4 | SAC domain-containing protein | phosphoinositide phosphatase | no |
| 4 | 0.4 | Phosphatidylinositol-4-phosphate 5-kinase | PI4P → PI(4,5)P2 | no |
| 3 | 0.3 | DDHD domain-containing protein | phospholipase/lipid binding | no |
| 2 | 0.2 | Pleckstrin homology domain-containing family A member 8 (FAPP2) | PI4P-binding transfer protein | no |
| 1 | 0.1 | **Cytochrome b-c1 complex subunit 9 (UQCR10)** | respiratory chain subunit | no — pure artifact |
| ~10 | ~1.0 | assorted myotubularin cDNAs / fragments | phosphoinositide phosphatases | no |

**Only 8 of 1,000 sampled proteins (0.8%) are PI synthase.** Extrapolated, roughly 40 of the
4,782 emitted annotations are biochemically defensible.

The single UQCR10 (cytochrome b-c1 complex subunit 9) hit is a striking domain-promiscuity
artifact: a small single-transmembrane respiratory-chain subunit with no connection to
lipid metabolism.

### Human subset (taxonId=9606): 169 annotations

| Gene | n | Gene | n |
|---|---:|---|---:|
| FIG4 | 28 | MTMR2 | 6 |
| SACM1L | 16 | SYNJ2 | 5 |
| MTMR1 | 16 | MTMR4 | 5 |
| MTM1 | 15 | PITPNM1 | 5 |
| INPP5F | 12 | INPPL1 | 5 |
| SYNJ1 | 9 | PITPNM2 | 4 |
| MTMR3 | 9 | PLEKHA3 | 4 |
| PLEKHA8 | 6 | MTMR7 | 3 |
| **CDIPT** | **2** | INPP5D | 1 |

**2 of 169 human annotations (1.2%) are CDIPT.** Every other human gene hit by this rule
is a phosphoinositide phosphatase, a lipid-transfer/PH-domain protein, or an inositol
polyphosphate 5-phosphatase.

### Curator report (upstream, treated as a report only)

geneontology/go-annotation issue **#5835** (opened 2025-06-12 by a PomBase curator) flags
"Lots of off target inferences" on *S. pombe* dpm1 (SPAC31G5.16c) across
ARBA00027430 / ARBA00026302 / ARBA00027853 / ARBA00028538 / ARBA00028655. For this rule the
curator wrote of `GO:0006661 | phosphatidylinositol biosynthetic process | IEA with
ARBA00028655`: "I don't get this one?" — i.e. no rationale was visible to them. Condition
set 25 (the DPM1 FunFam, `3.90.550.10:FF:000036`) is the route by which dpm1 was hit.
*S. pombe* DPM1 (O14466) currently carries GO:0180047, GO:0006488, GO:0006506 and
GO:0035269 — and no GO:0006661 — consistent with the curator's objection having been acted
on locally while the rule remains unchanged.

---

## 4. Per-condition-set verdict table

| CS | Conditions (domain / FunFam) | Taxon | Protein family captured | Actual reaction / role | Verdict | Recommended term |
|---:|---|---|---|---|---|---|
| 1 | IPR000387 + IPR010569 | Primates | Myotubularins (MTM1, MTMR1-7) | PI3P → PI; PI(3,5)P2 → PI5P | **INCORRECT** | GO:0046856 |
| 2 | IPR002013 (SAC domain) | Haplorrhini | SACM1L, SYNJ1/2, FIG4, INPP5F | PI4P → PI, PIP 5-phosphatase | **INCORRECT** | GO:0046856 |
| 3 | 1.10.1070.11:FF:000002 | Eukaryota | PIK3C3 / VPS34 (class III PI3K) | PI → PI3P | **INCORRECT** | GO:0036092 |
| 4 | 1.10.1070.11:FF:000006 + 1.25.40.70:FF:000001 + 2.60.40.150:FF:000041 | — | PIK3CA/CB p110 (class IA) | PI(4,5)P2 → PI(3,4,5)P3 | **INCORRECT** | GO:0046854 |
| 5 | 1.10.1070.11:FF:000001 + 1.25.40.70:FF:000004 + 2.60.40.150:FF:000046 | — | PIK3CB p110β | PI(4,5)P2 → PIP3 | **INCORRECT** (also ~duplicate of CS4) | GO:0046854 |
| 6 | 1.10.1070.11:FF:000003 + 2.60.40.150:FF:000036 + 3.30.1010.10:FF:000001 | — | PIK3C2B (class II) | → PI3P / PI(3,4)P2 | **INCORRECT** | GO:0046854 |
| 7 | 3.30.800.10:FF:000002 + 3.30.810.10:FF:000003 | Primates | PIP4K2B (type II) | PI5P → PI(4,5)P2 | **INCORRECT** | GO:0046854 |
| 8 | 2.30.29.30:FF:000038 | Haplorrhini | **PH-domain superfamily** (label says "Myotubularin 1, isoform CRA_a"; actually hits PLEKHA3, PLEKHA8, PITPNM1/2) | lipid binding / transfer | **INCORRECT + PROMISCUOUS** | delete (no BP term) |
| 9 | 3.30.470.160:FF:000001 ("Kinase") | Catarrhini | PIP-kinase insert region; label uninformative | — | **INCORRECT** | delete (or GO:0046854) |
| 10 | 3.30.800.10:FF:000001 | Mus | PIP5K1C (type I PIP5K) | PI4P → PI(4,5)P2 | **INCORRECT** | GO:0046854 |
| 11 | 3.30.800.10:FF:000009 | *(none)* | *S. pombe* Its3 PIP5K | PI4P → PI(4,5)P2 | **INCORRECT** | GO:0046854 |
| 12 | 3.40.720.10:FF:000015 | *(none)* | PIGN (GPI-EtNP transferase 1) | modifies GPI intermediate | **INCORRECT** | GO:0006506 |
| 13 | 1.10.1070.11:FF:000010 + 1.25.40.70:FF:000006 + 2.60.40.150:FF:000087 | — | PIK3CG p110γ (class IB) | PI(4,5)P2 → PIP3 | **INCORRECT** (also ~duplicate of CS4/5) | GO:0046854 |
| 14 | 1.10.1070.11:FF:000013 + 1.25.40.70:FF:000010 | Glires | PIK3C2G (class II) | → PI3P / PI(3,4)P2 | **INCORRECT** (concept-duplicate of CS6) | GO:0046854 |
| 15 | 1.10.287.1490:FF:000001 + 1.10.555.10:FF:000035 | Rodentia | **PIK3R1 / p85α — REGULATORY subunit** | non-catalytic | **INCORRECT — NON-CATALYTIC** | delete (MF GO:0035014 if anything) |
| 16 | 3.30.505.10:FF:000035 + 3.60.10.10:FF:000005 | Homo | INPPL1 / INPP5D (SHIP) | PIP3 → PI(3,4)P2 | **INCORRECT** | GO:0046856 |
| 17 | 1.10.1070.11:FF:000019 ("PI 4-kinase beta 1") | **Viridiplantae** | PI4K | PI → PI4P | **INCORRECT + inconsistent taxon** | GO:0046854 |
| **18** | **1.20.120.1760:FF:000003** | **Vertebrata** | **CDIPT / PIS (EC 2.7.8.11)** | **CDP-DAG + myo-inositol → PI** | **CORRECT — RETAIN** | GO:0006661 |
| **19** | **1.20.120.1760:FF:000021** | **Fungi** | **PIS** | **CDP-DAG + myo-inositol → PI** | **CORRECT — RETAIN** | GO:0006661 |
| 20 | 2.60.40.150:FF:000148 | Euteleostomi | **UVRAG — non-catalytic VPS34 complex II subunit** | regulatory/targeting | **INCORRECT — NON-CATALYTIC** | delete (macroautophagy/endosomal terms) |
| 21 | 3.30.40.10:FF:000073 | Mammalia | MTMR4 (in Zn-finger RING/FYVE/PHD superfamily) | PI3P phosphatase | **INCORRECT + PROMISCUOUS FOLD** | GO:0046856 / delete |
| 22 | 3.40.50.10320:FF:000002 | Eutheria | PIGL (GlcNAc-PI de-N-acetylase) | GlcNAc-PI → GlcN-PI | **INCORRECT** | GO:0006506 |
| 23 | 3.40.720.10:FF:000041 | Euarchontoglires | PIGO (GPI-EtNP transferase 3) | modifies GPI intermediate | **INCORRECT** | GO:0006506 |
| 24 | 3.60.21.10:FF:000022 | *(none)* | PGAP5 / MPPE1 | GPI remodelling phosphodiesterase | **INCORRECT** | GO:0006506 |
| 25 | 3.90.550.10:FF:000036 | *(none)* | **DPM1** | GDP-Man + Dol-P → Dol-P-Man | **INCORRECT — flagged by curators (#5835)** | GO:0180047 (+ GO:0006506) |

Summary: **2 correct (CS18, CS19)**; 15 kinase/phosphatase wrong-branch; 2 non-catalytic
regulatory subunits (CS15, CS20); 5 GPI/glycosylation-pathway sets (CS12, CS22, CS23,
CS24, CS25); 2 sets built on promiscuous structural folds (CS8, CS21; CS9 has an
uninformative "Kinase" label).

Notably, **no condition set targets CDS1/CDS2** (CDP-DAG synthases), the one other family
the literature considers a legitimate participant in de novo PI biosynthesis. The rule thus
manages to be both massively over-inclusive and incomplete.

---

## 5. Taxonomic scope

The taxon constraints across the 25 sets are: Primates (×2), Haplorrhini (×2), Catarrhini,
Homo, Mus, Glires, Rodentia, Eutheria, Euarchontoglires, Mammalia, Vertebrata,
Euteleostomi, Viridiplantae, Fungi, Eukaryota — and **no constraint at all** for CS4, CS5,
CS6, CS11, CS12, CS13, CS24, CS25.

None of these restrictions tracks the biology. Myotubularins, SAC-domain phosphatases,
PI3Ks, PIP5Ks, the GPI pathway and DPM1 are all pan-eukaryotic; there is no biological
reason for a "Homo"-only INPPL1 set (CS16), a "Mus"-only PIP5K1C set (CS10), or
"Catarrhini"-only kinase set (CS9). These read as artifacts of the association-mining step
picking up whichever clade happened to be densely annotated, and they make the rule's
behaviour unpredictable: the sets with **no** taxon constraint (notably CS25/DPM1 and
CS11/Its3) fire across all of UniProt, which is exactly how *S. pombe* dpm1 acquired the
annotation that prompted issue #5835.

CS17 is internally inconsistent in a diagnostic way: a FunFam labelled "Phosphatidylinositol
4-kinase beta 1" paired with a Viridiplantae restriction.

Separately, the deep research notes that "PI synthesis is not eukaryote-exclusive" (PI/PIP
synthases occur in mycobacteria and in archaea with inositol ether lipids), so the two
correct condition sets (Vertebrata / Fungi) are also *too narrow* for the underlying
biology — although narrowness of a correct set is a far smaller problem than the
false-positive load of the other 23.

---

## 6. Recommendation

**SPLIT.** Do not simply deprecate: condition sets 18 and 19 are correct and useful, and
CDIPT/PIS is exactly the family GO:0006661 exists to describe. The rest of the rule should
be dissolved.

1. **Keep GO:0006661 only on CS18 and CS19** (the two CDIPT/PIS FunFams). Consider merging
   them into one PIS rule and broadening the taxon to Eukaryota (or dropping the taxon),
   since the CDP-DAG/PIS route is pan-eukaryotic and not eukaryote-exclusive. Consider
   adding a CDS1/CDS2 condition set, which is currently missing.
2. **Retire GO:0006661 from the other 23 condition sets.**
3. **Move the PI/PIP kinase sets** (CS3, CS4, CS5, CS6, CS7, CS9, CS10, CS11, CS13, CS14,
   CS17) to **GO:0046854** phosphatidylinositol phosphate biosynthetic process, or to the
   product-specific child where the FunFam pins the product (e.g. **GO:0036092** for
   VPS34/CS3).
4. **Move the phosphoinositide phosphatase sets** (CS1, CS2, CS16, CS21) to **GO:0046856**
   phosphatidylinositol dephosphorylation.
5. **Move the GPI-pathway sets** (CS12, CS22, CS23, CS24) to **GO:0006506** GPI anchor
   biosynthetic process.
6. **Move CS25 (DPM1)** to **GO:0180047** dolichol phosphate mannose biosynthetic process
   (GO:0006506 additionally by pathway participation). This directly resolves the dpm1
   complaint in geneontology/go-annotation#5835.
7. **Delete CS15 (PIK3R1/p85α) and CS20 (UVRAG) entirely** from any biosynthetic rule — both
   are non-catalytic; at most p85 warrants the MF GO:0035014.
8. **Delete CS8 and CS21 as fold-promiscuous**: CS8 is a bare PH-domain-superfamily FunFam
   with a misleading myotubularin label that in practice captures PLEKHA3/8 and PITPNM1/2;
   CS21 sits in the Zn-finger RING/FYVE/PHD superfamily. CS9's label is merely "Kinase" and
   should not be used as a sole condition.
9. **Retract the ~4,740 existing GO:0006661 IEA annotations** attributed to this rule that
   do not derive from CS18/CS19.
