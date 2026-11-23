# TRAPPC1 notes

Review started from `just fetch-gene human TRAPPC1`. The proteostasis network places TRAPPC1 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Autophagy component recruitment to autophagophore > TRAPP complex component`.

Falcon deep research was requested with `just deep-research-falcon human TRAPPC1`; the provider timed out after 600 seconds and no Falcon research file was generated.

TRAPPC1 is a small core subunit of the transport protein particle (TRAPP) complex. UniProt names the protein "Trafficking protein particle complex subunit 1" and says it is "Part of the multisubunit transport protein particle (TRAPP) complex" with TRAPPC6B-TRAPPC3 interacting with TRAPPC1 to provide a core for TRAPP complex formation. The direct structural paper describes "a human Bet3-Tpc6B heterodimer" as a "core sub-complex in the assembly of TRAPP" and reports that "Bet3-Tpc6A and Bet3-Tpc6B, are able to recruit Mum2, a further TRAPP subunit" [PMID:16828797 "Structure of the Bet3-Tpc6B core of TRAPP: two Tpc6 paralogs form trimeric complexes with Bet3 and Mum2."]. Mum2 is the TRAPPC1 alias in UniProt, so TRAPP-complex membership is the strongest gene-level annotation.

The main process-level role is ER-to-Golgi vesicle-mediated trafficking through TRAPP/RAB1. The TRAPP review states that TRAPP was identified as a complex that co-precipitated with Bet3, "which mediates endoplasmic reticulum (ER)-to-Golgi transport" and that TRAPP "acts as a Ypt/Rab GEF and possibly as a tether" [PMID:27066478 "TRAPP Complexes in Secretion and Autophagy."]. Reactome similarly summarizes that "The TRAPPC complex acts as a guanine-nucleotide exchange factor for RAB1, activating it" [Reactome:R-HSA-5694409 "Nucleotide exchange on RAB1"] and that "TRAPPC is a multi-subunit tethering complex that facilitates ER-to-Golgi traffic" [Reactome:R-HSA-5694439 "COPII coat binds TRAPPCII and RAB1:GDP"]. For TRAPPC1, this supports complex membership and contribution to the complex-level RAB1 GEF/trafficking function, not an independent catalytic MF.

PN autophagy context should be used carefully. The PN mapping rationale itself says the TRAPP leaf is "autophagy-contextual" but that "shared gene-level semantics are still cleanly captured by TRAPP complex membership" [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv]. Reactome notes that in macroautophagy "RAB1 and the TRAPPCIII complex play a role in the formation of the pre-autophagosomal structure (PAS) and contribute to the localization of ATG9" [Reactome:R-HSA-8877475 "TRAPPC complexes exchange GTP for GDP on RAB1"]. However, the TRAPP review cautions that "the connection of the mammalian TRAPP III complex to autophagy is currently not clear" [PMID:27066478]. Therefore, avoid adding a broad autophagy BP for TRAPPC1 in the main review; accept TRAPPIII/TRAPP complex membership and ER/Golgi trafficking, and mention autophagy as contextual.

The coat-assembly annotations are likely over-specific. Reactome says TRAPPCII is recruited to ER-derived vesicles through TRAPPC3-SEC23/COPII interaction, and "Interaction of TRAAPPCII with RAB1:GDP promotes release of GDP" [Reactome:R-HSA-8877475]. That supports TRAPP/RAB1-dependent ER-Golgi traffic and COPII interaction, but not that TRAPPC1 itself assembles vesicle coats. For `vesicle coat assembly` and `COPII vesicle coat assembly`, prefer modifying to ER-to-Golgi vesicle-mediated transport or marking over-annotation rather than accepting the coat-assembly process as core.

The obsolete `vesicle tethering` annotation should not be retained as-is. The TRAPP review explicitly says evidence that TRAPP complexes act as membrane tethers is "currently inconclusive" [PMID:27066478], and the term is obsolete. Replace with ER-to-Golgi vesicle-mediated transport if the annotation is meant to capture the trafficking role.

Generic protein binding annotations from high-throughput interactome maps are not informative for TRAPPC1. Specific interaction information is better captured as TRAPP complex membership and TRAPPII/TRAPPIII protein complex annotations.

The Reactome neutrophil degranulation-derived extracellular region and azurophil granule lumen annotations are not supported by the TRAPPC1/TRAPP literature as core localization. Treat them as over-annotated unless stronger TRAPPC1-specific evidence emerges.

Annotation stance:
- Core: TRAPP complex membership (GO:0030008), including TRAPPII/TRAPPIII protein complex membership where supported.
- Complex-level molecular function to synthesize in core functions: TRAPPC1 contributes to TRAPPC complex guanyl-nucleotide exchange factor activity for RAB1 (GO:0005085), but does not independently enable the GEF activity.
- Core processes: ER-to-Golgi vesicle-mediated transport (GO:0006888) and more general vesicle-mediated transport only as a broad parent/modification target.
- Core locations: cytoplasm/cytosol, endoplasmic reticulum, Golgi apparatus.
- Modify/over-annotate: generic protein binding; vesicle coat assembly and COPII vesicle coat assembly; obsolete vesicle tethering; extracellular/azurophil granule lumen from neutrophil degranulation Reactome.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the Proteostasis Network autophagy component recruitment context was interpreted at gene level through TRAPP/TRAPPII/TRAPPIII complex membership rather than a broad autophagy-process annotation.

## 2026-11-06 ORGANELLES ER batch 4 (endoplasmic reticulum rows)

Row: GO:0005783 IEA (GO_REF:0000044, located_in), the only ER row. No sub-compartment rows.

- UniProt: "Endoplasmic reticulum {ECO:0000250}" (by similarity); yeast BET5 (Q03630, UniProt REST 2026-11-06) carries cis-Golgi network and ER lines unattributed; mouse Q5NCF2 is also ECO:0000250. No TRAPPC1-specific localization study.
- Complex-level support: [PMID:21525244 "TRAPP functions either at ER exit sites or at peripheral ERGIC (BFA-resistant) elements"]; [PMID:21525244 "Localization of subunits by fluorescence microscopy has proven difficult due to the large soluble pools of the proteins"]. Core partner TRAPPC3/Bet3 is concentrated on Sec31-labelled transitional ER by immuno-EM (PMID:16880271; handled in the TRAPPC3 review in this batch, which adds a NEW ER exit site row).
- Soluble, no signal peptide or TM: no ER membrane/lumen row. No NEW GO:0070971 row: only a partner's localization line, and SEC23 binding belongs to TRAPPC3.
- Yeast PMID:11239471 ("TRAPP I is the receptor on the Golgi for COPII vesicles") fetched to check, not cited, deleted.
- Outcome: ACCEPT kept (RAB1 GEF/tethering exercised at ERES); KEEP_AS_NON_CORE noted as alternative. core_functions unchanged.
