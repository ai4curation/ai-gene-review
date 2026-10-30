# Module-context oracle: MODULE:ubiquitin_transfer_relay

Detector: `ubiquitin_transfer_relay.yaml`. Cache (counts of proteome members per
InterPro signature, proteome completeness, CR-0003 matches): `cache/ubiquitin_transfer_relay.yaml`.
Reproduce or extend with:

```bash
just evaluate-module-context rules/curated/context/ubiquitin_transfer_relay.yaml UP000005640 ... --rule rules/curated/CR-0003.yaml
```

Counts come live from UniProt REST (2026-10-30 run) and change with releases; add
`--refresh` to re-fetch cached proteomes.

## Results (2026-10-30)

| Proteome | Organism | BUSCO | UBC E2 (IPR000608) | Ubiquitin-like (IPR000626) | Verdict | CR-0003 |
|---|---|---|---|---|---|---|
| UP000005640 | *Homo sapiens* | 99 | 268 | 398 | satisfiable | annotates 72 |
| UP000002311 | *Saccharomyces cerevisiae* S288c | 99 | 14 | 14 | satisfiable | annotates 7 |
| UP000008243 | *Haloferax volcanii* DS2 | 99 | 0 | 0 | unsatisfiable | blocks 2 |
| UP000000242 | *Metallosphaera sedula* DSM 5348 | 98 | 0 | 0 | unsatisfiable | blocks 1 |
| UP000001584 | *Mycobacterium tuberculosis* H37Rv | 99 | 0 | 0 | unsatisfiable | 0 matches |
| UP000321408 | *Promethearchaeum syntrophicum* (Asgard) | 89 | 1 | 1 | satisfiable | annotates 2 |
| UP001208689 | *Candidatus* Lokiarchaeum ossiferum (Asgard) | 87 | 2 | 2 | satisfiable | annotates 3 |
| UP000050535 | *Halolamina pelagica* | 86 | 1 | 0 | not evaluated (incomplete) | annotates 2 |

"Satisfiable" means every module step (E1, E2, E3) and the detector's extra
ubiquitin-modifier step has at least one matching protein. "Unsatisfiable" is
reported only for a complete proteome (reference proteome, full assembly, BUSCO
at least 95); otherwise the verdict is "not evaluated" and the rule still fires.

## What this shows

- The two haloarchaeal and sulfolobal proteomes have only a ThiF-fold activating
  enzyme (the SAMP/MoaD system) and no UBC E2 or ubiquitin-like protein, so CR-0003
  blocks ubiquitin-dependent catabolism on their proteasome alpha subunits.
- The two Asgard proteomes contain a UBC E2, a ubiquitin-like-domain protein and a
  RING protein, so the rule keeps the term there. A plain Eukaryota condition would
  have blocked them. Whether these Asgard systems are functional ubiquitin systems
  was not assessed here; the detector only shows the components are encoded.
- *Halolamina pelagica* has one UBC-domain protein but no ubiquitin-like protein.
  Its proteome is below the completeness threshold, so the oracle declines to call
  the module absent. The single UBC hit in a haloarchaeon is unusual and was not
  investigated.
- *M. tuberculosis* proteasome subunits do not match IPR000426, so the InterPro
  mapping never reached them; bacterial proteasomes are outside this rule.

## Limits

- Detection is by InterPro signature presence only; a matching domain is not proof
  of a working enzyme.
- The cache covers eight proteomes. Applying CR-0003 at scale means resolving every
  proteome that has an IPR000426 member (about 900 archaeal entries).
