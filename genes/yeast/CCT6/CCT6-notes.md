# CCT6 notes

## 2026-10-01 current GOA and IBA re-review

Forced a current GOA/UniProt refresh with `just fetch-gene yeast CCT6 --force`.
QuickGO now returns 12 rows. The live rows keep the two sound PTHR11353 IBA
assertions, add the InterPro2GO `GO:0005524` ATP-binding row, and add a
ComplexPortal `GO:0005832` row against the yeast CCT crystal structure
(PMID:21701561).

The stale rows from the older snapshot are retained as `retired: true` so source
preservation remains explicit: obsolete `GO:0051082` by IBA, IEA and IDA;
the retired generic `GO:0000166` keyword row; the retired GO_REF:0000120
ATP-binding row; and three retired high-throughput `GO:0005515` IPI rows. The
live `GO:0005524` row is accepted, mirroring the other current InterPro ATPase
rows, while the old `GO:0000166` row is narrowed to ATP binding plus ATP
hydrolysis.

The core GO representation is the TRiC/CCT chaperonin role. The unassembled-Cct6
suppression phenotypes remain contextual observations rather than separate core
annotations.

The current PTHR11353 PAINT extract retains `PTN004253040` for inherited
CCT/TRiC protein-folding biology and `PTN000143755` for zeta-subunit membership
in the chaperonin-containing T-complex. It no longer carries the obsolete
`GO:0051082` molecular-function assertion, so the old unfolded-protein-binding
IBA is a historical stale-source row rather than a current IBA to dispute.

Cached PMID checks read:

- PMID:16762366: abstract establishes purified yeast CCT as an essential
  ATP-dependent protein-folding machine required for actin and tubulin folding.
- PMID:21701561: abstract establishes the 3.8 A yeast CCT-actin crystal
  structure and the asymmetric CCT subunit organization.
- PMID:15704212: abstract establishes the two-ring, eight-subunit yeast CCT
  architecture and CCT6 overexpression biology for the existing contextual
  question.
- PMID:19536198 and PMID:37968396: full text available; both are
  high-throughput interactome/AP-MS resources that support CCT/TRiC connectivity
  but not a precise replacement for generic protein binding.

The default `deep-research-falcon` command failed because no Falcon/OpenAI/Asta/
Perplexity API key was available. The cached May 2026 Falcon report was already
present and was reviewed.

Manual literature search for CCT6, Cct6 and YDR188W in yeast through 2026-10-01
found one newer direct yeast-TRiC structural paper, PMID:40070846, which resolves
ADP-state cryo-EM intermediates of yeast TRiC and places CCT6 in the outward
tilting wave after CCT3 initiates ring opening. This supports the structural
subunit narrative but does not require a new GO term beyond the existing ATP
hydrolysis, ATP-dependent chaperone contribution, protein-folding, and CCT-complex
membership terms.
