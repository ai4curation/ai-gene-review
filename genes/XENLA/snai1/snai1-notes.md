# snai1 (Snail1, Xsna; P19382) — Xenopus laevis — review notes

Project: NEURAL_CREST_ORIGINS (Tier 3, blastula programme retained in the crest).
Reviewed 2026-10-07. Read alongside `genes/XENLA/snai2/` (paralog; Tier 1).

## Identity

- P19382 = snai1.L (Xenbase XB-GENE-17344016, chr 9_10L); 259 aa, N-terminal SNAG repression
  motif, five C-terminal C2H2 zinc fingers [file:XENLA/snai1/snai1-uniprot.txt "Belongs to the
  snail C2H2-type zinc-finger protein family."]. The S homeolog snai1.S is TrEMBL A0A1L8ELB6 and
  carries only ARBA IEAs (QuickGO, 2026-10-07).
- Cloned as the frog homologue of Drosophila snail [PMID:2226210 "We have cloned a Xenopus cDNA
  that is related to snail, a gene that is required for mesoderm formation in Drosophila."].
- UniProt function: "Transcriptional repressor. Acts upstream of snai2/slug, zic5 and other neural
  crest markers in the specification of the neural crest and neural crest migration. Involved in
  embryonic mesoderm formation." [file:XENLA/snai1/snai1-uniprot.txt]

## Expression (where / when)

- Maternal (vegetal) and zygotic from stage 9; induced in caps by mesoderm inducers
  [PMID:2226210 "xsna is not present in isolated animal caps but can be induced by the
  mesoderm-inducing factors XTC-MIF and bFGF."].
- All early mesoderm, then tissue-specific down-regulation [PMID:8305705 "Like its homologue snail
  in Drosophila, Xsna is expressed zygotically in all early mesoderm."].
- Ectoderm from stage 11, in the arc that defines the border, then prospective crest (deep layer)
  and roof plate (superficial) [PMID:8305705 "Xsna is also expressed in the prospective neural fold
  ectoderm from stage 11 in a low arc above the dorsal marginal zone, precisely identifying a
  distinct band of cells that surrounds the prospective neural plate that we designate the neural
  plate border."]; persists in migrating crest [PMID:8305705 "Xsna expression persists in the neural
  crest during migration and in some derivatives at least until metamorphosis"].
- Precedes slug in the crest [PMID:12490555 "in Xenopus, Snail precedes Slug expression in this
  population"]; [PMID:24360906 "Snail1 is expressed in the mesoderm during gastrulation and starts to
  be expressed at the neural border along with snail2 at stage 11"].
- Blastula animal-pole (pluripotent) cells co-express Snail1 with Oct/Sox/Vent factors
  [PMID:25931449 "We found that Id3, TF-AP2, Ets1, FoxD3 and Snail1 were co-expressed with the core
  pluripotency factors"].

## Upstream inputs (network position)

- First-wave target of Pax3/Zic1 [PMID:23509273 "Indeed, a group of early genes ( snail1 , sox8 ,
  and myc ) was activated during early neurulation"].
- Direct Zic1 target: cycloheximide-resistant induction and EMSA on a conserved upstream element
  [PMID:24360906 "were highly and reproducibly activated either by Pax3 (snail2, twist1) or by Zic1
  (snail1) in the presence of cycloheximide"]; [PMID:24360906 "Zic1 binds to snail1 putative
  oligonucleotide"]; [PMID:24360906 "Zic1 is essential for snail1 induction at the neural border"].
  So snai1 sits one step *below* the border specifiers.

## Molecular activity

- Repressor: Engrailed-repressor fusion of the zinc fingers mimics Snail, E1A-activator fusion
  inhibits (Aybar Fig. 8, via deep research); abstract [PMID:12490555 "We show that Snail is
  required for neural crest specification and migration and that it works as a transcriptional
  repressor."].
- Corepressors: Ajuba LIM proteins (Ajuba, LIMD1, WTIP) via SNAG [PMID:18331720 "Here, we identify
  the Ajuba family of LIM proteins as functional corepressors of the Snail family via an
  interaction with the SNAG domain."]. These are the GOA IPI partners (Xenopus limd1 Q06BR1; mouse
  Wtip Q7TQJ8, Ajuba Q91XC0, Limd1 Q9QXD8; identities checked against UniProt REST 2026-10-07)
  -> MODIFY protein binding to GO:0001222 transcription corepressor binding (same term snai2 got).
- Elp3 (Q5HZM6) IPI: Elp3 binds the zinc-finger region and blocks beta-Trcp ubiquitination,
  stabilising Snail1 [PMID:27189455 "Thus, we favor the model that Elp3 binds and stabilizes
  Snail1, which is required for the transactivation of mesenchymal genes."]. Upstream regulation of
  Snail1 protein, not a Snail1 activity -> REMOVE generic protein binding (as for snai2).
- No ChIP-level direct target in frog. Responsive genes: Delta1 [PMID:14681193 "At the early
  gastrula stage, the coordinated action of Xiro1, as a positive regulator, and Snail, as a
  repressor, restricts the expression of Delta 1 at the border of the neural crest territory."],
  Bmp4 (deep research). Mammalian SNAI1 represses E-cadherin directly (not re-annotated here).

## Gain of function

- Sufficient (inducible GR construct) to induce all crest markers tested in embryos and in naive
  caps, without neural-plate or mesoderm markers [PMID:12490555 "We show that Snail is able to induce
  the expression of Slug and all other neural crest markers tested (Zic5, FoxD3, Twist and Ets1) at
  the time of specification."]; [PMID:12490555 "This activation is observed in whole embryos and in
  animal caps, in the absence of neural plate and mesodermal markers."]. Slug cannot do this
  [PMID:12490555 "Slug alone is unable to induce other neural crest markers in animal cap assays"].
  -> Snai1 has *stronger* specifier credentials by gain of function than Snai2.

## Loss of function

- Dominant-negative / inducible constructs: required for specification and migration; Slug rescues
  dn-Snail, so Snail is upstream of Slug [PMID:12490555 "Snail lies upstream of Slug in the genetic
  cascade leading to neural crest formation"].
- Blastula: blocking Snail1 in animal cells loses pluripotency factors and competence to form
  mesoderm and endoderm [PMID:25931449 "Blocking Snail1 function in the animal pole of blastula
  embryos cells led to loss of expression of factors linked to the neural crest state"]. This is a
  competence role, not crest specification.
- Caveat: no clean null (MO/CRISPR) for snai1 in frog; reagents (dn zinc-finger constructs) would
  hit both homeologs and probably Snai2 targets.

## Layer placement (synthesis)

Snail1 occupies TWO layers, sequentially:
1. **Competence factor (blastula)**: co-expressed with, and required to maintain, the
   pluripotency network; shared with the crest (Buitrago-Delgado 2015). Same layer as myc-a / id3-a.
   No GO term fits (stem cell population maintenance GO:0019827 raised as a question, as for id3-a).
2. **Earliest crest specifier**: direct Zic1 target in the first wave (with sox8, myc), upstream of
   snai2, foxd3, twist, ets1; sufficient in caps; required for specification. -> `GO:0014036`.
   Not a border specifier: it is downstream of Pax3/Zic1 and its activity induces crest rather
   than border identity; its early stage-11 "border" expression (Essex 1993) reflects how early it
   is activated, not a border-patterning activity.
3. Later: migration (dn-Snail at stage 16 reduces migration; Elp3-stabilised Snail1 needed for
   migration) -> `GO:0001755` kept, core-ish (EMT effector face).

Non-core: mesoderm formation / gastrulation (expressed in all early mesoderm; mouse Snai1 carries
GO:0001707 by IMP), not annotated in frog — no snai1-specific frog functional evidence; raised as a
question. EMT generically (GO:0001837) not added; the crest-migration term covers the frog data.

Module: belongs in `neural_crest_fate_specification` (as a Snail-paralog annoton beside snai2, or a
Snail variant set) AND in `progenitor_competence_maintenance` (one annoton per role). Edge:
zic1_border -> snai1_spec (direct, EMSA); snai1_spec -> snai2_spec (epistasis).

## Comparator checks (QuickGO, 2026-10-07)

Query 1: `annotation/downloadSearch?goId=GO:0014029,GO:0001755,GO:0014032,GO:0014033&goUsage=descendants&goUsageRelationships=is_a,part_of`
(46,708 rows), grep for Snail-family symbols:
- Experimental NC-branch rows on Snail family exist only for frog snai1 (P19382: GO:0014036 IMP,
  GO:0001755 IMP), frog snai2 (Q91924: IMP/IGI/IDA) and human SNAI2 (O43623: GO:0014032 IMP,
  PMID:12444107).
- Mouse Snai1 (Q02085), human SNAI1 (O95863), zebrafish snai1a/snai1b: **no** NC-branch term by any
  evidence. All other hits are ARBA (GO_REF:0000117) or Ensembl-Compara (GO_REF:0000107) IEAs.
- So Snai1 crest annotation is frog-only. This is partly a coverage gap and partly biology:
  in mouse, Snail rather than Slug is in premigratory crest [PMID:12490555 abstract], yet no mouse
  crest annotation exists for Snai1. Not used to justify any NEW term.
Query 2: `annotation/downloadSearch?geneProductId=Q02085,O95863`:
- Both carry GO:0001227 (IDA, IBA); mouse Snai1 carries GO:0001707 mesoderm formation (IMP) and
  GO:0001837 EMT; neither carries GO:0001222. Supports NEW GO:0001227 for frog snai1 (frog evidence:
  repressor fusion mimicry).

## Evolution / outgroups

- Amphioxus: Snail is the one crest specifier at the border [PMID:18562679 "The single exception was
  amphioxus Snail , which is transiently expressed at the neural plate border in the early neurula
  stage."] -> Snail border expression ancestral to chordates.
- Lamprey: one snail gene [PMID:39060477 "the lamprey genome encodes a single snail ortholog (11),
  which has affinities to both snai1 and snai2"], expressed in animal-pole cells and at the
  border/crest [PMID:39060477 "were all expressed in lamprey animal pole cells"], with flat dynamics
  [PMID:39060477 "or were maintained at similar levels across stages (klf17, snail, myc)"], whereas
  Xenopus snai2 rises monotonically like a definitive crest factor.
- Interpretation (subfunctionalisation): the single cyclostome snail combines blastula + border/crest
  expression. After the gnathostome duplication, frog snai1 kept the blastula/competence + earliest
  border-crest expression (the lamprey-like pattern), while snai2 took the definitive crest
  specifier / EMT dynamics. Mouse shows the reverse paralog usage in premigratory crest (Snail, not
  Slug), so which paralog leads in the crest is lineage-specific (as for SoxE).

## Decisions summary

- 21 GOA rows: ACCEPT 15, MODIFY 5 (protein binding -> GO:0001222 x4; TAS GO:0014029 ->
  GO:0014036), REMOVE 1 (Elp3 protein binding). + NEW GO:0001227 (IDA PMID:12490555).
- PMID:15242799 (Id2 cardiac crest paper) is again the AgBase TAS source; miscited (as for snai2,
  twist1).
