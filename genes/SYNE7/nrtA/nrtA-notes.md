# nrtA review notes

## 2026-10-27: PCC 7942 native-system review

Reviewed all 2 seeded annotation rows for P38043, NCBITaxon:1140 (PCC 7942). Original annotation fields and both raw files were snapshotted before editing and retained. No NEW rows were introduced.

NrtA is the membrane-anchored substrate-binding lipoprotein of the high-affinity NrtABCD nitrate/nitrite uptake system in Synechococcus elongatus PCC 7942. It binds nitrate and nitrite on the extracytoplasmic side of the cytoplasmic membrane and supplies substrate to the NrtB permease and NrtC/NrtD ATP-binding components, enabling uptake for nitrogen assimilation.

One normal Falcon deep-research attempt with perplexity-lite fallback failed; no synthetic provider file was created. Manual primary-source review supplies the evidence below. Normal acquisition logs are in `.cache/module-audit-logs/nitrate-syne7-review/`.

Family grounding: target UniProt membership is PTHR30024:SF7, official PANTHER label **NITRATE_NITRITE BINDING PROTEIN NRTA**, checked against `interpro/panther/panther.obo`. Broad family labels do not determine substrate specificity; a chloroplastic family name does not place a cyanobacterial protein in a chloroplast.

- [PMID:16594065 Genetically engineered mutant of the cyanobacterium Synechococcus PCC 7942 defective in nitrate transport.] Native PCC 7942 membrane-protein disruption and nitrate uptake phenotype. Canonical cache is abstract-only; the PMC landing page has scanned-page links, not an independently parsed full text.
  The 45-kDa NrtA protein is a major cytoplasmic-membrane protein in nitrate-grown PCC 7942 cells. Supporting text: "contain a 45-kDa protein as a major protein in the cytoplasmic membrane"
- [PMID:9006953 Substrate-binding lipoprotein of the cyanobacterium Synechococcus sp. strain PCC 7942 involved in the transport of nitrate and nitrite.] Primary PCC 7942 deletion and globomycin experiments plus binding assays on truncated NrtA expressed in E. coli. Abstract read; DOI retrieval returned a redirect rather than full text. The measured affinity is for the recombinant truncation, not an intact-cell transport Km.
  Recombinant truncated NrtA binds nitrate and nitrite; native-cell precursor accumulation supports lipoprotein processing. Supporting text: "A truncated NrtA protein lacking the N-terminal 81 amino acids, expressed in Escherichia coli cells as a histidine-tagged soluble protein, was shown to bind nitrate and nitrite with high affinity"
  NrtA is the nitrate/nitrite-binding lipoprotein of the transporter. Supporting text: "These findings indicated that the nrtA gene product is a nitrate- and nitrite-binding lipoprotein."
- [PMID:9341163 Involvement of the C-terminal domain of an ATP-binding subunit in the regulation of the ABC-type nitrate/nitrite transporter of the Cyanobacterium synechococcus sp. strain PCC 7942.] Primary PCC 7942 NrtC domain deletion, complementation and nitrate accumulation experiments. Full text read in the separately cached University of Seville PDF; methods specify the plasmid-cured PCC 7942 derivative R2-SPc. C-terminal regulation is not evidence for direct ammonium binding.
  NrtABCD mediates active uptake of both nitrate and nitrite. Supporting text: "an ATP-binding cassette transporter encoded by the genes nrtA, nrtB, nrtC, and nrtD mediates active transport of nitrate and nitrite"
  The C-terminal extension of NrtC participates in ammonium-promoted inhibition. Supporting text: "the C-terminal domain of NrtC is involved in the ammonium-promoted inhibition of the nitrate/nitrite transporter."

Annotation decisions:

- GO:0005886 plasma membrane: ACCEPT. PMID:16594065 detects the native 45-kDa protein in the cytoplasmic membrane, and PMID:9006953 independently supports lipoprotein anchoring through globomycin-dependent precursor accumulation. Plasma membrane is the correct bacterial compartment; the protein is a substrate-binding component, not the transmembrane pore.
- GO:0005886 plasma membrane: ACCEPT. PMID:16594065 detects the native 45-kDa protein in the cytoplasmic membrane, and PMID:9006953 independently supports lipoprotein anchoring through globomycin-dependent precursor accumulation. Plasma membrane is the correct bacterial compartment; the protein is a substrate-binding component, not the transmembrane pore.


## 2026-10-29 PR5740 follow-up: direct participation and nonredundant proposals

The earlier sentence “No NEW rows were introduced” records the initial review scope; it is not an evidential reason to omit a justified proposal. This follow-up applies the participation, comparator, ontology-parentage and GO-CAM checks separately. Original machine annotation payloads and all raw records remain unchanged.

Live UniProt identity and QuickGO queries were saved without alteration in `.cache/module-audit-logs/nitrate-syne7-followup/` on 2026-10-30 UTC. The comparator annotation state is used only to test a proposed convention, never as `supported_by` evidence. All queried pages were complete (one page per protein). The primary sources already cached for the native target supply biological evidence; no new publication or raw-gene fetch was needed. The local `gocams/index.tsv` and all cached `*-src.yaml` models contain no P38043, P39458 or P39661 match. This absence does not itself justify an annotation.
The participation test passes because NrtA binds the transported nitrate/nitrite and contributes the substrate-recognition component of the ABC uptake machinery. The native knockout phenotype is supplemented by direct binding biochemistry; NrtA is neither the transported substrate nor simply an upstream regulator. PMID:9006953 states that the deletional mutant protein is “essential for the functioning of the nitrate/nitrite transporter” and reports that recombinant truncated NrtA binds both ions. PMID:9341163 establishes active transport by native NrtABCD. The new GO:0015414 row is explicitly `contributes_to`: it does not assign independent ATP hydrolysis or pore formation to NrtA.

The same-role comparator check is deliberately mixed. Cyanobacterial NrtA P73452 (PCC 6803) has only one unrelated process row plus a location row, and Q44292 (PCC 7120) has only location rows. Broadening to substrate-binding components performing the same ABC-import role finds E. coli MalE P0AEX9 annotated to maltose transport GO:0015768 and PstS P0AG82 to phosphate transport GO:0006817/phosphate transmembrane transport GO:0035435, including experimental evidence. Thus sparse NrtA homolog coverage is not evidence of a rule excluding substrate-binding components from transport processes. Their process annotations are not evidence about this target.

Two NEW rows are proposed: contributes_to GO:0015414 and GO:0015707 nitrite transport. QuickGO verifies both current labels and definitions. GO:0015707 lies under inorganic-anion transport and is not an ancestor or descendant of GO:0015414. The nitrate-specific MF already reaches GO:0015706 nitrate transmembrane transport through the `is_a`/`part_of` graph, via GO:0015112; therefore a separate NEW GO:0015706 would be redundant under the explicit project rule against ancestor/descendant proposals. Nitrate transport remains explicit in `core_functions`, and the new complex-activity proposal captures its curation recommendation. No generic binding or broader transport proposal is added. This is a specific evidential repair, not mechanical copying of the three core terms.

The completed review is now marked `status: COMPLETE`; this status records the finished evidence review, including explicit remaining biological uncertainties.
