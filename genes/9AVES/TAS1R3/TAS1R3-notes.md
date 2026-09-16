# TAS1R3 (A0A7L3N407, Oreotrochilus melanogaster) - curation notes

## Identity and record status

- UniProt A0A7L3N407, unreviewed (TrEMBL), 832 aa, `Flags: Fragment`, `NON_TER` at
  both residue 1 and 832. Derived from the Bird 10,000 Genomes (B10K) Project
  whole-genome shotgun assembly (ORF `OREMEL_R00692`, strain OUT-0002; Zhang G.,
  submitted Sep 2019).
- NCBI taxon id in the record is **689266** (`Oreotrochilus melanogaster`), per the
  `OX` line of `TAS1R3-uniprot.txt`. The seeded YAML stub had the wrong taxon id
  (`NCBITaxon:8782`, which is not this organism's id) - corrected to `689266`
  during this review.
- `gene_symbol` in the seeded stub was set to the UniProt accession
  (`A0A7L3N407`) rather than the gene symbol - corrected to `TAS1R3` (UniProt
  `GN Name=Tas1r3`).
- No gene-specific PMIDs were seeded for this record (`fetch-gene-pmids` found
  none); all 9 GOA rows are IEA (ARBA / InterPro2GO / TreeGrafter / UniProt
  combined pipelines), not experimental.

## Key background biology (not species-specific evidence)

Baldwin et al. 2014 Science, PMID:25146290 (full text cached,
`publications/PMID_25146290.md`, PMC4302410):

- Most vertebrates have three T1Rs; TAS1R2-TAS1R3 mediates sweet taste and
  TAS1R1-TAS1R3 mediates umami taste. Birds (including chickens, turkeys,
  zebra finches, and swifts) generally **lack TAS1R2** entirely
  [PMID:25146290 "We failed to detect T1R2 in bird genomes, despite the
  presence of flanking loci."].
- In the hummingbird lineage specifically (studied via Anna's hummingbird,
  *Calypte anna*), the ancestral TAS1R1-TAS1R3 umami heterodimer was
  repurposed to detect carbohydrates instead of amino acids
  [PMID:25146290 "Receptor expression studies revealed that the ancestral
  umami receptor (the T1R1-T1R3 heterodimer) was repurposed in hummingbirds
  to function as a carbohydrate receptor."].
- Neither TAS1R1 nor TAS1R3 alone gave a ligand response in heterologous
  cells - only the co-expressed heterodimer did
  [PMID:25146290 "Responses were not observed when T1R1 or T1R3 alone was
  used, suggesting that hummingbird T1R1-T1R3 functions as an obligate
  heterodimer."]. This means TAS1R3 cannot sensibly be annotated as an
  independently-functional receptor; its molecular activity is always
  exercised as part of the TAS1R1-TAS1R3 dimer.
- Chicken/swift T1R1-T1R3 (which lack the hummingbird-specific
  substitutions) instead detect amino acids (alanine, serine), not sugars
  [PMID:25146290 "cells expressing chicken or swift T1R1-T1R3 failed to
  detect carbohydrates at any concentration tested and instead recognized
  alanine and serine."]. Hummingbird T1R1-T1R3 retains only low-affinity
  amino-acid responses [PMID:25146290 "Low-affinity responses were observed
  to some amino acids, as with the human sweet receptor..."].
- The sugar-response-conferring substitutions are concentrated in the TAS1R3
  Venus-flytrap domain (109-residue region; 19 key substitutions)
  [PMID:25146290 "Reintroducing 109 amino acids (residues 158 to 266) of
  hummingbird T1R3 into the chicken T1R3 venus flytrap domain restored
  sucrose responses (chimera 2)."], with additional contributing
  substitutions in TAS1R1.
- Receptor pharmacology (sugars/sugar-alcohols agonist; several human
  sweeteners inactive/aversive) matched taste behavior in both captive and
  wild hummingbirds (ruby-throated and Anna's hummingbirds respectively).
- **Important caveat for this gene review**: PMID:25146290 studied *Calypte
  anna* (Anna's hummingbird) and *Archilochus colubris* (ruby-throated
  hummingbird), **not** *Oreotrochilus melanogaster* (the species behind the
  UniProt accession reviewed here, a high-Andean hillstar). There is no
  UniProt entry, and apparently no published functional study, for T1R1/T1R3
  from *O. melanogaster* itself. All functional claims made in the ai-review
  YAML for this gene are by homology/lineage inference, not direct
  experimental evidence on this exact protein.

## Deep research

`genes/9AVES/TAS1R3/TAS1R3-deep-research-falcon.md` (Falcon/Edison provider,
generated 2026-09-07) independently reaches the same conclusion: no
accession-, ORF-, or species-specific functional literature exists for
A0A7L3N407 / *O. melanogaster* Tas1r3; the InterPro domain architecture
(ANF_lig-bd_rcpt / GPCR_3 / GPCR_3_9-Cys_dom / GPCR_3_C) is consistent with a
class C TAS1R-family GPCR, and the recommended annotation is "probable
class-C, seven-transmembrane taste-receptor subunit... by hummingbird-lineage
homology... likely heterodimerizes with T1R1... to detect nectar
carbohydrates."

## Annotation review summary

All 9 seeded GOA rows are IEA (ARBA/InterPro2GO/TreeGrafter/UniProt combined),
reviewed against PMID:25146290 and GO term definitions verified via QuickGO
(`https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/...`):

- GO:0033041 "sweet taste receptor activity" - **ACCEPT**. QuickGO definition
  ("Combining with soluble sweet compounds to initiate a change in cell
  activity") does not require the canonical TAS1R2 partner mechanism, so the
  hummingbird-repurposed TAS1R1-TAS1R3 dimer legitimately satisfies it. This
  is treated as the gene's core molecular function.
- GO:0050916 "sensory perception of sweet taste" and GO:0001582 (its BP
  detection-of-stimulus child) - **ACCEPT**, paralleling GO:0033041.
- GO:0050917 "sensory perception of umami taste" - **KEEP_AS_NON_CORE**. This
  is the ancestral, family-wide function of TAS1R1-TAS1R3 (still primary in
  most non-hummingbird birds), but PMID:25146290 shows it was largely
  superseded by the sweet-taste function in hummingbirds specifically, with
  only weak/low-affinity amino-acid responses retained. Not REMOVE (some
  retained low-affinity capacity, and no species-specific data to say it is
  fully lost in *O. melanogaster*), not co-equal ACCEPT (would overstate the
  minor residual capacity against the well-established, dominant sweet-taste
  function).
- GO:0050909 "sensory perception of taste" (broad ARBA parent),
  GO:0004930 "G protein-coupled receptor activity", GO:0005886 "plasma
  membrane", GO:0007186 "GPCR signaling pathway", GO:0016020 "membrane"
  (generic, redundant with plasma membrane but not incorrect) - all
  **ACCEPT** as broad-but-accurate domain/family-based calls, consistent with
  project precedent (cf. `genes/human/LRP10` accepting GO:0016020 alongside a
  more specific plasma-membrane term).

## Validation

Ran `just validate 9AVES TAS1R3` after completing the review - passed cleanly
(see terminal output in the session transcript).

## Related record

`genes/9AVES/TAS1R1/` (UniProt A0A7L3NBT4, same species) is the obligate
dimerization partner for this receptor but its `ai-review.yaml` is still
`INITIALIZED`/`PENDING` as of this session - **not reviewed here**; a
separate review pass would be needed for TAS1R1. It also has the same wrong
placeholder taxon id (`NCBITaxon:8782`) in its seeded stub, which would need
the same correction to `NCBITaxon:689266` if/when reviewed.
