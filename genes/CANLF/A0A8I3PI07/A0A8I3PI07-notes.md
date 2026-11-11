# A0A8I3PI07 (dog CNNM4) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used.

### Identity
- A0A8I3PI07 is an unreviewed (TrEMBL) dog CNNM4 gene model, 796 aa, gene CNNM4.
- Full-length, not a fragment or isoform: 92.6% identity to human CNNM4 Q6P4Q7 (775 aa)
  over all 775 aligned columns; 65.9% to human CNNM2, so CNNM4 ortholog not a paralog
  [file:CANLF/A0A8I3PI07/A0A8I3PI07-bioinformatics/RESULTS.md].
- Extra ~21 aa (3 + 18 aa insertions near positions 645-670) after the CBS pair; signal
  peptide, CNNM TM domain (178..358) and CBS domain present. Possibly an alternative exon;
  not resolved.
- PANTHER PTHR12064:SF26 (METAL TRANSPORTER CNNM4), same subfamily as human Q6P4Q7 and
  mouse Q69ZF7 (interpro/panther/PTHR12064/PTHR12064-entries.csv).

### Evolutionary basis
- PAINT nodes: PTN000248898 (plasma membrane, family-wide), PTN008532859 (Mg2+
  homeostasis, eukaryotes), PTN002635769 (Euteleostomi; Mg2+ and Na+ transporter
  activities and Mg2+ transport, seeded only by mouse Cnnm4 MGI:2151060). The dog sits
  under all three. The CNNM4-specific node makes ortholog transfer of the exchange
  activity sound.
- No dog experimental literature. Evidence used: mouse/human CNNM4
  [PMID:24339795 "In the absence of extracellular Na+, Mg2+ depletion did not induce Mg2+
  extrusion (Phase 3), but restoration of Na+ instantaneously caused Mg2+ extrusion
  (Phase 4)."]; human structure [PMID:42497866 "the outward-facing state, thereby
  promoting Mg2+/Na+ exchange."].

### Changes vs. previous draft
- Mg2+ and Na+ transporter MF rows (IBA+IEA): UNDECIDED/ACCEPT -> MODIFY to GO:0061768
  magnesium:sodium antiporter activity, matching genes/human/CNNM4. Core MF switched to the
  antiporter term; Na+ transmembrane transport now accepted.
- Generic terms (membrane, transmembrane transporter activity, transmembrane transport,
  intracellular monoatomic cation homeostasis) changed from ACCEPT/KEEP_AS_NON_CORE to
  MODIFY with specific replacements already supported (GO:0010961 for the last).
- Added real literature references and a sequence-comparison analysis.
- Not added as NEW: TRPM7 ion channel regulator activity and ATP binding (human IDA
  only, not in GOA/PAINT; left as a suggested question).
- Caveat: GO:0061768 definition is written in the Mg2+-import direction.

### Relative
- Closest characterised relative: human CNNM4 (Q6P4Q7, same SF26), reviewed in
  genes/human/CNNM4/ (complete). Mouse Cnnm4 (Q69ZF7) has no review folder.
- Family review interpro/panther/PTHR12064/PTHR12064-review.yaml agrees with SF26
  placement. No modules mention CNNM4.
