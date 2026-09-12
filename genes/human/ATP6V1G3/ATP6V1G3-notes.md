# ATP6V1G3 (V-type proton ATPase subunit G 3) — Gene Review Notes

## Identity and overview

- UniProt: Q96LB4 (VATG3_HUMAN), 118 aa, ~13.9 kDa.
- HGNC:18265, gene ID 127124, chromosome 1.
- One of three human paralogs of the V-ATPase V1 "G" subunit (G1/ATP6V1G1, G2/ATP6V1G2, G3/ATP6V1G3).
- G3 is the kidney-specific/kidney-enriched isoform [PMID:12384298 "TISSUE SPECIFICITY: Kidney"] [file:human/ATP6V1G3/ATP6V1G3-uniprot.txt "TISSUE SPECIFICITY: Kidney. {ECO:0000269|PubMed:12384298}"]; HPA reports "Tissue enriched (kidney)".

## Function

- Subunit of the V1 peripheral (cytosolic) complex of the vacuolar H+-ATPase (V-ATPase). The V-ATPase couples ATP hydrolysis (V1) to proton translocation across membranes (V0), acidifying intracellular compartments and, in some cell types, the extracellular space [file:human/ATP6V1G3/ATP6V1G3-uniprot.txt "Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase)... a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons"].
- The G subunit is part of the peripheral stalk (stator). Each of the three peripheral stalks consists of an E-G heterodimer; the G subunit partners with subunit E [file:human/ATP6V1G3/ATP6V1G3-uniprot.txt "three peripheral stalks each consisting of EG heterodimers"].
- Belongs to the V-ATPase G subunit family [file:human/ATP6V1G3/ATP6V1G3-uniprot.txt "Belongs to the V-ATPase G subunit family"].
- Structurally: coiled-coil (residues 5-54), N-terminal disordered region (1-34); consistent with an elongated stalk subunit.

## Tissue-specific V-ATPase in kidney / inner ear

- The H+-ATPases in inner ear and acid-handling cells of the renal collecting duct contain tissue-specific subunits a4 (ATP6V0A4) and B1 (ATP6V1B1), and in kidney additionally C2, d2, and G3, replacing the ubiquitous forms [PMID:17360703 "they contain tissue-specific subunits, such as a4 and B1, and in the kidney, C2, d2, and G3 as well. These subunits replace the ubiquitously expressed forms"].
- G3 expression is limited to the kidney among major organs of mouse and man; additionally detected in human inner ear epithelial fragments [PMID:17360703 "G3 subunit expression is limited to the kidney... demonstrated additional G3 expression in epithelial fragments from human inner ear"].
- Tissue-specific renal V-ATPase mediates apical proton secretion in intercalated cells of the collecting duct (acid-base homeostasis); mutations in the related tissue-specific subunits ATP6V0A4 (a4) and ATP6V1B1 (B1) cause autosomal recessive distal renal tubular acidosis. The original cloning paper evaluated G3 (and C2, d) for involvement in dRTA [PMID:12384298].

## Key interaction: G3 links V1 to V0 via subunit a

- Phage display + ELISA and pull-down with immobilized full-length G3 identified and verified an interaction between the G3 subunit and the a4 (ATP6V0A4) subunit, pulling a4 down from human kidney membrane preparations [PMID:17360703 "identified a possible interaction between the G3 subunit and the a4 subunit... purified, immobilized full-length G3 to pull down the a4 subunit from human kidney membrane preparations. This confirms that a4 and G3 are component subunits of the same proton pump"].
- The G/a interaction is a more general feature: G1/a1, G3/a1, and G1/a4 interactions were also demonstrated [PMID:17360703 "similar G1/a1, G3/a1, and G1/a4 interactions were also demonstrated"].
- This G-a interaction is a novel link between the V1 and V0 domains, required for H+-ATPase assembly and regulation [PMID:17360703 "a novel link between the V(1) and V(0) domains in man, which is known to be required for H(+)-ATPase assembly and regulation"].
- IPI evidence (GOA) for "ATPase binding" (GO:0051117) is from PMID:17360703 with WITH/FROM UniProtKB:Q93050 (ATP6V0A1, a1) and UniProtKB:Q9HBG4 (ATP6V0A4, a4).
- The same paper provided the IDA cytosol (GO:0005829) and plasma membrane (GO:0005886) localizations for G3 in kidney (PMID:17360703).

## Annotation assessment summary

- Core, accept: V1 domain membership (GO:0000221), V-ATPase complex membership (GO:0016471), rotational-mechanism proton-transporting ATPase activity (GO:0046961, contributes_to semantics), proton transmembrane transport (GO:1902600), plasma membrane localization (GO:0005886, kidney apical — IDA experimental + IEA). ATPase binding (GO:0051117) accepted because the underlying interaction (G3-a4/a1) is specific and experimentally demonstrated, not generic "protein binding".
- Synaptic vesicle annotations (GO:0030672 synaptic vesicle membrane, GO:0097401 synaptic vesicle lumen acidification) are IBA phylogenetic transfers reflecting the neuronal V-ATPase context of orthologs/paralogs; for the kidney-specific G3 these are non-core → KEEP_AS_NON_CORE.
- Cytosol (GO:0005829): real disassembled/free-V1 state but non-core; many Reactome TAS duplicates and one IEA/IDA → KEEP_AS_NON_CORE (IDA from PMID:17360703 accepted as experimentally observed but still non-core localization).
- No bare "protein binding" (GO:0005515) annotation present; no exosome HDA annotation present.

## Paralogs / WITH-FROM identities verified

- Q93050 = ATP6V0A1 (V0 subunit a1).
- Q9HBG4 = ATP6V0A4 (V0 subunit a4, kidney).
- O75348 = ATP6V1G1 (G1, ubiquitous paralog).
