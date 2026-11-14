# PA4218 (ampP / ampGh1, Q9HWG8) review notes

MFS permease, 414 aa, 10 TM helices by PhoA/LacZ fusions. Unreviewed UniProt
entry ("Probable transporter"). NCBIfam TIGR02718 sider_RhtX_FptX; TC
2.A.1.57.1; PANTHER PTHR12778 (same family as AmpG). 19% identical to AmpG
(PA4393). Second gene of the ampO-ampP operon (PA4219-PA4218).

## Literature (no deep-research provider available; own reading)

- Kong et al. 2010 (full text read). Topology: 10 TM helices
  [PMID:21192796 "consistent with 10 TM domains (Figures 4A and 4B)."]. ampP
  mutant lacks maximal beta-lactamase induction and benzylpenicillin induction
  of the ampC promoter [PMID:21192796 "Benzyl-penicillin dependent induction of
  PampC-lacZ was lost in PAOampG or PAOampP (Figure 6)."]. The paper reports no
  transport assay; it says only that the topologies are consistent with
  transport.
- Zhang et al. 2010 (abstract only): ampGh1 (PA4218) deletion had little effect
  on resistance and PA4218 does not complement ampG mutants [PMID:20713660
  "resistance while ampGh1 deletion had little effect on the resistance"].
- The RhtX/FptX subfamily assignment suggests a siderophore (ferripyochelin)
  permease; I could not retrieve the FptX literature (PubMed API errors on
  2026-11-05), so the substrate is left open and no siderophore term is
  asserted.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008542531 | GO:0022857 transmembrane transporter activity | 4 | 45 (40 taxa) | GO:0022857, IDA, PMID:21192796 (PseudoCAP) | UNVERIFIABLE | Full text read: topology fusions and induction phenotypes only, no transport assay. The term is plausible on family evidence, but the paper does not show the activity, so the IDA code is wrong. | human SLC33A1 O00400 (IDA), E. coli AmpG P0AE16 (IDA), AmpG PA4393 G3XCT7 (PseudoCAP IMP, SOUND) | Yes; see ampG notes for the node-level judgement |

PSEUDOCAP defect: WRONG_EVIDENCE_CODE on the GO:0022857 IDA row, CONFIRMED
(full text read), requested change CHECK (downgrade to ISS or remove). The
term stays accepted on the IBA/IEA rows. No GO_CENTRAL defect; the node-level
assessment is recorded once on ampG.

### Other PseudoCAP rows (not seeds)

| term | verdict | defect |
|---|---|---|
| GO:0009276 Gram-negative-bacterium-type cell wall (IDA) | WRONG | PSEUDOCAP WRONG_TERM, CONFIRMED: the paper's own topology shows an inner-membrane protein; repoint to GO:0005886. |
| GO:0033252 regulation of beta-lactamase activity (IDA) | WRONG | PSEUDOCAP WRONG_TERM, CONFIRMED: the effect is on ampC promoter induction, not on the enzyme. |
| GO:0046677 response to antibiotic (IDA) | SOUND-ish, non-core | none (downstream phenotype; companion paper found little effect on resistance). |
