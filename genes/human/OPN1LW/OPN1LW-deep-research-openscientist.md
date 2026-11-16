---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T04:05:34.842188'
end_time: '2026-11-14T04:21:53.146804'
duration_seconds: 978.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: OPN1LW
  gene_symbol: OPN1LW
  uniprot_accession: P04000
  protein_description: 'RecName: Full=Long-wave-sensitive opsin 1 {ECO:0000303|Ref.6};
    AltName: Full=Red cone photoreceptor pigment; AltName: Full=Red-sensitive opsin;
    Short=ROP;'
  gene_info: Name=OPN1LW {ECO:0000312|HGNC:HGNC:9936}; Synonyms=RCP;
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: OPN1LW-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: OPN1LW-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P04000
- **Protein Description:** RecName: Full=Long-wave-sensitive opsin 1 {ECO:0000303|Ref.6}; AltName: Full=Red cone photoreceptor pigment; AltName: Full=Red-sensitive opsin; Short=ROP;
- **Gene Information:** Name=OPN1LW {ECO:0000312|HGNC:HGNC:9936}; Synonyms=RCP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family. Opsin
- **Key Domains:** GPCR_opsins. (IPR050125); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Opsin. (IPR001760); Opsin_red/grn. (IPR000378)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "OPN1LW" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'OPN1LW' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **OPN1LW** (gene ID: OPN1LW, UniProt: P04000) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of OPN1LW (Human Long-Wave-Sensitive Opsin 1 / Red Cone Pigment)

**UniProt:** P04000 · **Gene:** OPN1LW (synonym RCP) · **Organism:** *Homo sapiens* · **Locus:** Xq28
**Family:** G-protein-coupled receptor (GPCR) class A, opsin subfamily (rhodopsin-like)

## Gene Identity Verification

The gene symbol **OPN1LW** unambiguously matches the UniProt record P04000. It encodes the **long-wave-sensitive (L) cone opsin**, also called the **red cone photoreceptor pigment / red-sensitive opsin (ROP)**. This identity is fully consistent with the literature: OPN1LW is repeatedly described as the long-wavelength ("red") cone photopigment of the human retina, a member of the opsin GPCR family, encoded in the Xq28 L/M opsin array [PMID 8394581; PMID 26153062; PMID 34440353]. The domain architecture given by UniProt (GPCR_opsins, GPCR_Rhodpsn_7TM, Opsin, Opsin_red/grn) confirms it is a seven-transmembrane opsin of the red/green class. **No ambiguity or cross-organism symbol conflict was found.** All statements below refer to this human L-cone opsin.

---

## 1. Summary — Answer to the Research Question

OPN1LW is the **light-sensing G-protein-coupled receptor of long-wavelength ("red") cone photoreceptors**. Its primary molecular function is **light-activated signal transduction**: it is a 7-transmembrane opsin that covalently binds the chromophore **11-*cis*-retinal** as a protonated Schiff base. Absorption of a long-wavelength photon (λmax ≈ 560–563 nm) isomerizes the chromophore to all-*trans*-retinal, driving the receptor into its active (Metarhodopsin-II-like) conformation, which **catalyzes GDP→GTP exchange on the cone G protein transducin (Gαt2/GNAT2)**, thereby triggering the phototransduction cascade (PDE6C activation → cGMP hydrolysis → closure of CNG channels → cone hyperpolarization). It performs this function **in the membrane discs of the L-cone outer segment** in the retina. By providing the long-wavelength spectral channel, OPN1LW is one of the two pigments (with OPN1MW/green) that create the human red–green chromatic axis and underlie trichromatic color vision.

---

## 2. Primary Function: A Light-Activated GPCR (Photoreceptor Signaling)

**Molecular architecture.** OPN1LW is a rhodopsin-like (type II) **class-A GPCR** built from **seven transmembrane α-helices**. Its 11-*cis*-retinal ligand "is covalently linked to a lysine in helix seven forming a protonated Schiff base," buried deep within the helical bundle [PMID 29410984; PMID 15506960]. A conserved acidic counterion stabilizes the protonated Schiff base, and an intramembrane **disulfide bond** (the Cys that is mutated to Arg in the disease variant Cys203Arg) rigidifies the extracellular/retinal-pocket fold. Internal **water molecules** organize a hydrogen-bond network near the chromophore and toward the cytoplasmic G-protein-binding face; "rearrangement of this network leads to the stabilization of the active state" during photoactivation [PMID 29410984]. Thus photon capture in the TM core is relayed through conserved water/residue networks to the intracellular surface that engages transducin.

**Chromophore chemistry.** Like all visual opsins, OPN1LW is an apoprotein that binds **11-*cis*-retinaldehyde (11cRAL) through a protonated Schiff base** to a conserved lysine in transmembrane helix 7. "The light absorbing chromophore in opsin visual pigments is the protonated Schiff base of 11-cis-retinaldehyde (11cRAL). Absorption of a photon isomerizes 11cRAL to all-trans-retinaldehyde (atRAL), briefly activating the pigment before it dissociates" [PMID 28473692]. After photobleaching, the all-*trans*-retinal dissociates and the apo-opsin must recombine with fresh 11-*cis*-retinal (supplied by the retinoid/visual cycle) to regenerate a light-sensitive pigment.

**Transducin activation is the catalyzed "reaction."** OPN1LW is not an enzyme in the metabolic sense; its catalytic output is **guanine-nucleotide exchange on transducin**. Light-activated cone opsins "stimulated [35S]guanosine 5'-(gamma-thio)triphosphate nucleotide exchange on ... transducin in a time-dependent manner," activating many transducin molecules per photoisomerization [PMID 8995408]. In cones this G protein is the cone-specific transducin (Gαt2/GNAT2 with Gγc/GNGT2); activated transducin-GTP relieves inhibition of cone phosphodiesterase (PDE6C), lowering cGMP and closing cyclic-nucleotide-gated channels, producing the graded hyperpolarizing light response of the cone. Deactivation/recovery of this cascade depends on the GTPase-activating RGS9–Gβ5–R9AP complex in the outer segment [PMID 42094530].

**Signal termination (deactivation).** The active lifetime of OPN1LW is terminated by the canonical GPCR shutoff module. Light-activated cone opsins undergo **multi-site phosphorylation by G-protein-coupled receptor kinase 1 (GRK1)**, after which **cone arrestin (ARR3/Arr4/"CAR")** binds the phosphorylated receptor to quench transducin activation — "specific binding of mCAR to light-activated, phosphorylated cone opsins," abolished in GRK1-null cones [PMID 12853434]. Loss of visual arrestins delays cone pigment shutoff [PMID 24292827]. This rapid quenching, together with the fast cascade kinetics and GAP-complex (RGS9/R9AP) recovery, gives cones their high temporal resolution.

**Cone-specific biophysics (distinguishes OPN1LW from rhodopsin).** Cone pigments, including the red pigment, **spontaneously dissociate into apo-opsin + retinal even without light**. Microspectrophotometry found apo-opsin fractions of "∼30% in L cones, ∼3% in M cones, and negligible in S cones" in darkness [PMID 33065015]. Because free opsin has weak constitutive activity, this creates "dark light": "With its constitutive transducin-stimulating activity, the free cone opsin produces an approximately 2-fold desensitization in red cones, equivalent to that produced by a steady light causing 500 photoisomerizations s⁻¹" [PMID 15953417]. This intrinsic instability of the L-cone holo-pigment contributes to the lower absolute sensitivity, higher background noise, and faster dark adaptation of cones relative to rods.

---

## 3. Substrate / Ligand Specificity: Spectral Tuning (Why "Red")

The functional specificity of OPN1LW is **wavelength selectivity**, not substrate turnover. The L (red, OPN1LW) and M (green, OPN1MW) pigments are ~96% identical in sequence yet differ in peak sensitivity by ~28 nm ("peaks at around 563 nm and 535 nm, respectively") [PMID 8394581]. This difference is produced by a **small number of amino acid substitutions lining the retinal-binding pocket** (classically the "three/seven-site" tuning residues at positions such as 180, 277, 285, with 277 and 285 being the largest contributors; chloride binding near His197/Lys200 further red-shifts LWS pigments).

Biophysical evidence localizes the tuning to the chromophore environment: FTIR spectroscopy of primate green vs. red pigments showed that although protein-bound waters flank both the Schiff base and the retinal β-ionone ring, "only the latter showed differences between MG and MR, which suggests their role in color tuning" [PMID 28687791]. Mutagenesis of LWS opsins demonstrates that **single residue changes cause large spectral shifts** — e.g., a 292S→292A substitution shifts λmax from 524 to 552 nm [PMID 9471225] — confirming the mechanism by which OPN1LW is tuned to long wavelengths. Thus OPN1LW's "red" identity is encoded by polar/hydroxyl residues (hydroxyl-bearing Ser/Thr/Tyr at the tuning sites red-shift; non-polar Ala/Phe blue-shift) that stabilize charge separation in the excited state of the retinylidene chromophore.

**OPN1LW is itself spectrally polymorphic (residue 180).** The red pigment carries a common **Ser180Ala polymorphism**: reconstituted recombinant red pigment occurs as two variants [PMID 1492133], and "a serine/alanine polymorphism at amino acid position 180 ... shifts the spectrum of the pigment produced by about 6 nm," accounting for individual differences in red/green Rayleigh color matches among people with normal color vision [PMID 8451836]. In vivo studies of single-gene dichromats (each X chromosome carrying one opsin gene) directly correlate the deduced OPN1LW amino acid sequence with corneal spectral sensitivity, confirming that identified residues (notably 180, 277, 285, and the exon-3 cluster) set the L-cone λmax [PMID 9822760].

---

## 4. Subcellular and Tissue Localization

- **Tissue / cell type:** Retina; expressed exclusively in **long-wavelength (L / "red") cone photoreceptors**. L and M cones together make up "the vast majority (~94%) are L and M cones" of the human cone mosaic [PMID 34440353]. S (blue) cones use the unrelated OPN1SW pigment.
- **Subcellular site of function:** The **cone outer segment**, in the stacked membrane discs/infoldings where opsin, transducin and PDE are concentrated; this is where phototransduction is executed and optically measurable (optoretinography) light responses originate [PMID 42094530]. As a 7-TM integral membrane GPCR, OPN1LW is synthesized in the inner segment and trafficked via the connecting cilium (VxPx-type ciliary targeting) to the outer segment, analogous to rhodopsin trafficking [PMID 42818542].

---

## 5. Pathway Context and Biological Process

**Pathway:** OPN1LW is the **initiating receptor of the cone phototransduction cascade** (visual phototransduction): photon → OPN1LW* → cone transducin (GNAT2) → PDE6C → ↓cGMP → CNGB3/CNGA3 channel closure → membrane hyperpolarization → modulation of glutamate release onto bipolar cells. Recovery requires RGS9/R9AP-mediated GTP hydrolysis and opsin phosphorylation/arrestin binding, plus chromophore regeneration through the retinoid visual cycle [PMID 28473692; PMID 42094530].

**Expression regulation (why OPN1LW marks a discrete L-cone subtype).** The array is controlled by a single upstream **locus control region (LCR)**. Chromosome-conformation-capture in human (and mouse) retina shows "the L/M enhancer locus control region (LCR) loops with either the L or M promoter," so each cone transcribes only one opsin gene; proper looping/transcription requires the photoreceptor transcription factors **CRX, NRL and NR2E3** [PMID 22006320]. Cell-fate specification of L/M vs. S cones is governed by thyroid hormone signaling through **THRβ2**: loss-of-function THRβ2 mutations reduce L- and M-cone and increase S-cone function with no OPN1LW coding change [PMID 22551329]. This explains the stochastic, mutually exclusive one-gene-per-cone expression of OPN1LW.

**Biological process:** Phototopic (daylight) vision, high-acuity vision, and specifically the **long-wavelength / red–green color channel** of trichromatic color vision. L and M cone signals are differenced downstream to compute red–green chromatic contrast [PMID 8394581]. Beyond image-forming vision, L/M cones contribute to the **visual feedback that regulates refractive (myopic) eye development** — "they are critically important in the visual feedback mechanism that regulates refractive development of the eye during childhood" [PMID 34440353].

---

## 6. Genetic Architecture and Disease (Functional Validation in Humans)

OPN1LW sits at the head of a **tandem array on Xq28** with one or more OPN1MW genes under a shared **locus control region (LCR)**; a cone expresses either an L or an M gene from the array. The paralogs are "composed of 2-9 paralogs with 99.8% sequence homology and is susceptible to deletions, duplications, and mutations" [PMID 26153062]. This near-identity drives unequal recombination and gene conversion, generating hybrid L/M genes and the common **protan (red) / deutan (green) red–green color-vision deficiencies** [PMID 37894926].

Loss or inactivation of OPN1LW provides direct functional proof of its role:
- **Blue cone monochromacy (BCM):** "an X-linked condition caused by a loss-of-function of both the OPN1LW and OPN1MW opsin genes," abolishing L- and M-cone function [PMID 26153062; PMID 35759666].
- **X-linked cone dysfunction / protanopia** from specific OPN1LW exon-3 haplotypes (e.g., deleterious LIAVA-type variants) that misfold or mis-splice the pigment [PMID 34287097].
- **Bornholm Eye Disease (BED)** — cone dysfunction with **myopia and dichromacy** — is caused by rare OPN1LW exon-3 haplotypes (or the disulfide-disrupting **Cys203Arg**). In vitro these variant opsins "formed functional pigments, which trafficked to the cell membranes [but] were, however, less stable than wild type," and/or cause "defective splicing of exon 3," linking reduced OPN1LW pigment stability to cone dystrophy and myopia [PMID 23322568].
- Gene-augmentation (AAV L-/M-opsin) rescues cone structure/function in BCM models, confirming the pigment is both necessary and sufficient for L/M cone function [PMID 35272502].

---

## 6b. Evolutionary Origin and Therapeutic Validation

**Evolution.** OPN1LW is the long-wavelength product of a recent gene duplication. Most mammals are dichromatic; primate trichromacy arose "via allelic differentiation (e.g. most New World monkeys) or gene duplication (e.g. Old World primates) of the middle to long-wavelength sensitive (M/LWS, or red-green) opsin gene" [PMID 27594978]. In the Old World/hominoid lineage this duplication produced the separate, X-linked **OPN1LW (L)** and **OPN1MW (M)** genes; their high sequence identity reflects shared ancestry and explains both the recombination-prone Xq28 array and the red–green chromatic channel they jointly create. The event is temporally linked to relaxation of vomeronasal pheromone signaling in catarrhines [PMID 14963105].

**Therapeutic proof of function.** AAV-mediated delivery of human **L-opsin (OPN1LW) cDNA** under a cone-specific promoter restores cone ERG responses and regenerates cone outer-segment structure in mouse models of blue cone monochromacy, including the common **C203R (murine C198R)** opsin mutation [PMID 42275379; PMID 28751656]. This gain-of-function rescue confirms that OPN1LW is both necessary and sufficient to confer L-cone phototransduction competence.

## 7. Evidence Summary

| Claim | Evidence type | Source |
|---|---|---|
| L-cone/red pigment, λmax ≈ 563 nm | Microspectrophotometry / psychophysics | PMID 8394581 |
| 11-*cis*-retinal Schiff base; photoisomerization activates pigment | Biochemistry / photochemistry | PMID 28473692 |
| Light-activated opsin catalyzes transducin GDP/GTP exchange | In vitro transducin assay | PMID 8995408 |
| Spectral tuning via β-ionone-ring environment & single residues | FTIR spectroscopy; site-directed mutagenesis | PMID 28687791; PMID 9471225 |
| Ser180Ala polymorphism shifts λmax ~6 nm (benign variation) | Recombinant pigment spectra; psychophysics | PMID 1492133; PMID 8451836; PMID 9822760 |
| LCR-looping enforces mutually exclusive L/M expression; THRβ2 fate | Chromosome conformation capture; clinical ERG | PMID 22006320; PMID 22551329 |
| Cone-specific apo-opsin dissociation / dark noise in L cones | Microspectrophotometry; single-cell electrophysiology | PMID 33065015; PMID 15953417 |
| Outer-segment site of phototransduction; G-protein cascade | Optoretinography (human) | PMID 42094530 |
| Deactivation by GRK1 phosphorylation + cone arrestin (ARR3) | Pure-cone KO biochemistry/genetics | PMID 12853434; PMID 24292827 |
| Destabilizing coding/exon-3 variants → Bornholm Eye Disease (myopia, dichromacy) | In vitro expression; family genetics | PMID 23322568 |
| 7-TM GPCR fold; retinal–Lys(TM7) Schiff base; water networks | Structural/biophysical review | PMID 29410984; PMID 15506960 |
| Origin by M/LWS opsin gene duplication (primate trichromacy) | Comparative genetics/evolution | PMID 27594978 |
| AAV OPN1LW gene therapy rescues cone function (gain-of-function) | Preclinical mouse models | PMID 42275379; PMID 28751656 |
| Xq28 L/M array, high homology, BCM on biallelic loss | Molecular genetics / CGH | PMID 26153062; PMID 35759666 |
| ~94% of cones are L/M; role in refractive development | Review | PMID 34440353 |

## 8. Supported vs. Refuted Hypotheses

- **Supported:** OPN1LW is a light-activated GPCR (opsin) whose primary function is transducin activation in the L-cone outer segment; it provides the long-wavelength spectral channel; its loss/mutation causes protan defects and (with OPN1MW) blue cone monochromacy.
- **Refuted / excluded:** OPN1LW is **not** an enzyme with a small-molecule metabolic substrate, **not** a transporter, and **not** a structural protein — its "substrate specificity" is correctly understood as photon-wavelength selectivity and its "catalysis" as nucleotide exchange on a G protein.

## 9. Limitations and Future Directions

- Much mechanistic detail (transducin activation kinetics, apo-opsin behavior) derives from non-human/amphibian/fish cones and heterologously expressed opsins; human L-cone-specific single-cell measurements remain limited by cell scarcity and pigment instability.
- No experimental high-resolution structure of human OPN1LW itself is cited here; tuning-residue assignments rest on homology, mutagenesis of related LWS pigments, and spectroscopy. A cryo-EM structure of human L-opsin–transducin would sharpen the model.
- The exact per-residue "L vs M" tuning contributions and chloride-binding stoichiometry for the human pigment warrant direct confirmation.

## 10. Concluding Synthesis

OPN1LW is unambiguously the human **long-wave-sensitive ("red") cone opsin** (P04000; Xq28). Its **primary function is as a light-activated class-A GPCR photoreceptor**: it binds 11-*cis*-retinal via a protonated Schiff base to a TM7 lysine; long-wavelength light (λmax ≈ 560–563 nm, tuned by pocket residues 180/277/285 and chloride binding) isomerizes the chromophore and switches the receptor to an active state that **catalytically activates cone transducin (GNAT2)**, launching the PDE6C→cGMP→CNG-channel phototransduction cascade and hyperpolarizing the L-cone. It acts **in the outer-segment disc membranes** of L cones, is switched off by **GRK1 phosphorylation + cone arrestin (ARR3)**, and is restored by chromophore regeneration and the RGS9/R9AP GAP complex. Biologically it supplies the **long-wavelength input to the red–green chromatic axis** of trichromatic, high-acuity daylight vision and contributes to emmetropization. These conclusions rest on convergent experimental (biochemical transducin assays, spectroscopy, electrophysiology, human psychophysics, gene therapy) and inferential (structural homology, evolutionary duplication) evidence, and are clinically validated by loss-of-function (color blindness, blue cone monochromacy), destabilizing (Bornholm Eye Disease), and gain-of-function (AAV rescue) phenotypes.

---
*Report compiled over Iterations 1–5. Fifteen confirmed findings; 45 papers reviewed. Citations are PubMed PMIDs with verbatim abstract support recorded in the knowledge state.*


## Artifacts

- [OpenScientist final report](OPN1LW-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](OPN1LW-deep-research-openscientist_artifacts/final_report.pdf)