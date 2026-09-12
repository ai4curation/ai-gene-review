# adg2 (SPAC19G12.16c / mug46) — curation notes

UniProt: O13854 (ADG2_SCHPO). *Schizosaccharomyces pombe* (NCBITaxon:284812).
PomBase systematic name: SPAC19G12.16c (also SPAC23A1.01c). Standard name: adg2.
Synonym: mug46 ("meiotically up-regulated gene 46").

This is an **understudied ("dark") gene**: PE 3 (Inferred from homology). No targeted
knockout, purification, or biochemical assay of Adg2 itself has been reported. Function
is inferred from (i) sequence/domain features, (ii) genome-wide GPI-protein prediction,
and (iii) co-regulation with characterized cell-separation genes.

## KNOWN (evidence-supported)

### Protein architecture (from UniProt O13854 + inline sequence analysis)
- 670 aa **precursor** with an N-terminal **signal peptide** (residues 1–19, ECO:0000255)
  → enters the secretory pathway.
- **Serine/threonine-rich**: RecName is literally "Serine/threonine-rich protein adg2".
  Inline compositional analysis of the mature chain gives ~50% Ser+Thr (Ser ~198, Thr ~137
  of ~670 residues). This is the hallmark composition of fungal cell-wall/cell-surface
  glycoproteins and adhesin stalks.
- **Heavily N-glycosylated**: 17 predicted N-linked glycosylation sites (CARBOHYD, ECO:0000255);
  UniProt keyword "Glycoprotein"; GlyCosmos lists 17 sites. Consistent with a secreted/surface
  glycoprotein.
- **Disordered region** 526–651 (MobiDB-lite) within the S/T-rich body — consistent with an
  extended, glycosylated stalk rather than a compact globular enzyme.
- **C-terminal hydrophobic tail**: the last ~20 residues (…SLQRISLL**CVFIPLLFLF**) are ~14/20
  hydrophobic, immediately following a small-residue region — the canonical shape of a
  **GPI-anchor addition signal** (omega site + spacer + hydrophobic tail), NOT an internal
  transmembrane helix. No internal TM domains.
- Family/domain calls: **InterPro IPR052479 "GPI-anchor_Adhesion_Reg"**;
  **PANTHER PTHR35185** "SERINE/THREONINE-RICH PROTEIN ADG2-RELATED" (subfamily SF3 = Adg2 itself).
  There is no catalytic domain (no glycoside hydrolase, no kinase, etc.).

### GPI-anchored cell-surface prediction
- adg2 (SPAC19G12.16c) is one of **33 predicted GPI-protein candidates** in the *S. pombe*
  genome identified by a genome-wide computational survey
  [PMID:12845604 "Genome-wide identification of fungal GPI proteins." De Groot et al. 2003 Yeast].
  The abstract states: *"In Sz. pombe … only 33 GPI candidates were identified"* and the method
  screens for a C-terminal GPI attachment consensus plus an N-terminal secretion signal and
  absence of internal TM domains — all of which adg2 satisfies. (Abstract-only in cache; the
  gene-level assignment is the basis of the PomBase TAS `cell surface` annotation.)
- This is the basis for the UniProt SubCell mapping **extracellular region** (SL-0243); note
  UniProt marks "Secreted {ECO:0000305}" (i.e. inferred, not experimental).

### Subcellular localization
- **Endoplasmic reticulum** — experimental, high-throughput YFP-tagging ORFeome localization
  screen [PMID:16823372 "ORFeome cloning and global analysis of protein localization in the fission
  yeast Schizosaccharomyces pombe." Matsuyama et al. 2006 Nat Biotechnol]. This is the
  ECO:0000269 experimental basis in the UniProt SUBCELLULAR LOCATION line ("Endoplasmic reticulum
  {ECO:0000269|PubMed:16823372}"). ER localization is fully consistent with a secretory-pathway
  glycoprotein transiting the ER en route to the surface/wall. Abstract-only in cache (the
  per-protein localization is in the paper's dataset, not the abstract).
- **Cell surface** — TAS (PomBase, is_active_in), original_reference PMID:12845604, i.e. the GPI
  prediction. PomBase's own product description is "conserved fungal cell surface (protein)".

### Transcriptional regulation / process association (co-regulation inference)
- adg2 is a member of the **"Eng1 cluster"**, a nine-gene, tightly cell-cycle-regulated,
  Ace2-controlled module "involved in cell separation"
  [PMID:15966770 "The cell cycle-regulated genes of Schizosaccharomyces pombe." Oliva et al. 2005
  PLoS Biol], verbatim (full text cached):
  *"The Eng1 cluster (Figure 8C) contains nine genes, and these are involved in cell separation.
  The genes are adg1 and adg2 (cell surface glycoproteins), adg3 (β-glucosidase), agn1 and eng1
  (glycosyl hydrolases), cfh4 (chitin synthase regulatory factor), mid2 (an anillin needed for
  cell division and septin organization), ace2 (a cell cycle transcription factor), and SPCC306.11,
  a sequence orphan of unknown function."*
  Each cluster gene carries ≥1 Ace2 binding site (consensus CCAGCC); peak expression is slightly
  after the Cdc15/Cdc18 clusters (M/cytokinesis).
- Flocculation network: adg2 is an Ace2 target whose transcript is down-regulated (1.5–3.4×) when
  the FLO8-like activators Adn2/Adn3 are overexpressed
  [PMID:23236291 "Deciphering the transcriptional-regulatory network of flocculation in
  Schizosaccharomyces pombe." Kwon et al. 2012 PLoS Genet]. (Regulatory placement only; does not
  assign a molecular function to Adg2.)
- **mug46 = meiotically up-regulated gene 46**: adg2 was identified in the meiotic-upregulation
  gene set (Mata et al. 2002 transcriptome). Reflects transcriptional induction during sexual
  differentiation, not a demonstrated meiotic function.

## NOT known (genuine gaps)
- **Molecular function is unknown.** No catalytic domain; no ligand/binding partner identified;
  no adhesin binding activity demonstrated. The IPR052479/PANTHER "adhesion regulation" family
  name is a computational family label, not experimental evidence that Adg2 is an adhesin.
- **Direct biological role is inferred, not demonstrated.** "Involved in cell separation" is a
  *cluster-level co-regulation inference* (Oliva 2005 grouped adg2 with eng1/agn1 by expression
  timing + shared Ace2 sites + a "cell surface glycoprotein" descriptor). Adg2 itself was not
  functionally assayed; there is no adg2Δ separation phenotype in the retrieved literature.
- **GPI anchorage is predicted, not experimentally confirmed** for Adg2 (the C-terminal ω-site
  has not been mapped; the anchor has not been shown biochemically). The experimental localization
  that exists (PMID:16823372) is ER, i.e. a transit/secretory compartment, not confirmation of a
  mature GPI-anchored wall protein.
- **Meiotic/sporulation function** implied by the mug46 name is uncharacterized.

## Annotation-by-annotation plan (GOA has 5)
1. GO:0005576 extracellular region — IEA, GO_REF:0000044 (SubCell SL-0243). KEEP_AS_NON_CORE.
   Defensible from signal peptide + GPI/secretion prediction; broad CC.
2. GO:0005783 endoplasmic reticulum — IEA, GO_REF:0000044 (SubCell SL-0095). KEEP_AS_NON_CORE.
   Backed experimentally by PMID:16823372 (transit compartment for a secretory glycoprotein).
3. GO:0003674 molecular_function (root) — ND, GO_REF:0000015. ACCEPT (honestly captures that MF is
   unknown; do not invent a function).
4. GO:0008150 biological_process (root) — ND, GO_REF:0000015. ACCEPT (BP not experimentally
   established for adg2 itself; cell-separation role is co-regulation inference only).
5. GO:0009986 cell surface — TAS (PomBase), PMID:12845604. KEEP_AS_NON_CORE. Grounded in the GPI
   prediction + S/T-rich glycoprotein architecture; location, not mechanism.

No REMOVE actions: nothing is contradicted, and the two experimental/curated calls (ER, cell surface)
are consistent with the protein's secretory-glycoprotein architecture. No `protein binding`.

core_functions: none author-able with confidence — the molecular function is genuinely unknown.
Leave core_functions empty and put the reasoning in knowledge_gaps (primary deliverable).
