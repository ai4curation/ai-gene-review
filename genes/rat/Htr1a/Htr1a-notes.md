# Htr1a (rat, P19327) review notes

## Session 1 (initial review)

- `just fetch-gene rat Htr1a` resolved P19327 (5HT1A_RAT); 68 GOA rows.
- No deep-research API; literature synthesis in `Htr1a-deep-research-manual.md`.
- Full text available in cache only for PMID:18442977, PMID:24055683, PMID:24275076;
  the remaining cited papers are abstract-only, so experimental rows were not removed on
  the basis of abstract content alone.

### Key decisions

- Core MF: Gi/o-coupled serotonin receptor activity (GO:0001586). All generic
  GPCR / serotonin receptor MF rows refined to it [PMID:2156831 "it mediates
  agonist-induced inhibition of basal and stimulated cAMP accumulation"; PMID:16772521
  Galpha(o)/Galpha(i3) coupling; PMID:8271204 PTX sensitivity].
- Core BP: adenylate cyclase-inhibiting serotonin receptor signaling pathway (GO:0007198).
  Note GO:0007198 is not a descendant of GO:0007210 "serotonin receptor signaling
  pathway" in the current ontology (it sits under GO:0098664); the GO:0007210 rows are
  refined to it as a semantic, not is_a, refinement.
- PMID:8271204 IMP to GO:0007198: the abstract states cAMP did not alter the 5-HT K+
  response; the paper is about GIRK coupling. Kept (ACCEPT) because the claim holds via
  PMID:2156831 and PMID:12149253 and the curator saw the full text; flagged for expert.
  GO has no current term for GIRK activation by a GPCR (GO:0099109 is obsolete).
- PMID:18442977 "NMDA glutamate receptor clustering": 5-HT1A activation reduces surface
  NR2B clusters and NMDAR currents; receptor does not perform clustering. MODIFY to
  GO:1904782 negative regulation of NMDA glutamate receptor activity.
- FGFR1 interaction rows (protein binding, signaling receptor binding) -> MODIFY to
  GO:0090722 receptor-receptor interaction (an MF under signaling receptor binding).
- Yif1B protein binding -> REMOVE (receptor is the cargo; no informative MF for HTR1A).
- IEP "response to X" rows (morphine, nicotine, alcohol, glycoside): transcript/protein
  level changes after drug treatment; MARK_AS_OVER_ANNOTATED, not core.
- "serotonin metabolic process" ISO/ISS: the receptor does not catalyse any step of 5-HT
  metabolism; REMOVE (over-propagated participation claim).
- No NEW process terms proposed (strict NEW bar).

### Open questions

- Is the presynaptic-membrane localization in basolateral amygdala (PMID:10381597)
  supported by anything beyond 8-OH-DPAT/spiperone pharmacology? 5-HT1A is classically
  somatodendritic/axon-initial-segment.
