# cact (Cactus, Q03017) review notes

## Identity
- Drosophila melanogaster IkappaB-family protein, FBgn0000250; 500 aa; N-terminal signal-responsive region, five ankyrin repeats, C-terminal PEST region (UniProt Q03017).
- UniProt: "Belongs to the NF-kappa-B inhibitor family"; PANTHER PTHR46680:SF3 "NF-KAPPA-B INHIBITOR CACTUS".
- Isoforms A (maternal/zygotic) and C (zygotic).

## Core biology (with provenance)
- Cactus binds Dorsal and holds it in the cytoplasm: [PMID:7705656 "Cactus, like its mammalian homolog I kappa B, inhibits nuclear translocation by binding Dorsal and retaining it in the cytoplasm."]
- Mechanism in yeast reconstitution: [PMID:7479760 "Cactus blocks the DNA binding and nuclear localization functions of Dorsal"]
- Cactus is the inhibitor of both Rel proteins downstream of Toll: [PMID:24086459 "Cactus, a fly IκB protein, is the inhibitor for both Dif and Dorsal."]
- Signal-dependent degradation is the switch: [PMID:7705656 "signal-dependent degradation of Cactus does not require the presence of Dorsal, indicating that Cactus degradation is a direct response to signaling"]; gradient of Cactus degradation shapes the Dorsal nuclear gradient [PMID:9025065].
- Kinase: Pelle (IRAK homolog), not IKK: [PMID:24086459 "We conclude that Pelle acts as a Cactus kinase and preferentially phosphorylates Cactus at the serines required for signal responsiveness."]; [PMID:24086459 "Surprisingly, the Drosophila IKK does not function in the fly Toll pathway"]. Slimb (betaTrCP) is required for degradation in S2 cells.
- Loss of function ventralizes embryos; cactus acts via dorsal: [PMID:1794309 "the maternal gene cactus acts as a negative regulator of the nuclear localization of the dorsal protein"].
- Immunity: spz/Toll/cact cassette controls drosomycin [PMID:8808632]; fat-body mosaic [PMID:10369678 "a linear activation cascade Spaetzle--> Toll-->Cactus-->Dorsal/DIF leads to the induction of the drosomycin gene"]. cactus is itself a Toll target (autoregulation) [PMID:9553105 "the cactus gene is autoregulated"]; feedback via Bre1/Rad6 [PMID:36516751].
- Hematopoiesis: Cact knockdown in prohemocytes drives differentiation [PMID:27163255 "over-expression of Dorsal, or knockdown of Cactus, promotes differentiation"].
- NMJ: Dorsal and Cactus concentrated in postsynaptic side of larval NMJ [PMID:10192771]; levels change with synaptic activity, possibly Toll-independent [PMID:12532402].
- Partners (IPI): Dorsal, Dif, cactin [PMID:10842059], Kurtz beta-arrestin [PMID:20802461], IKKbeta/DLAK in LPS-stimulated cells [PMID:10636911].

## Curation decisions (summary)
- MF core: GO:0140311 protein sequestering activity + GO:0051059 NF-kappaB binding (ACCEPT IBA and experimental rows).
- BP core: GO:0045751 negative regulation of Toll signaling pathway (ACCEPT all). Dorsoventral patterning ACCEPT.
- GO:0043124 negative regulation of canonical NF-kappaB signal transduction (IBA, IMP): the GO definition is IKK-dependent; the fly Toll pathway uses Pelle as the Cactus kinase and IKK is dispensable (PMID:24086459). MODIFY to GO:0045751.
- protein binding rows: Dorsal partner rows -> MODIFY to NF-kappaB binding; cactin, Kurtz, IKKbeta rows -> REMOVE as uninformative.
- NMJ / subsynaptic reticulum / hemocyte differentiation: KEEP_AS_NON_CORE.
- HMP from the Schupbach & Wieschaus female-sterile screen (oogenesis, dorsal appendage formation): abstract does not mention cactus, full text not cached -> UNDECIDED.

## Deep research
Falcon deep research had not started for DROME genes when this review was written (the batch job was still working through human genes). Review was carried out from the UniProt record and cached publications only. See final section if updated.
