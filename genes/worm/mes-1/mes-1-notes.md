# mes-1 (G5EBL2, WBGene00003219) review notes

## Provenance of this research

- Automated deep research (FutureHouse, Perplexity, OpenAI) was not available in this
  environment: no provider API keys. No `-deep-research-<provider>.md` file was generated.
  The only provider file is the verbatim WormBase description
  (`mes-1-deep-research-wormbase.md`).
- Literature gathered by hand on 2026-11-16:
  - PubMed E-utilities query `(mes-1[tiab] OR "MES-1"[tiab]) AND elegans[tiab]` (20 hits);
    relevant papers cached with `just fetch-pmid`.
  - Web search for the Bei et al. 2002 full text; the author PDF (Mello lab site) was read
    with pdftotext, but it is not in the publication cache, so its sentences are not used as
    `supporting_text`.
  - Kinase-domain catalytic residue check: `mes-1-bioinformatics/kinase_motifs.py`,
    results in `mes-1-bioinformatics/RESULTS.md`.

## Identity

- 966-aa single-pass type I transmembrane protein: signal peptide 1-19, extracellular
  20-470, TM 471-491, cytoplasmic 492-966 with a protein kinase-like domain (656-966).
  PANTHER PTHR44535:SF1 (NEK9 subfamily). Maternal-effect sterile.
- Pseudokinase: [PMID:11003841 "mes-1 encodes a receptor tyrosine kinase-like protein,
  though it lacks several residues conserved in all kinases and therefore is predicted not
  to have kinase activity."] UniProt DOMAIN: "The protein kinase domain is predicted to be
  catalytically inactive." Own check (RESULTS.md): the catalytic-loop Asp aligns to Arg832
  (loop reads HTRVTTLN), the DFG Asp to Asn860 (NFG), and there is no glycine-rich loop. No
  kinase assay has been reported.

## Germline asymmetric divisions (P2, P3)

- [PMID:7555722 "mes-1 embryos display a premature and progressive loss of polarity in these
  divisions"] [PMID:7555722 "As an apparent consequence of these defects, P4 is transformed
  into a muscle precursor, like its somatic sister cell D, and generates up to 20 body muscle
  cells instead of germ cells."]
- [PMID:11003841 "MES-1 is present in four- to 24-cell embryos, where it is localized in a
  crescent at the junction between the germline cell and its neighboring gut cell."]
  [PMID:11003841 "during early stages of mitosis in P(2) and P(3), one centrosome is
  positioned adjacent to the MES-1 crescent."]
- PAR-2 orientation [PMID:20823070 "The PAR-2 localization during the asymmetric P2 and P3
  divisions is controlled by extracellular signals via MES-1/SRC-1 signaling."]
- GPR-1/2 asymmetry is in P2, not EMS [PMID:21903670 "We show that MES-1/Src signaling plays
  an instructive role in P(2) for asymmetric GPR-1/2 localization and normal spindle
  orientation."]

## P2/EMS signaling (EMS spindle orientation, endoderm)

- [PMID:12110172 "two tyrosine kinase-related genes, src-1 and mes-1, are required for the
  accumulation of phosphotyrosine between P2 and EMS."] [PMID:12110172 "src-1 and mes-1
  mutants strongly enhance endoderm and EMS spindle rotation defects associated with Wnt
  pathway mutants."]
- Bei et al. full text (author PDF, read online): double mutants with Wnt pathway genes show
  "an endoderm to mesoderm transformation in the E cell lineage" and "a fully L/R division
  axis in EMS", which "appeared to result from a failure of the nascent mitotic apparatus to
  rotate onto the A/P axis". MES-1 junctional localization needs MES-1 in both cells; MES-1
  "may therefore function directly as both ligand and receptor in a homotypic interaction".
  The UniProt IGI row "left/right axis specification" appears to come from this L/R
  division-axis wording, which describes EMS spindle orientation, not body L/R asymmetry.
- Downstream: LET-99 and LIN-5 (PMID:27672093), PIG-1 (PMID:30213539), CED-10/ARX-2
  (PMID:39891664), nuclear anchoring (PMID:20298434).
- Werts et al. 2011 found GPR-1/2 symmetric in EMS and ruled out LET-99 inhibition as the
  localizing mechanism, which dates the UniProt claim that MES-1 controls EMS spindle
  orientation by enriching GPR-1/2 and excluding LET-99 at the junction.

## Other

- mes-1 sterility (germline-less animals) is linked to resistance to P. aeruginosa-induced
  neurodegeneration (PMID:26475858). This follows from germline loss; not annotated.

## Source text checks

- WormBase: all claims trace (RTK-like protein, unequal germline divisions, spindle and
  P granule positioning). Omits P2/EMS signaling with SRC-1 (endoderm, EMS spindle) and the
  predicted inactive kinase.
- UniProt FUNCTION: P2/P3 and SRC-1 statements fine; "Controls EMS spindle orientation
  probably by promoting lin-5 and gpr-1/2 enrichment at, and let-99 exclusion from the
  junction between P2 and EMS cells" is outdated (PMID:21903670, PMID:27672093).

## Annotation decisions (summary)

- Kinase activity rows (IBA S/T kinase, IEA protein kinase, IEA and ISS tyrosine kinase)
  removed: pseudokinase. ATP binding marked over-annotated.
- Left/right axis specification modified to establishment of mitotic spindle orientation;
  embryonic digestive tract morphogenesis modified to endodermal cell fate specification.
- Core: plasma membrane at the P2/EMS contact; asymmetric cell division; establishment of
  mitotic spindle localization; cell fate specification.
