# avr-15 curation notes

## 2026-11-22

`just fetch-gene worm avr-15` seeded 19 GOA rows for UniProtKB G5ECH3. The
accession is the C. elegans `avr-15` / `R11G10.1` TrEMBL record. Unlike the
Q8IFY7 `avr-14` accession curated immediately before it, G5ECH3 is long enough
to encode an extracellular Cys-loop ligand-binding domain and the transmembrane
pore region: the UniProt record is 657 aa, carries Pfam `Neur_chan_LBD` and
`Neur_chan_memb` hits, and has `FT TRANSMEM` predictions.

Follow-on fetches:

- `just fetch-gene-pmids worm avr-15` found PMID:15238517, PMID:16527366 and
  PMID:12750328; these are now cached.
- `just fetch-pmid 9312045 9407104` added the primary avr-15 cloning/oocyte
  expression papers.
- `just mod-description-deep-research worm avr-15` fetched the WormBase curated
  description as `avr-15-deep-research-wormbase.md`.
- `just paint-losses worm avr-15` reported no IRD or IKR loss on this gene's
  lineage.
- `just deep-research-falcon worm avr-15 --fallback perplexity-lite` could not
  run here because the deep-research client reported that `agentapi` was
  missing and only `claude_code` was available; no provider deep-research file
  was written.

Dent, Davis and Avery is abstract-only in the local cache but provides the
central avr-15 evidence: `avr-15` is necessary postsynaptically for functional
M3 synapses and for glutamate's hyperpolarizing effect on pharyngeal muscle,
encodes two alternatively spliced GluCl channel subunits, and produces a
homomeric ivermectin-sensitive, glutamate-gated channel
[PMID:9312045, "avr-15, a gene that confers ivermectin sensitivity on worms";
PMID:9312045, "An avr-15-encoded subunit forms a homomeric channel"]. The
Vassilatis et al. abstract independently supports the same channel assignment
for GluClalpha2, later identified as AVR-15, and records both homomeric
GluClalpha2 channels and heteromeric GluClalpha2/GluClbeta channels
[PMID:9407104, "This subunit forms homomeric channels"].

Dent et al. 2000 is full text locally and places AVR-15 in the three-pathway
ivermectin-sensitivity system with AVR-14 and GLC-1 [PMID:10716995,
"simultaneous mutation of three genes, avr-14, avr-15, and glc-1"]. Keane and
Avery is abstract-only but verifies that `avr-15` and `avr-14` participate in
the glutamatergic pathway linking adult tail tap to inhibition of pharyngeal
pumping [PMID:12750328, "Tail tap of adults inhibits pharyngeal pumping"].

The Cook et al. abstract supports the locomotion rows at the level WormBase
curated: four GluClalpha subunits regulate the pattern of C. elegans locomotor
activity. I retained these rows as real, non-core motor-system contexts because
they are downstream of the receptor's core molecular function.

PMID:15238517 is a WormBase source for the `GO:0001508 action potential` and
one `GO:0043051 regulation of nematode pharyngeal pumping` row, but the cached
abstract is about GAR-3 and does not name `avr-15`. I did not second-guess the
WormBase full-text curation from the abstract alone; the rows are kept as
non-core pharyngeal-muscle physiology because the direct Dent et al. avr-15
evidence independently establishes postsynaptic M3 signaling and
glutamate-induced pharyngeal-muscle hyperpolarization.

The GO-CAM `GO:0060079 excitatory postsynaptic potential` row propagates a
sign error from `GO:0005231 excitatory extracellular ligand-gated monoatomic ion
channel activity`. AVR-15 opens chloride channels and mediates inhibitory
hyperpolarization, so I modified the PAINT `GO:0005231` row to the inhibitory
extracellular ligand-gated channel parent, removed the excitatory-postsynaptic
row, and proposed `GO:0008068 extracellularly glutamate-gated chloride channel
activity` as the specific missing molecular function.
