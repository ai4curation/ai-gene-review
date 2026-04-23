# Frmpd2 - Research Notes

## Gene Overview

Frmpd2 (FERM and PDZ domain-containing protein 2) is a multi-domain scaffold protein
consisting of an N-terminal KIND domain, a FERM domain, and three PDZ domains. It functions
as a molecular adaptor/scaffold in multiple cellular contexts, including epithelial cell
polarity, synaptic transmission, retinal synapse formation, and innate immune signaling.

UniProt: A0A140LI67 | MGI: MGI:2685472 | Synonyms: Gm626

## Domain Architecture

- **KIND domain** (aa 15-197): Function not well characterized for FRMPD2 specifically
- **FERM domain** (aa 342-642): Binds phosphatidylinositols (especially PtdIns(3,4)P2);
  sufficient for membrane localization; interacts with actin filaments
- **PDZ1 domain** (aa 775-861): Function less characterized
- **PDZ2 domain** (aa 950-1035): Key interaction domain; binds GluN2A/GluN2B C-termini,
  p0071/PKP4, ARVCF, CTNND2; crystal structure solved (PDB: 5ZDS)
- **PDZ3 domain** (aa 1079-1167): Binds LRIT1 C-terminus

## Key Literature

### 1. Epithelial cell polarity and tight junctions
[PMID:19706687 Stenzel et al. 2009, "PDZ-domain-directed basolateral targeting of the
peripheral membrane protein FRMPD2 in epithelial cells"]

Key findings:
- FRMPD2 localizes to basolateral membrane in epithelial cells (human cell lines)
- Partially colocalizes with ZO-1 (TJP1) at tight junctions
- Knockdown in Caco-2 cells impairs tight junction formation
- FERM domain binds phosphatidylinositols, sufficient for membrane localization
- E-cadherin-dependent recruitment to cell-cell junctions
- PDZ2 binds p0071 (armadillo protein PKP4) for basolateral restriction
- Catenin family proteins identified as binding partners

### 2. NMDA receptor scaffolding at synapses
[PMID:31196628 Lu et al. 2019, "The second PDZ domain of scaffold protein Frmpd2 binds
to GluN2A of NMDA receptors"]

Key findings (mouse):
- Frmpd2 specifically expressed at postsynaptic membrane
- PDZ2 domain (not PDZ1 or PDZ3) binds GluN2A and GluN2B C-termini
- Higher affinity for GluN2A than GluN2B (SPR data)
- Crystal structure of mouse PDZ2 solved at 1.80 A (PDB: 5ZDS)
- Suggests role in synaptic NMDAR-mediated neural excitatory transmission

Additional data from bioRxiv preprint (doi:10.1101/403360):
- FRMPD2 anchors GluN2A at synapses without changing total NMDAR expression
- FERM domain directly interacts with actin filaments
- Modifies excitatory synapse morphogenesis
- Mediates behavioral and field potential phenotypes of epilepsy

### 3. Cone photoreceptor synapse formation
[PMID:29590622 Ueno et al. 2018, "Lrit1, a Retinal Transmembrane Protein, Regulates
Selective Synapse Formation in Cone Photoreceptor Cells and Visual Acuity"]

Key findings (mouse retina):
- Frmpd2 described as "photoreceptor scaffold protein"
- PDZ3 domain interacts with LRIT1 C-terminus
- Part of Frmpd2-Lrit1-mGluR6 axis
- Regulates selective synapse formation between cone photoreceptors and cone ON-bipolar cells
- Lrit1-deficient retinas show aberrant cone pedicle morphology
- Lrit1-null mice show impaired visual acuity

### 4. NOD2 innate immune signaling
[PMID:23213202 Lipinski et al. 2012, "RNAi screening identifies mediators of NOD2
signaling: Implications for spatial specificity of MDP recognition"]

Key findings (human cell lines):
- FRMPD2 identified in RNAi screen as positive NF-kB regulator
- Interacts with NOD2 via leucine-rich repeats
- Forms complex with membrane-associated protein ERBB2IP
- Spatially assembles NOD2-signaling complex (NOD2-RIPK2) at basolateral membrane
- Restricts NOD2-mediated immune responses to basolateral compartment
- Crohn disease NOD2 truncation mutations impair FRMPD2 interaction
- Intestinal inflammation leads to FRMPD2 downregulation

## Expression

From UniProt/Bgee: Expressed in retinal neural layer and 57 other cell types/tissues.
NCBI Gene: Chromosome 14 in mouse.

## Interaction Partners (summary)

| Partner | Domain | Evidence | Context |
|---------|--------|----------|---------|
| GluN2A (GRIN2A) | PDZ2 | Direct (PubMed:31196628) | Synaptic transmission |
| GluN2B (GRIN2B) | PDZ2 | Direct (PubMed:31196628) | Synaptic transmission |
| LRIT1 | PDZ3 | Direct (PubMed:29590622) | Retinal synapse |
| PKP4/p0071 | PDZ2 | By similarity | Basolateral targeting |
| CTNND2 | PDZ2 | By similarity | Cell junctions |
| ARVCF | PDZ2 | By similarity | Cell junctions |
| NOD2 | LRR interaction | Human (PubMed:23213202) | Innate immunity |
| ERBB2IP | complex | Human (PubMed:23213202) | Innate immunity |
| Actin filaments | FERM | bioRxiv | Synapse morphogenesis |
| PtdIns(3,4)P2 | FERM | By similarity | Membrane localization |

## Assessment Notes

The core function of Frmpd2 is as a **signaling adaptor/scaffold protein** that organizes
multi-protein complexes at the membrane. The specific biological contexts are:

1. **Primary in mouse**: Synaptic scaffolding (direct experimental evidence in mouse)
   - NMDAR anchoring at postsynaptic density (PMID:31196628)
   - Cone photoreceptor synapse formation via LRIT1 (PMID:29590622)

2. **Inferred from human ortholog (Q68DX3)**: Epithelial polarity
   - Basolateral membrane targeting (PMID:19706687)
   - Tight junction regulation (PMID:19706687)
   - NOD2 signalosome assembly (PMID:23213202)

The tight junction and NOD2 functions are based on human FRMPD2 studies and transferred
by ISO/IBA. The synaptic functions have direct experimental evidence in mouse.
