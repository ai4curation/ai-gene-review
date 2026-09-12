# BRIP1 (FANCJ) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 38 discoveries · self-eval pairwise = win (faith 100%) · gates passed = True.

## Agreement (brief)

The Affinage narrative and the curated AIGR review agree on BRIP1/FANCJ's core
biology, and Affinage's PMID-dense narrative is largely accurate and on-target:

- **5′→3′ Fe-S DNA helicase (Rad3/XPD family)** whose loss defines Fanconi anemia
  group J — matches AIGR `core_functions[0]` (GO:0043139) and the NEW 4Fe-4S
  cluster-binding annotation (GO:0051539).
- **G-quadruplex unwinding / replication-fork roadblock resolution** — matches
  `core_functions[1]` (GO:0160225), RPA-stimulated / MSH2-MSH6-inhibited.
- **BRCA1 BRCT partner (phospho-Ser990) in HR** and **BRCA1-independent MLH1
  (MutLα) interaction required for the ICL response** — matches the HR core
  function, the BRCA1-B complex (GO:0070532), and the NEW ICL-repair annotation
  (GO:0036297).
- **DNA-protein crosslink (DPC) repair via ATPase-driven adduct unfolding for
  SPRTN** — matches `core_functions[2]` (GO:0106300 / PMID:36608669).
- **Fe-S cluster and Q25 dimerization requirements, RPA cooperation** — consistent
  with AIGR notes.

Notably, **Affinage did NOT exhibit the BACH1 transcription-factor collision.**
Its entire narrative and all 40 PMIDs concern the FANCJ helicase (Q9BX63); none
belong to the unrelated bZIP repressor BACH1 (O14867). It never imported the
heme-oxygenase-1 / Nrf2 / cadmium-export material (PMID:14504288) that AIGR had to
strip from GOA. This is a point in Affinage's favor.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| GO grounding layer | `mechanism_profile` MF = ATP-dependent activity (GO:0140657), catalytic activity acting on DNA (GO:0140097), DNA binding, hydrolase activity, and **molecular adaptor activity (GO:0060090)** | Core MF is the specific **5′-3′ DNA helicase activity (GO:0043139)** + **G-quadruplex unwinding (GO:0160225)** + **4Fe-4S binding**; generic parents (hydrolase, nucleic-acid binding) marked over-annotated | **AIGR.** Affinage's own profile block is coarse (collapses to high-level parents) and its "molecular adaptor activity" is a wrong-branch call for a catalytic helicase. The Affinage file itself flags this layer as unreliable; the narrative + PMIDs, which AIGR grounds precisely, are the substantive content. |
| Enzyme class label | Narrative calls FANCJ a "DEAH-box" helicase | AIGR: Rad3/XPD (DinG) superfamily-2 Fe-S helicase | **AIGR (nuance).** "DEAH/DEAH-box" traces to the original 2001 discovery paper's family assignment (PMID:11301010) and is loosely used; FANCJ is mechanistically a Rad3/XPD-family Fe-S helicase, as AIGR states. Not a substantive conflict. |
| Transcriptional role | Cites PMID:31767869 (lncRNA REG1CP tethers FANCJ to the REG3A promoter via an RNA-DNA triplex; FANCJ unwinds dsDNA to permit GRα-driven transcription) as a "transcriptional regulatory role for FANCJ" | AIGR removed GO:0006357 (regulation of transcription by RNA Pol II) as a BACH1-alias mis-mapping | **AIGR (net).** The two are unrelated: AIGR's removal targeted the wrong-gene PMID:14504288, whereas Affinage's transcription hook is a genuine single-paper FANCJ finding but mechanistically just helicase activity applied at one promoter locus. It does not justify a sequence-specific transcription-regulation GO term; adding one would over-reach. Correctly excluded. |
| FANCD2/FANCI regulation | Emphasizes FANCJ directly binds/stabilizes FANCD2-FANCI and is reciprocally required for FANCD2 chromatin loading (PMID:25070891, 26336824, 20676667) | Not called out as a distinct annotation | **Draw / minor gap.** Well-evidenced but subsumed within the ICL/FA-pathway process (GO:0036297) already annotated; no clean separate GO term without over-reach. Left as narrative context. |
| Microsatellite-instability suppression / lymphoma predisposition | Highlights a FANCD2-independent MSI-suppression role and Fancj-null lymphoma (PMID:26637282, 27179029) | Captured only under general DNA repair / genome maintenance | **Draw.** Phenotype-level; maps to already-annotated GO:0006281 (DNA repair). No conservative new term warranted. |
| Meiotic recombination | Fancj mice: altered meiotic crossover processing, increased MLH1 foci/chiasmata (PMID:26490168) | Had GO:1990918 (DSB repair in meiotic recombination, IBA) but **without supporting text** | **Both — gap now closed.** AIGR already carried the term as KEEP_AS_NON_CORE; Affinage surfaced the direct ortholog evidence, now attached as `supported_by` (see below). |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:26490168 | GO:1990918 double-strand break repair involved in meiotic recombination (IBA, KEEP_AS_NON_CORE) | Added to `references` with `reference_review` (relevance MEDIUM, correctness VERIFIED); attached two verbatim `supported_by` snippets ("indicative of increased DSB repair via CO"; "MLH1 focus frequency is increased in Fancj (GT/GT) males") to an annotation that previously had none, and expanded the summary to note the ortholog-level meiotic evidence. |

- **NEW annotations added:** 0 (the well-supported functions Affinage foregrounds
  are already represented by existing `core_functions` / process terms; no
  additional real, correctly-branched GO term was warranted under a conservative
  pass).

## Net assessment

The AIGR review is materially complete and accurate; the reconciliation produced
one conservative improvement — an ortholog-level meiotic-recombination reference
(PMID:26490168) supplied by Affinage, which closed a genuine "annotation lacking
supporting text" gap on GO:1990918. Affinage's mechanistic narrative is strong,
PMID-dense, and — importantly — **free of the BACH1 transcription-factor
collision** that contaminated GOA; it stayed entirely on the FANCJ helicase.
Its weakness is the expected one: the self-reported `mechanism_profile` GO layer
is coarse and partly wrong-branch (e.g. "molecular adaptor activity" for a
catalytic helicase), which the AIGR curated MF grounding correctly supersedes.
The lone content over-reach — reading PMID:31767869 as a "transcriptional
regulatory role" — is appropriately excluded by AIGR, and is unrelated to the
earlier BACH1-alias transcription mis-mapping that AIGR had already removed.

Validation after edits: **✓ Valid** (single benign "no annotation references the
deep-research file" warning).
