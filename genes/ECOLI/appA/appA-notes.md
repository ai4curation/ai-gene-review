# appA notes

## 2026-10-02

`just deep-research-falcon ECOLI appA` resolved UniProt P07102 and constructed
the expected `deep-research-client` call, but failed before generating provider
output because `agentapi` was absent from `PATH` and no remote-provider API keys
were configured. I therefore created `appA-deep-research-manual.md` from the
GOA-linked cached primary literature.

Reviewed all 21 seeded GOA rows for AppA. The core picture is a Sec-exported,
periplasmic histidine acid phosphatase whose dominant physiological activity is
phytate/inositol-phosphate hydrolysis during phosphate scavenging
[PMID:8387749; PMID:11035187; PMID:10696472]. Dassa et al. explain the older
GTPase, nucleotidase, and sugar-phosphatase rows: the purified pH 2.5 acid
phosphatase preferentially hydrolysed GTP and ppGpp among nucleotides and also
accepted a small subset of phosphomonoesters, including fructose
1,6-bisphosphate [PMID:6282821]. The Ostanin mutagenesis papers support the
histidine-acid-phosphatase active site and AppA catalytic mechanism
[PMID:1429631; PMID:8407904].

I accepted the two `GO:0052745 inositol phosphate phosphatase activity` rows as
core; kept GTPase, nucleotidase, sugar-phosphatase, and broad dephosphorylation
rows as non-core; accepted `GO:0016036 cellular response to phosphate
starvation`; modified broad `GO:0042597 periplasmic space` rows to
`GO:0030288 outer membrane-bounded periplasmic space`; and marked
`GO:0071454 cellular response to anoxia` as over-annotated because the
available text supports anaerobic induction of AppA, not a direct AppA step in
an anoxia-response pathway.
