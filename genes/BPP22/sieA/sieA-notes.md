# sieA (Salmonella phage P22) — curation notes

**Provenance note:** no deep-research API keys were available in this container, so
`just deep-research` was not run and no `-deep-research-<provider>.md` file exists. Research
was done directly from the cached publications (`publications/PMID_7768804.md`,
`PMID_4610992.md`, `PMID_38236051.md`), the UniProt record (`sieA-uniprot.txt`), the PubMed
MCP, and OLS. The GONUTS wiki (gowiki.tamu.edu) was tried for the CACAO student evidence on
both PMID pages (`/wiki/index.php/PMID:4610992`, `/wiki/index.php/PMID:7768804`) but the site
is currently offline for upgrades ("temporarily offline for upgrades"), so the student notes
could not be read.

## Protein

Q38674, 164 aa (start codon uncertain: 492 or 480 bp ORF, so 164 or 162 aa), encoded between
P22 genes *mnt* and *16*. Three predicted transmembrane helices (UniProt FT TRANSMEM 8–28,
85–105, 121–141, ECO:0000255; TMHMM in Fig. 3A of PMID:38236051). Pfam PF26849 (SIEA),
InterPro IPR059742. UniProt subcellular location: "Host cell inner membrane
{ECO:0000269|PubMed:7768804}; Multi-pass membrane protein {ECO:0000305}". No catalytic motif,
no known molecular activity.

## Function

- P22 prophages carry four superinfection exclusion systems (c2 repressor, gtrABC, sieA,
  sieB). SieA acts early: [PMID:38236051 "The SieA protein blocks superinfection by P22-like
  phages (including P22 itself) at an early stage of infection (19, 22–24)."]
- Adsorption is unaffected, and so is progeny production after induction:
  [PMID:38236051 "Previous studies have shown that a sieA+ P22 prophage does not affect the
  adsorption of superinfecting P22 phage virions (18, 23, 24) or the production of progeny
  after P22 prophage induction (24)."]
- The classic genetic/physiological evidence that the block is at DNA entry is Susskind,
  Botstein & Wright 1974 (PMID:4610992; cache is abstract-only, abstract text itself is not in
  the cached record — only title, authors, DOI), summarized by the 2024 paper:
  [PMID:38236051 "In a sieA+ lysogen, superinfecting P22 DNA is not cleaved by cytoplasmic
  host restriction endonucleases, and superinfecting P22 genes are not expressed (20)."] and
  [PMID:38236051 "These findings suggest that the sieA block occurs early in the infection
  cycle after adsorption has occurred, and the current hypothesis is that the SieA protein
  blocks entry of superinfecting phage DNA into the target cell."] The paper's own title
  states the result: "Failure of superinfecting phage DNA to enter sieA+ lysogens."
- Exclusion is not DNA-sequence specific — transduction is excluded too:
  [PMID:38236051 "SieA exclusion is not specific for the type of DNA in the infecting virion
  since generalized transduction by phage P22 is also greatly lowered by a sieA+ 22 prophage
  in the recipient cell (19, 22–24)."]

## Leavitt et al. 2024 (PMID:38236051, full text cached)

- *sieA* alone, in one chromosomal copy, is sufficient:
  [PMID:38236051 "Thus, the sieA gene in one copy per Salmonella genome is sufficient to
  mediate robust superinfection exclusion."] with plaque formation lowered ≥7 logs (Fig. 1):
  [PMID:38236051 "lowered the plaque-forming ability of P22 by at least seven orders of
  magnitude (Fig. 1)"].
- DNA injection per se is blocked, by K+ efflux assay (Fig. 2A):
  [PMID:38236051 "Figure 2A shows that P22 causes very little, if any, K+ release from the
  sieA+ strain, while nearly all of the cellular K+ is released from the isogenic sieA–
  strain, suggesting that DNA injection per se is blocked by SieA."] and
  [PMID:38236051 "We conclude from the above results that SieA alone blocks injection of P22
  DNA into Salmonella cells and has no other additional effect on P22 growth."]
- Inner membrane localization (Fig. 3B, anti-FLAG immunoblot of inner vs outer membrane
  fractions of a chromosomal *sieA-FLAG* strain that retains exclusion activity):
  [PMID:38236051 "We conclude that SieA is an exclusively inner membrane protein."]; the 1995
  study had not resolved this: [PMID:38236051 "That study did not determine whether SieA is in
  the inner or the outer membrane."]
- Mechanism: escape mutants map to ejection (E-) proteins gp16 and gp20:
  [PMID:38236051 "Since amino acid changes in E-proteins gp16 and gp20 confer escape from
  SieA exclusion, we conclude that SieA very likely blocks P22 DNA injection by interfering
  with the functions of these two proteins and that the mutations avoid this interference."]
  and [PMID:38236051 "The observations here that (i) P22 infection by virions lacking
  E-proteins mimics the SieA block phenotype, (ii) P22 hybrids with phage HK620 E-proteins are
  partially resistant to SieA, and (iii) mutations that alter P22 gp16 and gp20 confer SieA
  resistance strongly suggest that SieA protein interferes with assembly of the E-protein
  conduit or with conduit function after its assembly."] Location of the interference:
  [PMID:38236051 "The presence of SieA protein in the inner membrane suggests that it
  interferes with DNA injection at that location."]
- Specificity: [PMID:38236051 "Since SP6 is not affected, the P22 SieA protein does not
  exclude all short-tailed phages and appears to be specific for P22-like phages."]
- Diversity: three sequence types <30% identical;
  [PMID:38236051 "coli prophage SieA proteins are either type A or B, and type C is currently
  limited to the Providencia, Morganella and Proteus genera."]

## Hofer et al. 1995 (PMID:7768804, abstract-only; PMC full text not retrievable via PMC API)

[PMID:7768804 "According to three hydrophobic regions, all of which are long enough to span
the membrane, the product of sieA should be a protein of the inner membrane of a P22-lysogenic
cell of Salmonella typhimurium."] and [PMID:7768804 "The SieA protein was moderately
overproduced from an expression vector in cultures of Escherichia coli and could be recovered
from the membrane fraction."] — i.e. the experimental part is a crude membrane-fraction
recovery under overproducing conditions in *E. coli*; the inner-membrane assignment there is
sequence-based inference, later confirmed experimentally in 2024.

## CACAO rows (ASSIGNED BY = CACAO in sieA-goa.tsv)

| term | ev | PMID | assessment |
|---|---|---|---|
| GO:0046596 regulation of viral entry into host cell | IMP | 4610992 | correct direction (negative), but less informative than GO:0098669, which is annotated from the same paper; superinfection exclusion is the process the gene executes |
| GO:0098669 superinfection exclusion | IMP | 4610992 | matches the paper exactly (failure of superinfecting DNA to enter sieA+ lysogens) |
| GO:0098669 superinfection exclusion | IDA | 38236051 | matches; necessary-and-sufficient plus K+ efflux and escape-mutant data |
| GO:0020002 host cell plasma membrane | IDA | 38236051 | matches Fig. 3B inner/outer membrane fractionation |
| GO:0033644 host cell membrane | IDA | 7768804 | true but entailed by the host cell plasma membrane rows; the 1995 paper's own evidence is a crude membrane fraction, which is all it can support |

No CACAO row here is a phenotype-as-process error, a paper-not-about-the-gene error, or an
unsupported single-image localization: every row is on the one protein the papers are about,
and the localization row is backed by a fractionation with two methods plus a tagged-protein
control. The only granularity issues are the broad `GO:0033644` beside `GO:0020002`, and
`GO:0046596`, which is a parent-level restatement of the same experiment that yielded the
specific `GO:0098669`.

## Open questions

- Does SieA bind gp16/gp20 directly, or alter the inner membrane so the conduit cannot
  assemble? No binding assay has been reported.
- Why is SieA specific for P22-like phages and not other short-tailed phages (SP6)?
- Is the host inner membrane protein YajC, required for P22 DNA injection, a SieA target?
  [PMID:38236051 "Bohm et al. (67) found the host inner membrane protein YajC to be essential
  for P22 DNA injection."] — the SieA-resistant triple mutants still did not plate on a
  *yajC–* host, so the two requirements are separable but unexplained.
- Which start codon is used in vivo, and what is the membrane topology of the conserved
  cytoplasmic motif FxRYPxEAxxFNK (residues 145–157)?
