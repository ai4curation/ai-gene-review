# Mitochondrial Protein Import Pathways — Deep Research

## 1. Overview of Import Pathways

~99% of mitochondrial proteins are nuclear-encoded and must be imported post-translationally. Seven major pathways handle different classes of precursor proteins:

### 1.1 TOM-TIM23-PAM (Presequence Pathway → Matrix)
- **Substrates**: Proteins with N-terminal cleavable presequences (matrix-targeted)
- **Route**: Tom20 (receptor, recognizes amphipathic presequence) → Tom22 → Tom40 channel → Tim50 (IMS receptor) → Tim23-Tim17 channel → Tim44/mtHsp70 (PAM motor)
- **Key insight**: Cryo-EM structures (Araiso et al., Nature 2023, PMID:37344598) revealed that Tim17, not Tim23, forms the actual translocation path. Tim23 serves as a structural platform connecting Tim17, Tim44, and other subunits.
- **PAM motor**: HSPA9 (mortalin/mtHsp70 in human) drives import via ATP-dependent trapping mechanism. TIMM44 tethers it to the channel. PAM16 (Tim16/Pam16) and DNAJC19 (Tim14/Pam18) regulate ATPase activity.
- **Processing**: After import, MPP (PMPCA/PMPCB heterodimer) cleaves the presequence in the matrix.
- **Latest**: Dynamic TOM-TIM23 supercomplex structure at 2.7 Å and 9.4 Å translocation intermediate captured (Fielden et al., Nat Struct Mol Biol 2025).

### 1.2 TOM-TIM23-SORT (Lateral Insertion into Inner Membrane)
- **Substrates**: Single-pass IM proteins with presequence + hydrophobic sorting signal (stop-transfer signal)
- **Route**: Same as 1.1 through TOM, but at TIM23, the sorting signal causes lateral release into the inner membrane lipid bilayer rather than matrix translocation.
- **Key subunit**: Tim21 (TIMM21) connects TIM23 to respiratory chain complexes (bc1 complex), facilitating membrane potential-dependent lateral sorting.
- **Mgr2** (ROMO1 in humans) seals the lateral gate of Tim17, acting as a gatekeeper for the SORT pathway.

### 1.3 TOM-TIM22 (Carrier Pathway)
- **Substrates**: Multi-pass inner membrane proteins with internal targeting signals (e.g., SLC25 family metabolite carriers, Tim17, Tim22, Tim23 themselves)
- **Route**: Tom70 (receptor, recognizes internal hydrophobic segments via chaperone-mediated delivery) → Tom40 → small TIM chaperones (Tim9-Tim10, Tim8-Tim13) in IMS → Tim22 channel for lateral insertion into IM.
- **Cryo-EM**: Human TIM22 complex structure determined (Qi et al., Cell Res 2021, PMID:33230262). Tim22 forms a twin-pore translocase similar to Tim23 but specialized for carriers.
- **Accessory subunits**: TIMM29 and AGK are metazoan-specific TIM22 complex components.

### 1.4 TOM-SAM/TOB (β-Barrel Outer Membrane Insertion)
- **Substrates**: β-barrel proteins of the outer membrane (VDAC, Tom40, Sam50)
- **Route**: Tom20/Tom22 → Tom40 → small TIM chaperones (Tim9-Tim10) in IMS → SAM complex (Sam50/Tob55 channel + Sam35 + Sam37) inserts β-barrels into OM from the IMS side.
- **Human SAM complex**: SAMM50 is the channel. MTX1 (metaxin-1) and MTX2 (metaxin-2) are the human equivalents of Sam37 and Sam35, respectively. MTX3 has also been identified.
- **Mechanism**: Sam50 itself is a β-barrel and uses a "β-signal" in substrates. Recent work shows lateral gate opening of Sam50 for substrate release into the lipid bilayer.

### 1.5 MIM/MTCH Pathway (α-Helical OM Protein Insertion)
- **Substrates**: α-helical outer membrane proteins — signal-anchored (SA), tail-anchored (TA), and multi-pass proteins
- **Yeast**: Mim1/Mim2 complex mediates insertion; Tom70 serves as initial receptor for some substrates.
- **Metazoan**: MTCH2 (and its paralog MTCH1) identified as the insertase (Bhatt et al., Science 2022, PMID:36264797). MTCH2 uses a diverged solute carrier fold. CRISPR screens showed MTCH2/MTCH1 are required for insertion of TA, SA, and multipass α-helical OM proteins but NOT β-barrels.
- **Structural evolution**: The MTCH family evolved from ancestral solute transporters; structural studies reveal a conserved insertase fold (2026 preprint on structural evolution of MTCH family).
- **MTCH1**: Can also function as an insertase (Bhatt et al., J Cell Sci 2025).

### 1.6 TOM-MIA/Disulfide Relay (IMS Import)
- **Substrates**: Small IMS proteins with twin CX₃C or CX₉C motifs (e.g., small Tims, Cox17, CHCHD2/10)
- **Route**: Unfolded precursors pass through Tom40 → CHCHD4 (Mia40 in yeast) introduces disulfide bonds via transient intermolecular disulfide with substrate → traps them in the IMS.
- **Oxidative relay**: CHCHD4 is re-oxidized by GFER (ALR/Erv1 in yeast), a FAD-dependent sulfhydryl oxidase. Electrons flow to O₂ (producing H₂O₂) or to cytochrome c → Complex IV.
- **Clinical**: GFER mutations cause autosomal-recessive myopathy with cataract and combined respiratory chain deficiency (Di Fonzo et al., Am J Hum Genet 2009, PMID:19409522).
- **Review**: Modjtahedi et al., Biochem Soc Trans 2021, PMID:33599699.

### 1.7 OXA Pathway (Mitochondrial-Encoded IM Insertion)
- **Substrates**: Mitochondrial-encoded inner membrane proteins (Cox1, Cox2, Cox3, cytochrome b, ATP6, etc.) and some nuclear-encoded proteins re-inserted from the matrix ("conservative sorting").
- **Key component**: OXA1L (Oxa1 in yeast) — insertase of the YidC/Oxa1/Alb3 family.
- **Mechanism**: Co-translational insertion of mitochondrial translation products into the inner membrane. Also handles "conservative sorting" — nuclear-encoded proteins that first enter the matrix via TIM23-PAM, then are inserted into the IM from the matrix side via OXA.

## 2. Structural Studies — Landmark Papers

| Complex | Organism | Resolution | Key Finding | PMID |
|---------|----------|-----------|-------------|------|
| TOM core | Human | 3.4 Å | Dimeric Tom40 β-barrel architecture | 33083003 |
| TOM core | Human | 3.0 Å | PDB 7CP9 | 33083003 |
| TOM+Tom20/22 cytosolic | Human | 3.7 Å | Receptor orientation | 35604389 |
| TOM holo | Yeast | 3.8 Å | First near-atomic TOM | 31740857 |
| TIM23 core | Yeast | 2.7 Å | Tim17 is translocation path | 37344598 |
| TIM23-SORT translocation intermediate | Yeast | 9.4 Å | Precursor spanning OM+IM | 37344598 |
| TOM-TIM23 supercomplex | Yeast | varies | Dynamic supercomplex | 2025 NSMB |
| TIM22 | Human | 3.7 Å | Twin-pore carrier translocase | 33230262 |
| SAM/TOB | Yeast | 2.9 Å | β-barrel insertion mechanism | various |

## 3. Key Human Genes by Complex

### TOM Complex
| Gene | Protein | Function | UniProt |
|------|---------|----------|---------|
| TOMM40 | Tom40 | Central β-barrel channel | O96008 |
| TOMM20 | Tom20 | Presequence receptor | Q15388 |
| TOMM22 | Tom22 | Central receptor, connects pores | Q9NS69 |
| TOMM70 | Tom70 | Receptor for carrier proteins/chaperone-bound substrates | O94826 |
| TOMM5 | Tom5 | Small subunit, transfer to channel | Q8N4H5 |
| TOMM6 | Tom6 | Small subunit, complex stability | Q96B49 |
| TOMM7 | Tom7 | Small subunit, quality control/dynamics | Q9P0U1 |

### TIM23 Complex + PAM
| Gene | Protein | Function | UniProt |
|------|---------|----------|---------|
| TIMM23 | Tim23 | Channel structural platform | O14925 |
| TIMM17A | Tim17a | Translocation channel subunit | Q99595 |
| TIMM50 | Tim50 | IMS receptor, phosphatase-like domain | Q3ZCQ8 |
| TIMM21 | Tim21 | SORT pathway, connects to respiratory chain | Q9BVV7 |
| TIMM44 | Tim44 | Tethers mtHsp70 to channel | O43615 |
| HSPA9 | mtHsp70/mortalin | PAM motor ATPase | P38646 |
| PAM16 | Tim16/Pam16 | J-protein-like regulator | Q9Y3D7 |
| DNAJC19 | Tim14/Pam18 | J-protein, stimulates mtHsp70 ATPase | Q96DA6 |

### TIM22 Complex
| Gene | Protein | Function |
|------|---------|----------|
| TIMM22 | Tim22 | Channel for carrier insertion |
| TIMM29 | Tim29 | Metazoan-specific, connects to TOM |
| TIMM10 | Tim10 | Small Tim chaperone (also shared with SAM pathway) |
| AGK | Acylglycerol kinase | Metazoan-specific TIM22 subunit |

### SAM Complex
| Gene | Protein | Function |
|------|---------|----------|
| SAMM50 | Sam50/Tob55 | β-barrel channel |
| MTX1 | Metaxin-1 | Sam37 equivalent, substrate release |
| MTX2 | Metaxin-2 | Sam35 equivalent, β-signal recognition |
| MTX3 | Metaxin-3 | Additional metaxin |

### MIM/MTCH Pathway
| Gene | Protein | Function |
|------|---------|----------|
| MTCH2 | MTCH2 | α-helical OM protein insertase |
| MTCH1 | MTCH1 | Paralog, can also function as insertase |

### MIA/Disulfide Relay
| Gene | Protein | Function |
|------|---------|----------|
| CHCHD4 | Mia40 | Oxidoreductase, introduces disulfide bonds |
| GFER | ALR/Erv1 | Sulfhydryl oxidase, re-oxidizes CHCHD4 |

### Processing Enzymes
| Gene | Protein | Function |
|------|---------|----------|
| PMPCA | MPPα | MPP regulatory subunit |
| PMPCB | MPPβ | MPP catalytic subunit, cleaves presequences |

## 4. Cross-Species Conservation

- **TOM, TIM23, TIM22, SAM, MIA/DRS, OXA**: All conserved from yeast to human
- **MIM pathway diverged**: Yeast uses Mim1/Mim2 (no sequence homology to MTCH2). Metazoans evolved MTCH2 from solute carrier ancestor.
- **TIM22 accessory subunits**: TIMM29 and AGK are metazoan-specific
- **Small Tims**: Tim9, Tim10, Tim8, Tim13 conserved; function as chaperones in IMS for both carrier and β-barrel pathways
- **PAM complex**: Core (Hsp70, Tim44) conserved. Some modulators differ.

## 5. Key Review Articles

- Wiedemann & Pfanner, Annu Rev Biochem 2017, PMID:28301740 — comprehensive pathway overview
- Chacinska et al., Cell 2009, PMID:19285397 — classic review on import machinery
- Modjtahedi et al., Biochem Soc Trans 2021, PMID:33599699 — CHCHD4/MIA40 review
- Araiso et al., Nature 2023, PMID:37344598 — structural basis of TIM23
- Bhatt et al., Science 2022, PMID:36264797 — MTCH2 as insertase
