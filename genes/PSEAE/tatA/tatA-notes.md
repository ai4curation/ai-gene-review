# tatA (PA5068, Q9HUB5) review notes

## Sources and research (2026-11-05)

Manual research (no deep-research provider). Sources: UniProt Q9HUB5 (Swiss-Prot, HAMAP
MF_00236), the GOA file, cached PMID:16621825 (abstract only; the PubMed MCP returned an
empty PMC body for PMC1447448), and the parallel tatC review (genes/PSEAE/tatC).

- TatA is the single-pass inner-membrane subunit of the twin-arginine translocase that is
  thought to form the protein-conducting channel; it oligomerizes and joins the
  substrate-bound TatBC receptor to form the active translocon (UniProt CC:FUNCTION and
  CC:SUBUNIT, HAMAP MF_00236; one TM segment, residues 1-21).
- In P. aeruginosa, the Tat pathway exports PvdN to the periplasm and is needed for pyoverdine
  production [PMID:16621825 "However, in the tat mutant, no Pvd was produced."];
  [PMID:16621825 "We located PvdN, a still unknown but essential component in Pvd biogenesis, at the periplasmic side of the cytoplasmic membrane and showed that its export is Tat dependent."].
- The abstract does not say which tat gene the mutant lacks. PseudoCAP attached the same
  paper, with the same two terms (GO:0008320 and GO:0033281, IMP), to both tatA and tatC
  (tatC-goa.tsv). If the mutant was a single-gene tatC mutant, the tatA rows would carry the
  paper by operon inference. This cannot be checked without the full text; the claims
  themselves are correct for TatA, so no defect is recorded.

## PseudoCAP IBA-seed assessment

Seeds of PTN002452729 (`.cache/paint/IBD.gaf`, column 8): GO:0033281 and GO:0008320 are each
seeded by P69428 (E. coli TatA), P0A843 (E. coli TatE) and Q9HUB5 (this gene). GO:0043953 at
the same node is seeded by the two E. coli proteins only. QuickGO (2026-11-05): E. coli TatA
has GO:0033281 IDA (EcoCyc, PMID:11279240), GO:0009977 IDA (EcoCyc, PMID:11350936) and
GO:0008320 IGI (PMID:9649434); TatE has GO:0033281 IMP and GO:0008320 IGI (PMID:9649434).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002452729 | GO:0033281 TAT protein transport complex | 3 | 39 (28 taxa) | GO:0033281, IMP, PMID:16621825 (PseudoCAP) | SOUND | The claim is correct: TatA is a core Tat translocase subunit (HAMAP MF_00236, TIGR01411). The paper's evidence is a tat-mutant export phenotype (PvdN, pyoverdine), so it supports membership only indirectly, and the abstract does not say which tat gene was mutated. Node term suits the TatA/E clade. | E. coli TatA (IDA), E. coli TatE (IMP) | Yes. No GO_CENTRAL defect. |
| PTN002452729 | GO:0008320 transmembrane protein transporter activity | 3 | 39 (28 taxa) | GO:0008320, IMP, PMID:16621825 (PseudoCAP) | SOUND | Same paper and caveat. TatA forms the translocation channel, so the activity is right, but the more specific GO:0009977 (proton motive force dependent) is supported by E. coli TatA IDA and is used for tatC. MODIFY on all GO:0008320 rows; the IBD is correct at its level. | E. coli TatA, TatE (IGI) | Yes. No GO_CENTRAL defect. |

Coordination with tatC (PA5070, parallel review): tatC is on a different node
(PTN000769484, TatC family), so no node is shared. The tatC review calls its PMID:16621825
seed rows SOUND; tatA is judged the same way. tatC treats GO:0008320 as TOO_GENERAL because
it carries GO:0009977 by IBA; tatA has no GO:0009977 row, so its GO:0008320 rows are MODIFY
to GO:0009977, which gives the same end state. No node-level defect needed on tatA.

## Annotation decisions

- GO:0033281 (IBA, IEA, IMP): ACCEPT.
- GO:0008320 (IBA, IEA, IMP): MODIFY to GO:0009977 (is_a GO:0008320).
- GO:0043953 (IBA, IEA): ACCEPT; core process.
- GO:0005886 plasma membrane (IEA): ACCEPT. GO:0016020 membrane: TOO_GENERAL.
- GO:0015031 protein transport (IEA): TOO_GENERAL (GO:0043953 is_a GO:0015031).
