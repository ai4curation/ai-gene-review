# Cf-4 (O50025, Solanum habrochaites) — curation notes

## Identity
- O50025 (TrEMBL, 806 aa) = EMBL CAA05268.1, the Cf-4 (Hcr9-4D) gene from *Lycopersicon hirsutum* (= *S. habrochaites*), cloned by Thomas et al. 1997. Signal peptide 1-21, LRR ectodomain, TM 752-776, short cytoplasmic tail, no kinase domain (UniProt features).
- Cf-4 has 25 LRRs vs 27 in Cf-9; >91% identity [PMID:9437864 "Cf-4 contains 25 leucine-rich repeats, which is two fewer than Cf-9. The proteins have > 91% identical amino acids."]
- Cf-4 locus carries five Hcr9 paralogues; Hcr9-4D = Cf-4 (Avr4), Hcr9-4E recognizes Avr4E [PMID:15469522 "While Hcr9-4D represents the functional Cf-4 resistance gene matching Avr4, Hcr9-4E confers resistance towards C. fulvum by mediating recognition of the novel avirulence determinant Avr4E."]
- Cf-4 from L. hirsutum; Cf-4/Cf-9 at the same locus [PMID:15166169 "Cf-4 from L. hirsutum and Cf-9 from L. pimpinellifolium are located at the same locus on the short arm of tomato chromosome 1 in an array of five paralogs."]
- Hcr9-Avr4s conserved across wild tomatoes [PMID:16167771 "Therefore, we conclude that both Cf-4 and Cf-9 predate Lycopersicon speciation."]

## Function
- Specificity determinants in N-terminal domains and LRRs 11-12 [PMID:11226184 "Additional sequences required for Cf-4 function are located in LRRs 11 and 12"].
- Constitutive complex with SOBIR1; SOBIR1 needed for Cf-4 HR/immunity and Cf-4 stability [PMID:23716655 "SOBIR1/EVR is required for stability of the Cf-4 and Ve1 receptors, supporting our observation that these RLPs are present in a complex with SOBIR1/EVR in planta."]
- Avr4 induces BAK1/SERK3 recruitment and endocytosis of Cf-4; Cf-4 at the plasma membrane [PMID:26765243 "Cf-4 interacts with SOBIR1 at the plasma membrane and is recruited to late endosomes upon Avr4 trigger, also depending on BAK1/SERK3."]
- Direct Cf-4–Avr4 binding not established (deep research: "does not establish a purified-protein binding constant or a resolved direct Cf-4–Avr4 structure"). AVR4 chitin binding belongs to the effector, not Cf-4 (see FULFL/AVR4 review).

## Curation decisions
- GO:0038187 pattern recognition receptor activity (EXP, PMID:23716655): definition requires combining with a conserved PAMP. Avr4 is a race-specific effector and direct binding is unproven -> MODIFY to GO:0140376 innate immune receptor activity (already on Cf-4 by EXP; same choice as the CF-9 review).
- GO:0140376 rows: ACCEPT. The PMID:15469522 abstract is about Hcr9-4E/Avr4E, not Cf-4 (Hcr9-4D); full text not cached. Curator (PHI-base) probably used Cf-4 controls; per project rules not removed. Raised as a suggested question.
- GO:0002768 (EXP): ACCEPT (Cf-4 is the receptor initiating the SOBIR1/BAK1 signalling). Consistent with CF-9 NEW row.
- defense response to fungus (ARBA IEA): ACCEPT, consistent with CF-9.
- plasma membrane (IEA): ACCEPT, supported by Postma 2016.
- No NEW rows: all core aspects already present.
