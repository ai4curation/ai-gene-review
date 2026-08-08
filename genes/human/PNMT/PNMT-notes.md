# PNMT (P11086) — gene review notes

## Identity
- Human **PNMT** = **phenylethanolamine N-methyltransferase** (Short: PNMTase; AltName: Noradrenaline N-methyltransferase); synonym PENT. HGNC:9160, GeneID 5409, chromosome 17. UniProt **P11086**, 282 aa, ~30.9 kDa. [file:human/PNMT/PNMT-uniprot.txt "RecName: Full=Phenylethanolamine N-methyltransferase"]
- EC **2.1.1.28**. [file:human/PNMT/PNMT-uniprot.txt "EC=2.1.1.28"]

## Core molecular function
- SAM-dependent methyltransferase catalyzing **N-methylation of noradrenaline (norepinephrine) → adrenaline (epinephrine)**, S-adenosyl-L-methionine → S-adenosyl-L-homocysteine. [file:human/PNMT/PNMT-uniprot.txt "to form epinephrine (adrenaline), using S-adenosyl-L-"] [file:human/PNMT/PNMT-uniprot.txt "methionine as the methyl donor (PubMed:20496117). Other substrates"]
- **GO:0004603** phenylethanolamine N-methyltransferase activity — confirmed current & non-obsolete via OLS; def "S-adenosyl-L-methionine + phenylethanolamine = S-adenosyl-L-homocysteine + N-methylphenylethanolamine."
- Additional in vitro substrates: phenylethanolamine, octopamine (→ synephrine), normetanephrine (by similarity). [file:human/PNMT/PNMT-uniprot.txt "methionine as the methyl donor (PubMed:20496117). Other substrates"]
- Reactome: "It performs transmethylation of noradrenaline to adrenaline using S-adenosyl L-methionine (SAM) as the methyl donor." [Reactome:R-HSA-209903]

## Core biological process
- **GO:0042418** epinephrine biosynthetic process (specific core BP) — OLS current. UniPathway: "adrenaline from (R)-noradrenaline: step 1/1." [file:human/PNMT/PNMT-uniprot.txt "adrenaline from (R)-noradrenaline: step 1/1."]
- **GO:0042423** catecholamine biosynthetic process — correct parent BP; PNMT is the terminal of 4 enzymes (TH, AADC, DBH, PNMT). [Reactome:R-HSA-209905]

## Location
- **GO:0005829** cytosol — soluble cytoplasmic enzyme (Reactome TAS + IBA). OLS current.

## Family / structure
- Class I-like SAM-binding methyltransferase superfamily, NNMT/PNMT/TEMT family. [file:human/PNMT/PNMT-uniprot.txt "Belongs to the class I-like SAM-binding methyltransferase"]
- Extensively crystallized (>40 PDB entries, e.g. 1HNN, 4MIK) in complex with S-adenosyl-L-homocysteine and inhibitors; active-site residues Tyr35, Glu185, Glu219, Asp267 dissected by mutagenesis. [PMID:16363801 "reduced the kcat without affecting the Km"]

## Expression / regulation
- Predominant in adrenal medulla chromaffin cells; also retina and CNS adrenergic neurons; glucocorticoid-induced. Transgenic-mouse study: hPNMT expressed in "the adrenal gland and eye". [PMID:2835776 "the adrenal gland and eye"] [PMID:2835776 "for the conversion of norepinephrine to epinephrine"]
- HPA: "Tissue enhanced (adrenal gland, brain)". [file:human/PNMT/PNMT-uniprot.txt "HPA; ENSG00000141744; Tissue enhanced (adrenal gland, brain)."]

## Evidence used for annotation review
- **IDA** PMID:8812853: recombinant hPNMT purified to homogeneity, kinetics (Km phenylethanolamine 130 uM, SAM 16 uM). [PMID:8812853 "for phenylethanolamine and S-adenosyl-L-methionine were determined to be 130 and"]
- **EXP** PMID:16363801: crystal structures + mutagenesis (Glu185 catalysis). [PMID:16363801 "Here we report three crystal structure complexes of human phenylethanolamine"]
- **IMP** PMID:16277617: allozyme functional genomics; Asn9Ser, Thr98Ala, Arg112Cys, Ala175Thr; Ala98 lowers activity. [PMID:16277617 "N-methylation of norepinephrine to form epinephrine"] [PMID:16277617 "allozyme displayed significantly lower levels of both activity and"]
- **IMP** PMID:20496117: HPLC enzymatic assay in inhibitor discovery. [PMID:20496117 "An enzymatic activity assay"]
- **TAS** PMID:2835776, Reactome R-HSA-209903/209905.

## Curation decisions (summary)
- All GO:0004603 activity annotations (IBA, IEA GO_REF:0000120, TAS x2, EXP, IMP x2, IDA) → **ACCEPT** (core MF; experimental annotations retained per policy).
- GO:0008168 methyltransferase activity (IEA InterPro2GO) → **MODIFY** to GO:0004603 (over-general parent; specific child well supported).
- GO:0005515 protein binding (IPI, PMID:32296183 HuRI; partners LNX1/Q8TBB1, KLHL8/Q9P2G9-2) → **MARK_AS_OVER_ANNOTATED** (bare protein binding, high-throughput Y2H, no functional context; retained not removed per policy). Full text of PMID:32296183 does not name PNMT/LNX1/KLHL8 (large-scale dataset; pairs are in supplementary). Interactors sourced from GOA WITH/FROM + UniProt INTERACTION.
- GO:0042418 epinephrine biosynthetic process (IEA) → **ACCEPT** (specific core BP).
- GO:0042423 catecholamine biosynthetic process (TAS) → **ACCEPT** (correct parent BP).
- GO:0005829 cytosol (IBA is_active_in; TAS located_in) → **ACCEPT** (core CC).

## Term-id verification (OLS, non-obsolete)
- GO:0004603 MF phenylethanolamine N-methyltransferase activity ✓
- GO:0042418 BP epinephrine biosynthetic process ✓
- GO:0042423 BP catecholamine biosynthetic process ✓
- GO:0005829 CC cytosol ✓
