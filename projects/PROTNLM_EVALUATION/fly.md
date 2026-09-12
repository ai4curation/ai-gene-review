---
title: Fly ProtNLM evaluation
species: [DROME]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Fly ProtNLM evaluation

**The released Drosophila melanogaster set contains 94 protein records mapping to 94 distinct FlyBase genes. The first review cohort includes all 41 genes with GO predictions or function descriptions: 50 GO claims and 13 function paragraphs.** This is a complete census of that published species subset, followed by a content-based review tier; no gene was dropped to meet an arbitrary cohort size.

[Prioritized review queue](fly-benchmark/review-queue.csv) · [Coverage audit](fly-benchmark/review-inventory.json) · [41-gene cohort](fly-benchmark/functional-cohort.csv) · [Original GO/function statements](fly-benchmark/functional-predictions.csv) · [Claim/donor provenance](fly-benchmark/claim-provenance.csv) · [Full 94-record inventory](fly-benchmark/inventory.csv) · [All prediction statements](fly-benchmark/prediction-statements.csv) · [Sequences](fly-benchmark/sequences.fasta) · [Snapshot provenance](fly-benchmark/manifest.json) · [Parent project](../PROTNLM_EVALUATION.md)

## Coverage and scope

| Review tier | Records | Scope |
|---|---:|---|
| GO and/or function descriptions | 41 | First cohort; 33 have GO claims, 13 have function text, and five have both |
| Location/keyword output without GO or function text | 29 | Retained as a separate localization review tier |
| Name only | 24 | Retained in the census; not included in the initial function benchmark |

Across all 94 records there are 50 GO predictions, 13 function paragraphs, 58 location statements and two keywords. All 94 current UniProt entries are unreviewed/TrEMBL. This does **not** mean that their genes are uncharacterized: a predicted protein may be sequence-identical to a reviewed entry or represent an alternative isoform of a well-studied gene.

The census starts from the official [ProtNLM2 accession list](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv), restricted to NCBITaxon:7227, and freezes the live prediction and ordinary UniProt records on 8 September 2026. Symbols and primary gene IDs are resolved through the [FlyBase FB2026_02 identifier table](https://s3ftp.flybase.org/releases/current/precomputed_files/genes/fbgn_annotation_ID_fb_2026_02.tsv.gz). Other fly species are outside this initial cohort. API-served proteins absent from the published list are also outside this census.

Like the horse cohort, this benchmark is constructed **after the predictions were released**. It supports case-based evaluation of the available predictions, not an unbiased estimate of performance across the fly proteome. The investigation order prioritizes potentially informative errors and includes supported comparison candidates; it does not alter cohort membership or establish correctness in advance.

## GO prediction assessments

| Assessment | Claims | Meaning |
|---|---:|---|
| COR | 1 | Supported novel prediction |
| CNN | 11 | Supported biology already known |
| LSP | 16 | Supported, but less precise than existing knowledge |
| NPI | 7 | Refuted by biological evidence |
| UNC | 15 | Evidence does not yet validate or refute the claim |
| **Total** | **50** | **GO claims only** |

The 13 function paragraphs are assessed claim by claim in separate linked reviews; they are not assigned an artificial single GO score. CNN records established prior biology, not independently verified membership in the model's training data. [Validation summary](fly-benchmark/validation-summary.json) and [prediction evidence checks](fly-benchmark/prediction-evidence-validation.json) accompany the coverage audit.

Four unresolved mechanisms are selected for [focused OpenScientist investigations](fly-openscientist-selection.md): Dic4 substrate specificity, CG5611 reaction assignment, ttv-PC catalytic competence and TyrRS resveratrol recognition. These investigations target evidence gaps that structural or comparative analysis could help resolve.

The [next 20-gene selection](fly-next20.md) emphasizes metabolic enzymes and transport, drawing on remaining published records and additional original-export accessions. It includes GO/function, localization and name-only tiers and is separate from the completed results below.

## Illustrative findings

**All 41 genes have been reviewed: 456 existing GOA annotations, nine new annotation proposals, 50 ProtNLM GO claims and 13 function paragraphs.** The [coverage audit](fly-benchmark/review-inventory.json) reports annotation actions, prediction assessments and supporting artifacts separately. An UNC/UNDECIDED assessment records an evidence limitation, rather than an unexamined claim. The cases below illustrate supported predictions and different failure mechanisms; they are not a separate benchmark sample.

| Target | Current finding | Decisive evidence |
|---|---|---|
| <gene species="DROME" symbol="Lcp3">Lcp3</gene>, A0A0B4KEF3 | The cuticle core is supported; the full sentence has an incorrect spider attribution (NPI). The “rigid” qualifier remains UNC. | The current target is identical to reviewed fly Lcp3 P07188 (112/112 aa). Its recorded function TMalign donor, spider cuticle protein P80519, carries the matching sentence. The separate predicted Lcp4 name is also incorrect. |
| <gene species="DROME" symbol="ftz-f1">ftz-f1</gene>, M9NFK2 | Transcriptional regulation is supported; high-affinity thyroid-hormone receptor specificity is PLI. | The target is identical to FTZ-F1 P33244-2 (803/803 aa). The recorded function phmmer match is flounder thyroid receptor Q91279, whose paragraph matches the prediction. FTZ-F1 experiments support a different regulatory mechanism; phospholipid binding is documented and must not be conflated with thyroid specificity. |
| <gene species="DROME" symbol="Ank2">Ank2</gene>, Q3KN55 | Toxin activity is NPI. Exocytosis and extracellular localization remain UNC for the exact short product. | FlyBase confirms native Ank2-PE, 697 aa. The toxin claim points to alpha-latrocrustotoxin Q9XZC0, whose experimentally resolved membrane-insertion architecture is not supplied by shared ankyrin repeats. Giant-Ank2 synaptic findings cannot be assumed to characterize the short isoform. |
| <gene species="DROME" symbol="CG43124">CG43124</gene>, A0A0B4K7P3 | Serine-type endopeptidase activity is NPI: pseudoenzyme overannotation. | A supported PF00089 alignment maps catalytic His/Asp to Ser69/Asn112, agreeing with current NOT annotations. Active references recover an intact triad. The third catalytic site is not confidently mapped; extracellular/immune function is evaluated separately. |
| <gene species="DROME" symbol="CG4793">CG4793</gene>, Q8IP30 | Serine-type endopeptidase activity is NPI: pseudoenzyme overannotation. | The exact 910-aa sequence matches RefSeq NP_723941.2. Two active-trypsin comparisons map the catalytic serine to Gly290. Cellular-immunity experiments support a regulatory role despite catalytic inactivity; they do not establish an intrinsic protease reaction. |
| <gene species="DROME" symbol="CG34171">CG34171</gene>, X2JEK1 | Serine-type endopeptidase activity is NPI for the native short product. | The 176-aa PC isoform lacks the catalytic-serine-bearing C-terminal region. Its 292-aa PB counterpart retains that region but has Phe222 at the serine position. Those are distinct defects; the long isoform's substitution must not be assigned to a position absent from the short one. |
| <gene species="DROME" symbol="metro">metro</gene>, A1Z8G0 | Cell-junction localization is LSP; electronic kinase/transferase annotations are rejected. | The full Metro paper directly places the scaffold at the subsynaptic reticulum. Two alignment strategies map the exact GUK domain to experimentally characterized nucleotide-pocket substitutions, with active enzyme and MAGUK controls. A correct ProtNLM localization coexists with incorrect electronic catalytic annotations. |
| <gene species="DROME" symbol="Pld">Pld</gene>, A4UZ54 | Lipid catabolism is CNN; cytoplasm is LSP. | Direct fly phospholipase activity establishes the predicted lipid breakdown, and embryo imaging shows cytoplasm and cytoplasmic vesicles. A different GO identifier does not make established phosphatidylcholine hydrolysis a novel function. |
| <gene species="DROME" symbol="CG33116">CG33116</gene>, Q9VIU4 | All three broad predictions are LSP; Golgi IBA localization is rejected. | The primary study explicitly localizes CG33116/dCCS1 to ER while placing other family members in Golgi. The conserved phosphatidylethanolamine-synthesis assignment is separated from ceramide phosphoethanolamine synthesis measured for CG4585. |
| <gene species="DROME" symbol="CG5611">CG5611</gene>, Q9VB17 | The tentative fatty-acid oxidation sentence is UNC. | The native protein has a crotonase-family domain, but neither a diagnostic substrate-specific subfamily nor a target reaction is established. The source donor carries the same qualified statement; the evidence does not refute it. |
| <gene species="DROME" symbol="Nepl19">Nepl19</gene>, Q9VAS1 | Metalloendopeptidase activity is NPI: pseudoenzyme overannotation. | Two sequence alignments map a zinc-binding histidine and catalytic glutamate to Q511/Q512, while an active mouse neprilysin control preserves the catalytic sites. The conclusion concerns conventional M13 proteolysis; the native noncatalytic role remains unknown. |
| <gene species="DROME" symbol="TyrRS">TyrRS</gene>, Q9VV60 | Starvation response is supported and already known (CNN); resveratrol binding remains UNC. | The primary fly study directly observes TyrRS secretion after serum deprivation with controls for cell lysis. Its cell-competition experiments also establish an extracellular chemoattractant mechanism. The broad response term does not require TyrRS to be a starvation sensor. |
| <gene species="DROME" symbol="Gfat1">Gfat1</gene>, A8Y5A1; <gene species="DROME" symbol="Hn">Hn</gene>, E8NH57 | Complete catalytic reactions are refuted for the selected short native products. | Gfat1-PF lacks the glutaminase nucleophile and most of its domain; Hn-PD lacks substrate/pterin-binding architecture despite retaining iron ligands. In contrast, <gene species="DROME" symbol="ttv">ttv</gene>'s retained glycosyltransferase domain leaves broad activity unresolved. Short length alone is not the criterion. |
| <gene species="DROME" symbol="loqs">loqs</gene>, X2J5X6 | Small-RNA processing is supported; the literal mammalian complex and Dicer allocation are incorrect. | Fly experiments distinguish Dcr-1/Loqs/AGO1 miRNA processing from Dcr-2/Loqs-PD siRNA production. The PF target retains PB-like processing domains. Processing participation does not establish an absolute requirement for RISC assembly. |

The matching donor descriptions are attribution evidence, not a reconstruction of ProtNLM's internal reasoning or training history. The biological judgments also use verified target identity, primary experiments and domain/isoform context. Detailed sources, original predictions, caveats and fly-focused research records are available in the linked gene reviews. Assessment counts describe this released cohort. They do not estimate proteome-wide accuracy, and mixed function paragraphs are evaluated separately from GO claims.

## First investigations

The initial review group comprises **Ank2, Lcp3 and ftz-f1**. Their claims expose three distinct questions: an extracellular toxin assignment to a particular ankyrin isoform, explicit spider context in a fly cuticle description, and thyroid-hormone receptor specificity assigned to FTZ-F1. These are prompts for evidence tracing, not preassigned error categories.

The serine-protease group comprises **CG43124, CG4793 and CG34171**. All three positive ProtNLM activity claims conflict with current **NOT GO:0004252** annotations. The [Cao and Jiang sequence study](https://pubmed.ncbi.nlm.nih.gov/30367934/) provides the family-level catalytic-triad classification underlying IKR curation; the gene reviews independently check the exact current target sequences. They distinguish supported substitutions from absent or poorly aligned sequence. Catalytic inactivity does not by itself refute participation in proteolysis through a regulatory role. A GO-ID match across opposite annotation polarities is not agreement or a correct-but-not-novel prediction.

Other informative questions include fly-specific RNA-silencing partners for **loqs**, resveratrol binding for **TyrRS**, substrate specificity for **Dic4**, and the distinction between a short gene product and full-length enzyme function for **Gfat1, Hn and ttv**. **awd** and **CycA** provide candidates for examining well-grounded conserved functions alongside the challenge cases.

## Review queue

The focus column preserves the original review question. Names link to the gene reviews, which contain the current assessments and evidence.

| Priority | Gene | Exact prediction accession | GO | Function text | Review focus |
|---|---|---|---:|---:|---|
| 1 | <gene species="DROME" symbol="Ank2">Ank2</gene> | [Q3KN55](https://rest.uniprot.org/uniprotkb/protnlm/Q3KN55) | 3 | 0 | Resolve toxin/extracellular claims and exocytosis for the exact short isoform |
| 2 | <gene species="DROME" symbol="Lcp3">Lcp3</gene> | [A0A0B4KEF3](https://rest.uniprot.org/uniprotkb/protnlm/A0A0B4KEF3) | 0 | 1 | Separate cuticle function from the explicit spider taxon and inspect donor provenance |
| 3 | <gene species="DROME" symbol="ftz-f1">ftz-f1</gene> | [M9NFK2](https://rest.uniprot.org/uniprotkb/protnlm/M9NFK2) | 0 | 1 | Separate transcriptional regulation from thyroid-hormone receptor specificity |
| 4 | <gene species="DROME" symbol="CG43124">CG43124</gene> | [A0A0B4K7P3](https://rest.uniprot.org/uniprotkb/protnlm/A0A0B4K7P3) | 1 | 0 | Test intrinsic serine-protease activity using catalytic residues and family placement |
| 5 | <gene species="DROME" symbol="CG4793">CG4793</gene> | [Q8IP30](https://rest.uniprot.org/uniprotkb/protnlm/Q8IP30) | 1 | 0 | Test intrinsic serine-protease activity in an SPH-labeled protein |
| 6 | <gene species="DROME" symbol="CG34171">CG34171</gene> | [X2JEK1](https://rest.uniprot.org/uniprotkb/protnlm/X2JEK1) | 1 | 0 | Test serine-protease activity for this 176-aa model and its catalytic-site coverage |
| 7 | <gene species="DROME" symbol="loqs">loqs</gene> | [X2J5X6](https://rest.uniprot.org/uniprotkb/protnlm/X2J5X6) | 1 | 1 | Resolve fly Dicer/Argonaute partners and isoform-dependent miRNA versus siRNA roles |
| 8 | <gene species="DROME" symbol="TyrRS">TyrRS</gene> | [Q9VV60](https://rest.uniprot.org/uniprotkb/protnlm/Q9VV60) | 2 | 1 | Separate aminoacylation from resveratrol binding and starvation-response transfer |
| 9 | <gene species="DROME" symbol="CG33453">CG33453</gene> | [A0A0B4LFV5](https://rest.uniprot.org/uniprotkb/protnlm/A0A0B4LFV5) | 2 | 0 | Test ganglioside catabolism in fly and identify the proposed enzyme-activation mechanism |
| 10 | <gene species="DROME" symbol="Gfat1">Gfat1</gene> | [A8Y5A1](https://rest.uniprot.org/uniprotkb/protnlm/A8Y5A1) | 0 | 1 | Verify catalytic-domain coverage of the 434-aa model before transferring the full reaction |
| 11 | <gene species="DROME" symbol="Hn">Hn</gene> | [E8NH57](https://rest.uniprot.org/uniprotkb/protnlm/E8NH57) | 2 | 0 | Verify catalytic-domain coverage and substrate class for the 178-aa model |
| 12 | <gene species="DROME" symbol="ttv">ttv</gene> | [D5SHU8](https://rest.uniprot.org/uniprotkb/protnlm/D5SHU8) | 1 | 0 | Separate generic glycosyltransferase activity from full-length EXT-family functions |
| 13 | <gene species="DROME" symbol="CSN5">CSN5</gene> | [A0A0B4KHM2](https://rest.uniprot.org/uniprotkb/protnlm/A0A0B4KHM2) | 1 | 0 | Test synaptic-vesicle residence versus indirect effects of COP9 signalosome regulation |
| 14 | <gene species="DROME" symbol="Dic4">Dic4</gene> | [Q9VVS1](https://rest.uniprot.org/uniprotkb/protnlm/Q9VVS1) | 0 | 1 | Distinguish dicarboxylate-carrier family membership from thiamine-pyrophosphate substrate specificity |
| 15 | <gene species="DROME" symbol="qkr58E-1">qkr58E-1</gene> | [Q9W255](https://rest.uniprot.org/uniprotkb/protnlm/Q9W255) | 2 | 1 | Test the specific splice-site recognition narrative against fly RNA-binding evidence |
| 16 | <gene species="DROME" symbol="CG5565">CG5565</gene> | [Q9VQ04](https://rest.uniprot.org/uniprotkb/protnlm/Q9VQ04) | 0 | 1 | Verify the stated in-vitro substrate reaction without inferring an in-vivo pathway |
| 17 | <gene species="DROME" symbol="awd">awd</gene> | [A0A0B4LHX6](https://rest.uniprot.org/uniprotkb/protnlm/A0A0B4LHX6) | 0 | 1 | Check conserved phosphotransfer chemistry as a supported comparison candidate |
| 18 | <gene species="DROME" symbol="CycA">CycA</gene> | [M9NFR3](https://rest.uniprot.org/uniprotkb/protnlm/M9NFR3) | 2 | 1 | Evaluate CDK regulation and cell-cycle transition as a supported comparison candidate |
| 19 | <gene species="DROME" symbol="metro">metro</gene> | [A1Z8G0](https://rest.uniprot.org/uniprotkb/protnlm/A1Z8G0) | 1 | 0 | Evaluate junctional localization and the exact protein model |
| 20 | <gene species="DROME" symbol="Pld">Pld</gene> | [A4UZ54](https://rest.uniprot.org/uniprotkb/protnlm/A4UZ54) | 2 | 0 | Separate lipid catabolism from cytoplasmic versus membrane-associated localization |
| 21 | <gene species="DROME" symbol="sns">sns</gene> | [Q0E9F2](https://rest.uniprot.org/uniprotkb/protnlm/Q0E9F2) | 3 | 0 | Connect differentiation and morphogenesis to the demonstrated cell-surface mechanism |
| 22 | <gene species="DROME" symbol="CG31099">CG31099</gene> | [Q8IMT2](https://rest.uniprot.org/uniprotkb/protnlm/Q8IMT2) | 1 | 0 | Distinguish phosphorylation participation from intrinsic catalytic activity |
| 23 | <gene species="DROME" symbol="orb">orb</gene> | [Q8IMZ2](https://rest.uniprot.org/uniprotkb/protnlm/Q8IMZ2) | 1 | 0 | Evaluate translation-regulator specificity and isoform coverage |
| 24 | <gene species="DROME" symbol="CG31606">CG31606</gene> | [Q8IPG8](https://rest.uniprot.org/uniprotkb/protnlm/Q8IPG8) | 4 | 0 | Separate lipid binding/transport from extracellular localization and lipoprotein metabolism |
| 25 | <gene species="DROME" symbol="Mst27D">Mst27D</gene> | [Q8IPI4](https://rest.uniprot.org/uniprotkb/protnlm/Q8IPI4) | 1 | 0 | Evaluate microtubule binding and target-specific evidence |
| 26 | <gene species="DROME" symbol="CG32706">CG32706</gene> | [Q8IRM9](https://rest.uniprot.org/uniprotkb/protnlm/Q8IRM9) | 0 | 1 | Test transfer of SSU-processome and named rRNA cleavage-site functions |
| 27 | <gene species="DROME" symbol="betaTub97EF">betaTub97EF</gene> | [Q8MST5](https://rest.uniprot.org/uniprotkb/protnlm/Q8MST5) | 1 | 0 | Check broad microtubule function against more specific fly annotations |
| 28 | <gene species="DROME" symbol="IKKepsilon">IKKepsilon</gene> | [Q9V3Y8](https://rest.uniprot.org/uniprotkb/protnlm/Q9V3Y8) | 1 | 0 | Check protein phosphorylation against the specific kinase mechanism |
| 29 | <gene species="DROME" symbol="dati">dati</gene> | [Q9V4C9](https://rest.uniprot.org/uniprotkb/protnlm/Q9V4C9) | 2 | 1 | Distinguish transcription activation from generic transcriptional involvement |
| 30 | <gene species="DROME" symbol="Nepl19">Nepl19</gene> | [Q9VAS1](https://rest.uniprot.org/uniprotkb/protnlm/Q9VAS1) | 1 | 0 | Verify metallopeptidase catalytic competence and subfamily placement |
| 31 | <gene species="DROME" symbol="CG5611">CG5611</gene> | [Q9VB17](https://rest.uniprot.org/uniprotkb/protnlm/Q9VB17) | 0 | 1 | Resolve the vague fatty-acid oxidation statement and its proposed mechanism |
| 32 | <gene species="DROME" symbol="cdm">cdm</gene> | [Q9VEC5](https://rest.uniprot.org/uniprotkb/protnlm/Q9VEC5) | 2 | 0 | Evaluate nuclear transport specificity versus general intracellular transport |
| 33 | <gene species="DROME" symbol="Hmt-1">Hmt-1</gene> | [Q9VF20](https://rest.uniprot.org/uniprotkb/protnlm/Q9VF20) | 1 | 0 | Evaluate generic ABC-transporter activity against substrate-specific evidence |
| 34 | <gene species="DROME" symbol="CG33116">CG33116</gene> | [Q9VIU4](https://rest.uniprot.org/uniprotkb/protnlm/Q9VIU4) | 3 | 0 | Connect phosphotransfer chemistry to membrane localization and phospholipid synthesis |
| 35 | <gene species="DROME" symbol="RluA-1">RluA-1</gene> | [Q9VKV0](https://rest.uniprot.org/uniprotkb/protnlm/Q9VKV0) | 1 | 0 | Evaluate pseudouridine synthesis and substrate specificity |
| 36 | <gene species="DROME" symbol="CG3515">CG3515</gene> | [Q9VQD1](https://rest.uniprot.org/uniprotkb/protnlm/Q9VQD1) | 1 | 0 | Test nuclear localization using target-specific evidence |
| 37 | <gene species="DROME" symbol="msk">msk</gene> | [Q9VSD6](https://rest.uniprot.org/uniprotkb/protnlm/Q9VSD6) | 1 | 0 | Compare generic intracellular transport with the importin mechanism |
| 38 | <gene species="DROME" symbol="CG8915">CG8915</gene> | [Q9VX63](https://rest.uniprot.org/uniprotkb/protnlm/Q9VX63) | 1 | 0 | Evaluate broad nucleic-acid binding against substrate-specific evidence |
| 39 | <gene species="DROME" symbol="NtR">NtR</gene> | [Q9W288](https://rest.uniprot.org/uniprotkb/protnlm/Q9W288) | 1 | 0 | Verify ligand-gated ion-channel mechanism and ligand specificity |
| 40 | <gene species="DROME" symbol="jumu">jumu</gene> | [Q9XTP7](https://rest.uniprot.org/uniprotkb/protnlm/Q9XTP7) | 1 | 0 | Evaluate sequence-specific DNA binding and isoform applicability |
| 41 | <gene species="DROME" symbol="CG33090">CG33090</gene> | [X2JE45](https://rest.uniprot.org/uniprotkb/protnlm/X2JE45) | 1 | 0 | Verify glycoside-hydrolase catalytic competence and substrate scope |

## Evidence and identity checks

Use fly primary literature and FlyBase's curated evidence first, with comparative evidence where a function is demonstrably conserved. Deep research should focus on the fly gene. A paired human review is useful for a specific transfer question, rather than a required default for every fly gene.

Preserve the exact predicted accession and frozen sequence. Resolve the FlyBase protein/transcript when possible, and distinguish evidence on that product from experiments on a different isoform. A short annotated product is not automatically a broken model. Current UniProt sequences are not proven prediction-time inputs, so a discrepancy alone cannot establish a wrong-input-sequence error.

Separate biological support from annotation overlap. Exact GO overlap in the inventory uses ordinary UniProt cross-references and is descriptive only; the individual reviews use fetched GOA and trace their evidence. Agreement with an electronic assertion is not validation. Donor-match metadata can identify a plausible source of a transferred phrase, but does not alone prove how the model generated its output.

Review function paragraphs as individual biological claims without inventing GO mappings. A paragraph can combine a supported activity with an incorrect ligand, partner, organism or compartment. Record current assessments in the review files and curation provenance in the separate history mechanism.

See the [frozen data and reproduction instructions](fly-benchmark/README.md).
