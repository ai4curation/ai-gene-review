# patched (ptc), Drosophila melanogaster — curation notes

UniProt: P18502 (PTC_DROME) · FlyBase: FBgn0003892 (CG2411) · 1286 aa · PANTHER PTHR46022 ("PROTEIN PATCHED")

Journal for the GO annotation review in `ptc-ai-review.yaml`. All assertions carry an inline
citation; `[PMID:x "quote"]` means the quoted string is verbatim in `publications/PMID_x.md`.

---

## 1. What the protein is

Twelve-pass integral membrane protein of the RND (resistance-nodulation-division) permease
superfamily, with a sterol-sensing domain (SSD) spanning TM2–TM6 (UniProt features: `DOMAIN 428..583 /note="SSD"`),
two large extracellular loops, and a ~180-residue disordered cytoplasmic C-terminal tail
(`REGION 1116..1237 /note="Disordered"`). TCDB classifies it under the RND superfamily
(`DR TCDB; 2.A.6.6.2`). It is the founding member of the Patched family; human PTCH1 (Q13635)
and PTCH2 (Q9Y6C5) sit in the same PANTHER family PTHR46022, which is the structural evidence
that the Hedgehog reception tier is conserved from insects to vertebrates
(see `modules/hedgehog_signaling.yaml`, annoton `patched_receptor`).

Two things are true simultaneously and are the frame for everything below:

- ptc is the **receptor** for the Hedgehog (Hh) morphogen, and
- ptc is the pathway's **brake**: in the unliganded state it keeps Smoothened (Smo) off, and it is
  itself a Hh target gene, so Hh reception raises ptc levels and thereby sharpens and shortens the
  gradient.

## 2. Genetics that established the brake

Ingham, Taylor & Nakano showed that ptc acts permissively, repressing wingless transcription, and
that hh antagonises it — and proposed, before any biochemistry, that Ptc *is* the Hh receptor:
[PMID:1653906 "the role of patched in positional signalling is permissive rather than instructive, its activity being required to suppress wingless transcription in cells predisposed to express the latter"]
and [PMID:1653906 "We suggest that the patched protein may itself be the receptor for this signal, implying that this is an unusual mechanism of ligand-dependent receptor inactivation."]

Chen & Struhl separated the two jobs explicitly — reception/transduction and ligand sequestration:
[PMID:8898207 "we present evidence that implicates another multiple-pass transmembrane protein, Patched (Ptc), in Hh reception and suggests a novel signal transduction mechanism in which Hh binds to Ptc, or a Ptc-Smo complex, and thereby induces Smo activity"]
and [PMID:8898207 "Our results also show that Ptc limits the range of Hh action; we provide evidence that high levels of Ptc induced by Hh serve to sequester any free Hh and therefore create a barrier to its further movement."]

Denef et al. added the reciprocal trafficking logic, and — importantly for the mechanism question
below — argued for **indirect** regulation:
[PMID:10966113 "Here we present evidence that Patched destabilizes Smoothened in the absence of Hedgehog."],
[PMID:10966113 "Hedgehog binding causes removal of Patched from the cell surface."],
[PMID:10966113 "These findings raise the possibility that Patched acts indirectly to regulate Smoothened activity."]

## 3. The receptor is Ptc *plus* a co-receptor

Ihog/Boi are required for pathway activation and bind Ptc directly:
[PMID:20048000 "We demonstrate that Ihog interacts directly with Ptc, is required for presentation of Ptc on the cell surface, and that Ihog and Ptc are both required for high-affinity Hh binding."]
The same paper is candid that direct Hh–Ptc binding had not been demonstrated biochemically in the fly:
[PMID:20048000 "the lack of physical evidence for direct binding of Hh to Ptc"], and
[PMID:20048000 "immobilized HhN fails to precipitate detergent-solubilized Ptc alone, but does so in the presence of detergent-solubilized Ihog"].

Camp et al. later dissociated the two roles genetically and put the ligand-binding job back on Ptc:
[PMID:25231763 "cells expressing Ptc can retain and sequester the Hh ligand without Ihog and Boi, but that Ihog and Boi cannot do so without Ptc"], and
[PMID:25231763 "they are essential for pathway activation because they allow Hh to inhibit Ptc and thereby relieve its repression of Smo"].

So: **Ptc binds Hh (GO:0097108) and is the Hh receptor (GO:0008158); Ihog/Boi raise the affinity and
are required for transduction but are not required for sequestration.** Both GO terms are justified
on fly evidence alone.

Ihog also binds Hh itself [PMID:16630821 "The first of two extracellular fibronectin type III (FNIII) domains of the Ihog protein mediates a specific interaction with Hh protein in vitro"],
and the ptc IDA to GO:0097108 from this paper rests on the cell-binding assays
[PMID:16630821 "the second FNIII domain is additionally required for in vivo signaling activity and for Ihog-enhanced binding of Hh protein to cells coexpressing Ptc"].

## 4. Where it acts

- Plasma membrane, and specifically the **basal** membrane where reception happens on cytonemes:
  [PMID:28825565 "Extracellular staining of Ptc and Hh confirms this basal localization of Hh-Ptc complex for signal reception"],
  [PMID:28825565 "The canonical Hh receptor Patched is localized in these cellular protrusions and Hh reception takes place in membrane contact sites between Hh-sending and Hh-receiving cytonemes."]
- Endocytic vesicles: [PMID:18198278 "We found a high percentage of colocalization of Hh, Ptc and ApoLs in early endocytic vesicles"].
  Ptc turnover is controlled by C2-WW-HECT E3 ligases [PMID:26446620 "PTC is post-translationally downregulated by HH, which promotes its endocytosis and destabilization"]
  and by Smurf, which ubiquitinates K1261 [PMID:24302888 "we found that Smo interacts with Smurf and promotes it to mediate Patched ubiquitination by targeting the K1261 site in Ptc"];
  UniProt records this as `CROSSLNK 1261 ... ECO:0000269|PubMed:24302888`.
- Cilium/ciliary membrane, but only in the one ciliated Drosophila cell type studied:
  [PMID:24768000 "Drosophila cells are nonciliated during development, which has led to the assumption that cilia-mediated Hh signaling is restricted to vertebrates. Here, we identify and characterize a cilia-mediated Hh pathway in Drosophila olfactory sensory neurons."]
  UniProt curates this as `Cell projection, cilium membrane {ECO:0000269|PubMed:24768000}`. This is a
  genuine but highly restricted location, unlike the vertebrate case where the cilium is the default
  venue for the pathway.

## 5. The mechanism question: how does Ptc restrain Smo?

This is an open knowledge gap, and `modules/hedgehog_signaling.yaml` records it as such
("The biochemical mechanism by which ligand-free Patched restricts Smoothened remains undetermined").
The important point for this review is that **the Drosophila record does not support a cholesterol-transport
molecular function for ptc.** What the fly record does contain:

1. **Arguments against direct Ptc–Smo inhibition.** [PMID:26863604 "It is unlikely that Ptc inhibits Smo by direct association"],
   with the stoichiometric argument spelled out in the same sentence — inhibition persists with Smo in
   50-fold molar excess, and substoichiometric Ptc represses Smo, i.e. the inhibition behaves catalytically.
   Denef et al. reached the same conclusion from trafficking [PMID:10966113 "These findings raise the possibility that Patched acts indirectly to regulate Smoothened activity."].
   The only fly physical evidence is complex-level co-fractionation
   [PMID:17284519 "We find that Cubitus interruptus, Sex-lethal, Patched and Smoothened co-immunoprecipitate and co-fractionate, suggesting a large complex of both membrane and cytoplasmic components of the Hedgehog pathway."],
   which does not distinguish direct from indirect association.

2. **Ptc binds PI(4)P through its SSD.** [PMID:26863604 "PtcWT and HA-SSD strongly bound PI(4)P, whereas HA-PtcΔSSD did not bind"],
   and Hh shifts the pool [PMID:26863604 "Hh treatment increases the interaction between Smo and PI(4)P but decreases the interaction between Ptc and PI(4)P"].
   Loss of Ptc raises PI(4)P [PMID:26863604 "We found that mutation of ptc or knockdown of Ptc by RNAi increased PI(4)P levels in the wing disc"].

3. **Ptc binds phosphatidic acid through its cytoplasmic tail, and this is required for Smo inhibition.**
   [PMID:37847757 "Deleting the Ptc C-terminal tail or mutating the predicted PA-binding sites within it prevented Ptc from inhibiting Smo in wing discs and in cultured cells."],
   [PMID:37847757 "The C-terminal tail of Ptc directly interacted with PA in vitro, an association that was reduced by Hh, and increased the amount of PA at the plasma membrane in cultured cells."],
   [PMID:37847757 "Our findings suggest that Ptc may sequester PA in the absence of Hh and release it in the presence of Hh, thereby increasing the amount of PA that is locally available to promote Smo activation."]

4. **Ptc is a lipoprotein receptor and moves lipid in bulk, independently of Hh signalling.**
   [PMID:18198278 "Ptc actively internalizes Lp into the endocytic compartment in a Hh-independent manner and physically interacts with Lp."],
   [PMID:18198278 "ApoLI protein was immunoprecipitated by Ptc in salivary glands overexpressing Ptc-GFP"],
   and the loss-of-function control [PMID:18198278 "in ptc 16 mutant clones, which do not produce Ptc protein at the A/P compartment border, we were unable to observe a down-regulation of lipid droplets"],
   with the authors' own separation of the two jobs [PMID:18198278 "we concluded that the effect of Ptc in lipid metabolism is an aspect of Ptc function independent of its role in the Hh signal transduction"].

**Decision taken in this review.** The human PTCH1 framing — molecular function `GO:0140303
intramembrane lipid carrier activity`, cholesterol as the transported species — is grounded in
vertebrate structures and transport assays and in the curated human GO-CAMs. Drosophila UniProt
carries the same claim but flags it `By similarity` from Q13635, and the fly GOA contains **no**
GO:0140303 annotation and no cholesterol-transport annotation of any kind. The three fly lipid
observations that do exist point at *three different lipids* (PI(4)P, phosphatidic acid, lipophorin
cargo), two of which (PI(4)P, PA) are read as Ptc *sequestering a Smo activator* rather than
exporting a Smo inhibitor, and one of which (lipophorin) the authors explicitly uncouple from
signalling. On that record it would be an unsupported import to assert an intramembrane cholesterol
carrier activity for fly ptc. The review therefore grounds ptc's molecular function on what the fly
data show — `GO:0008158 hedgehog receptor activity`, `GO:0097108 hedgehog family protein binding`,
and the two lipid-binding activities — and raises the transport question in `suggested_questions`
rather than asserting it. No `NEW` molecular-function term is proposed.

This is also why `GO:0005119 smoothened binding` (IBA) is marked as an over-annotation rather than
accepted: the PAINT node placement is reasonable at family level, but in the fly the best evidence
argues the restraint is *not* by direct association, and the term invites reading a binding claim as
the mechanism.

## 6. Downstream / pleiotropic annotations

Every one of these is a consequence of ptc restraining Smo in a particular tissue; none is a
separate molecular activity, so they are kept as non-core (or, where the paper itself says the
effect is non-autonomous, marked as over-annotated).

| Process | Paper | Note |
|---|---|---|
| Bolwig's organ morphogenesis | [PMID:10704398] | abstract foregrounds hh/eya/so; a Ci- and Fu-independent branch |
| eye-antennal disc morphogenesis | [PMID:11934850 "loss of Ptc or Smoothened activity affects cell proliferation in the eye-antennal disc and results in adult head capsule defects"] | authors argue a *positive*, non-canonical Ptc–Smo–Babo route |
| ovarian somatic stem cells | [PMID:11279500 "These cells cannot proliferate as stem cells in the absence of Hh signalling, whereas excessive Hh signalling produces supernumerary stem cells."] | GOA term is the vague `regulation of mitotic cell cycle`; the phenotype is stem-cell proliferation |
| follicle cell development | [PMID:29093440 "Hh signalling delayed differentiation of all follicle cell types"] | ptc(S2) FSC clones give supernumerary stalk cells |
| hippo signalling | [PMID:28667262 "Both the level and nuclear distribution of Yki were increased in ptc mutant clones."] | Hh acts upstream of Hippo; indirect |
| apoptosis | [PMID:23018595 "Surprisingly, cells with deregulated Hh activity do not protect themselves from apoptosis; instead, they promote cell survival of neighboring wild-type cells."] | explicitly non-cell-autonomous |
| axon guidance | [PMID:15754211 "guidance defects of this tract are due to loss and mis-specification of vMP2"] | the paper's own title says the effect is via neural identity |
| tracheal migration | [PMID:24651658 "Our results show that Hh modulates cell migration non-autonomously in the tissues surrounding the action of its activity."] | ptc mutants used as a Hh gain-of-function tool |
| gonad development | [PMID:21377458 "These gonads had completed SGP cluster fusion, but failed to condense completely into the round shape characteristic of the mature embryonic gonad."] | ptc is screen group com4 |
| genital disc primordium | [PMID:15893978 "several segment polarity genes (wingless, engrailed, hedgehog, and patched) are required for the proper allocation of the GDPCs"] | |
| wing shape | [PMID:16648592] | quantitative morphometrics on heterozygous insertions; weak as evidence, but the term is independently sound |

## 7. Protein-binding rows

Three `GO:0005515` rows, all removed as uninformative (the interactions themselves are not disputed):

- l(2)tid/Tid47 (FB:FBgn0002174) [PMID:12783860 "We provide functional evidence for its direct in vivo interaction with the Hh-bound Ptc receptor during signal transmission."]
- Sxl (FB:FBgn0264270) [PMID:17284519], complex-level co-IP, not a defined activity for Ptc.
- ihog (FB:FBgn0031872) [PMID:20048000]. This one has real functional content, but it is already
  carried by `GO:0008158` and `GO:0097108`, and GO has no term for "co-receptor binding" that would
  fit Ptc's side of the Ptc–Ihog interaction. `GO:0015026 coreceptor activity` describes Ihog, not Ptc.

## 8. Loose ends

- `GO:0045169 fusome` (IDA, `colocalizes_with`, [PMID:8898240]) is left UNDECIDED. The cached record is
  abstract-only and describes ptc as a *somatic* germarial protein
  [PMID:8898240 "patched (ptc) and cubitus interruptus (ci) are expressed in somatic cells throughout the germarium and in developing egg chambers"],
  while the fusome is a germline organelle. The curator saw the staining and we did not, so this is
  not overruled — but it cannot be confirmed from what is cached either.
- `GO:0048099` and `GO:0048100` are TAS rows. PMID:10625531's cached record carries no abstract at
  all, and PMID:11253649 is a review about adhesion, not about Hh. Both underlying processes are
  independently supported (e.g. [PMID:25231763 "it is through Hh pathway activation that Ihog and Boi maintain the boundary between the anterior and posterior compartments"]),
  so the terms are kept as non-core with the citation weakness recorded in `reference_review`.
- `GO:0016192 vesicle-mediated transport` is an inter-ontology IEA off `GO:0030228`. It is true but
  maximally vague; modified to `GO:0006898 receptor-mediated endocytosis`, which is what the
  lipophorin and Hh internalisation data actually show.
