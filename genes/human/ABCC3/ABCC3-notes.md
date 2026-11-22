# ABCC3 (MRP3 / MOAT-D) — curation notes

## Identity and architecture
- UniProt O15438, HGNC:54, gene *ABCC3*; synonyms MRP3, MOAT-D, cMOAT2, MLP2 (MMADHC-unrelated). 1527 aa, ~169 kDa, N-glycosylated.
- ABC transporter superfamily, ABCC (MRP) family, conjugate-transporter subfamily (TC 3.A.1.208.9). Closest human homolog is MRP1/ABCC1 (~58% identity); also related to MRP2/ABCC2 (~48%) [PMID:9827529 "MOAT-D is predicted to encode a 1527-amino-acid protein that is the closest known relative of MRP (about 58% identity)."].
- Domain layout like MRP1/MRP2: an N-terminal membrane-spanning extension (TMD0, ~5 extra TM helices) plus the core 2×(TMD+NBD) MDR1-like unit [PMID:10359813 full text].
- Cryo-EM structures (PDB 8HVH/8HW2/8HW4/8IZP) resolve an amphiphilic substrate pocket accommodating steroid glucuronides and sulfates (UniProt RN [24], PMID:37485728; not cached).

## Molecular function — ATP-driven efflux of organic-anion conjugates
- Primary active transporter: two NBDs bind and hydrolyze ATP to power transport. Purified protein shows substrate-dependent ATPase activity and, reconstituted into proteoliposomes, transports MTX and LTC4 with positive cooperativity [PMID:19334674 "ABCC3-dependent uptake of the anticancer drug methotrexate (MTX), as well as the physiological substrate leukotriene C(4) (LTC(4))."; "revealing positive allosteric cooperativity for ABCC3-mediated substrate translocation."].
- Organic anion / multidrug transporter [PMID:10359813 "MRP3 is an organic anion and multidrug transporter, like the GS-X pumps MRP1 and MRP2."]. EC 7.6.2.2 (xenobiotic) and EC 7.6.2.3 (glutathione S-conjugate) assigned with experimental evidence (UniProt).
- **Glucuronides** (core cargo): estradiol-17-glucuronide, estrone/estriol/testosterone/DHT glucuronides, bilirubin mono- and bis-glucuronides, xenobiotic glucuronides (etoposide glucuronide, acetaminophen glucuronide) [PMID:11581266 "Membrane vesicles from infected insect cells expressing MRP3 mediated ATP-dependent transport of estradiol 17-beta-D-glucuronide, leukotriene C(4), dinitrophenyl S-glutathione but not glutathione itself, and etoposide glucuronide"; PMID:15083066 "We identified monoglucuronosyl bilirubin, bisglucuronosyl bilirubin and leukotriene C4 as substrates for both MRP3 and MRP3-ArgHis."].
- **Glutathione S-conjugates**: DNP-GS and LTC4, but NOT free glutathione (distinguishes it from MRP1/MRP2 GS-X pumps) [PMID:10359813 "Neither 2008 cells nor Madin-Darby canine kidney II cells overexpressing MRP3 showed an increase in glutathione export or a decrease in the level of intracellular glutathione, in contrast to cells overexpressing MRP1 or MRP2."].
- **Steroid sulfates**: DHEA-3-sulfate and androgen sulfates (androsterone, testosterone-sulfate); inactive toward estrone-3-sulfate (UniProt FUNCTION; PMID:15083066 "Dehydroepiandrosterone-3-sulphate and 17beta-glucuronosyl oestradiol were transported with similar kinetics by MRP3 and MRP3-ArgHis.").
- **Bile acids/salts**: taurocholate, glycocholate, taurolithocholate-3-sulfate — transported, but weakly; "does not contribute substantially to bile acids physiology, but provides an alternative route for the export of bile acids and glucuronate conjugates from cholestatic hepatocytes" (UniProt, By similarity to rat O88563). Treated here as a **non-core** activity.
- **Drugs / MDR**: confers low-level resistance to etoposide and teniposide and high (short-exposure) resistance to methotrexate by reducing intracellular accumulation [PMID:11581266 "Stable clones overproducing MRP3 were resistant to the epipodophyllotoxins etoposide and teniposide"; PMID:10359813 "MRP3 also confers high-level resistance to methotrexate"]. Fexofenadine is an ABCC3 substrate effluxed sinusoidally [PMID:18245269 "ATP-dependent transport of FEX was observed in hMRP3-enriched membrane vesicles but not hMRP4."].

## Localization — basolateral / basal plasma membrane
- Basolateral membrane of hepatocytes (cholangiocytes and periportal hepatocytes), by double-label immunofluorescence [PMID:10094960 "localized it to the basolateral membrane domain of hepatocytes"]; strongly upregulated there in MRP2-deficient Dubin–Johnson patients [PMID:10094960 "A particularly strong expression of the MRP3 protein was observed in the basolateral hepatocyte membrane of two patients with Dubin-Johnson syndrome who are deficient in MRP2."].
- Basolateral in polarized MDCKII cells [PMID:10359813 "MRP3 routes to the basolateral membrane and mediates transport of the organic anion"]; WT and R1297H variant basolateral [PMID:15083066 "MRP3-ArgHis was correctly localized to the basolateral membrane of polarized MDCKII cells."].
- Basolateral in human jejunum enterocytes (targeted proteomics) [PMID:28408210 "the known basolateral proteins ABCC3 and Na/K-ATPase"].
- Basal membrane of Sertoli cells and peritubular myoid cells in testis (blood-testis barrier) [PMID:35307651 "the localization of MRP3, MRP6, and MRP7 to the basal membrane of SCs and the PMCs are the first to be identified here"].
- Tissue: mainly liver; also intestine/colon, prostate, testis, brain, lower in kidney (UniProt). Induced under cholestasis / MRP2 deficiency.

## Curation decisions of note
- **Plasma membrane / membrane (GO:0005886, GO:0016020) → MODIFY to basolateral plasma membrane (GO:0016323).** Correct but general; the gene already carries the specific, well-supported basolateral term. (GO:0016323 itself is ACCEPT, as is basal plasma membrane GO:0009925 in testis.)
- **Xenobiotic metabolic process (GO:0006805) → MODIFY to xenobiotic transport (GO:0042908).** ABCC3 transports but does not metabolize xenobiotics; it supplies the efflux step of ADME pathways (aspirin/paracetamol Reactome TAS).
- **Carboxylic acid transport (GO:0046942, ARBA IEA) → MODIFY to bile acid and bile salt transport (GO:0015721).** Broad; its meaningful carboxylate cargo are bile acids.
- **transmembrane transporter activity (GO:0022857) → TOO_GENERAL**, entailed by accepted ABC-type xenobiotic/GS-conjugate/glucuronoside transporter activities. ABC-type transporter activity (GO:0140359), ATPase-coupled transmembrane transporter activity (GO:0042626) and transmembrane transport (GO:0055085) kept as ACCEPT (informative mechanistic class / conserved phylogenetic process).
- **Bile acid transport (MF GO:0015432, BP GO:0015721) → KEEP_AS_NON_CORE.** Genuine but secondary/alternative-route activity per UniProt.
- **transport across blood-brain barrier (GO:0150104, NAS ×2) → MARK_AS_OVER_ANNOTATED.** Both cited papers (PMID:26590417, PMID:30280653) are general BBB reviews that do **not** mention ABCC3; no functional evidence places ABCC3 at the BBB. (These full texts were checked — `full_text_available: true` — and neither discusses the gene.)
- **Abstract-only experimental rows** (PMID:9827529, 11581266, 15083066, 18698235, 18245269, 19334674, 10094960 are cached as `full_text_available: false`; abstracts suffice to confirm the functions). Per policy, experimental (EXP/IDA/IMP) annotations were not overruled on abstract text alone; PMID:9827529 EXP catalytic rows retained deferring to UniProt's ECO:0000269 attribution.
- No bare `GO:0005515` protein binding present; no REMOVE or UNDECIDED required (all cited publications accessible).

## Core functions (see YAML)
1. Glucuronoside efflux — GO:0015164 at basolateral plasma membrane.
2. Glutathione S-conjugate / LTC4 efflux — GO:0015431 at basolateral plasma membrane.
3. Xenobiotic/drug-conjugate efflux and multidrug resistance — GO:0008559 at basolateral plasma membrane.


## Generic CC/MF term convention (batch-2 review, 2026-11-11)
Applied consistently across ABCA8/ABCC1/ABCC3/ABCC4: GO:0016020 membrane -> MODIFY to GO:0005886 plasma membrane (paradigm MODIFY case); GO:0022857 transmembrane transporter activity -> TOO_GENERAL (entailed by the specific accepted transporter activities); GO:0005886 plasma membrane -> ACCEPT (the generic PM term is informative, and apical/basolateral sidedness is carried by the gene's own GO:0016324/GO:0016323 rows, not by blanket-MODIFYing the PM parent to a sub-domain).
This gene: reverted its 9 GO:0005886 rows from MODIFY->GO:0016323 back to ACCEPT (basolateral sidedness remains on the gene's distinct GO:0016323 rows).
