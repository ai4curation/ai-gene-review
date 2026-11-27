# DYNC2I2 saved-data evidence audit

Run `python3 replay.py --check` with Python 3.10 or later. Only the standard library is required. The script reads `source-inputs.zip`, authenticates every raw input against `source-manifest.json`, and independently derives the comparison with `results.json`. To inspect newly computed output, run `python3 replay.py --output /tmp/DYNC2I2-results.json`.

The code selects literal IntAct participant/reference pairs, preserves PSI-MI methods, expansion and feature sides, and recomputes ROGIDs from official reference sequences plus organism identifiers. These checks authenticate the curator's reference sequences; they do not reconstruct the physical plasmid insert or prove an endogenous interaction. Missing selected IntAct records are reported as empty lists, not negative biological evidence. Source-specific primary experiments are assessed in the source guide.

The same replay reconstructs the target's PAINT tree path and MSA sequence, reads literal IBD rows on that path, evaluates ARBA conditions against the target's official cross-references and taxonomic lineage, and traverses actual Reactome input/output/component edges to the human target. It extracts HPA's individual location reliability labels rather than assigning the aggregate score to every location. It reads the original AP-MS graph edge, not a cell-embedding prediction.

The MEOX2 comparison preserves the literal unreviewed Q6FHY5 partner rather than replacing its identity with P50222. TRIM54 class evidence is a current human IBA record, explicitly distinguished from a direct human enzyme assay. These partner classes refine the kind of binding without assigning DYNC2I2 enzyme or transcription-factor activity.

All results come from archived raw data. Primary article bodies and the nuclear supplement image are not redistributed here; their public locators and the limits of their interpretation are documented in [the source guide](../../DYNC2I2-source-guide.md). These computations are provenance checks, not new independent biological experiments. Network access is unnecessary for replay; fresh downloads may differ from the archived versions.
