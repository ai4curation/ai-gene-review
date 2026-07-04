# DCAR-1 (C. elegans) — research notes

UniProt: G5EDI0 (G5EDI0_CAEEL) · WormBase: WBGene00007395 · sequence name C06H5.7 ·
Reactome: R-CEL-416476 "G alpha (q) signalling events" · 396 aa, 7-TM class A (rhodopsin-like)
GPCR (PROSITE PS50262 G_PROTEIN_RECEP_F1_2; PANTHER PTHR24243). Chromosome V.

DCAR-1 = "DihydroCaffeic Acid Receptor 1". Two distinct, experimentally established
functional contexts, in two tissues:

1. **Epidermal innate immunity** (flagship function; Zugasti et al. 2014, Nat Immunol,
   PMID:25086774). DCAR-1 is a plasma-membrane GPCR on the apical surface of the hyp7
   epidermal syncytium that senses the endogenous tyrosine-derived metabolite HPLA
   (4-hydroxyphenyllactic acid, a damage-associated molecular pattern, DAMP) produced upon
   fungal infection/wounding, and triggers antimicrobial-peptide (nlp-29 cluster) gene
   expression via the GPA-12 (Gα) → TIR-1 → NSY-1/SEK-1/PMK-1 (p38 MAPK) → STA-2 cascade in
   the epidermis. Required for resistance to the fungus *Drechmeria coniospora*.
2. **Neuronal chemosensory avoidance** (Aoki et al. 2011, J Neurosci, PMID:22090488).
   DCAR-1 was originally identified in a Xenopus oocyte expression screen as a receptor
   for the water-soluble repellent dihydrocaffeic acid (DHCA); expressed in the ASH (and
   ASI, PVQ) sensory neurons, where it mediates avoidance of DHCA acting with ocr-2/osm-9.

## KNOWN (well supported)

- **7-TM class A GPCR.** UniProt/InterPro: 7 predicted TM helices, GPCR family 1 profile
  domain (PS50262), CDD 7tm_classA_rhodopsin-like, PANTHER PTHR24243. FunFam name
  "DihydroCaffeic Acid Receptor". Reactome links it to "G alpha (q) signalling events".
- **Innate immune receptor.** [PMID:25086774 "we identified the G protein-coupled receptor
  (GPCR) DCAR-1 as being required for the response to fungal infection and wounding."] Sole
  hit from an RNAi screen of 1,150 GPCR genes for reduced nlp-29p::gfp AMP induction; two
  null alleles (tm2484, nj66) confirm. dcar-1 mutants are markedly more susceptible to
  *D. coniospora* while having normal development/longevity and normal resistance to
  *P. aeruginosa*.
- **Acts via p38 MAPK / GPA-12 in epidermis.** [PMID:25086774 "DCAR-1 acted in the
  epidermis to regulate the expression of antimicrobial peptides via a conserved p38
  mitogen-activated protein kinase pathway."] [PMID:25086774 "dcar-1 alone acts upstream
  or in parallel to GPA-12"]. Methods list gpa-12(pk322), tir-1(tm3036), pmk-1(km25),
  tpa-1(fr1) epistasis strains — this is the GPA-12→TIR-1→p38/PMK-1 cassette. Links to the
  already-reviewed **gpa-12** (Gα12/13 ortholog).
- **Endogenous ligand = HPLA (a DAMP).** [PMID:25086774 "the tyrosine derivative
  4-hydroxyphenyllactic acid (HPLA) as an endogenous ligand"]. Identified by comparative
  metabolomics: HPLA present at low level in controls, increased upon infection and in
  cuticle-defective dpy-10 mutants. [PMID:25086774 "HPLA can act through DCAR-1 to regulate
  the epidermal innate immune response"]. [PMID:25086774 "HPLA appears to act as a DAMP, to
  the best of our knowledge, the first described for C. elegans."]
- **Exogenous ligand = DHCA.** [PMID:25086774 "Dihydrocaffeic acid (DHCA) has been described
  as a potent ligand for DCAR-1 in both in vivo and in heterologous Xenopus oocyte assays"].
  Original identification: [PMID:22090488 "we identified a candidate dihydrocaffeic acid
  receptor (DCAR), DCAR-1. DCAR-1 is a novel seven-transmembrane protein that is expressed
  in the ASH avoidance sensory neurons of C. elegans."]
- **Localization.** Apical plasma membrane in hyp7 epidermis:
  [PMID:25086774 "dcar-1 was expressed on the apical surface in the major epidermal
  syncytium, hyp7"] (IDA, GO:0016324). Neuronal expression in ASH/ASI/PVQ (ciliated sensory
  neurons); WormBase IDA GO:0097730 non-motile cilium from PMID:22090488 (abstract-only in
  cache; the cilium sub-localization is not stated in the abstract but was curated by
  WormBase from the full text — trust the curator).
- **Response to wounding.** [PMID:25086774] dcar-1 mutants show "an almost complete block of
  nlp-29p::gfp induction following physical injury", i.e. activation is damage/wound-dependent
  even without a pathogen (GO:0009611 response to wounding, IMP).
- **Cell-autonomous, tissue-separable.** Epidermal (col-12p) but not neuronal (sra-6p)
  expression rescues AMP induction/immunity; conversely neuronal expression rescues the
  avoidance phenotype. [PMID:25086774 "dcar-1 acts in an epidermis-specific and
  cell-autonomous manner to regulate AMP gene expression and defense against infection"].
- **Phylogenetically nematode-restricted.** [PMID:25086774 "Clear homologs of DCAR-1 can be
  found in nematode genomes, but not in other animals'"].

## NOT known / open (for knowledge_gaps)

- **Structural basis of HPLA/DHCA sensing is unknown.** No direct binding data, no structure,
  and the ligand-binding pocket / residues are undefined. HPLA binding is inferred from
  correlative genetics + metabolomics, not a direct receptor-binding assay:
  [PMID:25086774 "We provide strong correlative evidence that HPLA is an endogenous ligand
  for DCAR-1. Proving this definitively is not straightforward"]. Whether DCAR-1 is even the
  direct HPLA receptor (vs an upstream sensor) is not biochemically proven.
- **Whether DCAR-1 has other (neuropeptide or microbial) ligands / roles is unknown.** Its
  natural neuronal ligand and whether it detects any microbe-associated molecular pattern are
  undetermined: [PMID:25086774 "It is not known whether any GPCR recognizes specific
  microbe-associated molecular patterns."] A speculated second role in pathogen-avoidance
  behavior is unproven.
- **HPLA biosynthesis / how infection raises HPLA is uncharacterized.** [PMID:25086774
  "Although its biosynthetic pathway has not been characterized in any eukaryote, HPLA is
  likely derived from tyrosine"]; whether the fungus contributes to HPLA or it is purely host
  damage-derived is an open question.
- **Nematode-restricted receptor with a conserved-metabolite ligand** — whether an
  HPLA/DAMP-sensing receptor exists outside nematodes is unknown: [PMID:25086774 "It could be
  that receptor(s) for HPLA exist outside the nematode phylum, but are not recognizable from
  their primary sequence."]

## Annotation review plan (existing_annotations)

| term | ev | ref | action | rationale |
|---|---|---|---|---|
| GO:0004930 G protein-coupled receptor activity | IEA | GO_REF:0000104 | ACCEPT (core MF) | 7-TM class A GPCR; receptor for HPLA/DHCA |
| GO:0007186 GPCR signaling pathway | IEA | GO_REF:0000104 | ACCEPT (core BP) | signals via GPA-12 Gα |
| GO:0007165 signal transduction | IEA | GO_REF:0000104 | KEEP_AS_NON_CORE | correct but generic parent of GPCR signaling |
| GO:0050832 defense response to fungus | IMP | PMID:25086774 | ACCEPT (core BP) | required for anti-D. coniospora defense |
| GO:0009611 response to wounding | IMP | PMID:25086774 | ACCEPT (core BP) | wound/damage-activated AMP induction |
| GO:0016324 apical plasma membrane | IDA | PMID:25086774 | ACCEPT (core CC) | apical hyp7 surface |
| GO:0005886 plasma membrane | IBA | GO_REF:0000033 | ACCEPT | correct (parent of apical PM) |
| GO:0016020 membrane | IEA | GO_REF:0000120 | KEEP_AS_NON_CORE | generic; subsumed by apical PM |
| GO:0097730 non-motile cilium | IDA | PMID:22090488 | KEEP_AS_NON_CORE | neuronal (ASH) chemosensory localization; abstract-only cache, defer to WB curator |
| GO:0008188 neuropeptide receptor activity | IBA | GO_REF:0000033 | REMOVE | over-propagated family IBA; DCAR-1 ligands are small-molecule metabolites (HPLA/DHCA), not neuropeptides |
| GO:0007218 neuropeptide signaling pathway | IBA | GO_REF:0000033 | REMOVE | same; not a neuropeptide receptor |

Proposed new term candidate: a specific MF for "dihydroxyphenyl/hydroxyphenyllactic acid
(DAMP) receptor activity" — currently only GO:0004930 available. Note as ontology gap.

## Deep research provenance

Automated deep research could not be generated: `just deep-research-falcon` (Edison/falcon)
timed out at 600s on both the initial run and a retry, and the perplexity-lite fallback
returned HTTP 401 (API quota exhausted). No `-deep-research-*.md` file was fabricated (per
policy). This review is therefore grounded directly in the two primary papers
(PMID:25086774 full text; PMID:22090488 abstract) plus the UniProt/InterPro/PANTHER records.
All supporting_text quotes were verified as verbatim (whitespace-normalized) substrings of
the cached publications before use.
