# Acetylcholine module evidence checks

Run from the repository root:

```sh
uv run python modules/acetylcholine_signaling-source-analysis/check_receptor_assemblies.py
uv run python modules/acetylcholine_signaling-source-analysis/check_signaling_choices.py
uv run python modules/acetylcholine_signaling-source-analysis/check_review_refinements.py
uv run python modules/acetylcholine_signaling-source-analysis/check_module.py
```

The first command checks explicit receptor subunit combinations, copy counts,
same-species assembly boundaries and source quotes. It does not infer assembly
from protein presence. The production module compiler treats each complex
activity as an atom, so the subunit checks inspect `active_units` directly.

The signaling checker tests exact receptor/G-alpha choices and independent
regulator alternatives using the production compiler, with an explicit complex
subunit oracle. The refinement checker audits GO aspects using is_a ancestry;
it excludes part_of because an MF activity can be part of a BP. These checks
were added after independent scientific review found real structural and
annotation mistakes, and do not replace assessment of the supporting papers.

The final command checks the 44-member review panel, exact accessions and taxonomy,
PANTHER placement against normally fetched UniProt records, and the production
module validator. `members.json` includes the exact VAChT interface member;
generic downstream PLC/cAMP and exocytosis modules are not recursively expanded
into unreviewed additional panels. The panel does not claim exhaustive sampling
of vertebrates or all experimentally possible receptor assemblies.

## Muscarinic construct provenance

`structure-provenance/` contains unmodified RCSB JSON responses retrieved on
2026-10-26 for the two structures in PMID:31073061. Regenerate explicitly with
`python3 modules/acetylcholine_signaling-source-analysis/fetch_structure_provenance.py`.
Each filename identifies the PDB entry and polymer-entity number (or `entry`).
Source endpoints use `https://data.rcsb.org/rest/v1/core/` followed by
`entry/6OIK` or `polymer_entity/6OIK/2`, for example.

* 6OIK entity 2 maps across its 354 residues to human GNAO1/P09471, with
  engineering substitutions E9D, R10K, L13V and A18M. Entity 1 maps to human
  CHRM2/P08172. The mouse component in the complex is a stabilizing antibody;
  it does not make the receptor or G-alpha a mouse exemplar.
* 6OIJ entity 1 is explicitly a human Gi1/G11 chimera: the first 29 residues
  derive from Gi1 and the remainder maps to GNA11/P29992. Entity 2 is an
  engineered human M1 receptor. This is structural support for coupling with
  construct limitations, not a wild-type human G11 sequence determination.

These structures establish receptor/G-protein interfaces. They do not directly
assay adenylyl cyclase inhibition or prove that all G-alpha family members share
an effector. The separate M4/Go cellular reporter experiment (PMID:7961880)
supports context-dependent cAMP suppression without establishing purified
Go–ADCY6 inhibition. G14 provenance is documented separately under the GNA14
gene's source analysis; the 2024 BRET experiment lacks an explicit construct
sequence, and its human assignment is a method/supplier inference.

## Evidence boundaries

Each module edge has source evidence. Transport/synthesis/hydrolysis links are
chemical continuity between independently measured reactions, rather than
claims of protein association. Human heterologous-expression experiments keep
the host organism distinct from the protein's species. Native mouse regulator
and rat/chicken channel measurements are explicit comparisons; none proves a
complete alternative pathway in that species.

The module and gene notes retain literature access limits and failed actual
deep-research provider attempts. No generated provider report is fabricated.
