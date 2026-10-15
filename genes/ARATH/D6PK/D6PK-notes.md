# D6PK (D6 PROTEIN KINASE, AGC1-1, PK64; At5g55910; UniProt Q9FG74) notes

Identity verified: UniProt Q9FG74 "Serine/threonine-protein kinase D6PK", OrderedLocusNames At5g55910.
Deep research: falcon failed (Edison API 429, 2026-10-05).

## Activity and localization
- Basal PM, colocalizes with PINs; phosphorylates PINs [PMID:19168677 "D6PK localizes to the basal (lower) membrane of Arabidopsis root cells, where it colocalizes with PIN1, PIN2 and PIN4."; "D6PK phosphorylates PIN proteins in vitro and in vivo"].
- Activates PIN-mediated efflux; kinase-dead inactive [PMID:24948515 "a kinase-dead variant of D6PK could not activate auxin efflux in this system"].
- Lipid binding through polybasic motif [PMID:27836964 "We further show that D6PK directly binds polyacidic phospholipids through a polybasic lysine-rich motif in the middle domain of the kinase."].
- Planar polarity switch at root-hair initiation [PMID:27251533].

## Physiology
- Phototropism via PIN3/4/7 [PMID:23709629 "phototropic hypocotyl bending is strongly dependent on the activity of D6PKs and the PIN proteins PIN3, PIN4, and PIN7"]; gravitropism [PMID:29490064].

## Decisions
- Specific phosphoinositide-binding rows KEEP_AS_NON_CORE (non-selective polyacidic lipid binding); GO:1901981 accepted.
- PMID:14749726 (Anthony 2004) abstract is about AGC2-1/OXI1; D6PK-PDK1 binding row removed as GO:0005515 regardless.
- NEW GO:2000012 regulation of auxin polar transport (IDA PMID:24948515).
