# NPR1 (P93002) Review Notes

## Gene Overview
NPR1 is a master transcriptional regulator of systemic acquired resistance (SAR) in Arabidopsis. It functions as a salicylic acid (SA)-binding transcription cofactor.

## Key Functional Evidence

### Molecular Function - CORE
1. **Transcription coregulator activity** (GO:0003712) - Well-supported by multiple IDA/IMP studies [PMID:26269953, PMID:35545668]. NPR1 bridges TGA transcription factors to activate defense genes.

2. **Salicylic acid binding** (GO:1901149) - Direct biochemical evidence [PMID:32788727]. This is essential for NPR1 activation.

3. **Zinc ion binding** (GO:0008270) - Structural evidence from UniProt showing C2HC zinc finger motif critical for TGA interaction.

### Biological Process - CORE
1. **Systemic acquired resistance, salicylic acid mediated signaling pathway** (GO:0009862) - The central function of NPR1, well-documented [PMID:17172357, PMID:11607555, PMID:12615947, etc.]

2. **Regulation of systemic acquired resistance** (GO:0010112) - Supported [PMID:9002272]

3. **Defense response to bacterium** (GO:0042742) - Well-supported [PMID:22699612, PMID:26269953]

4. **Defense response to fungus** (GO:0050832) - Supported [PMID:17513501]

5. **Regulation of jasmonic acid mediated signaling pathway** (GO:2000022) - NPR1 negatively regulates JA signaling [PMID:12615947]

6. **Regulation of salicylic acid mediated signaling pathway** (GO:2000031) - Supported [PMID:12615947]

### Cellular Component
1. **Nucleus** (GO:0005634) - Multiple IDA studies showing nuclear localization after SA treatment [PMID:11148282, PMID:10662863, PMID:26269953]

2. **Cytoplasm** (GO:0005737) - IDA evidence for cytoplasmic localization in uninduced state [PMID:10662863, PMID:26269953]

3. **Nuclear body** (GO:0016604) - IDA evidence for sumoylated NPR1 in nuclear bodies [PMID:26269953]

4. **RNA polymerase II transcription regulator complex** (GO:0090575) - Evidence for complex with TGA factors [PMID:12084833]

### Annotations to REMOVE or MODIFY

1. **Protein binding** (GO:0005515) - Multiple IPI annotations. This is uninformative and should be REMOVED per curation guidelines. The specific interacting partners are documented but the generic "protein binding" term doesn't tell us about function.

2. **Defense response** (GO:0006952) - Too general, MODIFY to more specific terms (defense response to bacterium, fungus)

3. **Metal ion binding** (GO:0046872) - Too general, already have zinc ion binding which is more specific

4. **Innate immune response** (GO:0045087) - Somewhat redundant with SAR, but could keep as non-core

5. **Regulation of defense response** (GO:0031347) - Too general, have more specific terms

## Non-Core Functions (Pleiotropic)
- Response to heat (GO:0009408)
- Response to hypoxia (GO:0001666)
- Response to wounding (GO:0009611)
- Response to insect (GO:0009625)
- Extracellular ATP signaling (GO:0106167)
- Induced systemic resistance (GO:0009682)

These are all real but represent context-dependent or downstream effects rather than core NPR1 function.

## Post-translational Modifications
- Phosphorylation at Ser-11, Ser-15, Ser-55, Ser-59
- Sumoylation (by SUMO3)
- Ubiquitination and proteasomal degradation
- S-nitrosylation at Cys-156
- Redox regulation via Cys-82/Cys-216 disulfide bonds

## References
All PMIDs referenced are from the GOA file and UniProt record.
