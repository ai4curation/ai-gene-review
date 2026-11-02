# N. crassa erg-1 Notes

## 2026-10-11

`just fetch-gene NEUCR erg-1` seeded five GOA rows for the reviewed UniProt
entry `Q92254`: three PAINT/IBA rows for C-8 sterol isomerase activity,
endoplasmic reticulum, and ergosterol biosynthesis, plus UniProt/UniPathway IEA
rows for endoplasmic-reticulum membrane localization and sterol biosynthesis.

Automated deep research was not available in this environment:

```text
just deep-research-falcon NEUCR erg-1 --fallback perplexity-lite
```

failed because neither `agentapi` nor provider API keys were configured. I
therefore did a manual literature and PAINT pass.

### PAINT

`interpro/panther/PTHR10868/PTHR10868-paint.tsv` has one fungal ERG2 ancestor,
`PTN001280219`, carrying `GO:0000247 C-8 sterol isomerase activity` and
`GO:0006696 ergosterol biosynthetic process`. The source list includes the CGD
and SGD ERG2 entries for the activity row and PomBase plus SGD ERG2 entries for
the ergosterol-biosynthesis row, so the Neurospora IBA assignments come from a
fungal sterol-isomerase node, not from animal Sigma receptors.

The ER row comes from a broader `PTN001328958` eukaryotic ERG2/SIGMAR1-family
node seeded by both fungal ERG2 and animal SIGMAR1 entries. That is a safe
transfer for the shared ER compartment. The animal signaling, postsynaptic, and
neuron-apoptosis rows in this PANTHER family sit on `PTN001593709` and
`PTN008312250`; none propagate to `Q92254`.

### Cached Publications

- PMID:33046504 is full text locally. Weichert et al. sequenced the classical
  `erg-1` mutant, created an `erg-1` knockout strain, and confirmed by GC/MS
  that loss of erg-1 blocks ergosterol biosynthesis and causes accumulation of
  sterol intermediates with a double bond between C-8 and C-9 rather than C-7
  and C-8. Those data corroborate the enzymatic assignment and the ergosterol
  pathway row.
- The developmental and plasma-membrane fusion phenotypes in PMID:33046504 are
  downstream consequences of altered sterol composition. They do not justify
  adding direct erg-1 annotations to vegetative germling fusion, fruiting body
  formation, or asexual sporulation.

### Curation Decisions

The review has one core function: C-8 sterol isomerase activity at the ER
membrane, directly involved in ergosterol biosynthesis. All five seeded rows
were accepted. The fungal `PTN001280219` C-8 sterol isomerase and
ergosterol-biosynthesis IBAs were accepted with `NO_FAILURE_CORE` propagation
reviews, as was the broader eukaryotic `PTN001328958` ER-localization IBA. The
UniPathway sterol-biosynthesis row was accepted as a true parent of ergosterol
biosynthesis, and the UniProt ER-membrane row was accepted as the most specific
current compartment annotation for erg-1.

No new GO rows are proposed. The 2020 phenotypes identify cellular processes
that require proper sterol B-ring chemistry, not additional processes executed
by the ERG-1 enzyme itself.
