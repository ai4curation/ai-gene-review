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
