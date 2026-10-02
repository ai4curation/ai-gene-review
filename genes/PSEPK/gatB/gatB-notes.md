# gatB curation notes

- Q88PC0 is the ATP-dependent GatB subunit of heterotrimeric GatABC
  [file:PSEPK/gatB/gatB-uniprot.txt, "SUBUNIT: Heterotrimer of A, B and C subunits."].
- The reviewed record includes both Glu-tRNA(Gln) and Asp-tRNA(Asn)
  transamidation reactions [file:PSEPK/gatB/gatB-uniprot.txt,
  "Reaction=L-glutamyl-tRNA(Gln) + L-glutamine + ATP + H2O"].
- The Asn-forming reaction is required in the PSEPK pathway because the genome
  has non-discriminating AspS but no canonical AsnRS; the corresponding route
  is experimentally established in Pseudomonas aeruginosa
  [PMID:14729703, "The essential role of AdT in the formation of Asn-tRNA in P. aeruginosa"].

## 2026-09-27 retired process term

- GO:0070680 was retired in GO release 2026-05-19, so the NEW proposal and the
  authored core process now use GO:0043039 (tRNA aminoacylation), the
  bacterial_aminoacyl_trna_charging module's root concept; the module
  carries the transamidation step itself without a term id. GO's own replaced_by for it, GO:0070981 L-asparagine biosynthetic process, is not used: the
  transamidation route ends at Asn-tRNA(Asn), not free asparagine. The evidence and reasoning are unchanged.
