# cas1 (Q02ML7) — Pseudomonas aeruginosa UCBPP-PA14 — curation notes

Deep research was unavailable in this environment (no provider API keys), so this file
is my own literature journal. Every assertion carries an inline PMID plus a verbatim
quote from the cached record in `publications/`.

## System context

PA14 carries a type I-F (Yersinia-subtype, "Csy") CRISPR-Cas system; `cas1`
(PA14_33350) is the integrase of its adaptation stage. Type I-F has no standalone
Cas2: [PMID:26586803 "A specific feature of type I-F systems is a fusion of cas2 and
cas3 homologs, which are encoded on separate genes in other CRISPR"]. UniProt records
this from the PA14 side as "This bacteria does not encode Cas2; Cas1 must interact with
a different protein to insert spacers (Probable)" — the partner is the Cas2 moiety of
the Cas2-3 fusion encoded by `cas3`.

Cas1 is the universal CRISPR protein:
[PMID:19523907 "cas1) encodes the only universally conserved protein component of
CRISPR immune systems"].

## Biochemistry (this protein, this strain)

PMID:19523907 is a study of the PA14 Cas1 protein itself (PDB 3GOD, cited by UniProt
for the FUNCTION, COFACTOR, ACTIVITY REGULATION and SUBUNIT lines):

- Catalysis and substrate specificity:
  [PMID:19523907 "the Cas1 protein is a metal-dependent DNA-specific endonuclease that
  produces double-stranded DNA fragments of approximately 80 base pairs in length"].
  Note "DNA-specific" — the generic `GO:0003676 nucleic acid binding` understates this.
- Metal dependence:
  [PMID:19523907 "The 2.2 A crystal structure of the Cas1 protein reveals a distinct
  fold and a conserved divalent metal ion-binding site"] and
  [PMID:19523907 "Mutation of metal ion-binding residues, chelation of metal ions, or
  metal-ion substitution inhibits Cas1-catalyzed DNA degradation"]. UniProt records
  Mn(2+)/Mg(2+) ligands at residues 190, 254, 268 from PDB 3GOD, with Mn(2+) supporting
  ss- and dsDNA cleavage and Mg(2+) only dsDNA, and inhibition by EDTA.
- Oligomeric state: UniProt SUBUNIT "Homodimer (PubMed:19523907)", and the IntAct
  self-interaction Q02ML7–Q02ML7 (NbExp=2) behind GOA's `GO:0042802` row.

The cached record for PMID:19523907 is abstract-only
(`full_text_available: false`), so I have quoted only the abstract; the residue-level
detail above is taken from the UniProt feature table, not invented.

## In vivo requirement for adaptation

The PA14 type I-F system was transplanted into E. coli and its adaptation genetics
dissected:
[PMID:26586803 "both modes require, in addition to Cas1 and Cas2, intact Csy complex,
an ortholog of the E. coli Cascade, and crRNA"]. The active-site requirement is
specific:
[PMID:26586803 "This is an expected result since D268 is a conserved metal coordinating
residue and substitution of the corresponding residue in E. coli Cas1 also abolishes
adaptation"] — i.e. the Cas1 D268A allele abolished spacer acquisition. This is the
grounding for the CACAO IMP on `GO:0043571`, and it is PA14 Cas1 that was mutated, so
the annotation is correctly attributed.

Cas1 is *not* part of the interference machinery:
[PMID:26586803 "Cas1 and Cas2 are not required for CRISPR interference (22)"]. That
matters for the `GO:0051607` call below.

## Curation decisions

- `GO:0003676 nucleic acid binding` (IEA, InterPro) → MODIFY to `GO:0003677 DNA
  binding`. The protein is explicitly DNA-specific by direct assay (quote above), and
  UniProt carries the `DNA-binding` keyword. The generic parent loses the one piece of
  specificity that was actually measured.
- `GO:0004519 endonuclease activity` (IEA, UniRule) → MODIFY to `GO:0004520 DNA
  endonuclease activity`. Same argument; `GO:0004520` is already annotated from a
  different InterPro signature, so this consolidates rather than adds.
- `GO:0004520 DNA endonuclease activity` (IEA, InterPro IPR019857) → ACCEPT as core.
  Though the code is IEA, the activity was measured on this very protein.
- `GO:0042802 identical protein binding` (IPI, self) → MODIFY to `GO:0042803 protein
  homodimerization activity`. **Comparator check:** E. coli Cas1 (Q46896) carries
  `GO:0042803` by IDA from PMID:21219465 (`genes/ECOLI/ygbT/ygbT-goa.tsv`), so the more
  informative term is the established convention for this family.
- `GO:0043571 maintenance of CRISPR repeat elements` IEA → ACCEPT; IMP (PMID:26586803)
  → ACCEPT as core. The term's definition names "capture of new spacer elements"
  directly.
- `GO:0046872 metal ion binding` (IEA, UniRule) → ACCEPT. Cofactor and binding sites
  are experimentally established for this protein.
- `GO:0051607 defense response to virus` (IEA, UniRule) → KEEP_AS_NON_CORE. Cas1 is
  dispensable for interference (quote above); it contributes to immunity only by
  building the array, so an `involved_in` on the antiviral response is a step removed
  from what Cas1 does. It is also the term for which PA14's own phenotype is most
  equivocal — see the cas6f notes for the PMID:21398535 / PMID:23242138 tension.
  Keeping rather than removing: the statement is not wrong, and `REMOVE` for a
  pipeline-sourced term I can argue is merely indirect would overreach.

## Gaps identified (missing annotation)

- `GO:0099048 CRISPR-cas system` — E. coli Cas1 (Q46896) carries it by IDA
  (PMID:27899566) and by IBA, as does Cas2 (P45956). PA14 Cas1 does not. The term's
  definition names "acquisition of foreign DNA by integration into CRISPR loci" as one
  of its three stages, which is exactly the step Cas1 catalyses, and the D268A
  phenotype is PA14-specific evidence. Checked via QuickGO that `GO:0099048` is neither
  ancestor nor descendant of `GO:0043571` or `GO:0051607`. → NEW (IMP).

## Not proposed

- No separate process term for "protospacer integration" / "primed adaptation". The
  integration chemistry is covered by `GO:0004520` plus `GO:0043571`; adding a narrower
  invented process would duplicate.
- No annotation for the Cas1–Cas2-3 interaction: UniProt flags the partner identity as
  "Probable" and there is no cached experimental pairwise evidence for PA14. Raised as
  a `suggested_question` instead.
