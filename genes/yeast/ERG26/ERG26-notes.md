# ERG26 (YGL001C) notes

UniProt P53199; sterol-4alpha-carboxylate 3-dehydrogenase (decarboxylating), EC 1.1.1.170; 3beta-HSD family; peripheral ER membrane [UniProt:P53199].

## Evidence journal
- erg26 accumulates carboxysterols; disruption lethal in heme-competent cells [PMID:9811880 "Segregants containing the YGL001c disruption were not viable after transfer to fresh, sterol-supplemented media."].
- erg26-1 microsomes lack activity; GFP-Erg26 ER [PMID:11279045 "microsomes isolated from erg26-1 cells contained greatly reduced 4alpha-carboxysterol-C3 dehydrogenase activity when compared with microsomes from wild type cells"].
- Cofactor: full text of PMID:9811880 does not assay NAD+ vs NADP+; only cites NAD-depleted microsome work in other systems.

## Decisions
- GO:0000252 core (cofactor-neutral); GO:0102175 (NAD+-specific, IMP) KEEP_AS_NON_CORE; generic CH-OH oxidoreductase IEA -> MODIFY GO:0000252; protein binding REMOVE (incl. MCM7 AP-MS hits); RCA cytosol -> ER membrane.
