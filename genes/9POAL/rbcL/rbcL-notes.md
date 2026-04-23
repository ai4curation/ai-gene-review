# rbcL Notes - Ribulose bisphosphate carboxylase large chain (RuBisCO large subunit)

## Gene Overview

rbcL encodes the large subunit of ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO, EC 4.1.1.39), 
the most abundant protein on Earth and the key enzyme in photosynthetic carbon fixation. The gene is 
chloroplast-encoded in land plants. This review uses the rice (Oryza sativa subsp. japonica) entry P0C512 
as a representative for Poales (9POAL).

## Key Functions

### 1. Carbon Fixation (Carboxylase Activity)
RuBisCO catalyzes the primary carbon fixation reaction in the Calvin-Benson-Bassham cycle (reductive 
pentose-phosphate cycle): fixation of atmospheric CO2 onto ribulose-1,5-bisphosphate (RuBP) to produce 
two molecules of 3-phosphoglycerate (3-PGA) [PMID:22609438 "RuBisCO catalyzes two reactions: the 
carboxylation of D-ribulose 1,5-bisphosphate, the primary event in carbon dioxide fixation"].

### 2. Oxygenase Activity (Photorespiration)
RuBisCO also catalyzes an oxygenase reaction where O2 competes with CO2 at the same active site, 
cleaving RuBP into 2-phosphoglycolate and 3-PGA. This initiates the photorespiratory pathway 
[UniProt P0C512: "the oxidative fragmentation of the pentose substrate in the photorespiration process. 
Both reactions occur simultaneously and in competition at the same active site"].

### 3. Enzyme Structure
- Form I RuBisCO: heterohexadecamer (L8S8) - 8 large subunits (rbcL) and 8 small subunits (rbcS)
- Large subunit homodimer is the basic functional unit arranged head-to-tail
- Four L2 dimers form a barrel-like tetramer, capped by S4 tetramers [PMID:22609438]

### 4. Cofactor Requirements
- Requires Mg2+ (1 per subunit) for catalysis [PMID:22609438]
- Activation by carbamylation of Lys-201 (formation of N6-carboxylysine) [PMID:22609438]
- NADPH and 6-phosphogluconate act as positive effectors promoting activation [PMID:22609438]

### 5. Subcellular Localization
- Chloroplast stroma (soluble enzyme in the chloroplast stroma)
- Gene is chloroplast-encoded (plastid genome)

## Key References

- PMID:22609438 - Crystal structure of rice RuBisCO at 1.35 A resolution; activation by NADPH and 
  6-phosphogluconate; Mg2+ binding; subunit structure [Matsumura et al. 2012, J Mol Biol]
- PMID:2770692 - Complete rice chloroplast genome sequence [Hiratsuka et al. 1989]
- PMID:15122023 - Rice chloroplast genome comparison [Tang et al. 2004]
- PMID:16758443 - Proteomic identification of rbcL in rice tissues [Nozu et al. 2006]

## Annotation Notes

### Monooxygenase activity (GO:0004497)
UniProt annotates rbcL with "monooxygenase activity" (GO:0004497) via the KW "Monooxygenase". However, 
RuBisCO's oxygenase reaction does NOT fit the GO definition of monooxygenase activity ("incorporation of 
one atom of molecular oxygen into the substrate and reduction of the other atom to water"). RuBisCO's 
oxygenase reaction cleaves RuBP using O2, producing 2-phosphoglycolate + 3-PGA + 2H+. This is mechanistically 
distinct from a monooxygenase. The monooxygenase annotation appears questionable/over-annotated.

### Nucleotide binding (GO:0000166)
UniProt also has "nucleotide binding" from the KW "Nucleotide-binding". This relates to NADP binding 
(positive effector), but nucleotide binding is very generic. A more specific term would be appropriate 
if annotating this function.

### Carbon fixation vs reductive pentose-phosphate cycle
Both GO:0015977 (carbon fixation) and GO:0019253 (reductive pentose-phosphate cycle) are annotated. 
Carbon fixation is a broader parent term. The reductive pentose-phosphate cycle (Calvin cycle) is more 
specific and represents the core pathway. Both are appropriate - carbon fixation as the high-level 
function, and the Calvin cycle as the specific pathway context.

### Plastid vs chloroplast redundancy
GO:0009536 (plastid) and GO:0009507 (chloroplast) are both annotated. Chloroplast is a subtype of 
plastid. Having both is somewhat redundant; chloroplast is more specific and informative. The plastid 
annotation could be considered redundant but is not incorrect.
