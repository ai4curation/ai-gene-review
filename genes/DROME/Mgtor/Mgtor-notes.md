# Mgtor review notes

## Session 1 (create review)

- Fetched A1Z8P9 (TPR_DROME, Swiss-Prot reviewed; FlyBase FBgn0013756). Accession matched the request.
- No deep-research API available; wrote `Mgtor-deep-research-manual.md` from cached papers.
- Full text read for PMID:19273613 (key paper), 31913420, 34133927, 20174442, 15356261, 22855526,
  26714316, 18562695. Abstract only: 16543150, 9152019, 12027452.

### Key decisions

- Core: NPC basket scaffold (structural constituent of nuclear pore); SAC spatial regulator (Mad1 docking
  at NPC, Mad2/Mps1 kinetochore recruitment, spindle matrix); attenuator of MSL-dependent X transcription.
- Indirect mitotic phenotypes marked over-annotated: spindle elongation and metaphase plate congression
  defects are rescued by delaying anaphase with MG132 [PMID:19273613 "We found no difference in half-spindle elongation velocity between Mtor RNAi (0.7 ± 0.1 µm/min) and control cells (0.7 ± 0.2 µm/min) treated with MG132"].
- Reduced mitotic index after RNAi (PMID:15356261) was annotated as positive regulation of mitotic
  nuclear division / cell division; later work explains it as faster, checkpoint-weakened mitosis.
- NOT regulation of chromosome segregation (FlyBase, PMID:19273613) conflicts logically with SAC
  signaling (a GO descendant) and with PMID:31913420; REMOVE proposed and flagged for experts.
  NOT regulation of mitotic spindle elongation kept.
- UniProt lists a kinetochore location citing PMID:19273613, but the paper says Mtor does not accumulate
  at kinetochores; FlyBase has NOT kinetochore. Possible UniProt subcellular-location error.
- Chromatin organization / remodeling from PMID:20174442 rest on "data not shown" Mtor depletion and a
  suggestion of open chromatin; marked over-annotated. Positive regulation of RNAPII transcription
  UNDECIDED given later evidence that Mtor attenuates transcription.
- Nuclear inclusion body and metaphase plate CC terms do not fit the observations.
- No NEW annotations proposed. Bare protein binding rows removed per policy.
