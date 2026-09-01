# arl5a (F6WPT1) notes

## Re-review 2026-08-29

Re-checked the completed review against the GOA tsv, UniProt entry, and the
falcon deep-research file.

- All 9 GOA rows have matching `existing_annotations` entries (term id +
  evidence code + reference); no PMIDs are cited in GOA (all IBA/IEA), so no
  publication caching issues arise.
- All actions retained: the six IBA annotations are phylogenetically sound and
  well supported by mammalian ARL5A/ARL5B experimental literature summarized in
  the deep research (GARP recruitment, ARFRP1-SYS1-dependent TGN localization,
  ARMH3-PI4KB axis, Ragulator interaction). GO:0005737 cytoplasm remains
  KEEP_AS_NON_CORE (real but uninformative for a TGN-acting GTPase); broad BP
  terms (GO:0016192, GO:0006886) remain ACCEPT since the IBA level is
  defensible and the specific retrograde-trafficking biology is captured in
  `core_functions` and annotation summaries.
- Added `supported_by` evidence citing
  file:XENTR/F6WPT1/F6WPT1-deep-research-falcon.md (verbatim quotes) to all 9
  annotations, plus a uniprot.txt quote for GTP binding; added both files to
  the top-level references with findings. This resolves the validation warning
  that no annotations referenced the available deep-research file.
- Trimmed curation-flavored wording ("functional annotation rests on...",
  "annotation is based on...") from `description` and `core_functions` in
  favor of biological phrasing (function inferred from orthology).
- `just validate XENTR F6WPT1` passes with no warnings.

## Family/PTN curation pass 2026-08-31

Second IBA pass, this time using the FamilyReview framework: authored
`interpro/panther/PTHR11711/PTHR11711-review.yaml` and added structured
`review.propagation_review` blocks to the six IBA rows plus the InterPro
GTPase-activity IEA row. No review action changed — the family-level inspection
confirmed each existing judgement rather than overturning any.

**Subfamily placement (the thing that was missing before).** UniProt's PANTHER
cross-reference for F6WPT1 gives only the family (`PTHR11711`) with no `:SF` line, so
the subfamily was read from the PANTHER 19 geneinfo service: **F6WPT1 is
PTHR11711:SF147, "ADP-RIBOSYLATION FACTOR-LIKE PROTEIN 5A"** — the same subfamily as
human ARL5A (Q9Y689). Human ARL5B is SF146 and the invertebrate ARL5s (Drosophila
Arl5 Q9VSG8, C. elegans arl-5 P34212) are SF31. Every label was checked verbatim
against `interpro/panther/panther.obo`.

**Which node backs which IBA** (from `PTHR11711-paint.tsv`, dates are the PAINT
snapshot column):

| Term | Node | Snapshot | Assessment |
|---|---|---|---|
| GO:0005802 trans-Golgi network | PTN000195484 | 20171006 | SOUND |
| GO:1903292 protein localization to Golgi membrane | PTN000195484 | 20171006 | SOUND |
| GO:0005525 GTP binding | PTN000917851 | 20230110 | SOUND |
| GO:0005737 cytoplasm | PTN000917851 | 20260828 | SOUND |
| GO:0016192 vesicle-mediated transport | PTN000918181 | 20260828 | SOUND |
| GO:0006886 intracellular protein transport | PTN000918181 | 20250902 | SOUND |

The useful finding is that the two TGN-related terms sit on a **different, shallower
node** than the generic ones. PTN000195484 is the ARL5-clade node — its seeds are
Drosophila Arl5 plus human ARL5A and ARL5B, i.e. the ARL5 orthologs and nothing else —
while the family's other compartment assertions live at separate nodes (plasma membrane
at PTN000918064 and PTN002619726, Golgi apparatus at PTN000195580, lysosomal membrane
at PTN000918220, axoneme at PTN000196179). So the TGN annotation on this gene is not
loose family-level propagation; it is a clade-specific assertion and this gene is inside
the clade. That is recorded family-side as `GO:0005802` scoped `SUBFAMILY_ONLY` to
SF31/SF146/SF147.

Conversely, GO:0006886's node (PTN000918181) is seeded partly by **mouse Arl6/BBS3**
(MGI:1927136, verified at MGI), the ciliary BBSome GTPase — which is exactly why PAINT
asserted the generic parent term there rather than anything route-specific. That seed is
marked `SUPPORTS_SOURCE_BUT_NOT_TARGET`: its evidence is real but ciliary, and nothing
narrower should be read across from it.

**Seed identities were resolved, not assumed:** FB:FBgn0035866 = Drosophila Arl5
(Q9VSG8); SGD:S000000368 = yeast ARL1; SGD:S000005620 = yeast ARF3; WB:WBGene00000182 =
C. elegans arf-1; FB:FBgn0010348 = Drosophila Arf1; FB:FBgn0000115 = Drosophila Arl1;
MGI:MGI:1927136 = mouse Arl6. Seeds that could not be confirmed (e.g. UniProtKB:P36406)
were left out of the declared subsets rather than given a guessed label.

**Residue site.** Created `PANTHER:PTHR11711#g_domain` anchored on human ARL5A (Q9Y689,
sequence version 1), covering seven positions that all fall inside that record's own
curated GTP BINDING features: K29 and T30 (G1/P-loop), D66, G69 and Q70 (G3 and switch
II), K126 and D128 (G4/NKxD). Verified directly against the sequences — ARL5A, ARL5B and
F6WPT1 are all 179 aa with G1 = `GLDNAGKT` at 23-30, G3 = `WDIGG` at 65-69 and G4 =
`NKQD` at 125-128, while ARF1 runs one residue ahead (`GLDAAGKT` at 24-31), which is why
its positive control cites position 30.

F6WPT1 **retains all of them**, so four `RETAINED` residue claims were recorded (K29 and
D128 on the GTP binding row; Q70 and D66 on the GTPase activity row). This is the
opposite of the usual pseudo-enzyme use of the field: the site is recorded so that any
future claim that this protein lost its nucleotide machinery is contradicted by data.
Note Q70 is the position of the classic constitutively active Q70L allele. Site strength
is `CONTRIBUTES`, not `REQUIRED`, deliberately: Arf-family intrinsic hydrolysis is slow
and completed by an ArfGAP arginine finger in trans, so the G domain alone does not
determine turnover rate, and `REQUIRED` would license a validator to contradict gene
reviews on a basis the biology does not support.

**Deliberately not asserted:** no `clade_node_id` on any subfamily (PTN000195484 sits
above SF31/SF146/SF147 together rather than at the root of any one of them); no negative
control for the g_domain site (no PTHR11711 member with a degenerate nucleotide site was
found); and family-level scope left `UNRESOLVED` for GO:1903292, GO:0016192 and
GO:0006886, because those terms are true of every branch inspected but this review looked
at 5 of 77 subfamilies and will not convert that into a family-wide grant.

**Validation.** `just validate XENTR F6WPT1` passes; gene residue claims 16 pass / 0 fail;
family review passes schema, GO term/label, residue-site (32 pass / 0 fail) and
family-gene cross-check (0 conflicts). Two expected UNRESOLVED classes remain and are
documented in the family review's notes: none of the cited proteins are in
`panther-members.tsv` yet (`just refresh-panther-members` deliberately not run — shared
file), and the cross-check cannot place F6WPT1 inside the `SUBFAMILY_ONLY` set for
GO:0005802 because its UniProt record carries no `:SF` cross-reference.
