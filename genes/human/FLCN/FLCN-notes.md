# FLCN (human, Q8NFG4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: this review is the experimental reference for transfer to donkey FLCN (EQUAS A0A8C4MM62). Donkey and
human FLCN are in the same PANTHER subfamily, PTHR31441:SF2 (FOLLICULIN). Human FLCN is the main experimental donor
under TreeGrafter node PTN009120754. No ProtNLM2 files were opened.

### Deep research
`just deep-research-falcon human FLCN --fallback perplexity-lite` failed: falcon could not authenticate, and
perplexity returned HTTP 401 (insufficient_quota). No deep-research file exists. The review is built from the
cached publications (all GOA PMIDs plus the mouse donor papers behind the ISS rows, fetched with `just fetch-pmid`)
and the UniProt record.

### Evolutionary grounding
- UniProt places FLCN in PANTHER PTHR31441:SF2. The family file `interpro/panther/PTHR31441/PTHR31441-entries.csv`
  has one subfamily, SF2, which contains yeast LST7 (P53237), S. pombe bhd1 (O74769), bovine FLCN and Xenopus flcn.
- PAINT node PTN002833743 is deep: its donors include yeast LST7 and S. pombe Bhd1. Terms propagated from it are
  positive regulation of TORC1 signaling, the FNIP-folliculin RagC/D GAP complex, cytosol and nucleus. So the Rag GAP
  module is ancestral to opisthokonts.
- The transcription-repression and TGF-beta terms were propagated from vertebrate-level nodes (PTN001265854 and
  PTN001265856) seeded by MGI Flcn.
- On QuickGO, mouse Flcn (Q8QZS3) carries GO:0005096 by IBA with `contributes_to`, seeded from LST7. Human IDA rows use
  enables, which is appropriate because FLCN carries the catalytic Arg164 [PMID:31672913 "First, we identified Arg164
  of FLCN as a catalytically required arginine residue for GAP activity."].

### Experimentally established in human (direct)
- RagC/D GAP activity of FLCN-FNIP [PMID:24095279 "we identified the FLCN-FNIP complex as a potent GTPase activating
  protein (GAP) for RagC/D"]. This is supported by the R164A catalytic mutant (PMID:31672913, PMID:31704029) and by
  the GAP-competent structure (PMID:36103527).
- Substrate-specific TORC1 control of TFEB/TFE3, but not S6K/4E-BP1 [PMID:32612235 "Importantly, expression of
  active RagCS75L or RagDS77L mutants in FLCN KO cells rescued TFEB phosphorylation"].
- Lysosomal membrane localization in amino acid starvation and cytosol on refeeding (PMID:24081491, PMID:24095279,
  PMID:29848618, PMID:31672913).
- Secondary functions: perinuclear lysosome clustering via RILP-Rab34 (PMID:27113757); LDHA inhibition
  (PMID:34381247, one laboratory); a moderate effect on basal autophagy (PMID:25126726); localization at cilia,
  centrosomes and the mitotic spindle (PMID:23784378; PMID:27072130).

### Inferred / phenotype-only (mostly mouse)
QuickGO shows that the mouse source annotations for embryonic development, haemopoiesis, kidney proliferation,
ERK/AKT, TOR regulation and pro-B differentiation are IMP annotations with `acts_upstream_of_or_within`. The human ISS
rows restate them as `involved_in`. These rows are MARK_AS_OVER_ANNOTATED, as knockout phenotypes, not participation.

The adipose browning and thermogenesis terms are kept as non-core. They have a mechanism through FLCN's core axis
(PMID:27913603: FLCN-mTOR-TFE3-PGC-1beta), but the evidence is from mouse only.

The "negative regulation of TOR signaling" rows are marked as over-annotation. mTORC1 hyperactivation in FLCN-null
kidney depends on TFEB [PMID:32612235 "TFEB is constitutively nuclear and active in Flcn-KO kidneys and its depletion
rescues mTORC1 hyperactivation."].

The "regulation of Ras protein signal transduction" rows are MODIFY to GO:1904263. GO:0007265 is defined for the Ras
subfamily, and the Rags are not in it.

### Transfer guidance for orthologs (e.g. EQUAS/HORSE FLCN in SF2)
Safe to transfer within SF2: GO:0005096, GO:1990877, GO:1904263, GO:0005765, GO:0005829 and GO:0034198.
Do not transfer: the mouse knockout phenotype terms listed above; GO:0160193 (LDHA inhibition, one human study only).
