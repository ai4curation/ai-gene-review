# CCT7 notes

## 2026-10-01 current GOA and IBA re-review

Forced a current GOA/UniProt refresh with `just fetch-gene yeast CCT7 --force`.
QuickGO now returns 14 rows. The live rows keep the two sound PTHR11353 IBA
assertions, add the InterPro2GO `GO:0005524` ATP-binding row, and add a
ComplexPortal `GO:0005832` row against the yeast CCT crystal structure
(PMID:21701561).

Five stale rows from the older snapshot are retained as `retired: true` so
source preservation stays explicit: obsolete `GO:0051082` by IBA, IEA and IDA;
the retired generic `GO:0000166` keyword row; and the retired GO_REF:0000120
ATP-binding row. The live `GO:0005524` row is accepted, mirroring the other
current InterPro ATPase rows, while the old `GO:0000166` row is narrowed to ATP
binding plus ATP hydrolysis.

The current PTHR11353 PAINT extract retains `PTN004253040` for inherited
CCT/TRiC protein-folding biology and `PTN000143937` for eta-subunit membership
in the chaperonin-containing T-complex. It no longer carries the obsolete
`GO:0051082` molecular-function assertion, so the old unfolded-protein-binding
IBA is a historical stale-source row rather than a current IBA to dispute.

Cached PMID checks read:

- PMID:16762366: abstract establishes purified yeast CCT as an essential
  ATP-dependent protein-folding machine required for actin and tubulin folding
  [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential ATP-dependent
  protein folding machine"].
- PMID:21701561: abstract establishes the yeast CCT-actin crystal structure and
  the asymmetric CCT subunit organization [PMID:21701561 "We have solved the
  crystal structure of yeast CCT in complex with actin"].
- PMID:15704212: abstract establishes the two-ring, eight-subunit yeast CCT
  architecture and supports the Cct7-Cct6 complex-membership row [PMID:15704212
  "each of which is composed of a stoichiometric array of eight different subunits"].
- PMID:11914276: high-throughput localization study; kept because the cytoplasmic
  result is consistent with the CCT/TRiC folding machine [PMID:11914276 "we report
  the first proteome-scale analysis of protein localization within any eukaryote"].

The default `deep-research-falcon` command failed because no Falcon/OpenAI/Asta/
Perplexity API key was available. The cached May 2026 Falcon report was already
present and was reviewed.

Manual literature search for CCT7, Cct7 and YJL111W in yeast through 2026-10-01
found the same newer direct yeast-TRiC structural paper cached for CCT6,
PMID:40070846, which resolves ADP-state cryo-EM intermediates of yeast TRiC and
places CCT7 in the outward tilting wave after CCT3/CCT6/CCT8. This supports the
structural subunit narrative but does not require a new GO term beyond the
existing ATP hydrolysis, ATP-dependent chaperone contribution, protein-folding,
and CCT-complex membership terms [PMID:40070846 "and expands to the outward
leaning of the consecutive CCT6/8/7/5 subunits."].
