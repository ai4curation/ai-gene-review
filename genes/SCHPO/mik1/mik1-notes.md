# mik1 (S. pombe, UniProt P30290, PomBase SPBC660.14) — curation notes

## Identity

- Mitosis inhibitor protein kinase Mik1; 581 aa; protein kinase domain 289-561, ATP-binding Lys320,
  catalytic Asp417 (UniProt features). Belongs to the Ser/Thr kinase superfamily, WEE1 subfamily;
  PANTHER PTHR11042:SF190; CDD cd14052 "PTKc_Wee1_fungi".
- Paralogue of wee1 (SPCC18B5.03); orthologous group also contains S. cerevisiae SWE1.
- Deletion viable (PomBase). UniProt PE level 3 despite the direct biochemistry in PMID:7982971.

## Core biology

- Discovery: mik1 cloned as a wee1-related 66 kDa kinase [PMID:1706223 "We show here that a related 66 kd
  kinase, called mik1, acts redundantly with wee1 in the negative regulation of cdc2 in S. pombe."].
  Null is silent; double mutant is lethal [PMID:1706223 "A null allele of mik1 has no discernible phenotype,
  but a mik1 wee1 double mutant is hypermitotically lethal"] and Cdc2 loses Tyr phosphate in the absence of
  both kinases [PMID:1706223 "In the absence of mik1 and wee1 activity, cdc2 rapidly loses phosphate on
  tyrosine"]. PomBase phenotype from the same paper: mik1 overexpression gives viable elongated cells
  (FYPO:0001492), i.e. Mik1 dosage delays mitotic entry.
- Direct activity: Mik1 immunoprecipitates from insect cells and S. pombe phosphorylate Cdc2 Tyr15; the
  K320R kinase-dead mutant does not; activity co-elutes with monomeric ~68 kDa Mik1 after gel filtration
  [PMID:7982971 "Immunoprecipitates of Mik1 from both sources catalyzed the phosphorylation of p34cdc2 on
  tyrosine 15 whereas immunoprecipitates of a kinase-deficient mutant of Mik1 were negative in this assay."
  "The tyrosine 15 kinase activity co-eluted with the 68 kDa form of Mik1."]. This is the only characterised
  substrate residue; no physiological Ser/Thr substrate is known (UniProt's "acts both on serines and on
  tyrosines" is a family-level statement).
- Cell-cycle regulation: mik1 is an MBF target with an MCB in its promoter (PomBase: "promoter contains MCB",
  PMID:14648198; transcription activated by Cdc10/MBF, PMID:18662996 [PMID:18662996 "mik1 , encoding a
  mitosis-inhibiting kinase"]). Mik1 protein and mRNA peak around S phase and the protein is short-lived
  and ubiquitinated [PMID:10637286 "Mik1 protein and mRNA oscillate during the unperturbed cell cycle, with
  peak amounts detected around S phase." "Ubiquitinated Mik1 accumulates in a proteasome mutant, which
  indicates that Mik1 normally has a short half-life."]. Mik1 phosphorylates Cdc2 Y15 as cells pass through
  S phase [PMID:26131711 "In S.pombe, Y15 is also modified by Mik1 kinase when cells progress through S phase"].
- Replication checkpoint: PomBase records (PMID:9572736, Boddy et al. 1998) that Mik1 protein level is
  increased in HU and that this increase is lost in cds1 and rad3 disruptants (gene-expression annotations
  "affected by mutation in" cds1/rad3). The deep-research summary agrees: replication arrest increases mik1
  mRNA and stabilises the protein in a Cds1-dependent manner. mik1 deletion combined with loss of
  Cdc25/14-3-3 binding almost completely bypasses the replication checkpoint [PMID:10523629 "Here we show
  that a more complete disruption of Cdc25/14-3-3 interactions coupled with mik1 + deletion results in an
  almost complete bypass of the DNA replication checkpoint."] — Mik1 and Cdc25 inhibition are parallel arms.
- DNA damage checkpoint: G2 arrest depends on Cdc2 Tyr phosphorylation by Wee1 and Mik1 [PMID:9042863 "the G2
  DNA damage checkpoint arrest in S. pombe depends on the inhibitory tyrosine phosphorylation of Cdc2 carried
  out by the Wee1 and Mik1 kinases"]. Mik1 is positively regulated by the checkpoint [PMID:10637286 "Mik1 is
  required for checkpoint response in strains that lack Cdc25." "Long-term DNA damage checkpoint arrest fails
  in Deltamik1 cells." "DNA damage increases Mik1 abundance in a Chk1-dependent manner."]. PomBase phenotypes
  from PMID:9042863: mik1Δ wee1-50 shows premature mitosis and a decreased duration of the IR-induced G2
  checkpoint.
- Meiosis: the Cds1-dependent meiotic replication checkpoint maintains Cdc2 Tyr15 phosphorylation
  [PMID:10521402 "When DNA replication is blocked, the checkpoint maintains Cdc2 tyrosine 15 phosphorylation
  keeping Cdc2 protein kinase activity low and preventing onset of meiosis I."], assayed with a pat1 mik1Δ
  wee1-ts strain lacking both Tyr15 kinases. Kakui et al. 2015 (full text cached): mik1Δ wee1-50 at 32 °C
  enters nuclear division shortly after horsetail movement stops, shortens horsetail duration to 15-25 min
  even in HU, and overrides the checkpoint [PMID:25492408 "These results indicate that inactivation of
  Mik1/Wee1 overcomes the DNA replication checkpoint."]; csn1Δ mik1Δ wee1-50 is inviable.
- Stability: Mik1 associates via its kinase domain with the Hsp90/Wos2/Cyp40 complex and is degraded when
  Hsp90 is impaired (deep research, Goes & Martin 2001, PMID:11298745 per PomBase physical-interaction
  records with swo1 and wos2). Not cached locally; not used for annotation decisions.
- Localisation: ORFeome YFP screen (PMID:16823372) records nucleus + cytosol. Deep research (citing a thesis)
  reports nuclear accumulation in S phase / HU arrest that is lost in checkpoint mutants. No cell-cycle-resolved
  imaging of endogenous Mik1 is cached, so localisation is graded as moderate confidence.

## Annotation decisions (summary)

- MF: protein tyrosine kinase activity (IDA, IBA) ACCEPT — core. protein kinase activity (IEA) and ATP
  binding (IEA) ACCEPT. protein serine/threonine kinase activity (IEA, EC 2.7.11.1) KEEP_AS_NON_CORE
  (dual-specificity family, no physiological Ser/Thr substrate). protein serine kinase activity (IEA, Rhea)
  MODIFY -> GO:0004674 per the term's own usage note (same treatment as SWE1 and PKMYT1).
- BP: negative regulation of G2/M transition of mitotic cell cycle (IBA; IGI with wee1; IGI with nrm1)
  ACCEPT. The nrm1 IGI (PMID:25533348) is abstract-only locally and the abstract does not mention mik1; the
  PomBase phenotype record (mik1Δ nrm1Δ: normal vegetative cell length) shows the curators read a suppression
  of the nrm1Δ elongation by mik1 loss, consistent with mik1 being an MBF/Nrm1-repressed target — deferred to
  the curator, ACCEPT. negative regulation of G2/MI transition of meiotic cell cycle (IBA, IMP) ACCEPT —
  genuine meiotic effector role, not an expression-based "mug" annotation. signaling (NAS, keyword mapping)
  MODIFY -> GO:0010972: root-level, uninformative, already subsumed by specific signalling-pathway terms.
- CC: nucleus (HDA, IBA) ACCEPT. cytoplasm (IBA, family node includes eIF2-alpha kinases) and cytosol (HDA)
  KEEP_AS_NON_CORE — observed, not wrong, but the site of Cdc2 inhibition is the nucleus.
- No NEW annotations proposed. Checkpoint-signalling terms (GO:0033314, GO:0044773) are used only in
  core_functions as synthesis. Comparator check (QuickGO, taxon 4896): GO:0044773 is carried by wee1 (IGI
  with chk1, PMID:12186947), chk1, cdc2, cdc13, crb2, rad3, rad9, rad4, tel1; GO:0033314 by rad3, cds1, mrc1,
  rad24 (IMP PMID:10523629 — the same paper in which mik1Δ + Cdc25 14-3-3 mutant bypasses the replication
  checkpoint), rad1/9/17/hus1, hsk1 etc. The effector (wee1/cdc2/cdc13) is annotated for the damage
  checkpoint, so mik1 would be in the same role; but PomBase curated PMID:10523629 and PMID:10637286 without
  adding a checkpoint term to mik1, so this is raised in suggested_questions rather than asserted as NEW.
  The two validator warnings about these core_functions terms are therefore expected.

## Comparators

- S. pombe wee1 review (genes/SCHPO/wee1): same IBA rows graded the same way; Ser/Thr rows ACCEPT there
  because wee1 has direct dual-specificity biochemistry (PMID:1372994), which mik1 lacks.
- S. cerevisiae SWE1 review (genes/yeast/SWE1): EC row KEEP_AS_NON_CORE, Rhea serine row MODIFY, cytoplasm
  IBA KEEP_AS_NON_CORE, meiotic G2/MI IBA ACCEPT — followed here.
- Human PKMYT1: Rhea serine row MODIFY -> GO:0004674.

## Open questions

- Direct Cds1/Chk1 phosphorylation of Mik1 and the E3 ligase for its turnover are unidentified.
- Whether Mik1 has any Ser/Thr substrate (e.g. Cdc2 Thr14) in vivo.
- Basal localisation dynamics of endogenous Mik1 across the cell cycle.
