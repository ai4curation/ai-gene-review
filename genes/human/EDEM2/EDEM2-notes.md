# EDEM2 (Q9BV94) review notes

## Identity
- ER degradation-enhancing alpha-mannosidase-like protein 2 (C20orf31/C20orf49). 578 aa precursor; signal peptide 1-21; soluble ER **lumenal** protein (NOT a type II membrane protein, unlike EDEM1). GH47 family (Pfam PF01532; InterPro IPR044674 EDEM1/2/3). N-glycosylated.

## Function (synthesis)
- EDEM2 catalyzes the **first** mannose-trimming step of mammalian gpERAD, converting Man9GlcNAc2 (M9) to Man8GlcNAc2 isomer B (M8B). This was the surprising, defining finding from endogenous knockout analysis [PMID:25092655 "the upstream mannose trimming from Man9GlcNAc2 to Man8GlcNAc2 is conducted mainly by EDEM2, which was previously considered to lack enzymatic activity"; "EDEM2, a novel-type Htm1 homologue that catalyzes the first mannose trimming step from Man9GlcNAc2"].
- The mannosidase activity requires the EF-hand glutamate E117; the E117Q mutant fails to rescue gpERAD [UniProt MUTAGEN 117 "E->Q: Loss of ERAD activity" ECO PubMed:25092655]; ["stable introduction of Flag-tagged hEDEM2, but not Flag-tagged hEDEM2-E117Q, into hEDEM2-KO cells restored degradation of endogenous hATF6"].
- Catalytic activity historically controversial: the original characterization found NO mannosidase activity for recombinant EDEM2 [PMID:15537790 "Using recombinantly generated EDEM2, no alpha-1,2 mannosidase activity was observed"] and proposed a lectin role; the later endogenous-KO study established the activity. UniProt CAUTION records both. This is the source of a NOT GO:0004571 IDA (PMID:15537790) and a positive GO:0004571 IMP (PMID:25092655) — a genuine historical tension. Do NOT remove either experimental annotation.
- EDEM2 is involved in ERAD of misfolded glycoproteins; overexpression accelerates degradation of misfolded alpha-1-antitrypsin (NHK) [PMID:15537790 "Overexpression of EDEM2 accelerates the degradation of misfolded alpha1-antitrypsin, indicating that the protein is involved in ERAD"]; associates with misfolded A1AT [PMID:15537790 "recombinant EDEM2 is localized to the ER where it can associate with misfolded alpha1-antitrypsin"].
- EDEM2 promotes ER-to-cytosol retrotranslocation (ricin A chain) [PMID:24200403 "EDEM2 is also involved in ricin retrotranslocation out of the ER"; "more ricin can interact with EDEM2 in comparison with EDEM1"]. IGI with EDEM1 (Q92611).
- Unlike EDEM1/EDEM3, EDEM2 does NOT bind SEL1L [PMID:25092655 "SEL1L... binds to EDEM1 and EDEM3 but not to EDEM2"]; EDEM2 acts upstream of EDEM1/3.
- (Gene-set context: EDEM2's mannosidase activity is demonstrated in a disulfide-linked complex with TXNDC11; not directly in cached pubs but consistent with the "novel-type Htm1 homologue" framing.)

## Localization
- ER lumen [PMID:15537790, EXP]. ER (IDA, PMID:24200403 MGI; PMID:15537790). ERQC (TAS Reactome).

## Annotation review decisions
- GO:0004571 mannosyl-oligosaccharide 1,2-alpha-mannosidase activity: IMP (PMID:25092655) ACCEPT — CORE (first trimming step). TAS Reactome x5 ACCEPT. The NOT/IDA (PMID:15537790) KEEP_AS_NON_CORE (historical, superseded). Note: GOA TAS Reactome entries are mostly labeled "MAN1B1 hydrolyses..." but cross-annotated to EDEM2 because EDEM2 performs analogous trimming; accept as mannosidase activity.
- GO:1904380 ER mannose trimming: IMP (PMID:25092655) ACCEPT core; TAS Reactome, IEA ACCEPT.
- GO:0036503 ERAD pathway: IMP x2 (PMID:15537790, 25092655) ACCEPT core.
- GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway (IBA): ACCEPT — specific and correct (N-glycan-dependent gpERAD).
- GO:0030968 endoplasmic reticulum unfolded protein response (IBA): EDEM2 is UPR/IRE1-XBP1 induced and acts in ERAD; "involved_in UPR" is defensible but peripheral. KEEP_AS_NON_CORE (the protein is UPR-induced and functions in the ERAD arm; not a UPR signaling component).
- GO:1904154 positive regulation of retrograde protein transport ER->cytosol (IMP/IGI PMID:24200403; IEA): ACCEPT/KEEP_AS_NON_CORE.
- GO:0036510 trimming of terminal mannose on C branch (TAS Reactome): a specific trimming sub-step; ACCEPT (KEEP_AS_NON_CORE; specific Reactome substep). Note EDEM2 mainly does Man9->Man8B (B branch); C-branch trimming is borderline but TAS-curated, keep.
- GO:0019082 viral protein processing (TAS Reactome, SARS-CoV-2 spike): real but peripheral; KEEP_AS_NON_CORE (mannosidase acting on viral substrate).
- GO:0005509 calcium ion binding (IEA): GH47 cofactor; KEEP_AS_NON_CORE.
- GO:0005788 ER lumen (IEA, EXP): ACCEPT.
- GO:0005783 ER (IDA x2): ACCEPT.
- GO:0044322 ERQC (TAS x5): ACCEPT.
- GO:0005975 carbohydrate metabolic process / GO:0009100 glycoprotein metabolic process / GO:0016020 membrane (IEA): over-general -> MARK_AS_OVER_ANNOTATED. Note membrane is also arguably WRONG (EDEM2 is luminal/soluble), but InterPro-derived; mark over-annotated (uninformative; EDEM2 is luminal).
</content>

## Falcon deep-research findings (incorporated 2026-06)
- George et al. 2020 (eLife) is the central mechanistic paper: EDEM2 is stably disulfide-bonded to TXNDC11 (EDEM2 Cys558 to TXNDC11 Cys692, in TXNDC11 Trx5 CXXC motif), and this covalent bond is essential for the first mannose-trimming step and gpERAD in HCT116 cells [PMID:32065582 "EDEM2 was stably disulfide-bonded to TXNDC11, an endoplasmic reticulum protein containing five thioredoxin (Trx)-like domains. C558... was linked to C692 in Trx5... This covalent bonding was essential for mannose trimming and subsequent gpERAD"].
- George 2020 provides the FIRST in vitro demonstration of EDEM-family mannosidase activity: the purified EDEM2-TXNDC11 complex converts Man9GlcNAc2 to Man8GlcNAc2 isomer B, reconciling the earlier "no activity" result for recombinant EDEM2 alone [PMID:32065582 "EDEM2-TXNDC11 complex purified from transfected HCT116 cells converted Man9GlcNAc2 to Man8GlcNAc2 (isomerB) in vitro... represent the first clear demonstration of in vitro mannosidase activity of EDEM family proteins"]. This is the disulfide-bonded-partner mechanism the notes previously flagged as "not in cached pubs."
- Shenkman et al. 2018 (Commun Biol): EDEM2 mannosidase activity is folding-state dependent - modest on free glycans/native glycoproteins but markedly higher on denatured glycoproteins; EDEM2 associates with oxidoreductases including TXNDC11 and PDI, which enhance activity on glycoproteins but not free N-glycans [PMID:30374462 "mannosidase activity of ERManI and the EDEMs is significantly higher on a denatured glycoprotein. The EDEMs associate with oxidoreductases, protein disulfide isomerase, and especially TXNDC11"].
- Ninagawa et al. 2024 (eLife, doi:10.7554/eLife.93117): glycoprotein fate is a tug-of-war between UGGT1-mediated reglucosylation (folding) and EDEM-mediated mannose trimming (degradation); EDEM2 provides the initiating M9->M8B step upstream of EDEM1/EDEM3 [PMID:39654396 "the fate of glycoproteins is determined by a tug-of-war between structure formation by UGGT1 and degradation by EDEMs"].
- Murase et al. 2023 (BPB Reports, doi:10.1248/bpbreports.6.6_193, NOT added as a formal reference - lower priority/3 citations): EDEM2 protein is strongly post-transcriptionally regulated; TXNDC11 deficiency decreases EDEM2 protein (TXNDC11 supports EDEM2 stability), and EDEM2 is itself partly a SEL1L-mediated ERAD substrate.
- Wu et al. 2023 (Front Oncol) reports EDEM2 as a glioma biomarker (overexpression, prognosis, immune infiltration); not incorporated as it is correlative disease-association data not directly establishing molecular function.
- References ADDED to review: PMID:32065582 (George 2020, HIGH), PMID:30374462 (Shenkman 2018, MEDIUM), PMID:39654396 (Ninagawa 2024, MEDIUM). PMID:32065582 also added (id only, no supporting_text - uncached) to the first core_function supported_by.
