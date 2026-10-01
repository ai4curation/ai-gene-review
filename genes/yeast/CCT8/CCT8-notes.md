# CCT8 notes

## 2026-10-01 current GOA and IBA re-review

Forced a current GOA/UniProt refresh with `just fetch-gene yeast CCT8 --force`.
QuickGO now returns 14 rows. The live rows keep the two sound PTHR11353 IBA
assertions, add the InterPro2GO `GO:0005524` ATP-binding row, and add a
ComplexPortal `GO:0005832` row against the yeast CCT crystal structure
(PMID:21701561).

Nine stale rows from the older snapshot are retained as `retired: true` so
source preservation stays explicit: obsolete `GO:0051082` by IBA, IEA and IDA;
the retired generic `GO:0000166` keyword row; the retired GO_REF:0000120
ATP-binding row; and four generic `GO:0005515` IntAct interaction rows that are
no longer present in current GOA. The live `GO:0005524` row is accepted,
mirroring the other current InterPro ATPase rows, while the old `GO:0000166`
row is narrowed to ATP binding plus ATP hydrolysis.

The current PTHR11353 PAINT extract retains `PTN004253040` for inherited
CCT/TRiC protein-folding biology and `PTN000144200` for theta-subunit
membership in the chaperonin-containing T-complex. It no longer carries the
obsolete `GO:0051082` molecular-function assertion, so the old
unfolded-protein-binding IBA is a historical stale-source row rather than a
current IBA to dispute.

Cached PMID checks read:

- PMID:16762366: abstract establishes purified yeast CCT as an essential
  ATP-dependent protein-folding machine required for actin and tubulin folding.
- PMID:21701561: abstract establishes the yeast CCT-actin crystal structure and
  the asymmetric CCT subunit organization.
- PMID:15704212: abstract establishes the two-ring, eight-subunit yeast CCT
  architecture and supports the Cct8-Cct6 complex-membership row.
- PMID:11914276: high-throughput localization study; kept because the
  cytoplasmic result is consistent with the CCT/TRiC folding machine.
- PMID:19536198: high-throughput chaperone atlas; useful as context for
  chaperone-protein contacts but not a distinct generic Cct8 binding function.

The default `deep-research-falcon` command failed because no Falcon/OpenAI/Asta/
Perplexity API key was available. The cached May 2026 Falcon report was already
present and was reviewed.

Manual literature search for CCT8 and YJL008C in yeast through 2026-10-01 found
the same newer direct yeast-TRiC structural paper cached for CCT6/CCT7,
PMID:40070846, which resolves ADP-state cryo-EM intermediates of yeast TRiC and
places CCT8 among the CCT6-side subunits that lean outward early during ring
opening. This supports the structural subunit narrative but does not require a
new GO term beyond the existing ATP hydrolysis, ATP-dependent chaperone
contribution, protein-folding, and CCT-complex membership terms.
