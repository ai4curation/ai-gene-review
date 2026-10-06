# GPM1 notes (P00950, YKL152C)

- BPG-dependent phosphoglycerate mutase, EC 5.4.2.11 [UniProt:P00950 "Reaction=(2R)-2-phosphoglycerate = (2R)-3-phosphoglycerate;"]; His181 general acid/base [PMID:1386023 "Kinetic analysis shows a large decrease (1.6 x 10(4)) in the catalytic efficiency"].
- Sole PGAM for glycolysis and gluconeogenesis: deletion cannot grow on glucose or on glycerol or ethanol alone [PMID:3033435 "growth was inhibited by glucose and neither glycerol nor ethanol alone were sufficient to support growth"].
- Mostly cytosolic [PMID:3332961 "Ten of them were identified as corresponding to cytoplasmic enzymes of the carbon metabolism machinery"]; minor mitochondrial-surface pool [PMID:16962558 "we show that all glycolytic enzymes are associated with mitochondria in yeast"]; recovered in IMS proteome [PMID:22984289 "we found 20 novel intermembrane space proteins"].
- Pathway flag: YeastCyc also attaches EC 5.4.2.12 (cofactor-independent iPGM) to GPM1; that is incorrect for this dPGM (UniProt gives only EC 5.4.2.11).

Decisions: REMOVE bifid shunt (GLUCFERMEN-PWY mis-mapping); MODIFY obsolete canonical/G6P glycolysis terms -> GO:0006096; MODIFY generic catalytic / intramolecular phosphotransferase -> GO:0004619; mitochondrial/IMS rows KEEP_AS_NON_CORE.
