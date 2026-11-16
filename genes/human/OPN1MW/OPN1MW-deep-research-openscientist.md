---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T04:21:57.747383'
end_time: '2026-11-14T04:39:14.413732'
duration_seconds: 1036.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: OPN1MW
  gene_symbol: OPN1MW
  uniprot_accession: P04001
  protein_description: 'RecName: Full=Medium-wave-sensitive opsin 1 {ECO:0000303|Ref.6};
    AltName: Full=Green cone photoreceptor pigment; AltName: Full=Green-sensitive
    opsin; Short=GOP;'
  gene_info: Name=OPN1MW {ECO:0000312|HGNC:HGNC:4206}; Synonyms=GCP;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 1 family. Opsin
  protein_domains: GPCR_opsins. (IPR050125); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM.
    (IPR017452); Opsin. (IPR001760); Opsin_red/grn. (IPR000378)
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
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: OPN1MW-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: OPN1MW-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P04001
- **Protein Description:** RecName: Full=Medium-wave-sensitive opsin 1 {ECO:0000303|Ref.6}; AltName: Full=Green cone photoreceptor pigment; AltName: Full=Green-sensitive opsin; Short=GOP;
- **Gene Information:** Name=OPN1MW {ECO:0000312|HGNC:HGNC:4206}; Synonyms=GCP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family. Opsin
- **Key Domains:** GPCR_opsins. (IPR050125); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Opsin. (IPR001760); Opsin_red/grn. (IPR000378)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "OPN1MW" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'OPN1MW' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **OPN1MW** (gene ID: OPN1MW, UniProt: P04001) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# OPN1MW (P04001): The Human Green Cone Opsin — A Functional Annotation Report

**Gene:** OPN1MW (HGNC:4206; synonym GCP) · **Protein:** Medium-wave-sensitive opsin 1 / green cone photoreceptor pigment · **UniProt:** P04001 (OPSG_HUMAN) · **Organism:** *Homo sapiens* · **Length:** 364 aa · **Family:** GPCR class A (rhodopsin) / opsin subfamily, LWS class.

---

## Summary

**OPN1MW encodes the human medium-wave-sensitive (green) cone photopigment, a light-activated G-protein-coupled receptor (GPCR) of the rhodopsin/opsin (class A) family.** Its gene product is a ~364-amino-acid, seven-transmembrane apoprotein (the "green cone opsin," also called green cone photoreceptor pigment, GOP/GCP) that becomes a functional photoreceptor only when it covalently binds the vitamin-A-derived chromophore **11-cis-retinal** via a protonated Schiff base at Lys312 in transmembrane helix 7, with **Glu129** in TM3 acting as the Schiff-base counterion. In this holoprotein form the pigment absorbs light maximally at λmax ≈ 530 nm (green). The identity, organism (*Homo sapiens*), GPCR/opsin family, and key domains stated in the UniProt target definition were all confirmed against primary literature — this report concerns the correct gene.

The protein's **primary molecular function is that of a light receptor and signal transducer**: absorption of a photon isomerizes the bound 11-cis-retinal to all-trans-retinal, which drives the opsin through a defined series of spectral intermediates to an active "Meta-II-like" state. The active receptor catalyzes GDP→GTP exchange on **cone transducin (Gαt2 / GNAT2)**, which activates cGMP phosphodiesterase (PDE6), lowering cytoplasmic cGMP, closing cyclic-nucleotide-gated (CNG) channels and hyperpolarizing the photoreceptor. This is the canonical **cone phototransduction cascade**, and OPN1MW is its initiating step in the medium-wavelength (M) cone. The cascade operates in the **outer-segment membrane** of M-cone photoreceptors, where the pigment and its downstream machinery are concentrated. Signaling is terminated by C-terminal phosphorylation (by GRK1/GRK7) followed by arrestin binding, with recovery supported by the RGS9 GTPase-activating complex.

Functionally, OPN1MW provides the **green channel of human trichromatic color vision**. It arose by a recent gene duplication of an ancestral X-linked long-wave opsin within the catarrhine (Old World primate) lineage, and it remains **96% identical to its red paralogue OPN1LW**, from which it differs chiefly by a handful of spectral-tuning residues that shift λmax by ~30 nm. The two genes lie head-to-tail in a tandem array on Xq28, an arrangement that both underlies red–green color vision and predisposes the locus to the unequal recombination and splicing defects that cause the common red–green color-vision deficiencies and blue cone monochromacy. The precision of this human genetic evidence — natural mutagenesis mapping exactly which residues and regulatory elements are required — makes OPN1MW one of the most thoroughly validated GPCRs in terms of genotype-to-function mapping.

---

## Key Findings

### Finding 1 — OPN1MW is the human green (M) cone photopigment, a light-activated GPCR

OPN1MW (UniProt **P04001**) encodes one of the three human cone/rod-related light-sensitive pigment apoproteins. The classic cloning and sequencing of the human color-vision pigment genes established that the deduced amino-acid sequences share **41 ± 1% identity with rhodopsin**, placing the green pigment unambiguously in the rhodopsin/opsin branch of the class-A GPCR superfamily, and that the **red and green pigments are 96% mutually identical** but only ~43% identical to the blue pigment ([PMID: 2937147](https://pubmed.ncbi.nlm.nih.gov/2937147/)). The apoprotein (~364 aa, seven transmembrane helices) is non-functional on its own; it becomes a holoreceptor only upon covalent attachment of an **11-cis-retinal chromophore** within a transmembrane chromophore-binding pocket. Spectral tuning of visual pigments is understood to involve modulation of the physical properties of the **11-cis-retinylidene protonated Schiff base (PSB)** by side chains in and around that pocket ([PMID: 10614049](https://pubmed.ncbi.nlm.nih.gov/10614049/)). Light absorption isomerizes the retinal, converting the receptor to its active conformation. The maximal absorbance of the green pigment is λmax ≈ 530 nm, defining it as the medium-wavelength (green) sensor of the retina.

This finding confirms the UniProt target description: gene symbol OPN1MW matches "medium-wave-sensitive opsin 1 / green cone photoreceptor pigment," the organism is human, and the GPCR/opsin family and key opsin domains are all corroborated by primary literature.

### Finding 2 — OPN1MW initiates the cone phototransduction cascade in the M-cone outer segment

The green pigment carries out its function in the **disc/lamellar and plasma membranes of the outer segment (OS)** of the M (medium-wavelength) cone photoreceptor, where phototransduction proteins are concentrated. Photoactivation of the opsin, via 11-cis→all-trans retinal isomerization, triggers the vertebrate cone cascade: activated opsin catalyzes GDP/GTP exchange on cone transducin (Gαt2/GNAT2), which activates cGMP phosphodiesterase, lowering cytoplasmic cGMP, closing CNG channels, and hyperpolarizing the cell. Recovery is governed by cGMP/Ca²⁺ homeostasis and the RGS9 GAP complex. A review of rod and cone phototransduction describes exactly this machinery: "A protein machinery in rod and cone cells underlying the light response mediates photoexcitation, the return to the dark state, and adaptation processes. The machinery controls the homeostasis and mutual dependence of two cytoplasmic messengers, cGMP and Ca²⁺" ([PMID: 42106180](https://pubmed.ncbi.nlm.nih.gov/42106180/)).

Two localization facts anchor where the pigment acts. First, 11-cis-retinal is not only the molecular switch but also a chaperone for correct opsin trafficking: it "functions not only as a molecular switch for activating cone and rod visual pigments in response to light stimulation, but also as a chaperone for normal trafficking of cone opsins to the outer segments" ([PMID: 27225770](https://pubmed.ncbi.nlm.nih.gov/27225770/)). Second, cone outer-segment biogenesis is itself driven by opsin-laden membrane: "in cones, OS formation is initiated by the growth of opsin-containing membrane" ([PMID: 24736412](https://pubmed.ncbi.nlm.nih.gov/24736412/)). Together these establish the outer-segment membrane as the site of OPN1MW function.

```
         PHOTON (green, ~530 nm)
              |
              v
   [ OPN1MW·11-cis-retinal ]  --isomerization-->  [ OPN1MW*·all-trans-retinal ]  (Meta-II-like active state)
                                                            |
                                                            v
                              Gαt2 / GNAT2 (cone transducin): GDP -> GTP exchange
                                                            |
                                                            v
                                        PDE6 activation  -> cGMP hydrolysis
                                                            |
                                                            v
                            cytoplasmic [cGMP] falls -> CNG channels close
                                                            |
                                                            v
                                   M-cone membrane HYPERPOLARIZES  -> neural signal

   SHUT-OFF:  OPN1MW* --GRK1/GRK7 phosphorylation--> arrestin binding (quench)
   RECOVERY:  RGS9-GAP complex accelerates Gαt2 GTP hydrolysis; visual cycle (RPE65) regenerates 11-cis-retinal
```

### Finding 3 — Green-vs-red spectral tuning is set by a few chromophore-pocket residues; near-identity to OPN1LW underlies red–green vision

The ~30 nm λmax difference between OPN1MW (~530 nm) and OPN1LW (~560 nm) does **not** arise from large structural differences but from a small set of polar/dipolar side chains near the retinal chromophore. The green-to-red opsin shift "is best explained by dipolar side chains near the chromophore ring that lower the transition energy that occurs upon electronic excitation by affecting the change in electric dipole moment" ([PMID: 10614049](https://pubmed.ncbi.nlm.nih.gov/10614049/)). The classic "three-site" residues (positions 180, 277, 285), together with positions 230/233, account for most of the shift. A common **Ser180Ala** polymorphism measurably shifts spectral sensitivity: "a common single amino-acid polymorphism (62% Ser, 38% Ala) at residue 180 of the X-linked red visual pigment explains the finding of two major groups in the distribution of colour matching among males with normal colour vision" ([PMID: 1557123](https://pubmed.ncbi.nlm.nih.gov/1557123/)).

OPN1MW and OPN1LW are 96% identical and lie in a head-to-tail tandem array on Xq28, "composed of 2 to 6 (typically 3) genes — a single L is followed by one or more M genes. Only the first two genes of the array are expressed and contribute to the colour vision phenotype" ([PMID: 16758855](https://pubmed.ncbi.nlm.nih.gov/16758855/)). Their high homology promotes unequal recombination/gene conversion, generating the deletions and L/M hybrid genes that cause the common red–green color-vision deficiencies — effectively a natural mutagenesis experiment confirming which residues set spectral identity.

| Pigment | Gene | λmax (approx.) | Identity to OPN1MW | Chromosomal locus |
|---|---|---|---|---|
| Green (M) | **OPN1MW** | ~530 nm | — | Xq28 (L/M tandem array) |
| Red (L) | OPN1LW | ~560 nm | 96% | Xq28 (first in array) |
| Blue (S) | OPN1SW | ~420 nm | ~43% | chromosome 7 |
| Rhodopsin | RHO | ~500 nm | ~41% | chromosome 3 |

### Finding 4 — OPN1MW is an apoprotein covalently bound to 11-cis-retinal that acts as an inverse-agonist ligand; light flips it to an active GPCR

Like all vertebrate visual pigments, the green cone opsin is a GPCR built from an apoprotein covalently linked to 11-cis-retinal: "Cone opsins are G-protein-coupled receptors consisting of an opsin apoprotein covalently linked to the 11-cis-retinal chromophore" ([PMID: 29590586](https://pubmed.ncbi.nlm.nih.gov/29590586/)). The chromophore attaches via a protonated Schiff base to a conserved transmembrane lysine, stabilized by a carboxylate counterion. In the dark, the covalently bound 11-cis-retinal behaves as an **inverse agonist**, locking the receptor in its inactive state. Photon absorption isomerizes retinal to all-trans, driving the receptor through spectroscopically defined conformational intermediates that expose the cytoplasmic G-protein-binding surface (the active Meta-II-like state).

Systematic mutagenesis and spectroscopy of rhodopsin and cone pigments defined the chromophore-binding pocket and the mechanism of the opsin shift: "systematic analysis of the chromophore-binding pocket in rhodopsin and cone pigments has led to an improved understanding of the mechanism of the opsin shift, and of particular molecular determinants underlying color vision in humans" ([PMID: 9427838](https://pubmed.ncbi.nlm.nih.gov/9427838/)). Importantly, cone opsins show regeneration behavior beyond simple spectral tuning — secondary retinal-binding events and binding-site conformational versatility — which "point to relevant functional, unexpected roles other than spectral tuning for the cone visual pigments" ([PMID: 29590586](https://pubmed.ncbi.nlm.nih.gov/29590586/)).

### Finding 5 — Loss of OPN1MW function abolishes M-cone vision; expression requires the upstream Locus Control Region (LCR)

Human genetics pinpoints OPN1MW's specific function to medium-wavelength cone photoreception. **Blue cone monochromacy (BCM)** is defined by complete loss or severe reduction of both long- and middle-wavelength cone function with preserved S (blue) cones and rods: "Blue cone monochromacy (BCM) is a congenital vision disorder characterized by complete loss or severely reduced long- and middle-wavelength cone function, caused by mutations in the OPN1LW/OPN1MW gene cluster on the X-chromosome" ([PMID: 37001420](https://pubmed.ncbi.nlm.nih.gov/37001420/)). More broadly, "Mutations in the OPN1LW (L-) and OPN1MW (M-)cone opsin genes underlie a spectrum of cone photoreceptor defects from stationary loss of color vision to progressive retinal degeneration" ([PMID: 25168334](https://pubmed.ncbi.nlm.nih.gov/25168334/)).

Three mutational mechanisms are established, each illuminating a requirement for a functional pigment: "deletions of the locus control region (LCR); missense mutation (p.Cys203Arg) in an L-/M-hybrid gene; and exon 3 single-nucleotide polymorphism (SNP) interchange haplotypes" ([PMID: 25168334](https://pubmed.ncbi.nlm.nih.gov/25168334/)). (1) The **LCR** upstream of the array is required to drive OPN1LW/OPN1MW transcription — its deletion silences both genes. (2) Inactivating missense mutations such as **p.Cys203Arg** disrupt a conserved disulfide and cause misfolding. (3) **Exon-3 SNP interchange haplotypes** (e.g., LIAVA, LVAVA, MIAVA; key SNP c.532A>G) cause aberrant pre-mRNA splicing/exon-3 skipping and loss of functional pigment. Moderate-to-high myopia frequently accompanies these defects.

### Finding 6 — Structural map: 7-TM GPCR with retinylidene-Lys312, Glu129 counterion, Cys126–Cys203 disulfide, and Asn34 glycosylation

The 364-aa green cone opsin has canonical class-A GPCR topology: an extracellular N-terminus (residues ~1–52), seven transmembrane helices, and a cytoplasmic C-terminus (~326–364), now directly observed by cryo-EM. Recent structural work reports that "Color vision in catarrhine primates relies on red-, green-, and blue-sensitive cone pigments that share an 11-[cis-retinal chromophore]" and provides structures of the human cone pigments (including the green/M pigment; PDB entries 8Y01 and 9YDA) ([PMID: 42348681](https://pubmed.ncbi.nlm.nih.gov/42348681/)). From these structures and from mutagenesis, specific functional residues are assigned:

| Feature | Residue(s) | Role | Evidence type |
|---|---|---|---|
| Chromophore attachment | **Lys312** (TM7) | N6-(retinylidene)lysine Schiff-base linkage to 11-cis-retinal | Cryo-EM (PDB 8Y01) |
| Schiff-base counterion | **Glu129** (TM3) | Stabilizes protonated Schiff base; E129Q → constitutive activity | Mutagenesis |
| Structural disulfide | **Cys126–Cys203** (ECL2) | Required for folding | Mutagenesis / disease variants |
| N-glycosylation | **Asn34** | Post-translational maturation | Sequence/structure |
| Regeneration determinant | residues **17–43** | Required for 11-cis-retinal regeneration | Mutagenesis |
| Deactivation | C-terminal Ser/Thr | Phosphorylation sites | Biochemistry |

The chromophore-binding pocket is essential and finely composed: "The variable composition of the chromophore-binding pocket in visual receptors is essential for vision" ([PMID: 30770468](https://pubmed.ncbi.nlm.nih.gov/30770468/)). Pathogenic missense variants confirm these assignments functionally — **N94K, W177R, C203R, and M273K** abolish visible-light absorption and/or cause misfolding with endoplasmic-reticulum retention and failure to localize to the outer segment, while **R330Q** reduces absorption.

### Finding 7 — OPN1MW signaling is terminated by C-terminal phosphorylation and arrestin binding

OPN1MW is annotated as a phosphoprotein, consistent with the canonical GPCR/visual-pigment deactivation mechanism. After photoactivation, the opsin is phosphorylated on C-terminal Ser/Thr residues by a G-protein-coupled receptor kinase (rhodopsin/cone opsin kinase, GRK1/GRK7), after which arrestin binds to quench further transducin activation. The principle is general: "Phosphorylation of G-protein-coupled receptors (GPCRs) is a required step in signal deactivation" ([PMID: 16219764](https://pubmed.ncbi.nlm.nih.gov/16219764/)); the same work shows high-gain phosphorylation including trans-phosphorylation of non-activated pigment in intact photoreceptors. Recovery of the cone light response additionally requires the RGS9-based GTPase-activating complex acting on transducin.

### Finding 8 — OPN1MW arose by recent gene duplication within the LWS opsin class, enabling catarrhine trichromacy

OPN1MW belongs to the long/middle-wave-sensitive (LWS) opsin class and arose from a relatively recent duplication of an ancestral X-linked long-wave opsin gene in Old World (catarrhine) primates. The resulting red (OPN1LW) and green (OPN1MW) genes remain 96% identical and lie head-to-tail in a tandem array on Xq28. Functional divergence was achieved almost entirely through a handful of spectral-tuning substitutions, not wholesale sequence change. The standard evidence framework is: "To understand the molecular genetic basis of spectral tuning of visual pigments, it is essential to establish correlations between a series of the sequences of visual pigments and their lambda(max) values. The potentially important amino acid changes identified in this way have to be tested whether they are in fact responsible for the lambda(max)-shifts using site-directed mutagenesis and cultured cells" ([PMID: 10785616](https://pubmed.ncbi.nlm.nih.gov/10785616/)). The duplicated, tandem-array architecture was documented in the original cloning work: "Green pigment genes vary in number among color-normal individuals and, together with a single red pigment gene, are proposed to reside in a head-to-tail tandem array within the X chromosome" ([PMID: 2937147](https://pubmed.ncbi.nlm.nih.gov/2937147/)).

---

## Mechanistic Model / Interpretation

OPN1MW is best understood as a **single-photon-sensing GPCR that converts a quantum of green light into a change in the electrical state of an M-cone photoreceptor.** The protein is modular in function:

1. **Light capture (sensor module).** The 11-cis-retinal chromophore, covalently bound at Lys312 and stabilized by the Glu129 counterion, is the actual photon absorber. Dipolar residues lining the binding pocket tune the absorbance to ~530 nm (green). In the dark, bound 11-cis-retinal is an inverse agonist; the entire device is "spring-loaded."

2. **Signal generation (transducer module).** Photoisomerization to all-trans-retinal relaxes the inverse-agonist constraint, and the receptor adopts the active Meta-II-like conformation, exposing its cytoplasmic surface. This surface is a nucleotide-exchange catalyst for cone transducin (GNAT2).

3. **Amplification (effector cascade).** One activated OPN1MW* activates many transducins; each activates PDE6; cGMP is hydrolyzed; CNG channels close; the cell hyperpolarizes. The cascade provides the large gain needed for sensitive vision.

4. **Shut-off and reset.** GRK1/GRK7 phosphorylates the C-terminus; arrestin caps the receptor; RGS9-GAP accelerates transducin GTP hydrolysis; the visual cycle (RPE65 in the RPE) regenerates 11-cis-retinal, which re-binds the opsin — also serving as a folding/trafficking chaperone that keeps the pigment in the outer segment.

The **evolutionary and genomic context** explains both the protein's exquisite paralogy with OPN1LW and its vulnerability. Because OPN1MW and OPN1LW are 96% identical neighbors on Xq28, the locus both encodes the red–green discrimination axis and is a hotspot for unequal recombination, gene conversion, and splicing errors. This is why the clinical genetics are so rich: the same homology that enables trichromacy also generates hybrid genes, deletions, and mis-splicing haplotypes that produce color-vision deficiency, blue cone monochromacy, and progressive cone dysfunction. Human disease variants thus double as a natural saturation-mutagenesis screen that has validated the structural assignments (e.g., C203R disulfide loss → ER retention; LCR deletion → transcriptional silencing).

In short, the "precise role" requested by the research question is: **OPN1MW is the receptor/sensor that performs the first, defining step of the medium-wavelength branch of cone phototransduction, acting at the M-cone outer-segment membrane, feeding the GNAT2→PDE6→cGMP/CNG cascade, and supplying the green input to red–green color vision.**

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [2937147](https://pubmed.ncbi.nlm.nih.gov/2937147/) | Molecular genetics of human color vision genes | Establishes OPN1MW as a rhodopsin-family pigment apoprotein (41% identity to rhodopsin; 96% to red), tandem array on X (F001, F003, F008) |
| [10614049](https://pubmed.ncbi.nlm.nih.gov/10614049/) | Colour tuning mechanisms of visual pigments | 11-cis-retinal PSB chromophore; dipolar residues set green-vs-red shift (F001, F003) |
| [1557123](https://pubmed.ncbi.nlm.nih.gov/1557123/) | Ser180Ala polymorphism and colour matching | Single pocket residue shifts spectral sensitivity (F003) |
| [16758855](https://pubmed.ncbi.nlm.nih.gov/16758855/) | Inherited colour vision deficiencies | X-chromosome L/M array structure and expression rules (F003) |
| [29590586](https://pubmed.ncbi.nlm.nih.gov/29590586/) | Human blue cone opsin regeneration | Cone opsins = apoprotein + covalent 11-cis-retinal; roles beyond spectral tuning (F004) |
| [9427838](https://pubmed.ncbi.nlm.nih.gov/9427838/) | Rhodopsin: prototypical GPCR | Chromophore-binding pocket and opsin-shift mechanism (F004) |
| [42106180](https://pubmed.ncbi.nlm.nih.gov/42106180/) | Phototransduction in rod and cone cells | cGMP/Ca²⁺ cone cascade that OPN1MW initiates (F002) |
| [27225770](https://pubmed.ncbi.nlm.nih.gov/27225770/) | Cone survival in LCA model | 11-cis-retinal as switch and trafficking chaperone (F002) |
| [24736412](https://pubmed.ncbi.nlm.nih.gov/24736412/) | Cone outer segment protein distribution | Cone OS formed by opsin-containing membrane; localization (F002) |
| [37001420](https://pubmed.ncbi.nlm.nih.gov/37001420/) | Blue cone monochromacy and gene therapy | Loss of L+M function defines BCM (F005) |
| [25168334](https://pubmed.ncbi.nlm.nih.gov/25168334/) | Three cone-opsin mutational mechanisms | LCR deletion, C203R misfolding, exon-3 mis-splicing (F005, F006) |
| [42348681](https://pubmed.ncbi.nlm.nih.gov/42348681/) | Cryo-EM of cone visual pigments | Structures of human cone pigments; Lys312 retinylidene linkage (F006) |
| [30770468](https://pubmed.ncbi.nlm.nih.gov/30770468/) | Specificity of chromophore-binding site | Binding-pocket composition essential for vision (F006) |
| [16219764](https://pubmed.ncbi.nlm.nih.gov/16219764/) | Light-induced phosphorylation of visual pigments | Phosphorylation deactivates visual-pigment GPCRs (F007) |
| [10785616](https://pubmed.ncbi.nlm.nih.gov/10785616/) | Molecular evolution of vertebrate visual pigments | Sequence–λmax + mutagenesis framework for tuning (F008) |

Supporting context (not primary citations for the findings above) includes work on the RGS9/R9AP recovery machinery and the optoretinogram as a readout of G-protein signaling in human cones ([PMID: 42532840](https://pubmed.ncbi.nlm.nih.gov/42532840/), [PMID: 36122241](https://pubmed.ncbi.nlm.nih.gov/36122241/)), cone-opsin array mutational cohorts ([PMID: 35400991](https://pubmed.ncbi.nlm.nih.gov/35400991/), [PMID: 3485310](https://pubmed.ncbi.nlm.nih.gov/3485310/)), and comparative LWS-opsin evolution across fishes and basal vertebrates ([PMID: 38861038](https://pubmed.ncbi.nlm.nih.gov/38861038/), [PMID: 30804415](https://pubmed.ncbi.nlm.nih.gov/30804415/), [PMID: 19398493](https://pubmed.ncbi.nlm.nih.gov/19398493/), [PMID: 32189477](https://pubmed.ncbi.nlm.nih.gov/32189477/)).

---

## Limitations and Knowledge Gaps

- **Species transfer of mechanistic detail.** Much of the fine kinetic and structural detail of phototransduction (transducin activation rates, Meta-II lifetimes, shut-off kinetics) is derived from rod rhodopsin and from non-human or heterologous systems. While the GPCR architecture and cascade are conserved, M-cone-specific quantitative parameters (e.g., single-photon response amplitude, deactivation rate constants) for human OPN1MW specifically are less completely characterized than for rhodopsin.
- **Structural data are recent and still maturing.** The cryo-EM structures (PDB 8Y01/9YDA) that directly visualize the green pigment and Lys312 linkage are newly reported; some residue-level assignments (e.g., exact counterion network, conformational intermediates) rest partly on homology to rhodopsin rather than direct human-M-cone data.
- **Residue numbering.** Spectral-tuning "site" numbering (180, 277, 285, 230/233) follows conventions partly based on the red pigment; care is needed when mapping to the exact OPN1MW sequence coordinates.
- **"Non-canonical" cone-opsin behavior.** Observations of secondary retinal binding and binding-site versatility in cone opsins ([PMID: 29590586](https://pubmed.ncbi.nlm.nih.gov/29590586/)) suggest functions beyond spectral tuning that are not yet mechanistically defined.
- **Regulatory biology.** The precise rules by which the LCR and array position dictate stochastic L-vs-M expression in individual cones are not fully resolved, and most expression data are high-throughput rather than single-cone functional measurements.

---

## Proposed Follow-up Experiments / Actions

1. **Human M-cone single-cell physiology.** Use suction-electrode or adaptive-optics optoretinography (ORG) recordings of identified human M-cones to directly measure OPN1MW single-photon response amplitude, activation gain, and deactivation kinetics, closing the gap left by rod-derived parameters.
2. **High-resolution active-state structure.** Determine a cryo-EM structure of the photoactivated (Meta-II-like) green opsin in complex with cone transducin (GNAT2) to visualize the exact G-protein coupling interface and confirm the roles of Glu129 and the TM movements.
3. **Deep mutational scan.** Perform saturation mutagenesis of OPN1MW expressed in cultured cells with spectrophotometric and trafficking readouts, cross-referenced to the catalog of disease variants, to build a complete genotype→(λmax, folding, OS-localization) map.
4. **Counterion and constitutive-activity test.** Directly validate E129Q constitutive activity in a human M-cone-opsin reconstitution/transducin-activation assay and quantify dark noise ("dark light") contributions.
5. **Splicing-mechanism dissection.** Use minigene and patient-derived photoreceptor (iPSC-derived organoid) assays to define how exon-3 interchange haplotypes (LIAVA/LVAVA/MIAVA) disrupt splicing, informing antisense-oligonucleotide or gene-replacement therapy for BCM.
6. **LCR/array expression logic.** Apply single-cell transcriptomics plus reporter arrays to determine how LCR–promoter looping sets the L:M expression ratio and whether OPN1MW position in the array quantitatively limits M-cone output.

---

## Conclusion

OPN1MW encodes the **human green (medium-wavelength-sensitive) cone opsin**, a light-activated class-A GPCR of the rhodopsin/opsin family. It covalently binds 11-cis-retinal (at Lys312, counterion Glu129) and absorbs green light (λmax ≈ 530 nm); photoisomerization activates cone transducin (GNAT2), initiating the cone phototransduction cascade (GNAT2 → PDE6 → cGMP drop → CNG-channel closure → hyperpolarization) in the **outer-segment membrane of M-cone photoreceptors**. Through this activity — and together with its 96%-identical red paralogue OPN1LW on the Xq28 tandem array — OPN1MW supplies the medium-wavelength input underlying the red–green axis of human trichromatic color vision. The gene symbol, organism, family, and domains in the UniProt target definition were all verified; this report concerns the correct protein.


## Artifacts

- [OpenScientist final report](OPN1MW-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](OPN1MW-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2937147
2. PMID:10614049
3. PMID:42106180
4. PMID:27225770
5. PMID:24736412
6. PMID:1557123
7. PMID:16758855
8. PMID:29590586
9. PMID:9427838
10. PMID:37001420
11. PMID:25168334
12. PMID:42348681
13. PMID:30770468
14. PMID:16219764
15. PMID:10785616
16. PMID:42532840
17. PMID:36122241
18. PMID:35400991
19. PMID:3485310
20. PMID:38861038
21. PMID:30804415
22. PMID:19398493
23. PMID:32189477