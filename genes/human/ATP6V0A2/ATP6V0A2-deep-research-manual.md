# ATP6V0A2 manual deep research fallback

Falcon deep research was attempted on 2026-06-03 with `just deep-research-falcon human ATP6V0A2 --fallback perplexity-lite`. Falcon timed out after 600 seconds, and the configured Perplexity fallback returned an insufficient-quota 401. This manual fallback summarizes the local evidence used for the review.

## Core function

ATP6V0A2 encodes the a2 isoform of the V-type proton ATPase 116 kDa a-subunit. UniProt curates ATP6V0A2 as a "Subunit of the V0 complex of vacuolar(H+)-ATPase" and describes V-ATPase as the enzyme responsible for acidifying intracellular compartments [file:human/ATP6V0A2/ATP6V0A2-uniprot.txt].

Human V-ATPase structural and review literature supports the complex-level function. Wang et al. describe V-ATPases as ATP-driven proton pumps with a cytoplasmic V1 ATP-hydrolysis module and membrane Vo proton-transfer module, and state that organellar V-ATPases maintain pH homeostasis of endosomes and lysosomes [PMID:33065002]. Vasanthakumar and Rubinstein describe V-ATPases as the primary source of organellar acidification in eukaryotes [PMID:32001091].

## Endosomal acidification and trafficking

The strongest direct ATP6V0A2/a2 evidence is the early endosome paper by Hurtado-Lorenzo et al. They report that the a2 isoform is targeted to early endosomes, interacts with ARNO/PSCD2 in an intra-endosomal acidification-dependent manner, and that inhibiting endosomal acidification disrupts protein trafficking between early and late endosomal compartments [PMID:16415858]. This supports endosome membrane localization, V-ATPase-dependent proton transport/acidification, and mechanistic text about pH sensing. It does not make GO:0005515 protein binding an informative retained molecular-function annotation.

## Lysosomal and Golgi context

Lysosomal membrane evidence comes from lysosomal membrane proteomics, which identified polypeptides comprising or associated with vacuolar ATPase in purified placental lysosomal membranes [PMID:17897319]. Together with ATP6V0A2 V0-subunit identity, this supports the PN-projected lysosomal V0-domain annotation.

Golgi context is supported by UniProt's statement that ATP6V0A2 may maintain Golgi functions such as glycosylation maturation by controlling Golgi pH, consistent with the glycosylation defects seen in ATP6V0A2 disease [file:human/ATP6V0A2/ATP6V0A2-uniprot.txt].

## HIF and iron

Miles et al. identified ATP6V0A2 among V-ATPase subunits enriched in a HIF1A reporter screen. Their mechanism is not direct oxygen sensing; V-ATPase disruption leads to intracellular iron depletion, impaired PHD activity, and HIF activation [PMID:28296633]. This supports retaining intracellular iron ion homeostasis as a non-core downstream role and treating the broad "cellular response to increased oxygen levels" annotation as over-annotated.

## PN projection assessment

The Proteostasis PN projection proposes two ATP6V0A2 additions: GO:0007042 lysosomal lumen acidification and GO:0046610 lysosomal proton-transporting V-type ATPase, V0 domain [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv]. The PN mapping audit flags lysosomal acidification mappings for manual gene-level review before review changes [file:projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv].

Both projected terms are accepted conservatively in the review because they are supported by ATP6V0A2 V0-subunit identity, lysosomal membrane evidence, and the broader human V-ATPase endosome/lysosome acidification literature. Broader ALP/nutrient-sensing context was not converted into additional GO terms.

## Conservative removals and non-core calls

GO:0005515 protein binding is removed because the ARNO interaction is better represented as mechanistic context for endosomal pH sensing and trafficking. Regulation of macroautophagy is marked over-annotated because the supporting lipofuscin paper does not establish ATP6V0A2-specific macroautophagy regulation [PMID:22982048]. Immune response is marked over-annotated because the old cDNA paper only supports a putative immune-regulatory context and does not establish ATP6V0A2's modern V-ATPase function as a direct immune-response role [PMID:2247090].
