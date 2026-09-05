# LRP3 evidence notes

## Evidence inventory and identity

The reviewed human record is UniProtKB O75074, a 770-aa LRP3 precursor
[file:human/LRP3/LRP3-uniprot.txt "ID   LRP3_HUMAN              Reviewed;         770 AA."].
The cached record has no `ALTERNATIVE PRODUCTS` section, so this review has no
evidence for functionally distinct human isoforms. Isoform-specific claims should
not be inferred from transcript databases or sequence-accession cautions.

The primary cloning paper covers both human and rat cDNAs. Its architecture claim
is explicitly cross-species—[PMID:9693042 "and rat LRP3 cDNAs encode a 770-amino-acid type 1 membrane protein with the"]—whereas its tissue-expression
statement is explicitly human [PMID:9693042 "LRP3 transcript was detected in a wide range of"]. The differentiation work is human and uses immortalized human
bone-marrow stromal-cell clones; it is not evidence from primary tissue or an
animal model [PMID:28340487 "The goal of the current study was to unravel the
novel role of the low-density lipoprotein receptor-related protein 3 (LRP3) in
regulating the osteogenic and adipogenic differentiation of immortalized hBMSCs."].

## Stromal differentiation: direct phenotype, downstream scope

In the assayed immortalized human stromal-cell system, LRP3 expression was higher
in the more osteogenic clone and increased during osteogenic induction
[PMID:28340487 "Gene expression profiling revealed significantly higher LRP3 levels in the"]. Perturbation assays support a context-specific
role favoring osteoblast differentiation and opposing adipocyte differentiation
[PMID:28340487 "Data from functional and gene expression assays demonstrated
the role of LRP3 as a molecular switch promoting hBMSC lineage differentiation
into osteoblasts and inhibiting differentiation into adipocytes."].

The paper also supports miR-4739 regulation of LRP3 mRNA through the 3' UTR
[PMID:28340487 "expression by miR-4739 was subsequently confirmed by qRT-PCR, western blotting,"]. These data do
not identify an extracellular ligand, transported cargo, proximal signaling
reaction, or biochemical receptor activity. The ALPL, SPP1, ITGA10, CDH11,
DKK2, ADIPOQ, FABP4, LPL, and PPARG expression changes are downstream lineage
readouts; they should not be generalized into nine independent direct regulatory
activities of LRP3 or into a role in every tissue where LRP3 transcript occurs.
Those nine entities and the bone-marrow-cell context are transcribed from the
current QuickGO annotation API extension payload; the accessible abstract supports
the lineage phenotype but does not itself enumerate the marker entities.

## Topology, motif, and uptake boundary

The cloning paper describes a type-I membrane protein with extracellular repeat
regions, a transmembrane segment, and a proline-rich cytoplasmic region
[PMID:9693042 "region with a tyrosine-based internalization signal."]. UniProt's
predicted feature table (ECO:0000255/PROSITE-ProRule) assigns the extracellular
domains more specifically as CUB1–LDLRA1–LDLRA2–CUB2–LDLRA3–LDLRA4
[file:human/LRP3/LRP3-uniprot.txt "FT   DOMAIN          43..159
FT                   /note=\"CUB 1\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00059\"
FT   DOMAIN          165..201
FT                   /note=\"LDL-receptor class A 1\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\"
FT   DOMAIN          211..250
FT                   /note=\"LDL-receptor class A 2\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\"
FT   DOMAIN          254..365
FT                   /note=\"CUB 2\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00059\"
FT   DOMAIN          415..453
FT                   /note=\"LDL-receptor class A 3\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\"
FT   DOMAIN          454..490
FT                   /note=\"LDL-receptor class A 4\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\""]. The
reviewed database record independently represents LRP3 as a predicted single-pass
type-I membrane protein [file:human/LRP3/LRP3-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass type I"]. These are
sequence/topology statements, not an experimentally resolved three-dimensional
structure.

The cytoplasmic tyrosine-based motif is compatible with internalization, but a
motif is not a cargo-uptake assay. Indeed, the available abstract reports a
negative binding result in transfected CHO cells [PMID:9693042 "not bind beta-migrating very-low-density lipoprotein or receptor-associated"]. The abstract-only cache does not show uptake of another ligand or
cargo. Therefore membrane localization is supported, while receptor-mediated
endocytosis remains curator-deferred and mechanistically unresolved.

UniProt additionally asserts GGA1/GGA2 binding only by similarity
[file:human/LRP3/LRP3-uniprot.txt "CC   -!- SUBUNIT: Binds GGA1 and GGA2. {ECO:0000250}."],
which is not direct experimental evidence for adaptor recruitment by human LRP3.
Its DR block also carries an IEA keyword mapping to clathrin-coated pit
[file:human/LRP3/LRP3-uniprot.txt "DR   GO; GO:0005905; C:clathrin-coated pit; IEA:UniProtKB-KW."],
but GO:0005905 is absent from the local LRP3 GOA snapshot and therefore is not an
existing-annotation row in this review. Neither database statement establishes a
directly demonstrated coated-pit mechanism for human LRP3.

## BBB citation and family-transfer limits

PMID:30280653 is a broad BBB physiology review [PMID:30280653 "Blood-Brain Barrier: From Physiology to Disease and Back."]. An exact, case-insensitive search
of the local file finds no `LRP3` occurrence, but the cache ends after the introduction
despite being flagged as full text. That incomplete local copy cannot establish that
the curator miscited the review or that the inaccessible remainder lacks LRP3-specific
evidence. The transport-across-BBB annotation therefore remains UNDECIDED pending
verification of the complete article.

The GO_REF/PANTHER/ARBA rows document propagation mechanisms. The local record
places LRP3 in the broad LDLR family [file:human/LRP3/LRP3-uniprot.txt "CC   -!- SIMILARITY: Belongs to the LDLR family. {ECO:0000305}."], but the plasma-membrane
IBA draws on many distant LDLR-family source proteins, and the vesicle-transport
IEA is an automated ARBA transfer. Family membership supports cautious topology
and trafficking plausibility; it does not license transferring the ligand,
cargo, signaling pathway, tissue role, or disease mechanism of another paralog to
LRP3. LRP10 is a more relevant compact comparator because its predicted ectodomain
also contains two CUB and four LDL-receptor class-A domains
[file:human/LRP10/LRP10-uniprot.txt "FT   DOMAIN          28..136
FT                   /note=\"CUB 1\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00059\"
FT   DOMAIN          139..175
FT                   /note=\"LDL-receptor class A 1\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\"
FT   DOMAIN          192..305
FT                   /note=\"CUB 2\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00059\"
FT   DOMAIN          307..354
FT                   /note=\"LDL-receptor class A 2\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\"
FT   DOMAIN          355..397
FT                   /note=\"LDL-receptor class A 3\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\"
FT   DOMAIN          398..434
FT                   /note=\"LDL-receptor class A 4\"
FT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00124\""]. Even so, LRP10's
predicted internalization role [file:human/LRP10/LRP10-uniprot.txt "CC   -!- FUNCTION: Probable receptor, which is involved in the internalization"]
cannot be transferred to LRP3, whose own record says only that it may participate in
internalization and whose reported VLDL/LRPAP1 binding test was negative. Functions of
the larger LDLR/LRP1/LRP2/LRP4/LRP8 receptors are still more distant.

## Cancer and disease boundary

None of the decisive cached sources establishes a normal LRP3 function in cancer,
a causal tumor mechanism, or a cancer-cell phenotype. Database cancer cross-links,
expression associations, and family-level disease knowledge are not functional
evidence. Any future cancer claim needs an LRP3-specific perturbation study with
mechanistic and rescue evidence and must be kept distinct from the immortalized
stromal differentiation phenotype above.
