# BTF3L4 curation notes

Date: 2026-07-18

## Scope and retrieval record

- Reviewed human BTF3L4, UniProtKB Q96K17, against the fetched UniProt and GOA records, cached primary literature, the existing human BTF3 review, QuickGO term records, and manually inspected BioGRID interaction details.
- Ran `just fetch-gene human BTF3L4` and `just fetch-gene-pmids human BTF3L4` to create the review stub and cache the GOA-supported publications.
- The requested Falcon deep-research run failed with HTTP 402. Its automatic Perplexity-lite fallback also failed with HTTP 401 because no quota was available. No provider-labelled deep-research file was created; the evidence synthesis is recorded in BTF3L4-deep-research-manual.md.

## Protein identity, family, and isoforms

BTF3L4 is a reviewed 158-residue human protein. UniProt names it transcription factor BTF3 homolog 4, places residues 33-98 in a NAC-A/B domain, predicts residues 122-158 to be disordered, and assigns it to the NAC-beta family [file:human/BTF3L4/BTF3L4-uniprot.txt, "Belongs to the NAC-beta family."; "NAC-A/B"]. UniProt does not provide a direct function statement or a curated subcellular-location statement for BTF3L4. PAN-GO reports zero evolutionary-model annotations, and Pharos classifies the protein as Tdark [file:human/BTF3L4/BTF3L4-uniprot.txt, "PAN-GO; Q96K17; 0 GO annotations based on evolutionary models."; "Pharos; Q96K17; Tdark."].

Three UniProt isoforms are recorded:

- Q96K17-1 is the displayed 158-residue sequence.
- Q96K17-2 lacks residues 1-58, removing the amino terminus and the first 26 residues of the annotated NAC-A/B domain [file:human/BTF3L4/BTF3L4-uniprot.txt, "Missing (in isoform 2)"].
- Q96K17-3 substitutes residues 57-78 and lacks residues 79-158, disrupting the NAC-A/B domain and deleting the disordered acidic carboxyl terminus [file:human/BTF3L4/BTF3L4-uniprot.txt, "Missing (in isoform 3)"].

No publication found here establishes isoform-specific function. The structural differences instead motivate direct isoform-resolved interaction tests.

## Direct and convergent interaction evidence

The strongest gene-specific molecular evidence is association with NACA:

- Targeted NACA affinity purification followed by mass spectrometry in HEK293T cells explicitly identified BTF3L4 among proteins recruited to dephosphorylated NACA [PMID:30948508, "NACA dephosphorylation was associated with specific recruitment of novel NACA interactants, such as basic transcription factor 3 (BTF3) and its homolog BTF3L4."]
- BioGRID interaction detail for NACA-BTF3L4 was manually inspected on 2026-07-18. It records independent support from BioPlex AP-MS in PMID:33961781, cross-species co-fractionation in PMID:26344197, and tissue XL-MS in PMID:38334954, in addition to PMID:30948508. The methods in the cached papers are consistent with those records [PMID:33961781, "Through affinity-purification mass spectrometry, we have created two proteome-scale, cell-line-specific interaction networks."]; [PMID:38334954, "cross-linking mass spectrometry (XL-MS) has emerged as a powerful tool for defining endogenous PPIs of cellular networks."]
- The conserved NAC-A/B domain and NAC-beta family assignment provide independent structural-family support for an alpha-beta NAC pairing [file:human/BTF3L4/BTF3L4-uniprot.txt, "Belongs to the NAC-beta family."].

Taken together, these data support BTF3L4 membership in a NACA-containing nascent polypeptide-associated complex. The evidence is strongest for physical association and complex membership. It does not by itself establish that BTF3L4-containing NAC binds ribosomes or performs the same cotranslational targeting function as canonical BTF3.

## Existing GOA annotations

The fetched GOA contains five rows, grouped into three review records. Every row is GO:0005515 protein binding with IPI evidence:

- PMID:25416956: TXLNA and TXLNB from a large binary-interactome screen [PMID:25416956, "a systematic map of ?14,000 high-quality human binary protein-protein interactions"].
- PMID:32296183: TXLNA and SMYD2 from HuRI [PMID:32296183, "reference interactome map of human binary protein interactions"].
- PMID:40205054: TXLNA from a U2OS multimodal cell map using AP-MS and imaging [PMID:40205054, "Proteins are purified from whole-cell biochemical extracts and their biophysical interactions are determined using AP-MS."].

These interactions are not rejected. TXLNA recurs in three independent studies, and UniProt also lists interactions with TXLNA, TXLNB, and SMYD2 [file:human/BTF3L4/BTF3L4-uniprot.txt, "Q96K17; P40222: TXLNA"]. However, GO:0005515 conveys only generic binding and none of these screens establishes a partner-specific molecular activity. Each existing annotation is therefore marked MARK_AS_OVER_ANNOTATED rather than REMOVE.

## Biological-process evidence outside the molecular core

- In mouse C3H10T1/2 mesenchymal stem cells, Btf3l4 was identified in a BMP-2-induced chondrogenic proteomics experiment, and the paper reports experimental verification of a role in differentiation [PMID:20008835, "the biological roles of BTF3l4 and fibulin-5, two novel chondrogenesis-related proteins identified in the present study, were verified in the context of chondrogenic differentiation."]. Inspection of the available article text showed that Btf3l4 knockdown reduced Alcian blue staining and Col2a1, aggrecan, and Col11a1 expression without reducing Sox9. This supports a conservative human orthology-based proposal for GO:0032332 positive regulation of chondrocyte differentiation with ISS evidence. It is contextual and non-core.
- In human glioma cells, BTF3L4 down-regulation reduced migration, invasion, and proliferation [PMID:38320629, "the down-regulation of BTF3L4 protein in the glioma cell line had a detrimental effect on cell migration, invasion, and proliferation."]. A gastric-cancer study independently found that BTF3L4 knockdown reversed proliferation and invasion promoted by MIR194-2HG depletion [PMID:39425187, "knockdown of BTF3L4 significantly recovered the promotion effect of MIR194-2HG knockdown on GC cell proliferation and invasion"]. These data support a proposed GO:0008284 positive regulation of cell population proliferation annotation with IMP evidence, but only as a cancer-context phenotype rather than an evolved molecular core.
- Mouse and AML-12 acetaminophen-injury models associated BTF3L4 overexpression with apoptosis, inflammatory responses, reactive oxygen species, and mitochondrial disruption [PMID:38426192, "Increased BTF3L4 expression increases the degree of apoptosis, reactive oxygen species generation, and oxidative stress, which induces cell death and liver injury."]. This toxic-injury model does not establish a normal human core function, so no GO proposal was made from it.

## Deliberate boundaries

The canonical human BTF3 protein is a well-established NACA partner with ribosome binding and prevention of inappropriate endoplasmic-reticulum targeting. BTF3L4 is homologous and has a compatible NAC-beta domain, but the BTF3L4-specific papers inspected here do not directly demonstrate ribosome binding, nascent-chain association, cotranslational folding, prevention of ER mistargeting, or direct DNA-binding/transcription-factor activity. Those functions were not transferred to BTF3L4.

Likewise, the CD-CODE nucleolar record and the U2OS cell-map syntaxin-binding assembly were not promoted to core locations or functions. The former is a database localization call without a gene-specific mechanistic paper in this evidence set, and the latter is a data-driven assembly whose specific TXLNA interaction is more safely retained as interaction evidence.

## Final annotation decisions

- Existing GO:0005515 records from PMID:25416956, PMID:32296183, and PMID:40205054: MARK_AS_OVER_ANNOTATED.
- New GO:0005854 nascent polypeptide-associated complex: IPI, supported chiefly by PMID:30948508 and convergent NACA-BTF3L4 interaction datasets.
- New GO:0032332 positive regulation of chondrocyte differentiation: ISS from the mouse Btf3l4 study PMID:20008835; non-core.
- New GO:0008284 positive regulation of cell population proliferation: IMP from human glioma cells in PMID:38320629, corroborated in gastric-cancer cells by PMID:39425187; non-core.
- Core function: alternative NAC-beta partner of NACA in a nascent polypeptide-associated complex. Direct ribosome-associated and cotranslational activities remain unresolved.

## Key experimental priorities

1. Test endogenous reciprocal NACA-BTF3L4 association and co-migration with ribosomes, with BTF3 as a quantitative comparator.
2. Resolve whether isoforms 2 and 3 bind NACA despite disruption of the NAC-A/B domain.
3. Use BTF3 and BTF3L4 single and combined perturbations with nascent-chain and ER-mistargeting reporters to distinguish redundancy from specialization.
4. Determine whether the developmental, cancer, and toxic-injury phenotypes converge on cotranslational proteostasis or reflect a separate NACA-dependent nuclear mechanism.

