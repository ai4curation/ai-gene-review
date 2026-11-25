# ssc1 review notes

## Retrieval

- `just fetch-gene SCHPO ssc1` seeded UniProt, GOA and the review YAML. The
  first run timed out after writing UniProt and GOA; the rerun completed and
  seeded 19 GOA rows.
- `just fetch-gene-pmids SCHPO ssc1` found PMID:1923816, PMID:2123810,
  PMID:26545917 and PMID:16823372; PMID:2123810 was newly cached.
- `just mod-description-deep-research SCHPO ssc1` skipped `SCHPO`; there is no
  MOD-description provider for PomBase genes in this repository.
- `just deep-research SCHPO ssc1 --provider perplexity` failed because the
  provider was unavailable. I wrote `ssc1-deep-research-manual.md` from local
  cached evidence instead.
- `just paint-losses SCHPO ssc1` reported no IRD or IKR loss on the ssc1
  lineage.

## GO-CAM 69729a3800007453

The GO-CAM activity `gomodel:69729a3800007453/6994852c00000305` uses
PomBase:SPAC664.11/ssc1 in the PAM complex and places its ATP hydrolysis
activity in the mitochondrial matrix as part of protein import into the
mitochondrial matrix. This is the right gene, pathway, complex and
compartment: Ssc1 is the mitochondrial Hsp70 motor that binds translocating
preproteins on the matrix side of TIM23 [PMID:14638855, "the mitochondrial
Hsp70 (mtHsp70) of the matrix forms the core of the protein import motor and
directly binds to the preprotein in transit"].

One disagreement should go into the final GO-CAM consistency-notes PR: the model
uses the generic `GO:0016887 ATP hydrolysis activity` for the Ssc1 PAM activity,
whereas the gene review supports the more specific existing S. pombe annotation
to `GO:0140388 protein translocation chaperone activity`. The ATPase row is
correct, but `GO:0140388` states the import-motor activity that distinguishes
Ssc1 from other Hsp70 ATPases.

## Annotation synthesis

S. pombe ssc1/ssp1 encodes a mitochondrial Hsp70. Direct fission-yeast evidence
establishes mitochondrial localization [PMID:2123810, "a 70-kDa protein which
is associated with the mitochondria"], and the curated UniProt record places
the protein in the mitochondrial matrix.

The matrix import role is inferred from budding-yeast Ssc1 and from the
conserved fungal Hsp70/PAM architecture. Budding-yeast mtHsp70 is a named core
PAM motor subunit [PMID:14638855, "Three essential subunits of the motor are
known: mitochondrial Hsp70 (mtHsp70); the peripheral membrane protein Tim44;
and the nucleotide exchange factor Mge1."]. PomBase's ISO rows for PAM
membership, matrix import and protein translocation chaperone activity are
therefore retained.

The Fe/S biogenesis role is direct in S. pombe. Unlike S. cerevisiae, where Jac1
mostly works through the specialized Hsp70 Ssq1, fission yeast uses the same
multifunctional Ssc1 for Jac1-dependent Fe/S biogenesis [PMID:26545917, "in
most eukaryotes, including Schizosaccharomyces pombe, FeS biogenesis involves
interaction between the J-protein Jac1 and the multifunctional Hsp70 Ssc1"].
That supports the direct ATP hydrolysis, ATP-dependent chaperone, and [2Fe-2S]
cluster assembly rows as core Fe/S annotations.

The PTHR19375 PAINT rows are mostly sound for ssc1. The mitochondrial Hsp70
node supports mitochondrion and iron-sulfur cluster assembly; the ancestral
Hsp70 node supports ATP hydrolysis and J-protein binding. I marked only the
cytoplasm row `TOO_GENERAL`, because the review already has matrix and
mitochondrion rows, and marked the inherited root-level protein-refolding row
over-annotated because the family review says that assertion overreaches into
specialized Fe/S Hsp70 branches.
