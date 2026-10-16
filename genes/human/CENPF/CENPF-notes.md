# CENPF review notes

## 2026-09-27 initial review (claude-code)

Sources: UniProt P49454, GOA (89 rows), cached publications. The Falcon deep-research
file was absent at the start and arrived mid-review; it was incorporated (see end).

### Identity and structure
- ~3114 aa coiled-coil protein (mitosin/CENP-F), C-terminal CAAX farnesylation, nuclear
  in S/G2, kinetochore corona from late G2 to anaphase, then spindle midzone/midbody;
  degraded after mitosis [PMID:7542657 "CENP-F is protein of the nuclear matrix that gradually accumulates during the cell cycle until it reaches peak levels in G2 and M phase cells and is rapidly degraded upon completion of mitosis"].
- Outer kinetochore plate [PMID:7904902 "CENP-F is localized to the kinetochore plates and specifically to the outer surface of the outer kinetochore plate"].
- Farnesylation needed for NE and kinetochore localization [PMID:12154071].

### Microtubule coupling at kinetochores
- Two MT-binding domains (N- and C-terminal) [PMID:23892111 "We have biochemically and structurally characterized the microtubule-binding properties of the amino- and carboxyl-terminal domains of CENP-F"];
  both track depolymerizing MT ends and transduce force [PMID:26101217 "identifying CENP-F as a highly effective coupler to shortening MTs"].
- Depletion: misalignment, reduced tension, unstable K-fibres [PMID:15870278; PMID:16252009 "a crucial role for CENP-F in efficient assembly of a stable microtubule-kinetochore interface"].
- Depletion does NOT affect S/G2 progression [PMID:16252009 "the absence of nuclear CENP-F does not affect cell cycle progression in S and G2"] -> G2/M regulation rows (overexpression of truncations) marked over-annotated.
- Kinetochore recruitment directly via BUB1 (and CENP-E) [PMID:29748388, PMID:29632243].

### Adaptor for NudE/NudEL-LIS1-dynein
- Kinetochores: Ndel1/Nde1/Lis1 kinetochore localization Cenp-F dependent [PMID:17600710 "A major function of Cenp-F, therefore, is to link the Ndel1/Nde1/Lis1/Dynein pathway to kinetochores."].
- Nuclear envelope (prophase/G2): NUP133 N-terminal beta-propeller binds CENP-F, which recruits NudE/EL and thereby dynein/dynactin; tethers centrosomes to NE [PMID:21383080 "Recent studies have demonstrated a role for CENP-F in indirectly recruiting dynein/dynactin to kinetochores via NudE and/or NudEL"]. Mapping of the NUP133/CENP-F interface [PMID:29632243].
- Rat brain RGPs: CENP-F RNAi arrests apical INM [PMID:24034252 "Nup133 and CENP-F RNAi each also severely inhibited apical INM"].
- Key point for the nucleokinesis module: dynein recruitment by CENP-F is INDIRECT (via NDE1/NDEL1). GO:0070840 dynein complex binding overstates a direct CENP-F-dynein contact; the better MF is an adaptor (GO:0030674 protein-macromolecule adaptor activity).
  The only IDA for GO:0070840 (PMID:12974617) is abstract-only and the abstract reports dynein-dependent poleward transport of CENP-F, not binding. Left UNDECIDED.

### Other roles
- Miro-dependent mitochondrial distribution at cytokinesis [PMID:26259702 "Miro and Cenp-F promote anterograde mitochondrial movement and proper mitochondrial distribution in daughter cells"].
- Cilia: subdistal appendages of mother centriole, ciliary axoneme with IFT88; Stromme syndrome / ciliopathy with microcephaly [PMID:25564561; PMID:26820108]. The IMP "ciliary transition fiber" is not what the paper shows (subdistal appendages; transition fibres derive from DISTAL appendages) -> MODIFY to GO:0120103.
- ATF4 repression [PMID:15677469], RB binding [PMID:7651420] - kept as non-core.

### Deep research incorporated (CENPF-deep-research-falcon.md, appeared mid-review)
- Adds Auckland et al. 2020 [PMID:32207772 "Taken together, these data demonstrate that CENP-F restricts dynein-stripping activity through a physical interaction with Nde1."]
  and Gassmann 2023 review (not cached): CENP-F is not required for bulk kinetochore dynein-dynactin recruitment. Reinforces the decision to keep GO:0070840 UNDECIDED and to prefer an adaptor MF.
- Adds Peterka & Kornmann 2019 [PMID:30856164 "We observe that, despite the phenotypes apparent in cultured cells, mutant mice develop normally."] - mitochondrial pool dispensable in mice; mitochondrial transport NEW kept as non-core only.
- Cancer-biomarker material in the report was not used (proliferation marker, not function).
