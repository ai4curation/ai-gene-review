# ATG2B notes

## Deep research provenance

Falcon deep research was attempted with the requested `perplexity-lite` fallback using:

```bash
just deep-research-falcon human ATG2B --fallback perplexity-lite
```

The Falcon child process timed out after 600 seconds. The fallback attempt then failed with a Perplexity API quota error, so no `ATG2B-deep-research-falcon.md` or fallback provider artifact was written. Per repository guidance, this manual notes file records the evidence review instead of creating a fake provider-named deep-research file.

## Evidence synthesis

ATG2B is one of the two mammalian ATG2 orthologs. The core mammalian phenotype is a redundant ATG2A/ATG2B requirement for autophagy: combined ATG2A/B depletion blocks autophagic flux, accumulates unclosed autophagic structures, and leaves other ATG proteins on abnormal LC3-positive membranes [PMID:22219374 "both Atg2A and Atg2B are required for autophagy and that they have redundant and overlapping functions"; PMID:22219374 "these results suggest that Atg2A/B play an essential role, probably at a late step of autophagosome formation"].

The best-supported molecular function is membrane tethering plus lipid transfer. Osawa et al. report that human ATG2B has membrane tethering and lipid-transfer activity, promoted by negatively charged membranes and WIPI4 [PMID:31721365 "ATG2B possesses the membrane tethering (MT) and LT activity"; PMID:31721365 "negatively charged membranes and an Atg18 ortholog WIPI4"]. This supports `GO:0120013 lipid transfer activity` and `GO:0120009 intermembrane lipid transfer`, with `GO:0000045 autophagosome assembly` as the best replacement for broad `GO:0006914 autophagy`.

The PN projection report lists ATG2B under `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ATG2-WIPI complex component`, projecting `GO:0062079 ATG2-ATG18 complex` as a candidate addition. This projection is biologically plausible and conservative when treated as a component annotation, not as evidence for a new proteostasis/chaperone/degradation role. Direct evidence supports ATG2B-WDR45/WIPI4 complex membership [PMID:28820312 "We also purified the ATG2B-WDR45 complex and then performed 3-dimensional reconstruction of the complex"; PMID:28820312 "conserved aromatic H/YF motif in the C terminus of ATG2A and ATG2B that is crucial for complex formation"]. A human autophagy interaction-network paper also detects ATG2A/ATG2B/WDR45 association [PMID:20562859 "association between ATG2A, ATG2B, and WDR45 was unaltered by mTOR inhibition"].

The PI3P-binding IBA annotation should be interpreted cautiously. WIPI/ATG18 proteins are the PI3P-binding effectors in the complex, while ATG2B binds liposomes without requiring PI3P or WDR45 in the cited abstract [PMID:28820312 "PtdIns3P-binding effectors which can form complexes with proteins in the Atg2 family"; PMID:28820312 "ATG2B and found that it could bind to liposomes independently of PtdIns3P or WDR45"]. I marked `GO:0032266 phosphatidylinositol-3-phosphate binding` as over-annotated for ATG2B.

Lipid droplet localization is experimentally supported but not the main PN-relevant role. Velikkakath et al. report mammalian ATG2 proteins on lipid droplets and altered lipid droplet size/distribution after ATG2A/B depletion [PMID:22219374 "One novel aspect of the present study is the finding that mammalian Atg2 proteins are present on lipid droplets"; PMID:22219374 "These data suggest that mammalian Atg2A and Atg2B function both in autophagosome formation and regulation of lipid droplet volume and distribution."]. The same paper notes the directness/mechanism remains unresolved [PMID:22219374 "Further experiments will be required to test whether Atg2 proteins directly or indirectly associate with lipid droplets"], so I kept lipid-droplet annotations as non-core.

Selective autophagy terms such as mitophagy, pexophagy, glycophagy, reticulophagy, and piecemeal microautophagy of the nucleus are plausible for a conserved core autophagy membrane-expansion factor, but they should not be read as cargo-specific receptor or recognition functions. I kept those as non-core rather than adding proteostasis-projection-driven cargo-specific conclusions.
