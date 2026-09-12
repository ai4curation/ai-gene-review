# Ptk7 (A0A8I6ALM9): evidence and exact-input prediction review

PTK7 is an inactive receptor kinase scaffold, not a tyrosine kinase or ATP-binding enzyme. The ProtNLM name captures this distinction correctly. Its function paragraph, however, transfers Off-track functions from fly, including R1–R6 photoreceptor targeting to the lamina, to a rat protein. Homology makes the donor biologically related but does not make the fly-specific developmental statement correct in rat.

## Input identity and functional boundary

The 1,079-residue rat sequence retains seven immunoglobulin-like domains, a membrane helix and a complete pseudokinase domain. Comparison with human PTK7 Q13308 maps 257/271 identical residues across the kinase-like domain. Human L828, Y877 and ALG948–950, implicated in the obstructed nucleotide pocket, map to identical rat L837, Y886 and ALG957–959. The N-terminal signal-peptide region is less conserved (12/30 identities), and the selected record does not call a signal peptide; this leaves initiation/topology details to verify without erasing the strong full-domain ortholog relationship. The emitted function donor Q6AWJ9 is Drosophila Off-track, not an unrelated cadherin.

## Biological evidence

- [PMID:32619402 — Structural Insights into Pseudokinase Domains of Receptor Tyrosine Kinases.](https://pubmed.ncbi.nlm.nih.gov/32619402/): Human PTK7 structural analysis identifies a sterically obstructed ATP-binding site; the implicated PTK7 residues are retained in the selected rat sequence.

> ATP binding to PTK7 and ROR2 is prevented by projection of a tyrosine side-chain from the β5/αD hinge region

- [PMID:24703874 — PTK7-Src signaling at epithelial cell contacts mediates spatial organization of actomyosin and planar cell polarity.](https://pubmed.ncbi.nlm.nih.gov/24703874/): Cell experiments show PTK7 recruits or organizes active Src at junctions rather than catalyzing Src-like phosphorylation itself.

> PTK7 interacts with the
> tyrosine kinase Src and stimulates Src signaling along cell-cell contacts.


> PTK7-Src signaling module for spatial regulation of ROCK activity, actomyosin
> contractility, and epithelial PCP.

- [PMID:21132015 — Protein tyrosine kinase 7 has a conserved role in Wnt/β-catenin canonical signalling.](https://pubmed.ncbi.nlm.nih.gov/21132015/): PTK7 depletion reduces canonical Wnt reporter output in the tested cells; the positive sign is experimentally grounded and context-specific.

> PTK7-deficient cells exhibit weakened β-catenin/T-cell factor transcriptional activity on Wnt3a stimulation.

- [PMID:20643356 — Epidermal wound repair is regulated by the planar cell polarity signaling pathway.](https://pubmed.ncbi.nlm.nih.gov/20643356/): Mouse genetic interactions implicate PTK7 in wound repair without establishing an autonomous wound-specific catalytic activity.

> Mice carrying mutant alleles of PCP genes Vangl2, 
> Celsr1, PTK7, and Scrb1, and the transcription factor Grhl3, interact 
> genetically, exhibiting failed wound healing

- [PMID:20704721 — The novel mouse mutant, chuzhoi, has disruption of Ptk7 protein and exhibits defects in neural tube, heart and lung development and abnormal planar cell polarity in the ear.](https://pubmed.ncbi.nlm.nih.gov/20704721/): Histology of Ptk7/chuzhoi mutant lungs identifies thickened interstitial mesenchyme and defective septation.

> thickened interstitial mesenchyme and reduced sepatation in chuzhoi mutants.


> Chuzhoi mutants exhibit defects in the heart including double outlet right ventricle (DORV) with a ventricular septal defect (VSD), or parallel arterial trunks.

- [PMID:15229603 — PTK7/CCK-4 is a novel regulator of planar cell polarity in vertebrates.](https://pubmed.ncbi.nlm.nih.gov/15229603/): The original mouse Ptk7 mutant study directly supports neural-tube closure and cochlear-polarity roles.

> disrupts neural tube closure and stereociliary bundle
> orientation

- [PMID:17910947 — Identification of twinfilin-2 as a factor involved in neurite outgrowth by RNAi-based screen.](https://pubmed.ncbi.nlm.nih.gov/17910947/): The donor paper is a neuronal RNAi screen; its abstract foregrounds twinfilin-2 and does not enumerate the PTK7 result.

> Phenotype-based screening of differentiating SH-SY5Y cells following
> retinoic acid (RA) stimulation

- [PMID:20837484 — The Wnt/planar cell polarity protein-tyrosine kinase-7 (PTK7) is a highly efficient proteolytic target of membrane type-1 matrix metalloproteinase: implications in cancer and embryogenesis.](https://pubmed.ncbi.nlm.nih.gov/20837484/): Human cell experiments connect PTK7 to actin organization and invasion; direction depends on context and receptor shedding.

> The enforced expression of membrane PTK7 in cancer cells
> leads to the actin cytoskeleton reorganization and the inhibition of cell
> invasion.

## Exact non-GO claims

The complete emitted record is preserved in [Ptk7-protnlm-source.json](Ptk7-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Inactive tyrosine-protein kinase 7

CNN (CS 2). “Inactive tyrosine-protein kinase 7” identifies the supported PTK7 pseudokinase lineage. Human structural evidence and conservation of the rat pocket-occluding residues independently support inactivity; the label is not accepted merely because another annotation uses it. [PMID:32619402](https://pubmed.ncbi.nlm.nih.gov/32619402/); [sequence analysis](Ptk7-bioinformatics/RESULTS.md).

### Function

> Acts as a calcium-dependent, homophilic cell adhesion molecule that regulates neural recognition during the development of the nervous system. Component of the repulsive Plexin signaling response to regulate motor axon guidance at the embryonic stage. Also component of a receptor complex that is required in the adult visual system to innervate the lamina layer; specific targeting of R1-R6 axons

NPI (CS 0; TAXON_CONSTRAINT_VIOLATION) for the composite statement, specifically its claim that rat PTK7 targets fly R1–R6 axons to the lamina. Q6AWJ9 is the homologous fly receptor Off-track, so this is a lineage-specific developmental overtransfer rather than a random unrelated-protein match. Generic adhesion, Plexin interaction and axon guidance are separately UNC for this rat product: homologous developmental signaling makes them plausible, but the fly paragraph does not establish each mechanism in rat. The demonstrated mammalian PTK7-Src-ROCK polarity mechanism is a different, independently supported claim. [Donor record](Ptk7-otk-prediction-donor.json); [PMID:24703874](https://pubmed.ncbi.nlm.nih.gov/24703874/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

The selected PTHR45080:SF21 assignment is consistent with PTK7 ancestry. Family-wide tyrosine kinase activity cannot be applied to the conserved inactive PTK7 branch. Its ALG motif and pocket-occluding residues explain catalytic divergence, whereas the Off-track relationship illustrates a separate boundary: conserved receptor ancestry does not imply conserved fly-specific neural anatomy. No unsupported ancestral-node placement is asserted.

## Evidence limits

Both decisive primary publications are available with full text. The structural experiment concerns human PTK7, and the junctional studies use cultured canine epithelial cells and mouse auditory epithelium; transfer to rat is explicitly ortholog-based. The exact N-terminus and each narrow developmental or stimulus annotation are not independently assayed here. The genuine Falcon report correctly identifies pseudokinase function but supplies a 2021 meeting citation for the structural work; the review instead cites the verified 2020 Molecular Cell paper (DOI:10.1016/j.molcel.2020.06.018). Donor tracing is preserved in the Q13308 and Q8BKG3 QuickGO snapshots. PMID:17910947 and PMID:15229603 are abstract-only in the cache; their gene-specific screen or apical-basal details remain unresolved without claiming a curator error.

Exact sequence mapping: [Ptk7-bioinformatics/RESULTS.md](Ptk7-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Donor annotation audit

The [human](Ptk7-Q13308-donor-goa.json) and [mouse](Ptk7-Q8BKG3-donor-goa.json) QuickGO snapshots preserve the source terms, qualifiers and primary references. Three ISO annotations explicitly negate kinase or ATP-binding activity; those negations are retained. The positive non-receptor-kinase IBA and transferase UniRule are separate conflicting claims.

The kidney screen’s [original XML](Ptk7-PMC4804176-fulltext.xml), DOI [10.1038/ncomms11103](https://doi.org/10.1038/ncomms11103), includes a table omitted from the ordinary publication text extraction. Reproducible [table extraction](Ptk7-bioinformatics/extract_kidney_table.py) shows [moderate cystic kidneys in all three Ptk7 mutants](Ptk7-bioinformatics/kidney-table.md). This is sufficient to retain kidney development as non-core.

The coronary-vasculature annotation traces to PMID:25807483. Its available full-text extraction does not expose a Ptk7-specific row; Europe PMC returned 404 for the full-text XML and the PMC page was blocked by browser verification. This narrow phenotype remains UNDECIDED, without inferring a curator error. The accessible chuzhoi paper independently establishes heart and ventricular-septum defects, so those broader annotations are retained.

PMID:17910947 is a kinase RNAi screen whose accessible abstract highlights twinfilin-2; this is not evidence that the PTK7 annotation is misattributed. Its PTK7 neurite/retinoic-acid result remains unverified. The apical-basal term similarly traces to an abstract-only original PTK7 paper and remains distinct from the clearly established planar-polarity axis.
