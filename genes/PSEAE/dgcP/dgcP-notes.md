# dgcP (PA5487, Q9HT84) review notes

Reviewed UniProt entry (DGCP_PSEAE), 671 aa, GGEEF domain with DGCcoil
(PF20975). No TRANSMEM feature; a Kyte-Doolittle scan (19-residue window, mean
above 1.6, run in this session) finds no hydrophobic window. UniProt places DgcP
at the inner membrane only by similarity to PA14 DgcP (A0A0H2ZJS2), via
FimV-dependent polar recruitment, which would make it a peripheral membrane
protein.

## Literature (no deep-research provider available; own reading)

- Kulasakara et al. 2006 (PMID:16477007; cached copy abstract only, full text
  PMC1413825 read on the PMC web page, excerpts verbatim below). Cells
  overexpressing PA5487 accumulated 109 pmol c-di-GMP per mg wet cell weight;
  PA5487 insertion abolished biofilm formation in PA14.
- Aragon et al. 2015 (PMID:25809128; abstract only). DgcP activity in P.
  savastanoi depends on an intact GGDEF domain; deletion of dgcP in P.
  savastanoi and P. aeruginosa PAK increases motility and reduces biofilm
  [PMID:25809128 "deletion of the dgcP gene revealed that DgcP negatively
  regulates motility and positively controls biofilm formation in both the olive
  tree pathogen P. savastanoi pv. savastanoi and the human opportunistic pathogen
  Pseudomonas aeruginosa"]. Source of the UniProt EXP row. From the abstract it
  is unclear whether the P. aeruginosa protein itself was assayed; the term is
  correct regardless (PMID:16477007).
- UniProt FUNCTION (curated, ECO:0000269 PubMed:25809128): "Catalyzes the
  synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP
  molecules".

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IDA, PMID:16477007 (PseudoCAP) | SOUND | Cells overexpressing PA5487 accumulated 109 pmol/mg c-di-GMP (Table 1, full text read). | E. coli DosC, DgcC, DgcJ, DgcM, DgcN, DgcQ, DgcZ and others; B. subtilis DgcK, DgcP; Shewanella Q8EGF8; P. aeruginosa wspR, PA1107, PA2870, PA3177, PA3343, PA4332, PA4843 | Yes. Many seeds with direct activity evidence; DgcP also has a UniProt EXP row. No GO_CENTRAL defect. |

Batch consistency: see wspR-notes.md. All seed rows for PTN002895344 in this
batch are SOUND except the wspR IMP (PMID:12426335).

## Non-seed IBA node PTN002895351

The node-level GO_CENTRAL defects for PTN002895351 (plasma membrane; GO:0043709)
are recorded once, on wspR. For DgcP:

- PM (IBA, IEA, ISS): KEEP_AS_NON_CORE. The IBA's reasoning (TM seeds) does not
  apply, but polar, FimV-dependent membrane association by similarity to PA14
  DgcP makes a peripheral PM location plausible.
- GO:0043709 IBA: MARK_AS_OVER_ANNOTATED (regulates biofilm through c-di-GMP).
- GO:1902201 IBA: ACCEPT (deletion is hypermotile, PMID:25809128).

## Verbatim excerpts from PMID:16477007 full text (PMC1413825, PMC web page)

- PA5487 GGEEF +(109)
- DGC activity is measured as pmol of c-diGMP produced per mg wet cell weight.
- Insertions in PA0169 , PA1120 , PA4959 , and PA5487 abolished biofilm formation
