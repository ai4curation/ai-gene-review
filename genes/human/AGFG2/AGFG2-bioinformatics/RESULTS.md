# AGFG2 (O95081) — computed analyses supporting the GO annotation review

All numbers below are produced by the scripts in this directory and written to the
adjacent JSON files. Nothing is hand-entered. Re-run with the repo virtualenv:

```
python resolve_withfrom.py     # withfrom.json      — WITH/FROM provenance + donor evidence
python node_reach.py           # node_reach.json    — what each PAINT node donates, to whom
python arfgap_domain.py        # arfgap_domain.json — catalytic-site residues + identity
python provenance_checks.py    # provenance.json    — reference projection, InterPro2GO, family census
python term_checks.py          # term_checks.json   — every term-level fact the review leans on
python distribution.py         # distribution.json  — clade distribution + node taxon breadth
python litsearch.py            # litsearch.json     — recorded PubMed queries + retraction checks
python intact.py               # intact.json        — interaction records, partners, methods
python audit_claims.py         # gates every claim in this file against the review YAML
```

`mafft` (v7, `--localpair --maxiterate 1000`) is the only external binary.

---

## 1. Row/annotation reconciliation

`AGFG2-goa.tsv` has **7** data rows (8 lines including the header), all 7 distinct.
The `fetch-gene` stub seeded **7** `existing_annotations` entries. The counts
reconcile exactly; no `GO:0005515` or same-term/different-assigner collapse occurred
on this gene, so no rows had to be restored.

## 2. The catalytic question: two residues, opposite answers

The gene name asserts an "Arf-GAP domain". Testing only the catalytic arginine gives
the opposite conclusion from testing both residues that the field identifies as
required, so both are measured.

**The two positions are located by two different methods, and only one is a
derivation.** Both are gated by a literature anchor, but the gates are not equivalent
and the table says which is which:

| residue | method | literature anchor | result |
|---|---|---|---|
| catalytic Arg | **derived** from the consensus `C-x2-C-x16-C-x2-C-x4-R`, located by regex inside each protein's own UniProt-annotated zinc finger | PMID:34369554 names `AGFG2[R75Q]` as its GAP-dead mutant, i.e. 75 | derivation returns **75** — reproduces the literature number |
| Arf-contacting Asp | **asserted, not derived**: the position is an input constant (`ASP_CONTROL = ("Q8TDY4", 484)`), then transferred to every other protein by MAFFT alignment column | PMID:23433073 names `D484` in the ASAP3 structure | residue at 484 verified as **D**, inside the annotated domain, and its alignment column holds `D` for ASAP3 |

Only the first row reproduces a literature number from an independent computation. The
second verifies an asserted number and transfers it; the script raises if the residue is
not an Asp, if it falls outside the annotated Arf-GAP domain, or if ASAP3 and AGFG2 fail
to co-align at the catalytic arginine.

Result over the annotated Arf-GAP domains (all Swiss-Prot except drongo):

| accession | protein | subfamily | catalytic Arg | Arf-contacting Asp |
|---|---|---|---|---|
| O95081 | human AGFG2 | AGFG | **R75 present** | **Thr89 — absent** |
| P52594 | human AGFG1 | AGFG | R57 present | Thr71 — absent |
| Q80WC7 | mouse Agfg2 | AGFG | R75 present | Thr89 — absent |
| Q8K2K6 | mouse Agfg1 | AGFG | R57 present | Thr71 — absent |
| E1JHR0 | *Drosophila* drongo (TrEMBL) | AGFG | R58 present | Ala72 — absent |
| Q8N6T3 | ARFGAP1 | ArfGAP1 | R50 present | **D65 present** |
| Q9ULH1 | ASAP1 | ASAP | R482 present | **D497 present** |
| Q8TDY4 | ASAP3 | ASAP | R469 present | **D484 present** (control) |
| Q8IYB5 | SMAP1 | SMAP | R61 present | **D76 present** |

Every derived arginine falls in the same alignment column, so the comparison is
reciprocally anchored rather than resting on residue identity alone.

**The panel discriminates perfectly on the aspartate: 5/5 AGFG proteins lack it, 4/4
non-AGFG ArfGAPs have it.** SMAP1 is the strongest internal control — it is the *other*
hit from the same siRNA screen in PMID:34369554, and it keeps the aspartate.

This reproduces, by an independent method and for human AGFG2 specifically, what
PMID:23433073 reports for the subfamily: only two of forty AGFG sequences retain that
aspartate, and the subfamily "*is predicted to have lost substantial levels of GAP
activity*". That paper's own suggestion is that AGFG proteins are Arf **effectors**
rather than GAPs.

**A refuted assumption, kept on the record.** An earlier version of this script placed
the aspartate at a fixed offset (the second of the four residues between the fourth
cysteine and the arginine). Its own control refused that: ASAP3 gave position 466, not
484. The aspartate is 15 residues C-terminal of the arginine *in ASAP3*, and indels move
it between subfamilies, so alignment transfer is the only sound method. `probe_asap3.py`
records the measurement that settled it.

**What is NOT shown here.** No GAP activity measurement exists for any AGFG protein
(section 6). An intact arginine licenses "untested", not "active"; a missing aspartate
licenses "predicted to have lost", not "measured inactive".

## 3. Paralogy, orthology, and which one PAINT used

| vs human AGFG2 | full-length identity | Arf-GAP domain identity | PANTHER subfamily |
|---|---|---|---|
| mouse Agfg2 (Q80WC7) | **83.2 %** | 97.6 % | PTHR46134:SF4 — same as AGFG2 |
| human AGFG1 (P52594) | 47.6 % | 71.2 % | PTHR46134:SF1 |
| mouse Agfg1 (Q8K2K6) | **46.5 %** | 71.2 % | PTHR46134:SF1 |
| *Drosophila* drongo (E1JHR0) | 26.6 % | 51.6 % | — |
| SMAP1 (Q8IYB5) | 21.2 % | 25.4 % | — |
| ARFGAP1 (Q8N6T3) | 20.6 % | 25.5 % | — |

So AGFG1 and AGFG2 are genuine paralogues — same PANTHER family `PTHR46134`, different
subfamilies, ~48 % identity, both carrying the ArfGAP + FG-repeat architecture — which
is the claim their shared name only implies. PMID:23433073 reaches the same conclusion
phylogenetically: AGFG is one of four subfamilies that "*have each undergone a single
duplication resulting in two paralogs*".

**The negative control is the finding.** Mouse *Agfg2* exists, is Swiss-Prot reviewed,
sits in the same PANTHER subfamily as human AGFG2, and is **36 percentage points closer
to it than mouse Agfg1 is** — and it appears in *none* of AGFG2's WITH/FROM fields. Every
IBA row on AGFG2 is seeded from the paralogue's mouse orthologue while the gene's own
mouse orthologue is unused.

## 4. WITH/FROM provenance and each donor's own evidence

Six distinct WITH/FROM tokens across the 7 GOA rows; **zero unresolved**. QuickGO
positive control (`UniProtKB:P52594` / `GO:0001675`) returned a non-zero result, so the
zeros below are real zeros and not rejected queries.

| GO term | evidence | protein donors with their OWN experimental annotation to this term |
|---|---|---|
| GO:0005737 cytoplasm | IBA | drongo IDA (`PMID:27654348`); mouse Agfg1 and human AGFG1 hold only the descendant GO:0031410 |
| GO:0031410 cytoplasmic vesicle | IBA | mouse Agfg1 IDA (`PMID:11711676`); human AGFG1 EXP (`PMID:10613896`) |
| GO:0001675 acrosome assembly | IBA | mouse Agfg1 IMP ×2 (`PMID:11711676`, `PMID:14724135`) — **sole source** |
| GO:0007289 spermatid nucleus differentiation | IBA | mouse Agfg1 IMP (`PMID:16765935`) — **sole source** |
| GO:0045109 intermediate filament organization | IBA | mouse Agfg1 IMP (`PMID:14724135`) — **sole source** |
| GO:0005096 GTPase activator activity | IEA | none — the token is `InterPro:IPR001164`, a signature, not a protein |
| GO:0016020 membrane | HDA | no WITH/FROM |

Resolver notes reported rather than hidden:

- `FB:FBgn0020304` (drongo) resolves to **7 UniProt entries, 0 of them reviewed**. Its
  GO:0005737 IDA is therefore real curated evidence attached to a TrEMBL entry; the
  entry's *name* carries no Swiss-Prot authority.
- `MGI:MGI:1333754` resolves to 5 mouse *Agfg1* entries, 1 reviewed (`Q8K2K6`). All
  candidates were queried, not one picked by `size=1`.
- `PANTHER:PTN…` tokens are tree nodes, not proteins — unresolvable and not-a-protein are
  different facts.

## 5. Which node reaches which genes, and what it gives them

| node | annotations | gene products | human recipients | terms donated |
|---|---|---|---|---|
| `PTN002353603` | 87 | 66 | AGFG1, AGFG2 (only) | GO:0005737 (66), GO:0016020 (21, no human) |
| `PTN002919572` | 336 | 68 | AGFG1, AGFG2 (only) | GO:0001675, GO:0007289, GO:0031410, GO:0045109 (68 each); GO:0005737, GO:0016020 (32 each, no human) |

Asking the reciprocal question — *which node's human reach is exactly my gene set, and
what did it give them?* — `PTN002919572`'s human reach is exactly {AGFG1, AGFG2}, and what
it gave them is the mouse *Agfg1* knockout phenotype set.

Its 68 gene products span, with names resolved rather than left as taxon ids,
**sea lamprey and hagfish (*Petromyzon marinus*, *Eptatretus burgeri*)** through
cartilaginous fish, ray-finned fish, coelacanth, amphibians, reptiles, birds, monotremes,
marsupials and placental mammals — plus one non-vertebrate outlier, the tardigrade
*Hypsibius exemplaris*. So a single mouse knockout is the sole experimental basis for
acrosome-assembly and spermatid-differentiation annotations across the whole vertebrate
range.

**Human AGFG1's five IBA rows are the same five terms as AGFG2's** (GO:0001675, GO:0005737,
GO:0007289, GO:0031410, GO:0045109). AGFG2's entire IBA record is its better-studied
paralogue's IBA record. The difference is evidential, not textual: on AGFG1 those rows are
an **orthologue** transfer from mouse Agfg1; on AGFG2 they are a **paralogue** transfer.

Record counts: AGFG2 has **7** annotations, **1** experimental (the bulk-proteomics HDA);
AGFG1 has **35**, **7** experimental.

## 6. Provenance of the two non-IBA rows

**`GO:0016020` membrane, HDA, `PMID:19946888`.** Fully paginated, the reference carries
**1142 annotations over 1142 distinct gene products, every one `GO:0016020`, every one
HDA, every one assigned by UniProt**. One NK-cell membrane-proteome survey giving 1142
proteins one identical term is a bulk import, not 1142 localisation determinations.
Entity counts are derived as a distinct set of gene-product ids — an annotation count is
not an entity count. Positive control on the same endpoint and call pattern:
`GO_REF:0000033` restricted to human GO:0005096 descendants returns 188 annotations over
188 entities. AGFG2's own feature table has no transmembrane segment, no signal peptide
and no lipid-anchor site.

**`GO:0005096` GTPase activator activity, IEA, `InterPro:IPR001164`.** AGFG2 matches four
InterPro entries; each one's interpro2go mapping was looked up separately.

| InterPro entry | type | proteins | maps to |
|---|---|---|---|
| IPR052248 Arf-GAP domain and FG repeat-containing protein | family | 3 656 | **nothing** |
| IPR037278 ARFGAP/RecO-like, zinc finger superfamily | homologous superfamily | 77 285 | **nothing** |
| IPR038508 ArfGAP domain superfamily | homologous superfamily | 61 770 | **nothing** |
| **IPR001164 Arf GTPase activating protein** | domain | 60 678 | **GO:0005096 (F)** |

The three entries that map to nothing are the control: InterPro2GO is capable of restraint
here. The activity claim comes from the pan-ArfGAP catalytic-domain entry, which spans
60 678 proteins across all ArfGAP subfamilies and by construction cannot discriminate the
AGFG subfamily's loss of the Arf-contacting aspartate. The AGFG-specific entry
(`IPR052248`), which *could* encode the subfamily's distinct properties, carries no GO
terms at all.

**Family census.** All 6 reviewed (Swiss-Prot) members of `PTHR46134` — human and
mouse AGFG2, human/mouse/rat/bovine AGFG1 — carry `GO:0005096` by `IEA GO_REF:0000002`,
and **not one has any experimental evidence for it** (0/6). Reported as the Swiss-Prot
subset: 6 entries out of the family's 3 656 proteins, i.e. **0.16 %**; the cached
`PTHR46134-entries.csv` is built from InterPro's reviewed-only endpoint, so this is not a
statement about the family.

## 7. Term-level facts, verified against QuickGO

- `GO:0005096` is **not obsolete** and `GO:0008060` "ARF GTPase activator activity" is one
  of its `secondaryIds` — i.e. merged, not absent. Its only live child is `GO:1902773` via
  `capable_of`. **`GO:0005096` is already maximal**; no substrate-specific GAP child exists
  to propose or to MODIFY toward.
- `GO:0031410` is a verified descendant of `GO:0005737`, so the two location rows are
  nested rather than independent.
- GO has **no** term for von Willebrand factor secretion or Weibel-Palade body exocytosis
  (searches for both return only the CC term `GO:0033093`). But the class is curatable and
  has been curated: `GO:0045055 regulated exocytosis` has verified `is_a` children
  including `GO:0002576` platelet degranulation, `GO:0043299` leukocyte degranulation,
  `GO:0016079` synaptic vesicle exocytosis and `GO:0060471` cortical granule exocytosis.
  This is an inconsistency in coverage, not a missing modelling pattern.
- `GO:0046784 viral mRNA export from host cell nucleus` was **rejected** for the Rev-export
  result on two counts: its definition specifies "*intronless viral mRNA*" whereas the
  Rev/RRE pathway exports intron-containing transcripts, and it carries **0** human
  annotations, so using it here would make AGFG2 its sole human holder.
- `GO:0044794 host-mediated activation of viral process` carries **58** human annotations
  over 53 entities including IMP, so it is an actively used host-factor term rather than an
  unused corner of the ontology. The declined alternative `GO:1903077` carries 37 over 31.
  All of these counts, including the `GO:0046784` zero, are recorded in `term_checks.json`
  with `GO:0045055` (369 over 201) as the non-zero control that makes the zero readable.
- `GO:0045109`'s definition is "*Control of the spatial distribution of intermediate
  filaments…*", i.e. a genuine cytoskeletal-organisation claim, not a by-product term.

## 8. Recorded search-derived negatives (each a statement about a query)

Positive controls in the same call pattern are shown alongside, so a zero cannot be a
broken query. Full query strings are in `litsearch.json`.

| query | hits |
|---|---|
| AGFG2/HRBL **and** acrosome / acrosomal / spermatid / spermatogenesis / sperm / testis | **0** |
| AGFG1/Hrb **and** acrosome / acrosomal — *control* | 9 |
| AGFG2/HRBL **and** keratin / intermediate filament / vimentin / manchette | **0** |
| AGFG1/AGFG2/HRB/HRBL/drongo **and** GAP activity / GTPase-activating / GTP hydrolysis / ArfGAP | 7, none of which measures GAP activity on an AGFG protein |
| GAP activity / GTPase-activating **and** ARFGAP1 / ASAP1 — *control* | 134 |
| AGFG2 with all synonyms (AGFG2, HRBL, HRB-like, RAB-R) | 19, of which 5 concern this gene |
| AGFG1 with all synonyms — *control* | 587 |

Retraction / erratum / expression-of-concern check, read from `CommentsCorrections` on each
cited article's own PubMed record: **none flagged** for any of the **12** references relied
on (`PMID:9303539`, `10613896`, `11711676`, `14724135`, `16765935`, `19946888`, `21284487`,
`23433073`, `25496667`, `26701340`, `27654348`, `34369554`). The set checked is the union of
`TITLES_NEEDED` and `CITED_BY_REVIEW` in `litsearch.py`, and `litsearch.json` records the
count as `n_cited_checked: 12` so the number here cannot drift from the sweep.

## 9. Checks that came back negative, reported as negatives

- **Logical-opposite citation cross-product.** No pair of AGFG2's 7 terms is a
  positive/negative regulation pair or otherwise logically opposed, so the cross-product
  test has nothing to intersect. Run, empty.
- **IntAct** (`intact.py` / `intact.json`). 10 records, of which 2 are miRNA–mRNA CLASH
  and **8 are protein–protein over 5 distinct partners**: AGFG1, TRIM68 and STARD7 by
  `anti tag coip` in **both** BioPlex releases (`PMID:28514442`, `PMID:33961781` — one
  platform, not two independent methods), XPO1 by pull-down (`PMID:26673895`), and
  *Yersinia* lcrS by `two hybrid pooling` (`PMID:20711500`, MI-score 0.37, a host–pathogen
  screen). That leaves **4 human partners with co-IP or pull-down support**, which is the
  figure the review quotes. lcrS drops out on *method*, not on species — the by-name
  non-human filter in the script is a no-op here and is reported as one rather than
  credited with the exclusion. **None of the five appears in GOA: AGFG2 has zero
  `GO:0005515` rows**, so no per-partner verdicts were needed — but the absence is itself
  an under-curation datum.
- **Self-referential IBA.** No WITH/FROM token on any row is AGFG2's own accession, so no
  row records a PAINT curator judging the function core to this gene.

## 10. A discrepancy between two cited papers, settled

`PMID:21284487` states AGFG2 proteins are "*present in mammals only*", from an analysis of
"*the first section of the coding mRNAs*". Two independent lines say otherwise:

- `PMID:23433073`, a dedicated phylogenetic study, places the AGFG duplication among the
  subfamilies that duplicated "*at the base of vertebrates*";
- a UniProt symbol census (totals read from `x-total-results`, never from a page), using
  `distribution.json`'s own clade names so the sets do not appear to double-count —
  **Aves is a subset of Sauropsida**, not a separate tally:

  | clade (NCBI taxon) | `agfg2` | `agfg1` (control) |
  |---|---|---|
  | Actinopterygii, 7898 | **72** | 50 |
  | Sauropsida, 8457 (reptiles + birds) | **23** | 473 |
  | Aves, 8782 (⊂ Sauropsida) | **1** | 363 |
  | Amphibia, 8292 | **4** | 28 |
  | Mammalia, 40674 | 274 | 591 |

  The control is non-zero in every clade, so none of the small `agfg2` numbers is a
  rejected query. The avian asymmetry is real and worth noting — **1** avian `agfg2`
  against **363** avian `agfg1` — but it is a symbol count, and the caveat below applies
  to it as much as to the positive result.

A symbol census is a name-matching pipeline's output, not an orthologue count, so on its
own it would not settle this; combined with the phylogenetic result it is enough to say the
mammals-only claim is unsupported. Consistently, `PTN002919572` reaches lamprey, hagfish
and zebrafish (section 5).
