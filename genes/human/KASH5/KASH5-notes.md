# KASH5 (CCDC155) review notes

## 2026-09-27 — initial review (claude-code)

Sources: UniProt Q8N6L0, GOA (177 rows; 147 are GO:0005515 protein binding), cached publications.
Falcon deep research not yet available at the time of review (see end of file for status).

### Identity and architecture
- Tail-anchored ONM protein, 562 aa; TM 522-542, perinuclear KASH peptide 543-562 [file:human/KASH5/KASH5-uniprot.txt "Single-pass type IV"].
- N-terminal EF-hand pair (Pfam EF-hand_9), central coiled coil (164-349), C-terminal KASH peptide.
- KASH peptide is divergent but acts as a canonical KASH domain [PMID:22826121 "acts as a canonical KASH domain"]; carries a 545-PPP-547 motif used at the SUN1-KASH5 6:6 interface [PMID:33393904 "The KASH domains of Nesprin-4 and KASH5 exhibit sequence divergence from Nesprins 1–3"].
- Behaves as authentic KASH protein: NE targeting SUN1/2-dependent, KASH domain sufficient, displaces NESP2 [PMID:24062341 "Together these data demonstrate that KASH5 behaves as an authentic KASH protein."].

### LINC partners
- SUN1 (major; SUN1 KO abolishes KASH5 telomere localization) [PMID:22826121 "KASH5 is localized to the NE near telomeres through the direct interaction with SUN1 in early meiosis"].
- SUN1-KASH5 crystal structure; 6:6 complexes [PMID:33393904 "SUN1-KASH4, SUN1-KASH5, and SUN1-KASH1 form 6:6 complexes in solution"]. SUN2-KASH5 structure [PMID:33058875]; SUN2-KASH5 less stable in solution than SUN1-KASH5 (PMID:33393904).
- ComplexPortal CPX-2537 (SUN1-KASH5) and CPX-7666 (SUN2-KASH5).

### Dynein activating adaptor
- Recruits dynein IC and p150Glued to NE; co-IPs DHC, IC, p150, LIS1 [PMID:24062341 "These data imply that KASH5 is an adaptor for cytoplasmic dynein."].
- In vitro: converts dynein-dynactin into processive complex [PMID:35703493 "KASH5 is a bona fide activating adaptor that converts dynein and dynactin into a processive complex"]; EF-hand pair binds LIC helix 1; homodimer.
- Independent confirmation; LIC1/2 binding; LIS1 required for dynactin incorporation; dynein recruitment can be dynactin-independent [PMID:36946995 "Here, we show that KASH5 is a transmembrane activating adaptor for dynein"].
- => Proposed NEW GO:0140660 cytoskeletal motor activator activity (IDA, PMID:35703493). Comparator note: GO:0140660 is barely used in human GOA (1 NAS); BICD2 carries dynein complex binding only. Kept NEW because the in vitro motility data directly meet the definition; GO:0070840 retained as ACCEPT.

### Process
- Kash5-/- mice: infertile both sexes, prophase I arrest, pairing fails although telomeres still attach to NE; no clustering of SUN1 foci; no dynein at telomere attachment sites [PMID:24062341].
- Human: L197P (coiled coil) blocks NE distribution and SUN1 NE enrichment; NOA + POI [PMID:35587281, abstract only].
- Oocyte post-prophase: knockdown -> GV arrest, small spindles, low F-actin mesh; KASH5 at MII spindle poles [PMID:26842404]. Single knockdown study; used to judge spindle/actin IBA/IEA rows (non-core / over-annotated).

### Decisions summary
- Protein binding: 3 SUN1/SUN2 structural rows -> MODIFY to GO:0140444 (consistent with SUN1/SUN2/SYNE1/SYNE2 reviews); 144 HT Y2H rows -> REMOVE (uninformative; predominantly TM/ER-Golgi partners typical of tail-anchor Y2H artefacts).
- Chromosome-side CCs (telomeric region, lateral element) -> MARK_AS_OVER_ANNOTATED: KASH5 is in the ONM, contacting telomeres only indirectly via SUN1/SUN2.
- GO:0034993 is the right complex term for KASH5 (meiosis-specific).

### Deep research (Falcon) — incorporated after arrival
- Report arrived during review; consistent with the literature-based conclusions above: ONM tail-anchored KASH protein, SUN1 principal partner with SUN2 partially redundant, first transmembrane dynein activating adaptor, EF-hands bind LIC helix 1 without detectable Ca2+ binding [file:human/KASH5/KASH5-deep-research-falcon.md "It is therefore regarded as the first established transmembrane dynein-activating adaptor"].
- DR-reported, not verified against cached papers (not used as annotation evidence): L535Q TM variant mistargets KASH5 to mitochondria (Bentebbal et al. 2021); p.Arg424Thrfs*20 family with NOA + diminished ovarian reserve/recurrent miscarriage (Hou 2023, PMID:36864840 per UniProt); possible link to recurrent androgenetic hydatidiform mole (Rezaei 2024, PMID:39545410).
- DR cites Garner et al. with a bioRxiv DOI; the published JCB paper is PMID:36946995 (cached).
