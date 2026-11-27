---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T02:02:07.714972'
end_time: '2026-10-04T02:54:38.059203'
duration_seconds: 3150.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Q7KNF5
  gene_symbol: Su-var-2-10
  uniprot_accession: Q7KNF5
  protein_description: 'SubName: Full=Suppressor of variegation 2-10, isoform A {ECO:0000313|EMBL:AAF58984.1};'
  gene_info: Name=Su(var)2-10 {ECO:0000313|EMBL:AAF58984.1, ECO:0000313|FlyBase:FBgn0003612};
    Synonyms=CLOT2057 {ECO:0000313|EMBL:AAF58984.1}, Dmel\CG8068 {ECO:0000313|EMBL:AAF58984.1},
    DmPias {ECO:0000313|EMBL:AAF58984.1}, DPIAS {ECO:0000313|EMBL:AAF58984.1}, Dpias
    {ECO:0000313|EMBL:AAF58984.1}, dPIAS {ECO:0000313|EMBL:AAF58984.1}, dpias {ECO:0000313|EMBL:AAF58984.1},
    i184 {ECO:0000313|EMBL:AAF58984.1}, l(2)03697 {ECO:0000313|EMBL:AAF58984.1}, PIAS
    {ECO:0000313|EMBL:AAF58984.1}, pias {ECO:0000313|EMBL:AAF58984.1}, Su(var)-10
    {ECO:0000313|EMBL:AAF58984.1}, SU(VAR)2-10 {ECO:0000313|EMBL:AAF58984.1}, Su(Var)2-10
    {ECO:0000313|EMBL:AAF58984.1}, Su-var(2)10 {ECO:0000313|EMBL:AAF58984.1}, Suvar(2)10
    {ECO:0000313|EMBL:AAF58984.1}, Sv210 {ECO:0000313|EMBL:AAF58984.1}, ZIMP {ECO:0000313|EMBL:AAF58984.1},
    zimp {ECO:0000313|EMBL:AAF58984.1}, ZimpA {ECO:0000313|EMBL:AAF58984.1}, ZimpB
    {ECO:0000313|EMBL:AAF58984.1}; ORFNames=CG8068 {ECO:0000313|EMBL:AAF58984.1, ECO:0000313|FlyBase:FBgn0003612},
    Dmel_CG8068 {ECO:0000313|EMBL:AAF58984.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the PIAS family.
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Su-var-2-10-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Su-var-2-10-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q7KNF5
- **Protein Description:** SubName: Full=Suppressor of variegation 2-10, isoform A {ECO:0000313|EMBL:AAF58984.1};
- **Gene Information:** Name=Su(var)2-10 {ECO:0000313|EMBL:AAF58984.1, ECO:0000313|FlyBase:FBgn0003612}; Synonyms=CLOT2057 {ECO:0000313|EMBL:AAF58984.1}, Dmel\CG8068 {ECO:0000313|EMBL:AAF58984.1}, DmPias {ECO:0000313|EMBL:AAF58984.1}, DPIAS {ECO:0000313|EMBL:AAF58984.1}, Dpias {ECO:0000313|EMBL:AAF58984.1}, dPIAS {ECO:0000313|EMBL:AAF58984.1}, dpias {ECO:0000313|EMBL:AAF58984.1}, i184 {ECO:0000313|EMBL:AAF58984.1}, l(2)03697 {ECO:0000313|EMBL:AAF58984.1}, PIAS {ECO:0000313|EMBL:AAF58984.1}, pias {ECO:0000313|EMBL:AAF58984.1}, Su(var)-10 {ECO:0000313|EMBL:AAF58984.1}, SU(VAR)2-10 {ECO:0000313|EMBL:AAF58984.1}, Su(Var)2-10 {ECO:0000313|EMBL:AAF58984.1}, Su-var(2)10 {ECO:0000313|EMBL:AAF58984.1}, Suvar(2)10 {ECO:0000313|EMBL:AAF58984.1}, Sv210 {ECO:0000313|EMBL:AAF58984.1}, ZIMP {ECO:0000313|EMBL:AAF58984.1}, zimp {ECO:0000313|EMBL:AAF58984.1}, ZimpA {ECO:0000313|EMBL:AAF58984.1}, ZimpB {ECO:0000313|EMBL:AAF58984.1}; ORFNames=CG8068 {ECO:0000313|EMBL:AAF58984.1, ECO:0000313|FlyBase:FBgn0003612}, Dmel_CG8068 {ECO:0000313|EMBL:AAF58984.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the PIAS family.
- **Key Domains:** PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); Znf_MIZ. (IPR004181)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Su-var-2-10" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Su-var-2-10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Su-var-2-10** (gene ID: Q7KNF5, UniProt: Q7KNF5) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Su(var)2-10 / dPIAS (Q7KNF5), *Drosophila melanogaster*

## Gene Identity Verification

Before presenting findings, the target identity was confirmed against the UniProt record and the primary literature. The gene symbol, organism, protein family, and domain architecture are **fully concordant** across all sources:

| Attribute | UniProt Q7KNF5 | Literature / FlyBase | Match |
|-----------|----------------|----------------------|-------|
| Gene symbol | Su(var)2-10 | Su(var)2-10 (dPIAS, ZIMP) | ✔ |
| Organism | *Drosophila melanogaster* | *Drosophila melanogaster* | ✔ |
| FlyBase ID | FBgn0003612 | FBgn0003612 | ✔ |
| Protein family | PIAS | PIAS (Protein Inhibitor of Activated STAT) | ✔ |
| Key domains | SAP, PINIT, SP-RING/MIZ zinc finger | SAP (2–36), PINIT (113–278), SP-RING (310–391) | ✔ |

The gene product is a **nuclear PIAS-family SUMO (Smt3) E3 ligase** — not an ambiguous or mis-mapped symbol. All literature cited below describes this specific *Drosophila* protein. The report proceeds with high confidence in gene identity.

---

## Summary

**Su(var)2-10** (also known as **dPIAS**, **ZIMP**, CG8068; UniProt **Q7KNF5**) encodes the principal **PIAS-family SUMO E3 ligase** of *Drosophila melanogaster*. Its primary biochemical function is to catalyze the transfer of the small ubiquitin-like modifier **SUMO (Smt3)** onto the lysine residues of specific nuclear substrate proteins. As an E3 ligase, it operates as the specificity-conferring final step of the SUMO conjugation cascade (E1 activating enzyme → E2 conjugating enzyme Ubc9 → E3 ligase Su(var)2-10 → substrate). The protein is built on the canonical tripartite PIAS architecture in which a **SP-RING/MIZ zinc finger** provides catalysis by activating the SUMO-charged E2 (Ubc9), a **PINIT domain** selects substrates and redirects conjugation to non-consensus target lysines, and an N-terminal **SAP domain** targets the enzyme to DNA/chromatin and the nucleus.

The dominant, best-characterized biological role of Su(var)2-10 is to act as a **molecular bridge that converts sequence/target recognition into SUMO-dependent assembly of H3K9-methyltransferase silencing machinery on chromatin**. In the germline nuclear piRNA pathway, it binds the piRNA/Piwi target-recognition complex and, through SUMO conjugation, recruits the SetDB1(Eggless)/Wde histone methyltransferase effector to deposit repressive **H3K9me3** and transcriptionally silence transposons. Genome-wide, the deposition of most of the H3K9me3 mark depends on SUMO and Su(var)2-10. A specific, mechanistically resolved substrate is **Bonus**, the single *Drosophila* homolog of the mammalian TIF1 transcription intermediary factors: Su(var)2-10 SUMOylates Bonus at a single conserved N-terminal site, and this modification nucleates the recruitment of SetDB1 and the NuRD remodeler to silence tissue-specific genes — a clear illustration of **"SUMO as molecular glue."**

Beyond chromatin silencing, Su(var)2-10 is essential for viability and organizes **interphase chromosome structure**, telomere clustering, and telomere–nuclear-lamina associations (it colocalizes with nuclear lamin in interphase). It also functions as a classical **PIAS negative regulator of JAK/STAT signaling**, modulating Stat92E activity in a dose-dependent manner during blood cell and eye development. The protein carries out all of these functions **in the nucleus**, at chromatin and the nuclear periphery.

---

## Key Findings

### Finding 1 — Su(var)2-10 is the Drosophila PIAS-family SUMO E3 ligase (dPIAS)

The *Su(var)2-10* locus was originally identified genetically as a dominant **Suppressor of Position-Effect Variegation** and was shown to be allelic to the lethal complementation group **l(2)03697**. Molecular cloning of the locus by Hari, Cook & Karpen (2001) demonstrated that it encodes a member of the **PIAS protein family** — the family of SUMO E3 ligases — establishing the gene product as the *Drosophila* PIAS ortholog (dPIAS) [PMID: 11390354](https://pubmed.ncbi.nlm.nih.gov/11390354/). The paper states directly that *"Su(var)2-10 encodes a member of the PIAS protein family, a group of highly conserved proteins that control diverse functions."*

Within the SUMO conjugation cascade, Su(var)2-10 occupies the **E3 ligase** position, acting downstream of the E2 conjugating enzyme **Ubc9**. This hierarchy was reinforced by Kalamarz et al. (2012), who refer to *"the conjugating E2 enzyme, Ubc9, or the E3 SUMO ligase, PIAS"* in *Drosophila* [PMID: 23213407](https://pubmed.ncbi.nlm.nih.gov/23213407/). The protein carries the canonical PIAS architecture: an N-terminal **SAP** DNA/chromatin-binding domain, a central **PINIT** domain, and the catalytic **SP-RING/MIZ** zinc finger that recruits the SUMO-charged Ubc9 to catalyze transfer of SUMO (Smt3) onto substrate lysines.

### Finding 2 — Su(var)2-10 links piRNA target recognition to SUMO-dependent chromatin silencing via SetDB1/Wde

The central mechanistic insight into Su(var)2-10 function comes from two companion 2020 papers from the Aravin laboratory. Ninova et al. (*Molecular Cell*) showed that in the *Drosophila* **nuclear piRNA pathway**, Su(var)2-10 physically bridges the piRNA target-recognition machinery to the chromatin-silencing effector: *"Su(var)2-10 links the piRNA-guided target recognition complex to the silencing effector by binding the piRNA/Piwi complex and inducing SUMO-dependent recruitment of the SetDB1/Wde histone methyltransferase effector"* [PMID: 31901446](https://pubmed.ncbi.nlm.nih.gov/31901446/).

The companion paper (Ninova et al., *Genes & Development*) established the **genome-wide scope** of this activity, showing that *"deposition of most of the H3K9me3 mark depends on SUMO and the SUMO ligase Su(var)2-10, which recruits the histone methyltransferase complex SetDB1/Wde"* [PMID: 31901448](https://pubmed.ncbi.nlm.nih.gov/31901448/). Su(var)2-10 thereby controls both heterochromatic repeat/transposon silencing and tissue-specific euchromatic gene repression, and participates in a **negative-feedback loop** on heterochromatin components. This is the protein's **primary function**: converting target recognition into the SUMO-dependent deposition of repressive H3K9me3.

### Finding 3 — Su(var)2-10 controls interphase chromosome structure, telomere/nuclear-lamina organization, and chromosome inheritance

Su(var)2-10 is **essential for viability**. Hypomorphic and loss-of-function mutations cause a constellation of chromosomal phenotypes: minichromosome and endogenous chromosome **inheritance (segregation) defects**, improperly condensed mitotic chromosomes, and structurally abnormal, disorganized polytene chromosomes (Hari, Cook & Karpen 2001) [PMID: 11390354](https://pubmed.ncbi.nlm.nih.gov/11390354/).

Critically for localization, the SU(VAR)2-10 protein *"colocalize[s] with nuclear lamin in interphase, and little to no SU(VAR)2-10 is found on condensed mitotic chromosomes."* It localizes to some polytene telomeres, and mutants show defective telomere clustering and loss of telomere–nuclear-lamina associations. The authors proposed that *"Su(var)2-10 controls multiple aspects of chromosome structure and function by establishing/maintaining chromosome organization in interphase nuclei."* This defines both a **structural/organizational role** and the **subcellular compartment** (the nuclear periphery/lamina, in interphase) where part of the protein's function is executed.

### Finding 4 — Su(var)2-10/dPIAS negatively regulates JAK/STAT (Stat92E) signaling

Consistent with the defining property of the PIAS family (**P**rotein **I**nhibitor of **A**ctivated **STAT**), Su(var)2-10/dPIAS functions as a **negative regulator of JAK/STAT signaling** in *Drosophila*. Betz et al. (2001) demonstrated *"the in vivo functional interaction of the Drosophila homologues stat92E and a Drosophila PIAS gene (dpias)"* using a dpias loss-of-function allele and conditional overexpression in JAK-STAT mutant backgrounds, concluding that *"the correct dpias/stat92E ratio is crucial for blood cell and eye development"* [PMID: 11504941](https://pubmed.ncbi.nlm.nih.gov/11504941/). This establishes a **dose-dependent, in vivo regulatory relationship** between dPIAS and Stat92E.

The signaling role is embedded in a broader SUMO-tumor-suppressive context: loss of SUMO pathway components (E1/E2/E3, including PIAS) causes hematopoietic progenitors to fail to quiesce and form microtumors [PMID: 23213407](https://pubmed.ncbi.nlm.nih.gov/23213407/). More recent work (Vincze et al. 2026) reports that selective autophagy *"fine-tunes Stat92E activity by degrading Su(var)2-10/PIAS"* in glia, confirming Su(var)2-10/PIAS as a regulator of Stat92E whose own level is controlled by autophagic turnover [PMID: 41500791](https://pubmed.ncbi.nlm.nih.gov/41500791/).

### Finding 5 — Catalytic mechanism and domain division of labor (SP-RING activates E2~SUMO; PINIT redirects target-lysine specificity; SAP mediates nuclear/DNA targeting)

Su(var)2-10 shares the conserved **Siz/PIAS tripartite architecture**, for which precise catalytic mechanisms have been established in orthologs. The X-ray structure of the founding Siz/PIAS ligase **Siz1** (Yunus & Lima 2009) showed that *"the SP-RING and SP-CTD are required for activation of the E2 approximately SUMO thioester, while the PINIT domain is essential for redirecting SUMO conjugation to the proliferating cell nuclear antigen (PCNA) at lysine 164, a nonconsensus lysine residue that is not modified by the SUMO E2 in the absence of Siz1"* [PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/). This defines a clean division of labor: **SP-RING = catalysis (E2~SUMO activation)**; **PINIT = substrate/target-lysine specificity**.

Domain-dissection of the orthologous yeast Ull1/Siz1 (Takahashi & Kikuchi 2005) confirmed that *"a novel conserved N-terminal domain, called PINIT, as well as the RING-like domain (SP-RING) were required for the SUMO ligase activity,"* whereas the SAP motif *"was not required for the ligase activity but was involved in nuclear localization"* [PMID: 16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/). Arabidopsis SIZ1 point-mutant complementation (Cheong et al. 2010) similarly mapped separable functions to the PINIT, SAP, and SP-RING domains [PMID: 20404572](https://pubmed.ncbi.nlm.nih.gov/20404572/). By homology, Su(var)2-10's SP-RING catalyzes, its PINIT selects substrates and non-consensus lysines, and its SAP directs the enzyme to chromatin — consistent with its observed chromatin/nuclear-lamina localization.

### Finding 6 & 8 — Bonus (Drosophila TIF1) is a defined SUMO substrate; SUMOylation nucleates SetDB1/NuRD repressive complexes ("SUMO as molecular glue")

The most precisely resolved substrate of Su(var)2-10 is **Bonus**, the single *Drosophila* homolog of the mammalian **TIF1 (Transcription Intermediary Factor)** family. Godneeva, Ninova, Fejes-Tóth & Aravin (2023) established that *"the conserved family of Transcription Intermediary Factors (TIF1) proteins consists of key transcriptional regulators that control transcription of target genes by modulating chromatin state"* and showed that **Bonus SUMOylation is mediated by the SUMO E3-ligase Su(var)2-10** [PMID: 37999956](https://pubmed.ncbi.nlm.nih.gov/37999956/) (preprint [PMID: 37645991](https://pubmed.ncbi.nlm.nih.gov/37645991/)).

Mechanistically, Bonus is SUMOylated at a **single N-terminal site conserved among insects**, and this modification is **indispensable for its repressive activity**. SUMOylation influences Bonus's subnuclear localization, its association with chromatin, and its interaction with the histone methyltransferase SetDB1. Bonus-induced silencing requires both **SetDB1** and the **NuRD** chromatin remodeler and is accompanied by **H3K9me3 accumulation**. Functionally, this axis safeguards germline identity by silencing tissue-specific genes in the ovary. This is the clearest demonstration of the **"SUMO-as-glue"** model: a single SUMO mark placed by Su(var)2-10 serves as the nucleation point that assembles a multi-protein repressive complex on chromatin.

### Finding 7 — Bioinformatic confirmation of domain architecture and nuclear SUMO-transferase annotation (UniProt Q7KNF5)

The UniProt Q7KNF5 record (**554 aa, ~61.7 kDa, isoform A**) independently confirms the functional model. It annotates the canonical PIAS tripartite architecture at defined boundaries: an **N-terminal SAP domain (residues 2–36)**, a **central PINIT domain (113–278)**, and the **catalytic SP-RING-type zinc finger (310–391)**, followed by a large **C-terminal intrinsically disordered region (402–554)** carrying polar and basic/acidic compositional biases (consistent with a SUMO-interacting / SP-CTD substrate-binding region). Keyword/annotation highlights include: **Nucleus**; **Transferase**; **Zinc-finger / Metal-binding / Zinc**; **"Ubl conjugation pathway"**; **Pathway = Protein modification; protein sumoylation**; **Subcellular location = Nucleus**; **family = PIAS**. The bioinformatic annotation is in complete agreement with the experimental and structural literature.

---

## Mechanistic Model / Interpretation

Su(var)2-10 is best understood as a **nuclear molecular machine that converts recognition events into chromatin marks using SUMO as the linking currency.** The protein does not silence genes by itself; rather, it tags substrate proteins with SUMO, and those SUMO marks act as docking surfaces (molecular glue) that nucleate the assembly of H3K9 methyltransferase and remodeling complexes.

### Domain division of labor

```
        N ──[ SAP ]────────[ PINIT ]──────[ SP-RING / MIZ ]────[ C-terminal IDR / SP-CTD ]── C
            2–36            113–278          310–391              402–554
             │                 │                │                     │
   Chromatin/DNA &      Substrate &      Catalysis:            SUMO-interaction /
   nuclear targeting    target-lysine    activates E2~SUMO     substrate binding
                        selection        (Ubc9) thioester
```

### The SUMO conjugation cascade and the silencing output

```
   SUMO (Smt3)
      │  E1 activation (Aos1/Uba2)
      ▼
   E1 ~ SUMO
      │  trans-thiolation
      ▼
   E2 (Ubc9) ~ SUMO ──────────────┐
                                   │  Su(var)2-10 SP-RING activates the
                                   │  E2~SUMO thioester; PINIT positions
                                   ▼  the target lysine
   SUBSTRATE–K–SUMO  (e.g., Bonus/TIF1 at a single conserved N-terminal Lys)
                                   │
                                   │  SUMO acts as "molecular glue"
                                   ▼
        Recruitment of SetDB1(Eggless)/Wde HMT  +  NuRD remodeler
                                   │
                                   ▼
                H3K9me3 deposition → heterochromatin / transcriptional silencing
```

### Two complementary targeting routes to the same output

| Route | Recognition module | Su(var)2-10 action | Effector recruited | Outcome |
|-------|--------------------|--------------------|--------------------|---------|
| piRNA pathway (germline) | piRNA/Piwi target-recognition complex | Binds complex; SUMO-conjugates local factors | SetDB1/Wde | H3K9me3 silencing of transposons [PMID: 31901446](https://pubmed.ncbi.nlm.nih.gov/31901446/) |
| TIF1 co-repressor route | Bonus (TIF1) bound at target genes | SUMOylates Bonus at single N-terminal Lys | SetDB1 + NuRD | H3K9me3 silencing of tissue-specific genes; germline identity [PMID: 37999956](https://pubmed.ncbi.nlm.nih.gov/37999956/) |

Both routes converge on **SetDB1-dependent H3K9me3**, explaining why *"most of the H3K9me3 mark depends on SUMO and the SUMO ligase Su(var)2-10"* [PMID: 31901448](https://pubmed.ncbi.nlm.nih.gov/31901448/).

### Reconciling the "moonlighting" roles

The chromatin-structure role (telomere clustering, nuclear-lamina association, interphase organization) and the JAK/STAT role are coherent extensions of the same core biochemistry:

- **Chromatin architecture** — the SAP domain anchors Su(var)2-10 to chromatin and the nuclear lamina, and SUMO-dependent assembly of heterochromatin contributes to higher-order interphase organization (telomere–lamina tethering, polytene integrity) [PMID: 11390354](https://pubmed.ncbi.nlm.nih.gov/11390354/).
- **JAK/STAT regulation** — as a canonical PIAS, Su(var)2-10 restrains activated Stat92E, with the dpias/stat92E ratio determining developmental outcomes in blood and eye [PMID: 11504941](https://pubmed.ncbi.nlm.nih.gov/11504941/). Its own abundance is tuned by selective autophagy [PMID: 41500791](https://pubmed.ncbi.nlm.nih.gov/41500791/).

**Primary function (bottom line):** Su(var)2-10 is a **nuclear SUMO (Smt3) protein transferase (E3 ligase)**. Its substrate specificity is directed by the PINIT domain toward nuclear chromatin-regulatory proteins (e.g., Bonus/TIF1) and target-recognition complexes (piRNA/Piwi), and its catalytic output is the SUMO-dependent assembly of SetDB1/Wde(/NuRD) complexes that deposit H3K9me3. It functions **in the nucleus**, at chromatin and the nuclear periphery.

---

## Evidence Base

| PMID | Study | Relevance to findings |
|------|-------|------------------------|
| [11390354](https://pubmed.ncbi.nlm.nih.gov/11390354/) | *The Drosophila Su(var)2-10 locus regulates chromosome structure and function and encodes a member of the PIAS protein family* (Hari, Cook & Karpen 2001) | Foundational: identifies gene as PIAS family; defines nuclear-lamina/interphase localization and chromosome-structure role. Supports F001, F003. |
| [31901446](https://pubmed.ncbi.nlm.nih.gov/31901446/) | *Su(var)2-10 and the SUMO Pathway Link piRNA-Guided Target Recognition to Chromatin Silencing* (Ninova et al. 2020, *Mol Cell*) | Primary mechanism: binds piRNA/Piwi, SUMO-dependent SetDB1/Wde recruitment. Supports F002. |
| [31901448](https://pubmed.ncbi.nlm.nih.gov/31901448/) | *The SUMO Ligase Su(var)2-10 Controls Hetero- and Euchromatic Gene Expression via Establishing H3K9 Trimethylation and Negative Feedback Regulation* (Ninova et al. 2020, *Genes Dev*) | Genome-wide: most H3K9me3 depends on SUMO/Su(var)2-10. Supports F002. |
| [37999956](https://pubmed.ncbi.nlm.nih.gov/37999956/) / [37645991](https://pubmed.ncbi.nlm.nih.gov/37645991/) | *SUMOylation of Bonus, the Drosophila TIF1 homolog...* (Godneeva et al. 2023) | Defines a specific substrate (Bonus/TIF1) SUMOylated by Su(var)2-10; single conserved site; recruits SetDB1/NuRD. Supports F006, F008. |
| [11504941](https://pubmed.ncbi.nlm.nih.gov/11504941/) | *A Drosophila PIAS homologue negatively regulates stat92E* (Betz et al. 2001) | Establishes dPIAS as negative regulator of JAK/STAT (Stat92E). Supports F004. |
| [23213407](https://pubmed.ncbi.nlm.nih.gov/23213407/) | *Sumoylation is tumor-suppressive and confers proliferative quiescence to hematopoietic progenitors...* (Kalamarz et al. 2012) | Places PIAS as E3 downstream of Ubc9; tumor-suppressive SUMO signaling in blood. Supports F001, F004. |
| [19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/) | *Structure of the Siz/PIAS SUMO E3 ligase Siz1 and determinants required for SUMO modification of PCNA* (Yunus & Lima 2009) | Structural mechanism: SP-RING activates E2~SUMO; PINIT redirects to non-consensus lysine. Supports F005. |
| [16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/) | *Yeast PIAS-type Ull1/Siz1 is composed of SUMO ligase and regulatory domains* (Takahashi & Kikuchi 2005) | PINIT + SP-RING required for ligase activity; SAP dispensable for catalysis but for nuclear localization. Supports F005. |
| [20404572](https://pubmed.ncbi.nlm.nih.gov/20404572/) | *Structural and functional studies of SIZ1, a PIAS-type SUMO E3 ligase from Arabidopsis* (Cheong et al. 2010) | Separable domain functions (PINIT/SAP/SP-RING). Supports F005. |
| [41500791](https://pubmed.ncbi.nlm.nih.gov/41500791/) | *Selective autophagy fine-tunes Stat92E activity by degrading Su(var)2-10/PIAS* (Vincze et al. 2026) | Su(var)2-10 level is regulated by autophagy to tune Stat92E. Supports F004. |
| [18583943](https://pubmed.ncbi.nlm.nih.gov/18583943/) | *Cytoplasmic sumoylation by PIAS-type Siz1-SUMO ligase* | Context: PIAS/Siz regulatory domains outside SP-RING govern localization and substrate access. |
| [18502747](https://pubmed.ncbi.nlm.nih.gov/18502747/) | *The PHD domain of plant PIAS proteins mediates sumoylation of bromodomain GTE proteins* | Context: PIAS domains beyond SP-RING contribute to substrate selection and chromatin-factor SUMOylation. |
| [30242710](https://pubmed.ncbi.nlm.nih.gov/30242710/) | *Strategies to Trap Enzyme-Substrate Complexes...During E3-Mediated Ubiquitin-Like Protein Ligation* | Context: general RING/SP-RING E3 mechanism — stabilizing E2-Ubl thioester for nucleophilic attack by substrate lysine. |
| [17159999](https://pubmed.ncbi.nlm.nih.gov/17159999/) | *H3K9 methylation and RNA interference regulate nucleolar organization and repeated DNA stability* | Context: links H3K9 methylation to nuclear/repeat-DNA architecture, consistent with the silencing output of Su(var)2-10. |
| [28195188](https://pubmed.ncbi.nlm.nih.gov/28195188/) | *SUMO regulates the activity of Smoothened and Costal-2 in Drosophila Hedgehog signaling* | Context: shows Drosophila PIAS (E3) participates in SUMOylation events in Hedgehog signaling — a potential additional pathway. |

### How the evidence converges

The strongest evidence is **experimental and specific**: direct genetic/molecular identification of the gene as PIAS (11390354), direct demonstration of the piRNA→SUMO→SetDB1 mechanism in *Drosophila* (31901446, 31901448), and substrate-resolved biochemistry of Bonus SUMOylation (37999956). These are complemented by **structural mechanism** from orthologs (19748360, 16109721, 20404572) that explains *how* each domain contributes. The convergence of genetics, genomics, biochemistry, structure, and UniProt bioinformatic annotation (Q7KNF5) gives high confidence in the functional model.

---

## Limitations and Knowledge Gaps

1. **Few validated direct substrates in *Drosophila*.** The only mechanistically resolved endogenous substrate is Bonus/TIF1. The piRNA-pathway work establishes that Su(var)2-10 induces SUMO-dependent SetDB1 recruitment, but the complete catalog of relevant lysine-SUMOylated substrates at target loci remains incompletely defined.

2. **Mechanistic details inferred from orthologs.** The precise catalytic roles of Su(var)2-10's SP-RING and PINIT domains (E2~SUMO activation; non-consensus lysine targeting) are established for Siz1/SIZ1 in yeast and plants (19748360, 16109721, 20404572), not from a *Drosophila* Su(var)2-10 crystal structure. There is no published high-resolution structure of Q7KNF5 itself.

3. **SUMO-binding function of the C-terminal IDR is annotated by bioinformatics, not experiment.** The large C-terminal disordered region (402–554) is inferred to serve SUMO-interaction/SP-CTD functions; direct biochemical validation in the fly protein is lacking.

4. **Boundary between catalytic and non-catalytic (structural) roles is unclear.** It is not fully resolved how much of the chromosome-architecture/telomere–lamina phenotype depends on SUMO ligase catalytic activity versus a scaffolding function of the SAP-anchored protein.

5. **Scope of non-chromatin signaling roles.** The JAK/STAT (Stat92E) regulatory role is genetically well supported but its molecular basis (which STAT lysines, or sequestration vs. SUMOylation) is less defined in the fly. The Hedgehog-pathway SUMO involvement (28195188) suggests additional pathways that have not been dissected for Su(var)2-10 specifically.

6. **One cited study is a very recent/forward-dated report** (41500791, Vincze et al. 2026). It corroborates the Stat92E-regulation role but should be regarded as newer, less-replicated evidence.

---

## Proposed Follow-up Experiments / Actions

1. **Define the direct SUMO substrate catalog in vivo.** Perform SUMO-site proteomics (e.g., K-ε-GG/SUMO-remnant immunoprecipitation mass spectrometry) in wild-type versus *Su(var)2-10* catalytic-dead backgrounds in ovary/germline to identify lysine-SUMOylation events that are strictly Su(var)2-10-dependent.

2. **Separation-of-function catalytic-dead rescue.** Engineer SP-RING zinc-coordinating mutants (catalytically dead) and PINIT substrate-selection mutants of Su(var)2-10 and test which phenotypes (H3K9me3 silencing vs. telomere–lamina architecture vs. Stat92E regulation) require catalysis versus scaffolding.

3. **Solve or model the Su(var)2-10 structure.** Determine a cryo-EM/crystal structure of the Su(var)2-10•Ubc9~SUMO•substrate (e.g., Bonus peptide) complex, or build a validated AlphaFold model, to confirm that the inferred Siz1-like catalytic geometry holds for the fly enzyme and to map the non-consensus target-lysine positioning.

4. **Dissect the SAP/chromatin-targeting contribution.** Use SAP-domain deletions/point mutants to quantify how DNA/chromatin anchoring contributes to target-locus selection, H3K9me3 spreading, and telomere–nuclear-lamina tethering.

5. **Characterize the C-terminal IDR as a SUMO-interaction module.** Test SUMO-binding (SIM-like) activity of residues 402–554 biochemically and determine whether it supports poly-SUMO chain recognition or product release.

6. **Molecular basis of Stat92E regulation.** Determine whether Su(var)2-10 regulates Stat92E by SUMOylation of specific lysines, by nuclear sequestration, or by promoting chromatin silencing of STAT target genes — and relate this to autophagic turnover of Su(var)2-10 (41500791).

---

## Final Answer

**Su(var)2-10 (dPIAS, Q7KNF5) is the principal *Drosophila* PIAS-family SUMO (Smt3) E3 ligase.** Its catalytic SP-RING/MIZ zinc finger activates the SUMO-charged E2 Ubc9 to transfer SUMO onto substrate lysines; the PINIT domain confers substrate/target-lysine specificity and the SAP domain anchors the enzyme to chromatin and the nucleus. Its primary function is to convert target recognition into SUMO-dependent assembly of H3K9-methyltransferase silencing machinery — binding the piRNA/Piwi complex and SUMOylating chromatin co-repressors such as the TIF1 homolog Bonus to recruit SetDB1(/Wde)/NuRD and deposit repressive H3K9me3 — thereby driving heterochromatin formation and transposon/tissue-specific gene silencing. It additionally organizes interphase chromosome and telomere–nuclear-lamina architecture and acts as a negative regulator of JAK/STAT (Stat92E) signaling. It carries out these functions in the **nucleus**, at chromatin and the nuclear periphery.


## Artifacts

- [OpenScientist final report](Su-var-2-10-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Su-var-2-10-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11390354
2. PMID:23213407
3. PMID:31901446
4. PMID:31901448
5. PMID:11504941
6. PMID:41500791
7. PMID:19748360
8. PMID:16109721
9. PMID:20404572
10. PMID:37999956
11. PMID:37645991