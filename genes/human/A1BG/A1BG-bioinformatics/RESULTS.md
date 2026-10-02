# A1BG hydropathy artifact recheck

The provider's canonical-sequence calculation reproduces from the untouched local P04217 record: the maximum 19-residue mean Kyte–Doolittle score among windows starting at residue 22 or later is 0.9842105263. Only the window at residues 1–19 exceeds the chosen 1.6 threshold (1.6947368421), within the annotated cleaved signal peptide. Full profiles, input hashes and computed coordinates are saved in the JSON outputs.

This corroborates absence of an ordinary hydrophobic transmembrane helix in canonical mature A1BG. It does not test surface binding, peripheral association, receptor-complex function, membrane insertion under all conditions, or all alternative mechanisms. The unrelated AKIRIN1 sequence also runs successfully and produces its own profile. Lack of threshold crossings is not by itself a biological exclusion test.

The provider script fetched only the canonical P04217 sequence. The curated alternative isoform deletes canonical residues 1–122, so it introduces no new amino-acid segment; no new hydrophobic segment can arise from that terminal deletion. Nevertheless, no named-isoform expression, localization, lipidation or receptor function was experimentally assayed by this computation. The provider's broader claim that the result closes every membrane-pool route is invalid, independently contradicted by the mouse cardiomyocyte surface experiment in PMID:40270023.

- [x] Input paths are arguments; no protein sequence or result is hardcoded.
- [x] Executed on A1BG and the unrelated AKIRIN1 record.
- [x] Both calculations completed with valid sequence-window parameters.
- [x] Direct computed profiles and exact input hashes are saved beside the script.
- [x] Method, threshold and biological limits are documented; the result is a hydropathy calculation, not a membrane-localization or signaling assay.

Reproduction: `just` in this directory, Python 3.12.9, standard library only. Source method: the stored OpenScientist provenance JSON (19-residue Kyte–Doolittle window). No cached UniProt source was edited.
