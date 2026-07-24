# MAGI1 manual deep research

## Scope and provenance

Manual synthesis performed on 2026-07-18 after the configured deep-research
providers failed: Falcon/Edison returned HTTP 402 and the Perplexity fallback
returned HTTP 401 (quota exceeded). No provider-branded deep-research output was
created. Evidence below comes from the reviewed UniProt record Q96QZ7 and
primary publications cached under `publications/`.

## Biological synthesis

MAGI1 is a large, multidomain MAGUK-family scaffold rather than a demonstrated
enzyme. The reviewed human protein has six PDZ domains, two WW domains, and a
guanylate-kinase-like domain. Its modular architecture supports simultaneous
recruitment of transmembrane proteins, signaling regulators, and cytoskeletal
proteins at specialized membrane contacts
[file:human/MAGI1/MAGI1-uniprot.txt, "Interacts through its WW 2 domain with SYNPO and through its PDZ 5 domain with ACTN4"].

The best-supported core role is organization of cell-cell junction complexes.
Human MAGI1 is localized to epithelial tight junctions and the cell membrane
[file:human/MAGI1/MAGI1-uniprot.txt, "Localizes to epithelial cells tight junctions"].
The original BAI1 study identified PDZ-dependent association and colocalization
at the cytoplasmic membrane, especially cell-cell junctions
[PMID:9647739, "both products were co-localized at the cytoplasmic membrane, especially at cell-cell junctions"].
MAGI1 also scaffolds RAPGEF2/Rap GEP at tight junctions
[PMID:11168587, "MAGI-1/BAP1 serves as a scaffolding molecule for Rap GEP at tight junctions in epithelial cells"].

Junctional scaffolding has direct functional consequences. ESAM recruits MAGI1
to endothelial cell contacts; ESAM-MAGI1 colocalization activates RhoA, promotes
actin polymerization, and strengthens cell-cell adhesion
[PMID:20298433, "ESAM-mediated MAGI-1 recruitment to the cell membrane and mature cell adhesion were inhibited by a RhoA inhibitor"].
MAGI1 binds the actin-associated proteins synaptopodin and alpha-actinin-4,
supporting a physical route from junctional complexes to the actin cytoskeleton
[PMID:12042308, "The interaction and colocalization of MAGI-1 with two actin-bundling proteins suggest that MAGI-1 may play a role in actin cytoskeleton dynamics within polarized epithelial cells"].

MAGI1 is also required for tight-junction integrity in human epithelial cells.
High-risk HPV E6-mediated MAGI1 degradation disrupts ZO-1 localization, whereas
E6 ablation restores junctions in a MAGI1-dependent manner
[PMID:21123374, "Ablation of E6 expression restores tight junctions, and this restoration is dependent on the presence of MAGI-1"].
In colorectal cancer cells, MAGI1 gain and loss reciprocally affect E-cadherin
and beta-catenin localization, actin organization, adhesion, and Wnt signaling
[PMID:21666716, "MAGI1 silencing decreased E-cadherin and beta-catenin localization at cell-cell junctions"].

MAGI1 has context-specific roles outside canonical epithelial tight junctions.
Interaction studies place it in the podocyte slit-diaphragm neighborhood and in
neuronal/postsynaptic compartments, but several older papers use the S-SCAM/MAGI
nomenclature ambiguously. Those annotations should not be rejected from
abstract-only evidence; they are retained as undecided or non-core where the
cached text does not resolve the exact MAGI family member.

## Curation conclusions

- Core molecular function: molecular adaptor activity (GO:0060090), supported
  by direct evidence that MAGI1 brings multiple proteins into junctional
  signaling and adhesion complexes.
- Core locations: cell-cell junction, bicellular tight junction, adherens
  junction, and the cytoplasmic face of the plasma membrane.
- Core processes: cell-cell adhesion, bicellular tight-junction assembly or
  restoration, junction-associated actin organization, and junctional signal
  transduction.
- The numerous `protein binding` annotations are experimentally useful as
  interaction records but are too generic to describe MAGI1 molecular function.
  They should not substitute for molecular adaptor activity.
- No catalytic guanylate-kinase activity should be inferred merely from the
  guanylate-kinase-like domain.

## Evidence limitations

Many interaction annotations derive from proteome-scale, motif-screening,
proximity-labeling, or virus-host studies. These establish physical association
or proximity but often do not establish a physiological MAGI1 function. The
cached versions of several older papers are abstract-only, and the exact MAGI1
row may reside only in supplementary data. Experimental annotations were not
removed on that basis.
