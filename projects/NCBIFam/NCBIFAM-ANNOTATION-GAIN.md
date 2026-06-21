---
title: "NCBIFAM → GO Annotation Gain"
---

# NCBIFAM → GO Annotation Gain

**Parent project:** [NCBIFam.md](../NCBIFam.md)

How many GO annotations would be **gained** if NCBIFAM's own NCBI-curated
`go_terms` (from `hmm_PGAP.tsv`) were ingested as an `ncbifam2go` mapping and
propagated to every UniProtKB entry that already carries the family signature?
This is the NCBIFAM analog of [RHEA-ANNOTATION-GAIN.md](../RHEA/RHEA-ANNOTATION-GAIN.md),
computed live by [`ncbifam_go_gain.py`](ncbifam_go_gain.py).

## Method

For each NCBIFAM model with a GO term:

```
gain = N(xref:ncbifam-<id>) − N(xref:ncbifam-<id> AND go:<id>)
```

against the UniProtKB REST API (`x-total-results`, no records fetched). UniProt's
`go:` query is **closure-aware** (matches the term *and its descendants*), so a
family whose GO term is already covered by a more specific child counts as **no
gain** — the gain is closure-filtered, not naive exact-match. Gain is reported for
**Swiss-Prot (reviewed)** — the curation-relevant, trustworthy number — and for
all of UniProtKB (mostly automated TrEMBL) as context.

## Headline: the gain is real but lives in TrEMBL, not Swiss-Prot

Two deterministic samples of `equivalog` models with a single GO term:

| Sample | Models | Σ gain reviewed (Swiss-Prot) | Σ gain all UniProtKB |
|--------|-------:|----------------------------:|---------------------:|
| 25-model | 25 | 4 | 8,385 |
| 60-model | 60 | 19 | 26,578 |

**The curation-relevant (reviewed) gain is small; the all-UniProtKB gain is
large.** This is the opposite emphasis from RHEA (which gained ~42 *reviewed*
annotations). The reason is structural: NCBIFAM is **prokaryote-heavy**, and
Swiss-Prot's curated prokaryotic enzymes already carry the GO term (often added by
hand or via the InterPro route), whereas the millions of **unreviewed TrEMBL**
entries carrying the same signature do not. So ingesting `ncbifam2go` would mostly
improve automated annotation depth, with a modest but non-zero curated-entry gain
concentrated in newer biology.

⚠️ The all-UniProtKB numbers inherit the reliability of automated annotation and
should not be extrapolated naively to "true gaps" — they are an upper bound on
propagation volume, not a count of curation-ready additions.

## Where the gap concentrates — mobile elements, defense, secretion, division

Top propagation gaps in the 60-model `equivalog` sample (`gain_all` = entries
carrying the signature that lack the GO term or any descendant):

| Family | GO | N(sig) | gain (all) | gain (rev) | What it is |
|--------|----|-------:|-----------:|-----------:|------------|
| NCBIFAM:NF033545 | GO:0004803 transposase activity | 18,881 | 18,874 | 2 | IS630 family transposase |
| NCBIFAM:TIGR00439 | GO:0000910 cytokinesis | 3,306 | 3,304 | 5 | permease-like cell division protein FtsX |
| NCBIFAM:NF041162 | GO:0140737 encapsulin nanocompartment | 901 | 897 | 0 | family 2A encapsulin shell protein |
| NCBIFAM:TIGR03744 | GO:0005524 ATP binding | 706 | 694 | 0 | conjugative transfer ATPase |
| NCBIFAM:TIGR02165 | GO:0043571 …CRISPR… | 432 | 432 | 0 | type I-G CRISPR protein Csb2 |
| NCBIFAM:TIGR02878 | GO:0030436 sporulation | 298 | 298 | 1 | sporulation protein YpjB |
| NCBIFAM:TIGR02791 | GO:0043684 type IV secretion system complex | 298 | 298 | 4 | P-type DNA transfer protein VirB5 |
| NCBIFAM:NF042963 | GO:0051607 defense response to virus | 151 | 151 | 0 | anti-phage DUF1156 protein |

The pattern is consistent: **transposases / IS elements, conjugation and type
III/IV/VI secretion, CRISPR and anti-phage defense, sporulation, encapsulins, cell
division** — the mobile-genetic-element and microbial-defense biology where
InterPro integration of the NCBIFAM signature lags, so NCBIFAM's own GO assignment
never propagates. Several even show a **reviewed** gap (FtsX 5, VirB5 4), i.e.
Swiss-Prot entries that are missing the term too — the cleanest gap-fill targets.

## The verification caveat is mandatory

NCBIFAM's `go_terms` are NCBI-assigned and **not** automatically current or correct.
Three distinct failure modes turned up while building the 28-row seed, each of which
a naive bulk ingest would have propagated:

- **Obsolete** — `GO:0009448` on a GABA transaminase is an obsolete id.
- **Outright wrong** — the diacylglycerol-kinase model **NF009874** (EC 2.7.1.107)
  is tagged `GO:0003951 NAD+ kinase activity`; the correct term `GO:0004143
  ATP-dependent diacylglycerol kinase activity` exists. A wrong-MF assignment, not
  just an altitude issue — excluded.
- **Altitude-broad** — several sit far above the family's real function, up to the
  ontology **near-root** `GO:0003824 catalytic activity` (enoyl-CoA hydratase
  NF005804, spermidine synthase TIGR00417), or a class parent (dGTPase NF002326 →
  `GO:0016793` when `GO:0008832 dGTPase activity` exists). For these we **propose our
  own specific term** as the `exactMatch` mapping (the EC-bridged child) instead of
  recording NCBI's broad value.

### Proposing the specific term unmasks the gain

The altitude fix is **not cosmetic**. Because UniProt's `go:` query is closure-aware,
the gain measured against a broad parent is near-zero (the parent is already
near-universal), so the broad NCBI term makes a real gap look like *no* gap.
Re-measuring against the specific child we propose flips this:

| Family | NCBI broad term (gain) | Our specific term (gain all / reviewed) |
|--------|-----------------------:|----------------------------------------:|
| spermidine synthase TIGR00417 | `GO:0003824` (~0) | `GO:0004766` — **575** / 1 |
| LL-DAP aminotransferase TIGR03542 | `GO:0008483` (77) | `GO:0010285` — **1,185** / 2 |
| dihydroorotase NF006559 | `GO:0016810` (4) | `GO:0004151` — **491** / 0 |
| dGTPase NF002326 | `GO:0016793` (20) | `GO:0008832` — **456** / **13** |
| enoyl-CoA hydratase NF005804 | `GO:0003824` (~0) | `GO:0004300` — **184** / 1 |

So suggesting our own term is what converts these from invisible to actionable — and
surfaces genuine **reviewed/Swiss-Prot** gaps (dGTPase 13, LL-DAP 2) that the broad
NCBI assignment hid entirely.

### …but high gain can also be an over-annotation trap (FtsX)

The same machinery warns against over-reach. For `TIGR00439` (cell division protein
**FtsX**) the candidate terms give:

| Term | gain (all / reviewed) | Interpretation |
|------|----------------------:|----------------|
| `GO:0051301` cell division | **22** / 0 (of 3,306 / 7) | curator consensus; all 7 reviewed FtsX already carry it |
| `GO:0000910` cytokinesis (NCBI's) | 3,304 / 5 | only 2/7 reviewed carry it |
| `GO:0043093` FtsZ-dependent cytokinesis | 3,304 / 5 | most specific; only 2/7 reviewed carry it |

A naive "maximise gain" rule would pick `GO:0043093` (3,304!), but the ontology says
cytokinesis is `part_of` cell division (so the specific terms are *narrower*, not
parents), and curators apply them to only 2/7 FtsX — FtsX/FtsEX *regulates* septal
hydrolysis rather than performing constriction. Propagating the specific term to all
3,306 entries would assert more than the evidence supports. The seed therefore maps
FtsX to the consensus `GO:0051301` (gain 22, confirmatory) and **declines** the
high-gain specific term. **High gain is a flag for review, not an instruction to
propagate** — it can mean a real masked gap (the five rows above) *or* an
over-annotation waiting to happen (FtsX).

So an `ncbifam2go` build must, like the curated seed in
[`ncbifam2go.sssom.yaml`](ncbifam2go.sssom.yaml):

1. drop obsolete **and incorrect** GO ids (check against EC where available),
2. **propose the specific child** where the NCBI term is a broad parent, and measure
   gain against *that* term, not the parent,
3. EC-bridge-confirm enzyme rows via `ec2go`.

## Reproduce

```bash
uv run python ncbifam_go_gain.py --family-type equivalog --single-go --sample 60
uv run python ncbifam_go_gain.py --accessions NF033545.0,TIGR02791.1,TIGR00439.2
```
