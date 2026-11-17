# PA1257 (Q9I487) review notes

## Sources and research (2026-11-05)

Manual research (no deep-research provider). Sources: UniProt Q9I487 (TrEMBL), the GOA
file, and the cached full text of PMID:18833300 (Johnson et al. 2008, PLoS Genet).

- PA1257 is the membrane (permease) subunit of a polar-amino-acid ABC transporter: four
  Phobius TM helices, the ABC_TM1 domain (PF00528, PS50928), NCBIfam TIGR01726
  (HEQRo_perm_3TM), InterPro IPR043429 ArtM/GltK/GlnP/TcyL/YhdX-like. PANTHER places it in
  PTHR30614:SF0, named after E. coli TcyL.
- Its operon partners are PA1256 (ATP-binding protein) and PA1260 (periplasmic
  substrate-binding protein) [PMID:18833300 "PA1256, PA1257 and PA1260 are all components of a predicted ABC amino acid transporter encoded in a putative operon along with two hypothetical genes."].
- Johnson et al. screened sequenced, PCR-confirmed Mini-Tn5 transporter mutants on Biolog
  Phenotype MicroArrays and measured induction by qRT-PCR. PA1257 is one of the mutants in the
  PAO1 background (Table 1, "PA1257PA01amino acid ABC transporter membrane protein").
  [PMID:18833300 "Knockouts in these genes affected growth on hydroxy-L-proline as a carbon source, and expression of all three genes was induced by hydroxy-L-proline (Table 2 and 3)."]
  [PMID:18833300 "There was no growth defect on L-proline, nor was expression affected by L-proline as an inducer, suggesting specificity for hydroxy-L-proline."]
  [PMID:18833300 "three genes are part of a single operon (PA1256, PA1257 and PA1260) which was predicted to be involved in amino acid transport and instead found to be involved in Hydroxy-L-Proline transport"].
- No uptake assay with labelled hydroxyproline is reported. The transport claim rests on the
  growth defect of three subunit mutants, their substrate-specific induction, and the
  permease identity; together these are a good genetic case for a hydroxyproline ABC
  importer.

## PseudoCAP IBA-seed assessment

Seeds of PTN000770157 for GO:0006865 amino acid transport (`.cache/paint/IBD.gaf`, column 8):
P0AFT2 (E. coli TcyL), P0AEQ6 (E. coli GlnP), Q9I404 and Q9I403 (PAO1 glutamate/glutamine
permease subunits, both PseudoCAP IMP from the same paper), and Q9I487 (this gene, through its
GO:0034589 row; GO:0034589 is_a GO:0006865). QuickGO (2026-11-05): TcyL has IDA and IGI for
L-cystine transport (EcoCyc, PMID:25139244, PMID:26350134); GlnP has EXP for glutamine
transport (EcoCyc, PMID:3027504).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000770157 | GO:0006865 amino acid transport | 5 | 84 (28 taxa) | GO:0034589 hydroxyproline transport, IMP, PMID:18833300 (PseudoCAP) | SOUND | A sequenced, PCR-confirmed PAO1 transposon mutant of this permease cannot grow on hydroxy-L-proline as carbon source, and the operon is induced specifically by hydroxy-L-proline. No direct uptake assay, but for a permease subunit this is direct genetic evidence of the transport it performs. Node term (amino acid transport) suits a polar-amino-acid permease clade. Full text read. | E. coli TcyL (IDA/IGI), E. coli GlnP (EXP), PAO1 Q9I404, Q9I403 | Yes, on the E. coli seeds. No GO_CENTRAL defect for this node. |

### Second node, not seeded by PA1257

PA1257 also receives GO:0015184 L-cystine transmembrane transporter activity and GO:0015811
L-cystine transport by IBA from PTN000770175, whose only seed for both terms is E. coli TcyL
(P0AFT2). The only experimental data on PA1257 point to hydroxy-L-proline, and in these
binding-protein-dependent systems substrate choice is set largely by the periplasmic binding
protein, which differs between operons; the cystine IBD therefore probably spans permeases of
different specificity. No assay has tested PA1257 with cystine, so this is not a refutation:
both rows are MARK_AS_OVER_ANNOTATED with a GO_CENTRAL CHECK defect, now CONFIRMED after the tree
check below, recorded on the GO:0015184 row.

## PANTHER tree check (2026-11-05)

Topology of PTN000770175 in PTHR30614 fetched with `projects/PSEUDOCAP/panther_tree.py node
PTN000770175 --depth 5` and `--contains`. The node is a **SPECIATION** node (Proteobacteria),
18 leaves, all PTHR30614:SF0.

| Child node | Event | Leaves | Subfamilies | Contents | Verdict |
|---|---|---|---|---|---|
| PTN002826365 / PTN002826366 / PTN001577545 | LEAF | 1 each | SF0 | *H. pylori* HP_0939, *N. meningitidis* NMB0788, *G. sulfurreducens* GSU0799 ("amino acid ABC transporter permease") | specificity unknown |
| PTN002826367 | DUPLICATION | 2 | SF0 | *Bradyrhizobium* blr2225, blr3310 | specificity unknown |
| PTN000770168 | SPECIATION (Gammaproteobacteria) | 13 | SF0 | the four clades below | mixed |
| &nbsp;&nbsp;PTN008625440 | HORIZ_TRANSFER | 4 | SF0 | *B. subtilis* TcyB, *B. cereus* BC_0873 (cystine), *S. aureus* SAOUHSC_02698, *H. influenzae* HI_1079 | cystine for the two named |
| &nbsp;&nbsp;PTN008625441 | HORIZ_TRANSFER | 2 | SF0 | *B. subtilis* YxeN, *V. cholerae* VC_0009 | specificity unknown |
| &nbsp;&nbsp;**PTN002413080** | DUPLICATION | 3 | SF0 | **PA1257, PA1258, PA0313** (PA0313 = YecS-like L-cysteine system permease) | hydroxyproline operon for PA1257/PA1258 |
| &nbsp;&nbsp;**PTN002024099** | SPECIATION (Enterobacteriaceae) | 4 | SF0 | *E. coli* TcyL (the seed), *Salmonella* YecS and STM1636, *Yersinia* YecS | cystine/YecS throughout |

Verdict: the earlier concern holds and is now CONFIRMED on primary data. The node is not a clade of
cystine permeases: it mixes permeases of several specificities across two horizontal transfers and
three lineage-specific duplications. `--contains P0AFT2,Q7CQB5,A0A380PDF6,Q8ZPA0` returns
PTN002024099, i.e. every cystine/YecS-named enterobacterial member sits in that one 4-leaf clade, so
the cystine-specific support stops there. `--contains P0AFT2,P42200` and `--contains P0AFT2,Q9I6H8`
both return the whole 13-leaf PTN000770168, confirming that the other cystine-named leaves (*B.
subtilis* TcyB, PAO1 PA0313) are not monophyletic with TcyL and so cannot be gathered into a single
narrower cystine node. `--contains Q9I486,Q9I487` returns PTN002413080, the *Pseudomonas* duplication
that produced the hydroxyproline permeases.

Recommendation recorded in the defect: move the GO:0015184 / GO:0015811 IBDs down to
**PTN002024099**, and if a term is wanted at PTN000770175 use GO:0015424 ABC-type amino acid
transporter activity (plus GO:0006865 for the process), which the node's composition supports.

## Annotation decisions

- GO:0034589 hydroxyproline transport (IMP): ACCEPT, core process.
- GO:0005886 plasma membrane (IBA, IEA): ACCEPT. GO:0016020 membrane: TOO_GENERAL.
- GO:0022857 transmembrane transporter activity: MODIFY to GO:0015424 ABC-type amino acid
  transporter activity (hydroxyproline is an amino acid in GO: GO:0034590 is_a GO:0015179).
- GO:0043190 ABC transporter complex: MODIFY to GO:0055052 (substrate-binding
  subunit-containing), since the operon encodes the periplasmic binding protein PA1260.
- GO:0055085 transmembrane transport: MODIFY to GO:0003333 amino acid transmembrane transport.
- GO:0015184 and GO:0015811 (IBA from PTN000770175): MARK_AS_OVER_ANNOTATED.
