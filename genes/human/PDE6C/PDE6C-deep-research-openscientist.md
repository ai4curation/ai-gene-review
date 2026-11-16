---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T04:57:08.891472'
end_time: '2026-11-14T05:13:24.400836'
duration_seconds: 975.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PDE6C
  gene_symbol: PDE6C
  uniprot_accession: P51160
  protein_description: 'RecName: Full=Cone cGMP-specific 3'',5''-cyclic phosphodiesterase
    subunit alpha''; EC=3.1.4.35 {ECO:0000269|PubMed:21127010, ECO:0000269|PubMed:28583373};
    AltName: Full=cGMP phosphodiesterase 6C; Flags: Precursor;'
  gene_info: Name=PDE6C {ECO:0000312|HGNC:HGNC:8787}; Synonyms=PDEA2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the cyclic nucleotide phosphodiesterase family.
  protein_domains: GAF. (IPR003018); GAF-like_dom_sf. (IPR029016); HD/PDEase_dom.
    (IPR003607); PDEase. (IPR023088); PDEase_catalytic_dom. (IPR002073)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PDE6C-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PDE6C-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P51160
- **Protein Description:** RecName: Full=Cone cGMP-specific 3',5'-cyclic phosphodiesterase subunit alpha'; EC=3.1.4.35 {ECO:0000269|PubMed:21127010, ECO:0000269|PubMed:28583373}; AltName: Full=cGMP phosphodiesterase 6C; Flags: Precursor;
- **Gene Information:** Name=PDE6C {ECO:0000312|HGNC:HGNC:8787}; Synonyms=PDEA2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the cyclic nucleotide phosphodiesterase family.
- **Key Domains:** GAF. (IPR003018); GAF-like_dom_sf. (IPR029016); HD/PDEase_dom. (IPR003607); PDEase. (IPR023088); PDEase_catalytic_dom. (IPR002073)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PDE6C" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PDE6C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PDE6C** (gene ID: PDE6C, UniProt: P51160) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PDE6C (UniProt P51160): The Cone cGMP-Phosphodiesterase α′ Catalytic Subunit — Functional Annotation Report

**Gene:** PDE6C (HGNC:8787; synonym PDEA2) · **Protein:** Cone cGMP-specific 3′,5′-cyclic phosphodiesterase subunit α′ · **EC:** 3.1.4.35 · **Organism:** *Homo sapiens* · **Family:** Class I cyclic-nucleotide phosphodiesterase, PDE6 subfamily · **Domains:** Two tandem N-terminal regulatory GAF domains (GAF-A/GAF-B) + C-terminal HD/PDEase catalytic domain; C-terminal CaaX prenylation motif.

---

## Summary

**PDE6C encodes the cone-specific α′ (alpha-prime) catalytic subunit of photoreceptor cyclic-GMP phosphodiesterase (PDE6; EC 3.1.4.35), the effector enzyme of the cone phototransduction cascade.** Its primary biochemical function is the hydrolysis of the intracellular second messenger 3′,5′-cyclic GMP (cGMP) to 5′-GMP. This is a high-turnover reaction — recombinant PDE6C hydrolyzes cGMP with a Michaelis constant (Km) of ~20–23 µM and a catalytic rate constant (kcat) of ~4,200–5,100 s⁻¹ — making PDE6C one of the fastest cyclic-nucleotide phosphodiesterases known. In cone photoreceptors the active enzyme is a catalytic homodimer of two PDE6C subunits held in check by two inhibitory Pγ (PDE6H) subunits, a composition that distinguishes it from the rod enzyme, which is the PDE6A/PDE6B catalytic heterodimer regulated by PDE6G.

PDE6C performs its function at a very specific subcellular location: the **disc-membrane surface of the cone outer segment**, where it is anchored by C-terminal prenylation (isoprenylation of a CaaX motif). Here it sits at the heart of the cone phototransduction G-protein cascade. Upon absorption of light by cone opsin, cone transducin (Gαt2·GTP) is activated and relieves the inhibitory Pγ subunit's block of the PDE6C catalytic pocket. PDE6C then rapidly hydrolyzes cytoplasmic cGMP, lowering cGMP concentration, closing cyclic-nucleotide-gated (CNG) channels, reducing the inward Na⁺/Ca²⁺ dark current, and hyperpolarizing the cone. This is the molecular event that converts a photon signal into an electrical response, enabling daylight (photopic) and color vision.

The non-redundant, cone-specific importance of PDE6C is established by convergent genetics across three species. In humans, biallelic loss-of-function mutations cause **achromatopsia (ACHM5) and early-onset/progressive cone dystrophy**. A naturally occurring rhesus macaque model carrying a homozygous catalytic-domain mutation (R565Q) produces a correctly localized but catalytically dead enzyme and recapitulates human achromatopsia. The spontaneous *cpfl1* mouse carries a cone-specific *Pde6c* loss-of-function allele that abolishes cone electroretinogram responses while leaving rod responses intact. Together, these data pinpoint **cGMP hydrolysis by PDE6C as the essential, cone-dedicated effector step of photopic phototransduction.**

---

## Gene/Protein Identity Verification

As mandated, the research target was verified against the UniProt record before and throughout the investigation. All retrieved literature is consistent with the target protein — there is **no ambiguity**.

| Attribute | UniProt P51160 | Literature consistency |
|---|---|---|
| Gene symbol | PDE6C (synonym PDEA2) | Confirmed — all papers reference cone PDE6 / PDE6C |
| Protein | Cone cGMP-specific 3′,5′-cyclic phosphodiesterase subunit α′ | Confirmed |
| EC number | 3.1.4.35 | Confirmed (cGMP → 5′-GMP) |
| Organism | *Homo sapiens* (human); orthologs in macaque, mouse | Confirmed |
| Family | Cyclic nucleotide phosphodiesterase family | Confirmed |
| Key domains | GAF (IPR003018), GAF-like (IPR029016), HD/PDEase (IPR003607), PDEase (IPR023088), PDEase catalytic (IPR002073) | Confirmed — tandem regulatory GAF domains + C-terminal HD/PDEase catalytic domain |

The gene symbol, organism, protein family, and domain architecture are fully concordant with the primary literature. This is a well-characterized human vision gene. No research was conducted on any other gene.

---

## Key Findings

### Finding 1 — PDE6C is the cone cGMP-PDE α′ catalytic subunit and the effector enzyme of cone phototransduction

PDE6C encodes the cone-specific α′ catalytic subunit of cyclic-GMP phosphodiesterase (PDE6), the enzyme that converts cGMP to 5′-GMP, and it is the effector enzyme of the vertebrate cone phototransduction cascade. In the cone, the functional PDE6 holoenzyme is a **catalytic homodimer of two PDE6C subunits** associated with two inhibitory Pγ subunits (the product of PDE6H) — distinct from the rod enzyme, a **PDE6A/PDE6B catalytic heterodimer** regulated by the PDE6G inhibitory subunit.

The direct evidence is unambiguous. [PMID: 19615668](https://pubmed.ncbi.nlm.nih.gov/19615668/) states that "the PDE6C gene encodes the cone alpha subunit of cyclic guanosine monophosphate (cGMP) phosphodiesterase, which converts cGMP to 5′-GMP, and thereby plays an essential role in cone phototransduction." The subunit partitioning between rods and cones was crisply summarized by [PMID: 27296292](https://pubmed.ncbi.nlm.nih.gov/27296292/): "PDE6A and PDE6B code for the catalytic and PDE6G the inhibitory subunits in rods while PDE6C codes for the catalytic and PDE6H the inhibitory subunits in cones." The enzyme's status as the cone cascade's terminal effector is reinforced by cryo-EM work ([PMID: 39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/)): "Cone cGMP-phosphodiesterase (PDE6) is the key effector enzyme for daylight vision." **PDE6C is thus an enzyme — a cGMP-hydrolyzing phosphodiesterase — and the molecular switch that terminates the cone's dark state in response to light.**

### Finding 2 — PDE6C is a high-turnover cGMP hydrolase activated by cone transducin and inhibited by Pγ

Enzymatic characterization of recombinant PDE6C defines its catalytic parameters precisely. [PMID: 20940301](https://pubmed.ncbi.nlm.nih.gov/20940301/) reports that PDE6C and chimeric PDE6C-A/PDE6C-B constructs "hydrolyzed cGMP with similar K(m) (20-23 μM) and k(cat) (4200-5100 s⁻¹) values." These numbers mark PDE6C as a remarkably fast enzyme, consistent with its role in rapidly collapsing cytoplasmic cGMP during the light response. Its **substrate specificity is for cGMP** (the physiological cyclic-nucleotide second messenger of phototransduction), yielding 5′-GMP as product. Hydrolysis occurs at the C-terminal HD/PDEase catalytic domain using the bimetal active-site chemistry typical of class I PDEs.

PDE6C catalytic activity is gated by two upstream regulators. First, it is activated by the photoreceptor G protein transducin-α: the same study found that "recombinant cone transducin-α (Gα(t2)) and native rod Gα(t1) fully and potently activated PDE6C." Comparative data show PDE6C is activated at markedly lower Gαt concentrations than rod PDE6 requires, indicating distinct transducin-coupling and higher intrinsic activity. Second, PDE6C is held inactive in darkness by its inhibitory γ-subunit (Pγ). Cryo-EM ([PMID: 39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/)) revealed "the dynamic nature of PDE6C association with its regulatory γ-subunit (Pγ) which allows openings of the catalytic pocket in the absence of phototransduction signaling, thereby controlling photoreceptor noise and sensitivity." This dynamic, partly-leaky inhibition sets the basal (dark) PDE activity that calibrates cone sensitivity and noise.

Functional corroboration comes from a transgenic swap ([PMID: 26085644](https://pubmed.ncbi.nlm.nih.gov/26085644/)) in which cone PDE6C was expressed in rods lacking rod PDE6. The substituted rods acquired "light-adapted" characteristics — higher basal PDE activity, faster deactivation, reduced dark current and sensitivity, and faster response kinetics — demonstrating that intrinsic PDE6C properties (higher spontaneous activity and faster shut-off) contribute mechanistically to the faster, less sensitive responses that distinguish cones from rods.

### Finding 3 — PDE6C localizes to photoreceptor outer-segment disc membranes via C-terminal prenylation

PDE6C performs its function on membranes, not free in the cytosol. The catalytic subunits are targeted to the photoreceptor outer segment and concentrated at the disc rims. [PMID: 20940301](https://pubmed.ncbi.nlm.nih.gov/20940301/) showed by EGFP-fusion imaging that "EGFP-PDE6C-A and EGFP-PDE6C-B were targeted to the rod outer segments and concentrated at the disc rims," confirming the outer-segment disc-membrane localization expected for a phototransduction effector and placing the enzyme alongside transducin and the CNG channels.

Membrane anchoring is achieved by lipidation. [PMID: 15504722](https://pubmed.ncbi.nlm.nih.gov/15504722/) established that "membrane binding is a consequence of prenylation of PDE6 catalytic subunits, whereas soluble PDE6 is purified with a 17-kDa prenyl-binding protein (PDEdelta) tightly bound." The C-terminal CaaX motif of PDE6C is isoprenylated, tethering the enzyme to the disc membrane where its substrate cGMP and its activator transducin are concentrated. The prenyl-binding protein PrBP/δ (PDE6D) can shield the prenyl group and solubilize PDE6, providing a mechanism for trafficking and for modulating the enzyme's availability to transducin. In domain terms, PDE6C carries — in addition to the C-terminal catalytic domain — noncatalytic cGMP-binding GAF domains (GAF-A/GAF-B) in its N-terminal regulatory region (see Finding 6).

### Finding 4 — Loss of PDE6C catalytic function causes achromatopsia and progressive cone dystrophy, confirming a non-redundant role in cones

The physiological necessity of PDE6C is demonstrated by human and primate genetics. Biallelic PDE6C mutations cause autosomal-recessive cone photoreceptor disorders: early-onset cone dystrophy and complete/incomplete achromatopsia (ACHM5). Through homozygosity mapping, [PMID: 19615668](https://pubmed.ncbi.nlm.nih.gov/19615668/) found that "sequence analysis of 104 probands with arCD and 10 probands with ACHM revealed compound heterozygous PDE6C mutations in three complete ACHM patients," establishing PDE6C as a *bona fide* achromatopsia gene.

The most mechanistically informative evidence comes from a naturally occurring nonhuman-primate model. [PMID: 30667376](https://pubmed.ncbi.nlm.nih.gov/30667376/) describes "a homozygous R565Q missense mutation in the catalytic domain of PDE6C, a cone-specific phototransduction enzyme associated with achromatopsia in humans." Critically, the mutant "mRNA is translated into a stable protein that displays normal cellular localization but is unable to hydrolyze cyclic GMP (cGMP)." Because the protein is stably expressed and correctly trafficked yet disease still results, **the defect is specifically loss of catalytic activity — isolating cGMP hydrolysis as the essential, non-replaceable function of PDE6C.** Detailed phenotyping of this primate colony ([PMID: 39641747](https://pubmed.ncbi.nlm.nih.gov/39641747/)) found absent cone ERG responses from as early as 3 months postnatally and slow cone degeneration with aging, while heterozygotes were indistinguishable from wild type — matching recessive human disease. PDE6C is a recurrent causative gene in achromatopsia cohorts worldwide, including as a leading gene among Japanese ACHM families ([PMID: 39287548](https://pubmed.ncbi.nlm.nih.gov/39287548/), [PMID: 41666299](https://pubmed.ncbi.nlm.nih.gov/41666299/)) and across consanguineous/multiethnic cohorts ([PMID: 39024658](https://pubmed.ncbi.nlm.nih.gov/39024658/), [PMID: 42099125](https://pubmed.ncbi.nlm.nih.gov/42099125/)).

### Finding 5 — The *cpfl1* mouse confirms PDE6C function is cone-specific and non-redundant with rod PDE6

A third, independent genetic line comes from the mouse. The spontaneously arising *cpfl1* mouse carries a loss-of-function mutation in the cone-specific *Pde6c* gene. [PMID: 20467778](https://pubmed.ncbi.nlm.nih.gov/20467778/) reports that "the cpfl1-mouse is a naturally arising mouse mutant with a loss-of-function mutation in the cone-specific Pde6c gene. Cpfl1-mice displayed normal rod-specific light responses while cone-specific responses were strongly diminished," followed by progressive cone degeneration accompanied by Müller-glia gliosis and STAT3/LIF survival signaling.

The key inference is that **rod PDE6 (PDE6A/PDE6B) cannot compensate for loss of cone PDE6C in cones, and vice versa** — the two catalytic paralogs are functionally partitioned to their respective photoreceptor types. Intact rod function with selectively abolished cone function in *cpfl1* mice parallels the human and primate phenotypes exactly, establishing a robust cross-species consensus. The *Pde6c* mouse has since become a workhorse model for cone dystrophy, used to study compensatory cone mechanisms ([PMID: 37440055](https://pubmed.ncbi.nlm.nih.gov/37440055/)) and epigenetic survival responses ([PMID: 35810394](https://pubmed.ncbi.nlm.nih.gov/35810394/)).

### Finding 6 — PDE6C regulatory GAF domains bind cGMP at noncatalytic sites and allosterically couple to Pγ inhibition

Beyond the catalytic site, PDE6C has a sophisticated allosteric regulatory layer. The N-terminal regulatory region contains tandem GAF domains (GAF-A/GAF-B) that bind cGMP at **noncatalytic sites** — distinct from the C-terminal catalytic site where cGMP is hydrolyzed. The inhibitory Pγ subunit binds the GAF region, and the strength of the Pγ–GAF interaction is reported through allosteric changes in cGMP binding to these noncatalytic sites.

This coupling, part of the PDE6-family regulatory logic, was demonstrated in work on the homologous rod enzyme: [PMID: 11741972](https://pubmed.ncbi.nlm.nih.gov/11741972/) found that "the strength of Pgamma interaction with the regulatory GAF domain of PDE6 was reduced severalfold upon Pgamma phosphorylation at Thr(22) (but not Thr(35)), as judged by allosteric changes in cGMP binding to these noncatalytic sites on the enzyme." Chemical cross-linking and quantitative mass spectrometry have further mapped how Pγ allosterically regulates the holoenzyme ([PMID: 31394113](https://pubmed.ncbi.nlm.nih.gov/31394113/)). Thus PDE6C is **bifunctional toward cGMP** — hydrolyzing it catalytically and sensing it allosterically.

Cone-specific structural adaptation of this system was revealed by cryo-EM of human holoPDE6C ([PMID: 39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/)), which identified "evolutionarily recent adaptations of PDE6C stemming from residue substitutions in the Pγ subunit and the noncatalytic cGMP binding site and influencing the Pγ dynamics in holoPDE6C." The GAF/noncatalytic-cGMP/Pγ triad is not merely inherited from the ancestral PDE — it has been fine-tuned in the cone enzyme to tune Pγ dynamics for fast, noise-tolerant photopic signaling.

### Finding 7 — PDE6C arose during vertebrate 2R genome duplications and is the cone-dedicated paralog of the PDE6 family

Evolutionary analysis explains why a dedicated cone PDE catalytic gene exists. Phylogenetic and comparative-synteny analyses show that the PDE6 catalytic gene family expanded from a single ancestral gene to three members (PDE6A, PDE6B, PDE6C) during the two rounds of whole-genome duplication (2R) at the base of vertebrate evolution. [PMID: 27296292](https://pubmed.ncbi.nlm.nih.gov/27296292/) states that "both gene families expanded from one to three members in the two rounds of genome doubling (2R) that occurred at the base of vertebrate evolution." The inhibitory-subunit family (including PDE6G and PDE6H) is vertebrate-specific, co-evolving with the catalytic subunits.

The resulting division of labor is clean: rods express catalytic PDE6A/PDE6B plus inhibitory PDE6G, while cones express catalytic PDE6C plus inhibitory PDE6H. PDE6C is therefore the **cone-dedicated catalytic paralog**, and its lineage-specific refinements continue into recent evolution. The cryo-EM study ([PMID: 39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/)) concludes that "our structural analysis sheds light on the previously unrecognized molecular evolution of the effector enzyme in cones that advances adaptation for photopic vision," linking PDE6C-specific substitutions directly to the functional specialization of daylight vision.

### Finding 8 — PDE6C operates as the central effector of the cone phototransduction cascade, controlling cytoplasmic cGMP/Ca²⁺ homeostasis

Integrating the above, PDE6C is the pivotal node that converts a light-triggered G-protein signal into a change in the cone's cytoplasmic second-messenger state. In the cone outer segment, light-activated cone opsin activates cone transducin (Gαt2·GTP), which relieves Pγ inhibition of PDE6C. Activated PDE6C rapidly hydrolyzes cGMP, lowering cytoplasmic cGMP, closing CNG channels, reducing the inward Na⁺/Ca²⁺ dark current, and hyperpolarizing the cone. Recovery to the dark state requires guanylate cyclase to resynthesize cGMP under Ca²⁺-dependent (GCAP) feedback control.

The review literature frames this as a tightly coupled homeostatic system. [PMID: 42106180](https://pubmed.ncbi.nlm.nih.gov/42106180/) notes that the phototransduction "machinery controls the homeostasis and mutual dependence of two cytoplasmic messengers, cGMP and Ca[²⁺]." Cone-versus-rod differences are attributable largely to the kinetic parameters set by the effector PDE: [PMID: 38709779](https://pubmed.ncbi.nlm.nih.gov/38709779/) identifies that "the most important differences in their light responses are likely to be differences in amplification of the G-protein cascade, different decay rates of phosphodiesterase (PDE) and pigment phosphorylation, and different rates of turnover of cGMP in darkness." Because the PDE decay rate and dark cGMP turnover in cones are properties of PDE6C, **PDE6C is a principal molecular determinant of the speed and reduced sensitivity that define cone (photopic) vision.**

---

## Mechanistic Model / Interpretation

PDE6C is best understood as the **signal-terminating effector enzyme** of the cone phototransduction cascade — the step that physically translates "a photon was captured" into "the membrane potential changed." The cascade and PDE6C's place in it:

```
   LIGHT (photon)
        │
        ▼
   Cone opsin (R*)  ── photoisomerization of 11-cis retinal
        │
        ▼
   Cone transducin  Gαt2·GDP → Gαt2·GTP   (G-protein activation, amplification)
        │
        ▼
   ┌─────────────────────────────────────────────────────┐
   │  PDE6C HOLOENZYME  (disc membrane, prenyl-anchored)   │
   │                                                       │
   │   (PDE6C)₂ catalytic homodimer  + 2× Pγ (PDE6H)       │
   │                                                       │
   │   Gαt2·GTP displaces Pγ  ⇒  catalytic pocket OPENS     │
   │                                                       │
   │   cGMP  ──(EC 3.1.4.35)──►  5′-GMP                     │
   │   Km ≈ 20–23 µM     kcat ≈ 4,200–5,100 s⁻¹            │
   └─────────────────────────────────────────────────────┘
        │
        ▼
   [cGMP]cytoplasm  ↓↓
        │
        ▼
   CNG channels CLOSE  ⇒  Na⁺/Ca²⁺ inward dark current ↓
        │
        ▼
   Cone HYPERPOLARIZES  ⇒  neural signal (photopic / color vision)

   RECOVERY:  transducin GTP hydrolysis + Pγ re-inhibition turn PDE6C off;
              guanylate cyclase (Ca²⁺/GCAP feedback) resynthesizes cGMP → dark state
```

Three control layers make PDE6C a precisely tunable switch rather than a simple on/off enzyme:

1. **Transducin activation** (the "on" input) — Gαt2·GTP physically relieves Pγ inhibition.
2. **Pγ inhibition** (the dark "off" clamp) — but dynamic: the catalytic pocket transiently opens even without signaling, setting basal dark activity that calibrates sensitivity and noise.
3. **GAF/noncatalytic cGMP allostery** — tandem GAF domains bind cGMP at noncatalytic sites and allosterically modulate Pγ affinity, integrating the enzyme's own substrate state into its regulation.

The following table consolidates how PDE6C contrasts with its rod counterpart, clarifying its specialization:

| Property | Cone enzyme (PDE6C) | Rod enzyme (PDE6A/B) |
|---|---|---|
| Catalytic subunit(s) | PDE6C homodimer (α′α′) | PDE6A + PDE6B heterodimer (αβ) |
| Inhibitory subunit | Pγ = PDE6H | Pγ = PDE6G |
| Reaction | cGMP → 5′-GMP (EC 3.1.4.35) | cGMP → 5′-GMP (EC 3.1.4.35) |
| Km (cGMP) | ~20–23 µM | comparable |
| kcat | ~4,200–5,100 s⁻¹ | comparable |
| Transducin sensitivity | Activated at low Gαt (high intrinsic activity) | Requires higher Gαt |
| Basal (dark) activity | Higher; faster deactivation | Lower |
| Localization | Cone outer-segment disc membranes (prenyl-anchored) | Rod outer-segment disc membranes |
| Evolutionary origin | 2R vertebrate genome duplication; cone-dedicated | 2R vertebrate genome duplication; rod-dedicated |
| Disease (biallelic LOF) | Achromatopsia / cone dystrophy (ACHM5) | Rod-related retinal degeneration |

**Primary function answer (enzyme framing):** PDE6C catalyzes the hydrolysis of 3′,5′-cyclic GMP to 5′-GMP (EC 3.1.4.35), with substrate specificity for cGMP, acting as a high-turnover effector activated by cone transducin and inhibited by the Pγ (PDE6H) subunit. It carries out this function **at the disc membranes of cone outer segments**, anchored by prenylation, within the **cone phototransduction signaling pathway**, where its hydrolysis of cGMP closes CNG channels and hyperpolarizes the cone.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [19615668](https://pubmed.ncbi.nlm.nih.gov/19615668/) | PDE6C mutations in cone disorders | PDE6C encodes the cone α subunit converting cGMP→5′-GMP; biallelic mutations in complete ACHM — Findings 1 & 4 |
| [20940301](https://pubmed.ncbi.nlm.nih.gov/20940301/) | Rod PDE6A/PDE6B enzymatically equivalent | Km/kcat for PDE6C; transducin-α activation; disc-rim localization — Findings 2 & 3 |
| [15504722](https://pubmed.ncbi.nlm.nih.gov/15504722/) | 17-kDa prenyl-binding protein | Prenylation mediates PDE6 membrane binding; PrBP/δ binds prenyl group — Finding 3 |
| [30667376](https://pubmed.ncbi.nlm.nih.gov/30667376/) | NHP model of inherited retinal disease | R565Q = stable, correctly localized, catalytically dead PDE6C causing achromatopsia — isolates catalysis (Finding 4) |
| [39641747](https://pubmed.ncbi.nlm.nih.gov/39641747/) | Onset/progression in NHP PDE6C disorder | Absent cone ERG from infancy; slow degeneration; recessive — Finding 4 |
| [20467778](https://pubmed.ncbi.nlm.nih.gov/20467778/) | STAT3 genes in cpfl1 cones | cpfl1 Pde6c LOF abolishes cone but not rod responses — Finding 5 |
| [11741972](https://pubmed.ncbi.nlm.nih.gov/11741972/) | PDE6 regulation by Pγ phosphorylation | GAF noncatalytic cGMP sites allosterically couple to Pγ — Finding 6 |
| [31394113](https://pubmed.ncbi.nlm.nih.gov/31394113/) | Allosteric regulation of rod PDE6 (XL-MS) | Maps Pγ allosteric control of the holoenzyme — Finding 6 |
| [39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/) | Human cone PDE6 cryo-EM dynamics | Dynamic Pγ; noncatalytic cGMP site; cone-specific evolutionary adaptations — Findings 1, 2, 6, 7 |
| [27296292](https://pubmed.ncbi.nlm.nih.gov/27296292/) | Evolution/expression of PDE6 genes | Rod/cone subunit partitioning; 2R origin of PDE6A/B/C — Findings 1 & 7 |
| [26085644](https://pubmed.ncbi.nlm.nih.gov/26085644/) | Cone-for-rod PDE6 swap | PDE6C intrinsic properties drive cone-like, light-adapted responses — Findings 2 & 8 |
| [42106180](https://pubmed.ncbi.nlm.nih.gov/42106180/) | Phototransduction in rods and cones | Cascade controls cGMP/Ca²⁺ homeostasis — Finding 8 |
| [38709779](https://pubmed.ncbi.nlm.nih.gov/38709779/) | Rod–cone response differences | PDE decay rate and cGMP turnover set cone responses — Finding 8 |
| [39287548](https://pubmed.ncbi.nlm.nih.gov/39287548/), [41666299](https://pubmed.ncbi.nlm.nih.gov/41666299/), [39024658](https://pubmed.ncbi.nlm.nih.gov/39024658/), [42099125](https://pubmed.ncbi.nlm.nih.gov/42099125/) | ACHM cohort/genetics studies | PDE6C recurrent causative gene across populations — Finding 4 |

The evidence base is strong because it combines (a) **direct enzymology** on recombinant protein (Km, kcat, transducin activation), (b) **structural biology** (cryo-EM of the human holoenzyme), (c) **cross-species genetics** with convergent phenotypes (human, macaque, mouse), and (d) **precise mechanistic dissection** (the macaque R565Q mutant that separates stability/localization from catalysis). No retrieved paper challenges the core annotation; disagreements in the literature concern finer kinetic details and the relative contributions of pigment-level versus effector-level mechanisms to rod–cone differences, not PDE6C's identity or primary function.

---

## Limitations and Knowledge Gaps

1. **Human-native enzymology is partly inferred from heterologous and non-human systems.** Several quantitative parameters derive from recombinant/chimeric constructs and non-human orthologs (bovine, mouse, macaque). The 2025 human cone cryo-EM ([PMID: 39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/)) narrows but does not fully close the gap for native human cone holoenzyme kinetics.
2. **In-vivo stoichiometry and trafficking.** The cone holoenzyme is described as a PDE6C homodimer with two Pγ (PDE6H) subunits, but in-vivo PDE6C:PDE6H stoichiometry, assembly dynamics, and the role of PrBP/δ (PDE6D) in cone-specific trafficking are less characterized than in rods.
3. **Function of the noncatalytic cGMP-binding sites.** The GAF domains clearly bind cGMP allosterically, but the quantitative contribution of noncatalytic cGMP binding to steady-state signaling, adaptation, and noise remains incompletely resolved.
4. **Mechanism of cone degeneration.** Loss of PDE6C catalysis causes slow cone death across species. Whether degeneration is driven chiefly by chronically elevated cGMP/Ca²⁺ (CNG channels held open, Ca²⁺ overload) or by additional cone-specific mechanisms is not fully established from the retrieved evidence.
5. **Structural basis of transducin-mediated Pγ displacement** in cone (versus rod) PDE6 is still being resolved.
6. **Dark-noise origin.** Classic models attribute photoreceptor dark continuous noise to spontaneous PDE activation, but [PMID: 39656211](https://pubmed.ncbi.nlm.nih.gov/39656211/) argues much of this noise originates from the pigment itself. The precise contribution of PDE6C's dynamic Pγ "leak" versus pigment noise to cone dark noise is an open quantitative question.

---

## Proposed Follow-up Experiments / Actions

1. **Native human cone PDE6C enzymology.** Purify or reconstitute the authentic human cone holoenzyme (PDE6C₂·Pγ₂) and directly measure Km, kcat, transducin-activation EC₅₀, and basal activity, replacing rod-based or chimeric extrapolations.
2. **Structure–function of disease alleles.** Systematically express catalogued human ACHM/cone-dystrophy PDE6C variants (plus the macaque R565Q) in matched systems to classify each as catalytic-dead, misfolded, mislocalized, or regulation-defective — directly informing gene-therapy and base-editing eligibility (cf. ~80% HDR correction in ACHM iPSCs, [PMID: 42264060](https://pubmed.ncbi.nlm.nih.gov/42264060/)).
3. **Dissect the GAF/noncatalytic cGMP allostery in cones.** Use cone-specific cryo-EM (building on [PMID: 39739818](https://pubmed.ncbi.nlm.nih.gov/39739818/)) with cGMP-occupied and cGMP-free GAF states to quantify how noncatalytic cGMP binding modulates Pγ affinity and catalytic-pocket opening.
4. **In-vivo cGMP/Ca²⁺ imaging in PDE6C models.** Combine genetically encoded cGMP/Ca²⁺ sensors with the *Pde6c* (cpfl1) mouse and macaque models to test whether degeneration correlates with second-messenger dysregulation, and to time the therapeutic window (cf. slow degeneration in [PMID: 39641747](https://pubmed.ncbi.nlm.nih.gov/39641747/) and [PMID: 20574029](https://pubmed.ncbi.nlm.nih.gov/20574029/)).
5. **Rescue and kinetics validation.** Extend the cone-for-rod swap paradigm ([PMID: 26085644](https://pubmed.ncbi.nlm.nih.gov/26085644/)) with point-mutant PDE6C variants to map which residues confer cone-specific high basal activity and fast deactivation, defining the molecular determinants of photopic signaling speed.

---

## Conclusion

PDE6C (UniProt P51160) is unambiguously identified as the **cone-specific α′ catalytic subunit of photoreceptor cGMP phosphodiesterase (PDE6; EC 3.1.4.35)**. Its primary function is the high-turnover hydrolysis of the second messenger cGMP to 5′-GMP. It acts as the **effector enzyme of the cone phototransduction cascade** at the disc membranes of cone outer segments, where it is prenyl-anchored, activated by cone transducin (Gαt2), and inhibited by the Pγ (PDE6H) subunit through a dynamically regulated, GAF-domain-coupled allosteric system. By collapsing cytoplasmic cGMP to close CNG channels and hyperpolarize the cone, PDE6C enables daylight and color vision. Its cone-dedicated, non-redundant role — the product of vertebrate 2R genome duplication and continued molecular adaptation — is established by convergent human, nonhuman-primate, and mouse genetics, in which loss of its catalytic activity causes achromatopsia and progressive cone dystrophy.


## Artifacts

- [OpenScientist final report](PDE6C-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PDE6C-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19615668
2. PMID:27296292
3. PMID:39739818
4. PMID:20940301
5. PMID:26085644
6. PMID:15504722
7. PMID:30667376
8. PMID:39641747
9. PMID:39287548
10. PMID:41666299
11. PMID:39024658
12. PMID:42099125
13. PMID:20467778
14. PMID:37440055
15. PMID:35810394
16. PMID:11741972
17. PMID:31394113
18. PMID:42106180
19. PMID:38709779
20. PMID:39656211
21. PMID:42264060
22. PMID:20574029