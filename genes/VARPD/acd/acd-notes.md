# Curation Notes for *Variovorax paradoxus* TBEA6 `acd` (`B9U6P5`, `SPCAD_VARPD`, `VPARA_05440`)

## Overview
- **UniProt Accession:** `B9U6P5` (`SPCAD_VARPD`)
- **Ordered Locus Name:** `VPARA_05440` (strain TBEA6 `acd`, `UniProtKB:B9U6P5`)
- **Gene Symbol:** `acd`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, characterized in strain TBEA6)
- **Protein Function:** 3-sulfinopropanoyl-CoA (3SP-CoA) desulfinase (`Acd`, 399 aa, EC 3.13.1.4), a neofunctionalized member of the acyl-CoA dehydrogenase (ACD) fold family that catalyzes the non-oxidative, hydrolytic C–S bond cleavage of 3-sulfinopropanoyl-CoA into propanoyl-CoA and sulfite (`SO3(2-)`), utilizing non-covalently bound FAD strictly as a structural cofactor rather than a redox cofactor.

## Literature & Biochemical Evidence
1. **Discovery in the 3,3'-Thiodipropionic Acid / 3-Sulfinopropionate Catabolic Pathway (`PMID:19001372`):**
   - Bruland, Wübbeler & Steinbüchel (2009) *J Biol Chem* 284:660–672 elucidated the catabolic pathway of 3,3'-thiodipropionic acid (TDP) and 3-sulfinopropionate (3SP) in *Variovorax paradoxus* TBEA6 via transposon mutagenesis and proteome analysis, identifying an acyl-CoA dehydrogenase-like protein (`acd`) essential for growth on TDP and 3SP (`PMID:19001372`).
2. **Direct Biochemical Characterization as a Non-Redox 3SP-CoA Desulfinase (`PMID:24317404`):**
   - Schürmann et al. (2014) *J Bacteriol* 196:882–893 purified and biochemically characterized `AcdTBEA6` (`B9U6P5`) alongside two other bacterial 3SP-CoA desulfinases and compared it directly against its paralog `AcdS110` (`C5CPU9`, `Vapar_1144`) from *V. paradoxus* S110 (`PMID:24317404`).
   - **Key experimental findings (`PMID:24317404`):**
     - `AcdTBEA6` (`B9U6P5`) catalyzes the irreversible hydrolytic desulfination of 3-sulfinopropionyl-CoA (3SP-CoA) to propionyl-CoA and sulfite (`SO3(2-)`) with $K_m = 0.052 \pm 0.008\text{ mM}$, $V_{\max} = 3.47 \pm 0.16\text{ }\mu\text{mol min}^{-1}\text{ mg}^{-1}$, and $k_{\text{cat}} = 2.5\text{ s}^{-1}$ (EC 3.13.1.4).
     - `AcdTBEA6` forms a homotetramer ($\sim 173\text{ kDa}$, subunit mass 42.99 kDa) containing one non-covalently bound FAD molecule per monomer (`UV-Vis` absorption maxima at 365 nm and 445 nm). Although the reaction involves no net electron transfer, the FAD prosthetic group is essential for maintaining the native homotetrameric quaternary structure (`PMID:24317404`).
     - Crucially, `AcdTBEA6` was tested for canonical acyl-CoA dehydrogenase activity against propionyl-CoA, butyryl-CoA, isobutyryl-CoA, valeryl-CoA, isovaleryl-CoA, glutaryl-CoA, and succinyl-CoA and exhibited **zero dehydrogenase activity with any tested acyl-CoA thioester** (`PMID:24317404`).
     - Conversely, its sequence homolog `AcdS110` (`C5CPU9`, `Vapar_1144`) from *V. paradoxus* S110 exhibited canonical isobutyryl-CoA / butyryl-CoA / valeryl-CoA dehydrogenase activity and **could not desulfinate 3SP-CoA** (`PMID:24317404`).
     - Sequence alignment against the prototype desulfinase `Acd_DPN7` (`UniProtKB:K4L7X3`) revealed the molecular basis for this neofunctionalization ([PMID:24317404 "all three new 3SP-CoA desulfinases possess a glutamine residue corresponding to glutamine 246 in Acd DPN7"]; [PMID:24317404 "An arginine residue in a position corresponding to Arg84 in Acd DPN7 occurs in each of the novel desulfinases"]): in `AcdTBEA6` (`B9U6P5`), the catalytic glutamate base of canonical acyl-CoA dehydrogenases is replaced by `Gln247` (immediately upstream of conserved `Arg248` in `241-MTAYNAQRVG-250`; `Gln247` itself is not `FT`-annotated in `B9U6P5`, whereas `Tyr244-Asn245` carry `FT BINDING 244..245 /ligand="substrate"` inferred by similarity to `K4L7X3`), abolishing $\alpha,\beta$-dehydrogenation, while conserved `Arg84` (`FT SITE 84 /note="Important for activity"` in `B9U6P5`, corresponding to `Arg84` in `Acd_DPN7`) is positioned to coordinate the sulfino (`-SO2-`) group of 3SP-CoA (`PMID:24317404`, `UniProtKB:B9U6P5`).

## Review of Existing GOA Annotations (Major Curation Error Showcase!)
Because `AcdTBEA6` (`B9U6P5`) retains the canonical acyl-CoA dehydrogenase 3-domain fold (`Pfam:PF02771`, `PF02770`, `PF00441`; `PANTHER:PTHR43884`), automated pipelines (InterPro2GO, UniProtKB-KW, and PANTHER TreeGrafter) annotated it as a fatty acid $\beta$-oxidation / butyrate-degrading acyl-CoA dehydrogenase. Four of its 5 existing GOA rows are false positives directly refuted by `PMID:24317404`:
1. `GO:0003995` (`acyl-CoA dehydrogenase activity`, IEA via InterPro) -> **REMOVE** (directly refuted by `PMID:24317404`: `AcdTBEA6` lacks the catalytic glutamate base and shows no dehydrogenase activity toward any tested acyl-CoA substrate).
2. `GO:0016627` (`oxidoreductase activity, acting on the CH-CH group of donors`, IEA via InterPro / UniProtKB-KW) -> **REMOVE** (directly refuted by `PMID:24317404`: `AcdTBEA6` is a carbon-sulfur bond hydrolase [EC 3.13.1.4], not an oxidoreductase).
3. `GO:0033539` (`fatty acid beta-oxidation using acyl-CoA dehydrogenase`, IEA via TreeGrafter `PTN005188827`) -> **REMOVE** (TreeGrafter over-propagation; `AcdTBEA6` functions in 3,3'-thiodipropionate / 3-sulfinopropionate organosulfur catabolism, not fatty acid $\beta$-oxidation, `PMID:19001372`, `PMID:24317404`).
4. `GO:0046359` (`butyrate catabolic process`, IEA via TreeGrafter `PTN005188827`) -> **REMOVE** (TreeGrafter over-propagation; `AcdTBEA6` cannot oxidize butyryl-CoA, `PMID:24317404`).
5. `GO:0050660` (`flavin adenine dinucleotide binding`, IEA via InterPro / UniProtKB-KW) -> **ACCEPT** (confirmed by UV-Vis spectroscopy in `PMID:24317404`: binds 1 FAD molecule per subunit non-covalently as a structural cofactor).

## Proposed New Annotations & Ontology Terms
- **Proposed new MF term (`proposed_new_terms`):** `3-sulfinopropanoyl-CoA desulfinase activity` (EC 3.13.1.4, `RHEA:41560`), supported by `PMID:24317404` (GO currently lacks a dedicated Molecular Function term for non-oxidative sulfinylacyl-CoA desulfinases).
- `GO:0044273` (`sulfur compound catabolic process`) — `involved_in` (`IDA`), supported by purified enzyme assays in `PMID:24317404` and pathway context in `PMID:19001372`.
- `GO:0005829` (`cytosol`) — `located_in` (`IC`), supported by purification as a soluble homotetrameric intracellular enzyme lacking signal peptides or transmembrane spans (`PMID:24317404`).
