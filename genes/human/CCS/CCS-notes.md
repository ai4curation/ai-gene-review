# CCS notes

Deep research provider status, 2026-11-21: `just deep-research-falcon human CCS
--fallback perplexity-lite` could not run because only the `claude_code`
provider was available in this checkout, and `just deep-research-claude-code
human CCS` failed because the Claude Code CLI was not authenticated. These
manual notes are the literature trail for the first CCS review.

## Core picture

CCS is the cytosolic and mitochondrial intermembrane-space copper chaperone that
matures SOD1. Human CCS and SOD1 directly interact in vitro and in vivo
[PMID:9726962 "CCS and SOD1 directly interact in vitro and in vivo"], and a
mechanistic human study of Ctr1-to-CCS-to-SOD1 copper transfer describes CCS as
providing SOD1's catalytic copper ion and helping form the SOD1 intra-subunit
disulfide [PMID:31292775 "Ccs proteins consist of three conserved domains that
are essential for target recognition and copper ion delivery"; PMID:31292775
"Unlike other copper chaperones, Ccs also plays a crucial role in the formation
of an intra-subunit disulfide bond within Sod1"].

CCS itself belongs to the Cu/Zn superoxide dismutase fold family but is not the
superoxide dismutase enzyme. The local PANTHER review records a PAINT IRD at
`PTN008300250` that negates `GO:0004784` on the CCS clade, matching the
biochemistry: CCS transfers copper to SOD1 instead of directly dismutating
superoxide.

CCS has two well-supported active compartments. A Nat Commun study reports that
human CCS1 and SOD1 localize to both cytosol and mitochondrial intermembrane
space and that CCS import into mitochondria depends on its Cys141/Cys144/Cys227
oxidation cycle [PMID:24026195 "both localize to the cytosol and the
mitochondrial intermembrane space"; PMID:24026195 "CCS1 import parallels SOD1
import that also depends on CCS1"].

## Annotation decisions

- `GO:0016532` superoxide dismutase copper chaperone activity is the core
  molecular function. The Reactome event `R-HSA-3299753` summarizes the same
  activity as copper transfer to a zinc-bound SOD1 monomer followed by SOD1
  disulfide formation and dimerization.
- `GO:0005507` copper ion binding is accepted: CCS needs bound copper for its
  delivery reaction, and UniProt records zinc-liganding residues 147, 155, 164
  and 167 in human CCS domain II.
- The `GO:0015035` protein-disulfide reductase activity row from
  PMID:24026195 should be corrected to `GO:0015036` disulfide oxidoreductase
  activity. The paper supports oxidation-dependent CCS import and disulfide
  formation during CCS/SOD1 maturation, not the reductase direction named by
  `GO:0015035`.
- The InterPro2GO `GO:0006801` superoxide metabolic process and the family-level
  `GO:0019430` removal of superoxide radicals rows describe the activity of
  mature SOD1-type enzymes. CCS indirectly supports those processes by maturing
  SOD1, but does not itself metabolize superoxide.
- `GO:0045041` protein import into mitochondrial intermembrane space is retained
  as non-core. CCS appears to serve as a specialized import receptor for both
  CCS and SOD1 in the IMS, but its defining activity is copper/disulfide
  maturation of SOD1.
- All bare `GO:0005515` rows are removed under the project protein-binding
  policy. Several are real contacts, especially SOD1 and SLC31A1, but the
  generic term carries no molecular-function information.

## Family-level notes

PTHR10003 uses a family-wide `GO:0004784` and `GO:0019430` IBD from
`PTN000000113`. Those terms are sound for SOD1/SOD3-type enzymes but not for
CCS. The review now excepts human, yeast and fly CCS proteins from both terms:
`GO:0004784` has a PAINT IRD at `PTN008300250`, and `GO:0019430` has a proposed
ADD_IRD at the same CCS clade because SOD1 maturation is upstream of, not
directly part of, superoxide radical removal.
