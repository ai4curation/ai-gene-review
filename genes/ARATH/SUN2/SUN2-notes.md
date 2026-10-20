# ARATH SUN2 review notes

## 2026-09-27 (claude-code)

Sources: UniProt Q9FF75/Q9SG79 entries, GOA-cited publications in `publications/`. Full text cached for
PMID:22270916, PMID:24667841, PMID:24891605, PMID:25330379, PMID:25759303; abstract-only for PMID:19807882,
PMID:21294795, PMID:25217773, PMID:25412930, PMID:27630107, PMID:23973298, PMID:15469496. Falcon deep research
not available at time of review.

Key findings
- Cter-SUN, type II INM protein; coiled coil drives homo/heteromers with its paralog
  [PMID:19807882 "AtSUN1 and AtSUN2 are present as homomers and heteromers in vivo, and that the coiled-coil domains are required for this"].
- SUN domain binds plant KASH proteins WIP1-3 [PMID:22270916 "Here, we show that AtWIP1, AtWIP2, and AtWIP3 interact with AtSUN1 and AtSUN2 at the NE"],
  SINE1-4 via conserved KASH pocket [PMID:24891605 "confirming that the KASH-binding pocket within the SUN domain is required for interaction"], and TIK (PMID:25217773).
- SUN required for WIP1/RanGAP1 NE retention [PMID:22270916 "The interaction is required for both AtWIP1 and AtRanGAP1 NE localization"].
- Nuclear shape: SUN-WIP-WIT2-myosin XI-i bridge [PMID:25759303 "supporting the existence of LINC complexes comprised of SUN, WIP, WIT2 and myosin XI-i"];
  SUN1 predominant [PMID:25759303 "Compared with SUN2, SUN1 plays a predominant role in nuclear shape"].
- Nuclear POSITION is not affected in sun1-KO sun2-KD [PMID:22270916 "the nuclear position in root hairs and trichomes is not affected in sun1-KO sun2-KD"]
  -> no nuclear migration annotation proposed; relevant to the nucleokinesis module (plant nuclear movement is actomyosin/WIT/myosin XI-i driven).
- Meiosis: NE in prophase I; double mutant synapsis/chiasma defects [PMID:25412930 "overlapping functions of SUN1 and SUN2 ensure normal meiotic recombination and synapsis"].
- SUN recruits CRWN1/LINC1 on overexpression (PMID:24667841) but SUN and CRWN1 act independently on nuclear shape in planta (PMID:25759303).

Decisions
- Protein binding: KASH partners (WIP/SINE/TIK) -> MODIFY to GO:0140444 (consistent with human SUN1/SUN2 reviews);
  SUN-SUN, SUN3/4, CRWN1, NEAP1 -> REMOVE (uninformative; oligomerization / NE localization captured elsewhere).
- ER / ER membrane / phragmoplast -> KEEP_AS_NON_CORE (mitotic/transit locations).
- GO:2000769 (SUN1 only) -> MODIFY to GO:0006997: the paper measures nuclear, not cell, shape/polarity.
- Spindle HDA (SUN2 only) -> UNDECIDED (abstract-only GFP survey).
- Complex: GO:0106094 is microtubule-specific; plant bridge is actin/myosin XI-i-linked, so core function uses GO:0106083.

## 2026-09-27 update: Falcon deep research incorporated

- Deep research surfaced Cromer et al. 2024 (PMID:39013853, PubMed-verified via DOI; full text cached).
  [PMID:39013853 "we observed that telomere association with the NE is rare in sun1 sun2, even if not wholly absent"];
  rapid prophase chromosome movements abolished in sun1 sun2. Strengthens the GO:0070197 IMP/IEA rows and meiotic core function.
- Deep research also notes OPENER recruitment by SUN1/2 and CDC48/PUX-regulated SUN1 turnover (not added; not GOA-cited, not verified here).

## 2026-10-15 journal: spindle row resolved (PR #5026 follow-up)

Supersedes the "Spindle HDA (SUN2 only) -> UNDECIDED" line above.

- GO:0005819 spindle HDA (PMID:15469496, Van Damme et al. 2004 BY-2 GFP survey) is KEEP_AS_NON_CORE: a transient mitotic location of the SUN2 fusion, consistent with NE/ER membranes surrounding the spindle during open mitosis (Oda & Fukuda 2011), handled like the phragmoplast (GO:0009524) rows. No role in spindle microtubule function is implied.
- Query (re-run 2026-10-15): QuickGO REST, `https://www.ebi.ac.uk/QuickGO/services/annotation/search?reference=PMID:15469496&limit=200` returned 136 annotations on 54 UniProtKB entries, all HDA located_in, all assigned by TAIR. SUN2 (Q9SG79): GO:0005635 nuclear envelope, GO:0005819 spindle, GO:0009524 phragmoplast. SUN1 (Q9FF75): GO:0005635 only. 16 entries carry GO:0005819.
- Full text: `fetch-pmid PMID:15469496 --force` on 2026-10-15 cached abstract only (no PMC record); Europe PMC lists no PMCID and isOpenAccess N. The survey's images were not inspected.
