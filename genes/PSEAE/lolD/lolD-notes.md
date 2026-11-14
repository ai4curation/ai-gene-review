# lolD (PA2987, Q9HZL7) notes

ATPase subunit of the LolCDE lipoprotein-release complex (operon PA2988 permease, PA2987 lolD, PA2986 permease). No deep-research provider was available; literature search by hand (PMID:17350955 abstract; QuickGO for E. coli LolD P75957; UniProt for PTN000655654 seeds).

## Literature

- Tanaka, Narita & Tokuda 2007 (PMID:17350955; abstract only): purified P. aeruginosa LolCDE reconstituted into proteoliposomes released lipoproteins with ATP and LolA ["When incubated in the presence of ATP and a LolA homologue, the reconstituted LolCDE homologue released lipoproteins, leading to the formation of a LolA-lipoprotein complex."]; LolB then put them in the outer membrane ["Lipoproteins were then incorporated into the outer membrane depending on a LolB homologue."]; Lys3-Ser4 lipoproteins stay in the inner membrane.
- QuickGO (2026-11-05), E. coli LolD P75957: GO:0044874 IDA (PMID:17509078, ComplexPortal), IMP (PMID:10783239, CACAO); GO:0089705 IDA (PMID:10783239); GO:0140306 lipoprotein releasing activity IDA/IMP; GO:0043190 IPI.
- GO:0140306 is_a GO:0140318 protein transporter activity / GO:0005215 transporter activity, not GO:0022857 transmembrane transporter activity (OAK, go.db). GO:0089705 is not an ancestor of GO:0044874.

## Review decisions

- ACCEPT: ATP binding, ATP hydrolysis, plasma membrane IBA/IEA, GO:0044874 x3, GO:0089705 x3.
- GO:0016020: MODIFY to GO:0005886. GO:0044873: TOO_GENERAL.
- GO:0022857 IBA (PTN000655654, sole source M. tuberculosis Rv2688c): MODIFY to GO:0140306; LolCDE releases lipoproteins to LolA rather than moving them across a membrane.
- GO:0055085 IBA (PTN000655654): MARK_AS_OVER_ANNOTATED, same reasoning. PTN000655654 is a deep ABC node not seeded by PseudoCAP, so no defect is recorded here; it would be a GO_CENTRAL question if that node is reviewed.
- NEW: GO:0140306 lipoprotein releasing activity (IDA) and GO:0043190 ABC transporter complex (IDA), as in the PA2988 review.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000656700 | GO:0044874 lipoprotein localization to outer membrane (also GO:0089705 protein localization to outer membrane) | 2 | 15 (12 taxa) | GO:0044874 and GO:0089705, IDA, PMID:17350955 (PseudoCAP) | SOUND | Abstract states purified P. aeruginosa LolCDE releases lipoproteins to LolA (ATP-dependent) and LolB inserts them into the outer membrane: direct biochemistry on the complex containing LolD. Node term suits a LolD clade. | E. coli LolD P75957 (IDA PMID:17509078; IMP/IDA PMID:10783239) | Yes, on E. coli LolD |

PTN000656700 is the LolD node and is distinct from the LolC/LolE permease node PTN002524722, whose node-level record is on genes/PSEAE/PA2988 (PA2986 cross-references it); both are SOUND on the same paper. No PSEUDOCAP or GO_CENTRAL defect.
