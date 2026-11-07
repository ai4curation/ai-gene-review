# FdeB candidate-site comparison, 2026-11-07

The three proteins support a broad hydrolase inference, but the report's particular catalytic-triad numbering must not be treated as experimentally established. The frozen PP_3195 sequence contains **S268, K358, D359, H394 and H405**. Thus the prior provider report's Asp358 is a one-residue numbering error. Its proposed H405 corresponds to H370 in Hsero_1004 but **Q374 in bll6428**. This difference alone does not establish loss of catalysis because the target histidine assignment was never experimentally established.

As an independent comparison, the reviewed UniProt Q93NG6 record annotates experimentally supported S217/D300/H329 active sites with PMID:17275835. Global alignment maps these to PP_3195 S268/D359/H394, Hsero_1004 S233/D324/H359, and bll6428 S237/D328/H363. All are present. The reference-to-target alignment is distant (about 30–34% identity among aligned positions), so these are **candidate correspondences**, not proof of active-site geometry. The close FdeB-to-FdeB alignment makes the target residue conservation/difference clear, but cannot establish which histidine is catalytic.

The evidence supporting a broad function is the combination of FrsA-like family membership, alpha/beta-hydrolase architecture and conserved candidate catalytic chemistry, with experimentally characterized hydrolytic members. Neither alternative histidine mapping selects ester versus carbon-carbon hydrolysis. No measured target activity, native flavonoid-catabolic participation or substrate-resolved assay is asserted. bll6428's existing PAINT-supported broad hydrolase judgment is not rejected based on an unverified provider-site assignment.

The current official Q89GB7 record has the same Q374-containing sequence as the frozen bll6428 record. The separately checked official P04335 record (the FrsA PAINT seed) retains experimentally supported ester hydrolysis, including pNP-butyrate activity attributed to PMID:15808744; its curated statement is not an assay of the FdeB targets. Official Q93NG6 classifies the experimentally characterized C-C hydrolase in IPR050261; its primary characterization is PMID:16321959 and its structural/mutational study is PMID:17275835. Both newly fetched caches are abstract-only. They establish the characterized comparator's hydrolytic activity/fold; full-text target-residue experiments have not been inspected. The old provider report and raw sequence records are unchanged.

Reproduce from the repository root:

```sh
just --justfile genes/PSEPK/PP_3195/PP_3195-bioinformatics/fdeb-round2/justfile --working-directory . analyze
```

The generic script takes query, target paths, positions and output paths as arguments. It uses the repository's pinned `uv` environment and records the installed Biopython version, BLOSUM62/global alignment parameters, input hashes, aligned-pair counts and every mapped residue. Results are in `analysis/module_audits/bacterial_flavonoid_degradation/round2-fdeb-sequence-map.yaml` and `round2-primary-site-map.yaml`; official comparison records are in the round1/round2 evidence directories. The source records use 1-based numbering.

- [x] Script inputs and outputs are explicit arguments, without hardcoded protein paths or expected outcomes.
- [x] Tested with two independent query sequences: PP_3195 and Q93NG6.
- [x] All six alignments completed and mapped residue identities were inspected.
- [x] Direct results, parameters, dependency version and input hashes are retained.
- [x] Sequence observations are separated from unmeasured geometry, catalytic-site identity and substrate specificity.
