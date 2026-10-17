# HOG1 (YLR113W, UniProt P32485) curation notes

## 2026-09-24 initial review

### Identity and activation
- Hog1 is the terminal MAPK of the high-osmolarity glycerol (HOG) pathway; Pbs2 is its MAPKK.
  [PMID:7681220 "Two of these genes, HOG1 and PBS2, encode members of the mitogen-activated protein kinase (MAP kinase) and MAP kinase kinase gene families, respectively."]
  [PMID:7681220 "A rapid, PBS2-dependent tyrosine phosphorylation of HOG1 protein occurred in response to increases in extracellular osmolarity."]
- Activation-loop TGY: Pbs2 phosphorylates Thr174/Tyr176.
  [file:yeast/HOG1/HOG1-deep-research-falcon.md "Pbs2 is the immediate upstream MAPK kinase and phosphorylates Hog1 at Thr174 and Tyr176."]
- Upstream: Sln1-Ypd1-Ssk1 phosphorelay -> Ssk2/Ssk22 and the Sho1 branch (Ste11) converge on Pbs2 (deep research, section 2). This is the grounding for modules/scer_hog1_cascade.yaml, where Hog1 is the MAPK tier (GO:0004707).

### Kinase activity / direct substrates (all with in vitro kinase assays)
- Rck2 (Ser519) [PMID:10805732 "Taken together, these results indicate that Rck2 is a direct substrate for the MAPK Hog1."]
- Sko1 [PMID:11230135 "Hog1 phosphorylates Sko1 in vitro at multiple sites within the N-terminal region."]
- Smp1 [PMID:12482976 "Hog1 phosphorylated Smp1 in vitro at the C-terminal region."]
- Sic1 [PMID:15448699 "Hog1 interacts physically with Sic1 in vivo and in vitro, and phosphorylates a single residue at the carboxyl terminus of Sic1"]
- Hsl1 [PMID:16688223 "Activated Hog1 interacts and directly phosphorylates a residue within the Hsl7-docking site of the Hsl1 checkpoint kinase"]
- Ubp3 S695 [PMID:21743437 "Hog1 interacts with and phosphorylates Ubp3 at serine 695"]
- Mrc1 [PMID:23178807 "Hog1 interacts with and phosphorylates Mrc1, a component of the replication complex."]
- Net1 [PMID:32265285 "Hog1 phosphorylates Net1 on T62 and S385 in vitro and in vivo."]
- Dot1 [PMID:38270553 "In vitro kinase assays showed that Hog1p phosphorylates Dot1p at multiple sites, including at several proline-adjacent sites that are consistent with known Hog1p substrate preferences."]
- Rgc2/Fps1 channel closure. [PMID:24298058 "Hog1 was recruited to the N-terminal cytoplasmic domain of Fps1, which it uses as a platform from which to multiply phosphorylate Rgc2."]

### Localization
- Cytoplasmic at rest, transient nuclear accumulation on activation. [PMID:10817757 "The MAP kinase Hog1 transiently accumulates in the nucleus upon activation."]
- Ptp2 (nuclear) and Ptp3 (cytoplasmic) tether/anchor Hog1. [PMID:10817757 "Thus, Ptp2 and Ptp3 regulate Hog1 localization by binding Hog1."]
- Recruited to chromatin at stress promoters via Hot1 and other TFs. [PMID:12743037 "In response to high osmolarity, Hot1 targets Hog1 to specific osmostress-responsive promoters."]

### Transcriptional output
- Hog1 anchored at promoters recruits Pol II. [PMID:12743037 "Thus, anchoring of active Hog1 to promoters by the Hot1 activator is essential for recruitment and activation of RNA Pol II."]
- lncRNA / CDC28 induction via chromatin association. [PMID:24508389 "Therefore, Hog1 associates to and stimulates the recruitment of RNA Pol II at the promoters of stress-induced lncRNAs."]
- Hot1 was found as a two-hybrid partner, but the biochemical interaction could not be confirmed in that paper. [PMID:10409737 "Various attempts to obtain biochemical evidence for Hog1p-Hot1p interaction by coprecipitation assays or by immunokinase assays failed (data not shown)."]

### Cell-cycle control (non-core, osmostress-coupled)
- G1 (Sic1), S (Mrc1: [PMID:23178807 "Mrc1 phosphorylation by Hog1 delays early and late origin firing by preventing Cdc45 loading"]), G2 (Hsl1), mitotic exit (Net1: [PMID:32265285 "Here we show that Hog1 delays mitotic exit when cells are stressed during metaphase."]).

### Other
- Calmodulin binding: single study, abstract only. [PMID:27421986 "we demonstrate that Hog1 is a novel CaM-binding protein"]
- Autophagy: hog1 deletion makes starvation-induced autophagy osmosensitive (addendum, abstract only). [PMID:16874103 "loss of Hog1, the yeast orthologue of p38(MAPK), leads to osmosensitivity of starvation-induced autophagy"]

### Curation decisions (summary)
- Protein binding rows: MODIFY to protein kinase binding (GO:0019901) for kinase partners (Rck2, Hsl1, Ste7); MODIFY to RNA polymerase II-specific DNA-binding transcription factor binding (GO:0061629) for Hot1; REMOVE for Sic1, Ubp3 and Mrc1 (enzyme-substrate contacts that are better captured by the kinase activity and the downstream process annotations; removing the rows does not mean the interactions are false).
- Core: MAP kinase activity in the osmosensory signaling pathway / stress-activated MAPK cascade / cellular hyperosmotic response (cytoplasm, nucleus); MAP kinase activity driving positive regulation of Pol II transcription at osmostress genes (nucleus, chromatin).
- GO:0000161 "osmosensory signaling MAPK cascade" is obsolete (checked with runoak), so it was not used.

## 2026-10-11 fungal PAINT re-review

- Re-fetched `yeast/HOG1`; the 60 GOA rows were still in sync with the existing review and validation passed before PAINT edits.
- `PTHR24055` PAINT currently uses the broad MAPK-family `PANTHER:PTN000622075` for generic Ser/Thr kinase activity, nucleus and cytoplasm, and the fungal HOG/Sty1 `PANTHER:PTN001172058` for osmosensory signaling pathway, cellular response to oxidative stress, and stress-activated MAPK cascade. These six IBAs remain biologically correct for budding yeast Hog1. The broad node is safe for kinase/nucleocytoplasmic calls because Hog1 is an intact MAPK with direct cytoplasmic and nuclear substrates, and the fungal HOG/Sty1 node matches the HOG cascade; the oxidative-stress process remains non-core because peroxide/organic-acid activation is contextual relative to the central hyperosmotic response. The peroxide support was rechecked from a UniProt-cited primary paper. [PMID:15177185 "Mutants in either pathway are sensitive to hydrogen peroxide and the double mutants exhibit a near perfectly additive phenotype."]
- A fresh PubMed sweep found and cached the 2013 Rgc2/Fps1 mechanism paper, resolving the initial-review caveat above. Hog1 is recruited to the Fps1 N-terminal cytoplasmic domain and phosphorylates Rgc2 to close the glycerol channel. [PMID:24298058 "Activation of Hog1 in response to hyperosmotic shock induces the rapid eviction of Rgc2 from Fps1 and consequent channel closure."]
- Newer full-text HOG literature extends the non-osmotic and SHO1-gating picture but does not overturn the core PAINT calls: acetic-acid stress granules scaffold Hog1 with its upstream kinase Pbs2 [PMID:40067148 "Rather, acetic acid treatment drives the formation of stress granules, which function as a scaffold to bring Hog1 together with Pbs2"], and the SHO1 branch has three osmotic gates, including control over Pbs2-to-Hog1 phosphorylation [PMID:42256267 "Together with a previously described step in Pbs2-mediated Hog1 phosphorylation, these findings show that osmotic stress regulates the pathway at three levels"]. A 2024 flocculation paper also links HOG signaling to FLO-gene expression and flocculation, but its abstract does not justify any new core GO term. [PMID:38648231 "Altogether, our results suggest a role for HOG MAPK signaling in the regulation of FLO genes and yeast flocculation."]
- Attempted `just deep-research yeast HOG1 --provider falcon --fallback perplexity-lite`, but no Falcon or Perplexity provider credentials were available in this run. The existing Falcon research file plus cached primary literature were sufficient for this targeted PAINT re-review.
