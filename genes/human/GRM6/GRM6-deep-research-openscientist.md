---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T05:35:51.272524'
end_time: '2026-11-14T06:00:12.956485'
duration_seconds: 1461.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GRM6
  gene_symbol: GRM6
  uniprot_accession: O15303
  protein_description: 'RecName: Full=Metabotropic glutamate receptor 6; Short=mGluR6;
    Flags: Precursor;'
  gene_info: Name=GRM6; Synonyms=GPRC1F, MGLUR6;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 3 family.
  protein_domains: ANF_lig-bd_rcpt. (IPR001828); GPCR_3. (IPR000337); GPCR_3_9-Cys_dom.
    (IPR011500); GPCR_3_9-Cys_sf. (IPR038550); GPCR_3__mGluR6. (IPR000112)
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRM6-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRM6-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O15303
- **Protein Description:** RecName: Full=Metabotropic glutamate receptor 6; Short=mGluR6; Flags: Precursor;
- **Gene Information:** Name=GRM6; Synonyms=GPRC1F, MGLUR6;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 3 family.
- **Key Domains:** ANF_lig-bd_rcpt. (IPR001828); GPCR_3. (IPR000337); GPCR_3_9-Cys_dom. (IPR011500); GPCR_3_9-Cys_sf. (IPR038550); GPCR_3__mGluR6. (IPR000112)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GRM6" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GRM6' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GRM6** (gene ID: GRM6, UniProt: O15303) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GRM6 / mGluR6 (UniProt O15303): Functional Annotation Report

## Gene/Protein Identity Verification

- **UniProt:** O15303 — Metabotropic glutamate receptor 6 (mGluR6), precursor
- **Gene:** GRM6 (synonyms GPRC1F, MGLUR6); **Organism:** *Homo sapiens*
- **Family:** G-protein-coupled receptor family 3 (class C GPCR); domains ANF_lig-bd_rcpt (extracellular Venus-flytrap ligand-binding, IPR001828), GPCR_3 7TM (IPR000337), and the cysteine-rich 9-Cys linker domain (IPR011500), plus the mGluR6-specific signature IPR000112.

The gene symbol **GRM6 unambiguously matches** the protein described by UniProt O15303. All retrieved literature — retinal ON-bipolar-cell signaling, group III mGluR pharmacology, congenital stationary night blindness — is fully consistent with this identity, organism, family, and domain architecture. **No gene-symbol ambiguity was encountered.**

---

## Summary

**GRM6** encodes **metabotropic glutamate receptor 6 (mGluR6)**, an 877-residue **class C (group III) G-protein-coupled receptor (GPCR)** for the neurotransmitter **L-glutamate**. It is a *signaling receptor* — not an enzyme or transporter. Its sole physiologically characterized role is in vision: mGluR6 is the postsynaptic glutamate sensor at the **first synapse of the retinal ON (depolarizing) visual pathway**, located on the dendritic tips of **ON-bipolar cells** where they invaginate photoreceptor terminals in the outer plexiform layer (OPL).

The **primary function is sign-inverting signal transduction**. In darkness, photoreceptors release glutamate tonically; glutamate binds the extracellular "Venus-flytrap" domain of mGluR6, activating the heterotrimeric G-protein **Gαo**, which **closes the TRPM1 cation channel** and hyperpolarizes the ON-bipolar cell. In light, glutamate release falls, a GTPase-activating-protein (GAP) complex (RGS7/RGS11/R9AP, scaffolded by GPR179) deactivates Gαo, TRPM1 opens, and the bipolar cell depolarizes. mGluR6 thereby **inverts the sign** of the photoreceptor signal, creating the ON channel that reports light increments. This was proven genetically (mGluR6-knockout mice selectively lose the electroretinogram ON response) and biochemically (the Gαo→TRPM1 cascade and L-AP4/glutamate pharmacology).

Beyond ligand sensing, mGluR6 is the **organizing hub of a postsynaptic "signalplex"** (with TRPM1, nyctalopin, LRIT3, GPR179, and the Gαo/RGS machinery) and a **bidirectional trans-synaptic adhesion organizer** that binds presynaptic ELFN1/ELFN2 — an interaction requiring complex N-glycosylation acquired in the Golgi. Loss-of-function mutations in GRM6 cause **autosomal-recessive complete congenital stationary night blindness (CSNB1B; OMIM 257270)**, characterized by a selectively reduced ERG b-wave with preserved a-wave.

---

## Gene and Protein Architecture (database grounding)

Authoritative annotation (UniProt O15303, reviewed; Ensembl ENSG00000113262; NCBI GeneID 2916; HGNC:4598; OMIM gene 604096) describes an **877-amino-acid precursor** encoded by **GRM6 on human chromosome 5**. The protein has the canonical **class C GPCR topology**:

| Region | Approx. residues | Role |
|---|---|---|
| Extracellular ligand-binding region (Venus-flytrap + 9-Cys) | ~25–585 | Glutamate binding, dimerization, conformational relay |
| Seven transmembrane helices (7TM) | 586–845 | G-protein coupling |
| Cytoplasmic C-terminus | 846–877 | Intracellular signaling/interactions |

Four **N-glycosylation sites** are annotated (Asn296, Asn451, Asn479, Asn567), consistent with the experimentally demonstrated requirement for complex N-glycosylation in trafficking and ELFN binding. UniProt's curated function states it is a "*G protein-coupled receptor for glutamate… Signaling inhibits adenylate cyclase activity… Signaling stimulates TRPM1 channel activity and Ca²⁺ uptake. Required for normal vision,*" with curated subcellular locations spanning the **cell membrane, ER membrane, Golgi membrane, and dendrite** — mirroring the secretory-pathway trafficking and dendritic-tip destination described below. The gene maps to OMIM phenotype **257270 (CSNB1B)**.

---

## Key Findings

### 1. mGluR6 is the postsynaptic glutamate receptor essential and specific for the retinal ON visual pathway

The defining genetic evidence comes from targeted disruption of the *mGluR6* gene in mice (Masu et al., 1995). Homozygous mutants showed a **selective loss of the electroretinogram (ERG) ON response with a fully preserved OFF response**, and crucially *no* change in retinal cell organization or optic projection — demonstrating a purely functional (synaptic) deficit. The authors state: "*The homozygous mutant mice showed a loss of ON responses but unchanged OFF responses to light*" and "*mGluR6 is essential in synaptic transmission to the ON bipolar cell*" [PMID: 7889569](https://pubmed.ncbi.nlm.nih.gov/7889569/).

This places mGluR6 at the branch point where the visual signal splits into parallel ON and OFF channels. GRM6 is one of several genes of the depolarizing bipolar cell "signalplex" (NYX, GRM6, TRPM1, GPR179, LRIT3), loss of any of which causes complete congenital stationary night blindness — reinforcing that mGluR6 is a non-redundant, obligatory component of ON-pathway transmission.

### 2. mGluR6 signals through Gαo to gate the TRPM1 cation channel, inverting the photoreceptor signal

The downstream mechanism is defined at the level of specific players. In ON-bipolar cells, the heterotrimeric G-protein **Go (Gαo1/Gβ3/Gγ13)** couples mGluR6 to **TRPM1**. As Tummala et al. (2016) summarize: "*In retinal ON bipolar cells, Go couples the metabotropic receptor mGluR6 to the TRPM1 channel and closes it in the dark, thus hyperpolarizing the cell. Light, via GTPase-activating proteins, deactivates Go, opens TRPM1 and depolarizes the cell*" [PMID: 27037829](https://pubmed.ncbi.nlm.nih.gov/27037829/).

TRPM1 was identified as the transduction channel by Shen et al. (2009) using ERG and pharmacology with the mGluR6 agonists L-AP4/glutamate and group III antagonists; they showed that "*glutamate binds to a metabotropic receptor which couples to the closure of a cation-selective transduction channel*" [PMID: 19439586](https://pubmed.ncbi.nlm.nih.gov/19439586/).

The functional logic is a **sign inversion**: because glutamate (the dark signal) *closes* the depolarizing channel, light — which *reduces* glutamate — *opens* it. As a canonical Gi/o-coupled receptor, mGluR6 also inhibits adenylate cyclase (the generic group III output annotated in UniProt), but the physiologically decisive effector in ON-bipolar cells is **TRPM1 gating**, not cyclic AMP.

### 3. mGluR6 localizes to ON-bipolar dendritic tips and requires glycosylation and ELFN1 adhesion for synaptic targeting

mGluR6 functions at a precise site: "*the postsynaptic metabotropic glutamate receptor mGluR6, located at BC [bipolar cell] dendritic tips*" invaginating the photoreceptor terminal (Pindwarawala et al., 2025) [PMID: 39681475](https://pubmed.ncbi.nlm.nih.gov/39681475/). Delivery there is a regulated, multi-step process. CSNB missense mutations in the extracellular ligand-binding domain cause a **trafficking defect** — the mutant lacks complex N-glycosylation, bypasses the Golgi, fails to bind ELFN1, and mislocalizes: "*These mutants fail to bind ELFN1, consistent with lack of a necessary modification normally acquired in the Golgi. The same mutants were mislocalized in bipolar cells, explaining the loss of function in CSNB*" [PMID: 39681475](https://pubmed.ncbi.nlm.nih.gov/39681475/). The mGluR6 complex is further physically tethered to the presynaptic rod terminal via matrix proteins (Tummala et al., 2016 [PMID: 27037829](https://pubmed.ncbi.nlm.nih.gov/27037829/)).

### 4. GRM6 loss-of-function mutations cause autosomal-recessive complete congenital stationary night blindness

GRM6 is an established disease gene — one of the recessive genes (with TRPM1, GPR179, LRIT3) causing **complete (Schubert-Bornschein) CSNB** (night blindness, myopia, nystagmus; selectively reduced ERG b-wave with preserved a-wave). In a cohort of 122 patients, Katta et al. (2024) report "*X-linked (CACNA1F and NYX) and autosomal recessive (TRPM1, GRM6, GPR179 and CABP4) genotypes were identified*" [PMID: 38522615](https://pubmed.ncbi.nlm.nih.gov/38522615/).

Mouse models confirm causation. A homozygous missense *Grm6* variant (p.Arg346His) in the *nob* mouse abolishes scotopic b-waves while a-waves remain normal: "*Scotopic b waves were absent, whereas a waves remained normal, indicating intact rod function but impaired bipolar cell function*" (Lin et al., 2025) [PMID: 40923695](https://pubmed.ncbi.nlm.nih.gov/40923695/). AAV-*Grm6* gene therapy restores mGluR6 expression and the localization of partner proteins (TRPM1, GPR179, Gβ5, RGS7, RGS11, dystrophin) in *Grm6*-null mice (Varin et al., 2021) [PMID: 33729473](https://pubmed.ncbi.nlm.nih.gov/33729473/). The b-wave-specific defect with normal a-wave is the electrophysiological signature of a lesion at the mGluR6 synapse.

### 5. mGluR6 is a group III metabotropic glutamate receptor activated by glutamate and L-AP4, coupled to Gi/o

Pharmacologically, mGluR6 is a **group III mGluR**: selectively activated by **L-(+)-2-amino-4-phosphonobutyrate (L-AP4)** and glutamate and blocked by group III antagonists (CPPG, LY341495) (Shen et al., 2009 [PMID: 19439586](https://pubmed.ncbi.nlm.nih.gov/19439586/)). Recombinant mGluR6 expressed in Chinese hamster ovary cells was used to map structure-activity relationships that distinguish its selectivity from mGluR1/2; the study examined "*the signal transduction of mGluR1, mGluR2 and mGluR6 subtypes expressed in Chinese hamster ovary cells*" (Sekiyama et al., 1996) [PMID: 8730745](https://pubmed.ncbi.nlm.nih.gov/8730745/).

Coupling to TRPM1 is context-dependent. In non-retinal cells (human melanocytes), mGluR6 responds to L-AP4 and couples to TRPM1-mediated Ca²⁺ influx: "*treatment of melanocytes with L-AP4, a type III mGluR-selective agonist, enhances Ca(2+) uptake*" (Devi et al., 2013) [PMID: 23452348](https://pubmed.ncbi.nlm.nih.gov/23452348/). The coupling polarity reverses depending on whether Gαo is supplied — consistent with Gαo being the physiological transducer mediating channel *closure* in bipolar cells.

### 6. mGluR6 organizes a postsynaptic signalplex

mGluR6 is the receptor hub of an interdependent protein complex. Three structural dependencies have been mapped:

- **Nyctalopin (NYX)**, an extracellular leucine-rich-repeat protein, interacts directly with TRPM1 and positions it at DBC dendrites, acting as an accessory channel subunit: "*nyctalopin and TRPM1 interact directly, suggesting that nyctalopin is acting as an accessory TRP channel subunit critical for proper channel localization to the synapse*" (Pearring et al., 2011) [PMID: 21734298](https://pubmed.ncbi.nlm.nih.gov/21734298/).
- **LRIT3** interacts with and is required for nyctalopin expression, and thus for TRPM1 at all DBC dendritic tips (Hasan et al., 2020) [PMID: 31959619](https://pubmed.ncbi.nlm.nih.gov/31959619/).
- **GPR179** binds RGS7 and, with R9AP, scaffolds the **GAP complex (RGS7/RGS11)** that inactivates Go upon light: "*RGS7 binds to a conserved site in GPR179 and that RGS11 in vivo forms a complex only with R9AP. R9AP and GPR179 are further integrated via direct protein-protein interactions*" (Sarria et al., 2016) [PMID: 26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/).

This architecture explains why mutations in *any* signalplex gene produce a clinically indistinguishable CSNB phenotype: receptor (mGluR6), effector (TRPM1), channel-localization machinery (nyctalopin/LRIT3), and signal-termination machinery (GPR179/R9AP/RGS7/RGS11) are all mutually dependent.

### 7. mGluR6 is a dimeric class C GPCR activated by Venus-flytrap domain closure transmitted through a cysteine-rich linker

By homology to structurally characterized relatives, mGluR6 is a **constitutive dimer**; each protomer has a clamshell/"Venus-flytrap" ligand-binding domain (LBD). Glutamate binding closes the clamshell, and this closure — with reorientation of the dimer interface from resting to active — is the first step of activation: "*A 'clamshell' ligand-binding domain (LBD), which contains the ligand-binding site, is coupled to the transmembrane domain via a cysteine-rich domain, and LBD closure seems to be the first step in activation*" (Vafabakhsh et al., 2015) [PMID: 26258295](https://pubmed.ncbi.nlm.nih.gov/26258295/).

The **9-cysteine-rich domain** present in mGluR6 is the mechanical relay. Group II/III mGluR structures show "*the cysteine-rich domain, which is tightly linked to the ligand-binding domain by a disulfide bridge, suggesting a potential role in transmitting a ligand-induced conformational change into the downstream transmembrane region*" (Muto et al., 2007) [PMID: 17360426](https://pubmed.ncbi.nlm.nih.gov/17360426/). Mutagenesis of LBD residues contacting the glutamate α-amino and γ-carboxyl groups, and of dimer-interface residues, abolishes activation (Sato et al., 2003 [PMID: 12444084](https://pubmed.ncbi.nlm.nih.gov/12444084/); Kubo & Tateyama 2005 [PMID: 15922585](https://pubmed.ncbi.nlm.nih.gov/15922585/)).

### 8. mGluR6 engages in bidirectional trans-synaptic adhesion with presynaptic ELFN1/ELFN2, requiring complex N-glycosylation

mGluR6 is also a **trans-synaptic organizer**. The leucine-rich-repeat (LRR) and LRRCT regions of presynaptic **ELFN1** (expressed in rod photoreceptors) are necessary and sufficient to bind all group III mGluRs including mGluR6. The interaction is **bidirectional**: ELFN1 is required for mGluR6 dendritic-tip localization, and mGluR6 is required for presynaptic ELFN1 enrichment. In mGluR6-null mice ELFN1 only partially colocalizes with synapses, rescued by re-expressing mGluR6-EGFP in ON-bipolar cells: "*Our results demonstrate bidirectional mutual regulation of presynaptic enrichment of ELFN1 and postsynaptic enrichment of mGluR6 at photoreceptor synapses*" (Lee et al., 2025) [PMID: 40930976](https://pubmed.ncbi.nlm.nih.gov/40930976/).

This adhesion is glycosylation-gated. ELFN1/ELFN2 bind exclusively the **complex-N-glycosylated (Golgi-matured) form** of mGluR6: "*these proteins interact exclusively with the complex glycosylated form of mGluR6*" (Miller et al., 2024) [PMID: 38428819](https://pubmed.ncbi.nlm.nih.gov/38428819/). This links trafficking/glycosylation (Finding 3) to the trans-synaptic organizing function and explains why CSNB missense mutants that fail Golgi maturation also fail ELFN binding and synaptic targeting.

---

## Mechanistic Model / Interpretation

mGluR6 is a **sign-inverting signal transducer and synaptic organizer** at the photoreceptor→ON-bipolar-cell synapse. The diagram integrates Findings 1–8.

```
                PHOTORECEPTOR (rod/cone) terminal — PRESYNAPTIC
   ┌───────────────────────────────────────────────────────────────┐
   │   DARK: high tonic glutamate release                           │
   │   LIGHT: reduced glutamate release                             │
   │        ELFN1/ELFN2 (LRR adhesion) ───┐  (trans-synaptic)       │
   └──────────────────────────────────────┼────────────────────────┘
                   glutamate               │  binds only complex-
                      │                     │  glycosylated mGluR6
   ════════════════ synaptic cleft ════════╪══════════════════════
                      │            ELFN1 ⇄ mGluR6 (bidirectional)
                      ▼
   ┌───────────────────────────────────────────────────────────────┐
   │   ON-BIPOLAR CELL dendritic tip — POSTSYNAPTIC (invaginating)  │
   │                                                                │
   │   mGluR6 (dimer, class C GPCR)                                 │
   │     Venus-flytrap LBD → closes on glutamate                    │
   │         │ relayed via 9-Cys domain → 7TM                       │
   │         ▼                                                      │
   │     Gαo (Go: Gαo1/Gβ3/Gγ13)                                    │
   │         │ active (GTP) in DARK                                 │
   │         ▼                                                      │
   │     TRPM1 cation channel  ── CLOSED in dark → HYPERPOLARIZED   │
   │       (localized by nyctalopin/NYX; NYX needs LRIT3)          │
   │                                                                │
   │   LIGHT: glutamate ↓ → GAP complex (RGS7/RGS11 + R9AP,        │
   │          scaffolded by GPR179) deactivates Gαo →              │
   │          TRPM1 OPENS → Ca2+/Na+ influx → DEPOLARIZED           │
   └───────────────────────────────────────────────────────────────┘
                 ⇒ SIGN INVERSION: light = depolarization (ON channel)
```

**The logic.** The retina must encode both increments (ON) and decrements (OFF) of light from a single presynaptic variable — glutamate, which is *high* in darkness. OFF-bipolar cells use ionotropic (AMPA/kainate) receptors and follow glutamate (sign-conserving). ON-bipolar cells use mGluR6, a *metabotropic* receptor whose cascade **closes** a depolarizing channel in response to glutamate; thus falling glutamate (light) opens TRPM1 and depolarizes the cell — the sign inversion that creates the ON channel.

**Two layers of function.** The receptor performs (i) **acute signal transduction** (glutamate → Gαo → TRPM1), fast and reversible, and (ii) **structural organization** of the synapse: correct Golgi maturation/glycosylation and ELFN1/ELFN2 adhesion assemble and stabilize the invaginating synapse and recruit/retain TRPM1, nyctalopin, GPR179 and the RGS GAP module. The near-identical CSNB phenotype across signalplex genes reflects this mutual dependence.

---

## Evidence Base

| Finding | Key paper(s) | PMID | Nature of evidence |
|---|---|---|---|
| ON-pathway requirement | Masu et al. 1995 | [7889569](https://pubmed.ncbi.nlm.nih.gov/7889569/) | Gene knockout; ERG (direct genetic) |
| Gαo→TRPM1 sign inversion | Tummala 2016; Shen 2009 | [27037829](https://pubmed.ncbi.nlm.nih.gov/27037829/); [19439586](https://pubmed.ncbi.nlm.nih.gov/19439586/) | Cascade mapping; ERG/pharmacology |
| Dendritic-tip localization, glycosylation, trafficking | Pindwarawala 2025 | [39681475](https://pubmed.ncbi.nlm.nih.gov/39681475/) | CSNB-mutant cell biology |
| CSNB1B disease gene | Katta 2024; Lin 2025; Varin 2021 | [38522615](https://pubmed.ncbi.nlm.nih.gov/38522615/); [40923695](https://pubmed.ncbi.nlm.nih.gov/40923695/); [33729473](https://pubmed.ncbi.nlm.nih.gov/33729473/) | Patient cohorts; mouse model + therapy |
| Group III pharmacology (L-AP4) | Sekiyama 1996; Devi 2013 | [8730745](https://pubmed.ncbi.nlm.nih.gov/8730745/); [23452348](https://pubmed.ncbi.nlm.nih.gov/23452348/) | Recombinant CHO; melanocyte Ca²⁺ |
| Signalplex (NYX, LRIT3, GPR179) | Pearring 2011; Hasan 2020; Sarria 2016 | [21734298](https://pubmed.ncbi.nlm.nih.gov/21734298/); [31959619](https://pubmed.ncbi.nlm.nih.gov/31959619/); [26961947](https://pubmed.ncbi.nlm.nih.gov/26961947/) | Interaction + localization |
| Class C dimer / Venus-flytrap / 9-Cys relay | Vafabakhsh 2015; Muto 2007; Sato 2003; Kubo 2005 | [26258295](https://pubmed.ncbi.nlm.nih.gov/26258295/); [17360426](https://pubmed.ncbi.nlm.nih.gov/17360426/); [12444084](https://pubmed.ncbi.nlm.nih.gov/12444084/); [15922585](https://pubmed.ncbi.nlm.nih.gov/15922585/) | Structure + mutagenesis (homology) |
| Bidirectional ELFN1/2 adhesion; glycosylation-gated | Lee 2025; Miller 2024 | [40930976](https://pubmed.ncbi.nlm.nih.gov/40930976/); [38428819](https://pubmed.ncbi.nlm.nih.gov/38428819/) | Trans-synaptic biochemistry/genetics |

**Convergence.** Genetic (knockout, patient cohorts, *nob* mouse), pharmacological (L-AP4 selectivity), biochemical (Gαo/TRPM1 cascade, ELFN binding), cell-biological (trafficking/glycosylation), and structural (class C dimer/Venus-flytrap) evidence are mutually consistent. Gene-therapy rescue in the *Grm6*-null mouse — where restoring mGluR6 relocalizes the whole signalplex ([PMID: 33729473](https://pubmed.ncbi.nlm.nih.gov/33729473/)) — strongly demonstrates that mGluR6 is both necessary and sufficient to organize the postsynaptic complex.

**An extending (not contradicting) frontier.** Recent human retinal-organoid work (CRISPR ablation; PMID 42987835) suggests that in humans — unlike mouse — mGluR6 is *transiently* expressed in developing cone photoreceptors and contributes to cone terminal targeting and OPL assembly. This adds a species-specific developmental dimension to the canonical ON-bipolar role and warrants confirmation in native human retina.

---

## Supported and Refuted Hypotheses

**Supported:**
1. mGluR6 is the postsynaptic glutamate receptor essential and specific for the retinal ON pathway (Masu 1995).
2. It is a group III, Gαo-coupled class C GPCR activated by glutamate/L-AP4 (Sekiyama 1996; Shen 2009).
3. The effector is TRPM1, held closed when the receptor is occupied → sign-inverting transduction (Tummala 2016; Shen 2009).
4. It functions at ON-bipolar dendritic tips in the OPL and requires Golgi glycosylation + ELFN1 adhesion for targeting (Pindwarawala 2025).
5. GRM6 loss causes autosomal-recessive cCSNB (Katta 2024; Lin 2025).
6. It is the hub of an interdependent signalplex (Pearring 2011; Hasan 2020; Sarria 2016).
7. It is a dimeric class C GPCR activated via Venus-flytrap LBD closure relayed through the 9-Cys domain (Muto 2007; Vafabakhsh 2015).
8. It is additionally a bidirectional trans-synaptic organizer via ELFN1/ELFN2 (Lee 2025; Miller 2024).
9. Database annotation independently confirms the 877-aa class C architecture, chromosome-5 locus, N-glycosylation sites, Gi/o signaling, ER→Golgi→membrane→dendrite localization, and CSNB1B causation.

**Refuted / ruled out:** mGluR6 is **not** an enzyme or transporter, and does **not** act in the OFF pathway (OFF responses are intact in knockouts; Masu 1995). The transduction channel is TRPM1, not a TRPV channel (Shen 2009).

---

## Limitations and Knowledge Gaps

1. **No experimental structure of mGluR6 itself.** The dimer/Venus-flytrap/9-Cys mechanism is inferred by homology from mGluR1/5 and group II/III structures. A cryo-EM structure of full-length human mGluR6 (ideally Gαo-bound) is lacking.
2. **Quantitative signaling parameters undefined.** Glutamate affinity/EC₅₀, Gαo→TRPM1 kinetics, and receptor:channel stoichiometry at native synapses are not precisely established for mGluR6.
3. **Adenylate-cyclase inhibition is a by-similarity annotation.** The physiologically decisive output in bipolar cells is TRPM1 gating, not cAMP; the relevance of cAMP signaling in bipolar cells is unresolved.
4. **Species differences.** Transient cone expression and a developmental role seen in human organoids are absent in mouse, limiting model fidelity for therapy development.
5. **C-terminal interactome.** The short cytoplasmic C-terminus (846–877) likely mediates localization-relevant protein interactions that are incompletely mapped.
6. **Extra-retinal functions.** Reports of mGluR6 in melanocytes and some visceral/CNS neurons exist, but their physiological significance is uncertain and secondary to the retinal role.

---

## Proposed Follow-up Experiments / Actions

1. **Cryo-EM of human mGluR6** in apo, glutamate-bound, and Gαo-coupled states to confirm the activation mechanism and map the G-protein interface.
2. **Quantitative reconstitution of the Gαo→TRPM1 module** (± nyctalopin, ± GPR179/RGS GAP) to measure gating kinetics and signal-termination dynamics.
3. **Define the glycosylation code** by mutating the annotated N-glycosylation sites (Asn296/451/479/567; plus the ELFN-critical site) to dissect roles in Golgi maturation, ELFN binding, and targeting.
4. **Structural basis of mGluR6–ELFN1/2 adhesion** via a co-structure of the mGluR6 extracellular region with ELFN LRR/LRRCT domains.
5. **Resolve the human cone-expression finding** using primate retina and organoids to test conservation and therapeutic relevance.
6. **Optimize GRM6 gene therapy** — improve ON-bipolar transduction efficiency and promoter design to convert signalplex relocalization into functional vision restoration in CSNB1B.

---

## Conclusion

GRM6/mGluR6 (UniProt O15303) is unambiguously the human retinal **class C, group III metabotropic glutamate receptor** that performs **sign-inverting signal transduction at the first synapse of the ON visual pathway**. It senses photoreceptor-released glutamate via an extracellular Venus-flytrap domain and, through Gαo, closes the TRPM1 cation channel — so that light (falling glutamate) depolarizes ON-bipolar cells. It works at the dendritic tips of ON-bipolar cells, acting simultaneously as the receptor hub of an interdependent signalplex and as a glycosylation-dependent, bidirectional trans-synaptic organizer via ELFN1/ELFN2. Loss of function causes autosomal-recessive complete congenital stationary night blindness (CSNB1B). Gene symbol, organism, family, and domain architecture all match the target identity, and the evidence base spans genetics, pharmacology, biochemistry, cell biology, and structural inference.


## Artifacts

- [OpenScientist final report](GRM6-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRM6-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7889569
2. PMID:27037829
3. PMID:19439586
4. PMID:39681475
5. PMID:38522615
6. PMID:40923695
7. PMID:33729473
8. PMID:8730745
9. PMID:23452348
10. PMID:21734298
11. PMID:31959619
12. PMID:26961947
13. PMID:26258295
14. PMID:17360426
15. PMID:12444084
16. PMID:15922585
17. PMID:40930976
18. PMID:38428819