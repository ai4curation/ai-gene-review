# msrA (PA5018, Q9HUF1) review notes

Peptide methionine (S)-sulfoxide reductase MsrA (HAMAP MF_01401, PMSR Pfam).

## Literature (no deep-research provider available; own reading)

- Romsang et al. 2013 (full text cached, PMC3719549): msrA is constitutively and
  highly expressed; msrB is oxidant-inducible. msrA mutants are less resistant to
  NaOCl and H2O2 [PMID:23687271 "rendered the mutants less resistant than the
  parental PAO1 strain to oxidants such as NaOCl"], and plasmid msrA fully
  complements [PMID:23687271 "pBBR msrA and pBBR msrB plasmids fully complemented
  the NaOCl-sensitive phenotypes of msrA and msrB mutants to resistance levels
  attained by the parental strain"]. msrA mutants are paradoxically more
  paraquat resistant, and msrA/msrB mutants are attenuated in a Drosophila model.
  The paper does not assay Msr enzyme activity; the MF rows rest on family
  (IBA/IEA) inference, which is strong for MsrA.
- Comparator for the BP: MsrA repairs oxidised Met residues itself, so it does
  some of the work of the oxidative-stress response (not only required for it).
  Other seeds at the same node carry the same term by IMP (yeast MXR1, S. pombe
  mxr1, Arabidopsis MSRA2/MSR4, A. nidulans).
- PubMed MCP search returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Seed support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000019085 | GO:0034599 cellular response to oxidative stress | 7 | 289 (116 taxa) | GO:0034599, IMP, PMID:23687271 (PseudoCAP) | SOUND | Full text read: deletion reduces NaOCl and H2O2 resistance and is complemented; MsrA directly repairs oxidised proteins, so this is participation, not an indirect phenotype. | S. cerevisiae MXR1 P40029 (IMP/IGI), S. pombe mxr1 Q09859 (IMP), Arabidopsis MSRA2 Q9LY15 (IMP) and MSR4 P54150 (IMP/IEP), A. nidulans C8V8B9 (IMP), Drosophila MsrA P08761 (IEP) | Yes; five independent IMP seeds across fungi and plants |

No PSEUDOCAP or GO_CENTRAL defect. The node is the MsrA family; the term suits it.
