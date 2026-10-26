# FAS (CD95/APO-1) Notes - ISOFORMS Project

## Key Isoform Biology

FAS is a classic example of **antagonistic membrane vs soluble isoforms**.

### Isoforms (7 named)

| Isoform | UniProt ID | Synonym | Key Feature | Function |
|---------|------------|---------|-------------|----------|
| Isoform 1 | P25445-1 | - | Full-length, membrane-bound | **INDUCES APOPTOSIS** |
| Isoform 2 | P25445-2 | del2, D | Lacks exons | Soluble, blocks apoptosis |
| Isoform 3 | P25445-3 | del3, E | Lacks exons | Soluble, blocks apoptosis |
| Isoform 4 | P25445-4 | B | - | Soluble, blocks apoptosis |
| Isoform 5 | P25445-5 | C | - | Soluble, blocks apoptosis |
| **Isoform 6** | P25445-6 | TMdel, A | **Lacks TM domain** | Soluble, **BLOCKS APOPTOSIS** |
| Isoform 7 | P25445-7 | FasExo8Del | - | Unknown |

### Critical Antagonism: Membrane vs Soluble

**Membrane-bound FAS (Isoform 1)**:
- Contains transmembrane domain
- Forms DISC (Death-Inducing Signaling Complex)
- Recruits FADD and CASP8
- **TRIGGERS APOPTOSIS**

**Soluble FAS (Isoforms 2-6)**:
UniProt states:
> "The secreted isoforms 2 to 6 block apoptosis (in vitro)"

Mechanism: Soluble FAS acts as a **decoy receptor**, binding FasL without triggering apoptosis.

### Tissue-Specific Expression (UniProt)

> "Isoform 1 and isoform 6 are expressed at equal levels in resting peripheral blood mononuclear cells. After activation there is an increase in isoform 1 and decrease in the levels of isoform 6."

This suggests splicing regulation shifts towards the pro-apoptotic membrane form upon immune activation.

## GOA Annotation Status

- **96 total annotations**
- **NO isoform-specific annotations** (no P25445-X identifiers)
- All apoptosis annotations likely refer to membrane-bound isoform 1

## Expected Annotation Issues

1. **"Positive regulation of apoptotic process"** - TRUE for isoform 1, FALSE for isoforms 2-6
2. **"Negative regulation of apoptotic process"** - should be annotated for soluble isoforms!
3. **Death domain** - present in all, but only functional in membrane form

## Key References

- PMID:7533181, PMID:9184224 - Soluble FAS blocks apoptosis
- PMID:7575433 - Isoform expression patterns

## 2026-09-30 APOPTOSIS generic-binding cleanup

`just fetch-gene human FAS` appended 17 partner-specific `GO:0005515` rows
that were split out from IntAct/UniProt imports already represented by older
generic rows:

- Tightened canonical DISC-context rows with CASP8 or FADD support
  (PMIDs 11717445, 16498403, 17159907, 21382479, 21625644) to FAS
  `GO:0005031` receptor activity, matching the existing core function.
- Removed the NAS `cytosol` row sourced to PMID:7533181 because the paper
  supports secreted soluble FAS splice isoforms rather than cytosolic FAS.
- Left abstract-only rows `UNDECIDED` where the cached abstract did not verify
  the exact partner imported by IntAct: the TNFR1-specific PMID:12887920 row,
  the FADD/CASP8 rows from the CD95/Yes/PI3K glioblastoma paper
  (PMID:18328427), PMLRARalpha rows whose partners were not evident in
  PMID:21803845.
- Removed generic `protein binding` rows for non-core inhibitory cap proteins
  from PMID:18846110, the direct PMLRARalpha inhibitory interaction from
  PMID:21803845, the FADD/DAXX rows from the proximity-ligation screen
  (PMID:25241761), and the BioPlex AP-MS FAS-CASP8 row from PMID:33961781
  because none supports a more informative FAS-side molecular function.


## Direct-source reassessment (2026-10-26)

The current direct-source reassessment covers all42 present PMID groups plus the historical PMID:11717445 FAS–FADD/caspase8 contexts. Those historical positive associations remain valid records despite their absence from current imports. The source guide and exact partner table document operative evidence, assay boundaries and inaccessible contexts. Supported generic protein interactions are retained as non-core under the standing ClinGen project instruction. No molecular function is inferred merely from a partner name, and DISC cellular components are not substituted for molecular-function binding annotations.

FAS activity is refined to death receptor activity rather than literal TNF cytokine receptor activity. Original receptor-complex experiments support the CD95-specific DISC, and the relevant broad signaling assertion is refined to FAS signaling. Inaccessible exact SRC/FADD/caspase8 assays, source-specific self-association, exosome target identification, mechanical-stimulus support and soluble-paper cytosol/receptor contexts remain undecided. Earlier assertions of absence or generic-binding exclusion in these notes are historical reasoning superseded by the explicit current reviews.

All113 inherited annotation source objects,78 quotation paths and reference associations, seven products, inherited core/description/status and unowned reviews are preserved in this direct lane. The inherited all-soluble-products death-domain claims require a separate correction: current UniProt isoform6 retains the death domain, while isoform7 retains the membrane segment but lacks the death domain. Other soluble truncations need their own ligand-binding evidence. Sequence topology and predicted consequences must not be represented as measured isoform function. No new quotation, guessed mature product, natural isoform assignment or NEW annotation is proposed here.


# FAS database review — 2026-10-26

This is an appendable database-lane note, not a replacement for historical notes. Earlier blanket claims that all soluble products lack the intracellular/death domain or that only isoform 1 contains a membrane anchor are superseded by the accepted official sequence reconstruction. Existing product objects are unchanged here; ROOT owns their reconciliation.

Manual scope: 36 inherited database rows (32 current plus four historical), one separate fresh current context 62, and 20 complete database-reference successor objects. Current actions: 27 ACCEPT, four KEEP_AS_NON_CORE, two MODIFY. Historical actions: three ACCEPT and calmodulin binding KEEP_AS_NON_CORE. No REMOVE, authored NEW, added quote, or source-field mutation. All 77 inherited direct rows remain identical.

Actual phylogeny, IBD and donor assays were considered, including legitimate human self-WITH. The source-scope problem for GO:0005031 is literal TNF cytokine specificity, not orthology. Human CD95 stimulation and FAS/FADD assembly support death receptor activity; GO:0036337 captures the receptor's pathway. The retained provider and superfamily quotations remain historical context and are not independent evidence of TNF cytokine binding.

The official GO_REF:0000043 method restriction to viruses provides a genuine lifecycle consideration for historical human old11. Fresh62 replaces the provenance combination of old14 at the same apoptotic-process assertion. In contrast, old17 and old20 still have matching current ARBA rules. `lifecycle-proposal.json` offers explicit alternatives without automatically retiring any source to satisfy validation. Current absence does not mean the biology is false. Old27/96 are direct-lane historical sources and were not altered.

Source acquisition reused accepted caches byte-for-byte. Ten missing donor/corroboration PMIDs were genuinely fetched after an exact-head/base open-PR ownership inventory. The selected PTHR46874 entries/metadata remain the accepted main bytes; the timestamp-only fresh metadata stays private. No source is installed canonically by this packet.

The actual murine soluble FasB original was finally recovered through the author's uploaded article text after preserved PMC/PDF access failures. Read scope is explicit, not retrospectively labeled complete. The article's positive conditioned-medium effect is retained without claiming direct ligand sequestration or equivalence to each human natural product. Likewise the necroptosis donor paper's human FAS construct in mouse L929 cells is stated accurately.

Schema and exact reference validation are checked in a new isolated frozen runtime. The legacy-only candidate intentionally retains inherited source history and leaves fresh source adoption to integration. Its strict GOA/focused coverage failures therefore expose the known four current additions and six historical absences; the separate 111-context current projection passes strict GOA. No historical object or source code was rewritten to hide that difference.


## ROOT integration preparation (2026-10-26)

The sections above preserve the earlier source-specific review record. The proposed integration combines all 113 inherited source contexts and appends the four exact fresh contexts in fresh order. Six historical contexts retain their reviewed biology and evidence, with retirement scoped only to absence from the pinned current GOA snapshot; the marker is not a claim of biological invalidity or official withdrawal. The ROOT description, product, functional-class and core successors supersede the earlier pending-integration statements. All seven product identities, names and sequence notes and all 78 inherited supporting-text anchors are preserved. No new supporting text is introduced.

The shared PMID:25301068 assessment preserves both complete source-review notes. Normal-source selection retains 75 exact files; all 64 shared-path versions have identical hashes and modes. This preparation does not claim a completed whole-gene review. The candidate is provisional DRAFT until ROOT runs integrated validation and computed-status checks.

## 2026-10-26 — Product synthesis and preserved source boundary

The seven official product sequences have lengths 335, 103, 86, 149, 132, 314 and 220 residues. Isoform 6 removes the membrane-anchor region while retaining the death-domain sequence; isoform 7 retains the membrane segment and loses the death domain. Soluble-product antagonism is documented in expression assays without assigning a universal FASLG-sequestration mechanism. The FasExo8Del evidence is from lymphoma cells. Primary evidence and access limits are summarized in the source guide.

The existing UniProt cache remains byte-identical. Its sequence, product identities and variant edits agree with the fresh official record used for the architecture check; that newer record remains private evidence. The fresh GOA snapshot is adopted explicitly. Six historical contexts retain their source data, positive or uncertain scientific reviews and inherited quotations; their retired markers concern this snapshot’s active set, not official withdrawal or biological falsity.

Final synthesis also refines the broad InterPro signal-transduction assertion (historical index 16, current index 67) to Fas signaling, consistently with the literature-source refinement. The two fresh PMID:25301068 localization assertions carry reference-only support links; no quotation is added.

## 2026-10-26 — Canonical validation

All seven canonical checks pass: status update, standard validation, strict GOA matching, ontology terms, component checks, computed status and rendering of 236 narratives. DRAFT status retains 38 accounted advisories: 37 supported generic-binding cases under project policy and one intentional receptor-source MODIFY/UNDECIDED distinction. The existing UniProt cache, 75 normal dependencies, prior history and inherited HTML remain exact. Thirteen normal dependencies are genuine additions; the fresh GOA snapshot is adopted explicitly. Both evidence tables and a source guide document assay scope. Rendered HTML was checked privately. Unrelated workspace edits remain unchanged.

## 2026-10-26 — Authored record format

The interaction and database-decision tables are now YAML, following the repository rule for authored structured records. All 40 interaction records and 36 database records retain their field values and order. The source guide points to the YAML files; earlier notes describe the superseded TSV representation. Annotation decisions, source fields, normal caches, all 78 inherited quotations and product/core summaries are unchanged. The seven canonical checks and 236-narrative render remain applicable to the byte-identical main review.
