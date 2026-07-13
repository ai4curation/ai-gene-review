---
title: "PSEPK ppu02010 ABC transporter cluster report"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02010 ABC Transporter Cluster Report

- Candidate genes: 207
- Locus-neighborhood clusters: 74
- Review status: {'PRESENT': 207}
- Asta status: {'PRESENT': 207}

## Product-Class Summary

| Product class | Genes | Missing reviews | Dominant-neighborhood clusters |
|---|---:|---:|---:|
| methionine/amino acid/polyamine | 63 | 0 | 20 |
| general ABC | 38 | 0 | 14 |
| metal/cobalamin/siderophore | 22 | 0 | 7 |
| sulfur/sulfonate/taurine | 20 | 0 | 9 |
| sugar/polyol | 17 | 0 | 4 |
| lipid/lps/lipoprotein | 14 | 0 | 6 |
| phosphate/phosphonate/glycerol-phosphate | 14 | 0 | 4 |
| osmoprotectant/choline/betaine/carnitine | 12 | 0 | 6 |
| efflux/secretion/toxin | 4 | 0 | 3 |
| other | 3 | 0 | 1 |

## Candidate Sub-Batch Guidance

- Do not treat `ppu02010` as a single satisfiable pathway. It is an umbrella map for many unrelated ABC import/export systems.
- Reuse already curated sulfur-transporter members from `sulfur_metabolism_boundary` rather than reopening them unless a warning appears.
- Good first sub-batches are coherent locus blocks with recognizable substrates: methionine/zinc at PP_0112-PP_0120, sulfur/cystine at PP_0225-PP_0240, choline/betaine/carnitine at PP_0294-PP_0304, phosphonate at PP_0824-PP_0827, and zinc/nickel/metal systems.
- Large generic ABC clusters should be deferred until substrate-specific neighbors or module context are clearer.

## Locus-Neighborhood Clusters

| Cluster | Locus span | Size | Dominant class | Review status | Asta status | Genes |
|---|---|---:|---|---|---|---|
| ppu02010-C01 | PP_0076-PP_0076 | 1 | osmoprotectant/choline/betaine/carnitine | PRESENT:1 | PRESENT:1 | PP_0076 |
| ppu02010-C02 | PP_0112-PP_0120 | 6 | methionine/amino acid/polyamine | PRESENT:6 | PRESENT:6 | metQ, metI, metN1, znuB, znuC, PP_0120 |
| ppu02010-C03 | PP_0140-PP_0142 | 3 | general ABC | PRESENT:3 | PRESENT:3 | PP_0140, PP_0141, PP_0142 |
| ppu02010-C04 | PP_0167-PP_0172 | 4 | general ABC | PRESENT:4 | PRESENT:4 | paxB, PP_0170, PP_0171, PP_0172 |
| ppu02010-C05 | PP_0207-PP_0209 | 3 | sulfur/sulfonate/taurine | PRESENT:3 | PRESENT:3 | PP_0207, PP_0208, tauB-I |
| ppu02010-C06 | PP_0219-PP_0221 | 3 | methionine/amino acid/polyamine | PRESENT:3 | PRESENT:3 | metP, metN2, PP_0221 |
| ppu02010-C07 | PP_0225-PP_0227 | 3 | sulfur/sulfonate/taurine | PRESENT:3 | PRESENT:3 | sctC, sctS, fliY |
| ppu02010-C08 | PP_0231-PP_0233 | 3 | sulfur/sulfonate/taurine | PRESENT:3 | PRESENT:3 | tauC, tauB, tauA |
| ppu02010-C09 | PP_0237-PP_0240 | 3 | sulfur/sulfonate/taurine | PRESENT:3 | PRESENT:3 | ssuA, ssuC, ssuB |
| ppu02010-C10 | PP_0280-PP_0283 | 4 | methionine/amino acid/polyamine | PRESENT:4 | PRESENT:4 | PP_0280, PP_0281, artJ, aotP |
| ppu02010-C11 | PP_0294-PP_0296 | 3 | osmoprotectant/choline/betaine/carnitine | PRESENT:3 | PRESENT:3 | cbcV, cbcW, cbcX |
| ppu02010-C12 | PP_0304-PP_0304 | 1 | osmoprotectant/choline/betaine/carnitine | PRESENT:1 | PRESENT:1 | caiX |
| ppu02010-C13 | PP_0524-PP_0524 | 1 | metal/cobalamin/siderophore | PRESENT:1 | PRESENT:1 | PP_0524 |
| ppu02010-C14 | PP_0615-PP_0619 | 5 | methionine/amino acid/polyamine | PRESENT:5 | PRESENT:5 | PP_0615, PP_0616, PP_0617, PP_0618, PP_0619 |
| ppu02010-C15 | PP_0804-PP_0804 | 1 | efflux/secretion/toxin | PRESENT:1 | PRESENT:1 | PP_0804 |
| ppu02010-C16 | PP_0824-PP_0827 | 4 | phosphate/phosphonate/glycerol-phosphate | PRESENT:4 | PRESENT:4 | ptxB, phnC, phnE, ptxC |
| ppu02010-C17 | PP_0868-PP_0873 | 5 | osmoprotectant/choline/betaine/carnitine | PRESENT:5 | PRESENT:5 | yehX, yehW, PP_0870, PP_0871, potF-I |
| ppu02010-C18 | PP_0878-PP_0885 | 7 | methionine/amino acid/polyamine | PRESENT:7 | PRESENT:7 | dppF, dppD, dppC, dppB, dppA-I, dppA-II, dppA-III |
| ppu02010-C19 | PP_0953-PP_0953 | 1 | lipid/lps/lipoprotein | PRESENT:1 | PRESENT:1 | lptB |
| ppu02010-C20 | PP_0958-PP_0962 | 5 | lipid/lps/lipoprotein | PRESENT:5 | PRESENT:5 | mlaF, mlaE, mlaD, ttg2D, ttg2E |
| ppu02010-C21 | PP_0982-PP_0983 | 2 | lipid/lps/lipoprotein | PRESENT:2 | PRESENT:2 | PP_0982, PP_0983 |
| ppu02010-C22 | PP_1015-PP_1018 | 4 | sugar/polyol | PRESENT:4 | PRESENT:4 | gtsA, gtsB, gtsC, gtsD |
| ppu02010-C23 | PP_1068-PP_1071 | 4 | general ABC | PRESENT:4 | PRESENT:4 | gltL, gltK, gltJ, gltI |
| ppu02010-C24 | PP_1078-PP_1078 | 1 | general ABC | PRESENT:1 | PRESENT:1 | PP_1078 |
| ppu02010-C25 | PP_1137-PP_1141 | 5 | methionine/amino acid/polyamine | PRESENT:5 | PRESENT:5 | livF-I, livG, livM, livH, livK |
| ppu02010-C26 | PP_1297-PP_1300 | 4 | methionine/amino acid/polyamine | PRESENT:4 | PRESENT:4 | yhdW, yhdX, yhdY, yhdZ |
| ppu02010-C27 | PP_1741-PP_1741 | 1 | osmoprotectant/choline/betaine/carnitine | PRESENT:1 | PRESENT:1 | betX |
| ppu02010-C28 | PP_1778-PP_1779 | 2 | general ABC | PRESENT:2 | PRESENT:2 | PP_1778, PP_1779 |
| ppu02010-C29 | PP_2154-PP_2156 | 3 | lipid/lps/lipoprotein | PRESENT:3 | PRESENT:3 | lolC, lolD, lolE |
| ppu02010-C30 | PP_2195-PP_2195 | 1 | methionine/amino acid/polyamine | PRESENT:1 | PRESENT:1 | PP_2195 |
| ppu02010-C31 | PP_2240-PP_2240 | 1 | efflux/secretion/toxin | PRESENT:1 | PRESENT:1 | PP_2240 |
| ppu02010-C32 | PP_2260-PP_2264 | 5 | sugar/polyol | PRESENT:5 | PRESENT:5 | PP_2260, PP_2261, PP_2262, PP_2263, PP_2264 |
| ppu02010-C33 | PP_2454-PP_2459 | 4 | sugar/polyol | PRESENT:4 | PRESENT:4 | rbsB, rbsA-I, rbsC, rbsD |
| ppu02010-C34 | PP_2560-PP_2560 | 1 | efflux/secretion/toxin | PRESENT:1 | PRESENT:1 | aprDA |
| ppu02010-C35 | PP_2595-PP_2596 | 2 | general ABC | PRESENT:2 | PRESENT:2 | PP_2595, PP_2596 |
| ppu02010-C36 | PP_2628-PP_2628 | 1 | general ABC | PRESENT:1 | PRESENT:1 | PP_2628 |
| ppu02010-C37 | PP_2656-PP_2659 | 4 | phosphate/phosphonate/glycerol-phosphate | PRESENT:4 | PRESENT:4 | pstS, pstC, pstA, pstB1 |
| ppu02010-C38 | PP_2748-PP_2753 | 6 | methionine/amino acid/polyamine | PRESENT:6 | PRESENT:6 | PP_2748, PP_2749, PP_2750, PP_2751, PP_2752, PP_2753 |
| ppu02010-C39 | PP_2757-PP_2761 | 5 | sugar/polyol | PRESENT:5 | PRESENT:5 | PP_2757, PP_2758, rbsA, PP_2760, PP_2761 |
| ppu02010-C40 | PP_2767-PP_2770 | 4 | methionine/amino acid/polyamine | PRESENT:4 | PRESENT:4 | PP_2767, PP_2768, PP_2769, PP_2770 |
| ppu02010-C41 | PP_2774-PP_2775 | 2 | osmoprotectant/choline/betaine/carnitine | PRESENT:2 | PRESENT:2 | opuA, PP_2775 |
| ppu02010-C42 | PP_3076-PP_3078 | 3 | general ABC | PRESENT:3 | PRESENT:3 | PP_3076, PP_3077, PP_3078 |
| ppu02010-C43 | PP_3147-PP_3147 | 1 | methionine/amino acid/polyamine | PRESENT:1 | PRESENT:1 | potF-II |
| ppu02010-C44 | PP_3217-PP_3217 | 1 | sulfur/sulfonate/taurine | PRESENT:1 | PRESENT:1 | PP_3217 |
| ppu02010-C45 | PP_3228-PP_3229 | 2 | sulfur/sulfonate/taurine | PRESENT:2 | PRESENT:2 | PP_3228, PP_3229 |
| ppu02010-C46 | PP_3342-PP_3346 | 5 | metal/cobalamin/siderophore | PRESENT:5 | PRESENT:5 | nikA, nikB, nikC, nikD, nikE |
| ppu02010-C47 | PP_3528-PP_3528 | 1 | sulfur/sulfonate/taurine | PRESENT:1 | PRESENT:1 | PP_3528 |
| ppu02010-C48 | PP_3558-PP_3559 | 2 | methionine/amino acid/polyamine | PRESENT:2 | PRESENT:2 | PP_3558, PP_3559 |
| ppu02010-C49 | PP_3719-PP_3719 | 1 | methionine/amino acid/polyamine | PRESENT:1 | PRESENT:1 | PP_3719 |
| ppu02010-C50 | PP_3801-PP_3803 | 3 | general ABC | PRESENT:3 | PRESENT:3 | PP_3801, PP_3802, PP_3803 |
| ppu02010-C51 | PP_3818-PP_3818 | 1 | phosphate/phosphonate/glycerol-phosphate | PRESENT:1 | PRESENT:1 | PP_3818 |
| ppu02010-C52 | PP_3828-PP_3830 | 3 | general ABC | PRESENT:3 | PRESENT:3 | modA, modB, modC |
| ppu02010-C53 | PP_3845-PP_3845 | 1 | methionine/amino acid/polyamine | PRESENT:1 | PRESENT:1 | potF-III |
| ppu02010-C54 | PP_4146-PP_4150 | 5 | methionine/amino acid/polyamine | PRESENT:5 | PRESENT:5 | PP_4146, yejA, PP_4148, PP_4149, yejF |
| ppu02010-C55 | PP_4210-PP_4210 | 1 | metal/cobalamin/siderophore | PRESENT:1 | PRESENT:1 | pvdT |
| ppu02010-C56 | PP_4216-PP_4216 | 1 | metal/cobalamin/siderophore | PRESENT:1 | PRESENT:1 | pvdE |
| ppu02010-C57 | PP_4305-PP_4305 | 1 | sulfur/sulfonate/taurine | PRESENT:1 | PRESENT:1 | sbp-I |
| ppu02010-C58 | PP_4324-PP_4327 | 4 | metal/cobalamin/siderophore | PRESENT:4 | PRESENT:4 | ccmD, ccmC, ccmB, ccmA |
| ppu02010-C59 | PP_4483-PP_4486 | 4 | methionine/amino acid/polyamine | PRESENT:4 | PRESENT:4 | hisP, hisM, hisQ, argT |
| ppu02010-C60 | PP_4542-PP_4542 | 1 | general ABC | PRESENT:1 | PRESENT:1 | PP_4542 |
| ppu02010-C61 | PP_4841-PP_4845 | 5 | general ABC | PRESENT:5 | PRESENT:5 | urtA, urtB, urtC, urtD, urtE |
| ppu02010-C62 | PP_4863-PP_4867 | 5 | methionine/amino acid/polyamine | PRESENT:5 | PRESENT:5 | livF-II, braF, braE, braD, PP_4867 |
| ppu02010-C63 | PP_4881-PP_4882 | 2 | metal/cobalamin/siderophore | PRESENT:2 | PRESENT:2 | PP_4881, PP_4882 |
| ppu02010-C64 | PP_4927-PP_4927 | 1 | lipid/lps/lipoprotein | PRESENT:1 | PRESENT:1 | cyaB |
| ppu02010-C65 | PP_4935-PP_4935 | 1 | lipid/lps/lipoprotein | PRESENT:1 | PRESENT:1 | msbA |
| ppu02010-C66 | PP_5109-PP_5110 | 2 | other | PRESENT:2 | PRESENT:2 | ftsX, ftsE |
| ppu02010-C67 | PP_5135-PP_5137 | 3 | general ABC | PRESENT:3 | PRESENT:3 | PP_5135, PP_5136, fbpC |
| ppu02010-C68 | PP_5157-PP_5157 | 1 | general ABC | PRESENT:1 | PRESENT:1 | PP_5157 |
| ppu02010-C69 | PP_5165-PP_5171 | 5 | sulfur/sulfonate/taurine | PRESENT:5 | PRESENT:5 | plpB, cysA, cysW, cysU, sbp-II |
| ppu02010-C70 | PP_5177-PP_5181 | 5 | methionine/amino acid/polyamine | PRESENT:5 | PRESENT:5 | spuH, spuG, spuF, spuE, spuD |
| ppu02010-C71 | PP_5195-PP_5196 | 2 | metal/cobalamin/siderophore | PRESENT:2 | PRESENT:2 | PP_5195, fbpA |
| ppu02010-C72 | PP_5283-PP_5283 | 1 | methionine/amino acid/polyamine | PRESENT:1 | PRESENT:1 | dppA-IV |
| ppu02010-C73 | PP_5326-PP_5329 | 4 | phosphate/phosphonate/glycerol-phosphate | PRESENT:4 | PRESENT:4 | pstB2, PP_5327, PP_5328, PP_5329 |
| ppu02010-C74 | PP_5341-PP_5341 | 1 | methionine/amino acid/polyamine | PRESENT:1 | PRESENT:1 | potF-IV |
