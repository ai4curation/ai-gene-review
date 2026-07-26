# UBE2T (Q9NPD8) — gene review notes

## Identity
- UBE2T = Ubiquitin-conjugating enzyme E2 T (UBC family). AltNames: PIG50 (cell proliferation-inducing gene 50), HSPC150. HGNC:25009. 197 aa; UBC catalytic core (residues 2–152) with active-site Cys86; C-terminal disordered tail (149–197). EC 2.3.2.23.
- Fanconi anemia complementation group T (FANCT / FA-T); biallelic loss causes FA.

## Core biology (E2 of the Fanconi anemia pathway)
- UBE2T is the ubiquitin-conjugating enzyme (E2) essential for the FA pathway; it binds the RING E3 ligase FANCL and is required for monoubiquitination of FANCD2 in vivo. UBE2T depletion → abnormal chromosomes (FA hallmark) after DNA damage [PMID:16916645 "UBE2T is the ubiquitin-conjugating enzyme (E2) essential for this pathway. UBE2T binds to FANCL, the ubiquitin ligase subunit of the Fanconi anemia core complex, and is required for the monoubiquitination of FANCD2 in vivo. DNA damage in UBE2T-depleted cells leads to the formation of abnormal chromosomes that are a hallmark of Fanconi anemia."].
- Active-site Cys86 is required for E2 activity: C86A abolishes activity (mutagenesis across PMID:16916645, 17938197, 19111657, 19589784, 19887602; UniProt MUTAGEN 86 "C->A: Loss of E2 enzyme activity").
- FANCL–UBE2T is a strict, exclusive/cognate E3–E2 pair; FANCL selects UBE2T over other E2s via an extensive electrostatic/H-bond network beyond the conserved hydrophobic interface; Arg60 of UBE2T is the positive selector (salt bridge with Glu340 of FANCL) [PMID:24389026 "FANCL will preferentially select Ube2T"; "the positive selector in Ube2T for FANCL is Arg60, which forms a salt bridge with Glu340 of FANCL ... and is required for FANCL-Ube2T-mediated monoubiquitination of FANCD2"; "FANCL exclusively formed a complex with Ube2T"].
- Minimal reconstitution: UBE2T + FANCL monoubiquitinate FANCD2; FANCL's RWD-like domain stimulates it; adding FANCI enhances and restricts modification to the physiological substrate lysine of FANCD2 [PMID:19111657 "we minimally reconstitute this monoubiquitination reaction with Ube2t and the FANCL protein, revealing that monoubiquitination is stimulated by a conserved RWD-like domain in FANCL. Furthermore, addition of the FANCI protein enhances monoubiquitination and also restricts it to the in vivo substrate lysine residue on FANCD2."].
- UBE2T–FANCL also monoubiquitinates FANCI on Lys-523 in vitro [PMID:19589784 "FANCI can be ubiquitinated on Lys-523 by the UBE2T-FANCL pair in vitro"].
- Regulation is by localization, not complex assembly: UBE2T, the FA core complex, and FANCD2 are recruited independently to chromatin; an active E2/E3 holoenzyme forms transiently on chromatin. UBE2T is constitutively present in the chromatin compartment [PMID:17938197 "UBE2T and FANCD2 access this subcellular fraction independently of the FA core complex. FANCD2 monoubiquitination is therefore not regulated by multiprotein complex assembly but by the formation of an active E2/E3 holoenzyme on chromatin."; "The E2-conjugating enzyme UBE2T is constitutively present in this compartment."].

## Localization
- Nucleus (UniProt SUBCELLULAR LOCATION "Nucleus"; Note="Accumulates to chromatin"). Experimental nuclear localization [PMID:19887602], TAS nucleus [PMID:17938197]. Reactome places it in nucleoplasm.

## Disease (FANCT / FA-T)
- Biallelic UBE2T mutations cause FA; the p.Gln2Glu variant abolishes FANCD2 monoubiquitination and interaction with FANCL; complementation group named FA-T [PMID:26046368 "each harboring biallelic mutations in UBE2T. They both produced a defective UBE2T protein with the same missense alteration (p.Gln2Glu) that abolished FANCD2 monoubiquitination and interaction with FANCL. We suggest this FA complementation group be named FA-T."]. UniProt VARIANT 2 (Q->E) in FANCT.

## Autoregulation / autoubiquitination
- UBE2T undergoes automonoubiquitination (Lys-91, also Lys-182); one report says this inactivates the E2 [PMID:16916645 "UBE2T undergoes automonoubiquitination in vivo. This monoubiquitination is stimulated by the presence of the FANCL protein and inactivates UBE2T."], another finds no effect on activity (PMID:19111657). Regulatory/self-limiting, not the core catalytic output.

## Other reported activities (context-dependent / in vitro)
- Polyubiquitination of BRCA1 and its downregulation upon UBE2T overexpression in breast cancer cells; interacts/colocalizes with BRCA1/BARD1; requires active Cys86 [PMID:19887602 "BRCA1 to be polyubiquitinated by incubation with wild-type UBE2T protein, but not with C86A-UBE2T ... knocking down of UBE2T protein induced upregulation of BRCA1 protein ... whereas its overexpression caused the decrease of the BRCA1 protein"]. This is an overexpression/cancer-cell context; not the canonical FA-pathway function.
- In vitro (E3-free) assay of all human E2s: UBE2T can drive polyubiquitination through multiple ubiquitin lysines; UniProt summarizes "In vitro able to promote polyubiquitination using all 7 ubiquitin Lys residues, but may prefer 'Lys-11'-, 'Lys-27'-, 'Lys-48'- and 'Lys-63'-linked polyubiquitination (PubMed:20061386)." Source paper [PMID:20061386] was performed in the ABSENCE of E3 ("this study was performed in the absence of an E3 enzyme"), so the six lysine-linkage-specific BP annotations reflect intrinsic in-vitro lysine preference, not the physiological (monoubiquitination) role → over-annotation of biological role.
- GNB2 interaction (P62879) reported in a large-scale neurodegenerative-disease Y2H interactome [PMID:32814053]; also in UniProt INTERACTION. Non-core, generic protein binding.

## Annotation review synthesis
- CORE MF: ubiquitin conjugating enzyme (E2) activity GO:0061631.
- CORE BP: FANCD2/FANCI monoubiquitination in interstrand cross-link repair (FA pathway) → protein monoubiquitination GO:0006513; interstrand cross-link repair GO:0036297; DNA damage response GO:0006974.
- CORE CC: nucleus / nucleoplasm (functions on chromatin).
- CORE partner interaction: FANCL (ubiquitin protein ligase binding GO:0031625).
- Non-core: autoubiquitination (regulatory), polyubiquitination + lysine-linkage in-vitro capacities, BRCA1 downregulation (overexpression context), generic protein binding (FANCL redundant w/ GO:0031625; GNB2 HT screen).
- GO:0004842 (ubiquitin-protein transferase activity) IDA x4 → MODIFY to the more specific E2 term GO:0061631.
- GO:0006281 (DNA repair) IMP → MODIFY to GO:0036297 interstrand cross-link repair (MMC/ICL context).
</content>
</invoke>
