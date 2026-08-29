# ARBA00028538 analysis — GO:0046467, a consequent that GO obsoleted

Companion analysis for `ARBA00028538-review.yaml`.

- Rule created: 2021-10-20; last modified: **2025-12-15**
- Consequent: a single GO annotation, **GO:0046467**, which UniProt's rule record
  labels "membrane lipid biosynthetic process"
- Antecedent: **51 alternative condition sets** (OR-ed), built from 14 InterPro
  entries, 51 CATH FunFams and 39 taxon constraints
- Raised by a GO curator in
  [geneontology/go-annotation#5835](https://github.com/geneontology/go-annotation/issues/5835),
  against PomBase `SPAC31G5.16c` (= UniProtKB:O14466, *S. pombe* Dpm1)

**Verdict in one line: GO:0046467 was obsoleted by GO on 2025-12-09; the rule was
modified six days later and still asserts it, so the rule now emits zero
annotations — and the `replaced_by` term it would inherit, GO:0008610, is wrong
for roughly a third of its own condition sets, so the obsoletion must not be
allowed to "fix" this rule by remapping.**

Every number below is reproduced by `scripts/census_arba00028538.py`, run on
2026-08-29 against the live UniProt ARBA, QuickGO and CATH APIs. Nothing is
hardcoded.

---

## 1. The decisive fact: the consequent no longer exists

`census_arba00028538.py` fetches the rule from `rest.uniprot.org/arba/` and the
term from the QuickGO ontology service in the same run:

```
=== ARBA00028538: rule as served by UniProt now ===
created  : 2021-10-20
modified : 2025-12-15
condition sets: 51
consequent GO terms: [('GO:0046467', '')]

=== consequent term status in GO ===
{
  "id": "GO:0046467",
  "name": "obsolete membrane lipid biosynthetic process",
  "isObsolete": true,
  "comment": "The reason for obsoletion is that this term groups lipids by their
              localization rather than by their metabolic function, which is
              problematic since most lipids can function in multiple locations.",
  "replacements": ["replaced_by -> GO:0008610"],
  "obsoletion_history_dates": ["2025-12-09"]
}
*** the rule asserts an OBSOLETE GO term ***

=== annotation counts for the consequent ===
GO:0046467 exact, any source        : 0
GO:0046467 exact, GO_REF:0000117    : 0
GO:0008610 (lipid biosynthetic process) exact, GO_REF:0000117: 75535
```

Three things follow.

**(a) The rule is inert but not retired.** It has zero downstream annotations
because the term it points at is gone, yet UniProt still serves it, and its
`modifiedDate` of 2025-12-15 is *after* the 2025-12-09 obsoletion. Whatever
maintenance touched the rule that week did not notice that its only consequent
had been obsoleted. This is exactly the state in which a rule quietly comes back
to life the moment somebody "repairs" it by substituting the `replaced_by` term.

**(b) The obsoletion was requested off the back of the same class of complaint.**
GO's tracker item is
[geneontology/go-ontology#26698](https://github.com/geneontology/go-ontology/issues/26698),
which obsoleted the whole membrane-lipid grouping branch in one action:

| obsoleted term | replaced_by |
|---|---|
| GO:0006643 membrane lipid metabolic process | GO:0006629 lipid metabolic process |
| GO:0046467 membrane lipid biosynthetic process | GO:0008610 lipid biosynthetic process |
| GO:0046466 membrane lipid catabolic process | GO:0016042 lipid catabolic process |
| GO:1905038 regulation of membrane lipid metabolic process | GO:0019216 regulation of lipid metabolic process |

The stated reason — grouping lipids "by their localization rather than by their
metabolic function" — is an ontology-design argument, not a judgment about this
rule. It removes the term but leaves the rule's biology unexamined.

**(c) The curator's specific complaint is only accidentally resolved.** In
go-annotation#5835 the reporter wrote of this rule: *"Dolichol phosphate mannose
(DPM) is not directly involved in membrane lipid biosynthesis, but rather in
protein glycosylation processes"*, and later followed up that pombe "no longer
has these annotations". The census confirms the disappearance and shows what
O14466 carries instead:

```
=== protein flagged in go-annotation#5835: O14466 ===
GO:0004582 (dolichyl-phosphate beta-D-mannosyltransferase activity)  ECO:0000501  GO_REF:0000120  with=['ARBA00088233']
GO:0006664 (glycolipid metabolic process)                            ECO:0000256  GO_REF:0000117  with=['ARBA00028659']
GO:0046474 (glycerophospholipid biosynthetic process)                ECO:0000256  GO_REF:0000117  with=['ARBA00028351']
GO:0051604 (protein maturation)                                      ECO:0000256  GO_REF:0000117  with=['ARBA00026902']
GO:1901137 (carbohydrate derivative biosynthetic process)            ECO:0000256  GO_REF:0000117  with=['ARBA00026302']
ARBA-sourced rows mentioning ARBA00028538: 0
```

ARBA00028538 is indeed gone from this protein. But the reporter's follow-up
comment — *"oh no, some definitely are there now. Will reopen"* — is borne out:
`GO:0046474 glycerophospholipid biosynthetic process` (ARBA00028351) makes the
*same* category error on the *same* protein, and `GO:1901137` (ARBA00026302) is
one of the other rules named in the very same issue. Dpm1 makes dolichyl-phosphate
mannose, a lipid-linked **sugar donor** consumed by N-glycosylation, O- and
C-mannosylation and GPI assembly. UniProt itself already annotates O14466 to
`GO:0180047 dolichol phosphate mannose biosynthetic process`, which is the term
this rule's DPM1 condition sets should have used.

**Reading the term status from the rule record alone will mislead you.** The raw
UniProt JSON carries the term id with an empty label; the label "membrane lipid
biosynthetic process" that appears in this repo's `.enriched.json` comes from
`rules/_labels.json`, which still holds the pre-obsoletion string. Any workflow
that trusts the cached label sees a live, sensible-sounding term.

---

## 2. Why remapping to GO:0008610 would be the wrong repair

`GO:0008610 lipid biosynthetic process` is a legitimate term and already carries
75,535 ARBA-sourced annotations. Substituting it here would keep the rule's
directional and pathway errors intact while making them harder to see, because
the new term is broad enough to look innocuous. Grouped by what the condition
sets actually do:

| class | condition sets | count | is GO:0008610 defensible? |
|---|---|---|---|
| direct membrane-lipid biosynthesis | 1, 4, 7–9, 11, 13, 14, 16–18, 20, 21, 24, 27, 30, 32, 34, 36, 38–42, 44, 49 | 26 | yes, but far too broad — pathway-specific children exist |
| GPI-anchor / lipid-linked-donor assembly | 22, 23, 46, 47, 50 | 5 | wrong pathway; belongs to GO:0006506 / GO:0180047 |
| catabolic — opposite direction | 2, 5, 15, 19, 45 | 5 | **no** — these hydrolyse membrane lipids |
| modification / interconversion, not synthesis | 10, 25, 28, 29, 31, 35 | 6 | no — tailoring or signalling-metabolite turnover |
| non-diagnostic generic families | 3, 6, 33, 48, 51 | 5 | no — acceptor could be protein, glycan or wall |
| mechanistically unrelated | 12, 26, 37, 43 | 4 | **no** — kinase, glycolysis, heme, lipid *binding* |

So at most 26 of 51 sets (51%) survive even the loosest reading, and none of
those 24 needs a term as vague as GO:0008610. The five catabolic sets and four
unrelated sets — 9 of 51 — would become *false* annotations under the remap, not
merely imprecise ones. LpxH (CS38) is the instructive counter-case: it is a
hydrolase, but its hydrolysis is an obligate step *inside* the anabolic Raetz
pathway, so it belongs with the biosynthetic group. Reaction chemistry does not
settle direction; pathway position does.

---

## 3. The structural argument: FunFam specificity borrowed from promiscuous folds

The rule looks specific — 51 named CATH FunFams — but those FunFams sit in only
**26 distinct CATH superfamilies**, and the superfamily names (fetched from CATH
by `census_arba00028538.py --cath`) show what the signal is actually resting on:

```
1.10.10.60      Homeodomain-like
1.10.150.50     Transcription Factor, Ets-1
1.10.510.10     Transferase(Phosphotransferase) domain 1
1.20.144.10     Phosphatidic acid phosphatase type 2/haloperoxidase
2.30.29.30      Pleckstrin-homology domain (PH domain)/Phosphotyrosine-binding domain (PTB)
3.10.120.10     Cytochrome b5-like heme/steroid binding domain
3.20.20.80      Glycosidases
3.40.1090.10    Cytosolic phospholipase A2 catalytic domain
3.40.50.1260    Phosphoglycerate kinase, N-terminal domain
3.40.50.2000    Glycogen Phosphorylase B;
3.40.50.720     NAD(P)-binding Rossmann-like Domain
3.40.640.10     Type I PLP-dependent aspartate aminotransferase-like (Major domain)
3.40.720.10     Alkaline Phosphatase, subunit A
3.90.1480.20    Glycosyl transferase family 29
3.90.76.10      Dipeptide-binding Protein; Domain 1
```

Ten superfamilies are reused across two or more condition sets, and the
same-superfamily neighbours frequently disagree about the biology:

- **3.40.640.10 (Type I PLP fold)** supplies CS18 (serine palmitoyltransferase 1),
  CS27 (serine palmitoyltransferase 2) **and CS37 (5-aminolevulinate synthase)**.
  SPT and ALAS are both α-oxoamine synthases. CS37 is not a random error: it is
  the rule reaching one fold too far and picking up the heme-biosynthesis branch
  of the same family. Its FunFam is even named "5-aminolevulinate synthase,
  **mitochondrial**" while the condition restricts to Bacteroidota.
- **3.60.21.10 (calcineurin-like metallophosphoesterase)** supplies CS19
  (sphingomyelin phosphodiesterase, catabolic), CS38 (LpxH, biosynthetic) and
  CS48 ("Putative metallophosphoesterase 1", unknown). One superfamily, three
  different answers to "does this make a membrane lipid?". If CS48 is in fact
  MPPE1/PGAP5 it is a GPI-*remodelling* enzyme, but the CATH name does not
  establish that, so it is counted here among the non-diagnostic conditions.
- **3.10.120.10 is the cytochrome b5-like domain**, not a catalytic domain. Both
  CS16 (FA2H) and CS30 (Δ8 desaturase) key on the fused electron-donor module
  that is shared by desaturases, hydroxylases and many unrelated b5-domain
  proteins. The catalytic di-iron histidine boxes are not part of the condition.
- **3.40.50.2000 ("Glycogen Phosphorylase B", the GT-B fold)** carries six
  condition sets (13, 14, 17, 32, 33, 34) spanning UDP-glucuronosyltransferases,
  mycobacterial PIM mannosyltransferases, a plastid galactolipid synthase and two
  FunFams whose CATH names are literally "Glycosyl transferase" and "Probable
  glycosyl transferase".
- **3.90.550.10 (GT-A fold)** carries another six (21, 23, 39, 40, 41, 50).
- **CS12** is 1.10.510.10 (protein-kinase catalytic domain) **AND** 2.30.29.30
  (PH domain) — a PH-domain-containing Ser/Thr kinase. There is no route from
  that architecture to lipid biosynthesis.
- **CS43** is 3.90.76.10, "Dipeptide-binding Protein; Domain 1" — a
  periplasmic-binding-protein-like fold. The condition's own label,
  "Monoacyl phosphatidylinositol tetramannoside-**binding** protein", says it is
  a lipid carrier, not a synthase.
- **CS44** ("sphingomyelin synthase-related protein 1") is assigned to
  1.10.150.50, "Transcription Factor, Ets-1" — a winged-helix superfamily. SMSr's
  catalytic domain is a lipid-phosphate-phosphatase-like fold. This is a partial
  or spurious domain assignment and should not be trusted as a condition.
- **CS8** ("Ceramide synthase 5") is assigned to 1.10.10.60, "Homeodomain-like".
  CerS2–6 genuinely carry an N-terminal Hox-like domain, so the FunFam is
  plausible — but the condition is keying on the homeobox, not on the TLC
  catalytic domain, which is a fragile basis for an enzymatic annotation.

---

## 4. Redundancy and taxonomic incoherence

**Redundancy.** KDSR is matched three times, by two different mechanisms:
CS4 (InterPro IPR002347 + IPR020904 + IPR045022), CS9
(3.40.50.720:FF:000165, Eukaryota) and CS36 (3.40.50.720:FF:000578,
Saccharomycotina) — the third being a subset of the second's taxon scope. DPM1 is
matched twice by two FunFams of one superfamily, CS23 (3.90.550.10:FF:000119) and
CS50 (3.90.550.10:FF:000036), both carrying the identical CATH label
"Dolichol-phosphate mannosyltransferase subunit 1". GPI ethanolamine-phosphate
transferases appear as CS22 and CS47, both in 3.40.720.10.

**Taxonomy.** The 39 taxon conditions name **34 distinct taxa**, and 12 of the 51
sets carry no taxon constraint at all. The scopes are not biological statements;
they read as fossils of wherever the training annotations happened to sit:

- `Homo` for sphingosine kinase 2 (CS31) and `Hominidae` for SPT2 (CS27) — both
  enzymes are pan-eukaryotic.
- `Glires` for B4GALT6 (CS21), `Euarchontoglires` for ST3GAL (CS3) and PNPLA1
  (CS25), `Primates` for the kinase (CS12).
- Against which, `Bacteria` (CS7, CS10) and `Eukaryota` (CS6, CS9) are wide open.

Neither direction is defensible. A `Homo`-scoped condition cannot be right if the
biology is conserved, and a `Bacteria`-scoped one cannot be right given that
lipid-A architecture is famously plastic across bacterial phyla. Taxon
constraints here are doing filtering work, not encoding phylogenetic judgment,
and in the CS37 case (`Bacteroidota` on a FunFam named "mitochondrial") they
actively conceal an error rather than catching it.

---

## 5. What the deep research adds, and where it needs correcting

The falcon deep-research pass
(`ARBA00028538-deep-research-falcon.md`, Edison Scientific, 2026-08-29, 21
citations) audited all 51 condition sets independently and reached a compatible
conclusion: *"the rule is not valid in its present OR-ed form"* and *"Because any
single condition triggers GO:0046467, the weakest condition determines the rule's
practical specificity."* It independently flagged CS12, CS26, CS37 and CS43 as
mechanistically unrelated, the five hydrolase sets as directionally wrong, CS6/33/51
as non-diagnostic, and CS23/CS50 as redundant — matching the structural analysis
above, which was derived from CATH superfamily membership rather than from
literature.

It also supplies the literature anchors this review relies on for direction. All
of these were resolved from DOI to PMID via NCBI esearch and cached in
`publications/` on 2026-08-29, and the quotes used in the review YAML were
checked verbatim against those cached files:

| claim | reference | cached |
|---|---|---|
| acid sphingomyelinase is a lysosomal/secretory phospholipase C for phospholipid **catabolism** | Breiden & Sandhoff 2021, doi:10.3390/ijms22169001 | PMID:34445706 (full text) |
| ceramidases "catalyze the degradation of ceramide to sphingosine" (ACER1-3, ASAH1, ASAH2) | Gomez-Larrauri et al. 2021, doi:10.3390/medicina57070729 | PMID:34357010 (full text) |
| LpxC "catalyzes the first committed step of LPS synthesis" | Möller et al. 2024, doi:10.1016/j.jbc.2024.107143 | PMID:38458396 (full text) |
| lipid A "anchors LPS to the outer membrane"; acyl-chain specificity varies between taxa | Xiao et al. 2017, doi:10.1016/j.cbpa.2017.07.008 | PMID:28942130 (full text) |
| GPI structure and insertion of its fatty chains into the outer leaflet | Kinoshita & Fujita 2016, doi:10.1194/jlr.r063313 | PMID:26563290 (abstract only) |
| FunFams give more precise annotation than other domain resources — but it is still a prediction | Das et al. 2015, doi:10.1093/bioinformatics/btv398 | PMID:26139634 (full text) |

The last of these is the right citation for the caveat that FunFam membership is
a hypothesis about function, not a measurement of it.

Four corrections and caveats:

1. **It did not know the term is obsolete.** The prompt supplied the stale label
   "membrane lipid biosynthetic process" from this repo's label cache, so the
   deep research reasoned about a live term throughout, and its section 3 recommends
   annotating specific children and letting *"GO's ancestor propagation to supply
   GO:0046467 where that ancestry is valid"*. That route no longer exists. This
   is the single most important thing the deep research gets wrong, and it is our
   input's fault, not the model's.
2. **Its removal list is internally inconsistent.** The executive summary says
   *"At least 12 conditions are strong candidates for removal: 2, 5, 6, 12, 15, 19,
   26, 31, 33, 37, 43, 45, 48, and 51 (14 conditions under a conservative audit)"* —
   it enumerates 14 while claiming 12, and the recommendation section then
   partitions the same sets differently. The individual per-set verdicts in its
   table are sound; the roll-up counts are not, and should not be quoted as
   statistics.
3. **The PNPLA1 citation is loose.** Grabner et al. 2022
   (doi:10.1021/jacs.1c10836) is about small-molecule inhibitors of lipolysis in
   human adipocytes; it is cited to support PNPLA1's ω-O-acylceramide synthase
   role in skin. The claim about PNPLA1 is standard, but that reference is not
   where to verify it.
4. **It missed the CS44 and CS8 fold mismatches** (Ets-1 winged-helix and
   homeodomain-like superfamily assignments), which only surface from CATH
   superfamily membership.

The deep research recommends deactivating and splitting the rule. Given the
obsoletion, splitting cannot be done by editing this rule's consequent — there is
nothing to edit it to that would be correct for more than a fraction of its
antecedents.

---

## 6. Recommendation

**DEPRECATE.** Specifically:

1. Retire ARBA00028538 rather than remapping its consequent to GO:0008610.
   Remapping would resurrect 9 sets that are false rather than merely vague, and
   would bury the rest under a term two levels too general to be useful.
2. Do not treat the go-annotation#5835 complaint as closed. The obsoletion of
   GO:0046467 removed this rule's output without addressing the reasoning that
   produced it, and the sibling rules named in that issue — ARBA00026302
   (GO:1901137) and ARBA00028351 (GO:0046474) — still make the same category
   error on the same *S. pombe* protein.
3. Re-derive, as separate pathway-scoped rules, only the condition sets whose
   family assignment is specific enough to name a product: sphingolipid/ceramide
   biosynthesis (GO:0030148, GO:0046513) from CS1, 4, 8, 9, 18, 27, 36;
   glycosphingolipid biosynthesis (GO:0006688) from CS13, 21, 40; lipid-A
   biosynthesis (GO:0009245) from CS7, 24, 38; GPI-anchor biosynthesis
   (GO:0006506) from CS22, 46, 47; dolichyl-phosphate-mannose biosynthesis
   (GO:0180047) from CS23 and CS50 merged. Everything else — the hydrolases, the
   generic glycosyltransferases, the kinase, PGK, ALAS and the lipid-binding
   protein — should be dropped, not re-pointed.
4. Refresh `rules/_labels.json` for obsoleted GO terms, and add an obsoletion
   check to rule enrichment. A rule whose consequent has been obsoleted should be
   flagged at sync time, not discovered by a curator noticing that annotations
   vanished.

Confidence in the DEPRECATE call is high (0.95). The obsoletion, the zero
annotation count, the modification date and the CATH superfamily assignments are
all directly observed from live APIs and reproducible from the script in
`scripts/`. The per-condition-set biology is a judgment call in maybe a dozen
borderline cases, but none of those cases changes the recommendation.
