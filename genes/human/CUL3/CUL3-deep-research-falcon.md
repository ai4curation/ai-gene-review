---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T22:12:09.078505'
end_time: '2026-05-12T22:23:38.188346'
duration_seconds: 689.11
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

Concise GO annotation research for human CUL3 / UniProt Q13618 (cullin-3). Focus only on GO-relevant evidence: core molecular function as a cullin-RING E3 ubiquitin ligase scaffold / ubiquitin ligase complex scaffold activity; assembly of CRL3 complexes with RBX1 and BTB-domain substrate adaptors; roles in protein ubiquitination, protein polyubiquitination, proteasome-mediated ubiquitin-dependent protein catabolic process; neddylation/deneddylation regulation of CUL3 activity; cellular components including Cul3-RING ubiquitin ligase complex, cytoplasm/cytosol, nucleus, and any membrane/centrosome/cytoskeleton claims that need caution; substrate/adaptor examples such as KEAP1-NFE2L2/NRF2, KLHL3-WNK kinases, SPOP, KCTD proteins, cell-cycle or developmental substrates, and whether these should be core or non-core; distinguish direct CUL3 scaffold function from downstream phenotypes including cell cycle, development, oxidative stress response, neuronal phenotypes, blood pressure/electrolyte homeostasis, viral processes, and disease. Include caveats for generic protein binding or ubiquitin protein ligase binding annotations and for over-annotation from pathway membership or substrate phenotypes. Include PMID/DOI citations and keep under 1500 words.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

Concise GO annotation research for human CUL3 / UniProt Q13618 (cullin-3). Focus only on GO-relevant evidence: core molecular function as a cullin-RING E3 ubiquitin ligase scaffold / ubiquitin ligase complex scaffold activity; assembly of CRL3 complexes with RBX1 and BTB-domain substrate adaptors; roles in protein ubiquitination, protein polyubiquitination, proteasome-mediated ubiquitin-dependent protein catabolic process; neddylation/deneddylation regulation of CUL3 activity; cellular components including Cul3-RING ubiquitin ligase complex, cytoplasm/cytosol, nucleus, and any membrane/centrosome/cytoskeleton claims that need caution; substrate/adaptor examples such as KEAP1-NFE2L2/NRF2, KLHL3-WNK kinases, SPOP, KCTD proteins, cell-cycle or developmental substrates, and whether these should be core or non-core; distinguish direct CUL3 scaffold function from downstream phenotypes including cell cycle, development, oxidative stress response, neuronal phenotypes, blood pressure/electrolyte homeostasis, viral processes, and disease. Include caveats for generic protein binding or ubiquitin protein ligase binding annotations and for over-annotation from pathway membership or substrate phenotypes. Include PMID/DOI citations and keep under 1500 words.

## Concise GO annotation research report: Human **CUL3** (Cullin-3; UniProt **Q13618**) — GO-relevant evidence only

### Scope and annotation philosophy
This report summarizes evidence supporting **core Gene Ontology (GO)** annotations for human CUL3 as a **cullin–RING E3 ubiquitin ligase scaffold** (CRL3). Emphasis is on **direct molecular function (MF), complex assembly/cellular component (CC), and proximal biological processes (BP)** (ubiquitination and ubiquitin-dependent proteolysis), while **downstream phenotypes/pathway roles** (oxidative stress response, blood pressure, neurodevelopment, cancer, viral infection) are treated as *non-core* unless the evidence directly establishes CUL3’s mechanistic role.

### 1) Key concepts and definitions (current understanding)

#### CUL3 as a cullin–RING E3 ligase scaffold (GO: MF/CC core)
CUL3 is the **central scaffold** of CRL3 ubiquitin ligases, bridging (i) a **RING protein (RBX1)** that recruits E2~ubiquitin and (ii) **BTB-domain substrate adaptor/receptor proteins** that recruit specific substrates. This architecture is described in recent mechanistic reviews and supported by primary structural work, including explicit **CUL3–RBX1** and adaptor-bound complexes (jeong2023targetinge3ubiquitin pages 2-3, sharma2023insightsintothe pages 1-3, hu2024dynamicmoleculararchitecture pages 1-21).

**Direct structural/biochemical evidence** includes:
- Cryo-EM showing CRL3 assemblies containing **CUL3 + RBX1 + BTB adaptor** (e.g., KLHL22-based CRL3) and supporting the concept that **dimerization** of BTB adaptors yields a **2:2 stoichiometry** (BTB dimer recruiting two CUL3–RBX1 arms) that supports ligase activity (wang2024aconservednterminal pages 1-2, wang2024aconservednterminal pages 7-8).
- KEAP1–CUL3 crystal structure evidence of a **heterotetrameric 2:2 complex (KEAP1:CUL3)** with quantitative binding (KD ~0.2 μM), reinforcing the scaffold/adaptor binding model (preprint) (adamson2023structuralandbiochemical pages 1-7).

**GO MF term guidance:** evidence best supports a CUL3 annotation consistent with **“ubiquitin ligase complex scaffold activity”** / **E3 ligase scaffold** rather than “ubiquitin-protein transferase activity” (which is catalytic and typically attributed to the E2/E3 catalytic machinery rather than the scaffold) (jeong2023targetinge3ubiquitin pages 2-3, wang2024aconservednterminal pages 1-2).

#### Assembly of CRL3 complexes with RBX1 and BTB adaptors (GO: CC and complex assembly)
Recent structural work shows that CRL3s are **multi-subunit complexes** with physically resolved interfaces that underlie assembly.
- A May 2024 cryo-EM/biochemistry study on CRL3^KLHL22 identifies a **conserved N-terminal motif in CUL3** that contributes to **dimeric CRL3 assembly and E3 activity**; deletion reduces adaptor binding and changes complex stoichiometry (wang2024aconservednterminal pages 7-8, wang2024aconservednterminal pages 1-2).
- Feb 2024 cryo-EM structural states of CRL3^KBTBD2 include substrate-engaged forms and regulatory complexes with the COP9 signalosome and CAND1, supporting CUL3’s role as a structural platform that coordinates catalytic and regulatory modules (hu2024dynamicmoleculararchitecture pages 1-21).

### 2) Recent developments and latest research (prioritize 2023–2024)

#### 2024 cryo-EM reveals CRL3 architecture, substrate recruitment, and regulation
A 2024 Nature Structural & Molecular Biology study provides multiple cryo-EM reconstructions of **CRL3^KBTBD2** including:
- A **neddylated** CRL3 form (CUL3~NEDD8),
- complexes with the **COP9 signalosome (CSN)** (including mutant CSN states), and
- a **CUL3–RBX1–CAND1** complex.
These structures directly support GO-relevant assertions that CRL3 activity is coupled to **neddylation/deneddylation** and regulated by exchange factors such as **CAND1** (hu2024dynamicmoleculararchitecture pages 1-21).

#### 2023–2024 tools to measure activated (neddylated) CRLs in cells
A 2023 Nature Chemical Biology study developed a **conformation-specific probe** recognizing **NEDD8-linked active cullins** and profiled activated CRL networks including **CUL3-containing complexes** (henneberg2023activitybasedprofilingof pages 1-2). The work includes experimental perturbations with **MLN4924** (NAE inhibitor; blocks neddylation) and **CSN5i-3** (blocks deneddylation), and explicitly detects **NEDD8–CUL3** species by IP–MS (henneberg2023activitybasedprofilingof pages 6-6). This supports GO-relevant statements that (i) **neddylation activates** CRLs and (ii) active-state abundance is dynamically regulated.

#### 2024 synthesis of structural knowledge on neddylation regulators (CSN, CAND1)
A 2024 review in *Signal Transduction and Targeted Therapy* compiles recent structures that include **CUL3–KLHL22–RBX1**, **CAND1–CUL3–RBX1**, and **KBTBD2–NEDD8–CUL3–RBX1–CSN** assemblies (listed PDBs/EM structures), and emphasizes that **CSN removes NEDD8** whereas **CAND1 preferentially binds unneddylated cullins** as a negative regulator/exchange factor (zhang2024proteinneddylationand pages 8-10). (Review-level evidence; use primarily to support general regulatory concepts rather than highly specific GO regulator terms.)

### 3) Current applications and real-world implementations (GO-relevant)
While not GO terms per se, applications inform which mechanistic aspects are robustly established.

- **Pharmacologic modulation of CRL3 activity via neddylation**: MLN4924 is widely used to inhibit NEDD8-activating enzyme (NAE), thereby inhibiting CRL activity; CUL3-linked CRL activity is described as requiring neddylation in multiple contexts (henneberg2023activitybasedprofilingof pages 6-6, gu2024cullin3ring pages 1-2).
- **Targeted protein degradation and E3 ligase engagement**: CRL3 adaptors such as **KEAP1** appear in degrader/TPD discussions as E3 components that can be recruited in chemical biology approaches; this supports the practical importance of accurate annotation of CRL3 scaffold/adaptor assembly, though it does not add new GO terms (jeong2023targetinge3ubiquitin pages 2-3).

### 4) Expert opinions and analysis: GO annotation recommendations and caveats

#### Core GO: Molecular function
**Strongly supported (core):**
- **Ubiquitin ligase complex scaffold activity / E3 ubiquitin ligase scaffold** — CUL3 is repeatedly defined and structurally demonstrated as a CRL scaffold bridging RBX1 and BTB adaptors, including detailed stoichiometry and interface determinants (wang2024aconservednterminal pages 1-2, adamson2023structuralandbiochemical pages 1-7, hu2024dynamicmoleculararchitecture pages 1-21).

**Caution:**
- Avoid annotating CUL3 with generic “protein binding” or “ubiquitin protein ligase binding” unless the evidence is specifically required for MF, because these terms are often **low-information** and may reflect experimental detection rather than biological specificity.

#### Core GO: Biological process
**Strongly supported (core/proximal):**
- **Protein ubiquitination / protein polyubiquitination**: Multiple CRL3 systems demonstrate ubiquitination output; for example, CRL3^KLHL22 assays support ubiquitination activity dependence on CUL3 structural motifs (wang2024aconservednterminal pages 1-2), and CRL3^KCTD7 demonstrates CUL3-dependent ubiquitination of calpains (sengupta2023theubiquitinlikeproteins pages 4-5).

**Proteasome-mediated ubiquitin-dependent protein catabolic process (supported, but adaptor/substrate-dependent):**
- Proteasomal targeting is a canonical outcome for many CRLs, and reviews explicitly describe substrate ubiquitination “for proteasomal degradation” as a CRL3 output (sharma2023insightsintothe pages 1-3). However, **not all CUL3-dependent ubiquitination is degradative** (see KCTD7/calpain below), so proteasome-related BP annotations should be supported by **substrate degradation evidence** rather than ubiquitination alone.

**Critical caveat (avoid over-annotation):**
- **Non-degradative ubiquitination**: the KCTD7–CUL3–RBX1 complex ubiquitinates calpains with atypical chain linkages (K6/K27/K29/K63) and regulates activity rather than proteasomal turnover; this supports “protein ubiquitination” but argues against automatically applying proteasome-mediated catabolism for all CUL3-dependent ubiquitination (sengupta2023theubiquitinlikeproteins pages 4-5).
- **Pathway membership / phenotype-only evidence**: oxidative stress response, blood pressure/electrolyte phenotypes, neurodevelopmental phenotypes, or cancer-associated phenotypes can be downstream of CUL3-dependent substrate regulation. These should not be treated as core CUL3 BP terms without direct mechanistic evidence that CUL3’s scaffold activity is required in the specific pathway node being annotated.

#### Core GO: Cellular component
**Supported (core):**
- **Cul3-RING ubiquitin ligase complex / cullin-RING ubiquitin ligase complex**: direct structural evidence places CUL3 in CRL3 assemblies containing RBX1 and BTB adaptors (hu2024dynamicmoleculararchitecture pages 1-21, wang2024aconservednterminal pages 1-2).

**Cytosol/cytoplasm and nucleus (plausible but evidence here is limited):**
- A 2024 preprint reports differential tumor-context localization of CUL3 (cytoplasmic in one subtype; nuclear/perinuclear in another) and suggests nuclear engagement via interactions with RNA polymerase complexes in DNA damage contexts (pantazi2024ubiquitylationmediatedrnapiigenomic pages 100-104). Because this is **preprint-level** and partially inference-based, it supports a *cautious* note that CUL3 can be found in cytoplasmic and nuclear contexts but may not be sufficient alone for strong CC annotations.

**Membrane/centrosome/cytoskeleton claims require caution:**
- A 2024 structure paper on CRL3^KCTD5 describes compatibility with **membrane-bound Gβγ** in the reaction complex; this is **substrate-contextual** and does not justify annotating CUL3 broadly as a membrane component (jeong2023targetinge3ubiquitin pages 2-3).
- No strong direct evidence in the retrieved set supports **centrosome** or **cytoskeleton** localization as a general CC term for CUL3; references to kinetochores/mitosis are often substrate-contextual and may reflect downstream phenotype or adaptor targeting rather than stable CUL3 localization.

### 5) Relevant statistics and data (recent studies)
- **Stoichiometry data:** structural/biochemical studies support **2:2 assemblies** (BTB dimer with two CUL3 arms) in CRL3 complexes and provide measurable changes in complex stoichiometry when CUL3 motifs are deleted (wang2024aconservednterminal pages 1-2, wang2024aconservednterminal pages 7-8). KEAP1–CUL3 binding is reported with **KD ~0.2 μM** and a **2:2 heterotetramer** in structural/biochemical assays (preprint) (adamson2023structuralandbiochemical pages 1-7).
- **Network scale estimate:** a 2023 review states mammals may form up to **188 distinct CUL3–BTB E3 complexes**, underscoring annotation relevance for “CUL3-RING ubiquitin ligase complex” rather than overly specific pathway terms (jeong2023targetinge3ubiquitin pages 2-3).
- **Quantitative profiling of NEDD8–CUL3:** IP–MS profiling explicitly detects “NEDD8–CUL3” and uses inhibitors (MLN4924; CSN5i-3) to modulate neddylation/deneddylation states, providing empirical support that CUL3 participates in dynamic neddylation-regulated CRL activation (henneberg2023activitybasedprofilingof pages 6-6).

### GO-relevant adaptor/substrate examples (evidence-weighted)
The table below summarizes adaptor modules and indicates which are core vs cautionary for CUL3 GO inference.

| Adaptor / CRL3 example | Example substrate or process context | What is directly evidenced about **CUL3** | GO annotation relevance for human CUL3 | Caveats / evidence limits | Recent source (date; DOI/URL) |
|---|---|---|---|---|---|
| **KEAP1–CUL3–RBX1** | NRF2 degradation under basal/non-oxidative conditions; KEAP1 recognizes NRF2 degrons | CUL3 N-terminus binds BTB/3-box adaptor KEAP1; CUL3 C-terminus assembles with RBX1; KEAP1:CUL3 forms a heterotetrameric **2:2** assembly; neddylation of CUL3 CTD promotes active ubiquitin-transfer geometry (adamson2023structuralandbiochemical pages 1-7, jeong2023targetinge3ubiquitin pages 2-3) | **Core** for MF/CC: ubiquitin ligase complex scaffold activity; Cul3-RING ubiquitin ligase complex. **Process**: protein ubiquitination / polyubiquitination; proteasome-mediated ubiquitin-dependent catabolic process can be supported when tied to NRF2 degradation, but keep focus on scaffold role (adamson2023structuralandbiochemical pages 1-7, sharma2023insightsintothe pages 1-3) | Preprint for detailed KEAP1-CUL3 structure; KEAP1/NRF2 oxidative-stress phenotypes are downstream and should not be over-transferred to CUL3 as core BP beyond ubiquitination/catabolism (adamson2023structuralandbiochemical pages 1-7, sharma2023insightsintothe pages 1-3) | Feb 2023, doi:10.1101/2023.02.15.528651, https://doi.org/10.1101/2023.02.15.528651; Oct 2023, doi:10.1186/s12964-023-01269-z, https://doi.org/10.1186/s12964-023-01269-z |
| **KLHL22–CUL3–RBX1** | Polyubiquitination of reported substrates such as PLK1/PD1/DEPDC5; model for CRL3 dimeric activity | Cryo-EM/biochemistry show CUL3 is the scaffold of CRL3; BTB dimer recruits two CUL3-RBX1 arms (**2:2**); conserved CUL3 N-terminal motif contributes to dimeric assembly and E3 activity; deletion impairs binding and ubiquitination activity (wang2024aconservednterminal pages 1-2, wang2024aconservednterminal pages 7-8) | **Core** for MF/CC: scaffold activity; Cul3-RING ubiquitin ligase complex assembly. **Core/moderate** for BP: protein polyubiquitination (directly assayed in CRL3 context) (wang2024aconservednterminal pages 1-2) | Substrate-specific phenotypes (mitosis, autophagy, signaling) should be treated as **non-core for CUL3** unless directly evidenced in human CUL3 context; avoid over-annotation from adaptor pathway membership (wang2024aconservednterminal pages 1-2) | May 2024, doi:10.1038/s41467-024-48045-2, https://doi.org/10.1038/s41467-024-48045-2 |
| **KLHL12–CUL3** | SEC31 monoubiquitylation; large COPII structure formation / procollagen export | Review/primary evidence states CUL3 is CRL3 scaffold; CRL3^KLHL12 ubiquitylates SEC31; CUL3 neddylation activates CRL3 via conformational change near RBX1/E2-Ub positioning (moretti2023klhl12canform pages 1-2) | **Core** for MF: scaffold in ubiquitin ligase complex. **Caution** for BP: “protein ubiquitination” supported; **do not default to proteasome-mediated catabolism** here because SEC31 example is monoubiquitylation and collagen effects may involve lysosomal handling (moretti2023klhl12canform pages 1-2) | Not a strong basis for proteasome-related GO on CUL3 from this module alone; COPII/ER-exit-site or membrane-trafficking claims are adaptor/substrate-contextual, not core CUL3 location/function (moretti2023klhl12canform pages 1-2) | Mar 2023, doi:10.1091/mbc.e22-08-0383, https://doi.org/10.1091/mbc.e22-08-0383 |
| **KBTBD2–CUL3–RBX1** | p85α / PI3K regulatory subunit recruitment; substrate-engaged CRL3 architecture | High-resolution cryo-EM captures CRL3^KBTBD2, substrate-bound complexes, **neddylated CUL3**, CUL3–RBX1–CAND1, and CUL3 complexes with **COP9 signalosome (CSN)**, providing direct evidence for scaffold assembly plus neddylation/deneddylation and exchange regulation (hu2024dynamicmoleculararchitecture pages 1-21) | **Core** for MF/CC/BP**:** ubiquitin ligase complex scaffold activity; Cul3-RING ubiquitin ligase complex; regulation of CRL3 activity by neddylation/deneddylation can support regulation-related annotation if term selection is careful (hu2024dynamicmoleculararchitecture pages 1-21) | Best recent structural support for regulation, but substrate-specific signaling outputs should remain non-core; no direct subcellular localization claim should be expanded beyond complex membership from this study alone (hu2024dynamicmoleculararchitecture pages 1-21) | Feb 2024, doi:10.1038/s41594-023-01182-6, https://doi.org/10.1038/s41594-023-01182-6 |
| **KCTD5–CUL3–RBX1** | Gβγ ubiquitylation; membrane-proximal signaling context | Pentameric KCTD5/CUL3/Gβγ complex architecture shows CUL3 in BTB/cullin core CRL3; CUL3-based complex positions substrate for ubiquitin transfer; reaction complex is described as compatible with **membrane-bound Gβγ** (jeong2023targetinge3ubiquitin pages 2-3) | **Core** for scaffold/ubiquitination. **Caution** for localization: membrane compatibility of a specific CRL3^KCTD5 reaction complex does **not** justify generic membrane annotation for CUL3 (jeong2023targetinge3ubiquitin pages 2-3) | Membrane association is context-specific and substrate-dependent; avoid annotating CUL3 broadly to membrane based on one adaptor/substrate system (jeong2023targetinge3ubiquitin pages 2-3) | Apr 2024, doi:10.1073/pnas.2315018121, https://doi.org/10.1073/pnas.2315018121 |
| **KCTD7–CUL3–RBX1** | Calpain regulation by non-degradative ubiquitination | Primary study shows KCTD7 works in complex with CUL3 and RBX1 to ubiquitinate calpains with non-K48 linkage patterns and regulate activity rather than degradation (sengupta2023theubiquitinlikeproteins pages 4-5) | **Core** for “protein ubiquitination.” **Caution/non-core** for proteasome-mediated catabolic process, because this is explicitly **non-degradative ubiquitination** (sengupta2023theubiquitinlikeproteins pages 4-5) | Do not infer protein catabolism/proteasome process from all CUL3 substrates; also avoid inferring neuronal disease phenotypes as direct CUL3 GO BP terms (sengupta2023theubiquitinlikeproteins pages 4-5) | Mar 2023, doi:10.1038/s41421-023-00533-3, https://doi.org/10.1038/s41421-023-00533-3 |
| **SPOP–CUL3–RBX1** | Broad substrate adaptor example; cancer- and virus-related substrate studies discussed in reviews | Reviews describe SPOP as a BTB adaptor of the CUL3/RBX1 complex; BACK/BTB adaptors and SPOP higher-order assemblies can enhance CRL3 activity (jeong2023targetinge3ubiquitin pages 2-3) | **Useful as supporting example**, but usually **non-core for CUL3 annotation** unless citing direct human CUL3 biochemical evidence in the same experiment. Safe use: adaptor repertoire supporting CRL3 assembly concept (jeong2023targetinge3ubiquitin pages 2-3) | Many SPOP papers focus on adaptor phenotypes or disease substrates, not direct CUL3 scaffold biochemistry; avoid over-annotation from cancer/viral phenotypes to CUL3 BP terms (jeong2023targetinge3ubiquitin pages 2-3) | Oct 2023, doi:10.1038/s12276-023-01087-w, https://doi.org/10.1038/s12276-023-01087-w |
| **CUL3 regulation by NEDD8 / CSN / CAND1** | Activation/inactivation cycle of CRL3 complexes | NEDD8 conjugation activates cullin-RING ligases; recent work measures NEDD8-CUL3 and perturbation by MLN4924 or deneddylation inhibitor CSN5i-3; reviews state CSN removes NEDD8; structural studies capture CUL3–RBX1–CAND1 and CUL3~NEDD8–CSN complexes (henneberg2023activitybasedprofilingof pages 1-2, henneberg2023activitybasedprofilingof pages 6-6, sharma2023insightsintothe pages 1-3, zhang2024proteinneddylationand pages 8-10, hu2024dynamicmoleculararchitecture pages 1-21) | **Core regulatory context** for CRL3 activity. Good support for annotations tied to cullin deneddylation/neddylation regulation or regulation of ubiquitin ligase activity, if the GO term matches the evidence scope (zhang2024proteinneddylationand pages 8-10, hu2024dynamicmoleculararchitecture pages 1-21, henneberg2023activitybasedprofilingof pages 1-2, sharma2023insightsintothe pages 1-3) | Some evidence is general-to-cullin or review-based; use care in assigning highly specific regulator terms unless direct human CUL3 experimental support is cited. No direct support here for broad cellular-component claims beyond CRL3 complex itself (zhang2024proteinneddylationand pages 8-10, henneberg2023activitybasedprofilingof pages 1-2, sharma2023insightsintothe pages 1-3) | Aug 2023, doi:10.1038/s41589-023-01392-5, https://doi.org/10.1038/s41589-023-01392-5; Apr 2024, doi:10.1038/s41392-024-01800-9, https://doi.org/10.1038/s41392-024-01800-9; Feb 2024, doi:10.1038/s41594-023-01182-6, https://doi.org/10.1038/s41594-023-01182-6 |


*Table: This table summarizes direct GO-relevant evidence for human CUL3 across key CRL3 adaptor systems, highlighting what supports core scaffold and ubiquitination annotations versus what should be treated cautiously as adaptor-specific, non-degradative, or phenotype-driven.*

### Summary: Recommended core GO assertions for CUL3 (evidence-backed)
1. **MF:** ubiquitin ligase complex scaffold activity (CRL3 scaffold) supported by multiple 2023–2024 structural/biochemical studies (wang2024aconservednterminal pages 1-2, hu2024dynamicmoleculararchitecture pages 1-21, adamson2023structuralandbiochemical pages 1-7).
2. **CC:** member of Cul3-RING ubiquitin ligase complex / CRL3 complexes with RBX1 and BTB adaptors (hu2024dynamicmoleculararchitecture pages 1-21, wang2024aconservednterminal pages 1-2).
3. **BP:** protein ubiquitination and, in contexts with demonstrated degradative ubiquitination, protein polyubiquitination and proteasome-mediated ubiquitin-dependent protein catabolic process—while explicitly recognizing that some CRL3 outputs are **non-degradative** (wang2024aconservednterminal pages 1-2, sengupta2023theubiquitinlikeproteins pages 4-5, sharma2023insightsintothe pages 1-3).
4. **Regulation of activity:** reversible **neddylation** activates CRLs; **deneddylation (CSN)** and exchange regulation via **CAND1** are structurally supported for CUL3 complexes and experimentally manipulable in cells (hu2024dynamicmoleculararchitecture pages 1-21, henneberg2023activitybasedprofilingof pages 6-6, sharma2023insightsintothe pages 1-3, zhang2024proteinneddylationand pages 8-10).

### Key references (URLs, dates)
- Hu Y et al. *Nat Struct Mol Biol* (Feb 2024). “Dynamic molecular architecture…” DOI:10.1038/s41594-023-01182-6 https://doi.org/10.1038/s41594-023-01182-6 (hu2024dynamicmoleculararchitecture pages 1-21)
- Wang W et al. *Nat Commun* (May 2024). DOI:10.1038/s41467-024-48045-2 https://doi.org/10.1038/s41467-024-48045-2 (wang2024aconservednterminal pages 1-2, wang2024aconservednterminal pages 7-8)
- Henneberg LT et al. *Nat Chem Biol* (Aug 2023). DOI:10.1038/s41589-023-01392-5 https://doi.org/10.1038/s41589-023-01392-5 (henneberg2023activitybasedprofilingof pages 1-2, henneberg2023activitybasedprofilingof pages 6-6)
- Zhang S et al. *Signal Transduct Target Ther* (Apr 2024). DOI:10.1038/s41392-024-01800-9 https://doi.org/10.1038/s41392-024-01800-9 (zhang2024proteinneddylationand pages 8-10)
- Moretti T et al. *Mol Biol Cell* (Mar 2023; online Jan 2023). DOI:10.1091/mbc.e22-08-0383 https://doi.org/10.1091/mbc.e22-08-0383 (moretti2023klhl12canform pages 1-2)
- Sharma P, Chatrathi HE. *Cell Commun Signal* (Oct 2023). DOI:10.1186/s12964-023-01269-z https://doi.org/10.1186/s12964-023-01269-z (sharma2023insightsintothe pages 1-3)
- Adamson RJ et al. bioRxiv (posted Feb 16, 2023). DOI:10.1101/2023.02.15.528651 https://doi.org/10.1101/2023.02.15.528651 (adamson2023structuralandbiochemical pages 1-7)



References

1. (jeong2023targetinge3ubiquitin pages 2-3): Yelin Jeong, Ah-Reum Oh, Young Hoon Jung, HyunJoon Gi, Young Un Kim, and KyeongJin Kim. Targeting e3 ubiquitin ligases and their adaptors as a therapeutic strategy for metabolic diseases. Experimental &amp; Molecular Medicine, 55:2097-2104, Oct 2023. URL: https://doi.org/10.1038/s12276-023-01087-w, doi:10.1038/s12276-023-01087-w. This article has 56 citations and is from a peer-reviewed journal.

2. (sharma2023insightsintothe pages 1-3): Prashant Sharma and Harish E. Chatrathi. Insights into the diverse mechanisms and effects of variant cul3-induced familial hyperkalemic hypertension. Cell Communication and Signaling : CCS, Oct 2023. URL: https://doi.org/10.1186/s12964-023-01269-z, doi:10.1186/s12964-023-01269-z. This article has 6 citations.

3. (hu2024dynamicmoleculararchitecture pages 1-21): Yuxia Hu, Zhao Zhang, Qiyu Mao, Xiang Zhang, Aihua Hao, Yu Xun, Yeda Wang, Lin Han, Wuqiang Zhan, Qianying Liu, Yue Yin, Chao Peng, Eva Marie Y. Moresco, Zhenguo Chen, Bruce Beutler, and Lei Sun. Dynamic molecular architecture and substrate recruitment of cullin3-ring e3 ligase crl3kbtbd2. Nature structural & molecular biology, 31:336-350, Feb 2024. URL: https://doi.org/10.1038/s41594-023-01182-6, doi:10.1038/s41594-023-01182-6. This article has 21 citations and is from a highest quality peer-reviewed journal.

4. (wang2024aconservednterminal pages 1-2): Weize Wang, Ling Liang, Zonglin Dai, Peng Zuo, Shang Yu, Yishuo Lu, Dian Ding, Hongyi Chen, Hui Shan, Yan Jin, Youdong Mao, and Yuxin Yin. A conserved n-terminal motif of cul3 contributes to assembly and e3 ligase activity of crl3klhl22. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48045-2, doi:10.1038/s41467-024-48045-2. This article has 16 citations and is from a highest quality peer-reviewed journal.

5. (wang2024aconservednterminal pages 7-8): Weize Wang, Ling Liang, Zonglin Dai, Peng Zuo, Shang Yu, Yishuo Lu, Dian Ding, Hongyi Chen, Hui Shan, Yan Jin, Youdong Mao, and Yuxin Yin. A conserved n-terminal motif of cul3 contributes to assembly and e3 ligase activity of crl3klhl22. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48045-2, doi:10.1038/s41467-024-48045-2. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (adamson2023structuralandbiochemical pages 1-7): Roslin J Adamson, N Connor Payne, Sergio G. Bartual, Ralph Mazitschek, and Alex N Bullock. Structural and biochemical characterization establishes a detailed understanding of keap1-cul3 complex assembly. bioRxiv, Feb 2023. URL: https://doi.org/10.1101/2023.02.15.528651, doi:10.1101/2023.02.15.528651. This article has 34 citations.

7. (henneberg2023activitybasedprofilingof pages 1-2): Lukas T. Henneberg, Jaspal Singh, David M. Duda, Kheewoong Baek, David Yanishevski, Peter J. Murray, Matthias Mann, Sachdev S. Sidhu, and Brenda A. Schulman. Activity-based profiling of cullin–ring e3 networks by conformation-specific probes. Nature Chemical Biology, 19:1513-1523, Aug 2023. URL: https://doi.org/10.1038/s41589-023-01392-5, doi:10.1038/s41589-023-01392-5. This article has 32 citations and is from a highest quality peer-reviewed journal.

8. (henneberg2023activitybasedprofilingof pages 6-6): Lukas T. Henneberg, Jaspal Singh, David M. Duda, Kheewoong Baek, David Yanishevski, Peter J. Murray, Matthias Mann, Sachdev S. Sidhu, and Brenda A. Schulman. Activity-based profiling of cullin–ring e3 networks by conformation-specific probes. Nature Chemical Biology, 19:1513-1523, Aug 2023. URL: https://doi.org/10.1038/s41589-023-01392-5, doi:10.1038/s41589-023-01392-5. This article has 32 citations and is from a highest quality peer-reviewed journal.

9. (zhang2024proteinneddylationand pages 8-10): Shizhen Zhang, Qing Yu, Zhijian Li, Yongchao Zhao, and Yi Sun. Protein neddylation and its role in health and diseases. Signal Transduction and Targeted Therapy, Apr 2024. URL: https://doi.org/10.1038/s41392-024-01800-9, doi:10.1038/s41392-024-01800-9. This article has 148 citations and is from a peer-reviewed journal.

10. (gu2024cullin3ring pages 1-2): Lijie Gu, Yanhong Du, Jianglei Chen, Mohammad Nazmul Hasan, Yung Dai Clayton, David J. Matye, Jacob E. Friedman, and Tiangang Li. Cullin 3 ring e3 ligase inactivation causes nrf2-dependent nadh reductive stress, hepatic lipodystrophy, and systemic insulin resistance. Proceedings of the National Academy of Sciences of the United States of America, Apr 2024. URL: https://doi.org/10.1073/pnas.2320934121, doi:10.1073/pnas.2320934121. This article has 21 citations and is from a highest quality peer-reviewed journal.

11. (sengupta2023theubiquitinlikeproteins pages 4-5): Swarnab Sengupta and Elah Pick. The ubiquitin-like proteins of saccharomyces cerevisiae. Biomolecules, 13:734, Apr 2023. URL: https://doi.org/10.3390/biom13050734, doi:10.3390/biom13050734. This article has 4 citations.

12. (pantazi2024ubiquitylationmediatedrnapiigenomic pages 100-104): Vasiliki Pantazi. Ubiquitylation-mediated rnapii genomic eviction in response to dna dsbs. ArXiv, 2024. URL: https://doi.org/10.14232/phd.12363, doi:10.14232/phd.12363. This article has 0 citations.

13. (moretti2023klhl12canform pages 1-2): Tamara Moretti, Kyungho Kim, Astha Tuladhar, and Jinoh Kim. Klhl12 can form large copii structures in the absence of cul3 neddylation. Molecular Biology of the Cell, Mar 2023. URL: https://doi.org/10.1091/mbc.e22-08-0383, doi:10.1091/mbc.e22-08-0383. This article has 11 citations and is from a domain leading peer-reviewed journal.

## Citations

1. adamson2023structuralandbiochemical pages 1-7
2. hu2024dynamicmoleculararchitecture pages 1-21
3. henneberg2023activitybasedprofilingof pages 1-2
4. henneberg2023activitybasedprofilingof pages 6-6
5. zhang2024proteinneddylationand pages 8-10
6. wang2024aconservednterminal pages 1-2
7. sengupta2023theubiquitinlikeproteins pages 4-5
8. sharma2023insightsintothe pages 1-3
9. pantazi2024ubiquitylationmediatedrnapiigenomic pages 100-104
10. wang2024aconservednterminal pages 7-8
11. https://doi.org/10.1101/2023.02.15.528651;
12. https://doi.org/10.1186/s12964-023-01269-z
13. https://doi.org/10.1038/s41467-024-48045-2
14. https://doi.org/10.1091/mbc.e22-08-0383
15. https://doi.org/10.1038/s41594-023-01182-6
16. https://doi.org/10.1073/pnas.2315018121
17. https://doi.org/10.1038/s41421-023-00533-3
18. https://doi.org/10.1038/s12276-023-01087-w
19. https://doi.org/10.1038/s41589-023-01392-5;
20. https://doi.org/10.1038/s41392-024-01800-9;
21. https://doi.org/10.1038/s41589-023-01392-5
22. https://doi.org/10.1038/s41392-024-01800-9
23. https://doi.org/10.1101/2023.02.15.528651
24. https://doi.org/10.1038/s12276-023-01087-w,
25. https://doi.org/10.1186/s12964-023-01269-z,
26. https://doi.org/10.1038/s41594-023-01182-6,
27. https://doi.org/10.1038/s41467-024-48045-2,
28. https://doi.org/10.1101/2023.02.15.528651,
29. https://doi.org/10.1038/s41589-023-01392-5,
30. https://doi.org/10.1038/s41392-024-01800-9,
31. https://doi.org/10.1073/pnas.2320934121,
32. https://doi.org/10.3390/biom13050734,
33. https://doi.org/10.14232/phd.12363,
34. https://doi.org/10.1091/mbc.e22-08-0383,