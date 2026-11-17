# Mycobacterial FadBA identity and substrate scope

PMID:23496842 identifies a divergent alpha2beta2 TFE. Official H37Rv PDB 4B3H entities and SIFTS map alpha O53872/Rv0860/fadB and beta O53871/Rv0859/fadA. The 720-residue alpha is exactly present after a 16-residue tag in the 736-residue construct; beta 403 residues match exactly. FadA2 is a different thiolase and does not assemble with this alpha in that study. See sequence-identity.json for executable-source endpoints and sequence hashes. Species and locus agree; no virulence or native complete-oxidation conclusion follows from the purified complex.

## Primary 2021 author-source text

PMID:34371166, DOI 10.1016/j.jsb.2021.107776. Official author repository PDF: https://oulurepo.oulu.fi/bitstream/handle/10024/31233/nbnfi-fe2021091546215.pdf?isAllowed=y&sequence=1 . Downloaded 2026-11-06; exact PDF hash and download metadata are in provenance.json. pdftotext -layout produced the ignored extraction. Quotes below join line wraps and the PDF's line-break hyphenation; no biological wording is changed.

Verbatim Results: "no thiolase activity is detected with the substrate acetoacetyl-CoA."

Verbatim Results: "This qualitative thiolase assay showed activity when testing for degradation of 3-ketodecanoyl-CoA and 3-ketohexadecanoyl-CoA."

Verbatim Table 2 column labels: "ECH" and "HAD". At 60 µM 2E-hexadecenoyl-CoA, reported activities are 125.2±15.9 and 5.3±0.2µmol mg−1 min−1, respectively. The measured HAD signal is NADH production, coupled to upstream hydration; the long-chain substrate is C16. No HAD activity was detected with 2E-butenoyl-CoA. The KAT test generates 3-ketoacyl-CoA using hydration/dehydrogenation, then adds CoA and monitors loss of its Mg2+ complex. It is qualitative, not a steady-state thiolase specificity ratio. Acetoacetyl-CoA non-detection has no quantitative LOD stated in the main text and does not prove an evolutionary loss.

The isolated alpha has both ECH and HAD activities but is less stable and less active, especially for HAD. The proposed need for alpha to stabilize a competent Mtb beta dimer partly rests on a Mycobacterium avium homolog structure and interface analysis; it is not the same direct isolated-beta inactivity experiment as in P. fragi. Small residual turnover of a cholesterol-derived FadA5 substrate is reported; it does not establish native cholesterol-side-chain function for this FadA.

PMID:39012716 full primary reports fragment-bound structures and proposes a substrate-channeling path. Orthogonal studies are still needed to validate channeling and identify substrates using it. These are not kinetic measurements of complete fatty-acid oxidation.

## Secondary isomerase lead

The 2021 introduction reports 3E-octenoyl→2E-octenoyl conversion by Mtb FadB, citing PMID:26628360, whereas 3Z-octenoyl is not a substrate. Current GO:0004165 explicitly allows either 3Z or 3E reaction. The 2015 abstract confirms cis-substrate restriction and auxiliary isomerases, but publisher full-text/PDF attempts returned 403 and institutional/Oulu searches found no accessible primary manuscript. No new isomerase annotation is based solely on this second-hand assay detail; exact 2015 construct and assay remain to be verified.
