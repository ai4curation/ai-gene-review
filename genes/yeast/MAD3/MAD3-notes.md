# MAD3 (P47074, YJL013C) - curation notes

Working notes for the GO annotation review of *Saccharomyces cerevisiae* MAD3, the
budding-yeast orthologue of BubR1. Inline citations use the repository convention
`[PMID:NNN "verbatim text"]`; claims from papers that are not in the publication cache are
attributed to the deep-research file (`MAD3-deep-research-falcon.md`) with their DOI.

## 1. Identity and architecture

- MAD3 = YJL013C = UniProt P47074, 515 aa, 58 kDa. Nuclear. Not essential.
  [PMID:10704439 "We show that MAD3 encodes a novel 58-kD nuclear protein which is not essential for viability, but is an integral component of the spindle checkpoint in budding yeast."]
- Two regions of homology to the N-terminus of Bub1 (46-47 % identity); homology region I
  (Bub1 N-terminal/TPR-like, PROSITE BUB1_N 67-228) and homology region II (GLEBS motif,
  354-401). **No kinase domain of any kind**, unlike vertebrate BubR1's pseudokinase.
  [PMID:17227844 "Mad3 from Saccharomyces cerevisiae has homology to Bub1 but lacks a corresponding C-terminal kinase domain."]
- Mad3 arose from a fungal duplication of Bub1 and retained only the non-catalytic part.
  [PMID:17227844 "Mad3 presumably originated from a duplicated copy of Bub1 and subsequently evolved a new or related function that did not require kinase activity."]
- Extended (~200 A) molecule; 1:1 heterodimer with the Bub3 beta-propeller via the GLEBS
  motif; crystal structure PDB 2I3T (Mad3 354-400 + Bub3).
  [PMID:17227844 "Mad3 forms a stable heterodimer with Bub3."]
  [PMID:17227844 "The Gle2-binding-sequence (GLEBS) motifs found in Mad3 and Bub1 are necessary and sufficient for interaction with Bub3."]
- Key residues: GIGS156-159 (region I) needed for Cdc20 binding; E382 (region II, buried salt
  bridge with Bub3 R197) needed for Bub3 binding; both mutants benomyl-sensitive
  (UniProt MUTAGEN features from PMID:10704439).
  [PMID:17227844 "The first Glu 382 Mad3 /337 Bub1 is completely buried and forms a salt bridge with Arg-197 Bub3 from blade 5."]
- KEN boxes KEN30 and KEN296 (from King et al. 2007 PLoS ONE, doi:10.1371/journal.pone.0000342,
  not cached): KEN30 is essential for Cdc20 binding and MCC assembly.
  [file:yeast/MAD3/MAD3-deep-research-falcon.md "KEN30-to-AAA mutation eliminates detectable Cdc20 binding, prevents MCC assembly, and yields a checkpoint-null phenotype."]

## 2. Interactions and the mitotic checkpoint complex

- Two-hybrid: Mad3 interacts with Bub3 and Cdc20 but not Mad1, Mad2, Bub1 or Bub2.
  [PMID:10704439 "Fig. 4 a shows that full-length Mad3p interacts with both Bub3p and Cdc20p in the two-hybrid assay, but not significantly with Mad1p, Mad2p, Bub1p, or Bub2p."]
- Co-IP: Bub3 binding is constitutive and independent of other checkpoint proteins; Cdc20 and
  Mad2 co-associate with Mad3 in mitotically arrested cells.
  [PMID:10704439 "Mad3p was stably associated with both Cdc20p and Mad2p."]
  [PMID:10704439 "We have shown by coimmunoprecipitation that the Mad3p–Bub3p interaction is not cell cycle regulated and does not require the presence of the other known checkpoint proteins."]
- Fraschini 2001: Mad2, Mad3, Bub3 co-fractionate with Cdc20; complex formation needs all
  checkpoint proteins but not intact kinetochores; Bub3 WD40 mutants lose Mad3/Mad2/Cdc20
  binding and the checkpoint.
  [PMID:11726501 "Moreover, co-fractionation experiments suggest that Mad2, Mad3 and Bub3 may be concomitantly present in protein complexes with Cdc20."]
  [PMID:11726501 "Substitution with glycines of two Bub3 conserved tryptophan residues, which should be exposed on the top surface of the propeller, abolishes the interaction of Bub3 with Cdc20, Mad2 and Mad3."]
- Poddar 2005: Mad2/Mad3/Bub3 are in excess over Cdc20 and Cdc27; MCC (Mad2-Mad3-Bub3-Cdc20)
  is a minor Mad2 pool distinct from the larger Mad2-Cdc20 pool; MCC forms in ndc10-1 cells
  without kinetochores; Mad3 degron shows Mad3 is needed to *maintain* an arrest.
  [PMID:15879521 "The fractionation profiles, Fig. 1D , demonstrate that Bub3, Mad3, Cdc20, and Cdc27 comigrated as a large multiprotein complex (670 kDa) when extracts were prepared from cells grown in the presence of nocodazole to activate the spindle checkpoint."]
  [PMID:15879521 "Pds1 levels began to decline as soon as the Mad2 or Mad3 levels dropped (Fig. 3A )."]
  [PMID:15879521 "Similar amounts of MCC were present in both wild-type and ndc10-1 cells, and Mad2-Cdc20 was also present in both wild-type and ndc10-1 cells (Fig."]
- SGD identifiers in the IPI/IGI rows: S000003084 = CDC20, S000003567 = MAD2, S000005552 =
  BUB3, S000003420 = BUB1, S000005032 = TOP2 (checked against the sibling UniProt records and
  UniProt cross-references).

## 3. Molecular function: APC/C-Cdc20 inhibition (Foster and Morgan 2012)

- Purified Mad3-Bub3 (co-expressed in E. coli) inhibits Cdc20-dependent securin
  ubiquitination by purified yeast APC/C.
  [PMID:22940250 "We found that this complex inhibited Cdc20-dependent securin ubiquitination (IC50 ~1 μM), but had little effect on autoubiquitination except at very high concentrations (Figure 1B)."]
- Synergy with Mad2 brings the IC50 to 6 nM.
  [PMID:22940250 "The presence of Mad2 dramatically increased the potency of the Mad3-Bub3 complex, shifting the IC50 from ~1 μM to 6 nM (Figure 3A, C)."]
- Mad3-Bub3 stimulates Cdc20 binding to the APC/C and Cdc20 autoubiquitination (opposite to
  Mad2); the MCC is not a global APC/C inhibitor but blocks substrate targeting.
  [PMID:22940250 "The low level of Cdc20-IR autoubiquitination was stimulated by the Mad3-Bub3 complex (Figure 1C)."]
  [PMID:22940250 "we found that Mad3-Bub3 reversed the inhibitory effect of Mad2 on Cdc20 autoubiquitination, and the dose response curve was the mirror image of the securin inhibition curve (Figure 3B, C)"]
- Pseudosubstrate mechanism via KEN boxes.
  [PMID:22940250 "KEN boxes in Mad3 were proposed to function as pseudosubstrate inhibitor motifs that interfere with substrate binding to Cdc20 (Burton and Solomon, 2007), and recent structural data provides evidence for engagement of a Mad3 KEN box by the WD40 domain of Cdc20 (Chao et al., 2012"]
- This is the basis for resolving the ND `molecular_function` row and the mechanistic
  Cdc20 protein-binding rows to **GO:1990948 ubiquitin ligase inhibitor activity** (the term
  used for human BUB1B in this repository), and for the GO:1902499 IDA row.

## 4. Checkpoint phenotypes

- mad3 disruptions: benomyl sensitive, continue dividing in microcolony assays under
  microtubule perturbation.
  [PMID:10704439 "We used a number of assays to show that mad3 strains are spindle checkpoint defective. Mad3 strains show a similar benomyl sensitivity to mad1 and mad2 mutants."]
  [PMID:10704439 "Gene disruption experiments revealed that lack of Mad3p abolishes spindle checkpoint function, and mutational analyses indicate that two regions of Mad3/Bub1 homology are critical for Mad3p's function."]
- mad3 delta fails to establish a benomyl arrest (securin destroyed with normal timing).
  [PMID:22940250 "However, the CDC20-5K, mad2Δ, and mad3Δ strains all failed to establish the SAC arrest, leading to destruction of securin with relatively normal timing (Figure 5D; mad3Δ data not shown)."]
- Cdc20 instability during a SAC arrest requires Mad3 (King 2007; Pan and Chen 2004).
  [PMID:22940250 "In budding yeast, the instability of Cdc20 during a SAC arrest requires Mad2 and Mad3 (King et al., 2007; Pan and Chen, 2004)."]
- Phosphorylation on checkpoint activation depends on Cdc5 (Polo) and Ipl1 (Aurora B)
  (Rancati et al. 2005 Cell Cycle, doi:10.4161/cc.4.7.1829, not cached).
  [file:yeast/MAD3/MAD3-deep-research-falcon.md "Mad3 becomes hyperphosphorylated following checkpoint activation by microtubule depolymerization, kinetochore defects, or insufficient tension."]
- Ser268 is a Cdk1-site phosphosite from a global study (UniProt MOD_RES, PMID:19779198).

## 5. Topoisomerase II checkpoint (GO:0044774 IGI with TOP2)

- top2-B44 cells show a G2/M delay independent of DNA-damage checkpoints and of Pds1; deletion
  of MAD1, MAD2, MAD3 or IPL1 abolishes it, BUB3 is partially required.
  [PMID:16651657 "as did other spindle checkpoint components, Mad3 and Ipl1."]
  [PMID:16651657 "spindle assembly checkpoint components are required for the Topo II checkpoint, but checkpoint activation is not the result of failed chromosome biorientation or a lack of spindle tension."]
- Kept as non-core: genuine genetic requirement, mechanism not via securin, so not the core
  MCC output.

## 6. Meiosis

- Cheslock 2005 (abstract only): Mad3 dispensable for exchange chromosomes but essential for
  nonexchange chromosome segregation; acts as a prophase timer in every meiosis.
  [PMID:15951820 "We identified a new meiotic role for MAD3; though dispensable for the segregation of exchange chromosomes, it is essential for the segregation of nonexchange chromosomes."]
  [PMID:15951820 "MAD3 acts as a crucial meiotic timer, mediating a prophase delay in every meiosis."]
- Mukherjee, Spanos and Marston 2024:
  Mad3 associates with the TOGL1 domain of Stu1/CLASP and promotes homolog capture/alignment in
  meiosis I independently of checkpoint timing; achiasmate mini-chromosomes segregate randomly
  in mad3 delta.
  [PMID:39079532 "Mad3BUBR1 associates with the TOGL1 domain of Stu1CLASP, a conserved plus-end microtubule protein that is important for chromosome capture onto the spindle."]
  [PMID:39079532 "the TOGL1 domain of Stu1 is not required for the canonical spindle checkpoint"]
- GO:0032837 distributive segregation IMP therefore kept as non-core. No NEW term proposed for
  the Stu1-dependent role because the appropriate MF is unclear; raised in `suggested_questions`.

## 7. The GO:0051754 IBA (meiotic sister chromatid cohesion, centromeric)

- Donors: PomBase SPCC1322.12c (bub1 kinase) and FB FBgn0263855 (Drosophila BubR1), node
  PTN000361607 (pre-duplication Bub1/Mad3 ancestor). QuickGO shows yeast BUB1 carries the same
  IBA from the same node; eight S. cerevisiae products carry GO:0051754, all cohesion/shugoshin
  machinery plus the two Bub1-family IBAs.
- In yeasts the centromeric-cohesion function is the Bub1 kinase (H2A phosphorylation ->
  shugoshin). Mad3 has no kinase domain and no yeast study links it to cohesion; its direct
  meiotic phenotypes are timing and nonexchange segregation.
- Graded MARK_AS_OVER_ANNOTATED with a `propagation_review` (PROPAGATION_BAD;
  WRONG_ORTHOLOG_OR_PARALOG + PSEUDO_OR_SUBACTIVITY_LOSS). Not REMOVE because there is no
  direct contradicting experiment (suggested in `suggested_experiments`). One step below the
  BUB1B row (KEEP_AS_NON_CORE), where mouse oocyte data provide some support.

## 8. Protein-binding IPI rows (13 rows) - policy applied

- Cdc20 rows from mechanistic papers (PMID:10704439, PMID:11726501, PMID:15879521) ->
  MODIFY to GO:1990948 ubiquitin ligase inhibitor activity (as for BUB1B-CDC20).
- Bub3 and Mad2 rows from mechanistic/structural papers (PMID:10704439, PMID:11726501,
  PMID:15879521, PMID:17227844) -> REMOVE. They support Mad3's MCC membership, but that is a CC
  assertion and is already present in existing GO:0033597 rows; a protein-binding MF row should not be
  converted into a cellular-component replacement.
- High-throughput rows (PMID:10688190 Uetz Y2H, PMID:11805837 Ho HMS-PCI, PMID:14660704
  Graumann TAP-MudPIT, PMID:18719252 Yu Y2H) -> REMOVE as uninformative; interactions not
  disputed.

## 9. Items deliberately not done

- King 2007 and Rancati 2005 are cited through the deep-research file only.
- No bioinformatics folder: domain architecture is settled by UniProt/InterPro and the
  crystal structure; nothing to test computationally.
- `proposed_new_terms: []`; no `NEW` annotations.
