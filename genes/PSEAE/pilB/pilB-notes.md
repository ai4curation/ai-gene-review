# pilB (PA4526, UniProt P22608) review notes

No deep-research provider was available; the notes below are from my own
reading of the cached publications, PubMed and the UniProt entry.

## Identity

- Fetched accession P22608 (PILB_PSEAE), PA4526, 566 aa, matches the
  PseudoCAP worklist entry (rank 11).
- GspE / secretion NTPase superfamily; PANTHER PTHR30258:SF1; NCBIfam
  TIGR02538 (type_IV_pilB); Pfam MshEN (PF05157) + T2SSE (PF00437); Walker A
  ATP site at 326-333 and a C4 zinc site by similarity to Thermus PilF
  [file:PSEAE/pilB/pilB-uniprot.txt].

## Function

- pilB, pilC and pilD are needed to make pili [PMID:1971619 "This report
  describes three novel genes necessary for the formation of pili."].
  PilB function is restricted to pilus biogenesis, unlike PilD
  [PMID:1671384 "The function of the other two accessory proteins, PilB and
  PilC, appears to be restricted to pilus biogenesis"].
- Purified PilB is an ATPase [PMID:18174131 "Assay of purified 6xHis-tagged
  PilB, PilT and PilU from P. aeruginosa showed that all three proteins have
  ATPase activities in vitro."]; it powers extension [PMID:18174131 "PilB and
  PilT are bipolar proteins belonging to the secretion NTPase superfamily, and
  power pilus extension and retraction, respectively"]; Walker A/B mutations
  abolish twitching [PMID:18174131 "Mutation of conserved WA or WB residues in
  any of the three ATPases abrogated twitching motility"].
- Bipolar, cytoplasmic, PilC-dependent localization [PMID:15659660 "YFP-PilB
  exhibited diffuse cytoplasmic localization in a pilC mutant, suggesting that
  PilC is required for polar localization of PilB"].
- Phage D3112 Tip binds and inhibits PilB [PMID:25049409 "Tip interacts with
  and blocks the activity of bacterial-encoded PilB, the TFP
  assembly/extension ATPase"].
- PilB is the only extension motor [PMID:33593905 "PilB is the only known
  extension motor, PilT is considered the primary retraction motor, and PilU
  has been shown to affect retraction"].
- UniProt records FimX stimulation of PilB ATPase (PubMed:28854278) and PilC
  interaction (PubMed:23413032); not cached here, used only via the UniProt
  curated text.

## Reference check: PMID:18174131

Verified against PubMed: Chiang et al. 2008, Microbiology 154:114-126,
"Functional role of conserved residues ... PilB, PilT and PilU". It is the
correct paper for both pilB and pilU (not a mis-keyed neighbour; PMID:18174132
is the ccmC paper in the same issue, pages 127-138). For pilB the IDA term
(ATP hydrolysis activity) is exactly what the abstract reports.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001250205 | GO:0016887 ATP hydrolysis activity | 1 (sole seed) | 90 (36 taxa) | GO:0016887 ATP hydrolysis activity, IDA, PMID:18174131 (PseudoCAP) | SOUND | In vitro ATPase assay of purified P. aeruginosa PilB, reported in the abstract. The Walker A/B and Asp/His box catalytic motifs are invariant across the GspE/PilB extension ATPases, so ATP hydrolysis is a safe and appropriately broad term for this subfamily node. |

The same node also carries an IBD of plasma membrane (is_active_in), seeded
by two other members (P0AFA5, Q00512), which I keep as non-core for PilB
(peripheral, PilC-docked).

## Other PseudoCAP rows

- type IV pilus assembly and type IV pilus-dependent motility (IDA,
  PMID:1671384): claims correct, accepted. PMID:1671384 is a pilD paper whose
  abstract only restates pilB's biogenesis role from PMID:1971619 and has no
  motility assay. Recorded SUSPECTED/CHECK source defects (wrong reference for
  the motility row, IMP rather than IDA for the assembly row). Full text not
  seen, so not overruled.

## Decisions summary

- ACCEPT: cytoplasm (EXP, IEA), ATP hydrolysis activity (IBA, IDA, IEA),
  type IV pilus-dependent motility (IDA, IMP), type IV pilus assembly (IDA).
- KEEP_AS_NON_CORE: plasma membrane (IBA, is_active_in).
- MODIFY: pilus assembly (IEA) -> type IV pilus assembly; cell motility (IMP)
  -> type IV pilus-dependent motility.
