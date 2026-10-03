# MKK4 (At1g51660, O80397) – curation notes

## Identity
- Arabidopsis MAP kinase kinase 4; group C plant MAP2K, closest paralog MKK5. Not MPK4, not MAPKKK4/YODA.
- UniProt: EC 2.7.12.2; activation-loop Thr-224/Ser-230 phosphorylated by MAPKKK5. [PMID:27679653 "Therefore, we substituted the S/TxxxxxS/T motif residues, T‐224/S‐230 of MKK4 and T‐215/S‐221 of MKK5 with alanine."]

## Core biochemistry
- MAP2K tier of MAP3K -> MKK4/MKK5 -> MPK3/MPK6. [PMID:11875555 "Here we identify a complete plant MAP kinase cascade (MEKK1, MKK4/MKK5 and MPK3/MPK6) and WRKY22/WRKY29 transcription factors that function downstream of the flagellin receptor FLS2"]
- Redundant with MKK5. [PMID:27679653 "MKK4 and MKK5 redundantly function as MAPKKs for MPK3 and MPK6"]
- Activated by MAPKKK5 (chitin). [PMID:27679653 "MAPKKK5 interacts with MKK4 and MKK5 in vivo and phosphorylates their activation loops"]; [PMID:27679653 "a possible phospho‐signaling pathway consisting of CERK1–PBL27–MAPKKK5–MKK4/MKK5–MPK3/MPK6"]
- MKK4DD specifically activates MPK3/MPK6. [PMID:18378893 "The absence of activation of other MAPKs in GVG-NtMEK2 DD , GVG-MKK4 DD , and GVG-MKK5 DD plants supports this notion"]
- Immunity vs development MAP3Ks. [PMID:35652263 "MAPKKK3/MAPKKK5 function upstream of MKK4/MKK5‐MPK3/MPK6 in plant immunity"]; [PMID:17259259 "MKK4/MKK5-MPK3/MPK6 module is downstream of YODA"]

## Outputs (pleiotropic; downstream of MPK3/MPK6) – non-core
- Pathogen resistance [PMID:11875555 "Activation of this MAPK cascade confers resistance to both bacterial and fungal pathogens"]
- Camalexin: gain-of-function only [PMID:18378893 "DEX treatment of GVG-MKK4 DD or GVG-MKK5 DD Arabidopsis plants also led to camalexin induction"]. No MKK4-specific loss-of-function camalexin data -> no camalexin term (consistent with MKK5); raised as question.
- Stomatal patterning [PMID:17259259], inflorescence [PMID:23263767], abscission [PMID:18809915; PMID:25730871].
- Wound ethylene (Li et al. 2018, from deep research; not cached): mkk4 knockdown ~10%, mkk5 >50%, double >80% reduction.

## Localization
- Cytosol (BiFC with MAPKKK5) [PMID:27679653 "MAPKKK5 interacts with MKK2, MKK4, and MKK5 mainly in the cytosol"].
- Chloroplast: in vitro import only [PMID:19516975 "In vitro uptake experiments confirm the predicted import of an oxidant-responsive MAPKK, AtMKK4, into the chloroplast"]; authors call it "primarily cytosolic". Kept non-core.

## Problem annotation
- Pollen-pistil interaction IGI (PMID:32890733, abstract-only): abstract names MKK1/2/3/7/9 + MPK3/MPK4. WITH list = MKK1, MKK2, MKK7, MKK9, MPK3, AT1G51660 (MKK4) and no MKK3 (AT5G40440) -> possible MKK3/MKK4 identifier swap. UNDECIDED, raised as question.
- IDA MAPKK activity / IC MAPK cascade from PMID:9878570 (abstract about MKK2/MEK1); full text not available, function independently correct -> ACCEPT, defer to curator.

## Decisions (consistent with MKK5)
- 13 protein binding rows REMOVE; protein serine kinase activity (Rhea) MODIFY -> GO:0004708; no NEW (no cell surface PRR signaling term; question raised).
