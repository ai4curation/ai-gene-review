# BABAM1 notes

## 2026-10-05 review (PAINT, affinage)

- MERIT40/NBA1: [PMID:19261748 "Importantly, MERIT40 regulates BRCA1 retention at DNA breaks and checkpoint function primarily via a role in maintaining the stability of BRE and this five-subunit protein complex at sites of DNA damage."]
- Both complexes: [PMID:21282113 "Both BRCC36-containing complexes contain common components including BRE and NBA1/MERIT40."]
- Accepted the complex, DSB repair, G2 checkpoint, IR response, DNA repair regulation and location rows.
- Response to vitamin B6 (NAS) is marked as an over-annotation: PLP sensing is done by SHMT2 (PMID:31142841).
- Identical protein binding, chromatin remodeling, G2/M checkpoint NAS and nuclear body are kept as non-core.
- Removed 17 GO:0005515 rows. BABAM2 and ABRAXAS1 are captured by the complex rows.

## 2026-10-05 revision (reviewer round 1)

- Nucleus and nucleoplasm rows now quote UniProt's Nucleus line (the previous line quoted stated the cytoplasm). The NAS rows were re-quoted for their own terms.
- NEW GO:0030674 adaptor activity (IDA, PMID:30533199) is the core MF [PMID:30533199 "We found that tankyrase is localized to DSBs through its interaction with MERIT40, and pharmacological inhibition of tankyrase sensitized human lung cancer cells to DNA-damaging anticancer agents."].
- ICL repair (PMID:26338419): MERIT40 is at psoralen ICLs and needed for BRCA1/RAD51/RPA recruitment, and Merit40-null MEFs are MMC-sensitive but not IR-sensitive. GO:0036297 is not asserted because no BRCA1-A member (nor BRCA1) carries it in GOA; it is raised as a suggested question. The IR-resistance (GO:0010212) rows stay accepted, as they rest on human depletion screens (PMID:19261749) rather than the mouse null.
- HSC expansion in MERIT40 deficiency (PMID:25636339, thrombopoietin signalling) was considered and not annotated: it is a physiological phenotype with no defined molecular mechanism in the abstract.
