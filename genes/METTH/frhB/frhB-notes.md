# frhB (P19499, MTH_1297) notes

Methanothermobacter thermautotrophicus Delta H, coenzyme F420-reducing [NiFe]-hydrogenase (Frh), beta subunit (281 aa, iron-sulfur flavoprotein).

## Literature search (2026-11-07)

Deep-research providers were unavailable, so no deep-research file exists. The literature set
of the sister review genes/METTH/frhA was reused; all are cached in publications/:

- PMID:3663585 (Fox et al. 1987; purification of FRH from strain Delta H; abstract only)
- PMID:2207102 (Alex et al. 1990; cloning of frhADGB from strain Delta H; abstract only)
- PMID:23483797 (Mills et al. 2013; cryo-EM structure of Frh from M. marburgensis; full text)
- PMID:24569482 (Allegretti et al. 2014; 3.36 A cryo-EM structure of M. marburgensis Frh; full text)
- PMID:18487331 (Hendrickson & Leigh 2008; M. maripaludis fru/frc deletion mutants; full text)

No FrhB-specific genetics or biochemistry in strain Delta H was found beyond these.

## Delta H enzyme

- Three-subunit enzyme [PMID:3663585 "composed of three subunits, alpha (Mr 47K), beta (Mr 31K), and gamma (Mr 26K)"]; beta (31K) is FrhB.
- Cofactors per heterotrimer [PMID:3663585 "The tightly associated redox cofactors per 115K species are 0.6-0.7 nickel atom, 0.8-0.9 flavin adenine dinucleotide (FAD), and 13-14 iron atoms in iron-sulfur centers."]; placement unresolved then [PMID:3663585 "placement of the nickel and FAD has not been established"].
- Subunits could not be separated with cofactors intact [PMID:2207102 "This has been hindered due to the refractory nature of the enzyme to denaturation methods needed in order to obtain individual subunits with cofactors intact."]
- UniProt FUNCTION [file:METTH/frhB/frhB-uniprot.txt "Reduces the physiological low-potential two-electron acceptor coenzyme F420, and the artificial one-electron acceptor methylviologen."] (entry-level text, shared by the three subunit entries).

## Cofactor placement (ortholog structure, M. marburgensis)

- [PMID:24569482 "the 31 kDa iron–sulphur flavoprotein FrhB, which contains the F420-binding site and has one [4Fe4S] cluster and an FAD."]
- [PMID:23483797 "FrhB contains one Fe-S cluster, an FAD, and the F420-binding site."]
- Electron path [PMID:24569482 "Electrons are extracted from hydrogen by the [NiFe] cluster in FrhA, and transferred via the three [4Fe4S] clusters in FrhG and another one in FrhB to FAD and from there to the substrate."]
- Hydride transfer at FrhB [PMID:23483797 "F420 is in van der Waals distance from its hydride donor, the FAD isoalloxazine ring"].
- F420 density near S209/V210 [PMID:23483797 "The F420 density is close to the small residues S209 and V210 in a loop between two β-strands"]; F420 turn 163IGKGK; FAD loop Lys75-Tyr76 [PMID:23483797 "near the highly conserved loop Lys75-Tyr76"]; FAD loop G73-T77 and I132-F138 (PMID:24569482).
- Novel fold, shared with FrhB family (FsrF, FqoF, FpoF, FdhB) [PMID:23483797 "The residues coordinating the Fe-S cluster, FAD, and F420 are conserved in the FrhB family"].
- No nickel in FrhB; the [NiFe] centre is in FrhA [PMID:24569482 "Green and orange spheres indicate the [NiFe] center in FrhA"].

### Sequence check on P19499 (own analysis, Python on the UniProt sequence)

Residue numbering of the M. marburgensis FrhB maps directly onto P19499: G73, T74, K75, Y76, T77
(the "AAGTKYTFSP" FAD loop starts at 73); I163-G-K-G-K167 (the F420 turn); S209, V210 (the F420
loop); I132 and F138 (the isoalloxazine loop). All match the residues named in the structures.
P19499 has five cysteines (C104, C134, C148, C192, C195), enough for the single [4Fe-4S]
cluster. So the cofactor sites of the ortholog are conserved in P19499.

## Decisions

- nickel cation binding (IPR017679): wrong for FrhB; nickel is in FrhA. REMOVE + source defect (pattern 18).
- FAD binding (IPR017679): right; ACCEPT (core).
- iron-sulfur cluster binding (IPR017679): right but general; MODIFY to GO:0051539 4 iron, 4 sulfur cluster binding.
- coenzyme F420 hydrogenase activity: whole-complex activity (pattern 16); MARK_AS_OVER_ANNOTATED, contributes_to in core, as frhA.
  No subunit-level catalytic GO term for "reduced FAD to F420 hydride transfer" exists (OLS search for coenzyme F420 terms).
  GO:0070967 coenzyme F420 binding exists and fits FrhB specifically; added as NEW (IC from ortholog structure plus conserved residues).
- oxidoreductase activity (IPR045220): true but general; MODIFY to GO:0050454 (as contributes_to).
- GO:0052592 (TreeGrafter PTN001263539): definition is CH/CH2 donor reducing an Fe-S protein (EC 1.17.7 class). Frh uses H2 as donor and F420 as acceptor (EC 1.12.98.1). PANTHER PTHR31332 is named for 7-hydroxymethyl chlorophyll a reductase (HCAR), a ferredoxin-dependent plant enzyme of that EC class, so the node's term reflects the family founder's reaction (pattern 14). REMOVE.
- NEW cytoplasm and methanogenesis from CO2, mirroring frhA.
