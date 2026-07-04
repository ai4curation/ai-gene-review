# glh-2 (Germline helicase 2) — research notes

UniProt: Q966L9 (GLH2_CAEEL). WormBase: WBGene00001599 / C55B7.1. NCBI taxon 6239.
Family: DEAD-box helicase, DDX4/VASA subfamily. 974 aa, EC 3.6.4.13.
Human ortholog: DDX4 (VASA). Part of the CAEEL_P_GRANULES flagship project; glh-1 and glh-4
are already reviewed, glh-2 is the last GLH paralog.

## Protein architecture (from UniProt Q966L9)
- Central DEAD-box helicase core: Helicase ATP-binding domain (583-767), Helicase C-terminal
  domain (803-950). Q motif (552-580), DEAD box motif (710-713), ATP-binding P-loop (596-603).
- SIX CCHC-type zinc fingers (257-274, 282-299, 371-388, 396-413, 453-470, 473-490) — this
  distinguishes GLH-2 from GLH-1 (which has four). CCHC fingers are of the retroviral
  nucleocapsid RNA-binding type.
- Large N-terminal intrinsically disordered region (212-435 disordered) rich in Gly and
  FG/FGG-like Gly-Phe repeats (glycine-rich compositional bias). These FGG repeats in GLH
  proteins mediate perinuclear anchoring via FG-nucleoporins (established for GLH-1/GLH-4).
- PE 1: Evidence at protein level.

## KNOWN (glh-2-specific evidence)

### Molecular function / structure
- GLH-2 is a putative germline RNA helicase with SIX CCHC zinc fingers.
  [PMID:8943022 "The predicted GLH-1 protein has four CCHC fingers; GLH-2 has six"]
- Both GLH-1 and GLH-2 are "putative germ-line RNA helicases (GLHs) that contain CCHC zinc
  fingers of the type found in the RNA-binding nucleocapsid proteins of retroviruses."
  [PMID:8943022]
- UniProt: "Probable ATP-binding RNA helicase." Catalytic activity ATP + H2O = ADP + Pi + H+
  (RHEA:13065), EC 3.6.4.13. Belongs to DEAD box helicase family, DDX4/VASA subfamily.
- NOTE: direct in vitro RNA-unwinding / ATPase biochemistry has NOT been published for GLH-2
  specifically (nor, in fact, for GLH-1). The "RNA helicase activity" IDA (PMID:8943022) is
  sequence/domain-based, not a biochemical unwinding assay. This is a genuine MF-dark gap.

### Localization
- Constitutive P-granule component; both GLH proteins "localize in the P granules at all stage
  of germ-line development." [PMID:8943022]
- P granules are perinuclear (nuclear-pore associated) cytoplasmic RNP condensates in germ
  cells. GLH-2 is cytoplasmic in oocytes/early embryo and perinuclear in later stages
  (secondary source: Alliance/WormBase gene page, from Gruidl 1996 / Spike 2008 — not used as
  a verbatim citation because primary full text not cached).
- The IBA "nucleus" annotation: GLH proteins are predominantly perinuclear-cytoplasmic. HOWEVER
  GLH-2 has separately been reported to associate with sperm chromatin (noted in the Spike 2008
  discussion), i.e. a possible bona fide nuclear association distinct from glh-1. So unlike the
  glh-1 review (which REMOVED nucleus), for glh-2 nucleus is better kept as non-core than
  removed outright.

### Biological process / genetics
- Antisense knockdown: "Injection of antisense glh-1 or glh-2 RNA into wild-type worms causes
  some offspring to develop into sterile adults, suggesting that either or both genes are
  required for normal germ-line development." [PMID:8943022] — this is the experimental basis
  for the glh-2 IMP annotations (germ cell development, post-embryonic development). It is a
  combined glh-1/glh-2 antisense experiment, so the glh-2-specific contribution is not cleanly
  separable.
- The two glh genes "display different patterns of RNA and protein accumulation in the germ
  lines of hermaphrodites and males" and "physically map within several hundred kilobases of
  one another, it seems likely that they represent a fairly recent gene duplication event."
  [PMID:8943022] — glh-1 and glh-2 are recent paralogs.
- Deletion genetics (Spike et al. 2008, PMID:18430929, abstract cached): "Caenorhabditis
  elegans has four Vasa family members, the germline helicases GLH-1, GLH-2, GLH-3, and GLH-4."
  "Our analysis of deletion alleles of each glh gene demonstrates that GLH-1 is the key member
  of the family". "The other GLHs are not essential." "GLH-4 serves redundant roles with
  GLH-1". "GLH-1 and GLH-4 are required for proper association of the PGL family of proteins
  with P granules". => a glh-2 null (um2) is NOT sterile on its own; GLH-1 (with GLH-4
  redundancy) carries the essential germline function, not GLH-2. glh-2(um2) shows only a
  modest ~25% brood reduction at 15C (secondary WebFetch of full text; not verbatim-cited).

### Protein interactions
- "The GLH proteins belong to a family of four germline RNA helicases in Caenorhabditis
  elegans." [PMID:12435362]
- GLHs (including GLH-2) bind KGB-1, a JNK/JUN MAP kinase: "KGB-1 is a putative JNK MAP kinase
  that GLHs bind"; and CSN-5 (COP9 signalosome subunit 5) and ZYX-1 (zyxin-like). "GST
  pull-down assays independently established that these proteins bind GLHs." [PMID:12435362]
  => basis for the JUN kinase binding IPI and the generic protein binding IPI (with_from
  UniProtKB:O44408 = kgb-1). GLH-2 also self-associates in vitro (secondary source; the KGB-1
  and self-interaction are why "protein binding" and "JUN kinase binding" are annotated).
- csn-5 RNAi phenocopies glh-1;glh-4 double loss: "RNA interference (RNAi) with csn-5 results
  in sterile worms with small gonads and no oocytes, a defect essentially identical to that
  produced by RNAi with a combination of glh-1 and glh-4." "loss of either CSN-5 or KGB-1
  causes oogenesis to cease, but does not affect the initial assembly of P granules."
  [PMID:12435362] — note these fertility phenotypes are glh-1/glh-4-referenced, NOT glh-2.

## NOT known / knowledge gaps (glh-2-specific)
1. GLH-2's non-redundant molecular role vs GLH-1/GLH-4 is undefined. glh-2 single null is
   essentially fertile; whether GLH-2 has any unique substrate or step, or is purely a
   buffering paralog, is unknown. Spike 2008: "The other GLHs are not essential."
2. Direct RNA substrates of GLH-2 are unknown. No CLIP/biochemical target identification; the
   six CCHC fingers predict RNA binding but bound RNAs are uncharacterized.
3. Whether GLH-2 has catalytically active (ATP-dependent unwinding) helicase activity, and
   whether that activity is required in vivo, is untested. No in vitro helicase/ATPase assay
   and no catalytic-dead (DQAD/DEAD-motif) allele analysis has been reported for GLH-2 (unlike
   GLH-1, where ATPase-cycle mutants were made).
4. Mechanistic contribution of GLH-2 to P-granule assembly/organization is unresolved. The
   epistasis placing GLHs upstream of PGL proteins was established with GLH-1/GLH-4; GLH-2's
   role in condensate assembly per se is unmeasured.
5. The functional meaning of GLH-2's reported sperm-chromatin association (possible nuclear
   role) is unknown.

## Annotation-by-annotation plan (23 GOA rows)
- MF RNA helicase activity (IBA GO_REF:33; IEA GO_REF:120; IDA PMID:8943022) -> ACCEPT core;
  IDA is domain-based but sound.
- MF mRNA binding (IBA) -> ACCEPT (CCHC fingers + DEAD-box; RNA binding is well supported;
  "mRNA" is a reasonable specific for a germline RNP helicase).
- MF nucleic acid binding (IEA InterPro) -> ACCEPT but general (subsumed by RNA binding/mRNA).
- MF ATP binding (IEA InterPro) -> ACCEPT (P-loop/Walker A).
- MF zinc ion binding (IEA InterPro) -> ACCEPT (six CCHC fingers).
- MF ATP hydrolysis activity (IEA RHEA) -> ACCEPT (DEAD-box ATPase; core catalytic step).
- MF JUN kinase binding (IEA GO_REF:117; IPI PMID:12435362 with WB:kgb-1) -> ACCEPT
  (experimentally, GLHs bind KGB-1).
- MF protein binding (IPI PMID:12435362, with UniProtKB:O44408=kgb-1) -> MODIFY: uninformative
  "protein binding"; the interactor is KGB-1 -> propose JUN kinase binding (GO:0008432).
- CC P granule (IBA; IEA GO_REF:117; IDA PMID:8943022) -> ACCEPT core (defining localization).
- CC nucleus (IBA GO_REF:33) -> KEEP_AS_NON_CORE (predominantly perinuclear/cytoplasmic; weak
  sperm-chromatin nuclear hint; not core; do not REMOVE given genuine uncertainty).
- BP germ cell development (IBA; IEA GO_REF:117; IMP PMID:8943022) -> ACCEPT (antisense sterile).
- BP gamete generation (IBA GO_REF:33) -> ACCEPT/KEEP (broad; part of germline function).
- BP cell differentiation (IBA GO_REF:33) -> KEEP_AS_NON_CORE (very general; germ cell dev is
  the informative term).
- BP post-embryonic development (IMP PMID:8943022; IEA GO_REF:117) -> KEEP_AS_NON_CORE (broad;
  reflects timing of germline proliferation).
- BP RNA metabolic process (ISS PMID:8943022) -> MODIFY/KEEP: very broad; RNP remodeling is
  the mechanistic intent but no glh-2-specific process term is strongly supported. Keep as
  non-core rather than invent specifics.

## Provenance policy
Cached publications used for verbatim supporting_text: PMID_8943022 (abstract-only),
PMID_12435362 (abstract-only), PMID_18430929 (abstract-only). No fabricated quotes; every
supporting_text below is a verbatim substring of a cached abstract.

## Deep research status (2026-07-04)
Falcon deep-research was attempted TWICE (`just deep-research-falcon worm glh-2 --fallback
perplexity-lite`). Both attempts hung: the deep-research-client (falcon provider) ran >20 min
with zero output, the wrapper's 600s per-provider timeout left an orphaned falcon child, and
NO deep-research file (falcon or perplexity-lite fallback) was ever produced. Per repo policy
I did NOT fabricate a `-deep-research-*.md` file. The review is therefore grounded in UniProt
(Q966L9), the GOA TSV, and three cached primary/genetic papers (PMID:8943022 Gruidl 1996;
PMID:12435362 Smith 2002; PMID:18430929 Spike 2008), supplemented by non-cited WebSearch of
the Alliance/WormBase gene page for orientation only. Where glh-2-specific evidence is absent,
annotations are handled conservatively (KEEP_AS_NON_CORE / MODIFY, not REMOVE) and the
uncertainties are recorded as knowledge_gaps.
