# Enterobacteria phage M13 — Gene I (G1P / pI and G11P / pXI)

## Overview
- **UniProt Accession:** P03656 (`G1P_BPM13`)
- **Gene Symbol:** `I`
- **Alternative Products:**
  - **Isoform G1P (pI, P03656-1):** Full-length 348 aa protein (~39.6 kDa). Single-pass inner membrane protein (residues 1–253 cytoplasmic, 254–270 transmembrane helix, 271–348 periplasmic). Contains essential N-terminal Walker A (residues 8–15, `GKLGSGKT`) and Walker B (`DEXG`, Asp-88/Glu-89) ATP-binding/hydrolyzing motifs [PMID:28397779, PMID:35746635].
  - **Isoform G11P (pXI, P03656-2):** 108 aa protein (~12 kDa) translated from an internal in-frame start codon at Met-241 (missing residues 1–240; N-formylated in *f1*/*M13*). Contains the same transmembrane segment and periplasmic C-terminal domain as pI but lacks the cytoplasmic ATPase domain [PMID:35746635].

## Biological Role in the M13 Lifecycle
- **Transmembrane Assembly Machine (pI/pXI–pIV Complex):** pI and pXI co-assemble in the *Escherichia coli* inner membrane into a ~320 kDa oligomeric ring structure (~12 nm outer diameter, ~5 nm central pore, likely hexameric with ~6 copies each of pI and pXI) [PMID:35746635]. Its periplasmic C-terminal domain interacts across the periplasm with the outer-membrane pIV secretin multimer to form a continuous envelope-spanning assembly and extrusion conduit [PMID:35746635].
- **ATP-Driven Viral Extrusion and Virion Assembly:** The cytoplasmic N-terminal domain of pI binds the pV-coated progeny (+)ssDNA packaging complex (recognizing the morphogenetic packaging signal alongside minor coat proteins pVII and pIX) and couples ATP hydrolysis to the displacement of pV dimers by membrane-embedded coat proteins (pVIII, capped by pVII/pIX at the distal tip and terminated by pIII/pVI at the proximal tip) as the nascent filament is extruded through the cell envelope without lysing the host [PMID:28397779, PMID:35746635].

## Key GO Annotations
- **Cellular Component:** `GO:0020002` (host cell plasma membrane) — experimentally demonstrated localization to the *E. coli* inner membrane [PMID:35746635].
- **Molecular Function:** `GO:0005524` (ATP binding) / `GO:0016887` (ATP hydrolysis activity) — Walker A/B P-loop NTPase domain in cytoplasmic N-terminus of pI [PMID:28397779, PMID:35746635].
- **Biological Process:** `GO:0099045` (viral extrusion) and `GO:0019068` (virion assembly) — essential inner-membrane assembly motor for concomitant filamentous phage morphogenesis and non-lytic secretion [PMID:35746635].
