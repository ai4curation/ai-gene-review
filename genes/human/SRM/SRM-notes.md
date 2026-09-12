# SRM (Spermidine synthase) — review notes

UniProt: P19623 (SPEE_HUMAN). Gene: SRM (synonyms SPS1, SRML1). 302 aa. Chromosome 1.

## Core identity and function

SRM is human **spermidine synthase** (EC 2.5.1.16), also called **putrescine aminopropyltransferase**
[file:human/SRM/SRM-uniprot.txt "RecName: Full=Spermidine synthase"; "EC=2.5.1.16"; "AltName: Full=Putrescine aminopropyltransferase"].

It catalyzes the committed aminopropyl-transfer step of spermidine biosynthesis: it transfers an
aminopropyl group from **decarboxylated S-adenosylmethionine (dcSAM)** onto **putrescine**, producing
**spermidine** plus **5'-methylthioadenosine (MTA)**
[file:human/SRM/SRM-uniprot.txt "Catalyzes the production of spermidine from putrescine and"; "decarboxylated S-adenosylmethionine (dcSAM)"].

Catalytic reaction (UniProt / Rhea RHEA:12721):
`S-adenosyl 3-(methylsulfanyl)propylamine + putrescine = S-methyl-5'-thioadenosine + spermidine + H+`
[file:human/SRM/SRM-uniprot.txt "Reaction=S-adenosyl 3-(methylsulfanyl)propylamine + putrescine = S-"].

Substrate specificity: strong preference for putrescine as the amine acceptor; **very low** activity
toward spermidine and **very low** activity toward 1,3-diaminopropane
[file:human/SRM/SRM-uniprot.txt "Has a strong preference"; "for putrescine as substrate, and has very low activity towards 1,3-"; "Has extremely low activity towards spermidine."].
Aminopropyltransferases as a class "transfer aminopropyl groups from decarboxylated S-adenosylmethionine
to amine acceptors, forming polyamines" and human spermidine synthase "is highly specific for putrescine
as the amine acceptor" [PMID:17585781 "Aminopropyltransferases transfer aminopropyl groups from"; "S-adenosylmethionine to amine acceptors, forming polyamines"; "which is highly specific for putrescine as the amine acceptor"].

Kinetics (PubMed:17585781, quoted in UniProt): KM = 20 uM for putrescine; KM = 0.9 uM for
S-adenosylmethioninamine (dcSAM); kcat ~1.9 sec^-1
[file:human/SRM/SRM-uniprot.txt "KM=20 uM for putrescine"; "KM=0.9 uM for S-adenosylmethioninamine"].

Activity regulation: "thought to be regulated mainly by the availability of decarboxylated
S-adenosylmethionine" (i.e. by AMD1/SAMDC output)
[file:human/SRM/SRM-uniprot.txt "the availability of decarboxylated S-adenosylmethionine"].

## Pathway / metabolic context

Pathway assignment: "Amine and polyamine biosynthesis; spermidine biosynthesis; spermidine from
putrescine: step 1/1" — i.e. the single, dedicated enzymatic step producing spermidine from putrescine
[file:human/SRM/SRM-uniprot.txt "spermidine from putrescine: step 1/1"].
Reactome places SRM in "Metabolism of polyamines" (R-HSA-351202) and as the reaction "Putrescine +
dc-Adenosyl methionine => Spermidine + 5'-methylthioadenosine" (R-HSA-351215)
[reactome:R-HSA-351215 "Spermidine synthase (SRM) carries out the final step of spermidine biosynthesis,"].

## Structure / oligomeric state

Member of the **spermidine/spermine synthase (aminopropyltransferase) family**; PABS domain; SAM-dependent
methyltransferase-like (Rossmann) fold plus an N-terminal tetramerization domain
[file:human/SRM/SRM-uniprot.txt "Belongs to the spermidine/spermine synthase family."].
Solved by X-ray crystallography (PDB 2O05, 2O06, 2O07, 2O0L, 3RW9) in complexes with spermidine,
putrescine, MTA and S-adenosylmethioninamine; these structures established the catalytic mechanism and
the structural basis of putrescine specificity [PMID:17585781 "provide a"; "general mechanistic hypothesis for the aminopropyl transfer reaction. The"; "structural basis for the specificity of the spermidine"].
**Oligomeric state: homodimer or homotetramer** [file:human/SRM/SRM-uniprot.txt "Homodimer or homotetramer."].
Active-site proton acceptor at residue 173 (PROSITE) [file:human/SRM/SRM-uniprot.txt "Proton acceptor"].

## Localization

Cytosolic (GO:0005829). Supported by phylogenetic (IBA, GO_Central) and Reactome TAS annotations in GOA;
consistent with polyamine biosynthesis being a cytosolic pathway. UniProt lists no membrane/organelle
targeting features.

## Gene structure (historical)

The human SRM gene is on chromosome 1, comprises 8 exons / 7 introns, ~5.8 kb, GC-rich TATA-less promoter;
transient expression of the genomic clone restored spermidine synthase activity in CHO cells with low
endogenous activity — confirming it is a functional gene [PMID:2069720 "the gene comprised"; "of 5,818 nucleotides"; "revealed that the gene was"; "transiently expressed and hence in all likelihood represents a functional gene."].
This paper (TAS in GOA for GO:0004766) is essentially a gene-structure/chromosomal-localization paper; it
identifies SRM as spermidine synthase (EC 2.5.1.16) but does not itself provide direct enzyme-mechanism
data — the mechanistic/enzymological evidence comes from PMID:17585781.

## Protein interactions

UniProt INTERACTION section:
- P19623–P19623 (self, NbExp=6) — homodimer/homotetramer, consistent with GO:0042802 identical protein
  binding and GO:0042803 protein homodimerization activity [file:human/SRM/SRM-uniprot.txt "P19623; P19623: SRM; NbExp=6"].
- P19623–P54274 (TERF1, NbExp=2) [file:human/SRM/SRM-uniprot.txt "P19623; P54274: TERF1; NbExp=2"].

GOA IPI annotations:
- GO:0005515 protein binding, PMID:21044950 (WITH/FROM P54274 = TERF1). PMID:21044950 is a genome-wide YFP
  fluorescence-complementation screen for telomere-signaling regulators; the interaction captured here is
  the SRM–TERF1 pair. This is a bare "protein binding" IPI — uninformative about SRM's catalytic function;
  keep but mark as over-annotated (per policy, never REMOVE a protein-binding IPI). The functional
  significance of an SRM–TERF1 interaction is not established.
- GO:0042802 identical protein binding, PMID:17585781, PMID:29892012, PMID:31515488, PMID:32296183
  (all WITH/FROM P19623 = self). These correspond to detection of the SRM homodimer, either
  crystallographically (17585781) or via large-scale binary interactome / Y2H maps (HuRI reference map
  PMID:32296183; variant-interactome perturbation studies PMID:29892012, PMID:31515488). Biologically
  sound (SRM is a homodimer/homotetramer) but redundant across four references.

## Annotation-review reasoning summary

- **Core MF:** GO:0004766 spermidine synthase activity. Supported by direct enzyme assay + structures
  (IDA/EXP PMID:17585781), phylogeny (IBA), EC/Rhea (IEA), and TAS. ACCEPT all.
- **Core BP:** GO:0008295 spermidine biosynthetic process — the specific pathway. ACCEPT (IBA, IDA);
  IEA (UniPathway) redundant but ACCEPT.
- **Broader BP:** GO:0006596 polyamine biosynthetic process (parent) and GO:0006595 polyamine metabolic
  process (grandparent) are correct-but-more-general; KEEP_AS_NON_CORE (informative broader context, but
  GO:0008295 is the precise term).
- **GO:0003824 catalytic activity** (IEA, InterPro): trivially true root-ish MF, superseded by the
  specific GO:0004766 IEA from the same pipeline family; MARK_AS_OVER_ANNOTATED (uninformative).
- **CC:** GO:0005829 cytosol — ACCEPT (IBA + TAS).
- **Protein binding / homodimer:** GO:0042803 protein homodimerization activity (IDA, structure) — KEEP
  AS_NON_CORE (structural property, not the catalytic function, but well-supported). GO:0042802 identical
  protein binding IPI ×4 — MARK_AS_OVER_ANNOTATED (captures the same homodimer, redundant, not core).
  GO:0005515 protein binding IPI (TERF1) — MARK_AS_OVER_ANNOTATED (bare, uninformative).

## Term id verifications (OLS, GO)

- GO:0004766 spermidine synthase activity — verified (MF).
- GO:0008295 spermidine biosynthetic process — verified (BP).
- GO:0006596 polyamine biosynthetic process — verified (BP, parent).
- GO:0006595 polyamine metabolic process — verified (BP, grandparent).
- GO:0005829 cytosol — verified (CC).
- GO:0042803 protein homodimerization activity — verified (MF).
