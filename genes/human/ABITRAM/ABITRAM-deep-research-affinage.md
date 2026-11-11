---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABITRAM
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q9NX38
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABITRAM (human)

## Current model (mechanistic narrative)

ABITRAM (Simiate) is an actin-binding protein that couples actin cytoskeleton dynamics to nuclear gene-expression activity in neurons, functioning as a molecular link between transcription regulation and dendritogenesis [PMID:24782708]. It directly binds both G-actin and F-actin, modulating actin polymerization and turnover in living cells, influencing filopodia dynamics, and specifically promoting branching of proximal dendrites in developing neurons [PMID:24782708]. ABITRAM partitions between the cytosol and the nucleus, where it is enriched in the core domain of nuclear speckles [PMID:24349419, PMID:41617053]. In the nucleus it preferentially associates with an 80 kDa isoform of FAK1; nuclear-confined ABITRAM selectively triggers primary dendrite formation and enhances transcription activity, an effect counterbalanced by co-expression of nuclear FAK1, while neurotrophin-induced dendritogenesis drives co-localization of FAK1 and ABITRAM in dendritic growth cones [PMID:35787638]. ABITRAM mRNA contains FMRP recognition motifs and the protein co-precipitates with FMRP, and nuclear speckles are specifically altered in FMR1-knockout mice, linking ABITRAM to Fragile X-related regulation of speckle organization [PMID:24349419].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005654 nucleoplasm, GO:0005634 nucleus, GO:0005829 cytosol
- **pathway (Reactome):** *(none)*
- **partners:** FMRP, FAK1, ACTIN
- **complexes:** nuclear speckle

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | Medium | Simiate (ABITRAM) mRNA contains FMRP recognition motifs and the protein associates with FMRP (Fragile X Mental Retardation Protein) upon co-precipitation. Simiate localizes to somata and nuclear speckles, and nuclear speckles are specifically altered in FMR1(-/-) mice. Antibody-based block of endogenous Simiate revealed that the protein is essential for cell survival. | PMID:24349419 | PloS one |
| 2014 | Medium | Simiate (ABITRAM) directly associates with both G-actin and F-actin, affects actin polymerization and actin turnover in living cells, influences filopodia dynamics, and specifically increases branching of proximal (but not distal) dendrites of developing neurons. Simiate functions as a molecular link between transcription regulation and dendritogenesis via the actin cytoskeleton. | PMID:24782708 | Frontiers in cellular neuroscience |
| 2015 | Low | Simiate (ABITRAM) is enriched in nuclear speckles of retinal neurons. In rod and cone photoreceptor cells, Simiate localizes to the nuclear periphery, whereas in neurons of the inner nuclear and ganglion cell layer it is concentrated in the nuclear interior in a clustered pattern. This peripheral localization in photoreceptors is a general characteristic of photoreceptor organization, not related to the animal's diurnal/nocturnal lifestyle. | PMID:26013685 | Cell and tissue research |
| 2022 | Medium | Simiate (ABITRAM) associates with Focal Adhesion Kinase FAK1 as shown by co-precipitation from heterologous expression systems and mouse brain extracts. The interaction occurs in both cytosolic and nuclear fractions; in the nucleus, Simiate preferentially binds an 80 kDa isoform of FAK1. Nuclear-confined Simiate selectively triggers primary dendrite formation and enhances transcription activity, and this effect is counterbalanced by co-expression of nuclear FAK1. Neurotrophin-induced dendritogenesis causes striking co-localization of FAK1 and Simiate in dendritic growth cones, suggesting cytosolic interaction stimulates growth-cone-mediated dendritogenesis in response to external signals. | PMID:35787638 | Scientific reports |
| 2026 | Low | Using STED super-resolution microscopy and 3D reconstructions in mouse brain slices, Simiate (ABITRAM) is highly enriched in the core domain of nuclear speckles, while FAK1 is predominantly in peripheral areas of speckles. Both proteins are organized in spherical clusters that may occasionally co-localize. As speckle number increases, FAK1 diminishes from the core domain while Simiate remains enriched there, suggesting dynamic rearrangement consistent with their distinct roles in speckle sub-domains. | PMID:41617053 | Experimental cell research |

## Citations

- PMID:24349419
- PMID:24782708
- PMID:26013685
- PMID:35787638
- PMID:41617053
