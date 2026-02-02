# Quantum Sensing Proteins and Engineering Chassis

## Scope
Working definition: biological systems in which quantum effects (spin chemistry, quantum coherence, or tunneling) materially affect a sensing or signal transduction step. The strongest evidence base today is for radical-pair magnetoreception in cryptochromes; other areas are more speculative or are about energy transfer rather than sensing.

## Deep research synthesis (Jan 31, 2026)
Based on `projects/QUANTUM_SENSING/QUANTUM_SENSING-deep-research-openai.md`, the field splits into three main biological mechanisms:
- Radical-pair magnetoreception (cryptochromes): strongest mechanistic evidence; light-dependent, spin-chemistry based sensing in birds/insects; still debated in some models (notably Drosophila behavior).
- Magnetite-based sensing: magnetite crystals act as mechanical transducers; strong evidence in magnetotactic bacteria and growing evidence in some fish/vertebrate tissues; molecular players remain unclear.
- Induction-based sensing: possible in aquatic animals moving through fields; less protein-specific.

Practical constraints from the literature:
- Earth-field sensitivity is weak and noisy; most lab demonstrations use stronger fields.
- Orientation and immobilization of the sensor protein matter for directional sensing.
- Signal readout and controls are a persistent challenge (risk of false positives).

Application themes that are emerging:
- Magneto-sensitive reporters (e.g., engineered flavoproteins with ODMR).
- Magnetogenetics (mixed evidence and reproducibility; careful controls needed).
- Conservation/behavioral applications (e.g., manipulating magnetic cues for navigation studies).

## Proteins with evidence for quantum-level sensing

### Cryptochromes (radical-pair magnetoreception)
Mechanism hypothesis: blue-light excitation of FAD in cryptochrome triggers electron transfer along a tryptophan chain, forming spin-correlated radical pairs. The spin dynamics are sensitive to weak magnetic fields, modulating the yield or lifetime of signaling states.

Key evidence and notes:
- Avian CRY4: European robin CRY4 shows magnetic field effects on radical pair yields in vitro; site-specific mutations implicate multiple FAD-Trp radical pairs in the magnetic response. This is one of the most direct biochemical demonstrations of magnetically sensitive cryptochrome photochemistry. (Nature 2021)
- Broad review: The radical-pair mechanism of magnetoreception is comprehensively reviewed with spin-chemistry and biological context. (Annual Review of Biophysics 2016)
- Monarch butterfly CRY1: Light-dependent inclination sensing requires CRY1 (not CRY2), with antennae and eyes implicated as magnetosensory organs. (Nature Communications 2021)
- Human CRY2: Human cryptochrome 2 can function as a light-dependent magnetosensor in a Drosophila transgenic system, suggesting the photochemistry is conserved even if a human magnetosense is not established. (Nature Communications 2011)
- Drosophila CRY: Initial behavioral reports of light-dependent magnetosensitivity (Nature 2008) are now contested by a large-scale replication study reporting no magnetic behavioral effect (Nature 2023) and ongoing debate (Nature 2024). Treat Drosophila as a contested model.

Implication: cryptochromes are the leading protein family for quantum-sensitive sensing via spin chemistry.

### Engineered LOV-domain proteins (MagLOV; ODMR in living cells)
- A Nature paper published 21 January 2026 reports optically detected magnetic resonance (ODMR) in living bacterial cells using engineered LOV2-domain magneto-sensitive fluorescent proteins (MagLOV variants). The ODMR and magnetic-field effects are explained by a radical-pair mechanism involving the protein backbone and a bound flavin cofactor, with signal-to-noise sufficient for single-cell detection at room temperature. (Nature 2026)
- The study uses directed evolution to tune magnetic and radio-frequency responses and demonstrates applications including spatial localization with gradient fields (fluorescence MRI-like), microenvironment sensing, multiplexing/lock-in detection, and mitigation of scattering/autofluorescence. (Nature 2026)

### Magnetite-based systems (classical magnetic sensing, not quantum)
- Magnetotactic bacteria use magnetosome gene clusters to build magnetite particles that align cells in fields.
- Vertebrate evidence is suggestive but mixed; recent work points to magnetite-bearing cells in fish olfactory tissues and candidate biomineralization gene signatures.

## Shortlist: candidate proteins and constructs to pursue

### Priority protein candidates (mechanistic evidence strongest)
- ErCRY4 (European robin cryptochrome 4): in vitro magnetic sensitivity with radical-pair signatures and mutational mapping of Trp radical pairs; strong biochemical anchor for magnetoreception. (Nature 2021)
- DpCRY1 (monarch butterfly cryptochrome 1): required for light-dependent inclination sensing in vivo; CRY2 dispensable in that system. (Nature Communications 2021)
- hCRY2 (human cryptochrome 2): supports light-dependent magnetosensing when expressed in Drosophila; good for readily available human sequence and protein tools. (Nature Communications 2011)
- DmCRY (Drosophila cryptochrome): historically used in magnetosensing assays, but behavioral evidence is contested by large-scale replication; still useful as a biochemically tractable CRY. (Nature 2023; Nature 2024)
- MagLOV (engineered LOV2 magneto-sensitive fluorescent proteins): ODMR and magnetic-field effects in living cells at room temperature; directed-evolution variants enable tunable responses and practical imaging/sensing. (Nature 2026)

### Engineering-ready constructs (signal coupling or structural leverage)
- AtCRY2-CIB1 optogenetic module: blue-light inducible dimerization with rapid kinetics; useful to wire cryptochrome photochemistry into readouts. (Nature Methods 2010)
- AtCRY1 PHR domain-based constructs: structural templates with bound FAD enable rational tuning of electron-transfer paths; useful starting point for designing radical-pair lifetimes. (Swiss-Model Repository, PDB 1u3d/1u3c)
- AsLOV2-derived MagLOV variants: LOV2 backbone with flavin cofactor; demonstrated ODMR and strong magnetic-field effects in vivo with single-cell readouts. (Nature 2026)

## UniProt snapshot (cursory)
Examples of cryptochrome entries and accessions linked from UniProt-connected resources:
- Homo sapiens CRY1: UniProt Q16526 (CRY1_HUMAN). (iPTMnet)
- Homo sapiens CRY2: UniProt Q49AN0. (Human Protein Atlas)
- Arabidopsis thaliana CRY1: UniProt Q43125 (CRY1_ARATH). (iPTMnet; Swiss-Model)
- Arabidopsis thaliana CRY2: UniProt Q96524. (InParanoid)
- Drosophila melanogaster CRY: UniProt O77059. (RCSB PDB/AlphaFold entry)
UniProt-linked annotations for CRY2 include FAD as a ligand/cofactor, consistent with flavoprotein photochemistry. (Human Protein Atlas)

## Reproducible pipeline (draft)
I sketched a minimal, reproducible pipeline for candidate triage in `projects/quantum-sensing-bioinformatics/`:
- Fetch UniProt JSON + FASTA by accession list.
- Pull RCSB PDB mappings/metadata and ligands (flag FAD).
- Produce a per-accession summary table for quick screening.

This is intentionally conservative and not a functional claim; it’s meant to surface evidence and prioritize targets.

### Photosynthetic energy-transfer complexes (quantum coherence; not sensing per se)
- FMO complex in green sulfur bacteria showed signatures interpreted as wavelike (coherent) energy transfer in ultrafast spectroscopy. (Nature 2007)
- Follow-up theoretical/experimental analyses argue that coherence signatures can be affected by ensemble dephasing and that the functional role in vivo is still debated. (J Phys Chem B 2011)

Implication: strong evidence of quantum coherence in pigment-protein complexes, but these systems are energy-transfer devices rather than sensors.

### Olfaction (vibrational theory; speculative and contested)
- Drosophila can discriminate isotopomers in conditioning assays, interpreted as evidence for a vibration-sensing component of olfaction. (PNAS 2011)
- A later study found no isotopomer discrimination in several human and mouse olfactory receptors and argued against the vibrational theory for those receptors. (PNAS 2015)

Implication: potential quantum-tunneling or inelastic electron transfer mechanisms in odorant recognition remain controversial and receptor-specific at best.

## Engineering chassis: candidates and rationale

### 1) Purified protein / in vitro reconstitution
- Best for mechanistic benchmarking of magnetic field effects (EPR, transient absorption, opto-chemistry) and rapid mutational screening.
- Straightforward to express cryptochromes in E. coli or insect cells and reconstitute with FAD.
- Enables decoupling photochemistry from cellular signaling, useful for engineering stronger magnetic field effect sizes.

### 2) Yeast and mammalian cell culture (HEK, U2OS, etc.)
- Good for eukaryotic folding, post-translational modifications, and targeting to specific subcellular locations.
- Compatible with reporter assays (luciferase, transcriptional switches) to couple cryptochrome conformational changes to measurable outputs.
- Suitable if the goal is to engineer a quantum-sensitive signal transduction module.

### 3) Insect systems (Drosophila S2 cells, insect cell lines, monarch)
- Useful for expressing insect CRY1s and leveraging existing genetic tools for sensory assays.
- Caution: behavioral magnetosensitivity in Drosophila is contested; monarch CRY1 has stronger evidence but is a more specialized chassis.

### 4) Plant systems (Arabidopsis, Nicotiana)
- Plants already use cryptochromes as blue-light photoreceptors; robust expression and optical readouts.
- Could be a chassis for engineering magnetically sensitive photoreceptor signaling pathways.

### 5) Magnetotactic bacteria (magnetosome proteins; classical magnetic sensing)
- Not quantum sensing, but a practical chassis for magnetic field coupling via magnetite crystals and magnetosome-associated proteins.
- Useful as a parallel track if the project goal is magnetic sensing rather than specifically quantum spin effects.

## Engineering targets and design levers
- Radical-pair lifetime and yield: mutate residues in the electron-transfer chain (Trp triad/tetrad) or tune FAD redox chemistry.
- Signal coupling: fuse cryptochrome C-terminus to transcriptional regulators, ion channels, or dimerization modules to convert spin effects to outputs.
- Orientation and localization: membrane anchoring or anisotropic scaffolds may be required to translate magnetic anisotropy into directional signals.
- Photophysics: optimize absorption spectrum to desired illumination regimes (e.g., 380-500 nm for many CRYs).

## Open questions for project scoping
- Do you want a biological sensor (in vivo behavior or cell signaling) or an in vitro quantum-chemistry module?
- Is the goal magnetic-field sensing (geomagnetic range) or broader quantum coherence/tunneling effects?
- What constraints on chassis (biosafety level, genetic tools, throughput) are acceptable?

## References (selected)
- Hore PJ, Mouritsen H. The radical-pair mechanism of magnetoreception. Annu Rev Biophys. 2016. doi:10.1146/annurev-biophys-032116-094545.
- Xu J et al. Magnetic sensitivity of cryptochrome 4 from a migratory songbird. Nature. 2021. doi:10.1038/s41586-021-03618-9.
- Wan G et al. Cryptochrome 1 mediates light-dependent inclination magnetosensing in monarch butterflies. Nat Commun. 2021. doi:10.1038/s41467-021-21002-z.
- Foley LE et al. Human cryptochrome exhibits light-dependent magnetosensitivity. Nat Commun. 2011. doi:10.1038/ncomms1364.
- Gegear RJ et al. Cryptochrome mediates light-dependent magnetosensitivity in Drosophila. Nature. 2008. doi:10.1038/nature07183.
- Bassetto M et al. No evidence for magnetic field effects on the behaviour of Drosophila. Nature. 2023. doi:10.1038/s41586-023-06397-7.
- Engel GS et al. Evidence for wavelike energy transfer through quantum coherence in photosynthetic systems. Nature. 2007. doi:10.1038/nature05678.
- Ishizaki A, Fleming GR. On the interpretation of quantum coherent beats observed in two-dimensional electronic spectra of photosynthetic light harvesting complexes. J Phys Chem B. 2011. doi:10.1021/jp112406h.
- Franco MI et al. Molecular vibration-sensing component in Drosophila melanogaster olfaction. PNAS. 2011. doi:10.1073/pnas.1012293108.
- Block E et al. Implausibility of the vibrational theory of olfaction. PNAS. 2015. doi:10.1073/pnas.1503054112.
- Peigneux A et al. Learning from magnetotactic bacteria: synthesis of biomimetic nanoparticles mediated by magnetosome-associated proteins. J Struct Biol. 2016. doi:10.1016/j.jsb.2016.06.026.
- Bassetto M et al. Magnetic field effects on behaviour in Drosophila: Matters Arising. Nature. 2024. doi:10.1038/s41586-024-08209-0.
- Abrahams G et al. Quantum spin resonance in engineered proteins for multimodal sensing. Nature. 2026. doi:10.1038/s41586-025-09971-3.
- Kennedy MJ et al. Rapid blue-light-mediated induction of protein interactions in living cells. Nat Methods. 2010. doi:10.1038/nmeth.1524.
- iPTMnet Report for Q16526 (CRY1_HUMAN). University of Delaware.
- iPTMnet Report for Q43125 (CRY1_ARATH). University of Delaware.
- Human Protein Atlas: CRY2 (UniProt Q49AN0).
- Swiss-Model Repository: Q43125 (CRY1_ARATH) structures (PDB 1u3d/1u3c).
- InParanoid: CRY1_ARATH ortholog group lists Q96524 (CRY2).
- RCSB PDB/AlphaFold: UniProt O77059 (Drosophila cryptochrome).
- Deep research report: file:projects/QUANTUM_SENSING/QUANTUM_SENSING-deep-research-openai.md
