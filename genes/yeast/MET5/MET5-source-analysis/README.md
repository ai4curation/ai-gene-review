# Yeast sulfite-reductase domain evidence

Source: Rotte et al. (2001), PMID:11319255,
[original article](https://doi.org/10.1093/oxfordjournals.molbev.a003853).
The publication title concerns protist pyruvate metabolism, but its Results and
Figure 3 explicitly compare the yeast sulfite-reductase subunits. These are
sequence/domain comparisons, not isolated-subunit FMN-binding measurements.
The standard PMID refresh and full-text warming did not retrieve the publisher
body into the PMID cache. This extraction preserves the inspected, normally
cached publisher text without rewriting that cache or inventing a quotation.

Source cache SHA256: `649f64b821d71bbf695f31f7bddfbde60fee7bf53dea9c81106b0c712f90bd27`.
Reproduce with `uv run python genes/yeast/MET5/MET5-source-analysis/extract_domain_evidence.py`.

## Verbatim target passages

> Regions homologous to PFO domain III and a portion of domain II plus the FAD and NADP domains of CPR are found in the Saccharomyces cerevisiae MET10 gene product (L26504), which encodes the α-subunit of assimilatory sulfite reductase (SRα) (Hansen, Cherest, and Kielland-Brandt 1994 ), and in the Schizosaccharomyces pombe homolog (T41439) (fig. 3G ).

> PuSR encodes a translational fusion of PFO domains I, II (partial), and VI with the FMN domain of CPR, which, in turn, is fused to a hemoprotein domain (fig. 3F ).

> F, Conservation between PNO and putative sulfite reductase from Saccharomyces cerevisiae (PuSR; P47169) and Schizosaccharomyces pombe (014167). G, Sulfite reductase α-subunit (MET10) from yeast (L26504) and S. pombe (T41439).

## Interpretation

The Results identify Met10/SR-alpha with FAD and NADP domains. The Figure 3F
legend identifies PuSR as S. cerevisiae P47169 (Met5); its architecture includes
the FMN domain fused to a hemoprotein domain. This supports the domain-based
placement of FMN on Met5 rather than Met10, together with the independent
Met10 sequence study and measured FMN content of the complete holoenzyme.
It does not show direct cofactor binding by purified isolated Met5.
