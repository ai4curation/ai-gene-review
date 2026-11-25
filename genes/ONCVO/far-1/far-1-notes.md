# ONCVO far-1 notes

## 2026-11-24 review

UniProt resolves `far-1` in ONCVO to reviewed entry Q25619/FAR1_ONCVO, a
178-amino-acid O. volvulus fatty-acid and retinol-binding protein also known as
Ov-FAR-1, Ov20, OvS1, and OvMBP/11. The Swiss-Prot record annotates a predicted
1-16 signal peptide and cross-references `InterPro; IPR008632; Gp-FAR-1.` and
PANTHER `PTHR31418:SF7`.

The seeded GOA snapshot contains nine rows: three IDA rows for
`GO:0005504 fatty acid binding`, two IDA rows for `GO:0019841 retinol binding`,
two IDA rows for `GO:0005576 extracellular region`, one combined ARBA/UniProtKB
SubCell IEA row for extracellular region, and one InterPro2GO row from
IPR008632 to `GO:0008289 lipid binding`. `just paint-losses ONCVO far-1`
reported no IRD or IKR loss on this gene lineage, and the gene carries no IBA
rows.

The ligand-binding rows are well supported. PMID:9368002 reports recombinant
Ov20 expression and fluorescence assays in which "the protein contains a high
affinity binding site for retinol, fluorescent fatty acids", with competition
by oleic and arachidonic acids. PMID:10693749 tested long-chain fatty-acid
competition with host serum albumin and found that "OvS1 protein bound
arachidonic acid with an affinity five-fold greater than the affinity exhibited
by serum albumin." PMID:12106870 compared recombinant Ov-FAR-1 and Bm-FAR-1
and reports that both proteins "bind all-trans-retinol, (dansylamino)
undecanoic acid (DAUDA), and oleic acid by competition."

The extracellular-region rows are also supportable. PMID:7770083 cloned the
OvMBP/11 cDNA, reported that "The cDNA encodes a protein of 20.5 kDa (termed Ov
20) containing a putative signal peptide", and detected antigen in the
supernatant of cultured adult female nematodes. PMID:12106870 more broadly
found that filarial FAR proteins "were released into culture medium by all the
species and developmental stages investigated." The GO:0005576 term is retained
for both the direct rows and the automated row.

The InterPro2GO `GO:0008289 lipid binding` row is true but too general for a
protein with direct fatty-acid and retinol-binding annotations. Local PANTHER
entries place Q25619 in PTHR31418:SF7 with B. malayi Q93142 and C. elegans
P34382 FAR-1; C. elegans FAR-2/P34383 is the related PTHR31418:SF19 paralog.

Ov-FAR-1 has direct in vitro fatty-acid and retinol-binding evidence and direct
secretion evidence, but native in vivo cargoes, uptake routes, and
immunomodulatory phenotypes in O. volvulus remain inferred from the FAR family
model rather than directly assayed for Q25619.
