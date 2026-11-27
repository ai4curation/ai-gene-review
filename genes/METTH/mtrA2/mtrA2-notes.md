# mtrA2 (O27134, MTH_1062) notes

## 2026-11-09: initial review (ARCHAEA project, round-7 lead)

### What the entry says
- Swiss-Prot entry, PE 3. Every annotation (name, EC 7.2.1.4, FUNCTION,
  SUBUNIT, cell membrane single-pass, TOPO_DOM/TRANSMEM 102-118, BINDING 87)
  carries `ECO:0000255|HAMAP-Rule:MF_01093`, the MtrA rule.
- The HAMAP rule itself (fetched from hamap.expasy.org, version 33) lists
  `Size: 183-262`, `Duplicate: in METRM, METTH, METTM`, and
  `General; Transmembrane; -; 1; trigger=yes`, plus the unconditional
  `SUBCELLULAR LOCATION: Cell membrane; Single-pass membrane protein`. The rule's
  size window was widened to 183 so that it covers this 183-aa paralog, but the
  rule body has no case for the anchorless paralogs. The TM predictor called a
  helix at 102-118 to satisfy the rule's "one TM" template.

### Literature
- No paper on MTH_1062/mtrA2 itself was found (WebSearch on "MTH_1062",
  "MTH1062", "mtrA2 Methanothermobacter"; no hits beyond database pages). The
  bgpt search tool was unavailable (quota).
- Wagner et al. 2016 [PMID:27324530] describe the class: "Genome analysis has
  revealed an extra copy or copies of the mtrA gene in many methanogenic archaea
  (e.g., M. marburgensis, ...)" and "These cytoplasmic MtrA homologues consist
  only of a soluble cobalamin-binding domain of 170–180 amino acids". The
  classification criterion: "sequences less than 215 amino acids correspond to
  cytoplasmic MtrA homologue without the juxtamembrane and transmembrane
  segments".
- The M. fervidus cytoplasmic homologue binds cobalamin tightly after refolding
  and its crystal structure shows base-off/His-on binding through His84
  [PMID:27324530 "The tight binding of cobalamin to the MtrA homologue was
  verified by gel filtration"]. Wagner et al. used the homologue only as a
  crystallisation model of MtrA; they report no physiological role,
  expression data or partner for any cytoplasmic homologue.

### Analysis (mtrA2-bioinformatics/RESULTS.md)
- mtrA2 aligns to residues 1-180 of mtrA1 at 60.6% identity; the last 58
  residues of mtrA1, including the TM 219-237, have no counterpart.
- The UniProt TRANSMEM 102-118 has mean KD 0.49 (three charged residues) and
  aligns to mtrA1 99-115, a non-TM segment inside the cobamide domain. The
  most hydrophobic window in mtrA2 scores 1.29; the real anchors score 2.05-2.21.
- His87 (= His84), Glu57 (= Glu54) and Ile115 (= Ile111 of the M. fervidus
  structure) are conserved.

### Decisions
- Lead holds: MF_01093 is applied to a soluble paralog and gives it a membrane
  location, a spurious TM, the whole-complex EC and complex membership.
  Recorded as source_defects to UNIPROT (SCOPE_OVER_REACH).
- Membrane, Na+ transport and methyltransferase rows: REMOVE.
- Methanogenesis and one-carbon rows: MARK_AS_OVER_ANNOTATED. A cobamide
  protein in a methanogen may well carry a methyl group in some methanogenic
  reaction, but there is no evidence of which, and the rows rest only on Mtr
  membership.
- Cobalt ion binding: MODIFY to GO:0031419 cobalamin binding, as for mtrA1 and
  METJA/mtrA (pattern 17), supported by conserved His87 and the M. fervidus
  homologue's cobalamin binding.
- NEW cytoplasm (IC): no TM, no signal, soluble class, and soluble M. fervidus
  homologue.
- Function unknown: knowledge gap (BIOLOGY, BP_DARK) with suggested experiments.
