# HSPB8 (Q9UJY1) research notes

## Identity
- Heat shock protein beta-8 / HSP22 / H11 / E2IG1 / alpha-crystallin C chain, small heat shock protein (HSP20/alpha-crystallin) family, 196 aa, ~21.6 kDa.
- Predominantly expressed in skeletal muscle and heart [file:human/HSPB8/HSPB8-uniprot.txt "Predominantly expressed in skeletal muscle and heart."]. Estrogen-inducible (E2IG1).

## Function (core)
- UniProt FUNCTION: "Involved in the chaperone-assisted selective autophagy (CASA), a crucial process for protein quality control, particularly in mechanical strained cells and tissues such as muscle. Displays temperature-dependent chaperone activity." [file:human/HSPB8/HSPB8-uniprot.txt].
- ATP-independent holdase activity demonstrated in vitro: prevents heat-induced aggregation of yeast alcohol dehydrogenase and bovine rhodanese, comparable to HSP20 [PMID:14985082 "Hsp22 effectively prevents heat-induced aggregation of yeast alcohol dehydrogenase and bovine liver rhodanese with chaperone activity comparable to that of recombinant human small heat shock protein with apparent molecular mass 20 kDa (Hsp20)."].
- NOT a protein kinase: despite early naming as "protein kinase H11", recombinant Hsp22 has "negligibly low autophosphorylation activity and...is unable to phosphorylate casein or histone" [PMID:14985082]. The NOT|protein kinase activity annotation (GO:0004672, IDA, PMID:14985082) is supported.

## CASA / aggrephagy mechanism
- Component of the CASA complex: BAG3, HSPA8/HSC70, HSPB8, STUB1/CHIP [file:human/HSPB8/HSPB8-uniprot.txt "Component of the chaperone-assisted selective autophagy (CASA) complex consisting of BAG3, HSPA8/HSC70, HSPB8 and STUB1/CHIP (PubMed:20060297)."].
- CASA facilitates degradation of damaged Z-disk components (e.g. filamin) via autophagy; BAG3 coordinates Hsc70 and HspB8; CHIP ubiquitin ligase and p62 adaptor [PMID:20060297 "Stv and its mammalian ortholog BAG-3 coordinate the activity of Hsc70 and the small heat shock protein HspB8 during disposal that is initiated by the chaperone-associated ubiquitin ligase CHIP and the autophagic ubiquitin adaptor p62."; "Impaired CASA results in Z disk disintegration and progressive muscle weakness in flies, mice, and men."].
- HspB8 chaperone activity toward poly(Q) proteins depends on Bag3-stimulated macroautophagy [PMID:18006506 "HspB8 forms a stable complex with Bag3 in cells and that the formation of this complex is essential for the activity of HspB8."; "the HspB8-Bag3 complex might stimulate the degradation of Htt43Q by macroautophagy."]. This is the basis for the positive regulation of aggrephagy (GO:1905337, IMP) and cellular response to unfolded protein (GO:0034620, IMP) annotations.
- Forms ternary complex with BAG3 and HSPA1A (Hsp70) [PMID:27884606 BAG3 links Hsp70 to small HSPs]. Interacts with HSPB1 [PMID:11342557], DNAJB6 [PMID:22366786], HSPB7/HSPB2 [PMID:14594798].

## Oligomerization
- Forms stable dimers / homodimerization [PMID:14985082 "Hsp22 forms stable dimers."]. GO:0042803 (protein homodimerization activity) and GO:0042802 (identical protein binding) supported.

## Localization
- Cytoplasm and nucleus; translocates to nuclear foci during heat shock [file:human/HSPB8/HSPB8-uniprot.txt "Cytoplasm ... Nucleus ... Note=Translocates to nuclear foci during heat shock."]. GOA: cytosol (IDA, HPA), nucleoplasm (IDA, HPA), protein folding chaperone complex (IDA).

## Disease
- Distal hereditary motor neuronopathy type 2 (HMND2), Charcot-Marie-Tooth type 2L (CMT2L), myofibrillar myopathy 13 (MFM13). Hot-spot K141 variants (K141E/N/M/T) affect chaperone function, increase aggregation, and alter BAG3/HSPB1 interactions [file:human/HSPB8/HSPB8-uniprot.txt VARIANT 141; PMID:15122253; PMID:28144995].

## GO review plan
- Core MF: unfolded protein binding / holdase (GO:0051082) and Hsp70-co-chaperone CASA role. Core BP: positive regulation of aggrephagy (GO:1905337) and CASA.
- Many bare protein binding IPIs (GO:0005515): the BAG3 (O95817), HSPB1, DNAJB6, HSPB7 ones are informative -> heat shock protein binding / chaperone binding; the generic interactome ones KEEP_AS_NON_CORE.
- protein folding chaperone complex (GO:0101031, part_of): ACCEPT (CASA complex / sHSP complex).
- NOT protein kinase activity (GO:0004672 negated): ACCEPT - correctly negated.
</content>
