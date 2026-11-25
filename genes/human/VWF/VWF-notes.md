# VWF (von Willebrand factor) — curation notes

UniProt: P04275 (VWF_HUMAN). 2813 aa precursor: signal peptide (1-22), propeptide
"von Willebrand antigen 2" / VWFpp (23-763; domains D1D2), mature VWF (764-2813;
D'D3-A1-A2-A3-D4-C1..C6-CTCK).

## Deep research status

- `just deep-research-falcon human VWF` was launched in parallel with
  `just fetch-gene-pmids human VWF` (see bottom of this file for outcome).
- Literature below is from cached `publications/PMID_*.md` (mostly abstract-only) and
  the UniProt record.

## Core biology (with provenance)

- Function summary: [file:human/VWF/VWF-uniprot.txt "it promotes adhesion of platelets to the sites of vascular injury by forming a molecular bridge between sub-endothelial collagen matrix and platelet-surface receptor complex GPIb-IX-V"]
- FVIII carrier: [file:human/VWF/VWF-uniprot.txt "Also acts as a chaperone for coagulation factor VIII, delivering it to the site of injury"]; [PMID:9759493 "VWF also is a carrier protein for blood clotting factor VIII, and this interaction is required for normal factor VIII survival in the circulation."]
- FVIII binding is high-affinity: [PMID:7756647 "the dissociation constants (kd) for binding of factor VIII to vWF were 0.21 +/- 0.04 and 0.22 +/- 0.05 nmol/L"]; D'D3 is the FVIII-binding region [PMID:24928861 "D′ and D3 bind factor VIII (FVIII) and thus deliver FVIII to platelet plugs."]; type 2N-like mutations R19W/H54Q (mature numbering) impair FVIII binding [PMID:8562925].
- GPIb binding via A1 domain: [PMID:10764791 "The GPIb-binding site within vWF has been localized to the vWF-A1 domain."]; crystal structures of A1–GPIbα [PMID:12183630, PMID:15039442]. Binding is shear/modulator-regulated [PMID:11943773 "the binding does not occur in normal circulation"].
- Collagen binding: A3 is main site for collagen I/III [file:human/VWF/VWF-uniprot.txt "VWFA 3; main binding site for collagens type I and"]; collagen III site RGQOGVMGF [PMID:16912226]; collagen VI in subendothelium [PMID:2056120 "purified type VI collagen also bound vWF"].
- Integrin binding: αIIbβ3 binds RGD in C4 [PMID:24928861 "Platelet integrin α IIb β 3 binds an RGD motif in the VWC4 module"]; propeptide binds α4β1 (VLA-4) [PMID:9079671 "pp-vWF is a novel physiological ligand for VLA-4"].
- Platelet capture under high shear: [PMID:8565074 "glycoprotein Ib alpha binding to immobilized von Willebrand factor (vWF) appears to have fast association and dissociation rates as well as high resistance to tensile stress"]; aggregation at high shear [PMID:24928861 "Extension above a threshold shear correlates with activation of VWF-dependent aggregation of platelets in stirred cuvettes"].
- Platelet signaling downstream of VWF–GPIb: [PMID:12871509 "The interaction between von Willebrand factor (VWF) and glycoprotein (GP) Ib results in platelet agglutination and activation of many signaling intermediates."]; [PMID:14656219] GPIb-IX-V-driven Syk/PLCγ2 phosphorylation.

## Biosynthesis, multimerization, storage

- Dimerization (CTCK, ER) and multimerization (D3, Golgi), propeptide acts as pH-dependent oxidoreductase/chaperone: [PMID:17895385 "Von Willebrand factor (VWF) dimerizes through C-terminal CK domains, and VWF dimers assemble into multimers in the Golgi by forming intersubunit disulfide bonds between D3 domains."]; Cys1099/Cys1142 essential.
- Low pH and Ca2+ drive tubule assembly of D1D2 + D'D3 in WPB [PMID:18182488]; C-terminal dimeric bouquet at acidic pH [PMID:21857647].
- ER chaperone clients: binds BiP, Grp94, ERp72, calnexin, calreticulin [PMID:10887119]; transient BiP association [PMID:3121636]. NB: the GO "immunoglobulin binding" annotation from PMID:3121636 appears to derive from BiP's alias "heavy chain binding protein" — VWF was shown to associate with BiP, not immunoglobulin.
- Storage in endothelial Weibel–Palade bodies [PMID:6754744; PMID:3082891; PMID:3087627 "Endothelial cells therefore concentrate a special subclass of very large and biologically potent vWf multimers in Weibel-Palade bodies"]; also platelet alpha granules [PMID:9759493 review; Reactome R-HSA-481007].
- Deposited in subendothelial / endothelial ECM [PMID:6754744 "on filaments of the extracellular matrix"; PMID:2839553].

## Regulation by ADAMTS13

- ADAMTS13 cleaves Tyr1605-Met1606 in A2 [PMID:16221672]; binding Kd 14 nM, spacer domain required [PMID:15824096]; A3/A1 docking under flow [PMID:12775718]; VWF allosterically activates ADAMTS13 [PMID:25512528]; FVIII accelerates cleavage [PMID:18492805]. VWF is the *substrate*; "protease binding" is true but not a core function of VWF.

## Disease

- von Willebrand disease types 1, 2 (2A, 2B, 2M, 2N), 3 (UniProt). Type 3 also causes FVIII deficiency (loss of carrier function).

## Curation decisions summary

- Core MF: collagen binding; cell adhesion molecule binding (GPIbα — replaces protein binding rows); integrin binding; protein carrier chaperone for FVIII (replaces protein binding rows with F8); identical protein binding (multimerization).
- Core BP: hemostasis / blood coagulation; cell-substrate adhesion (platelet adhesion to injured vessel); NEW platelet aggregation (comparator: fibrinogen FGA/FGB/FGG carry GO:0070527 as bridging ligands; VWF performs the bridging); NEW protein stabilization (VWF itself protects FVIII from clearance).
- Core CC: extracellular region, Weibel-Palade body, platelet alpha granule, extracellular matrix.
- ECM structural constituent: over-annotation (VWF is adhesive bridge, not a structural-integrity component).
- Immunoglobulin binding: MODIFY to protein-folding chaperone binding (BiP).
- Note: GO:0005615 extracellular space is obsolete in current GO (verified via QuickGO 2026-10), so not proposed.

## Deep research outcome

- Falcon deep research succeeded: `VWF-deep-research-falcon.md` (2026-10-05). Its synthesis
  agrees with the decisions above (adhesive scaffold + FVIII carrier, not an enzyme; TIL/CK
  modules are structural folds, no protease-inhibitor activity; A1 also contributes to WPB tubule
  geometry; angiogenic roles via WPB/Ang-2 are secondary and mechanistically unresolved).
  It reports ~0.5 nM FVIII Kd and >95% of plasma FVIII VWF-bound (citing Lenting et al. 2024 Blood,
  doi:10.1182/blood.2023023277 — not cached here, so not used as supporting text).
- No new GO annotations proposed from the angiogenesis literature (indirect, mechanism unresolved);
  raised as a suggested question instead.
