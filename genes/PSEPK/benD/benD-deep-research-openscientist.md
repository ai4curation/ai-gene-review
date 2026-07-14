---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-13T11:30:16.793689'
end_time: '2026-07-13T11:56:12.506614'
duration_seconds: 1555.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: benD
  gene_symbol: benD
  uniprot_accession: Q88I37
  protein_description: 'SubName: Full=1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate
    dehydrogenase {ECO:0000313|EMBL:AAN68772.1}; EC=1.3.1.25 {ECO:0000313|EMBL:AAN68772.1};'
  gene_info: Name=benD {ECO:0000313|EMBL:AAN68772.1}; OrderedLocusNames=PP_3164 {ECO:0000313|EMBL:AAN68772.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the short-chain dehydrogenases/reductases (SDR)
  protein_domains: BenD. (IPR047686); NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS.
    (IPR020904); SDR_fam. (IPR002347); adh_short (PF00106)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: benD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: benD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I37
- **Protein Description:** SubName: Full=1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase {ECO:0000313|EMBL:AAN68772.1}; EC=1.3.1.25 {ECO:0000313|EMBL:AAN68772.1};
- **Gene Information:** Name=benD {ECO:0000313|EMBL:AAN68772.1}; OrderedLocusNames=PP_3164 {ECO:0000313|EMBL:AAN68772.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the short-chain dehydrogenases/reductases (SDR)
- **Key Domains:** BenD. (IPR047686); NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS. (IPR020904); SDR_fam. (IPR002347); adh_short (PF00106)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "benD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'benD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **benD** (gene ID: benD, UniProt: Q88I37) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# benD (PP_3164, UniProt Q88I37) in *Pseudomonas putida* KT2440: NAD⁺-Dependent Dihydrodiol Dehydrogenase of Benzoate Catabolism

## Summary

**benD** (locus tag **PP_3164**; UniProt **Q88I37**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes a soluble, cytoplasmic, NAD⁺-dependent **1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase** (EC 1.3.1.25), historically also called **benzoate cis-dihydrodiol (2-hydro-1,2-dihydroxybenzoate) dehydrogenase**. The enzyme catalyzes the **second committed step of the aerobic benzoate degradation pathway**: it oxidatively re-aromatizes the *cis*-1,2-dihydrodiol of benzoate — the product of the BenABC benzoate 1,2-dioxygenase — to yield **catechol**, concomitantly reducing NAD⁺ to NADH and releasing CO₂. This reaction funnels benzoate into the central catechol branch of the β-ketoadipate (ortho-cleavage) pathway, ultimately feeding succinyl-CoA and acetyl-CoA into the TCA cycle.

The gene identity was rigorously verified against all UniProt criteria: the gene symbol *benD*, the organism (*P. putida* KT2440), the EC number (1.3.1.25), and the protein family (short-chain dehydrogenases/reductases, SDR) all align consistently with the primary literature and database annotation. benD sits within the benzoate-inducible **benABCDK–catA2–benE** gene cluster (PP_3161–PP_3167), positioned **directly between the multicomponent dioxygenase that synthesizes its substrate and the catechol 1,2-dioxygenase (CatA-II) that consumes its product** — a textbook example of pathway gene co-localization that both reflects and enforces metabolic channeling. Expression of the operon is controlled by the AraC/XylS-family activator **BenR** in response to benzoate, and is subject to **Crc-mediated carbon catabolite repression**.

Structurally, benD is a 253-residue classical SDR with a Rossmann NAD-binding fold, the canonical N-terminal glycine-rich cofactor motif (TGxxxGxG), a **Ser136–Tyr148–Lys152 catalytic triad**, and an **aspartate (Asp38)** at the β2-strand position that specifies NAD(H) rather than NADP(H) cofactor usage. A high-confidence AlphaFold model (AF-Q88I37-F1, mean pLDDT 97.2) confirms the predicted active-site geometry (Tyr148–Lys152 dyad separation 4.56 Å). Together, genetic, genomic, database, and structural/bioinformatic evidence converge on a single, well-supported functional assignment.

---

## Gene / Protein Identity Verification

Before presenting findings, all mandatory identity checks were completed and **passed**:

| Verification criterion | UniProt reference | Literature / database evidence | Status |
|---|---|---|---|
| Gene symbol matches protein description | *benD* = 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase | Cowles et al. 2000 assign *benD* the dihydrodiol dehydrogenase function in the *P. putida ben* operon [PMID: 11053377] | ✅ Match |
| Organism correct | *P. putida* KT2440 | KT2440 *ben* cluster characterized in this exact strain lineage | ✅ Match |
| Protein family / domains align | SDR family; PF00106, IPR002347, IPR036291, IPR020904, IPR047686 (BenD) | Sequence exhibits canonical SDR architecture (TGxxxGxG + YxxxK) | ✅ Match |
| No conflict with a same-symbol gene in another organism | — | Homologous *nagB* (naphthalene) and other dihydrodiol dehydrogenases are distinct genes but the same enzyme class; no misassignment | ✅ Clear |

The gene symbol *benD* is **not ambiguous** for this protein. The literature, EC annotation, and domain architecture are mutually consistent, so research proceeded on the correct target.

---

## Key Findings

### Finding 1 — benD is the NAD⁺-dependent dihydrodiol dehydrogenase of benzoate catabolism (F001)

benD encodes the enzyme that performs the **second step of aerobic benzoate degradation**. UniProt Q88I37 annotates benD/PP_3164 as **1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase, EC 1.3.1.25** (GO:0047116). The catalyzed reaction is:

```
2-hydro-1,2-dihydroxybenzoate (benzoate cis-1,2-dihydrodiol) + NAD⁺
        │
        ▼  benD  (EC 1.3.1.25)
catechol + CO₂ + NADH + H⁺
```

Mechanistically, the enzyme oxidizes the C1 (or C2) hydroxyl of the non-aromatic *cis*-dihydrodiol ring. This oxidation, coupled with spontaneous decarboxylation of the carboxylate substituent, **re-aromatizes the ring** to produce catechol — the branch-point intermediate that enters ring-cleavage catabolism.

The functional assignment rests on the genetic work of **Cowles, Nichols & Harwood (2000)** [PMID: 11053377], who identified the *benABCDKFE* cluster in *P. putida* and state verbatim: *"The benABC genes likely encode benzoate dioxygenase, and benD likely encodes 2-hydro-1,2-dihydroxybenzoate dehydrogenase."* A *benR* regulator mutant was unable to grow on benzoate, confirming that the operon (including *benD*) is required for benzoate assimilation.

> **Evidence:** UniProt EC 1.3.1.25 / GO:0047116 annotation; Cowles et al. 2000 genetic operon identification (verified quote).

### Finding 2 — benD is a cytoplasmic SDR with a Rossmann fold and Ser-Tyr-Lys catalytic triad (F002)

benD is a **253-amino-acid protein** belonging to the **short-chain dehydrogenases/reductases (SDR) family** (UniProt SIMILARITY annotation). Its domain complement — Pfam **PF00106** (adh_short), InterPro **IPR002347** (SDR family), **IPR036291** (NAD(P)-binding domain superfamily), **IPR020904** (SDR conserved site), and the dedicated **IPR047686 (BenD)** signature — is fully consistent with a single-domain SDR oxidoreductase.

Sequence analysis confirms the canonical SDR architecture:
- **N-terminal cofactor-binding motif:** the glycine-rich **TGxxxGxG** Rossmann fingerprint (T13-G14-A-A-Q-G18-I-G20), which cradles the pyrophosphate of the dinucleotide cofactor.
- **Catalytic motif:** the **YxxxK** signature with **Tyr148** and **Lys152**, plus the upstream catalytic **Ser136** (within an NVSS motif), forming the classical **Ser–Tyr–Lys catalytic triad** universal to SDR enzymes.

SDR enzymes are soluble cytoplasmic proteins; benD carries no signal peptide or membrane-spanning segment, consistent with a **cytoplasmic localization**, where it acts on the soluble dihydrodiol intermediate generated by the upstream dioxygenase.

> **Evidence:** UniProt family annotation; Pfam/InterPro domain assignments; sequence-level identification of TGxxxGxG and Ser136/Tyr148/Lys152 motifs.

### Finding 3 — benD is expressed from the benzoate-inducible *ben* operon under BenR and Crc control (F003)

Transcription of *benD* is embedded in the regulation of the entire *ben* operon:

- **BenR activation:** Cowles et al. 2000 [PMID: 11053377] showed *benR* encodes an **AraC/XylS-family transcriptional activator** with high similarity to XylS (*"The deduced amino acid sequence of BenR showed high similarity (62% identity) to the sequence of XylS, a member of the AraC family of regulators."*). BenR is required for growth on benzoate and activates the *benA-lacZ* fusion in response to benzoate. Because *benD* lies within the same operon as *benA*, it is co-induced.
- **Catechol feedback:** van Duuren et al. 2011/2012 [PMID: 21906639; PMID: 21954182] demonstrated that the *ben* operon (containing *benABCD* and *catA2*/PP_3166) is highly expressed in the presence of benzoate, and that **catechol accumulation represses *ben* operon expression** — a feedback that balances flux through the pathway.
- **Carbon catabolite repression:** Moreno et al. 2009 [PMID: 19825982] showed the global regulator **Crc** binds *benR* mRNA and inhibits its translation when preferred carbon sources are available (*"Crc inhibits translation of the Pseudomonas putida alkS and benR mRNAs, which code for transcriptional regulators of genes required to assimilate alkanes (hydrocarbons) and benzoate (an aromatic compound), respectively"*). Thus benD expression is indirectly subject to hierarchical carbon-source control.

> **Evidence:** Cowles et al. 2000 (BenR = XylS homolog, verified quote); Moreno et al. 2009 (Crc represses *benR*, verified quote); van Duuren et al. 2011/2012 (catechol feedback).

### Finding 4 — A high-confidence AlphaFold model validates the predicted active-site geometry (F004)

The AlphaFold DB model **AF-Q88I37-F1** (v6, 253 aa) is of very high quality: **mean pLDDT = 97.2**, with 97% of residues at pLDDT > 90 and 100% > 70, indicating a confidently predicted single-domain fold. In the model, the predicted SDR catalytic residues cluster within a single active-site cleft with geometry matching functional SDR enzymes:

- **Tyr148(OH) – Lys152(NZ) = 4.56 Å** — the canonical SDR catalytic dyad distance.
- **Ser136(OG)** positioned ~6–7 Å away, completing the Ser–Tyr–Lys triad.
- The N-terminal **Rossmann NAD-binding motif (TGxxxGxG, T13–G20)** forms the expected dinucleotide-binding cradle.

This structural evidence independently corroborates the sequence-based active-site assignment and supports the enzyme's classification as a catalytically competent SDR dehydrogenase.

> **Evidence:** AlphaFold DB AF-Q88I37-F1; measured Tyr148–Lys152 dyad distance and triad clustering.

### Finding 5 — Asp38 specifies NAD(H) over NADP(H) cofactor usage (F005)

Cofactor specificity in SDR enzymes is governed by residues at the C-terminal end of the β2 strand (~15–20 residues downstream of the TGxxxGxG motif). **NAD(H)-specific SDRs carry an aspartate** there that hydrogen-bonds the 2′- and 3′-OH groups of the adenosine ribose; NADP(H)-preferring SDRs lack this aspartate and instead present basic residues (Arg/Lys) to accommodate the 2′-phosphate.

benD (Q88I37) possesses **Asp38** at exactly this position (motif …QVVAV-**D38**-RSE…), roughly 18 residues after the glycine motif (TGAAQGIG, ending at G20). This bioinformatic signature **predicts NAD⁺-dependent catalysis**, in full agreement with the annotated EC 1.3.1.25 reaction:

```
2-hydro-1,2-dihydroxybenzoate + NAD⁺ → catechol + CO₂ + NADH
```

The NAD⁺ dependence is biologically sensible: benD operates in a **catabolic** (oxidative, energy-harvesting) direction, generating NADH for the respiratory chain, whereas NADPH-linked SDRs typically serve biosynthetic reductive roles.

> **Evidence:** SDR cofactor-specificity rule; identification of Asp38 at the β2-strand determinant position.

### Finding 6 — benD is genomically embedded between the enzyme making its substrate and the enzyme consuming its product (F006)

The KT2440 locus around PP_3164 forms a contiguous, functionally ordered cluster:

| Locus | Gene | Protein / EC | UniProt | Role relative to benD |
|---|---|---|---|---|
| PP_3161 | *benA* | Benzoate 1,2-dioxygenase α subunit (EC 1.14.12.10) | Q88I40 | Makes benD's substrate |
| PP_3162 | *benB* | Dioxygenase β subunit | Q88I39 | Makes benD's substrate |
| PP_3163 | *benC* | Dioxygenase reductase/electron-transfer (EC 1.14.12.10 / 1.18.1.3) | Q88I38 | Makes benD's substrate |
| **PP_3164** | **benD** | **Dihydrodiol dehydrogenase (EC 1.3.1.25)** | **Q88I37** | **This protein** |
| PP_3165 | *benK* | Benzoate MFS transporter | Q88I36 | Imports pathway substrate |
| PP_3166 | *catA-II* | Catechol 1,2-dioxygenase (EC 1.13.11.1) | Q88I35 | Consumes benD's product |
| PP_3167 | *benE-II* | Benzoate transporter | Q88I34 | Imports pathway substrate |

benD sits **immediately downstream of *benABC*** (the three-component dioxygenase that synthesizes its *cis*-dihydrodiol substrate) and **immediately upstream of *catA-II*** (the catechol 1,2-dioxygenase that consumes its catechol product). This synteny provides strong contextual confirmation of benD's role as the intermediate-processing step, and it physically co-localizes the enzymes of a metabolic relay.

> **Evidence:** UniProt/KEGG annotation of the contiguous PP_3161–3167 locus.

---

## Mechanistic Model / Interpretation

benD is the **second enzyme of the "benzoate → catechol" upper funnel** that channels benzoate into the ortho-cleavage (β-ketoadipate) pathway. The full local pathway is:

```
                 O2 + NADH                    NAD+      NADH + CO2
                     │                          │           │
   Benzoate ─────────▼──────────► benzoate ─────▼───────────▼──► Catechol
        │      BenABC (PP_3161-63)  cis-1,2-      benD                │
   (imported by     benzoate        dihydrodiol  (PP_3164,            │
    BenK/BenE)      1,2-dioxygenase  (2-hydro-    EC 1.3.1.25)        │
                    EC 1.14.12.10    1,2-DHB)     SDR, NAD+           ▼
                                                             CatA-II (PP_3166)
                                                             catechol 1,2-dioxygenase
                                                             EC 1.13.11.1
                                                                      │
                                                                      ▼
                                                          cis,cis-muconate
                                                                      │
                                                                      ▼
                                                          β-ketoadipate pathway
                                                                      │
                                                                      ▼
                                                     succinyl-CoA + acetyl-CoA → TCA
```

**Reaction chemistry.** The BenABC dioxygenase first performs a dihydroxylation that dearomatizes the ring and produces the unstable non-aromatic *cis*-1,2-dihydrodiol (still bearing the carboxylate). benD then oxidizes a ring hydroxyl using NAD⁺; the resulting instability drives **spontaneous decarboxylation**, re-aromatizing the ring and yielding catechol. This "dioxygenase + dihydrodiol dehydrogenase" two-step motif is a **conserved paradigm across aromatic catabolism** — the same architecture is seen for naphthalene (NahB/NagB *cis*-dihydrodiol dehydrogenase), phenylacetate, and chlorotoluene degradation (see Evidence Base). benD is the benzoate-specific member of this enzyme class.

**Localization.** As a soluble cytoplasmic SDR with no signal peptide or transmembrane region, benD carries out its reaction in the **cytoplasm**, acting on the soluble dihydrodiol generated by the upstream (also cytoplasmic) dioxygenase. Benzoate itself is imported by the MFS/permease transporters BenK and BenE encoded in the same cluster.

**Regulation and flux control.** benD expression is gated at three levels: (1) **substrate induction** via BenR (AraC/XylS activator) responding to benzoate; (2) **product/intermediate feedback**, where catechol accumulation dampens *ben* operon expression, preventing toxic catechol buildup; and (3) **carbon catabolite repression** via Crc, which suppresses *benR* translation when preferred carbon sources are present. The neighboring **CatA-II** acts as a "safety valve" for excess catechol (per the *P. putida* mt-2 studies), underscoring how tightly the pathway around benD's product is managed.

**Cofactor logic.** The Asp38 determinant fixes benD as **NAD⁺-dependent**, consistent with its catabolic direction: the NADH produced is a respiratory electron donor, coupling aromatic degradation to energy conservation. This is the expected cofactor choice for an oxidative catabolic dehydrogenase, in contrast to NADPH-using reductive/biosynthetic SDRs.

---

## Evidence Base

| PMID | Study focus | How it supports the benD assignment |
|---|---|---|
| [PMID: 11053377](https://pubmed.ncbi.nlm.nih.gov/11053377/) | BenR/XylS regulation of aromatic acid degradation in *P. putida* | **Primary genetic evidence.** Identifies the *benABCDKFE* cluster; states *benD* "likely encodes 2-hydro-1,2-dihydroxybenzoate dehydrogenase"; BenR = 62% identical to XylS; *benR* mutant cannot grow on benzoate. |
| [PMID: 19825982](https://pubmed.ncbi.nlm.nih.gov/19825982/) | Crc global regulator binding *alkS*/*benR* mRNA | Establishes that benD's activator (BenR) is under Crc catabolite-repression control at the translational level. |
| [PMID: 21906639](https://pubmed.ncbi.nlm.nih.gov/21906639/) | *catR*-deficient KT2440 mutant producing muconate | Confirms *ben* operon (incl. *benABCD* and *catA2*/PP_3166) is highly benzoate-induced; places *catA2* immediately downstream. |
| [PMID: 21954182](https://pubmed.ncbi.nlm.nih.gov/21954182/) | pH-stat production of *cis,cis*-muconate from benzoate | Shows catechol accumulation represses the *ben* operon (feedback regulation of the benD-containing operon). |
| [PMID: 24341396](https://pubmed.ncbi.nlm.nih.gov/24341396/) | CatA2 as a catechol "safety valve" in *P. putida* mt-2 | Characterizes the downstream partner (CatA-II) that consumes benD's product catechol; confirms operon topology. |
| [PMID: 26373670](https://pubmed.ncbi.nlm.nih.gov/26373670/) | Transcriptomics of aromatic catabolism, *P. putida* mt-2 | Confirms the chromosomal *ben*/*cat* ortho route is activated by benzoate (not by TOL substrates), consistent with benD's benzoate-specific induction. |
| [PMID: 20632934](https://pubmed.ncbi.nlm.nih.gov/20632934/) | Naphthalene metabolism enzymes, *P. fluorescens* | Demonstrates the analogous **NAD⁺-dependent *cis*-dihydrodiol dehydrogenase** reaction in a parallel pathway, supporting the enzyme class assignment. |
| [PMID: 9573207](https://pubmed.ncbi.nlm.nih.gov/9573207/) | *nag* cluster (naphthalene → gentisate) | *nagB* = *cis*-dihydrodiol dehydrogenase; homologous enzyme/gene-order paradigm for dioxygenase + dihydrodiol dehydrogenase. |
| [PMID: 2719478](https://pubmed.ncbi.nlm.nih.gov/2719478/) | p-chlorotoluene degradation, *Pseudomonas* sp. JS6 | Illustrates the conserved "dioxygenase + dihydrodiol dehydrogenase → catechol → ortho cleavage" route benD belongs to. |
| [PMID: 7346381](https://pubmed.ncbi.nlm.nih.gov/7346381/) | Aromatic carboxylic acid degradation, chloridazon bacteria | Documents dihydrodiol dehydrogenase converting *cis*-dihydrodiols to catechols, the reaction class of benD. |

**Convergence of evidence.** The functional assignment is supported by four independent lines: (1) **direct genetic annotation** in the correct strain (Cowles et al. 2000), (2) **database/EC annotation** (UniProt EC 1.3.1.25, GO:0047116, KEGG), (3) **verified genomic synteny** placing benD between substrate-producing and product-consuming enzymes, and (4) **structural/sequence bioinformatics** (SDR fold, Ser–Tyr–Lys triad, NAD-specifying Asp38, high-confidence AlphaFold model). No line of evidence conflicts.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the KT2440 benD protein.** The functional assignment is based on genetic operon analysis, homology, and structural inference — there is **no published purification, kinetic characterization (kcat, Km), or in vitro assay** of the specific Q88I37 gene product. Cowles et al. use "likely encodes" language, reflecting inference rather than direct enzymatic proof for this exact protein.

2. **Cofactor preference is predicted, not measured.** The NAD⁺ specificity rests on the Asp38 bioinformatic determinant and analogy to related dihydrodiol dehydrogenases; it has not been experimentally confirmed for benD itself (e.g., by comparing activity with NAD⁺ vs NADP⁺).

3. **No experimental structure.** All structural conclusions derive from the AlphaFold model and sequence motifs. While the model is high-confidence (pLDDT 97.2), no crystal or cryo-EM structure — and no substrate/cofactor-bound complex — exists to confirm active-site details or substrate binding mode.

4. **Substrate specificity breadth unknown.** Whether benD acts exclusively on the benzoate *cis*-dihydrodiol or also on substituted (e.g., methyl-/chloro-) dihydrodiol analogs has not been tested for this protein, though the broader enzyme class is known to accept substituted substrates.

5. **Quaternary structure not established.** Many dihydrodiol dehydrogenases are homotetramers or homohexamers (e.g., the naphthalene enzyme is a homohexamer, PMID: 20632934). benD's oligomeric state has not been experimentally determined.

6. **Reaction stoichiometry / decarboxylation mechanism.** Whether CO₂ release is enzyme-catalyzed or spontaneous downstream of oxidation for benD specifically has not been directly demonstrated.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_3164, express and purify the His-tagged protein, and directly assay dihydrodiol dehydrogenase activity using benzoate *cis*-1,2-dihydrodiol (generated in situ by BenABC) as substrate, monitoring NADH formation spectrophotometrically (340 nm). Determine kcat, Km for substrate and cofactor.

2. **Cofactor-specificity test.** Compare initial-rate activity with NAD⁺ versus NADP⁺ to experimentally confirm the Asp38-predicted NAD⁺ preference; complement with an Asp38→Arg mutant to test whether specificity can be switched to NADP⁺.

3. **Active-site mutagenesis.** Generate Ser136Ala, Tyr148Phe, and Lys152Met single mutants to verify the catalytic triad; measure residual activity to confirm the SDR mechanism.

4. **Gene knockout / complementation.** Construct a clean ΔbenD deletion in KT2440 and confirm loss of growth on benzoate (with accumulation of the *cis*-dihydrodiol intermediate detectable by LC-MS), then restore growth by complementation to establish essentiality and specificity.

5. **Product identification.** Use LC-MS/NMR to confirm catechol (and CO₂) as reaction products and to clarify whether decarboxylation is enzyme-catalyzed or spontaneous.

6. **Structural determination.** Pursue X-ray crystallography or cryo-EM of benD, ideally with NAD⁺ and a substrate analog bound, to validate the AlphaFold model and define substrate-binding determinants; also determine oligomeric state by size-exclusion chromatography / analytical ultracentrifugation.

7. **Substrate-range profiling.** Test activity against substituted benzoate *cis*-dihydrodiols (methyl-, chloro-, fluoro-) to define substrate specificity, informing biocatalytic/muconate-production applications.


## Artifacts

- [OpenScientist final report](benD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](benD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11053377
2. PMID:21906639
3. PMID:21954182
4. PMID:19825982
5. PMID:24341396
6. PMID:26373670
7. PMID:20632934
8. PMID:9573207
9. PMID:2719478
10. PMID:7346381