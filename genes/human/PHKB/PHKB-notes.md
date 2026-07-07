# PHKB (human) review notes

UniProtKB:Q93100 (KPBB_HUMAN) — Phosphorylase b kinase regulatory subunit beta. HGNC:8927. 1093 aa.

## Core biology (established)

PHKB encodes the **beta regulatory subunit of phosphorylase kinase (PhK)**. PhK is a
large ~1.3 MDa (αβγδ)4 hexadecamer. Within it:
- **gamma (PHKG1 muscle / PHKG2 liver) is the catalytic Ser/Thr protein kinase**;
- **alpha (PHKA1/PHKA2) and beta (PHKB) are large regulatory subunits** — NOT themselves
  kinases;
- **delta is calmodulin** (the Ca2+ sensor).

PHKB is shared between the muscle and liver holoenzymes (Reactome R-HSA-71541 muscle /
R-HSA-71588 liver; ComplexPortal CPX-2640 muscle, CPX-9581 liver).

Mechanism of activation: both alpha and beta are phosphorylated by cAMP-dependent
protein kinase (PKA); this, together with Ca2+ sensing by the delta (calmodulin)
subunit, relieves autoinhibition of the catalytic gamma subunit, so PhK phosphorylates
glycogen phosphorylase (b → a) and triggers glycogenolysis.
[PMID:25051373 "the γ-subunit possesses enzymatic activity that is tightly regulated by the other three regulatory subunits"]
[PMID:25051373 "cAMP levels that stimulate protein kinase A (PKA) to phosphorylate the α- and β-subunits (PHKA and PHKB)"]

Cryo-EM of human muscle PhK (Yang et al 2024) shows the beta subunit forms the central
β4 scaffold connecting the four αβγδ modules, has a glucoamylase-like fold but NO enzyme
activity, and contains an ADP-binding pocket that allosterically enhances PhK activity.
[PMID:38548794 "The α- and β-subunits possess glucoamylase-like domains, but exhibit no detectable enzyme activities"]
[PMID:38548794 "wherein four αβγδ modules are connected by the central β4 scaffold"]
[PMID:38548794 "We also reveal an ADP-binding pocket in the β-subunit, which plays a role in allosterically enhancing PhK activity"]

PHKB's own molecular role is regulatory/structural. It is NOT catalytic. Any
GO:0004689 phosphorylase kinase activity attributable to PHKB reflects the holoenzyme
(contributes_to), not intrinsic PHKB catalysis.

UniProt records calmodulin-binding regions (aa 7-29, 768-795, 920-951; ECO:0000255
predicted) and the Calmodulin-binding keyword. Note: the primary calmodulin (delta)
subunit binds the gamma subunit; PHKB calmodulin binding is by keyword/InterPro
inference and is at most a secondary/contributory MF.

## Localization
- Cytosolic (Reactome TAS): the PhK complex is a cytosolic enzyme (R-HSA-71541/71588).
- UniProt lists Cell membrane; Lipid-anchor; Cytoplasmic side (ECO:0000305, inferred
  from farnesylation of C-terminal Cys-1090, by similarity to rabbit P12798). The
  UniProt-SubCell IEA to GO:0005886 plasma membrane derives from this inferred lipid
  anchor. Weak/inferred; keep as non-core.

## Disease
GSD IXb / GSD9B (MIM:261750): autosomal-recessive liver + muscle phosphorylase kinase
deficiency, generally mild, clinical improvement with age.
[PMID:9402963 "liver glycogenosis caused by Phk deficiency"]
UniProt: mild phenotype attributed to an "incomplete holoenzyme that lacks the beta
subunit, but that may possess residual activity".

## Interactions (IPI protein binding annotations)
- PMID:21418524 (IntAct, with PASK/PASKIN Q96RG2): this paper is about PASKIN substrate
  preference and PI-monophosphate inhibition; PHKB is only an IntAct high-throughput
  interactant. Bare GO:0005515 protein binding — uninformative → MARK_AS_OVER_ANNOTATED.
- PMID:25051373 (IntAct, with CEMIP/KIAA1199 Q8WUJ3): pull-down + co-IP shows PHKB binds
  the C-terminal region of KIAA1199/CEMIP, proposed to promote glycogen breakdown in
  cancer cells. Real binding evidence but bare protein binding term is uninformative →
  MARK_AS_OVER_ANNOTATED.
- PMID:25416956 (IntAct, with CAMK2B Q13554): proteome-scale Y2H interactome map; PHKB is
  one of ~14,000 binary interactions. Bare protein binding → MARK_AS_OVER_ANNOTATED.

Per policy: bare protein binding IPIs are NOT removed; use MARK_AS_OVER_ANNOTATED.

## Annotation-by-annotation plan
- GO:0005964 phosphorylase kinase complex (IBA, IEA, IPI-ComplexPortal): ACCEPT (core CC).
- GO:0005516 calmodulin binding (IEA/InterPro): KEEP_AS_NON_CORE (inferred; delta subunit
  is the main CaM; PHKB CaM-binding regions are ECO:0000255 predicted).
- GO:0005886 plasma membrane (IEA-SubCell): KEEP_AS_NON_CORE (inferred lipid anchor;
  complex is cytosolic; weak).
- GO:0005975 carbohydrate metabolic process (IEA/InterPro): MODIFY → glycogen catabolic
  process / glycogen metabolic process are more specific and accurate.
- GO:0005977 glycogen metabolic process (IEA + TAS): ACCEPT (accurate BP).
- GO:0005515 protein binding x3 (IPI): MARK_AS_OVER_ANNOTATED (uninformative).
- GO:0005980 glycogen catabolic process (IDA-ComplexPortal, PMID:38548794): ACCEPT (core).
- GO:0005829 cytosol (TAS x2, Reactome): ACCEPT (core CC).
- GO:0006091 generation of precursor metabolites and energy (TAS, PMID:9402963):
  KEEP_AS_NON_CORE (glycogenolysis liberates glucose for energy, but this is a broad
  parent process; keep non-core).
</content>
