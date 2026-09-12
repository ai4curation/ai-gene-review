# LRP10 reference-review notes

## Scope and evidence hierarchy

This reference pass reviewed the four seeded GO_REF records, both seeded PubMed
records, five decisive cached primary papers, and the current reviewed UniProt
record. Direct human APP-sorting and endogenous brain-cell localization studies
receive the greatest weight. Mouse beta-VLDL uptake supports a narrow ortholog
inference; HuRI interactions remain screen observations; and disease-associated
variants or stressed overexpression models are not treated as definitions of
normal core function.

## Record, topology, family, isoform, and structure boundaries

Human LRP10 is UniProtKB Q7Z4F1, a reviewed 713-residue precursor
[file:human/LRP10/LRP10-uniprot.txt, "ID   LRP10_HUMAN             Reviewed;         713 AA."].
The record places the signal peptide at residues 1-16, the extracellular region
at 17-440, the transmembrane helix at 441-461, and the cytoplasmic tail at
462-713 [file:human/LRP10/LRP10-uniprot.txt, "FT   TRANSMEM        441..461"].
Domain resources record two CUB domains and four LDLRA repeats
[file:human/LRP10/LRP10-uniprot.txt, "DR   SMART; SM00042; CUB; 2.";
"DR   SMART; SM00192; LDLa; 4."].

The exact PANTHER assignment is PTHR24270:SF17
[file:human/LRP10/LRP10-uniprot.txt, "DR   PANTHER; PTHR24270:SF17; LOW-DENSITY LIPOPROTEIN RECEPTOR-RELATED PROTEIN 10; 1."].
The reviewed member boundary used here is narrow—human Q7Z4F1 and mouse Q7TQH7—
whereas parent PTHR24270 is a broad LDL-receptor-related family. Parent-family
properties therefore should not be transferred as though every LDLR paralog had
LRP10 substrate specificity.

UniProt isoform 2 lacks residues 557-713
[file:human/LRP10/LRP10-uniprot.txt, "FT                   /note=\"Missing (in isoform 2)\""].
This deletes much of the long cytoplasmic tail, but no reviewed source here
demonstrates an isoform-2-specific localization or function. Disease-associated
splice products must not be conflated with this normal alternative product.
The record has an AlphaFoldDB cross-reference
[file:human/LRP10/LRP10-uniprot.txt, "DR   AlphaFoldDB; Q7Z4F1; -."], but no
experimental PDB cross-reference. Structural claims are consequently domain-
and prediction-level, not experimentally solved full-length structures.

## Direct APP cargo-sorting mechanism

The strongest direct human functional study identifies APP as an LRP10 cargo.
Biochemical mapping concluded that "LRP10 interacts directly and predominantly with the ectodomain of APP in vitro." [PMID:22734645]. In cultured cells, surface
LRP10 is internalized into early endosomes and returned to the Golgi: "After rapid internalization in early endosomes, LRP10 is recycled back to the Golgi, a step that requires the DXXLL motifs in the cytoplasmic tail of LRP10 ."
[PMID:22734645]. These results support a type-I cargo/sorting receptor whose
cytoplasmic tail controls itinerary; they do not imply an enzyme activity.

In human SH-SY5Y neuroblastoma cells, increased LRP10 retained mature APP in the
Golgi and reduced its surface abundance and Aβ processing, while depletion
increased Aβ production [PMID:22734645, "knockdown of LRP10 expression
increases Aβ production."]. These are direct cultured-cell findings, but the
paper's Alzheimer-disease interpretation should not be generalized into a
universal in-vivo disease mechanism.

## Lipoprotein evidence is mouse and beta-VLDL-specific

PMID:11123907 characterized the mouse ortholog under the historical name LRP9;
the abstract explicitly says it arose from "a mouse lymphocyte cDNA library."
The functional assay found that "Apolipoprotein E (apoE)-enriched beta-VLDL stimulated cellular
cholesteryl ester formation in ldl-A7/LRP9."
[PMID:11123907]. This supports ortholog transfer of very-low-density-lipoprotein
particle receptor activity, not direct human Q7Z4F1 activity and not blanket
LDL-particle receptor activity.

## Endogenous human brain localization and SORL1

The strongest localization study used post-mortem human brain and control
iPSC-derived cells with knockout-validated antibodies. It reports that LRP10 is
mainly expressed in astrocytes and neurovasculature and was undetectable in the
examined neurons; iPSC-derived astrocytes likewise expressed LRP10 whereas the
examined iPSC-derived neurons did not [PMID:33913039, "LRP10 is highly
expressed in iPSC-derived astrocytes but cannot be observed in iPSC-derived
neurons."]. In astrocytes, LRP10 was found at the TGN, plasma membrane,
retromer, and early endosomes and "partially
co-localises and interacts with sortilin-related receptor 1 (SORL1)." [PMID:33913039]. This directly supports a
non-neuronal vesicle-trafficking context and SORL1 association, without proving
a constitutive binary complex in every cell type.

## Interaction-screen and membrane-proteomics boundaries

The HuRI paper constructed a proteome-scale binary interaction map using nine
screens and "pairwise verification by quadruplicate retesting and sequence confirmation" [PMID:32296183]. The 21 LRP10 partners in GOA/IntAct are valid
screen observations, but their diversity and lack of targeted physiological
validation prevent a shared mechanistic function or native complex from being
assigned. Generic protein binding is therefore non-core.

PMID:19946888 is a membrane-proteome survey of the human NK-like YTS cell line
[PMID:19946888, "The present study was initiated to define the composition of the membrane"]. Its cached abstract does not name LRP10 or expose the protein/
peptide table. The seeded HDA membrane assignment is retained with curator
deference, but the source cannot independently establish a more specific
compartment from the accessible record.

## Disease and model boundaries

The 2018 genetics paper found rare variants across familial Parkinson disease,
Parkinson disease dementia, and dementia with Lewy bodies. It explicitly calls
the segregation support "independent-albeit limited-evidence" and reports
variant-specific effects on mRNA, protein stability, or localization
[PMID:29887161]. These results motivate loss-of-function hypotheses but do not
establish a core disease process or show that every LRP10 variant has the same
mechanism.

The 2024 study reports that wild-type LRP10 is secreted in extracellular
vesicles and can be internalized by clathrin-dependent endocytosis in its cell
and organoid systems [PMID:38315424, "Here, we demonstrate that
wild-type LRP10 is secreted via extracellular vesicles (EVs) and can be
internalised via clathrin-dependent endocytosis."]. It also links LRP10 overexpression and a
patient-derived splice product to changes in α-synuclein. The authors explicitly
identify "our model to study LRP10 and α-synuclein has important limitations, including overexpression, the use of non-neural cell lines, and the lack of the aging component of LBDs" [PMID:38315424]. These
are valuable disease-context mechanisms, not evidence that constitutive EV
secretion or α-synuclein regulation is the normal universal core function of
LRP10.

## Curation conclusions for later synthesis

- Treat APP/SORL1-associated cargo sorting across plasma membrane, early
  endosomes, retromer, and TGN as the directly supported human functional axis.
- Keep mouse LRP9 beta-VLDL uptake species- and cargo-specific.
- Do not turn HuRI screen partners into physiological complexes or specific
  functions without targeted evidence.
- Do not infer an isoform-2-specific function from the 557-713 deletion alone.
- Do not describe an experimental full-length structure; only AlphaFold and
  domain annotations are present.
- Keep disease association, Lewy-body localization, EV secretion, and
  α-synuclein effects bounded to the reported variants and experimental models.
