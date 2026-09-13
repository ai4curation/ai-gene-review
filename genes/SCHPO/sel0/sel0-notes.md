# sel0 (SPAC20G4.05c) — S. pombe — curation notes

## Identity (verified from UniProt record)

- PomBase standard name: **sel0**; systematic name: **SPAC20G4.05c**
- UniProt: **O13890** (`SELO_SCHPO`), 568 aa, `PE 3: Inferred from homology`
- RecName: **Protein adenylyltransferase SelO, mitochondrial**; AltName: Selenoprotein O (SelO); EC 2.7.7.-
- **This is Selenoprotein O / SelO, NOT a Sel1-repeat / SEL1L-related ERAD protein.** The task
  brief hypothesized a "Sel1-repeat / SEL1L-related" ERAD-adjacent protein; the UniProt record
  (Pfam PF02696 SelO, InterPro IPR003846 SelO, HAMAP MF_00692 YdiU_SelO, PANTHER PTHR32057
  "PROTEIN ADENYLYLTRANSFERASE SELO, MITOCHONDRIAL") unambiguously identifies it as a member
  of the **SELO family** of protein-tyrosine/Ser/Thr AMPylases (pseudokinase-fold
  nucleotidyltransferases). The "sel0" symbol = "SelO", not "Sel-zero" or a Sel1 relative.
  All ERAD/glycoprotein-QC framing from the brief is discarded as mistaken.

## Domain / sequence reasoning (inline, from `sel0-uniprot.txt`)

- **Pfam PF02696 (SelO)** spanning the chain; **InterPro IPR003846 (SelO)**; **HAMAP MF_00692
  (YdiU_SelO)** — this is the bacterial-to-eukaryote-conserved SelO/YdiU family.
- **Pseudokinase (protein-kinase-like) fold**: SelO adopts a protein-kinase-like fold but with
  ATP "flipped" in the active site, enabling AMP transfer instead of phosphotransfer
  [PMID:30270044 abstract, "The crystal structure of a SelO homolog reveals a protein / kinase-like fold with ATP flipped in the active site"].
- **ATP-binding site**: multiple UniProt BINDING features for ATP (residues 120, 122, 123, 144,
  156, 157, 208, 215, 297) transferred by similarity from the bacterial homolog (Q87VB1) →
  supports GO:0005524 ATP binding.
- **Mg2+ cofactor / metal binding**: BINDING features for Mg(2+) at 288 and 297; UniProt COFACTOR
  Mg(2+) → supports GO:0046872 metal ion binding. ACT_SITE 287 "Proton acceptor".
- **Mitochondrial targeting**: N-terminal TRANSIT peptide (`FT TRANSIT 1..?  /note="Mitochondrion"`),
  KW Mitochondrion, Transit peptide → supports mitochondrial localization.
- **Disulfide bond** KW: "Forms probably one or more intrachain disulfide bridges" (by similarity)
  — consistent with a redox-linked role, though the pombe disulfides are inferred not observed.

## What is KNOWN (about the SelO family / orthologs) vs NOT known for S. pombe sel0

### KNOWN (family/ortholog level; strong homology basis)
- **SelO is a protein AMPylase (adenylyltransferase)**: transfers AMP from ATP to Ser/Thr/Tyr
  residues of target proteins. Demonstrated experimentally for the SelO family (bacterial homolog
  crystal structure + human/yeast enzymes) [PMID:30270044 abstract, "we show
  that the highly conserved pseudokinase selenoprotein-O (Sel / O) transfers AMP from / ATP to Ser, Thr, and Tyr residues on protein substrates (AM / Pylation)"].
- **SelO localizes to mitochondria** [PMID:30270044 abstract, "SelO pseudokinases localize / to the mitochondria"; PMID:40849408, "Selenoprotein O (SelO), which is localized in the mitochondria"].
- **SelO AMPylates redox-homeostasis proteins and is required for the oxidative-stress response**
  [PMID:30270044 abstract, "and AMPylate proteins involved in redox homeostasis. Consequently, SelO activity / is necessary for the proper cellular response to oxidative / stress"].
- **Family is deeply conserved** — bacteria (E. coli YdiU), S. cerevisiae, human — and in
  E. coli / S. cerevisiae SelO "catalyzes AMPylation to protect cells from oxidative damage and
  cell death" [PMID:40849408, "SelO is conserved in E. coli and S. cerevisiae, where it catalyzes AMPylation to protect cells from oxidative damage and cell death"].
- **Mammalian SelO substrates include mitochondrial metabolic enzymes** (glutamate dehydrogenase,
  pyruvate dehydrogenase), regulating metabolic flux [PMID:40849408 abstract, "mammalian
  Selenoprotein O regulates metabolic flux through AMPylation of key mitochondrial proteins including glutamate / dehydrogenase and pyruvate dehydrogenase"].

### NOT known specifically for S. pombe sel0 (knowledge gaps)
- **No S. pombe-specific experimental data.** UniProt `PE 3: Inferred from homology`; every GOA
  annotation for O13890 is electronic/by-similarity (IBA, IEA, ISO, ISS) or curator inference (IC).
  Neither PMID:30270044 (E. coli/S. cerevisiae/human) nor PMID:40849408 (mammalian) assays the
  fission-yeast protein.
- **AMPylase activity of sel0 has not been demonstrated in vitro or in vivo in S. pombe** — it is
  inferred from orthologs. Whether the pombe active site is catalytically competent is untested
  (though catalytic ACT_SITE 287 and the Mg2+/ATP residues appear conserved by the similarity
  transfer).
- **In-vivo substrates in S. pombe are unknown.** The specific redox/metabolic proteins AMPylated
  in fission yeast, if any, have not been identified.
- **Loss-of-function phenotype in S. pombe is uncharacterized** — no reported growth, oxidative-
  stress-sensitivity, or metabolic phenotype for a pombe sel0 deletion in the cached literature.
- **The biological role (oxidant detoxification vs metabolic regulation vs other) in S. pombe is
  inferred, not established.** The GO:0098869 "cellular oxidant detoxification" annotation is an
  IC (Inferred by Curator) call built on the ISS AMPylase inference, not on a pombe phenotype.

## Reference adjudication notes

- **PMID:30270044** (Sreelatha et al. 2018, Cell) — foundational SelO-AMPylation paper. Abstract-
  only in cache (`full_text_available: false`) but the abstract itself contains the key claims.
  Relevance HIGH, correctness VERIFIED (PubMed title matches).
- **PMID:40849408** (Gonzalez et al. 2025, Nat Commun) — full text cached. Confirms mammalian SelO
  mitochondrial AMPylation of metabolic enzymes; conservation statement. Relevance HIGH/MEDIUM,
  VERIFIED.
- **PMID:9700395** — "Education and research: where are we going?" (Niethe G, Aust Vet J 1998,
  Editorial). This is a **veterinary editorial with no connection to SelO or AMPylation**. It
  appears in GOA as the reference for one ISO AMPylase annotation (WITH/FROM `UniProtKB:P31040`).
  This is a spurious/erroneous PMID in the GOA source (right-format id, wrong paper — it cannot
  support the AMPylase annotation). Per project policy I do NOT rewrite the GOA id, but I flag it
  via `reference_review` (correctness: WRONG_IDENTIFIER) and treat the annotation itself as still
  supportable on the strength of the other AMPylase-activity evidence lines. Note P31040 is
  succinate dehydrogenase flavoprotein (SDHA) — plausibly a SelO substrate/interactor context, but
  the *citation* is wrong regardless.

## Annotation plan (10 GOA rows)

- GO:0070733 AMPylase activity — the molecular function. Multiple lines (IBA, IEA-Rhea, ISO×3,
  ISS). ACCEPT the family-level MF; this is the core function. Keep all lines (do not REMOVE
  by-similarity lines that are biologically sound).
- GO:0005739 mitochondrion — location (IBA, IEA-SubCell, ISS). ACCEPT; well supported by transit
  peptide + ortholog localization. Core location.
- GO:0005524 ATP binding — not in GOA rows list but present as UniProt DR (IEA-KW). (Only GOA rows
  are reviewed; ATP/metal binding appear in core_functions as supporting MFs.)
- GO:0098869 cellular oxidant detoxification (IC) — biological process; supported by ortholog
  phenotype (oxidative-stress response). KEEP_AS_NON_CORE / ACCEPT as a reasonable curator
  inference, but note it is inferred, not demonstrated in pombe.

## Falcon deep research
- `just deep-research-falcon SCHPO sel0` via `python3` (system 3.9.5) fails: wrapper uses
  `dict | None` PEP-604 syntax needing py>=3.10. Re-ran via `uv run python scripts/deep_research_wrapper.py`
  (py3.12). Awaiting result; grounding here is from UniProt + GOA + the two primary papers so the
  review is complete regardless.

## Falcon deep research (completed)

`sel0-deep-research-falcon.md` completed (duration ~857s, 23 citations). The `just`
wrapper reported "timed out after 600s" and the perplexity-lite fallback 401'd on quota,
but falcon itself wrote a genuine, cited report directly (its own timeout was null). Key
corroborating points (all consistent with the review; not used to add uncited claims):

- Confirms identity as the fission-yeast SELO-family ortholog; the S. cerevisiae ortholog
  is **Fmp40**. Direct S. pombe literature remains limited; function is inferred from
  E. coli, S. cerevisiae (Fmp40), P. syringae and human orthologs.
- Reiterates the flipped-ATP pseudokinase mechanism, Mg2+ cofactor, and Ser/Thr/Tyr
  AMPylation.
- Ortholog substrates span redox enzymes (glutaredoxins, thioredoxin Trx3, peroxiredoxin
  Prx1) and metabolic enzymes (glutamate dehydrogenase, pyruvate dehydrogenase) — supports
  the "redox homeostasis + metabolic regulation" framing and the substrate knowledge gap.

The core review is grounded in UniProt + GOA + the two cached primary papers (PMID:30270044,
PMID:40849408); the falcon report is retained as supporting deep-research provenance.

## Reassessment — 2026-09-05: phenotype evidence and hypothesis limits

This entry supersedes the earlier blanket statements that no pombe phenotype or
experimental data exist. The live [PomBase sel0 record](https://www.pombase.org/gene/SPAC20G4.05c)
was checked via its gene-data API on 2026-09-05. Its curated, high-throughput
`sel0delta` records include:

- Sensitivity to diamide, FYPO:0000799, annotation 398214: 3 mM diamide at
  32°C, prototrophic background, cell-growth assay [PMID:37787768;
  PomBase annotation 398214, "sensitive to diamide"].
- Resistance to tert-butyl hydroperoxide, FYPO:0003383, annotation 321729:
  1.5 mM at 32°C, cell-viability assay, reported `fitness_log2(0.0367)`
  [PMID:34984977; PomBase annotation 321729, "resistance to tert-butyl hydroperoxide"].
- Resistance to phloxine B and hydrogen peroxide, FYPO:0009046, annotation
  319831: 10 mM peroxide, 2x phloxine B at 32°C, cell-growth assay,
  reported `fitness_log2(0.175)` [PMID:34984977; PomBase annotation 319831,
  "resistance to phloxine B and hydrogen peroxide"]. This is a combined-condition
  result, not an isolated peroxide-resistance measurement.
- Loss of viability in stationary phase, FYPO:0000245, annotation 317223,
  cell-growth assay [PMID:34250083; PomBase annotation 317223,
  "loss of viability in stationary phase"].

These phenotype directions and assay conditions must remain distinct. They
support condition-dependent stress/viability effects, but do not identify the
AMPylated substrates or demonstrate direct oxidant detoxification. The remaining
question is the mechanism connecting the inferred enzyme activity to these
phenotypes, rather than whether a phenotype exists at all.

The title of PMID:34984977 foregrounds lincRNAs, but its abstract explicitly
includes "diverse coding-gene mutants for functional context". Thus the title
is no basis for disputing PomBase's coding-gene phenotype records. The full text
was fetched with `just fetch-pmid 34984977 32966796`; PMID:34984977 has full text,
whereas PMID:32966796 is abstract-only. Gene-specific phenotype provenance above
is the curated PomBase record, not a claim that sel0 appears in article prose.

The [OpenScientist hypothesis report](sel0-hypotheses/catalytic-competence/openscientist.md)
must not be treated as a reproduced sequence
or structural analysis: the delivered report lacks the executable evidence needed
to validate its exact conservation, pLDDT and pocket-distance numbers. Its proposed
bacterial-UMPylation/eukaryotic-AMPylation split is too categorical. The bacterial
YdiU study explicitly reports "the self-AMPylation of YdiU padlocks" its chaperone
UMPylation activity [PMID:32966796, abstract]. This supports testing nucleotide
and substrate specificity rather than assuming a kingdom-exclusive reaction.

The linked correction was also fetched and read [PMID:35085068]. It replaces
Figure 4A's left graph with the lincRNA-mutant data and adjusts Figure 4C's
axis. It does not report changes to the sel0 phenotype records; the correction
states that the conclusions are unchanged. Its cached text is present even
though the metadata flag says full text unavailable; this note relies on the
actual correction text, not that flag.

### Ortholog identity and source-specific assertions

UniProt Q08968 was rechecked directly: `SELO_YEAST`, `Name=FMP40`,
`OrderedLocusNames=YPL222W`, Saccharomyces cerevisiae S288c. The earlier
review's description of this ISS source as human was wrong
[UniProt:Q08968, "Name=FMP40"].

PomBase's `has_input` extensions explain the ISO WITH/FROM entities. They are
substrate orthologs in these assertions, not evidence that a metabolic enzyme
was mistaken for the AMPylase:

| PMID | Annotation | WITH/FROM | Pombe substrate in `has_input` |
| --- | --- | --- | --- |
| 30270044 | 75261 | UniProtKB:P68688 | SPAC4F10.20 |
| 40849408 | 75262 | UniProtKB:P26443 | SPCC622.12c |
| 40849408 | 75263 | UniProtKB:Q9D051 | SPBC30D10.13c |
| 9700395 | 75264 | UniProtKB:P31040 | SPAC1556.02c |

The first three assertions can be assessed as orthology-based substrate claims,
with species-specific experimental limits retained. PMID:9700395 remains an
independently verified wrong identifier. Its source-specific assertion should
be UNDECIDED pending the intended primary reference, while other evidence still
supports the core AMPylase function. This supersedes the earlier plan to accept
that row solely because the broad molecular function is independently supported.
The two PMID:40849408 source rows must be reviewed separately after supported
GOA seeding restores their distinct identities.

### Evidence depth for the two metabolic-substrate sources

The cached full text of PMID:40849408 was re-read around Figure 6. Glud1 has
stronger mechanistic follow-up than PdhB in the article text: the study compares
active SelO with D338A, immunoprecipitates tagged Glud1, detects AMPylated Glud1
peptides by mass spectrometry, and measures reduced glutamate-dehydrogenase
activity. PdhB is a candidate recovered in the enrichment analysis and Figure 6C;
the Glud1-specific site and activity experiments must not be attributed to PdhB.
Both are mammalian results, so their pombe substrate assertions remain orthology
inferences [PMID:40849408, Figure 6/results, "Among our top candidates is Glud1";
"β subunit of pyruvate dehydrogenase E1 complex"].

## Source migration and completed row assessment — 2026-09-05

After wrapper PR #2926 merged, this branch was rebased onto main and
`just fetch-gene SCHPO sel0 --force` fetched 11 GOA assertions, restored one
missing source row, and backfilled supporting entities on ten prior rows.
All 11 source assertions and the pre-existing proposed protein-adenylylation
annotation now have explicit review decisions; none remains PENDING.

The P26443 and Q9D051 PMID:40849408 rows were reviewed separately with their
PomBase substrate contexts and the unequal depth of mammalian follow-up noted.
Both retain ISO and ACCEPT; neither claims a direct pombe assay. The
PMID:9700395 substrate assertion remains UNDECIDED despite independent support
for the broad AMPylase function. The workflow status remains DRAFT because
advisory validation issues remain, not because a source was left unreviewed.
