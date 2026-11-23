# gap2 (sll1342, P80505) - Synechocystis sp. PCC 6803 - notes

## Session 2026-10-19

### Deep research status

`just deep-research SYNY3 gap2 --provider falcon` was run twice in the foreground and failed both
times with an authentication error from the Edison API ("Failed to authenticate", HTTP 403). No
deep-research file exists. This review is grounded in the UniProt record, the GOA file and primary
literature cached under `publications/` (fetched with `just fetch-pmid`).

### Identity and family

- Gap2 is a 337-residue type I (phosphorylating) GAPDH, product of sll1342
  [file:SYNY3/gap2/gap2-uniprot.txt "GN   Name=gap2; OrderedLocusNames=sll1342;"].
- Family: glyceraldehyde-3-phosphate dehydrogenase family; NCBIfam TIGR01534 (GAPDH-I) and
  NF005641 (PRK07403); PANTHER PTHR43148
  [file:SYNY3/gap2/gap2-uniprot.txt "DR   NCBIfam; TIGR01534; GAPDH-I; 1."].
- Active-site nucleophile Cys154 by similarity to P00362
  [file:SYNY3/gap2/gap2-uniprot.txt "FT   ACT_SITE        154"].
- Cyanobacteria have two divergent GAPDH genes; gap1 is related to plant cytosolic GAPDH and gap2
  to the chloroplast GAPDH [PMID:9484473 "Cyanobacterial genomes harbour two separate highly
  divergent glyceraldehyde-3-phosphate dehydrogenase (GAPDH) genes, gap1 and gap2, which are
  closely related at the sequence level to the nuclear genes encoding cytosolic and chloroplast
  GAPDH of higher plants, respectively."].

### Activity and cofactor specificity

- Gap2 was cloned by complementing an E. coli gap mutant; native and recombinant enzymes are
  homotetramers with dual NAD/NADP specificity [PMID:9226260 "The recombinant GAPDH2 showed the dual
  pyridine nucleotide specificity characteristic of the native cyanobacterial enzyme"].
- UniProt curates both the NADP+ and NAD+ reactions (EC 1.2.1.59) from PMID:9226260
  [file:SYNY3/gap2/gap2-uniprot.txt "can use both NADP and NAD."].
- Koksharova et al. measured anabolic (1,3-BPG reduction) activity in wild type and mutants:
  [PMID:9484473 "Gap2 is a major enzyme with dual cosubstrate specificity for NAD and NADP, while
  Gap1 displays a minor NAD-specific GAPDH activity."]
- The catabolic (G3P oxidation) activity of Gap2 in extracts is low and seems repressed by a
  low-molecular-weight inhibitor [PMID:9484473 "if measured in the catabolic direction (oxidation of
  glyceraldehyde-3-phosphate) Gap2 activity is very low"].

### Biological process

- gap2 insertion mutants grow only on glucose under dim light, not on organic acids, and do not
  survive photoautotrophically; gap1 mutants show the reciprocal phenotype [PMID:9484473
  "Homozygous gap2- mutants show the reciprocal phenotype. Under dim light they only grow on glucose
  but not on organic acids nor do they survive under photosynthetic conditions."].
- Conclusion of the authors [PMID:9484473 "While Gap2 operates in the photosynthetic Calvin cycle and
  in non-photosynthetic gluconeogenesis, Gap1 seems to be essential only for glycolytic glucose
  breakdown"].
- Review: [PMID:39036361 "Therefore, GapDH2 is mainly part of the CBB cycle, in which it reduces
  G1,3BP using photosynthetic NADPH"]. Gap1 uses NADH only and is the active isoenzyme in low light
  or darkness, when Gap2 is inhibited by CP12 [PMID:39036361].
- Valverde et al. proposed a possible amphibolic role (anabolic and catabolic) [PMID:9226260 "A
  possible amphibolic role of the cyanobacterial GAPDH2, namely, anabolic for photosynthetic carbon
  assimilation and catabolic for carbohydrate degradative pathways, is discussed."]. The mutant
  data argue that Gap1, not Gap2, is required for glycolytic glucose breakdown, so the glycolysis
  IEA (UniPathway) is an over-annotation for this paralog, though not strictly wrong.

### Regulation by CP12

- Gap2 forms a CP12-mediated ternary complex with phosphoribulokinase (PRK) under oxidizing / dark
  conditions; NADPH dissociates it [PMID:9689144 "light regulation of Calvin cycle activity via
  NADPH-mediated reversible phosphoribulokinase/CP12/GAPDH complex dissociation is conserved in all
  photosynthetic organisms"].
- In vivo: eYFP-tagged GapDH2 (Sll1342) forms CP12-dependent foci in the dark [PMID:36330266 "These
  results show for the first time the CP12-dependent complex formation with GapDH2 or PRK during
  light/dark transitions inside living Synechocystis cells."].
- No GO annotation records the CP12 complex membership. This is regulatory context, not the core
  catalytic function; no NEW annotation proposed for it.

### Location

- Cytoplasm by UniProt curator inference (ECO:0000305). Soluble Calvin-cycle enzyme; some CP12
  complexes may associate with carboxysomes [PMID:36330266, speculative].

### Low-quality paper

- PMID:39826747 (Hameed et al. 2025) describes "SyGAPDH2" as 350 aa, 86.48 kDa, with NuoI and
  NADH-ubiquinone oxidoreductase chain 6 domains. That is inconsistent with sll1342 (337 aa,
  ~36 kDa, Gp_dh_N/Gp_dh_C domains), so the cloned sequence and its conclusions cannot be trusted
  for this gene. Recorded as LOW_QUALITY; not used to support any annotation.

### Annotation decisions (summary)

- MF GO:0047100 (NADP+) and GO:0004365 (NAD+): accept all rows (EXP, IBA, IEA, ISS).
- GO:0043891 [NAD(P)+]: the exact GO counterpart of EC 1.2.1.59 and of the enzyme's dual
  specificity; accept.
- GO:0016620: correct but general; MODIFY to GO:0047100 / GO:0004365.
- NAD binding / NADP binding: true (cosubstrates) but peripheral; KEEP_AS_NON_CORE.
- GO:0006006 glucose metabolic process (IBA, IEA): true but general; MODIFY to GO:0006094
  gluconeogenesis.
- GO:0006096 glycolysis (IEA): MARK_AS_OVER_ANNOTATED (Gap1 is the glycolytic paralog).
- NEW GO:0019253 reductive pentose-phosphate cycle (IMP, PMID:9484473). Participation test: GAPDH
  catalyses the reduction of 1,3-bisphosphoglycerate, a step of the cycle. Comparator check:
  Arabidopsis chloroplast GAPA1/GAPB (P25856, P25857) carry GO:0019253 in QuickGO (NAS, IEA).

### PGAP

- WP_010874115.1 is named by NF005641.0 (PRK07403, "type I glyceraldehyde-3-phosphate
  dehydrogenase"), which carries EC 1.2.1.- and no GO terms. PGAP propagates GO only from the naming
  model, so the protein gets no GO, even though TIGR01534 (same product name) also matches and maps
  GO:0006006, GO:0016620, GO:0050661, GO:0051287.
- PGAP EC 1.2.1.- is correct but less precise than the curated EC 1.2.1.59: LSP.
