# clk-1 (COQ7 ortholog) — research notes

UniProt: P48376 (COQ7_CAEEL). WormBase: WBGene00000536 / ZC395.2. Gene symbol clk-1
("clock abnormal / clk"). Human ortholog: COQ7. 187 aa precursor with an N-terminal
mitochondrial transit peptide (1–8) cleaved to a mature 9–187 chain.

## Summary of what is KNOWN (with provenance)

### Direct molecular function: di-iron ubiquinone/CoQ biosynthetic monooxygenase
- clk-1/COQ7 catalyzes the penultimate step of ubiquinone (coenzyme Q) biosynthesis: the
  hydroxylation of 5-demethoxyubiquinone (DMQ) at the C6 (C5 in some numbering) position,
  producing 3-demethylubiquinone. EC 1.14.13.253; RHEA:81211. It uses a carboxylate-bridged
  di-iron center and NAD(P)H (UniProt P48376 CATALYTIC ACTIVITY / COFACTOR: "Binds 2 iron
  ions per subunit"; FT BINDING residues 30/60/63/112/148/151 to Fe cation).
- The enzyme belongs to the COQ7 family / ferritin-like di-iron superfamily
  (Pfam PF03232 COQ7; InterPro IPR011566; PANTHER PTHR11237 "COENZYME Q10 BIOSYNTHESIS
  PROTEIN 7"; HAMAP MF_01658/MF_03194).
- Founding paper established structural + functional conservation of clk-1 as a "timing gene"
  and did mutagenesis of the catalytic Glu148: [PMID:9020081 "Structural and functional
  conservation of the Caenorhabditis elegans timing gene clk-1"] (Science 1997). (Not in GOA
  annotation set but is the founding functional reference; cited in UniProt.)
- Biochemical proof that CLK-1 is required for UQ biosynthesis in the worm:
  [PMID:11244089 "clk-1 mutants mitochondria do not contain detectable levels of UQ(9).
  Instead, the UQ(9) biosynthesis intermediate, demethoxyubiquinone (DMQ(9)), is present at
  high levels. This result demonstrates that CLK-1 is absolutely required for the biosynthesis
  of UQ(9) in C. elegans."] Also: DMQ9 can substitute as an electron carrier —
  [PMID:11244089 "DMQ(2) can act as an electron acceptor for both complex I and complex II in
  clk-1 mutant mitochondria"].
- clk-1 encodes "a hydroxylase involved in the biosynthesis of the redox-active lipid
  ubiquinone (co-enzyme Q), and in clk-1 mutants, ubiquinone is replaced by its biosynthetic
  precursor demethoxyubiquinone" [PMID:14517217].

### Subcellular location: mitochondrion (inner membrane, matrix face)
- UniProt SUBCELLULAR LOCATION: "Mitochondrion inner membrane; Peripheral membrane protein;
  Matrix side" (so a genuine "extrinsic component of mitochondrial inner membrane",
  GO:0031314, not an integral membrane protein).
- CLK-1-GFP is fully active and localizes to mitochondria of all somatic cells:
  [PMID:10202142 "CLK-1 is fully active when fused to green fluorescent protein and is found
  in the mitochondria of all somatic cells."]
- Mitochondrial localization independently observed: [PMID:25961505 "adult transgenic worms
  expressing CLK-1 fused to green fluorescent protein (GFP) also display fluorescence in both
  compartments"] (mitochondria and nucleus).

## Downstream / mutant-phenotype (NON-CORE) biology
The mutant phenotypes are consequences of altered Q/DMQ, not the direct molecular activity.

- Longevity ("Clk" clock phenotype): clk-1 mutations extend lifespan and slow developmental
  and behavioral rates. [PMID:10202142 "Mutations in the clk-1 gene ... result in an average
  slowing of a variety of developmental and physiological processes, including the cell cycle,
  embryogenesis, post-embryonic growth, rhythmic behaviors and aging."] Overexpression shortens
  lifespan and accelerates behavior [PMID:10202142 "Overexpression of CLK-1 activity in
  wild-type worms can increase mitochondrial activity, accelerate behavioral rates during aging
  and shorten life span"].
- Lifespan extension by RNAi of UQ-biosynthesis genes incl. clk-1: [PMID:12709403 "We have
  identified by RNA interference (RNAi) eight genes, including clk-1, involved in ubiquinone
  biosynthesis in C. elegans ... and extended life span compared with non-interfered animals."]
- Maternal rescue / developmental-timing: [PMID:14517217 "homozygous clk-1 mutants display a
  wild-type phenotype when issued from a heterozygous mother ... increased adult longevity can
  be uncoupled from the early mutant phenotypes"].
- Genetic-interaction lifespan modulation with translation / DR pathways (clk-1 used as a
  long-lived ETC/"clk" mutant partner): [PMID:17277769 "lack of IFE-2 enhances the long-lived
  phenotype of clk and dietary-restricted eat mutant animals."]; [PMID:19783783] (DR / NLP-7,
  clk-1 as ETC-mutant control; IGI/IMP determination of adult lifespan).
- Oxidative phosphorylation / anesthetic (xenobiotic) sensitivity: complex I–dependent OXPHOS
  correlates with volatile-anesthetic sensitivity, tested across ETC/CoQ mutants including
  clk-1: [PMID:16920626 "a clear correlation between complex I-dependent oxidative
  phosphorylation capacity and volatile anesthetic sensitivity."]
- CLK-1 protein level tracks mitochondrial biogenesis; used as a mito marker reduced on hsp-6
  knockdown: [PMID:17189267 "Knockdown of HSP-6 by RNA interference in young adult nematodes
  caused a reduction in the levels of ATP-2, HSP-60 and CLK-1"].

## DEBATED / secondary nuclear moonlighting role — treat cautiously
- A distinct **nuclear** pool of CLK-1/COQ7 was reported to regulate mitochondrial stress
  responses and longevity independently of UQ biosynthesis: [PMID:25961505 "We have uncovered a
  distinct nuclear form of CLK-1 that independently regulates lifespan."]; the nuclear-only,
  MTS-deleted CLK-1 "localised predominantly to the nucleus" and "CLK-1nuc(+) could not" rescue
  UQ biosynthesis [PMID:25961505 "full length CLK-1 was able to rescue ubiquinone biosynthesis
  in these worms, however, CLK-1nuc(+) could not"], yet partially rescued ROS, UPRmt, and
  longevity phenotypes. Nuclear COQ7 associates with chromatin [PMID:25961505 "the uncleaved
  form of COQ7, but not the R28A mutant, was enriched in the chromatin fraction"] and modulates
  transcription of ROS/UPRmt genes (sod-2, skn-1, hsp-6, hsp-60, spg-7; human SOD2/NRF2/HMOX1,
  HSPA9/HSPD1/AFG3L2 etc.). This underlies the WormBase IMP annotations to
  negative/positive regulation of transcription by RNA Pol II, regulation of ROS metabolic
  process, and determination of adult lifespan on PMID:25961505.
- An older, isolated in-vitro report: CLK-1 binds the O_L region of **mitochondrial** DNA:
  [PMID:11959146 "C. elegans CLK-1 as well as its mouse homologue have DNA binding activity
  that is specific to the O(L) region of mitochondrial DNA."] This is the basis of the IDA
  "transcription cis-regulatory region binding" (GO:0000976) annotation. Note the binding is to
  mtDNA (a replication/transcription origin), a single in-vitro study, not widely replicated —
  a possible moonlighting activity, not the core enzymatic function.

Caveat on the nuclear model: the nuclear localization/role is a genuine experimental report
(Nat Cell Biol 2015) but remains debated in the field; CLK-1's N-terminus and human COQ7's NTS
are not conserved ([PMID:25961505 "the N-terminal residues we identified as being critical for
nuclear localisation of COQ7 do not appear to be conserved in CLK-1"]), and independent
confirmation of an endogenous, functionally significant nuclear pool in the worm is limited.

## What is NOT known (knowledge gaps)
1. **How DMQ-vs-Q levels produce the longevity signal.** clk-1 mutants accumulate DMQ9 and lack
   UQ9 yet respire near-normally (DMQ9 substitutes as an electron carrier) [PMID:11244089], and
   lifespan extension appears "independent of ubiquinone biosynthesis and ATP production"
   [PMID:25961505]. The mechanistic chain from the specific quinone species (DMQ vs Q, ROS
   output) to the pro-longevity signal is not established.
2. **The disputed nuclear/non-mitochondrial role.** Whether an endogenous nuclear CLK-1 pool of
   physiological significance exists in the worm, how it is targeted (worm N-terminus lacks the
   COQ7 NTS), whether it binds DNA sequence-specifically, and whether "transcription regulation"
   is a direct molecular function or an indirect consequence, are unresolved.
3. **Ontology gap:** CLK-1/COQ7 is described as a component of a multi-subunit COQ enzyme
   ("CoQ synthome") complex with a structural stabilizing role (UniProt, By similarity), but GO
   has no "coenzyme Q biosynthesis complex" cellular-component term to capture this membership.

## Provenance note on deep research
Falcon deep research (`just deep-research-falcon worm clk-1 --fallback perplexity-lite`) took
~29 min on the congested shared Edison endpoint and the wrapper recipe ultimately reported a
timeout, but the Edison run did land a real report at the boundary:
`clk-1-deep-research-falcon.md` (provider: falcon, model: Edison Scientific Literature,
cached: false, 40 cited sources). It was verified as genuine and on-target (di-iron DMQ9->UQ9
hydroxylase, COQ metabolon/CoQ-synthome membership, debated nuclear moonlighting "requires
further confirmation", 2,4-DHB bypass showing phenotypes are attributable to UQ deficiency) and
is committed as corroborating context. The review itself is grounded in the UniProt record, the
GOA TSV, and the 11 cached primary publications (PMID_9020081, 10202142, 11244089, 11959146,
12709403, 14517217, 16920626, 17189267, 17277769, 19783783, 25961505); every `supporting_text`
is a verbatim PMID quote. The falcon file is cited only once (core_functions corroboration) with
a verbatim quote from the committed file. There are no UNDECIDED calls.

## Annotation-review plan (core vs non-core)
- CORE (keep, ACCEPT): 3-demethoxyubiquinone 3-hydroxylase (NADH) activity (GO:0160224);
  ubiquinone biosynthetic process (GO:0006744); mitochondrion (GO:0005739); mitochondrial inner
  membrane (GO:0005743); extrinsic component of mitochondrial inner membrane (GO:0031314);
  general MF parents monooxygenase activity (GO:0004497) and oxidoreductase...NAD(P)H one-oxygen
  (GO:0016709) are correct but less-informative parents — keep, flag as non-core/general.
- NON-CORE (KEEP_AS_NON_CORE): determination of adult lifespan (all evidence); cellular
  respiration; oxidative phosphorylation; adult behavior; positive regulation of behavior;
  positive regulation of growth rate; positive regulation of developmental process; response to
  xenobiotic stimulus; regulation of ROS metabolic process; nucleus (all); neg/pos regulation
  of transcription by RNA Pol II; transcription cis-regulatory region binding (debated in-vitro
  mtDNA-binding moonlighting).
- No REMOVE actions: all experimental annotations are defensible; the debated nuclear/DNA
  functions are experimental (IDA/IMP) so are retained as non-core with caveats rather than
  removed.
</content>
</invoke>
