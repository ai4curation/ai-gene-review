# nlp-29 (Caenorhabditis elegans) — research notes

UniProt: O44664 (NLP29_CAEEL). WormBase: WBGene00003767 / B0213.4. Chromosome V.
Gene: neuropeptide-like protein 29. Part of the *nlp-29* cluster (nlp-27..nlp-34) of the
YARP (YGGW-amide related peptide) family. Flagship project: CAEEL_SURVEILLANCE_IMMUNITY.

This is a small, secreted, infection/wounding-inducible antimicrobial-peptide (AMP) precursor.
Notes below separate what is KNOWN (with provenance) from what is NOT known (the deliverable
for a "dark" effector peptide).

## Protein architecture (from UniProt O44664)

- 73-aa precursor (PE 2, evidence at transcript level). Signal peptide 1–22; SUBCELLULAR
  LOCATION: Secreted.
- The precursor is predicted (ECO:0000255) to be cleaved on pairs of basic residues into
  several short amidated peptides: QWGYGGY-amide (23–29), GYGGYGGY-amide (32–39), and
  four GMYGGY/GMYGGW-amide repeats (42–71). All the mature peptides are Tyr/Trp-amidated
  glycine/tyrosine-rich motifs — hence "YGGW-amide related peptide" (YARP) family.
- KEYWORDS: Amidation; Antibiotic; Antimicrobial; Fungicide; Neuropeptide; Secreted; Signal;
  Repeat; Cleavage on pair of basic residues.
- Note: the peptide cleavage sites, amidation, and "Antimicrobial/Fungicide/Neuropeptide"
  keywords are all UniProt *predictions/keyword-transfers* (ECO:0000255 / keyword), not direct
  biochemical demonstration for NLP-29 peptides themselves.

## KNOWN — expression & regulation (well supported experimentally)

nlp-29 is an infection- and damage-inducible epidermal (hypodermal) AMP gene. It is the
canonical transcriptional *readout* of the C. elegans epidermal antifungal immune pathway.

- Identified as one of 32 C. elegans *nlp* neuropeptide-like genes; placed by sequence in the
  YGGWamide family [PMID:11717458 "The nlp genes define at least 11 families of putative
  neuropeptides with unique motifs"]. This paper is purely a bioinformatic
  family/preproprotein prediction; it is the ISM basis for the GOA "neuropeptide receptor
  binding" and "extracellular" annotations. Note that its general statement "Most C. elegans
  nlp gene expression is in neurons" does NOT apply to nlp-29, whose expression is epidermal.
- Infection-inducible AMP whose expression is differentially regulated by fungal vs bacterial
  infection and depends in part on the TIR-domain adaptor tir-1/SARM
  [PMID:15048112 "Expression of two of these peptides, NLP-29 and NLP-31, was differentially
  regulated by fungal and bacterial infection and was controlled in part by tir-1"].
- Induced in the epidermis by both infection (fungus *Drechmeria coniospora*) AND sterile
  physical wounding; a conserved p38-MAPK (PMK-1) cascade is required in the epidermis for
  both responses [PMID:18394898 "Injury induces a wound-healing response in C. elegans that
  includes induction of nlp-29 in the epidermis"; "a conserved p38-MAP kinase cascade is
  required in the epidermis for the response to both infection and wounding"].
- The tribbles-like kinase NIPI-3 is required for nlp-29 induction after infection but not
  after wounding — infection and wounding converge on the same p38 cassette via distinct
  upstream inputs [PMID:18394898 "We find NIPI-3 is required only for nlp-29 induction after
  infection and not after wounding"].
- Upstream of p38: G-protein signaling and PKCδ (tpa-1), with pkc-3 acting nonredundantly, and
  specific C-type phospholipases; identified in a forward screen for mutants failing to express
  nlp-29 after fungal infection [PMID:19380113 "In a screen for mutants that fail to express
  nlp-29 following fungal infection, we isolated alleles of tpa-1, homologous to the mammalian
  protein kinase C (PKC) delta"; "C. elegans PKC acts through the p38 MAPK pathway to regulate
  nlp-29"; "the tribbles-like kinase nipi-3 acts upstream of PKCdelta"].
- Also induced by osmotic stress and physical injury, not only infection
  [PMID:19380113 "Upon physical injury and osmotic stress" — INDUCTION, per UniProt CC].
- Expression is transcriptionally driven by the STAT-like factor STA-2 (with the SLC6
  transporter SNF-12) during molting and after adult epidermal injury; nlp-29 is part of a
  >dozen-AMP module [PMID:33259791 "STAT/STA-2 and SLC6 (solute carrier)/SNF-12-dependent
  expression of antimicrobial peptide (AMP) genes"]. (UniProt records this as
  "Transcriptionally regulated by the transcription factor sta-2".)
- Developmentally, nlp-29 oscillates with the molting cycle, peaking during lethargus
  [UniProt DEVELOPMENTAL STAGE, ECO:0000269|PMID:33259791: "expressed in an oscillating
  pattern with expression increasing during the lethargus phase"].
- Tissue: weakly/not expressed without infection; upon *D. coniospora* infection expressed in
  hypoderm and in perivulval cells where spores adhere [UniProt TISSUE SPECIFICITY, PMIDs
  11717458/15048112/18394898/19380113]. The nlp-29 promoter (Pnlp-29::GFP, the "IFB" reporter)
  is a standard immune reporter.

## KNOWN — a downstream signaling (somnogen) role via NPR-12

Beyond being an effector, secreted NLP-29 peptide has a demonstrated cross-tissue signaling
function: after wounding/infection it promotes protective sleep.

- NLP-29 acts through the neuropeptide receptor NPR-12 on locomotion-controlling neurons that
  are presynaptic to the sleep-active RIS neuron, depolarizing RIS to induce sleep
  [PMID:33259791 "for one AMP, neuropeptide-like protein (NLP)-29, that it acts through the
  neuropeptide receptor NPR-12 in locomotion-controlling neurons that are presynaptic to RIS
  and that depolarize this neuron to induce sleep"].
- This is the strongest direct evidence that (a) NLP-29 engages a specific GPCR (NPR-12), and
  (b) it functions as a signaling ligand, not only as a putative microbicide. It retrospectively
  supports the family-predicted "neuropeptide receptor binding" annotation with a named receptor.
- UniProt FUNCTION summarizes: "Through the neuropeptide receptor nlp-29, induces sleep..." —
  this phrasing is garbled (the receptor is NPR-12, not "nlp-29"); the CC provenance is
  PMID:33259791.

## NOT KNOWN — the load-bearing gaps (deliverable)

1. **Direct microbicidal activity & mechanism (MF-dark).** Whether the mature amidated NLP-29
   peptides *themselves* directly kill or inhibit microbes — and by what mechanism (membrane
   permeabilization? specific target?) — is not established in the cached primary literature.
   Every C. elegans study above uses nlp-29 as an *induced-expression readout*; the "antibacterial
   against S. marcescens / antifungal against D. coniospora" statements in UniProt FUNCTION are
   attributed to PMID:15048112/PMID:19380113, which demonstrate infection-dependent *induction*
   and genetic *requirement of the pathway*, not a purified-peptide killing assay for NLP-29.
   (The related family member NLP-31 has been the one more often tested biochemically in the
   literature; NLP-29 itself is comparatively unassayed.) → BIOLOGY gap, MF_DARK.
   NOTE: this is exactly why GO MF for nlp-29 is essentially only the family-predicted
   "neuropeptide receptor binding"; there is no curated MF term capturing "antimicrobial peptide
   activity".

2. **In-vivo necessity of nlp-29 itself.** Because nlp-29 sits in a redundant multigene AMP
   cluster (nlp-27–34, plus the cnc caenacins), the phenotypic contribution of *nlp-29 alone*
   (single-gene loss of function) to pathogen resistance/survival is not cleanly established in
   the cached literature — most functional genetics manipulates upstream regulators or the whole
   cluster. → BIOLOGY gap (redundancy).

3. **Which mature peptide does what.** The precursor yields ≥6 distinct amidated peptides; which
   one(s) mediate antimicrobial activity vs which engage NPR-12 (the somnogen role) is unknown.
   The processing itself (proprotein convertase, amidation) is predicted, not directly shown for
   NLP-29. → BIOLOGY gap.

4. **Receptor scope.** NPR-12 is the only demonstrated receptor (sleep role, PMID:33259791).
   Whether NLP-29 peptides have additional receptors/targets in the antimicrobial context, or act
   receptor-independently as a microbicide, is unresolved. → BIOLOGY gap.

## Existing GOA annotations to review (4)

1. GO:0005576 extracellular region — IEA (GO_REF:0000044, from SubCell "Secreted"). Consistent
   with signal peptide + Secreted. ACCEPT.
2. GO:0003674 molecular_function (root) — ND (GO_REF:0000015). "No data" placeholder from
   WormBase. Root/ND is uninformative; a more specific MF (neuropeptide receptor binding) is
   annotated. Mark as over-annotated placeholder / remove-worthy per ND conventions.
3. GO:0005576 extracellular region — ISM (PMID:11717458). Same location, sequence-model basis.
   ACCEPT (redundant with #1 but valid).
4. GO:0071855 neuropeptide receptor binding — ISM (PMID:11717458). Family-based prediction;
   now corroborated by NPR-12 interaction (PMID:33259791). ACCEPT (keep; evidence upgraded by
   later work but GOA record remains ISM).

BP terms present in UniProt DR-GO but NOT in the GOA TSV (dropped after GO_REF:0000043 SPKW
retirement): defense response to bacterium (GO:0042742), defense response to fungus (GO:0050832),
killing of cells of another organism (GO:0031640), neuropeptide signaling pathway (GO:0007218) —
all IEA:UniProtKB-KW. These are biologically well-motivated but are not in existing_annotations
(only GOA annotations are reviewed here); captured instead in core_functions/knowledge_gaps.

## Provenance caveat

The five *core-pathway* primary publications (11717458, 15048112, 18394898, 19380113, 33259791)
are cached ABSTRACT-ONLY (full_text_available: false). Reviews must therefore not REMOVE
experimental-style annotations on the basis of abstract wording alone; where the abstract does not
let me verify a specific claim I defer (ACCEPT/UNDECIDED) rather than overrule curators. THREE
publications are cached FULL-TEXT (full_text_available: true) and were used for verbatim provenance:
PMID:18636113 (Pujol 2008 PLoS Pathogens), PMID:29301098 (E 2018 Neuron), PMID:22870075 (Pujol 2012
Front Immunol, open-questions review).

## Review completed — key direct evidence and decisions (journal)

- STRONGEST DIRECT MF EVIDENCE (upgrades the ISM neuropeptide-receptor-binding annotation):
  E 2018 shows synthetic NLP-29 activates the neuronal orphan GPCR NPR-12 in a heterologous cell
  assay — [PMID:29301098 "induced a significant elevation of calcium, while the solvent-only control
  did not cause any changes"] — with specificity vs the paralog NLP-31 and vs NPR-32/beta2-AR, plus
  genetic epistasis (nlp-29;npr-12). This is why GO:0071855 is ACCEPTed as core rather than left as a
  bare family prediction.
- DIRECT-MICROBICIDAL activity for NLP-29 itself remains UNPROVEN in the cached literature: the
  in-vivo antifungal effect is shown only by whole-cluster overexpression — [PMID:18636113 "These
  results indicate that the nlp genes can contribute in vivo to increased resistance to fungal
  infection"] — and the nlp-29 single null is phenotypically silent — [PMID:18636113 "we saw no marked
  change in its resistance to D. coniospora infection"]. Hence the MF_DARK + in-vivo-necessity
  knowledge gaps; no MF antimicrobial-activity term is asserted (proposed as an ONTOLOGY gap instead).
- Annotation decisions (4 PENDING resolved + 2 NEW): GO:0005576 extracellular IEA -> ACCEPT;
  GO:0003674 ND root -> REMOVE (superseded placeholder); GO:0005576 extracellular ISM -> ACCEPT;
  GO:0071855 neuropeptide receptor binding ISM -> ACCEPT (core); + NEW GO:0050832 defense response to
  fungus (IEP); + NEW GO:0007218 neuropeptide signaling pathway (IMP).
- VALIDATION FLAKINESS: the pre-edit hook re-fetches references over the network; PMID:22870075
  full-text fetch (openalex/cell.com) intermittently 403s/times out and falls back to abstract-only,
  which fails otherwise-valid full-text quotes. Kept 22870075 as a reviewed reference only (no
  supporting_text) and anchored all provenance to PMID:18636113 / PMID:29301098 full text instead.
  `just validate worm nlp-29`, `validate-references`, and `validate-terms` all pass.
