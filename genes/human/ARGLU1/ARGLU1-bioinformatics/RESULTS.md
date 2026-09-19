# ARGLU1 bioinformatics results

Four analyses supporting the human ARGLU1 GO annotation review. Each is a
standalone script in this directory writing a JSON artefact; this file is a
hand-written summary of those artefacts, not a generated report.

| script | artefact | question |
|---|---|---|
| `panther_node_audit.py` | `results.json` | What does PANTHER node `PTN001271790` propagate, to whom, and on whose experimental evidence? |
| `reference_scope_audit.py` | `reference_scope.json` | How many gene products does each cited reference annotate — a finding or a screen? |
| `intact_partner_audit.py` | `intact_partners.json` | Are the four GOA IPI partners canonical, topologically plausible, and independently replicated? |
| `composition_and_features.py` | `composition.json` | What is actually in the sequence, and what fold evidence exists? |
| `sibling_row_verdicts.py` | `sibling_verdicts.json` | How did already-merged reviews resolve the rows ARGLU1 shares with them? |
| `splicing_factor_eligibility.py` | `splicing_factor_eligibility.json` | Which IPI partners qualify for `GO:1990935` splicing factor binding? |

Run any of them with `uv run python <script>.py` from this directory. All but
`composition_and_features.py` and `sibling_row_verdicts.py` require network
access (QuickGO, UniProt, IntAct); `composition_and_features.py` reads the
committed `../ARGLU1-uniprot.txt` and `sibling_row_verdicts.py` reads the
repository's own review YAMLs (it derives the repo root rather than hardcoding
a worktree path).

---

## 1. The mitochondrion IBA rests on one *Candida albicans* Mediator-tail paralog

`panther_node_audit.py` compares the two cellular-component terms human ARGLU1
receives by IBA **from the same PANTHER node**, `PTN001271790`:

| term | IBA rows from this node | distinct gene products | distinct NCBI taxa | gene products holding it by their **own** experimental evidence |
|---|---|---|---|---|
| `GO:0005654` nucleoplasm | 111 | 111 | 64 | **3** — human ARGLU1, mouse Arglu1, *Drosophila* Arglu1 (all Swiss-Prot ARGLU1 orthologs) |
| `GO:0005739` mitochondrion | 111 | 111 | 64 | **1** — *Candida albicans* **TLO16** (`A0A1D8PRM3`, **TrEMBL**), IDA from `PMID:22923044` |

The node's reach is identical for the two terms, so the difference is entirely in
the donor pool. Every one of the 111 mitochondrion rows names `CGD:CAL0000179812`
in its WITH/FROM field — i.e. the whole family's mitochondrial annotation, across
64 taxa including plants, green algae, *Selaginella*, *Marchantia*, *Trichoplax*,
*Daphnia* and all vertebrates, traces to that single protein.

What that protein is matters. InterPro assigns `A0A1D8PRM3` three signatures:

```
interpro IPR021017 | Mediator complex, subunit Med2, fungi | family
interpro IPR027267 | AH/BAR domain superfamily         | homologous_superfamily
interpro IPR033371 | Arginine and glutamate-rich protein 1 | family
pfam     PF11214   | Mediator complex subunit 2
panther  PTHR31711 | ARGININE AND GLUTAMATE-RICH PROTEIN 1
```

Human ARGLU1 (`Q9NWB6`) carries only `IPR033371` / `PF15346` / `PTHR31711`. TLO16
is therefore a **fungal Med2-family protein that also matches the ARGLU1 family
signature** — an architecturally distinct occupant of the node, not an ARGLU1
ortholog.

The source paper is explicit that the mitochondrial localisation is not even a
property of the TLO family as a whole: the TLO family is a *C. albicans*-specific
expansion "from one or two copies in other CUG clade members to 14 expressed
copies", and only the γ clade reaches mitochondria while clades α and β "encode
proteins that localize primarily to the nucleus".

**Conclusion:** a clade-restricted localisation of a lineage-specific fungal
gene-family expansion has been placed at a pan-eukaryotic node and distributed to
111 gene products. This is a node-placement defect, not evidence about ARGLU1.

**Divergence from the corpus, stated deliberately.** `sibling_row_verdicts.py`
finds 213 merged reviews in this repository carrying a `GO:0005739` IBA row, and
their modal verdict is `ACCEPT` (127), with `KEEP_AS_NON_CORE` 68,
`MARK_AS_OVER_ANNOTATED` 12, `MODIFY` 2 and `REMOVE` 2. This review's `REMOVE` is
therefore against the corpus trend. That is intended: for most of those 213 genes
the donor pool is genuinely mitochondrial, whereas here the entire donor pool is
one *Candida* TLO protein whose own source paper restricts the localisation to one
clade of one lineage-specific family. The corpus trend is not an argument about
this node.

## 2. The cadherin-binding row is a proximity-labelling screen read as binding

`reference_scope_audit.py` counts, per (reference, term) pair, how many *distinct
gene products* the reference annotates. Annotation counts and entity counts are
reported separately because they are different numbers; where the result set is
too large to enumerate, the entity count is reported as unavailable rather than
extrapolated from one page.

| reference | term | annotations | distinct gene products | evidence |
|---|---|---|---|---|
| `PMID:25468996` E-cadherin proximity biotinylation | `GO:0045296` cadherin binding | 272 | **272** | HDA ×271, IDA ×1 (all `BHF-UCL`) |
| `PMID:33961781` BioPlex 3.0 | `GO:0005515` | 9509 | not enumerated (>2000 cap) | — |
| `PMID:22365833` spliceosome PPI map | `GO:0005515` | 447 | 155 | IPI (IntAct) |
| `PMID:23602568` CMGC kinase interactome | `GO:0005515` | 278 | 121 | IPI (IntAct) |
| `PMID:39251607` post-transcriptional modules | `GO:0005515` | 201 | 122 | IPI (IntAct) |
| `PMID:30698747` **ARGLU1 primary paper (control)** | `GO:0005515` | 8 | **4** | IPI |

The control discriminates: the paper that actually studied ARGLU1 annotates four
gene products; the screens annotate 121–272+ each.

For the cadherin row specifically, the assay measures proximity, not binding —
the paper reports "561 proteins in the vicinity of the cytoplasmic tail of
E-cadherin" — and ARGLU1's every curated location is nuclear (nucleus,
nucleoplasm, nuclear speck, chromosome).

**Cross-check against merged reviews:** 38 gene reviews already in this
repository carry this same `GO:0045296` / `PMID:25468996` row. Their verdicts are
`MARK_AS_OVER_ANNOTATED` ×21, `KEEP_AS_NON_CORE` ×11, `REMOVE` ×3, `UNDECIDED` ×1,
`ACCEPT` ×1, `PENDING` ×1. This review follows the modal verdict.

## 3. Partner audit: three checks, and what each returned

`intact_partner_audit.py`. ARGLU1 has **250 IntAct binary rows across 222 distinct
partner accessions** — it is a well-connected disordered protein, so partner count
alone discriminates nothing.

Note on counting: IntAct lists several identifier *forms* for one study (PubMed
id, DOI, MINT ac, IntAct ac), so the raw identifier count overstates the number of
studies — 10 forms for SRPK2's 3 studies. The table counts distinct PubMed ids.

| partner | accession | status | length | UniProt locations | rows with ARGLU1 | distinct PubMed studies | distinct detection methods | partner's own IntAct partners |
|---|---|---|---|---|---|---|---|---|
| SRPK2 | `P78362` | Swiss-Prot | 688 aa | Chromosome; Cytoplasm; Nucleus speckle; Nucleoplasm | 3 | 3 | **3** (`protein kinase assay`, `2 hybrid`, `anti tag coip`) | 517 |
| U2AF2 | `P26368` | Swiss-Prot | 475 aa | Nucleus | 4 | 2 | 3 (`anti tag coip`, `confocal microscopy` ×2, `proximity-dependent biotin identification`) | 473 |
| PUF60 | `Q9UHX1` | Swiss-Prot | 559 aa | Nucleus | 4 | 2 | 2 (`anti tag coip` ×2, `confocal microscopy` ×2) | 184 |
| JMJD6 | `Q6NYC1` | Swiss-Prot | 403 aa | Cytoplasm; Nucleolus; Nucleoplasm | 5 | 3 | **1** (`anti tag coip` ×5) | 172 |

Results of the three standing checks, including the nulls:

1. **Canonical-partner check — negative (no defect).** All four accessions resolve
   to reviewed Swiss-Prot entries at their canonical lengths. No unreviewed
   partial-ORFeome substitution of the kind found on ACRV1.
2. **Topological-plausibility check — negative (no defect).** All four partners
   are nuclear; SRPK2 is itself annotated to nuclear speckles, the compartment
   ARGLU1 occupies. The partner set coheres with ARGLU1's own biology rather than
   with a screen's bait panel.
3. **`NbExp` inflation check — mixed.** UniProt lists `NbExp=3` for SRPK2 and
   `NbExp=4` for the other three. Expanding the records shows SRPK2's three rows
   are **three orthogonal methods from three independent laboratories**
   (Varjosalo 2013 in vitro kinase assay; Hegele 2012 yeast two-hybrid; Huttlin
   2021 AP-MS) — genuine replication, not one screen logged three ways. JMJD6 is
   the opposite: all five rows are `anti tag coip`, and three of them are
   spoke-expanded BioPlex rows from two releases of the same pipeline, so its
   effective independent support is the primary paper's directed co-IP plus one
   AP-MS pipeline.

**The single most informative row in the table** is SRPK2's, which IntAct types
not as `physical association` but as **`phosphorylation`**, detected by
`protein kinase assay`, host `In vitro`. ARGLU1 is recorded there as an in vitro
substrate of SRPK2, not merely a binding partner.

## 3b. A term the review first said did not exist — and who it applies to

`splicing_factor_eligibility.py`. An earlier draft of this review removed all six
U2AF2 / PUF60 / JMJD6 `GO:0005515` rows on the stated ground that GO had no
splicing-factor-binding molecular function term. **That was false.**
`GO:1990935 splicing factor binding` is active, is a molecular function, and is
defined as *"Binding to a protein involved in the process of removing sections of
the primary RNA transcript to form the mature form of the RNA."*

The error is instructive rather than careless: the draft searched for
*"spliceosomal complex binding"*. GO's text search is **token-based**, and
*spliceosomal complex* shares no token with *splicing factor*, so that query could
not have returned the term however it was phrased. It was found by walking the
ontology (children of `GO:0044877`, plus compound-word searches) rather than by
searching harder.

Whether the recovered term *applies* is then a per-partner question, settled by
querying GOA for each partner's own annotations under `GO:0008380` RNA splicing:

| partner | accession | annotations under RNA splicing | evidence | verdict |
|---|---|---|---|---|
| U2AF2 | `P26368` | 6 | **IDA** (`GO:0000398`), NAS ×2, IC, IBA, IEA | splicing factor — term applies, experimentally grounded |
| PUF60 | `Q9UHX1` | 2 | IBA ×2 | splicing factor — term applies, but on inferred evidence only |
| JMJD6 | `Q6NYC1` | **0** | — | **not** a splicing factor — term withheld |
| SRPK2 | `P78362` | 4 | **IDA ×2** (`GO:0000245`, `GO:0008380`), IBA, IEA | also a splicing factor, but see below |

Consequences for the review:

- U2AF2 (×3 rows) and PUF60 (×2 rows) → `MODIFY` to `GO:1990935`.
- JMJD6 (×2 rows) → stays `REMOVE`, now on a measured JMJD6-specific ground: an
  oxygenase that hydroxylates a splicing factor is not itself one, and the term's
  definition requires the partner be involved in splicing.
- SRPK2 (×3 rows) → stays `MODIFY` to `GO:0019901` protein kinase binding. SRPK2
  qualifies under *both* terms, but the in vitro **kinase assay** typed by IntAct
  as `phosphorylation` is the better-evidenced relationship, and the kinase term
  carries the mechanistic content.

The general rule this cost a round to relearn: **a failed keyword search is not
evidence that a term is absent.** Search the compound word as well as the
fragment, and enumerate children of the plausible parent rather than trusting a
text query.

## 4. The composition is a composition, and there is no domain

`composition_and_features.py`, parsing the committed UniProt flat file (parsed
length asserted equal to the declared 273 aa before anything is computed).

| region | length | R | K | R+K | E | E+D | S | RS dipeptides | longest alternating RS run |
|---|---|---|---|---|---|---|---|---|---|
| N-terminal RNA-binding region (1–74) | 74 aa | 33.8% | 12.2% | **46.0%** | 6.8% | 9.5% | 27.0% | 12 RS / 12 SR | **8 dipeptides** |
| C-terminal transcription-regulatory region (75–273) | 199 aa | 14.1% | 12.1% | 26.2% | **24.6%** | 27.1% | 4.0% | 1 RS / 1 SR | 1 |
| full length | 273 aa | 19.4% | 12.1% | 31.5% | 19.8% | 22.4% | 10.3% | 13 RS / 13 SR | 8 |

Three things follow.

- The two regions UniProt delimits by experiment have **opposite charge
  character**, and the boundary is sharp: E+D goes 9.5% → 27.1% and S goes 27.0%
  → 4.0% across it.
- The N-terminal RNA-binding region is not merely "arginine-rich": it is a
  genuine **RS-repeat (SR-protein-like) region**, with 12 RS and 12 SR dipeptides
  and an unbroken 8-dipeptide alternating run. This is the structural fact behind
  SRPK2 — an SR-protein kinase — phosphorylating ARGLU1 in vitro, and behind
  UniProt's phosphoserines at Ser-58, Ser-60 and Thr-61, all of which fall inside
  this region (the other three annotated sites, Ser-76, Ser-77, Ser-266, fall in
  the C-terminal region).
- **The complete signature content of the entry is `IPR033371` / `PF15346` /
  `PTHR31711(:SF1)`** — one family and its own PANTHER family, nothing else.
  `PF15346` is typed by InterPro as `coiled_coil`, not `domain`. There is no
  catalytic, nucleotide-binding, or recognised nucleic-acid-binding fold anywhere
  in the protein.

That last point is the negative result that matters for curation: **no molecular
function can be reverse-engineered from ARGLU1's domain content, because it has
none.** "Arginine and glutamate rich" names a composition. Every molecular
function claim on this gene has to come from an experiment, and the review treats
it that way.
