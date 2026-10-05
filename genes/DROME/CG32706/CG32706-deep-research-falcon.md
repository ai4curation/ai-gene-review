---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:17:41.050219'
end_time: '2026-09-08T18:24:21.455450'
duration_seconds: 400.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: CG32706
  gene_symbol: Dmel\CG32706
  uniprot_accession: Q8IRM9
  protein_description: 'RecName: Full=RRM domain-containing protein {ECO:0000259|SMART:SM00360};'
  gene_info: Name=Dmel\CG32706 {ECO:0000313|EMBL:AAN09240.1}; ORFNames=CG32706 {ECO:0000313|EMBL:AAN09240.1,
    ECO:0000313|FlyBase:FBgn0052706}, Dmel_CG32706 {ECO:0000313|EMBL:AAN09240.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the ESF2/ABP1 family.
  protein_domains: ABT1/Esf2. (IPR039119); ABT1/ESF2_RRM. (IPR034353); Nucleotide-bd_a/b_plait_sf.
    (IPR012677); RBD_domain_sf. (IPR035979); RRM_dom. (IPR000504)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CG32706-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8IRM9
- **Protein Description:** RecName: Full=RRM domain-containing protein {ECO:0000259|SMART:SM00360};
- **Gene Information:** Name=Dmel\CG32706 {ECO:0000313|EMBL:AAN09240.1}; ORFNames=CG32706 {ECO:0000313|EMBL:AAN09240.1, ECO:0000313|FlyBase:FBgn0052706}, Dmel_CG32706 {ECO:0000313|EMBL:AAN09240.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the ESF2/ABP1 family.
- **Key Domains:** ABT1/Esf2. (IPR039119); ABT1/ESF2_RRM. (IPR034353); Nucleotide-bd_a/b_plait_sf. (IPR012677); RBD_domain_sf. (IPR035979); RRM_dom. (IPR000504)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG32706" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG32706' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG32706** (gene ID: CG32706, UniProt: Q8IRM9) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8IRM9
- **Protein Description:** RecName: Full=RRM domain-containing protein {ECO:0000259|SMART:SM00360};
- **Gene Information:** Name=Dmel\CG32706 {ECO:0000313|EMBL:AAN09240.1}; ORFNames=CG32706 {ECO:0000313|EMBL:AAN09240.1, ECO:0000313|FlyBase:FBgn0052706}, Dmel_CG32706 {ECO:0000313|EMBL:AAN09240.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the ESF2/ABP1 family.
- **Key Domains:** ABT1/Esf2. (IPR039119); ABT1/ESF2_RRM. (IPR034353); Nucleotide-bd_a/b_plait_sf. (IPR012677); RBD_domain_sf. (IPR035979); RRM_dom. (IPR000504)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG32706" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG32706' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG32706** (gene ID: CG32706, UniProt: Q8IRM9) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional-annotation report: *Drosophila melanogaster* CG32706 (Q8IRM9)

## Executive conclusion

CG32706 is a poorly characterized *D. melanogaster* gene whose identifiers—CG32706, FBgn0052706, EMBL protein AAN09240.1, and UniProt Q8IRM9—are concordant with the supplied record for an RRM-domain-containing protein assigned to the ESF2/ABP1 family. Exact searches for **CG32706**, **FBgn0052706**, and **Q8IRM9** found no primary study directly establishing its molecular activity, RNA substrate, binding partners, localization, pathway, or phenotype. No conflicting literature for a similarly named protein was identified. Accordingly, literature concerning yeast Esf2 must not be presented as direct evidence about the fly protein.

The best-supported working annotation is: **a putative nucleolar RNA-associated assembly factor involved in early precursor-rRNA processing and 40S ribosomal-subunit biogenesis**. More specifically, CG32706 may bind pre-rRNA through its RRM-like region and cooperate with a DEAD-box helicase analogous to yeast Dbp8. This is a family/domain-based hypothesis, not an experimentally demonstrated function in *Drosophila*.

| Topic | Direct CG32706 evidence | ESF2-family evidence (organism) | Best-supported annotation | Confidence |
|---|---|---|---|---|
| Identity and organism | The supplied UniProt record maps Q8IRM9 to **CG32706 / FBgn0052706 / AAN09240.1** in *Drosophila melanogaster*; exact-identifier searches found no conflicting protein. | Published mechanistic studies concern **Esf2/Ynr054c in *Saccharomyces cerevisiae***, not CG32706 (granneman2006thenucleolarprotein pages 1-2, hoang2005esf2pau3associated pages 2-3). | *D. melanogaster* CG32706 encodes Q8IRM9, an uncharacterized ESF2/ABP1-family protein. | **High** for identity; **low** for functional characterization. |
| RRM and ABT1/Esf2 domains | The supplied UniProt/InterPro annotations identify **RRM**, **ABT1/Esf2**, and **ABT1/ESF2_RRM** domains; no fly structural validation was found. | Yeast Esf2 contains a noncanonical/predicted RRM, and deleting that region prevents complementation of Esf2 depletion (hoang2005esf2pau3associated pages 3-4, granneman2006thenucleolarprotein pages 7-8). | Q8IRM9 is probably an RNA-binding ESF2/ABP1-family protein. | **Moderate–high** for domain assignment; **low–moderate** for RNA-binding function in flies. |
| Primary molecular role | No CG32706 biochemical assay was found. | Yeast Esf2 directly binds Dbp8 and stimulates its ATPase activity by improving ATP utilization; stimulation varies with assay conditions and can reach approximately 30-fold (granneman2006thenucleolarprotein pages 1-2, granneman2006thenucleolarprotein pages 9-10, granneman2006thenucleolarprotein pages 6-6). | Probable **RNA-associated ribosome-assembly factor** and possible helicase cofactor, not an enzyme itself. | **Moderate** as family-based inference; **low** for the exact fly mechanism. |
| Substrate | No RNA ligand or sequence specificity has been measured for fly CG32706. | Recombinant yeast Esf2 binds tested 5′ ETS, 18S, and 25S pre-rRNA fragments, apparently without strong sequence specificity; physiological targeting remains unresolved (granneman2006thenucleolarprotein pages 6-6, granneman2006thenucleolarprotein pages 5-6). | Likely substrate class: **nascent pre-rRNA or a pre-ribosomal RNP**, rather than a defined sequence-specific RNA. | **Low–moderate**. |
| Interaction partner | No experimentally validated CG32706 partner was found. | Yeast Esf2 interacts directly and in vivo with the DEAD-box helicase **Dbp8**; its C-terminal region is required for binding and efficient ATPase stimulation (granneman2006thenucleolarprotein pages 7-8, granneman2006thenucleolarprotein pages 5-6). | A fly Dbp8-related helicase is a testable candidate partner, but conservation of this interaction is unproven. | **High** for yeast; **low** for flies. |
| Biochemical pathway | No direct fly pathway experiment was found. | Yeast Esf2 is a component of the **90S/small-subunit processome**, required for early A0–A2 pre-rRNA processing and efficient 18S-rRNA production (hoang2005esf2pau3associated pages 4-5, hoang2005esf2pau3associated pages 2-3, hoang2005esf2pau3associated pages 1-2). | Probable pathway: **nucleolar pre-rRNA processing and 40S ribosomal-subunit biogenesis**. | **Moderate** as evolutionary inference. |
| Cellular localization | No CG32706 microscopy, fractionation, or proximity-labeling result was found. | Yeast Esf2 localizes mainly to the **nucleolus**, associates with 90S particles and 5′ ETS fragments, and is inferred to depart after A2 cleavage (hoang2005esf2pau3associated pages 3-4, hoang2005esf2pau3associated pages 4-5). | Predicted site of action: **nucleolus**, within an early pre-ribosomal assembly complex. | **Low–moderate** for CG32706. |
| Phenotype and essentiality | No CG32706-specific loss-of-function, viability, fertility, or developmental phenotype was found. | Yeast **ESF2 is essential**. Depletion slows growth, disrupts processome assembly, reduces early cleavage, and lowers 18S production relative to 25S by about 50% after 24 hours (hoang2005esf2pau3associated pages 3-4, hoang2005esf2pau3associated pages 4-5, hoang2005esf2pau3associated pages 2-3). | CG32706 may support cellular growth through ribosome production, but fly essentiality is unknown. | **High** for yeast; **very low** for flies. |
| Major uncertainty | Direct fly biochemical, localization, interaction, and phenotype evidence was not found; no 2023–2024 CG32706-specific study was identified. | Even in yeast, the physiological RNA-binding site, precise remodeling event, structural basis of Dbp8 activation, and conservation of the module beyond yeast remain unresolved (granneman2006thenucleolarprotein pages 1-2, granneman2006thenucleolarprotein pages 8-9, granneman2006thenucleolarprotein pages 10-10). | CG32706 should remain annotated as a **putative ESF2/ABP1-family RRM ribosome-biogenesis factor**, with all mechanistic details explicitly labeled as inference from *S. cerevisiae*. | **High** confidence in the uncertainty assessment. |


*Table: Evidence-tier assessment of Drosophila CG32706/Q8IRM9, separating direct fly annotation from mechanistic findings for yeast Esf2. It highlights the probable nucleolar ribosome-biogenesis role and the substantial unresolved uncertainty.*

## 1. Identity verification and nomenclature

The target is specifically the *D. melanogaster* protein **Q8IRM9**, encoded by **CG32706/FBgn0052706**, and not another gene sharing an ESF2-, ABP1-, or CG-like designation. The supplied domain calls—ABT1/Esf2 (IPR039119), ABT1/ESF2_RRM (IPR034353), RRM domain (IPR000504), RNA-binding-domain superfamily (IPR035979), and nucleotide-binding α/β-plait fold (IPR012677)—are internally consistent with the description “RRM domain-containing protein” and ESF2/ABP1-family assignment.

The literature retrieved under “Esf2” instead characterizes *Saccharomyces cerevisiae* Ynr054c/Esf2. That yeast protein was named Esf2 after proteomic/genomic evidence connected it to preribosomal particles; these publications contain no CG32706, FBgn0052706, or Q8IRM9-specific experiment (granneman2006thenucleolarprotein pages 1-2, hoang2005esf2pau3associated pages 2-3).

Useful database URLs for record verification are:

- UniProt Q8IRM9: https://www.uniprot.org/uniprotkb/Q8IRM9/entry
- FlyBase FBgn0052706: https://flybase.org/reports/FBgn0052706
- InterPro entries: https://www.ebi.ac.uk/interpro/entry/InterPro/IPR039119/ and https://www.ebi.ac.uk/interpro/entry/InterPro/IPR034353/

## 2. Protein class and likely molecular function

### Directly supported for CG32706

The protein is computationally assigned an RRM-related α/β-plait RNA-binding fold and an ABT1/Esf2-family region. An RRM designation supports an RNA-associated role, but it does **not** establish a particular RNA sequence, catalytic activity, or cellular pathway. No purified-CG32706 RNA-binding assay, enzymatic assay, structure, or interaction experiment was found.

CG32706 should therefore not be annotated as an enzyme. The most plausible role is that of an **RNA-binding adaptor or ribosome-assembly cofactor**. If the yeast mechanism is conserved, it would modulate another enzyme—a DEAD-box ATPase—rather than catalyze a reaction itself.

### Mechanistic evidence from yeast Esf2

Yeast Esf2 directly interacts with the DEAD-box helicase Dbp8 in yeast two-hybrid, pull-down, and in-vivo co-immunoprecipitation experiments. Recombinant Esf2 binds multiple pre-rRNA fragments and stimulates Dbp8 ATP hydrolysis by lowering its apparent ATP requirement; the authors proposed that Esf2 could both activate Dbp8 and help position it on pre-rRNA (publication: 15 June 2006, https://doi.org/10.1093/nar/gkl419) (granneman2006thenucleolarprotein pages 1-2, granneman2006thenucleolarprotein pages 5-6).

The interaction is functionally meaningful in yeast: deleting Esf2 residues 206–317, encompassing its C-terminal interaction region, abolished detectable Dbp8 binding and reduced ATPase stimulation from approximately ninefold with full-length Esf2 to twofold. Neither this C-terminal mutant nor an RRM-deletion mutant supported growth after endogenous Esf2 depletion (granneman2006thenucleolarprotein pages 7-8).

Reported stimulation varied substantially with buffer and protein/RNA conditions—from about twofold at 200 mM KCl to approximately 30-fold under optimized conditions. This variation cautions against treating any single fold-change as an intrinsic biochemical constant (granneman2006thenucleolarprotein pages 6-6, granneman2006thenucleolarprotein pages 9-10).

## 3. RNA substrate and specificity

There is no experimentally defined CG32706 substrate. For yeast Esf2, approximately 200–300-nucleotide transcripts spanning the 5′ external transcribed spacer, 18S rRNA, and 25S rRNA regions all bound recombinant protein; one 5′-ETS fragment spanning positions 361–799 bound more weakly. The broad binding pattern suggests little obvious sequence specificity in the isolated-protein assay (granneman2006thenucleolarprotein pages 6-6, granneman2006thenucleolarprotein pages 5-6).

Thus, the appropriate CG32706 substrate annotation is **putative pre-rRNA or an early preribosomal ribonucleoprotein particle**, not a defined nucleotide motif. The physiological RNA-binding site, if any, remains unknown. Yeast Dbp8-mediated ATP-dependent strand separation was also not unequivocally demonstrated, so the exact RNA-remodeling reaction cannot presently be assigned even to the reference Esf2–Dbp8 system (granneman2006thenucleolarprotein pages 10-10).

## 4. Biological process and biochemical pathway

The strongest family-based model places CG32706 in **ribosome biogenesis**, specifically early maturation of the 18S-rRNA-containing small subunit. In yeast, Esf2 associates with U3 snoRNA, 5′-ETS fragments, and 90S/small-subunit-processome factors. Its depletion impairs cleavage at A0, A1, and A2; causes accumulation of 35S, 33S/32S, and aberrant 23S precursors; reduces 27SA2 and 20S intermediates; and slows 20S-to-18S maturation (publication: July 2005, https://doi.org/10.1128/MCB.25.13.5523-5534.2005) (hoang2005esf2pau3associated pages 4-5, hoang2005esf2pau3associated pages 1-2).

After 24 hours of yeast Esf2 depletion, 18S-rRNA synthesis relative to 25S was reduced by approximately 50%, while large-subunit 27S processing and 25S production were comparatively preserved. This argues for a primary role in small-subunit production rather than a nonspecific shutdown of all ribosome synthesis (hoang2005esf2pau3associated pages 4-5).

Chromatin-spread measurements provide additional quantitative evidence. Average processomes per rDNA gene fell from 9.6 in controls to 7.9 after 18 hours and 6.1 after 24 hours of depletion; cleaved transcripts fell from 8.1 to 2.1 and 1.7, respectively. These results support roles in processome assembly, compaction, and cotranscriptional cleavage (hoang2005esf2pau3associated pages 2-3).

For CG32706, however, “pre-rRNA processing” and “40S-subunit biogenesis” should remain **predicted** biological-process annotations until fly loss-of-function experiments demonstrate altered pre-rRNA intermediates or small-subunit output.

## 5. Cellular localization

No direct localization study of Q8IRM9 was found. The predicted site of function is the **nucleolus**, because that is where early pre-rRNA transcription, SSU-processome assembly, and the characterized yeast Esf2 mechanism occur.

In yeast, GFP-tagged Esf2 localizes predominantly to the nucleolus, with minor cytoplasmic signal. Biochemical fractionation places it in early 90S particles and particles associated with 5′-ETS fragments, but not prominently in later pre-40S fractions. The investigators therefore inferred that Esf2 acts early and probably departs after A2 cleavage (hoang2005esf2pau3associated pages 3-4, hoang2005esf2pau3associated pages 4-5).

Consequently, “nucleolar” is a biologically coherent prediction for CG32706, but it is not yet a verified fly localization. Nuclear/nucleolar imaging of an endogenously tagged protein would be required to establish it.

## 6. Phenotype, essentiality, and physiological significance

No CG32706-specific viability, developmental, fertility, or tissue phenotype was identified. It is therefore inappropriate to call the fly gene essential solely because yeast ESF2 is essential.

In yeast, depletion progressively increased doubling time from 140 minutes before depletion to 166 minutes after 10 hours and 260 minutes after 20–24 hours, compared with approximately 120 minutes for wild type. This growth defect accompanies the pre-rRNA-processing phenotype and is consistent with inadequate ribosome production (hoang2005esf2pau3associated pages 3-4).

The likely real-world cellular consequence of CG32706 loss—if the family function is conserved—would be reduced 40S-subunit supply, impaired translation capacity, and growth or developmental defects in rapidly biosynthetic tissues. These downstream effects remain predictions, not observed CG32706 phenotypes.

## 7. Current research status and 2023–2024 literature

No 2023–2024 publication specifically characterizing CG32706/Q8IRM9 was found. The decisive mechanistic literature remains the 2005 SSU-processome study and the 2006 Esf2–Dbp8 biochemical study. A 2022 expert review describes ribosome-biogenesis helicases as regulators of pre-rRNA folding and RNP remodeling and notes the Esf2–Dbp8 interaction, but the underlying evidence remains predominantly yeast-based; it does not validate the same module in *Drosophila* (review published 13 June 2022: https://doi.org/10.1080/15476286.2022.2079890).

The absence of recent gene-specific papers is itself important. Modern cryo-EM and functional-genomics advances have greatly refined many stages of 90S and pre-40S maturation, but they have not, in the retrieved literature, supplied a direct structure, binding site, or fly phenotype for CG32706. Even for yeast Esf2, the precise physiological RNA site, the ATP-coupled remodeling event, and the structural basis of Dbp8 activation remain unresolved (granneman2006thenucleolarprotein pages 1-2, granneman2006thenucleolarprotein pages 8-9, granneman2006thenucleolarprotein pages 10-10).

## 8. Recommended functional annotation

A suitably conservative annotation is:

> **CG32706/Q8IRM9 is an uncharacterized *Drosophila melanogaster* ESF2/ABP1-family protein containing an RRM-related RNA-binding fold. By family homology, it is predicted to act in the nucleolus as an RNA-associated assembly factor during early pre-rRNA processing and 40S ribosomal-subunit biogenesis, potentially as a cofactor for a Dbp8-like DEAD-box ATPase. Its RNA substrate, interaction partner, localization, necessity, and biochemical mechanism have not been experimentally established in *Drosophila*.**

Confidence is high for the identifier, organism, and domain/family assignment; moderate for a general RNA-associated ribosome-biogenesis role; low-to-moderate for nucleolar localization; and low for the specific Dbp8-cofactor mechanism in flies.

## 9. Highest-priority validation experiments

1. Endogenous fluorescent or epitope tagging to test nuclear/nucleolar localization and recruitment to nascent rDNA.
2. CG32706 knockout or acute depletion followed by Northern blotting or targeted RNA sequencing of fly pre-rRNA intermediates and measurement of mature 18S:28S ratios.
3. Polysome and ribosomal-subunit profiling to test for selective 40S deficiency.
4. Affinity purification–mass spectrometry or proximity labeling to identify a fly Dbp8-like helicase and SSU-processome partners.
5. UV-crosslinking/RIP or CLIP to determine whether CG32706 directly occupies 5′-ETS or 18S precursor sequences.
6. Purified-protein assays testing RNA binding and stimulation of the candidate fly helicase’s ATPase activity, coupled to RRM and interaction-region mutants.

These experiments would distinguish a conserved ESF2-like ribosome-assembly factor from another RRM-dependent RNA-processing role and convert the present computational/family assignment into a defensible fly-specific functional annotation.

References

1. (granneman2006thenucleolarprotein pages 1-2): S. Granneman, Chieyu Lin, E. A. Champion, M. R. Nandineni, Cornelia Zorca, and S. Baserga. The nucleolar protein esf2 interacts directly with the dexd/h box rna helicase, dbp8, to stimulate atp hydrolysis. Nucleic Acids Research, 34:3189-3199, Jun 2006. URL: https://doi.org/10.1093/nar/gkl419, doi:10.1093/nar/gkl419. This article has 81 citations and is from a highest quality peer-reviewed journal.

2. (hoang2005esf2pau3associated pages 2-3): Tran Hoang, Wen-Tao Peng, Emmanuel Vanrobays, Nevan Krogan, Shawna Hiley, Ann L. Beyer, Yvonne N. Osheim, Jack Greenblatt, Timothy R. Hughes, and Denis L. J. Lafontaine. Esf2p, a u3-associated factor required for small-subunit processome assembly and compaction. Molecular and Cellular Biology, 25:5523-5534, Jul 2005. URL: https://doi.org/10.1128/mcb.25.13.5523-5534.2005, doi:10.1128/mcb.25.13.5523-5534.2005. This article has 42 citations and is from a domain leading peer-reviewed journal.

3. (hoang2005esf2pau3associated pages 3-4): Tran Hoang, Wen-Tao Peng, Emmanuel Vanrobays, Nevan Krogan, Shawna Hiley, Ann L. Beyer, Yvonne N. Osheim, Jack Greenblatt, Timothy R. Hughes, and Denis L. J. Lafontaine. Esf2p, a u3-associated factor required for small-subunit processome assembly and compaction. Molecular and Cellular Biology, 25:5523-5534, Jul 2005. URL: https://doi.org/10.1128/mcb.25.13.5523-5534.2005, doi:10.1128/mcb.25.13.5523-5534.2005. This article has 42 citations and is from a domain leading peer-reviewed journal.

4. (granneman2006thenucleolarprotein pages 7-8): S. Granneman, Chieyu Lin, E. A. Champion, M. R. Nandineni, Cornelia Zorca, and S. Baserga. The nucleolar protein esf2 interacts directly with the dexd/h box rna helicase, dbp8, to stimulate atp hydrolysis. Nucleic Acids Research, 34:3189-3199, Jun 2006. URL: https://doi.org/10.1093/nar/gkl419, doi:10.1093/nar/gkl419. This article has 81 citations and is from a highest quality peer-reviewed journal.

5. (granneman2006thenucleolarprotein pages 9-10): S. Granneman, Chieyu Lin, E. A. Champion, M. R. Nandineni, Cornelia Zorca, and S. Baserga. The nucleolar protein esf2 interacts directly with the dexd/h box rna helicase, dbp8, to stimulate atp hydrolysis. Nucleic Acids Research, 34:3189-3199, Jun 2006. URL: https://doi.org/10.1093/nar/gkl419, doi:10.1093/nar/gkl419. This article has 81 citations and is from a highest quality peer-reviewed journal.

6. (granneman2006thenucleolarprotein pages 6-6): S. Granneman, Chieyu Lin, E. A. Champion, M. R. Nandineni, Cornelia Zorca, and S. Baserga. The nucleolar protein esf2 interacts directly with the dexd/h box rna helicase, dbp8, to stimulate atp hydrolysis. Nucleic Acids Research, 34:3189-3199, Jun 2006. URL: https://doi.org/10.1093/nar/gkl419, doi:10.1093/nar/gkl419. This article has 81 citations and is from a highest quality peer-reviewed journal.

7. (granneman2006thenucleolarprotein pages 5-6): S. Granneman, Chieyu Lin, E. A. Champion, M. R. Nandineni, Cornelia Zorca, and S. Baserga. The nucleolar protein esf2 interacts directly with the dexd/h box rna helicase, dbp8, to stimulate atp hydrolysis. Nucleic Acids Research, 34:3189-3199, Jun 2006. URL: https://doi.org/10.1093/nar/gkl419, doi:10.1093/nar/gkl419. This article has 81 citations and is from a highest quality peer-reviewed journal.

8. (hoang2005esf2pau3associated pages 4-5): Tran Hoang, Wen-Tao Peng, Emmanuel Vanrobays, Nevan Krogan, Shawna Hiley, Ann L. Beyer, Yvonne N. Osheim, Jack Greenblatt, Timothy R. Hughes, and Denis L. J. Lafontaine. Esf2p, a u3-associated factor required for small-subunit processome assembly and compaction. Molecular and Cellular Biology, 25:5523-5534, Jul 2005. URL: https://doi.org/10.1128/mcb.25.13.5523-5534.2005, doi:10.1128/mcb.25.13.5523-5534.2005. This article has 42 citations and is from a domain leading peer-reviewed journal.

9. (hoang2005esf2pau3associated pages 1-2): Tran Hoang, Wen-Tao Peng, Emmanuel Vanrobays, Nevan Krogan, Shawna Hiley, Ann L. Beyer, Yvonne N. Osheim, Jack Greenblatt, Timothy R. Hughes, and Denis L. J. Lafontaine. Esf2p, a u3-associated factor required for small-subunit processome assembly and compaction. Molecular and Cellular Biology, 25:5523-5534, Jul 2005. URL: https://doi.org/10.1128/mcb.25.13.5523-5534.2005, doi:10.1128/mcb.25.13.5523-5534.2005. This article has 42 citations and is from a domain leading peer-reviewed journal.

10. (granneman2006thenucleolarprotein pages 8-9): S. Granneman, Chieyu Lin, E. A. Champion, M. R. Nandineni, Cornelia Zorca, and S. Baserga. The nucleolar protein esf2 interacts directly with the dexd/h box rna helicase, dbp8, to stimulate atp hydrolysis. Nucleic Acids Research, 34:3189-3199, Jun 2006. URL: https://doi.org/10.1093/nar/gkl419, doi:10.1093/nar/gkl419. This article has 81 citations and is from a highest quality peer-reviewed journal.

11. (granneman2006thenucleolarprotein pages 10-10): S. Granneman, Chieyu Lin, E. A. Champion, M. R. Nandineni, Cornelia Zorca, and S. Baserga. The nucleolar protein esf2 interacts directly with the dexd/h box rna helicase, dbp8, to stimulate atp hydrolysis. Nucleic Acids Research, 34:3189-3199, Jun 2006. URL: https://doi.org/10.1093/nar/gkl419, doi:10.1093/nar/gkl419. This article has 81 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CG32706-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. granneman2006thenucleolarprotein pages 7-8
2. granneman2006thenucleolarprotein pages 10-10
3. granneman2006thenucleolarprotein pages 1-2
4. granneman2006thenucleolarprotein pages 9-10
5. granneman2006thenucleolarprotein pages 6-6
6. granneman2006thenucleolarprotein pages 5-6
7. granneman2006thenucleolarprotein pages 8-9
8. https://www.uniprot.org/uniprotkb/Q8IRM9/entry
9. https://flybase.org/reports/FBgn0052706
10. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR039119/
11. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR034353/
12. https://doi.org/10.1093/nar/gkl419
13. https://doi.org/10.1128/MCB.25.13.5523-5534.2005
14. https://doi.org/10.1080/15476286.2022.2079890
15. https://doi.org/10.1093/nar/gkl419,
16. https://doi.org/10.1128/mcb.25.13.5523-5534.2005,