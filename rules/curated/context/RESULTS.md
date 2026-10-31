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

## All archaeal proteomes with IPR000426 (2026-10-31)

Run with `just evaluate-module-context rules/curated/context/ubiquitin_transfer_relay.yaml
--rule rules/curated/CR-0003.yaml --taxon 2157`. The bulk mode streams one UniProt query
per signature across Archaea instead of one count per proteome; for the seven
archaeal proteomes resolved individually above it gave identical counts.

888 archaeal UniProtKB entries match IPR000426. 873 of them belong to 610 proteomes,
all of them reference proteomes; 15 belong to no proteome and cannot be evaluated, so
the rule still fires on them.

| Verdict | Proteomes | IPR000426 proteins | CR-0003 |
|---|---|---|---|
| unsatisfiable (complete proteome, relay absent) | 501 | 733 | blocks GO:0006511 |
| satisfiable | 3 | 6 | keeps GO:0006511 |
| not evaluated (BUSCO below 95) | 106 | 134 | keeps GO:0006511 |
| no proteome | - | 15 | keeps GO:0006511 |

So CR-0003 removes 733 of the 888 archaeal GO:0006511 annotations the InterPro2GO
mapping produces (83%). The other 155 keep it: 6 because the relay is detected, 149
because the evidence is not good enough to call it absent.

Every not-evaluated proteome failed on BUSCO alone (type and assembly level passed).
The cut-off of 95 is a policy choice: lowering it would block more proteins at more
risk of calling a detection gap an absence.

The three satisfiable proteomes:

| Proteome | Organism | UBC E2 | Ubiquitin-like | RING | Notes |
|---|---|---|---|---|---|
| UP000321408 | *Promethearchaeum syntrophicum* (Asgard) | A0A5B9D7T8 | A0A5B9D6M8 | A0A5B9DAL9, A0A5B9DG89 | BUSCO 89; satisfiable regardless of completeness |
| UP001208689 | *Candidatus* Lokiarchaeum ossiferum (Asgard) | 2 | 2 | 1 | BUSCO 87 |
| UP000030787 | *Candidatus* Methanoplasma termitum | A0A0A7LA35 (161 aa) | A0A0A7LA92 (80 aa) | A0A0A7LF26 (175 aa) | BUSCO 98; a termite-gut Thermoplasmata methanogen, not an Asgard archaeon |

The *Methanoplasma* hit was not expected. It carries one small UBC E2, one
ubiquitin-like protein and one RING protein, which may be a minimal ubiquitin-like
operon or a horizontal acquisition; this was not assessed. Two incomplete haloarchaeal
proteomes, *Halolamina pelagica* (UP000050535) and *Halosegnis longus* (UP000270581), each
carry a single UBC-domain protein but lack a RING or ubiquitin-like protein
respectively, so the relay is not satisfied; being below the completeness threshold,
they are not evaluated and keep the term.

## Limits

- Detection is by InterPro signature presence only; a matching domain is not proof
  of a working enzyme.
- Bacterial and other non-eukaryotic, non-archaeal IPR000426 entries (74) were not
  resolved; run the bulk mode with `--taxon 2` to add bacteria.
