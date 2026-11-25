---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T18:45:47.594499'
end_time: '2026-10-24T19:12:19.818813'
duration_seconds: 1592.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SCGB2A1
  gene_symbol: SCGB2A1
  uniprot_accession: O75556
  protein_description: 'RecName: Full=Mammaglobin-B; AltName: Full=Lacryglobin; AltName:
    Full=Lipophilin-C; AltName: Full=Mammaglobin-2; AltName: Full=Secretoglobin family
    2A member 1; Flags: Precursor;'
  gene_info: Name=SCGB2A1; Synonyms=LIPHC, MGB2, UGB3;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the secretoglobin family. Lipophilin subfamily.
  protein_domains: Secretoglobin. (IPR016126); Secretoglobin_sf. (IPR035960); Uteroglobin
    (PF01099)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SCGB2A1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SCGB2A1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O75556
- **Protein Description:** RecName: Full=Mammaglobin-B; AltName: Full=Lacryglobin; AltName: Full=Lipophilin-C; AltName: Full=Mammaglobin-2; AltName: Full=Secretoglobin family 2A member 1; Flags: Precursor;
- **Gene Information:** Name=SCGB2A1; Synonyms=LIPHC, MGB2, UGB3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the secretoglobin family. Lipophilin subfamily.
- **Key Domains:** Secretoglobin. (IPR016126); Secretoglobin_sf. (IPR035960); Uteroglobin (PF01099)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SCGB2A1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SCGB2A1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SCGB2A1** (gene ID: SCGB2A1, UniProt: O75556) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SCGB2A1 (Mammaglobin-B / Lipophilin C): Functional Annotation Report

**Gene:** SCGB2A1 (synonyms: LIPHC, MGB2, UGB3)
**Protein:** Mammaglobin-B / Lacryglobin / Lipophilin-C / Mammaglobin-2 / Secretoglobin family 2A member 1
**UniProt:** O75556 | **Organism:** *Homo sapiens* (Human) | **Locus:** chromosome 11q12–q13.1
**Family:** Secretoglobin superfamily, Lipophilin subfamily
**Domains:** Secretoglobin (IPR016126); Secretoglobin_sf (IPR035960); Uteroglobin (PF01099)

---

## Summary

**SCGB2A1 encodes Mammaglobin-B (Lipophilin C), a small (~77-residue mature chain, ~8.9 kDa, acidic pI ≈ 4.94) secreted protein of the secretoglobin (uteroglobin) superfamily.** Its primary, best-supported function is **non-enzymatic binding and sequestration of small hydrophobic ligands — principally steroids and lipids — within the central hydrophobic cavity of a disulfide-locked, α-helical heterodimer.** It has no known catalytic activity; it is not a classical enzyme, transporter, or cytoskeletal structural protein. Rather, it belongs to a family of secreted "lipid-loving" carrier/sequestration proteins. SCGB2A1 was first identified biochemically as the covalent **"lipophilin AC" heterodimer** in human tears, where it pairs with Lipophilin A (SCGB1D1), and was independently cloned as "mammaglobin B," a uteroglobin-family gene on chromosome 11q12–q13.1.

The protein functions **extracellularly** — it is secreted into tear fluid, prostatic fluid, and other glandular secretions, where it is proposed to contribute to the tear-film lipid layer and to the handling of lipophilic molecules. The functional inference rests on three convergent lines of evidence: (1) direct biochemical isolation of the tear heterodimer, with the measured mass of tear lipophilin C (8854.1 Da) exactly matching the computed mature chain of O75556; (2) an identical cysteine framework to the biophysically characterized mammaglobin-A/lipophilin-B complex, which is a head-to-tail, three-disulfide α-helical globule; and (3) experimental ligand-binding and ligand-transfer activity of its direct rodent homolog, rat prostatein (prostatic steroid-binding protein), which binds steroids/carcinogens with high affinity and transfers them to intracellular receptors.

Expression of SCGB2A1 is **driven by androgen signaling through an unusual indirect, Sp1/Sp3-mediated promoter mechanism** (the androgen receptor is recruited but does not bind DNA directly), and is largely restricted to androgen-responsive secretory epithelia — prostate, lacrimal/ocular glands, pituitary, and respiratory/mammary tissue. Its prominence as a breast- and epithelial-cancer micrometastasis biomarker reflects this tissue-restricted secretory expression rather than any defined oncogenic driver function.

---

## Key Findings

### Finding 1 — SCGB2A1 is a small secreted lipophilin that forms a disulfide-linked heterodimer with Lipophilin A (SCGB1D1)

SCGB2A1/Mammaglobin-B (also called lipophilin C, lacryglobin) is a small secreted protein of roughly 77 residues in its mature form (measured mass 8854.1 Da, pI 4.94). It is homologous to the rat prostatein C3 subunit, to mammaglobin A, and to CC10/uteroglobin. The protein was first isolated biochemically from **human tears** as a covalent heterodimer named **"lipophilin AC,"** paired with **lipophilin A (SCGB1D1)** — a basic 69-residue chain (mass 7575.1 Da, pI 9.47). The complex is stabilized by three cystine disulfide bonds, and the heterodimers can undergo further non-covalent assembly into tetramers; some are glycosylated [[PMID: 9720917](https://pubmed.ncbi.nlm.nih.gov/9720917/); [PMID: 11193779](https://pubmed.ncbi.nlm.nih.gov/11193779/)].

> *"We identified a novel heterodimeric protein, lipophilin AC, in human tears. One of its components, lipophilin A (69 residues; mass, 7575.1; pI, 9.47) was homologous to the C1 and C2 components of prostatein"* [[PMID: 9720917](https://pubmed.ncbi.nlm.nih.gov/9720917/)].

> *"These proteins form covalent heterodimers that are stabilized by three intramolecular cystine disulfide bonds. The heterodimers, some of which are glycosylated, may undergo additional non-covalent assembly to form tetramers."* [[PMID: 11193779](https://pubmed.ncbi.nlm.nih.gov/11193779/)].

The gene was independently cloned as "mammaglobin B" (MGB2), a member of the uteroglobin gene family, placing it firmly in the secretoglobin superfamily alongside rabbit uteroglobin, human Clara Cell 10-kDa protein (CC10), and the multimeric rat prostatein [[PMID: 9806831](https://pubmed.ncbi.nlm.nih.gov/9806831/)].

### Finding 2 — SCGB2A1 is a secreted hydrophobic-ligand (steroid/lipid) binding protein acting extracellularly

By homology to rat prostatein (an estramustine/steroid-binding protein) and to uteroglobin — the founding secretoglobin, which binds and sequesters hydrophobic ligands (progesterone, retinols, phospholipids, prostaglandins, polychlorinated biphenyls) and inhibits secretory phospholipase A2 — SCGB2A1 is inferred to be a **hydrophobic-ligand binding protein** [[PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)]. It is secreted into tear fluid where, as an androgen-regulated secretoglobin that "most likely binds hydrophobic ligands," it is proposed to contribute to **tear-film lipid-layer formation and function** [[PMID: 16395610](https://pubmed.ncbi.nlm.nih.gov/16395610/)].

> *"an androgen-regulated secretoglobin, which most likely binds hydrophobic ligands, for tear film lipid layer formation and function is discussed"* [[PMID: 16395610](https://pubmed.ncbi.nlm.nih.gov/16395610/)].

> *"It inhibits soluble phospholipase A(2) activity and binds and perhaps sequesters hydrophobic ligands such as progesterone, retinols, polychlorinated biphenyls, phospholipids, and prostaglandins."* [[PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)].

No direct catalytic activity is known for SCGB2A1. Its function is **extracellular** — it is a lipid-binding constituent of secretions including the prostatic fluid of rats and the tears of humans and rabbits [[PMID: 11193779](https://pubmed.ncbi.nlm.nih.gov/11193779/)].

### Finding 3 — Expression is androgen-controlled via an indirect Sp1/Sp3 mechanism, in androgen-responsive epithelia

In androgen-responsive LNCaP prostate cells, SCGB2A1 is induced **more than 20-fold** by dihydrotestosterone within 6 hours. Strikingly, the androgen receptor (AR) is recruited to the proximal promoter within 10 minutes but **does not bind the DNA directly**; instead, a 32-bp dimeric inverted-repeat GC box ("dim-IR-GA box") bound by the Sp1/Sp3 transcription factors is required. This defines SCGB2A1 as a member of a new class of **indirect AR target genes** whose androgen responsiveness is mediated by DNA-bound Sp factors [[PMID: 16020486](https://pubmed.ncbi.nlm.nih.gov/16020486/)].

> *"SCGB 2A1 is under androgen control in the androgen-responsive prostatic cell line LNCaP and can be induced more than 20-fold by dihydrotestosterone"* and *"we propose that SCGB 2A1 represents a new class of androgen target genes that are purely under indirect AR control mediated by DNA-bound Sp factors"* [[PMID: 16020486](https://pubmed.ncbi.nlm.nih.gov/16020486/)].

Consistent with androgen control, SCGB2A1 is expressed in all ocular glands, the keratinized stratified squamous epithelium of the eyelid, the conjunctival epithelium, and the orbicularis oculi muscle — tissues that co-express AR [[PMID: 16395610](https://pubmed.ncbi.nlm.nih.gov/16395610/)]. It is among the most prominently expressed secretoglobin mRNAs in the normal human **pituitary** [[PMID: 15668787](https://pubmed.ncbi.nlm.nih.gov/15668787/)], is detectable at low levels in normal lung with neo-/up-regulation in lung cancers [[PMID: 12826312](https://pubmed.ncbi.nlm.nih.gov/12826312/)], and lipophilin genes generally are widely expressed, especially in endocrine-responsive organs [[PMID: 10066439](https://pubmed.ncbi.nlm.nih.gov/10066439/)].

### Finding 4 — Dysregulation in epithelial cancers is associative (biomarker), not a defined oncogenic mechanism

Mammaglobin-B mRNA is absent in normal lymph nodes but detectable in primary breast and digestive-tract carcinomas, which has enabled its use as an **RT-PCR marker for axillary and abdominal lymph-node micrometastases** [[PMID: 10674878](https://pubmed.ncbi.nlm.nih.gov/10674878/); [PMID: 10755390](https://pubmed.ncbi.nlm.nih.gov/10755390/)].

> *"The transcript of mammaglobin B gene was detected in none of the control lymph nodes, but in all of the 14 primary breast cancers."* [[PMID: 10674878](https://pubmed.ncbi.nlm.nih.gov/10674878/)].

Importantly, when secretoglobins were functionally tested in ovarian carcinoma, the proliferative effect was driven by **concerted overexpression of mammaglobin-1 (MGB1/SCGB2A2) and lipophilin B (SCGB1D2) — not by MGB2/SCGB2A1** — and only MGB1 correlated with FIGO stage and grade [[PMID: 24603286](https://pubmed.ncbi.nlm.nih.gov/24603286/)]. This clarifies that SCGB2A1's role in cancer is associative (a tissue-restricted secretion marker), rather than a demonstrated oncogenic driver.

> *"Concerted overexpression of MGB1 and LIPB resulted in significant increase in cell proliferation."* [[PMID: 24603286](https://pubmed.ncbi.nlm.nih.gov/24603286/)].

Aptamers against MGB2 have been developed for circulating-tumor-cell detection, underscoring its biomarker (not mechanistic) utility [[PMID: 29101327](https://pubmed.ncbi.nlm.nih.gov/29101327/)].

### Finding 5 — Sequence analysis of O75556 confirms a secreted 77-residue acidic secretoglobin chain with three cysteines

Direct analysis of the UniProt O75556 sequence (a 95-aa precursor) reveals an N-terminal signal peptide (MKLLMVLMLAALLLHCYA, residues 1–18) preceding a **77-residue mature chain** (residues 19–95). The computed average mass of the mature chain is **8854.1 Da — exactly matching the measured mass of tear lipophilin C** (8854.1 Da; [[PMID: 9720917](https://pubmed.ncbi.nlm.nih.gov/9720917/)]). The mature chain is acidic (Asp+Glu = 12 vs. Lys+Arg+His = 10), consistent with the reported pI 4.94. It contains exactly **three cysteines** (mature positions 4, 47, 72), matching the three cystine disulfide bonds that stabilize the secretory-lipophilin heterodimer [[PMID: 11193779](https://pubmed.ncbi.nlm.nih.gov/11193779/)]. A single N-glycosylation sequon (N-Q-S at Asn68) is consistent with the report that some lipophilins are glycosylated.

> *"Human lipophilin C (77 residues; mass, 8854.1; pI, 4.94) was homologous to the rat prostatein C3 component and to human mammaglobin"* [[PMID: 9720917](https://pubmed.ncbi.nlm.nih.gov/9720917/)].

This bioinformatic correspondence provides a rigorous identity check: UniProt O75556 is unambiguously the tear lipophilin C characterized biochemically by Lehrer and colleagues, satisfying the mandatory gene-identity verification requirement. The gene symbol SCGB2A1, the organism (human), and the secretoglobin/uteroglobin family/domain annotations all align with the literature.

### Finding 6 — Identical cysteine framework to mammaglobin A implies an analogous head-to-tail, three-disulfide α-helical heterodimer

Cross-family sequence comparison shows that SCGB2A1 (O75556) and SCGB2A2/mammaglobin A (Q13296) have four cysteines at **identical precursor positions (16, 22, 65, 90)**; position 16 lies in the signal peptide, leaving three cysteines in each mature chain. Their partner chains, SCGB1D1/lipophilin A (O95968) and SCGB1D2/lipophilin B (O95969), share an identical six-cysteine framework (6, 15, 16, 24, 65, 88). The experimentally characterized paralogous complex — mammaglobin A covalently bound to lipophilin B — is a small α-helical globule joined **head-to-tail by exactly three disulfide bridges**, with signal-sequence cleavage after residues 19 (mammaglobin) and 21 (lipophilin B) and N-glycans at each pole [[PMID: 12022875](https://pubmed.ncbi.nlm.nih.gov/12022875/)].

> *"Molecular modeling, secondary structure prediction, and circular dichroism indicate that the complex is a small alpha-helical globule that has three disulfide bridges and a carbohydrate chain at each pole. LC-ESI-MS shows that mammaglobin and lipophilin B are bonded in a head to tail orientation."* [[PMID: 12022875](https://pubmed.ncbi.nlm.nih.gov/12022875/)].

Because SCGB2A1 has the same cysteine spacing and signal-peptide cleavage architecture, it is inferred to form the structurally analogous three-disulfide heterodimer with its partner lipophilin A (SCGB1D1) — precisely as directly observed for the lipophilin AC complex in tears [[PMID: 9720917](https://pubmed.ncbi.nlm.nih.gov/9720917/)].

### Finding 7 — The rat prostatein homolog experimentally binds steroids/xenobiotics and transfers them to receptors

Lipophilin C/SCGB2A1 is the human homolog of the **C3 subunit of rat prostatein** (prostatic steroid-binding protein, PSP). PSP is a highly abundant prostatic protein that "binds carcinogens reversibly and with high affinity." Purified PSP labeled with [³H]dioxin (TCDD) achieved **complete in vitro transfer of ligand from PSP to the rat hepatic dioxin receptor**, indicating a physiological role in cellular transfer/handling of hydrophobic ligands [[PMID: 3040289](https://pubmed.ncbi.nlm.nih.gov/3040289/)]. A conserved dodecapeptide putative steroid-recognition motif is shared between PSP and cytochrome P-450scc, both of which use steroids as ligands/substrates [[PMID: 4040479](https://pubmed.ncbi.nlm.nih.gov/4040479/)].

> *"The prostatic steroid-binding protein (PSP) represents a highly abundant protein in the rat prostate which binds carcinogens reversibly and with high affinity."* and *"a complete in vitro transfer of ligand from PSP to the rat hepatic dioxin receptor was observed"* [[PMID: 3040289](https://pubmed.ncbi.nlm.nih.gov/3040289/)].

These experimental data on the direct homolog substantiate the inference that SCGB2A1 binds small hydrophobic ligands (steroids, lipophilic xenobiotics) within its secretoglobin cavity and may shuttle or sequester them.

---

## Mechanistic Model / Interpretation

The convergent evidence supports a coherent model of SCGB2A1 as an **androgen-driven, secreted hydrophobic-ligand carrier/sequestration protein** that operates extracellularly in glandular fluids.

### Molecular architecture

```
   SCGB2A1 precursor (95 aa, O75556)
   +--------------+--------------------------------------+
   | signal 1-18  |        mature chain 19-95 (77 aa)    |
   +--------------+--------------------------------------+
                           |  secretion, signal cleavage
                           v
            Mature Lipophilin C (8854.1 Da, pI 4.94, acidic)
            Cys at mature positions 4, 47, 72 ; N-glycan @ Asn68

   HETERODIMER ASSEMBLY (covalent, 3 disulfide bonds)

   Lipophilin A (SCGB1D1)  ==S-S==  Lipophilin C (SCGB2A1)
   basic, pI 9.47                    acidic, pI 4.94
          head ---------------------------- tail
          (alpha-helical globule, glycans at each pole)
                           |
                           v non-covalent
                      Tetramers

   INTERNAL HYDROPHOBIC CAVITY  ->  binds steroids / lipids /
                                    lipophilic xenobiotics
```

### Functional logic

The secretoglobin fold creates a boomerang-shaped, antiparallel pairing of two subunits whose α-helices enclose a central hydrophobic cavity. In the founding family member uteroglobin, this cavity binds progesterone, retinols, phospholipids, prostaglandins, and PCBs [[PMID: 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)]. SCGB2A1 is built to the same blueprint: an acidic chain that pairs with a basic partner (lipophilin A) into a charge-complementary, disulfide-locked heterodimer. The complementary charges of the A (basic, pI 9.47) and C (acidic, pI 4.94) chains likely favor the specific A–C pairing over homodimerization.

Functionally, three roles are plausible and mutually compatible:

| Role | Supporting evidence | Location |
|------|---------------------|----------|
| **Hydrophobic-ligand sequestration** (steroids, lipids) | Uteroglobin binds steroids/lipids [PMID 17916741]; prostatein binds carcinogens with high affinity [PMID 3040289] | Tears, prostatic/glandular fluid (extracellular) |
| **Ligand transfer/shuttling to receptors** | Prostatein transfers dioxin to the dioxin receptor in vitro [PMID 3040289] | Extracellular -> target cells |
| **Tear-film lipid-layer contribution** | Androgen-regulated secretoglobin in all ocular glands; proposed tear-film role [PMID 16395610] | Tear film surface |

### Regulatory circuit

```
   Androgen (DHT)
        |
        v
   Androgen Receptor --(recruited, but does NOT bind DNA)--+
        |                                                  |
        v                                                  v
   dim-IR-GA box (32 bp) <-- Sp1 / Sp3 (DNA-bound) --> SCGB2A1 transcription (>20x)
```

SCGB2A1 thus sits at the output of an androgen-signaling axis but is activated by a distinctive **tethered/indirect mechanism** in which AR acts through DNA-bound Sp1/Sp3 rather than a canonical androgen-response element [[PMID: 16020486](https://pubmed.ncbi.nlm.nih.gov/16020486/)]. This explains its expression pattern in androgen-responsive secretory epithelia (prostate, ocular/lacrimal glands, pituitary, respiratory and mammary tissue).

### Reconciling the cancer literature

SCGB2A1's detection in carcinomas and lymph-node micrometastases is a **downstream consequence of its tissue-restricted secretory expression**, exploited diagnostically, rather than evidence of an oncogenic function. The functional assay in ovarian carcinoma attributes proliferative effects to MGB1/LIPB and not to MGB2/SCGB2A1 [[PMID: 24603286](https://pubmed.ncbi.nlm.nih.gov/24603286/)], reinforcing that SCGB2A1 is best annotated as a **lineage/secretion biomarker** in oncology.

---

## Evidence Base

| PMID | Study (abbrev.) | Contribution | Strength |
|------|------|--------------|----------|
| [9720917](https://pubmed.ncbi.nlm.nih.gov/9720917/) | *Lipophilin, a novel heterodimeric protein of human tears* | Direct biochemical isolation of lipophilin AC; measured mass/pI of lipophilin C | Primary, biochemical — strongest identity evidence |
| [11193779](https://pubmed.ncbi.nlm.nih.gov/11193779/) | *Secretory lipophilins: a tale of two species* | Three-disulfide heterodimer, tetramer assembly, glycosylation; lipids in prostatic/tear secretions | Primary/review — core structural model |
| [12022875](https://pubmed.ncbi.nlm.nih.gov/12022875/) | *Purification/characterization of mammaglobin/lipophilin B complex* | Experimental structural model of paralogous 2A/1D complex (head-to-tail, 3 disulfides, α-helical) | Primary, biophysical — structural template |
| [16020486](https://pubmed.ncbi.nlm.nih.gov/16020486/) | *SCGB 2A1 under selective androgen control* | >20× DHT induction; indirect AR→Sp1/Sp3 mechanism | Primary, mechanistic — regulation |
| [16395610](https://pubmed.ncbi.nlm.nih.gov/16395610/) | *IHC of SCGB 2A1 in ocular glands* | Ocular/glandular localization; tear-film lipid-layer hypothesis | Primary, expression/localization |
| [3040289](https://pubmed.ncbi.nlm.nih.gov/3040289/) | *Prostatein in transfer of ligand to dioxin receptor* | Homolog binds carcinogens with high affinity; transfers ligand to receptor | Primary, functional — ligand-binding proof (homolog) |
| [4040479](https://pubmed.ncbi.nlm.nih.gov/4040479/) | *Steroid binding site common to P-450scc and PSP* | Conserved steroid-recognition dodecapeptide motif | Bioinformatic — ligand specificity hint |
| [17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/) | *Uteroglobin review* | Founding secretoglobin binds steroids/lipids, inhibits sPLA2 | Review — family-level function |
| [9806831](https://pubmed.ncbi.nlm.nih.gov/9806831/) | *Identification of mammaglobin B* | Places MGB2 in uteroglobin superfamily | Primary — family assignment |
| [10066439](https://pubmed.ncbi.nlm.nih.gov/10066439/) | *Lipophilins homologous to rat prostatein* | cDNA, chromosomal localization (11q12–q13.1), broad endocrine-organ expression | Primary — genomics/expression |
| [15668787](https://pubmed.ncbi.nlm.nih.gov/15668787/) | *Secretoglobins in human pituitary* | SCGB2A1 prominently expressed in pituitary | Primary — expression |
| [12826312](https://pubmed.ncbi.nlm.nih.gov/12826312/) | *Dysregulated secretoglobins in lung cancer* | Low in normal lung; up-/neo-regulated in lung tumors | Primary — expression |
| [10674878](https://pubmed.ncbi.nlm.nih.gov/10674878/) / [10755390](https://pubmed.ncbi.nlm.nih.gov/10755390/) | *Mammaglobin B micrometastasis markers* | Absent in normal nodes; biomarker in breast/digestive cancers | Primary — diagnostic |
| [24603286](https://pubmed.ncbi.nlm.nih.gov/24603286/) | *Secretoglobins in ovarian carcinoma* | Proliferation driven by MGB1/LIPB, not MGB2 | Primary, functional — clarifies non-driver role |
| [29101327](https://pubmed.ncbi.nlm.nih.gov/29101327/) | *MGB2/MGB1 aptamers for CTCs* | Diagnostic aptamer development | Primary — diagnostic tool |

**How the evidence fits together:** The *identity* of O75556 as tear lipophilin C is established by exact mass/sequence correspondence (Findings 5, 1). The *structure* is established directly (tear heterodimer; [PMID 9720917](https://pubmed.ncbi.nlm.nih.gov/9720917/)) and by a biophysically solved paralog ([PMID 12022875](https://pubmed.ncbi.nlm.nih.gov/12022875/)) sharing an identical cysteine framework (Finding 6). The *function* (hydrophobic-ligand binding/transfer) is inferred from the family ([PMID 17916741](https://pubmed.ncbi.nlm.nih.gov/17916741/)) and demonstrated experimentally for the direct homolog ([PMID 3040289](https://pubmed.ncbi.nlm.nih.gov/3040289/)) (Findings 2, 7). *Regulation and localization* are experimentally established in prostate and ocular tissue (Finding 3).

---

## Limitations and Knowledge Gaps

1. **No direct ligand-binding data for human SCGB2A1 itself.** The hydrophobic-ligand-binding function is inferred from (a) family membership (uteroglobin), (b) the direct homolog (rat prostatein), and (c) structural analogy to the mammaglobin-A/lipophilin-B complex. No published study has measured the binding affinity or identified the specific physiological ligand(s) of the human lipophilin-AC complex.

2. **No experimental 3D structure of the lipophilin-AC complex.** The three-disulfide, head-to-tail α-helical model is derived from the paralogous mammaglobin-A/lipophilin-B complex and from the shared cysteine framework — not from a crystal or NMR structure of SCGB2A1 itself.

3. **Physiological role in the tear film is a hypothesis.** The tear-film lipid-layer contribution is proposed on the basis of localization and androgen regulation; functional/knockout evidence is lacking.

4. **The in vivo significance of ligand transfer is unproven for the human protein.** Prostatein transfers dioxin to a receptor in vitro; whether SCGB2A1 performs analogous transfer in human tissues is untested.

5. **Loss-of-function phenotype unknown.** No knockout model or human genetic deficiency phenotype has been described, so the organism-level requirement for SCGB2A1 is undefined.

6. **Possible functional redundancy.** Multiple paralogous secretoglobins (SCGB1D1, SCGB1D2, SCGB2A2) co-express in overlapping tissues, complicating attribution of specific functions.

---

## Proposed Follow-up Experiments / Actions

1. **Direct ligand-binding assays.** Express and purify recombinant human lipophilin-AC (SCGB2A1·SCGB1D1) and test binding to candidate ligands (progesterone, dihydrotestosterone, retinoids, free fatty acids, phospholipids, PCBs/dioxin) by isothermal titration calorimetry, fluorescence displacement, or microscale thermophoresis. This would convert the inferred function into a measured one.

2. **High-resolution structure.** Solve the crystal or cryo-EM/NMR structure of the lipophilin-AC heterodimer, ideally with a bound ligand, to define the cavity dimensions and ligand-binding residues. Compare directly with the mammaglobin-A/lipophilin-B model.

3. **Tear-film functional assays.** Test whether purified lipophilin-AC alters tear-film lipid-layer stability, surface tension, or lipid organization in vitro (Langmuir trough / interfacial rheology) to validate the tear-film hypothesis.

4. **Ligand-transfer assays with human components.** Recapitulate the prostatein experiment using human SCGB2A1: load the complex with a labeled hydrophobic ligand and test transfer to candidate receptors (e.g., nuclear receptors) or to lipid membranes.

5. **Cell/tissue loss-of-function.** Use CRISPR knockout or knockdown in relevant secretory epithelial models (prostate, lacrimal-gland organoids) to assess effects on secretion composition and lipid handling.

6. **Define the physiological ligand in vivo.** Perform lipidomic/metabolomic pull-down (affinity capture of native lipophilin-AC from human tears/prostatic fluid followed by LC-MS of co-eluting small molecules) to identify the endogenous bound ligand(s).

7. **Dissect the AR→Sp1/Sp3 regulatory module.** Map the dim-IR-GA box occupancy genome-wide (ChIP-seq for AR, Sp1, Sp3) to test whether this indirect mechanism governs a broader regulon, clarifying SCGB2A1's place in androgen physiology.

---

## Conclusion

SCGB2A1/Mammaglobin-B (Lipophilin C) is a small, acidic, secreted secretoglobin whose **primary function is non-enzymatic binding and sequestration of small hydrophobic ligands (steroids/lipids) within the central cavity of a disulfide-locked α-helical heterodimer** with Lipophilin A (SCGB1D1). It acts **extracellularly** in glandular secretions — most directly demonstrated as the covalent lipophilin-AC complex in human tears, where it is implicated in tear-film lipid-layer function. Its expression is **driven by androgen signaling through an indirect Sp1/Sp3 promoter mechanism** and restricted largely to androgen-responsive secretory epithelia. Its use as a cancer micrometastasis biomarker reflects this tissue-restricted secretion, not a defined oncogenic role. The function is well-supported by structural analogy and by experimental ligand-binding/transfer data from its direct rat prostatein homolog, though direct biochemical characterization of the human protein's specific ligand remains an open goal.


## Artifacts

- [OpenScientist final report](SCGB2A1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SCGB2A1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9720917
2. PMID:11193779
3. PMID:9806831
4. PMID:17916741
5. PMID:16395610
6. PMID:16020486
7. PMID:15668787
8. PMID:12826312
9. PMID:10066439
10. PMID:10674878
11. PMID:10755390
12. PMID:24603286
13. PMID:29101327
14. PMID:12022875
15. PMID:3040289
16. PMID:4040479