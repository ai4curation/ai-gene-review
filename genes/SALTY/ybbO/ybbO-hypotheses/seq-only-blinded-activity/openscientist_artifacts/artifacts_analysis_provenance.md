# Computed-analysis provenance (Iteration 1)

## Identity of the blinded sequence
- Query: 256 aa, blinded.
- UniProt CRC64 checksum (Jones/UniProt algorithm): `22B5C5A48E6D813A`
- UniParc exact match: `UPI000005A1DF` (256 aa, 1 result).
- UniProtKB cross-reference (taxon 99287, S. Typhimurium LT2): **Q7CR11, gene `ybbO`, "Oxidoreductase"**.
- Current UniProt GO for Q7CR11: only GO:0016491 (oxidoreductase activity, IBA). Seed term GO:0008106 is NOT yet on the Salmonella entry (consistent with blinded/proposed curation).

## Orthology (transfer of E. coli biochemistry)
- Reviewed ortholog: **P0AFP4 YBBO_ECOLI** (269 aa, Swiss-Prot).
- Ungapped identity query vs P0AFP4 = **90.6% over 256 aa** (best offset +13; E. coli has a 13-residue N-terminal extension).
- E. coli GO annotations: **GO:0008106 alcohol dehydrogenase (NADP+) activity — evidence IDA:EcoCyc (direct assay)**; GO:0016491 (IBA).
- Cofactor/catalytic region conserved: query `LITGCSSGIGL...LAGCRKPDD` vs E. coli `LITGCSSGIGL...LAGCRKPDD`.

## SDR catalytic/cofactor motifs in the query (1-indexed)
- Rossmann glycine-rich cofactor loop: `TGCSSGIG` (pos 8–15; TGxxxGxG).
- NADP 2'-phosphate determinant: basic pair **R34/K35** within `CRKPDD` (matches Tanaka 1996 PMID 8805511 rule for NADPH-SDRs).
- Catalytic tetrad (classical SDR N-S-Y-K): **Asn81** (NNAG), **Ser132/133** (TSS), **Tyr146 / Lys150** (YxxxK motif `YAASK`). All present -> machinery intact.

## QuickGO annotation provenance (Iteration 2)
- P0AFP4 (E. coli YbbO): **GO:0008106 IDA (ECO:0000314), references PMID:25108218 and PMID:27134112**; plus GO:0016491 IBA.
- Q7CR11 (Salmonella YbbO): **only GO:0016491 IBA** (GO_REF:0000033, PANTHER PTN000672121) — seed term GO:0008106 not yet propagated.

## InterPro family provenance (Iteration 2) for Q7CR11
- Pfam **PF00106** (short chain dehydrogenase); InterPro **IPR002347** (SDR family) + IPR020904 (conserved site); PROSITE **PS00061**; PANTHER **PTHR43313**; NCBIfam NF005950; Rossmann superfamily SSF51735 / G3DSA:3.40.50.720.
- CDD **cd05374** "17beta hydroxysteroid dehydrogenase-like, classical (c) SDRs" = broad classical-SDR cluster label (likely origin of the HSD competing hypothesis), NOT evidence of steroid substrate.

## Interpretation
Direct-assay biochemistry of the 91%-identical E. coli ortholog (NADP+-dependent aldehyde reductase, aliphatic C6–C18, optimal C16/C18) transfers to the Salmonella query. Motif-only cofactor inference was ambiguous (both basic R/K pair and downstream Asp present); the direct NADP+ assay resolves it in favor of NADPH. Retinal->retinol is a documented promiscuous side activity, not the native substrate.
