# rhp51 (Rad51) — S. pombe — review notes

UniProt P36601 (RAD51_SCHPO), gene SPAC644.14c. PomBase standard name now `rad51` (synonym rhp51).
365 aa. RecA family, RAD51 subfamily. The central RecA-family recombinase of homologous recombination (HR) in fission yeast. "rhp" = rad homolog pombe.

## Core biochemistry (purified protein, in vitro)
[PMID:15899844 "Purified Rad51 and Dmc1 form homo-oligomers, bind single-stranded DNA preferentially, and exhibit DNA-stimulated ATPase activity. Both Rad51 and Dmc1 promote the renaturation of complementary single-stranded DNA. Importantly, Rad51 and Dmc1 proteins catalyze ATP-dependent strand exchange reactions with homologous duplex DNA. Electron microscopy reveals that both S. pombe Rad51 and Dmc1 form nucleoprotein filaments. Rad51 formed helical nucleoprotein filaments on single-stranded DNA"]
- Establishes: ssDNA binding, dsDNA binding, ATP binding, DNA-dependent ATPase (ATP-dependent activity acting on DNA), DNA strand exchange/recombinase activity, homo-oligomerization, nucleoprotein filament (DNA recombinase assembly).

UniProt FUNCTION: "Required both for recombination and for the repair of DNA damage caused by X-rays. Binds to single and double-stranded DNA, in the presence of magnesium, and exhibits DNA-dependent ATPase activity. Promotes DNA strand annealing and strand exchange via DNA recombinase activity and forms helical nucleoprotein filaments." {ECO:0000269|PubMed:15899844}

ATP binding site FT BINDING 149..156 (Walker A / P-loop). ATP hydrolysis: NAS (GO_REF S. pombe keyword mapping) but supported by DNA-stimulated ATPase in PMID:15899844.

## Mediators / strand-exchange stimulation
Swi5-Sfr1 complex stimulates Rhp51-mediated strand exchange in vitro:
[PMID:16921379 "the Schizosaccharomyces pombe Swi5-Sfr1 complex, a conserved eukaryotic protein complex, at substoichiometric concentrations stimulates strand exchange mediated by Rhp51 (the S. pombe Rad51 homolog) and Dmc1 on long DNA substrates. ... the Swi5-Sfr1 complex preferentially stimulates the ssDNA-dependent ATPase activity of Rhp51"]
Structure of activator:
[PMID:22405003 "Rad51 forms a helical filament on single-stranded DNA and promotes strand exchange between two homologous DNA molecules during homologous recombination. The Swi5-Sfr1 complex interacts directly with Rad51 and stimulates strand exchange. ... suitable for transient binding within the helical groove of the Rad51 filament"] — also IDA ssDNA binding + Swi5-Sfr1 complex binding.

Strand exchange mechanism (real-time, three-strand intermediates):
[PMID:29323270 "strand exchange by fission yeast Rad51 proceeds via two distinct three-strand intermediates, C1 and C2. Both intermediates contain Rad51 ... Swi5-Sfr1 ... facilitates the C1-C2 transition and subsequent ssDNA release from C2 to complete strand exchange in an ATP-hydrolysis-dependent manner"] — meiotic strand invasion IDA; dsDNA & ssDNA binding IDA.
[PMID:39340300 "The Swi5-Sfr1 complex in fission yeast, a conserved auxiliary factor, stimulates DNA strand exchange driven by both Dmc1 and Rad51. ... Swi5-Sfr1 facilitates the C1-C2 transition and releases single-stranded DNA (ssDNA) from C2, acting as a strand exchange activator."] — Swi5-Sfr1 complex binding EXP.

## In vivo / genetic roles
DSB repair via HR (HO-induced DSB on minichromosome):
[PMID:12628934 "the homologous recombination (HR) genes rhp51(+), rad22A(+), rad32(+) and the nucleotide excision repair gene rad16(+) were required for efficient interchromosomal gene conversion"] — DSB repair via HR IMP.

Meiotic DSB repair:
[PMID:15238514 "Rhp51, Swi5, and Rad22 + Rti1 were required for full levels of DNA repair in S. pombe"] — DSB repair involved in meiotic recombination IMP.

Telomere maintenance (Ku-independent):
[PMID:12930956 "the rearrangements of telomere-associated sequences in pku80+ mutants are Rhp51 dependent ... Rhp51 binds to the G-rich overhang and promotes homologous pairing between two different telomere ends in the absence of Ku heterodimer"] — telomere maintenance IGI (with pku80, SPBC543.03c). Note: role is conditional (absence of Ku), but it is a genuine role in telomere maintenance.

Centromere stability / GCR suppression:
[PMID:18923422 "the deletion of Rad51 recombinase preferentially elevates isochromosome formation. Chromatin immunoprecipitation analysis shows that Rad51 localizes at centromere around S phase. These data suggest that Rad51 suppresses rearrangements of centromere repeats"] — localizes at centromeric region IDA.

Replication fork processing / restart of arrested forks:
[PMID:23093942 "the restart of collapsed or broken replication forks is dependent upon homologous recombination" ; system shows HR-dependent recovery of RTS1-arrested forks is error-prone] — mitotic recombination-dependent replication fork processing IMP.
[PMID:28475874 "Rad52 and the DNA binding activity of Rad51, but not its strand-exchange activity, act to protect terminally arrested forks from unrestrained Exo1-nucleolytic activity"] — replication fork processing EXP (fork protection).
[PMID:33159083 "relocation of arrested forks to NPCs occurred after Rad51 loading and its enzymatic activity"] — stalled replication fork localization to nuclear periphery IMP.

Interstrand crosslink repair:
[PMID:24192486 Fan1/Pli1 ICL pathways; rhp51 involved] — recombinational interstrand cross-link repair IMP.

Regulation of Rad51 by Rrp1 (translocase + E3 ligase) — also nuclear localization + ubiquitination:
[PMID:34157114 "Rrp1 directly interacts with Rad51 and removes it from double-stranded DNA ... Rrp1 affects Rad51 binding at centromeres. ... Rrp1 possesses E3 ubiquitin ligase activity with Rad51 as a substrate"] — nucleus EXP; dsDNA & ssDNA binding IDA; protein binding (rrp1, O13762) IPI; ubiquitinated by rrp1.

Fbh1 regulation:
[PMID:25165823 "Fbh1-Skp1 complex ... inhibited Rad51-driven DNA strand exchange by disrupting Rad51 nucleoprotein filaments ... SCFFbh1 E3 ligase efficiently promotes ubiquitination of Rad51"] — ssDNA binding IDA; DNA recombination IDA.

Mating-type switching / recombination repair sub-pathways:
[PMID:14663140 "the fission yeast swi5+ gene ... is involved in a previously uncharacterized Rhp51 (Rad51sp)-dependent recombination repair pathway that does not require the Rhp55/57 ... the Swi5-Swi2-Rhp51 interactions may function, together with chromodomain protein Swi6 (HP1 homolog), in mating-type switching"] — mating type switching IGI (with swi2, SPBC409.03); protein binding swi2 (Q10668) & sfr1 (Q9USV1).

Foci at sites of DSB after IR; Cdc2-cyclin B influences Rhp51 focus formation:
[PMID:12023299 "a defect in Cdc2 kinase activity ... affects the formation of Rhp51 (Rad51(sp)) foci in response to ionizing radiation in a process that is redundant with the function of Rad50"] — site of double-strand break IDA.

MCM interaction at forks:
[PMID:18180284 MCM proteins interact with checkpoint and recombination proteins; Rhp51 focus formation] — site of double-strand break IDA; protein binding (mcm, SPCC16A11.17).

## Interactions (IPI partners)
- Rad22/Rad52 (P36592): PMID:11560889, PMID:12050150, PMID:14551247, PMID:23695164. Direct physical interaction (PMID:12050150).
- Rti1 (O42905): PMID:11560889, PMID:14551247.
- Rhp54/Rad54 (P41410): PMID:11560889, PMID:14551247, PMID:23695164.
- Swi2 (Q10668): PMID:14663140.
- Sfr1 (Q9USV1): PMID:14663140, PMID:16921379, PMID:22405003, PMID:23695164. (part of Swi5-Sfr1; better captured by Swi5-Sfr1 complex binding GO:1905334.)
- Rrp1 (O13762): PMID:34157114.
- Rad22 via SUMO study (SPBC660.13c = pli1? actually): PMID:11600706 lists SPBC660.13c.
- MCM (SPCC16A11.17): PMID:18180284.
- Swi5 (SPBC28F2.07) / Sfr1 (SPBC409.03): PMID:16921379, PMID:22405003.
- Ubc9/hus5 cross study PMID:8610150 — this is a MAMMALIAN study (HsUbc9 interacts with mammalian Rad51). The IPI here (PomBase, with SPAC30D11.13 = hus5) is by PomBase inference to pombe ortholog; treat cautiously, keep as protein binding -> generalize.
- PMID:23695164 cross-species interactome (Sci Signal) — high-throughput Y2H, partners Rad22/Rhp54/Sfr1.

## CC summary
- Nucleus (EXP PMID:34157114; HDA PMID:16823372).
- Nuclear envelope (HDA PMID:16823372) — likely a localization captured in global study; Rad51 relocates arrested forks to nuclear periphery/NPC (PMID:33159083) so peripheral/NE signal is biologically plausible but HDA-level.
- Site of double-strand break (IDA, PMID:12023299, PMID:18180284) — Rad51 foci.
- Chromosome, centromeric region (IDA PMID:18923422).
- Chromatin (NAS), condensed nuclear chromosome (IBA), chromosome (IEA).

## Curation decisions summary
- Core MF: ssDNA binding, dsDNA binding, ATP binding, ATP-dependent activity acting on DNA (DNA-dependent ATPase), DNA strand exchange activity, ATP hydrolysis. ACCEPT experimental; ACCEPT/KEEP IBA; IEA duplicates accept.
- DNA recombinase assembly (filament formation): ACCEPT.
- Swi5-Sfr1 complex binding: ACCEPT (specific, informative).
- protein binding GO:0005515 (bare): MODIFY where a more informative term exists, otherwise the partner-specific physical interactions are real but uninformative as bare "protein binding"; per guidelines avoid bare protein binding. Mark these for replacement with identical protein binding (self) or note adaptor/mediator interactions. For most IPI partner annotations, KEEP_AS_NON_CORE or MODIFY toward more specific function is not always possible; the underlying interaction is real -> ACCEPT but note bare term is uninformative. I will MODIFY the self-interaction protein binding entries are already captured by identical protein binding. For partner interactions, ACCEPT (real, experimentally supported) but flag uninformative.
- identical protein binding / protein homooligomerization: ACCEPT (filament).
- Core BP: DNA recombination, DSB repair via HR, meiotic DSB repair, meiotic strand invasion, DNA strand invasion, replication fork processing, mitotic recombination-dependent replication fork processing, mitotic recombination. ACCEPT.
- telomere maintenance: KEEP_AS_NON_CORE (conditional, Ku-absence). IEA ARBA telomere maintenance — ACCEPT as supported by IGI.
- mating type switching: KEEP_AS_NON_CORE (indirect, via recombination repair; Rhp51 needed because MTS uses recombination-based switching).
- ICL repair: KEEP_AS_NON_CORE.
- stalled fork localization to nuclear periphery: ACCEPT (specific phenotype).
- chromosome organization involved in meiotic cell cycle (IBA): KEEP_AS_NON_CORE (high-level).
- nuclear envelope (HDA): KEEP_AS_NON_CORE (localization, not primary site of action).
- DNA repair, DNA metabolic process, DNA binding, nucleotide binding (IEA high-level): MARK as generic/over-broad -> KEEP_AS_NON_CORE or MODIFY to more specific (DNA binding -> already have ssDNA/dsDNA). These are accurate but redundant/generic.
- ATP-dependent DNA damage sensor activity GO:0140664 (IEA InterPro): MODIFY/REMOVE — Rad51 is a recombinase, not a damage sensor; this is an InterPro over-propagation. Use MARK_AS_OVER_ANNOTATED.
