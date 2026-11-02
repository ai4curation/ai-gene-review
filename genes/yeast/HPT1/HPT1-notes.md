# HPT1 (YDR399W, UniProt Q04178) notes

## Function
- HGPRT EC 2.4.2.8, hypoxanthine -> IMP and guanine -> GMP [UniProt:Q04178].
- "The enzyme recognized hypoxanthine and guanine, but not adenine or xanthine, as substrates." [PMID:6170313]
- "guanine is highly preferred over hypoxanthine as substrate in the forward reaction" (ordered bi-bi) [PMID:7035445]; Km hypoxanthine 23, guanine 18, PRPP 50 microM [PMID:371963].
- bra6 = HPT1: "BRA6 and BRA1 are new genes encoding, respectively, hypoxanthine guanine phosphoribosyl transferase and adenylosuccinate lyase." [PMID:9335580]
- GMP salvage in vivo: guanine fails to rescue "gua1-G388D Δhpt1 mutants unable to refill the internal GMP pool through the salvage pathway" [PMID:20980241].
- Feedback inhibition by GMP; deregulated mutants accumulate toxic guanylates [PMID:18245832].

## Pathway / YeastCyc / IBA
- GUANPRIBOSYLTRAN-RXN and HYPOXANPRIBOSYLTRAN-RXN in PWY3O-1/285; HYPOXAN in PWY3O-2220; GUAN in PWY3O-743. YeastPathways->GO conversion uses GO:0004422 for the guanine reaction too (GO-CAM PWY3O-743 should use GO:0052657).
- IBA PTN001262736 gave HPT1 "XMP salvage" seeded only by XPT1 -> REMOVE (Hpt1 does not use xanthine [PMID:6170313]; xpt1 disruption leaves HPRT unaffected [PMID:10217799]).

## Decisions
- Core MF GO:0004422 (IMP salvage) and GO:0052657 (GMP salvage); cytoplasm.
