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
recorded with bare PTN labels and `SOURCE_STALE_OR_MISSING`. The target's own SGD
identifier in WITH/FROM is expected experimental grounding, not circularity.

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
an evidence-matched replacement. Crucially, the full text describes association
with a folded assembly intermediate: [PMID:9660861, "The first step in the
assembly pathway would involve the association of the fully translocated and
folded Vph1p with the Vma12p/Vma22p assembly complex in the ER membrane."] It
also distinguishes these proteins from general chaperones: [PMID:9660861,
"Vma12p, Vma21p, and Vma22p represent a class of ER resident proteins dedicated
to the assembly of a specific enzyme complex, the V-ATPase."] Accordingly, the
review does not replace GO:0051082 with a holdase/chaperone term and instead
proposes a dedicated V-ATPase V0-sector assembly-factor activity term.

For the IBA GO:0051082 row, the PTN source cannot be recovered. The VMA22 source
seed is classified `SOURCE_BAD` for this term because the experimental mutant
and assembly evidence does not establish unfolded-protein binding. This is a
term-scoping/role-conflation problem, not a claim that target self-evidence is
circular.

## Localization and evidence limitations

The PMID:26928762 nucleus HDA row is UNDECIDED. The full cached article describes
the library and its manual localization calls without co-localization markers,
but the VMA22-specific supplementary row is absent from the cache. The method
states: [PMID:26928762, "Since no co-localization markers were used we only
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
biochemical evidence. The nine physical GOA rows have five ACCEPT decisions,
three MARK_AS_OVER_ANNOTATED decisions, and one UNDECIDED decision; the review
also contains one NEW annotation.
