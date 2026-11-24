# Rubcnl (mouse, Q3TD16) review notes

## 2026-10-10 session

Context: PANTHER family PTHR45971 (Rubicon family). Mouse Rubcnl/Pacer is in subfamily
PTHR45971:SF2 [file:mouse/Rubcnl/Rubcnl-uniprot.txt, "PTHR45971:SF2; PROTEIN ASSOCIATED WITH UVRAG AS AUTOPHAGY ENHANCER"].
Domains: C-terminal Rubicon homology (RH) domain (Pfam PF13901) and RUBC_PIKBD (PF21054)
[file:mouse/Rubcnl/Rubcnl-uniprot.txt, "Pfam; PF13901; RH_dom; 1."].

No falcon deep-research file was present for mouse Rubcnl at review time; the review uses
UniProt, GOA, and cached publications.

### Mechanism (mostly from human cells, transferred by orthology)

- Discovery paper (Cheng et al. 2017, Mol Cell -- note: not Nat Cell Biol): "Pacer localizes to
  autophagic structures and positively regulates autophagosome maturation"; "Pacer antagonizes
  Rubicon to stimulate Vps34 kinase activity"; "Pacer recruits PI3KC3 and HOPS complexes to the
  autophagosome for their site-specific activation by anchoring to the autophagosomal SNARE Stx17"
  [PMID:28306502]. Abstract-only in cache.
- Phosphoinositide binding (PtdIns(3)P, PtdIns(4)P, PtdIns(5)P) is from the same paper, per UniProt
  [file:mouse/Rubcnl/Rubcnl-uniprot.txt, "Binds phosphoinositides phosphatidylinositol 3-phosphate"].
  I could not access the full text to confirm which region binds the lipids or the assay format
  (likely a lipid overlay). The claim that the RH domain is the PI3P-binding module is NOT verified;
  the RH domain is instead shown to bind phospho-Ser72 RAB7A [PMID:38728007, "Pacer-RH binds to
  phosho-RAB7A but not to unphosphorylated RAB7A"]. Treat PI3P binding as supported (IDA in human)
  but PI4P/PI5P as in vitro, non-core.
- Regulation: mTORC1 phosphorylates Pacer (Ser157 human, Ser144 mouse) to disrupt its association
  with Stx17 and HOPS; TIP60 acetylation under starvation enhances HOPS recruitment [PMID:30704899,
  "mTORC1 phosphorylates Pacer at serine157 to disrupt the association of Pacer with Stx17 and the
  HOPS complex"].
- Cheng and Sun describe RUBCNL as "vertebrate-specific" [PMID:30894088, "we identified a
  vertebrate-specific macroautophagy/autophagy regulator, RUBCNL/Pacer"], consistent with the
  PAINT RUBCNL clade node PTN002915558 at Euteleostomi.

### Mouse-specific experimental data

- Hepatocyte-specific knockout [PMID:30704899, "Hepatocyte-specific Pacer knockout in mice results
  in impaired autophagy flux, glycogen and lipid accumulation, and liver fibrosis"]. This is the
  basis of the two mouse IMP rows (autophagosome maturation; regulation of lipid metabolic process).
  UniProt: "Conditional deletion in the liver results in impaired autophagy flux, glycogen and
  lipid accumulation and liver fibrosis" [file:mouse/Rubcnl/Rubcnl-uniprot.txt].
- Mouse NSC34 motoneuron-like cells: "motoneurons depleted of Pacer are impaired in their autophagy
  flux" [PMID:30917850].
- Neuronal overexpression of human PACER in SOD1G93A mice worsened disease [PMID:39551782,
  "Pacer gain-of function is detrimental to autophagy"]; a dosage effect, not a new function.

### Other reported roles (not annotated)

- Parkin-dependent mitophagy via phospho-RAB7A binding by the RH domain, human HeLa cells
  [PMID:38728007, "Pacer knockout reduces Parkin mitophagy with little effect on bulk autophagy or
  Parkin-independent mitophagy"]. Human-only; not proposed as NEW for mouse.
- Negative regulation of RIPK1-dependent apoptosis/necroptosis in MSCs [PMID:38873940, "RUBCNL
  mutants that lose the ability to regulate autophagy, retain their function in negatively
  regulating cell death"]. Single study; not proposed.

### Decisions

- Autophagosome membrane, autophagosome maturation, autophagosome-lysosome and -endosome fusion:
  ACCEPT (PACER does part of the work by recruiting PI3KC3 and HOPS tethering machinery to
  STX17-positive autophagosomes).
- PI3P binding ACCEPT; PI4P/PI5P binding KEEP_AS_NON_CORE (in vitro breadth, no functional role
  shown).
- GO:1901981 IBA (PTN002915557, Eukaryota root, seeded by human RUBCNL only): MODIFY to PI3P
  binding for Rubcnl. At the family root the term is weakly grounded: no experimental
  phosphoinositide binding is recorded for Rubicon, fly Rubicon or worm Y56A3A.16 in this repo.
- Regulation of lipid metabolic process IMP: KEEP_AS_NON_CORE (downstream of hepatic
  autophagy/lipophagy).
