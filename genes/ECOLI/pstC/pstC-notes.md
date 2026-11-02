# pstC notes

## 2026-10-02

`pstC` encodes the second inner-membrane permease of the E. coli PstSACB
phosphate importer. It is homologous to, but non-identical with, PstA and should
be modeled as the PstA partner in the transmembrane pathway rather than as an
independent phosphate transporter.

Cox et al. 1989 provide the key functional evidence: PstC Arg237Gln, Glu240Gln,
and the double substitution all abolished phosphate transport through the Pst
system while leaving alkaline phosphatase repressed [PMID:2646285]. That is a
transport-specific defect and cleanly supports PstC involvement in phosphate
ion transmembrane transport.

The radiation response annotation is phenotype-derived from a Keio deletion
screen [PMID:27718375]. I kept it out of core function because PstC's direct
activity is the phosphate permease contribution, and radiation sensitivity is
likely an indirect consequence of perturbing phosphate uptake or envelope
homeostasis.
