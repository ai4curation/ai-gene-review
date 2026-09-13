# AKAP10 (D-AKAP2, O43572) — review notes

Working journal for the GO annotation review. Provenance is recorded inline as
`[PMID:xxxx "verbatim"]` or `[file:... "verbatim"]`.

## 1. Row accounting (done first, per the ADAMTSL5 lesson)

```
wc -l < genes/human/AKAP10/AKAP10-goa.tsv   -> 40  (1 header + 39 data rows)
grep -c '^- term:' AKAP10-ai-review.yaml     -> 39  (stub, before editing)
```

The stub did **not** under-seed this gene: 39 GOA rows, 39 stub entries, and the 23
`GO:0005515` rows are seeded one per partner rather than collapsed. Breakdown of the
23: 1 from PMID:20159461 (P00514), 21 from PMID:36115835, 1 from PMID:40205054
(Q15599). Reconciliation with the final file: 39 reviewed rows + 3 `NEW` proposals = 42
`existing_annotations` entries.

## 2. What the protein is

662 aa, one chain, no catalytic domain, no EC number. Architecture from UniProt's own
feature table:

- `[file:human/AKAP10/AKAP10-uniprot.txt "FT   TRANSIT         1..28"]` — mitochondrial
  transit peptide, evidence `ECO:0000255` (rule-based prediction, **not** measured).
- `[file:human/AKAP10/AKAP10-uniprot.txt "FT   DOMAIN          125..369"]` RGS 1 and
  `[file:human/AKAP10/AKAP10-uniprot.txt "FT   DOMAIN          379..505"]` RGS 2, both
  `ECO:0000255|PROSITE-ProRule:PRU00171`.
- `[file:human/AKAP10/AKAP10-uniprot.txt "FT   REGION          634..647"]` with
  `[file:human/AKAP10/AKAP10-uniprot.txt "FT                   /note=\"PKA-RII subunit binding\""]`
  — the A-kinase binding (AKB) segment.
- `[file:human/AKAP10/AKAP10-uniprot.txt "FT   HELIX           629..653"]` from PDB 3IM4.
- C-terminal `...TKL` class-I PDZ-binding motif (not in the FT table; established in the
  literature and removed in the ΔPDZ construct of PMID:19797056).

`[file:human/AKAP10/AKAP10-uniprot.txt "PE   1: Evidence at protein level;"]` — so this is
not a dark gene; it is a well-studied one with a thin GO record.

### The RII-binding amphipathic helix IS present and IS mapped

The brief asked specifically whether the anchoring helix is in the FT table. It is, twice
over: as a named `REGION` (634–647) and as an experimentally determined `HELIX` (629–653,
`ECO:0007829|PDB:3IM4`). UniProt also states the mechanism:
`[file:human/AKAP10/AKAP10-uniprot.txt "CC   -!- DOMAIN: RII-alpha binding site, predicted to form an amphipathic helix,"]`.

And the crystallised peptide is the **human** sequence, not an orthologue's — UniProt's
own cross-reference pins the chain to human residues 623–662:
`[file:human/AKAP10/AKAP10-uniprot.txt "DR   PDB; 3IM4; X-ray; 2.28 A; C=623-662."]` and
`[file:human/AKAP10/AKAP10-uniprot.txt "DR   PDB; 3TMH; X-ray; 3.80 A; D/H/L=623-662."]`.

## 3. Hazard 1 — was the PKA-anchoring claim MEASURED on the human protein?

Yes, three independent ways, and the first two are on human sequence:

1. **Crystal structure** of the human AKAP10 AKB helix bound to the PKA RIα D/D domain
   [PMID:20159461 "Here we have determined the structures of the RIalpha D/D domain alone and in complex with D-AKAP2."],
   with the affinity claim [PMID:20159461 "Dual-specific AKAP 2 (D-AKAP2) binds to the dimerization/docking (D/D) domain of both RI and RII regulatory subunits of PKA with high affinity."].
2. **Fluorescence anisotropy** against human PKA-RIα and PKA-RIIα
   [PMID:25097019 "To verify the validity of these newly predicted anchoring sites and their putative specificities, we used computational modeling approaches (HADDOCK), biochemical affinity studies (fluorescence anisotropy), and cellular colocalization studies."].
   These are the GOA `GO:0051018` IPI rows (P10644 = human PRKAR1A, P13861 = human PRKAR2A).
3. A **ternary structure** with PKA-RII and PDZK1
   [PMID:25348485 "Here, we describe a structure of D-AKAP2 in complex with two interacting partners and the exact mechanism by which a segment that on its own is disordered presents an α-helix to PKA and a β-strand to PDZK1."].

The originating 1997 paper was mouse work — the full-length clone came from a mouse testis
library [PMID:9326583 "cDNA cloning from a mouse testis library identified the full length D-AKAP2."]
— but the human full-length protein was cloned and characterised in 2001
[PMID:11248059 "Here, we report the cloning of full-length human D-AKAP2 (662 residues) with an additional putative RGS domain, and the corresponding mouse protein less the first two exons (617 residues)."].

**Verdict: the name is earned.** No AGFG1/AGT-style retitling is warranted. What *is*
wrong is the precision of the term: GOA says `GO:0051018 protein kinase A binding`, while
every experiment measured binding to the **regulatory** subunit D/D domain, never the
catalytic subunit. `GO:0034237 protein kinase A regulatory subunit binding` is an active
`is_a` child of `GO:0051018` (verified via QuickGO, `isObsolete: false`, no secondaryIds)
and is the correct term. That drives three `MODIFY` actions.

## 4. Hazard 3 — the RGS domains. Hypothesis NOT confirmed, in both directions

An RGS domain implies Gα GAP activity. Two questions: is it annotated, and is it real?

**Is it annotated?** No. There is no `GO:0005096`, no `GO:0001965`, no
`GO:0031267`-via-Gα, and no G-protein BP row anywhere in the 39-row GOA. So the predicted
defect simply is not present — reported as a **non-confirmation**, exactly as ADAMTSL5 did,
not manufactured into a finding.

**Is it real?** No, and three independent lines say so.

- The original describers already flagged it as divergent:
  [PMID:9326583 "Surprisingly, not all of the charged residues conserved in RGS proteins reported so far were conserved in D-AKAP2."]
  and [PMID:9326583 "The lack of conservation of these charge residues suggests that if D-AKAP2 is a functional RGS, it may not interact with Giα as most of the known RGSs do, but with other Gα isoforms."].
  The domain assignment itself was homology-only:
  [PMID:9326583 "Surprisingly, however, residues 70–215 showed homology to the RGS domain found in RGS proteins."].
- Twelve years later the same lab states the negative outright:
  [PMID:19797056 "D-AKAP2 has so far demonstrated no specific interactions with heterotrimeric G proteins, and no ability to activate them, raising the possibility of nontraditional targets."].
- **Residue measurement** (`AKAP10-bioinformatics/rgs_gap_residues.py`, reproducible):
  both AKAP10 RGS domains retain **0 of 5** RGS4 Gα transition-state contacts
  (S85/E87/N88/N128/R167), scoring exactly like the AXIN1 negative control (0/5, an RGS
  fold that is not a Gα GAP) and unlike the RGS16 and RGS9 positive controls (5/5 each).
  The decisive asparagine — RGS4 N128, whose N128A abolishes GAP activity — aligns to
  **Pro315** in RGS-A and **Gly452** in RGS-B.

  Caveat kept in the report rather than hidden: RGS-B sits at 24.3% identity, below the
  range where a residue call is safe on alignment alone (the AADACL2 lesson). RGS-A at
  30.3% is directly comparable to AXIN1 at 31.5%, and N128→Pro is independently
  disruptive. The computation corroborates the two published statements; it does not
  carry the claim by itself. Both of the script's guards were tested by deliberately
  breaking them (mutating the site table, and pointing a "positive control" at
  haemoglobin alpha) and both aborted the run.

**What the RGS domains actually do** is bind small GTPases, which GO does not record at
all — see §6.

## 5. Hazard 2 — dual localisation, and the I646V variant

Three claims kept strictly apart.

**Where it is.** Genuinely contested, and the contradiction is the deliverable.
- For mitochondria: human endogenous protein
  [PMID:11248059 "Subcellular localization for endogenous mouse, rat, and human D-AKAP2 was determined by immunocytochemistry, immunohistochemistry, and tissue fractionation. D-AKAP2 from all three species is highly enriched in mitochondria."],
  plus the independent MitoCoP high-confidence human mitochondrial proteome (PMID:34800366,
  the GOA `HTP` row), plus mouse Akap10 IDA + 5 HDA rows.
- Against: the same laboratory eight years later, in HeLa,
  [PMID:19797056 "Cell fractionation showed that endogenous D-AKAP2 is almost entirely cytosolic"],
  [PMID:19797056 "D-AKAP2 showed very little colocalization with markers of the endoplasmic reticulum, the Golgi complex, lysosomes, peroxisomes, or mitochondria"],
  and they say so explicitly: [PMID:19797056 "D-AKAP2 was suggested previously to localize partially to mitochondria"] —
  attributing the difference to antibody cross-reactivity or cell type.
- The transit peptide that gives the protein its UniProt name is a *prediction*
  (`ECO:0000255`), not a measurement, and there is no TM segment and no lipid-binding
  domain anywhere in the entry — so how AKAP10 attaches to any membrane is unresolved.
  PMID:25348485 states the point for the PDZ route:
  [PMID:25348485 "In contrast to many other AKAPs, D-AKAP2 does not interact directly with the membrane protein."]

Both localisations are annotated and both are kept. Cytosol has its own human IDA (HPA)
and is corroborated by the 2009 fractionation; mitochondrion has an independent human HTP
row that does not depend on the disputed antibody. Recorded as an open knowledge gap.

**What the variant associates with.** `I646V` (`rs203462`, ~40% of alleles) is a
population association with heart-rate phenotypes
[PMID:17485678 "We also found that a common variant of AKAP10 in humans (646V, 40% of alleles) was associated with increased basal heart rate and decreased heart rate variability (markers of low cholinergic/vagus nerve sensitivity)."].
The mouse allele is a C-terminal gene trap that the authors themselves read as
**dominant-interfering**
[PMID:17485678 "In both heterozygous and homozygous mutant mice derived from these mESCs, the same Akap10 disruption increases the cardiac response to cholinergic signals, suggesting a dominant interfering effect of the Akap10 mutant allele."],
so it is not a clean loss of function for the wild-type protein, and the authors close with
[PMID:17485678 "Although the molecular mechanism remains unknown, our findings in mutant mESCs, mice, and a common human AKAP10 SNP all suggest a role for AKAP10 in heart rhythm control."].

GOA carries **no** cardiac term on human AKAP10 and **none is proposed here**: an
association is not a BP of the wild-type protein, the perturbation was in mouse (so the
code would be ISS/ISO at best), and the allele is dominant-interfering. Second predicted
defect that is simply absent — reported as such.

Worth noting for anyone reading PMID:19797056: every construct in it carries the variant
[PMID:19797056 "All D-AKAP2 constructs used the human gene with valine at position 646."],
i.e. the endocytic-recycling function was characterised on the 646V form.

## 6. The finding: an entire measured function is missing from GO

`PMID:19797056` establishes that AKAP10's tandem RGS domains bind Rab4 and Rab11 and that
the protein sets the rate of transferrin-receptor recycling. **QuickGO returns zero
annotations for `reference=PMID:19797056` across all of GOA** — not on AKAP10, not on Rab4,
Rab11 or TFRC, not on any gene in any species. A 17-year-old *JBC* paper with a
first-of-its-kind result has produced no GO annotation anywhere.

The experiments, all on the human protein in human cells:
- [PMID:19797056 "We show here that these RGS domains interact with Rab11 and GTP-bound Rab4, the first demonstration of RGS domains binding small GTPases."]
- [PMID:19797056 "D-AKAP2 specifically co-immunoprecipitated GFP-tagged Rab4 and Rab11 but not Rab5."] (HEK293)
- [PMID:19797056 "Furthermore, purified GST-tagged Rab4 bound to the nonhydrolyzable nucleotide analog GTPγS was much more able to pull down D-AKAP2 from a HEK293 lysate than GDP-bound GST-Rab4 or GST alone"] — nucleotide-state dependence.
- [PMID:19797056 "The tandem RGS domains (residues 120–513) were necessary and sufficient for this colocalization"] and
  [PMID:19797056 "Neither RGS-A (residues 120–369) nor RGS-B (residues 374–513) alone was able to interact with Rab4 or Rab11, suggesting that the two RGS domains form a single functional unit."]
  — the binding surface is mapped, and it is the two RGS domains acting as one unit.
- [PMID:19797056 "Endogenous D-AKAP2 also clearly colocalized with GFP-Rab4 and mCh-Rab11 on endosomes, with an apparent preference for endosomes positive for both Rab proteins"]
  and [PMID:19797056 "D-AKAP2 in these puncta colocalized significantly with internalized fluorescently labeled transferrin, a marker of the endocytic recycling pathway"].
- siRNA in HeLa [PMID:19797056 "Treating HeLa cells for 2 days with siRNA directed against D-AKAP2 effectively knocked down nearly all of the endogenous protein"]
  gives [PMID:19797056 "Fitting all of the data to an exponential decay function yielded a rate of transferrin recycling that was 73 ± 21% faster in the D-AKAP2 knockdown cells than in control cells"]
  and [PMID:19797056 "These results suggest that endogenous D-AKAP2 may promote the accumulation of transferrin in the slow recycling pathway of the Rab4/Rab11-containing ERC."].

**Direction check** (the GO:2000738 trap): knockdown makes recycling *faster*, so the
wild-type protein *slows* it → `GO:2001136 negative regulation of endocytic recycling`,
verified active, definition "Any process that stops, prevents or reduces the frequency,
rate or extent of endocytic recycling." Not the positive-regulation term.

**Term check for the Rab binding.** `GO:0017137 Rab GTPase binding` has been **merged into
`GO:0031267 small GTPase binding`** — QuickGO lists `GO:0017137` among `GO:0031267`'s
`secondaryIds`, and `GO:0031267` has zero children. So `GO:0031267` is already maximal and
no substrate-specific child should be proposed (the brief's ACAP2 lesson). Recorded
machine-readably with `extensions` / `has_input` instead.

Three `NEW` rows follow: `GO:0031267` (IPI), `GO:2001136` (IMP), `GO:0055037 recycling
endosome` (IDA).

## 7. What the 23 `protein binding` rows actually are

Resolved every accession (`Swiss-Prot` status printed for each, `startswith("UniProtKB reviewed")`
so "unreviewed" cannot masquerade): **25/25 reviewed Swiss-Prot, 0 TrEMBL**, all canonical
lengths, no ORFeome fragments. 23 human, 1 mouse (O88845), 1 bovine (P00514).

IntAct expansion (222 records, pagination asserted complete) gives the method breakdown,
which is far more informative than UniProt's `NbExp`:

| method | rows |
|---|---|
| holdup assay | 124 |
| tap | 68 |
| anti tag coip | 22 |
| two hybrid array | 2 |
| clash | 2 |
| x-ray diffraction | 1 |
| fluorescence spectr | 1 |
| 2h fragment pooling | 1 |
| two hybrid pooling | 1 |

Per partner:
- **P00514** (bovine PKA RIα; `Xeno` in UniProt's own INTERACTION block): x-ray
  diffraction + fluorescence spectroscopy — the 3IM4 structure. → `GO:0034237`.
- **21 partners from PMID:36115835**: holdup assay only, 2–9 rows each. Those counts are
  replicate holdup measurements, not independent experiments (the `NbExp` trap again:
  PATJ's "NbExp=9" is nine holdup rows). Every one of the 21 is a **PDZ-domain protein**,
  and the assay is a proteome-scale PBM-versus-PDZ affinity survey
  [PMID:36115835 "Here, we measure the affinities of 65,000 interactions involving PDZ domains and their target PDZ-binding motifs (PBM) within a human interactome region particularly relevant for viral infection and cancer."].
  So what was measured is not "AKAP10 binds protein X" but "AKAP10's PBM binds a PDZ
  domain" → `GO:0030165 PDZ domain binding`, verified active, no children.
- **Q15599** (NHERF2) is the only PDZ partner with an orthogonal cellular method:
  `anti tag coip` (PMID:40205054) **plus** holdup.
- **Q5T2W1** (PDZK1) is holdup-only in IntAct but has the strongest independent biology:
  [PMID:14531807 "In pull-down experiments, D-AKAP2 tightly bound PDZK1 as well as N+/H+ exchanger regulator factor (NHERF-1), but the latter with an apparent fourfold lower affinity."],
  recruitment of FLAG-PDZK1 to Rab11 endosomes by mCherry-D-AKAP2 in HeLa (PMID:19797056,
  abolished in the ΔPDZ construct), and the ternary crystal structure PMID:25348485.
- **P13861** (human PRKAR2A) has **no** IntAct row — its `GO:0051018` IPI comes from
  UniProt's curation of PMID:25097019 directly.

Note a name trap: the 2003 paper's second partner is **NHERF-1** (`SLC9A3R1`, O14745),
which is *not* in GOA. The GOA partner `Q15599` is **NHERF2** (`SLC9A3R2`). Affinage's
narrative says "NHERF-1"; the annotation says NHERF2. They are different proteins and are
kept apart here.

## 8. PAINT: one node, three terms, and a reciprocal defect

`PTHR13155` "Cell Polarization and PKA Anchoring", InterPro metadata `proteins: 3775`.
The cached entries CSV holds **6 reviewed (Swiss-Prot) members — 0.16% of the family**, and
all six sit in one subfamily, `PTHR13155:SF1`, named
`[file:human/AKAP10/AKAP10-uniprot.txt "DR   PANTHER; PTHR13155:SF1; A-KINASE ANCHOR PROTEIN 10, MITOCHONDRIAL; 1."]`:

| accession | gene | organism | length | what it is |
|---|---|---|---|---|
| O43572 | AKAP10 | human | 662 | AKAP |
| O88845 | Akap10 | mouse | 662 | AKAP |
| P57770 | AKAP10 | pig | 650 | AKAP |
| Q08760 | RAX1 | *S. cerevisiae* | 435 | bud site selection protein |
| Q10955 | rgs-5 | *C. elegans* | 492 | RGS protein |
| Q9P7S8 | rax1 | *S. pombe* | 343 | bud site selection protein |

`PTHR13155-paint.tsv` shows a single node, `PTN001775426`, asserting exactly three terms —
`GO:0005739` (seed `MGI:MGI:1890218`), `GO:0043495` (seed `MGI:MGI:1890218`) and
`GO:0008104` (seeds `MGI:MGI:1890218` + `SGD:S000005827`).

**Donor evidence, queried rather than assumed.** `MGI:MGI:1890218` returns **two**
accessions, not one (the `size=1` trap): `O88845` AKA10_MOUSE, Swiss-Prot, 662 aa — the
true 1:1 orthologue — and `Q3TR91`, TrEMBL, 343 aa, a fragment carrying zero annotations
for any of the three terms. The orthologue carries its own experimental evidence for all
three: `GO:0005739` IDA + 5 HDA, `GO:0043495` IDA, `GO:0008104` IDA, all traceable to
PMID:11248059. `SGD:S000005827` resolves to `Q08760` RAX1_YEAST, Swiss-Prot, 435 aa, with
`GO:0008104` IMP ×2 from PMID:25416945. So every protein-level donor carries real
experimental evidence — `SOURCE_WEAK_OR_INFERRED` would be factually wrong here.

**The reciprocal half (the `blow` pattern).** The node's `GO:0005739 mitochondrion` is
seeded by mouse Akap10 alone, yet it lands on all six members — including the two fungal
Rax1 proteins, whose own experimental localisations contradict it:

| member | `GO:0005739` | own experimental CC |
|---|---|---|
| *S. cerevisiae* RAX1 | IBA `is_active_in` | cellular bud neck IDA, cellular bud scar IDA, plasma membrane EXP, cellular bud tip EXP, fungal-type vacuole HDA |
| *S. pombe* rax1 | IBA `is_active_in` | endoplasmic reticulum HDA |
| *C. elegans* rgs-5 | IBA `is_active_in` | none |

So a plasma-membrane bud-site-selection protein with five experimental localisations, none
of them mitochondrial, is asserted to be *active in* mitochondria because a mouse AKAP is.
That is a PAINT node-placement problem, not an AKAP10 problem: the human row is
independently supported and stays. Stated once in `suggested_questions` with all affected
genes named.

**And the general term that is correct.** `GO:0008104 intracellular protein localization`
looks vague, but its two donors are an AKAP that localises PKA and a yeast protein that
localises cortical bud-site landmarks. Those are genuinely different biologies whose least
common ancestor *is* "intracellular protein localization". This is the AADACL4 case:
heterogeneous donors make the general term the right call, and `GRANULARITY_MISMATCH` does
not apply. ACCEPT, do not try to specialise.

## 9. Projection check (QuickGO by reference)

| reference | annotations | distinct entities | reading |
|---|---|---|---|
| PMID:9326583 | 4 | 2 | fine |
| PMID:11248059 | 3 | 1 | fine — mouse Akap10 only |
| PMID:25097019 | 26 | 8 | `GO:0032991` IDA given to **all 8** AKAPs in the study |
| PMID:20159461 | 3 | 2 | fine |
| PMID:19797056 | **0** | **0** | the coverage defect above |
| PMID:34800366 | 1235 | unavailable | paginated; projection test not run |
| PMID:36115835 | 18539 | unavailable | paginated; projection test not run |
| PMID:40205054 | 3026 | unavailable | paginated; projection test not run |

For the three large references the honest output is "entity counts unavailable", recorded
rather than substituted with the annotation total (the ACTRT3 lesson). The `GO:0032991`
result *is* the projection shape — one term, one evidence code, every entity in the study —
but it is benign: each AKAP in that paper was individually assayed, so this is parallel
per-protein curation, not a phenotype distributed with membership. The term is kept and
demoted on informativeness, not on provenance.

## 10. Retraction / erratum sweep

All 12 cited PMIDs checked via `CommentsCorrections/RefType` on each article's own PubMed
record (a Publisher Correction is not findable by a publication-type search — the ACTR8
lesson). No retractions, no expressions of concern. Two errata:

- `PMID:36115835` → `PMID:36477203`, an Author Correction covering *"errors in Fig. 2,
  Fig. 4 and Fig. 5"* — missing PCC values, absent axis labels, panel ordering. No affinity
  measurement or PDZ datum is affected.
- `PMID:40205054` → `PMID:41039152`, a Publisher Correction fixing duplicated variable
  names in the fourth "Loss functions" equation in Methods. No interaction or AP-MS datum
  is affected.

Neither bears on any claim used here, but both are flagged in `reference_review`.

## 11. Reactome compartment check

The `GO:0005829 cytosol` TAS row cites `Reactome:R-HSA-992708`, which the cached entry
shows is *"Dual-specific AKAPs bind type I and II PKA regulatory subunits"* — a **binding
reaction**, whose `[cytosol]` tag is the reaction's compartment, not a measurement of where
AKAP10 is (the AHI1 lesson). Unlike AHI1, however, the term survives on independent
grounds: an HPA immunofluorescence IDA in human cells and endogenous cell fractionation in
PMID:19797056. So the check came back "weak provenance, corroborated conclusion" — the row
is kept, demoted rather than removed. A negative result from a check is still a result.

## 12. Affinage assessment

`gates_passed`: the run reported *"AKAP10: trust gates clear"*; the record's frontmatter
carries `faith_pct: 100.0` and 8 citations, **all numeric PMIDs** (no `PMID:bio_*` preprint
ids). Recall was good on this gene: the record surfaced PMID:19797056, PMID:25348485,
PMID:12206784, PMID:14531807, PMID:17485678 and PMID:11248059, i.e. **6 references absent
from GOA**, including the decisive one. That is better than the campaign's 52% average and
worth recording, since recall is only ever measured by someone writing it down.

Two things it got wrong or under-specified, neither imported:
- It reports the PDZ partner as "NHERF-1"; the GOA partner is **NHERF2** (see §7).
- It describes the Rab work without noting that every construct carried the 646V variant.

Per the campaign rule, no affinage sentence is used as `supporting_text` for a mechanistic
claim; each lead was re-verified against the PMID or against UniProt before use.

## 13. Actions, in one table

| term | evidence | action | why |
|---|---|---|---|
| `GO:0005515` ×1 (P00514, PMID:20159461) | IPI | MODIFY → `GO:0034237` | crystal structure of the human AKB helix on the RIα D/D domain |
| `GO:0005515` ×21 (PMID:36115835) | IPI | MODIFY → `GO:0030165` | holdup affinity of the AKAP10 PBM against purified PDZ domains |
| `GO:0005515` ×1 (Q15599, PMID:40205054) | IPI | MODIFY → `GO:0030165` | AP-MS co-complex, mechanism supplied by the holdup measurement |
| `GO:0051018` ×3 | IEA, IPI, IPI | MODIFY → `GO:0034237` | only the R subunit was ever assayed |
| `GO:0043495` IBA | IBA | ACCEPT | mouse orthologue IDA; the anchoring function itself |
| `GO:0043495` IEA | IEA | KEEP_AS_NON_CORE | same donor, same evidence as the IBA |
| `GO:0005739` HTP | HTP | ACCEPT | MitoCoP, human, independent of the disputed antibody |
| `GO:0005739` IBA | IBA | ACCEPT | right for human; node placement flagged separately |
| `GO:0005739` IEA | IEA | KEEP_AS_NON_CORE | redundant |
| `GO:0005829` IDA (HPA) | IDA | ACCEPT | human immunofluorescence + 2009 fractionation |
| `GO:0005829` TAS (Reactome) | TAS | KEEP_AS_NON_CORE | reaction compartment, not a measurement |
| `GO:0005737` IEA | IEA | KEEP_AS_NON_CORE | parent of a term with its own IDA |
| `GO:0016020` IEA | IEA | KEEP_AS_NON_CORE | no TM, no lipid-binding domain; attachment unresolved |
| `GO:0032991` IDA | IDA | KEEP_AS_NON_CORE | true but root-level; GO has no apt child |
| `GO:0008104` IBA | IBA | ACCEPT | LCA of heterogeneous donors — correct as-is |
| `GO:0008104` TAS | TAS | KEEP_AS_NON_CORE | 1997 paper measured binding, not localisation |
| `GO:0007165` TAS | TAS | MARK_AS_OVER_ANNOTATED | BP root; its rationale was the RGS speculation §4 refutes |
| `GO:0031267` | IPI | **NEW** | tandem RGS domains bind Rab4/Rab11 |
| `GO:2001136` | IMP | **NEW** | siRNA → 73% faster transferrin recycling |
| `GO:0055037` | IDA | **NEW** | endogenous protein on Rab4/Rab11 endosomes |

No `REMOVE`. Nothing in this record is demonstrably wrong; the defects are precision
(`protein binding` ×23, `protein kinase A binding` ×3, `signal transduction`) and
**coverage** (an entire measured function missing). That is the AFF4 diagnosis, not the
over-annotation one, and the review says so.

## 14. Checked and NOT acted on

Recording the nulls so the next reviewer knows these were run:

- No Gα GAP annotation exists to remove (§4).
- No cardiac/heart-rhythm annotation exists to remove (§5).
- No paralogue review exists in this repo to cross-check against (`genes/human/AKAP*`
  contains only AKAP10), so the sibling-consistency check could not be run.
- `GO:0010738 regulation of protein kinase A signaling` was considered as a replacement for
  `GO:0007165` and is **obsolete** — checked before proposing, so no replacement is offered.
- `GO:0005952 cAMP-dependent protein kinase complex` was considered as a replacement for
  `GO:0032991` and is defined strictly as the R₂C₂ holoenzyme, which AKAP10 is not part of.
  It has no children. No apt term exists; the row stays at the root.
- An OLS search for `AKAP` and for `A-kinase anchoring protein complex` returns **nothing**
  in GO. Searching is token-based and a null search is not proof of absence, so this is
  recorded as an observation for GO in `suggested_questions`, not as a `proposed_new_terms`
  entry.

## 15. One validation warning is left standing, deliberately

`just validate human AKAP10` reports `✓ Valid (with 1 warnings)`:

> `No annotations reference available deep research files (AKAP10-deep-research-affinage.md)`

It is not silenced. The warning wants a `supported_by` entry inside an annotation citing the
provider record, and the campaign's standing rule is that a provider sentence is a **lead,
not evidence** — quoting one as `supporting_text` for a mechanistic claim is how the ACBD3
domain error propagated into seven places. The provider's assessment belongs in
`references[].reference_review`, which is where it is, together with the two defects found in
it (§12). Inventing an annotation-level citation to clear a warning would be exactly the
"do NOT invent content to silence them" failure.

## 16. A committed claim lint, and the self-test that was initially fake

`AKAP10-bioinformatics/audit_akap10_claims.py` re-derives every number asserted in the PR
body from the review file itself, matches each GOA row to an `existing_annotations` entry by
(term, evidence, reference, WITH/FROM), reconciles raw against parsed `supporting_text`
counts through a duplicate-key-rejecting loader, and enforces four claim-level invariants
stated over the **class** of error rather than a list of sites:

- no forbidden term id anywhere in the document (`GO:0005096` GAP activity, `GO:2001137` the
  inverted direction, `GO:0010738` obsolete, `GO:0017137` merged);
- no `proposed_replacement_terms` pointing back at the parent it moves away from;
- no experimental evidence code on a row citing a reference whose experiments were done in
  another organism;
- no `supported_by` citing a reference that is not declared.

`--self-test` breaks each one and requires the audit to notice. **It found a defect in
itself.** The first version of the "inject a GAP term" mutation edited an
`existing_annotations` term id — and was caught by the *coverage* check, not by the
forbidden-term check. The guard under test was never exercised, and the self-test still
printed green. Moving the injection into `core_functions`, where no other check can see it,
is what made the test real. Exactly the AHI1 pattern: a passing self-test proves the guards
you thought of fire, and says nothing about the one you failed to write.

## 17. Tooling note: the pre-write hook validates against the WRONG repo root

Worth recording because it cost a round and would mislead any agent working in a worktree.
`.claude/hooks/validate_ai_review_pretool_hook.py` computes
`project_root = Path(__file__).parent.parent.parent` and runs the validator with that as
`cwd`, on a copy of the YAML in a **temp directory**. Two consequences:

1. `file:` references resolve against the *main checkout*, not the worktree. It reported
   `File reference points to non-existent file: human/AKAP10/AKAP10-bioinformatics/RESULTS.md`
   for a file that exists. `/Users/cjm/repos/ai-gene-review/genes/human/AKAP10` does not exist
   at all — the whole gene folder is worktree-only.
2. Quote validation runs against the main checkout's `publications/` cache, which lacks the
   PMIDs this branch fetched, so the validator **re-downloads** them and checks against
   whatever it gets. That produced one spurious `Text part not found` on a quote that is
   verbatim in the cached full text.

Same class as the `checkquotes.py` hardcoded-root incident: a confident wrong answer, and the
natural response (deleting the reference, rewriting the quote) would corrupt correct work.
**Trust `just validate <org> <gene>` run from the worktree root** — that resolved everything
correctly and reports `✓ Valid`. The one substantive thing the hook did catch was real: three
`statement:` strings contained `": "` inside plain YAML scalars, which is a parse error.
