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
   RBM17 to phosphorylated SF3B1 [PMID:38065098, "a U2AF-homology motif (UHM) in RBM17 binds
   directly to a newly identified UHM-ligand motif in SAP30BP"]. This is a recently
   characterized human function of the family, but the accessible abstract does not
   establish that the interaction is conserved in fungi.

IMPORTANT CAVEAT: both threads are established for the *human/animal* ortholog. For S. pombe
mug151 there is NO published biochemical demonstration of either a SAP30/Sin3 interaction or
a spliceosomal role; the family assignment is by sequence/domain only. So these inform a
plausible molecular hypothesis but must NOT be asserted as established S. pombe functions.

## What is actually KNOWN about mug151 in S. pombe

- **Meiotically up-regulated**: transcript is induced in meiosis (basis of the "mug" name and
  the UniProt `KW Meiosis` / GO:0051321 keyword). Up-regulation of expression during meiosis
  does NOT by itself establish a meiotic *function*.
- **PMID:16303567** (Martín-Castellanos et al., Curr Biol 2005): the cached abstract says
  "we have deleted 175 meiotically upregulated genes and found seven genes not previously
  reported to be critical for meiotic events." It names rec24, rec25, rec27, tht2, bqt1,
  bqt2, and moa1, but **does not mention mug151 or its assay result**. UniProt cites the
  full paper for `FUNCTION: Has a role in meiosis {ECO:0000269|PubMed:16303567}`. Because
  the cache is abstract-only (`full_text_available: false`), the gene-specific evidence
  cannot be verified and the curator's full-text assessment must not be overruled.
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
- Small SAP30BP/HCNGP-family protein (Pfam PF07818), predicted nuclear by similarity; human
  ortholog SAP30BP.
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
  unresolved. UniProt asserts an experimentally supported meiotic role from PMID:16303567,
  but the cached abstract of that screen does not mention mug151, so its gene-specific
  assay result cannot be verified without the full text.
- No characterized phenotype tying loss of mug151 to a defined biological process.

## 2026-08-31 research refresh

- `just deep-research SCHPO mug151 --provider perplexity` reached the provider but failed
  with an `insufficient_quota` 401; no Perplexity artifact was produced.
- `just deep-research SCHPO mug151 --provider falcon` completed and wrote
  `mug151-deep-research-falcon.md` plus its Edison artifact. The report found no direct
  mug151-focused functional study and independently recommended retaining molecular
  function, biological process, and experimental localization as unknown. Its cautious
  synthesis supports leaving the family-based transcription/splicing ideas as hypotheses.
- A focused OpenScientist job was launched through `just gene-hypothesis-research` to test
  whether RBM17/SPF45-associated splicing is the ancestral SAP30BP-family function and to
  compare splicing-partner versus SAP30/Sin3/Clr6 evidence in S. pombe. The provider ended
  with `ConnectError: [Errno 8] nodename nor servname provided, or not known`; it wrote no
  result or citations, so it contributed no evidence to the review.
- Repository-wide searches found no existing project, module, or GO-CAM reference to
  mug151/SPAC3H1.03/Q10069, so no linked project/module update is warranted in this gene PR.

## Annotation decisions (rationale)

- GO:0005634 nucleus (IEA, GO_REF:0000044, SubCell): KEEP_AS_NON_CORE — consistent with
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
- GO:0003674 MF ND and GO:0005575 CC ND (PomBase GO_REF:0000015): ACCEPT as accurate
  "not yet annotated" placeholders; do not invent a molecular activity or experimentally
  established active site/component to replace them.
- GO:0008150 BP ND (PomBase GO_REF:0000015): UNDECIDED because UniProt separately asserts an
  experimentally supported role in meiosis from PMID:16303567, whose gene-specific evidence
  cannot be checked in the abstract-only cache.
- Meiosis: no separate GOA row for GO:0051321 in the TSV (it is the UniProt KW→GO mapping).
  Defer to UniProt's ECO:0000269 full-text curation while asking what mug151-specific result
  supports the claim and whether GO:0051321 or a more specific process term is warranted.
