# MMACHC (Q9Y4U1) review notes

Human MMACHC = "Cyanocobalamin reductase / alkylcobalamin dealkylase" (a.k.a. CblC).
Cytosolic vitamin-B12 (cobalamin) processing chaperone/enzyme. HGNC:24525, chr1.
282 aa. Belongs to the MMACHC family; a divergent member of the NADPH-dependent flavin
reductase / nitroreductase fold family.

## Core biology (well established, multiple structural + biochemical papers)

MMACHC performs the FIRST intracellular tailoring step on incoming (dietary/circulating)
cobalamin, removing the upper axial (beta) ligand of cob(III)alamin to generate a common
cob(II)alamin intermediate that is then partitioned to the two downstream B12 enzymes:
- methylcobalamin (MeCbl) -> methionine synthase (MTR) cytosolic remethylation arm
- 5'-deoxyadenosylcobalamin (AdoCbl) -> methylmalonyl-CoA mutase (MMUT) mitochondrial arm

Two distinct chemistries on the same scaffold:
1. Reductive **decyanation** of cyanocobalamin (CNCbl, the dietary/supplement form):
   base-off, FAD/FMN + NADPH-dependent reductive cleavage of the Co-CN bond -> cob(II)alamin
   + cyanide. EC 1.16.1.6; GO:0033787 cyanocobalamin reductase (cyanide-eliminating) (NADP+).
   [PMID:18779575 "the trafficking chaperone, MMACHC, catalyzes a reductive decyanation reaction"]
   [PMID:19700356 "wild-type MMACHC is able to reductively decyanate CNCbl to cob(II)alamin
   requiring only the presence of NADPH and FAD"]
2. Glutathione-dependent **dealkylation** of alkylcobalamins (MeCbl, AdoCbl): thiolate of
   GSH performs nucleophilic displacement of the alkyl group -> cob(I)alamin + S-alkyl-glutathione.
   EC 2.5.1.151 (alkylcobalamin:glutathione S-alkyltransferase). GOA maps this to GO:0016765
   (transferase, alkyl/aryl other than methyl). There is NO dedicated GO MF for EC 2.5.1.151.
   [PMID:19801555 "catalyzes an entirely different chemical reaction with alkylcobalamins using
   the thiolate of glutathione for nucleophilic displacement to generate cob(I)alamin and the
   corresponding glutathione thioether"; "Biologically relevant thiols, e.g. cysteine and
   homocysteine, cannot substitute for glutathione"]
   [PMID:21697092 "CblC is the first example of an enzyme with glutathione transferase activity
   that has a sequence and structure unrelated to the GST superfamily"]

## Structure / mechanism
- Nitroreductase-like scaffold; uses FMN or FAD as prosthetic group. [PMID:21697092
  "CblC is the most divergent member of the NADPH-dependent flavin reductase family and can
  use FMN or FAD as a prosthetic group to catalyze reductive decyanation"]
- Binds Cbl "base-off" (dimethylbenzimidazole displaced). [PMID:19700356 "MMACHC binds CNCbl
  in the base-off form, with the dimethylbenzimidazole (DMB) base of cobalamin displaced"]
- Arginine-rich pocket binds GSH; domain-swapped homodimer (PNRRP loop exchange) triggered by
  FMN or AdoCbl binding; monomer without substrate. [PMID:22642810 "identified an arginine-rich
  pocket close to the Cbl binding site responsible for GSH binding and dealkylation activity";
  "two Cbl-binding monomers dimerize to mediate the reciprocal exchange of a conserved 'PNRRP'
  loop"; "dimerization is triggered upon binding its substrate adenosyl-Cbl or cofactor FMN"]

## Interactions
- MMADHC/CblD: heterodimer, partitions cofactor between MeCbl and AdoCbl routes.
  [PMID:23415655 "a complex between CblC and CblD can be isolated ... adapter function for CblD,
  which in complex with CblC.HOCbl ... partitions the cofactor between AdoCbl and MeCbl"]
- MTR (methionine synthase, Q99707) and MTRR: multiprotein cytosolic Cbl-processing complex.
  [PMID:27771510 "the processing of Cbl in cytoplasm occurs in a multiprotein complex composed
  of at least MS, MSR, MMACHC and MMADHC"]
  [PMID:23825108 "interaction of MS with MMACHC may play a role in the regulation of the cellular
  processing of Cbls"]
- Lysosomal exporters LMBD1 (LMBRD1, Q9NUN5) and ABCD4 (O14678): deliver Cbl from lysosome to
  cytosolic MMACHC. [PMID:25535791 "the cytoplasmic vitamin B(12)-processing protein MMACHC also
  interacts with LMBD1 and ABCD4 with low nanomolar affinity"]
- HuRI/BioPlex proteome-scale two-hybrid: CCT6B (Q92526) [PMID:33961781]. Non-functional
  scaffolding/chaperonin contact from high-throughput interactome; not a core function.

## Subcellular location
- Cytosolic. [PMID:23270877 "MMACHC is cytoplasmic while MMADHC is both mitochondrial and
  cytoplasmic"]. HPA reports a nucleoplasm IDA (GO:0005654) — likely antibody/localization
  signal but not supported by the well-established cytosolic biology; keep as non-core.

## Disease
cblC disease (MAHCC, MIM:277400): most common inborn error of intracellular cobalamin metabolism.
Combined methylmalonic aciduria AND homocystinuria because BOTH the AdoCbl (MMUT) and MeCbl (MTR)
arms lose cofactor. [PMID:18779575 "Defects in MMACHC represent the most common cause of inborn
errors of B(12) metabolism"] [PMID:19700356 "Patients with the cblC ... disorder are defective in
the intracellular synthesis of adenosylcobalamin and methylcobalamin and have combined
homocystinuria and methylmalonic aciduria"]. Pathogenic mutations (e.g. R161Q/G, G147D) impair
Cbl binding, stability, decyanation and/or dealkylation. [PMID:25809485 "R161Q and R161G CblC
mutants display lower protein stability and decreased dealkylation but not decyanation activity"]

## Curation reasoning summary
- CORE MF: GO:0033787 cyanocobalamin reductase (EXP/IDA, well supported) + GO:0016765 alkyl
  transferase (the GSH dealkylase, EXP) + GO:0031419 cobalamin binding (substrate binding; in
  UniProt DR but NOT in GOA) + GO:0071949 FAD binding (cofactor) + GO:0043295 glutathione binding.
- CORE BP: GO:0009235 cobalamin metabolic process. CORE CC: GO:0005829 cytosol.
- GO:0032451 demethylase activity / GO:0070988 demethylation: these are GO's mapping of the
  MeCbl dealkylation. Strictly MMACHC removes a methyl group FROM cobalamin (an S-alkyltransfer
  to glutathione), not classic substrate demethylation. The essence (removes methyl group) is
  sound but the terms are the wrong flavor; the alkyltransferase term (GO:0016765) is more
  accurate. Marking demethylase/demethylation as over-annotated (essence right, term imprecise).
- GO:0016491 oxidoreductase activity: correct but general parent of the reductase; keep as
  non-core (the specific GO:0033787 is the informative term).
- protein binding IPIs: MARK_AS_OVER_ANNOTATED per policy (uninformative; specific complex
  partners captured better). Do NOT REMOVE (experimental IPIs).
- Reactome TAS cytosol block (many R-HSA rows) + cobalamin metabolic process TAS: accept as
  location/process; keep cytosol duplicates as non-core to avoid redundancy inflation.

## DR status
Falcon deep-research file (MMACHC-deep-research-falcon.md) not present within the 8-min poll
window; review grounded in UniProt (Q9Y4U1), seeded GOA, cached PMID abstracts, and the dismech
disorder KB. No -deep-research-*.md fabricated.
