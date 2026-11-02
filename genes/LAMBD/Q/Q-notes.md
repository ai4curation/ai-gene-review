# Q (P03047) - Curation Notes

## Overview
- **Gene symbol**: `Q`
- **UniProt ID**: `P03047` (`ANTQ_LAMBD`)
- **Protein name**: Antitermination protein Q (Late gene regulator, 207 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Late gene transcription antitermination factor**: Lambda Q (207 AA) is a delayed-early regulatory protein that controls the switch to late lytic gene expression by modifying bacterial RNA polymerase (RNAP) initiating at the late promoter `PR'`. Without Q, transcripts from `PR'` terminate at `tR'` (`t6S`) to produce a short 194-nt 6S RNA; with Q, RNAP reads through `tR'` and all downstream terminators to transcribe the entire ~26 kb late operon encoding lysis, head, and tail morphogenesis proteins [PMID:18832144, "Through its association with RNAP, λQ renders RNAP resistant to transcription pausing and insensitive to downstream termination signals"].
- **DNA-mediated loading onto the sigma70-dependent paused early elongation complex**:
  - Unlike N (which loads via nascent `boxB` RNA), Q is a DNA-binding antiterminator that recognizes a specific DNA element (`qut`, Q-utilization site, located between `-30` and `-10` of `PR'`) while RNAP is paused at nucleotide `+16`/`+17` via sigma70 region 2 recognition of a `-10`-like pause element [PMID:24440517, "λQ binds to the paused early-elongation complex through interactions between λQ and two regions of RNA polymerase: region 4 of the σ(70) subunit and the flap region of the β subunit."].
  - During engagement, Q contacts sigma70 region 4 and directly binds the RNAP beta-flap tip helix, competing with sigma70 region 4 for the beta-flap and becoming a stable subunit of the elongating RNAP complex [PMID:18832144, "Here, we provide an explanation for this requirement by showing that lambdaQ establishes direct contact with the beta-flap during the engagement process, thus competing with sigma(70) region 4 for access to the beta-flap."].
- **Four-cysteine zinc-finger structural arm**: Crystal structure of the DNA- and RNAP-binding region of Q (`PMID:24440517`) shows a helix-turn-helix DNA-binding motif and an extended antiparallel beta-ribbon arm stabilized at its base by a structural zinc ion tetrahedrally coordinated by four cysteine residues (`Cys118`, `Cys121`, `Cys144`, `Cys147`) [PMID:24440517, "There is also a zinc ion bound at the base of the arm, coordinated by four cysteine residues (Cys118, Cys121, Cys144 and Cys147), which may be important for the structural integrity and/or flexibility of this arm."].
- **Direct interaction with host NusA**: Q also interacts directly with host elongation factor NusA via NusA's N-terminal domain (NTD) and acidic repeat 2 (AR2) domain, releasing NusA autoinhibition and stabilizing the protective nozzle at the RNAP RNA exit channel that blocks termination hairpin formation and Rho access [PMID:32313022, "We also provide evidence that multidomain protein NusA interacts directly with λQ via its N-terminal domain (NTD) and the acidic repeat (AR) 2 domain, with the λQ:NusA-AR2 interaction being able to release NusA autoinhibition."].

## Review of Existing GO Annotations
- `GO:0003677` (DNA binding, IEA, `GO_REF:0000120`): **ACCEPT**. Q binds specifically to the `qut` DNA site upstream of the `+16/+17` pause site at `PR'` via its helix-turn-helix domain (`PMID:24440517`).
- `GO:0006353` (DNA-templated transcription termination, IEA, `GO_REF:0000120`): **MODIFY** to `GO:0031564` (transcription antitermination), as Q prevents termination rather than promoting it.
- `GO:0006355` (regulation of DNA-templated transcription, IEA, `GO_REF:0000120`): **MODIFY** to `GO:0031564` (transcription antitermination), which is more specific and already experimentally annotated on Q.
- `GO:0008270` (zinc ion binding, IEA, `GO_REF:0000120`): **ACCEPT**. Directly verified by the X-ray crystal structure (`PMID:24440517`) showing a structural `Zn2+` ion coordinated by `Cys118`, `Cys121`, `Cys144`, and `Cys147`.
- `GO:0031564` (transcription antitermination, IDA `PMID:18832144` and IEA `GO_REF:0000104`): **ACCEPT** (both rows). Core biological process of Q.
- `GO:0046872` (metal ion binding, IEA, `GO_REF:0000043`): **MODIFY** to `GO:0008270` (zinc ion binding), which is more specific and already present on the gene.
