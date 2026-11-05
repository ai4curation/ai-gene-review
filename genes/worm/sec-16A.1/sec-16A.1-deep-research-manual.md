# sec-16A.1 (ZK512.5; UniProt P34643) - manual literature review

No deep-research provider was available for this review, so this file records a
manual literature survey (PubMed search plus cached full texts in `publications/`).

## Search

PubMed query `(sec-16 OR SEC-16 OR Sec16) AND (elegans)` (2026-10-28) returned three
records: PMID:21478858, PMID:23840591 and PMID:35870495. PMID:35870495 is a
Drosophila tracheal study that mentions C. elegans only in passing and does not
study the worm protein; it was not used.

## Identity and family

- UniProt P34643 (SC161_CAEEL), 1232 aa, gene sec-16A.1, ORF ZK512.5; two isoforms
  (a, b; b lacks residues 1-8).
- Pfam PF12932 (Sec16 central conserved domain) and PF12931 (TPR_Sec16 / Sec23-binding
  C-terminal domain); InterPro IPR024340 Sec16_CCD and IPR024298 Sec16_Sec23-bd;
  PANTHER PTHR13402:SF6. UniProt: "Belongs to the SEC16 family."
- Long N-terminal and internal stretches are predicted disordered (MobiDB-lite),
  typical of Sec16 proteins.
- The protein was identified as the worm Sec16 homologue by Witte et al.
  [PMID:21478858 "Based upon the sequence of human Sec16A, we identified a Sec16 homolog in C. elegans encoded by ZK512.5, which we named sec-16"].

## Experimental findings

### Witte et al. 2011 (PMID:21478858, full text)

- Sec16 is framed as the ERES scaffold [PMID:21478858 "Sec16 interacts with all COPII coat components, potentially serving as a scaffold for their recruitment"].
- SEC-16 immunoprecipitation from embryo extracts plus mass spectrometry identified
  19 reproducible partners; RNAi showed [PMID:21478858 "7 out of 19 gene products were necessary for embryo production: SEC-16, four COPII subunits"].
- Direct binding to TFG-1 [PMID:21478858 "We found that a GST-fusion to SEC-16, but not GST alone, was capable of binding to recombinant TFG-1"; "These data confirm a direct biochemical association between SEC-16 and TFG-1."]. The TFG-1 N-terminus mediates the interaction.
- Localization: SEC-16 marks ER exit sites in the germline/oocytes [PMID:21478858 "We conclude that TFG-1 localizes to ER exit sites with both SEC-16 and COPII machinery."].
- Mutual dependence [PMID:21478858 "We conclude that TFG-1 requires SEC-16 for its localization, while SEC-16 requires TFG-1 to accumulate normally on ER exit sites."].
- SEC-16 depletion disrupts ERES and COPII puncta [PMID:21478858 "Depletion of SEC-16 led to nearly complete loss of puncta labeled by TFG-1, and the few structures that were observed appeared abnormally large and did not co-stain for the COPII component SEC-13"].
- SEC-16 recruits COPII in proportion to its own level at ERES [PMID:21478858 "indicating that the remaining SEC-16 on ER exit sites can continue to recruit COPII components in the absence of TFG-1"].
- Secretory pathway phenotype of SEC-16 depletion [PMID:21478858 "following depletion of either SEC-16 or TFG-1, RAB-6 accumulated on fewer, large punctate structures in the germline that also harbored RAB-5, suggesting that RAB-6 localization was shifted from the Golgi to enlarged early endosomes"].
- SEC-16 and TFG-1 co-fractionate in large (>800 kD) complexes; TFG-1 hexamers promote
  assembly of SEC-16/COPII complexes.

### Ackema et al. 2013 (PMID:23840591, full text)

- Studies the ArfGEF GBF-1; SEC-16 is used as an anti-SEC-16 antibody ERES marker.
  [PMID:23840591 "GBF-1 was localized juxtaposed to the ERES marker SEC-16."]
- gbf-1(RNAi) does not change SEC-16 localization [PMID:23840591 "However, in all analyzed oocytes SEC-16 still localized in marked patches on close to the Golgi, similar to its localization in wild-type or mock-treated animals"].
- The paper does not describe SEC-16 in an ERGIC; "ERGIC" does not appear in the full
  text. UniProt nevertheless cites it for "Endoplasmic reticulum-Golgi intermediate
  compartment" localization.

## Gaps

- No biochemical reconstitution of worm SEC-16 with Sec23/Sec24, Sec13/Sec31 or SAR-1.
- Roles of the paralogous worm Sec16-family genes (other sec-16 loci) relative to
  sec-16A.1 are not established in the literature found.
- No studies in somatic secretory tissues (intestine, hypodermis, neurons) were found.
