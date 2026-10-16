# N (Notch) — curation notes (DROME, P07207)

## Session 2026-09-30 (Notch signaling module)

Deep research: `just deep-research-falcon DROME N --fallback perplexity-lite` — the wrapper reported
a 600 s falcon timeout, but the falcon client completed and wrote `N-deep-research-falcon.md`
later in the session; it was used for corroboration (NRR autoinhibition, glycan tuning). The review
is primarily based on UniProt P07207, cached publications, and the GOA set (298 rows, 163 distinct
terms; no IBA rows for N).

### Key findings (with provenance)

- Receptor: EGF repeats 11-12 are necessary and sufficient for Delta binding, and also bind
  Serrate [PMID:1657403 "We find that of the 36 EGF repeats of Notch, only two, 11 and 12, are both
  necessary and sufficient to mediate interactions with Delta."].
- Signal-competent adhesion with Delta needs both ectodomain and ICD [PMID:15611340 "Both the Notch
  extracellular and intracellular domains are required for the high adhesion force with Delta."].
- ICD has intrinsic activity [PMID:8343960 "Our results indicate that the intracellular domains of
  Lin-12 and Notch have intrinsic activity and that the principal role of the extracellular domains
  in the intact proteins is to regulate this activity."].
- Su(H) binds the RAM region directly [PMID:8749394 "RBP-J kappa and Su(H) bind directly to the
  RAM23 regions of mouse Notch1 and Drosophila Notch, respectively"] and is retained in the
  cytoplasm by Notch until ligand binding [PMID:7954795].
- Ternary complex with Su(H) and Mam [PMID:11390662 "Drosophila Mam forms a similar complex with the
  intracellular domain of Drosophila Notch and Drosophila CSL protein during activation of Enhancer
  of split"]; Mam lengthens CSL dwell time at targets [PMID:29478922].
- NICD ChIP at the chn promoter and E(spl)m-delta (PMID:16763555, full text) — basis of the
  chromatin binding IDA (kept non-core: indirect via Su(H)).

### Decisions
- Core MF: GO:0004888 transmembrane signaling receptor activity (plasma membrane / apical PM);
  GO:0003713 transcription coactivator activity (nucleus, in GO:1990433).
- NEW: GO:0007221 positive regulation of transcription of Notch receptor target (IDA,
  PMID:11390662).
- REMOVE: all 27 GO:0005515 protein binding rows (uninformative; specific functions captured
  elsewhere), GO:0019899 enzyme binding and GO:0019904 protein domain specific binding (ARBA IEA).
- MODIFY: GO:0038023 -> GO:0004888; GO:0032991 -> GO:1990433.
- ~140 developmental BP terms kept as non-core (pleiotropic Notch contexts); lateral inhibition and
  Notch signaling pathway accepted as core.
- Trafficking/biosynthetic compartments (endosomes, MVB, lysosome, ER/Golgi lumen) kept non-core.

### Variant-relevant biology
- Single Notch receptor in Drosophila (vs 4 in mammals), 36 EGF repeats; Fringe (fng)
  GlcNAc-extension of O-fucose alters Notch-Delta binding [PMID:10935637] and inhibits responsiveness
  to Serrate while potentiating responsiveness to Delta [PMID:9202123].
- Ligand-independent activation from endosomes/lysosomes when ESCRT sorting is disrupted
  (UniProt summary; PMID:23178945 etc.).
- PANTHER assignment in the UniProt record: PTHR24049 / PTHR24049:SF22 (labels "CRUMBS FAMILY
  MEMBER" / "DROSOPHILA CRUMBS HOMOLOG" — PANTHER naming quirk; the same family also contains Dl).
