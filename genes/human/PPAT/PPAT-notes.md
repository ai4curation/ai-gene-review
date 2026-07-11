# PPAT (human, Q06203) review notes

## Identity
- UniProt Q06203 (PUR1_HUMAN), gene PPAT (HGNC:9238). Synonym GPAT.
- Amidophosphoribosyltransferase (ATase); Glutamine phosphoribosylpyrophosphate amidotransferase (GPAT). EC 2.4.2.14.
- 517 aa precursor; residues 1-11 are a propeptide (PRO_0000029283) whose removal is required for activity; mature chain 12-517.

## Core biochemistry
- Catalyses the FIRST committed and rate-limiting step of de novo purine synthesis: transfer of the L-glutamine amide nitrogen to PRPP, giving 5-phospho-beta-D-ribosylamine (PRA) + L-glutamate + diphosphate.
  - UniProt CATALYTIC ACTIVITY (written right-to-left): "5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O" (RHEA:14905, EC 2.4.2.14); physiological direction right-to-left.
  - UniProt FUNCTION: "Catalyzes the formation of phosphoribosylamine from phosphoribosylpyrophosphate (PRPP) and glutamine."
- N-terminal glutamine amidotransferase type-2 domain (12-261); C-terminal PRTase (Pribosyltran/PF00156) domain. Active-site nucleophile Cys at position 12 (N-terminal nucleophile after propeptide removal).
- Cofactors: 1 Mg2+ per subunit; 1 [4Fe-4S] cluster per subunit (cluster ligands at 280, 426, 503, 506; by similarity to B. subtilis P00497). KW: 4Fe-4S, Iron, Iron-sulfur, Magnesium, Metal-binding, Allosteric enzyme.
- SUBUNIT: homotetramer (by similarity). Reactome: active form is a dimer that associates to a tetramer with sharply reduced activity.

## Regulation (allosteric / feedback)
- Feedback-inhibited by purine nucleotides (AMP, GMP, IMP).
- Reactome R-HSA-111285: "Cytosolic AMP, GMP, and IMP stimulate the association of phosphoribosyl pyrophosphate amidotransferase (PPAT) dimers to form tetramers" (inactive tetramer = feedback-inhibited state).
- Reactome R-HSA-111289: "PRPP stimulates the dissociation of ... tetramers to form dimers" (substrate activates by driving the active dimer form).
- Reactome R-HSA-73815 (the reaction): "This event is the committed step in de novo purine synthesis... pulled strongly in the direction of 5'-phosphoribosylamine synthesis by the irreversible hydrolysis of the pyrophosphate." Also notes PPAT is cytosolic (fluorescence microscopy, An et al. 2008) and an inferred iron-sulfur protein.

## Localization
- Cytosol. UniProt DR GO: GO:0005829 cytosol (TAS:Reactome). Reactome states "Cytosolic PPAT".

## Pathway placement
- UniProt PATHWAY: "Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2." UniPathway UPA00074, UER00124.
- Reactome R-HSA-73817 Purine ribonucleoside monophosphate biosynthesis.
- PRA is the entry metabolite feeding the entire de novo purine branch -> IMP -> AMP/GMP; hence IMP/purine-nucleotide biosynthesis annotations are directly downstream of this one catalytic step.

## GOA annotations (17-line TSV -> 16 annotation rows)
- GO:0004044 amidophosphoribosyltransferase activity: IBA (GO_REF:0000033), IEA (GO_REF:0000120, RHEA/EC), ISS (GO_REF:0000024 from rat P35433), TAS (PMID:8106516). Core MF. ACCEPT all (multiple evidence codes for same true MF are fine).
- GO:0006164 purine nucleotide biosynthetic process: IBA + TAS(PMID:8106516). Correct, general BP. ACCEPT.
- GO:0009113 purine nucleobase biosynthetic process: IEA InterPro. NOTE: PPAT makes the nucleoTIDE precursor PRA, not a free nucleobase; this InterPro2GO term is a slightly imprecise BP but points to purine biosynthesis. MODIFY -> de novo IMP biosynthetic process (GO:0006189) which is the accurate downstream process. (Not REMOVE: it is an IEA, but the branch is wrong-ish -- nucleobase vs nucleotide.)
- GO:0005515 protein binding x2 (IPI, PMID:28514442 and PMID:33961781, both vs NUDT5 Q9UKK9): bare protein binding from BioPlex/IntAct high-throughput AP-MS. Uninformative. Per policy: MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IPI). Full text of both papers does not name PPAT/NUDT5 (large-scale supplementary data).
- GO:0006177 GMP biosynthetic process (IEA Ensembl/ortholog): downstream; PPAT provides PRA upstream of GMP branch but does not itself act in GMP-specific steps. Over-propagated ortholog IEA. MARK_AS_OVER_ANNOTATED.
- GO:0006189 'de novo' IMP biosynthetic process (IEA UniProt/UniPathway): ACCEPT -- this is exactly the pathway PPAT's product feeds; the accurate de novo purine process.
- GO:0044208 'de novo' AMP biosynthetic process (IEA Ensembl): downstream AMP-specific branch. Over-propagated. MARK_AS_OVER_ANNOTATED.
- GO:0097294 'de novo' XMP biosynthetic process (IEA Ensembl): downstream XMP-specific branch. Over-propagated. MARK_AS_OVER_ANNOTATED.
- GO:0005829 cytosol x3 (TAS Reactome): ACCEPT (cytosolic; Reactome + UniProt).

Rationale for AMP/GMP/XMP as over-annotated rather than accepted: PPAT catalyses only the single committed step producing PRA. IMP is the first branch-point nucleotide of the de novo pathway; annotating PPAT to the AMP-, GMP-, and XMP-specific downstream branches (each requiring distinct dedicated enzymes) over-states its direct involvement. The de novo IMP process (GO:0006189) and the general purine nucleotide biosynthetic process (GO:0006164) correctly capture its role. Marked over-annotated (not removed) since they are automated ortholog transfers, not clearly-wrong mappings.

## No Mendelian disease
- No common Mendelian disorder attributed to PPAT; it is the committed regulatory entry point of the pathway. Pharos Tclin (drug target context: antimetabolites e.g. mercaptopurine/azathioprine act on this pathway).
