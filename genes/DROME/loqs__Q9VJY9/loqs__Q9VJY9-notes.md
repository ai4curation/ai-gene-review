# loqs (Q9VJY9, canonical Swiss-Prot entry) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: new review of the canonical Swiss-Prot accession Q9VJY9 (LOQS_DROME; isoform PB
displayed, PA/PC/PD named isoforms), placed in `genes/DROME/loqs__Q9VJY9/` because
`genes/DROME/loqs/` is keyed to the TrEMBL isoform-F accession X2J5X6. No ProtNLM2 file or
prediction-evidence folder was opened or used.

### Setup and deep research

- `just fetch-gene DROME Q9VJY9 --alias loqs__Q9VJY9` produced the UniProt, GOA (44 rows) and
  stub files. `just fetch-gene-pmids` cached all 17 GOA PMIDs. Additional primary papers were
  cached with `just fetch-pmid`: PMID:21245036, PMID:28874570, PMID:36182693, PMID:29550490
  (PMID:27184838 failed to fetch).
- `just deep-research-falcon DROME Q9VJY9 --alias loqs__Q9VJY9 --fallback perplexity-lite`
  FAILED: falcon "Exception: Failed to authenticate"; perplexity-lite fallback returned HTTP 401
  "insufficient_quota". No deep-research file exists in this folder. The review is built from
  the cached primary literature and the curated Swiss-Prot entry.

### Evolutionary grounding

- PANTHER: Q9VJY9 is in PTHR46205:SF3 ("LOQUACIOUS, ISOFORM B"), per the UniProt DR line. In the
  same family, human TARBP2 is SF1 and PRKRA is SF2 (`interpro/panther/PTHR46205/PTHR46205-entries.csv`).
  Fly r2d2 and blanks fall in other subfamilies. SF1/SF2 mammalian specifics are therefore not
  transferred: the DICER1/TARBP2/AGO2 RLC composition, PKR activation by PRKRA and
  nuclear/transcriptional roles.
- PAINT: all IBA rows come from node PANTHER:PTN005287422. Its WITH/FROM list spans DIP1
  (FBgn0024807), r2d2 (FBgn0031951), blanks (FBgn0035608), loqs itself (FBgn0032515),
  TARBP2/Tarbp2 and PRKRA, so the node sits at or near the family root. Loqs appears in its own
  WITH/FROM for cytoplasm, RLC, siRNA processing, siRNA binding and regulation of regulatory
  ncRNA processing. That is expected and is not circular: it marks fly experimental grounding.
  Loqs is not among the donors for nucleus or RISC complex. Those two IBA terms are where the
  loqs-specific data conflict with the family-level generalisation:
  - Nucleus: all experimental localisation of Loqs is cytoplasmic (PMID:15918769 IF). The nuclear
    donors are blanks, DIP1 and PRKRA, which are lineage-specific. MARK_AS_OVER_ANNOTATED.
  - RISC complex: Loqs is in the Dcr-1/Loqs/AGO1 miRLC but is absent from the AGO1-GW182 miRISC
    (PMID:19451544), and loqs-null flies assemble miRISC (PMID:17928574). MARK_AS_OVER_ANNOTATED.

### Biology summary, with isoform resolution (what is experimental in Drosophila)

- Loqs-PB (Q9VJY9-1, r3d1-L) has three DRBMs. It binds Dcr-1 through DRBM3 and binds pre-miRNA
  through DRBM2 [PMID:17666393 "Loqs-PB uses the second dsRNA-binding domain to bind pre-miRNA
  and the third dsRNA-binding domain to interact with Dcr-1."]. It raises Dcr-1 affinity for
  pre-miRNA and stimulates miRNA production in vitro [PMID:15985611 "recombinant R3D1-L enhances
  miRNA production by Dicer-1 in vitro"]. It forms a 1:1 complex with Dcr-1 and shifts the
  Dcr-1 cleavage site of pre-miR-307a (PMID:23063653). Cryo-EM shows the Dcr-1 and Loqs-PB dsRBDs
  forming a belt that positions the scissile bonds (PMID:36182693). Loqs-PB is required for GSC
  maintenance and female fertility, and the knockout is rescued by PB but not PA (PMID:17320391,
  PMID:23063653). It is part of the miRLC with Dcr-1 and AGO1 (PMID:19451544), but miRISC
  assembly does not require Loqs (PMID:17928574), and PB is not needed for Ago1 loading
  (PMID:20037596).
- Loqs-PA (Q9VJY9-2) binds Dcr-1 and supports viability (PMID:23063653) but does not rescue the
  GSC defect (PMID:17320391).
- Loqs-PD (Q9VJY9-4) arises by alternative polyadenylation (PMID:19644447), lacks DRBM3 and has a
  unique C-terminus. That C-terminus binds the Dcr-2 helicase domain (PMID:21245036,
  PMID:28874570). PD stimulates Dcr-2 processing of endo- and exo-siRNA precursors
  (PMID:19635780, PMID:19644447, PMID:23063653, PMID:28874570), lowers the KM of Dcr-2 for long
  dsRNA (PMID:21419681) and relieves phosphate inhibition (PMID:29550490). Its two DRBMs bind
  siRNA duplexes, and in S2 cells it forms an alternative RLC with Dcr-2 that is needed for
  endo-siRNA strand choice (PMID:29040648).

### Decisions

- Because Q9VJY9 is the gene-level canonical accession, siRNA-pathway rows (PD-mediated) are
  ACCEPTED here. This differs from the X2J5X6 (PF, PB-like) review, where they were UNDECIDED.
  The isoform attribution is recorded in `functional_isoforms`.
- GO:0005515 protein binding (four IPI rows, Dcr-1): MODIFY to GO:0170054 ribonuclease activator
  activity. Each paper shows that Loqs-PB binding stimulates Dcr-1 miRNA production.
- GO:1905172 RISC complex binding (IPI with Dcr-1, PMID:23063653): the partner is Dcr-1, which on
  its own is not a RISC. The paper measures the Loqs-PB:Dcr-1 heterodimer and shows that PB
  changes the Dcr-1 cleavage site. MODIFY to GO:0170054.
- GO:0003723 RNA binding → MODIFY to GO:0003725. GO:0010468 → MODIFY to GO:0031054 + GO:0030422.
  GO:0010586 → MODIFY to GO:0031054.
- Developmental IMPs (CNS development, GSC maintenance, GSC asymmetric division, oogenesis):
  KEEP_AS_NON_CORE as downstream miRNA-dependent requirements. Dosage compensation (IGI,
  sensitized roX1 roX2 viability): MARK_AS_OVER_ANNOTATED, a necessity result.
- Regulation of regulatory ncRNA processing (IBA, IDA): KEEP_AS_NON_CORE. RISC complex assembly
  (IMP, PD alternative RLC): KEEP_AS_NON_CORE, since that RLC is a minor route in flies.
- No NEW terms proposed. The ribonuclease-activator function is covered as the MODIFY replacement.

### Follow-ups (curation, not knowledge gaps)

- `interpro/panther/PTHR46205/PTHR46205-review.yaml` lists only X2J5X6 as the SF3 representative.
  Q9VJY9 (canonical, Swiss-Prot) would be a better representative. This was not edited here,
  because the folder is outside this gene's scope.

### Validation

- `just validate DROME loqs__Q9VJY9` passes with no warnings. Propagation_review blocks were added
  to the two over-annotated IBA rows (nucleus, RISC complex). RISC complex assembly was left out
  of core_functions (`directly_involved_in`), because the row is KEEP_AS_NON_CORE.
- History record: `history/genes/DROME/loqs__Q9VJY9/2026-10-21T082044Z-claude-code-7cd789.yaml`.
