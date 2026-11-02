# gatC curation notes

- Q88PB8 is the small structural GatC subunit of heterotrimeric GatABC
  [file:PSEPK/gatC/gatC-uniprot.txt, "SUBUNIT: Heterotrimer of A, B and C subunits."].
- GatC was curated as contributing to the complex reaction rather than as an
  independently catalytic enzyme.
- Both GatABC outputs are represented at the complex level. The indirect
  Asn-tRNA(Asn) route is supported by the exact Q88PB8 reaction and comparative
  Pseudomonas experiments [PMID:14729703, "The essential role of AdT in the formation of Asn-tRNA in P. aeruginosa"].

## 2026-09-27 retired process term

- GO:0070680 was retired in GO release 2026-05-19, so the NEW proposal and the
  authored core process now use GO:0043039 (tRNA aminoacylation), the
  bacterial_aminoacyl_trna_charging module's root concept; the module
  carries the transamidation step itself without a term id. GO's own replaced_by for it, GO:0070981 L-asparagine biosynthetic process, is not used: the
  transamidation route ends at Asn-tRNA(Asn), not free asparagine. The evidence and reasoning are unchanged.

## 2026-10-26 complete annotation reassessment

GatC is the small structural subunit of the soluble GatABC tRNA-dependent amidotransferase. It supports the assembly that couples GatA glutamine hydrolysis to GatB-mediated modification of a tRNA-bound amino acid, including conversion of Asp-tRNA(Asn) to Asn-tRNA(Asn). GatC contributes to the complete complex reaction without being an autonomous aminoacyl-tRNA ligase or glutaminase.

Exact accession Q88PB8 and KT2440 symbol/locus were checked against the immutable UniProt record and current fetched identity snapshot. All original machine-seeded row fields and order are preserved. Actual Falcon/fallback attempts failed; no provider report was fabricated. Normal publication caching completed; FEBA retrieval was attempted but no data source was reachable.

The target biochemical assignment rests on curated HAMAP/family and site evidence, augmented by the source-specific comparative papers below. No generic family label is treated as a native kinetic assay. Ordinary relationship metadata does not negate a real complex contribution; contributes_to cores explicitly represent shared catalytic work. Integral substrate/cofactor binding and the supported intracellular location are not classified as peripheral solely because they are binding or location. Current QuickGO retires the amino-acid-specific BP terms; original ids/labels remain unchanged and reviews use current supported process replacements.

- PMID:14729703: Native PAO1 uses direct GlnRS and indirect Asn formation; its GatABC also transamidates supplied heterologous Glu-tRNA(Gln) in vitro. Do not infer native KT2440 Gln-transamidation flux from that capacity.
- PMID:25548166: PAO1 transamidosome structure and kinetics distinguish stabilization of the mischarged Asp-tRNA substrate from product release. This is a comparative architectural basis, not a native KT2440 complex or error-rate measurement.

The inherited reviewer-authored NEW GO:0043039 charging proposal is retired: GatABC modifies the charged amino acid, not its ester linkage. Existing broad translation and obsolete pathway rows instead point to GO:0019988 as a lateral mechanistic correction. The machine-seeded rows are untouched. The Asn route is the physiological inference; Gln-forming substrate capacity is kept separate from native pathway flux.

### Fidelity assessment resolved

Full PMID:33072044 and PMID:34225495 establish mycobacterial GatC/complex-stability effects on mistranslation. Together with the PAO1 transamidosome mechanism and target GatC family architecture, these support ACCEPT of the existing broad fidelity term as conserved inference. No KT2440 error-rate assay, native mycobacterial stress phenotype, or direct ribosomal action is asserted. The three retired authored charging proposals address a different biochemical distinction. Reciprocal annotation-reviewer consultation found no contrary target boundary.
