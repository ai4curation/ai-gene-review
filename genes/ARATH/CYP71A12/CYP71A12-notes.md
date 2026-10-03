# CYP71A12 (At2g30750, UniProt O49340) — curation notes

## Sources used
- UniProt O49340 (Swiss-Prot): function "Converts indole-3-acetaldoxime to indole cyanohydrin. Involved in the biosynthetic pathway to 4-hydroxyindole-3-carbonyl nitrile (4-OH-ICN)"; single-pass membrane; interaction with CYP71B15 (IntAct, 5 experiments).
- Deep research: `CYP71A12-deep-research-falcon.md` (Edison/falcon). Used for orientation; claims below are anchored to cached PMIDs.
- Cached publications: PMID:17573535 (abstract only), PMID:31511315 (abstract only), PMID:23073694 (full text), PMID:39627368 (full text), PMID:26352477 (full text), PMID:21712415 (full text). Newly cached: PMID:24151049 (full text), PMID:25953104 (abstract only), PMID:31411742 (abstract only).
- PMID:33831160 (GOA source for the ER lumen IDA) is a deleted PubMed duplicate of PMID:31511315 (Mucha et al. 2019). Handled as in genes/ARATH/CYP71B15: is_invalid + replacement DUPLICATE_RECORD.

## Biochemistry
- Tandem paralog of CYP71A13; ~89.5% identity [PMID:24151049 "CYP71A12 shares 89.5% amino acid identity with CYP71A13"].
- Turns over IAOx at a rate similar to CYP71A13 but with a different product ratio (more IAL, less Cys-IAN) [PMID:24151049 "Although CYP71A12 turned over IAOx at a rate comparable to that of CYP71A13"].
- 18O2 labelling shows monooxygenation to an alpha-hydroxy-IAN (indole-3-cyanohydrin) intermediate [PMID:24151049 "both CYP71A13 and CYP71A12 catalyze incorporation of the isotopic label into IAL"]. So "IAOx dehydratase" (GO:0047720, IAOx -> IAN + H2O) is an over-simplification of the chemistry for both paralogs; the product for CYP71A12 is chiefly the cyanohydrin, which collapses to indole-3-carbaldehyde + HCN [PMID:25953104 "for CYP71A12, indole-3-carbaldehyde and cyanide were identified as major reaction products"].
- Substituting CYP71A12 for CYP71A13 in in vitro reconstitution still yields camalexin, at lower levels [PMID:24151049 "Substituting CYP71A12 in place of CYP71A13 also resulted in camalexin production, albeit at lower levels"].

## Pathways
- Camalexin: minor contributor. cyp71a12 cyp71a13 double knockouts make only traces of camalexin [PMID:25953104 "double mutants synthesized only traces of camalexin, demonstrating that CYP71A12 contributes to camalexin biosynthesis in leaf tissue"]. Metabolon paper: [PMID:31511315 "indole-3-cyanohydrin, which is synthesized by CYP71A12 and especially CYP71A13"].
- ICOOH / ICA: major enzyme [PMID:25953104 "A major role of CYP71A12 was identified for the inducible biosynthesis of ICOOH."]; [PMID:31411742 "CYP71A12, but not CYP71A13, is the major enzyme responsible for the accumulation of ICA in Arabidopsis in response to pathogen ingression"].
- ICN / 4-OH-ICN: first committed enzyme upstream of FOX1 and CYP82C2 [PMID:26352477 "all ICN derivatives with the exception of A6 are at ~10% of WT levels in the cyp71A12 mutant, but unaffected in the cyp71A13 and cyp71A18 mutants"]; reconstitution [PMID:26352477 "A combination of yeast microsomal CYP71A12 and CYP82C2 and N. benthamiana-expressed FOX1 was sufficient to catalyze the conversion of IAOx to ICN"].

## Location
- Single N-terminal anchor; ER-anchored with cytosolic catalytic domain, as for the other camalexin P450s [PMID:21712415 "associated with the endoplasmic reticulum, having their catalytic domain facing the cytosol"]. Deep research reports CYP71A12-GFP colocalizing with RFP-HDEL in N. benthamiana (Mucha 2019, full text not cached). ER lumen IDA conflicts with this topology -> UNDECIDED (as for CYP71B15), propose ER membrane.

## Phenotypes (necessity, not mechanism)
- cyp71A12 more susceptible to Pst DC3000 [PMID:26352477]; cyp71a12 cyp71a13 double mutant up to 120-fold more Pst [PMID:39627368]; CYP71A12 strongly induced by leaf commensals (GNSR marker gene) [PMID:39627368].
- Pf.SS101 rhizobacterium-induced resistance requires camalexin/glucosinolate pathway genes including cyp71A12 [PMID:23073694], but that response is SA-dependent [PMID:23073694 "the Pf .SS101 -induced resistance response to Pst is dependent on salicylic acid signaling"], while GO:0009682 induced systemic resistance is defined as SA-independent. CYP71A12 makes defence metabolites; it does not carry out the systemic signalling. ISR rows marked over-annotated.
- Pastorczyk 2020: CYP71A12 and CYP71A13 key for post-invasive resistance to filamentous pathogens [PMID:31411742]. Did not add a NEW "defense response to fungus" row: this is necessity evidence; the mechanistic term (metabolite biosynthesis) is the core function (project curation question 3).

## Decisions
- Core MF: monooxygenase activity (GO:0004497) on IAOx; specific activity (IAOx -> indole-3-cyanohydrin) has no GO term -> proposed new term. GO:0047720 deliberately not asserted (consistent with modules/camalexin_biosynthesis.yaml, and the 18O data argue the product is the cyanohydrin rather than IAN).
- Core BP: camalexin biosynthetic process (minor), indole-containing compound biosynthetic process (ICN/ICA branch; no specific GO term exists — CYP82C2 comparator carries no ICN pathway BP term either, so no NEW row).
- Protein binding (IPI with CYP71B15) REMOVE, same as CYP71B15 review.
