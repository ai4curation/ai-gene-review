# Curation Notes for Mycobacteriophage L5 Gene XIS (Excisionase gp36, Q05246)

## Summary
- **Gene symbol**: `XIS` (synonym `36`)
- **UniProt ID**: `Q05246` (`VXIS_BPML5`, 56 aa, 6.3 kDa)
- **Domain architecture**: Contains a winged helix-turn-helix DNA-binding domain (`IPR041657` / `PF12728` `HTH_17`, `TIGR01764` `excise`).
- **Experimental characterization**:
  - **Identification and function** [PMID:10652095]: Identified gene `36` as the L5 excisionase (`Xis-L5`), a small (56 aa), heat-stable protein that strongly stimulates excisive recombination (`attL` x `attR`) both in vivo and in vitro.
  - **Mechanism of directionality control** [PMID:12581642]: Demonstrated that Xis-L5 binds cooperatively to four 10-bp direct repeat sites (`X1`–`X4`) located between the `P2` and `P3` arm-type integrase sites in `attR` (and `attP`), introduces a pronounced DNA bend, and promotes recruitment of Int-L5 to adjacent `P1`–`P2` arm sites to assemble the excisive `intasome-R` complex (together with host mIHF). Xis-L5 also inhibits Int-L5-mediated integrative recombination by preventing formation of a recombinogenic synaptic intermediate, acting purely as an architectural DNA-binding and DNA-bending factor.
- **Curation decisions**:
  - `GO:0003677` (`DNA binding`, IEA): `ACCEPT`. Directly supported by EMSA, footprinting, and DNA-bending experiments in [PMID:10652095, PMID:12581642].
  - `GO:0032359` (`provirus excision`, IDA `PMID:10652095` and IEA `GO_REF:0000043`): `ACCEPT`. Both rows represent the core biological process of Xis-L5.
  - `GO:0006310` (`DNA recombination`, IEA): `TOO_GENERAL`. Entailed by `GO:0032359` (`provirus excision`); furthermore, Xis-L5 is a non-catalytic architectural accessory factor that directs Int-L5 toward prophage excision rather than catalyzing strand exchange itself.
