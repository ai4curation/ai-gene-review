# VMA22 annotation re-review notes

## Scope and reconciliation

Dedicated re-review performed on 2026-08-28 against `VMA22-goa.tsv`, UniProt
P38784, the Falcon deep-research report, all locally cached cited publications,
and the available local PAINT snapshot. The GOA contains nine physical rows and
nine unique qualifier-aware signatures; all nine are represented one-for-one in
the review. All are positive annotations, with no NOT annotations or isoform-
specific rows. The review additionally proposes one NEW ER-membrane annotation.

The exact IBA WITH/FROM traces are:

- GO:0051082 `enables`: `PANTHER:PTN001592797|SGD:S000001102`
- GO:1990871 `part_of`: `PANTHER:PTN001278552|SGD:S000001102`

Neither PTN is recoverable in the current local PAINT snapshot, and the UniProt
PANTHER family PTHR31996 has no local PAINT table. Both PTNs are therefore
recorded with bare PTN labels and `SOURCE_STALE_OR_MISSING`; the target's own
SGD identifier in WITH/FROM is expected experimental grounding behind the IBD,
not a separate propagation source or circularity.

## Biological synthesis

Vma22 is a dedicated ER-associated V-ATPase assembly factor, not a mature
V-ATPase subunit. Deletion prevents enzyme assembly: [PMID:7673216, "vma22 delta
cells contain no V-ATPase activity due to a failure to assemble the enzyme
complex; V1 subunits accumulate in the cytosol, and the V0 100-kDa subunit is
rapidly degraded."] Vma22 is ER-membrane-associated despite being hydrophilic:
[PMID:7673216, "Vma22p is a 21-kDa hydrophilic protein that is not a subunit of
the V-ATPase but rather is associated with ER membranes."]

Full-text biochemical evidence establishes the stable named complex and its
direct assembly-substrate interaction: [PMID:9660861, "Vma12p and Vma22p were
found to interact directly as determined by chemical cross-linking analysis and
cofractionation under conditions of gentle detergent solubilization."] The
authors further conclude that interaction with the complex stabilizes Vph1 in
the ER so it can assemble into V0.

## GO:0051082 and molecular-function scope

All three `unfolded protein binding` rows are marked over-annotated. GO:0051082
is obsolete, but no current generic holdase or protein-folding-chaperone term is
an evidence-matched replacement. The authors' proposed model, rather than a
direct folding-state assay, places a folded assembly intermediate at the
interaction step: [PMID:9660861, "The first step in the assembly pathway would
involve the association of the fully translocated and folded Vph1p with the
Vma12p/Vma22p assembly complex in the ER membrane."] The experiments establish
stabilization in the assembly pathway [PMID:9660861, "We conclude that the
interaction of Vph1p with the assembly complex stabilizes this Vo subunit in the
ER allowing it to assemble into the Vo subcomplex."], while the authors
explicitly distinguish these proteins from general chaperones: [PMID:9660861,
"Vma12p, Vma21p, and Vma22p represent a class of ER resident proteins dedicated
to the assembly of a specific enzyme complex, the V-ATPase."] Accordingly, the
review does not replace GO:0051082 with GO:0044183 protein folding chaperone:
stabilization is demonstrated, but assistance of client protein folding is not.
It instead proposes a dedicated V-ATPase V0-sector assembly-factor activity term.

For the IBA GO:0051082 row, the PTN source cannot be recovered. VMA22's own
experimental mutant and assembly evidence in the descendant evidence set does
not establish unfolded-protein binding; this reflects over-scoping rather than a
wrong experiment. This is a term-scoping/role-conflation problem, not a claim
that target self-evidence is circular.

### 2026-09-29 IBA project alignment

This pass rechecked the two VMA22 IBA rows against the current IBA project
convention. Both rows still point to PTNs that are present in GOA WITH/FROM but
absent from a current local `PTHR31996` PAINT export, so the stale-PTN
classification remains the right level of certainty. Their `source_entities`
were tightened to the PAINT nodes only; the `SGD:S000001102` self-entry in
WITH/FROM marks target-descendant experimental support behind the PAINT placement
and is expected, but it is not the source entity to curate.

The newly cached Wang et al. 2023 cryo-EM study (PMID:36724250) directly
resolved yeast V0 assembly intermediates bound by Vma12p and Vma22p and supports
the dedicated V-ATPase assembly-factor mechanism. Its Vma22p-specific section
shows that Vma22p occupies the V0 subunit-d site otherwise used by V1 subunit D,
so Vma22p can both connect Vma12p to subunit d and prevent premature V1 binding
to the partially assembled V0 sector. The structure reinforces the core
V-ATPase assembly call and the proposed dedicated assembly-factor term, but it
does not rescue `GO:0051082 unfolded protein binding`; the remaining structural
question is what the 35-residue disordered loop C-terminal to Vma22p's folded
subunit-D-like core contributes.

## Localization and evidence limitations

The PMID:26928762 nucleus HDA row is UNDECIDED. The full cached article describes
the library and its manual localization calls without co-localization markers,
but the VMA22-specific supplementary row is absent from the cache. The method
used amino-terminal GFP tagging, a concrete caveat for a protein with alternative
initiation products [PMID:26928762, "To establish this strategy we constructed a
library containing ~1,800 strains where all proteins with known or predicted
localization to the yeast endomembrane system are tagged with an amino terminal
(N′) SWAT acceptor module. The used module also contains a constitutive promoter
and a GFP tag."]. It also states: [PMID:26928762, "Since no co-localization markers were used we only
assigned localizations that could be easily discriminated by eye: ER, nuclear
periphery, cytosol, cell periphery, vacuole lumen, vacuole membrane, mitochondria,
nucleus, bud/bud neck and punctate"]. Focused evidence strongly establishes the
ER as Vma22's functional location, but it cannot exclude a minor, conditional,
or tag-dependent nuclear signal. The experimental row is therefore not removed
without its gene-specific evidence.

PMID:7673216, PMID:8582630, and PMID:1628805 are abstract-only in the local cache.
Their directly visible claims are used conservatively. The vacuolar-acidification
IMP from PMID:1628805 is retained with curator deference because the abstract
establishes the Vph- mutant screen but does not expose the VMA22-specific assay.
PMID:9660861 and PMID:26928762 have cached full text, subject to the supplementary-
data limitation above.

## Final curation shape

The core function is V-ATPase V0-sector assembly in the ER as part of the
Vma12-Vma22 assembly complex, with vacuolar acidification as a valid downstream
process consequence. The NEW ER membrane annotation is supported by focused
biochemical evidence. The nine physical GOA rows have four ACCEPT decisions,
three MARK_AS_OVER_ANNOTATED decisions, one KEEP_AS_NON_CORE decision, and one
UNDECIDED decision; the review also contains one NEW annotation.

### 2026-10-01 live-GOA refresh

Refreshing current GOA changed the PAINT surface substantially. The older
GO_REF:0000033 transfers for `GO:0051082 unfolded protein binding` and
`GO:1990871 Vma12-Vma22 assembly complex` are no longer live, so those exact
source rows were retained as `retired: true` provenance rows. Current GOA now
has three `PANTHER:PTN001592797` IBA rows: `GO:0005783 endoplasmic reticulum`,
`GO:0007035 vacuolar acidification`, and `GO:0016471 vacuolar
proton-transporting V-type ATPase complex`. The first is consistent with
focused ER-association evidence, and the second is a real downstream phenotype
of failed V-ATPase assembly. The mature V-ATPase complex `part_of` row is a
role-confounded transfer because Vma22 is a transient ER Vma12-Vma22 assembly
factor rather than a subunit of the final proton pump.

The current local `PTHR31996` cache contains family metadata and entries for
yeast Vma22 and human CCDC115/VMA22, but no `PTHR31996-paint.tsv`, so the exact
current IBD placement could not be inspected locally. The GOA `WITH/FROM`
strings identify `PANTHER:PTN001592797` as the PTN source for all three live
IBA rows; the extant `UniProtKB:Q96NT0` and `SGD:S000001102` entries in
`WITH/FROM` are descendant evidence, not the curated source entity.

Current SGD also carries a `GO:0005515 protein binding` row from the 1995
Vma22-Vma12 evidence. The interaction is real, but the generic molecular
function should be removed because the precise physical biology is already
captured by the `GO:1990871 Vma12-Vma22 assembly complex` IPI row.

No newer primary yeast VMA22 paper was found that changes the core
assembly-factor interpretation. Chen et al. 2025 reported that `vma22`
deletion nearly depletes inorganic polyphosphate in a 55-strain screen
[PMID:40291979, "deletions of vtc1, kcs1, vma22, vma5, pho85, vtc4, vma2,
vma3, ecm14, and vph2 resulted in near-complete polyP depletion"], but Vma22's
effect on polyP is an indirect consequence of impaired vacuolar V-ATPase
assembly rather than evidence that Vma22 performs VTC-mediated polyphosphate
synthesis.

The refreshed review now has 14 total rows: nine current GOA rows, four
retired rows, and the existing proposed ER membrane annotation. The final action
counts are five ACCEPT, two KEEP_AS_NON_CORE, three MARK_AS_OVER_ANNOTATED, two
REMOVE, one UNDECIDED, and one NEW.
