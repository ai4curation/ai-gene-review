# abi1a notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8M3AND6 (TrEMBL, RefSeq XP_009295502.1, "isoform X1",
  522 aa); 8 GOA rows (5 IBA, 3 IEA), none with a PMID. ZFIN ZDB-GENE-040426-1701,
  Ensembl ENSDARG00000010155, chromosome 24.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` was generated. Literature searched by hand via Europe PMC
  (queries: `abi1a zebrafish`, `abi1b zebrafish`, `(abi1 OR "abl interactor 1") AND zebrafish`,
  title searches for ABI1, ABI2, WAVE regulatory complex).
- Part of DANRE_DUPLICATION batch 3 (random draw 7 of seed 20260928); paralog abi1b.

## What the zebrafish literature says

Essentially nothing on function. The only experiment found:

- F0 CRISPR knockdown of "abi1" in a congenital-heart-disease follow-up gave no cardiac
  phenotype (1/72 embryos with reversed looping) [PMID:32368696 "Finally, loss of cyfip1 and abi1a, unlike the other WAVE2 complex genes, was not found to impact zebrafish heart development."].
  The authors speculate compensation by the paralog, without testing it
  [PMID:32368696 "Zebrafish, unlike mouse or human, have 2 orthologs for ABI1 (abi1a and abi1b) with abi1b likely compensating to maintain normal cardiac development."].
  F0 embryos are mosaic [PMID:32368696 "Using CRISPR-guided knockdown, we observed cardiac phenotypes in F0 embryos with mosaic loss of brk1, cul3a, nckap1, racgap1, and wasf2 (Table 3)."].
- Other hits (inner-ear transcriptomes, spinal-cord microarrays, mutagenesis screens) only list the
  gene in datasets.

## Mammalian ABI1 (the ancestral function)

- Discovered as an SH3 protein binding the Abl C-terminus [PMID:7590237 "A novel cellular protein, Abl-interactor-1 (Abi-1), which specifically interacts with the carboxy-terminal region of Abl oncoproteins, has been identified in a mouse leukemia cell line."]
  and widely expressed [PMID:7590237 "The gene is widely expressed in the mouse, with highest levels of mRNA found in the bone marrow, spleen, brain, and testes."].
- Core subunit of the WAVE regulatory complex (WRC = SCAR complex)
  [PMID:15048123 "Abi1 interacts directly with the WHD domain of WAVE2, increases WAVE2 actin polymerization activity and mediates the assembly of a WAVE2-Abi1-Nap1-PIR121 complex."];
  needed for Rac-dependent lamellipodia [PMID:15048123 "Consistently, inhibition of Abi1 by RNA interference (RNAi) abrogates Rac-dependent lamellipodia protrusion."]
  and relocalizes to the leading edge [PMID:15048123 "The WAVE2-Abi1-Nap1-PIR121 complex is as active as the WAVE2-Abi1 sub-complex in stimulating Arp2/3, and after Rac activation it is re-localized to the leading edge of ruffles in vivo."].
- Structure: Abi forms a four-helix bundle with WAVE and HSPC300 in the WRC
  [PMID:21107423 "A long four-helix bundle created by a helix from HSPC300 (residues 14-68), two helices from Abi2 (residues 1-39 and 43-112) and a helix from WAVE1 (residues 26-81) contacts Sra1 extensively and is aligned roughly parallel to the long axis of the dimer (Supplementary Figs."];
  the Abi subunit forms part of the WIRS receptor-binding surface
  [PMID:24439376 "Structural, biochemical, and cellular studies reveal that a sequence motif that defines these ligands binds to a highly conserved interaction surface of the WRC formed by the Sra and Abi subunits."].
- Also activates N-WASP [PMID:16155590 "Thus, Abi1 is a dual regulator of WAVE and N-WASP activities in specific processes that are dependent on actin dynamics."].
- Mouse knockouts: Abi1 is essential mid-gestation, heart and brain affected
  [PMID:21482783 "Thus, Abi1-signaling events are not required for gastrulation but are critical during brain and heart development."];
  [PMID:21173240 "Mice lacking Abi1 or α4 exhibit midgestational lethality with abnormalities in placental and cardiovascular development."].
  Abi2 cannot compensate [PMID:21482783 "This finding suggests that the presence of Abi1 is critical for the integrity and stability of WAVE complex and that Abi2 levels are not sufficiently increased to compensate fully for the loss of Abi1 in KO cells and to restore the integrity and function of the WAVE complex."].
- Neuron migration donor for the IBA is mouse Abi2 (MGI:106913)
  [PMID:15572692 "Loss of Abi2 also resulted in cell migration defects in the neocortex and hippocampus, abnormal dendritic spine morphology and density, and severe deficits in short- and long-term memory."].

## Own analyses

`abi1a-bioinformatics/pair_analysis.py` (results in `RESULTS.md`, raw `output.txt`):
protein identity, conserved regions, gar relative-rate test, E-ERAD-475 time course, Bgee
calls for both copies and gar, local synteny. Key points:
- abi1a 81.6% identical to human ABI1; abi1b 77.5%; abi1a vs abi1b 79.2%.
- WAVE-binding N-terminus, coiled coil and SH3 conserved in both; Y213 (ABL site) kept.
- Relative-rate test vs gar not significant (17 vs 28 unique changes).
- Temporal reciprocity: abi1b is the maternal/cleavage-stage transcript (26-28 TPM at 128- to
  1k-cell) while abi1a takes over from mid-gastrula (26-36 TPM from 75% epiboly onward; abi1b
  3-7 TPM).
- Synteny: no conserved microsynteny within 1.5 Mb; 3 teleost-level paralogue pairs from the
  abi1a neighbourhood have partners elsewhere on chr2 (kmt2c, agtr1). Ensembl Compara places the
  duplication at Clupeocephala, agreeing with PANTHER.
- Bgee: abi1a called in many adult tissues (gill, intestine, skin, spleen, liver, muscle,
  kidney, testis, eye); abi1b only in embryo, retina, brain, ovary, bone. Gar ABI1 is broadly
  expressed, like abi1a.

## Curation decisions (summary)

All 8 rows are family-level (IBA, SubCell IEA). WRC membership, lamellipodium location and
adaptor MF are accepted; neuron migration (Abi2-seeded IBA) and filopodium kept as non-core.
No NEW terms: nothing zebrafish-specific supports one.
