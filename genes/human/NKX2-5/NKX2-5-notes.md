# NKX2-5 (human, P52952) curation notes

## Provenance note

Automated deep research could not be run for this gene (falcon provider returned HTTP 402,
OpenAI provider returned HTTP 401). No `*-deep-research-<provider>.md` file was created.
These notes were assembled manually from the cached publications in `publications/`
(several are abstract-only; `full_text_available` checked per paper), the UniProt record
(`NKX2-5-uniprot.txt`) and PubMed searches used to locate three additional key mouse papers
(PMID:7628699, PMID:17350578, PMID:15085192), which were already cached.

## Identity and structure

- NK-2 class homeodomain transcription factor; vertebrate ortholog of Drosophila *tinman*.
  [PMID:8900537 "hCsx, the human homolog of Drosophila tinman, is expressed in heart in a tissue restricted manner"]
  [PMID:8900537 "The predicted amino acid sequence of hCsx has 87% overall homology to the murine gene with 100% identity in the homeodomain"]
- Homeodomain binds the NKE (TNAAGTG; TAAG core) element. Crystal structure of the HD on the
  NPPA/ANF -242 element: [PMID:22849347 "Tyr54, absolutely conserved in NK2 family proteins, mediates sequence-specific interaction with the TAAG motif"]
  and [PMID:22849347 "NKX2.5 homeodomains occupy both DNA binding sites separated by five nucleotides without physical interaction between themselves"].
  (Note: argues against a DNA-independent homodimer interface in the HD; UniProt still states "Homodimer".)
- Nuclear localization signal at the N-terminus of the homeodomain; CK2 phosphorylation of the HD
  (Ser163) increases DNA binding. [PMID:9858576 "the putative nuclear localization signal (NLS) of Csx/Nkx2.5 was identified by site-directed mutagenesis to the amino terminus of the homeodomain"]
- C-terminal autorepressive domain; GATA4 binding to it unmasks activation.
  [PMID:9312027 "binding of GATA-4 to the C-terminus autorepressive domain of Nkx2-5 may induce a conformational change that unmasks Nkx2-5 activation domains"]
- SUMOylated at K51 (PIAS1/PIASx/PIASy), which enhances activity.
  [PMID:18579533 "SUMO modification serves as a positive regulator for Nkx2.5 transcriptional activity"]

## Molecular function: sequence-specific RNA Pol II TF (activator > repressor)

- Activates NPPA/ANF through the NKE2 element. [PMID:10075728 "Deletion and mutational analyses of the ANP promoter revealed that the Csx/Nkx-2.5-binding element (NKE2) located at -240 was required for high level transactivation by Csx/Nkx-2.5"]
- Context-dependent repression: [PMID:10075728 "Csx/Nkx-2.5 reduced the GATA-4-induced transactivation of the GATA-4-dependent promoters"]
- Direct targets in human fetal cardiomyocytes: activates GATA4, represses CTNNB1 (beta-catenin)
  through promoter NKEs. [PMID:19479054 "the identified NKX2-5 binding sites were essential for the suppression of beta-catenin, and upregulation of GATA4 by NKX2-5"]
- Activates miR-143/145 enhancer together with SRF/MYOCD. [PMID:19578358 "miR-145 and miR-143 were direct transcriptional targets of serum response factor, myocardin and Nkx2-5"]
- Activates COL3A1 in pulmonary artery endothelial cells with NEDD9 (non-cardiac context).
  [PMID:29899023 "increased NEDD9 complex formation with Nk2 homeobox 5 (NKX2-5), and increased NKX2-5 binding to COL3A1"]
- Ectopically expressed in T-ALL, activating MEF2C. [PMID:18079734 "Knockdown and overexpression assays confirmed MEF2C activation by NKX2-5 at both the RNA and protein levels"]
- HT-SELEX (methyl-SELEX) profiling of human TFs includes NKX2-5 (PMID:28473536; NKX2-5 only in supplementary data).

## Partners (combinatorial cardiac TF code)

- GATA4: mutual cofactors, synergistic activation of ANF. [PMID:9312027 "The synergy involves physical Nkx2-5-GATA-4 interaction, seen in vitro and in vivo"]
- TBX5: binds Nppa in tandem; synergy; HD of NKX2-5 required. [PMID:11431700 "Tbx5 and Nkx2-5 directly bound to the promoter of the gene for cardiac-specific natriuretic peptide precursor type A (Nppa) in tandem, and both transcription factors showed synergistic activation"]
  Ternary structure: [PMID:26926761 "Here we report a crystal structure of human NKX2.5 and TBX5 DNA binding domains in a complex with a 19 bp target DNA"]
  Holt-Oram TBX5 mutants lose the interaction: [PMID:12499378 "All seven missense mutations greatly reduced the interaction of TBX5 with NKX2.5 in vivo and in vitro"]
- Coactivators: Cal/FBLIM1 [PMID:14757752 "Cal itself possessed the transcription-promoting activity, and cotransfection of Cal enhanced CSX/NKX2-5-induced activation of atrial natriuretic peptide gene promoter"]; CAMTA2 [PMID:16678093 "activates the ANF gene, at least in part, by associating with the cardiac homeodomain protein Nkx2-5"].
- MYOCD binds NKX2-5 but without functional synergy at ACTG2 [PMID:19797053 "no such functional relationship is evident with the related NKX2.5 transcription factor despite its interaction with MYOCD"].
- HuRI Y2H hits (SHOX, TRIP10, KRTAP8-1, RBPMS; PMID:32296183) - no functional follow-up.

## Biological roles

### Heart (core)
- Mouse null: heart tube forms, but looping fails and ventricular MLC2v is absent.
  [PMID:7628699 "looping morphogenesis, a critical determinant of heart form, was not initiated at the linear heart tube stage"]
  [PMID:7628699 "The data demonstrate that Nkx2-5 is essential for normal heart morphogenesis, myogenesis, and function"]
- Second heart field: [PMID:17350578 "feedback repression of Bmp2/Smad1 signaling by Nkx2-5 critically regulates SHF proliferation and outflow tract (OFT) morphology"]
- Conduction system: dosage-dependent; AV node primordium absent in nulls.
  [PMID:15085192 "the number of cells in the cardiac conduction system is directly related to Nkx2-5 gene dosage"]
  [PMID:15109497 "At birth, mutant mice display a hypoplastic atrioventricular (AV) node and then develop selective dropout of these conduction cells"]
- Adult myocyte survival: [PMID:11889119 "Csx/Nkx2-5 plays a critical role in maintaining highly differentiated cardiac phenotype"]
- Cardiomyocyte differentiation with TBX5 in P19CL6 cells (PMID:11431700).

### Human disease (heterozygous, dosage-sensitive)
- ASD with AV block: [PMID:9651244 "These data indicate that NKX2-5 is important for regulation of septation during cardiac morphogenesis and for maturation and maintenance of atrioventricular node function throughout life"]
- Broader CHD spectrum: [PMID:10587520 "Associated phenotypes included AV block, which was the primary manifestation of cardiac disease in nearly a quarter of affected individuals, as well as atrial septal defect and ventricular septal defect"]; TOF/DORV, Ebstein.
- Disease mutants lose DNA binding/transactivation: [PMID:10948187 "Electrophoretic mobility shift assay showed that Csx/Nkx-2.5-binding sequences were bound strongly by WT and C, weakly by B, but not by A"]

### Non-cardiac
- Spleen: [PMID:22560297 "This study establishes that a Pbx/Nkx2-5/p15 regulatory module is essential for spleen development"]; human isolated congenital asplenia P236H.
- Thyroid: [PMID:16418214 "Our results indicate that Nkx2-5(-/-) embryos exhibit thyroid bud hypoplasia, providing evidence that NKX2-5 plays a role in thyroid organogenesis"]
- Overexpression in C2C12 myoblasts blocks myotube formation and induces neuron-like cells (PMID:15653675) - ectopic, not physiological.

## Curation judgements (summary)

- Core: GO:0000981 / GO:0000978 / GO:0045944 / nucleus-chromatin; GATA4/TBX5 binding as
  GO:0061629; heart looping, cardiac muscle cell differentiation, AV node/conduction system
  development, atrial/ventricular septum morphogenesis.
- Non-core: spleen, thyroid, pharyngeal, adult heart maintenance, anti-apoptotic, Wnt repression.
- Over-annotated: sodium ion transport, heart contraction, cardiac muscle contraction,
  hemopoiesis, vasculogenesis, neuron differentiation, myotube differentiation, cytoplasm,
  homodimerization.
- protein binding (GO:0005515): GATA4/TBX5 -> MODIFY to GO:0061629; Cal/FBLIM1 -> GO:0001223;
  PIAS1, MYOCD, NEDD9 and HuRI Y2H rows -> REMOVE (uninformative).
