# FBF1 review notes

## 2026-10-03: sources and scope

- GOA snapshot 28 rows; UniProt Q8TES7. GOA PMIDs cached (PMID:23348840 abstract-only; PMID:18838552 and PMID:21399614 full text).
- Additional papers: PMID:29789620 (FBF1 in the distal appendage matrix; gating), PMID:24231678 (FBF1/DYF-19 and IFT entry), PMID:30131441 (LRRC45 recruits FBF1).
- Deep research: first falcon run timed out at 600 s; the rerun with `--timeout 2400` succeeded (`FBF1-deep-research-falcon.md`).

## Functional synthesis

- FBF1 is one of the five DAP proteins and is recruited downstream of SCLT1 [PMID:23348840 "Subsequent recruitment of FBF1 and CEP164 is independent of CEP89 but mediated by SCLT1."], and also via LRRC45 [PMID:30131441 "Once there, LRRC45 recruits the keratin-binding protein FBF1."]
- Unlike the blade proteins, FBF1 sits in the distal appendage matrix and is needed for gating [PMID:29789620 "By contrast, FBF1 marks the distal end of the DAM near the ciliary membrane. Strikingly, unlike CEP164, which is essential for ciliogenesis, FBF1 is required for ciliary gating of transmembrane proteins"]
- The worm orthologue DYF-19 binds IFT-B and admits IFT trains into the cilium, a function shared by human FBF1 [PMID:24231678 "Here we report that FBF1, a highly conserved transition fibre protein, is required for the ciliary import of assembled IFT particles at the ciliary base."] and [PMID:24231678 "Furthermore, we found that human FBF1 shares conserved localization and function with its worm counterpart."]
- Epithelial role (Albatross): forms a complex with Par3 and is needed for apical junction formation and polarity [PMID:18838552 "Here, we show that Albatross complexes with Par3 to regulate formation of the apical junctional complex (AJC) and maintain lateral membrane identity."]

- In FBF1-knockout cells initiation proceeds but cilia rarely form [PMID:29789620 "Both CP110 removal and TTBK2 recruitment occurred normally in FBF1−/− cells (~ 70%), compared with WT cells (~ 80%) and yet cilia were detected in only ~ 14% of the population"]. So FBF1 acts after mother-centriole licensing.
- Deep research summary [file:human/FBF1/FBF1-deep-research-falcon.md "Its experimentally best-supported function is **non-enzymatic organization of a selective ciliary gate**"]. It also reports that TALPID3-ANKRD26 and DZIP1L-ANKRD26 position FBF1 at transition fibers (Yan 2020; Chen 2024), an FBF1-AKAP9/BBS12 role at the ciliary base in adipocyte precursors (Zhang 2021, mouse hypomorph), and delayed cilium disassembly after Fbf1 knockdown in NIH3T3 cells (Je and Ko 2024). These were not cached or used for annotation.

## Annotation decisions

- Accept centriole, centrosome, basal body, transition fiber and cilium assembly rows; both knockdown and knockout reduce ciliation, but knockout cells still remove CP110 and recruit TTBK2.
- Epithelial polarity, apical junction assembly, AJC/keratin colocalization, anchoring junction: non-core.
- Spindle pole, Reactome cytosol: non-core. PARD3 protein binding: remove.
- No molecular function asserted in core_functions (none established).

## HPA cilium atlas vs module role

- Module role: "distal appendage component" (stage 1, mother centriole licensing).
- HPA v25: Primary cilium (Uncertain); Basal body (Supported); Centrosome (Supported); main locations basal body and centrosome.
- Comparison: HPA localization agrees with FBF1 being at the basal body. However, the module places FBF1 in an assembly hierarchy that licenses the mother centriole. The literature argues FBF1 is not a structural scaffold for that hierarchy: it sits in the appendage matrix, its knockout still removes CP110 and recruits TTBK2 (so it is not needed for licensing), and its demonstrated function is gating entry of IFT trains and membrane proteins at the ciliary base. core_functions therefore describe a gating/IFT-entry role at the transition fibers. This is a partial disagreement with the module, which could note FBF1's role in the transition zone/IFT-entry stage as well as stage 1.
