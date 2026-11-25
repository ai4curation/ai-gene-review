# mas2 review notes

- GO-CAM `69729a3800007453` has one Mas2 activity for `PomBase:SPBC18E5.12c`, enabled by peptidase activator activity (`GO:0016504`), part of mitochondrial protein processing (`GO:0034982`), and occurring in the mitochondrial matrix (`GO:0005759`).
- `just deep-research-falcon SCHPO mas2 --fallback perplexity-lite` failed because `falcon` and `perplexity` were unavailable to the uvx `deep-research-client` environment; the only listed provider was `claude_code`. I wrote `mas2-deep-research-manual.md` instead.
- `just mod-description-deep-research SCHPO mas2` skipped because no MOD provider is configured for `SCHPO`.
- `just paint-losses SCHPO mas2` reported no IRD or IKR on the O94745 lineage, so the `GO:0017087 mitochondrial processing peptidase complex` and obsolete `GO:0070585 protein localization to mitochondrion` IBA rows were reviewed from their current PAINT placement.
- The gene review agrees with the GO-CAM's Mas2 molecular function, process, matrix location, and direct-positive-regulation edge to mas1. The final GO-CAM notes PR does not need a Mas2 conflict note.
