# fabL (Bacillus subtilis 168, UniProtKB:P71079) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml`, where FabL is the
representative of the NADPH-dependent enoyl-ACP reductase variant of the
enoyl-reduction step. Only cached, citable sources were used; the two primary
papers are abstract-only in `publications/`, so every quote in the review comes
from those abstracts or from the reviewed UniProt record.

## What FabL is

FabL (originally the uncharacterized ORF *ygaA*) is the second enoyl-ACP
reductase of *B. subtilis*. It reduces the C=C bond of an ACP-linked enoyl
thioester with NADPH, the last reaction of each FAS-II elongation round
[PMID:11007778 "The purified YgaA protein catalyzed the NADPH-dependent reduction
of trans-2-enoyl thioesters of both N-acetylcysteamine and ACP."]. The reviewed
UniProt entry records the same reaction with experimental evidence from that
paper, as EC 1.3.1.104
[file:BACSU/fabL/fabL-uniprot.txt "Reaction=a 2,3-saturated acyl-[ACP] + NADP(+) = a (2E)-enoyl-[ACP] +"],
with KM = 16 uM for NADPH
[file:BACSU/fabL/fabL-uniprot.txt "KM=16 uM for NADPH"].

The name marks a new enoyl-reductase family rather than a FabI variant: the
protein has only ~24% identity to FabI and is structurally closer to FabG and the
rest of the SDR superfamily, while placing the Tyr-(Xaa)6-Lys catalytic dyad in
essentially the FabI position
[PMID:21185310 "The positions of the catalytic dyad of Tyr-(Xaa)(6)-Lys in FabL are almost identical to that of FabI, but a detailed structural analysis shows that FabL shares more structural similarities with FabG and other members of the SDR (short-chain alcohol dehydrogenase/reductase) family."].
Both FabI and FabL are homotetramers
[file:BACSU/fabL/fabL-uniprot.txt "SUBUNIT: Homotetramer."].

## Redundancy with FabI, and triclosan

FabI and FabL cover the same essential step: either single knockout is viable,
the double knockout was not obtained
[PMID:11007778 "Single knockouts of the ygaA or fabI gene in B. subtilis were viable, but double knockouts were not obtained."],
and FabL expressed in *E. coli* rescues a *fabI*(Ts) strain
[PMID:11007778 "Expression of YgaA complemented the fabI(ts) defect in E. coli and conferred complete triclosan resistance."].
The two differ in drug sensitivity: triclosan is only a reversible inhibitor of
FabL and does not trap the stable enzyme-NAD(+)-triclosan ternary complex that
makes FabI the drug's target
[PMID:11007778 "YgaA was reversibly inhibited by triclosan, but did not form the stable ternary complex characteristic of the FabI proteins."],
which is why the *ygaA* knockout is 250-fold more triclosan-sensitive than wild
type. This is the reason FabL is modelled as a distinct cofactor/family variant of
the enoyl-reduction step and not as an interchangeable FabI.

## Annotation decisions

- `GO:0141148` enoyl-[acyl-carrier-protein] reductase (NADPH) activity: core,
  ACCEPT on both the EXP and the electronic row (they agree).
- `GO:0004318` enoyl-[acyl-carrier-protein] reductase (NADH) activity (IDA,
  PMID:11007778): MODIFY to `GO:0141148`. The enzymology in the cited paper is
  NADPH-dependent, and the same entry's curated reaction lines (ECO:0000269 from
  the same paper) are written with NADPH. This is a cofactor correction, not a
  refinement; the NADH-preferring reductase of *B. subtilis* is FabI, a different
  protein. Recorded as a `WRONG_TERM` source defect against UniProt with
  `confidence: PROBABLE` — the NADPH-specific child term did not exist in 2011
  when the row was made, so this is most likely a pre-term-split legacy row rather
  than a misreading.
- `GO:0016616` oxidoreductase activity, acting on the CH-OH group of donors (IBA
  from PANTHER node PTN002449287): REMOVE. The node's seeds are CH-OH-donor SDRs
  (E. coli FabG P0AEK2, human HSD17B8 Q92506); FabL keeps the fold but reduces a
  C=C bond. This does not overrule the family: the `PTHR43639` review already
  excepts P71079 by name from its GO:0016616 term assessment
  [file:interpro/panther/PTHR43639/PTHR43639-review.yaml "FabL reduces the C=C double bond of enoyl-ACP (EC 1.3.1.104, CH-CH donor)."].
- `GO:0030497` fatty acid elongation and `GO:0006633` fatty acid biosynthetic
  process: both ACCEPT. The specific elongation term is the core process; the
  broader biosynthesis term is the pathway the step belongs to, and the two rows
  are consistent rather than duplicative.
- `GO:0050661` NADP binding (IDA, PMID:21185310): KEEP_AS_NON_CORE — a real
  property shown by the ternary-complex structure and the kinetics, but it is the
  cofactor half of the catalysed reaction, not a separate function.

## Open question

FabI and FabL have opposite nucleotide preferences (NADH vs NADPH) for the same
essential step. Whether they partition the flux by cofactor availability across
growth phases, or are simply interchangeable, is not established — hence the
suggested experiment on acyl-ACP profiles and NAD(P)H pools in the single
deletions.
