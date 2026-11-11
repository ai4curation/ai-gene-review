# slo review notes

## Session 1 (2026-10-28)

- fetch-gene resolved Q03720 (SLO_DROME, reviewed, FlyBase FBgn0003429 per UniProt DR line); GOA keyed to Q03720, 39 rows.
- No deep-research API; literature synthesis in `slo-deep-research-manual.md`.
- Full text read: PMID:12417656, PMID:15569939, PMID:17369364, PMID:25359729, PMID:9502797,
  PMID:21690310 (via PMC full text PMC3216339; cached copy is abstract-only).
  Abstract-only: PMID:10234050, PMID:8973172, PMID:9539129, PMID:9504928, PMID:1497890, PMID:1857984;
  PMID:10798390 has no abstract; PMID:11092827/11715043 are reviews (NAS).

### Decisions
- Core MF: GO:0060072 large conductance calcium-activated potassium channel activity
  [PMID:1497890 "The
  single-channel conductance was 126 pS with symmetrical potassium concentrations."]. All
  GO:0015269 and GO:0005216 rows MODIFY to it.
- K+ transport rows (GO:0006813, GO:0006811, GO:0055085) MODIFY to GO:0071805 potassium ion
  transmembrane transport (carried by IBA).
- membrane -> plasma membrane (MODIFY); plasma membrane NAS ACCEPT [PMID:9502797 "reducing the number of BK channels in the
  plasma membrane"].
- Protein binding IPI rows REMOVE (policy); NEW GO:0019901 protein kinase binding (IPI, PMID:10234050) as non-core,
  since PKAc binds a 172-aa C-terminal region directly.
- circadian rhythm / circadian behavior IMP -> MODIFY to GO:0045475 locomotor rhythm (is_a circadian behavior);
  both papers assay locomotor activity rhythms. Non-core: slo acts on clock output, not the oscillator (PMID:17369364).
- ARBA modulation of chemical synaptic transmission -> MODIFY to GO:1900074 (IMP from PMID:25359729).
- Courtship song, xenobiotic response, NMJ synaptic assembly: KEEP_AS_NON_CORE.

### Heart (PMID:21690310)
- slo expression down in Cdc42/tin compound heterozygote hearts; tin/slo transheterozygotes arrhythmic.
  This is expression + genetic interaction data. Not added as NEW (NEW-term bar). Raised as question.
