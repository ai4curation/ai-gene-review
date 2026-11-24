---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:14:57.491388'
end_time: '2026-10-24T04:39:26.494506'
duration_seconds: 1469.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Lalba
  gene_symbol: Lalba
  uniprot_accession: P29752
  protein_description: 'RecName: Full=Alpha-lactalbumin; AltName: Full=Lactose synthase
    B protein; Flags: Precursor;'
  gene_info: Name=Lalba;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the glycosyl hydrolase 22 family.
  protein_domains: Glyco_hydro_22. (IPR001916); Glyco_hydro_22_CS. (IPR019799); Lactalbumin.
    (IPR000545); Lysozyme-like_dom_sf. (IPR023346); Lys (PF00062)
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
  path: Lalba-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lalba-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P29752
- **Protein Description:** RecName: Full=Alpha-lactalbumin; AltName: Full=Lactose synthase B protein; Flags: Precursor;
- **Gene Information:** Name=Lalba;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the glycosyl hydrolase 22 family.
- **Key Domains:** Glyco_hydro_22. (IPR001916); Glyco_hydro_22_CS. (IPR019799); Lactalbumin. (IPR000545); Lysozyme-like_dom_sf. (IPR023346); Lys (PF00062)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Lalba" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Lalba' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Lalba** (gene ID: Lalba, UniProt: P29752) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Lalba* (Alpha-lactalbumin, UniProt P29752)

## Gene/Protein Identity Verification

The research target is unambiguously identified. UniProt **P29752** is **alpha-lactalbumin** (gene symbol **Lalba**, also "lactose synthase B protein") from *Mus musculus* (mouse). All verification criteria are satisfied:

- **Gene symbol match:** The literature on "Lalba"/"α-lactalbumin" describes exactly the protein in the UniProt description (the regulatory subunit of lactose synthase).
- **Organism match:** The definitive genetic studies were performed in mouse (e.g., the *Lalba*-null mouse, PMID 7708733; isolation/sequencing of the mouse gene, PMID 1398111).
- **Family/domain match:** Literature and the UniProt record both place the protein in the **glycosyl hydrolase 22 / c-type lysozyme superfamily** (Glyco_hydro_22, Lysozyme-like domain), consistent with the listed domains (IPR001916, IPR000545, IPR023346, PF00062).

There is **no ambiguity**: the symbol, organism, family, and domains are mutually consistent, and an extensive, high-quality primary literature exists for this exact protein.

---

## 1. Summary (Answer to the Research Question)

**Mouse alpha-lactalbumin (Lalba) is a small, secreted, calcium-binding protein that functions as the non-catalytic regulatory ("B" or modifier) subunit of the enzyme lactose synthase.** It is not itself an enzyme. Its single, precise molecular function is to bind the catalytic galactosyltransferase **β-1,4-galactosyltransferase-1 (β4GalT1)** and reprogram its sugar-acceptor specificity — switching the preferred acceptor from *N*-acetylglucosamine (GlcNAc) to free **glucose** — so that the complex synthesizes **lactose** (Galβ1-4Glc) from UDP-galactose and glucose. This reaction occurs in the **lumen of the Golgi apparatus of mammary secretory (alveolar) epithelial cells** during lactation; the protein is then packaged into secretory vesicles and exported as an abundant whey protein of milk. Because lactose is the principal osmole of milk, α-lactalbumin — by enabling lactose synthesis — effectively sets the **osmotic water content and volume of milk**, making it essential for successful lactation. Its expression is restricted to differentiated lactating mammary epithelium and is driven by the **prolactin → PRLR → JAK2/STAT5 lactogenic signaling pathway**.

---

## 2. Primary Molecular Function: The Specifier Subunit of Lactose Synthase

### 2.1 The reaction catalyzed and the role of Lalba

Lactose synthase (EC 2.4.1.22) is a **1:1 heterodimeric complex** of two components:

- the **catalytic "A protein"**, β-1,4-galactosyltransferase-1 (β4GalT1), a Mn²⁺-dependent, trans-Golgi, type II membrane glycosyltransferase; and
- the **regulatory "B protein"**, α-lactalbumin (the product of *Lalba*).

On its own, β4GalT1 transfers galactose from UDP-galactose onto GlcNAc residues of glycoconjugates (forming the Galβ1-4GlcNAc unit, *N*-acetyllactosamine). **α-Lactalbumin is a non-catalytic specifier**: when it binds β4GalT1 it promotes the binding of free glucose and alters the enzyme's acceptor specificity from GlcNAc to glucose, enabling synthesis of lactose — the defining carbohydrate of milk (Qasba et al., *Curr Drug Targets* 2008, PMID 18393823; Ramakrishnan & Qasba 2001, PMID 11419947). As a 2012 review states, α-lactalbumin "in its native state acts as a substrate specifier in the lactose synthase complex, thereby defining a function essential for the survival of lactating mammals" (Ho et al. 2012, PMID 23130929).

- **Substrates of the α-lactalbumin-modified reaction:** UDP-galactose (sugar donor) + D-glucose (acceptor); requires Mn²⁺.
- **Product:** lactose (Galβ1-4Glc) + UDP.
- **Substrate-specificity change conferred by Lalba:** acceptor shifts from GlcNAc → glucose (dramatic lowering of the apparent Kₘ for glucose).

### 2.2 Structural mechanism (precise, crystallographic evidence)

The 2 Å crystal structures of lactose synthase reveal the physical basis of the specifier function (Ramakrishnan & Qasba 2001, PMID 11419947). Substrate binding triggers a **large conformational change in β4GalT1 (residues ~345–365)**, repositioning His347 to coordinate the catalytic metal ion and simultaneously **creating the α-lactalbumin- and sugar-acceptor-binding site**. α-Lactalbumin then **holds glucose in place by hydrogen bonding to its O-1 hydroxyl group** in the acceptor site; a reorientation of Arg359 blocks the hydrophobic *N*-acetyl pocket (which normally accommodates the GlcNAc *N*-acetyl group) and maximizes interactions with glucose. The direct enzyme–modifier complex has been captured crystallographically, including a pentenary complex of bovine Gal-T1·Mn²⁺·UDP-GalNAc·Glc·α-lactalbumin (Ramakrishnan et al. 2006, PMID 16497331). Comparative crystal structures of species variants show that the functionally important region (mature residues ~105–110), adjacent to the monosaccharide-binding residues Phe31/His32, is conformationally flexible and forms the enzyme-interaction surface (Pike et al. 1996, PMID 8805552).

### 2.3 Kinetic mechanism

Classical enzyme kinetics established that lactose synthesis proceeds by a **random-equilibrium mechanism**: binding of Mn²⁺ at the tight metal site (Kd ≈ 2.3 µM) is an obligatory prerequisite, and α-lactalbumin can associate with either the enzyme·Mn²⁺·acceptor or the enzyme·Mn²⁺·UDP-galactose complex (Bell et al. 1976, PMID 818085; Powell & Brew 1976, PMID 932002). Thus α-lactalbumin does not change the catalytic chemistry; it modulates acceptor binding.

**Interpretation:** The primary function of Lalba is best described as a **substrate-specificity modifier / regulatory binding subunit**, converting a general glycosyltransferase into the dedicated lactose-synthesizing enzyme of lactation.

---

## 3. Subcellular and Extracellular Localization

- **Site of action (intracellular):** the reaction occurs in the **lumen of the Golgi apparatus** of mammary epithelial cells, where UDP-galactose is available. Lactose "is synthesized in the Golgi of mammary epithelial cells by lactose synthase from glucose and UDP galactose," and α-lactalbumin co-localizes with Golgi markers (58K protein, GM130) and with the GLUT8 glucose transporter at the cis-Golgi lactose-synthase complex (Villagrán et al. 2019, PMID 31020623). Its catalytic partner β4GalT1 is a trans-Golgi type II membrane protein (PMID 18393823).
- **Secretory routing:** α-Lactalbumin is synthesized as a **precursor with a cleaved N-terminal signal peptide** (UniProt P29752: signal 1–20; secreted mature chain 21–143), directing it through the ER → Golgi secretory pathway. Pulse-chase studies show α-lactalbumin is sequestered within membrane-bound secretory vesicles and secreted ~30 min after synthesis (Boulton et al. 1984, PMID 6477529).
- **Extracellular destination:** It is ultimately **secreted into milk** as one of the major whey proteins (~0.8 mg/ml in mouse milk; PMID 10085224).

Thus Lalba acts **intracellularly (Golgi lumen)** as the specifier subunit and is also **exported extracellularly** into milk.

---

## 4. Biological Process / Pathway Context

### 4.1 Lactose biosynthesis and the osmotic control of milk volume

Lactose is the **major osmole of milk**. Because the Golgi membrane is relatively impermeant to lactose, **intravesicular lactose synthesis osmotically draws water into Golgi-derived secretory vesicles, causing them to swell before exocytosis** — directly coupling the rate of lactose production to the aqueous volume (yield) of milk (Holt 1983, PMID 6876831). This mechanistic link explains why *Lalba* ultimately governs milk volume.

### 4.2 Genetic proof of the primary function (mouse knockout)

Targeted deletion of the mouse *Lalba* gene provides definitive in vivo evidence: **homozygous null females are α-lactalbumin-deficient, produce reduced amounts of thickened (highly viscous) milk containing little or no lactose, and cannot sustain their offspring** (Stacey et al. 1995, PMID 7708733). Replacement with the human α-lac gene (humanized allele) restores normal lactation, and expression is gene-dosage dependent, with increased expression slightly increasing milk volume (PMID 7708733). An independent α-lac-deficient line likewise produces **lactose-free, viscous milk with a shortened lactation period** (Soulier et al. 1999, PMID 10095792), and a bovine α-lac transgene rescues lactation in deficient mice (PMID 9120073). These results establish that α-lactalbumin is **required for lactose synthesis** and that lactose is essential for normal milk production and offspring survival.

### 4.3 Upstream regulation: lactogenic hormone signaling

*Lalba* is a **committed, hormonally gated effector** of lactation rather than a signaling molecule. Its transcription is strongly induced during functional differentiation of the mammary gland by **lactogenic hormones — principally prolactin acting through the prolactin receptor (PRLR) and the JAK2/STAT5 pathway** (together with insulin and glucocorticoid):

- Insulin + hydrocortisone + prolactin induce α-lactalbumin mRNA several-hundred-fold in mammary explants (Shao et al. 2013, PMID 23063409).
- Prolactin induces α-lactalbumin dose-dependently in mammary epithelial cells (PMID 26641038).
- Conditional repression of STAT5 during lactation reduces α-lactalbumin expression and slows neonate growth (Reichenstein et al. 2011, PMID 21688337).

Accordingly, Lalba sits **downstream** of the prolactin–PRLR–STAT5 program as its biochemical output.

### 4.4 Substrate supply

Glucose supply to the Golgi lactose-synthase complex is provided by glucose transporters (GLUT1 and GLUT8), which are co-regulated with lactation and localize with the lactose-synthase machinery (PMID 31020623). UDP-galactose is generated by the Leloir pathway and imported into the Golgi; its supply can be rate-limiting for lactose synthesis (Mohammad et al. 2012, PMID 22649065).

---

## 5. Structure, Evolution, and Mouse-Sequence Evidence

### 5.1 A calcium-binding, lysozyme-fold protein that lost muramidase activity

α-Lactalbumin belongs to the **c-type lysozyme superfamily (glycosyl hydrolase 22 family)** and adopts the lysozyme fold, yet it has **no muramidase (glycosidase) activity** — it was evolutionarily repurposed from an ancestral lysozyme by gene duplication within the mammalian lysozyme gene family, acquiring a divergent regulatory function (Irwin et al. 2011, PMID 21676251; Prager & Jollès 1996, PMID 8765292). High-resolution X-ray structures show it binds a **single Ca²⁺ ion in a "novel" calcium-binding loop** (slightly distorted pentagonal-bipyramidal coordination, Ca–O distances 2.2–2.6 Å) that superficially resembles an EF-hand but is instead derived from the homologous loop of c-type lysozyme (Stuart et al. 1986, PMID 3785375; Acharya et al. 1989, PMID 2769757). Ca²⁺ binding stabilizes the native fold required for productive interaction with β4GalT1; conversely, loss of Ca²⁺ promotes the partially unfolded (molten-globule) state.

### 5.2 Direct confirmation from the mouse P29752 sequence

Analysis of the mouse UniProt record (143-aa precursor) independently confirms all functional hallmarks at the mouse-sequence level:

- **Signal peptide (residues 1–20)** cleaved to a **123-aa secreted mature chain (21–143)**, annotated as a C-type lysozyme domain — consistent with Golgi routing and milk secretion.
- **Ca²⁺-binding loop** formed by mature residues **Lys79, Asp82, Asp87, Asp88** (the aspartate-rich "DKLLDDELDDD" motif) — the canonical α-lactalbumin calcium loop.
- **Four disulfide bonds** (mature Cys6–Cys120, Cys28–Cys111, Cys61–Cys77, Cys73–Cys91) matching the conserved c-type lysozyme disulfide pattern.
- **One N-glycosylation site** (Asn65 in precursor numbering).
- Secondary-structure annotation shows the expected **α+β lysozyme fold** (four α-helices plus a small β-sheet).
- The functionally critical **monosaccharide (glucose)-binding residues Phe31 and His32** (mature numbering) implicated in lactose synthase (PMID 8805552) are **conserved in the mouse sequence**, directly linking the mouse ortholog to the glucose-binding/specifier mechanism derived from other mammalian structures.

These features corroborate, at the level of the actual mouse protein, the structural/mechanistic roles established from bovine/human/baboon crystal structures.

---

## 6. A Note on Moonlighting Activity (HAMLET) — Not the Primary Function

When α-lactalbumin **partially unfolds** (e.g., upon Ca²⁺ release and low pH) and binds **oleic acid**, it forms **HAMLET** (Human Alpha-lactalbumin Made LEthal to Tumor cells), a protein–lipid complex selectively toxic to tumor cells (Ho et al. 2012, PMID 23130929; Nadeem et al. 2019, PMID 31082436). Evidence indicates the **oleic acid cofactor is the principal cytotoxic agent**, with the protein acting as a solubilizing carrier (El-Fakharany & Redwan 2019, PMID 35539089; Hoque et al. 2013, PMID 24039698). This is a **gain-of-function of a conformationally altered, non-native state** — not the physiological function of Lalba — and is most relevant to human/bovine α-lactalbumin as a therapeutic. It is included here only for completeness and to avoid conflating it with the primary lactose-synthase specifier role.

---

## 7. Supported and Refuted Hypotheses

**Supported (high confidence, multiple independent lines of evidence):**
- H1. Lalba is the non-catalytic regulatory subunit of lactose synthase. — *Supported* (crystallography, kinetics, biochemistry; PMIDs 11419947, 18393823, 818085).
- H2. Lalba changes β4GalT1 acceptor specificity from GlcNAc to glucose to make lactose. — *Supported* (PMIDs 11419947, 16497331).
- H3. Lalba function/site of action is the Golgi lumen of mammary epithelial cells; the protein is secreted into milk. — *Supported* (PMIDs 31020623, 6477529; UniProt signal peptide).
- H4. Lalba is genetically required for milk lactose and successful lactation. — *Supported* (mouse knockout; PMIDs 7708733, 10095792, 9120073).
- H5. Lactose (enabled by Lalba) osmotically determines milk volume. — *Supported* (PMIDs 6876831, 7708733).
- H6. Lalba expression is controlled by prolactin/STAT5 lactogenic signaling. — *Supported* (PMIDs 23063409, 21688337, 26641038).
- H7. Lalba is a Ca²⁺-binding lysozyme-fold protein without muramidase activity. — *Supported* (PMIDs 3785375, 21676251; mouse sequence analysis).

**Refuted / excluded:**
- Lalba is itself a catalytic glycosyltransferase/hydrolase. — *Refuted*: it is non-catalytic and lacks the muramidase activity of its lysozyme ancestor (PMIDs 18393823, 21676251).
- HAMLET tumoricidal activity is the native cellular function of Lalba. — *Refuted/clarified*: it requires non-native partial unfolding + oleic acid and is not the physiological role (PMIDs 23130929, 35539089).

---

## 8. Limitations and Future Directions

- Several atomic-resolution mechanistic studies (crystallography, kinetics) were performed with **bovine, human, or baboon** α-lactalbumin; the mouse ortholog is highly conserved and the mouse genetic data (knockout) are definitive, but a mouse-specific lactose-synthase crystal structure is not the basis of the mechanistic claims. The mouse UniProt sequence analysis directly confirms conservation of the functional residues.
- Quantitative mouse-specific kinetic constants (Kₘ for glucose with/without α-lactalbumin) are drawn from bovine enzymology.
- Fine regulation (e.g., the precise transcription-factor complement at the mouse "milk-box"/STAT5 elements) and any post-secretory roles of milk α-lactalbumin in the neonate were not exhaustively surveyed.

---

## 9. Key References (PMIDs)

- 11419947 — Ramakrishnan & Qasba, crystal structure of lactose synthase (specificity switch mechanism).
- 18393823 — Qasba et al., structure/function of β-1,4-galactosyltransferase and α-lactalbumin.
- 16497331 — Ramakrishnan et al., structural snapshots / pentenary complex with α-lactalbumin.
- 818085 / 932002 — Bell et al.; Powell & Brew, kinetic mechanism and metal/α-lactalbumin binding.
- 7708733 — Stacey et al., *Lalba*-null and humanized mice (definitive genetic proof).
- 10095792 / 9120073 — Soulier et al., α-lac-deficient mice; bovine transgene rescue.
- 31020623 — Villagrán et al., Golgi localization and glucose transporters.
- 6477529 — Boulton et al., secretory-pathway transit of α-lactalbumin.
- 6876831 — Holt, lactose-driven osmotic swelling of Golgi vesicles / milk volume.
- 23063409 / 21688337 / 26641038 — lactogenic hormone (prolactin/STAT5) induction of α-lactalbumin.
- 1398111 / 2845947 / 10085224 — mouse gene isolation; milk-box promoter; expression level.
- 3785375 / 2769757 / 8805552 — α-lactalbumin calcium loop and lysozyme-fold structures.
- 21676251 / 8765292 — evolution within the lysozyme gene family.
- 23130929 / 31082436 / 35539089 / 24039698 / 34103518 — HAMLET moonlighting activity (non-native).


## Artifacts

- [OpenScientist final report](Lalba-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lalba-deep-research-openscientist_artifacts/final_report.pdf)