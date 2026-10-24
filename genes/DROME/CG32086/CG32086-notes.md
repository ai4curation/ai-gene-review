# CG32086 (M9NF85): evidence and ProtNLM claim review

CG32086 is a 475-residue EFHB-related protein with a C-terminal EF-hand domain. Its architecture is compatible with a calcium-responsive regulatory role, but calcium binding, a ciliary function, and the precise cellular location of this fly product remain unresolved.

Exact input: [M9NF85](https://www.uniprot.org/uniprotkb/M9NF85/entry), 475 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG32086-predictions-source.json](CG32086-predictions-source.json). Source features: [CG32086-uniprot.txt](CG32086-uniprot.txt), with an exact extraction in [CG32086-sequence-evidence.json](CG32086-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR057428; EFHB_EF-hand_C.
FT   DOMAIN          399..469
FT                   /note="EFHB C-terminal EF-hand"
FT                   /evidence="ECO:0000259|Pfam:PF25325"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | EF-hand domain-containing family member B | CNN | The EFHB C-terminal EF-hand domain PF25325 at residues 399-469 supports the EFHB-family name. This does not establish a calcium-signaling mechanism or specific substrate. |
| Location | Cytoskeleton (SL-0090) | UNC | The EFHB-family architecture does not independently establish attachment to the cytoskeleton. Direct localization or a functionally justified ortholog transfer is required. |
| Location | Cilium axoneme (SL-0304) | UNC | An EF-hand and EFHB-like sequence are insufficient to specify cilium axoneme residence. No exact-target ciliary localization or assembly phenotype is established by the retrieved source record. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

The accession-specific GOA fetch contains no existing annotation rows. The molecular activity remains unresolved; no broad GO root or invented function is added to create apparent coverage.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG32086-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This section was written without consulting any ProtNLM2 output; the earlier sections are left as they were.
Analysis: [CG32086-bioinformatics/RESULTS-rereview.md](CG32086-bioinformatics/RESULTS-rereview.md)
(script `compare_sequences_rereview.py`, raw output `RESULTS-rereview-raw.txt`).

### Identity of the benchmark accession
- FBgn0052086 has three TrEMBL entries and no Swiss-Prot entry: M9NF85 (475 aa, benchmark), Q8IQG0
  (491 aa, CG32086-RA / NP_729720.1 / FBpp0075878) and Q8T4E3 (245 aa, cDNA AT02370p, truncated before
  the EF-hand domain).
- M9NF85 is an **alternative splice isoform**, not a fragment: it matches Q8IQG0 exactly except that
  residue N234 replaces the 17-residue segment KYTFAVPDITFGVPLRS (Q8IQG0 234-250), so it is 16 residues
  shorter. The PF25325 EFHB C-terminal EF-hand domain (M9NF85 399-469) is intact. No catalytic residues
  are at stake (the protein is not an enzyme).
- Q8IQG0 is the gene's canonical/representative product: PANTHER uses it and GOA attaches the gene's five
  IBA rows to it (GO:0005879, GO:0061891, GO:0030317, GO:0070884, GO:2001256). M9NF85 has no GOA rows.

### Evolutionary placement
- PANTHER 19.0 fruit-fly classification puts FBgn0052086 (via Q8IQG0) in PTHR12086:SF12, EF-HAND
  DOMAIN-CONTAINING FAMILY MEMBER B, with human/mouse/bovine EFHB (CFAP21) and two fly paralogs
  (FBgn0053489, FBgn0053490; both CG6110 products). Fly Efhc1.1/Efhc1.2 sit in SF11. Alliance orthology
  lists human, mouse, rat and frog EFHB as orthologs (PANTHER among the methods).
- M9NF85 is ~48% identical to the two fly SF12 paralogs over its full length and 28% identical to human
  EFHB over human residues 252-708; the human N-terminal 251 residues have no fly counterpart.
- PROSITE PS00018 scan: human EFHB has one canonical calcium-binding loop (610 DVDNDGFINYLE); none of the
  fly SF12 proteins (including M9NF85) has one.
- PAINT (interpro/panther/PTHR12086/PTHR12086-paint.tsv): axonemal microtubule GO:0005879 is placed at
  PTN000250051 with nine experimental seeds across EFHC1, EFHC2 and EFHB; calcium ion sensor activity and
  regulation of SOCE are at PTN004335498 seeded by human EFHB alone; calcineurin-NFAT regulation and
  cilium-dependent motility at PTN000949412 (Eumetazoa).
- No PANTHER family review (FamilyReview YAML) exists for PTHR12086 under interpro/panther/, only the
  fetched entries/metadata/PAINT files, so there is no subfamily-placement disagreement to report. Note
  that the M9NF85 UniProt entry has no PANTHER cross-reference; placement is gene-level.

### Literature
- Falcon deep research (2026-09-10) found no CG32086-specific primary literature. Bgee: expressed in
  mid-late elongation-stage spermatids. Human EFHB curated UniProt function: axonemal doublet microtubule
  MIP (PMID:36191189, cryo-EM of human cilia) and a calcium sensor modulating STIM1-ORAI1/SOCE
  (PMID:30481768, a single cell-line study; not cached).

### Decisions
- No existing annotations to review for M9NF85.
- NEW: GO:0005879 axonemal microtubule (is_active_in, ISS): family-wide PAINT node, gene in the EFHB
  subfamily, spermatid expression; isoform difference does not touch a domain. Recorded as a prediction.
- Not proposed: calcium ion sensor activity, regulation of SOCE, regulation of calcineurin-NFAT signaling.
  The fly protein lacks a canonical Ca-binding loop and those rest on one human study; flagged as a
  suggested question for the Q8IQG0 IBA rows. Not proposed: any motility process term (organismal/phenotype
  level, no fly data).
- Description rewritten to state isoform identity, subfamily, absence of a canonical Ca loop and
  absence of experimental data.

### Relative to review next
Q8IQG0 (CG32086-RA), the canonical product of the same gene, has no review in the repo
(would be genes/DROME/CG32086__Q8IQG0 because genes/DROME/CG32086 is keyed to M9NF85). The closest
characterised relative by phylogeny is human EFHB (Q8N7U6, PTHR12086:SF12), also not yet reviewed.
No modules mention CG32086 or EFHB.

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0005879) on this accession. GOA already carries the same terms on
another product of the same gene, reviewed in `genes/DROME/CG32086__Q8IQG0/`. GOA propagates gene-level
annotations to one representative product per gene, so adding them to a second product fills a
convention rather than a curation gap. The rows were withdrawn, following the rule applied across the
ProtNLM2 re-review cohorts (first raised in the review of PR #5303). The gene-level function is unchanged.
