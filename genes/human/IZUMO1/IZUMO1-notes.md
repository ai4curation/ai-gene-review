# IZUMO1 notes

Deep research (`just deep-research-falcon human IZUMO1 --fallback perplexity-lite`) failed in this
environment (no agentapi / perplexity provider). Research done directly from cached publications and
the UniProt record.

## Identity
- UniProt Q8IYV9, IZUMO1; Izumo family (IZUMO domain helical bundle + Ig-like domain), single-pass type I
  membrane protein, sperm-specific.

## Function
- Mouse knockout: males sterile; sperm bind and penetrate the zona pellucida but cannot fuse with eggs
  [PMID:15759005 "They produced normal-looking sperm that bound to and penetrated the zona pellucida but were incapable of fusing with eggs."].
  Antibody to human Izumo blocks fusion of human sperm with zona-free hamster eggs
  [PMID:15759005 "addition of the antibody against human Izumo left the sperm unable to fuse with zona-free hamster eggs"].
- Egg receptor is JUNO (IZUMO1R/FOLR4); interaction is conserved in humans
  [PMID:24739963 "We show that the Izumo1-Juno interaction is conserved within several mammalian species, including humans."].
- Crystal structure of human IZUMO1-JUNO complex; beta-hairpin is the JUNO-binding platform
  [PMID:27309808 "The central β-hairpin region of IZUMO1 provides the main platform for JUNO binding"].
- Human oolemmal FCRL3/MAIA interacts with IZUMO1/JUNO complex
  [PMID:36070373 "MAIA forms a highly stable interaction with the known IZUMO1/JUNO sperm-egg complex, permitting specific gamete fusion."].
- IZUMO1-SPACA6-TMEM81 trimeric sperm complex, human orthologs interact in vitro
  [PMID:39423812 "we show that Izumo1, Spaca6, and Tmem81 interact in zebrafish sperm and that the human orthologs interact in vitro"].
- IZUMO1-JUNO is an adhesion step; IZUMO1 is not established as the fusogen (UniProt: "The ligand-receptor
  interaction probably does not act as a membrane 'fusogen'").

## Localization
- Initially in acrosomal membranes (inner and outer) of sperm head; exposed on sperm plasma membrane surface
  only after the acrosome reaction, relocating to the equatorial segment (UniProt; PMID:15759005; PMID:36070373).
- ER retention via FREY during spermatogenesis (mouse, UniProt by similarity) -- biosynthetic transit.
- Conclusion: plasma membrane (post-acrosome-reaction sperm), extracellular domain exposed; resident in
  acrosomal membrane before acrosome reaction. Not on surface of non-acrosome-reacted sperm.

## Curation decisions
- Zona pellucida binding (IBA/IEA, rat donor): contradicted by mouse KO phenotype (ZP binding normal) -> REMOVE.
- receptor ligand activity / signal transduction: JUNO is a GPI-anchored receptor with no shown signaling
  output; IZUMO1 is an adhesion molecule. Over-annotation; signal transduction IEA removed.
