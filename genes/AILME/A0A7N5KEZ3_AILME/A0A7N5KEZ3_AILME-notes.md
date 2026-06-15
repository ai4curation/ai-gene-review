# Notes: A0A7N5KEZ3_AILME (giant panda, *Ailuropoda melanoleuca*)

## Identity and provenance

- UniProt: A0A7N5KEZ3 (TrEMBL, **unreviewed**), 419 aa, "Uncharacterized protein"
  (SubName from Ensembl ENSAMEP00000039486.1). PE=4 (Predicted).
- Derived only from the giant panda genome assembly (PMID:20010809, Li et al. 2010,
  *Nature* 463:311-317) plus an Ensembl identification submission. No protein-level
  characterization, no organism-specific functional study exists.

## What kind of protein is this?

This is a **keratin-associated protein (KAP / KRTAP)** of the high-sulfur (B2) type. The
sequence is dominated by cysteine-rich pentapeptide-like repeats (`...CCKPVCCTPVCCKPVCC...`),
the diagnostic signature of high-sulfur hair/wool matrix proteins.

Domain/family evidence from the UniProt record:
- **Pfam PF13885** "Keratin_B2_2" (keratin, high-sulfur B2 protein)
- **InterPro IPR002494** "KAP" (Keratin-associated / high-sulphur keratin matrix protein)
- **PANTHER PTHR21523** (family); subfamily **PTHR21523:SF14** "EXPORTED REPETITIVE PROTEIN"
- Keyword: **Keratin** (ARBA)

Note PANTHER PTHR21523 is a broad, heterogeneous repetitive-protein family (its two SwissProt
members are *C. elegans* molting protein MLT-10 and *Drosophila* salivary glue Sgs-3), so the
PANTHER subfamily name alone is weak; the Pfam/InterPro KAP assignment plus the cysteine-repeat
sequence are the strong evidence that this is a hair/fur KAP.

## Function of KAPs (family-level, well established)

KAPs are structural matrix proteins of trichocyte ("hard") keratins — hair, wool, hoof, horn,
claw, baleen, quill. Keratin intermediate filaments (IF) are embedded in a matrix built from
KAPs; the high-sulfur KAPs are cysteine-rich and **cross-link adjacent keratin IFs via
inter- and intramolecular disulfide bonds**, organizing IFs into macrofibrils and conferring the
mechanical properties (hardness, toughness, rigidity) of the keratinized structure.
[PMID:29797269 Fraser & Parry 2018, "keratin intermediate filaments (IF) ... are embedded in a
matrix formed from at least 89 different types of keratin-associated proteins (KAPs)... especially
important roles in the organisation of the IF into macrofibrils... and in linking IF to one another
... stabilized predominantly by intramolecular disulfide bonds"]
[PMID:12895003 Shimomura et al. 2003, "Keratin-associated proteins are involved in the formation of
the cross-linked network of the keratin-intermediate filament proteins that support hair fibers...
classified primarily by a striking variation in double cysteine-containing pentapeptide repeats"]

In the giant panda this gene most plausibly contributes to pelage (fur) / claw hard-keratin
structure, but there is **no panda-specific experimental evidence**; all functional inference is
by family/domain homology.

## Existing annotations (QuickGO GOA; mirrored in UniProt DR lines)

QuickGO returns two IEA annotations for accession A0A7N5KEZ3, matching the UniProt flat-file
DR GO lines. (Note: the first `fetch-gene` run produced an empty GOA TSV because the entry *name*
`A0A7N5KEZ3_AILME` was passed to QuickGO's `geneProductId` instead of the accession `A0A7N5KEZ3`;
re-fetching with `--uniprot-id A0A7N5KEZ3` populated the two rows correctly.)

| GO term | Aspect | Evidence | Source / GO_REF |
|---|---|---|---|
| GO:0045095 keratin filament | C | IEA | InterPro (GO_REF:0000002) |
| GO:0005829 cytosol | C | IEA | UniProtKB-ARBA (GO_REF:0000117) |

Cross-check: human KRTAP4-3 (UniProtKB:Q9BYR4) carries the *identical* two IEA annotations
(cytosol GO_REF:0000117 ARBA + keratin filament GO_REF:0000002 InterPro), and additionally has an
experimental **GO:0042633 hair cycle** (IDA, PMID:21916889) and IBA hair cycle. This confirms the
GO_REF codes and the expected annotation pattern for the KAP family.

## Review decisions

- **GO:0045095 keratin filament** — ACCEPT (non-core localization is fine; this is the standard,
  well-supported KAP cellular-component term — KAPs are the matrix associated with keratin IFs).
- **GO:0005829 cytosol** — MARK_AS_OVER_ANNOTATED. Generic, low-information localization that ARBA
  assigns broadly to KRTAPs (also given TAS by Reactome for human KRTAPs); biologically the protein's
  role is in the cross-linked keratin matrix of the cornified hair/claw, not free cytosol. Not wrong
  enough to REMOVE, but a generic rule-based over-annotation rather than an informative localization.
  (Initially marked KEEP_AS_NON_CORE; revised to MARK_AS_OVER_ANNOTATED on annotation-reviewer advice.)

No molecular-function or biological-process term is currently annotated in GOA. The real "core"
of this protein is the **structural / matrix-cross-linking** role. Two **NEW** (ISS, homology-based)
annotations were added to make the core function traceable: **GO:0005198 structural molecule
activity** (MF, `enables`) and **GO:0031424 keratinization** (BP, `involved_in`), both supported by
the KAP family reviews and the Pfam/InterPro domain evidence. These are explicitly flagged as
homology inferences with no panda-specific evidence (GO does not currently assert an MF on human
KRTAPs, so the MF is a proposed addition).

## Tooling notes

- Automated deep-research (`deep_research_unified`) could not run in this environment: no
  OpenAI/Perplexity/Falcon API keys, and the Falcon template raised a "Missing template variables"
  error. Research above was done manually (PubMed + GO/Noctua annotation cross-check), so no
  `-deep-research-<provider>.md` file was written (per project rule against mislabeling manual
  content as provider deep research).
