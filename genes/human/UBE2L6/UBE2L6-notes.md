# UBE2L6 (human, O14933) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: UBE2L6 was reviewed as the closest experimentally characterised relative
(ortholog) of a ProtNLM2 benchmark gene (rabbit G1TUN6). Per campaign rules no
ProtNLM2 output was opened or used; this review stands on the literature, UniProt
and PANTHER/PAINT only.

### Deep research

`just deep-research-falcon human UBE2L6 --fallback perplexity-lite` failed: falcon
returned "Exception: Failed to authenticate" and the perplexity-lite fallback returned
HTTP 401 insufficient_quota. No deep-research file exists. The review is built from
the cached GOA-cited publications plus three additional UniProt-cited papers fetched
with `just fetch-pmid` (PMID:20508617, PMID:11237715; PMID:16428300 was already cached).

### Evolutionary placement

- UniProt DR line: `PANTHER; PTHR24067; UBIQUITIN-CONJUGATING ENZYME E2`. PANTHER 19
  places human UBE2L6 in `PTHR24068:SF43` "UBIQUITIN_ISG15-CONJUGATING ENZYME E2 L6"
  (verified in `interpro/panther/panther.obo`), a subfamily separate from the UBE2L3
  (UbcH7) subfamilies.
- PAINT (`interpro/panther/PTHR24068/PTHR24068-paint.tsv`):
  - `PTN000631065` (taxon:40674 Mammalia), seeds MGI:1914500 (mouse Ube2l6) and
    UniProtKB:O14933 itself: IBD for GO:0042296 ISG15 transferase activity and
    GO:0032020 ISG15-protein conjugation. ISG15 conjugation is thus inferred as an
    inherited mammalian UBE2L6 function, grounded on the human and mouse experiments.
  - `PTN000631055` (UBE2L3/UBE2L6 class; seeds include UBE2L3 P68036, fly, yeast UBC4/5
    lineage, worm) carries GO:0006511 ubiquitin-dependent protein catabolic process.
  - `PTN002514495` (deep E2 node) carries GO:0061631 ubiquitin conjugating enzyme activity
    and GO:0000209 protein polyubiquitination.
  - `PTN002374306` (seed UniProtKB:P68036 UBE2L3 only) carries GO:0070979 protein K11-linked
    ubiquitination. UBE2L6 does not inherit it: PAINT placed it on the UBE2L3 branch, so it
    is treated as a deliberate decision and not transferred.
- The family review `interpro/panther/PTHR24068/PTHR24068-review.yaml` does not mention
  UBE2L6/SF43, so no family-level member exception applies.

### Experimental findings in human (or human proteins)

- E2 for ISG15: purified from IFN-beta-treated A549 cells as the E2 charged by E1(ISG15)
  and identified by Edman sequencing as UbcH8 [PMID:15131269 "Its sequence, AEEFTLR, was
  identical to a sequence in UbcH8 (amino acids 149-155), an E2 for Ub"]; E1(ISG15)-dependent
  thioester transfer in vitro with purified proteins [PMID:15131269 "These results indicate
  that ISG15 was transferred from E1 ISG15 to UbcH8, and that UbcH8 functions as an E2 for
  ISG15."]; siRNA in IFN-treated HeLa cells reduced ISGylation [PMID:15131269 "UbcH8 serves
  as a major E2 enzyme for ISG15 conjugation in vivo"]. UbcH5b gave no ISG15 thioester and
  UbcH7 about 5% of UbcH8.
- Independent confirmation [PMID:15485925 "The reduction of Ubc8 expression by small
  interfering RNA causes a decrease in protein ISGylation in HeLa cells upon interferon
  treatment."]; UbcH7/UbcM4 and Ubc9 do not support ISGylation.
- Interferon-inducible [PMID:15131269 "the UbcH8 gene is transcriptionally induced by
  IFN-α/β"].
- Ubiquitin E2: cloned as an E6AP (HECT) interactor; supports E6AP ubiquitination of an
  E6-independent substrate [PMID:9153201]. With the yeast HECT Rsp5p, UbcH8 supports
  polyubiquitination of WBP2 in vitro [PMID:15131269 "Rsp5p catalyzed efficient
  polyubiquitination of WBP2 in the presence of E1 Ub and UbcH8"]. Partners with RING/RBR E3s:
  Staring/RNF40 (syntaxin 1 degradation) [PMID:12121982], Dorfin/RNF19A [PMID:11237715],
  p53RFP/RNF144B [PMID:16427630], NKLAM/RNF19B [PMID:16709802]; SIAH1 with UBCH8 targets
  FLT3-ITD for proteasomal degradation [PMID:20508617].
- UbcH8 is itself ISGylated [PMID:16428300].
- High-throughput Y2H/interactome data (PMID:19549727, 19690564, 25416956, 32296183,
  31515488, 33961781, 32814053) mostly recover RBR/RING E3s (ARIH2, RBCK1, LONRF1, DTX3,
  TRIM8, TRIM62, MID1, RNF216, RNF144B), consistent with an E2 that pairs with
  HECT/RBR-type ligases. GNB2 and LITAF hits have no functional context.
- Shigella OspG binds E2~Ub conjugates including UbcH8 [PMID:24446487] (host-pathogen,
  not a UBE2L6 function).
- PMID:28724761 (HEV): knockdown of UBE1L or UBE2L6 did not change HEV type I IFN
  sensitivity; the paper is weak support for "innate immune response" for UBE2L6
  specifically, but UBE2L6 does catalyse a step of IFN-induced ISGylation of antiviral
  targets (RIG-I, MxA, PKR per PMID:16009940 and Reactome), so kept as non-core.

### Decisions summary

- Core: GO:0061653 ISG15 conjugating enzyme activity (EXP) and GO:0061631 ubiquitin
  conjugating enzyme activity; process GO:0032020 ISG15-protein conjugation.
- GO:0042296 ISG15 transferase activity (IBA/IDA/IEA) -> MODIFY to GO:0061653 (descendant
  the gene already carries). General MF/BP parents (GO:0004842, GO:0019787, GO:0061650,
  GO:0016567, GO:0032446, GO:0036211) -> MODIFY to specific terms already carried.
- Bare GO:0005515 rows: MODIFY to GO:0031625 ubiquitin protein ligase binding for E3
  partners; REMOVE for GNB2, LITAF and the Shigella OspG effector.
- Cytoplasm -> MODIFY to cytosol (carried via Reactome); nucleoplasm kept as non-core
  (TRIM25-mediated PCNA ISGylation).

### Transfer guidance (for orthologs such as rabbit G1TUN6)

Transfer is supported only within the UBE2L6 subfamily (PTHR24068:SF43 / PAINT node
PTN000631065, Mammalia): ISG15 E2 activity and ISG15 conjugation, plus the generic
ubiquitin E2 activity inherited from the deep E2 node. Do not transfer UBE2L3-branch
terms (e.g. K11-linked ubiquitination) or E3-partner-specific substrates.
