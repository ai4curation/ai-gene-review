# VPS45 annotation re-review notes

## Scope and physical-row reconciliation

Dedicated re-review completed 2026-08-28 against `VPS45-goa.tsv`, UniProt
P38932, the Falcon deep-research report, all 17 cached PMID records, and the
available local PAINT data. GOA contains 40 physical rows. The review now has 40
one-for-one entries, including separate entries for distinct WITH/FROM partners
that had previously been collapsed:

- PMID:16429126 protein binding: Q03322 and Q08144
- PMID:18719252 protein binding: P32609 and Q08144
- PMID:37968396 protein binding: P32609, Q03322, and Q08144
- PMID:16769821 SNARE binding: SGD:S000005378 and SGD:S000005854

All rows are positive; there are no NOT or isoform-specific annotations.

## IBA provenance

The three IBA rows have two exact node traces:

- `GO:0016192 involved_in` — `PANTHER:PTN000187655` plus the full descendant
  source set recorded in GOA, including target `SGD:S000003063`.
- `GO:0006886 involved_in` — the same `PANTHER:PTN000187655`, with its GOA
  descendant source set including target `SGD:S000003063`.
- `GO:0000139 is_active_in` — `PANTHER:PTN000187915|MGI:MGI:891965|SGD:S000003063`.

UniProt assigns Vps45 to PANTHER family PTHR11679, official label `VESICLE
PROTEIN SORTING-ASSOCIATED`, and the family ontology contains a VPS45 subfamily
PTHR11679:SF3. Neither PTN is present in the current local PAINT snapshot, so the
node assertions cannot be inspected directly and are recorded as
`SOURCE_STALE_OR_MISSING`. This is a provenance limitation, not biological
evidence against the terms: direct yeast work independently establishes both
transport and Golgi-like membrane association. The target's own SGD source is
valid descendant evidence and is not circular.

## Core biology

Vps45 is a Sec1/Munc18-family regulator of SNARE-dependent Golgi/endosomal
traffic. Fractionation supports peripheral Golgi-like membrane association
[PMID:7720726, "Fractionation studies show that Vps45p is a peripheral membrane
protein"]. Functional inactivation accumulates post-Golgi vesicles and causes
CPY secretion, while another study directly concludes that Vps45 is required
for fusion of Golgi-derived vesicles with the prevacuolar compartment
[PMID:9650782, "Here we demonstrate that the Sec1p-like protein Vps45p is
required for the fusion of Golgi-derived vesicles with the prevacuolar
compartment"].

SNARE binding is the evidence-matched molecular function. Full-text work shows
two binding modes and direct binding to both Tlg2 and Snc2 [PMID:16769821, "Fig.
2 A demonstrates that His6-Vps45p interacts directly with the cytosolic domains
of both Tlg2p and the v-SNARE Snc2p (Snc2p-PrA)."] The L117R mutant abolishes
the Tlg2 N-terminal hydrophobic-pocket interaction, binding to assembled
Tlg2-containing complexes, and membrane association yet still rescues CPY
sorting, showing that this mode is dispensable for trafficking. A second,
N-terminus-independent mode is revealed by direct Snc2 binding and the
W244R-locked conformation; the authors propose that wild-type Vps45 samples this
conformation transiently. Vps45 also stabilizes Tlg2 and is needed for its
productive assembly with Tlg1 and Vti1 [PMID:11432826,
"However, the stabilized Tlg2p is non-functional and unable to bind its cognate
SNARE binding partners, Tlg1p and Vti1p, in the absence of Vps45p."]

The Cvt annotation is directly supported but pathway-specific: [PMID:10545112,
"Here we show that Tlg2p, a member of the syntaxin family of t-SNARE proteins,
and Vps45p, a Sec1p homologue, are required in the constitutive Cvt pathway, but
not in inducible macroautophagy."]

## Term-scope decisions

Both `GO:0031201 SNARE complex` rows are marked over-annotated. Vps45 binds
individual SNAREs and assembled SNARE complexes, but as an SM regulator it is
not one of the SNARE proteins forming the core four-helix bundle. `GO:0000149
SNARE binding` and `GO:0035543 positive regulation of SNARE complex assembly`
capture the evidence more precisely.

Both obsolete `GO:0051082 unfolded protein binding` rows are also marked
over-annotated. PMID:11432826 calls SM proteins chaperone-like for their cognate
t-SNAREs and shows stabilization/activation of Tlg2; it does not assay generic
unfolded clients. No replacement holdase/folding term was invented because
SNARE binding and SNARE-assembly regulation already express the demonstrated
activity.

All 12 generic protein-binding physical rows are retained one-for-one. The seven
rows whose WITH/FROM partner is the syntaxin SNARE Tlg1 or Tlg2 are MODIFY to
GO:0000149 SNARE binding; the other five remain over-annotated. Several are
informative interaction data, yet `GO:0005515` loses the partner and role
specificity. PMID:12553664 is especially limited: its
cached abstract is entirely about Ivy1, Ypt7, and Vps33, not Vps45; without full
text the row is not called wrong, but the reference is recorded as relevance
NONE/correctness UNVERIFIED.

The cytosol IDA from PMID:9624182 remains UNDECIDED. The cached abstract is
explicitly a Vps33 study and contains no Vps45 observation, while full text is
unavailable. Cytosolic Vps45 is independently biologically plausible and is
supported by UniProt through a different paper, so the row is neither rejected
nor claimed verified.

Vacuole inheritance, vacuole organization, and vacuolar acidification are kept
as non-core downstream phenotypes. For acidification, the source explicitly
reports normal V-ATPase activity despite defective acidification [PMID:7628704,
"Vacuoles from stt10 cells have a normal vacuolar H(+)-ATPase activity, but are
defective in vacuolar acidification."].

## Final action profile

The 40 physical rows have 20 ACCEPT, 9 MARK_AS_OVER_ANNOTATED, 7 MODIFY, 3
KEEP_AS_NON_CORE, and 1 UNDECIDED decisions. There are no PENDING or NEW rows.
