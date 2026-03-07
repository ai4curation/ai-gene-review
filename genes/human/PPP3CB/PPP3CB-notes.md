# PPP3CB Gene Review Notes

## Gene Identity
- **Gene symbol**: PPP3CB (also known as CALNA2, CALNB, CNA2)
- **UniProt**: P16298 (PP2BB_HUMAN)
- **Product**: Serine/threonine-protein phosphatase 2B catalytic subunit beta isoform (Calcineurin A beta, CNA beta)
- **EC**: 3.1.3.16
- **Family**: PPP phosphatase family, PP-2B subfamily
- **Location**: Chromosome 10q21-q22

## Core Function Summary

PPP3CB encodes one of three catalytic subunits (alpha, beta, gamma) of calcineurin (also called protein phosphatase 2B or PP2B), a calcium-dependent, calmodulin-stimulated serine/threonine phosphatase. Calcineurin is a heterodimer consisting of a catalytic subunit A (PPP3CA, PPP3CB, or PPP3CC) and a regulatory Ca2+-binding subunit B (PPP3R1 or PPP3R2).

### Enzyme Mechanism
- Binuclear metal center with Fe3+ and Zn2+ at the active site [PMID:8524402 "In the native CaN structure, an auto-inhibitory element binds at the Zn/Fe-containing active site. The metal-site geometry and active-site water structure suggest a catalytic mechanism involving nucleophilic attack on the substrate phosphate by a metal-activated water molecule."]
- X-ray crystal structure at 2.23 Å for full-length PPP3CB (PDB: 4OR9) [PMID:26794871]

### Activation Mechanism
Multi-level activation by Ca2+/calmodulin:
1. At low Ca2+, calcineurin A is bound to calcineurin B with only high-affinity Ca2+ sites occupied - inactive state [PMID:26794871]
2. Elevated Ca2+ occupies low-affinity sites on calcineurin B → conformational change → exposes calmodulin-binding domain → partial activation [PMID:26794871]
3. Ca2+/calmodulin binding displaces autoinhibitory domain (AID) from active site → full activation [PMID:26794871]
4. PPP3CB has a novel autoinhibitory segment (AIS, residues 416-423) in addition to AID (residues 474-496) [PMID:26794871 "revealed a novel autoinhibitory segment (AIS) in addition to the well-known autoinhibitory domain (AID). The AIS nestles in a hydrophobic intersubunit groove, which overlaps the recognition site for substrates and immunosuppressant-immunophilin complexes."]

### Isoform-Specific Features
PPP3CB has a unique proline-rich N-terminal sequence (poly-Pro domain) that determines substrate binding:
- CaN beta has the lowest Km values for all tested protein substrates [PMID:19154138 "CaN beta exhibits for all tested protein substrates the lowest K(m) values"]
- The poly-Pro domain is involved in substrate recognition [PMID:19154138 "the proline-rich sequence of CaN beta is involved in substrate recognition"]
- All CaN isoforms show same cytoplasmic distribution but differ in substrate specificities [PMID:19154138]
- Km for NFATC1: 0.69 μM; Km for DARPP32: 0.7 μM [PMID:19154138]

### Key Substrates
1. **NFAT family** (NFATC1, NFAT1): Dephosphorylation → nuclear translocation → transcriptional activation of cytokine genes [PMID:19154138, PMID:8631904 "a direct interaction between calcineurin and NFAT1 that is consistent with a direct enzyme-substrate relation"]
2. **TFEB**: Dephosphorylation in response to lysosomal Ca2+ release → TFEB nuclear translocation → lysosomal biogenesis and autophagy [PMID:25720963 "The most significant hit identified by the primary screening was the calcineurin catalytic subunit isoform beta (PPP3CB)"]
3. **ELK1**: Dephosphorylation → inactivation [PMID:19154138]
4. **DARPP-32**: Dephosphorylation [PMID:19154138]

### TFEB/Autophagy Pathway (Key for PPP3CB specifically)
PPP3CB was identified as the key calcineurin isoform for TFEB regulation:
- Lysosomal Ca2+ release through MCOLN1 activates calcineurin [PMID:25720963]
- Calcineurin binds and dephosphorylates TFEB → nuclear translocation [PMID:25720963]
- siRNA specifically targeting PPP3CB suppressed starvation-induced nuclear translocation of TFEB [PMID:25720963]
- IRGM promotes calcineurin-TFEB association [PMID:32753672 "IRGM directly interacted with TFEB and promoted the nuclear translocation of TFEB"]

### Calcineurin-NFAT Signaling
- Calcineurin is the target of immunosuppressants FK506 (tacrolimus) and cyclosporin A [PMID:11005320, PMID:8524402]
- AKAP79/150 scaffolds calcineurin with PKA and L-type Ca2+ channels, enabling bidirectional regulation [PMID:17640527, PMID:22343722]
- NHE1 binds calcineurin A directly via PVITID motif (resembles PxIxIT) → activates NFAT signaling → cardiomyocyte hypertrophy [PMID:22688515]

### Calcineurin Complex and Interactions
- Forms heterodimer with regulatory subunit PPP3R1 (calcineurin B) [PMID:26794871, PMID:8524402]
- Crystal structure of PPP3CB in complex with PPP3R1, iron, and zinc [PMID:26794871]
- Interacts with calmodulin in Ca2+-dependent manner [PMID:26794871]
- Interacts with SPATA33 (via PQIIIT motif) → localizes calcineurin to mitochondria in spermatozoa (note: this is primarily PPP3CC/PPP3R2 sperm calcineurin function) [PMID:34446558]
- Interacts with IRF2 and RCAN1 (IntAct data)
- Immunophilin-binding domain is highly conserved between CNA1 and CNA2, with no polymorphisms found [PMID:11005320]

### Expression and Localization
- Ubiquitously expressed (unlike PPP3CC which is testis-enriched) [PMID:34446558]
- Tissue enhanced in skeletal muscle (HPA data)
- Cytoplasmic localization [PMID:19154138]
- Can translocate to nucleus with NFAT [Reactome]
- Located at Z disc, T-tubule in muscle cells (Ensembl ortholog data)

### Disease Association
- PPP3CB at chromosome 10q22 associated with schizophrenia subgroup with deficits in attention and executive function [PMID:21531385 "significantly lower expression of... PPP3CB... In schizophrenic patients"]
- This is a GWAS association study, not a direct functional link

### Important Notes for Annotation Review
1. **GO:0006468 protein phosphorylation** is clearly WRONG for this gene - PPP3CB is a phosphatase (EC 3.1.3.16), not a kinase. This ISS annotation should be REMOVED.
2. **GO:0005515 protein binding** annotations are uninformative - should look for more specific MF terms
3. Many annotations from PMID:21531385 (schizophrenia GWAS) assign neuronal functions (learning, memory, axon extension, synaptic plasticity) based on chromosomal association, not direct experimental evidence for PPP3CB - these are over-annotations
4. PMID:8978785 is a chromosomal mapping paper, not functional - annotations to signal transduction, T cell proliferation, and transcription based on this are very weak (NAS)

## Cloning History
- First cloned in 1989, identified two isozymes from alternative splicing [PMID:2556704]
- Chromosomal location mapped to 10q21-q22 [PMID:8978785]
- At least 4 isoforms from alternative splicing

## Four Isoforms
- Isoform 1 (canonical, 524 aa)
- Isoform 2 (different C-terminus with 54bp insert + different 3' end)
- Isoform 3 (insertion at aa395 + deletion of aa456-465)
- Isoform 4 (insertion at aa395)
