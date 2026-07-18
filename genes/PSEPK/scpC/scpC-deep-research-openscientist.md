---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:23:54.437427'
end_time: '2026-07-11T17:37:13.782368'
duration_seconds: 799.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: scpC
  gene_symbol: scpC
  uniprot_accession: Q88RH5
  protein_description: 'SubName: Full=Propionyl-CoA:succinate CoA transferase {ECO:0000313|EMBL:AAN65788.1};
    EC=2.8.3.- {ECO:0000313|EMBL:AAN65788.1};'
  gene_info: Name=scpC {ECO:0000313|EMBL:AAN65788.1}; OrderedLocusNames=PP_0154 {ECO:0000313|EMBL:AAN65788.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the acetyl-CoA hydrolase/transferase family.
  protein_domains: AcetylCoA_hyd_C. (IPR026888); AcetylCoA_hyd_C_sf. (IPR038460);
    ActCoA_hydro. (IPR046433); ActCoA_hydro_N. (IPR003702); NagB/RpiA_transferase-like.
    (IPR037171)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: scpC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: scpC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RH5
- **Protein Description:** SubName: Full=Propionyl-CoA:succinate CoA transferase {ECO:0000313|EMBL:AAN65788.1}; EC=2.8.3.- {ECO:0000313|EMBL:AAN65788.1};
- **Gene Information:** Name=scpC {ECO:0000313|EMBL:AAN65788.1}; OrderedLocusNames=PP_0154 {ECO:0000313|EMBL:AAN65788.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the acetyl-CoA hydrolase/transferase family.
- **Key Domains:** AcetylCoA_hyd_C. (IPR026888); AcetylCoA_hyd_C_sf. (IPR038460); ActCoA_hydro. (IPR046433); ActCoA_hydro_N. (IPR003702); NagB/RpiA_transferase-like. (IPR037171)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "scpC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'scpC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **scpC** (gene ID: scpC, UniProt: Q88RH5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: scpC / PP_0154 (UniProt Q88RH5)
### *Pseudomonas putida* KT2440 (PSEPK)

## 1. Summary (Answer to the Research Question)

**scpC (PP_0154, Q88RH5) encodes a soluble, cytoplasmic class‑I coenzyme‑A transferase of the acetyl‑CoA hydrolase/transferase family (Pfam PF02550 + PF13336; EC 2.8.3.‑).** It catalyzes the reversible transfer of coenzyme A between a short‑chain acyl‑CoA thioester and a free carboxylic acid (a transthioesterification), proceeding through a covalent glutamyl‑CoA / acyl‑glutamyl‑anhydride intermediate on the active‑site glutamate (Glu288). Its physiological substrate pair in *P. putida* has **not been measured directly**; the two authoritative computational annotations disagree: the EMBL/UniProt gene name "propionyl‑CoA:succinate CoA transferase" is a homology transfer from *E. coli* YgfH/ScpC, whereas KEGG assigns it to orthology **K18118, succinyl‑CoA:acetate CoA‑transferase (EC 2.8.3.18, AarC‑type)** in the TCA cycle. Both describe the same chemistry on cytoplasmic C2–C4 acyl‑CoA/organic‑acid pools feeding central carbon metabolism.

> **Identity verification (mandatory):** The gene symbol *scpC* is ambiguous. This report concerns the *Pseudomonas putida* KT2440 **CoA‑transferase** Q88RH5 (PP_0154). It is **not** the unrelated streptococcal *scpC* (a cell‑envelope C5a peptidase/protease). The CoA‑transferase identity is confirmed by the acetyl‑CoA hydrolase/transferase domain architecture, the EC 2.8.3.‑ class, and orthology to *E. coli* ScpC/YgfH — all consistent with the UniProt record.

---

## 2. Molecular Identity and Structure

| Property | Value |
|---|---|
| UniProt | Q88RH5 |
| Gene / locus | *scpC* / PP_0154 |
| Organism | *Pseudomonas putida* KT2440 |
| Length / mass | 497 aa / 53.96 kDa |
| Family | Acetyl‑CoA hydrolase/transferase (class‑I CoA‑transferase) |
| Domains | PF02550 AcetylCoA_hydro (N, aa 11–215); PF13336 AcetylCoA_hyd_C (C, aa 322–463); SUPFAM SSF100950 (NagB/RpiA/CoA‑transferase‑like) |
| InterPro | IPR003702, IPR026888, IPR046433, IPR037171, IPR017821 (Succinate_CoA_transferase) |
| Orthology | eggNOG COG0427; KEGG K18118 |
| Catalytic residue | **Glu288** — "5‑glutamyl coenzyme A thioester intermediate" (UniProt); binding residues 378/382/402 |
| Localization | Cytoplasm (no signal peptide, no transmembrane segment) |

The two‑domain αβ architecture and the catalytic glutamate place scpC firmly in **class‑I CoA‑transferases**, which "catalyze transthioesterification reactions involving acyl‑CoA substrates, using an active‑site carboxylate to form covalent acyl anhydride and CoA thioester adducts" (Mullins & Kappock, 2012, PMID 23030530). This mechanism is directly supported by UniProt's annotation of Glu288 as the glutamyl‑CoA intermediate for Q88RH5.

---

## 3. Primary Function: The Catalyzed Reaction

scpC catalyzes a reversible, ping‑pong CoA transfer:

```
R1‑CO‑SCoA  +  R2‑COO⁻   ⇌   R1‑COO⁻  +  R2‑CO‑SCoA
```

**Substrate specificity — two candidate assignments (unresolved for the P. putida enzyme):**

1. **Propionyl‑CoA:succinate CoA‑transferase** (EMBL/UniProt name; EC 2.8.3.‑). Based on the *E. coli* homolog: "YgfH is propionyl CoA:succinate CoA transferase" (Haller et al., 2000, PMID 10769117). In *E. coli* this enzyme is the third step of the Sbm cycle converting succinate → propionate.
2. **Succinyl‑CoA:acetate CoA‑transferase** (KEGG K18118; EC 2.8.3.18). The best biochemically/structurally characterized member of this orthology group is *Acetobacter aceti* AarC: "AarC is succinyl‑coenzyme A (CoA):acetate CoA‑transferase, which replaces succinyl‑CoA synthetase in a variant CAC" (Mullins et al., 2008, PMID 18502856).

Both activities are short‑chain (C2–C4) acyl‑CoA:carboxylate CoA‑transfers by the same class‑I mechanism; they differ only in the preferred acyl donor/acceptor pair. **No enzyme‑kinetic study of the P. putida protein exists**, so its exact preference is inferred, not measured.

**Sequence evidence (this work).** Needleman–Wunsch pairwise alignment of Q88RH5 against characterized family members gives ~equal identity to the two succinate‑linked transferases and low identity to a pure acetate transferase:

| Homolog | Activity | % identity to scpC |
|---|---|---|
| *E. coli* YgfH/ScpC | propionyl‑CoA:succinate CoA‑transferase | 48.3% (234/484) |
| *A. aceti* AarC | succinyl‑CoA:acetate CoA‑transferase (EC 2.8.3.18) | 50.9% (251/493) |
| *E. coli* YdiF | acetate CoA‑transferase | 27.0% (129/477) |

Because both nearest homologs share **succinate/succinyl‑CoA** as one substrate, that partner is the most confidently assignable substrate for scpC. Identity is only marginally higher for AarC (+2.6%), so sequence cannot discriminate whether the second partner is propionyl‑CoA (YgfH‑like) or acetate (AarC‑like); the slight AarC lean is consistent with the KEGG K18118 assignment.

**Active‑site integrity (this work).** Residue mapping shows scpC's catalytic **Glu288** and CoA‑binding residues **Asn378 / Gly382 / Lys402** are identical in both YgfH and AarC, confirming a complete, catalytically competent class‑I active site (an active enzyme, not a pseudoenzyme). These positions lie on the conserved CoA/catalytic side and therefore do not discriminate acceptor specificity. Homolog identities were independently verified from UniProt (P52043 = *E. coli* ScpC "Propanoyl‑CoA:succinate CoA transferase"; A0AB33ICN5 = *A. aceti* AarC "Succinyl‑CoA:acetate CoA‑transferase"; P37766 = *E. coli* YdiF "Acetate CoA‑transferase").

---

## 4. Pathway Context and Localization

- **Localization:** cytoplasmic, soluble. The AarC‑type CoA‑transferase acts on the cytosolic organic‑acid/acyl‑CoA pool — the *A. aceti aar* genes "support flux through a complete but unorthodox CAC that is needed to lower cytoplasmic acetate levels" (PMID 18502856).
- **Pathway (KEGG):** PP_0154 is mapped to the **citrate cycle (ppu00020)** and **pyruvate metabolism (ppu00620)**, consistent with a succinyl‑CoA↔acetate transferase that can bypass succinyl‑CoA synthetase.
- **Genomic context distinguishes it from *E. coli*:** PP_0154 is a **standalone gene**. Its neighbors (PP_0153 hypothetical; PP_0152 exported protein; PP_0155/PP_0156 pyridine‑nucleotide transhydrogenase) are unrelated to CoA/propionate metabolism. This contrasts with *E. coli*, where the homolog lies in a four‑gene operon "that encodes homologues of methylmalonyl CoA mutases (Sbm) and acyl CoA transferases (YgfH)" (PMID 10769117).
- **Plausible physiological niche (hypothesis).** No primary study characterizes PP_0154 in *P. putida*; its function is annotated by homology only. *P. putida* KT2440 assimilates acetate via acetyl‑CoA and the glyoxylate shunt, and acetate‑grown cells appear to use "ATP independent acetyl‑CoA recycling as energy saving strategy" (Grether et al., 2026, PMID 42393666). An AarC‑type succinyl‑CoA:acetate CoA‑transferase (the KEGG K18118 activity) would provide exactly this ATP‑independent activation of acetate to acetyl‑CoA, consistent with PP_0154's KEGG mapping to the TCA cycle. This link is a reasonable but **untested** hypothesis.
- **The Sbm route is absent in *P. putida*:** KEGG shows *P. putida* KT2440 encodes **no methylmalonyl‑CoA mutase** (K01847) and no MCM subunit (K11942). Since propionate oxidation in *Pseudomonas* runs through the 2‑methylcitrate cycle — "the only known and described pathway for propionate oxidation in this organism" (Santos‑Oliveira et al., 2024, PMID 37995793) — scpC cannot be part of an *E. coli*‑style succinate→propionate cycle here. This argues that the "propionyl‑CoA:succinate" name is a **homology over‑transfer**, and that the KEGG succinyl‑CoA:acetate CoA‑transferase (TCA‑linked) role is the more parsimonious annotation.

---

## 5. Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| scpC is a class‑I CoA‑transferase (acetyl‑CoA hydrolase/transferase family) using a Glu covalent intermediate | **Supported** | Domain architecture, Glu288 active site, PMID 23030530 |
| scpC catalyzes reversible short‑chain acyl‑CoA:carboxylate CoA transfer | **Supported** | EC 2.8.3.‑ class; homologs YgfH & AarC |
| scpC operates as part of an *E. coli*‑style methylmalonyl‑CoA (Sbm) succinate→propionate cycle in *P. putida* | **Refuted** | No methylmalonyl‑CoA mutase/decarboxylase in KT2440; gene not in an sbm operon |
| Exact substrate pair (propionyl‑CoA/succinate vs succinyl‑CoA/acetate) is established for the *P. putida* enzyme | **Unresolved** | Conflicting database annotations; no direct kinetics |
| scpC is cytoplasmic | **Supported (inferred)** | No signal peptide/TM; analogy to soluble CAC enzymes |

---

## 6. Limitations and Future Directions

- **No primary biochemistry exists for Q88RH5 itself.** Function is inferred from sequence/family, orthology (KEGG K18118, COG0427), and characterized homologs (*E. coli* YgfH, *A. aceti* AarC). High‑throughput/database annotations disagree on the exact acyl specificity.
- **Recommended experiments:** (i) purify recombinant PP_0154 and assay CoA‑transfer with acetyl‑/propionyl‑/succinyl‑CoA donors against acetate/succinate/propionate acceptors to define kᶜᵃᵗ/Kₘ; (ii) Glu288Ala mutant to confirm the catalytic nucleophile; (iii) ΔPP_0154 phenotyping on acetate/propionate/succinate to place it physiologically; (iv) structure determination (or AlphaFold + docking) to map the auxiliary carboxylate‑recognition site described for AarC.

---

## References
- Haller T, Buckel T, Rétey J, Gerlt JA. *Biochemistry* 2000;39:4622‑4629. **PMID 10769117.**
- Mullins EA, Francois JA, Kappock TJ. *J Bacteriol* 2008. **PMID 18502856.**
- Mullins EA, Kappock TJ. *Biochemistry* 2012. **PMID 23030530.**
- Froese DS et al. *Biochimie/…* 2009. **PMID 18950999.**
- Santos‑Oliveira et al. 2024. **PMID 37995793.**
- Grether et al. *Acetate as alternative carbon source … Pseudomonas putida KT2440.* 2026. **PMID 42393666.**
- Database records: UniProt Q88RH5; KEGG ppu:PP_0154 (K18118, EC 2.8.3.18); InterPro/Pfam domains as listed.

---

## Bottom Line

scpC/PP_0154 is a **soluble cytoplasmic, catalytically competent class‑I CoA‑transferase** (acetyl‑CoA hydrolase/transferase family, EC 2.8.3.‑) that performs reversible CoA transfer between a short‑chain acyl‑CoA thioester and a free carboxylic acid via a Glu288 glutamyl‑CoA intermediate, feeding central carbon metabolism (TCA cycle). Succinate/succinyl‑CoA is the most confidently assigned substrate partner; the identity of the second partner (propionyl‑CoA vs acetate) is unresolved, with sequence, orthology (KEGG K18118), genomic context, and the absence of the Sbm pathway in *P. putida* collectively favouring a **succinyl‑CoA:acetate CoA‑transferase (AarC‑type, EC 2.8.3.18)** role over the literal "propionyl‑CoA:succinate" name. No gene‑specific experimental data exist for the *P. putida* protein, so all functional statements are inferences from family, structure/sequence, and orthology.


## Artifacts

- [OpenScientist final report](scpC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](scpC-deep-research-openscientist_artifacts/final_report.pdf)