# PDX3 (YBR035C, P38075) notes

## Identity
- Pyridoxamine 5'-phosphate oxidase (PNPOx), EC 1.4.3.5, FMN-dependent; PNPOx family with both PF01243 (PNPOx_N) and PF10590 (PNP_phzG_C) domains; crystal structure 1CI0 (homodimer with 2 FMN) [UniProt:P38075].
- Paralog-like YLR456W and YPR172W carry only PF01243 and are NOT PNP/PMP oxidases [PMID:26327315 "Different experimental approaches indicated that neither protein catalyzes PLP formation nor binds FMN."] -- relevant to the module: only Pdx3 is the yeast PNPOx.

## Function
- Original genetic/biochemical identification: aux30 (pdx3) mutants lack P(N/M)P oxidase activity and cannot use pyridoxine, but grow on pyridoxal or pyridoxamine [PMID:7896706 "These mutants are characterized by a lack in pyridoxine (pyridoxamine) phosphate oxidase [P(N/M)P oxidase] (EC 1.4.3.5) activity."]. Pleiotropic phenotypes (heme/sterol uptake) are downstream of PLP shortage.
- Recombinant Pdx3 binds FMN and oxidises PNP to PLP [PMID:26327315 "On the other hand, Pdx3 recombinant protein exhibits all expected properties of a bona fide P(N/M)P oxidase."; "Note that purified Pdx3 presents the characteristic yellow color of proteins that are bound to FMN."].

## Localization
- Found in the mitochondrial intermembrane space proteome (Bax-release SILAC) [PMID:22984289]; previous localization "Unknown" in that table. Whether there is also a cytosolic pool is not established.

## Pathway
- Yeast makes PLP de novo via Snz1/Sno1 (directly), so Pdx3 functions in salvage (PNP/PMP -> PLP), downstream of the kinase Bud16. InterPro2GO "pyridoxine biosynthetic process" reflects bacterial PdxH context and is not appropriate here.
