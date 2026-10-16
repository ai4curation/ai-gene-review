# C1GALT1C1 (Cosmc) — curation notes

## 2026-09-17 — de novo review

No `-deep-research-PROVIDER.md` exists for this gene: deep-research tooling was
unavailable (the configured OpenAI key is rejected). Per repository policy no
self-authored file was named as provider output. The review rests on the cached
publications, all of which were present for the PMIDs GOA cites, plus five papers
fetched during the work.

### The NOT annotation is the interesting row

GOA carries `GO:0016263` on Cosmc as **`NOT|enables`**. Read without the negation
flag this looks like a textbook necessity-mistaken-for-possession error: the IMP
behind it measured *T-synthase* activity in patient cells and found it reduced.
It is the opposite — the curators drew exactly the right distinction. Worth
remembering that the review-stub seeding does carry `negated: true` correctly;
the trap is reviewer-side, in reading the row before the flag.

### Cosmc is a pseudoenzyme, not a protein of unrelated fold

An early draft of this review asserted Cosmc has "no glycosyltransferase fold".
That is wrong, and the local UniProt record says so plainly:

- `SIMILARITY` — "Belongs to the glycosyltransferase 31 family. Beta3-Gal-T
  subfamily." The **same family as its client C1GALT1**.
- `CAUTION` — "Was originally (PubMed:12361956) assigned to be a
  glycosyltransferase. However, it was later shown (Ref.2 and PubMed:12464682)
  that it has no transferase activity and rather acts as a chaperone."

So Cosmc is a degenerate GT31 member that retains the family relationship while
having lost catalysis. This matters for the negation's value: family- and
sequence-based inference will keep proposing the activity *because* it is GT31,
and only an explicit `NOT` stops it.

Relevant to the project's `cazy2go` work, where GT31 is already flagged
`narrowMatch` as too heterogeneous to propagate at family level — a GT31 member
with zero activity is about as strong an argument for that flag as the family
can supply.

### ER, not Golgi — and by a mapped signal

Three GOA rows placed Cosmc in the Golgi. The compartment was inherited from its
client's reaction (Reactome models the Golgi-lumenal transfer). Cosmc's own ER
residence is not merely asserted in review prose:

- [PMID:21262965 "Here we show that the 18 amino acid transmembrane domain (TMD)
  of Cosmc is essential for ER localization and confers ER retention to select
  chimeras."]
- [PMID:21262965 "Moreover, mutations of a single Cys residue within the TMD of
  Cosmc prevent formation of disulfide-bonded dimers of Cosmc and eliminate ER
  retention."]
- [PMID:18695044 "We show that Cosmc is an endoplasmic reticulum (ER)-localized
  adenosine triphosphate binding chaperone that binds directly to human
  T-synthase."]

Note UniProt asserts only the generic "Membrane" and commits to neither
compartment, so correcting Golgi → ER does not contradict it.

### Chaperone activity is directly demonstrated

- [PMID:19923218 "These results show that mutated Cosmc is not as effective as
  soluble wild-type Cosmc in this in vitro assay in assisting refolding activity
  of T-synthase."] — in vitro refolding on purified protein, which isolates
  chaperone activity from any catalytic contribution.
- [PMID:21496458 "These results indicate that Cosmc mediates the co-translational
  activation of C1GalT"]

`GO:0044183 protein folding chaperone` is the term used. **Not** `GO:0051082
unfolded protein binding`, which an OpenScientist run recommended: that term is
obsolete (QuickGO returns "obsolete unfolded protein binding"), a known problem
tracked in issue #2222.

### Open question carried into the review

Whether a dedicated single-client chaperone should carry `involved_in` on the
process it enables. GOA itself is unsettled — it uses `involved_in` on two rows
and `acts_upstream_of_or_within` on a third. The existing rows are accepted, but
`core_functions.directly_involved_in` is deliberately **not** asserted: Cosmc
catalyses no step and contributes neither structure nor cofactor activity to the
glycosyl transfer, which is the same standard used to demote GCNT1's leukocyte
tethering and C1GALT1's angiogenesis in this batch.

### Provenance of the two OpenScientist runs

`function-hypothesis-go-0016263` (verdict SUPPORTED) and
`function-hypothesis-go-0000139` (verdict refuted, i.e. not Golgi). The first
supplied the GT31 correction above; the second surfaced PMID:21262965. Both
reports' claims were re-checked against local records before use, and both
carry `reference_review` notes recording what each got wrong as well as right.
