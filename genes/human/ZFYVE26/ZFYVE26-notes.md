# ZFYVE26 notes

## Review context

ZFYVE26 encodes spastizin/SPG15, a FYVE-domain protein in the AP5-SPG11-SPG15 endolysosomal machinery. In the Proteostasis Network browser it appears under autophagic lysosome reformation and class III PI3K complex 2/autophagosome maturation context. The PN row that lacks PMID mappings was treated as search/context only, not as direct evidence.

Falcon deep research was started with `just deep-research-falcon human ZFYVE26` and timed out after 600 seconds with `All providers failed`. This notes file and the cached publications are the manual evidence record.

## Evidence synthesis

The strongest proteostasis evidence places spastizin with spatacsin/SPG11 in autophagic lysosome reformation (ALR). The JCI abstract states that SPG15/spastizin and SPG11/spatacsin are "pivotal for autophagic lysosome reformation (ALR)", that lysosomal targeting of spastizin requires a FYVE domain binding PI3P, that loss of either protein depletes free lysosomes and causes autolysosome accumulation, and that they are essential for initiation of lysosomal tubulation [PMID:25365221 "pivotal for autophagic lysosome reformation (ALR)"; PMID:25365221 "Lysosomal targeting of spastizin required an intact FYVE domain, which binds phosphatidylinositol 3-phosphate"; PMID:25365221 "Loss of spastizin or spatacsin resulted in depletion of free lysosomes"; PMID:25365221 "essential components for the initiation of lysosomal tubulation"]. This supports `GO:0007040 lysosome organization` and the existing lysosome/late-endosome locations as core, while `GO:1905037 autophagosome organization` is less precise for this paper than lysosome organization/ALR.

Structural evidence now directly supports the AP5-SPG11-SPG15 membrane remodeling model. The 2025 structural paper reports that SPG11-SPG15 cooperates with AP5 in late-endosome membrane sorting, and that the AP5-SPG11-SPG15 complex binds PI3P, senses curvature, drives membrane remodeling in vitro, and is essential for autolysosome tubulation [PMID:40175557 "AP5-SPG11-SPG15 complex can bind PI3P molecules, sense membrane curvature and drive membrane remodeling in vitro"; PMID:40175557 "essential for the initiation of autolysosome tubulation"]. This supports `GO:0097212 lysosomal membrane organization`, `GO:0097753 membrane bending`, `GO:0007040 lysosome organization`, and PI3P binding as an informative molecular function.

The AP-5 interaction paper supports replacing generic protein-binding rows with endolysosomal membrane-organization terms: AP-5 subunits coimmunoprecipitate with SPG11/SPG15, all components colocalize on late endosomal/lysosomal compartments, and the authors propose a coat-like complex in which SPG15 docks the coat onto PI3P-containing membranes via its FYVE domain [PMID:23825025 "the four AP-5 subunits can be coimmunoprecipitated with SPG11 and SPG15"; PMID:23825025 "AP-5, SPG11, and SPG15 colocalize on a late endosomal/lysosomal compartment"; PMID:23825025 "SPG15 facilitating the docking of the coat onto membranes by interacting with PI3P via its FYVE domain"].

Autophagosome maturation has independent support from the Brain abstract. It states that spastizin interacts with Beclin 1, associates with the Beclin 1-UVRAG-Rubicon complex, and is required for autophagosome maturation; spastizin-deficient or mutant cells accumulate immature autophagosomes [PMID:24030950 "spastizin interacts with the autophagy related Beclin 1-UVRAG-Rubicon multiprotein complex and is required for autophagosome maturation"; PMID:24030950 "impairment of autophagosome maturation and an accumulation of immature autophagosomes"]. This supports adding `GO:0097352 autophagosome maturation` as a new annotation, separate from the ALR/lysosome-organization evidence.

ZFYVE26 also has a well-supported cytokinesis role that should be retained as non-core for this proteostasis-focused review. Sagona et al. report that PI3P localizes to the midbody and recruits FYVE-CENT/ZFYVE26, that FYVE-CENT/TTC19 translocation from centrosome to midbody requires KIF13A, and that depletion of FYVE-CENT phenocopies PI3K-III/KIF13A/TTC19 depletion with cytokinesis arrest and multinucleated cells [PMID:20208530 "PtdIns(3)P localizes to the midbody during cytokinesis and recruits a centrosomal protein, FYVE-CENT (ZFYVE26)"; PMID:20208530 "Translocation of FYVE-CENT and TTC19 from the centrosome to the midbody requires another FYVE-CENT-interacting protein, the microtubule motor KIF13A"; PMID:20208530 "cytokinesis arrest and an increased number of binucleate and multinucleate cells"]. Thus centrosome, midbody, regulation of cytokinesis, and mitotic cytokinesis are real but non-core.

The HR-DSBR evidence is experimentally based but not a proteostasis core function. The genome-scale DNA repair paper identifies KIAA0415/SPG48 as the main focus, but also reports that KIAA0415 interacts with SPG11 and SPG15 and that SPG15 silencing reduces the DR-GFP homologous recombination readout [PMID:20613862 "KIAA0415 interacts with SPG11, SPG15"; PMID:20613862 "significant reduction of GFP positive cells were observed upon silencing of C20orf29 and SPG15"]. Keep homologous recombination DSB repair as non-core with the caveat that the better-supported proteostasis function is endolysosomal membrane remodeling.

The `GO:0019901 protein kinase binding` annotation from PMID:25365221 could not be verified from the cached abstract. Because the relevant full text is not locally accessible, this row should remain undecided rather than accepted.

The HDA lysosomal membrane row from PMID:17897319 is broad proteomics evidence. It can be retained as a broad location, but the stronger functional interpretation comes from the ALR/AP5-SPG11-SPG15 literature [PMID:17897319 "identified 58 proteins, known to reside at least partially in the lysosomal membrane"].

## Review decisions

- Core: PI3P binding; AP5-SPG11-SPG15-dependent lysosomal/late endosomal membrane organization; membrane bending/remodeling; lysosome organization in ALR; autophagosome maturation.
- Non-core: cytokinesis, midbody/centrosome localization, and possible HR-DSBR role.
- Modify/replace: generic `protein binding` rows should be replaced by lysosome organization, lysosomal membrane organization, membrane bending, or regulation of cytokinesis depending on the source.
- Undecided: `protein kinase binding` from PMID:25365221, due missing accessible evidence.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: cytokinesis and HR-DSBR roles were treated as non-core in this proteostasis-focused review, and generic protein-binding annotations should be replaced by specific membrane-organization, membrane-remodeling, or cytokinesis terms supported by the source publications.
