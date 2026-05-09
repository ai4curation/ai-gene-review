# wspR notes

- `wspR` in KT2440 corresponds to locus `PP_4959` / UniProt `Q88D68`, a REC-PAS-GGDEF-EAL response regulator-like protein predicted in UniProt as a diguanylate cyclase with Mg2+ cofactor and no transmembrane segment.

- The KT2440 Wsp operon is a seven-gene surface-response module whose output affects the planktonic-to-sessile switch. The 2020 KT2440 study states that the wsp cluster "regulates cyclic di-GMP (cdGMP) levels upon surface contact" and that "the key components include WspR, a protein that harbours the domain for producing cdGMP, and WspF, which controls its activity." [PMID:32519402 "regulates cyclic di-GMP (cdGMP) levels upon surface contact... the key components include WspR, a protein that harbours the domain for producing cdGMP, and WspF, which controls its activity"]

- Wsp signaling promotes biofilm-associated lifestyles in KT2440. The 2022 study reports that the Wsp system "regulated K1-T6SS expression via synthesizing the second messenger cyclic di-GMP" and that "Wsp system promoted biofilm formation largely in a FleQ/FleN-dependent manner." [PMID:35178858 "regulated K1-T6SS expression via synthesizing the second messenger cyclic di-GMP... Wsp system promoted biofilm formation largely in a FleQ/FleN-dependent manner"]

- Under tetracycline stress, WspR is one of several c-di-GMP enzymes affecting biofilm, but the most prominent one in the tested conditions. The 2025 KT2440 paper states: "Among them, the diguanylate cyclase WspR displayed the most significant effect on c-di-GMP level and biofilm formation." [PMID:39589111 "Among them, the diguanylate cyclase WspR displayed the most significant effect on c-di-GMP level and biofilm formation"]

- Structural/biochemical work on WspR orthologs supports direct c-di-GMP synthesis plus feedback inhibition by product binding. PMID:18366254 reports the "crystal structure of the diguanylate cyclase WspR... bound to c-di-GMP at an inhibitory site" and that WspR changes oligomeric state during feedback regulation. [PMID:18366254 "crystal structure of the diguanylate cyclase WspR... bound to c-di-GMP at an inhibitory site... modulation of its activity through oligomerization"]

- Current GOA for `Q88D68` is clearly under-specific/over-broad: generic catalytic activity, generic phosphorelay participation, generic regulation of transcription, and plasma membrane localization. Likely curation direction:
  - `GO:0003824 catalytic activity` -> modify to `GO:0052621 diguanylate cyclase activity`
  - `GO:0000160 phosphorelay signal transduction system` -> keep
  - `GO:0006355 regulation of DNA-templated transcription` -> over-annotation; downstream phenotype is indirect via c-di-GMP and FleQ/FleN
  - `GO:0005886 plasma membrane` -> remove; WspR itself is not membrane-spanning
