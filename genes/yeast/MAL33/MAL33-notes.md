# MAL33 (YBR297W / P38157) — curation notes

Journal for the AI GO-annotation review of *Saccharomyces cerevisiae* MAL33 (MAL3R).
This is a **dark/understudied gene**: the S288C reference-strain MAL33 allele is a
**defective (non-functional) MAL-activator**, so essentially all "maltose regulon
activation" function is inferred from its functional paralogs (MAL63, MAL13, etc.),
not measured for MAL33 itself. The core defensible functions are domain-level (Zn2Cys6
DNA binding, zinc binding, nucleus); the specific biological role is a genuine gap.

## Identity and provenance

- UniProt: **P38157** (MAL33_YEAST); systematic name **YBR297W**; standard name MAL33;
  synonym **MAL3R**. SGD:S000000501. Chromosome II (right arm, telomere-associated MAL3 locus).
- 468 aa, 54,194 Da. PE level **3: Inferred from homology** (i.e. no protein-level
  experimental evidence in UniProt) [`genes/yeast/MAL33/MAL33-uniprot.txt`].
- UniProt FUNCTION (inferred): "Regulates the coordinate transcription of structural
  MAL3S (maltase) and MAL3T (maltose permease) genes." SUBCELLULAR LOCATION: Nucleus.
  SIMILARITY: "Belongs to the MAL13 family."
  [`genes/yeast/MAL33/MAL33-uniprot.txt` lines 59-62].

## Domain architecture (inline analysis from UniProt record)

From `MAL33-uniprot.txt`:
- **DNA_BIND 8..34**: "Zn(2)-C6 fungal-type" GAL4-class binuclear zinc cluster
  (PROSITE PS50048 / PS00463; Pfam PF00172 Zn_clus; SMART SM00066 GAL4; CDD cd00067 GAL4).
  This is the canonical fungal Zn2Cys6 (binuclear zinc cluster) DNA-binding domain: six
  cysteines coordinate two Zn(II) ions, and the domain binds CGG-triplet-containing
  sequence-specific DNA sites. → supports zinc ion binding and sequence-specific DNA binding.
- **MOTIF 41..49**: predicted nuclear localization signal (ECO:0000255) → supports nuclear location.
- **Middle homology region / "Fungal_trans"**: Pfam PF04082 (Fungal_trans, IPR007219
  "XlnR/fungal transcription factor regulatory middle homology region"; CDD cd12148
  fungal_TF_MHR). This central regulatory/transactivation region is characteristic of
  Zn2Cys6 activators and (in the functional MAL activators) carries the transactivation
  and maltose-responsive regulatory functions.
- PANTHER family **PTHR31668** ("Carbohydrate Metabolism and Transport Regulator" /
  RGT1-related), subfamily **PTHR31668:SF18** "MALTOSE FERMENTATION REGULATORY PROTEIN
  MAL13-RELATED" [`interpro/panther/PTHR31668/`].
- **Sequence check**: The S288C sequence (`MAL33-uniprot.txt` lines 132-141) is a
  full-length 468-aa ORF with an intact N-terminal Zn2Cys6 domain (residues MTLVKYACDYCRVRRVKCDGKKPCSRCIEHNFDC… — the C-x2-C-x6-C-x6-C-x2-C-x6-C zinc-cluster
  cysteine pattern is present). So MAL33's non-functionality in S288C is **NOT** a gross
  truncation of the DBD; the defect maps to sequence divergence across the protein
  (~71% identity to the functional Mal63p; see below), i.e. the DNA-binding domain is
  structurally present but the allele fails to activate the MAL regulon.

## KNOWN vs NOT-known

### KNOWN (domain- / homology-defensible)
- MAL33 is a **fungal Zn2Cys6 (GAL4-type binuclear zinc cluster) protein** with an
  intact N-terminal DBD (res 8-34) and a fungal-TF middle homology region. On domain
  grounds it can **coordinate zinc** and **bind sequence-specific DNA** and act as a
  **DNA-binding transcription factor** in the **nucleus** (predicted NLS).
  [UniProt domains; family classification].
- MAL33 is one of the paralogous **MAL-activator genes** of the *S. cerevisiae* MAL
  multigene loci. Each MAL locus (MAL1–MAL4, MAL6) is a complex of three genes — a
  MAL-activator (GENE 3 / R gene), a maltase (GENE 2 / S gene), and a maltose permease
  (GENE 1 / T gene). MAL33 is the activator of the **MAL3** locus on chromosome II
  (with MAL31 permease and MAL32 maltase) [Michels et al. 1992, PMID:1441745, MAL3 is a
  telomere-associated tandem array; Naumov et al. molecular evolution of MAL loci].
- The **prototype functional MAL-activator is Mal63p** (MAL6 locus). Functional-domain
  analysis of the MAL-activator was done on **MAL63** (LexA-Mal63 fusions): DNA-binding
  domain res 1-100; functional core incl. transactivation res 60-283; inhibitory region
  res 251-299; C-terminal maltose-responsive domain relieving that inhibition — i.e. a
  maltose-inducible autoregulation model [Hu et al. 1999, PMID:10447589, ABSTRACT].
  NOTE: this is **MAL63**, not MAL33; the MAL33 ISS annotations are transferred from
  Mal63p (with_from SGD:S000029659 = MAL63).

### NOT known / genuinely uncertain for MAL33 specifically
- **Whether the S288C MAL33 allele is a functional MAL-activator: it is NOT.** MAL33 (MAL3R)
  is "nonfunctional in the genomic reference strain S288C." S288C-derived strains carry two
  MAL loci (MAL1, MAL3) both with **defective activator genes (mal13, mal33)**; the
  reference strain therefore cannot ferment maltose from these loci without a functional
  activator supplied in trans. The defective mal33p (in YPH500, isogenic to S288C) is
  **71.2% identical** to the functional Mal63p (and mal13p 70.7%). The maltose-non-inducible
  phenotype of YPH500 is complemented by a plasmid copy of MAL63, confirming the defect is a
  lack of functional MAL-activator [web literature: Naumov/Charron/Michels MAL-locus work;
  Novak et al. "Intracellular maltose is sufficient to induce MAL gene expression" PMC126750;
  bioRxiv 2025 MAL33 allelic variation review-of-record for the "nonfunctional in S288C" claim].
- **The direct DNA targets and DNA-binding site(s) of MAL33 in vivo** — never mapped for
  MAL33. For the functional activator, the MAL UAS and Mal63p binding sites were mapped
  [PMID:2192262, identification of the MAL UAS and Mal63 binding sites] — but that is Mal63p.
- **The condition/mechanism (maltose induction) for MAL33** — inferred from Mal63p; not
  demonstrated for the (defective) S288C MAL33.
- **Redundancy / relationship with other MAL activators** — MAL33 vs MAL13 (the other
  S288C defective allele) vs functional Mal63p/Mal43p/Mal23p is characterized only at the
  sequence level, not by direct genetic test of MAL33.
- **Zinc stoichiometry / direct metal binding of MAL33** — inferred (Zn2Cys6 domain +
  RCA zinc-proteome inclusion [Wang et al. 2018, PMID:30358795, ABSTRACT]); not directly measured.

## GOA annotation inventory (11 rows; `MAL33-goa.tsv`)

MF:
- GO:0000981 DNA-binding TF activity, RNA Pol II-specific — IEA (InterPro) — ACCEPT (domain: Zn2Cys6)
- GO:0003677 DNA binding — IEA (InterPro) — ACCEPT (generic parent, domain)
- GO:0008270 zinc ion binding — IEA (InterPro) — ACCEPT (Zn2Cys6 coordinates 2 Zn)
- GO:0008270 zinc ion binding — RCA (PMID:30358795) — ACCEPT (zinc proteome computational)
- GO:0003700 DNA-binding TF activity — ISS (PMID:10447589, with_from MAL63) — ACCEPT (family MF; transferred from Mal63p)
BP:
- GO:0006351 DNA-templated transcription — IEA (InterPro) — KEEP_AS_NON_CORE (generic)
- GO:0006355 regulation of DNA-templated transcription — IEA (InterPro) — KEEP_AS_NON_CORE (generic parent)
- GO:0006357 regulation of transcription by RNA Pol II — IEA (GO_REF:0000108 logical inference from MF) — KEEP_AS_NON_CORE
- GO:0006355 regulation of DNA-templated transcription — ISS (PMID:10447589, MAL63) — KEEP_AS_NON_CORE (generic; specific MAL-regulon role is a gap for the defective allele)
CC:
- GO:0005634 nucleus — IEA (GO_REF:0000120) — ACCEPT (predicted NLS + TF)
- GO:0005634 nucleus — ISS (PMID:10447589, MAL63) — ACCEPT (is_active_in; family/homology)

Notes on actions:
- No REMOVE candidates: none of the annotations are wrong. The maltose-metabolic-process
  keyword (GO:0000023) appears in the UniProt DR block but is NOT in the GOA TSV, so it is
  not in the review set.
- The "maltose regulon activation" specificity is the crux: because the S288C allele is
  defective, I do NOT elevate a specific "positive regulation of maltose-regulon
  transcription" role to a core function; the generic RNA-Pol-II regulation terms are kept
  as non-core, and the maltose-specific role is written up as the primary knowledge gap.
- Avoid `protein binding` — not present in GOA; good.

## Core function synthesis

MAL33 is (domain-defensibly) a **fungal Zn2Cys6 sequence-specific DNA-binding
transcription factor of the MAL-activator family, acting in the nucleus**, expected on
family grounds to regulate RNA Pol II transcription. Its name-defining specific role
(maltose-inducible activation of MAL structural genes) is characterized for the
**functional paralog Mal63p**, and the **S288C MAL33 allele is a non-functional
activator**, so a specific "positive regulation of the maltose regulon" is not asserted
as a demonstrated MAL33 core function — it is the central knowledge gap.

## Key references
- PMID:10447589 — Hu et al. 1999, functional domain analysis of the MAL-activator (Mal63p). ABSTRACT-only cache. HIGH relevance (family MF), but note it is Mal63p not MAL33.
- PMID:30358795 — Wang et al. 2018, yeast zinc proteome. ABSTRACT-only cache. MEDIUM (supports zinc binding computationally).
- PMID:1441745 — Michels/Read/Nat/Charron 1992, MAL3 locus tandem array (context for MAL33 = MAL3 activator).
- PMID:2192262 — MAL UAS and Mal63 binding sites (context; Mal63p, not MAL33).
- Web/SGD: MAL33 nonfunctional in S288C; mal33p 71.2% identical to Mal63p; YPH500 maltose defect complemented by plasmid MAL63.

## Deep research
- Falcon deep research: attempt 1 timed out (600s) and the perplexity-lite fallback
  returned HTTP 401 (quota exhausted). Attempt 2 (falcon only) SUCCEEDED after ~1240s
  (~20.7 min) and wrote `MAL33-deep-research-falcon.md` (genuine, 49 KB).
- CAVEAT on the falcon report: its narrative is broadly consistent with this review
  (Zn2Cys6 MAL-activator; MAL3 locus regulator of MAL31/MAL32; nucleus; non-functional
  in several lab strains; MAL63 is the functional prototype), BUT its inline citation
  keys are **fabricated/mangled** (e.g. "ran2008hsp90hsp70chaperonemachine",
  "bali2003thehsp90molecular" — these are Hsp90 papers mis-attached to MAL-locus claims).
  Per project memory (falcon report citation style), such non-PMID keys are NOT trusted
  and are NOT cited in the review. The review is instead grounded in the two cached PMIDs
  (10447589, 30358795) plus PubMed-verified PMID:1441745 (MAL3 locus) and multiple
  independent web sources for the S288C non-functionality / 71.2% identity to Mal63p.
- One useful nuance the falcon report raises: UniProt annotates the S288C MAL33/YBR297W
  as an *intact ORF* (predicted functional activator), while the "non-functional" status
  is most explicitly documented for W303/JN516/5B6 and the S288C-isogenic YPH500. This
  review therefore hedges ("reported to be a non-functional MAL-activator") and frames
  the functional status of the S288C allele as the primary knowledge gap rather than
  asserting either way.
- Falcon report also outlines the broader regulatory circuit for the FUNCTIONAL MAL
  activator (Mal63p): Hsp90/Hsp70 chaperone-maintained inactive state released on maltose
  sensing; glucose repression via Mig1p/Cyc8-Tup1 and Snf1 kinase. This is context for
  the family, not MAL33-specific evidence, and is not annotated to MAL33.
