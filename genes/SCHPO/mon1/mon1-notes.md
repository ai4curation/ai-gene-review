# mon1 notes

## 2026-10-17 review

PTHR13027 is the PANTHER SAND/Mon1 family. S. pombe `mon1` (Q10150) is in
`PTHR13027:SF7`, the fungal/plant/metazoan Mon1 subfamily that contains the
S. cerevisiae PAINT seed `SGD:S000003092`.

The family PAINT cache has three relevant nodes that reach S. pombe `mon1`:

- `PTN000989606`, at Fungi, places `GO:0000329 fungal-type vacuole membrane`
  and `GO:0006623 protein targeting to vacuole` from the S. cerevisiae `MON1`
  seed.
- `PTN000315021`, at Eukaryota, places the `contributes_to`
  `GO:0005085 guanyl-nucleotide exchange factor activity` call from
  S. cerevisiae and Drosophila Mon1.
- `PTN000315023`, at Opisthokonta, places `GO:0035658 Mon1-Ccz1 complex` from
  fungal, metazoan, and worm Mon1 seeds.

I did not find a PubMed hit for a direct S. pombe `mon1`/`SPAC1D4.03c` study
using searches for `(Schizosaccharomyces pombe OR fission yeast) AND (mon1 OR
SPAC1D4.03c OR Ccz1)`, nor a direct S. pombe hit in a web search for
`Schizosaccharomyces pombe mon1 Mon1 Ccz1 vacuole autophagy`. The current
PomBase GOA rows are therefore judged as orthology transfers from the
S. cerevisiae gene rather than as direct fission-yeast experiments.

Key primary support:

- Wang et al. 2002 identified S. cerevisiae `mon1Delta` and `ccz1Delta` as
  mutants defective in Ape1 import by Cvt, autophagy, pexophagy, and multiple
  vacuole-terminal routes, and showed that Mon1 and Ccz1 form a stable
  peripheral membrane complex [PMID:12364329, "Subcellular fractionation and
  co-immunoprecipitation experiments confirm that Mon1 and Ccz1 physically
  interact as a stable protein complex termed the Ccz1-Mon1 complex."].
- Wang et al. 2003 placed S. cerevisiae Mon1-Ccz1 at the Ypt7-dependent
  tethering/docking step of homotypic vacuole fusion [PMID:14662743, "Analysis
  of homotypic vacuole fusion demonstrated that vacuoles from strains defective
  in the CCZ1 and MON1 genes could not fuse."].
- Nordmann et al. 2010 established that the dimeric S. cerevisiae Mon1-Ccz1
  complex is the Rab7/Ypt7 GEF, with neither subunit active alone
  [PMID:20797862, "We now provide evidence that the dimeric Mon1-Ccz1 complex is
  the Rab7/Ypt7 GEF."].
- Kiontke et al. 2017 combined Chaetomium thermophilum structural work with
  S. cerevisiae mutational analysis and showed that a Mon1-Ccz1 longin-domain
  interface drives Ypt7 exchange [PMID:28051187, "The crystal structure of a
  catalytic MC1 core complex bound to Ypt7 provides mechanistic insight into its
  function."].

Review decisions:

- Accept the PTN000989606 fungal vacuolar membrane and vacuolar protein-targeting
  IBAs as correct, core fungal Mon1 inheritances.
- Accept the PTN000315021 contributes_to GEF activity and the PTN000315023
  Mon1-Ccz1 complex placement as correct broader PAINT inheritances.
- Mark the InterPro longin-domain `GO:0016192 vesicle-mediated transport`
  mapping as over-general beside the accepted late endosome-to-vacuole transport
  row.
- Keep the autophagy orthology call as non-core because it is a pathway using the
  vacuolar Mon1-Ccz1/Ypt7 exchange module; leave the cytosol orthology transfer
  undecided until the SGD source row is checked.
