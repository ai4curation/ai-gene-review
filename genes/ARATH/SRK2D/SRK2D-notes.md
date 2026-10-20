# SRK2D / SnRK2.2 (At3g50500, UniProt Q39192) - curation notes

## Deep research status

`just deep-research ARATH SRK2D --provider falcon` failed on 2026-10-20 ("Exception: Failed to
authenticate"); `--provider perplexity` reported the provider unavailable and `--provider openai`
failed with an invalid API key. No deep-research file was generated. These notes were written
from my own reading of cached publications (`publications/PMID_*.md`) and the UniProt record.

## Identity and naming

- UniProt Q39192 (SRK2D_ARATH), primary gene name SRK2D; synonyms SNRK2.2, OSKL3, SPK2;
  At3g50500. The folder uses the UniProt primary name (SRK2D). In the literature the protein
  is mostly called SnRK2.2.
- Closest paralogs: SRK2I/SnRK2.3 (Q39193, At5g66880) and SRK2E/OST1/SnRK2.6 (Q940H6,
  reviewed in `genes/ARATH/OST1`). Together they form ABA-activated SnRK2 subclass III.

## Function summary with provenance

- SnRK2.2 and SnRK2.3 are redundant kinases needed for ABA responses in seeds and roots
  [PMID:17307925 "two protein kinases, SNF1-RELATED PROTEIN KINASE2.2 (SnRK2.2) and SnRK2.3, control
  responses to ABA in seed germination, dormancy, and seedling growth in Arabidopsis thaliana"].
  Only the double mutant shows the phenotype [PMID:17307925 "A snrk2.2 snrk2.3 double mutant, but
  not snrk2.2 or snrk2.3 single mutants, showed strong ABA-insensitive phenotypes in seed
  germination and root growth inhibition"].
- Mechanism through ABF phosphorylation [PMID:17307925 "The snrk2.2 snrk2.3 double mutant had a
  greatly reduced level of a 42-kD kinase activity capable of phosphorylating peptides from ABF
  (for ABA Response Element Binding Factor) transcription factors"].
- Direct in-gel phosphorylation of AREB1 by SRK2D [PMID:16446457 "we showed that ABA-activated
  SRK2C, SRK2D, SRK2E, SRK2F, and SRK2I ( 24 ) can phosphorylate the AREB1 polypeptide by using
  in-gel kinase activity assay"].
- Phosphorylates the bHLH factor AKS1 in vitro [PMID:28438792 "Three ABA-responsive SnRK2s
  (SnRK2.2/SRK2D, SnRK2.3/SRK2I, and SnRK2.6/SRK2E/OST1) phosphorylated AKS1 in vitro"].
- Triple mutant with OST1 is nearly completely ABA-insensitive [PMID:19420218 "In-gel kinase
  assays showed that all ABA-activated protein kinase activities are eliminated in the triple
  mutant"]; division of labour [PMID:19420218 "SnRK2.6 functions in guard cells, whereas
  SnRK2.2/2.3 specialize in seed germination and seedling growth regulation"].
- Drought [PMID:19880399 "srk2d srk2e srk2i (srk2d/e/i) triple mutants exhibit greatly reduced
  tolerance to drought stress and highly enhanced insensitivity to ABA"]; nuclear localization
  with AREB1 [PMID:19880399 "SRK2D/E/I and AREB1 co-localize and interact in nuclei in planta"].
- Seed development and dormancy [PMID:19541597 "These SnRK2 proteins were mainly expressed in the
  nucleus during seed development and germination"; "SRK2D, SRK2E and SRK2I protein kinases
  involved in ABA signaling are essential for the control of seed development and dormancy"].
- Activation by hyperosmolarity and ABA [PMID:15292193 "Nine of the 10 SnRK2 were activated by
  hyperosmolarity induced by mannitol, as well as NaCl"; "abscisic acid only activated five of the
  nine SnRK2"]. Osmotic signalling in the decuple mutant [PMID:21220313 "SnRK2.2/3/6 functions not
  only in the ABA-dependent pathway, but also in the ABA-independent pathway"].
- Root hydrotropism [PMID:28481327 "hydrotropism depends on the ABA signalling kinase SnRK2.2 and
  the hydrotropism-specific MIZ1, both acting specifically in elongation zone cortical cells"].
- Guard cells: although OST1 dominates, SnRK2.2 contributes; an srk2de double mutant was used as
  an ABA-insensitive guard-cell background [PMID:41417897 "srk2de, a double knockout mutant of
  SRK2D/SnRK2.2 and SRK2E/OST1"].

## Regulation by clade A PP2Cs

- PP2Cs bind and inactivate SnRK2s [PMID:19805022 "Group A PP2Cs interacted physically with SnRK2s
  in various combinations, and efficiently inactivated ABA-activated SnRK2s via dephosphorylation of
  multiple Ser/Thr residues in the activation loop"].
- Y2H: [PMID:19924127 "The three clade A PP2Cs (ABI1, ABI2 and HAB1) were each capable of
  interacting with the three SnRK2 kinases (SnRK2.2, SnRK2.3 and SnRK2.6) in yeast two-hybrid
  (Y2H) assays"].
- In planta with ABI1 [PMID:19874541 "ABI1 interacts with the ABA-signalling kinases OST1, SnRK2.2
  and SnRK2.3 in plants"].
- Park et al. 2009 Y2H [PMID:19407142 "we observe interaction of SnRK2.2 with PP2CA/AHG3 and AHG1
  using the Y2H assay (SOM Figure 3)"]. GOA has IPI rows from this paper with ABI1 (P49597) and
  AHG1 (Q9FLI3), but the main text names PP2CA/AHG3 (P49598) and AHG1. The ABI1 WITH/FROM may be
  an accession slip (P49597 vs P49598) or may come from the supplementary figure that I cannot
  read. Recorded as a possible source-database error; no action other than MODIFY to protein
  phosphatase binding (correct either way, both are clade A PP2Cs).

## Annotation decisions (summary)

- Protein kinase activity / kinase activity rows: MODIFY to protein serine/threonine kinase
  activity (GO:0004674), which the gene already carries (IBA, IEA-EC).
- protein binding IPI with clade A PP2Cs (ABI1, ABI2, HAB1, AHG1): MODIFY to protein phosphatase
  binding (GO:0019903). protein binding with substrates/other partners (AKS1/bHLH122, MAP4K1):
  REMOVE (uninformative; consistent with OST1 review).
- Localization nucleus/cytoplasm/cytosol: ACCEPT.
- Process: ABA response, water deprivation, osmotic stress, seed germination ACCEPT; salt stress
  and gibberellin response KEEP_AS_NON_CORE.
- NEW: abscisic acid-activated signaling pathway (GO:0009738), missing from GOA for SRK2D although
  present on OST1 and SRK2I; hydrotropism (GO:0010274) from PMID:28481327.

## Differences from OST1

OST1 is the predominant guard-cell kinase (SLAC1 activation, stomatal closure); SnRK2.2/2.3
predominate in seeds and roots (germination, dormancy, root growth inhibition, hydrotropism).
SnRK2.2 does not carry the SLAC1 regulator (ion channel regulator activity) or stomatal terms in
GOA, and I did not add them: the evidence for SnRK2.2 in guard cells is mainly redundancy in
higher-order mutants.
