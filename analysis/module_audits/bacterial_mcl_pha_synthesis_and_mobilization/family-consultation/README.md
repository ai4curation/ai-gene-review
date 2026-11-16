# Medium-chain PHA family consultation

This scoped audit creates PTHR36837 and PTHR43433 reviews and updates the relevant
PHA judgments in existing PTHR43194 and PTHR43798 reviews. The pre-edit baseline
captures all 13 existing family files before acquisition or curation, including
both existing review documents. No existing metadata, member list, PAINT slice,
publication, provider file or gene review was rewritten.

## Biological conclusions

| Family | Positive anchors | Boundary and judgment |
| --- | --- | --- |
| PTHR36837 | KT2440 Q88D25/Q88D23 and GPo1 P26494/P26496 class II synthases; C. necator P23608 class I synthase | SF5 contains both class I and II. The official PHB label is not universal mcl specificity, nor does class I imply absolute exclusion of longer substrates. Other unresolved branches prevent a universal functional grant. |
| PTHR43194 | KT2440 O85207 and PAO1 Q51553 PhaG; E. coli BioH P13001 | SF5 also contains BioH and RhlA. PhaG transfer is supported, but neither universal PhaG/BioH specificity nor absence of secondary hydrolysis is established. Prior categorical PhaG hydrolase/BioH exclusions and definitive BioH node pruning are withdrawn. |
| PTHR43433 | KT2440 Q88D24 PhaZ, with qualified KT2442 biochemical evidence; M. tuberculosis LipJ O07732 | SF5 is broader than intracellular PHA depolymerases. Polyester hydrolysis is not glycerolipid hydrolysis; no unsupported secondary-TAG negative assay is inferred. LipJ cyclase activity belongs to an additional domain, not every hydrolase-family protein. |
| PTHR43798 | Human ABHD6 Q9BV23; GPo1 PhaZ P26495 | Official SF5 contains both. Its ABHD6 label is preserved but no universal monoacylglycerol activity is granted. Positive ABHD6 activity remains valid; native PhaZ turnover neither establishes nor excludes secondary MAG hydrolysis. |

PTHR36837 SF4 includes Q8PAX3, whose PHB-depolymerase name is **submitter-only
ECO:0000313**. It is a scope question, not a verified synthase-to-hydrolase
transition. The old unchecked InterPro LLM family description is not functional
evidence. A bacterial/archaeal or class label is never used as a universal
substrate-positive or substrate-negative rule.

PhaG's purified CoA-to-ACP transfer is directly reported (PMID9727022 and the
PMID12200450 evidence discussed in the literature consultation). PMID35338129
uses product sinks and FadD controls favoring forward ACP-to-CoA transfer, but
explicitly states that forward in-vitro acyl-ACP data are unavailable. The
hydroxyacid/ligase phenotype in PMID22101037 does not uniquely distinguish
intrinsic PhaG hydrolysis from downstream endogenous thioesterases. This audit
does not present forward purified kinetics, obligate CoA-ligase coupling or an
absolute absence of secondary hydrolysis. Native PAO1 gluconate versus fatty-acid
phenotypes support conditional precursor routing, not universal PhaG necessity.

PMID17170116 and the actual constructs in PMID41055782 concern KT2442 PhaZ,
including E. coli expression, despite the latter title naming KT2440. GPo1 is a
polymer donor in those experiments. Q88D24 target chemistry therefore retains
homolog/domain/pathway qualification. Native GPo1 PhaZ turnover is independently
supported by a leaky mutant and rescue fragment containing **phaC1 plus phaZ**;
that is not purified single-enzyme, product-resolved evidence. The GPo1 gene
review therefore remains broader than exact GO:0050527 chemistry; the family
assessment likewise does not grant that precise activity to P26495. Intracellular
storage-granule mobilization is distinct from secreted attack on extracellular
polymer, and granule interaction does not establish lipid-bilayer membrane
location.

## Actual phylogenetic scope

Official snapshots are retained with retrieval URLs and hashes. The four current
reference trees contain 17, 106, 70 and 147 leaves respectively. These are not
complete species inventories or evidence counts. PAINT means a historical node
judgment, not a pairwise donor transfer.

PTHR43194 PTN002455972 has 17 reference descendants spanning BioH, PhaG/RhlA and
RsbQ. PAO1 Q51553 is an actual reference leaf beneath it. BioH is positive, while
the specific chemistry and biotin participation of all descendants remain
unresolved; a different established pathway role does not prove catalytic loss.

PTHR43433 PTN001335022 has 13 reference leaves, including the LipG seed and the
P. aeruginosa PhaZ relative G3XD91. Its precise TAG/glycerolipid scope remains
unresolved. PTN005163452 has three reference descendants and includes the
experimentally curated bifunctional LipJ seed; the additional cyclase domain is
not automatically transferred to the whole family. Some other raw PAINT nodes
are absent from the current family tree, and their reach is explicitly unresolved.

PTHR43798 PTN002465558 has 49 reference leaves beneath the 64-leaf
PTN008685307 and 134-leaf PTN001661081. P26495 itself is absent from the reference
leaf set. Its SF5 assignment is verified in raw entries and official UniProt;
this does **not** independently reconstruct its exact TreeGrafter graft. No
invented pruning point or catalytic residue discriminator is supplied. The prior
MAG/acylglycerol TOO_DEEP judgments relied on absence of assays; they now remain
UNRESOLVED while retaining positive ABHD6 evidence. Unrelated AcoC, membrane,
AMPA-receptor and other historical judgments are untouched.

Normal `fetch-panther-paint PTHR36837` resolved 30 nodes but found no node-level
annotations. No PAINT slice was created, and no synthetic ancestral assertions
were added. The failed expectation of a missing slice does not mean evidence of
biological absence.

## Preserving the independent AcoC judgment

PTHR43194's prior AcoC Q88QE1 hydrolase exclusion is unrelated to the PhaG change
and remains a **current negative scientific judgment**, with exact member, term,
reason and quoted support in `current-member-judgments.yaml`. Its quoted support
and conclusion also remain live in the family term assessment's prose.
`prior-term-assessments.json` separately preserves the exact historical objects.
The PhaG exclusion is explicitly withdrawn; it is not confused with AcoC.

LinkML schema validation itself permits an exception under UNRESOLVED, but the
production `family_gene_crosscheck.check_member_exceptions` rejects it with:

> EXCEPTION_OUTSIDE_SCOPE: member exception on a UNRESOLVED term: exceptions only carve members out of a FAMILY_WIDE or SUBFAMILY_ONLY scope

`exception-rule-control.json` records the exact observed conflict, and the
preservation checker reproduces it in memory without modifying the family file.
There is no current independent negative-member slot in FamilyReview. Thus the
negative is retained machine-readably in the active consultation ledger, but the
**production family/gene cross-check no longer enforces it**. This limitation is
explicit; a false universal hydrolase grant was not retained merely to satisfy
representation. The existing PTHR43798 AcoC exception remains live and completely
unchanged because that unrelated term assessment was not altered.

## Preservation and validation

The checker verifies all 59 root-protected sources and all 11 pre-existing raw
family files; the original review baselines remain exact. All 15 original review
PAINT assertion objects preserve identifier, term, evidence, polarity, seeds,
taxon and date. Ten unrelated node objects are entirely unchanged. The seven
new PTHR43433 assessments exactly copy their raw source assertions. Old review
seed lists differ from newer raw slices in some places; neither source was
silently synchronized or rewritten. Existing official family/subfamily labels
and representative-member objects are retained.

Four scoped schema, term, quote, member/PTN/residue and family/gene cross-checks
are recorded in this directory. The local preservation checker independently
checks all 29 unique quoted source/document combinations, including local/JSON
sources skipped by the publication-only phase. Manual source availability and
section provenance are recorded in `reference-assessments.yaml`, since the family
schema lacks the gene review's reference-review and record-section slots.
Generated `just new-history` records are append-only and individually validated.
There is no family HTML renderer in this checkout.

`curate.py` constructs the targeted documents from the immutable baseline; do
not rerun it after release as a routine verification step. Reproduce checks with:

```sh
uv run python analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/family-consultation/check_preservation.py
uv run ruff check analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/family-consultation
```

The one authorized member-index refresh is shared infrastructure, not a committed
source. No module/gene/project changes, full-corpus run, commit or push belong to
this consultation.

The class I boundary is additionally grounded in primary10612741: its accessed
abstract reports C8/C12 comonomer incorporation in engineered E. coli. This is
PHB-rich copolymer synthesis, not pure-mcl polymer or native H16 turnover. The
separate class-I consultation supplies the exact H16 accession/archive bridge.

Final shared-index grounding: **95 pass, 0 fail, 0 unresolved** for these four
families. Final family/gene cross-check: **0 conflicts, 0 unresolved, 3 consistent**.
The shared repository index resolves6,887/7,110 accessions; its223 unresolved
repository-wide references are not unresolved groundings in this scoped check.
