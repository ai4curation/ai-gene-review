---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T02:02:07.703599'
end_time: '2026-10-04T02:15:58.581750'
duration_seconds: 830.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Pias1
  gene_symbol: Pias1
  uniprot_accession: O88907
  protein_description: 'RecName: Full=E3 SUMO-protein ligase PIAS1; EC=2.3.2.27; AltName:
    Full=DEAD/H box-binding protein 1; AltName: Full=Protein inhibitor of activated
    STAT protein 1; AltName: Full=RING-type E3 ubiquitin transferase PIAS1 {ECO:0000305};'
  gene_info: Name=Pias1; Synonyms=Ddxbp1;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the PIAS family. .
  protein_domains: PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034);
    SAP_dom_sf. (IPR036361); Znf_MIZ. (IPR004181)
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
citation_count: 27
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pias1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pias1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O88907
- **Protein Description:** RecName: Full=E3 SUMO-protein ligase PIAS1; EC=2.3.2.27; AltName: Full=DEAD/H box-binding protein 1; AltName: Full=Protein inhibitor of activated STAT protein 1; AltName: Full=RING-type E3 ubiquitin transferase PIAS1 {ECO:0000305};
- **Gene Information:** Name=Pias1; Synonyms=Ddxbp1;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the PIAS family. .
- **Key Domains:** PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); Znf_MIZ. (IPR004181)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Pias1" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Pias1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Pias1** (gene ID: Pias1, UniProt: O88907) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PIAS1 (O88907, *Mus musculus*): A Nuclear SP-RING SUMO E3 Ligase and Inducible Brake on Inflammatory Transcription

**Gene:** *Pias1* (synonym *Ddxbp1*) · **Organism:** *Mus musculus* (Mouse)
**Protein:** E3 SUMO-protein ligase PIAS1 / Protein Inhibitor of Activated STAT protein 1 / DEAD/H box-binding protein 1
**EC:** 2.3.2.27 (SUMO–protein transferase; RING-type E3) · **Family:** PIAS family · **Length:** 651 aa

## Summary

Mouse **PIAS1** (Protein Inhibitor of Activated STAT1; gene *Pias1*, synonym *Ddxbp1*; UniProt **O88907**; 651 amino acids) is a **nuclear SUMO E3 ligase** (EC 2.3.2.27) of the **PIAS/Siz family**. Its catalytic core is the **SP-RING (Znf_MIZ) zinc-finger domain**, which recruits the SUMO-charged E2 conjugating enzyme **Ubc9** and accelerates the transfer of **SUMO** (small ubiquitin-like modifier) onto lysine residues of substrate proteins. The substrates are predominantly **nuclear transcription factors and chromatin/DNA-repair proteins**, including C/EBPβ, PNKP, Hes-1, the APP intracellular domain (AICD), and the androgen receptor. The identification of PIAS1 as a *bona fide* E3 ligase and the requirement of its catalytic activity for biological function are well supported across *in vitro* and cellular studies ([PMID: 12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/), [PMID: 24061474](https://pubmed.ncbi.nlm.nih.gov/24061474/), [PMID: 18583943](https://pubmed.ncbi.nlm.nih.gov/18583943/)).

Beyond its enzymatic activity, PIAS1's defining and physiologically validated function is to act as an **inducible negative-feedback brake on interferon (IFN) and inflammatory (NF-κB) gene transcription**. It binds **activated STAT1** and the **NF-κB subunit p65 (RelA)** and blocks their recruitment to target-gene promoter DNA. Critically, this transrepression is **mechanistically separable from SUMOylation of the transcription factors themselves** — PIAS1 inhibits STAT1 without requiring STAT1 to be SUMO-modified ([PMID: 12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/)). The physiological importance of these activities is established in *Pias1*-knockout mice, which display enhanced IFN responses, increased resistance to pathogens, and elevated proinflammatory cytokine production ([PMID: 15311277](https://pubmed.ncbi.nlm.nih.gov/15311277/), [PMID: 15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/)).

PIAS1 operates **in the nucleus** — on chromatin and promoters (via its DNA-binding **SAP domain**) and within **PML nuclear bodies (PML-NBs)**, where it contributes to intrinsic antiviral SUMOylation ([PMID: 27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/)). Its activity is finely tuned by post-translational modification: **IKKα-mediated phosphorylation at Ser90** is required to switch on transrepression ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)), **MAPKAPK2 phosphorylation at Ser522** enhances ligase and transrepression activity ([PMID: 23202365](https://pubmed.ncbi.nlm.nih.gov/23202365/)), and its abundance is controlled by a GSK3β/HECTD2 phosphodegron-directed degradation pathway ([PMID: 26157031](https://pubmed.ncbi.nlm.nih.gov/26157031/)). Gene identity is unambiguously confirmed: the UniProt record, PIAS-family domain architecture, mouse organism, and the published literature are internally consistent, and the *Ddxbp1* synonym traces directly to the original "GBP" (Gu/RH-II-binding protein) clone ([PMID: 9177271](https://pubmed.ncbi.nlm.nih.gov/9177271/)).

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was performed and **passed**:

| Verification item | Result |
|---|---|
| Gene symbol matches protein | ✅ "Pias1" = Protein Inhibitor of Activated STAT1; matches UniProt O88907 description |
| Organism | ✅ *Mus musculus* (mouse); literature is predominantly mouse/mammalian PIAS1 |
| Protein family / domains | ✅ PIAS family; SAP, PINIT, SP-RING (Znf_MIZ), SIM domains all confirmed in literature |
| Synonym resolution | ✅ *Ddxbp1* / "DEAD/H box-binding protein 1" traces to original GBP (Gu/RH-II-binding protein) clone ([PMID: 9177271](https://pubmed.ncbi.nlm.nih.gov/9177271/)) |

No conflicting literature for a different gene with the same symbol was found. Research proceeded on the correct target.

---

## Key Findings

### Finding 1 — PIAS1 is a SUMO E3 ligase (EC 2.3.2.27)

PIAS1 catalyzes the transfer of SUMO onto lysine residues of substrate proteins, functioning as the **E3 ligase** in the SUMOylation enzymatic cascade (E1 activating enzyme Aos1/Uba2 → E2 conjugating enzyme Ubc9 → E3 ligase). The PIAS family was shown to "function as E3 ligases that promote the SUMO modification of a number of transcription regulators" ([PMID: 12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/)). A precise, mechanistically-defined demonstration is PIAS1's role in adipogenesis, where it "functions as a SUMO E3 ligase of C/EBPβ," directly SUMOylating this transcription factor via its SAP domain in both *in vitro* and cellular assays, with catalytic activity required for the biological outcome ([PMID: 24061474](https://pubmed.ncbi.nlm.nih.gov/24061474/)).

The catalytic mechanism resides in the **SP-RING domain** (the "SUMO-ligase core"), characteristic of Siz/PIAS-type ligases, which positions the SUMO-charged Ubc9~SUMO thioester to catalyze isopeptide bond formation ([PMID: 18583943](https://pubmed.ncbi.nlm.nih.gov/18583943/)). The reaction catalyzed is:

```
Substrate-Lys-NH2  +  Ubc9~SUMO (thioester)
        │  (PIAS1 SP-RING E3 ligase)
        ▼
Substrate-Lys-N(H)-SUMO (isopeptide)  +  Ubc9
```

This establishes PIAS1's **primary enzymatic function**: it is an E3 ligase of EC class 2.3.2.27 (RING-type, acting here on SUMO rather than ubiquitin) with substrate specificity directed toward nuclear transcriptional and chromatin regulators.

### Finding 2 — PIAS1 negatively regulates STAT1 by blocking promoter recruitment

PIAS1 is a **physiologically important negative regulator of STAT1**, the central transcription factor of interferon (IFN-γ and IFN-β) signaling. Using *Pias1⁻/⁻* knockout mice and derived cells, Liu et al. demonstrated that "PIAS1 selectively regulates a subset of IFN-γ- or IFN-β-inducible genes by interfering with the recruitment of STAT1 to the gene promoter" ([PMID: 15311277](https://pubmed.ncbi.nlm.nih.gov/15311277/)). The physiological consequence is clear: disruption of *Pias1* enhanced the antiviral activity of IFN and *Pias1⁻/⁻* mice showed increased protection against pathogenic infection, confirming that "PIAS1 is a physiologically important negative regulator of STAT1" ([PMID: 15311277](https://pubmed.ncbi.nlm.nih.gov/15311277/)).

Mechanistically crucial: this inhibition **does not require SUMOylation of STAT1 itself** — "inhibition of STAT1 by PIAS proteins does not require SUMO modification of STAT1 itself" ([PMID: 12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/)). Thus PIAS1's transrepressive function toward STAT1 is distinct from (and additional to) its catalytic SUMO-ligase activity — it acts by physically occluding STAT1–promoter engagement. This mode of action is reinforced by independent work showing TGF-β suppresses IFN-γ–STAT1 signaling by enhancing STAT1–PIAS1 interactions and reducing STAT1 DNA binding in epithelia ([PMID: 17371985](https://pubmed.ncbi.nlm.nih.gov/17371985/)).

### Finding 3 — PIAS1 is a nuclear protein and PML nuclear body constituent; activity tuned by phosphorylation

PIAS1 localizes to the **nucleus** and is a **constituent protein of PML nuclear bodies (PML-NBs)**. Brown et al. "identify the SUMO ligase protein inhibitor of activated STAT1 (PIAS1) as a constituent PML-NB protein," recruited to PML-NBs in a **SIM (SUMO-interaction-motif)-dependent** manner and localized to incoming HSV-1 genomes to promote antiviral SUMO1 accumulation ([PMID: 27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/)). This places PIAS1 at a defined subnuclear structure central to intrinsic antiviral immunity.

PIAS1 activity is tuned by phosphorylation: MAPKAPK2 (MK2) "phosphorylates PIAS1 at the Ser522 residue," increasing both its SUMO E3 ligase activity and transrepression to limit endothelial inflammation ([PMID: 23202365](https://pubmed.ncbi.nlm.nih.gov/23202365/)). PIAS1 abundance is further controlled by regulated degradation: "GSK3β phosphorylation of PIAS1 provided a phosphodegron for HECTD2 targeting," linking PIAS1 turnover to ubiquitin-mediated proteolysis in innate immunity and lung injury ([PMID: 26157031](https://pubmed.ncbi.nlm.nih.gov/26157031/)).

### Finding 4 — PIAS1 SUMOylates diverse nuclear substrates linking it to DNA repair and transcription-factor control

Beyond immune transcription factors, PIAS1 SUMOylates a broad set of nuclear substrates with defined functional consequences:

| Substrate | Acceptor site(s) | Functional consequence | Reference |
|---|---|---|---|
| **PNKP** (DNA end-processing) | — | Component of transcription-coupled repair complex; PIAS1 knockdown restored PNKP activity/genomic integrity in Huntington's disease models | [PMID: 33468657](https://pubmed.ncbi.nlm.nih.gov/33468657/) |
| **C/EBPβ** | — | Regulates adipogenesis | [PMID: 24061474](https://pubmed.ncbi.nlm.nih.gov/24061474/) |
| **Hes-1** | Lys8, Lys27, Lys39 | Enhances Hes-1 repression of GADD45α → increased cell survival | [PMID: 24894488](https://pubmed.ncbi.nlm.nih.gov/24894488/) |
| **AICD** (APP intracellular domain) | Lys-43 predominantly | Increases nuclear translocation / transcriptional activation of Aβ-degrading enzymes (NEP, TTR) | [PMID: 32950104](https://pubmed.ncbi.nlm.nih.gov/32950104/) |

The PNKP finding is especially precise: "PIAS1 is a component of the transcription-coupled repair complex, that includes the DNA damage end processing enzyme polynucleotide kinase-phosphatase (PNKP), and that PIAS1 is a SUMO E3 ligase for PNKP" ([PMID: 33468657](https://pubmed.ncbi.nlm.nih.gov/33468657/)). The Hes-1 study demonstrates precise, lysine-resolved substrate specificity: "Hes-1 SUMOylation was greatly enhanced by the SUMO E3 ligase PIAS1 at Lys8, Lys27 and Lys39" ([PMID: 24894488](https://pubmed.ncbi.nlm.nih.gov/24894488/)). In the Alzheimer's-model study, AICD "is SUMO-modified by the SUMO E3 ligase protein inhibitor of activated STAT1 (PIAS1) in the hippocampus at Lys-43 predominantly," with functional consequences for Aβ degradation ([PMID: 32950104](https://pubmed.ncbi.nlm.nih.gov/32950104/)).

### Finding 5 — Catalysis requires SIMs; PIAS1 acts as a SUMO-dependent androgen-receptor corepressor

Full catalytic activity of PIAS-family RING ligases requires **C-terminal SUMO-interaction motifs (SIMs)**, which engage the SUMO moiety during transfer. In the related family member PIASy, multiple SIMs were found to be "both... required for the full ligase activity of PIASy" ([PMID: 28455449](https://pubmed.ncbi.nlm.nih.gov/28455449/)), a principle that extends to PIAS1's own C-terminal SIM region.

PIAS1 also serves as a **SUMO-dependent corepressor of the androgen receptor (AR)**: "the sumoylation of AR via the association of SUMO-1 and PIAS1 is able to repress AR-dependent transcription" ([PMID: 17336575](https://pubmed.ncbi.nlm.nih.gov/17336575/)). This is reviewed in the broader context of AR cofactors in prostate cancer, where PIAS1 is noted among AR cofactors that modulate AR function through SUMOylation ([PMID: 38417290](https://pubmed.ncbi.nlm.nih.gov/38417290/)), positioning PIAS1 as a nuclear-receptor cofactor acting through SUMOylation.

### Finding 6 — PIAS1 is a direct negative regulator of NF-κB, activated by IKKα-mediated Ser90 phosphorylation

PIAS1 directly restrains **NF-κB signaling**. It binds the nuclear-translocated **p65 (RelA)** subunit and blocks its DNA binding: "The binding of PIAS1 to p65 inhibits cytokine-induced NF-κB-dependent gene activation. PIAS1 blocks the DNA binding activity of p65 both in vitro and in vivo" ([PMID: 15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/)). Genetic validation: in *Pias1⁻/⁻* cells, p65 recruitment to NF-κB promoters is enhanced, a subset of TNF-/LPS-induced NF-κB genes is upregulated, and "Pias1 null mice showed elevated proinflammatory cytokines" ([PMID: 15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/)).

This brake is **inducibly switched on** by phosphorylation. Inflammatory stimuli trigger rapid PIAS1 phosphorylation: "PIAS1 becomes rapidly phosphorylated on Ser90 residue in response to various inflammatory stimuli" ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)). The responsible kinase is IKKα (not IKKβ), and — strikingly — the phosphorylation itself depends on PIAS1's own enzymatic activity: "IKKα, but not IKKβ, interacts with PIAS1 in vivo and mediates PIAS1 Ser90 phosphorylation, a process that requires the SUMO ligase activity of PIAS1" ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)). Ser90 phosphorylation is required for PIAS1 to repress transcription and associate with NF-κB target promoters. This establishes an elegant feed-forward loop: the same inflammatory signaling that activates NF-κB also activates its PIAS1 brake.

### Finding 7 — Domain architecture rationalizes the mechanism; nuclear/speckle/PML localization; auto-SUMOylation

The 651-residue mouse PIAS1 (O88907) has a domain order that precisely matches its mechanism:

```
N ─[SAP]──[NLS]────[PINIT]──────[SP-RING / Znf_MIZ]────[SIM]──[Ser/Thr-rich disordered tail]─ C
   11–45   56–64    124–288        320–405               462–473    (incl. Ser522)
   DNA-     nuclear  substrate      Zn-coordinating       SUMO-      heavily phosphorylated
   binding  import   recognition    (351/353/374/377);    binding    regulatory region
   (LXXLL             nuclear        recruits E2 Ubc9
   19–23)            retention
```

- The **SAP domain** binds A/T-rich DNA (scaffold/chromatin attachment), anchoring PIAS1 at promoters.
- The **PINIT domain** mediates substrate recognition and nuclear retention.
- The **SP-RING zinc finger** (Zn-coordinating residues 351/353/374/377) recruits Ubc9 — the catalytic heart.
- The **SIM region** engages SUMO for efficient transfer (consistent with Finding 5).
- The **disordered C-terminal tail** carries the regulatory phosphosites (Ser522, and the Ser90 context).

Six curated **auto-SUMOylation** acceptor lysines are annotated (K40, K46, K137, K238, K453, K493; SUMO2 isopeptide cross-links). Subcellular localization is curated as **Nucleus, Nucleus speckle, and PML body**, with a minor cytoplasm/cytoskeleton pool. The experimental origin of these annotations is the original GBP clone: "The GBP protein is localized to the nucleus in speckled or diffuse nucleoplasmic patterns. The GBP mRNA level is highest in testis" ([PMID: 9177271](https://pubmed.ncbi.nlm.nih.gov/9177271/)) — this also explains the *Ddxbp1*/"DEAD-box-binding-protein" synonym (GBP = Gu/RH-II binding protein). The MIZ-type zinc finger that confers SUMO E3 activity relates PIAS1 to the broader PIAS/ZMIZ coregulator family ([PMID: 35670836](https://pubmed.ncbi.nlm.nih.gov/35670836/)).

---

## Mechanistic Model / Interpretation

PIAS1 can be understood as a **dual-function nuclear regulator**: (1) a catalytic SUMO E3 ligase, and (2) a non-catalytic transrepressor that physically blocks transcription-factor–DNA binding. These two activities converge on the same overarching biological theme — **restraining inflammatory and interferon transcription** — and are integrated by phosphorylation-based signaling.

### Integrated model of PIAS1 as an inducible inflammatory brake

```
   Inflammatory / IFN stimulus (TNF, LPS, IFN-γ/β)
                 │
     ┌───────────┴────────────┐
     ▼                        ▼
  NF-κB / STAT1          IKKα kinase
  ACTIVATION               │
     │                     ▼
     │              PIAS1 Ser90-P  ◄── requires PIAS1 SUMO-ligase activity
     │              (also MK2 → Ser522-P enhances activity)
     ▼                     │
  p65 / STAT1              ▼
  enter nucleus      ACTIVE PIAS1
     │                     │
     └──────► PIAS1 binds p65 / STAT1 ──► blocks DNA binding / promoter recruitment
                                             │
                                             ▼
                               REPRESSION of IFN/NF-κB target genes
                               (SUMOylation-independent transrepression)

  In parallel: PIAS1 SP-RING + Ubc9 → SUMOylates nuclear substrates
  (C/EBPβ, PNKP, Hes-1, AICD, androgen receptor) at PML-NBs / chromatin
```

The key conceptual insights are:

1. **Transrepression ≠ substrate SUMOylation.** PIAS1 inhibits STAT1 and p65 by occluding their promoter DNA binding, not by SUMOylating them ([PMID: 12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/), [PMID: 15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/)). Yet its catalytic activity remains required for the Ser90 phosphorylation that activates transrepression ([PMID: 17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/)) — tying the two functions together.

2. **Feed-forward negative feedback.** The same inflammatory cascade that activates NF-κB/STAT1 also activates PIAS1 (via IKKα→Ser90 and MK2→Ser522), ensuring that transcriptional activation is self-limiting. This is a textbook negative-feedback motif that prevents runaway inflammation — explaining why *Pias1⁻/⁻* mice are hyper-inflammatory and hyper-responsive to IFN.

3. **Spatial logic.** The SAP domain tethers PIAS1 to A/T-rich promoter DNA where it can intercept transcription factors; PML-NB localization concentrates its SUMO-ligase activity for intrinsic antiviral defense ([PMID: 27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/)).

4. **Broad substrate repertoire with a common nuclear theme.** Whether SUMOylating PNKP (DNA repair), Hes-1 (Notch/repression), AICD (APP signaling), C/EBPβ (adipogenesis), or AR (nuclear-receptor signaling), PIAS1 consistently acts on **nuclear transcriptional and genome-maintenance machinery**.

---

## Evidence Base

| PMID | Study (abbreviated) | How it supports the findings |
|---|---|---|
| [12764129](https://pubmed.ncbi.nlm.nih.gov/12764129/) | SUMO modification of STAT1 and PIAS-mediated inhibition | Establishes PIAS proteins as SUMO E3 ligases for transcription regulators; shows STAT1 inhibition is SUMO-independent (F001, F002) |
| [24061474](https://pubmed.ncbi.nlm.nih.gov/24061474/) | PIAS1 is SUMO E3 ligase of C/EBPβ in adipogenesis | Direct demonstration of PIAS1 ligase activity on a defined substrate (F001, F004) |
| [18583943](https://pubmed.ncbi.nlm.nih.gov/18583943/) | Cytoplasmic sumoylation by Siz1 | Identifies SP-RING as the SUMO-ligase catalytic core (F001) |
| [15311277](https://pubmed.ncbi.nlm.nih.gov/15311277/) | PIAS1 selectively inhibits IFN-inducible genes (KO mice) | Mechanism (blocks STAT1 promoter recruitment) + physiological role in innate immunity (F002) |
| [17371985](https://pubmed.ncbi.nlm.nih.gov/17371985/) | TGF-β enhances STAT1–PIAS1 interaction | Independent support: PIAS1 reduces STAT1 DNA binding without blocking activation (F002) |
| [27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/) | PIAS1 as constituent PML-NB protein in HSV-1 restriction | Nuclear/PML-NB localization; SIM-dependent recruitment; antiviral SUMOylation (F003) |
| [23202365](https://pubmed.ncbi.nlm.nih.gov/23202365/) | MK2 phosphorylation of PIAS1 (Ser522) | Phosphoregulation enhancing ligase + transrepression activity (F003) |
| [26157031](https://pubmed.ncbi.nlm.nih.gov/26157031/) | HECTD2 in innate immunity / lung injury | GSK3β phosphodegron controls PIAS1 abundance via ubiquitination (F003) |
| [33468657](https://pubmed.ncbi.nlm.nih.gov/33468657/) | PIAS1 in Huntington's disease striatum | PNKP as substrate; transcription-coupled repair link (F004) |
| [24894488](https://pubmed.ncbi.nlm.nih.gov/24894488/) | Hes-1 SUMOylation by PIAS1 | Lysine-resolved substrate specificity (K8/K27/K39) with functional readout (F004) |
| [32950104](https://pubmed.ncbi.nlm.nih.gov/32950104/) | AICD SUMOylation in Alzheimer's model | PIAS1 SUMOylates AICD at Lys-43; melatonin-induced; Aβ clearance (F004) |
| [28455449](https://pubmed.ncbi.nlm.nih.gov/28455449/) | New SIM in PIASy | SIMs required for full PIAS-family ligase activity (F005) |
| [17336575](https://pubmed.ncbi.nlm.nih.gov/17336575/) | UBC9 C-terminus / nuclear receptor regulation | PIAS1 SUMOylates AR to repress AR transcription (F005) |
| [38417290](https://pubmed.ncbi.nlm.nih.gov/38417290/) | AR cofactors review | Contextualizes PIAS1 as an AR corepressor in prostate cancer (F005) |
| [15657437](https://pubmed.ncbi.nlm.nih.gov/15657437/) | Negative regulation of NF-κB by PIAS1 | PIAS1 binds p65, blocks DNA binding; KO mice hyper-inflammatory (F006) |
| [17540171](https://pubmed.ncbi.nlm.nih.gov/17540171/) | IKKα-mediated PIAS1 Ser90 phosphorylation | Defines activating signal (Ser90) and IKKα kinase; ties to ligase activity (F006) |
| [9177271](https://pubmed.ncbi.nlm.nih.gov/9177271/) | Cloning of Gu/RH-II binding protein (GBP) | Origin of Ddxbp1 synonym; early nuclear-speckle localization + testis expression (F007) |
| [35670836](https://pubmed.ncbi.nlm.nih.gov/35670836/) | ZMIZ/PIAS-family coregulator review | Structural/evolutionary framing of MIZ-type SUMO E3 activity (F007) |

### Supporting / contextual literature

Additional papers reinforce and extend the model: DNA methylation recruits PIAS1 to silence IFN-γ–induced IRF8 in colon carcinoma ([PMID: 19074829](https://pubmed.ncbi.nlm.nih.gov/19074829/)); PIAS1 cooperates with STAT3 to suppress iNOS in dendritic cells ([PMID: 24777831](https://pubmed.ncbi.nlm.nih.gov/24777831/)); PIAS1 regulates HSC DNA methylation and lineage commitment ([PMID: 24421322](https://pubmed.ncbi.nlm.nih.gov/24421322/)); PIAS1 cross-talks with the leukemogenic kinase FIP1L1-PDGFRA through reciprocal SUMOylation/phosphorylation ([PMID: 27960034](https://pubmed.ncbi.nlm.nih.gov/27960034/)); PIAS1 influences glucocorticoid-receptor translocation in chronic social defeat stress ([PMID: 30351951](https://pubmed.ncbi.nlm.nih.gov/30351951/)); a circPIAS1-encoded polypeptide modulates STAT1 SUMOylation/phosphorylation balance in melanoma ([PMID: 39334380](https://pubmed.ncbi.nlm.nih.gov/39334380/)); and the related family member PIAS4 acts in intrinsic antiviral immunity ([PMID: 26937035](https://pubmed.ncbi.nlm.nih.gov/26937035/)). The sumoylation-cascade structural review ([PMID: 18492068](https://pubmed.ncbi.nlm.nih.gov/18492068/)) provides structural framing for the SUMO E1/E2/E3 interactions, and an early macrophage study established PIAS1/GBP as a constitutive negative regulator of STAT1-mediated IFN-γ responses ([PMID: 11897494](https://pubmed.ncbi.nlm.nih.gov/11897494/)).

---

## Limitations and Knowledge Gaps

1. **No high-resolution structure of full-length mouse PIAS1.** Domain boundaries and mechanism are inferred from UniProt curation, homology to related PIAS/Siz proteins, and biochemical mapping rather than a complete experimental structure of O88907. The precise spatial coordination of SAP–PINIT–SP-RING–SIM during catalysis remains modeled rather than directly observed.

2. **Transrepression vs. SUMOylation boundary not fully resolved at the structural level.** While it is established that STAT1/p65 inhibition is SUMOylation-independent, the exact interaction surfaces by which PIAS1 occludes STAT1/p65 DNA binding, and how these relate to the catalytic domain, are not atomically defined.

3. **Substrate specificity determinants are incompletely defined.** PIAS1 SUMOylates a structurally diverse substrate set, but the rules governing substrate selection (consensus motif vs. SIM-mediated vs. PINIT-mediated recognition) have not been systematically mapped for mouse PIAS1.

4. **Many substrate studies are from disease models or non-mouse/overexpression systems.** Several substrate relationships (AICD, Hes-1, AR) derive from cellular/overexpression or human contexts; physiological relevance of each in normal mouse tissue varies in strength of evidence. The strongest, endogenous-level genetic evidence exists for the STAT1/NF-κB axis.

5. **Tissue- and isoform-specific functions underexplored.** The original GBP clone showed highest mRNA in testis ([PMID: 9177271](https://pubmed.ncbi.nlm.nih.gov/9177271/)), yet the testis-specific role of PIAS1 is not well characterized.

6. **Interplay among the regulatory modifications (Ser90, Ser522, auto-SUMOylation, degradation) is not integrated.** How these events are temporally ordered and combinatorially control PIAS1 activity in vivo remains open.

---

## Proposed Follow-up Experiments / Actions

1. **Structural determination** of full-length or multi-domain mouse PIAS1 (cryo-EM or crystallography), ideally in complex with Ubc9~SUMO and a substrate peptide, to resolve the catalytic geometry and the SIM's contribution.

2. **Separation-of-function mouse alleles.** Generate knock-in mice bearing (a) a catalytically dead SP-RING mutant, (b) a SIM-deficient mutant, and (c) a Ser90Ala mutant, to dissect which inflammatory/IFN phenotypes depend on catalysis vs. transrepression vs. phospho-activation in vivo.

3. **Unbiased substrate mapping** via SUMO-site proteomics (SUMO-remnant immunoprecipitation + MS) in wild-type vs. *Pias1⁻/⁻* mouse tissues to define the endogenous, physiological substrate repertoire and consensus specificity.

4. **ChIP-seq of PIAS1, p65, and STAT1** in wild-type vs. *Pias1⁻/⁻* macrophages/endothelium to genome-wide map where PIAS1 blocks transcription-factor promoter recruitment, and to test the SAP-domain DNA-binding dependence.

5. **Temporal phospho-signaling dissection.** Quantitative phosphoproteomics across an inflammatory time course to order the Ser90 (IKKα) and Ser522 (MK2) events relative to NF-κB/STAT1 activation and PIAS1 degradation (GSK3β/HECTD2), building a quantitative model of the negative-feedback loop.

6. **PML-NB function.** Test whether SIM-dependent PML-NB localization is required for PIAS1's intrinsic antiviral SUMOylation using SIM-mutant knock-in cells challenged with HSV-1, extending [PMID: 27099310](https://pubmed.ncbi.nlm.nih.gov/27099310/).

---

## Conclusion

Mouse PIAS1 (O88907) is a **nuclear SP-RING/Znf-MIZ SUMO E3 ligase (EC 2.3.2.27)** that transfers SUMO from Ubc9 onto lysines of nuclear substrate proteins — chiefly transcription factors and DNA-repair/chromatin proteins (C/EBPβ, PNKP, Hes-1, AICD, androgen receptor). Its defining, physiologically validated role is as an **inducible negative-feedback brake on interferon and inflammatory (NF-κB) transcription**: it binds activated STAT1 and NF-κB p65 and blocks their promoter DNA binding in a SUMOylation-independent manner, switched on by IKKα-mediated Ser90 phosphorylation and tuned by MAPKAPK2 (Ser522) and regulated degradation. It functions **in the nucleus** — on A/T-rich promoter chromatin (via its SAP domain) and within PML nuclear bodies, where it also contributes to intrinsic antiviral SUMOylation. The gene identity, domain architecture, and literature are fully consistent and confirmed.


## Artifacts

- [OpenScientist final report](Pias1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pias1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12764129
2. PMID:24061474
3. PMID:18583943
4. PMID:15311277
5. PMID:15657437
6. PMID:27099310
7. PMID:17540171
8. PMID:23202365
9. PMID:26157031
10. PMID:9177271
11. PMID:17371985
12. PMID:33468657
13. PMID:24894488
14. PMID:32950104
15. PMID:28455449
16. PMID:17336575
17. PMID:38417290
18. PMID:35670836
19. PMID:19074829
20. PMID:24777831
21. PMID:24421322
22. PMID:27960034
23. PMID:30351951
24. PMID:39334380
25. PMID:26937035
26. PMID:18492068
27. PMID:11897494