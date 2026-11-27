# pvdL (PA2424, Q9I157) — review notes

Tier-3 PseudoCAP review. `pvdL` is the last unreviewed member of the `GO:0003824` /
PMID:19854904 shared claim; `pvdJ` is merged and MODIFYs the term to `GO:1904091`. The
sibling NRPS `pvdD` is also merged and is used here as a second consistency reference.

## The gene

4342 residues — the largest protein in this batch by a wide margin — and a hybrid
non-ribosomal peptide synthetase. Its domain complement on the record:
`IPR001242 Condensation_dom`, three `NCBIfam TIGR01733` amino-acid adenylation domains,
`IPR000873 AMP-dep_synth/lig_dom`, `IPR020806 PKS_PP-bd` and `IPR009081 PP-bd_ACP` carrier
domains, `IPR006162 Ppantetheine_attach_site`, and — distinctively — `IPR040097 FAAL/FAAC`,
a fatty acyl-AMP ligase domain that the other pyoverdine NRPSs do not carry.

That extra domain matches what PMID:21892836 shows:

`[PMID:21892836 "We demonstrate herein that the initial module of the nonribosomal peptide synthetase PvdL adds a myristate moiety to the pyoverdine precursor."]`

So PvdL initiates pyoverdine assembly by loading a fatty acid onto the growing precursor,
and the acyl group is removed later by the periplasmic hydrolase PvdQ as one of the final
maturation steps. The paper calls PvdL a non-ribosomal peptide synthetase in as many words,
which is the direct support for the `GO:1904091` replacement below.

## Rows resolved in line with the merged siblings

`pvdJ` and `pvdD` set the pattern for this gene cluster, and `pvdL` follows it:

| term | pvdD / pvdJ | pvdL (here) |
|---|---|---|
| `GO:0003824` catalytic activity | MODIFY → `GO:1904091` (pvdJ) | MODIFY → `GO:1904091` |
| `GO:0002049` pyoverdine biosynthetic process | ACCEPT | ACCEPT |
| `GO:0031177` phosphopantetheine binding | ACCEPT | ACCEPT |
| `GO:0044550` secondary metabolite biosynthetic process | TOO_GENERAL | TOO_GENERAL |
| `GO:0043041` (obsolete) | MODIFY → `GO:0002049` | MODIFY → `GO:0002049` |

`GO:0003824 catalytic activity` is the root of the catalytic branch and says nothing about
what the enzyme does; `GO:1904091 non-ribosomal peptide synthetase activity` is the specific
term, and `pvdL` has this row's own evidence for it — two IDA rows and an IMP, and a paper
that names the protein an NRPS. For `GO:0044550`, checked in OLS: `GO:0002049` is a
descendant (via `GO:0019748 secondary metabolic process`), so the broad term is entailed by
the accepted specific one.

`GO:0043041` is obsolete. `pvdD` and `pvdJ` both MODIFY it to `GO:0002049` on the reasoning
that with the activation term retired the supported *process* is pyoverdine biosynthesis
while the activation step itself is captured by the NRPS *activity* in `core_functions`. The
replacement is a term `pvdL` already carries and accepts, which is what the MODIFY rule
prefers.

## Two rows specific to pvdL

Neither appears on `pvdD` or `pvdJ`; both come from the FAAL domain and both rest only on
ARBA association rules, which the project rules class as unvetted predictions.

**`GO:0008610 lipid biosynthetic process` → `MARK_AS_OVER_ANNOTATED`.** PvdL does handle a
fatty acyl group: its initial module activates myristate and transfers it to the pyoverdine
precursor. But it does not make a lipid. The myristate comes from the cell's existing pool,
goes onto a peptide siderophore, and is cut off again by PvdQ before the mature pyoverdine is
exported. The term is not simply false — a fatty-acyl-AMP ligase step is genuinely involved
— so it is marked over-annotated rather than removed, and the FAAL domain is the honest
reason the mapping exists. The ARBA rule presumably derives from mycobacterial FAALs, which
really do feed lipid biosynthesis.

**`GO:0071766 Actinobacterium-type cell wall biogenesis` → `REMOVE`.** *P. aeruginosa* is a
Pseudomonadota, not an Actinomycetota; it has no arabinogalactan-mycolate cell wall for this
process to occur in. The term is taxonomically inapplicable to the organism, so no evidence
about this protein could make it true. Almost certainly the same FAAL/FAAC signature at work:
mycobacterial FAAL enzymes do contribute to cell-envelope lipid assembly, and an association
rule keyed on that domain has carried an Actinomycetota-specific process into a
gamma-proteobacterium. Recorded as a `WRONG_TERM` defect against UniProt with
`cause: OVER_PROPAGATION`.

## On the catalytic-activity rows' evidence

Worth noting since this is a tier-3 review and the tier's concern is IMP-on-MF. Here the
molecular-function rows are **not** phenotype-only: `GO:0003824` carries two IDA rows
(PMID:12354233, PMID:21892836) alongside the IMP, and PMID:21892836's demonstration that the
initial module adds myristate is a direct biochemical result on PvdL itself. So the refinement
to `GO:1904091` has this gene's own direct evidence behind it, which is exactly what the
2026-11-14 ruling requires of a MODIFY.

The `GO:0002049` process rows are similarly strong — two IDA and two IMP from four separate
papers — and PvdL does part of the work of pyoverdine synthesis rather than merely being
required for it, so `involved_in` is right.

## The IMP reference is the wrong species

Found after the above was written, and it changes the reading of two rows. PMID:19854904 is
**not** a *P. aeruginosa* paper: it is Taguchi *et al.* 2010 on *Pseudomonas syringae* pv.
tabaci 6605, and the mutants it constructs are all in that organism —
`[PMID:19854904 "predicted pyoverdine synthesis-related genes, pvdJ, pvdL, and fpvA, were"]`
mutated there. A deletion phenotype in *P. syringae* cannot be IMP evidence for the PAO1
gene.

Two of pvdL's rows cite it: `GO:0002049` IMP and `GO:0003824` IMP. Both are **kept**, because
the claims are independently established by the two *P. aeruginosa* papers, and a true claim
should not be discarded over a coding error. What is faulted is the evidence code:
`WRONG_EVIDENCE_CODE`, IMP → ISS, `requested_change: CHECK`.

The merged `pvdJ` review reached exactly this conclusion on exactly this reference and filed
the same request — its explanation even names the Δ*pvdL* mutants. So this is a consistent
treatment of a shared claim rather than a new finding, and the defect is worded to ask that
both genes' rows be handled together. One defect is recorded, on the `GO:0002049` row, naming
both rows that cite the paper, so the upstream report carries a single coherent request per
gene instead of two.

`reference_review` for it is `relevance: LOW`, `correctness: MISCITED`, matching pvdJ's.

This is also why PMID:12686626, the other IMP, is left `UNVERIFIED` rather
than marked good: it *is* a *P. aeruginosa* pyoverdine paper, but its cached abstract does not
name pvdL, so unlike the *P. syringae* case there is nothing to fault and nothing to confirm.
