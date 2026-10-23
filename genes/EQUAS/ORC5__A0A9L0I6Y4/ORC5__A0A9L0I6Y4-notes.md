# ORC5 (donkey, A0A9L0I6Y4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: A0A9L0I6Y4 is the canonical-length (435 aa) donkey ORC5 product of Ensembl gene
ENSEASG00005017348, the same gene as benchmark entry A0A9L0JAR4 (reviewed separately in
`genes/EQUAS/ORC5/`). Folder uses the `<HOST>__<ACC>` convention because `genes/EQUAS/ORC5`
is keyed to A0A9L0JAR4. No ProtNLM2 output was opened or used.

Deep research: `just deep-research-falcon EQUAS ORC5__A0A9L0I6Y4 --fallback perplexity-lite`
failed (falcon "Failed to authenticate"; perplexity HTTP 401 insufficient quota). The review
uses cached human ORC literature instead.

Evolutionary grounding (`ORC5__A0A9L0I6Y4-bioinformatics/RESULTS.md`, live UniProt):
- PTHR12705:SF0 for both donkey and human ORC5 (the family has only one subfamily).
- 417/435 identical to human O43913, 100% coverage; Walker A GHTASGKT, DKAE Walker B and
  DNA-proximal H398 all conserved; human-type C-terminus RTVNFDIIKYLYDFL.
- The sibling gene-model comparison (`genes/EQUAS/ORC5/ORC5-bioinformatics/RESULTS-rereview.md`)
  shows this is the only 435-aa donkey product with the human-type C-terminus.

Evidence (all human; nothing experimental in donkey):
- ORC5 in ORC1/4/5 motor module; ATP bound at the ORC5 Walker A/B site
  [PMID:28112645 "The third nucleotide binds to Walker-A and -B motifs on ORC5 (Figure 3c)"].
- ORC5 Walker B D125 mutation barely affects ATPase, so the ORC5 site is mainly non-catalytic
  [PMID:28112645 "both are only slightly reduced for ATPase activity compared with wild-type activity"].
- ATP binding by ORC5 needed for assembly [PMID:17716973 "Mutations in the ATP-binding sites of Orc4 or Orc5 impair complex assembly"].
- ORC5 hairpin H398 near DNA [PMID:32808929 "H398 in close proximity to DNA"].
- OBI1 ubiquitylates chromatin-bound ORC5; required for origin firing [PMID:31160578].

Decisions: GO:0000808 -> MODIFY to GO:0005664; GO:0006260 -> MODIFY to GO:0006270;
GO:0003688, GO:0005634, GO:0005664, GO:0006270 ACCEPT; NEW GO:0005524 ATP binding (intrinsic
to ORC5, conserved motifs). Origin binding is recorded as contributes_to in core_functions since it
is a complex-level activity. No ATPase/hydrolase term proposed (ORC5 site is weakly catalytic at best).
