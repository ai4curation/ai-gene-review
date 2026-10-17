# YJL045W (SDH1b, P47052) notes

Evidence journal for the review; sources are UniProt and cached publications.

- Paralog of the SDH flavoprotein Sdh1p: [PMID:9730279 "The second plasmid (pG52/T8) had an insert with reading frame (YJL045w) of yeast chromosome X coding for a homologue of SDH1."]
- Functional: [PMID:9730279 "Subclones containing the SDH1 homologue (SDH1b), restored respiration in E264/U2 indicating that the protein encoded by this gene is functional."]
- Minor under standard conditions: [PMID:9730279 "indicates that the isoenzyme encoded by SDH1b is unlikely to play an important role in mitochondrial respiration"]; the SDH1b-lacZ fusion had 100-500-fold lower activity than SDH1-lacZ.
- Residual activity in sdh1 cells: [PMID:16232921 "the activity disappeared in double disruptants of the SDH1 and SDH2 or SDH1b (the SDH1 homologue) genes"].
- UniProt: "In vitro, can complement a SDH1 disruption and leads to less than 15% of wild-type SDH reductase activity" [UniProt:P47052].

Curation decisions
- Core MF: GO:0008177 (enables, as the catalytic flavoprotein), complex II, inner membrane. Annotations accepted, but the module should model it as a minor/backup paralog of SDH1, not an equal isozyme.
- IEA generic oxidoreductase terms were changed to GO:0008177; generic 'protein-containing complex' to GO:0045273.
- No direct biochemical isolation of a YJL045W-containing complex II is cited; part_of rests on IBA plus complementation.
