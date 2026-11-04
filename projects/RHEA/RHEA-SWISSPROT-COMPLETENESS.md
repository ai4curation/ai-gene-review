---
title: "RHEA -> GO completeness for Swiss-Prot reactions, and consistency with native GO"
---

# RHEA → GO completeness for Swiss-Prot reactions

**Parent project:** [RHEA.md](../RHEA.md)

**Goal.** Every RHEA reaction used in at least one Swiss-Prot catalytic-activity annotation gets a
predicated mapping in GO: an `xref: RHEA:n {source="skos:exactMatch"}` (GO term equals the reaction)
or `{source="skos:narrowMatch"}` (the reaction is narrower than the GO term, so GO is the broader term).
A `skos:broadMatch` xref (GO term narrower than the reaction) does not count. In parallel, for every
reaction that is already mapped, we check whether the Swiss-Prot entries carrying it agree with their
native GO molecular-function annotations.

The mappings live in GO itself: `rhea2go` is generated from the RHEA xrefs on GO terms in
`go-edit.obo`. So coverage is measured against `go-edit.obo` at go-ontology HEAD (`3ce60f4`,
2026-11-04), not against the last `rhea2go` release.

## Coverage (go-ontology HEAD, 2026-11-04)

The unit is the RHEA **master** (undirected) id. Every Swiss-Prot catalytic-activity row carries
the master id; about one in five also carries a directional id. A master counts as covered only by
an xref on the master itself. An xref on a directional child (for example `RHEA:57722` ATP synthesis)
does not cover the undirected master that most entries carry.

| Status | Reactions | Swiss-Prot entry–reaction pairs |
|---|---:|---:|
| `exactMatch` on the master | 3,734 | 219,937 |
| `narrowMatch` on the master (GO broader) | 2,782 | 37,741 |
| **unmapped** | **7,610** | **71,604** |
| only `broadMatch` (GO narrower), needs a broader call | 30 | 3,128 |
| xref with no predicate | 5 | 248 |
| only directional children mapped | 2 | 2,155 |
| **total** | **14,163** | |

So **46% of Swiss-Prot-used reactions are covered** and **7,647 need a call**. 144 of them already
have a curated proposal in [`rhea2go.sssom.yaml`](rhea2go.sssom.yaml) that has not been taken
into GO.

### Shape of the unmapped set

- **Size:** 2,773 reactions are on a single Swiss-Prot entry, and 325 are on more than 20.
  The largest are `RHEA:46608` (protein threonine phosphorylation, 3,735 entries; GO has no
  threonine-only kinase term, so it needs `narrowMatch` to GO:0004674), the complex I / NDH
  quinone reductases `RHEA:57888`, `RHEA:42608` and `RHEA:42612` (about 1,700–2,900 each), and
  `RHEA:54728` acetyl-CoA carboxylase carboxyltransferase (980).
- **Kind:** 5,530 small-molecule reactions, 1,141 transport reactions, 939 macromolecule
  (protein/RNA/DNA/ACP) reactions.
- **EC:** 5,451 have no EC number, so the EC bridge does not reach them.

### Candidate tiers for unmapped reactions

[`completeness/unmapped_candidates.tsv`](completeness/unmapped_candidates.tsv) lists every reaction
that needs a call, with the candidates from each tier:

| Tier | Rule | Reactions |
|---|---|---:|
| `A_rhea_parent` | A RHEA `is_a` ancestor reaction is mapped, so `narrowMatch` to its GO term | 34 |
| `B_ec_exact` | Single EC, the EC has only this reaction, and GO has the EC as `exactMatch`: candidate `exactMatch` | 12 |
| `B_ec` | Full EC mapped in GO, but the EC spans several reactions: candidate `narrowMatch` | 209 |
| `C_ec_parent` | Full EC not in GO; nearest EC sub-subclass in GO (usually a class term such as GO:0016838): candidate `narrowMatch` | 1,930 |
| `E_noec` | No EC: needs chemistry-aware judgement | 5,460 |
| `defmatch` column | RHEA equation equals a GO definition equation, meaning the GO term exists but the xref is missing | 14 |
| `native_cand` column | Most specific catalytic/transporter term shared by at least 60% of the carrying entries' non-circular MF annotations | 6,850 have one |

The `native_cand` column is a hint, not a mapping. Spot checks show it often names the enzyme's
*other* activity: a fatty-acid transport reaction on FATPs gets "long-chain fatty acid-CoA ligase",
and a side reaction of PPC decarboxylase gets the main activity. Every row still needs a check that
the GO definition subsumes the reaction's participants.

## Consistency of mapped reactions with native GO annotations

For each GO xref RHEA:id → GO term *g* (exactMatch or narrowMatch), and each Swiss-Prot entry whose
catalytic-activity annotation carries that exact RHEA id, the entry is classified by its MF annotations
(UniProt REST, all sources) **excluding the circular ones**: `IEA:RHEA` and `IEA:UniProtKB-EC`, which
are generated from these mappings and the EC bridge. Closure uses go-basic `is_a`
(`releases/2026-07-26`).

| Class | Meaning | Curated sources only | All non-circular sources |
|---|---|---:|---:|
| consistent | has *g* or an `is_a` descendant | 61,147 | 195,752 |
| ancestor_only | only less specific terms in *g*'s lineage | 5,597 | 5,864 |
| disjoint | has catalytic/transporter terms, none in *g*'s lineage | 6,852 | 24,054 |
| none | no catalytic/transporter MF | 184,093 | 32,019 |

Of the 6,518 mappings checked, 1,552 have at least one disjoint entry, and 373 (with at least 3
entries) are majority-disjoint. Thirty-four of those 373 point at `GO:777xxxx` terms that exist only
on go-ontology HEAD. Native annotations cannot use those yet (release lag, not conflict).
Per-mapping detail, with example accessions and the conflicting terms, is in
[`completeness/consistency.tsv`](completeness/consistency.tsv).

### What drives "disjoint"

The most frequent (mapped term, conflicting native term) pairs fall into three classes. Each needs a
different fix.

1. **Partial or component reactions.** UniProt records a half-reaction or coupled reaction whose
   GO mapping is chemically exact, while GO annotates the whole activity:
   - glutaminase half-reaction (`L-glutamine + H2O = L-glutamate + NH4+` → GO:0004359) on CTP
     synthase, GMP synthase and carbamoyl-phosphate synthase (1,921 disjoint entries, most carrying
     GO:0003883 CTP synthase activity);
   - ATP hydrolysis (→ GO:0016887) on RuvB four-way-junction helicase (2,104) and on ABC
     transporters.

   The mapping is right; the comparison needs `has_part`. **Not a conflict.**
2. **Sibling-specificity disagreements.** UniProt's reaction and the native GO term name sibling
   chemistries. **These are the real annotation-review targets:**
   - GuaA: RHEA glutamine-dependent GMP synthase (GO:0003922) vs native GO:0003921
     ammonia-dependent, from InterPro2GO, TreeGrafter and IBA (634);
   - succinyl-CoA ligase GDP-forming (GO:0004776) vs ADP-forming GO:0004775 (514);
   - GatCAB Asn-tRNA(Asn) amidotransferase (GO:0050566) vs Gln-tRNA(Gln) GO:0050567 only (564);
   - carbamoyl-phosphate synthase ammonia (GO:0004087) vs glutamine-hydrolysing GO:0004088 (240);
   - MsrA free L-Met-(S)-oxide reductase (GO:0033744) vs peptide-Met-(S)-oxide GO:0008113 (291);
   - archaeal tRNA-guanine15 transglycosylase (ArcTGT): every entry gets queuine TGT GO:0008479
     (guanine34) from InterPro2GO, an apparent InterPro2GO over-propagation.
3. **Ontology structure.** GO:0106310 protein serine kinase activity is not `is_a` GO:0004674
   protein serine/threonine kinase activity, so 1,409 Ser/Thr kinases look disjoint.

### Suspect mappings in GO (for go-ontology follow-up)

- `RHEA:30783` (D-glyceraldehyde + **NAD+** + H2O = (R)-glycerate + NADH) is `narrowMatch` to
  GO:0043795 glyceraldehyde oxidoreductase activity. That term is EC 1.2.99.8, the generic-acceptor
  (Mo/W) enzyme, while every carrying entry is an NAD-dependent ALDH. A better target is
  GO:0004029 aldehyde dehydrogenase (NAD+) activity.
- The 5 untyped xrefs (`RHEA:83435`, `55132`, `33179`, `69416`, `44884`) need a predicate.
- The 30 masters with only `broadMatch` xrefs need a broader GO call. These are mainly the uniporter
  and channel reactions (`K+(in) = K+(out)` has only channel/uniporter children) and the generic
  phosphomonoester hydrolysis `RHEA:15017`.
- The undirected masters `RHEA:57720` (H+-ATPase/ATP synthase, rotational; 2,150 entries) and
  `RHEA:58156` (Na+ analogue) are mapped only through their directional children.

## Reproduce

```bash
projects/RHEA/completeness/fetch_data.sh .cache/rhea-completeness        # RHEA TSVs, go-basic, UniProt MF GO (~5 min)
projects/RHEA/completeness/run_all.sh ../go-ontology/src/ontology/go-edit.obo .cache/rhea-completeness
```

Scripts: [`coverage.py`](completeness/coverage.py), [`candidates.py`](completeness/candidates.py),
[`defmatch.py`](completeness/defmatch.py), [`native_consensus.py`](completeness/native_consensus.py),
[`consistency.py`](completeness/consistency.py), shared parsing in
[`rheago_lib.py`](completeness/rheago_lib.py).
