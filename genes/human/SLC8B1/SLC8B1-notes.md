# SLC8B1 / NCLX (Q6J4K2) — review notes

## 1. What the protein is

SLC8B1 encodes NCLX, a 584-residue, ~13-TM member of the Ca2+/cation antiporter (CaCA) superfamily,
resident in the mitochondrial inner membrane and enriched in cristae. It is the long-accepted route
for Ca2+ efflux from the mitochondrial matrix.

- Localisation and the founding functional identification:
  [PMID:20018762 "we show that the Na(+)/Ca(2+) exchanger NCLX is enriched in mitochondria, where it
  is localized to the cristae."]
  [PMID:20018762 "our results converge to the conclusion that NCLX is the long-sought mitochondrial
  Na(+)/Ca(2+) exchanger."]
  [PMID:20018762 "NCLX-mediated mitochondrial Ca(2+) transport was inhibited, moreover, by CGP-37157
  and exhibited Li(+) dependence, both hallmarks of mitochondrial Na(+)-dependent Ca(2+) efflux."]
- Independent replication that NCLX (not LETM1) carries matrix Ca2+ extrusion:
  [PMID:24898248 "We conclude that NCLX, but not LETM1, mediates Ca(2+) extrusion from mitochondria."]
- Physiological consequences in beta cells:
  [PMID:23056385 "These findings suggest that the mitochondrial Na(+)/Ca(2+) exchanger, NCLX, shapes
  glucose-dependent mitochondrial and cytosolic Ca(2+) signals thereby regulating the temporal
  pattern of insulin secretion in"]
- Coupling to store-operated Ca2+ entry:
  [PMID:28219928 "we reveal that SOCE is accompanied by a rise in cytosolic Na+ that is critical in
  activating the mitochondrial Na+/Ca2+ exchanger (NCLX) causing enhanced mitochondrial Na+ uptake
  and Ca2+ efflux."]

The *Ca2+ efflux* role is about as well replicated as anything in mitochondrial Ca2+ biology. The
part that is now in question is the **counterion**.

## 2. The counterion problem

An anomaly has been on the record since NCLX was first cloned: unlike canonical NCX proteins, it
lacks several of the serines that coordinate Na+, and it uniquely accepts Li+ (PMID:15060069,
"Lithium-calcium exchange is mediated by a distinct potassium-independent sodium-calcium exchanger",
the paper behind the `GO:0005432` IDA of 2004). Two 2025/2026 cryo-EM studies turned this anomaly
into an explicit challenge.

### Fan et al., Nature 2025 (PMID:40931067) — H+/Ca2+, not Na+/Ca2+

[PMID:40931067 "Although proposed1 to mediate mito-NCX, NCLX, puzzlingly, lacks multiple
Na+-coordinating residues conserved in NCX proteins"]
[PMID:40931067 "Structural comparison indeed reveals that NCLX lacks the Na+-binding sites identified
in MjNCX (Sext and Sint)."]
[PMID:40931067 "Functional analyses further reveal an unexpected transport function of NCLX as a
H+/Ca2+ exchanger, rather than as a Na+/Ca2+ exchanger as widely believed"]
[PMID:40931067 "A key finding in this work is that NCLX functions as a H+/Ca2+ exchanger rather than
a Na+/Ca2+ exchanger."]

They also report the most direct challenge to the functional literature — mito-NCX survives loss of
NCLX, in four independently derived KO lines including two from another laboratory:
[PMID:40931067 "These results demonstrate that mito-NCX remains intact in NCLX KO cells."]

### Zhang et al., Nat Commun 2026 (PMID:42431881) — broader selectivity, not H+-specificity

Same structural premise, different functional conclusion:
[PMID:42431881 "While NCLX retains the canonical Ca²⁺-binding site, it lacks several key Na⁺-binding
residues found in NCXs, suggesting broader ion selectivity. Consistently, cell-based Ca²⁺ uptake
assays show that NCLX mediates Ca²⁺ exchange using Na⁺, K⁺, Li⁺, and potentially protons as
counterions."]
[PMID:42431881 "our assays indicate that NCLX operates as a non-selective cation/Ca²⁺ exchanger,
capable of coupling Ca²⁺ transport to Na⁺, K⁺, Li⁺, and potentially H⁺."]

Crucially, this study does **not** refute Na+ as a counterion — it demotes it from *the* counterion
to *one of several*. And it explicitly declines to adjudicate the TMEM65 question:
[PMID:42431881 "Although our study does not resolve this discrepancy, our structural and functional
data demonstrate that NCLX possesses intrinsic Ca²⁺ exchange activity and likely remains an essential
regulator of mitochondrial Ca²⁺ homeostasis."]

### Counter-evidence that should not be forgotten

Before the structures, mutagenesis mapped **distinct Na+- and Li+-selective residues** in the NCLX
transport site — i.e. positive functional evidence that NCLX *does* have counterion-specific sites:
[PMID:28130126 "We identified distinct Na+ and Li+ selective residues in the NCLX transport site."]
[PMID:28130126 "In permeabilized cells, N149A, P152A, D153A, N467Q, S468T and G494S demonstrated
normal Li+/Ca2+ exchange activity but a reduced Na+/Ca2+ exchange activity."]

And the Li+ anomaly itself was the founding observation:
[PMID:15060069 "Surprisingly, NCLX catalyzes active Li(+)/Ca(2+) exchange, thereby explaining the
exchange of these ions in mammalian tissues."]

The two structure papers also flatly contradict each other on the counterion question. Fan et al.
find monovalent cations do nothing:
[PMID:40931067 "Imposing inward Na+ or K+ gradients across the oocyte membrane did not affect NCLX
Ca2+ transport (Fig. 5f)"]
while Zhang et al. find Na+, K+ and Li+ all act as counterions. Both used heterologous expression;
they disagree about the result, not merely about its interpretation.

### What the two structures agree on

1. NCLX is a bona fide Ca2+ exchanger with a conserved central Ca2+ site.
2. It lacks the canonical Na+-coordinating residues.
3. It assembles as a **trimer**, not a dimer:
   [PMID:40931067 "adopts a trimeric assembly in both Ca2+-bound and -free conditions"]
   [PMID:42431881 "The larger SEC fraction contained trimeric NCLX, whose structure was determined at
   a resolution of 3.15 Å, with all three protomers adopting identical conformations"]

Point 3 is a clean, independently replicated contradiction of the `GO:0042803 protein
homodimerization activity` annotation (IPI, PMID:20018762). Self-association is right; the
stoichiometry is not.

## 3. Provenance caveat — this is not three independent votes

PMID:40931067 (NCLX = H+/Ca2+ exchanger) and PMID:40691517 (TMEM65 = mito-NCX) share senior authors
(Feng L., Tsai M.-F.). They form a single, internally coherent model in which TMEM65 does mito-NCX
and NCLX does something else. The independent structural study (PMID:42431881) reproduces the
*structural* observation but reaches a *different* functional conclusion and keeps Na+ in the list of
counterions. So the state of the evidence is:

- Na+-exclusivity: challenged by two structures, one of which nonetheless still finds Na+ works.
- Ca2+ exchange by NCLX: unchallenged by anyone.
- NCLX as the essential mediator of *mitochondrial* Ca2+ efflux: challenged by one lab's KO data,
  against ~15 years of loss-of-function work from several labs.

## 4. Curation decisions

**`GO:0005432 calcium:sodium antiporter activity` → `MODIFY` to `GO:0015368 calcium:monoatomic cation
antiporter activity`** (its direct `is_a` parent; verified via QuickGO, and already annotated to this
gene by Reactome TAS). Rationale:

- This is *not* a removal. Every experimental annotation is retained, just at the term the current
  evidence actually supports. The brief's rule against discarding experimental annotations on the
  strength of one structure paper is respected.
- The over-specific part of GO:0005432 is exactly the part under challenge — the identity of the
  counterion as Na+. The generalised parent is compatible with all three readings (Na+/Ca2+,
  H+/Ca2+, and non-selective cation/Ca2+) and with the Li+ exchange that has been on the record
  since 2004.
- The supporting argument is not a single paper: it is a structural fact reported independently
  twice, plus a long-standing sequence anomaly, plus NCLX's anomalous Li+ tolerance.
- All seven GO:0005432 rows (IBA, Ensembl IEA, IMP, IDA ×4, Reactome TAS) take the same action, per
  the same-term-same-action rule.

**`GO:0086038 calcium:sodium antiporter activity involved in regulation of cardiac muscle cell
membrane potential` → `MARK_AS_OVER_ANNOTATED`** (IEA/ISS only). The term's definition ties the
exchange to "regulating the membrane potential of a cardiac muscle cell" — a sarcolemmal NCX1
(SLC8A1) role. A cristae-resident exchanger does not set the cardiomyocyte membrane potential
directly; this is an orthology projection that carries the Na+ claim *and* a wrong membrane.

**`GO:0042803 protein homodimerization activity` → `MODIFY` to `GO:0042802 identical protein
binding`** (verified direct `is_a` parent). Self-association is real (co-IP, PMID:20018762; both
cryo-EM structures), the dimer stoichiometry is contradicted by both structures.

**`GO:0035725 sodium ion transmembrane transport` → `MARK_AS_OVER_ANNOTATED`.** Derived
automatically from GO:0005432 by inter-ontology inference (GO_REF:0000108); it inherits the
counterion claim that is under challenge, and no direct evidence for NCLX-mediated Na+ flux exists
independent of it.

**Plasma membrane / sarcolemma (`GO:0005886`, `GO:0042383`) → `MARK_AS_OVER_ANNOTATED`.** Residue of
the pre-2010 literature, when NCKX6/NCLX was characterised at the plasma membrane; Reactome still
models a plasma-membrane Li+/Ca2+ exchanger (R-HSA-425822). Everything since PMID:20018762 places
NCLX in the IMM/cristae.

**Everything in the Ca2+-efflux cluster is accepted as core**: `GO:0099093`, `GO:0006851`,
`GO:0051560`, `GO:0006874`, `GO:0051480`, `GO:0070588`, `GO:0015368`, and the IMM/crista locations.
Tissue-specific downstream processes (insulin secretion, glucose homeostasis, SOCE regulation,
lymphocyte chemotaxis, cardiac membrane potential) are kept as non-core.

## 5. Open questions recorded in the review

1. What is the physiological counterion in situ — Na+, H+, or several?
2. Why does mito-NCX persist in NCLX KO cells (PMID:40931067) when NCLX knockdown/knockout reduces
   mitochondrial Ca2+ efflux in so many other systems?
3. Does the trimeric assembly imply cooperativity, and what is the exchange stoichiometry?
4. What is the physical relationship between NCLX and TMEM65 (see `TMEM65-notes.md`)?
