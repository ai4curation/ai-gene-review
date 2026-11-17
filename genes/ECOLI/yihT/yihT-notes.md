# yihT (P32141) notes

## Session 2026-11-10

Deep research via `just deep-research` failed in this environment (deep-research-client
dependency unresolvable offline); review built from UniProt and cached literature:
PMID:24463506 (abstract), PMID:33791429 (full text), PMID:37838169 (full text, fetched
this session), PMID:41676062 (review).

- SFP aldolase is one of the four sulfo-EMP reactions shown with purified enzymes
  [PMID:24463506].
- Denger et al. detected DHAP and SLA in a coupled YihS/YihV/YihT system
  [PMID:33791429 "Schleheck and co-workers detected the formation of DHAP and SLA in a
  coupled system containing SQ and recombinantly produced YihS, YihV, and YihT"].
- Caveat: Sharma et al. could not detect activity of recombinant E. coli YihT on
  synthetic SFP and characterised the Salmonella ortholog (87% similar) instead
  [PMID:33791429 "we could not detect the formation of DHAP or SLA under a range of
  conditions"]. Activity of E. coli YihT therefore rests on the Denger coupled assay
  plus orthology; I do not treat the negative as evidence against function (likely an
  expression/handling issue; E. coli yihT deletion abolishes growth on SQ, UniProt
  DISRUPTION PHENOTYPE, PubMed:24463506).
- Class I (Schiff base, Lys193 in SeYihT) aldolase; homotetramer by SEC-MALS; inactive
  on FBP [PMID:33791429; PMID:37838169].

Decisions: GO:0061595 x3 ACCEPT; lyase activity MODIFY -> GO:0061595; GO:1902777 x3
MODIFY -> GO:0061722 sulphoglycolysis (same treatment as yihS, yihV).
