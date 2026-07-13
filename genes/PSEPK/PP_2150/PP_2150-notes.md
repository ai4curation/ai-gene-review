# PP_2150 notes

2026-07-09 PDT / 2026-07-10 UTC: First-pass cell-envelope/division
ApbE/FMNylylation singleton curation. UniProt names PP_2150 as a
FAD:protein FMN transferase with EC 2.7.1.180, states that it transfers the
FMN moiety of FAD to a threonine residue on target proteins, and records the
Rhea reaction for L-threonyl-[protein] flavinylation [file:PSEPK/PP_2150/PP_2150-uniprot.txt
"DE   RecName: Full=FAD:protein FMN transferase";
file:PSEPK/PP_2150/PP_2150-uniprot.txt "CC   -!- FUNCTION: Flavin
transferase that catalyzes the transfer of the FMN";
file:PSEPK/PP_2150/PP_2150-uniprot.txt "Reaction=L-threonyl-[protein] + FAD
= FMN-L-threonyl-[protein] + AMP +"]. GOA already includes the specific
`GO:7770036 flavin transferase activity` term along with broader transferase
and metal-ion binding annotations [file:PSEPK/PP_2150/PP_2150-goa.tsv
"GO:7770036	flavin transferase activity"; file:PSEPK/PP_2150/PP_2150-goa.tsv
"GO:0016740	transferase activity"; file:PSEPK/PP_2150/PP_2150-goa.tsv
"GO:0046872	metal ion binding"].

Localization and cofactors: UniProt places the protein at the cell inner
membrane with a lipid anchor and periplasmic-side orientation, and records Mg
and Mn cofactor context [file:PSEPK/PP_2150/PP_2150-uniprot.txt "CC   -!-
SUBCELLULAR LOCATION: Cell inner membrane"; file:PSEPK/PP_2150/PP_2150-uniprot.txt
"CC       Periplasmic side"; file:PSEPK/PP_2150/PP_2150-uniprot.txt
"Note=Magnesium. Can also use manganese."].

Asta retrieval was fast but did not find organism-specific PP_2150 experimental
papers; its useful signal was the same identifier/product/domain context from
the UniProt-seeded query [file:PSEPK/PP_2150/PP_2150-deep-research-asta.md
"- **Protein Description:** RecName: Full=FAD:protein FMN transferase";
file:PSEPK/PP_2150/PP_2150-deep-research-asta.md "- **Key Domains:** ApbE.
(IPR024932); ApbE-like_sf. (IPR003374); ApbE (PF02424)"].

Decision: accept `GO:7770036 flavin transferase activity` as the core
molecular function, modify the broad `GO:0016740 transferase activity` to that
specific term, keep metal-ion binding as non-core cofactor context, and accept
the generic plasma-membrane location. In module curation, PP_2150 should be
represented as related cell-envelope flavoprotein maturation/flavinylation
context near cytochrome-redox maturation, not as a CcmABCD heme-export subunit.
