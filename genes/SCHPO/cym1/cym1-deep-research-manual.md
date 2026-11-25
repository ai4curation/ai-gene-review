# Manual literature synthesis for S. pombe cym1

Live deep research was unavailable for this review, so this file records the
manual synthesis from cached publications, UniProt, and current PAINT records.

## Functional summary

S. pombe Cym1 should be curated as a mitochondrial matrix M16
metallopeptidase in the PreP family whose conserved function is degradation of
cleaved mitochondrial presequences and other unstructured matrix peptides. The
S. pombe UniProt record describes Cym1 as a matrix metalloendopeptidase that
degrades mitochondrial transit peptides by similarity to budding-yeast Cym1 and
places it in the peptidase M16/PreP subfamily.

The closest direct Cym1 literature comes from S. cerevisiae. Yasuhara et al.
identified the purified mitochondrial matrix protease M as the CYM1 gene
product and showed that the enzyme hydrolyzes peptide substrates on the
N-terminal side of paired basic residues [PMID:35997162]. Taskin et al.
summarize the established view that degradation of mitochondrial peptides is
performed by yeast Cym1 and human PreP, then show that the matrix
metalloprotease Ste23 cooperates with Cym1 in yeast peptide clearance
[PMID:28228553]. Teixeira and Glaser summarize the broader organellar model in
which targeting peptides are cleaved after import and then degraded by PreP
[PMID:22495024].

Current PAINT annotations in PANTHER family PTHR43016 place
metalloendopeptidase activity and protein catabolism at PTN000220482 and
mitochondrial matrix localization at PTN000220483. The PAINT
metalloendopeptidase and matrix IBDs are sound for S. pombe cym1. The process
IBD is directionally right but uses GO:0030163 protein catabolic process, which
overstates the substrate class for a protease that degrades released peptides;
PomBase already has the better transferred term GO:0043171 peptide catabolic
process.

## Annotation decisions

- Accept metalloendopeptidase activity, peptide catabolic process, and
  mitochondrial matrix as the core molecular function, process, and location.
- Keep the high-throughput S. pombe mitochondrion row because the root
  organelle call is true and informative beside the specific matrix rows.
- Accept both GO:0006508 proteolysis rows as broad but true assertions of the
  peptide-bond hydrolysis carried out by Cym1.
- Modify GO:0030163 protein catabolic process to GO:0043171 peptide catabolic
  process because Cym1 degrades released peptides rather than intact proteins.
- Keep GO:0008270 zinc ion binding as a non-core cofactor property and mark
  the generic IPR011249 metal-ion-binding IEA as too general beside the
  separately supported zinc term.
- Mark the mitochondrial intermembrane-space ISS row from budding-yeast Cym1 as
  over-annotated because it lacks S. pombe-specific or inspected donor evidence
  beyond the same homology transfer that also supports matrix localization; all
  specific PreP-family evidence supports the matrix.
