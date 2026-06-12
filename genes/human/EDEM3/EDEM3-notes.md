# EDEM3 (Q9BZQ6) review notes

## Identity
- ER degradation-enhancing alpha-mannosidase-like protein 3. ER lumenal protein (signal peptide; PROSITE PRU10138 ER retention). GH47 family (EDEM1/2/3). Contains a protease-associated (PA) domain of unknown function (distinguishes EDEM3 from EDEM1/2). EC 3.2.1.113.

## Function (synthesis)
- EDEM3 is an active alpha-1,2-mannosidase that accelerates glycoprotein ERAD by catalyzing mannose trimming from Man8GlcNAc2 to Man7GlcNAc2 (the second/downstream trimming step), and further to Man5 isomers [UniProt FUNCTION "Accelerates the glycoprotein ERAD by proteasomes, by catalyzing mannose trimming from Man8GlcNAc2 to Man7GlcNAc2 in the N-glycans (PubMed:25092655)"; CATALYTIC ACTIVITY RHEA:56008 (M9 isomer 9A1,2,3B1,2,3 -> M5A1,2 + 4 mannose) and RHEA:56028 (M8 -> M5 + 3 mannose), EC=3.2.1.113].
- Endogenous KO analysis: EDEM3 (mainly) and EDEM1 (to a lesser extent) perform the second trimming step Man8B->Man7 [PMID:25092655 "Mannose trimming from Man8GlcNAc2 to Man7GlcNAc2 is performed mainly by EDEM3 and to a lesser extent by EDEM1"; "M8B is trimmed by EDEM1 and EDEM3 to Man7-5GlcNAc2, which are recognized by lectin OS-9"]. EDEM3 acts downstream of EDEM2.
- Unlike EDEM2, EDEM3 (with EDEM1) binds SEL1L [PMID:25092655 "SEL1L... binds to EDEM1 and EDEM3 but not to EDEM2"].
- May also trim N-glycans on all glycoproteins, not just misfolded ERAD substrates [UniProt FUNCTION "May also participate in mannose trimming from all glycoproteins and not just misfolded ones targeted to ERAD (PubMed:34143952)"].
- Disease: biallelic variants cause Congenital disorder of glycosylation 2V (CDG2V/EDEM3-CDG), autosomal recessive neurodevelopmental delay [UniProt DISEASE; PMID:34143952, not cached but recorded in UniProt].
- Calcium cofactor (Ca2+) required (GH47 fold) [UniProt COFACTOR].

## Localization
- ER lumen [UniProt SUBCELLULAR LOCATION; IEA]. ER [IEA].

## Annotation review decisions
- GO:0004571 mannosyl-oligosaccharide 1,2-alpha-mannosidase activity: CORE. IBA, IEA (with EC 3.2.1.113/RHEA), TAS Reactome, ISS, IMP (PMID:25092655) — all ACCEPT. EDEM3 has the strongest/clearest catalytic activity of the three EDEMs (no NOT annotation). Core MF.
- GO:1904380 ER mannose trimming: IMP (PMID:25092655) ACCEPT core; IEA ACCEPT.
- GO:0036503 ERAD pathway: IMP (PMID:25092655) ACCEPT core; IEA ACCEPT.
- GO:1904382 mannose trimming involved in glycoprotein ERAD pathway (TAS Reactome): ACCEPT core.
- GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway (IBA): ACCEPT, specific/correct.
- GO:0006516 glycoprotein catabolic process (IEA ARBA): correct but generic parent of gpERAD; KEEP_AS_NON_CORE / could MARK_AS_OVER_ANNOTATED. Use ACCEPT-adjacent: it is reasonably specific (glycoprotein catabolism) -> KEEP_AS_NON_CORE.
- GO:0030968 ER unfolded protein response (IBA): UPR-induced effector acting in ERAD; KEEP_AS_NON_CORE.
- GO:0005509 calcium ion binding (IEA): GH47 cofactor; KEEP_AS_NON_CORE.
- GO:0005788 ER lumen (IEA), GO:0005783 ER (IEA): ACCEPT.
- GO:0044322 ERQC (TAS Reactome): ACCEPT.
- GO:0005975 carbohydrate metabolic process (IEA), GO:0016020 membrane (IEA): over-general/inaccurate (EDEM3 is luminal, not membrane) -> MARK_AS_OVER_ANNOTATED.
</content>

## Falcon deep-research findings (incorporated 2026-06)
- Hirao et al. 2006 (JBC) is the original EDEM3 characterization (was previously only referenced via UniProt): EDEM3 is a 931-aa soluble Class I GH47 alpha-mannosidase homolog with a C-terminal protease-associated (PA) motif; overexpression accelerates gpERAD of misfolded A1AT-NHK and TCRalpha and stimulates mannose trimming from misfolded AND total glycoproteins; the catalytic E147Q mutant abolishes trimming and decreases ERAD enhancement, proving in vivo alpha-1,2-mannosidase activity [PMID:16431915 "overexpression of the E147Q EDEM3 mutant... abolishes the stimulation of mannose trimming and greatly decreases the stimulation of ERAD by EDEM3. These results show that EDEM3 has alpha1,2-mannosidase activity in vivo"]. Notably distinguishes EDEM3 from EDEM (EDEM1) "which has no apparent alpha1,2-mannosidase activity."
- Yu et al. 2018 (JBC): the ER oxidoreductase ERp46 (TXNDC5) triggers EDEM3 mannose-trimming activity. ERp46 stably associates with EDEM3 via a disulfide bond between ERp46 redox-active cysteines and the EDEM3 alpha-mannosidase domain; this redox-dependent covalent interaction is REQUIRED to reconstitute EDEM3 trimming of misfolded TCRalpha in vitro [PMID:29784879 "the mannose-trimming activity of EDEM3 toward the model misfolded substrate... was reconstituted only when ERp46 had established a covalent interaction with EDEM3"]. This is the EDEM3 analog of the EDEM2-TXNDC11 redox pair (George 2020) - both EDEMs are gated by a disulfide-linked ER oxidoreductase.
- Manica et al. 2021 (IJMS): EDEM3 has four cooperating modules - GH47 (mannosidase, substrate binding), IMD (intermediate, needed for GH47 folding), PA (protease-associated), and IDD (intrinsically disordered). GH47 binds substrate even without trimming; PA and IDD do not affect trimming per se but modulate ERAD turnover timing of specific clients (NHK, soluble tyrosinase mutant). Few stable ER interactors -> transient substrate engagement [PMID:33671632 "the mannosidase domain provides substrate binding even in the absence of mannose trimming and requires the IMD domain for folding. The PA and IDD domains deletions... specifically modulate the turnover of two misfolded proteins"]. Defines EDEM3's role in setting ERAD timing/client selectivity.
- Ghionescu et al. 2025 (J Biomed Sci): EDEM3 is upregulated in HCC, highest in HBV-infected tumors, associated with progression/poor prognosis; EDEM3 overexpression attenuates UPR and activates secretory autophagy promoting HBV production, while depletion induces ER stress and apoptosis [PMID:39838427 "EDEM3-overexpressing hepatic cells exhibited attenuated UPR and activated secretory autophagy, which promoted HBV production"]. Pro-survival/pro-viral disease role.
- Lagou et al. 2023 (Nat Genet, PMID resolvable but NOT added): cross-ancestry random-glucose GWAS in 476,326 individuals nominated the EDEM3 locus (low-frequency coding variant) for glucose homeostasis - a genetic association, not a molecular-function finding, so notes-only.
- References ADDED to review: PMID:16431915 (Hirao 2006, HIGH), PMID:29784879 (Yu 2018, HIGH), PMID:33671632 (Manica 2021, HIGH), PMID:39838427 (Ghionescu 2025, MEDIUM). PMID:16431915 and PMID:29784879 added (id only, uncached) to core_function supported_by.
