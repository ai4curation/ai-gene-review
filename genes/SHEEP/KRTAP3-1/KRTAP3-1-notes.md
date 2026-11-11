# KRTAP3-1 (SHEEP) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- KRTAP3-1 protein (P02446, PE 1) was sequenced from wool; UniProt cites Elleman 1972 (PMID:4678578) whose title names SCMK-B2C, but UniProt attributes residues 2-98 of KRTAP3-1 to it; the abstract states only that a high-sulfur wool protein was sequenced. The review (PMID:27240405) notes no variation has been found in ovine KRTAP3-1 [PMID:27240405 "In the KAP3 family, variation has only been revealed in KRTAP3-2"].

- [PMID:4678578 "The amino acid sequence of a protein from the reduced and carboxymethylated high-sulphur fraction of wool has been determined."]
- [PMID:27240405 "BIIIB2 or KAP3-1"]
- [PMID:27240405 "The HS-KAPs (KAP1, KAP2 and KAP3) are initially expressed in the orthocortical cells, but soon after this are expressed in all cortical cells"]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). ND root and IEA structural molecule activity rows refined to it.
- CC: GO:0045095 keratin filament (ACCEPT/NEW/MODIFY of ND root).
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- ARBA cytosol: KEEP_AS_NON_CORE, harmonized with the human KRTAP reviews (KAPs are synthesized in the cytoplasm of the keratinizing cell but act in the keratin matrix; true but not the site of function).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.

## OpenScientist report (integrated)

`KRTAP3-1-deep-research-openscientist.md` used as leads. Verified against cached abstracts:
- HS proteins are matrix proteins of wool cortical cells and vary between breeds [PMID:12362341 "High sulphur proteins (HSPs) form part of the matrix surrounding the intermediate filaments in the cortical cells of the wool fibre."]
- HS proteins first appear on the paracortical side [PMID:17697142 "sulphur-rich proteins are initially expressed on the paracortical side of the fibre"]
- Paralogue KRTAP3-2 is anagen-associated in wool follicles [PMID:10594723 "and Dsg1 both play structural roles in hair follicles."] (not used in the YAML; paralogue evidence).
Caution: the report equates KRTAP3-1 with SCMK-B2C following UniProt's citation of PMID:4678578; the 2016 review maps B2C to KAP1-3 (PMID:27240405), so the Elleman paper may describe a KAP1 protein. UniProt still attributes the 2-98 sequence to it; the review YAML only uses the abstract sentence that a wool high-sulfur protein was sequenced.
Not re-run: report's composition (16.3% Cys) and cysteine-position analysis.
