# AAH1 (YNL141W, UniProt P53909) notes

## Function
- Adenine deaminase EC 3.5.4.2 "Reaction=adenine + H2O + H(+) = hypoxanthine + NH4(+);" Zn cofactor [UniProt:P53909 (HAMAP MF_03145)].
- "Exogenous adenine enters metabolic pathways primarily via the function of either AAH or adenine phosphoribosyltransferase (APRT; EC 2.4.2.7)." [PMID:1577682]
- "AAH specific activity is not induced by adenine and is reduced sevenfold when cells are cultivated in medium containing proline in place of ammonium as the sole nitrogen source." [PMID:1577682]
- Fungal adenine deaminases are related to adenosine deaminases, not bacterial adenine deaminases [PMID:14643670].
- "Adenine was the most favoured substrate for the yeast enzymes" (also N6-substituted adenines) [PMID:18673302].
- Quiescence: "the adenine deaminase Aah1p is specifically degraded via a process requiring the F-box protein Saf1p" [PMID:17517885].
- Route to IMP: "the second route is through adenine deaminase (Aah1p) and hypoxanthine-guanine phosphoribosyltransferase (Hpt1p)" [PMID:19635936].

## Pathway
- ADENINE-DEAMINASE-RXN in PWY3O-1/2220/285; correct; cytosol default fine.

## Decisions
- Core MF GO:0000034; BP GO:0043103 hypoxanthine salvage + GO:0006146 adenine catabolic process; cytoplasm.
- REMOVE InterPro2GO "purine ribonucleoside monophosphate biosynthetic process" (IPR006650 shared with AMP deaminase; Aah1 makes a base, not a nucleotide).
- REMOVE protein binding (Saf1) x3; MODIFY deaminase activity -> GO:0000034.
