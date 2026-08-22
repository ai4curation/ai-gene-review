# ARBA00027853 analysis — GO:0006720 "isoprenoid metabolic process"

Companion analysis for `ARBA00027853-review.yaml`.

- Rule created: 2021-10-20; last modified: 2025-12-15
- Consequent: a single GO annotation, **GO:0006720 isoprenoid metabolic process** (aspect P)
- Antecedent: **94 alternative condition sets** (OR-ed), built from 122 distinct
  InterPro entries, CATH FunFams and PANTHER families, plus taxon constraints
- Raised by GO curators in [geneontology/go-annotation#5835](https://github.com/geneontology/go-annotation/issues/5835)
  ("Lots of off target inferences")

**Verdict in one line:** unlike the sibling rule ARBA00028655 from the same issue,
this rule's GO term is in the *right* branch and roughly 65 of its 94 condition sets
are genuine isoprenoid-pathway families — but 13 branches are plainly off-target, 16
cannot be audited from their identifiers, and, most seriously, **the annotations the
rule actually emits cannot be reproduced from its published condition sets**.

All ontology facts below were checked against QuickGO/OLS on 2026-08-22. All census
numbers come from the reproducible script in `scripts/census_arba00027853.py`, run on
2026-08-22. PANTHER names were resolved against `interpro/panther/panther.obo`.

---

## 1. The GO term is appropriate, and the issue's premise needs a caveat

GO:0006720 is defined as:

> The chemical reactions and pathways involving isoprenoid compounds, isoprene
> (2-methylbuta-1,3-diene) or compounds containing or **derived from** linked isoprene
> (3-methyl-2-butenylene) residues.

The go-annotation issue text objects that a flagged protein "is derived from an
isoprenoid, but not an isoprenoid". That objection does not hold against the GO
definition as written: *derived from* linked isoprene residues is explicitly in scope.
This is why retinoid metabolism sits under isoprenoid metabolism —
`GO:0001523 retinoid metabolic process` **is** a descendant of GO:0006720 (QuickGO
ancestor closure, 2026-08-22), as are `GO:0006721 terpenoid metabolic process`,
`GO:0016114 terpenoid biosynthetic process`, `GO:0016109 tetraterpenoid biosynthetic
process`, `GO:0016102 diterpenoid biosynthetic process` and `GO:0009686 gibberellin
biosynthetic process`.

The converse is the boundary that *does* matter here: **steroids are not in the
isoprenoid branch**. The QuickGO ancestor closure of `GO:0008202 steroid metabolic
process` is `{GO:0008150, GO:0008152, GO:0006629, GO:0008202, GO:0044238, GO:0009987}`
— it does **not** contain GO:0006720. So condition sets that reach the rule through
sterol trafficking or steroid-modifying chemistry are wrong-branch, not merely broad.
Two branches fail on exactly this: CS63 (LDLR/LRP1) and, empirically, the steroid half
of the PRISE family reached by CS39 (see §4).

Note also what the issue's own follow-up comment records: the specific S. pombe protein
cited there, `SPAC31G5.16c` = **dpm1 (O14466)**, is a dolichol-phosphate
mannosyltransferase. It carries GO:0180047, GO:0006488, GO:0006506 and GO:0035269 and
**no** GO:0006720 today, and it is not reachable from any of this rule's 94 condition
sets. The DPM1 complaint in #5835 belongs to ARBA00028538 / ARBA00028655, not here.

## 2. What the rule emits (and why the deep research was misinformed)

The UniProt API's `statistics` block for this rule reports
`reviewedProteinCount: 0, unreviewedProteinCount: 0`. The commissioned Falcon deep
research was handed that figure and concluded there is "no present production set from
which empirical precision can be measured", making its "zero-hit behaviour" a central
theme of its recommendations. **That premise is false.** A QuickGO census on 2026-08-22
finds:

| quantity | value |
|---|---|
| live GO:0006720 / ECO:0000256 / GO_REF:0000117 annotations with `WITH/FROM = ARBA:ARBA00027853` | **8,974** |
| distinct proteins | 8,974 |
| distinct taxa | 1,570 |
| distinct protein names | 593 |

Protein-name census over all 8,974 (first-match-wins buckets; see the script):

| share | bucket |
|---|---|
| 47.6% | carotenoid/retinoid cleavage + isomerase (BCO1, BCO2, RPE65, NinaB) |
| 30.4% | prenyl/polyprenyl diphosphate synthase (PDSS1, PDSS2, FPPS, GGPPS) |
| 16.0% | uncharacterized / hypothetical / bare "domain-containing protein" |
| 1.9% | generic SDR / dehydrogenase / oxidoreductase |
| 1.5% | progesterone 5β-reductase / 3-oxo-Δ4-steroid 5β-reductase |
| 1.3% | other, unclassified |
| 0.9% | iridoid synthase / PRISE (monoterpenoid side) |
| 0.4% | terpene synthase / cyclase |
| 0.1% | MVA/MEP precursor enzymes |

So on the *emitted* evidence this is not a near-total-false-positive rule of the
ARBA00028655 kind: roughly 78% of what it produces is unambiguously isoprenoid
metabolism, and the demonstrable false-positive tail is a few percent. The human subset
(47 annotations, enumerated exhaustively) is **100% on-target**: BCO1, BCO2, GGPS1,
PDSS1, PDSS2 and nothing else. Mouse, rat, macaque, chimpanzee, cow and rabbit subsets
are likewise carotenoid oxygenases and prenyl diphosphate synthases only.

The corollary is uncomfortable for the rule's design: **the great majority of its 94
condition sets contribute nothing observable.** Terpene synthases — the single largest
group of branches, ~19 condition sets — account for 0.4% of output. Whatever the 94-way
disjunction is doing, it is not what the branch count suggests.

## 3. The emitted set does not match the published condition sets

This is the most serious finding, and it is independent of any biological judgement.

In a random 300-protein sample of the emitted set (seed 7):

- **187/300 (62%) carry InterPro IPR004294 "Carotenoid oxygenase"**, and **167 of those
  187 (89%) are not mammals** — Anopheles, cyprinid fish, snails, turtles. But the only
  IPR004294 branch in the published rule is **CS7 = IPR004294 AND taxon Mammalia**.
- **89/300 (30%) carry IPR000092 "Polyprenyl synthetase-like"**, but only **25 of those
  89 (28%)** also carry IPR039702, which the only IPR000092 branch (**CS16 = IPR000092
  AND IPR039702 AND taxon Ecdysozoa**) requires.

Two explanations are consistent with this, and the available data does not choose
between them: either the taxon and co-signature conjunctions are not enforced at
annotation time the way the published condition sets read, or the rule content served by
the API today (modified 2025-12-15) has diverged from the release that produced the
current GOA annotations. Either way, **the constraints that make this rule look safe on
paper are not visible in the data it is credited with**, and no downstream consumer can
audit it. This, rather than any single bad branch, is the strongest reason the rule
cannot be signed off as-is — and it is a plausible mechanism behind the "lots of off
target inferences" reported in #5835.

## 4. The observable false positives, and where they come from

Spot-checks confirm the small wrong tail is real, and that most of it enters through a
*correct* signature sitting on a *broken gene model* rather than through a bad condition:

| accession | UniProt protein name | organism | InterPro content |
|---|---|---|---|
| A0A182JU85 | Argininosuccinate lyase | *Anopheles christyi* | IPR004294 **+** IPR000362 (fumarase/ASL) |
| A0A2T7PU42 | Integrator complex subunit 11 | *Pomacea canaliculata* | IPR004294 **+** metallo-β-lactamase domains; entry carries an explicit `CAUTION: ... preliminary data` |
| A0A671PWY6 | Synaptic vesicle membrane protein VAT-1 homolog-like | *Sinocyclocheilus anshuiensis* | IPR004294, PANTHER PTHR10543:SF110 |

These are chimeric or mispredicted whole-genome-shotgun gene models that genuinely
contain a carotenoid-oxygenase domain next to something unrelated. The rule is not
inventing the domain; the upstream protein model is wrong. That is worth saying plainly,
because it means "delete the bad branches" would not remove these particular errors.

Other members of the tail are ordinary domain promiscuity: 14-3-3 protein beta/alpha
(*Ovis aries*), ribosomal protein S13 (*Rattus*), BolA-like protein 3, collagen
alpha-6(VI), sorting nexin-19a, cystathionine γ-lyase, GPAA1, IST1/CHMP8.

The one systematic biological false positive is **CS39** (CATH FunFam
3.40.50.720:FF:000808 "Iridoid synthase", asterids). This FunFam is the PRISE family
(**p**rogesterone 5β-**r**eductase / **i**ridoid **s**ynthase **e**nzymes). Its iridoid
synthase members are correctly in isoprenoid metabolism, but the family's progesterone
5β-reductase / 3-oxo-Δ4-steroid 5β-reductase members are **steroid** enzymes, and
steroid metabolic process is not under GO:0006720 (§1). Empirically the steroid side
(1.5%) outnumbers the iridoid side (0.9%) in the emitted set.

## 5. Per-condition-set triage

64 of 94 branches are on-target, 13 should be removed, 16 cannot be resolved from their
identifiers, and one (CS39) is mixed and needs splitting. (An earlier draft of this table
gave 65/13/16: it omitted CS39 entirely and counted CS89 in both the on-target set and the
hold set. The two errors cancelled to 94, which is why the total looked right.) Full per-set reasoning is in the `notes:` field of each condition set in
`ARBA00027853-review.yaml`; the summary is:

**Remove (13):** twelve off-target, plus CS43, which is removable as an *unsatisfiable*
branch rather than an off-target one — it requires two distinct FunFams from within the
same CATH superfamily (3.40.605.10 FF:000026 and FF:000054), which a single ALDH catalytic
domain cannot satisfy; read as the conjunction it is, its most specific conjunct would
confine it to ALDH1A3-like proteins, which are on-target via GO:0001523. The list: CS14
(bare UGT family + Caryophyllaceae), CS37 (CYP2C9),
CS43 (unsatisfiable ALDH FunFam conjunction), CS44 (hormone-sensitive lipase), CS51 (ADH class
4), CS55 (ADH5/formaldehyde dehydrogenase, *Mus*-only), CS63 (LDLR/LRP1), CS64
(PNPLA2/ATGL), CS66 (phenylalanine aminomutase), CS73 (CYP83B1, glucosinolate), CS78
(bare P450 FunFam, *Homo*-only), CS83 (bare "Glycosyltransferase" FunFam), CS94 (bare
Rossmann/SDR FunFam).

**Unresolved — hold (16):** CS6, CS23, CS35, CS38, CS49, CS65, CS75, CS77, CS80, CS82,
CS84, CS85, CS87, CS89, CS90, CS92.

**Mixed — split (1):** CS39 (FunFam 3.40.50.720:FF:000808 "Iridoid synthase", asterids);
see §7 — the PRISE family mixes isoprenoid iridoid synthases with steroid
5-beta-reductases.

**On-target (64):** the terpene synthase/cyclase branches, the carotenoid backbone and
cleavage branches, the MVA/MEP and prenyl-diphosphate branches, the gibberellin/ABA
branches, the named retinoid branches, and JHAMT.

### 5.1 Two corrections to the deep research

The Falcon report flagged several branches as unauditable "opaque identifiers" and
recommended holding or removing them. Resolving the identifiers against the repository's
PANTHER build settles them, and all of them are on-target:

| condition set | PANTHER id | official PANTHER name |
|---|---|---|
| CS1 | PTHR31225:SF93 | ALPHA-HUMULENE_(-)-(E)-BETA-CARYOPHYLLENE SYNTHASE |
| CS4 | PTHR31739:SF25 | (E,E)-GERANYLLINALOOL SYNTHASE |
| CS5 | PTHR31480 | BIFUNCTIONAL LYCOPENE CYCLASE/PHYTOENE SYNTHASE |
| CS8 | PTHR47950:SF4 | GERANIOL 8-HYDROXYLASE-LIKE |
| CS10 | PTHR31225:SF98 | TERPENE SYNTHASE 9-RELATED |
| CS12 | PTHR31225:SF9 | TERPENE SYNTHASE 10 |
| CS15 | PTHR10543:SF57 | RETINOID ISOMEROHYDROLASE |
| CS17 | PTHR42923:SF45 | 15-CIS-PHYTOENE DESATURASE, CHLOROPLASTIC_CHROMOPLASTIC |
| CS19 | PTHR31225:SF120 | GERMACRENE-A SYNTHASE |

(The one PANTHER condition that the lookup argues *against* is CS6's PTHR47955 =
"CYTOCHROME P450 FAMILY 71 PROTEIN" — the largest and most promiscuous plant P450
family, which is exactly the deep research's stated concern.)

Second, the report speculated that CS20's requirement of two differently named FunFams
(1.10.600.10:FF:000005 "ent-kaur-16-ene synthase" **and** 1.50.10.130:FF:000004 "carene
synthase") "may be internally contradictory or yield no proteins". It is not: the two
FunFams belong to different CATH superfamilies — 1.10.600.10 is the isoprenoid-synthase
α-helical fold and 1.50.10.130 is the terpene-cyclase βγ fold — and plant class-I
diterpene synthases carry both. The conjunction is a domain-architecture requirement and
is one of the better-constructed branches in the rule. The same reading applies to CS61.

It applies to the ALDH branches too, and this analysis did not originally apply it there.
CS65 pairs one FunFam from each of the two ALDH-fold superfamilies (3.40.309.10 and
3.40.605.10) exactly as CS20 pairs its two, so its broad "Aldehyde dehydrogenase 1"
conjunct cannot widen the match set — the specific ALDH8A1 conjunct binds it, and the
branch is better-founded than a first reading suggested. CS43 is the instructive
counter-case: it draws *two* FunFams from within the single superfamily 3.40.605.10, which
one ALDH catalytic domain cannot satisfy, so it is near-certainly a dead branch — and a
dead branch is itself further evidence for the section 3 finding that the emitted set
cannot be reproduced from the published condition sets.

### 5.2 Named FunFams whose taxon constraint contradicts the name

Three branches pair a specific enzyme name with a clade that cannot contain that enzyme,
which is a reliable sign the FunFam label is being read as a function rather than as the
name of its most-studied member:

- **CS23**: FunFam labelled "Cytochrome P450 99A2" restricted to **campanulids**. CYP99A2
  is a rice (Poales) momilactone-pathway P450; campanulids contain no rice.
- **CS75**: FunFam labelled "Taxadiene 5-alpha hydroxylase" restricted to
  **Caryophyllales**. Taxadiene 5α-hydroxylase is from *Taxus* (Pinopsida).
- **CS35**: FunFam labelled "Cytochrome P450 71D8" restricted to **Poales**. CYP71D8 is a
  legume enzyme.

## 6. Taxonomic scope

The taxon constraints are internally inconsistent to the point of arbitrariness.
Twenty-four of the 94 condition sets carry no taxon constraint at all (CS1, CS5, CS9,
CS13, CS17, CS24, CS30, CS34, CS40, CS43, CS52, CS56–CS60, CS80, CS88–CS94), so they fire
across all of UniProt, while other
branches on pan-taxonomic enzyme families are pinned to single genera or species:
**CS55 = *Mus*, CS78 = *Homo*, CS72 = Hominidae, CS37 = Primates, CS50 = Haplorrhini,
CS63 = Catarrhini**. Nothing about ADH5, an unnamed P450 FunFam, CYP26B1 or RDH12
justifies a genus-level restriction; these read as annotation-availability artifacts of
the association-rule mining, not as biology. Conversely, CYP26, LRAT, the GA oxidases and
most prenyl synthases are conserved far beyond the clades listed.

Where the constraints reflect real lineage-specific family expansions — Ocimeae,
Nepetoideae, Elsholtzieae and Mentheae for Lamiaceae terpene synthases, *Pinus* for
conifer TPS, Amoebozoa/Evosea/Eumycetozoa for slime-mould TPS, Actinomycetota for
2-methylisoborneol and geranyl-diphosphate methyltransferase, Arthropoda for JHAMT — they
are well chosen. The problem is that the same rule mixes those with the arbitrary ones,
and §3 shows the constraints may not be enforced in the emitted data anyway.

## 7. Recommended disposition

**MODIFY**, with SPLIT as the deep research's preferred longer-term route.

The reason for preferring MODIFY over DEPRECATE is the empirical one in §2: this rule is
currently producing ~8,900 annotations that are, in the large majority, correct and
useful — carotenoid oxygenases and polyprenyl diphosphate synthases across 1,570
taxa. Retiring it would lose far more good annotation than it removes bad. The reason for
not accepting it is §3: the rule as published is not auditable against its own output,
and 13 of its branches are indefensible.

The single highest-priority action is not a biological one. It is for UniProt to
reconcile the published condition sets with the emitted annotation set, and to fix the
`statistics` block that reports zero proteins for a rule with 8,974 live annotations —
that field is what caused an entire commissioned literature review to be conducted on a
false premise.

## 8. Primary literature cited

All six are cached under `publications/`.

- [PMID:37623827] Bajguz & Piotrowska-Niczyporuk (2023) *Biosynthetic Pathways of Hormones
  in Plants.* Metabolites 13:884 — places gibberellins, ABA, strigolactones and
  brassinosteroids downstream of IPP/DMAPP and the prenyl diphosphates.
- [PMID:36830762] Werck-Reichhart (2023) *Promiscuity, a Driver of Plant Cytochrome P450
  Evolution?* Biomolecules 13:394 — CYP706A3 "oxidizes more than twenty different mono- and
  sesquiterpenes"; CYP720B4 "catalyzes the three successive oxidations at C18 of 8 out of 24
  different diterpenoid olefin skeletons". The Falcon report's additional figure of "29
  documented substrates" for CYP706A3 is **accurate** — the paper states "A total of 29
  different substrates are thus currently reported for this enzyme" — but that total includes
  the dinitroaniline herbicides as well as the terpenoids, so it measures overall substrate
  breadth and should not be cited as a count of terpenoid substrates.
- [PMID:31632418] Karunanithi & Zerbe (2019) *Terpene Synthases as Metabolic Gatekeepers in
  the Evolution of Plant Terpenoid Chemical Diversity.* Front Plant Sci — TPS product
  specificity is not diagnosable from a broad TPS domain.
- [PMID:35033002] Rojano et al. (2022) *Assigning protein function from domain-function
  associations using DomFun.* BMC Bioinformatics — domain-based transfer is weaker for
  biological process (Fmax 0.492) than for molecular function (0.624).
- [PMID:38122964] Bonello & Orengo (2024) *FunPredCATH: an ensemble method for predicting
  protein function using CATH.* BBA Proteins Proteomics — abstract-only in our cache.
- [PMID:31319797] Scheibenreif et al. (2019) *FunFam protein families improve residue level
  molecular function prediction.* BMC Bioinformatics — FunFam members agree on only
  36.9 ± 0.6% of binding-residue annotations.
