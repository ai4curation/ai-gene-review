# PIF3 (Arabidopsis thaliana, At1g09530, UniProt O80536) — Review Notes

## Identity and structure
- PIF3 = PHYTOCHROME-INTERACTING FACTOR 3, also AtbHLH8 / bHLH008 / PAP3 / EN100.
- Basic helix-loop-helix (bHLH) transcription factor, 524 aa. bHLH domain 343-392 (UniProt FT DOMAIN). PROSITE BHLH (PS50888); Pfam HLH (PF00010). PANTHER PTHR46807 "TRANSCRIPTION FACTOR PIF3".
- Founding member of the phytochrome-interacting factor (PIF) family; bHLH subgroup 15 [PMID:23708772 "Phytochromeinteracting factors (PIFs) belonging to Arabidopsis basic helix-loop-helix (bHLH) subgroup 15 are key interacting proteins that play negative roles in light responses."].
- Contains an N-terminal active phytochrome B-binding (APB) motif region; characterized as PAS-domain-containing bHLH in original report [PMID:9845368 "a basic helix-loop-helix protein containing a PAS domain"].

## Core molecular function
- Sequence-specific DNA-binding transcription factor; binds the G-box element (5'-CACGTG-3') in target promoters. UniProt FUNCTION: "Activates transcription by binding to the G box (5'-CACGTG-3'), particularly in the dark but barely in far-red light".
- DNA binding and DNA-binding TF activity demonstrated experimentally (IDA) [PMID:31732705] (PIF8 paper that also assays PIF3 as a comparison/positive control: G-box binding and phyA-mediated sequestration). UniProt cross-ref GO:0003700 IDA:UniProtKB, GO:0043565 IDA:UniProtKB from this paper.
- DNA binding (IDA) also from anthocyanin ChIP study [PMID:17319847 "both PIF3 and HY5 regulate anthocyanin biosynthetic gene expression by directly binding to ... the gene promoters in vivo"].
- Homodimerizes and heterodimerizes via the HLH domain. UniProt SUBUNIT: "Homodimer (PubMed:25944101). Can form a heterodimer with REP1 and PIF4." GO:0042802 identical protein binding (IPI, self O80536) [PMID:10995393, PMID:12897250, PMID:21928113].

## Signaling / physical interactions
- Directly binds photoactivated phytochromes. phyB binds the Pfr (active) form of DNA-bound PIF3; reconversion to Pr causes dissociation [PMID:10466729 "full-length photoactive phytochrome B binds PIF3 in vitro only upon light-induced conversion to its active form, and that photoconversion back to its inactive form causes dissociation from PIF3"].
- Binds both phyA and phyB C-terminal domains [PMID:9845368 "PIF3 binds to wild-type C-terminal domains of both phyA and phyB"].
- phyB binds with greater apparent affinity than phyA; reaction requires the PAS domain of PIF3 [PMID:11069292 title].
- Many curated IPI partners (GOA WITH/FROM column): PHYA (P14712), PHYB (P14713), HFR1 (Q9FE22), PIF1 (Q8GZM7), PIF4 (Q8W2F3-2), RGA (Q9SLH3, a DELLA), APRR1/TOC1 (AT5G61380), HDA15 (Q8GXJ1), HEMERA/HMR/PTAC12 (F4IHY7), PIA2 (Q9FNP4), FYPP1/FYPP3 (Q9LHE7/Q9SX52). These are documented in UniProt SUBUNIT and INTERACTION sections.
- PIF3 protein is degraded in light and stabilized/activated in dark and by ethylene [PMID:29167353 "Light suppresses hypocotyl elongation by degrading transcription factor phytochrome-interacting factor 3 (PIF3), whereas the phytohormone ethylene promotes hypocotyl elongation by activating PIF3"].

## Biological roles
- Acts in red/far-red (phytochrome) light signaling, functioning largely as a negative regulator of photomorphogenesis (promotes skotomorphogenesis in the dark). [PMID:23548744 "a key basic helix-loop-helix transcription factor of Arabidopsis thaliana that negatively regulates light responses, repressing chlorophyll biosynthesis, photosynthesis, and photomorphogenesis in the dark"].
- Genetically required for normal phytochrome signaling; poc1 (PIF3 promoter T-DNA, overexpression) enhances phyB signaling [PMID:10318970 "consistent with PIF3 functioning as a positively acting signaling intermediate" ... "the poc1 mutation enhances phyB signal transduction"]. (Note: directionality of PIF3 in signaling is context-dependent; early work framed it as positively acting, later work emphasizes negative regulation of photomorphogenesis.)
- Represses chlorophyll biosynthesis and photosynthesis genes in etiolated seedlings by recruiting histone deacetylase HDA15 [PMID:23548744 "PIF3 associates with HDA15 to repress chlorophyll biosynthetic and photosynthetic genes in etiolated seedlings" ... "HDA15 and PIF3 cotarget to the genes involved in chlorophyll biosynthesis and photosynthesis in the dark and repress gene expression by decreasing the acetylation levels"]. This supports GO:0042548 regulation of photosynthesis, light reaction (IDA).
- Positively regulates anthocyanin biosynthesis in an HY5-dependent manner; binds anthocyanin biosynthetic gene promoters [PMID:17319847 "both PIF3 and HY5 positively regulate anthocyanin biosynthesis by activating the transcription of the same anthocyanin biosynthetic genes, but the positive effects of PIF3 required functional HY5"].
- Promotes hypocotyl cell elongation under light+ethylene by activating MDP60 (a microtubule-destabilizing protein) [PMID:29167353 "Ethylene signaling up-regulates MDP60 expression via PIF3 binding to the MDP60 promoter"]. Supports GO:0000976 cis-regulatory region binding (MDP60 = AT3G01015).
- Required for submergence/ethylene-induced underwater hypocotyl elongation; PIF3 is stabilized by ethylene signaling and drives MDP60 to reorganize cortical microtubules [PMID:31638649 "Submergence enhanced ethylene signaling, which then activated and stabilized its downstream transcription factor, phytochrome-interacting factor 3 (PIF3), to promote hypocotyl elongation"]. Disruption phenotype: inhibited submergence-induced hypocotyl elongation (UniProt DISRUPTION PHENOTYPE).
- Involved in gibberellin / light crosstalk preventing dark de-etiolation; PIF3 stabilized by GA/DELLA pathway [PMID:18053005 "stabilization of transcription factors that promote skotomorphogenesis, such as PIF3"].
- Acts in de-etiolation and prolonged red-light responses together with PIF4/PIF7 [PMID:18252845 title].

## Expression / induction (basis of the IEP "response to" annotations)
- PIF3 mRNA is up-regulated by ABA, ethylene, auxin, salt, cold and heat (this is transcript induction, not necessarily a dedicated functional role) [UniProt INDUCTION: "Up-regulated by abscisic acid (ABA), ethylene (ACC), auxin (IAA), salt (NaCl), cold and heat (PubMed:23708772)"]. The GOA IEP "response to heat/cold/ethylene/auxin/abscisic acid/salt" annotations (PMID:23708772) derive from these expression-induction observations in a review.

## Negative / refuted associations
- PIF3 does NOT have a significant role in the circadian clock; over/under-expression does not affect period length or light-resetting [PMID:16055924 "overexpression or lack of biologically functional PIF3 does not affect period length of rhythmic gene expression or red-light-induced resetting of the circadian clock"]. Supports the GOA NOT|involved_in GO:0007623 circadian rhythm (IMP) annotation.

## GO term definition checks (QuickGO API)
- GO:1990785 "response to water-immersion restraint stress" = "...as a result of water immersion while being held immobile." This is an animal restraint-stress model term; applying it to Arabidopsis submergence (PMID:31638649) is a mis-mapping of "submergence/water immersion." Over-annotation.
- GO:1905421 "regulation of plant organ morphogenesis" = modulation of plant organ form/structure. Defensible for hypocotyl elongation phenotype but quite general.

## Summary of curation judgments
- Core MF: sequence-specific DNA-binding transcription factor (G-box), protein dimerization (bHLH), binding to photoactivated phytochromes.
- Core BP: red/far-red light (phytochrome) signaling; negative regulation of photomorphogenesis (repression of chlorophyll/photosynthesis genes); transcriptional regulation.
- Non-core / developmental / stress-context BP: anthocyanin, hypocotyl elongation, submergence/ethylene responses, GA signaling, de-etiolation, the IEP hormone/abiotic "response to" terms.
- Generic "protein binding" (GO:0005515) IPI annotations: retained but not core (uninformative GO term per curation guidelines); the specific interactions are captured better in SUBUNIT/INTERACTION and in the dimerization/phytochrome-binding functions.
