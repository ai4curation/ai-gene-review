---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:14:57.293919'
end_time: '2026-10-24T04:51:07.836887'
duration_seconds: 2170.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: LALBA
  gene_symbol: LALBA
  uniprot_accession: P00709
  protein_description: 'RecName: Full=Alpha-lactalbumin; AltName: Full=Lactose synthase
    B protein; AltName: Full=Lysozyme-like protein 7; Flags: Precursor;'
  gene_info: Name=LALBA; Synonyms=LYZL7;
  organism_full: Homo sapiens (Human).
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
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: LALBA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: LALBA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P00709
- **Protein Description:** RecName: Full=Alpha-lactalbumin; AltName: Full=Lactose synthase B protein; AltName: Full=Lysozyme-like protein 7; Flags: Precursor;
- **Gene Information:** Name=LALBA; Synonyms=LYZL7;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glycosyl hydrolase 22 family.
- **Key Domains:** Glyco_hydro_22. (IPR001916); Glyco_hydro_22_CS. (IPR019799); Lactalbumin. (IPR000545); Lysozyme-like_dom_sf. (IPR023346); Lys (PF00062)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LALBA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LALBA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LALBA** (gene ID: LALBA, UniProt: P00709) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# LALBA (α-Lactalbumin, UniProt P00709): Functional Annotation Report

## Summary

Human **LALBA** (UniProt **P00709**; gene synonym *LYZL7*) encodes **α-lactalbumin (α‑LA)**, a small (~14 kDa), secreted, calcium-binding whey protein that functions as the **regulatory "B" subunit of lactose synthase** (EC 2.4.1.22). α‑Lactalbumin is not itself a catalytic enzyme. Instead, it is a **specificity-modifier protein**: it forms a 1:1 complex with the catalytic enzyme **β-1,4-galactosyltransferase-1 (β4Gal‑T1)** and reprograms that enzyme's acceptor-substrate specificity. In the absence of α‑LA, β4Gal‑T1 preferentially transfers galactose from UDP-galactose onto *N*-acetylglucosamine (GlcNAc) to make *N*-acetyllactosamine. When α‑LA binds, the complex instead transfers galactose onto free **glucose**, producing **lactose (Galβ1→4Glc)** — the dominant carbohydrate of milk. This is the protein's primary, physiologically essential function.

Structurally, α‑lactalbumin is a paradox worth emphasizing: it is a **catalytically dead homolog of c-type lysozyme**. It shares 35–40% sequence identity and a nearly superimposable three-dimensional fold with hen egg-white lysozyme (a glycoside hydrolase, family GH22), yet it has lost the ability to bind and cleave glycosidic bonds. Evolution has repurposed the lysozyme scaffold into a glucose-presenting cofactor. α‑LA is a **metalloprotein** with a strong, structurally critical Ca²⁺-binding site (a distinctive non-EF-hand loop) and a separate, destabilizing Zn²⁺ site, giving it a well-known propensity to adopt a partially folded "molten-globule" state. It carries out its lactose-synthetic function in the **trans-Golgi lumen of lactating mammary secretory epithelial cells**, after which it is secreted into milk as the major whey protein, where it additionally serves as a source of essential amino acids (notably tryptophan and cysteine) and bioactive peptides for the nursing infant.

Two functional caveats frame the annotation. First, α‑LA's lactose-synthetic role is **conditionally expressed**: it is switched on only in terminally differentiated, lactating mammary epithelium under the control of the lactogenic hormone triad (insulin + hydrocortisone + prolactin) acting through the prolactin→Stat5 pathway. Second, α‑LA has a well-documented conformation-dependent **"moonlighting" activity**: in a partially unfolded state complexed with oleic acid it forms **HAMLET** (Human α‑lactalbumin Made LEthal to Tumor cells), a tumoricidal and antibacterial complex. This activity derives from the molten-globule conformation carrying a fatty acid — not from any native enzymatic function — and should be considered distinct from the protein's physiological role in milk sugar synthesis.

---

## Identity Verification

The research target was fully verified. The gene symbol **LALBA** matches the UniProt description (Alpha-lactalbumin / Lactose synthase B protein / Lysozyme-like protein 7 = LYZL7). The organism is confirmed **Homo sapiens**. The protein-family and domain annotations (glycosyl hydrolase 22 family; Glyco_hydro_22, Lactalbumin, Lysozyme-like domains; Lys/PF00062) are **fully consistent** with the literature, which independently establishes the c-type-lysozyme fold and GH22 membership. There was **no ambiguity** and no conflation with a different gene — the published literature for human α‑lactalbumin aligns precisely with the provided UniProt identity.

---

## Key Findings

### Finding 1 — α-Lactalbumin is the regulatory subunit of lactose synthase

UniProt P00709 (human LALBA; synonym LYZL7) is annotated as the "Lactose synthase B protein," and the primary literature confirms this directly. α‑Lactalbumin forms a **1:1 heterodimeric complex** with the catalytic galactosyltransferase to constitute the functional **lactose synthase** enzyme system. Critically, recombinant human α‑LA expressed in a heterologous host (transgenic tobacco) was shown to be **"fully active in the synthesis of lactose when combined with galactosyltransferase"** [PMID: 9538226](https://pubmed.ncbi.nlm.nih.gov/9538226/). This establishes that the α‑LA polypeptide itself — independent of any mammalian post-translational modification — carries the information needed to confer lactose-synthetic capacity on the catalytic partner. The same work explicitly describes α‑LA as **"a major milk protein… the regulatory subunit of lactose synthase."**

This is the central annotation: α‑LA is a **regulatory/specificity subunit**, not a catalyst. It supplies substrate-specificity control rather than chemical catalysis.

### Finding 2 — α-LA switches β4Gal-T1 acceptor specificity from GlcNAc to glucose

The molecular mechanism is now understood at atomic resolution. Crystal structures of lactose synthase at ~2 Å show that **α-LA promotes the binding of glucose to β4Gal-T1, thereby altering the enzyme's sugar-acceptor specificity from N-acetylglucosamine (GlcNAc) to glucose, which enables the complex to synthesize lactose** [PMID: 11419947](https://pubmed.ncbi.nlm.nih.gov/11419947/). α‑LA holds the glucose acceptor in place via hydrogen bonding with the glucose O-1 hydroxyl in the acceptor site. Binding of α‑LA is coupled to a **large conformational change** in β4Gal‑T1 (a flexible loop closing over the active site).

Quantitatively, α‑LA has a dramatic kinetic effect. It **increases β4Gal-T1's glucosyltransferase activity almost 30-fold** and lowers the Km for the glucose acceptor by a comparable factor [PMID: 11485999](https://pubmed.ncbi.nlm.nih.gov/11485999/). This converts a minor side-reaction of β4Gal‑T1 (which has very low intrinsic activity toward glucose) into the dominant, biologically productive reaction. Later structural "snapshots" of β4Gal‑T1 along its kinetic pathway, including a pentenary complex with α‑lactalbumin, further detail how Mn²⁺ coordination and loop closure create the active ground-state geometry for catalysis [PMID: 16497331](https://pubmed.ncbi.nlm.nih.gov/16497331/).

| Property | β4Gal-T1 alone | β4Gal-T1 + α-LA (lactose synthase) |
|---|---|---|
| Preferred acceptor | GlcNAc | Free glucose |
| Product | N-acetyllactosamine (Galβ1→4GlcNAc) | **Lactose (Galβ1→4Glc)** |
| Relative activity toward glucose | baseline (low) | **~30-fold increased** |
| Km for glucose acceptor | high | **~30-fold lowered** |
| Donor substrate | UDP-galactose | UDP-galactose |
| Metal cofactor | Mn²⁺ | Mn²⁺ |

### Finding 3 — α-LA is essential for lactose synthesis and milk production in vivo

The in vivo requirement for α‑LA was established definitively by gene knockout. Mice homozygous for a targeted deletion of the α‑lactalbumin gene are **"α-lac-deficient, produce reduced amounts of thickened milk containing little or no lactose, and cannot sustain their offspring,"** providing **"definitive evidence that α-lac is required for lactose synthesis and that lactose is important for milk production"** [PMID: 7708733](https://pubmed.ncbi.nlm.nih.gov/7708733/). Because lactose is osmotically active and is the principal osmole drawing water into the milk, loss of lactose synthesis produces a low-volume, abnormally viscous ("thickened") milk that cannot support the pups.

Crucially, the same study showed that **"females homozygous for the humanized allele lactate normally, indicating that human α-lac can replace murine α-lac."** This cross-species rescue demonstrates that the human P00709 protein performs the identical function and that the mechanism is evolutionarily conserved.

### Finding 4 — α-LA has a c-type lysozyme fold and a unique Ca²⁺ site, but no hydrolase activity

High-resolution X-ray crystallography of baboon/human α‑lactalbumin at 1.7 Å reveals a **two-domain architecture (an α-helical domain and a small β-sheet domain)** that is essentially the **c-type lysozyme fold** [PMID: 2769757](https://pubmed.ncbi.nlm.nih.gov/2769757/). A **tightly bound Ca²⁺ ion** sits in a distorted pentagonal-bipyramidal coordination geometry in a loop between the two domains. Importantly, this calcium-binding fold **"resembles an EF-hand only superficially and presumably has no evolutionary relationship with it"** — rather, it shows **"clear homology with the corresponding loop in c-type lysozyme (the 'parent' molecule of α-lactalbumin)"** [PMID: 3785375](https://pubmed.ncbi.nlm.nih.gov/3785375/). This is an example of a novel, convergent calcium site built on a lysozyme scaffold.

Despite the shared fold, α‑LA has lost enzyme activity: **"Lysozymes bind and cleave the glycosidic bond linkage in sugars, whereas alpha-lactalbumin does not bind sugar but participates in the synthesis of lactose. Alpha-lactalbumin is a metallo-protein and binds calcium"** [PMID: 10195284](https://pubmed.ncbi.nlm.nih.gov/10195284/). This places α‑LA firmly in the **glycosyl hydrolase 22 (GH22) family** by structure and ancestry (consistent with the Glyco_hydro_22 / Lysozyme-like domains in the UniProt annotation), while functionally it is a **catalytically dead, substrate-presenting cofactor**. The evolutionary transition from an enzyme (lysozyme) to a regulatory protein (α‑LA) is a classic case study in protein engineering and evolution [PMID: 3678590](https://pubmed.ncbi.nlm.nih.gov/3678590/).

### Finding 5 — A secondary Zn²⁺ site links metal binding to the molten-globule state

In addition to the strong structural Ca²⁺ site, α‑lactalbumin possesses a **separate, strong Zn²⁺-binding site** (association constant ~5×10⁵ M⁻¹). Occupancy of this and other secondary sites by zinc has a strongly destabilizing effect: **"The binding of zinc at secondary sites is accompanied by destabilization of the protein structure and progressive protein aggregation… reflected in a shift of the thermal denaturation transition temperature by more than 40 degrees"** [PMID: 7945790](https://pubmed.ncbi.nlm.nih.gov/7945790/). Fluorescence energy-transfer measurements place the strong Zn²⁺ (Co²⁺) site **14–18 Å from the Ca²⁺ site, "in excellent agreement with recent crystallographic data for human alpha-lactalbumin."** Other heavy-metal ions (Pb²⁺, Hg²⁺) compete at the Ca²⁺ and Zn²⁺ sites and decrease thermal stability [PMID: 8876980](https://pubmed.ncbi.nlm.nih.gov/8876980/).

This metal-dependent conformational plasticity is mechanistically significant. Ca²⁺ binding **stabilizes** the native fold (and is required for efficient folding), whereas Zn²⁺ binding **destabilizes** it toward the partially folded molten-globule state. This "metal switch" underlies α‑LA's famous conformational malleability, and it is directly relevant to the moonlighting HAMLET activity (Finding 6), which requires a partially unfolded conformation.

### Finding 6 — Moonlighting: partially unfolded α-LA + oleic acid forms the tumoricidal HAMLET complex

α‑Lactalbumin has a well-studied non-canonical activity. In a **partially unfolded (molten-globule) state complexed with oleic acid**, human α‑LA forms **HAMLET** (Human α-lactalbumin Made LEthal to Tumor cells), which **"has potent tumoricidal activity"** and also kills some Gram-positive bacteria [PMID: 34103518](https://pubmed.ncbi.nlm.nih.gov/34103518/). A 39-residue α-helical peptide derived from α‑LA forms oleate complexes (α1-oleate) that retain tumoricidal activity and reached safety/efficacy endpoints in a Phase I/II bladder cancer trial (NCT03560479). Related complexes include BAMLET (bovine α‑LA–oleic acid) and liposome-delivered formulations.

Mechanistically, it is important to note that this cytotoxicity is **conformation- and lipid-dependent, not an intrinsic enzymatic property of the protein**: **"the protein portion of HAMLET, GAMLET, and the other HAMLET-like protein-oleic acid complexes is not the origin of their cytotoxicity"** [PMID: 23580643](https://pubmed.ncbi.nlm.nih.gov/23580643/). The oleic acid, delivered by the fluid protein scaffold, drives the toxicity. HAMLET is therefore best classified as a **moonlighting activity** distinct from LALBA's native physiological function in lactose synthesis.

### Finding 7 — α-LA is the major human-milk whey protein and a source of amino acids and bioactive peptides

Beyond its catalytic-cofactor role, secreted α‑LA is nutritionally central. An authoritative review notes that **"α-Lactalbumin is a whey protein that constitutes approximately 22% of the proteins in human milk and approximately 3.5% of those in bovine milk,"** and that **"within the mammary gland, α-lactalbumin plays a central role in milk production as part of the lactose synthase complex required for lactose formation, which drives milk volume"** [PMID: 29617841](https://pubmed.ncbi.nlm.nih.gov/29617841/). It is a rich source of tryptophan, lysine, branched-chain and sulfur amino acids. Upon digestion it **"is digested into smaller peptides with antimicrobial and prebiotic activities, immunostimulatory effect and acting as enhancers of mineral absorption"** [PMID: 21335989](https://pubmed.ncbi.nlm.nih.gov/21335989/). Its tryptophan richness modulates tryptophan/serotonin metabolism in developing infants, increasing circulating tryptophan and striatal serotonin in feeding models [PMID: 40610456](https://pubmed.ncbi.nlm.nih.gov/40610456/). These are secondary (nutritional/bioactive) roles of the secreted protein, downstream of its primary enzymatic-cofactor function.

### Finding 8 — Expression is confined to lactating mammary tissue by lactogenic hormones (prolactin/Stat5)

α‑Lactalbumin synthesis is a hallmark of terminal mammary differentiation. In mouse mammary explant cultures, **"functional differentiation was determined by the induction of casein and alpha-lactalbumin synthesis in the insulin, hydrocortisone, and prolactin (IFPrl)-treated explant cultures"** [PMID: 3034921](https://pubmed.ncbi.nlm.nih.gov/3034921/). α‑LA is a pregnancy/lactation-specific gene product [PMID: 6430550](https://pubmed.ncbi.nlm.nih.gov/6430550/). Consistent with control by the prolactin→Stat5 axis, disrupting ErbB4→Stat5 signaling abolishes expression: in such mice **"whey acidic protein mRNA was reduced, and alpha-lactalbumin mRNA was undetectable"** at mid-lactation [PMID: 10508857](https://pubmed.ncbi.nlm.nih.gov/10508857/). This hormonal gating ensures that the lactose-synthase B-subunit — and therefore lactose production — is restricted to lactating mammary epithelium.

### Finding 9 — Consolidated annotation

Convergent experimental, structural, genetic, and evolutionary evidence supports a single coherent annotation: **LALBA/α-lactalbumin is the regulatory B-subunit of lactose synthase (EC 2.4.1.22), acting in the mammary trans-Golgi**. (1) Isolated α‑LA confers lactose-synthesis activity on galactosyltransferase [PMID: 9538226]; (2) crystal structures show it switches β4Gal‑T1 acceptor specificity GlcNAc→glucose [PMID: 11419947, 11485999, 16497331]; (3) gene knockout abolishes milk lactose and lactation, rescued by the human gene [PMID: 7708733]; (4) it is a Ca²⁺/Zn²⁺ metal-binding, catalytically inactive c-type lysozyme homolog (GH22) [PMID: 2769757, 3785375, 10195284, 7945790]; (5) expression is restricted to lactating mammary epithelium by prolactin/Stat5 lactogenic signaling [PMID: 3034921, 10508857]. A conformation-dependent HAMLET activity is distinct from the native function [PMID: 34103518, 23580643].

---

## Mechanistic Model / Interpretation

### The core reaction

Lactose synthase catalyzes, in the mammary Golgi:

```
   UDP-galactose  +  D-glucose   ──(β4Gal-T1 + α-LA, Mn²⁺)──►   Lactose (Galβ1→4Glc)  +  UDP
```

α‑Lactalbumin does not participate in the chemistry. Its role is purely one of **substrate specificity control** and **acceptor presentation**:

```
  WITHOUT α-LA:                           WITH α-LA (lactose synthase):
  ┌───────────────┐                       ┌───────────────┐   ┌────────┐
  │   β4Gal-T1    │                       │   β4Gal-T1    │───│  α-LA  │
  │  (open loop)  │                       │ (closed loop) │   │(Ca²⁺)  │
  └──────┬────────┘                       └──────┬────────┘   └───┬────┘
         │ acceptor = GlcNAc                     │ acceptor = Glc │
         ▼                                       ▼  (held by H-bond to O1)
   N-acetyllactosamine                          LACTOSE
   (glycan elongation)                          (milk sugar)
```

The binding of α‑LA (1) triggers closure of β4Gal‑T1's flexible loop into the catalytically competent conformation and (2) creates a composite acceptor pocket that favors small, unmodified glucose over GlcNAc by hydrogen-bonding to the glucose O-1 hydroxyl. The net effect — a ~30-fold rate enhancement and ~30-fold drop in Km for glucose — rechannels the enzyme's output from glycan elongation to free-disaccharide synthesis.

### Evolution: enzyme → cofactor

α‑Lactalbumin is a textbook example of evolutionary **neofunctionalization on a conserved scaffold**:

| Feature | c-type lysozyme (ancestor) | α-lactalbumin (P00709) |
|---|---|---|
| Fold | α+β, two-domain lysozyme fold | Essentially identical fold |
| Sequence identity | — | 35–40% to lysozyme |
| GH22 family | Yes (active glycosidase) | Yes (by homology; catalytically dead) |
| Substrate | Binds & cleaves peptidoglycan glycosidic bonds | Does **not** bind sugar; cannot hydrolyze |
| Metal | — | Strong structural Ca²⁺ (non-EF-hand loop) + destabilizing Zn²⁺ site |
| Function | Antibacterial hydrolase | Specificity modifier of β4Gal-T1 |

The lysozyme catalytic machinery was lost, and a high-affinity Ca²⁺ loop plus a glucose-presenting surface were gained, converting an enzyme into a regulatory partner protein.

### Localization and physiological integration

```
 Prolactin ──► PRLR ──► JAK2 ──► STAT5  ──► LALBA transcription
 (Insulin + Hydrocortisone permissive)        │
                                              ▼
            Lactating mammary secretory epithelial cell
            ┌──────────────────────────────────────────┐
            │  trans-Golgi lumen:                       │
            │     α-LA + β4Gal-T1 + UDP-Gal + Glc       │
            │              │                            │
            │              ▼                            │
            │           LACTOSE  ──► osmotic draw of    │
            │                        water into Golgi   │
            │                        vesicles           │
            └───────────────┬──────────────────────────┘
                            ▼  secretion
            Milk:  lactose (volume) + α-LA whey protein
                   (Trp/Cys source, bioactive peptides, HAMLET potential)
```

α‑LA carries out its catalytic-cofactor function **intracellularly, in the trans-Golgi lumen** of the secretory epithelial cell, co-localized with the membrane-anchored β4Gal‑T1. The lactose it helps generate is osmotically active and draws water into secretory vesicles, which is why lactose production **drives milk volume** — and why its loss yields low-volume, thickened milk in knockouts. The α‑LA protein is then **secreted into milk**, where it takes on its secondary nutritional and bioactive roles extracellularly, in the infant gut.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [9538226](https://pubmed.ncbi.nlm.nih.gov/9538226/) | Expression of human α-LA in transgenic tobacco | Recombinant α-LA is "fully active in lactose synthesis when combined with galactosyltransferase"; names it the regulatory subunit of lactose synthase (F1, F9) |
| [11419947](https://pubmed.ncbi.nlm.nih.gov/11419947/) | Crystal structure of lactose synthase | Atomic mechanism: α-LA switches β4Gal-T1 acceptor specificity GlcNAc→glucose; large conformational change (F2, F9) |
| [11485999](https://pubmed.ncbi.nlm.nih.gov/11485999/) | β4Gal-T1·LA crystal structure with UDP-Glc | Quantifies ~30-fold activity increase toward glucose acceptor (F2) |
| [16497331](https://pubmed.ncbi.nlm.nih.gov/16497331/) | Structural snapshots of β4Gal-T1 | Kinetic-pathway structures incl. α-LA pentenary complex; Mn²⁺/loop dynamics (F2) |
| [7708733](https://pubmed.ncbi.nlm.nih.gov/7708733/) | α-LA knockout / humanized rescue in mice | In vivo proof: no lactose, no viable lactation; human gene rescues (F3, F9) |
| [2769757](https://pubmed.ncbi.nlm.nih.gov/2769757/) | Baboon α-LA structure at 1.7 Å vs lysozyme | Two-domain lysozyme fold; tightly bound Ca²⁺ (F4) |
| [3785375](https://pubmed.ncbi.nlm.nih.gov/3785375/) | Novel Ca²⁺-binding loop | Non-EF-hand Ca²⁺ site homologous to lysozyme loop (F4) |
| [10195284](https://pubmed.ncbi.nlm.nih.gov/10195284/) | MD simulation of α-LA vs lysozyme | α-LA does not bind sugar; is a Ca²⁺ metalloprotein (F4) |
| [3678590](https://pubmed.ncbi.nlm.nih.gov/3678590/) | From lysozyme to α-LA: engineering & evolution | Framing of enzyme→cofactor evolutionary transition (F4) |
| [7945790](https://pubmed.ncbi.nlm.nih.gov/7945790/) | Co²⁺ binding to α-LA | Strong Zn²⁺ site; >40 °C destabilization; 14–18 Å from Ca²⁺ (F5) |
| [8876980](https://pubmed.ncbi.nlm.nih.gov/8876980/) | Pb²⁺/Hg²⁺ binding to α-LA | Heavy metals compete at Ca²⁺/Zn²⁺ sites, reducing stability (F5) |
| [34103518](https://pubmed.ncbi.nlm.nih.gov/34103518/) | Bladder cancer therapy with α1-oleate | HAMLET/α1-oleate tumoricidal; Phase I/II trial (F6) |
| [23580643](https://pubmed.ncbi.nlm.nih.gov/23580643/) | Mechanisms of HAMLET cytotoxicity | Cytotoxicity is conformation/lipid-dependent, not from protein per se (F6) |
| [29617841](https://pubmed.ncbi.nlm.nih.gov/29617841/) | Applications for α-LA in human nutrition | Authoritative review: ~22% of human-milk protein; central lactose-synthase role drives milk volume (F7) |
| [21335989](https://pubmed.ncbi.nlm.nih.gov/21335989/) | Biological effects of bovine milk fractions | Digestion yields antimicrobial/prebiotic peptides; enhances mineral absorption (F7) |
| [40610456](https://pubmed.ncbi.nlm.nih.gov/40610456/) | α-LA, tryptophan & serotonin | Modulates Trp/serotonin metabolism in infants (F7) |
| [3034921](https://pubmed.ncbi.nlm.nih.gov/3034921/) | Functional differentiation of mammary epithelium | Insulin+hydrocortisone+prolactin induce α-LA synthesis (F8) |
| [10508857](https://pubmed.ncbi.nlm.nih.gov/10508857/) | ErbB4/Stat5 in mammary gland | Loss of ErbB4/Stat5 abolishes α-LA mRNA (F8) |
| [6430550](https://pubmed.ncbi.nlm.nih.gov/6430550/) | Pregnancy-specific gene expression | α-LA is a pregnancy/lactation-specific differentiation product (F8) |

**Supporting cross-species / mechanistic context:** The specificity-modifier concept is corroborated by the observation that α‑LA can reprogram related glycosyltransferases from other organisms — e.g., it induces the snail *Lymnaea stagnalis* β4-GalNAcT to act on glucose >100-fold more efficiently, producing a lactose analog [PMID: 8816760](https://pubmed.ncbi.nlm.nih.gov/8816760/) — demonstrating that the α‑LA interaction surface and the "acceptor-switching" mechanism are conserved features of this enzyme family. Early kinetic work on human milk galactosyltransferase also showed α‑LA switches specificity only for monosaccharide acceptors [PMID: 821753](https://pubmed.ncbi.nlm.nih.gov/821753/). Biophysical studies of α‑LA folding (rapid molten-globule collapse, Ca²⁺-accelerated folding) reinforce the metal-dependent conformational model underlying both native function and HAMLET formation [PMID: 10329172](https://pubmed.ncbi.nlm.nih.gov/10329172/), [PMID: 16731974](https://pubmed.ncbi.nlm.nih.gov/16731974/).

---

## Limitations and Knowledge Gaps

- **Human-specific in vivo data are indirect.** The definitive genetic proof (knockout and lack of lactose) comes from mouse. The human protein's sufficiency is demonstrated by the humanized-mouse rescue [PMID: 7708733] and by recombinant-protein activity assays [PMID: 9538226], but there is no human loss-of-function genetic model. Rare human LALBA variants and their phenotypic consequences are not well characterized in the reviewed literature.
- **LYZL7 synonym.** The UniProt synonym *LYZL7* (lysozyme-like 7) reflects the lysozyme homology, but the reviewed literature treats the protein uniformly as α‑lactalbumin; any distinct "lysozyme-like 7" functional role outside lactation was not substantiated here.
- **Quantitative kinetics.** The ~30-fold activity/Km effects derive largely from in vitro bovine/human enzyme assays; precise human physiological rate constants in the intact Golgi are not directly measured.
- **HAMLET physiology.** Whether HAMLET-type complexes form in vivo during normal milk digestion remains unproven; HAMLET is primarily a therapeutic/biophysical phenomenon rather than a confirmed endogenous function.
- **Zn²⁺ regulation in vivo.** The destabilizing Zn²⁺ site is characterized biophysically; its physiological role (e.g., in modulating secretion, folding, or molten-globule formation in the secretory pathway) is not established.

## Proposed Follow-up Experiments / Actions

1. **Human genetic association.** Survey human genomic/clinical databases (gnomAD, ClinVar) for LALBA loss-of-function or missense variants and correlate with lactation insufficiency or milk-composition phenotypes to provide direct human in vivo evidence.
2. **Cryo-EM/structural dynamics of the human complex.** Determine high-resolution structures of the intact human β4Gal‑T1·α‑LA·UDP-Gal·glucose complex (and trapped transition states) to refine the quantitative model of loop closure and glucose selection.
3. **Mutagenesis of the glucose-presenting interface.** Systematically mutate α‑LA residues predicted to hydrogen-bond the glucose O-1 and measure effects on the GlcNAc→glucose switch and on lactose yield, mapping the minimal specificity-determinant surface.
4. **Secretory-pathway cell model.** Use mammary epithelial organoids with endogenous prolactin/Stat5 signaling to measure α‑LA–dependent lactose flux and the osmotic/volume coupling in real time.
5. **Zn²⁺ and molten-globule physiology.** Test whether physiological Zn²⁺ fluxes in the secretory pathway modulate α‑LA conformation, secretion efficiency, or endogenous fatty-acid-complex (HAMLET-like) formation.
6. **Metabolic/neurodevelopmental follow-up.** Extend the tryptophan→serotonin findings [PMID: 40610456] to controlled human infant-feeding studies to quantify the nutritional (as opposed to enzymatic-cofactor) contribution of secreted α‑LA.

---

*Report prepared from a 5-iteration autonomous investigation: 9 confirmed findings, 34 papers reviewed. Gene identity (LALBA / P00709 / Homo sapiens / GH22) verified against all literature with no ambiguity.*


## Artifacts

- [OpenScientist final report](LALBA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](LALBA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9538226
2. PMID:11419947
3. PMID:11485999
4. PMID:16497331
5. PMID:7708733
6. PMID:2769757
7. PMID:3785375
8. PMID:10195284
9. PMID:3678590
10. PMID:7945790
11. PMID:8876980
12. PMID:34103518
13. PMID:23580643
14. PMID:29617841
15. PMID:21335989
16. PMID:40610456
17. PMID:3034921
18. PMID:6430550
19. PMID:10508857
20. PMID:8816760
21. PMID:10329172
22. PMID:16731974