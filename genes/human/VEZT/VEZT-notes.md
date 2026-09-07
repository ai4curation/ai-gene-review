# VEZT (vezatin, human, UniProt Q9HBM0) — curation notes

Journal for the GO annotation review. Provenance is given inline as
`[PMID:NNNNN "verbatim quote"]`. All quotes below were checked to be verbatim
substrings of the cached `publications/PMID_*.md` files.

## 2026-09-04 — annotation review pass

### Identity and architecture

VEZT encodes vezatin, a member of the vezatin family (Pfam PF12632; InterPro
IPR026858 Vezatin, IPR026859 Myosin-bd). UniProt Q9HBM0 is 779 aa with two
predicted transmembrane helices at 139–159 and 162–182, a coiled coil at
430–462, and long disordered stretches in the C-terminal region (618–719,
757–779). Four alternative products are annotated (Q9HBM0-1/-2/-5/-6); isoforms
5 and 6 are flagged as likely NMD substrates.

Topology was settled experimentally in the mouse/canine system:
[PMID:20049712 "We conclude that vezatin is an integral membrane protein with
two transmembrane domains, and cytoplasmic N- and C-terminal regions"].
Surface accessibility of the short extracytoplasmic loop was shown earlier:
[PMID:11080149 "both antibodies labelled the cell surface, demonstrating that
vezatin is a transmembrane protein"].

This topology is the main reason to treat the nuclear annotations sceptically
(see below) — there is no obvious route for a two-pass membrane protein with
both termini cytoplasmic to reach the nucleoplasm, although a non-membrane
splice product exists (the A34.2 ORF cloned in PMID:11080149 has no predicted
TM segment).

### Molecular function — myosin VIIA binding is the anchor

Vezatin was discovered as a two-hybrid partner of the MYO7A tail:
[PMID:11080149 "the C-terminal FERM domain of myosin VIIA binds to a novel
transmembrane protein, vezatin"], with domain resolution:
[PMID:11080149 "vezatin specifically interacts with the C-terminal FERM domain
of myosin VIIA"] (binds the FERM half, not the MyTH4 half; confirmed by
co-IP from co-transfected HEK293 cells and by pull-down of endogenous vezatin
from human Caco-2 extracts).

GO:0017022 myosin binding (IEA from InterPro:IPR026859) is therefore an
unusually well-grounded IEA — the domain mapping is validated by direct
experiment on the human protein. It is also the *only* MF annotation on VEZT.
Note there is no GO:0005515 protein binding line to worry about here.

Second cytoskeletal link: [PMID:20049712 "vezatin directly interacts with
radixin in its actin-binding conformation"] and [PMID:20049712 "we provide
evidence that vezatin associates with actin filaments at cell-cell junctions"].
Vezatin binds the radixin FERM domain (aa 1–310) but not the closed
T564A form — i.e. it engages ERM proteins only in their open, actin-competent
state. This is a candidate for a future MF term but there is currently no GOA
line for it.

Caveat carried forward from the primary paper: a *direct* vezatin–alpha-catenin
interaction was never demonstrated ("it remains to be established whether or
not vezatin directly binds to α-catenin", Discussion of PMID:11080149). The
frequently drawn VEZT–alpha-catenin edge is probably indirect. Do not annotate
cadherin binding or catenin binding on this evidence.

### Location — adherens junction is the core

[PMID:11080149 "These results identify vezatin as a ubiquitous protein of
adherens junctions"], with biochemical association to the cadherin–catenin
complex: [PMID:11080149 "Vezatin co-immunoprecipitated with E- or N-cadherin
and β- and α-catenins"]. Recruitment requires the E-cadherin cytoplasmic tail
(lost in ΔCyto and ΔCB but retained in ΔPR) and is restored by an
E-cadherin/alpha-catenin chimera. Vezatin is explicitly *not* at desmosomes or
focal adhesions.

Timing matters for choosing the right BP term:
[PMID:20049712 "vezatin recruitment at AJs in MDCKII cells is markedly delayed
compared to that of E-cadherin"] and [PMID:20049712 "the protein does not play
a role in the formation of junctions, but rather participates in their
stability"].

### Hair cells and the ankle-link complex (the Usher-adjacent part)

Two distinct hair-cell pools:
1. Adherens junctions between hair cells and supporting cells (this is the pool
   whose loss causes the noise phenotype).
2. The base of developing stereocilia, facing the ankle links:
   [PMID:11080149 "conspicuous vezatin labelling was observed at the base of the
   hair cell stereocilia"], [PMID:11080149 "which was shown to face the ankle
   links by immunoelectron microscopy"], and
   [PMID:11080149 "vezatin is, in addition, concentrated at another
   membrane-membrane interaction site, namely at the fibrillar links
   interconnecting the bases of adjacent stereocilia"].

Michalski et al. established the complex directly:
[PMID:17567809 "the putative transmembrane protein vezatin, and the PDZ
(postsynaptic density-95/Discs large/zona occludens-1) domain-containing
submembrane protein whirlin are colocalized with Vlgr1 at the stereocilia base
in developing cochlear hair cells"];
[PMID:17567809 "our results support the existence of an ankle-link molecular
complex (ALC)"];
[PMID:17567809 "we were able to show that vezatin binds to the cytoplasmic
region of usherin"].
Vezatin is delocalized from the stereocilia base in three independent mutants
(Vlgr1-null, shaker-1/Myo7a-null, whirler/Whrn-null), so the evidence is
genetic as well as biochemical.

**Key curation judgment.** GO:0002142 "stereocilia ankle link complex" is
defined as "A complex of proteins that connect growing stereocilia in
developing cochlear hair cells, composed of Vlgr1, usherin, vezatin, and
whirlin" — vezatin is named in the term definition, so the ISS part_of
annotation is exactly right. By contrast GO:1990696 "USH2 complex" is defined
as the four proteins USH2A, GPR98/ADGRV1, WHRN and PDZD7. Vezatin is not one of
them, and no VEZT coding mutation has been shown to cause Usher syndrome or any
Mendelian deafness. So: accept GO:0002142; do **not** add GO:1990696 on the
strength of the vezatin–usherin interaction alone. The two structures overlap
in space and share components but are not the same complex.

Functional consequence of losing hair-cell vezatin:
[PMID:20049712 "Conditional mutant mice bearing non-functional vezatin alleles
only in the sensory cells of the inner ear (hair cells) indeed exhibited
irreversible hearing loss after only one minute exposure to a 105 dB broadband
sound"] plus late-onset progressive hearing/vestibular loss with hair cell
death. This is a *modifier of sensory-epithelium resilience* phenotype, not a
monogenic deafness gene claim.

### Loss of function in mouse — junction maintenance

[PMID:17452094 "the lack of zygotic vezatin is embryonic lethal, indicating
that vezatin is an essential gene"] and, in null blastocyst outgrowths,
[PMID:17452094 "the junctional proteins E-cadherin and beta-catenin are
delocalized and not observed at the plasma membrane anymore"].
Earlier morpholino work agrees: [PMID:16199027 "It co-localizes with E-cadherin
throughout development, being found all around the cell cortex before
compaction and basolaterally in adherens junctions thereafter"].

Together with the MDCKII late-recruitment data this justifies a NEW annotation
of GO:0034334 "adherens junction maintenance" (involved_in, ISS from mouse),
which is more precise than the two existing GO:0098609 cell-cell adhesion
lines. GO:0098609 is kept (correct, appropriately general for an IBA).

### Provenance of the odd locations

- **Nucleus (GO:0005634, IEA SL-0191 + ISS from Q3ZK22) and nucleoplasm
  (GO:0005654, IDA/HPA).** The mouse source observation is
  [PMID:16199027 "vezatin is also detected in nuclei during most of the cell
  cycle"]. So this is *not* a fabricated mapping — there are two independent
  observations (mouse embryos; human HPA immunofluorescence). But it is
  irreconcilable with the established topology and there is no nuclear
  function, NLS, or nuclear partner on record. Called KEEP_AS_NON_CORE rather
  than REMOVE: removing a curated IDA and a legitimate ortholog transfer on
  the basis of a topology argument alone would be overreach.
- **Acrosomal vesicle (GO:0001669, IEA SL-0007).** From mouse germ cells:
  [PMID:17379651 "In differentiating spermatids, ultrastructural data indicate
  that vezatin localizes in the acrosome"] and
  [PMID:17379651 "In epididymal sperm, vezatin localizes also to the outer
  acrosomal membrane"]. Real, but germ-cell restricted, and notably vezatin is
  *absent* from the ectoplasmic specializations (the AJs of the seminiferous
  epithelium), so it is not just the junctional pool showing up. KEEP_AS_NON_CORE.

### Other vertebrate roles not currently in human GOA

Recorded as context; none used to support a human annotation.
- Neuromuscular junction: [PMID:31411944 "we used mass spectrometry to identify
  vezatin, a two-pass transmembrane protein, as an acetylcholine receptor
  (AChR)-associated protein"]. Required for postsynaptic maturation and AChR
  stability, not for synapse formation.
- Dendritic spines: [PMID:22745500 "Vezatin localizes in spines in mature mouse
  hippocampal neurons and codistributes with PSD95"].
- Retrograde axonal transport: [PMID:32788307 "we identify Vezatin as a
  conserved regulator of retrograde axonal transport"] — Drosophila/zebrafish;
  tagged human VEZT did not rescue the fly phenotype, and fungal VezA
  (dynactin assembly) must not be conflated with human Q9HBM0. Not annotated.
- Endometriosis: rs10859871 at 12q22 is a cis-eQTL raising VEZT expression
  [PMID:27005890 "expression is altered in the endometrium of endometriosis
  patients and is an excellent candidate for having a causal role in
  endometriosis"]. This is a regulatory/disease-association result, not
  evidence of molecular function — no GO annotation follows from it.

### Actions assigned (13 GOA lines + 1 NEW)

| Term | Evidence | Action |
|---|---|---|
| GO:0005886 plasma membrane | IBA | ACCEPT |
| GO:0098609 cell-cell adhesion | IBA | ACCEPT |
| GO:0001669 acrosomal vesicle | IEA | KEEP_AS_NON_CORE |
| GO:0005634 nucleus | IEA | KEEP_AS_NON_CORE |
| GO:0005886 plasma membrane | IEA | ACCEPT |
| GO:0005912 adherens junction | IEA | ACCEPT |
| GO:0017022 myosin binding | IEA | ACCEPT |
| GO:0060171 stereocilium membrane | IEA | ACCEPT |
| GO:0098609 cell-cell adhesion | IEA | ACCEPT |
| GO:0005654 nucleoplasm | IDA | KEEP_AS_NON_CORE |
| GO:0005634 nucleus | ISS | KEEP_AS_NON_CORE |
| GO:0005886 plasma membrane | EXP | ACCEPT |
| GO:0002142 stereocilia ankle link complex | ISS | ACCEPT |
| GO:0034334 adherens junction maintenance | ISS (proposed) | NEW |

No REMOVE, MODIFY, MARK_AS_OVER_ANNOTATED or UNDECIDED calls were needed: the
GOA set for VEZT is small, internally consistent, and every line traces back to
a real observation. The only over-reach risk in the set is the nucleus/
nucleoplasm cluster, handled with KEEP_AS_NON_CORE.

### Open questions for experts

- Which Q9HBM0 isoform accounts for the nuclear/nucleoplasmic signal, if any?
  Does the TM-less ORF (A34.2-type) exist as protein in human cells?
- What bridges vezatin to alpha-catenin, given that the direct interaction was
  never demonstrated?
- Is the vezatin–usherin interaction sufficient to place vezatin in the USH2
  complex proper, or only in the ankle-link complex? Curators of ADGRV1/USH2A/
  WHRN may have a view.
- Is there any human VEZT variant burden in noise-induced hearing loss or
  age-related hearing loss cohorts (the mouse phenotype predicts a modifier
  effect rather than Mendelian deafness)?
