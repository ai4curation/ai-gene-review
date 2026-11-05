# ampG (PA4393, G3XCT7) review notes

MFS permease of the AmpG/SLC33 family (TC 2.A.1.25.5; InterPro IPR004752
AmpG_permease/AT-1; PANTHER PTHR12778). Unreviewed UniProt entry. 594 aa,
14 TM helices by PhoA/LacZ fusions. Second gene of the ampF-ampG operon.

## Literature (no deep-research provider available; own reading)

- Zhang et al. 2010 (abstract only; PMC2976151 returned no full text via the
  PubMed MCP on 2026-11-05). E. coli AmpG imports GlcNAc-anhMurNAc and its
  peptides, the ampC inducer [PMID:20713660 "transports
  1,6-GlcNAc-anhydro-MurNAc and the 1,6-GlcNAc-anhydro-MurNAc peptide"].
  PA4393 inactivation strongly lowers intrinsic beta-lactam resistance
  [PMID:20713660 "inactivation of ampG drastically repressed the intrinsic
  β-lactam resistance"]; cloned PA4393 complements P. aeruginosa and E. coli
  ampG mutants [PMID:20713660 "The cloned ampG gene is able to complement both
  the P. aeruginosa and the E. coli ampG mutants"]; PA4218 does not.
- Kong et al. 2010 (full text read). AmpG topology: 14 TM helices
  [PMID:21192796 "suggesting that AmpG has only 14 TM helices (Figures 4C and
  4D)."]; ampC promoter induction lost in ampG and ampP mutants
  [PMID:21192796 "Benzyl-penicillin dependent induction of PampC-lacZ was lost
  in PAOampG or PAOampP (Figure 6)."]. No transport assay.
- IPR024371 (AcetylCoA_trans_1-like) InterPro2GO maps acetyl-CoA transport,
  the function of the animal SLC33A1 branch; wrong for bacterial AmpG (rows
  removed).

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008542531 | GO:0022857 transmembrane transporter activity | 4 | 45 (40 taxa) | GO:0022857, IMP, PMID:20713660 (PseudoCAP) | SOUND | Abstract: PA4393 complements the E. coli ampG mutant, so it is the functional muropeptide permease. Generic term correct (gene-level refinement GO:0015647). | human SLC33A1 O00400 (IDA GO:0008521 acetyl-CoA transporter), E. coli AmpG P0AE16 (IDA GO:0015647), P. aeruginosa PA4218 Q9HWG8 (PseudoCAP IDA; evidence code defective, see PA4218 notes) | Yes; two independent IDA seeds |

Node-level judgement (recorded here, the gene with the most direct
evidence, for the batch): the node spans bacterial AmpG-like permeases and
animal SLC33A1 acetyl-CoA transporters, so the generic transporter term is
the right level and the IBD is sound. No GO_CENTRAL defect. PA4218 shares the
node; its PseudoCAP IDA row has a WRONG_EVIDENCE_CODE defect (topology only)
but the IBD does not depend on it.

### Other PseudoCAP rows (not seeds)

| term | verdict | defect |
|---|---|---|
| GO:0009276 Gram-negative-bacterium-type cell wall (IMP) | WRONG | PSEUDOCAP WRONG_TERM, CONFIRMED: GO:0009276 is the peptidoglycan layer; AmpG is a 14-helix inner-membrane protein (topology, PMID:21192796 full text). Repoint to GO:0005886. Same defect on PA4218. |
| GO:0033252 regulation of beta-lactamase activity (IMP) | WRONG | PSEUDOCAP WRONG_TERM, PROBABLE (abstract only): AmpG imports the inducer of ampC expression; it does not act on the enzyme. |
| GO:0046677 response to antibiotic (IMP) | SOUND, non-core | none |
