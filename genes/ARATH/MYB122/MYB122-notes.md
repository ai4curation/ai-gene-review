# MYB122 (At1g74080, UniProt Q9C9C8) — curation notes

## Identity and domain structure

- R2R3-MYB transcription factor, 333 aa; two HTH myb-type repeats (R2 9-61, R3 62-116) with HTH DNA-binding motifs, followed by disordered C-terminal region (UniProt Q9C9C8 features).
- Member of R2R3-MYB subgroup 12 with MYB28, MYB29, MYB76 (aliphatic GSL regulators) and MYB34/ATR1, MYB51/HIG1 (indolic GSL regulators). MYB122 is the closest homologue of MYB51.
- PANTHER PTHR47994:SF5 (UniProt DR line).
- UniProt FUNCTION: "Transcription factor involved in glucosinolates biosynthesis." SUBUNIT: complexes with MYC2/MYC3/MYC4 [PMID:23943862]. Location: nucleus (ECO:0000305, by similarity/inference).

## Family, paralogs and phylogenetic (PAINT) context

- InterPro: IPR009057 Homeodomain-like_sf, IPR017930 Myb_dom, IPR001005 SANT/Myb, IPR015495 Myb_TF_plants (UniProt DR lines).
- PANTHER: MYB122 and MYB34 both map to PTHR47994:SF5 ("F14D16.11-RELATED"), whereas MYB51 maps to PTHR10641:SF1309 (TRANSCRIPTION FACTOR MYB51) — i.e. PANTHER splits the IG-MYB triad across two families, so there is no shared PAINT node for the three.
- No IBA annotations exist for MYB122, MYB34 or MYB51 in their GOA files, so no PAINT judgement constrains MYB122's GO profile. Function inference therefore rests on direct genetic/metabolite evidence for MYB122 plus paralog (MYB34/MYB51) behaviour.
- Paralog evidence: MYB51/HIG1 activates IG biosynthetic gene promoters and loss of function lowers IG [PMID:17461791 "HIG1/MYB51 was shown to activate promoters of indolic glucosinolate biosynthetic genes leading to increased accumulation of indolic glucosinolates."]. MYB34 and MYB51 carry GO:0009759 IMP in TAIR; aliphatic subgroup-12 paralogs MYB28/MYB29/MYB76 carry GO:0010439 IMP (QuickGO comparator check).
- Orthologs: subgroup-12 GSL MYBs are a Brassicales-specific radiation (GSL pathway is restricted to Brassicales); no ortholog-derived experimental annotation was used.

## Deep research status

- `just deep-research-falcon ARATH MYB122 --fallback perplexity-lite`: falcon timed out after 600 s; perplexity-lite fallback unavailable in this environment ("Provider 'perplexity' not available"). Retried with `just deep-research ARATH MYB122 --provider asta`, which succeeded (MYB122-deep-research-asta.md). The falcon job also eventually wrote MYB122-deep-research-falcon.md (796 s run) despite the wrapper timeout. Both were used only as leads; claims below are anchored to cached abstracts/full texts. Review synthesized directly from primary literature fetched via PubMed and `just fetch-pmid`.

## Function: indolic glucosinolate (IG) regulation

- Overexpression of MYB122 raises IG levels and causes a high-auxin phenotype, but does not rescue hig1-1 (myb51) [PMID:17461791 "Overexpression of MYB122, another close homologue of HIG1/MYB51, did not rescue the hig1-1 chemotype, but caused a high-auxin phenotype and increased levels of indolic glucosinolates in the wild-type."]
- MYB34, MYB51 and MYB122 act together; MYB122 accessory [PMID:24431192 "MYB34, MYB51, and MYB122 act together to control the biosynthesis of I3M in shoots and roots, with MYB34 controlling biosynthesis of IGs mainly in the roots, MYB51 regulating biosynthesis in shoots, and MYB122 having an accessory role in the biosynthesis of IGs."]
- Triple mutant devoid of IGs [PMID:24431192 "The myb34 myb51 myb122 triple mutant is devoid of IGs, indicating that these three MYB factors are indispensable for IG production under standard growth conditions."]
- Minor role in JA/ET-induced IG [PMID:24431192 "MYB122 plays only a minor role in JA/ET-induced glucosinolate biosynthesis"].
- Brassinosteroid repression of GSL requires MYB122 [PMID:23580754 "The deficiency of MYB34 and MYB122 lost the responsive ability to the application of BR"]; myb122 loss of function reduces IG [PMID:23580754 "MYB34, MYB51 and MYB122 loss-of-function mutation all conferred reduced indolic glucosinolate levels."]
- Target promoters (group-level statement): TSB1, CYP79B2, CYP79B3 [PMID:23580754 "MYB34, MYB51, and MYB122, identified as regulators of the indolic glucosinolate biosynthetic pathway, exclusively trans-activate the promoters of TSB1, CYP79B2, and CYP79B3"].
- MYC2/3/4 interact with GS-related MYBs [PMID:23943862 "yeast two-hybrid and pull-down experiments indicated that MYC2/MYC3/MYC4 interact directly with GS-related MYBs"].
- MYB122 expression downstream of MPK3/MPK6–ERF6 during Botrytis infection [PMID:27081184 "MPK3/MPK6 regulate the expression of MYB51 and MYB122, two key regulators of IGS biosynthesis"].
- Copper-induced IGS and defense: MYB51/MYB122 redundant [PMID:33756355, not cached; noted from PubMed abstract only, not used as evidence].

## Camalexin and IAOx supply

- Frerigmann et al. 2015 [PMID:26379682 "The abundance of camalexin was strongly reduced in myb34/51 and myb51/122 double and in triple myb mutant, suggesting that these transcription factors are important in camalexin biosynthesis."]; MYB122 induced by camalexin-inducing agents [PMID:26379682 "expression of MYB51 and MYB122 was significantly increased by biotic and abiotic camalexin-inducing agents"]; action upstream of IAOx [PMID:26379682 "supports a role for the three MYB factors in camalexin biosynthesis upstream of IAOx"]; MYBs do not activate the PAD3 promoter.
- Contrasting: pathogen-triggered camalexin not compromised in triple mutant [PMID:26802248 "gene induction and accumulation of ICAs and camalexin upon pathogen infection was not compromised in myb34/51/122 plants"]. Stahl 2016 [PMID:26802249] positive effect at P. syringae sites.
- Interpretation: MYB122 (with paralogs) controls CYP79B2/B3-dependent IAOx supply; camalexin effects are condition-dependent and indirect. No NEW camalexin term proposed (GO:1901183 positive regulation of camalexin biosynthetic process exists but evidence is inconsistent and largely from double/triple mutants).

## Hormone crosstalk partners

- BES1 interacts with MYB34, MYB51 and MYB122 to repress IG genes during herbivory [PMID:31776183 "BES1 inhibited biosynthesis of the JA-induced insect defense-related metabolite indolic glucosinolate by interacting with transcription factors MYB DOMAIN PROTEIN34 (MYB34), MYB51, and MYB122"].
- MYC2/3/4 interaction (activation arm) [PMID:23943862].

## Pathogen defense

- Tang et al. 2023 (PMID:37741284; cache is abstract-only; full text read from user-supplied PDF): single-cell atlas of Arabidopsis leaves infected with Colletotrichum higginsianum. Of the three IG MYBs, only MYB51 and MYB122 were induced at infection sites, with strict cell-type specificity: MYB122 only in epidermis, MYB51 only in vasculature (Fig. 6B,C, S6B). Two T-DNA insertion lines (SALK_027525 = myb122-1, second line myb122-2) showed larger lesions at 5 dpi (Fig. 6D) and accelerated invasive hyphal branching (more secondary IH) in epidermal cells at 36 and 42 hpi (Fig. 6E,F). Authors infer MYB122 restricts biotrophic growth, "presumably through elevating the production of GSL-related antimicrobial metabolites in epidermal cells" — the metabolite link was NOT measured.
  - Abstract quote: [PMID:37741284 "emphasizing the contribution of the epidermis-expressed MYB122 to disease resistance"].
  - Caveat: the paper's key-resources table lists the myb122 lines as "AT3G25800" (which is not MYB122; MYB122 is At1g74080) and labels myb122-2 as a "CRISPR line" while the text calls both T-DNA lines. Probably clerical errors; qRT-PCR confirmed loss of MYB122 transcript (Fig. S6C). Worth flagging to authors/curators.
  - GOA already carries GO:0050832 defense response to fungus (IDA, TAIR) from this paper; evidence is really a mutant phenotype (IMP would be more apt), but the annotation itself is sound.
- Frerigmann et al. 2016 [PMID:26802248]: myb34/51/122 triple mutant susceptible to Plectosphaerella cucumerina similar to pen2 [abstract: "MYB34/51/122 contribute to resistance toward P. cucumerina exclusively through IG biosynthesis"]; camalexin induction upon infection not compromised in triple mutant.
- Stahl et al. 2016 [PMID:26802249]: "Camalexin accumulation is positively affected by MYB122" at P. syringae inoculation sites — partly contrasts with Frerigmann 2016 for camalexin; not used for a NEW annotation.

## Expression

- Trichomes [UniProt, PMID:23115560].
- Induced by Brevicoryne brassicae aphid feeding [PMID:23144921 "Transcript levels of MYB122 were up-regulated as a result of feeding by B. brassicae in all water treatments."] — supports IEP response to insect.

## Other annotations

- Y1H promoter binding (TAIR IPI GO:0000976): nitrogen network (Gaudinier 2018, PMID:30356219, promoter AT2G22810) and PXY vascular network (Smit 2020, PMID:31806676, promoter AT2G34710). Large-scale eY1H screens; evidence for sequence-specific DNA binding to cis-regulatory regions is consistent with R2R3-MYB.
- Plasmodesma HDA (PMID:21533090): proteomic list with acknowledged ~35% cytoplasmic contaminants; a nuclear TF is most likely a contaminant.

## Decisions summary

- Core MF: DNA-binding transcription factor activity (GO:0003700); cis-regulatory region binding (GO:0000976).
- Core BP: regulation of glucosinolate biosynthetic process (GO:0010439) — proposed NEW. Comparator check: MYB28, MYB29, MYB76 (aliphatic GSL MYB regulators, same subgroup, same role) carry GO:0010439 in TAIR/GOA (QuickGO query 2026-10). MYB34/MYB51 carry GO:0009759 IG biosynthetic process (acts_upstream_of_or_within). MYB122 has neither; the TF performs the regulatory step (direct promoter trans-activation), so the participation test is met for a regulation term.
- defense response to fungus: accept (Tang 2023).
- Not proposing camalexin terms (conflicting evidence).
