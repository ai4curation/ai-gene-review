# gst-32 (Y53F4B.37, UniProtKB Q9NA96) - manual literature research

Deep-research API providers were not available for this session, so this file records a manual
literature search (PubMed MCP plus the cached publication) carried out by the reviewer.

## Search

- PubMed queries `("gst-32" OR "Y53F4B.37") AND elegans` and
  `glutathione S-transferase Caenorhabditis elegans "gst-32"` returned no hits (2026-10-28):
  gst-32 is not named in any title/abstract indexed by PubMed.
- The only publication attached to a GO annotation of gst-32 is PMID:23593298 (Luersen et al.
  2013, PLoS One), full text cached (`publications/PMID_23593298.md`, PMC3620388). gst-32 is
  mentioned only in the body text and Table 2 of that paper.

## Sequence and family (UniProt Q9NA96, TrEMBL, unreviewed)

- 209 aa protein with GST N-terminal (2-81, PROSITE PS50404) and GST C-terminal (83-209,
  PS50405) domains; CDD cd03039 GST_N_Sigma_like and cd03192 GST_C_Sigma_like; PANTHER
  PTHR11571:SF8 (GLUTATHIONE S-TRANSFERASE-RELATED) [file:worm/gst-32/gst-32-uniprot.txt].
- UniProt places it in the GST superfamily, sigma family (ARBA-derived note), whereas Luersen
  et al. describe it as "an alpha-class related GST (gst-32)" [PMID:23593298]. Nematode
  cytosolic GSTs are predominantly sigma-like; the class label is uncertain but the protein is
  clearly a canonical cytosolic (soluble) GST.
- The N-terminus reads MPTYKLTYFN..., i.e. the YxLxYF motif typical of tyrosine-type
  (sigma/alpha/mu/pi) cytosolic GSTs, where the second Tyr (here Tyr8) is the catalytic
  residue that activates glutathione (reviewer observation from the sequence; not
  experimentally tested for gst-32).
- No biochemical characterisation (substrate, kinetics, structure) of GST-32 has been
  published. UniProt PE level 1 reflects only PeptideAtlas proteomic detection.

## Experimental data: PMID:23593298

- Small-scale RNAi screen of 67 glutathione-metabolism genes for survival on 0.15 mM juglone
  (redox cycler / ROS generator) and 3 mM arsenite [PMID:23593298 Table 2 legend: "F1 L4/young
  adults of the treated worms were transferred to 0.15 mM juglone and 3 mM arsenite stress
  plates, respectively"].
- gst-32 (Y53F4B.37, clone II-9O18): juglone survival 87.8 +/- 6.9 (control 90.8 +/- 7.4,
  i.e. no effect); arsenite survival 24.0 +/- 13.2 (control 90.0 +/- 5.8, p<0.01).
- Text: "knockdown of an alpha-class related GST (gst-32), an omega-class GST (gst-44) and an
  extracellular glutathione peroxidase (C11E4.1) less profoundly affected the survival rate
  under arsenite stress (arsenite survival rate of 24.0±13.2 (p<0.01), ..." [PMID:23593298].
- Discussion (interpretive, not tested): "Both, the alpha-class related gst-32 and the GPX are
  implicated in the oxidative stress response by way of their GSH-dependent reduction of
  inorganic and organic peroxides or by their ability to eliminate secondary products of lipid
  peroxidation." [PMID:23593298]. This is a family-level rationale; no peroxidase assay was done.

## Implications for annotation

- The WormBase IMP to GO:0000302 response to reactive oxygen species rests on this paper, but
  the gst-32 RNAi phenotype is arsenite-specific; the direct ROS challenge (juglone) showed no
  effect. The phenotype matches GO:0046685 response to arsenic-containing substance better.
- Glutathione transferase activity is inferred from family membership (IBA, ARBA) and the
  conserved catalytic-Tyr motif; it is plausible but untested.
