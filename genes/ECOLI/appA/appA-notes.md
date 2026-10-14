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
GTPase and nucleotidase rows: the purified pH 2.5 acid phosphatase can
hydrolyse GTP and ppGpp in vitro, but these are slow phosphoanhydride reactions
rather than GO:0008252 nucleotidase chemistry, and they do not match AppA's
periplasmic phytase role [PMID:6282821]. The same paper supports the
sugar-phosphatase side rows because AppA accepts a small subset of
phosphomonoesters, including fructose 1,6-bisphosphate. The Ostanin mutagenesis
papers support the histidine-acid-phosphatase active site and AppA catalytic
mechanism [PMID:1429631; PMID:8407904].

I accepted the two direct `GO:0052745 inositol phosphate phosphatase activity`
rows and used `GO:0052745` for the core AppA function because it spans the
stepwise phytate and lower-inositol-phosphate dephosphorylation ladder; marked
the GTPase and nucleotidase rows over-annotated; kept sugar-phosphatase and
broad dephosphorylation rows as non-core; accepted `GO:0016036 cellular
response to phosphate starvation`; modified broad `GO:0042597 periplasmic
space` rows to `GO:0030288 outer membrane-bounded periplasmic space`; and
marked `GO:0071454 cellular response to anoxia` as over-annotated because the
available text supports anaerobic induction of AppA, not a direct AppA step in
an anoxia-response pathway. I checked `GO:0008707` in QuickGO during PR review
follow-up; it cross-references EC 3.1.3.26 and RHEA:20960, whose product is a
1D-1,2,3,5,6-pentakisphosphate, so it represents the 1D-4 reaction rather than
AppA's 1D-6 first step.
