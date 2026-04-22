# Ndufb1 (Mouse) - Research Notes

## Gene Identity

- **Gene symbol**: Ndufb1
- **UniProt**: P0DN34 (NDUB1_MOUSE)
- **Aliases**: Complex I-MNLL, CI-MNLL, NADH-ubiquinone oxidoreductase MNLL subunit
- **Organism**: Mus musculus (Mouse), NCBITaxon:10090
- **Length**: 57 amino acids, 6954 Da
- **Chromosome**: 12

## Protein Overview

Ndufb1 encodes a small, single-pass transmembrane accessory subunit of mitochondrial NADH:ubiquinone oxidoreductase (Complex I). The protein has a transmembrane helix (residues 10-26) and a C-terminal matrix-exposed domain. It is one of the smallest subunits of Complex I and belongs to the NDUFB1/MNLL family (InterPro: IPR012575, Pfam: PF08040).

## Key Literature

### PMID:38575788 - Vercellino & Sazanov 2024, Nat Struct Mol Biol
"SCAF1 drives the compositional diversity of mammalian respirasomes."
- Cryo-EM structures of mouse mitochondrial supercomplexes at 3.6 A resolution
- Directly demonstrates Ndufb1 as part of Complex I in mouse tissue (heart mitochondria)
- Confirms subcellular location: mitochondrial inner membrane, matrix side
- Confirms subunit composition of Complex I (45 subunits)
- This is the primary IDA evidence for the mouse protein

### PMID:30030361 - Signes & Fernandez-Vizarra 2018, Essays Biochem
"Assembly of mammalian oxidative phosphorylation complexes I-V and supercomplexes."
- Review article covering assembly pathways of all five OXPHOS complexes
- Describes Complex I assembly as modular, with NDUFB1 being part of the ND4-module
- Cited by ComplexPortal for NAS annotations on aerobic respiration and proton motive force-driven ATP synthesis
- REAL reference, verified

### PMID:19468303 - Church et al. 2009, PLoS Biol
"Lineage-specific biology revealed by a finished genome assembly of the mouse."
- Mouse genome assembly paper (C57BL/6J strain)
- Provides the genomic sequence for Ndufb1
- Not directly relevant to protein function

### PMID:27626371 - Stroud et al. 2016, Nature
"Accessory subunits are integral for assembly and function of human mitochondrial complex I."
- Systematic CRISPR knockout study of all 31 accessory subunits in human cells
- NDUFB1 knockout was included; loss of accessory subunits generally leads to loss of Complex I activity
- Demonstrates that accessory subunits are essential for assembly and function

### PMID:27720676 - Guerrero-Castillo et al. 2017, Cell Metab
"The assembly pathway of mitochondrial respiratory chain complex I."
- Dynamic complexome profiling of Complex I assembly
- NDUFB1 is part of the ND4-module assembly intermediate along with NDUFB4, NDUFB5, NDUFB6, NDUFB10, NDUFB11

### Structure
- Multiple cryo-EM structures in PDB: 6G2J, 6ZTQ, 7B93, 8OM1 (highest resolution at 2.39 A), 8PW5, etc.
- Single transmembrane helix with matrix-exposed C-terminus
- Contacts core subunit ND4 and neighboring accessory subunits NDUFB4, NDUFB5, NDUFB8, NDUFB11

## Function Assessment

- **Molecular function**: Structural molecule activity (GO:0005198). As an accessory subunit, NDUFB1 does NOT independently catalyze any reaction. It contributes structurally to the complex-level NADH dehydrogenase (ubiquinone) activity (GO:0008137). This is a contributes_to relationship, not enables.
- **Biological process**: Involved in mitochondrial respiratory chain complex I assembly (GO:0032981) as part of the ND4-module. Also involved in aerobic respiration (GO:0009060) and mitochondrial electron transport, NADH to ubiquinone (GO:0006120) through its role as a Complex I subunit.
- **Cellular component**: Part of respiratory chain complex I (GO:0045271), located in mitochondrial inner membrane (GO:0005743), matrix side.

## BioReason Claims Assessment

The BioReason deep research file makes several claims that need verification:

1. **Claim**: "contribute to GO:0034551 mitochondrial respiratory chain complex III assembly"
   - **INCORRECT**: This is Complex III assembly, not Complex I. NDUFB1 is a Complex I subunit with no known role in Complex III assembly. The BioReason model appears to have confused "integrity of the III-I neighborhood" (supercomplex interactions) with Complex III assembly, which are fundamentally different processes. This is a hallucination.

2. **Claim**: "Binding to the mitochondrial acyl carrier protein suggests a role in stabilizing the ACP module"
   - **PARTIALLY CORRECT but overspecified**: NDUFAB1 (the acyl carrier protein) is a different Complex I subunit. NDUFB1 does not directly bind ACP. The BioReason model confused NDUFB1 with NDUFAB1 (note the similar names).

3. **Claim**: "Contacts with NDUFB11, NDUFB5, NDUFB10, and NDUFB4 indicate lateral packing"
   - **CORRECT**: These are verified neighboring subunits in the beta subcomplex based on structural data.

4. **Claim**: "associations with NDUFA1, NDUFA2, NDUFA6, NDUFA8, and C2"
   - **PARTIALLY CORRECT but overspecified**: Some of these contacts are correct from structural data, but the specific claim of direct contacts with all of these subunits is not well-supported for the tiny NDUFB1 subunit specifically.

5. **Claim about "quinone-access channel" stabilization**
   - **OVERSPECIFIED**: NDUFB1 is in the membrane arm near ND4, which is in the proton-pumping region, not adjacent to the quinone-access channel (which is near ND1).

## Nuclear Speck Annotation (GO:0016607)
The ISO annotation for nuclear speck is transferred from human O75438. This is a questionable annotation for a mitochondrial inner membrane protein. It may derive from a high-throughput localization study with false positives, or from the small protein being detected in nuclear fractions. This should be treated skeptically.
