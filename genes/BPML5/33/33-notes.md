# Curation Notes for Mycobacteriophage L5 Gene 33 (Integrase Int-L5, P22884)

## Summary
- **Gene symbol**: `33` (synonym `int`)
- **UniProt ID**: `P22884` (`VINT_BPML5`, 371 aa, 41.8 kDa)
- **Domain architecture**: N-terminal arm-type DNA-binding domain (`IPR058717` / `PF26003` `Integrase_N_phage`), central core-binding (CB) domain (`IPR044068`, residues 73–151), and C-terminal tyrosine recombinase catalytic domain (`IPR002104` / `PF00589`, residues 171–362, with active-site Tyr-349 forming the covalent 3'-phosphotyrosyl DNA intermediate).
- **Experimental characterization**:
  - **Discovery & in vivo integration** [PMID:1901654, PMID:8459766]: Identified the L5 `int` gene (`33`) and `attP` site; showed that Int-L5 mediates site-specific integration into the `attB` site overlapping a host `tRNA-Gly` gene in *Mycobacterium smegmatis*, *M. tuberculosis*, and BCG.
  - **In vitro integrative recombination** [PMID:8226625]: Purified L5 integrase mediates site-specific recombination in vitro when stimulated by a mycobacterial host factor.
  - **Strand exchange and attB mapping** [PMID:8808947]: Mapped the 43-bp common core overlapping the host `tRNA-Gly` gene and defined the 29-bp minimal `attB` site and 7-bp overlap region of strand exchange.
  - **Host factor mIHF** [PMID:8986825]: Identified mycobacterial integration host factor (mIHF), which promotes specific Int-mIHF-`attP` intasome complex assembly.
  - **Intasome architecture** [PMID:9882658]: Demonstrated that Int-L5 forms intramolecular bridges between arm-type sites P4-P5 and the `attP` core (assisted by mIHF-induced DNA bending) while arm sites P1-P2 mediate `attB` capture.
  - **Excisive recombination** [PMID:10652095, PMID:12581642]: Int-L5 also catalyzes prophage excision (`attL` x `attR` -> `attP` + `attB`) in a reaction requiring both mIHF and the phage-encoded excisionase Xis (gp36, `Q05246`), which binds X1-X4 sites in `attR` to assemble `intasome-R`.
- **Curation decisions**:
  - `GO:0003677` (`DNA binding`, IEA): `ACCEPT`. Int-L5 is a bivalent DNA-binding protein that binds arm-type (P1-P7) and core-type (`attP`/`attB`) DNA sites [PMID:8986825, PMID:9882658].
  - `GO:0008979` (`prophage integrase activity`, IDA `PMID:8226625`): `ACCEPT` (and add `NEW` `GO:0008907` `integrase activity` if needed for `core_functions`).
  - `GO:0044826` (`viral genome integration into host DNA`, IEA): `ACCEPT`.
  - `GO:0075713` (`establishment of integrated proviral latency`, IEA): `ACCEPT`.
  - `GO:0032359` (`provirus excision`): `NEW` (IDA from `PMID:12581642` and `PMID:10652095`).
  - `GO:0006310` (`DNA recombination`, IEA): `TOO_GENERAL` (entailed by `GO:0044826`, `GO:0075713`, and `GO:0032359`).
  - `GO:0015074` (`DNA integration`, IEA): `TOO_GENERAL` (entailed by `GO:0044826` and `GO:0075713`).
  - `GO:0016740` (`transferase activity`, IEA): `TOO_GENERAL` (entailed by `GO:0008907` `integrase activity`).
  - `GO:0016787` (`hydrolase activity`, IEA): `REMOVE` (tyrosine recombinases catalyze concerted transesterification via a 3'-phosphotyrosyl intermediate without net hydrolysis of phosphodiester bonds).
  - `GO:0046718` (`symbiont entry into host cell`, IEA): `REMOVE` (false-positive keyword mapping; Int-L5 acts intracellularly on phage and host DNA after infection and does not mediate host cell entry).
