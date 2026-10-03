# MKK5 (At3g21220, Q8RXG3) – curation notes

## Identity
- Arabidopsis MAP kinase kinase 5 (MEK5, AtMAP2Kalpha); group C plant MAP2K, closest paralog MKK4.
  Not to be confused with MAPKKK5 (the upstream MAP3K).
- UniProt: EC 2.7.12.2 (dual-specificity MAPKK); activation-loop Thr-215/Ser-221 phosphorylated by MAP3Ks.

## Core biochemistry
- MAP2K tier of MAP3K -> MKK4/MKK5 -> MPK3/MPK6 relays. [PMID:11875555 "Here we identify a complete plant MAP kinase cascade (MEKK1, MKK4/MKK5 and MPK3/MPK6) and WRKY22/WRKY29 transcription factors that function downstream of the flagellin receptor FLS2"]
- Activated by MAPKKK5 on the activation loop. [PMID:27679653 "The kinase domain of MAPKKK5 directly phosphorylated MKK4K108R and MKK5K99R (Fig 8B)."] and [PMID:27679653 "MAPKKK5 interacts with MKK4 and MKK5 in vivo and phosphorylates their activation loops"]
- MKK4 and MKK5 are redundant. [PMID:27679653 "MKK4 and MKK5 redundantly function as MAPKKs for MPK3 and MPK6"]
- MKK5DD activates MPK3/MPK6 in vitro (used routinely as the activating kinase): [PMID:25843888 "BASL was phosphorylated by constitutively active MKK5 (MKK5DD)-activated MPK3 and 6"]
- Gain-of-function MEK5DD activates endogenous MPK3/MPK6. [PMID:18268539 "the activation of AtMEK5, a MAPK kinase, can in turn activate endogenous AtMAPK3 and AtMAPK6"]

## Upstream MAP3Ks by context
- Immunity: MAPKKK3/MAPKKK5. [PMID:35652263 "MAPKKK3/MAPKKK5 function upstream of MKK4/MKK5‐MPK3/MPK6 in plant immunity"]
- Chitin: CERK1-PBL27-MAPKKK5-MKK4/MKK5-MPK3/MPK6. [PMID:27679653 "a possible phospho‐signaling pathway consisting of CERK1–PBL27–MAPKKK5–MKK4/MKK5–MPK3/MPK6"]
- Development: YODA. [PMID:23263767 "the YDA-MKK4/MKK5-MPK3/MPK6 cascade functions downstream of the ER receptor in regulating localized cell proliferation"]; [PMID:17259259 "MKK4/MKK5-MPK3/MPK6 module is downstream of YODA"]
- ABA: AIK1/MAPKKK20. [PMID:27913741 "AIK1 was localized in the cytoplasm and shown to activate MKK5 by protein phosphorylation"]

## Outputs (pleiotropic; downstream of MPK3/MPK6)
- PAMP resistance [PMID:11875555 "Activation of this MAPK cascade confers resistance to both bacterial and fungal pathogens"]
- Camalexin induction by MKK5DD (gain of function only) [PMID:18378893 "DEX treatment of GVG-MKK4 DD or GVG-MKK5 DD Arabidopsis plants also led to camalexin induction"]. Consistent with MPK3 review, this is a positive regulation (signalling) role, not biosynthesis.
- Ethylene production and HR-like cell death (gain of function) [PMID:18268539].
- Stomatal patterning [PMID:17259259], inflorescence architecture [PMID:23263767], floral abscission [PMID:18809915; PMID:25730871], ABA responses in root/guard cells [PMID:27913741].

## Localization
- Cytoplasm: BiFC with MAPKKK5 [PMID:27679653 "MAPKKK5 interacts with MKK2, MKK4, and MKK5 mainly in the cytosol"].
- Stress granule proteome (Kosmacz 2019) – abstract only; minor stress-induced pool.
- Mitochondrion ISM (AtSubP) – no supporting evidence; removed.

## Decisions
- Protein binding (9 IPI rows) removed, consistent with MPK3/MPK6/MAPKKK5 reviews.
- protein serine kinase activity (GO:0106310) rows: the demonstrated activity is dual Thr/Tyr phosphorylation of the MPK3/MPK6 TEY loop; Ser label is an EC 2.7.12.2 -> Rhea expansion. MODIFY -> GO:0004708 MAP kinase kinase activity.
- Tyrosine kinase rows accepted (TEY Tyr phosphorylation is real).
- NEW: GO:0002752 cell surface PRR signaling pathway (participation: MKK5 performs the MAP2K phosphorylation step; comparator: MAPKKK5 review carries the same term in the same pathway).
- Developmental / hormone / defense processes: KEEP_AS_NON_CORE (consistent with MPK3/MPK6).

## Deep research
- genes/ARATH/MKK5/MKK5-deep-research-falcon.md used as retrieval aid; primary claims checked against cached papers.
