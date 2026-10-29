# nrdJa (PA5497, Q9HT76) — research notes

## Identity

- UniProt Q9HT76 (unreviewed), 734 aa, gene name `nrdJa`, ordered locus `PA5497`,
  *P. aeruginosa* PAO1 (NCBITaxon:208964). Matches the worklist entry (rank 28).
- UniProt RecName "Vitamin B12-dependent ribonucleotide reductase", EC 1.17.4.1,
  by RuleBase RU364064; family assignment "Belongs to the ribonucleoside
  diphosphate reductase class-2 family".
- Domains: ribonucleotide reductase large subunit N-terminal (PF00317, 40-110)
  and C-terminal (PF02867, 123-669); NCBIfam TIGR02504 (NrdJ_Z);
  PANTHER PTHR43371 / PTHR43371:SF1.
- PA5497 (`nrdJa`) and PA5496 (`nrdJb`) are consecutive genes separated by 16 bp
  and co-transcribed as the `nrdJab` operon
  [PMID:15722359, "Class II RNR of P. aeruginosa differs"].

## Biology

*P. aeruginosa* encodes all three classes of ribonucleotide reductase (RNR):
class I (`nrdAB`), class II (`nrdJab`) and class III (`nrdDG`). Class II RNRs
use adenosylcobalamin (AdoCbl, coenzyme B12) as the radical generator and are
oxygen-indifferent
[PMID:26225432, "Class II RNRs utilize the B12 coenzyme adenosylcobalamin (AdoCbl) as a radical generator."].

Unusually, the *P. aeruginosa* class II RNR is split into two polypeptides:
[PMID:26225432, "The nrdJ gene in these species is split at a specific site into two genes, nrdJa and nrdJb, of a single operon that encodes the two polypeptides NrdJa (734 residues in PA) and NrdJb (229 residues in PA)"].

### What each subunit does

The purified-protein study of the split enzyme (Crona et al. 2015) assigns
the roles explicitly:

- NrdJa carries the catalytic machinery, the AdoCbl site and the
  substrate/allosteric-effector sites:
  [PMID:26225432, "the full catalytic machinery for NTP reduction, including AdoCbl cofactor binding, resides within the NrdJa subunit, and that the main role of NrdJb is to provide thiol-disulfide exchange"].
- NrdJb supplies the C-terminal redox-active cysteine pair that normally sits on
  the C-terminal tail of an intact class II RNR:
  [PMID:26225432, "NrdJa-NrdJb complex formation probably facilitates access between the active site and the redox active cysteines at the C-terminal end of NrdJb"].
- NrdJa alone has measurable but low activity with the artificial reductant DTT;
  both subunits are needed for an efficient enzyme and for B12-dependent growth
  [PMID:15722359, "showed for the first time that presence of both NrdJa and NrdJb subunits were"].
- The active species is a dimer of heterodimers, (NrdJa-NrdJb)2.
- PA NrdJ lacks the overall-activity (dATP) allosteric site:
  [PMID:26225432, "PA NrdJ, as well as more than 90% of all class II RNRs, lacks this latter allosteric site"].

### Substrate: triphosphate, not diphosphate

This matters for the GO term on the PseudoCAP seed. With purified subunits,
the enzyme is a ribonucleoside *tri*phosphate reductase for practical purposes:

- [PMID:26225432, "The results revealed that CTP is the preferred substrate with a >60-fold higher activity compared to CDP"]
- [PMID:26225432, "For NrdJa-NrdJb from PA we found that NTP was the favored substrate."]
- Standard assay: [PMID:26225432, "50 mM Tris-HCl buffer at pH 7.5, 30 mM DTT, 10 mM MgCl2, 100 μM AdoCbl, 1 mM ATP, 1 mM CTP, and 2 μM of NrdJa and NrdJb"],
  giving [PMID:26225432, "the specific activity of the enzyme was determined to be 1.5 nmol/min/mg (with respect to the NrdJa subunit)"].

CDP reduction is real but ~60-fold slower, so GO:0004748 (diphosphate substrate)
is not false, merely the minor reaction. No GO term describes a
cobalamin-dependent RNR without committing to NDP or NTP; the two available
terms are GO:0004748 (NDP, thioredoxin acceptor) and GO:0008998 (NTP,
thioredoxin acceptor).

The physiological electron donor was not identified in the purified-enzyme
study, which used DTT (or TCEP) in vitro; for PMID:15722359 only the abstract
was read (no PMC copy, 2026-10-29), so its reductant is unchecked. The
"thioredoxin disulfide as acceptor" clause of
GO:0004748/GO:0008998 is an assumption from class I/II RNR precedent, not a
measurement in *P. aeruginosa*. *P. aeruginosa* does encode thioredoxins and
glutaredoxins, so the assumption is reasonable but untested here.

### Physiological role

- `nrdJa` transcript rises 6-7 fold on entry to stationary phase while `nrdA`
  falls [PMID:15722359, "Upon entry to stationary phase, the relative amount of nrdJa transcript"].
- AdoCbl rescues hydroxyurea-poisoned cells (HU inactivates class I RNR), which
  shows the class II enzyme can supply dNTPs in vivo
  [PMID:15722359, "Hydroxyurea treatment known to knock out the activity" ... "class II RNRs, was added to the rich medium."].
- The authors' interpretation: [PMID:15722359, "aeruginosa is primarily used for DNA repair and/or possibly DNA replication at"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000171476 | GO:0004748 ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor | 1 (sole seed) | 39 (33 taxa) | GO:0004748 \| IDA \| PMID:15722359 \| PseudoCAP | OVER-SPECIFIC | PMID:15722359 demonstrates class II RNR activity for the NrdJa+NrdJb pair in *P. aeruginosa*, so a cobalamin-dependent RNR activity claim is sound and the gene is squarely inside the clade. Both sub-specifications in the term are unsupported for this gene, however: (i) substrate — the purified enzyme prefers ribonucleoside *tri*phosphates by >60-fold over CDP [PMID:26225432], so GO:0008998 describes the main reaction better; (ii) acceptor — the purified-enzyme study used only DTT/TCEP (the 2005 paper is abstract-only here, so its reductant is unchecked). PTHR43371 itself mixes NDP- and NTP-specific members (its own member list includes several `rtpR` adenosylcobalamin-dependent ribonucleoside-*tri*phosphate reductases), so propagating only the NDP term to 39 leaves across 33 taxa asserts a substrate specificity the node cannot support. The node needs either both terms or a parent that does not fix the phosphorylation state (GO has none below GO:0016728). |

Consequences recorded in the review: a `PSEUDOCAP` defect (`WRONG_TERM`,
`CHECK`) asking that the row be re-pointed to, or accompanied by, GO:0008998;
and a `GO_CENTRAL` defect (`ADD`, `CHECK`) on PTN000171476 asking that the IBD
either add GO:0008998 or stop at a term that does not commit to NDP.

## Open questions

- Which thiol redox protein (thioredoxin, glutaredoxin, NrdH-like) is the
  physiological reductant of the NrdJa-NrdJb enzyme?
- Is the in vivo substrate CTP/NTP, as in vitro, and does the split enzyme feed
  dNTP pools directly or via nucleotide kinases?
