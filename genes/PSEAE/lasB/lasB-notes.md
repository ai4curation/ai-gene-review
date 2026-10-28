# lasB (PA3724, P14756) — curation notes

## Gene identity

UniProt P14756, `ELAS_PSEAE`, 498 aa precursor, reviewed; PseudoCAP PA3724;
matches the worklist accession. EC 3.4.24.26; MEROPS M04.005; peptidase M4
(thermolysin) family; PANTHER PTHR33794:SF1 ("bacillolysin"). 19 PDB entries,
most of the mature chain 198-498 (1EZM at 1.5 A), three of 24-498.

Chain structure (UniProt FT): SIGNAL 1-23, PROPEP 24-197, mature elastase
198-498; SITE 197..198 "Cleavage; by autolysis"; ACT_SITE 338 and 420 (proton
donor); catalytic Zn(2+) at His337/His341/Glu361; Ca(2+) at
Asp333/Asp369/Glu372/Asp380/Asp382; disulfides 227-255 and 467-494.
Literature residue numbers are usually on the mature chain (His-223 = His420).

## What is established

- Zinc metalloprotease with the thermolysin fold [PMID:1899664 "Pseudomonas
  aeruginosa elastase (PAE) is a zinc metalloprotease with 301 amino acids."],
  28% identity to thermolysin, "the active site cleft is significantly more
  'open' in PAE than in thermolysin". UniProt: 1 Zn(2+) and 1 Ca(2+) per
  subunit; monomer; inhibited by phosphoramidon.
- Catalysis and autoprocessing. Active-site His substitutions abolish activity
  [PMID:1744034 "No proteolytic or elastolytic activities were detected in
  extracts of E. coli cells containing the lasB mutant alleles."] and block
  maturation, while mature elastase processes the mutant pro-enzymes in trans;
  "The present results confirm that His-223 is essential for elastase activity
  and provide evidence for autoproteolytic processing of proelastase."
- Substrates. UniProt CC:FUNCTION: "Cleaves host elastin, collagen, IgG, and
  several complement components as well as endogenous pro-aminopeptidase";
  CC:CATALYTIC ACTIVITY: "Hydrolysis of proteins including elastin, collagen
  types III and IV, fibronectin and immunoglobulin A, generally with bulky
  hydrophobic group at P1'." Maturation of pro-PaAP depends on LasB
  [PMID:11533066 "a reaction that depended on elastase (LasB)"]; LasB also
  processes pro-CbpD [PMID:9642203 per UniProt].
- Export and location. Secreted; "We demonstrate that the propeptide and the
  mature elastase are both secreted but that the propeptide is degraded
  extracellularly." [PMID:9642203]; "The signal sequence is cleaved off during
  transport across the inner membrane and, in the periplasm, proelastase is
  further processed." UniProt: "Secreted in an Xcp-dependent fashion (a type II
  secretion pathway)."
- Metal requirement for production. [PMID:1597429 "High levels of proteolytic
  and elastolytic activity were exhibited by all strains when cultured in the
  presence of both zinc and calcium, and this was associated with the
  production of mature 33-kDa elastase and 21-kDa LasA."]
- Virulence. Deletion in an early-persistence CF isolate reduces burden in a
  murine persistent-pneumonia model; "The zinc metalloprotease elastase B (also
  called LasB or pseudolysin) is the most abundant protease in the P."
  [PMID:33510733].
- Surface behaviour. "Elastase LasB and PvdQ are essential for normal swarming
  behavior." and "all four tested lasB mutants also showed a strong impairment
  in biofilm formation with about 50% less biomass"; both complemented
  [PMID:18245294]. The authors link this to T2SS secretion rather than to a
  motility or matrix role of LasB itself.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002138658 | GO:0006508 proteolysis | 1 (sole seed) | 21 (10 taxa, PAINT leaf GAF) | GO:0006508, IDA, PMID:1597429 (PseudoCAP) | SOUND | The seed records the gene's own activity, not a downstream phenotype: supernatant proteolytic and elastolytic activity tracking with the mature 33 kDa elastase, with zinc-dependent recovery of activity in the assay. The claim is independently certain for LasB (EC 3.4.24.26, thermolysin-like active site resolved at 1.5 A, His-223 mutants inactive). The reference is a weaker choice than PMID:1899664/PMID:1744034 but is not wrong, so no PseudoCAP defect is raised. The node term is maximally conservative for a clade of 21 M4 thermolysin-family metalloproteinases (Bacillus bacillolysins, Listeria Mpl, Vibrio HA/protease, Leptospira thermolysins, Streptomyces neutral metalloproteinases), and the substrate specificity and virulence context were not propagated. |

PseudoCAP's other rows for PA3724 (GO:0015628, GO:0043952, GO:0044010,
GO:0071978) seed no IBD, but two of them are over-annotations:

- GO:0015628 protein secretion by the type II secretion system (IDA,
  PMID:9642203) and GO:0043952 protein transport by the Sec complex (IDA, same
  paper) treat the cargo as a participant in its own export. Flagged as
  PROBABLE PseudoCAP `WRONG_TERM`/CHECK defects, exactly as previously recorded
  for PaAP (genes/PSEAE/lap) from the same reference.
- GO:0044010 and GO:0071978 (IMP, PMID:18245294) are real, complemented
  requirements but downstream of secreted protease activity, so
  KEEP_AS_NON_CORE rather than core.

## Decisions summary

- ACCEPT (8): GO:0006508 proteolysis (IBA, IDA seed, IEA); GO:0004222
  metalloendopeptidase activity (IEA); GO:0005576 extracellular region (IEA and
  three EXP rows).
- MODIFY (2): both GO:0004175 endopeptidase activity rows ->
  GO:0004222 metalloendopeptidase activity (specific descendant already carried
  by the gene; metal dependence established structurally).
- MARK_AS_OVER_ANNOTATED (2): GO:0015628, GO:0043952 (cargo, not machinery),
  each with a PseudoCAP source defect.
- KEEP_AS_NON_CORE (2): GO:0044010 single-species biofilm formation,
  GO:0071978 swarming motility.
- NEW (3): GO:0008270 zinc ion binding and GO:0005509 calcium ion binding (IDA,
  PMID:1899664, mapped ligands in PDB 1EZM); GO:0016540 protein autoprocessing
  (IMP, PMID:1744034 — LasB cleaves its own 197/198 bond, so it does the work).
- No REMOVE.
