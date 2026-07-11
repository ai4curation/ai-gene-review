# MTR (methionine synthase, METH_HUMAN, Q99707) — review notes

## Environment note
Deep research (`just deep-research-falcon human MTR`) could not run in this worktree:
`scripts/deep_research_wrapper.py` uses `X | None` type syntax that requires Python 3.10+,
but the environment ships Python 3.9.5 (`TypeError: unsupported operand type(s) for |`).
Both the OLS MCP (`No module named 'rich.traceback'`) were also unavailable. No
`-deep-research-*.md` file was fabricated. Review is grounded in the UniProt record
(`MTR-uniprot.txt`), the seeded GOA (`MTR-goa.tsv`), cached publications, and local go.db
term checks via `runoak`.

## Core biology (verified)
MTR is the cytosolic **cobalamin(methylcobalamin)-dependent methionine synthase**
(EC 2.1.1.13), catalysing the folate/B12-dependent remethylation of homocysteine:
(6S)-5-methyltetrahydrofolate + L-homocysteine → (6S)-tetrahydrofolate + L-methionine
[UniProt CATALYTIC ACTIVITY, RHEA:11172; file:MTR-uniprot.txt]. This is the single
reaction that links the folate cycle (consuming 5-methyl-THF, regenerating THF) to the
methionine cycle (regenerating methionine → SAM). It is one of only two cobalamin-dependent
enzymes in humans (the other is MUT, methylmalonyl-CoA mutase).

Mechanism: the methyl group is shuttled via an enzyme-bound cobalamin. In the productive
cycle the methyl of methylcob(III)alamin is transferred to homocysteine (→ methionine +
cob(I)alamin), and cob(I)alamin is re-methylated by 5-methyl-THF (→ methylcob(III)alamin +
THF) [UniProt FUNCTION; Reactome R-HSA-174374, R-HSA-3149539]. Periodically the highly
reactive cob(I)alamin is oxidised to inactive cob(II)alamin; reductive reactivation
(reductive methylation using SAM + electrons) is provided by **MTRR** (methionine synthase
reductase) [UniProt DOMAIN]. MTRR also acts as a chaperone stabilising apoMS and promoting
holoenzyme (Cbl-loaded) formation [PMID:16769880].

Domains (UniProt): Hcy-binding (19–338, contains the catalytic Zn site — Cys/His residues
260/323/324 ligate Zn2+ to activate/deprotonate homocysteine thiol), Pterin-binding
(371–632, binds 5-methyl-THF), B12-binding N-terminal + B12-binding (662–907, binds
methylcobalamin), AdoMet activation domain (923–1265, binds SAM, mediates reactivation and
MTRR interaction). Zn is a genuine catalytic cofactor (thiol activation), not just a
structural metal.

Complex: MTR functions in a cytosolic multiprotein complex with MTRR, MMACHC and MMADHC
that safely shuttles cobalamin toward MTR [UniProt SUBUNIT/FUNCTION; PMID:16769880,
PMID:17288554, PMID:27771510, PMID:23825108].

## Disease
- cblG homocystinuria–megaloblastic anemia (HMAG, MIM 250940): autosomal recessive; loss of
  the homocysteine→methionine conversion → homocystinuria, hypomethioninemia, megaloblastic
  anemia, developmental delay [UniProt DISEASE; PMID:8968736, PMID:8968737].
- Folate-sensitive neural tube defect susceptibility (NTDFS, MIM 601634) associated with the
  common D919G polymorphism [UniProt DISEASE; PMID:12375236].

## Publication cache status
- PMID:16769880 (Yamada 2006) — full text available. hMS EC 2.1.1.13; MSR chaperone/
  aquacobalamin reductase; MSR maintains hMS activity.
- PMID:17288554 (Wolthers 2007) — abstract only. Crystal structure of activation domain;
  cobalamin-dependent enzyme converting homocysteine→methionine by methyl transfer; hMS:MSR
  complex; D963/K1071 important for MSR binding.
- PMID:27771510 (Bassila 2017) — abstract only. MS/MSR interact with MMACHC and MMADHC;
  multiprotein Cbl-processing complex.
- PMID:23825108 (Fofou-Caillierez 2013) — abstract only. cblG mutations in MTR decrease
  conversion of HOCbl→methylcobalamin; MS/MMACHC interaction; MS isoforms.
- PMID:8968737 (Leclerc 1996) — abstract only. cDNA cloning; remethylation of homocysteine
  to methionine in a methylcobalamin-dependent reaction; cblG mutations.

## Annotation-review reasoning highlights
- MF GO:0008705 methionine synthase activity — core; strongly supported (IDA/EXP/IBA/IEA/TAS).
- MF GO:0031419 cobalamin binding — core cofactor; UniProt B12-binding domains + methylcobalamin
  BINDING sites. ACCEPT.
- MF GO:0008270 zinc ion binding / GO:0046872 metal ion binding — genuine catalytic Zn in
  Hcy-binding domain (BINDING 260/323/324). ACCEPT zinc; metal ion binding is a redundant
  generalization → KEEP_AS_NON_CORE.
- CC cytosol (GO:0005829) / cytoplasm (GO:0005737) — verified cytosolic. cytosol is precise
  (ACCEPT); cytoplasm is the less-precise parent (KEEP_AS_NON_CORE).
- BP GO:0071265 L-methionine biosynthetic process, GO:0050667-equivalent homocysteine
  remethylation, GO:0046653 tetrahydrofolate metabolic process, GO:0000096 sulfur amino acid
  metabolic process — all describe facets of the one MTR reaction. Keep the specific
  biosynthetic ones as core; broader ones non-core.
- GO:0009235 cobalamin metabolic process — MTR is a cobalamin-processing enzyme (holoenzyme
  Cbl handling + only source of MeCbl). ACCEPT/KEEP.
- GO:0032259 methylation — MTR is a methyltransferase; broad-but-true. KEEP_AS_NON_CORE.
- GO:0071267 L-methionine salvage — IEA logical inference from GO:0008705; MTR is the *de novo*
  remethylation step, not the 5'-methylthioadenosine salvage pathway. This is an over-broad
  inter-ontology inference → MARK_AS_OVER_ANNOTATED.
- GO:0042558 pteridine-containing compound metabolic process — InterPro IEA; folate/THF is a
  pteridine, so true-but-broad. KEEP_AS_NON_CORE.
- GO:0031103 axon regeneration, GO:0048678 response to axon injury, GO:0071732 cellular
  response to nitric oxide — rat ortholog ISS/IEA electronic transfers; not part of the core
  enzymatic role; peripheral, weak. MARK_AS_OVER_ANNOTATED.
- GO:0007399 nervous system development (TAS PMID:8968737) — the paper is a cloning/mutation
  paper; it does not establish MTR in nervous-system development beyond the neurological
  phenotype of deficiency. Over-broad process attribution. MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515, IPI) — bare; interactors are MMACHC (Q9Y4U1), MTRR (Q9UBK8),
  MMADHC (Q9H3L0). Real and functionally meaningful (Cbl-processing complex) but uninformative
  as "protein binding". Per policy, MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IPI).
