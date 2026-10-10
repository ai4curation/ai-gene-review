# QNS1 (YHR074W) notes

UniProt P38795, glutamine-dependent NAD+ synthetase (EC 6.3.5.1) [UniProt:P38795].

- Essential; final step of NAD+ synthesis [PMID:12898714 "NAD(+) synthetase catalyses the final step in both pathways. Here we show that this enzyme is encoded by the QNS1 gene in Saccharomyces cerevisiae."; "These results demonstrate that NAD(+) synthetase activity is essential for cell viability."].
- N-terminal nitrilase-related glutaminase domain + C-terminal synthetase; both needed in cis [PMID:12771147 "Here we show yeast glutamine-dependent NAD+ synthetase Qns1 requires both the nitrilase-related active-site residues and the NAD+ synthetase active-site residues for function in vivo."; "glutamine-dependence is an obligate phenomenon involving intramolecular transfer of ammonia"].
- Glutaminase activity (GO:0004359) is a coupled partial reaction -> KEEP_AS_NON_CORE.
- Localization: GFP diffuse nucleus + cytosol [PMID:12898714 "A GFP-tagged version of Qns1p displayed a diffuse localization in both the nucleus and the cytosol."].
- YeastCyc RCA "L-tryptophan catabolic process" (TRYPTOPHAN-DEGRADATION-1) is superpathway inflation -> MARK_AS_OVER_ANNOTATED.
- IBA to obsolete GO:0034354 -> MODIFY to GO:0009435.
- Qns1 is not required for the Nrk1 NR -> NMN -> NAD+ route (bypasses NaAD) (general pathway logic; cf. PMID:19001417 "Qns1-independent NR utilization depends on Nrk1").
