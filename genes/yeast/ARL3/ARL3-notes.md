# Curation Notes for Saccharomyces cerevisiae ARL3 (UniProtKB:Q02804, SGD:S000005972)

## 1. Gene Identity & Critical Homonym Distinction
- **Symbol / Accession**: `ARL3` (`UniProtKB:Q02804`, `SGD:S000005972`, `YPL051W`, alias `ARP1`), 198 aa, founding fungal seed of `PANTHER:PTHR45909:SF1` (`PANTHER:PTN000196303`).
- **Homonym Alert (`yeast ARL3` = `mammalian ARFRP1`, NOT `mammalian ARL3`)**:
  - *S. cerevisiae* `ARL3` (`yARL3`) is the 1:1 ortholog of mammalian `ARFRP1` (`UniProtKB:Q13795`) [PMID:9920936, PMID:15077113]. Budding yeast lacks cilia and has no ortholog of mammalian ciliary `ARL3` (`UniProtKB:P36405`).
  - The SGD curated gene description (`file:yeast/ARL3/ARL3-deep-research-sgd.md`) explicitly and accurately states `"similar to ADP-ribosylation factor and orthologous to mammalian ARFRP1"`, completely avoiding the `ARL3` homonym trap!

## 2. Molecular Mechanism & Subcellular Localization
- **Intrinsic GTP Binding and GTPase Activity (`PMID:9920936`)**:
  - Conserves P-loop Walker A `24-GLDNAGKT-31` (`Lys30`, `Thr31`), Switch II catalytic `74-DVGGQ-78` (`Gln78`, homologous to human `Gln79`), and G4 `133-NKQD-136`.
  - Purified recombinant Arl3p binds and hydrolyzes GTP in vitro and, unlike canonical Arfs, does not stimulate cholera toxin ADP-ribosyltransferase activity (`PMID:9920936`).
- **NatC Co-translational N-terminal Acetylation and Sys1p Golgi Receptor Binding (`PMID:15077113`, `PMID:15077114`, `PMID:33139728`)**:
  - Lacks `Gly2` myristoylation and instead starts with `1-MFHLVKGLYNNWNK-14` (`Met1-Phe2`).
  - The heterotrimeric NatC complex (`Mak3p`/`Naa30` + `Mak10p`/`Naa35` + `Mak31p`/`Naa38`) acetylates `Met1` (`kcat` measured and crystal structure solved bound to `1-MFHLV-5` peptide in `PMID:33139728`).
  - N-terminally acetylated Arl3p binds directly to the multipass Golgi integral membrane protein `Sys1p` on the cytoplasmic face of the Golgi apparatus (`PMID:15077113`, `PMID:15077114`); loss of either NatC (`mak3Delta`) or `Sys1p` (`sys1Delta`) releases Arl3p to the cytosol.
  - Per `projects/ORGANELLES.md` Rule 7, because Arl3p is a soluble cytosolically synthesized protein (no signal peptide or TM segment) shown at the Golgi and stably tethered there by integral partner `Sys1p` (whose deletion releases Arl3p to the cytosol), we add `GO:0098548` (`cytoplasmic side of Golgi membrane`) as a `NEW` `IC` annotation (`PMID:15077113`, with `GO:0005794`), while accepting `GO:0005794` (`Golgi apparatus`) and keeping `GO:0005829` (`cytosol`, `HDA` `PMID:26928762` N-terminally SWAT-GFP-tagged pool where N-terminal tagging blocks NatC/Sys1p anchoring, plus `TAS` `Reactome:R-SCE-6814089` pre-acetylation soluble substrate pool) as `KEEP_AS_NON_CORE`.
- **Downstream Arl1p-Imh1p/GARP Golgi Cascade & Transport (`PMID:12620188`, `PMID:12620189`, `PMID:16926193`, `PMID:26966233`)**:
  - Golgi-tethered Arl3p is required to recruit `Arl1p` (activated by GEF `Syt1p` and regulated by GAP `Gcs1p`), which in turn recruits the sole yeast GRIP-domain golgin `Imh1p` and interacts with GARP/Vps53p tethering pathways (`PMID:12620188`, `PMID:12620189`), driving vacuolar hydrolase (CPY, ALP) maturation (`PMID:9920936`) and late-Golgi-to-plasma-membrane transport of GPI-anchored `Gas1p` (`PMID:16926193`).
  - Under ER stress, Ire1p-Hac1p UPR signaling phosphorylates `Syt1p` to modulate `Arl1p`/`Imh1p` late-Golgi recruitment (`PMID:26966233`).

## 3. SGD MOD Description Audit (`ARL3-deep-research-sgd.md`)
- Text: `"ARF-like small GTPase of the RAS superfamily; required for recruitment of Arl1p, a GTPase that regulates membrane traffic, to the Golgi apparatus; NatC-catalyzed N-terminal acetylation regulates Golgi membrane association mediated by interaction with membrane receptor, Sys1p; similar to ADP-ribosylation factor and orthologous to mammalian ARFRP1"`
- Every clause is concise, accurate (`correctness: VERIFIED`), traceable to `PMID:9920936`, `PMID:12620188`, `PMID:12620189`, `PMID:15077113`, and `PMID:15077114`, and explicitly disambiguates orthology to mammalian `ARFRP1`.

## 4. Key Annotation Decisions
- **`GO:0042175` (`nuclear outer membrane-endoplasmic reticulum membrane network`, `IDA` `PMID:9920936`)**: `MARK_AS_OVER_ANNOTATED` — `PMID:9920936` abstract explicitly states `"Indirect immunofluorescence analysis revealed that yARL3 when overexpressed was associated in part with the endoplasmic reticulum-nuclear envelope."` Physiological Arl3p localizes to the Golgi via NatC and Sys1p (`PMID:15077113`, `PMID:15077114`), making ER-nuclear-envelope staining an overexpression artifact per `projects/ORGANELLES.md`.
- **`GO:0034976` (`response to endoplasmic reticulum stress`, `IMP` `PMID:26966233`)**: `KEEP_AS_NON_CORE` — `PMID:26966233` (abstract-only cached) demonstrates UPR (`Ire1p`-`Hac1p`) modulation of `Syt1p`-`Arl1p`-`Imh1p` late-Golgi activation; we defer to the SGD curator who read the full text while marking ER-stress modulation as non-core relative to constitutive Golgi recruitment.
