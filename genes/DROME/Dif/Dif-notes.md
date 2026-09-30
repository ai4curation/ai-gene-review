# Dif (Dorsal-related immunity factor, P98149) review notes

Reviewed together with dl (P15330) for the INNATE_IMMUNITY project (batch 1, Toll/TLR axis). Actions were kept consistent with dl.

## Biology (with provenance)

- Immune Rel factor, not a D/V patterning factor [PMID:8242747 "Although Dif maps close to dorsal, it does not appear to participate in DV patterning, but instead mediates an immune response in Drosophila larvae."]
- Nuclear accumulation upon infection [PMID:8242747 "Dif is normally localized in the cytoplasm of the larval fat body, but quickly accumulates in the nucleus upon bacterial infection or injury."]
- Sequence-specific trans-activator [PMID:7621828 "This study establishes that Dif is a sequence-specific transcription factor and is probably a key activator of the immune response in Drosophila."]
- Downstream of Toll [PMID:10197979 "We also demonstrate that Dif is a downstream component of the Toll signaling pathway in activating the drosomycin expression."]
- Antifungal and Gram-positive defence; the only one required in adults [PMID:10843389 "DIF alone is required for the antifungal response in adults, but is redundant in larvae with Dorsal"] [PMID:10843389 "In Drosophila, Dif appears to be dedicated to the antifungal defense elicited by fungi and gram-positive bacteria."]
- Mediator dTRAP80 (MED17, FBgn0038578) is required for Dif activation [PMID:12556495 "activation of Drosophila antimicrobial peptide drosomycin gene expression by the NF-kappa B-like transcription factor Dif during induction of the Toll signaling pathway was dependent on the dTRAP80 module."]
- Dif-Relish heterodimer [PMID:20679214 "Our results demonstrate that the linked heterodimer can activate target genes of both the Toll and IMD pathways."]
- Caveat: in larvae, Wu & Anderson found that Toll is not required for Dif import [PMID:9510254 "here we show that the Toll pathway is not required for nuclear import of Dif"]. Later adult genetics (PMID:10843389, PMID:10197979) place Dif downstream of Toll. This is recorded as a suggested question.

## Key curation decisions

1. **Salivary gland histolysis (GO:0035070, IMP PMID:11973616)**: REMOVE. The paper's own abstract contradicts it: [PMID:11973616 "We show that null mutations in the three Drosophila Rel/NF-kappa B family members, either alone or in combination, have no apparent effect on this death response."] This is a contradicted function, not an unverifiable one. It may have been meant as a NOT annotation.
2. **Toll signaling pathway**: all rows ACCEPTed. There is no TLR (GO:0002224) term, which is correct.
3. **Canonical NF-kB (GO:0007249)** is non-core and **non-canonical NF-kB (GO:0038061) IBA** is removed, the same as for dl. See the dl notes; ird5/IKKbeta is dispensable for drosomycin induction [PMID:11156609 "The ird5 phenotype and sequence suggest that the gene is specifically required for the activation of Relish, a Drosophila NF-kappaB family member."]
4. **Protein binding**:
   - The Dorsal and Relish rows become MODIFY to protein heterodimerization activity (GO:0046982).
   - The dTRAP80 row becomes MODIFY to mediator complex binding (GO:0036033).
   - The Cactus row is REMOVEd as uninformative.
5. Core terms are all ACCEPTed: Gram-positive and fungal defence, positive regulation of antifungal/antimicrobial peptide production, innate immune response, and transcription activator activity.
6. Positive regulation of gene expression (NO/CCO under starvation, PMID:19221590), hemocyte proliferation, PNS development, immune response and response to cytokine are kept as non-core.
7. No NEW annotations. Dif carries no D/V patterning terms, which is correct.

## Deep research

Falcon deep research had been queued by a background job but had not finished by the time this review was written. The review is based on the UniProt record and the cached publications.
