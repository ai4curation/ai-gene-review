# Rv2887 (P9WME9) — curation notes

## 2026-10-21 — Full review, independent of the ProtNLM2 predictions

New gene folder; no prior notes existed. This review was written without opening
any ProtNLM2 prediction file, per the campaign rules.

### Deep research

`just deep-research-falcon MYCTU Rv2887` failed: the falcon provider exited with
`Exception: Failed to authenticate`, and the perplexity fallback returned HTTP 401
(`insufficient_quota`). No `-deep-research-*.md` file was produced. The review is
therefore built from the three primary papers cached in `publications/` plus the
UniProt record.

### Evidence base

Cached publications:

- `publications/PMID_26303802.md` — abstract only (`full_text_available: false`).
- `publications/PMID_27432954.md` — full text recovered from PMC on a retry.
- `publications/PMID_28743871.md` — full text from PMC.

Key experimental facts in *M. tuberculosis* H37Rv itself:

- Rv2887 represses *Rv0560c* (htm). Loss-of-function alleles give the largest
  transcript increase in the mutant RNA-seq: [PMID:27432954 "The gene with the
  largest increase in expression—∼400-fold—was rv0560c , annotated as a putative,
  nonessential benzoquinone methyltransferase."]. The authors state the model
  explicitly: [PMID:27432954 "Based on these data, we predicted a model in which
  Rv2887 acts as a repressor of rv0560c"].
- Direct, specific operator binding, with a negative control:
  [PMID:27432954 "Rv2887 did not bind to a 36-bp region corresponding to the
  promoter region of an IdeR-regulated gene, mbtB (mbtB-prom)"], and
  [PMID:27432954 "Introduction of the R81Q mutation into Rv2887 abolished its
  ability to bind 560c-prom DNA"].
- The operator is a 27-bp site defined by DNase I footprinting:
  [PMID:28743871 "identified a specific 27 bp DNA sequence,
  CGTCAGCTGAACGGCGGTCGTCGATCG, which is protected by Rv2887 protein"].
- Ligands bind two per dimer at the dimer interface:
  [PMID:28743871 "Two molecules of SA/PAS bind Rv2887 in two deep symmetry-related
  pockets at the dimerization interface, where each ligand interacts with residues
  from both protomers."], and ligand binding releases DNA:
  [PMID:28743871 "addition of SA or PAS to the Rv2887-DNA complex resulted in loss
  of the retarded band, indicating separation of the protein and DNA components"].
- Architecture: [PMID:28743871 "Each subunit is composed of two functional domains:
  helices α1, α5, and α6 form the dimerization domain, and helices α3 and α4 form a
  helix-turn-helix (HTH) DNA-binding domain."]. Structures: PDB 5HSM, 5HSO, 5X7Z,
  5X80.
- Wider regulon, from the abstract of the earlier study:
  [PMID:26303802 "We found that genes involved in benzoquinone and menaquinone
  biosynthesis were repressed by functional Rv2887."]. Only the *Rv0560c* operator
  has been mapped, so the rest of the regulon may be indirect — recorded as a
  suggested question rather than asserted.

### Evolutionary grounding

- PANTHER family PTHR33164 (MarR family), subfamily PTHR33164:SF43
  ("HTH-TYPE TRANSCRIPTIONAL REPRESSOR YETL"), per the UniProt DR lines.
- Both IBA rows descend from PAINT node PTN002109389
  (`interpro/panther/PTHR33164/PTHR33164-paint.tsv`): GO:0006355 from an eight-donor
  IBD including *E. coli* MarR (P27245), and GO:0006950 from a two-donor IBD
  (P27245, O34777). Rv2887 descends from that node, so both propagations are sound.
  PAINT asserted only the unsigned GO:0006355 at that depth; the sign is supplied
  here from species-specific experiments, which is why the IBA row is MODIFY rather
  than a challenge to the node.
- Note for downstream transfer work: CHRVO/Q7NUH2 shares the SF43 subfamily
  assignment and the same PAINT node, but the global identity to Rv2887 is low
  (~29%). Family membership supports only the generic DNA-regulatory claim. The
  *Rv0560c* operator sequence, the salicylate/PAS response and the repression of the
  htm locus are Rv2887-specific findings and must not be transferred on subfamily
  membership alone.

### Actions taken

- `GO:0003700` (IEA) → MODIFY to `GO:0141096` ligand-modulated transcription
  repressor activity: the ligand-off switch is directly demonstrated.
- `GO:0006355` (IBA and IEA) → MODIFY to `GO:0045892`, consistently on both rows.
- `GO:0006950` (IBA) → KEEP_AS_NON_CORE. Defensible (a chemical cue is transduced
  into a transcriptional change) but peripheral, and no better term exists: the
  salicylic-acid response branch in GO is plant-defence-centric. Not TOO_GENERAL,
  because nothing else in this review entails a stimulus.
- Two NEW rows: `GO:0000976` transcription cis-regulatory region binding (IDA,
  footprint + co-crystal + EMSA with a negative control) and `GO:1901149` salicylic
  acid binding (IDA, ITC + two ligand-bound structures + R42A/D114A mutagenesis).
  Neither is an ancestor or descendant of another term in the review.

Deliberately **not** proposed: any term for drug susceptibility or for the
methylation reaction. The methyl transfer is performed by Rv0560c, not by Rv2887;
Rv2887 only sets the level of that enzyme, so under the "name the entity that
performs the step" test the process terms belong to Rv0560c.
