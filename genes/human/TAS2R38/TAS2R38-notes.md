# TAS2R38 curation notes

## Identity
TAS2R38 (T2R38, PTC bitter taste receptor; UniProt P59533) is a single-exon, intronless
class-A-like 7TM GPCR of the human TAS2R bitter-taste-receptor family (PANTHER PTHR11394;
InterPro IPR007960 family / IPR030050 gene-specific). Confirmed via UniProt record and PANTHER
family assignment [file:human/TAS2R38/TAS2R38-uniprot.txt "Belongs to the G protein-coupled
receptor T2R family."].

## Core function
Principal human receptor for phenylthiocarbamide (PTC) and 6-n-propylthiouracil (PROP), and
other thiourea-containing bitter compounds. Established via a 25-receptor/104-compound
heterologous-expression screen [PMID:20022913 "we have challenged 25 human taste 2 receptors
(hTAS2Rs) with 104 natural or synthetic bitter chemicals in a heterologous expression system"].
UniProt's FUNCTION comment (by similarity) states the canonical downstream cascade:
gustducin -> PLCB2 -> IP3/Ca2+ -> TRPM5 [file:human/TAS2R38/TAS2R38-uniprot.txt "The activity of
this receptor may stimulate alpha gustducin, mediate PLC-beta-2 activation and lead to the
gating of TRPM5 (By similarity)."].

## PAV/AVI polymorphism
Three linked coding SNPs (A49P, A262V, I296V) define the common PAV ("taster") and AVI
(hypofunctional, "non-taster") haplotypes underlying classical PTC/PROP taste-sensitivity
variation [file:human/TAS2R38/TAS2R38-uniprot.txt "Variations in TAS2R38 are associated with
the ability to taste phenylthiocarbamide (PTC tasting) [MIM:171200]; also called thiourea
tasting."; falcon deep research: "Three strongly linked nonsynonymous variants at amino-acid
positions **49, 262, and 296** generate the common haplotypes"].

## Extraoral / innate-defense role (not annotated in GOA; recorded as a knowledge gap)
Falcon deep-research synthesis (not independently verified against primary full text by this
reviewer) describes TAS2R38 expression on sinonasal ciliated epithelium, where receptor
activation is linked to nitric-oxide-synthase activity, antibacterial NO production, and
increased ciliary beat frequency, with PAV/PAV cultures generally showing stronger responses
than AVI-containing cultures [falcon deep research, section 3.2]. Direct receptor-level
specificity for proposed bacterial quorum-sensing ligands (e.g. acyl-homoserine lactones) is
contested - one study "disputed direct HSL activation in its heterologous system and instead
identified several volatile bacterial metabolites" (falcon deep research, section 2.1) - so no
GOA-style GO annotation is proposed for this role here; it is recorded instead as a knowledge
gap in the review YAML.

## Annotation review summary (see TAS2R38-ai-review.yaml for full detail)
- All molecular-function and biological-process rows for GO:0033038 (bitter taste receptor
  activity), GO:0001580 (detection of chemical stimulus in bitter taste), GO:0004930 (GPCR
  activity) and GO:0007186 (GPCR signaling pathway): ACCEPT.
- GO:0005886 (plasma membrane) rows, including the CACAO IDA sourced to PMID:12379855 (whose
  cached title/abstract discuss TAS2R16, not TAS2R38): ACCEPT. UniProt's own reference list for
  TAS2R38 cites this identical PMID as the source of the TAS2R38 genomic sequence and the
  Val262 variant, so the paper evidently characterized TAS2R38 too, consistent with the
  "title/abstract foregrounds one gene, full text also assays others" pattern documented in
  this project's curation guide. Per that guide, an experimental annotation is not REMOVEd on
  this basis alone; flagged UNVERIFIED in `reference_review` instead.
- GO:0016020 (membrane) rows (IBA, IC, IEA) and the GO:0050909 (sensory perception of taste) IEA
  row: MODIFY -> propose the more specific, independently-supported terms already held for this
  gene (GO:0005886 plasma membrane; GO:0001580 bitter-taste detection, respectively). These are
  granularity corrections, not disputes with the underlying phylogenetic/family-level inference.

## Open questions
1. Full text of PMID:12379855 not accessible to this reviewer - would confirm whether it
   directly reports a TAS2R38 plasma-membrane localization assay.
2. Whether PAINT node PTN000149628 should carry a plasma-membrane-specific term for the wider
   TAS2R clade, most of whose members currently receive only the generic "membrane" by IBA.
3. No solved TAS2R38 structure exists; the PTC/PROP binding-pocket model (N103/F197/W201/F264)
   is mutagenesis-validated homology modeling only.
