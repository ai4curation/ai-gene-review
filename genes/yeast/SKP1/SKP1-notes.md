# SKP1 (yeast, P52286 / YDR328C / CBF3D) - curation notes

## 2026-09-26 - full review of the seeded GOA rows

Inputs: `SKP1-uniprot.txt`, `SKP1-goa.tsv` (174 rows, 101 of them GO:0005515 IPI from IntAct),
`SKP1-deep-research-falcon.md` (Edison/Falcon; covers SCF, CBF3, Sgt1-Hsp90 and Rcy1 but not RAVE),
cached publications for all 44 cited PMIDs (full text for 17 of them; the rest are abstract-only).
Comparators: `genes/yeast/CDC4` and `genes/yeast/CDC53` (both COMPLETE) and `genes/human/SKP1`.

### Gestalt

Skp1 is a non-catalytic adaptor whose one molecular trick is binding F-box motifs while its
N-terminal BTB/POZ-like region binds a cullin (or, in CBF3, contacts Cep3). Everything in GOA
follows from which partner it is holding.

1. **SCF adaptor.** Cloned as a cdc4 suppressor; defined the F-box
   [PMID:8706131 "directly binds Skp2p, cyclin F, and Cdc4p through a novel structural motif called the F-box"].
   Required for Sic1/Cln/Clb5 proteolysis
   [PMID:8706131 "SKP1 is required for ubiquitin-mediated proteolysis of Cin2p, Clb5p, and the Cdk inhibitor Sic1p"].
   Bridges Cdc53 to receptors
   [PMID:9499404 "Skp1 bridges Cdc53 to three different F-box proteins, Cdc4, Met30, and Grr1"];
   the Met30 F-box is necessary and sufficient
   [PMID:9499404 "The F-box of Met30 was both necessary and sufficient for interaction of Met30 with Skp1"],
   confirmed by mapping to residues 180-225
   [PMID:14660673 "The Met30p F-box motif, residues 180-225, is necessary and sufficient to bind Skp1p"].
   Reconstituted SCF(Cdc4) ubiquitinates phospho-Sic1
   [PMID:9346239 "SCFCdc4p subunits, E1 enzyme, the E2 enzyme Cdc34p, and ubiquitin are sufficient to reconstitute ubiquitination of Cdk-phosphorylated Sic1p"],
   and thirteen SCFs were built on Skp1/Cdc53
   [PMID:14747994 "We have reconstituted and purified 1 known and 12 novel yeast SCF complexes"].
   Allele map used throughout: skp1-11 (G160E/R167K) loses F-box binding, skp1-12 (L8G) loses Cdc53 binding
   [PMID:19942853 "skp1-12 carries a single mutation (L8G) that disrupts binding to Cdc53"].
   Phospho-S162 weakens Met30 binding
   [PMID:22817900 "the phosphorylation of S162 acts as a reversible switch for Met30 affinity"].
2. **CBF3 subunit (Cbf3d).** Fourth subunit, equal stoichiometry with Ctf13
   [PMID:8706132 "indicating equal stoichiometry of these two proteins in the CBF3 complex"];
   identified independently by reconstitution
   [PMID:8670864 "The 29 kDa protein was shown to be a fourth component of CBF3 and therefore was named Cbf3d"].
   Skp1-Ctf13 heterodimer
   [PMID:10352012 "p23(Skp1) and p58(Ctf13) form a heterodimer, and p64(Cep3) and p110(Ndc10) form homodimers"].
   Activation needs Hsp90, not phosphorylation
   [PMID:12084919 "Instead, the formation of active Ctf13p/Skp1p requires Hsp90."];
   Skp1-Sgt1 acts at the rate-limiting step
   [PMID:15090617 "Skp1p and Sgt1p contribute to a final, rate-limiting step in assembly, the binding of the core CBF3 subunit Ctf13p to Ndc10p"].
   skp1-4 has missegregation and a 2C/short-spindle arrest
   [PMID:8706132 "skp1-4 mutants arrest predominantly as large budded cells with a G2 DNA content and short mitotic spindle, consistent with a role in kinetochore function"];
   skp1-3 arrests in G1
   [PMID:8706132 "skp1-3 mutants, however, arrest predominantly as multiply budded cells with a G1 DNA content"].
3. **RAVE subunit.** Rav1-Rav2-Skp1
   [PMID:11283612 "Rav1, Rav2 and Skp1 form a complex that we have named 'regulator of the (H+)-ATPase of the vacuolar and endosomal membranes' (RAVE)"];
   essential for V-ATPase assembly, with Skp1 binding constitutive
   [PMID:11844802 "Skp1p recruitment to the RAVE complex does not appear to provide a signal for V-ATPase assembly"].
4. **Localisation.** Nucleus + cytoplasm by functional GFP
   [PMID:11080155 "The core SCF subunits Cdc53, Hrt1 and Skp1 were distributed in the nucleus and the cytoplasm, whereas the F-box protein Cdc4 was exclusively nuclear"];
   mostly cytoplasmic on fractionation
   [PMID:10352012 "p23Skp1 partitioned mostly to the cytoplasmic fraction"];
   at origins by ChIP as SCF(Dia2)
   [PMID:16421250 "both Skp1 and Cdc53 coprecipitated with ARS305 and ARS603 DNA in a cross-linker dependent manner"].
5. **Neddylation.** Rub1-Cdc53 absent in skp1 alleles
   [PMID:9531531 "only the 92-kD isoform was observed in skp1-3, skp1-4, and skp1-12 strains"];
   explained later by Lag2 eviction
   [PMID:19942853 "Skp1 is required to trigger Lag2 dissociation from cullins in vivo , which is a prerequisite for subsequent cullin neddylation"].

### Decisions and why

Action counts: ACCEPT 41, MODIFY 42, REMOVE 70, KEEP_AS_NON_CORE 16, MARK_AS_OVER_ANNOTATED 5. No PENDING.

* **Protein binding (101 rows).** Policy from the annotation-reviewer skill: MODIFY where the cited
  paper supports a specific MF, otherwise REMOVE as uninformative.
  - F-box proteins in focused SCF/CBF3 papers (Bai 1996, Patton 1998, Rouillon 2000, Brunson 2004,
    Kus 2004, Seol 2001, Rodrigo-Brenni 2004, Beltrao 2012, Hwang 2006) -> MODIFY to GO:1990444
    F-box domain binding (26 rows). For Hwang 2006 (abstract does not mention Skp1) the F-box
    binding of Hrt3/Ucc1 is supported by their reconstitution in Kus 2004, cited as additional reference.
  - Cdc53 in focused papers (Patton 1998, Seol 2001, Kus 2004, Siergiejuk 2009) -> MODIFY to
    GO:0097602 cullin family protein binding + GO:0160072 ubiquitin ligase complex scaffold activity
    (mirrors the human SKP1 review and the human SCF GO-CAMs).
  - HTP/incidental records (Uetz, Ito, Ho, Gavin, Yu, Kato, Breitkreutz, Hazbun, Meier, Michaelis,
    Weerasekera, Thelander, Ang) -> REMOVE (66 rows), same grading as the CDC4 exemplar used for the
    identical references. Eft2, Rav1, Sgt1 rows -> REMOVE (no MF term describes Skp1's side; RAVE and
    kinetochore-assembly rows carry the biology).
  - Bub1 (Kitagawa 2003) -> MODIFY to GO:0007094 mitotic spindle assembly checkpoint signaling,
    because the paper's claim is functional
    [PMID:12769845 "The Skp1's interaction with Bub1 is required for the mitotic delay induced by kinetochore tension defects"];
    flagged in suggested_questions since SGD did not add a checkpoint term.
* **G2/M transition (3 rows) -> KEEP_AS_NON_CORE**, matching CDC4/CDC53: a 2C short-spindle arrest
  is a metaphase-like block of undefined mechanism (kinetochore vs Sic1-independent SCF).
* **Vacuolar acidification (3) and regulation of complex assembly (2) -> MODIFY to GO:0070072**:
  RAVE performs assembly, acidification is the downstream outcome; the assembly term already exists.
  RAVE complex (4) and V-ATPase assembly IDA -> KEEP_AS_NON_CORE (fungal-specific, Skp1 contribution undefined).
* **Protein neddylation (2) -> MODIFY to GO:2000436 positive regulation**: Skp1 is required
  permissively (evicts Lag2) but the E1/E2/Dcn1 do the chemistry.
* **DNA replication origin binding -> MARK_AS_OVER_ANNOTATED** (same as CDC53): ChIP records SCF(Dia2)
  location, not a binding activity; Dia2 is the origin-binding subunit
  [PMID:16421250 "We propose that Dia2 is an origin-binding protein that plays a role in regulating DNA replication."].
* **Chromosome, telomeric region IEA -> REMOVE**: inter-ontology propagation from a NAS process row; no
  Skp1 evidence at telomeres.
* **Intra-S checkpoint NAS -> MODIFY to GO:1904290** (direction inverted; Dia2 mediates recovery
  [PMID:23172854 "Dia2 is required for robust deactivation of the Rad53 checkpoint kinase"]).
* **Regulation of mitotic cell cycle NAS -> MODIFY to GO:0000082**; protein-containing complex assembly
  IDA -> MODIFY to GO:0051382 (generic parents of already-annotated specific terms).
* **Receptor-specific SCF outputs** (GAL1/Mig2, mitochondrial fusion, Sir4 silencing x2, endomembrane) ->
  KEEP_AS_NON_CORE; glucose transport, methylmercury, exit from mitosis (direct), Rok1 translation ->
  MARK_AS_OVER_ANNOTATED. Mitotic-exit regulation (Bfa1) x2 -> KEEP_AS_NON_CORE (single abstract-only study).
* IBA rows (nucleus, cytoplasm, SCF-dependent catabolism, cullin binding, mitotic cell cycle) all ACCEPT;
  the target's own SGD entry among the WITH sources is expected, not circular.

### Core functions written

1. SCF scaffold: MF GO:0160072 (contributes_to GO:0061630); BP GO:0031146, GO:0016567, GO:0000082;
   nucleus + cytoplasm; in_complex GO:0019005.
2. CBF3 subunit: MF GO:1990444 F-box domain binding (Ctf13); BP GO:0051382; kinetochore + nucleus;
   in_complex GO:0031518.

RAVE and the Rcy1 complex are deliberately not core functions (see above); they are described in
`description` and raised in suggested_questions.

### Not in GOA but worth knowing (from the deep research; primary papers not cached)

* Cryo-EM of Cep3(2)-Ctf13-Skp1 at 3.6 A (Leber 2018): Skp1 helices alpha6-alpha8 bind the Ctf13
  F-box, residues 105-112 contact the LRRs, and Y139/N140 substitutions abolish complex formation.
* Sgt1 TPR-Skp1 BTB crystal structure at 2.8 A (Willhoft 2017), Kd ~0.6-0.7 uM; ~2% of Skp1 is Sgt1-bound.
* Rcy1-Skp1 complex lacks Cdc53/Hrt1 and is needed for Snc1 recycling (Galan 2001).
* 2024 SCF(Met30) work: cadmium and H2S sensing reside in Met30, not Skp1; Cdc48 extracts Met30 from the
  Cdc53-Skp1 core.

### Open items

* Whether the skp1-4/skp1-12 mitotic arrest is checkpoint-dependent (experiment suggested).
* Whether Skp1 phosphorylation (S162, T177) tunes receptor loading in vivo (experiment suggested).
* The Bub1 checkpoint claim rests on one abstract-only paper.

## 2026-09-29 - IBA propagation rereview

Rechecked the five IBA rows against the IBA project rubric and the cached support for their target-side
biology:

* `GO:0000278 mitotic cell cycle` from `PANTHER:PTN000877296` remains broad but sound; the direct
  Bai 1996 yeast abstract establishes the mixed G1/G2 skp1 arrest and the target's own SGD row in
  `WITH/FROM` is expected, not circular.
* `GO:0005634 nucleus`, `GO:0005737 cytoplasm`, `GO:0031146 SCF-dependent proteasomal ubiquitin-dependent
  protein catabolic process`, and `GO:0097602 cullin family protein binding` from `PANTHER:PTN000126179`
  remain core Skp1 calls, backed by the Mathias/Koepp/Kaplan localization, SCF receptor, and Cdc53-binding
  papers that were already cached.

`genes/yeast/SKP1/SKP1-goa.tsv` still names the two PTNs, but the local PAINT snapshot under
`interpro/panther/PTHR11165/` currently contains only `PTHR11165-metadata.yaml` and
`PTHR11165-entries.csv`, so the review now records each PTN source as `SOURCE_STALE_OR_MISSING`
while keeping the accepted biological decisions.

Fresh PubMed searches for 2025-2026 `Skp1`/`SKP1`/`Cbf3d` with exact `Saccharomyces cerevisiae` or
yeast SCF/RAVE terms recovered only a mammalian Rabconnectin-3/V-ATPase paper that mentions yeast
Skp1/RAVE as background; no newer budding-yeast SKP1 paper changes the 2026-09-26 curation.
