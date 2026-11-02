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

## 2026-10-26 complete annotation reassessment

GatB is the ATP-dependent acceptor-side subunit of the soluble GatABC tRNA-dependent amidotransferase. With ammonia supplied by GatA and the structural support of GatC, it converts Asp-tRNA(Asn) to Asn-tRNA(Asn). The conserved complex also has Glu-tRNA(Gln)-to-Gln-tRNA(Gln) capacity when that substrate is available; these reactions modify the charged amino acid rather than form its ester bond to tRNA.

Exact accession Q88PC0 and KT2440 symbol/locus were checked against the immutable UniProt record and current fetched identity snapshot. All original machine-seeded row fields and order are preserved. Actual Falcon/fallback attempts failed; no provider report was fabricated. Normal publication caching completed; FEBA retrieval was attempted but no data source was reachable.

The target biochemical assignment rests on curated HAMAP/family and site evidence, augmented by the source-specific comparative papers below. No generic family label is treated as a native kinetic assay. Ordinary relationship metadata does not negate a real complex contribution; contributes_to cores explicitly represent shared catalytic work. Integral substrate/cofactor binding and the supported intracellular location are not classified as peripheral solely because they are binding or location. Current QuickGO retires the amino-acid-specific BP terms; original ids/labels remain unchanged and reviews use current supported process replacements.

- PMID:14729703: Native PAO1 uses direct GlnRS and indirect Asn formation; its GatABC also transamidates supplied heterologous Glu-tRNA(Gln) in vitro. Do not infer native KT2440 Gln-transamidation flux from that capacity.
- PMID:25548166: PAO1 transamidosome structure and kinetics distinguish stabilization of the mischarged Asp-tRNA substrate from product release. This is a comparative architectural basis, not a native KT2440 complex or error-rate measurement.

The inherited reviewer-authored NEW GO:0043039 charging proposal is retired: GatABC modifies the charged amino acid, not its ester linkage. Existing broad translation and obsolete pathway rows instead point to GO:0019988 as a lateral mechanistic correction. The machine-seeded rows are untouched. The Asn route is the physiological inference; Gln-forming substrate capacity is kept separate from native pathway flux.
