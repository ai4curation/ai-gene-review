# PA5134 (Q9HU50, CtpA) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL), cached
abstracts of PMID:21204920, PMID:24082078 and PMID:24928312 (none with full text).
PubMed and Europe PMC searches failed on 2026-11-05 (server errors), so later CtpA
literature could not be retrieved.

## Function

- PA5134 is CtpA, one of two carboxyl-terminal processing proteases (CTPs, peptidase S41A)
  in PAO1, the other being Prc (PA3257)
  [PMID:24082078 "The P. aeruginosa genome encodes two CTPs annotated as PA3257/Prc and PA5134/CtpA in strain PAO1."].
- CTPs are serine proteases
  [PMID:21204920 "Carboxy (C)-terminal processing proteases (CTP) are a relatively new group of serine proteases."].
- Periplasmic location by fractionation
  [PMID:21204920 "We show for the first time the subcellular localization of a CTP-3 family protein from Pseudomonas aeruginosa, named CtpA, in the periplasm"];
  [PMID:24082078 "We have now found that endogenous CtpA is a soluble periplasmic protein"].
- Mutant phenotypes: altered envelope, defective T3SS, attenuated virulence; overexpression
  induces an ECF sigma factor regulon
  [PMID:24082078 "a ctpA null mutant has specific phenotypes consistent with an altered cell envelope"];
  [PMID:24082078 "CtpA is essential for the normal function of the type 3 secretion system (T3SS)"].
- Signal peptide 1-23 (SignalP); PDZ domain 93-161; Peptidase_S41 (PF03572); PANTHER PTHR32060:SF30 (CtpA).

## PMID:24928312 is a Staphylococcus aureus paper

PseudoCAP cites PMID:24928312 for three PA5134 rows (IDA signal transduction, IDA cell wall
biogenesis, ISS serine-type endopeptidase with E. coli Prc P23865). The abstract is about
the S. aureus CtpA only
[PMID:24928312 "Our results represent the first characterization of a C-terminal processing protease in a pathogenic Gram-positive bacterium"].
It cannot provide IDA evidence for a P. aeruginosa protein, and it reports neither signal
transduction nor cell wall biogenesis (it reports cell-wall localisation, stress sensitivity
and virulence). The two IDA rows are removed with CONFIRMED PSEUDOCAP WRONG_REFERENCE
defects. The ISS row's term (serine-type endopeptidase) is correct from family membership, so
it is accepted; only its reference is odd.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001279639 | GO:0007165 signal transduction | 3 | 58 (32 taxa) | GO:0007165 signal transduction, IDA, PMID:24928312 (PseudoCAP) | WRONG | The cited paper is about S. aureus CtpA and reports no signalling role; no P. aeruginosa CtpA paper seen here shows one. PSEUDOCAP WRONG_REFERENCE, CONFIRMED. | B. subtilis CtpB O35002 (SpoIVFA cleavage in sigma-K activation); P. aeruginosa Prc Q9HYY3 (PMID:24373018, cell-surface signalling; reviewed in this batch, seed SOUND) | Partly. The two remaining seeds support signal transduction for their own proteins, so the IBD is not baseless, but they are paralogous CTP lineages that each acquired a signalling role. Placed at their common ancestor, the term reaches CtpA-type members (PA5134) and E. coli Prc/Tsp (P23865), which have no signalling role on record. GO_CENTRAL defect recorded here (now CONFIRMED after the tree check, CHECK): drop Q9HU50 from WITH/FROM and move the term to the subfamily nodes that support it. |

Cross-reference: prc (PA3257, Q9HYY3) seeds the same node term; its seed is SOUND, and the
node-level defect is recorded once, here, as PA5134 has the decisive (wrong-reference) evidence.

Defects recorded: PSEUDOCAP 2 (WRONG_REFERENCE x2, CONFIRMED); GO_CENTRAL 1 (OTHER on
PTN001279639, CONFIRMED, CHECK).

## PANTHER tree check (2026-11-05)

Topology of PTN001279639 in PTHR32060 fetched with `projects/PSEUDOCAP/panther_tree.py node
PTN001279639 --depth 3`, then `--contains` for each seed and `--family PTHR32060` for the subclades.
The node is a **DUPLICATION** with 58 leaves spanning three subfamilies (SF22 9, SF29 2, SF30 47) and
exactly two children.

| Node | Event | Leaves | Subfamilies | Contents | Verdict |
|---|---|---|---|---|---|
| **PTN004918760** | SPECIATION (Eubacteria) | 9 | SF22 | Prc / tail-specific proteases: *Rhodopirellula* prc + PTN000786025 | signalling supported (Prc lineage) |
| &nbsp;&nbsp;PTN000786025 | SPECIATION (Gammaproteobacteria) | 8 | SF22 | *Haemophilus*, *Shewanella*, *Vibrio*, *Xanthomonas* prc; **PAO1 Prc Q9HYY3**; PTN002078873 (Enterobacteriaceae, incl. **E. coli Prc/Tsp P23865**) | smallest clade holding both Prc seeds |
| **PTN008644010** | SPECIATION (Eubacteria) | 49 | SF29 + SF30 | the CtpA branch (Terrabacteria, Cyanobacteria, Bacteroidetes, PVC, Proteobacteria ...) | no signalling evidence except CtpB |
| &nbsp;&nbsp;PTN002078920 | SPECIATION (Bacillus) | 2 | SF29 | **B. subtilis CtpB O35002**, *B. cereus* BC_5184 | signalling supported (CtpB) |
| &nbsp;&nbsp;PTN002078922 | SPECIATION (Gammaproteobacteria) | 6 | SF30 | *Coxiella*, *Shewanella*, three *Xanthomonas*, **PA5134 Q9HU50 (PTN002424651)** | no signalling evidence |

`--contains Q9HYY3,P23865` returns PTN000786025 (8 leaves); `--contains O35002,Q9HU50` returns
PTN008644010 (49 leaves). So the two sound seeds sit on **opposite sides** of the duplication that
defines PTN001279639, which is exactly why the IBD landed at the family root and reaches all 58
leaves. B. subtilis CtpA (O34666) is a separate SF30 leaf in the same Firmicutes clade as CtpB's
SF29 pair, so even within Bacillales the signalling role belongs to the CtpB subfamily, not to
CtpA-type proteases.

Verdict: concern CONFIRMED, raised from SUSPECTED (topology is primary data checked here). Requested
fix in the defect: drop Q9HU50 from the WITH/FROM (its seed row is mis-referenced - note that a gene
appearing in its own WITH/FROM is not in itself circular), and move GO:0007165 to PTN000786025 (or
PTN004918760) for the Prc lineage and PTN002078920 for CtpB, removing it from PTN001279639.
