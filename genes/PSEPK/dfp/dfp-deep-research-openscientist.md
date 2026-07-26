---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:46:52.529590'
end_time: '2026-07-18T14:54:54.493395'
duration_seconds: 4081.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dfp
  gene_symbol: dfp
  uniprot_accession: Q88C96
  protein_description: 'RecName: Full=Coenzyme A biosynthesis bifunctional protein
    CoaBC {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=DNA/pantothenate metabolism
    flavoprotein {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=Phosphopantothenoylcysteine
    synthetase/decarboxylase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPCS-PPCDC {ECO:0000256|HAMAP-Rule:MF_02225};
    Includes: RecName: Full=Phosphopantothenoylcysteine decarboxylase {ECO:0000256|HAMAP-Rule:MF_02225};
    Short=PPC decarboxylase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPC-DC {ECO:0000256|HAMAP-Rule:MF_02225};
    EC=4.1.1.36 {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=CoaC {ECO:0000256|HAMAP-Rule:MF_02225};
    Includes: RecName: Full=Phosphopantothenate--cysteine ligase {ECO:0000256|HAMAP-Rule:MF_02225};
    EC=6.3.2.5 {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=CoaB {ECO:0000256|HAMAP-Rule:MF_02225};
    AltName: Full=Phosphopantothenoylcysteine synthetase {ECO:0000256|HAMAP-Rule:MF_02225};
    Short=PPC synthetase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPC-S {ECO:0000256|HAMAP-Rule:MF_02225};'
  gene_info: Name=dfp {ECO:0000313|EMBL:AAN70850.1}; Synonyms=coaBC {ECO:0000256|HAMAP-Rule:MF_02225};
    OrderedLocusNames=PP_5285 {ECO:0000313|EMBL:AAN70850.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: In the N-terminal section; belongs to the HFCD (homo-
  protein_domains: CoaB-like_sf. (IPR035929); CoaBC. (IPR005252); DNA/pantothenate-metab_flavo_C.
    (IPR007085); Flavin_trans-like. (IPR036551); Flavoprotein. (IPR003382)
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
  path: dfp-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dfp-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C96
- **Protein Description:** RecName: Full=Coenzyme A biosynthesis bifunctional protein CoaBC {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=DNA/pantothenate metabolism flavoprotein {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=Phosphopantothenoylcysteine synthetase/decarboxylase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPCS-PPCDC {ECO:0000256|HAMAP-Rule:MF_02225}; Includes: RecName: Full=Phosphopantothenoylcysteine decarboxylase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPC decarboxylase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPC-DC {ECO:0000256|HAMAP-Rule:MF_02225}; EC=4.1.1.36 {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=CoaC {ECO:0000256|HAMAP-Rule:MF_02225}; Includes: RecName: Full=Phosphopantothenate--cysteine ligase {ECO:0000256|HAMAP-Rule:MF_02225}; EC=6.3.2.5 {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=CoaB {ECO:0000256|HAMAP-Rule:MF_02225}; AltName: Full=Phosphopantothenoylcysteine synthetase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPC synthetase {ECO:0000256|HAMAP-Rule:MF_02225}; Short=PPC-S {ECO:0000256|HAMAP-Rule:MF_02225};
- **Gene Information:** Name=dfp {ECO:0000313|EMBL:AAN70850.1}; Synonyms=coaBC {ECO:0000256|HAMAP-Rule:MF_02225}; OrderedLocusNames=PP_5285 {ECO:0000313|EMBL:AAN70850.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** In the N-terminal section; belongs to the HFCD (homo-
- **Key Domains:** CoaB-like_sf. (IPR035929); CoaBC. (IPR005252); DNA/pantothenate-metab_flavo_C. (IPR007085); Flavin_trans-like. (IPR036551); Flavoprotein. (IPR003382)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dfp" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dfp' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dfp** (gene ID: dfp, UniProt: Q88C96) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dfp* / *coaBC* (CoaBC) in *Pseudomonas putida* KT2440

**UniProt:** Q88C96 · **Gene:** *dfp* (synonym *coaBC*) · **Locus:** PP_5285
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
**EC numbers:** 6.3.2.5 (phosphopantothenate–cysteine ligase) + 4.1.1.36 (phosphopantothenoylcysteine decarboxylase)

---

## 1. Summary (Answer to the Research Question)

Q88C96 (*dfp*/*coaBC*, PP_5285) encodes **CoaBC**, a **bifunctional, cytoplasmic enzyme that carries out the second and third of the five steps of the universal coenzyme A (CoA) biosynthetic pathway**, converting 4′-phosphopantothenate into 4′-phosphopantetheine. It is a single polypeptide with two catalytic domains:

- A **C-terminal CoaB domain** = **phosphopantothenoylcysteine synthetase (PPCS, EC 6.3.2.5)**, which ligates L-cysteine to 4′-phosphopantothenate to form (R)-4′-phospho-*N*-pantothenoylcysteine (PPC), using **CTP** (not ATP) and Mg²⁺.
- An **N-terminal CoaC domain** = **phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36)**, an **FMN-dependent** member of the HFCD flavoprotein family that decarboxylates PPC to 4′-phosphopantetheine.

CoaBC is **essential**, acts in the **cytosol**, forms a higher-order oligomer (dodecamer) subject to **feedback regulation by CoA thioesters**, and is a validated antibacterial drug target.

---

## 2. Identity Verification

The assignment is unambiguous and consistent across independent lines of evidence:

- **Gene symbol history:** The *dfp* gene ("DNA/pantothenate metabolism flavoprotein") was renamed ***coaBC*** when Strauss et al. showed the Dfp protein carries both CoA-pathway activities (PMID 11278255). The UniProt record's dual naming (*dfp* / *coaBC*; PPCS-PPCDC; CoaB + CoaC) matches this literature exactly.
- **Domain/family match:** The provided InterPro/family annotation (HFCD flavoprotein in the N-terminal section; CoaB-like_sf; CoaBC; DNA/pantothenate-metab_flavo_C; Flavoprotein) precisely matches the biochemically defined two-domain architecture of Dfp/CoaBC.
- **Organism match:** Pseudomonad-specific CoA-pathway physiology (below) is documented for the closely related *P. aeruginosa* (PMID 21551303), directly relevant to *P. putida*.

No conflicting gene of the same symbol was encountered. The literature for "*dfp*/*coaBC*" describes this exact bifunctional CoA-biosynthesis flavoprotein.

**Target-specific sequence evidence (Q88C96, 403 aa):** Direct analysis of the *P. putida* KT2440 sequence confirms both intact catalytic domains and their conserved active-site residues:
- **N-terminal PPCDC/CoaC domain (~1–190):** carries the HFCD flavoprotein signature **G-G-I-A-A-Y-K at residues 15–21**, matching Kupke's conserved G-G/S-I-A-X-Y-K coenzyme/substrate-binding motif (PMID 11358972); a **Cys159** lies in the region homologous to the *E. coli* Dfp substrate-clamp Cys158.
- **C-terminal PPCS/CoaB domain (~200–403):** carries the strictly conserved synthetase motif **K-L-K-K at residues 288–291**, corresponding to the essential *E. coli* Lys289 (KXKK) motif (PMID 12140293).
- The N-terminus (MQRLYRKRIV…) is basic/hydrophilic with **no signal peptide or transmembrane segment**, consistent with cytoplasmic localization.

This confirms the orthology-based assignment at the level of the actual *P. putida* protein rather than relying solely on distant homologs.

---

## 3. Primary Function: Reaction Catalyzed and Substrate Specificity

**Overall reaction (two consecutive pathway steps):**

> 4′-phosphopantothenate + L-cysteine + CTP → (via PPC) → 4′-phosphopantetheine + CO₂ + CMP + PPi (+ Mg²⁺ required)

Strauss et al. identified PPCS as "the last unidentified coenzyme A biosynthetic enzyme in bacteria" and showed that the *dfp* product (renamed *coaBC*) "also has phosphopantothenoylcysteine synthetase activity, using CTP rather than ATP as the activating nucleoside 5′-triphosphate," which "completes the identification of all the enzymes involved in the biosynthesis of coenzyme A in bacteria" (PMID 11278255). Balibar et al. describe *coaBC* as "a single gene encoding a bifunctional protein catalyzing two consecutive steps in the CoA pathway converting 4′-phosphopantothenate to 4′-phosphopantetheine" (PMID 21551303).

### 3a. CoaB / PPCS domain (EC 6.3.2.5) — C-terminal
- **Substrates:** 4′-phosphopantothenate, L-cysteine, CTP, Mg²⁺.
- **Substrate specificity for the nucleotide:** distinctively uses **CTP** rather than ATP (PMID 11278255) — a hallmark that distinguishes bacterial PPCS from the eukaryotic (ATP-using) enzyme.
- **Mechanism:** proceeds in **two half-reactions**. The phosphopantothenate carboxyl is first activated as an **acyl-cytidylate (phosphopantothenoyl-cytidylate) intermediate**, then attacked by the cysteine amine. Kupke trapped this intermediate using mutant His-CoaB N210D (and with wild type when cysteine was omitted), and showed the strictly conserved **²⁸⁹KXKK²⁹² motif (Lys289)** is essential — its exchange abolishes both intermediate formation and product (PMID 12140293). The CoaB domain forms **dimers** (PMID 12140293).

### 3b. CoaC / PPCDC domain (EC 4.1.1.36) — N-terminal, flavoprotein
- **Substrate/product:** decarboxylates (R)-4′-phospho-*N*-pantothenoylcysteine (PPC) to **4′-phosphopantetheine** (PMID 11358972).
- **Cofactor:** **FMN**, bound **non-covalently at the interface between two subunits** within a Rossmann fold; the domain belongs to the **HFCD** ("homooligomeric flavin-containing Cys decarboxylase") family, together with the lantibiotic LanD enzymes EpiD/MrsD and the plant salt-tolerance protein AtHAL3a (PMID 11358972, PMID 15459342). Because the flavin sits at a subunit interface, oligomerization (trimer → dodecamer) is required to assemble a functional active site (PMID 15459342).
- **Mechanism:** an **FMN-mediated oxidative decarboxylation**. The reaction proceeds through an **oxidatively decarboxylated aminoenethiol intermediate** (loss of CO₂ + two H atoms, confirmed by high-resolution MS), which is then **re-reduced by a redox-active cysteine** (Cys175 in AtHAL3a; equivalents Asn125/Cys158 essential in bacterial Dfp) to yield the saturated phosphopantetheine thiol (PMID 11923307, PMID 11358972). Key catalytic/substrate-clamp residues in the conserved G-G/S-I-A-X-Y-K motif are required for flavin binding and activity (PMID 11358972).

**Note on domain order vs. reaction order:** In the polypeptide the **decarboxylase (CoaC) is N-terminal** and the **synthetase (CoaB) is C-terminal**, whereas in the pathway the synthetase acts first — hence the name "Coa**B**C."

---

## 4. Subcellular Localization

CoaBC is a **soluble cytoplasmic enzyme**. CoA biosynthesis is a cytosolic process, and CoaBC has been characterized as a soluble oligomeric protein (gel filtration; native MS; crystallography of homologs) with no signal peptide or membrane-spanning region in Q88C96 (PMID 12140293, PMID 33420031). Its function — producing the CoA precursor 4′-phosphopantetheine — is therefore carried out **inside the cell, in the cytoplasm**, where downstream CoaD/CoaE complete CoA assembly.

---

## 5. Pathway Context and Regulation

- **Pathway:** CoA is assembled in **five steps from pantothenate** (PanK/CoaA(X) → **PPCS(CoaB) → PPCDC(CoaC)** → PPAT/CoaD → DPCK/CoaE); the intermediates are common to prokaryotes and eukaryotes (PMID 15893380). CoaBC occupies steps 2–3, downstream of pantothenate kinase and upstream of phosphopantetheine adenylyltransferase.
- **Downstream fate of the product:** The 4′-phosphopantetheine made by CoaBC is converted by CoaD (PPAT) and CoaE (DPCK) into **free CoA**. CoA is then the donor from which **4′-phosphopantetheinyl transferases (PPTases; AcpS, Sfp)** transfer the 4′-phosphopantetheine moiety onto a conserved serine of apo-**acyl carrier proteins (ACP)** and **peptidyl carrier proteins (PCP)**, producing the holo forms whose phosphopantetheine "swinging arm" thiol is essential for fatty-acid, polyketide, and nonribosomal-peptide synthesis (PMID 15065855, PMID 11525165). Thus CoaBC feeds both the central CoA pool and the carrier-protein machinery — the basis of its essentiality.
- **Regulation:** The first full-length CoaBC structure (from *Mycobacterium smegmatis*) shows the enzyme "is organised as a **dodecamer** and **regulated by CoA thioesters**," with inhibitors binding "a **cryptic allosteric site within CoaB**" (PMID 33420031). This implies end-product/thioester feedback control over CoA output at the CoaBC node.
- **Pseudomonad-specific feature:** In *Pseudomonas*, the upstream pantothenate kinase is the **type III CoaX** (not *E. coli*'s CoaA). Consequently *P. aeruginosa* — unlike *E. coli* — **cannot use pantethine to bypass loss of coaBC**, because of the differing substrate specificity of its pantothenate kinase (PMID 21551303). This indicates pseudomonads, including *P. putida*, depend on **de novo CoaBC activity** with no salvage bypass at this step.

---

## 6. Essentiality and Biomedical/Biotechnological Relevance

- **Essential gene:** *coaBC* is essential in *E. coli* (arabinose-regulated depletion) and its depletion is **bactericidal** in *M. tuberculosis* (PMID 21551303, PMID 33420031).
- **Validated drug target:** The CoA biosynthetic pathway "is a target for antibacterial drug discovery" (PMID 15893380); CoaBC specifically has been pursued with high-throughput biochemical screens and native ion-mobility MS to find selective inhibitors of the CoaB domain (PMID 33420031, PMID 31488574). The same essentiality principle underlies its interest in *Pseudomonas*.
- **Essentiality in *P. putida* KT2440 (inference):** Genome-scale metabolic models of KT2440 predict a defined essential-gene set, and a genome-wide mini-Tn5 knockout screen recovered only *conditionally* essential auxotrophs (amino acids, biotin, nicotinate, vitamin B12) rescuable by supplementation (PMID 20158506). Because CoA cannot be imported and this pathway step cannot be salvaged in *Pseudomonas* (no pantethine bypass; PMID 21551303), *coaBC* (PP_5285) is expected to be **unconditionally essential** — consistent with its being absent from recoverable mutant/auxotroph collections and with demonstrated essentiality of *coaBC* in *E. coli* and *M. tuberculosis*.

---

## 7. Supported vs. Refuted Hypotheses

**Supported:**
- H1: Q88C96 is the bifunctional CoaBC (PPCS + PPCDC) of CoA biosynthesis — **strongly supported** (multiple primary studies of orthologs; family/domain match).
- H2: The synthetase uses CTP and an acyl-cytidylate intermediate — **supported** (PMID 11278255, 12140293).
- H3: The decarboxylase is an FMN-dependent HFCD flavoprotein acting via an aminoenethiol intermediate — **supported** (PMID 11358972, 11923307).
- H4: The enzyme is cytoplasmic and essential — **supported** (PMID 33420031, 21551303).

**Refuted / ruled out:**
- The bacterial synthetase does **not** use ATP as activator (uses CTP) — the ATP hypothesis is refuted for this domain (PMID 11278255).
- A pantethine-salvage bypass of CoaBC does **not** operate in *Pseudomonas* (refuted for pseudomonads; PMID 21551303).

---

## 8. Limitations and Future Directions

- **Direct evidence gap:** Mechanistic/structural data derive from orthologs (*E. coli* Dfp, *M. smegmatis*/*M. tuberculosis* CoaBC, *Arabidopsis* AtHAL3a). No *P. putida* KT2440-specific enzymological study was located; the annotation for Q88C96 is by strong orthology/inference. Direct biochemical confirmation (CTP specificity, FMN content, k_cat/K_m) and a *P. putida* structure would close this gap.
- **Regulation specifics:** Feedback by CoA thioesters is established in mycobacterial CoaBC; whether the *P. putida* enzyme shares the same allosteric site/kinetics remains to be tested.
- **Future work:** Verify essentiality in *P. putida* KT2440 (e.g., conditional knockdown), determine the oligomeric state and FMN stoichiometry, and evaluate CoaB-domain inhibitors for antipseudomonal activity.

---

## References (PMIDs)
- 11278255 — Strauss et al., *J. Biol. Chem.* 2001. PPCS identification; *dfp*→*coaBC*; CTP-dependent synthetase.
- 12140293 — Kupke, *J. Biol. Chem.* 2002. CoaB domain mechanism; acyl-cytidylate intermediate; Lys289 (KXKK) motif; CoaB dimerization.
- 11358972 — Kupke, *J. Biol. Chem.* 2001. N-terminal PPCDC domain; HFCD flavoprotein family; conserved motifs.
- 11923307 — Hernández-Acosta et al., 2002. AtHAL3a; general PPCDC oxidative-decarboxylation mechanism (aminoenethiol intermediate).
- 21551303 — Balibar et al., 2011. Essentiality of *coaBC*; Pseudomonas pantothenate kinase (CoaX) specificity; no pantethine bypass.
- 33420031 — Mendes et al., 2021. First full-length CoaBC structure (dodecamer); CoA-thioester regulation; allosteric CoaB inhibitors; bactericidal on depletion.
- 31488574 — Chan et al., 2019. Native IM-MS structural analysis of *E. coli* PPCS domain; inhibitor screening.
- 15893380 — Leonardi et al., *Prog. Lipid Res.* 2005. Review: CoA biosynthesis genetics/enzymology; antibacterial target.
- 15459342 — Rangarajan et al., 2004. HFCD/FMN flavoprotein fold; non-covalent FMN at subunit interface; trimer→dodecamer assembly (Pad1, EpiD, MrsD, AtHAL3a).
- 15065855 — Mofid et al., 2004. PPTase (Sfp) mechanism; transfer of 4′-phosphopantetheine from CoA to ACP/PCP serine.
- 11525165 — Xu et al., 2001. ACP structure; 4′-phosphopantetheine prosthetic group / swinging arm derived from CoA.
- 20158506 — Molina-Henares et al., 2010. Genome-wide *P. putida* KT2440 mutant screen; essential/conditionally essential gene identification.


## Artifacts

- [OpenScientist final report](dfp-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dfp-deep-research-openscientist_artifacts/final_report.pdf)