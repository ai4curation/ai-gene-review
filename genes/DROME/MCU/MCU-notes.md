# MCU (CG18769) review notes

UniProt Q8IQ70 (Calcium uniporter protein, mitochondrial); PANTHER PTHR13462.

## Literature journal

- Null allele abolishes fast uptake [PMID:31042479 "Altogether, these data show that MCU1 is a null mutant incapable of fast Ca2+ uptake."]; mild organismal phenotypes but short lifespan [PMID:31042479 "Despite lacking fast Ca2+ uptake, MCU and EMRE mutants present a surprising lack of organismal phenotypes, although both mutants are short lived, with a more pronounced effect when MCU is lost."]
- EMRE dependence of fly MCU [PMID:27099988 "metazoan MCU homologues from C. elegans and D. melanogaster require EMRE to transport Ca2+"]; [PMID:28726639 "Drosophila MCU contains evolutionarily conserved structures and requires essential MCU regulator (EMRE) for its calcium channel activities"].
- Gating residues conserved [PMID:33296646 "metazoan (containing EMRE) and non-metazoan (without EMRE) MCU homologs share a core gating mecha"] (fly MCU tested).
- Oxidative stress and ER-mitochondria transfer [PMID:28726639 "oxidative stress-induced increases in mitochondrial calcium, mitochondrial membrane potential depolarization, and cell death were prevented in these mutants"].
- Memory [PMID:27568554 "Collectively, these results demonstrate that MCU expression and function are required in MBn to support ITM, but not learning."]

## Curation decisions (uniporter module, applied to MCU, EMRE, MICU1, MICU3, CG4704)

- GO:1990246 uniplex complex ACCEPTED for all subunits.
- GO:0006851 mitochondrial calcium ion transmembrane transport -> MODIFY to child GO:0036444 calcium import into the mitochondrion for all subunits.
- GO:0051560 mitochondrial calcium ion homeostasis ACCEPTED for all subunits.
- MCU uniporter activity (GO:0015292, a carrier-type term under secondary active transport) -> MODIFY to calcium channel activity.
- MF slots: MCU enables calcium channel activity; EMRE contributes_to calcium channel activity; MICU1/MICU3 calcium channel regulator activity; CG4704 calcium ion binding (untested paralog).

## Deep research

`just deep-research-falcon` was still running or had timed out when this review was committed; any late-arriving report will be added in a follow-up commit.
