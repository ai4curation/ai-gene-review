# aruC (PA0895, O30508) notes

Review of *Pseudomonas aeruginosa* PAO1 N2-succinylornithine / N2-acetylornithine
5-aminotransferase for the PseudoCAP IBA-seed project (worklist rank 32). No
deep-research provider was available; these notes are from UniProt, PubMed and the
cached publications.

## Biology

- AruC is a class-III PLP-dependent aminotransferase, ArgD subfamily (HAMAP
  MF_01107; NCBIfam TIGR03246 arg_catab_astC and TIGR00707 argD; PANTHER
  PTHR11986:SF113). UniProt: "Transaminates both N(2)-acetylornithine and
  N(2)-succinylornithine", with Km 1.4 mM for succinylornithine and 1.1 mM for
  acetylornithine (ECO:0000269, PMID:9393691) [file:PSEAE/aruC/aruC-uniprot.txt].
- Catabolic role. aruC is the first gene of the ArgR-controlled aruCFGDB operon of
  the arginine succinyltransferase (AST) pathway, "the major arginine and ornithine
  utilization (aru) pathway under aerobic conditions" [PMID:9393691]. It specifies
  "N2-succinylornithine 5-aminotransferase" [PMID:9393691]. Jann et al. 1986 defined
  the pathway (arginine -> succinylarginine -> succinylornithine -> succinylglutamate
  semialdehyde -> succinylglutamate -> succinate + glutamate) by enzyme assays and
  showed that purified N2-acetylornithine 5-aminotransferase "efficiently transaminated
  N(2)-succinylornithine; this explains the enzyme's dual role in arginine
  biosynthesis and catabolism" [PMID:16593724].
- Biosynthetic role. Voellmy and Leisinger purified ACOAT from PAO1, called it "the
  fourth enzyme of arginine biosynthesis", found it induced ~15-fold by arginine and
  catabolite-repressed, and concluded "this enzyme functions in the biosynthesis as
  well as in the catabolism of L-arginine" [PMID:238949]. It was the regulated
  enzyme "involved in both the biosynthesis and catabolism of arginine" [PMID:103997].
  The kinetic match (Km 1.1 mM for acetylornithine in both PMID:238949 and the UniProt
  entry) supports that the purified ACOAT is AruC. I found no genetic test (arginine
  auxotrophy of an aruC mutant) in the abstracts I could read. PAO1 also has PA0530
  (Q9I606, PTHR11986:SF79), an uncharacterised paralog in the same PAINT clade, so
  whether AruC is the only biosynthetic ACOAT in vivo is open.
- So both process annotations are reasonable: AruC catalyses the ACOAT step of
  arginine biosynthesis and the SOAT step (step 3/5) of the AST catabolic pathway.
  The catabolic role is the better established physiologically (operon, ArgR
  induction); the biosynthetic role rests on enzymology and the classical dual-role
  interpretation.

## PAINT nodes

From `.cache/paint/IBD.gaf` and the PAINT leaf GAF:

- PTN000241318 (ArgD/AstC clade, 37 leaves). IBDs: GO:0003992 (seeds E. coli ArgD
  P18335, Salmonella ArgD P40732, Synechocystis P73133, E. coli AstC P77581, and
  O30508), GO:0005829 (seed E. coli PatA P42588), GO:0006526 (sole seed O30508). A
  NOT for GO:0006526 and GO:0003992 is placed at PTN001736429, which removes the two
  PatA putrescine aminotransferase leaves. The remaining 35 leaves include
  biosynthetic ArgD proteins (most of the clade), the catabolic AstC succinylornithine
  transaminases of E. coli, Salmonella and Yersinia, two LysJ-type [LysW]-aminoadipate
  semialdehyde transaminases (Q9RW75 *Deinococcus*, A9WB46 *Chloroflexus*), a
  diaminobutyrate-pyruvate aminotransferase (Q93S10 SCO6279), and PA0530. The
  arginine biosynthesis IBD is a reasonable majority call for ArgD, but over-reaches
  for the LysJ and diaminobutyrate-aminotransferase leaves (names only; their
  functions were not checked experimentally here), and for AstC it is at best a
  secondary role.
- PTN000241033 (broader class-III aminotransferase node, 8 seeds incl. yeast and
  fission yeast ornithine aminotransferases, Arabidopsis, B. subtilis RocD, E. coli
  AstC and O30508). IBD GO:0006525 arginine metabolic process, with a NOT at
  PTN000241294. AruC supports it via both its biosynthesis and catabolism rows.
  O30508 itself does not carry this IBA (it receives the more specific terms).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000241318 | GO:0006526 L-arginine biosynthetic process | 1 (sole seed) | 35 (26 taxa) | GO:0006526 L-arginine biosynthetic process, IDA, PMID:16593724 (PseudoCAP) | SOUND | AruC catalyses the ACOAT step; the paper assays the purified biosynthetic ACOAT and states its dual biosynthetic/catabolic role, and PMID:238949 purified it as the fourth arginine biosynthetic enzyme. The paper's own focus is catabolism, so the biosynthetic claim leans on earlier work. Node term suits the ArgD majority of the clade but propagates to LysJ-type, diaminobutyrate-aminotransferase and AstC leaves; a PAINT check is suggested. |
| PTN000241318 | GO:0003992 N2-acetyl-L-ornithine:2-oxoglutarate 5-transaminase activity | 5 | 35 (26 taxa) | GO:0003992, IDA, PMID:16593724 (PseudoCAP) | SOUND | Purified enzyme assayed; ACOAT activity also in UniProt (ECO:0000269, PMID:9393691). Four independent seeds. |
| PTN000241033 | GO:0006525 arginine metabolic process | 8 | 33 (18 taxa) | GO:0006526 and GO:0006527, IDA, PMID:16593724 (PseudoCAP) | SOUND | AruC participates in both arginine biosynthesis and AST catabolism; seven other seeds (ornithine aminotransferases, AstC, RocD). |

The PseudoCAP L-arginine catabolic process row (IDA, PMID:16593724) is also sound;
it is the paper's central finding.

## Decisions summary

- ACCEPT: ACOAT activity (IBA, IDA, IEA), succinylornithine transaminase activity
  (IEA), L-arginine biosynthetic process (IBA, IDA, IEA), L-arginine catabolic process
  (IDA), cytoplasm (IEA), cytosol (IBA).
- MODIFY: transaminase activity (IEA) to GO:0043825 + GO:0003992; amino acid metabolic
  process and arginine metabolic process (IEA) to L-arginine catabolic + biosynthetic
  process.
- KEEP_AS_NON_CORE: pyridoxal phosphate binding (IEA).
- Source defect: GO_CENTRAL CHECK (SUSPECTED) on the PTN000241318 arginine
  biosynthesis IBD for LysJ-type and DABA-aminotransferase leaves.
