# CDC53 (Q12018) curation notes

Working journal for the review of *S. cerevisiae* CDC53 / YDL132W (cullin-A, yeast Cul1).
Inputs: `CDC53-uniprot.txt`, `CDC53-goa.tsv` (94 rows), `CDC53-deep-research-falcon.md`
(Edison/Falcon), and the cached publications listed below. Comparators: the completed
`genes/yeast/CDC4` and `genes/human/CUL1` reviews, and `modules/g1_s_transition.yaml`,
which cites Cdc4-Skp1-Cdc53 as the SCF that ubiquitinates phospho-Sic1.

## Gestalt

Cdc53 is the non-catalytic cullin scaffold of every SCF ligase in budding yeast. The
defining paper is Patton et al. 1998 [PMID:9499404 "Cdc53 contains independent binding sites
for Cdc34 and Skp1 suggesting it functions as a scaffold protein within an E2/E3 core
complex."]: residues 9-280 bind Skp1 (and, through Skp1, the F-box proteins Cdc4, Grr1 and
Met30), residues 448-748 bind the E2 Cdc34 [PMID:9499404 "deletion of an internal region of
Cdc53 (residues 448–748) abrogated Cdc34 binding but did not affect binding of Skp1 or any
of the F-box proteins."], mutants unable to bind either module cannot complement
cdc53-delta, and a cysteine-less Cdc53 is fully functional and still Rub1-modified
[PMID:9499404 "Cdc53 thus appears to act as a noncatalytic scaffold protein for Cdc34 and
Skp1/F-box proteins."]. The cdc53-1 ts lesion is R488C, inside the Cdc34-binding region.

Seol et al. 1999 identified Hrt1 (yeast Rbx1) as the Cdc53-copurifying RING-H2 subunit and
showed that the Cdc53/Hrt1 heterodimer is the minimal ligase module that activates Cdc34
without a reactive thiol [PMID:10385629 "although the ubiquitin ligase activity of SCF Cdc4
is intrinsic to the Cdc53/Hrt1 subcomplex, this activity may be enhanced upon assembly of
Cdc53/Hrt1 with Cdc4/Skp1."]; Skowyra et al. 1999 showed Rbx1 promotes Cdc34 association
with Cdc53 [PMID:10213692 "Rbx1 promotes association of Cdc34 with Cdc53 and stimulates Cdc34
auto-ubiquitination in the context of Cdc53 or SCF complexes."]. This is why the GOA
`contributes_to` qualifier on GO:0004842/GO:0061630 is exactly right and why GO:0160072
(ubiquitin ligase complex scaffold activity) is the core MF.

Founding biology: cdc53 ts mutants phenocopy cdc4 and cdc34 (G1/S arrest, elongated
multibudded cells) [PMID:8943317 "Mutations in CDC53 cause a phenotype indistinguishable from
those of cdc4 and cdc34 mutations"]; SCF(Cdc4) reconstituted from Cdc4, Skp1, Cdc53 plus E1,
Cdc34 and ubiquitin ubiquitinates phospho-Sic1 [PMID:9346239 "SCFCdc4p subunits, E1 enzyme,
the E2 enzyme Cdc34p, and ubiquitin are sufficient to reconstitute ubiquitination of
Cdk-phosphorylated Sic1p."] [PMID:9346238 "Skp1, Cdc53, and the F-box protein Cdc4 form a
complex, SCFCdc4, which functions as a Sic1 ubiquitin-ligase (E3)"]; SCF(Grr1) does the same
to phospho-Cln1/2 and to Gic2 [PMID:9736614 "degradation of Gic2p required the
Skp1-cullin-F-box protein complex (SCF) components Cdc34p, Cdc53p, Skp1p and Grr1p, but not
Cdc4p."]; SCF(Met30) represses methionine genes [PMID:9499404 "in addition to Met30, Cdc34,
Cdc53, and Skp1 are required for appropriate repression of methionine biosynthesis genes."].

Regulation: Cdc53 is rubylated (Rub1 = NEDD8) on a C-terminal lysine (UniProt Lys760,
by similarity); Lag2 is the yeast CAND1 that binds only non-neddylated Cdc53, inserts a
beta-hairpin into the Skp1 pocket, covers the neddylation lysine and is displaced by
Skp1-adaptor modules [PMID:19942853 "Similar to Cand1, Lag2 directly interacts with
non-neddylated yeast cullin Cdc53 and prevents its neddylation in vivo and in vitro"]
[PMID:19942853 "the presence of Skp1 bound to substrate-specific adaptors is required to
counteract the inhibitory association of Cand1/Lag2 with Cdc53"]; Liu et al. 2009
independently found Lag2 blocks Cdc34 association and Rub1 conjugation [PMID:19763088 "Lag2
disrupts the ubiquitylation activity of the SCF E3 ligase by interrupting the association of
Cdc34 to SCF complex."]. Rubylated Cdc53 is read by the Cdc48 cofactor Ubx5 UIM
[PMID:22466964 "Ubx5 only bound to rubylated Cdc53 and this interaction was disrupted by
deletion or point mutation of the UIM domain"].

Localisation: UniProt lists cytoplasm and nucleus from the genome-wide GFP study
(PMID:14562095; cached abstract-only, no Cdc53 text). Cdc53-myc ChIPs to ARS305/ARS603 as part
of SCF(Dia2) [PMID:16421250 "both Skp1 and Cdc53 coprecipitated with ARS305 and ARS603 DNA in
a cross-linker dependent manner."]. The deep research concludes localisation is
"cytosolic and nuclear/context-dependent", which I adopt: both GO:0005634 and GO:0005737
accepted, both used in core_functions.

## Decisions on existing annotations (94 rows)

- Core (ACCEPT): G1/S transition (IDA/IMP/NAS), ubiquitin-protein transferase / ligase
  activity (contributes_to), SCF complex (all 11 rows), cullin-RING complex (IEA),
  ubiquitin-dependent and SCF-dependent proteasomal catabolic process, protein
  ubiquitination (IBA), ubiquitin ligase complex scaffold activity (IBA), ubiquitin
  protein ligase binding (IBA/IEA; Hrt1 is the RING E3), nucleus (IBA/IEA), cytoplasm (IEA).
- IBA rows: all four descend from PTN002631076 (cullin family) or PTN000231993 (Cul1
  clade). CDC53 (SGD:S000002290) appears in its own WITH/FROM for GO:0019005 and GO:0031146;
  this is expected (its IDA rows are descendant evidence) and was not treated as circular.
- Protein binding (44 IPI rows): followed the CDC4/CUL1 policy. Focused papers were
  MODIFIED to the informative MF: Patton 1998 Skp1/Cdc4/Grr1/Met30 -> GO:0160072, Patton
  1998 Cdc34 -> GO:0031624 (E2 binding; direct Cdc34-binding region mapped), Kus 2004 Skp1 ->
  GO:0160072, Siergiejuk 2009 Skp1 -> GO:0160072 and Hrt1 -> GO:0031625. All proteome-scale
  rows (Uetz, Seol 2001, Ho, Hazbun, Yu, Kato, Breitkreutz, Meier, Michaelis) were REMOVED as
  uninformative (interaction not disputed). Regulator-of-Cdc53 rows where Cdc53 is the
  bound/modified party (Lag2 x2, Dcn1, Ubx5, Saf1 control) were REMOVED with the biology
  recorded here and in core function 2.
- PMID:23267104 (Meier, Sit & Quake 2013, PNAS) is a microfluidic interaction map of
  *Streptococcus pneumoniae* proteins; the cached text never mentions yeast or SCF. IntAct
  attributes four Cdc53 pairs (Grr1, Met30, Skp1, Hrt1) to it, presumably benchmark
  measurements not in the cache. Flagged `reference_review.correctness: MISCITED`,
  relevance NONE; the rows were removed under the protein-binding policy anyway.
- GO:0030674 protein-macromolecule adaptor activity (IMP/IPI x3, Patton 1998): MODIFY to the
  specific child GO:0160072, which is exactly what the deletion mapping shows and what PAINT
  already assigns.
- GO:0007346 regulation of mitotic cell cycle (NAS, Met4 paper): MODIFY to GO:0000082
  (too general; off-topic reference).
- GO:0031573 mitotic intra-S DNA damage checkpoint signaling (NAS, Fong 2013): the paper
  shows SCF(Dia2) is needed to switch the checkpoint OFF (Rad53 deactivation, Mrc1
  degradation) [PMID:23172854 "Dia2 is required for robust deactivation of the Rad53
  checkpoint kinase and timely completion of DNA replication during recovery"], so MODIFY to
  GO:1904290 negative regulation of mitotic DNA damage checkpoint (non-core).
- Receptor-specific downstream processes: G2/M transition (IGI x2, NAS), GAL1/galactose
  transcription (SCF(Das1)-Mig2), mitochondrial fusion (SCF(Mdm30)-Fzo1), HMR and
  subtelomeric heterochromatin formation (SCF(Dia2)-Sir4) -> KEEP_AS_NON_CORE. The SCF does a
  step of each process, so the terms are not wrong for the scaffold, but in each case the
  CDC53 gene was not manipulated and the specificity lies in the F-box protein.
- MARK_AS_OVER_ANNOTATED: GO:0010828 positive regulation of glucose transport (IDA, cited to
  the Cln1/SCF(Grr1) reconstitution paper, which per its abstract has no glucose-transport
  assay; the HXT effect is several steps downstream via Grr1), GO:0071406 cellular response
  to methylmercury (NAS; F-box overexpression phenotype, target unknown), GO:0003688 DNA
  replication origin binding (IDA; Cdc53 ChIP at ARS is real but Cdc53 has no DNA-binding
  domain and the authors call Dia2 the origin-binding protein).
- REMOVE: GO:0000781 chromosome, telomeric region (IEA GO_REF:0000108), an inter-ontology
  inference chained from the NAS subtelomeric-silencing row; nothing places Cdc53 at
  telomeres.
- No NEW terms proposed. Candidate processes from the deep research (replisome disassembly
  via SCF(Dia2)-Mcm7, C-degron quality control via SCF(Das1), Met4 regulation, meiotic SC
  formation) are all receptor-specific outputs already handled by the F-box proteins and
  would fail the same test applied to the non-core rows above.

## Reference quality

Full text cached: PMID:9499404, 10385629, 19942853, 19763088, 22466964, 16421250, 22844255,
23172854, 37968396. Abstract-only: the 1994-1999 founding papers, Kus 2004, and all the
NAS-cited F-box papers; where a curator's IDA/IGI rests on full-text data I could not see
(G2/M IGIs, glucose-transport IDA) I deferred rather than removed. UniProt FUNCTION cites
PMID:7813440 and PMID:9312054, which are not in the cache.

## Validation

`just validate yeast CDC53`: valid, no warnings (94/94 reviewed; status COMPLETE).
Rendered with `just render yeast CDC53`.
