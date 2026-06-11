# TXNDC11 (Q6PKC3) review notes

## Identity
- Thioredoxin domain-containing protein 11; synonym EFP1 (EF-hand-binding protein 1). HGNC:28030. 985 aa.
- Type II single-pass ER membrane protein with five thioredoxin (Trx)-like domains and a C-terminal coiled coil. N-glycosylated ER glycoprotein.
- UniProt: "Belongs to the protein disulfide isomerase family." TRANSMEM 65..85; Thioredoxin domains 92..214 and 649..799; COILED 821..919.
- Redox-active disulfides annotated at 469..472 and 719..722 (PROSITE-predicted CXXC).

## Two distinct functional storylines

### 1. Legacy / UniProt: EFP1 partner of DUOX (thyroid H2O2 system)
- Discovered as a DUOX-interacting thioredoxin-related protein [PMID:15561711 "Identification of a novel partner of duox: EFP1, a thioredoxin-related protein."].
- UniProt FUNCTION: "May act as a redox regulator involved in DUOX proteins folding. The interaction with DUOX1 and DUOX2 suggest that it belongs to a multiprotein complex constituting the thyroid H(2)O(2) generating system. It is however not sufficient to assist DUOX1 and DUOX2 in H(2)O(2) generation."
- UniProt SUBUNIT: "Interacts with the cytoplasmic part of DUOX1 and DUOX2. Interacts with TPO and CYBA."
- This is the basis for the Reactome "Thyroxine biosynthesis" (R-HSA-209968) pathway mapping and the plasma-membrane TAS annotations (thyroid follicular apical membrane / DUOX context). Tissue specificity: "Expressed at higher level in thyroid and prostate."
- NOTE: this function is "May act" / suggestive; the protein is NOT sufficient for H2O2 generation. The plasma membrane localization is a downstream Reactome reaction-context inference, not a primary localization claim; UniProt's own SUBCELLULAR LOCATION is "Endoplasmic reticulum membrane; Single-pass membrane protein."

### 2. Current consensus: EDEM2 partner in glycoprotein ERAD (gpERAD)
The well-established molecular function (not yet in this UniProt FUNCTION block):
- TXNDC11 is stably disulfide-bonded to EDEM2 and this complex catalyzes the FIRST mannose-trimming step (M9 -> M8B) that initiates gpERAD.
- George et al. 2020 eLife [PMID:32065582, DOI:10.7554/eLife.53455]:
  - Abstract: "we found that EDEM2 was stably disulfide-bonded to TXNDC11, an endoplasmic reticulum protein containing five thioredoxin (Trx)-like domains. C558 present outside of the mannosidase homology domain of EDEM2 was linked to C692 in Trx5, which solely contains the CXXC motif in TXNDC11. This covalent bonding was essential for mannose trimming and subsequent gpERAD in HCT116 cells."
  - "EDEM2-TXNDC11 complex purified from transfected HCT116 cells converted ManGlcNAc to ManGlcNAc (isomerB) in vitro."
  - Text: "TXNDC11 ... was shown to be N-glycosylated, localized in the ER and required for gpERAD of various substrates, including CD3δ, TCRα and NHK ... but not for NHK-QQQ, a non-glycosylated version of NHK."
  - Text: "TXNDC11 in the gpERAD assay was inactivated by the double mutation of Cys692 and Cys695 in the CxxC motif of the Trx5 domain ... The Trx5 domain expressed and purified from cells exhibited reductase activity in vitro."
  - Text: "C558 of EDEM2 may be disulfide-bonded to C488 ... by the action of PDI and then reduced by the Trx5 domain of TXNDC11" — TXNDC11 acts as a REDUCTASE (reduction potential), not oxidase.
  - "only one cysteine residue of the CXXC motif (C692) of TXNDC11 is used for such covalent bonding. This can be explained by the finding that the C692-containing Trx5 domain of TXNDC11 ... exhibited reduction potential as a reductase rather than an oxidase."
- Shenkman et al. 2018 Commun Biol [PMID:30374462, DOI:10.1038/s42003-018-0174-8]: "The EDEMs associate with oxidoreductases, protein disulfide isomerase, and especially TXNDC11, enhancing mannosidase activity on glycoproteins but not on free N-glycans."
- George et al. 2021 eLife [PMID:34698634, DOI:10.7554/eLife.70357] recap: "We previously showed that EDEM2 stably disulfide-bonded to the thioredoxin domain-containing protein TXNDC11 is responsible for the first step."

So the core MF is best described as protein-disulfide reductase / thiol-disulfide oxidoreductase activity (the catalytically active CXXC is in Trx5 / C692-C695). TXNDC11 functions as an oxidoreductase chaperone partner whose redox activity supports EDEM2-mediated mannose trimming in gpERAD. BP = ER-associated misfolded glycoprotein catabolism (ERAD) / glycoprotein ERAD pathway. CC = ER membrane (lumen-facing Trx domains).

## Redox motifs / catalytic status
- TXNDC11 has five Trx-like domains but only ONE bona fide CXXC motif (Trx5, C692-x-x-C695) that is catalytically redox-active; Trx1 has a CXXS (C137) variant that is NOT required for gpERAD ("not by the mutation of Cys137 in the CxxS motif of the Trx1 domain"). So most Trx domains are redox-inactive/pseudo; the functional redox center is Trx5.
- Therefore the redox-active disulfide UniProt features (469..472, 719..722) are predicted; the experimentally validated functional CXXC is C692/C695 (Trx5, part of the 719..722-numbered redox feature region by domain count). The protein is a reductase, not an oxidase.

## GOA annotation assessment
- GO:0005789 ER membrane (IEA, SubCell) — ACCEPT (primary localization; UniProt SUBCELLULAR LOCATION).
- GO:0005515 protein binding x4 (IPI; HTT/PMID:17500595, HCV NS5A xeno/PMID:18985028, binary interactome partners/PMID:32296183, neurodegeneration interactome/PMID:32814053) — all HT interactome captures, uninformative; KEEP_AS_NON_CORE. None capture the functional EDEM2 or DUOX partnerships.
- GO:0005829 cytosol (IDA, HPA) — questionable; TXNDC11 is an ER membrane/luminal protein. HPA IF can show ER/reticular staining scored loosely. KEEP_AS_NON_CORE / not core (do not REMOVE an IDA on weak grounds; flag uncertainty).
- GO:0005886 plasma membrane (IDA HPA + 6x Reactome TAS thyroxine biosynthesis) — derives from the EFP1/DUOX thyroid-system role and thyroid apical membrane reaction context. Not the protein's primary/ER localization. KEEP_AS_NON_CORE (real but peripheral; legacy thyroid context).

## Missing annotations worth proposing
- Molecular function: protein-disulfide reductase activity / thiol-disulfide exchange (GO:0015035 protein-disulfide reductase activity or GO:0003756 PDI activity). The CXXC is a reductase.
- BP: ERAD pathway / ER-associated misfolded glycoprotein catabolic process (GO:1904153 or GO:0036503), specifically the glycoprotein mannose-trimming initiation.
- These are strongly supported by PMID:32065582 but are NOT currently in GOA — propose as NEW.
</content>
