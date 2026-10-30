# gatA curation notes

- Q88PB9 is the amidase-family GatA subunit of heterotrimeric GatABC
  [file:PSEPK/gatA/gatA-uniprot.txt, "SUBUNIT: Heterotrimer of A, B and C subunits."].
- GatA supplies glutaminase chemistry to the complex; full glutaminyl-tRNA
  synthase activity is a property of assembled GatABC.
- GatABC is also required for the indirect Asn-tRNA(Asn) route. The homologous
  Pseudomonas aeruginosa pathway was established experimentally
  [PMID:14729703, "The essential role of AdT in the formation of Asn-tRNA in P. aeruginosa"].

## 2026-09-27 retired process term

- GO:0070680 was retired in GO release 2026-05-19, so the NEW proposal and the
  authored core process now use GO:0043039 (tRNA aminoacylation), the
  bacterial_aminoacyl_trna_charging module's root concept; the module
  carries the transamidation step itself without a term id. GO's own replaced_by for it, GO:0070981 L-asparagine biosynthetic process, is not used: the
  transamidation route ends at Asn-tRNA(Asn), not free asparagine. The evidence and reasoning are unchanged.

## 2026-10-26 complete annotation reassessment

GatA is the glutamine-hydrolyzing subunit of the soluble GatABC tRNA-dependent amidotransferase. It supplies ammonia for conversion of the amino acid already attached to tRNA, supporting Asn-tRNA(Asn) formation from Asp-tRNA(Asn). The conserved complex can also support Gln-forming transamidation when Glu-tRNA(Gln) is supplied.

Exact accession Q88PB9 and KT2440 symbol/locus were checked against the immutable UniProt record and current fetched identity snapshot. All original machine-seeded row fields and order are preserved. Actual Falcon/fallback attempts failed; no provider report was fabricated. Normal publication caching completed; FEBA retrieval was attempted but no data source was reachable.

The target biochemical assignment rests on curated HAMAP/family and site evidence, augmented by the source-specific comparative papers below. No generic family label is treated as a native kinetic assay. Ordinary relationship metadata does not negate a real complex contribution; contributes_to cores explicitly represent shared catalytic work. Integral substrate/cofactor binding and the supported intracellular location are not classified as peripheral solely because they are binding or location. Current QuickGO retires the amino-acid-specific BP terms; original ids/labels remain unchanged and reviews use current supported process replacements.

- PMID:14729703: Native PAO1 uses direct GlnRS and indirect Asn formation; its GatABC also transamidates supplied heterologous Glu-tRNA(Gln) in vitro. Do not infer native KT2440 Gln-transamidation flux from that capacity.
- PMID:25548166: PAO1 transamidosome structure and kinetics distinguish stabilization of the mischarged Asp-tRNA substrate from product release. This is a comparative architectural basis, not a native KT2440 complex or error-rate measurement.

The inherited reviewer-authored NEW GO:0043039 charging proposal is retired: GatABC modifies the charged amino acid, not its ester linkage. Existing broad translation and obsolete pathway rows instead point to GO:0019988 as a lateral mechanistic correction. The machine-seeded rows are untouched. The Asn route is the physiological inference; Gln-forming substrate capacity is kept separate from native pathway flux.

### Final independent-QA correction

Retired the inherited authored NEW GO:0050566 after the broad catalytic-activity replacement was expanded to include the same supported Asn-forming contribution. The activity remains in the replacement and core. This is the fourth explicit authored-row exception across the panel: 107 final rows, four retained NEW; all 103 machine rows remain unchanged. GatB GO:0050566 is a machine IEA and GatC has no redundant broad MF replacement, so neither was removed.


## 2026-10-29 — PR #5616 evidence follow-up

Cytoplasm remains ACCEPT with native B. subtilis S100 activity and immunoblot evidence from PMID:9342321. The native Bacillus lane is explicitly distinguished from recombinant E. coli lanes. For Pseudomonas, the compartment is a conserved-machinery inference supported by target HAMAP GatA membership, not a native localization experiment. Generic catalytic activity now refines to GatA glutaminase chemistry; existing whole-complex contribution claims are retained. Original annotation payloads and row counts are unchanged.
