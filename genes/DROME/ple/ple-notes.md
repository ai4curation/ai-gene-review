# ple (pale, tyrosine 3-monooxygenase) notes

Gene: pale (ple), FBgn0005626, CG10118, 65B. UniProt P18459 (Swiss-Prot, 579 aa displayed),
the accession that carries all 40 GOA rows. PANTHER PTHR11473 (aromatic amino acid
hydroxylase), subfamily SF15 (tyrosine 3-monooxygenase). Pterin-dependent aromatic amino acid
hydroxylase: N-terminal regulatory domain with the PKA site Ser32, catalytic domain
(Biopterin_H, PF00351) with iron ligands at 409, 414 and 454 (by similarity).

## Sources and searches (2026-11-17)

- Cached GOA references: 15 PMIDs; full text only for PMID:17585895, 19168633, 19238209,
  21187381, 21455291, 21808060, 28289197. PMID:12957543 (Wittkopp review) and PMID:12000098
  (Billeter review) have no abstract in the cache.
- FlyBase hand-written description (`ple-deep-research-flybase.md`), fetched 2026-11-17.
  No Falcon/Perplexity deep research for this batch.
- PubMed searches run: "Birman novel major isoform tyrosine hydroxylase Drosophila
  alternative" (PMID:7929381); "Friggi-Grelin tissue-specific developmental requirements
  Drosophila tyrosine hydroxylase isoforms" (PMID:12717737); "Friggi-Grelin targeted gene
  expression dopaminergic tyrosine hydroxylase" (PMID:12555273); "Mao Davis eight different
  types dopaminergic neurons mushroom body" (PMID:19597562); "Nassel Elekes aminergic neurons
  blowflies Drosophila tyrosine hydroxylase" (PMID:1346506); "Drosophila tyrosine
  hydroxylase cytosolic" (6 hits; PMID:34732185 relevant); "Drosophila tyrosine hydroxylase
  soluble fraction" (0 hits); "Drosophila tyrosine hydroxylase synaptic vesicle" (4 hits;
  PMID:21985068, Catsup); "Drosophila N-acetyldopamine N-beta-alanyldopamine sclerotization
  dopamine" (PMID:1600191); "Drosophila tan encodes novel hydrolase pigmentation vision"
  (PMID:16299587).
- QuickGO comparator queries (annotation search, human/mouse/rat/fly/worm/zebrafish):
  GO:0001963 exact; GO:0050890 and descendants on fly Ddc, fly Hn, mouse Ddc, Dbh, Tph2,
  Chat and Th; GO:0048067 and GO:0042438 descendants in fly.
- Newly cached: PMID:7929381, 12717737, 12555273, 1346506 (abstracts), PMID:19597562,
  16299587, 34732185 (full text).
- PAINT/PANTHER analysis and isoform segment: `ple-bioinformatics/RESULTS.md`.

## Enzyme

- Cloning; TH activity in heads [PMID:2483109 "The presence of TH enzymatic activity in heads
  was demonstrated."]. The predicted 57,861 Da protein is the 508-residue CNS isoform.
- Both recombinant isoforms are active, iron- and pterin-dependent, feedback-inhibited by
  dopamine and activated by PKA at Ser32 [PMID:10358021 "The recombinant DTH isoforms are
  enzymatically active in the presence of ferrous iron and a tetrahydropteridine
  co-substrate."]; [PMID:10358021 "Site-directed mutagenesis of Ser32, a serine residue
  occurring in a PKA site conserved in all known TH proteins, abolishes phosphorylation of
  both isoforms and activation by PKA."].
- First, rate-limiting step of dopamine synthesis [PMID:12555273 "In Drosophila as in
  vertebrates, the rate-limiting step in DA biosynthesis is catalyzed by the enzyme tyrosine
  hydroxylase (TH)."]; dopamine is the only catecholamine transmitter in flies
  [PMID:12555273 "Dopamine (DA) is the only catecholaminergic neurotransmitter in the fruit
  fly Drosophila melanogaster."].
- Cytosolic zinc inhibits fly TH by competing with Fe2+ [PMID:34732185 "Zinc ion (Zn2+)
  negatively regulates dopamine synthesis through direct inhibition of TH activity, by
  antagonizing Fe2+ binding to TH, thus rendering the enzyme ineffective or non-functional."];
  [PMID:34732185 "From this perspective, the notion that the effect of Catsup mutation on TH
  arises from its cytosolic zinc reduction is reasonable"].

## Isoforms

- Two isoforms from tissue-specific splicing [PMID:7929381 "The major isoform (Type II)
  contains a novel acidic extension of 71 amino acids in the amino-terminal regulatory
  domain"]; [PMID:7929381 "Type I mRNA is present only in the CNS, where it is the primary
  form."]; [PMID:10358021 "Expression of DTH I is restricted to the central nervous system,
  whereas DTH II is expressed in non-nervous tissues like the epidermis."]; [PMID:10358021
  "DTH II specifically contains a very acidic segment of 71 amino acids inserted in the
  regulatory domain."].
- The hypodermal isoform is essential [PMID:12717737 "We show that the embryonic lethality of
  ple can be rescued by expression of the hypodermal, but not the neural, DTH isoform in all
  DA cells, indicating that the hypoderm- isoform is absolutely required for cuticle
  biosynthesis and survival in Drosophila."].
- UniProt P18459: the displayed 579-residue sequence contains the acidic 71-residue segment
  60-130 (23 D/E, 1 K/R; `ple-bioinformatics/RESULTS.md`), so it is DTH II, the hypodermal
  isoform; VSP_000545 (lacking 60-130, 508 aa, 57,862 Da) is DTH I, the neuronal isoform.
  UniProt names them the other way round ("Neuronal" displayed, "Hypodermal" for
  VSP_000545). Source defect recorded on the UniProt reference.

## Localization

- Anti-TH labels dopaminergic neuron somata and their projections in the brain
  [PMID:19597562 "Six clusters of neurons (green) were positive for anti-TH in the posterior
  protocerebrum"]; [PMID:19597562 "Robust anti-TH immunostaining of the medial tips of the
  horizontal lobes (arrow)"] (mushroom-body lobes, i.e. DA neuron terminals). Also
  [PMID:1346506 "In Drosophila, neurons homologous to the blowfly neurons were detected with
  the TH antiserum."].
- No fly subcellular fractionation found (PubMed "Drosophila tyrosine hydroxylase soluble
  fraction", 0 hits). Cytosolic action is inferred from the cytosolic-zinc mechanism
  (PMID:34732185), the absence of signal peptide or transmembrane segments, and vertebrate TH.

## Processes

- Dopamine synthesis in neurons; neural-DA-deficient flies (ple mutant rescued in hypoderm
  only) [PMID:21187381 "We found that DA is absent or below detection limits in the adult
  brain of these flies."]; behaviour [PMID:21187381 "Whereas odor and electrical shock
  avoidance are not affected, aversive olfactory learning is abolished."]; [PMID:21187381
  "Feeding the DA precursor L-DOPA to adults substantially rescues the learning deficit as
  well as other impaired behaviors that were tested."]; spatial orientation memory retained.
- Cuticle tanning [PMID:21808060 "Cuticular tanning processes are initiated by the
  hydroxylation of tyrosine to dopa by tyrosine hydroxylase and the subsequent decarboxylation
  of dopa to dopamine by dopa-decarboxylase (Ddc), which serves as a catechol precursor for
  the synthesis of melanin or derived quinones to tan and strengthen the cuticle matrix ( 23
  )"]; [PMID:21187381 "Because DA is also required in Drosophila as a precursor substrate for
  cuticle sclerotization and melanization, inactivating mutations of the genomic TH , alias
  pale ( ple ) locus, results in unpigmented cuticle and late embryonic lethality ( 19 )"];
  NBAD and NADA from dopamine [PMID:16299587 "Areas of the cuticle that are not melanized
  secrete NBAD, produced by the action of the Ebony protein [2,6], resulting in yellow or light
  tan cuticle, or N-acetyl dopamine, produced by the action of the arylalkylamine
  N-acyltransferases [27], which results in transparent cuticle (J"].
- Wing knockdown (en-GAL4) only lightens the wing blade; no held-out wing [PMID:21808060
  "However, because pale - and Ddc -knockdown flies did not exhibit the held-out wing
  phenotype, dDuox may also be involved in other processes besides sclerotization and
  melanization"].
- Wound response: ple is transcriptionally activated around epidermal wounds, through
  GRH/FOS enhancers, Toll signalling and H2O2 [PMID:28289197 "Our previous studies have shown
  that Duox and hydrogen peroxide act upstream of serine protease(s) for the wound-dependent
  activation of the ple and Ddc genes ( 26 )"].
- Locomotion (ple ts, PMID:12036114), temperature preference (PMID:21455291), male-male
  courtship via male attractiveness (PMID:19238209), tracheal cell migration through dopamine
  control of Btl endocytosis (PMID:17585895).

## Participation check for the non-duplicative IBA process rows

- GO:0006585 dopamine biosynthetic process from tyrosine: ple catalyses step 1 (L-Tyr to
  L-DOPA); Ddc catalyses step 2. ple does part of the work. Inherited from the Ecdysozoa node
  PTN000158597.
- GO:0001963 synaptic transmission, dopaminergic: the definition starts at vesicular release
  of dopamine and covers receptor activation; making the transmitter is a separate process
  (dopamine biosynthesis). Comparator check (QuickGO, GO:0001963 exact, 6 species, 128 rows):
  the term is on TH (mouse IMP, IBA elsewhere), Comt, Snca, Park7, Prkn and Cdk5 (mostly MGI
  IMP), and on dopamine receptors; it is not on DDC, the enzyme of the next synthesis step,
  in any of the six species, nor on the vesicular transporter or the dopamine transporter.
  The single seed, mouse Th, is a mutant-phenotype (necessity) annotation. ple is necessary
  for dopaminergic transmission but performs none of its steps.
- GO:0050890 cognition: also necessity, but the comparator check shows the convention for
  transmitter enzymes: fly Ddc (anesthesia-resistant and long-term memory, IDA/IGI), fly Hn
  (long-term memory, IGI), mouse Dbh (IMP) and mouse Th (learning and memory IMP) carry
  learning/memory terms. In flies, removing neural TH abolishes aversive olfactory learning,
  rescued by L-DOPA (PMID:21187381). Kept as non-core, like the fly behaviour rows.
- GO:0043204 perikaryon: anti-TH labels DA neuron somata (PMID:19597562, 1346506); the
  enzyme is cytosolic. Inherited.

## FlyBase description check

Text: "pale (ple) encodes a cytosolic tyrosine hydroxylase that catalyzes the hydroxylation of
L-tyrosine to form L-dopa, the first and rate-limiting step in the synthesis of dopamine (and
eventually, melanin). Dopamine acts as a neurotransmitter regulating various processes. It is
also a precursor for the synthesis of melanin and the cuticle sclerotization precursors,
N-acetyldopamine (NADA) and N-&bgr;-alanyldopamine (NBAD)."

- Tyrosine hydroxylase, L-Tyr to L-DOPA, first and rate-limiting step: correct
  (PMID:10358021, 12555273).
- Cytosolic: consistent with the cytosolic-zinc inhibition mechanism (PMID:34732185) and with
  vertebrate TH; no direct fly fractionation found.
- Dopamine as neurotransmitter: correct (PMID:12555273, 21187381).
- Melanin, NADA and NBAD from dopamine: correct (PMID:16299587, 21808060, 21187381).
- "&bgr;" is an unrendered HTML entity for beta in the served text.
- Missing: the two tissue-specific isoforms and the essential epidermal role.

## UniProt FUNCTION check

"Plays an important role in the physiology of adrenergic neurons." This is vertebrate text:
flies have no adrenergic neurons (no noradrenaline or adrenaline; dopamine is the only
catecholamine transmitter, PMID:12555273), and the main functions of the fly enzyme are
dopamine synthesis in dopaminergic neurons and L-DOPA/dopamine for cuticle tanning. Source
defect recorded (WRONG_STATEMENT, CONFIRMED). The isoform names are also swapped (above).
