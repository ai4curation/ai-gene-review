# GO:0016080 synaptic vesicle targeting — Obsolescence Review

**Goal:** Replace all annotations to GO:0016080 (synaptic vesicle targeting) with more precise GO terms so the term can be obsoleted.

**New relevant term:** GO:7770062 vesicle membrane tethering activity (MF)
- Definition: "A membrane-membrane adaptor activity that provides the first point of contact and physically bridges the vesicle membrane and its target membrane prior to vesicle docking and fusion." [PMID:19575650, PMID:19887069]
- Namespace: **molecular_function**
- Note: Since current annotations are BP, some will stay in BP (with a better term), while others — particularly tethering complex subunits — may move to this MF term. An annotation can change aspect where warranted.

---

## Annotation-by-annotation review

### 1–7. FlyBase Drosophila exocyst complex + CASK — PMID:10798391 (NAS)

**Paper:** Lloyd TE et al. (2000). "A genome-wide search for synaptic vesicle cycle proteins in Drosophila." *Neuron* 26(1):45–50.

**Summary:** A bioinformatics scan of the Drosophila genome identifying fly homologs of 93% of vertebrate synaptic vesicle cycle proteins. Evidence type is NAS (Non-traceable Author Statement) — no direct experimental function assigned in this paper; identities inferred by homology to vertebrate SVC proteins.

---

#### Exo84 (FB:FBgn0290418), Sec10 (FB:FBgn0266673), Sec8 (FB:FBgn0266672), Sec6 (FB:FBgn0266671), Sec5 (FB:FBgn0266670), Exo70 (FB:FBgn0266667)

**Proteins:** Subunits of the **exocyst complex**, a hetero-octameric vesicle-tethering complex.

**Recommendation:** Replace GO:0016080 (BP) with **GO:7770062 vesicle membrane tethering activity** (MF)

**Reasoning:** The exocyst complex is the canonical vesicle tethering complex in eukaryotes. Its subunits directly mediate the first physical contact between secretory vesicles and the target plasma membrane, prior to SNARE-mediated docking and fusion. This matches exactly the definition of GO:7770062: "provides the first point of contact and physically bridges the vesicle membrane and its target membrane prior to vesicle docking and fusion." Sec5, Sec6, Sec8, Sec10, Exo70, and Exo84 are all exocyst subunits conserved from yeast to vertebrates. The original annotation to "synaptic vesicle targeting" was a coarse placeholder; MF tethering activity is both more precise and more mechanistically accurate.

> Note: Evidence code NAS should be reviewed — if better experimental evidence exists in the literature, the evidence code should be updated. For now, the aspect change from BP→MF with NAS is appropriate given the strong phylogenetic/functional conservation.

**Alternative BP annotation (if BP annotation is also desired):** GO:0006904 vesicle docking involved in exocytosis, or a synaptic-vesicle-specific child term if one exists.

---

#### CASK (FB:FBgn0013759)

**Protein:** CASK — a MAGUK (membrane-associated guanylate kinase) scaffold protein, not an exocyst subunit.

**Recommendation:** **Do not use GO:7770062** (CASK does not perform direct membrane-membrane tethering). Replace GO:0016080 with a BP term.

**Reasoning:** CASK is a multi-domain scaffold (CaMK-like, L27, PDZ, SH3, GK domains) that organizes the presynaptic active zone and links cell-adhesion molecules (neurexin) to the cytoskeleton. Its role is in active zone assembly and organization, not in directly bridging vesicle and target membranes. The NAS annotation from a bioinformatics screen is weak.

**Suggested replacement BP term:** GO:0007416 synapse assembly
(or, if the gene is annotated in the context of neurotransmitter release: GO:0007269 neurotransmitter secretion)

> Quoted text from abstract: "A genome-wide search for synaptic vesicle cycle proteins in Drosophila" — this paper does not establish a specific molecular role for CASK in vesicle targeting; the annotation appears to be a guilt-by-association inference.

---

### 8. Psen1 (MGI:MGI:1202717, mouse) — PMID:12805290 (IMP)

**Paper:** Pigino G et al. (2003). "Alzheimer's presenilin 1 mutations impair kinesin-based axonal transport." *J Neurosci* 23(11):4499–4508.

**Summary:** PS1 (Presenilin-1) interacts with GSK3β. FAD-associated PS1 mutations increase GSK3β activity, leading to hyperphosphorylation of kinesin light chains, reduced kinesin–organelle binding, and decreased vesicle/mitochondrial density in neuritic processes. The phenotype observed is impaired **fast axonal transport**, not a synaptic vesicle targeting defect per se.

**Recommendation:** Replace GO:0016080 with **GO:0048489 synaptic vesicle transport** (BP)
or more specifically: **GO:0008090 retrograde axon cargo transport** / **GO:0099641 anterograde axonal protein transport**

**Reasoning:** The paper's key finding is disruption of kinesin-based axonal transport by PS1 mutations, resulting in reduced vesicle density in axons. This is mechanistically about **axonal transport**, not vesicle targeting to the presynaptic active zone. The annotation to GO:0016080 is an overreach.

> Key quote: "PS1 mutations increase GSK3β activity, leading to hyperphosphorylation of kinesin light chains, reduced kinesin binding to membrane-bound organelles, and decreased vesicle/mitochondrial density in neuronal processes."

**GO:7770062:** Not appropriate — Psen1 is a γ-secretase/intramembrane protease, not a tethering factor.

---

### 9. SEPTIN5 / CDCrel-1 (UniProtKB:Q99719, human) — PMID:10321247 (TAS)

**Paper:** Beites CL et al. (1999). "The septin CDCrel-1 binds syntaxin and inhibits exocytosis." *Nat Neurosci* 2(5):434–439.

**Summary:** SEPTIN5/CDCrel-1 localizes to synaptic vesicles and directly binds syntaxin-1 (a t-SNARE). Overexpression inhibits regulated exocytosis; dominant-negative mutants enhance secretion. CDCrel-1 acts as a **negative regulator of SNARE-mediated vesicle fusion** at the synapse.

**Recommendation:** Replace GO:0016080 with **GO:0010807 regulation of synaptic vesicle priming** (BP)
or: **GO:0046597 negative regulation of viral entry into host cell** — no, wrong.
Better: **GO:1900242 negative regulation of synaptic vesicle endocytosis** — need to verify.
Most appropriate: **GO:0016079 synaptic vesicle exocytosis** with a negative regulation qualifier, i.e., **GO:0099514 negative regulation of presynaptic membrane neurotransmitter receptor levels** — no.

Best fit BP: **GO:0007269 neurotransmitter secretion** (negative regulator of), or more precisely a child of regulation of exocytosis.

**Reasoning:** The paper establishes CDCrel-1 as a negative regulator of exocytosis acting by blocking syntaxin availability for SNARE complex formation. This is regulation of the fusion step, not vesicle targeting or tethering.

> Key quote: "CDCrel-1... directly binds syntaxin (a SNARE protein). Overexpression of wild-type CDCrel-1 inhibits secretion; dominant-negative mutants enhance secretion."

**GO:7770062:** Not appropriate — SEPTIN5 inhibits exocytosis via SNARE interaction, it does not physically bridge vesicle to target membrane.

**Note on TAS evidence:** TAS (Traceable Author Statement) evidence should be verifiable from the cited paper. The annotation to "synaptic vesicle targeting" is not well-supported by the paper's actual finding (which is inhibition of exocytosis/fusion, not targeting).

---

### 10. Pclo / Aczonin (MGI:MGI:1349390, mouse) — PMID:10508862 (NAS)

**Paper:** Wang X et al. (1999). "Aczonin, a 550-kD putative scaffolding protein of presynaptic active zones, shares homology regions with Rim and Bassoon and binds profilin." *J Cell Biol* 147(1):151–162.

**Summary:** Aczonin (PCLO/Piccolo) is a ~550 kDa neuron-specific protein concentrated at presynaptic active zones. It contains zinc fingers, a PDZ domain, two C2 domains, and binds profilin (an actin dynamics regulator). Proposed as a **scaffolding protein** organizing active zone architecture.

**Recommendation:** Replace GO:0016080 with **GO:0097091 synaptic vesicle clustering** (BP)
or: **GO:0045202 synapse assembly** (BP)

**Reasoning:** Aczonin is a presynaptic active zone scaffold. Its function is to organize the structural framework of the active zone where vesicles dock, not to directly tether vesicles to the membrane. "Synaptic vesicle targeting" (GO:0016080) is an overly specific and arguably incorrect characterization. Scaffolding/organizing the active zone (which indirectly supports vesicle clustering) is better captured by synapse assembly or synaptic vesicle clustering terms.

> Key quote: "Proposed as a scaffolding protein organizing active zone architecture and facilitating neurotransmitter vesicle trafficking."

**GO:7770062:** Possibly applicable given C2 domains (which can bind membranes) and PDZ domain (which can bind SNARE proteins), but the paper does not provide evidence that Aczonin directly bridges vesicle-to-target membranes as a primary function. The evidence is NAS and the paper describes a scaffolding role.

---

### 11. Pclo / Piccolo (RGD:69406, rat) — PMID:10707984 (NAS)

**Paper:** Fenster SD et al. (2000). "Piccolo, a presynaptic zinc finger protein structurally related to bassoon." *Neuron* 25(1):203–214.

**Summary:** Piccolo is an active zone cytomatrix protein structurally related to Bassoon. Its zinc finger domains interact with PRA1 (a Rab-GDI displacement factor involved in Rab GTPase recycling). Proposed role in synaptic vesicle trafficking regulation via the Rab pathway.

**Recommendation:** Replace GO:0016080 with **GO:0097091 synaptic vesicle clustering** (BP)
(Same reasoning as Pclo/Aczonin above — these are the same gene/protein, just different species entries.)

**Additional note:** The PRA1 interaction suggests a link to Rab GTPase regulation (GO:0031624 ubiquitin conjugating enzyme activity — no). Perhaps **GO:0099025 vesicle tethering** if such a BP term exists, otherwise GO:0097091 or GO:0045202.

**GO:7770062:** Same as above — insufficient evidence from this paper for direct membrane-bridging tethering activity.

---

### 12. Nlgn1 / Neuroligin-1 (MGI:MGI:2179435, mouse) — PMID:10892652 (IMP)

**Paper:** Scheiffele P et al. (2000). "Neuroligin expressed in nonneuronal cells triggers presynaptic development in contacting axons." *Cell* 101(6):657–669.

**Summary:** Neuroligin-1 and -2 are postsynaptic cell-adhesion molecules that, when expressed in non-neuronal cells, trigger de novo presynaptic differentiation in contacting axons, including SV clustering. The effect involves trans-synaptic interaction with β-neurexin on the presynaptic side.

**Recommendation:** Replace GO:0016080 with **GO:0007416 synapse assembly** (BP)

**Reasoning:** Neuroligin-1 is a **postsynaptic** cell-adhesion molecule that acts as a trans-synaptic organizer, inducing presynaptic differentiation via neurexin. The "synaptic vesicle targeting" annotation confuses a postsynaptic organizer with a presynaptic tethering factor. The actual function demonstrated in the paper is induction of presynaptic assembly/differentiation, which is synaptogenesis.

> Key quote: "Neuroligin-1 and -2, postsynaptic cell-adhesion proteins, trigger de novo presynaptic differentiation in contacting axons when expressed in non-neuronal cells."

**GO:7770062:** Not appropriate — Neuroligin-1 is a postsynaptic adhesion protein, not a vesicle tethering factor. It does not physically bridge vesicle to target membrane.

---

### 13. Scrib / Scribble (MGI:MGI:2145950, mouse) — PMID:19458197 (IMP)

**Paper:** Sun Y et al. (2009). "Scribble interacts with beta-catenin to localize synaptic vesicles to synapses." *Mol Biol Cell* 20(14):3390–3400.

**Summary:** Scribble interacts with the cadherin–β-catenin complex at synapses. RNAi knockdown causes diffuse SV distribution along axons and reduced vesicle recycling, without affecting synapse number or active zone protein (Bassoon) distribution. Scribble acts downstream of β-catenin to **cluster SVs at presynaptic sites**.

**Recommendation:** Replace GO:0016080 with **GO:0097091 synaptic vesicle clustering** (BP)

**Reasoning:** The paper explicitly shows that Scribble loss causes "diffuse distribution of synaptic vesicles along the axon" — a failure of SV clustering at presynaptic sites. The title itself says "localize synaptic vesicles to synapses." This is synaptic vesicle clustering (GO:0097091), not the broader and less specific GO:0016080.

> Key quotes:
> - "scribble is important for the clustering of synaptic vesicles at synapses"
> - "in scribble knockdown cells, there is a diffuse distribution of synaptic vesicles along the axon"
> - "scribble functions downstream of β-catenin to cluster synaptic vesicles at developing synapses"

**GO:7770062:** Not strongly supported — Scribble is a scaffold/adaptor (LAP family, LRR + PDZ domains) that recruits SVs via the cadherin complex, but the paper does not show it physically bridges the vesicle membrane to the plasma membrane as a primary activity. GO:0097091 (BP) is more accurate and better supported by the experimental data.

---

### 14. mec-15 (WB:WBGene00003177, C. elegans) — PMID:23527112 (IMP)

**Paper:** Sun Y et al. (2013). "The F-box protein MEC-15 (FBXW9) promotes synaptic transmission in GABAergic motor neurons in C. elegans." *PLoS One* 8(3):e59132.

**Summary:** MEC-15 is an F-box/WD40 protein (substrate adaptor for SCF ubiquitin ligase). Loss of mec-15 specifically impairs GABAergic but not cholinergic transmission. The SV protein SNB-1 (synaptobrevin) accumulates in cell bodies and is depleted at synapses in mec-15 mutants, implicating MEC-15 in ubiquitin-mediated control of synaptic vesicle protein trafficking.

**Recommendation:** Replace GO:0016080 with **GO:0048489 synaptic vesicle transport** (BP)
or more specifically: **GO:0099641 anterograde axonal protein transport** if supported, or **GO:0006511 ubiquitin-dependent protein catabolic process** if the mechanism is degradation-based.

**Reasoning:** MEC-15 promotes the trafficking of SV proteins (SNB-1) to synapses. The phenotype is mislocalization of SV proteins (accumulation in cell bodies, depletion at synapses), which reflects a failure in anterograde transport or delivery of SV components. This is more accurately captured by synaptic vesicle transport terms than "synaptic vesicle targeting."

> Key quote: "The synaptic vesicle protein SNB-1 (synaptobrevin) accumulates in cell bodies and is depleted at synapses in mec-15 mutants, implicating MEC-15 in controlling synaptic protein trafficking/abundance."

**GO:7770062:** Not appropriate — MEC-15 is an E3 ubiquitin ligase adaptor, not a membrane tethering factor.

---

## Summary table

| Gene | Taxon | PMID | Ev | Current | Recommended replacement | GO:7770062? |
|------|-------|------|----|---------|------------------------|-------------|
| Exo84 | fly | 10798391 | NAS | GO:0016080 | GO:0006904 vesicle docking involved in exocytosis (BP) | No — BP only |
| CASK | fly | 10798391 | NAS | GO:0016080 | GO:0007416 synapse assembly (BP) | No |
| Sec10 | fly | 10798391 | NAS | GO:0016080 | GO:0006904 vesicle docking involved in exocytosis (BP) | No — BP only |
| Sec8 | fly | 10798391 | NAS | GO:0016080 | GO:0006904 vesicle docking involved in exocytosis (BP) | No — BP only |
| Sec6 | fly | 10798391 | NAS | GO:0016080 | GO:0006904 vesicle docking involved in exocytosis (BP) | No — BP only |
| Sec5 | fly | 10798391 | NAS | GO:0016080 | GO:0006904 vesicle docking involved in exocytosis (BP) | No — BP only |
| Exo70 | fly | 10798391 | NAS | GO:0016080 | GO:0006904 vesicle docking involved in exocytosis (BP) | No — BP only |
| Psen1 | mouse | 12805290 | IMP | GO:0016080 | GO:0048489 synaptic vesicle transport (BP) | No |
| SEPTIN5 | human | 10321247 | TAS | GO:0016080 | Negative regulation of exocytosis BP term (verify) | No |
| Pclo | mouse | 10508862 | NAS | GO:0016080 | GO:0097091 synaptic vesicle clustering (BP) | Marginal |
| Pclo | rat | 10707984 | NAS | GO:0016080 | GO:0097091 synaptic vesicle clustering (BP) | Marginal |
| Nlgn1 | mouse | 10892652 | IMP | GO:0016080 | GO:0007416 synapse assembly (BP) | No |
| Scrib | mouse | 19458197 | IMP | GO:0016080 | GO:0097091 synaptic vesicle clustering (BP) | No |
| mec-15 | worm | 23527112 | IMP | GO:0016080 | GO:0048489 synaptic vesicle transport (BP) | No |

## Notes

- All GO term IDs for suggested replacements should be verified via OLS/QuickGO before implementing.
- Exocyst subunits (Sec5, Sec6, Sec8, Sec10, Exo70, Exo84) are the clearest candidates for GO:7770062 given their well-established role as a vesicle tethering complex.
- NAS annotations (from PMID:10798391 bioinformatics screen) should ideally be backed by experimental references for the new annotations.
- CASK: requires more research; synapse assembly is a conservative placeholder.
- SEPTIN5: need to verify exact GO ID for negative regulation of synaptic vesicle exocytosis/priming.
