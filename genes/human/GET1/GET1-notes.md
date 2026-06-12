# GET1 (WRB) gene review notes

## Identity
- UniProt O00258, GET1_HUMAN, 174 aa. Gene symbol GET1 (HGNC:12790); synonyms WRB, CHD5 (congenital heart disease 5 protein), tryptophan-rich basic protein. [file:human/GET1/GET1-uniprot.txt "RecName: Full=Guided entry of tail-anchored proteins factor 1"]
- ER membrane protein with three predicted transmembrane helices and a cytosolic coiled-coil domain. [file:human/GET1/GET1-uniprot.txt "Multi-pass membrane protein"]; [file:human/GET1/GET1-uniprot.txt "REGION          39..97" / "Interaction with GET3/TRC40"]; [file:human/GET1/GET1-uniprot.txt "COILED          39..94"]
- Belongs to the WRB/GET1 family; structurally related to the Oxa1 superfamily of insertases. [file:human/GET1/GET1-uniprot.txt "Belongs to the WRB/GET1 family"]; [PMID:31417168 "WRB, a member of the recently proposed Oxa1 superfamily"]

## Core function: ER membrane insertase receptor for GET3/TRC40
- GET1/WRB is the ER-membrane receptor for the cytosolic ATPase GET3/TRC40 (Get3 in yeast), which delivers tail-anchored (TA) proteins. [PMID:21444755 "we have identified tryptophan-rich basic protein (WRB), also known as congenital heart disease protein 5 (CHD5), as the ER membrane receptor for TRC40/Asna1"]
- The coiled-coil domain (cytosolic, between TMD1 and TMD2) is the docking site for TRC40/GET3. [PMID:21444755 "We identify the coiled-coil domain of WRB as the binding site for TRC40/Asna1"]; [PMID:21444755 "the coiled-coil domain of WRB functions as the ER membrane docking site for TRC40"]
- A soluble coiled-coil domain competes with endogenous WRB and blocks TRC40-mediated TA insertion in vitro (dose-dependent, up to 92% reduction). [PMID:21444755 "WRBcc interfered with HZZ-RAMP4op insertion in a dose-dependent manner"]
- GET1/WRB acts together with CAMLG/GET2 as the mammalian receptor; the two are necessary and synergistic for insertion. [PMID:23041287 "CAML and WRB synergistically insert TA proteins into the membrane"]; [PMID:23041287 "identification of CAML and WRB as components of the TRC40 receptor complex represents a crucial mechanism for driving ER membrane insertion of TA proteins in mammalian cells"]
- WRB + CAML reconstituted into liposomes are sufficient to confer TA insertion competence. [PMID:27226539 "in vitro synthesized CAML and WRB together were sufficient to confer insertion competence to liposomes"]
- WRB/CAML is described directly as "an essential insertase for tail-anchored proteins in the endoplasmic reticulum." [PMID:32187542 "the WRB/CAML complex, an essential insertase for tail-anchored proteins in the endoplasmic reticulum (ER)"]

## GET complex / structure
- Component of the GET complex: GET1/WRB + CAMLG/GET2 + GET3/TRC40. [file:human/GET1/GET1-uniprot.txt "Component of the Golgi to ER traffic (GET) complex, which is composed of GET1/WRB, CAMLG/GET2 and GET3/TRC40"]
- Cryo-EM of human WRB/CAML/TRC40: WRB and CAML form a heterotetramer stabilized by phosphatidylinositol; GET3 binding supports heterotetramer formation. [PMID:32910895 "Get3 binding to the membrane insertase supports heterotetramer formation, and phosphatidylinositol binding at the heterotetramer interface stabilizes the insertase for efficient TA insertion in vivo"]; [file:human/GET1/GET1-uniprot.txt "GET1 and CAMLG form a heterotetramer which is stabilized by phosphatidylinositol binding and which binds to the GET3 homodimer"]
- Structural homology with YidC and the EMC implies a conserved insertion mechanism via a hydrophilic groove. [PMID:32910895 "Structural homology with YidC and the ER membrane protein complex (EMC) implicates an evolutionarily conserved insertion mechanism for divergent substrates utilizing a hydrophilic groove"]
- PDB structures: 6SO5 (EM 4.2 A), 8CQZ (X-ray 2.8 A, residues 38-97), 8CR1/8CR2 (EM). [file:human/GET1/GET1-uniprot.txt "PDB; 6SO5; EM"]

## Role in CAMLG topogenesis / protein stabilization
- WRB is required for correct topology and integration of its partner CAML into the ER; without WRB, CAML adopts aberrant topoforms that cluster and are degraded by the proteasome. [PMID:31417168 "without sufficient levels of WRB, CAML fails to adopt this topology, and is instead incompletely integrated to generate two aberrant topoforms; these congregate in ER-associated clusters and are degraded by the proteasome"]; [PMID:31417168 "WRB ... acts catalytically to assist the topogenesis of CAML"]
- WRB can correct the topology of CAML in vitro and in cells. [PMID:32187542 "When present, WRB can correct the topology of CAML both in vitro and in cells"]
- This is the basis for the "protein stabilization" (GO:0050821) IDA annotations (PMID:31417168, PMID:32187542): WRB stabilizes/correctly integrates CAML. WRB and CAML are mutually dependent for expression. [PMID:31417168 "WRB and CAML depend strictly on each other for expression"]
- Note GO term scoping: GO:0050821 "protein stabilization" is about preventing degradation/maintaining native conformation; WRB preventing CAML mis-folding/degradation is a reasonable but secondary (non-core) consequence of its insertase activity. Keep as non-core.

## Subcellular location
- ER membrane (experimental). [file:human/GET1/GET1-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]; [PMID:21444755 "WRB is an ER-resident membrane protein"]
- The original 1998 paper reported a predominantly NUCLEAR localization by immunofluorescence (source of GO:0005634 nucleus TAS, PMID:9544840). [PMID:9544840 "Immunofluorescence analysis shows a predominant localization in the cell nucleus"]
- This nuclear localization was NOT reproduced and is contradicted by the later, function-defining study, which establishes ER residence and could not detect nuclear WRB. [PMID:21444755 "when the subcellular localization of the WRB protein was characterized by immunofluorescence analysis with polyclonal antibodies (anti-peptide 33-46 of WRB), a positive signal was predominantly observed over the cell nucleus (Egeo et al., 1998). We have not been able to detect WRB in untransfected RPE-1 or HeLa cells using our anti-WRB antibodies"]
- Conclusion: GO:0005634 nucleus is superseded/incorrect. WRB is a multi-pass ER membrane protein with no established nuclear function; the 1998 result predates knowledge of the protein and is best treated as an over-annotation. Mark as over-annotated (do not retain as a real location).

## Interactions (IPI / protein binding)
- PMID:32296183 (Luck et al., human binary interactome / HuRI Y2H map): source of a large list of IntAct GO:0005515 partners (APOA2, TFRC, CD53, COMT, AQP1, HMOX2, SLC7A1, STX2-2, etc.). These are high-throughput Y2H hits; many are themselves TA/membrane proteins (plausible insertase substrates) but the bare "protein binding" term is uninformative. Keep as non-core.
- CAMLG (P49069) IPI interactions (PMID:31417168, PMID:32187542) reflect the genuine, functionally central WRB-CAML association, but the GO term used is the uninformative GO:0005515. Keep as non-core (the informative MF is captured by GO:0043495 / GET3-receptor activity, and complex membership by GO:0043529).

## Disease / development context (background, not core MF/BP)
- WRB/CHD5 maps to chromosome 21q22.3 within the Down syndrome congenital heart disease region. [PMID:9544840 "a new gene, WRB, that maps to 21q22.3"]; [PMID:21444755 "the human gene encoding WRB has been mapped to Down syndrome (DS) region-2 of chromosome 21 (21q22.3), within the congenital heart disease region"]
- Loss in model organisms causes cardiac and eye/retinal phenotypes (medaka, zebrafish pwi photoreceptor degeneration), consistent with pleiotropic effects of impaired TA-protein insertion. [PMID:21444755 "In zebrafish, a WRB mutant (pwi) showed photoreceptor-specific retinal degeneration"]

## Annotation review decisions (summary)
- GO:0071816 tail-anchored membrane protein insertion into ER membrane (IDA/IMP/IBA/IEA): ACCEPT — core BP.
- GO:0043495 protein-membrane adaptor activity (IBA): MODIFY is tempting but this is the standard PAN-GO MF for the GET3 receptor; keep as ACCEPT representing the membrane-insertase-receptor MF (this is the term GO_Central uses for GET1 orthologs). Core MF.
- GO:0043529 GET complex (IDA/IPI/IBA): ACCEPT — core CC.
- GO:0005789 ER membrane (EXP/NAS/IEA): ACCEPT — core CC.
- GO:0045048 protein insertion into ER membrane (IDA/IMP/NAS): ACCEPT (parent of GO:0071816; correct, slightly less specific). Core BP.
- GO:0090150 establishment of protein localization to membrane (IEA/ARBA): ACCEPT as correct generic parent (non-core).
- GO:0050821 protein stabilization (IDA x2): KEEP_AS_NON_CORE — refers to WRB-dependent correct integration/stabilization of CAML; real but secondary to insertase function.
- GO:0005515 protein binding (IPI x3 refs): KEEP_AS_NON_CORE — uninformative; includes functionally important CAMLG binding and HuRI Y2H hits.
- GO:0005634 nucleus (TAS, PMID:9544840): MARK_AS_OVER_ANNOTATED — superseded by ER localization; not reproduced.

## Falcon deep-research findings (incorporated 2026-06)
- GET1/WRB is an active insertase, not merely a receptor: reconstituted Get1/2 (WRB/CAML) forms a dynamic aqueous channel (~2.5 nm, ≈ two Get1/2 complexes) sealed by Get3, and channel activity is required to release TA proteins from Get3 for membrane insertion; it acts as both insertase (TMD insertion) and translocase (C-terminal hydrophilic tail). [PMID:36640319 "the Get1/2 channel functions as an insertase for insertion of TMDs and as a translocase for translocation of C-terminal hydrophilic segments"]. Strengthens GO:0071816 (added to supported_by).
- 2023 human GET insertase structures: the Get1/Get2/Get3 fold is conserved across eukaryotes and the insertase induces local lipid-bilayer thinning near the hydrophilic groove to lower the energetic barrier for TA insertion. [PMID:37963916 "thinning of the lipid bilayer occurs in the vicinity of the hydrophilic groove to presumably lower the energetic barrier of membrane insertion"]. Supports GET1/WRB's active, membrane-remodeling insertase role (added to supported_by for GO:0071816).
- Gating mechanism: the interaction between Get2 helix α3' and Get3 drives conformational changes in both Get3 and the Get1/Get2 membrane heterotetramer, providing a structural basis for how Get1 (WRB) coiled-coil engagement promotes Get3 opening and substrate handoff. [PMID:37963916 "the gating interaction between Get2 helix α3' and Get3 drives conformational changes in both Get3 and the Get1/Get2 membrane heterotetramer"].
- Pathway review (Farkas & Bohnsack 2021) frames GET1/WRB + CAMLG/GET2 as the obligate ER receptor-insertase that receives TA cargo from cytosolic GET3/TRC40; corroborates existing core-function calls. [PMID:34264263] (added as HIGH-relevance reference).
- Falcon also cites Jung & Zimmermann 2023 (IJMS) reporting a TA-insertase preference ordering "Wrb >> TRAM1 >> Sec61 > EMC > TRAP > Sec63" (proteomics, indirect) and Hagiwara 2023 (Biochem J) on upstream BAG6-UBL4A dissociation under proteotoxic stress; these are pathway-context/quality-control and were not added as GET1-specific structured references (no GET1-specific functional finding).
