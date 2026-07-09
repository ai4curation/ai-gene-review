# LDHA (P00338) review notes

## Identity and core biology
- LDHA = L-lactate dehydrogenase A chain, a.k.a. LDH-A / LDH-M (muscle) subunit; EC 1.1.1.27.
- Catalyses reversible, NAD+-dependent interconversion of pyruvate + NADH ↔ L-lactate + NAD+.
  UniProt FUNCTION: "Interconverts simultaneously and stereospecifically pyruvate and lactate with
  concomitant interconversion of NADH and NAD(+)" [file:human/LDHA/LDHA-uniprot.txt].
- Catalytic activity (RHEA:23444, EC 1.1.1.27): (S)-lactate + NAD(+) = pyruvate + NADH + H(+).
- A/M subunit kinetically favours pyruvate→lactate (regenerates cytosolic NAD+ for glycolysis /
  lactate fermentation), whereas B/H favours the reverse [PMID:24816116 "the A (or M) subunit
  preferentially converts pyruvate to lactate, while for the B (or H) form the converse is true"].
- Active enzyme is a tetramer; LDHA (A/M) and LDHB (B/H) subunits assemble into five isoenzymes
  hLDH-1 (B4) … hLDH-5 (A4) [PMID:24816116]. LDHA homotetramer = M4 = LDH-5 [PMID:11276087
  "HOMOTETRAMERIZATION"; UniProt SUBUNIT "Homotetramer"].
- Cytosolic/cytoplasmic (UniProt SUBCELLULAR LOCATION: Cytoplasm; HPA IDA cytosol; Reactome TAS).
- Predominantly expressed in anaerobic tissues (skeletal muscle, liver).

## Disease
- Deficiency causes Glycogen storage disease 11 (GSD11 / LDH-M deficiency, MIM:612933):
  exertional myoglobinuria, myopathy, cramps, easy fatigue [UniProt DISEASE; PMID:2334430,
  PMID:1953713 genetic characterization of LDH-A(M) deficiency mutations].

## Regulation / interactions (mostly non-core, regulatory)
- FLCN (folliculin) binds LDHA directly and is an uncompetitive inhibitor; regulates Warburg
  effect [PMID:34381247]. This paper's IMP for GO:0004459 (via R106 mutant) and IPI to FLCN
  (Q8NFG4) and self (identical protein binding) are supported.
- MP31 micropeptide (from PTEN uORF; C0HLV8) competes with LDH for NAD+ [PMID:33406399]; IPI supported.
- K5 acetylation inhibits LDHA and targets it for chaperone-mediated (HSC70) lysosomal degradation
  [PMID:23523103]; explains IntAct IPI with HSPA8/HSC70 (P11142).
- CTLH E3 ligase ubiquitinates LDHA, inhibiting activity (Reactome R-HSA-9861563).

## GOA review approach
- Core MF: GO:0004459 L-lactate dehydrogenase (NAD+) activity (many redundant evidence lines: IBA,
  IEA, EXP PMID:11276087, IMP PMID:34381247, TAS, NAS) — ACCEPT the well-supported ones, the
  vaguer parents get MODIFY/MARK.
- GO:0004457 lactate dehydrogenase activity (parent of 0004459) — ACCEPT (correct, slightly broader).
- Core BP: pyruvate→lactate fermentation / lactate metabolic process / glycolytic process / pyruvate
  metabolism — all sound; keep the specific ones as core, broader/looser as non-core.
- Core CC: cytosol/cytoplasm — ACCEPT.
- GO:0005739 mitochondrion (IBA): LDHA is canonically cytosolic. A mitochondrial pool has been
  proposed (mLDH, e.g. PMID:33406399 "mitochondrial lactate dehydrogenase (mLDH)") but it is
  contested and not the core localization; the IBA is a projected/uncertain call. Mark as
  MARK_AS_OVER_ANNOTATED (non-core, contested) rather than accepting as a core location.
- GO:0005515 protein binding (bare) IPIs: uninformative per curation policy → MARK_AS_OVER_ANNOTATED
  (NOT remove; these are experimental IntAct/UniProt IPIs).
- GO:0042802 identical protein binding: informative (homotetramer self-association) → ACCEPT.
- GO:0045296 cadherin binding (HDA, BioID proximity proteomics, PMID:25468996): proximity-labeling
  hit, not a demonstrated functional cadherin interaction → MARK_AS_OVER_ANNOTATED.
- Exosome/membrane/nucleus/sperm-fibrous-sheath localizations: high-throughput proteomics
  (HDA/IEA-from-mouse ortholog) detecting abundant glycolytic enzyme in many fractions; not core
  → MARK_AS_OVER_ANNOTATED (keep as detected, not core; don't remove experimental HDA).
- GO:1990204 oxidoreductase complex (ComplexPortal IPI, PMID:24816116): LDH tetramer is a bona fide
  oxidoreductase complex → ACCEPT.
- IEA catalytic-activity/oxidoreductase parents (GO:0003824, GO:0016491, GO:0016616): correct but
  too general given the specific EC-level annotation exists → MODIFY to GO:0004459.
</content>
</invoke>
