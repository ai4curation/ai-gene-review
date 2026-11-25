# oct1 review notes

- GO-CAM `69729a3800007453` has one Oct1 activity for `PomBase:SPAC1F3.10c`, enabled by mitochondrial intermediate peptidase activity (`GO:0004222`), part of mitochondrial protein processing (`GO:0034982`), and occurring in the mitochondrial matrix (`GO:0005759`).
- `just deep-research-falcon SCHPO oct1 --fallback perplexity-lite` failed because `falcon` and `perplexity` were unavailable to the uvx `deep-research-client` environment; the only listed provider was `claude_code`. I did not launch a sub-worker and wrote `oct1-deep-research-manual.md` instead.
- `just mod-description-deep-research SCHPO oct1` skipped because no MOD provider is configured for `SCHPO`.
- `just paint-losses SCHPO oct1` reported no IRD or IKR on the Oct1 lineage, so the PANTHER `PTN000211184` and `PTN000211186` IBA rows are current.
- Cached `PMID:8035833` for the original S. cerevisiae `MIP1/OCT1` cloning and complementation evidence and `PMID:10332043` for the iron-homeostasis ISO source. `PMID:21525245`, `PMID:19837041`, and `PMID:22984266` were already cached and support yeast Oct1 substrate processing.
- The GO-CAM's core molecular function, process and location agree with the Oct1 review. The final GO-CAM notes PR should mention that the substrate input edges for the Oct1 activity have no per-edge evidence and that the two causal edges from Oct1 to Cym1 duplicate the same upstream processing relation.
