---
title: "PSEPK transport/membrane/efflux: Ion, metal, and antiporter systems"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK transport/membrane/efflux: Ion, metal, and antiporter systems

Deeper partition created in projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv because the 102-gene parent bucket mixes true cation transporters with redox, metalloenzyme, and envelope side nodes. Completed sub-splits include the 26-gene monovalent cation/potassium split in modules/monovalent_cation_antiporter_boundary.yaml, the five-gene P-type metal ATPase split in modules/p_type_metal_atpase_transport_boundary.yaml, and the three-gene chromate/fluoride/inorganic-channel split in modules/inorganic_ion_channel_resistance_boundary.yaml, and the 15-gene transition-metal/Mg/Co transporter split in modules/transition_metal_magnesium_cobalt_transport_boundary.yaml. The 14-gene sodium-solute/MATE split is first-pass curated in modules/sodium_solute_symporter_mate_boundary.yaml. The 14-gene membrane metalloenzyme/envelope side-node split is first-pass curated in modules/transport_membrane_enzyme_spillover_boundary.yaml. The 25-gene membrane redox/electron-transfer spillover split is first-pass curated in modules/membrane_redox_electron_transfer_boundary.yaml. All ion/metal sub-splits are now first-pass curated.

| Gene | Ordered locus | UniProt | Protein | Review | Asta |
|---|---|---|---|---|---|
| `PP_0026` | `PP_0026` | `Q88RV3` | Cobalt/cadmium/zinc exporter | CURATED | PRESENT |
| `cadA-I` | `PP_0041` | `Q88RT8` | P-type Zn(2+) transporter (EC 7.2.2.12) | CURATED | PRESENT |
| `trkA` | `PP_0065` | `Q88RR4` | Trk system potassium uptake protein TrkA | CURATED | PRESENT |
| `PP_0093` | `PP_0093` | `Q88RN6` | Zinc protease protein | CURATED | PRESENT |
| `PP_0111` | `PP_0111` | `Q88RL8` | Electron transport protein SCO1/SenC | CURATED | PRESENT |
| `PP_0125` | `PP_0125` | `Q88RK4` | Cytochrome c-type protein | CURATED | PRESENT |
| `cc` | `PP_0126` | `Q88RK3` | Cytochrome c4 | CURATED | PRESENT |
| `PP_0144` | `PP_0144` | `Q88RI5` | Metalloprotease, insulinase family | CURATED | PRESENT |
| `PP_0180` | `PP_0180` | `Q88RF0` | Cytochrome c family protein | CURATED | PRESENT |
| `PP_0496` | `PP_0496` | `Q88QJ5` | Sodium/alanine symporter | CURATED | PRESENT |
| `PP_0569` | `PP_0569` | `Q88QC5` | MATE efflux family protein | CURATED | PRESENT |
| `cadA-II` | `PP_0586` | `Q88QA8` | P-type Cu(+) transporter (EC 7.2.2.8) | CURATED | PRESENT |
| `PP_0629` | `PP_0629` | `Q88Q67` | Cobalt transport protein CbiM | CURATED | PRESENT |
| `PP_0670` | `PP_0670` | `Q88Q28` | Transporter, bile acid/Na+ symporter family | CURATED | PRESENT |
| `PP_0683` | `PP_0683` | `Q88Q15` | Cation transporter | CURATED | PRESENT |
| `kefB-I` | `PP_0713` | `Q88PY5` | Kef-type potassium/proton antiporter, CPA2 family | CURATED | PRESENT |
| `hmp` | `PP_0808` | `Q88PP0` | Flavohemoprotein (Flavohemoglobin) (Hemoglobin-like protein) (Nitric oxide dioxygenase) (NO oxygenase) (NOD) (EC 1.14.12.17) | CURATED | PRESENT |
| `PP_0928` | `PP_0928` | `Q88PC2` | K+-dependent Na+/Ca+ exchanger related-protein | CURATED | PRESENT |
| `PP_0947` | `PP_0947` | `Q88PA3` | ZIP family metal transporter | CURATED | PRESENT |
| `gltS` | `PP_0996` | `Q88P57` | Sodium/glutamate symporter | CURATED | PRESENT |
| `arcD-I` | `PP_1002` | `Q88P51` | Arginine-ornithine antiporter | CURATED | PRESENT |
| `arcD-II` | `PP_1003` | `Q88P50` | Arginine-ornithine antiporter | CURATED | PRESENT |
| `cumA` | `PP_1034` | `Q88P19` | Multicopper oxidase (EC 1.10.3.-) | CURATED | PRESENT |
| `PP_1083` | `PP_1083` | `Q88NX0` | Bacterioferritin-associated ferredoxin | CURATED | PRESENT |
| `PP_1124` | `PP_1124` | `Q88NT0` | Copper resistance protein D domain-containing protein | CURATED | PRESENT |
| `nhaA1` | `PP_1132` | `Q88NS2` | Na(+)/H(+) antiporter NhaA 1 (Sodium/proton antiporter NhaA 1) | CURATED | PRESENT |
| `kup` | `PP_1200` | `Q88NK7` | Probable potassium transport system protein Kup | CURATED | PRESENT |
| `PP_1227` | `PP_1227` | `Q88NI2` | Membrane protein | CURATED | PRESENT |
| `PP_1467` | `PP_1467` | `Q88MV1` | NhaP-type Na+(K+)/H+ antiporter | CURATED | PRESENT |
| `PP_1526` | `PP_1526` | `Q88MP4` | Beta-monoglucosyldiacylglycerol synthase (EC 2.4.1.336) (UDP-glucose:1,2-diacylglycerol 3-beta-D-glucosyltransferase) | CURATED | PRESENT |
| `PP_1587` | `PP_1587` | `Q88MI4` | NhaP-type Na+/H+ and K+/H+ antiporters | CURATED | PRESENT |
| `rseP` | `PP_1598` | `Q88MH3` | Zinc metalloprotease (EC 3.4.24.-) | CURATED | PRESENT |
| `fdxA` | `PP_1625` | `P0A122` | Ferredoxin 1 | CURATED | PRESENT |
| `actP-I` | `PP_1743` | `Q88M32` | Cation/acetate symporter ActP (Acetate permease) (Acetate transporter ActP) | CURATED | PRESENT |
| `wbpL` | `PP_1804` | `Q88LX3` | Glycosyl transferase WbpL | CURATED | PRESENT |
| `PP_1836` | `PP_1836` | `Q88LU1` | Metal transporter, ZIP family | CURATED | PRESENT |
| `PP_1838` | `PP_1838` | `Q88LT9` | Sulfatase N-terminal domain-containing protein | CURATED | PRESENT |
| `PP_1841` | `PP_1841` | `Q88LT6` | Cytochrome c family protein | CURATED | PRESENT |
| `PP_1843` | `PP_1843` | `Q88LT4` | Mg2+/Co2+ transporter | CURATED | PRESENT |
| `htpX` | `PP_1871` | `Q88LQ8` | Protease HtpX (EC 3.4.24.-) (Heat shock protein HtpX) | CURATED | PRESENT |
| `PP_2010` | `PP_2010` | `Q88LC5` | Cytochrome b561 | CURATED | PRESENT |
| `cmaX` | `PP_2085` | `Q88L50` | CmaX protein | CURATED | PRESENT |
| `mrpG` | `PP_2225` | `Q88KR5` | Multicomponent potassium-proton antiporter, subunit G | CURATED | PRESENT |
| `mrpF` | `PP_2226` | `Q88KR4` | K(+)/H(+) antiporter subunit F | CURATED | PRESENT |
| `mrpE` | `PP_2227` | `Q88KR3` | Multicomponent potassium-proton antiporter, subunit E | CURATED | PRESENT |
| `mrpD` | `PP_2228` | `Q88KR2` | K(+)/H(+) antiporter subunit D | CURATED | PRESENT |
| `mrpC` | `PP_2229` | `Q88KR1` | K(+)/H(+) antiporter subunit C | CURATED | PRESENT |
| `mrpAB` | `PP_2230` | `Q88KR0` | K(+)/H(+) antiporter subunit A/B | CURATED | PRESENT |
| `PP_2556` | `PP_2556` | `Q88JU1` | Chromate transporter | CURATED | PRESENT |
| `mgtA` | `PP_2645` | `Q88JK4` | Magnesium-transporting ATPase, P-type 1 (EC 7.2.2.14) (Mg(2+) transport ATPase, P-type 1) | CURATED | PRESENT |
| `PP_2675` | `PP_2675` | `Q88JH4` | Cytochrome c-type protein | CURATED | PRESENT |
| `actP-II` | `PP_2797` | `Q88J52` | Cation/acetate symporter ActP (Acetate permease) (Acetate transporter ActP) | CURATED | PRESENT |
| `PP_2886` | `PP_2886` | `Q88IW3` | Cytochrome b561 | CURATED | PRESENT |
| `PP_2893` | `PP_2893` | `Q88IV6` | Translocation and assembly module TamB C-terminal domain-containing protein | CURATED | PRESENT |
| `PP_2955` | `PP_2955` | `Q88IP4` | Magnesium/cobalt transporter, CorA family | CURATED | PRESENT |
| `PP_2968` | `PP_2968` | `Q88IN1` | Nickel/cobalt efflux system | CURATED | PRESENT |
| `PP_2974` | `PP_2974` | `Q88IM5` | Sulfatase | CURATED | PRESENT |
| `ybhN` | `PP_3263` | `Q88HU0` | Phospholipid modification enzyme | CURATED | PRESENT |
| `actP-III` | `PP_3272` | `Q88HT1` | Cation/acetate symporter ActP (Acetate permease) (Acetate transporter ActP) | CURATED | PRESENT |
| `PP_3293` | `PP_3293` | `Q88HR0` | Potassium channel domain-containing protein | CURATED | PRESENT |
| `kefB-II` | `PP_3311` | `Q88HP2` | Glutathione-regulated potassium/H+ antiporter | CURATED | PRESENT |
| `PP_3331` | `PP_3331` | `Q88HM3` | Sodium:proline symporter | CURATED | PRESENT |
| `PP_3332` | `PP_3332` | `Q88HM2` | Cytochrome c-type protein | CURATED | PRESENT |
| `cbtA` | `PP_3408` | `A0A140FWF2` | Cobalt transporter subunit A | CURATED | PRESENT |
| `PP_3543` | `PP_3543` | `Q88H22` | Iron-sulfur cluster-binding protein | CURATED | PRESENT |
| `PP_3556` | `PP_3556` | `Q88H09` | Sodium:proton antiporter | CURATED | PRESENT |
| `PP_3928` | `PP_3928` | `Q88FZ8` | Nickel/cobalt transporter regulator | CURATED | PRESENT |
| `yfbS` | `PP_3931` | `Q88FZ5` | Transporter | CURATED | PRESENT |
| `trkH-I` | `PP_3953` | `Q88FX4` | Trk system potassium uptake protein | CURATED | PRESENT |
| `nhaA2` | `PP_3958` | `Q88FW9` | Na(+)/H(+) antiporter NhaA 2 (Sodium/proton antiporter NhaA 2) | CURATED | PRESENT |
| `fluC` | `PP_4001` | `Q88FT1` | Fluoride-specific ion channel FluC | CURATED | PRESENT |
| `nhaB` | `PP_4031` | `Q88FQ6` | Na(+)/H(+) antiporter NhaB (Sodium/proton antiporter NhaB) | CURATED | PRESENT |
| `PP_4203` | `PP_4203` | `Q88F95` | Electron transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO) (EC 1.5.5.1) | CURATED | PRESENT |
| `PP_4259` | `PP_4259` | `Q88F40` | Iron-sulfur cluster-binding protein | CURATED | PRESENT |
| `PP_4261` | `PP_4261` | `Q88F38` | Cation-transporting P-type ATPase | CURATED | PRESENT |
| `PP_4263` | `PP_4263` | `Q88F36` | Membrane-bounded cytochrome biogenesis cycZ-like domain, copper tolerance protein | CURATED | PRESENT |
| `PP_4289` | `PP_4289` | `Q88F11` | Cytochrome c domain-containing protein | CURATED | PRESENT |
| `PP_4304` | `PP_4304` | `Q88EZ6` | Cation transporter, VIC family | CURATED | PRESENT |
| `ccmE` | `PP_4323` | `Q88EX9` | Cytochrome c-type biogenesis protein CcmE (Cytochrome c maturation protein E) (Heme chaperone CcmE) | CURATED | PRESENT |
| `mgtE` | `PP_4471` | `Q88EJ1` | Magnesium transporter MgtE | CURATED | PRESENT |
| `trkH-II` | `PP_4507` | `Q88EF8` | Trk system potassium uptake protein | CURATED | PRESENT |
| `PP_4524` | `PP_4524` | `Q88EE1` | Sodium-solute symporter | CURATED | PRESENT |
| `ypfJ` | `PP_4657` | `Q88E11` | Zinc metalloprotease | CURATED | PRESENT |
| `msrQ` | `PP_4675` | `Q88DZ3` | Protein-methionine-sulfoxide reductase heme-binding subunit MsrQ (Flavocytochrome MsrQ) | CURATED | PRESENT |
| `ftsH` | `PP_4718` | `Q88DV1` | ATP-dependent zinc metalloprotease FtsH (EC 3.4.24.-) | CURATED | PRESENT |
| `corC` | `PP_4789` | `Q88DN5` | Magnesium and cobalt efflux protein CorC | CURATED | PRESENT |
| `PP_4870` | `PP_4870` | `Q88DF5` | Azurin | CURATED | PRESENT |
| `putP` | `PP_4946` | `Q88D81` | Sodium/proline symporter (Proline permease) | CURATED | PRESENT |
| `PP_4970` | `PP_4970` | `Q88D57` | Cytochrome c | CURATED | PRESENT |
| `nhaP` | `PP_4974` | `Q88D53` | NhaP-type Na+/H+ and K+/H+ antiporters | CURATED | PRESENT |
| `yceJ` | `PP_4982` | `Q88D46` | Cytochrome b561, iron-regulated | CURATED | PRESENT |
| `PP_4986` | `PP_4986` | `Q88D42` | Channel protein, hemolysin III family | CURATED | PRESENT |
| `nhaP2` | `PP_5066` | `Q88CW4` | K(+)/H(+) antiporter NhaP2 (Potassium/proton antiporter NhaP2) | CURATED | PRESENT |
| `yfhL` | `PP_5124` | `Q88CQ6` | 4Fe-4S cluster-containing protein | CURATED | PRESENT |
| `tcyP` | `PP_5131` | `Q88CP9` | Sodium-cystine symporter | CURATED | PRESENT |
| `cadA-III` | `PP_5139` | `Q88CP1` | P-type Zn(2+) transporter (EC 7.2.2.12) | CURATED | PRESENT |
| `kefB-III` | `PP_5246` | `Q88CD5` | Glutathione-regulated potassium/H+ antiporter | CURATED | PRESENT |
| `norM` | `PP_5262` | `Q88CB9` | Probable multidrug resistance protein NorM (Multidrug-efflux transporter) | CURATED | PRESENT |
| `PP_5267` | `PP_5267` | `Q88CB4` | Cytochrome c5 | CURATED | PRESENT |
| `PP_5322` | `PP_5322` | `Q88C61` | Metal ion transporter | CURATED | PRESENT |
| `PP_5355` | `PP_5355` | `Q88C28` | Sodium/proton antiporter | CURATED | PRESENT |
| `ccmH` | `PP_5748` | `A0A140FWM4` | Cytochrome c-type biogenesis protein | CURATED | PRESENT |
