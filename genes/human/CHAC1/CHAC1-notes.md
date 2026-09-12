# CHAC1 review notes

UniProt: Q9BUX1 (CHAC1_HUMAN). Gene: CHAC1 (HGNC:28680). 222 aa. EC 4.3.2.7. Chr 15.

## Identity and core enzymology

CHAC1 = Glutathione-specific gamma-glutamylcyclotransferase 1 ("Gamma-GCG 1"); ChaC subfamily of the
gamma-glutamylcyclotransferase (GGCT-like) family. Also historically named "Botch" (Blocks Notch) and
"cation transport regulator-like protein 1" (from the bacterial *cha* operon homology, which is not a
conserved function in mammals).

Catalytic activity (UniProt CATALYTIC ACTIVITY):
[file:human/CHAC1/CHAC1-uniprot.txt "Reaction=glutathione = L-cysteinylglycine + 5-oxo-L-proline"]
(Rhea:RHEA:47724; EC=4.3.2.7). It performs the committed, intracellular (cytosolic) step of a dedicated
glutathione (GSH) degradation route, distinct from the extracellular GGT1 route.

Substrate specificity — GSH only, not other gamma-glutamyl peptides:
[file:human/CHAC1/CHAC1-uniprot.txt "Acts specifically on glutathione, but not on"] "other gamma-glutamyl peptides".
The kinetics paper reports human ChaC1 Km = 2.2 mM and kcat = 225.2 min-1 for glutathione, ~10-20x more
catalytically efficient than the constitutive paralog ChaC2, and both are specific for **reduced** GSH
with no activity on gamma-glutamyl amino acids or oxidized glutathione
[PMID:27913623 "Km of 2.2 ± 0.4 mm and kcat of 225.2 ± 15 min-1 toward glutathione for human ChaC1"]
[PMID:27913623 "shared the same specificity for \nreduced glutathione, with no activity against either γ-glutamyl amino acids or \noxidized glutathione"].
Note: PMID:27913623 is abstract-only in cache (full_text_available: false), but the abstract itself
reports the human ChaC1 kinetic constants and specificity, matching the UniProt CATALYTIC ACTIVITY and
BIOPHYSICOCHEMICAL PROPERTIES blocks (Km 2.2 mM, kcat 225.2). GOA also has an IDA (FlyBase-assigned) to
the same term from this paper.

## Subcellular location

Cytosol (experimentally, human): CHAC1-V5eGFP fractionated to the cytosolic compartment and gave diffuse
cytoplasmic staining
[PMID:19109178 "CHAC1 was primarily localized in the cytosolic compartment compared with the nucleus or pellet fractions"].
UniProt: [file:human/CHAC1/CHAC1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"].
A second, trans-Golgi-network location is annotated only by similarity to the mouse ortholog Botch
(Q8R3J5) and comes from the Notch-regulation work; it is ISS/IEA on human, not experimentally shown for
human CHAC1. [file:human/CHAC1/CHAC1-uniprot.txt "Golgi apparatus, trans-Golgi network"] carries
ECO:0000250 (by similarity to Q8R3J5).

## Integrated stress response / UPR induction and pro-apoptotic role

CHAC1 is a transcriptional target of the ATF4-ATF3-CHOP arm of the UPR/integrated stress response and is
strongly induced by ER-stress chemicals:
[PMID:19109178 "CHAC1 mRNA was robustly induced in HAEC and in HEK and HeLa cells following treatments that induce the UPR (tunicamycin, DTT, or thapsigargin) but not with general cell stressors"]
[PMID:19109178 "CHAC1 is indeed a component of the UPR and that it lies downstream of the ATF4-ATF3-CHOP pathway"].
UniProt INDUCTION: [file:human/CHAC1/CHAC1-uniprot.txt "Induced by chemical activators of the unfolded protein"] "response (UPR) such as tunicamycin, DTT and thapsigargin."
CHAC1 is pro-apoptotic: overexpression promotes and knockdown blocks apoptosis markers
[PMID:19109178 "CHAC1 expression as necessary and sufficient to induce well-characterized markers of apoptosis, TUNEL, cPARP, and AIF nuclear translocation"].
This underpins the GOA IMP to GO:0070059 (intrinsic apoptotic signaling pathway in response to ER stress).
Mechanistically the enzymatic GSH-depleting activity plausibly links CHAC1 to apoptosis and to
ferroptosis (GSH depletion sensitizes to ferroptosis), though the ferroptosis link is not directly in the
cited local files.

## Notch regulation ("Botch")

Reported (chiefly in mouse/rat, PMID:22445366) as a negative regulator of Notch during embryonic
neurogenesis. Botch binds the Notch1 extracellular region and blocks the S1 furin cleavage that matures
Notch, keeping Notch in its immature inactive full-length form, thereby de-repressing neuronal
differentiation:
[PMID:22445366 "Botch prevents cell surface presentation of Notch by "] "inhibiting the S1 furin-like cleavage of Notch"
[PMID:22445366 "Botch blocks furin cleavage in a manner similar to the furin inhibitor, DEC-RVKR-CMK"]
[PMID:22445366 "Co-immunoprecipitation experiments show Botch interacts with the extracellular domain of Notch1 (NECD1)"]
[PMID:22445366 "Botch regulates neurogenesis by promoting "] "neuronal differentiation".
Localizes partly to the trans-Golgi (where furin S1 cleavage of Notch occurs):
[PMID:22445366 "trans-Golgi marker (TGN38) but not the cis-Golgi marker (GM130), indicating that in the Golgi, Botch resides in the trans-Golgi (Figure 1F)"].
IMPORTANT: PMID:22445366 is largely a mouse Botch (NPG7) study; the human GOA IMP annotations
(GO:0010955, GO:0045746) are transferred from it. The human trans-Golgi / Notch binding / neurogenesis
terms are ISS/IEA by similarity to mouse Q8R3J5. These are real but non-core (moonlighting/secondary)
relative to CHAC1's core enzymatic GSH-catabolic function; keep as non-core rather than remove, since the
IMP experimental annotations should not be removed per policy.

## Protein interactions

GOA IPI GO:0005515 "protein binding" from PMID:16189514 (Rual et al., high-throughput Y2H human
interactome) — interaction partner RHOXF2 (Q9BQY4) per UniProt INTERACTION block
[file:human/CHAC1/CHAC1-uniprot.txt "Q9BUX1; Q9BQY4: RHOXF2; NbExp=2"]. This is a bare, uninformative
"protein binding" term from a large-scale screen; mark as over-annotated (do not remove IPI per policy).

## Paralog note

CHAC2 (Q8WUX2) is the constitutive, slow-turnover cytosolic GSH-degrading paralog (~50% identity);
PMID:27913623 characterizes ChaC2 but reports ChaC1 kinetics in parallel. Keep the review focused on
CHAC1 (the tightly ATF4/UPR-regulated, high-activity member).

## Annotation-action summary

- Core MF: GO:0061928 glutathione specific gamma-glutamylcyclotransferase activity (verified current, OLS).
- Core BP: GO:0006751 glutathione catabolic process (verified current, OLS).
- Core CC: GO:0005829 cytosol (experimental IDA, PMID:19109178).
- Notch/neurogenesis + trans-Golgi terms: KEEP_AS_NON_CORE (IMP experimental) or MARK_AS_OVER_ANNOTATED
  (ISS/IEA transfers of a mouse-specific moonlighting function).
- Bare "protein binding" IPI: MARK_AS_OVER_ANNOTATED.
- Golgi apparatus IEA (GO:0005794) from SubCell mapping: over-broad parent of TGN; MARK_AS_OVER_ANNOTATED.
</content>
