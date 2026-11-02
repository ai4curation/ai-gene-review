# C. albicans ERG2 Notes

## 2026-10-11

`just fetch-gene CANAL ERG2` seeded 10 GOA rows for the reviewed UniProt entry
`A0A1D8PCB9`: three PAINT/IBA rows, three direct or curator-transfer C-8 sterol
isomerase rows, a UniProt ER-membrane row, a UniPathway sterol-biosynthesis
row, a CGD root cellular-component ND placeholder, and a CGD xenobiotic-response
IMP row.

Automated deep research was not available in this environment:

```text
just deep-research-falcon CANAL ERG2 --fallback perplexity-lite
```

failed because neither `agentapi` nor provider API keys were configured. I
therefore did a manual literature and PAINT pass.

### PAINT

`interpro/panther/PTHR10868/PTHR10868-paint.tsv` has one fungal ERG2 ancestor,
`PTN001280219`, carrying `GO:0000247 C-8 sterol isomerase activity` and
`GO:0006696 ergosterol biosynthetic process`. The source list includes the CGD
and SGD ERG2 entries for the activity row and PomBase plus SGD ERG2 entries for
the ergosterol-biosynthesis row, so the Candida IBA assignments come from a
fungal sterol-isomerase node, not from animal Sigma receptors.

The ER row comes from a broader `PTN001328958` eukaryotic ERG2/SIGMAR1-family
node seeded by both fungal ERG2 and animal SIGMAR1 entries. That is a safe
transfer for the shared ER compartment. The animal signaling, postsynaptic, and
neuron-apoptosis rows in this PANTHER family sit on `PTN001593709` and
`PTN008312250`; none propagate to `A0A1D8PCB9`.

### Cached Publications

- PMID:15473366 is abstract-only locally. The abstract confirms that Pierson et
  al. built a viable C. albicans `erg2` mutant for ergosterol-pathway work, but
  it does not expose the full evidence behind CGD's IMP/IGI assignment to C-8
  sterol isomerase activity. I retained those rows because CGD curators had the
  full text and because the enzymatic assignment is corroborated by fungal
  PAINT, ISS from S. cerevisiae ERG2, and the UniProt/Rhea
  fecosterol-to-episterol reaction.
- PMID:17604452 is full text, but the ERG2-specific CaFT result behind
  `GO:0071466 cellular response to xenobiotic stimulus` appears to be in Text
  S1/Table S1 rather than the locally cached main text. The row is biologically
  plausible as a secondary drug-response phenotype and was kept as non-core.
- PMID:15105135 directly tested C. albicans `erg2` mutants and showed altered
  susceptibility to several xenobiotics, supporting the idea that sterol
  composition affects drug response downstream of ERG2's core enzymatic step.
- PMID:24204207 showed that C. albicans ERG2 loss can confer amphotericin B
  resistance, again via altered sterol chemistry rather than a separate core
  molecular function.
- PMID:26231054 followed C. albicans `erg2` and `erg24` deletion mutants and
  found vacuolar, morpholine-susceptibility, hyphal, and disseminated-virulence
  phenotypes. These are downstream consequences of late ergosterol-pathway
  disruption and should not be added as direct ERG2 process annotations.
- PMID:37791798 identified Adr1 as a Candida regulator of ergosterol-pathway
  genes and azole resistance. This is expression-regulation context around ERG2,
  not direct support for another ERG2 function.
- PMID:41251159 used a panel of C. albicans ergosterol-pathway knockout strains
  to image fluorescent polyene probes. This is useful newer context for
  polyene localization in altered-sterol cells but did not change the GO review.

### Curation Decisions

The review has one core function: C-8 sterol isomerase activity at the ER
membrane, directly involved in ergosterol biosynthesis. All three existing
C-8 sterol isomerase rows were accepted. The fungal `PTN001280219` ergosterol
IBA and the eukaryotic `PTN001328958` ER IBA were accepted with
`NO_FAILURE_CORE` propagation reviews. The generic sterol-biosynthesis
UniPathway row was accepted as a true parent of ergosterol biosynthesis. The CGD
root CC/ND placeholder and the CaFT xenobiotic-response phenotype were kept as
non-core.

No new GO rows are proposed. The later vacuolar physiology, hyphal-growth,
virulence, amphotericin-resistance, and polyene-localization papers all report
consequences of sterol alteration rather than independent work done by the ERG2
gene product.
