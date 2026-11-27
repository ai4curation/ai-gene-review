# UBE2F (Q969M7) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: canonical human UBE2F, UniProt Q969M7 (185 aa, Swiss-Prot). The sibling folder
`genes/human/UBE2F/` is keyed to the 101-residue TrEMBL fragment F8WDQ9 from the
ProtNLM2 benchmark; this folder reviews the canonical product under the GENE__ACC
convention. No ProtNLM2 file or prediction-evidence folder was opened or used.

### Deep research

`just deep-research-falcon human UBE2F__Q969M7 --fallback perplexity-lite` failed:
falcon returned `403 Forbidden` on `https://api.platform.edisonscientific.com/auth/login`
(authentication failure), and the perplexity-lite fallback timed out after 600 s. No
deep-research file was produced. The review is based on primary literature cached in
`publications/` (most with full text) and the UniProt record.

### Evolutionary grounding

See `UBE2F__Q969M7-bioinformatics/RESULTS.md` (script `panther_placement.py`).

- Live PANTHER places human and mouse UBE2F in PTHR24068:SF129 "NEDD8-CONJUGATING
  ENZYME UBE2F"; UBE2M and yeast UBC12 sit in SF132 "NEDD8-CONJUGATING ENZYME UBC12".
  Different subfamilies, so UBE2M-specific features (RBX1 pairing, CUL1-4 neddylation,
  UBE2M's dual ubiquitin-E2 activity) are not transferred.
- PAINT node PTN000630367 is seeded by UBE2M orthologs and by UBE2F itself, so it sits
  above both subfamilies: NEDD8 transferase activity and protein neddylation are ancestral
  to the NEDD8-E2 clade. PAINT curators deliberately placed NOT (IRD) ubiquitin
  conjugating enzyme activity and NOT protein polyubiquitination on the same node. I do
  not propose any ubiquitin-E2 term for UBE2F.
- Cys116 (active site) and N-terminal Met1 (acetylated) are present in the sequence.

### Literature summary

- Huang et al. 2009 [PMID:19250909 "the previously uncharacterized E2 UBE2F is a
  NEDD8-conjugating enzyme in vitro and in vivo"; "UBE2M/RBX1 and UBE2F/RBX2 displaying
  different target cullin specificities"]. Abstract only in cache. UniProt curated
  statement: "Together with the E3 ubiquitin ligase RNF7/RBX2, specifically neddylates
  cullin-5 (CUL5)" and "Does not neddylate CUL1, CUL2, CUL3, CUL4A or CUL4B".
- Monda et al. 2013 [PMID:23201271]: DCNL co-E3s recognise the N-acetylated N-terminus
  of UBC12 and UBE2F; "the PONY domains from all 5 DCNL family members potently
  stimulated NEDD8 transfer from UBE2FNAc to RBX2-associated CUL5CTD". DCNL3 shows the
  strongest preference for UBE2F.
- Stanley et al. 2012 [PMID:23300442 "conjugation of NEDD8 to Cullin-5 by the
  NEDD8-conjugating enzyme UBE2F is required for HIV Vif-mediated degradation of the host
  restriction factor APOBEC3G"]; UBE2F knockdown, not UBE2M knockdown, reduces CUL5
  neddylation in HEK293T cells; in vitro "CUL5 is completely NEDD8ylated by UBE2F".
- Zhou et al. 2017 [PMID:27591266 "By promoting CUL5 neddylation, UBE2F/SAG/CUL5
  tri-complex activates CRL5 (Cullin-RING-ligase-5) to ubiquitylate NOXA via a novel
  K11, but not K48, linkage"]. SAG = RBX2/RNF7. Downstream NOXA degradation and lung
  cancer cell survival are CRL5 outcomes, not UBE2F activities.
- Zhou et al. 2018 [PMID:29932898]: UBE2M acts as a ubiquitin E2 to target UBE2F for
  degradation, so UBE2F levels are regulated by the parallel UBE2M cascade.
- Lumpkin et al. 2021 [PMID:33268465]: CUL5 neddylation "sequesters the NEDD8 E2
  (UBE2F) binding site on RBX2".
- Horn-Ghetko et al. 2024 [PMID:38605244 "CUL9 as unique among RBX1-bound cullins in
  dependence on the metazoan-specific UBE2F neddylation enzyme"]. Extends UBE2F's
  substrate range to CUL9-RBX1.
- Zhang et al. 2025 [PMID:39762645 "UBE2F cooperates with E3 ligase SAG in neddylation of
  RHEB at K169"]. A non-cullin substrate; single lab, not yet independently confirmed.

### Annotation decisions (summary)

- NEDD8 conjugating enzyme activity (GO:0061654): ACCEPT all rows; core MF.
- NEDD8 transferase activity (GO:0019788): MODIFY to GO:0061654, which the gene already
  carries (is_a child, verified via OLS ancestors).
- Protein neddylation (GO:0045116): ACCEPT; core BP. UBE2F catalyses the conjugation
  step, so it is a direct participant.
- Post-translational protein modification (GO:0043687): MODIFY to protein neddylation.
- Cytosol: ACCEPT (IBA and Reactome TAS); a soluble cascade enzyme.
- Protein binding rows: RBX2 and DCNL2/3 rows MODIFY to ubiquitin-like protein ligase
  binding (GO:0044389), since these are the NEDD8 E3/co-E3 partners of the cascade. UBA3
  (E1) row and high-throughput rows (GNB2, PAX6, LCN2) REMOVE as uninformative.
- No NEW process terms. HIV Vif-mediated APOBEC3G degradation and NOXA turnover are
  downstream outcomes of CRL5 activity; UBE2F's work is the neddylation step.
