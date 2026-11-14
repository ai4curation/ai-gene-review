# motC (PA1460, G3XD73) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE G3XD73 --alias motC`; accession matches the
worklist. Unreviewed TrEMBL entry, named `motC` by the PAO1 annotation. No deep
research provider key was available; literature is the stator papers used for
motA and motB.

### Identity and literature

- MotA-like protein, three predicted TM helices (UniProt FT TRANSMEM 29..49,
  151..170, 182..203), PF01618 MotA_ExbB + PF20560 MotA_N, PTHR30433:SF3. The
  UniProt family line says exbB/tolQ (RuleBase), reflecting the shared
  ion-channel fold.
- MotCD (PA1460-PA1461) is the second stator
  [PMID:15629949 "The second putative stator was designated MotCD (PA1460-1461)
  based on its lower degree of sequence similarity to MotAB."]. **Caution:**
  Doyle et al. 2004 call this locus *motAB*.
- Single-mutant swarming defect, with complementation
  [PMID:15629949 "In contrast, the Δ motCD mutant can swarm to a degree
  comparable to that of the WT in a relatively low agar concentration (0.45%),
  but not at higher concentrations tested (above or equal to 0.5%)."];
  [PMID:15629949 "The Δ motAB Δ motCD /pMMB66EH- motCD strain swarmed (31.8 ±
  2.5 mm) to a degree comparable to that of the WT (42.2 ± 4.2 mm) on 0.5% agar"].
- Doyle et al. saw the same for PA1460 mutants in PAK and PAO1, with severe
  defects both in semisolid agar and on swarm plates
  [PMID:15375113 "Effects of motor mutations on swarming: MotA, MotB, and MotY
  are necessary to power movement on surfaces."], while swimming speed in liquid
  was near wild type — the locus contributes to, rather than being exclusively
  responsible for, motor function.
- Swimming is also supported: motCD in trans partially complements the swimming
  defect of the double stator mutant
  [PMID:15629949 "The pMMB66EH- motCD plasmid also partially complemented the
  swimming defect of the Δ motAB Δ motCD mutant"], and the double mutant does
  not swim.
- Chemotaxis was assayed directly in the PA1460-PA1461 mutants and is normal
  [PMID:15375113 "Therefore, the radial expansion defect observed for motAB
  strains in semisolid motility agar cannot be attributed to polar effects that
  disturb chemotaxis."], so the InterPro2GO chemotaxis row is an
  over-annotation.
- c-di-GMP context: MotAB may displace MotCD from the motor at high c-di-GMP
  [PMID:25349157 "We propose that when c-di-GMP level is high, the MotAB stator
  can displace MotCD from the motor, thereby affecting motor function."].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001252377 | GO:0071978 bacterial-type flagellum-dependent swarming motility | 2 (G3XD73, Q9HUL1) | 29 (19 taxa) | GO:0071978, IMP, PMID:15629949 (PseudoCAP) | SOUND | Single-mutant swarming defect on 0.5% agar or firmer, with plasmid complementation, for a stator subunit that does part of the work of flagellar rotation. Doyle et al. report the same for PA1460 mutants. | motA (Q9HUL1): weak — the motAB single mutant swarms like wild type (PMID:15629949) or better (PMID:25349157) | No. Without the motC seed the IBD would rest only on the motA rows, whose phenotype is not a swarming requirement. The term is sound for this gene but too specific for the clade, so a GO_CENTRAL WRONG_TERM/REPOINT to GO:0071973 is filed here (PROBABLE), cross-referenced from motA. |

Clade composition checked with `panther_tree.py node PTN001252377 --leaves`:
29 leaves in 19 taxa, all in PTHR30433:SF2/SF3/SF4. The node-level objection is
to the term, not to the leaves. GO:0071978 is_a GO:0071973 (QuickGO) and its
definition adds a lifestyle context, requiring "the smooth movement of a group
of cells along a solid surface". The clade's one experimentally characterised
leaf, E. coli MotA (P09348), carries GO:0071973 by IMP, GO:0015252 proton
channel activity and GO:0120101 stator complex by IPI, and no experimental
swarming annotation; torque generation for flagellar rotation is the shared
role. The earlier version of this note argued from leaf names ("Aquifex,
Thermotoga, Helicobacter, Leptospira and Rhodopirellula have not been shown to
swarm"); that claim is withdrawn as absence of evidence. What was checked
instead is the annotation state: in QuickGO (2026-11-06) every GO:0071978 row
on the 24 non-PAO1 leaves is IBA or IEA. The same node also carries an E. coli
MotA-seeded (P09348) IBD of GO:0120101 stator complex, which is sound and suits
the whole clade.

## Decisions summary

- ACCEPT: swarming motility (IMP, IBA, IEA), stator complex (IBA), plasma
  membrane (IEA).
- MODIFY: flagellum-dependent cell motility (IMP) -> swimming + swarming
  (both specific descendants are supported); membrane (IEA) -> plasma membrane.
- MARK_AS_OVER_ANNOTATED: chemotaxis (IEA, InterPro2GO).
- Counts: ACCEPT 5, MODIFY 2, MARK_AS_OVER_ANNOTATED 1.
- Defects: GO_CENTRAL 1 (PTN001252377 WRONG_TERM, REPOINT to GO:0071973,
  PROBABLE). PSEUDOCAP 0 — the motC seed row is sound.

## Leaf evidence check (2026-11-06)

Audit of the `GO_CENTRAL` defect on PTN001252377. The previous explanation
argued that "the leaves include Aquifex, Thermotoga, Helicobacter pylori,
Leptospira and Rhodopirellula stator proteins, which have not been shown to
swarm". Leaf membership is correct (`panther_tree.py node PTN001252377
--leaves`), but the claim itself is absence of evidence, and three of the five
names are submitter `SubName`s. **The leaf list has been dropped from the
entry.**

| Leaf | Name and its evidence | Experimental annotations found | Verdict |
|---|---|---|---|
| O67122 (Aquifex aeolicus motA) | Curated `RecName` "Motility protein A"; PE 1 | None. `GO:0120101` IBA, `GO:0071978` IBA, `GO:0006935` IEA only | Claim dropped — no evidence either way |
| Q9WZE3 (Thermotoga maritima TM_0676) | `SubName` ECO:0000313|EMBL:AAD35759.1 — submitter name, unvetted | None (IBA/IEA only) | Claim dropped |
| P65410 (Helicobacter pylori motA) | Curated `RecName`; PE 3 (inferred from homology) | None (IBA/IEA only) | Claim dropped |
| Q8F0B9, Q8F896 (Leptospira interrogans) | `SubName` "Endoflagellar motor protein A" ECO:0000313|EMBL — submitter names | None (IBA/IEA only) | Claim dropped |
| Q7ULV0 (Rhodopirellula baltica pomA) | `SubName` "Chemotaxis pomA protein" ECO:0000313|EMBL | None (IBA/IEA only) | Claim dropped |
| P09348 (E. coli motA) | Curated `RecName`; PE 1 | `GO:0071973` IMP:EcoliWiki; `GO:0120101` IPI:ComplexPortal; `GO:0005886` IDA:EcoCyc; `GO:0015252` proton channel activity TAS:EcoCyc. `GO:0071978` only IBA | **New load-bearing leaf.** The clade's one experimentally characterised member has the parent term by IMP and no experimental swarming annotation |

Replacement argument, as now written in the entry: GO:0071978 `is_a`
GO:0071973 (QuickGO), and its definition adds a lifestyle context — "the
smooth movement of a group of cells along a solid surface", and "Swarming
motility is observed in groups of bacteria". What a MotA-family protein
contributes is the ion-channel stator that generates torque, which is what
P09348's experimental annotations show. Whether an organism swarms depends on
surfactant, cell density and growth conditions, not on which stator it
encodes. One checked annotation-state fact replaces the behavioural absence
claim: in QuickGO (2026-11-06) every `GO:0071978` row on the 24 non-PAO1
leaves is IBA or IEA, so no leaf besides the two P. aeruginosa seeds has
experimental support for the specific term.

Confidence unchanged at PROBABLE. The weak behavioural claim was withdrawn and
replaced with verified ones, but the call remains a term-scoping
recommendation that a PAINT curator could reasonably answer differently, so
CONFIRMED would overstate it.
