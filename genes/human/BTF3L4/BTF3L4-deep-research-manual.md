# Manual deep research: human BTF3L4

Date: 2026-07-18

## Research question

What is experimentally established for human BTF3L4, which annotations are justified, and which apparent functions are only family-level or context-specific inferences?

## Search and source strategy

The review combined the local UniProt and GOA records with cached primary publications and targeted database checks. Searches focused on BTF3L4 protein interactions, NACA, nascent polypeptide-associated complex, chondrogenesis, glioma, gastric cancer, acetaminophen liver injury, isoforms, localization, and BTF3 paralog comparison. QuickGO was used to confirm current GO identifiers and labels. BioGRID interaction detail for NACA-BTF3L4 was inspected directly on 2026-07-18 at https://thebiogrid.org/interaction/3706787/naca-btf3l4.html.

Automated deep research was attempted with Falcon and its configured Perplexity-lite fallback. Falcon returned HTTP 402 and Perplexity-lite returned HTTP 401 because quota was unavailable. Consequently, this file records the manual synthesis and is intentionally not named for either provider.

## Protein-level evidence

UniProtKB Q96K17 is a reviewed, 158-residue human protein assigned to the NAC-beta family. Its annotated NAC-A/B domain spans residues 33-98, followed by a predicted disordered region at residues 122-158 and an acidic segment at residues 134-150. The exact family statement is: "Belongs to the NAC-beta family."

The entry has no curated function paragraph and no curated subcellular-location paragraph. This absence matters because the name transcription factor BTF3 homolog 4 is not itself evidence of direct transcriptional activity. The protein name should not be converted into a DNA-binding or transcription-regulator annotation.

Three isoforms are recorded. Isoform 2 lacks residues 1-58 and therefore removes part of the NAC-A/B domain. Isoform 3 changes residues 57-78 and lacks residues 79-158, disrupting much of the domain and removing the carboxyl terminus. No functional study located in this review resolved the isoforms.

## NACA association and NAC-complex membership

PMID:30948508 provides the clearest BTF3L4-specific molecular result. The investigators purified NACA complexes from HEK293T cells and used mass spectrometry. The cached abstract states: "NACA dephosphorylation was associated with specific recruitment of novel NACA interactants, such as basic transcription factor 3 (BTF3) and its homolog BTF3L4."

Manual inspection of the BioGRID NACA-BTF3L4 interaction page identified four independent methodological contexts:

- PMID:30948508: NACA affinity-capture mass spectrometry.
- PMID:33961781: BioPlex affinity-capture mass spectrometry.
- PMID:26344197: biochemical co-fractionation in the conserved metazoan complex survey.
- PMID:38334954: cross-linking mass spectrometry in breast-cancer patient-derived xenograft tissue.

The pair-specific records are held in BioGRID datasets rather than stated in the narrative text of every cached article. The articles nevertheless verify the relevant experimental platforms. PMID:33961781 states, "Through affinity-purification mass spectrometry, we have created two proteome-scale, cell-line-specific interaction networks." PMID:38334954 states, "cross-linking mass spectrometry (XL-MS) has emerged as a powerful tool for defining endogenous PPIs of cellular networks."

This convergence is stronger than a single high-throughput hit. Together with the BTF3L4 NAC-beta-family assignment and NAC-A/B domain, it supports the conclusion: BTF3L4 is an alternative beta-chain partner of NACA in a human nascent polypeptide-associated complex.

The conclusion is intentionally limited. None of these BTF3L4-specific experiments directly shows ribosome binding, contact with nascent chains, prevention of inappropriate endoplasmic-reticulum targeting, or cotranslational folding. Those functions are established for canonical BTF3-NACA but remain hypotheses for BTF3L4-NACA.

## Existing interaction annotations

All fetched GOA annotations use GO:0005515 protein binding and IPI evidence:

- PMID:25416956 records BTF3L4 with TXLNA and TXLNB in a proteome-scale binary interaction map.
- PMID:32296183 records BTF3L4 with TXLNA and SMYD2 in HuRI.
- PMID:40205054 records BTF3L4 with TXLNA in the U2OS multimodal cell map.

The repeated TXLNA observation is biologically interesting, and UniProt lists TXLNA, TXLNB, and SMYD2 interactions. The generic protein-binding term, however, does not encode a mechanistic molecular activity. These records should be retained as interaction evidence but marked as over-annotated GO molecular-function statements.

The U2OS map associates BTF3L4 with a syntaxin-binding protein assembly, but the publication describes large-scale integration of AP-MS and imaging with algorithmic assembly annotation. It does not establish that BTF3L4 itself has a syntaxin-binding molecular activity. No such activity is proposed.

## Developmental evidence

PMID:20008835 examined BMP-2-induced chondrogenic differentiation of mouse C3H10T1/2 mesenchymal stem cells by quantitative proteomics. Its abstract states: "the biological roles of BTF3l4 and fibulin-5, two novel chondrogenesis-related proteins identified in the present study, were verified in the context of chondrogenic differentiation."

The accessible article text reports that Btf3l4 knockdown reduced Alcian blue staining and expression of cartilage matrix genes Col2a1, aggrecan, and Col11a1 while not reducing Sox9. This is experimental evidence that mouse Btf3l4 positively influences chondrocyte differentiation downstream of, or parallel to, Sox9. A human annotation is therefore proposed conservatively as ISS rather than treating the mouse experiment as direct human IMP evidence.

## Cancer-cell evidence

PMID:38320629 tested human glioma cell lines. The abstract states: "the down-regulation of BTF3L4 protein in the glioma cell line had a detrimental effect on cell migration, invasion, and proliferation." This supports a positive effect on cell population proliferation in that experimental context.

PMID:39425187 provides independent support in human gastric-cancer cells through the MIR194-2HG-miR-194/miR-192-BTF3L4 axis. The full text states: "knockdown of BTF3L4 significantly recovered the promotion effect of MIR194-2HG knockdown on GC cell proliferation and invasion". The language "recovered" appears to mean reversed or rescued the promoted phenotype, as also indicated by the figure legend.

These studies justify a proposed GO:0008284 positive regulation of cell population proliferation annotation with IMP evidence. Because both studies use malignant cellular contexts and do not establish the underlying biochemical activity, this is retained as non-core.

## Toxic-injury evidence

PMID:38426192 studied acetaminophen-induced liver injury in mice and AML-12 mouse hepatocytes. The abstract states: "Increased BTF3L4 expression increases the degree of apoptosis, reactive oxygen species generation, and oxidative stress, which induces cell death and liver injury."

The study provides perturbational evidence in a toxic-injury model, but it does not define a normal human molecular function. It also does not establish that BTF3L4 is a mitochondrial protein; mitochondrial disruption is a downstream phenotype. No human GO annotations for apoptosis, inflammation, oxidative stress, mitochondrial localization, or liver injury are proposed from this paper.

## Synthesis

The defensible molecular core is NACA-containing complex membership. BTF3L4 is a NAC-beta-family protein with reproducible NACA association across targeted AP-MS, large-scale AP-MS, co-fractionation, and XL-MS. That evidence supports GO:0005854 nascent polypeptide-associated complex.

The following claims are not yet directly supported for BTF3L4 and are excluded from the core:

- GO:0043022 ribosome binding.
- GO:1905551 negative regulation of protein localization to endoplasmic reticulum.
- GO:0051083 de novo cotranslational protein folding.
- Direct DNA binding or a transcription-factor molecular activity.
- A definitive nuclear, nucleolar, cytosolic, ribosomal, or mitochondrial functional location.

Contextual evidence supports chondrocyte differentiation and cancer-cell proliferation, but these phenotypes do not yet reveal the biochemical mechanism. The central unresolved question is whether BTF3L4 substitutes for canonical BTF3 in a ribosome-bound NAC or creates a distinct, regulated NACA complex.

## Curation-ready conclusions

1. Mark all existing GO:0005515 annotations as MARK_AS_OVER_ANNOTATED, while preserving the underlying interaction evidence.
2. Add GO:0005854 nascent polypeptide-associated complex with IPI evidence from PMID:30948508 and NACA as the supporting interactor.
3. Add GO:0032332 positive regulation of chondrocyte differentiation with ISS evidence from mouse PMID:20008835.
4. Add GO:0008284 positive regulation of cell population proliferation with IMP evidence from human glioma PMID:38320629, corroborated by gastric-cancer PMID:39425187.
5. Treat NACA-complex membership as core; keep developmental, cancer, and toxic-injury phenotypes non-core.

