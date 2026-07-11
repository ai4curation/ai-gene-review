# mug151 (SPAC3H1.03 / Q10069) — curation notes

Fission yeast (*Schizosaccharomyces pombe*) protein. UniProt name: "Meiotically up-regulated
gene 151 protein". 146 aa. Classified as an UNDERSTUDIED / dark gene.

## Identity / provenance (verified from fetched records)

- UniProt Q10069, `mug151-uniprot.txt`: RecName "Meiotically up-regulated gene 151 protein";
  GN Name=mug151; ORFNames=SPAC3H1.03; taxon 284812 (S. pombe 972).
- PomBase (API `www.pombase.org/api/v1/dataset/latest/data/gene/SPAC3H1.03`, fetched
  2026-07-06): `name: mug151`, `product: "SAP30 binding protein ortholog"`,
  `characterisation_status: "biological role inferred"`, `feature_type: mRNA gene`.
  This is the key framing: the *only* functional label PomBase assigns is inferred from the
  ortholog/domain, NOT from direct experimental characterization of the S. pombe protein.

## Domain / family (inline analysis of `mug151-uniprot.txt`)

- **Pfam PF07818 (HCNGP)** — the single defining domain of the protein.
- **InterPro IPR012479 "SAP30BP"**.
- **PANTHER PTHR13464:SF0 = "SAP30-BINDING PROTEIN"** (family PTHR13464 = "TRANSCRIPTIONAL
  REGULATOR PROTEIN HCNGP").
- eggNOG **KOG2959** (conserved across Eukaryota).
- Feature table: N-terminal REGION 1..40 "Disordered" (MobiDB-lite); COMPBIAS 21..32
  "Basic and acidic residues". So the protein is a small (146 aa) protein with a
  disordered, charged N-terminus followed by the HCNGP globular region — architecture
  typical of small nuclear adaptor/regulator proteins, NOT of an enzyme (no catalytic
  domain, no nucleotide/metal-binding motif).
- Sequence has no transmembrane segment and no signal peptide → consistent with the
  UniProt `SUBCELLULAR LOCATION: Nucleus {ECO:0000250}` (by similarity).

## Ortholog function — what the SAP30BP/HCNGP family does (metazoan evidence)

The human ortholog is **SAP30BP** (SAP30 binding protein; HCNGP family). Two documented,
non-mutually-exclusive functional threads in the family:

1. **Transcriptional corepression via SAP30 / Sin3–HDAC.** SAP30BP was identified as a SAP30
   (Sin3-associated protein 30) binding partner; the family is annotated as an HCNGP
   transcriptional regulator that promotes histone-deacetylase-mediated repression
   (NCBI Gene 29115 for SAP30BP; OMIM 610218; the broader SAP30/Sin3 corepressor literature).
   This is consistent with the PomBase IC annotation GO:0045814 "negative regulation of gene
   expression, epigenetic" and the InterPro2GO annotation GO:0006355 "regulation of
   DNA-templated transcription".
2. **Splicing cofactor for RBM17/SPF45 on short introns.** SAP30BP interacts with RBM17/SPF45
   and is essential for splicing of a subset of human short introns with truncated
   polypyrimidine tracts; a UHM in RBM17 binds a UHM-ligand motif in SAP30BP, recruiting
   RBM17 to phosphorylated SF3B1 [Fukumura et al., Cell Reports 2023, PMID:38065098; the
   fly homologs of SAP30BP and RBM17 were detected on a short (62 nt) but not long (147 nt)
   intron, and yeast two-hybrid showed RBM17–SAP30BP interaction — i.e. the interaction is
   conserved beyond mammals]. This is a MORE RECENTLY characterized function of the family
   and is arguably the better-supported biochemical role for the domain.

IMPORTANT CAVEAT: both threads are established for the *human/animal* ortholog. For S. pombe
mug151 there is NO published biochemical demonstration of either a SAP30/Sin3 interaction or
a spliceosomal role; the family assignment is by sequence/domain only. So these inform a
plausible molecular hypothesis but must NOT be asserted as established S. pombe functions.

## What is actually KNOWN about mug151 in S. pombe

- **Meiotically up-regulated**: transcript is induced in meiosis (basis of the "mug" name and
  the UniProt `KW Meiosis` / GO:0051321 keyword). Up-regulation of expression during meiosis
  does NOT by itself establish a meiotic *function*.
- **PMID:16303567** (Martín-Castellanos et al., Curr Biol 2005): a screen deleting 175
  meiotically-upregulated genes. It reports **seven** genes as critical for meiotic events
  (rec24, rec25, rec27, tht2, bqt1, bqt2, moa1). **mug151 is NOT among the seven.** mug151 was
  one of the 175 deletions assayed but showed no reported critical meiotic phenotype in that
  screen. The UniProt `FUNCTION: Has a role in meiosis {ECO:0000269|PubMed:16303567}` and the
  `mug` name therefore rest on membership in the meiotically-upregulated set + the deletion
  screen, not on a demonstrated specific meiotic mechanism. (Abstract-only in cache;
  full_text_available: false. Do not overrule the curator — but the annotation is
  expression-driven, and the screen positively excluded mug151 from its "critical" list.)
- **Deletion viable / non-essential**: PomBase phenotype FYPO:0002060 "viable vegetative cell
  population" and FYPO:0002177 "viable vegetative cell with normal cell morphology" (fetched
  via PomBase API 2026-07-06). Mild growth phenotypes reported: FYPO:0009007 "decreased
  vegetative cell population viability", FYPO:0001355 "decreased vegetative cell population
  growth".
- **High-throughput stress-screen phenotypes** (deletion library screens): resistance to
  cadmium (FYPO:0000763), cycloheximide (FYPO:0000764), diamide (FYPO:0002693), ethanol
  (FYPO:0001453), tunicamycin (FYPO:0001034), lithium (FYPO:0001583), tert-butyl hydroperoxide
  (FYPO:0003383), amorolfine (FYPO:0009066); sensitivity to vanadate (FYPO:0003656) and EGTA
  (FYPO:0007931). These are pleiotropic HT-screen hits, not a specific characterized pathway.

## KNOWN vs NOT-KNOWN summary

KNOWN:
- Small nuclear protein of the SAP30BP/HCNGP (Pfam PF07818) family; human ortholog SAP30BP.
- Transcript is meiotically up-regulated.
- Deletion is viable (non-essential), normal cell morphology; only mild/HT-screen phenotypes.
- Predicted nuclear localization (by similarity).

NOT KNOWN (genuine gaps):
- The **molecular function of the S. pombe protein has never been assayed** (GOA carries
  GO:0003674 ND). No demonstrated catalytic or binding activity in S. pombe.
- Whether mug151 actually participates in transcriptional corepression (Sin3/HDAC) OR in
  pre-mRNA splicing (RBM17-type) in S. pombe — the two candidate family functions — is
  undetermined. The domain is compatible with either, but neither is experimentally
  demonstrated in fission yeast.
- Whether mug151 has a genuine, specific meiotic role, or whether its "mug" status simply
  reflects meiotic transcriptional induction of a broadly-acting nuclear regulator, is
  unresolved. The 2005 screen did NOT place it among the meiotically-critical genes.
- No characterized phenotype tying loss of mug151 to a defined biological process.

## Annotation decisions (rationale)

- GO:0005634 nucleus (IEA, GO_REF:0000044, SubCell): ACCEPT/KEEP_AS_NON_CORE — consistent with
  UniProt ECO:0000250 nuclear location and family (nuclear transcriptional/splicing regulator).
  Localization, not the core "function".
- GO:0006355 regulation of DNA-templated transcription (IEA, InterPro IPR012479): the
  best-supported *functional* inference from the domain family (transcriptional-regulator
  family). KEEP_AS_NON_CORE — reasonable domain-based inference but unproven in S. pombe, and
  the family also has a splicing role, so it is not exclusively transcriptional.
- GO:0045814 negative regulation of gene expression, epigenetic (IC:PomBase): in the UniProt DR
  block but NOT in the GOA TSV snapshot — noted; consistent with the SAP30/Sin3-HDAC family
  hypothesis. (Not present as a row in `mug151-goa.tsv`, so not added as an existing_annotation
  row; discussed in notes only.)
- GO:0003674 ND / GO:0005575 ND / GO:0008150 ND (PomBase GO_REF:0000015): these are the honest
  "not yet annotated" placeholders — ACCEPT as accurate reflections of the current knowledge
  state for a dark gene (do not invent MF/BP/CC to replace them).
- Meiosis: no separate GOA row for GO:0051321 in the TSV (it is the UniProt KW→GO). Treat the
  meiotic role as expression-driven and unproven; capture in knowledge_gaps.
