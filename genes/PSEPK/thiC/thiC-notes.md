# thiC (PP_4922, Q88DA5) — Pseudomonas putida KT2440 — curation notes

## 2026-11-12 session

**Deep research:** no deep-research provider was available in this session, so no
`thiC-deep-research-*.md` file exists. Sources used: the cached UniProt record, the
PTHR30557 PANTHER/PAINT machine files, and the module-level OpenScientist report
`modules/thiamine_diphosphate_biosynthesis-deep-research-openscientist.md`.

**Literature search:** I searched the local `publications/` cache for ThiC,
5-hydroxybenzimidazole, BzaA and aminoimidazole ribotide. No primary ThiC paper is cached.
The key family papers cited by the module report, e.g. Chatterjee et al. 2008, Nat Chem Biol
(PMID:18953358, ThiC reconstitution and structure), are not cached and were not quoted. No
publication specifically on KT2440 ThiC was found. The UniProt entry is PE 3 (inferred from
homology), and every functional statement in it is rule-based (HAMAP MF_00089, ECO:0000255).

### Evidence summary
- Function (HAMAP): [file:PSEPK/thiC/thiC-uniprot.txt "Catalyzes the synthesis of the
  hydroxymethylpyrimidine phosphate (HMP-P) moiety of thiamine from aminoimidazole ribotide
  (AIR) in a radical S-adenosyl-L-methionine (SAM)-dependent reaction."]
- Reaction: RHEA:24840 / EC 4.1.99.17. AIR + SAM -> HMP-P + CO + 5'-dA + formate + Met + 3 H+.
- Cofactor: [file:PSEPK/thiC/thiC-uniprot.txt "Binds 1 [4Fe-4S] cluster per subunit. The
  cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine."] I
  checked the sequence: Cys574, Cys577 and Cys582 (the CX2CX4C motif) are the cluster ligands.
- Zn2+ site: His430 and His494 (sequence checked). The family representative structure 4S28
  (Arabidopsis ThiC) was solved with Fe at this site
  [file:interpro/panther/PTHR30557/PTHR30557-metadata.yaml "Crystal structure of Arabidopsis
  thaliana ThiC with bound aminoimidazole"], so the physiological metal is uncertain.
- Substrate-binding residues (HAMAP): N232, M261, Y290, H326, 346-348, 387-390, 426, Y453.
- Subunit: homodimer (HAMAP). There is no signal peptide or TM segment, only an N-terminal
  disordered region (1-22, MobiDB-lite). The protein is soluble and cytoplasmic.
- Family: PTHR30557:SF1 (the only subfamily). This subfamily also contains the plant
  chloroplastic THIC (O82392), the archaeal and other short ThiC1/ThiC2 paralogs, the
  Bifidobacterium ThiE-ThiC fusion (Q8G7X1) and the diverged anaerobic BzaA/BzaB
  5-hydroxybenzimidazole synthases. KT2440 ThiC is the full-length (626 aa) canonical
  bacterial form.

### Pathway context (module)
The pyrimidine branch is AIR -> (ThiC) HMP-P -> (ThiD) HMP-PP. ThiE then couples HMP-PP with
the thiazole to give TMP, and ThiL phosphorylates TMP to ThDP.
[file:modules/thiamine_diphosphate_biosynthesis-deep-research-openscientist.md "ThiC catalyzes
one of the most complex known rearrangements in cofactor biology"]

### Decisions
| Term | Action | Note |
|---|---|---|
| GO:0005829 cytosol | ACCEPT | soluble bacterial enzyme; bacterial PAINT node (taxon:2) |
| GO:0008270 zinc ion binding | KEEP_AS_NON_CORE | conserved metal site; metal identity uncertain (Fe in 4S28) |
| GO:0009228 thiamine biosynthetic process | ACCEPT | catalytic step |
| GO:0009229 ThDP biosynthetic process | ACCEPT | UniPathway UPA00060; not is_a 9228 |
| GO:0016829 lyase activity | MODIFY -> GO:0070284 | |
| GO:0016830 C-C lyase activity | MODIFY -> GO:0070284 | |
| GO:0051536 Fe-S cluster binding | MODIFY -> GO:0051539 | [4Fe-4S] |
| GO:0070284 HMP-P synthase activity | ACCEPT | core |

Not proposed as NEW: S-adenosyl-L-methionine binding. The SAM is the radical-generating
co-substrate and is already implied by the GO:0070284 reaction, so a separate row would add
little.
