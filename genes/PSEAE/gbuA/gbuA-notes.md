# gbuA (PA1421, Q9I3S3) notes

Review of *Pseudomonas aeruginosa* PAO1 guanidinobutyrase for the PseudoCAP IBA-seed
project (worklist rank 33). No deep-research provider was available; these notes are
from UniProt, PubMed and the cached publications.

## Biology

- GbuA is a Mn2+-dependent ureohydrolase (arginase family, agmatinase subfamily;
  PANTHER PTHR11358:SF26) that hydrolyses 4-guanidinobutanoate to 4-aminobutanoate
  (GABA) and urea [file:PSEAE/gbuA/gbuA-uniprot.txt].
- Nakada and Itoh 2002 cloned gbuA by complementing the gbuA9005 mutant "defective in
  4-GB utilization"; a PA1421 knockout "did not grow on 4-GB and failed to form GBase";
  the purified enzyme "catalyzed the specific hydrolysis of 4-GB", and "No enzyme
  activity was detected with other guanidino compounds, including arginine, agmatine,
  3-guanidinopropionate, and guanidinoacetate" [PMID:12029055]. Mn2+ restored activity
  after EDTA [PMID:12029055]. Expression is induced by 4-GB through the LysR-type
  regulator GbuR [PMID:12029055].
- Lee et al. 2011 solved the GbuA crystal structure (with Mn2+) alongside GpuA, the
  paralogous guanidinopropionase, and showed active-site loop differences (Met161 of
  GbuA) behind their substrate specificity [PMID:21600989]. UniProt: homohexamer, two
  Mn2+ per subunit.
- Pathway. Jann et al. 1988 described the fourth arginine catabolic pathway of
  P. aeruginosa: D-arginine dehydrogenase gives 2-ketoarginine, "catabolized further
  to 4-guanidinobutyraldehyde, 4-guanidinobutyrate and 4-aminobutyrate", with
  guanidinobutyrase inducible by 2-ketoarginine and strongly by 4-guanidinobutyrate;
  "In mutants blocked in the L-arginine succinyltransferase pathway ... L-arginine was
  channelled partially into the D-arginine dehydrogenase pathway" [PMID:3141581].
  Later work showed that L-arginine enters this route via the AruH arginine:pyruvate
  transaminase and AruI 2-ketoarginine decarboxylase (the arginine transaminase
  pathway), and that in an aruF (AST-deficient) background "disruption of gbuA
  abolished growth on l-arginine" [PMID:17416670]. So GbuA is a genuine step of
  L-arginine (and D-arginine) catabolism in P. aeruginosa, downstream of 2-ketoarginine.

## PAINT node PTN004253691

From `.cache/paint/IBD.gaf` and the PAINT leaf GAF. IBDs at PTN004253691:
GO:0047971 guanidinobutyrase (seeds human AGMAT Q9BSE5, GbuA Q9I3S3), GO:0047972
guanidinopropionase (seeds Q9BSE5 and P. aeruginosa GpuA Q9I6K2), GO:0006527
L-arginine catabolic process (sole seed GbuA), and NOTs for agmatinase activity
(GO:0008783) and putrescine biosynthesis from arginine (GO:0009446). The 34 leaves
are vertebrate and invertebrate AGMAT orthologs ("guanidino acid hydrolase,
mitochondrial" in human, mouse and rat), *P. aeruginosa* GbuA and GpuA.

- The clade is a guanidino-acid hydrolase clade. Human AGMAT "efficiently hydrolyzed
  linear guanidino acids such as TC and GBA, whereas GPA and arginine were turned over
  less efficiently and guanidinoacetate or compounds lacking acidic residues such as
  agmatine were not accepted as substrates" [PMID:36543883].
- Every leaf receives both guanidinobutyrase and guanidinopropionase IBAs. For GbuA the
  guanidinopropionase IBA is directly contradicted: no activity with
  3-guanidinopropionate [PMID:12029055].
- L-arginine catabolic process is right for GbuA, but the node propagates it to GpuA
  (which has no activity on arginine and serves 3-guanidinopropionate utilisation) and
  to the vertebrate guanidino acid hydrolases, which metabolise arginine only poorly
  and whose physiological substrates (taurocyamine, 4-GB) are not arginine
  catabolites in the sense of a catabolic pathway. The node term over-reaches for the
  clade; it would sit better on a GbuA-only (bacterial guanidinobutyrase) subnode.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN004253691 | GO:0047971 guanidinobutyrase activity | 2 | 34 (24 taxa) | GO:0047971, IDA, PMID:3141581 (PseudoCAP) | SOUND | Guanidinobutyrase activity was assayed in P. aeruginosa extracts and is attributable to GbuA (the gbuA knockout lacks GBase, PMID:12029055). Independently backed by the UniProt EXP rows and the human AGMAT seed. |
| PTN004253691 | GO:0006527 L-arginine catabolic process | 1 (sole seed) | 34 (24 taxa) | GO:0006527, IDA, PMID:3141581 (PseudoCAP) | SOUND | The 1988 paper places guanidinobutyrase in the fourth arginine catabolic pathway (D-arginine, and L-arginine when the AST pathway is blocked); gbuA disruption abolishes L-arginine growth in an aruF mutant (PMID:17416670). But the node term does not suit the clade: it propagates to GpuA (no arginine activity) and vertebrate guanidino acid hydrolases. Flagged to GO_CENTRAL. |

Also: the GO:0047972 guanidinopropionase IBD at the same node (not PseudoCAP-seeded)
reaches GbuA, which has no guanidinopropionase activity; REMOVE on this gene and a
GO_CENTRAL MISSING_NEGATION defect.

## Decisions summary

- ACCEPT: guanidinobutyrase activity (EXP x2, IBA, IDA, IEA), L-arginine catabolic
  process (IBA, IDA).
- MODIFY: GO:0016813 amidine hydrolase activity to GO:0047971; metal ion binding to
  manganese ion binding (GO:0030145).
- REMOVE: guanidinopropionase activity (IBA), contradicted by direct assay.
- Source defects: GO_CENTRAL MISSING_NEGATION (NOT GO:0047972 at GbuA leaf, PROBABLE);
  GO_CENTRAL MISSING_NEGATION CHECK for the L-arginine catabolic process IBD on GpuA
  and vertebrate AGMAT leaves (SUSPECTED).
