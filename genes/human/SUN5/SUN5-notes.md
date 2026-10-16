# SUN5 (SPAG4L, TSARG4) review notes

## 2026-09-27 — initial review (claude-code)

Sources: UniProt Q8TC36, GOA (17 rows), cached publications, Falcon deep research (arrived during review).

### Identity / topology
- 379 aa single-pass SUN protein: nucleoplasmic N-terminus (1-105), TM 106-122, luminal coiled coil and SUN domain (205-364) [file:human/SUN5/SUN5-uniprot.txt].
- Stated INM location [PMID:27640305 "SUN5 is a 379-amino-acid transmembrane protein located in the inner nuclear membrane (INM)"] (by citation of prior work).

### Localization dynamics (mouse)
- Golgi transit and glycosylation, then NE, then head-tail junction [PMID:25775128 "Finally, we show that Sun5 transits through the Golgi apparatus, leading to post-translational modifications"]. Excluded from acrosome-facing NE (contradicts earlier apical localization claim, PMID:21159740).
- Mature sperm: coupling apparatus in implantation fossa [PMID:28945193 "In mature spermatozoa, SUN5 was localized to the coupling apparatus of the sperm head and tail in the implantation fossa"].

### Function
- Sun5-/- mice: acephalic sperm; HTCA assembles but detaches from implantation fossa; meiosis normal [PMID:28945193 "We found that knockout of Sun5 has no effects on mouse meiosis, acrosome biogenesis or sperm nuclear remodeling"].
- KASH partner = Nesprin-3 (SYNE3): co-IP + IF, Sun5 required to position Nesprin3 posteriorly [PMID:34268309 "Sun5 and Nesprin3 were indeed bona fide interaction partners that formed the linker of the nucleoskeleton and cytoskeleton (LINC) complex"]; human variant sperm + HEK293T co-IP SUN5-Nesprin3-ODF1 "triplet" [PMID:33848337, abstract only].
- Lamin B1 and Septin12/Septin2 partners (IP-MS; abstract only) [PMID:38870534 "SUN5 connected the nucleus by interacting with LaminB1 and connected the proximal centriole by interacting with Septin12"]. Topology puzzle: septins are cytoplasmic, SUN domain luminal.
- DNAJB13 chaperone-like partner [PMID:29298896].
- Claimed SPAG4L-Nesprin2 meiotic LINC complex [PMID:31144711, abstract only] — weak; not used for annotation.
- Human biallelic variants: acephalic spermatozoa syndrome (SPGF16) [PMID:27640305].

### Decisions
- GO:0034993 meiotic LINC IBA -> MODIFY to GO:0106094 (SUN5 forms a LINC complex with Nesprin3, but post-meiotically; meiosis normal in KO). propagation_review: TERM_SCOPING_PROBLEM / FUNCTIONAL_DIVERGENCE.
- Protein binding: LMNB1 -> MODIFY lamin binding; SEPTIN2/SEPTIN12 and SPAG4 (HuRI) -> REMOVE (uninformative; no septin-binding MF in GO).
- Golgi -> KEEP_AS_NON_CORE (transit compartment).
- Core: GO:0043495 protein-membrane adaptor activity; spermatid development; INM + sperm head-tail coupling apparatus; complex GO:0106094.

### Deep research (Falcon)
- Consistent with the above; highlights Nesprin3/ODF1 and 2024 lamin B1/SEPTIN12 work [file:human/SUN5/SUN5-deep-research-falcon.md "Its core role is structural attachment of the sperm HTCA/neck to the nuclear envelope."]. DR-only (not verified here): ARRDC5/SEC22A trafficking of SUN5 (Liu 2023), SPAG4Lbeta isoform lacking TM.
