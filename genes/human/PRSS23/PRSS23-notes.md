# PRSS23 (O95084) — review journal

## Why this gene is on the contested-function list

GOA carries `GO:0004252` serine-type endopeptidase activity and `GO:0006508` proteolysis
for PRSS23. Both come from a **single electronic source** — InterPro signatures
IPR001254/IPR018114 via `GO_REF:0000002`, evidence code **IEA** (confirmed by reading
`PRSS23-goa.tsv`; there is no IDA/IMP/EXP row for either term anywhere in the file).
UniProt likewise assigns `EC=3.4.21.-` with no experimental provenance and the
`SIMILARITY` line "Belongs to the peptidase S1 family" is an `ECO:0000305` inference.

So the protease assignment for PRSS23 rests entirely on domain-match, and a 2026 paper
now assays the protein directly and finds no activity.

## The 2026 direct-assay paper

Akhtar et al., *J Biol Chem* 2026 — verified: PMID:41985786, "PRSS23 promotes ovarian
cancer peritoneal dissemination independent of protease activity", J Biol Chem 2026,
DOI 10.1016/j.jbc.2026.111450, PMC13194640, full text cached.

Three independent lines of evidence against catalysis:

1. **Sequence/structure — the zymogen activation switch is gone.**
   [PMID:41985786 "Endogenous epitope tagging demonstrated that PRSS23 is synthesized as
   a precursor and secreted as a processed, glycosylated protease homology domain that
   retains the catalytic triad yet lacks the canonical Ile16-Asp194 zymogen activation
   switch."] and, specifically,
   [PMID:41985786 "PRSS23 substitutes Gln at the predicted mature N terminus and Ala at
   the Asp194-equivalent position, eliminating the canonical Ile16-Asp194 salt bridge; the
   His40-equivalent residue is also substituted."]
   This matters because in S1 proteases the triad is necessary but not sufficient — the
   switch is what orders the activation-domain loops that build the S1 pocket and oxyanion
   hole. The substitutions are not a human idiosyncrasy:
   [PMID:41985786 "Notably, these activation switch substitutions are conserved across
   vertebrate PRSS23 orthologs"].

2. **Activity-based probe labelling of conditioned media — negative.**
   [PMID:41985786 "Multiple probe-reactive secreted hydrolases are detected in CM;
   however, no probe-reactive band corresponding to PRSS23 is detected at the expected
   molecular weight in either CM or anti-HA IP fractions."]
   This is the strongest form of the negative result: the internal positive control (other
   secreted serine hydrolases in the same sample) labels fine.

3. **Chromogenic substrate panel — negative, with the right control.**
   [PMID:41985786 "Across this substrate panel, we did not observe reproducible substrate
   turnover above background that depended on the putative catalytic serine; WT and
   Ser316Ala preparations exhibited similar rates for all substrates tested"]
   The Ser316Ala control is what distinguishes "no activity" from "contaminating activity",
   and it also retires an earlier preliminary report of Z-FR-pNA hydrolysis by the authors'
   own group.

Summary statement: [PMID:41985786 "Taken together with the disrupted Ile16-Asp194
activation switch inferred from sequence analysis, these findings indicate that secreted
PRSS23 lacks detectable serine protease activity."] and the explicit annotation lesson:
[PMID:41985786 "Thus, sequence-based annotation focused solely on the catalytic triad will
tend to overestimate catalytic competence and underestimate the true prevalence of serine
pseudoproteases, as appears to be the case for PRSS23."]

**Independent corroboration that the biology is non-proteolytic.** In gastric cancer,
PRSS23 binds eIF4E through the protease-homology domain, and
[PMID:41985786 "Notably, eIF4E binding and progrowth phenotypes were retained in catalytic
triad mutants of PRSS23 in that system (60), providing an independent line of evidence for
nonproteolytic PRSS23 function."] The primary report is PMID:39920289 (Oncogene 2025,
"PRSS23-eIF4E-c-Myc axis promotes gastric tumorigenesis and progression"):
[PMID:39920289 "Our investigation revealed that PRSS23 interacts with eIF4E via its
trypsin domain, while eIF4E binds to PRSS23 through the amino acid residue S209, as
confirmed by co-IP and immunofluorescence assays."]
Two labs, two tumour types, both find the phenotype survives loss of the catalytic
residue(s).

### Decision on the catalytic annotations

`GO:0004252` and `GO:0006508` → **REMOVE**. Both are IEA-only, derived from the same
InterPro domain match, and both are now directly contradicted by assay in the only paper
that has looked. CLAUDE.md explicitly permits arguing down an over-propagated electronic
inference on biological grounds; nothing here overrules a curator who read a full text,
because no curator ever made an experimental protease annotation for this gene.

I have *not* proposed a NOT-qualified annotation. A `NOT|enables GO:0004252` would be a
defensible alternative reading of the same evidence and is worth an expert's opinion — it
would record the negative result rather than merely deleting the positive claim. I have
put that in `suggested_questions` instead of asserting it.

## Trafficking and localisation

[PMID:41985786 "These data indicate that in ovarian cancer cells PRSS23 enters the
secretory pathway as a precursor protein that is processed, likely at the canonical RRKR
motif, and secreted as a glycosylated protease domain fragment after removal of the
prodomain."]
UniProt: signal peptide 1-19, N-glycosylation sequons at Asn93 and Asn207, phosphoserine
109 by FAM20C (the basis of the Reactome `GO:0005788` ER-lumen row), `SUBCELLULAR
LOCATION: Secreted`.

- `GO:0005576` extracellular region (IEA, SubCell mapping) — MODIFY to `GO:0005615`
  "extracellular space"; now directly demonstrated by endogenous tagging, and recovery of
  the mature fragment from conditioned media places it in extracellular fluid specifically.
  (An earlier draft of this note claimed `GO:0005615` was obsolete and kept the parent on
  that basis. That was wrong — the term is live; `cache/go/terms.csv` resolves it and it is
  in current use across the repo.)
- `GO:0005788` ER lumen (TAS, Reactome R-HSA-8952289 "FAM20C phosphorylates FAM20C
  substrates") — real but transit-route only; non-core.
- `GO:0070062` extracellular exosome (HDA, PMID:19199708, parotid-gland exosome MudPIT) —
  a bulk-proteomics observation consistent with secretion; non-core.
- `GO:0005634` nucleus (IDA, `GO_REF:0000054`, LIFEdb GFP-fusion screen) — flagged as
  over-annotated, **not** removed. It is a single high-throughput fusion-protein screen,
  it is not corroborated by any other study, and it is hard to reconcile with a
  signal-peptide-bearing protein that endogenous tagging shows entering the secretory
  pathway and being secreted. I am deliberately not calling it wrong: I have not seen
  the images.

## Non-cancer physiology (thin, but real)

- Mouse ovary: [PMID:18566130 "PRSS23 was highly expressed in atretic follicles, and it was
  expressed in the ovarian stroma and theca tissues just before ovulation."]
- Zebrafish heart-valve development:
  [PMID:23213106 "We found that morpholino knockdown of Prss23 inhibited the
  endothelial-to-mesenchymal transition (EndoMT) at the AV canal."]
  This is a genuine loss-of-function developmental phenotype, and it is an EndoMT/Snail
  signalling role, not a demonstrated proteolytic one — the paper predates the activity
  assays and assumed protease function.
- The 2006 comparative-genomics paper that seeded the "PRSS23 is an active protease"
  framing is explicit about its reasoning being sequence-based:
  [PMID:16870946 "In contrast, PRSS23 possesses the standard catalytic Ser typical for this
  family of proteases."] — exactly the triad-only inference the 2026 paper warns about.

## Cancer phenotype (the only well-powered functional data)

[PMID:41985786 "PRSS23 knockdown reduced proliferation and increased anoikis sensitivity in
high-grade serous and clear cell ovarian carcinoma cell lines and diminished tumor
establishment, dissemination, and ascites in intraperitoneal xenograft models."]
I did not turn this into GO annotations. These are tumour-cell phenotypes in knockdown
lines, not a normal-physiology process the protein carries out, and the mediating molecular
activity is unknown.

## What I could not settle

The molecular function of PRSS23 is genuinely unknown. The 2026 paper surveys the
mechanistic options for S1 pseudoproteases — receptor ligand, non-catalytic cofactor/decoy
in a protease cascade, scaffold — without assigning PRSS23 to one. I therefore wrote the
`core_functions` entry with **no `molecular_function` term at all**: a location, a
description and the supporting quotes. Asserting even "protein binding" would be worse than
saying nothing.

The only named direct partner from a focused study is eIF4E (PMID:39920289), and that is
hard to reconcile with a secreted protein — eIF4E is cytosolic. Either there is an
unsecreted intracellular pool, or the interaction is an overexpression artefact. Flagged as
a question, not annotated.

## Validation notes

- `references:` titles filled with `fill_refs.py`; never hand-typed.
- Every `supporting_text` checked as a normalised verbatim substring of the cached
  `publications/PMID_*.md` before validating.
