# tth (Af-Tth, AFE_0029) — Acidithiobacillus ferrooxidans ATCC 23270, UniProtKB:B7J3C9

No provider deep research was available; these notes are from my own reading of cached
publications (abstracts unless marked full text) and the bioinformatics in
`tth-bioinformatics/RESULTS.md`.

## Identity and activity

- Tetrathionate hydrolase (4THase), purified from tetrathionate-grown ATCC 23270 cells and
  linked to AFE_0029 by N-terminal sequencing [PMID:17904676 "A 4THase having a dimeric structure of identical 50kDa polypeptides was purified from tetrathionate-grown cells. The 4THase showed the maximum activity at pH 3.0 and high stability under acidic conditions."].
- Products: elemental sulfur, thiosulfate and sulfate [PMID:25144400 "catalyzes tetrathionate hydrolysis to generate elemental sulfur, thiosulfate, and sulfate"]. Mechanistically
  sulfate plus the unstable disulfane monosulfonic acid are thought to form first, with
  sulfur/thiosulfate arising partly abiotically [PMID:23722856 "It is speculated that sulfate and a chemically unstable compound, disulfane monosulfonic acid (HS 2 SO 3 − ), are generated during the hydrolysis of tetrathionate by 4THase."].
- UniProt reaction: tetrathionate + H2O = sulfur + thiosulfate + sulfate + H(+) (RHEA:13541), EC 3.12.1.-.
  No GO term exists for tetrathionate hydrolase activity (OLS search for "tetrathionate" in GO
  returns only thiosulfate dehydrogenase terms and CHEBI entities). The nearest parent is
  GO:0016828 hydrolase activity, acting on sulfur-sulfur bonds. Proposed a new MF term.
- Structure: eight-bladed beta-propeller homodimer; Asp325 is the catalytic acid
  [PMID:33103311 "Af-Tth is a homodimer, and its monomer structure exhibits an eight-bladed β-propeller motif."]
  [PMID:33103311 "4THase activity was completely abolished in the site-specific Af-Tth D325N variant"].
  The sole Cys301 is dispensable [PMID:25144400 "the sole cysteine residue (Cys301) in Af-Tth is involved in neither the tetrathionate hydrolysis reaction nor the subunit assembly"].
- No PQQ cofactor, despite the PQQ-repeat (beta-propeller) Pfam/InterPro signatures
  [PMID:20546308 "No cofactor such as pyrroloquinoline quinone (PQQ) was required during the refolding process in spite of the similarity in the primary structure of Af-Tth to the PQQ family of proteins."].
  The PANTHER subfamily label (PTHR34512:SF30 "OUTER MEMBRANE PROTEIN ASSEMBLY FACTOR BAMB") is
  a family naming artefact; no GO propagation rests on it here.
- Recombinant enzyme needs acid exposure to fold [PMID:20546308 "Af-Tth required exposure to an acidic environment during protein folding for activation."].

## Physiological role (genetic evidence)

- Knockout: ΔtetH cannot grow on tetrathionate, still grows on sulfur and Fe2+ [PMID:24727223 "The ΔtetH mutant could not grow on tetrathionate but could proliferate on sulfur with a lower cell yield than the wild type's, which indicated that tetrathionate hydrolysis is mediated only by TetH, encoded by tetH."].
  Strain is ATCC 23270 (full text: "ferrooxidans ATCC 23270 genome (GenBank accession number NC_011761 )").
- Expression strongly induced on tetrathionate and sulfur relative to iron [PMID:36635106 "the expression ratios of S0/Fe2+ and S4O62-/Fe2+ were found to be 68 ± 21 and 181 ± 5, respectively"].
- Pathway context: S4-intermediate (S4I) thiosulfate oxidation pathway; TQO/TSD make tetrathionate,
  TetH hydrolyses it [PMID:38348185 "TTH, which catalyzes tetrathionate hydrolysis, is a unique enzyme that cooperates with TQO and/or TSD to function in the S4I pathway for RISC oxidation, particularly of thiosulfate (Figure 1)."].
- Ferric reductase activity attributed to the same protein (tetrathionate-dependent Fe3+ reduction)
  [PMID:19502725 "This is the first report on ferric reductase activity associated with tetrathionate hydrolase."].
  Single-lab report, abstract only; not used for annotation.

## Localization

- GOA/UniProt: "Cell membrane" (GO:0005886 plasma membrane), EXP from PMID:17904676 and IEA via SubCell SL-0039.
  UniProt's own note says only "Membrane-associated". The Kanao 2007 full text is not cached.
- Every other source places the protein on the OUTER membrane (not the cytoplasmic membrane), as a
  peripheral protein, with some release to the medium:
  - The same gene was first isolated as an outer membrane protein (OMP) from sulfur-grown cells [PMID:10406099 "Among these OMPs, a protein with a molecular mass of 54 kDa was purified and 18 amino acids of the N-terminal sequence determined."] and its mature 467-aa product after 32-aa signal peptide matches Af-Tth [PMID:23722856 "Prior to this identification, the corresponding gene in this bacterium was recognized as a sulfur-regulated outer membrane protein with unknown function (Buonfiglio et al. , 1999 ▶ )."].
  - Same lab as the EXP source, 2010 [PMID:20546308 "This property reflects a physiological characteristic of the Af-Tth localized in the outer membrane of the acidophilic A. ferrooxidans."].
  - 2024 review by the same group [PMID:38348185 "Although Af-Tth is localized on the outer membrane (peripheral protein), it is detected in the culture medium supernatant, suggesting that Af-Tth acts in the extracellular space to generate hydrophilic sulfur globules (Beard et al., 2011)."].
  - Culture supernatant proteomics identified TetH (MALDI-TOF MS band 1) and extracellular TTH activity [PMID:21833324 "supernatants from both OSC- and OLC-incubated cells showed extracellular TTH activity, which most likely accounted for tetrathionate consumption in the culture medium."] [PMID:21833324 "Protein band No. 1 corresponded to TetH protein of A. ferrooxidans ATCC 53993, which is identical to TetH from A. ferrooxidans ATCC 23270 used in this study"].
  - Mature chain (33-499) has no transmembrane segment in UniProt; acid optimum (pH 3) requires an
    outside-the-cytoplasm location.
- Against a confident outer-membrane call:
  - The UniProt RP line for PubMed:17904676 includes "SUBCELLULAR LOCATION", so a Swiss-Prot
    curator read the 2007 full text and chose "Cell membrane"; we have only the abstract.
  - An independent 2011 group [PMID:21833324 "Although TetH has a predicted Sec-type signal peptide, to date its subcellular location is not clear."], listing outer membrane, soluble/probably periplasmic and membrane-associated (Kanao 2007) reports.
  - Table 1 of PMID:38348185 gives the ATCC 23270 localization only as "membrane"; ATCC 19859 is "periplasm".
  - None of the outer-membrane statements we can read reports an inner/outer membrane separation;
    the 2010 and 2024 statements may rest on the 1999 OMP isolation.
- Decision (revised after PR #5627 review): do not overrule the curator. Both plasma-membrane rows
  (EXP and IEA) are UNDECIDED; GO:0009279 cell outer membrane is asserted separately as a NEW TAS
  row (PMID:38348185); the UniProt source defect is a CHECK query (SUSPECTED), not a REPOINT.
  Add GO:0005576 extracellular region (IDA, PMID:21833324) as non-core.

## Notes on CMMMech's claims (do not edit CMMMech)

CMMMech records (36+ protein examples for B7J3C9) describe it as a "Periplasmic tetrathionate
hydrolase ... generating sulfuric acid protons" and some causal-graph nodes as a "Periplasmic
pyrroloquinoline-domain hydrolase disproportionating tetrathionate into sulfate and protons".
Points where this exceeds the evidence:
1. Location: for A. ferrooxidans the evidence is membrane-associated, described as outer membrane
   (peripheral), plus secreted; the exact membrane is not settled, and none of the sources we could read demonstrates a
   periplasmic location for ATCC 23270 (earlier soluble/periplasmic reports are cited in
   PMID:21833324). Periplasmic localization was shown for A. caldus TetH [PMID:14717695] and a
   different A. ferrooxidans strain (ATCC 19859, Table 1 of PMID:38348185), not for ATCC 23270.
2. "Pyrroloquinoline-domain": the PQQ-repeat signature describes the beta-propeller fold; the
   enzyme does not use PQQ [PMID:20546308].
3. "Disproportionating tetrathionate into sulfate and protons" omits the thiosulfate and elemental
   sulfur products; one H+ per tetrathionate is released by the hydrolysis itself, while the bulk
   of biogenic sulfuric acid comes from downstream oxidation of thiosulfate/sulfur by other enzymes.
4. Leaching-record evidence links are inferential (CMMMech itself notes genes were not mutated);
   laboratory enzymology does not establish a role in any particular industrial leach.
