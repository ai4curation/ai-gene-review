# Canonical Isc capacity consultation

This is a finite, source-grounded oracle for the module's **Fdx-supported,
HscBA-assisted route**. It is not a proteome classifier, a measured flux result,
or a predictor that an organism lacking a role cannot assemble any Fe-S proteins.
Only files in this consultation directory are authored here.

## Reproduce

From the repository root:

```sh
uv run python analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/capacity-consultation/check_capacity.py
uv run ruff check analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/capacity-consultation/*.py
```

The checker reads the current module and calls the production `compile_module`,
`iter_atoms`, `enumerate_routes`, `core_atoms`, and `is_satisfied` functions. It
records the module and engine hashes in its output. It also checks the frozen
source hashes in `evidence-ledger.yaml`. A changed consulted source fails until
its implications are reviewed; rebuilding the ledger is a deliberate curation
operation, not an automatic repair of that failure.

`build_ledger.py` makes the ledger reproducible: the role tiers, primary references
and rationales are explicit human-readable curation decisions in the script,
while accessions, taxa, core-function consistency and classification records are
read from the released sources. It does not convert an ACCEPT action or a citation
count into an assay claim. The original gene reviews and their released receipts
are unchanged.

## Evidence profiles and gates

- `DIRECT_ROLE_ASSAY`: an experiment on the organism's named ISC proteins supports
  the particular role or interface. This includes recombinant purified proteins;
  it does not mean an unperturbed cell, measured physiological flux, or a single
  experiment reconstituting all five roles simultaneously.
- `QUALIFIED_INFERENCE`: specific ISC identity, conserved activity and cognate
  partner evidence support a transfer from characterized bacterial machinery.
  KT2440 is in this tier. Azotobacter Fdx combines original isc-region identity,
  native redox characterization, ISC-specific IPR011536/TIGR02007 and native
  dependence with E. coli donor chemistry. Its donor interface is inferred.
- `ROLE_UNRESOLVED`: Azotobacter housekeeping IscA has broad binding and native
  participation evidence, but no established GO:0140132 cluster-delivery witness.

The `supported_or_inferred` profile admits the first two tiers. The `assay_only`
profile admits only the first, separately for molecular role and exact partner
interface. Consequently all three species panels support the qualified profile;
ECOLI supports the separate-assay profile, AZOVI lacks a demonstrated Fdx donor
edge, and PSEPK remains based on comparative inference. None of these labels claims
an experimentally complete native pathway.

Every atom also requires a listed representative identity, matching verified
classification, its required molecular function, specific ISC-role evidence,
the context's taxon, and the appropriate cognate interface. Taxon and interface
checks are supplied by the oracle: the production compiler does not enforce them.
The exact same-taxon check is intentionally conservative; it does not predict
whether cross-species experimental complementation would work.

The HscA subfamily and family-level branches are alternative classifications of
**one role**. Four atom IDs appear in every enumerated route because neither
individual HscA alternative is universal, but five biological roles are required.
There are four routes (two HscA choices, with or without optional IscA). IscA's
absence must not prevent support for the five-role route. Broad IscA cluster
binding is not enough for the optional cluster-delivery activity.

## Source boundaries

The released native-member consultation establishes the AF010139-to-Azotobacter
sequence bridge and its DJ116/UW/DJ-derived strain caveats. Those caveats are
inherited, not replaced with an assertion that every strain is interchangeable.
The other exact identities, activity syntheses and specific signatures are read
from the released ECOLI/PSEPK reviews and unchanged UniProt sources.

PMID25688831's full text explicitly assays E. coli IscS, IscU, Fdx and FNR;
PMID23682711 supplies additional Fdx interaction/redox evidence. These are positive
mechanistic evidence for the E. coli donor role. PMID16964969 measures Azotobacter
cluster transfer **to apo-Fdx** and never supplies evidence that Fdx donated an
electron in that assay. Native FdIV redox measurements (PMID10542283) and genetic
requirements (PMID16936042) support a qualified inference, not the missing donor
assay. The ACS route for PMID18986169 returned HTTP403, but the follow-up obtained the
[primary paper through its author institutional repository](https://air.unimi.it/retrieve/dfa8b98f-b99c-748b-e053-3a05fe0a3a96/chaperoni%202008.pdf).
Experimental Procedures, PDF page 3, explicitly identifies recombinant E. coli
IscU, ferredoxin, HscA and HscB. The publication cache remains abstract-only.
`interface-evidence.yaml` records this external organism quotation and the local
cache quotations; the checker does not pretend that the external full PDF is
cached locally. Optional IscA delivery is grounded in PMID11319236/15964837; iron donation
alone is a different molecular function.

`classification-provenance.yaml` preserves the exact PANTHER19.0 classification
row placing E. coli HscA P0A6Z1 in SF176, with the release-pinned official source
URL. UniProt lists only the family for this protein. PSEPK and AZOVI HscA remain
family-classified; no unverified subfamily was invented.

The SufU control is motivated by the independently reviewed PTHR10093 ambiguity:
B. subtilis O32163 has sulfur-transfer evidence and conflicting older cluster
reconstitution evidence. Failing this *cognate ISC scaffold* qualification does
not assert that every SufU protein lacks every cluster-binding activity.

## Sensitivity checks

`capacity-results.yaml` records the three qualified panels, stricter assay
profiles, each required-role removal in each panel, optional IscA omission,
classification alternatives, mixed taxa, missing cognate interfaces, an isolated
redox protein, family/activity-only descriptors, an actual DnaK alternative,
generic ferredoxin evidence, SufU family ambiguity, and binding without delivery.
The descriptor-withdrawal cases are synthetic information tests; they are not
fabricated native-mutant observations.

Gate ablations independently demonstrate that taxon, classification, activity,
specific-role evidence and cognate interfaces affect the result. Both the role
tier and interface tier independently prevent promotion of Azotobacter Fdx to
assay-established donor status. Structural mutations demonstrate that making IscA
mandatory or making both HscA classifications jointly required would break the
expected panels.

Anaerobic Fdx bypass and scaffold-suppressor HscBA bypass are reported as
`OUTSIDE_CANONICAL_PROFILE`, with incomplete canonical circuits. The scope comes
from PMID26560204 and the separate final-boundary consultation; these cases are
not scored as biological impossibility or absence of all ISC synthesis. Upstream
iron/reductant supply, expression levels, oxygen-dependent client demand and
physiological flux remain outside this finite capacity test.

## Version 2 provenance correction

The original ledger accidentally selected the last partner's role references for
KT2440 interfaces. This caused sulfur-handoff and ferredoxin-donor edges to cite
IscU papers. Version 2 selects the matching E. coli **edge** bundle explicitly:
PMID11577100 for sulfur handoff; PMID23682711/25688831 for electron donation;
PMID10869428/15485839/18986169 for chaperone-assisted transfer. All remain qualified
inferences in KT2440. The source union is now constructed from interface references
as well as role references, and the checker verifies every interface source's hash
coverage and cached quotations. Organism scope is recorded per reference. The
Azotobacter donor bundle explicitly identifies the E. coli mechanistic source and
excludes the Azotobacter cluster-recipient assay from donor evidence.

`handoff.yaml` remains byte-for-byte historical. `handoff-v2.yaml` supersedes it,
records old/new payload hashes, and reports results against the current module.
The 38 scenario results, six gate sensitivities and two structure mutations retain
their expected biological outcomes; this revision fixes evidence provenance.
