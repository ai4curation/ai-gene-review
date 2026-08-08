---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:55:36.803670'
end_time: '2026-07-18T14:11:55.356596'
duration_seconds: 978.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0922
  gene_symbol: PP_0922
  uniprot_accession: Q88PC8
  protein_description: 'RecName: Full=ACP phosphodiesterase {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_0922 {ECO:0000313|EMBL:AAN66547.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ACP_PD. (IPR007431); ACP_PD (PF04336)
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
  path: PP_0922-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0922-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PC8
- **Protein Description:** RecName: Full=ACP phosphodiesterase {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_0922 {ECO:0000313|EMBL:AAN66547.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACP_PD. (IPR007431); ACP_PD (PF04336)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0922" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0922' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0922** (gene ID: PP_0922, UniProt: Q88PC8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0922 (AcpH) — Acyl Carrier Protein Phosphodiesterase of *Pseudomonas putida* KT2440

**UniProt:** Q88PC8 | **Gene / Ordered Locus:** PP_0922 | **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), taxid 160488
**EC:** 3.1.4.14 | **KEGG Orthology:** K08682 | **Pfam:** PF04336 (ACP_PD) | **InterPro:** IPR007431 | **eggNOG:** COG3124

---

## 1. Summary (Answer to the Research Question)

PP_0922 encodes **AcpH, an acyl carrier protein (ACP) phosphodiesterase** (also historically called "ACP hydrolyase"; EC 3.1.4.14). Its primary catalytic function is to **hydrolyze the phosphodiester bond that links the 4′-phosphopantetheine (4′-PP) prosthetic group to the active-site serine of acyl carrier protein**, thereby converting functional **holo-ACP (or acyl-ACP) back into inactive apo-ACP** and releasing 4′-phosphopantetheine. This is the reverse of the reaction carried out by holo-ACP synthase (AcpS). AcpH is a **soluble, cytoplasmic, Mn²⁺-dependent metalloenzyme** and a non-canonical member of the HD phosphohydrolase superfamily. Biologically, it operates in the **prosthetic-group turnover / coenzyme A (CoA)–pantetheine recycling cycle** rather than in a biosynthetic step; it is dispensable for growth but required for in vivo turnover of the ACP prosthetic group. The characterized *Pseudomonas* enzyme prefers ACPs of the fatty-acid-synthesis (FAS) pathway but can also process acylated and polyketide-synthase (PKS) carrier proteins.

The gene symbol is **not ambiguous**: domain (PF04336/ACP_PD), orthology (COG3124, KO K08682), GO term (GO:0008770), KEGG EC assignment, and a full-length 39% sequence identity to the biochemically characterized *E. coli* AcpH all converge on the same function.

---

## 2. Identity Verification

Multiple independent lines of evidence confirm PP_0922 is a genuine AcpH:

| Evidence type | Finding |
|---|---|
| Protein family | Single **ACP_PD** domain (Pfam **PF04336**; InterPro **IPR007431**) spanning the 194-aa protein |
| Orthology | **COG3124**; OrthoDB 8442777at2; KEGG KO **K08682** |
| Enzyme classification | **EC 3.1.4.14**, "[acyl-carrier-protein] phosphodiesterase" (KEGG, GO:0008770) |
| Sequence homology | **39.3% identity** (75/191 aligned positions) to experimentally characterized *E. coli* AcpH (P21515), colinear over the full length with no large indels |
| Active-site motifs | Conserved N-terminal **LAHLHL** block and internal **LDV..DH** metallo-motif that carry the essential metal-binding residues |

The organism is correctly *P. putida* KT2440 (KEGG ppu:PP_0922; gene coordinates 1,064,359–1,064,943, + strand). A proteome-wide scan shows **Q88PC8/PP_0922 is the single ACP_PD (PF04336) protein in the KT2440 genome** — AcpH is **single-copy**, so this gene is solely responsible for ACP-phosphodiesterase activity. The conserved His/Asp metal-binding constellation (His6, His8 in the LAHLHL motif; Asp78/Asp82/His83 in the LDV..FFDH motif, plus Asp49/Asp53/His55/His88/Asp94) reproduces the HD-superfamily active-site pattern whose ligands are essential in *E. coli* AcpH.

> Caveat on nomenclature: UniProt's "RecName: ACP phosphodiesterase" carries a low-confidence automatic annotation source (ProtNLM/Google) and KEGG's GenBank name is "conserved protein of unknown function." However, the curated KO/EC assignments, domain architecture, orthology, and sequence conservation with a biochemically defined enzyme make the AcpH assignment robust.

---

## 3. Primary Function — The Catalyzed Reaction

**Reaction (EC 3.1.4.14):**

> holo-[acyl-carrier-protein] + H₂O → apo-[acyl-carrier-protein] + 4′-phosphopantetheine

AcpH is described as "the only enzyme known to remove the 4′-phosphopantetheinyl moiety from holo acyl carrier proteins (ACP)" [PMID 20064615]. It cleaves the **phosphodiester link between 4′-phosphopantetheine and the serine-36 side chain of ACP** and is "the only enzyme known to cleave a phosphodiester-linked post-translational protein modification" [PMID 17198382]. The 4′-PP prosthetic group is the moiety onto which acyl/malonyl intermediates are loaded during fatty-acid synthesis; by removing it, AcpH inactivates ACP (apo-ACP is functionally inactive) and liberates phosphopantetheine.

**Substrate specificity:**
- The purified *E. coli* enzyme cleaves **acyl-ACP species with acyl chains of 6–16 carbons** and is active on some, but not all, non-native ACPs [PMID 16107329] — i.e., it accepts both unacylated holo-ACP and medium/long-chain acyl-ACP.
- The closely related, well-behaved ortholog ***P. aeruginosa* AcpH (PaAcpH)** — the best functional proxy for PP_0922 — shows **preferred specificity toward FAS-pathway ACPs** among eight carrier proteins tested, and it also **hydrolyzes/releases 4′-phosphopantetheinyl-linked products from a multidomain polyketide synthase**, demonstrating activity on acylated and PKS carrier-protein substrates [PMID 20064615].
- AcpH readily removes even a **modified (pantothenamide, N5-Pan) prosthetic group**, indicating tolerance for altered pantetheine moieties [PMID 20047918].

**By inference for PP_0922:** the physiological substrate in *P. putida* is most likely the primary FAS acyl carrier protein (AcpP, holo/acyl form), with capacity to edit/regenerate other carrier proteins.

---

## 4. Catalytic Mechanism, Structure & Fold

- **Metal dependence:** AcpH **requires Mn²⁺ for activity** [PMID 17198382].
- **Fold / superfamily:** Bioinformatic modeling placed AcpH on the structure of the **SpoT hydrolase (HD) domain**, identifying it as a **non-canonical member of the HD phosphatase/phosphodiesterase superfamily** — non-canonical because it **lacks the histidine characteristic of the canonical HD motif** [PMID 17198382].
- **Active-site validation:** Putative metal-binding ligands were tested by **site-directed mutagenesis; removal of any of them caused severe or total loss of phosphodiesterase activity** [PMID 17198382]. In this report's alignment, the corresponding His/Asp-bearing motifs (**LAHLHL**, **LDV..DH**) are conserved in PP_0922, supporting a shared Mn²⁺-dependent active site.
- **Solubility:** AcpH is a soluble protein that "very readily aggregates upon overexpression in vivo or concentration in vitro" [PMID 16107329]; the *Pseudomonas* orthologs are notably **more soluble and stable** than *E. coli* AcpH, which is why PaAcpH became the tractable model [PMID 20064615].

---

## 5. Localization

AcpH is a **soluble, cytoplasmic enzyme** — it was "purified to homogeneity … and is a soluble protein" [PMID 16107329]. It has no signal peptide or transmembrane segment (single cytoplasmic ACP_PD domain). It therefore acts in the **cytosol**, the same compartment where ACP, AcpS, the FAS-II enzymes, and CoA/pantetheine metabolism operate.

---

## 6. Biological Process & Pathway Context

**The 4′-phosphopantetheine prosthetic-group cycle.** ACP is functional only when its conserved serine bears a 4′-PP arm, installed from CoA by **holo-ACP synthase (AcpS / a phosphopantetheinyl transferase)** [PMID 35337986; PMID 11032795]. AcpH catalyzes the **opposing reaction**, removing 4′-PP to regenerate apo-ACP. Together AcpS and AcpH constitute a **prosthetic-group attachment/removal cycle**:

```
apo-ACP  --(AcpS, from CoA)-->  holo-ACP / acyl-ACP  --(AcpH, +H2O)-->  apo-ACP + 4'-phosphopantetheine
```

**Link to CoA metabolism.** Classic pulse-chase work showed the ACP 4′-PP prosthetic group **turns over metabolically**, at a rate that **depends on intracellular CoA concentration**, leading to the conclusion that "the acyl carrier protein prosthetic group turnover cycle may be related to coenzyme A metabolism rather than to lipid biosynthesis" [PMID 6363417]. Consistently, KEGG maps PP_0922 to **"Pantothenate and CoA biosynthesis" (ppu00770)** within *metabolism of cofactors and vitamins*. Thus AcpH's role is best understood as **cofactor recycling / homeostasis** — returning phosphopantetheine to the CoA/pantetheine pool — and quality-control "editing" of carrier proteins, rather than a step in fatty-acid biosynthesis per se.

**Non-essentiality.** A total *acpH* deletion in *E. coli* grows normally, showing the activity is **not essential for growth**, "although it is required for turnover of the ACP prosthetic group in vivo" [PMID 16107329]. Apo-ACP does not normally accumulate in cells (rapidly reconverted to holo-ACP), and no apo-ACP intermediate is detected under normal or CoA-depleted conditions [PMID 6317688], underscoring that AcpH sets the balance of a dynamic cycle rather than performing an obligatory metabolic transformation.

**Genomic context in KT2440.** PP_0922 is transcribed **divergently** from its neighbors (PP_0920 xenobiotic reductase, PP_0921 ArsR-family regulator, PP_0923/PP_0924 ornithine-lipid acyltransferases), which all lie on the opposite strand. It is therefore **not embedded in a FAS or CoA operon**, consistent with independent regulation and a homeostatic role. (Interestingly, the adjacent ornithine-lipid acyltransferases are themselves acyl-ACP–consuming enzymes, but the opposite-strand arrangement indicates coincidental proximity rather than co-transcription.)

---

## 7. Supported and Refuted Hypotheses

**Supported:**
1. PP_0922 is a genuine AcpH / ACP phosphodiesterase (EC 3.1.4.14) — supported by domain, orthology, EC/KO, GO, and 39% identity to characterized *E. coli* AcpH.
2. It catalyzes hydrolytic removal of 4′-phosphopantetheine from holo-/acyl-ACP, producing apo-ACP — supported by transitive biochemical evidence from *E. coli* and *P. aeruginosa* orthologs.
3. It is a soluble, cytoplasmic, Mn²⁺-dependent HD-superfamily metallohydrolase — supported by biochemistry, modeling, and conserved catalytic motifs.
4. Its physiological role is prosthetic-group turnover linked to CoA/pantetheine metabolism, non-essential for growth.

**Refuted / down-weighted:**
- Not an essential fatty-acid-biosynthesis enzyme (deletion is viable).
- Not membrane-associated or secreted (no signal/TM; purified as soluble).
- The gene is **not** part of a fatty-acid or CoA operon in KT2440.

---

## 8. Limitations & Future Directions

- **Direct biochemical data are lacking for the *P. putida* protein itself**; functional claims are transitive inferences from *E. coli* (P21515) and *P. aeruginosa* AcpH, justified by strong sequence/active-site conservation.
- **No experimental 3-D structure** of AcpH is available (fold assignment rests on modeling onto SpoT/HD).
- The exact in vivo substrate spectrum and any regulatory/physiological trigger for AcpH in *P. putida* (e.g., during solvent stress, PHA/rhamnolipid or secondary-metabolite production, or CoA imbalance) remain to be tested.
- **Future work:** recombinant expression and kinetic characterization of PP_0922; substrate profiling against *P. putida* AcpP and secondary-metabolite carrier proteins; a KT2440 Δ*PP_0922* phenotype under metabolic stress; and structural determination to confirm the Mn²⁺ HD-like active site.

---

## 9. Key References

- Thomas J, Cronan JE. *The enigmatic acyl carrier protein phosphodiesterase of Escherichia coli: genetic and enzymological characterization.* **PMID 16107329** (2005) — identity of acpH (yajB), non-essentiality, solubility, 6–16C acyl-ACP substrate range.
- Thomas J, Rigden DJ, Cronan JE. *AcpH … is a non-canonical member of the HD phosphatase/phosphodiesterase family.* **PMID 17198382** (2007) — Ser-36 phosphodiester cleavage, Mn²⁺ dependence, HD superfamily, mutagenesis of metal ligands.
- Murugan et al. *Expression, purification and characterization of the acyl carrier protein phosphodiesterase from Pseudomonas aeruginosa.* **PMID 20064615** (2010) — soluble Pseudomonas ortholog; FAS-ACP preference; activity on acyl/PKS carriers.
- Thomas J, Cronan JE. *Antibacterial activity of N-pentylpantothenamide…* **PMID 20047918** (2010) — AcpH removes modified (N5-Pan) prosthetic groups.
- Jackowski S, Rock CO. *Turnover of the 4′-phosphopantetheine prosthetic group of acyl carrier protein.* **PMID 6363417** (1984) — prosthetic-group turnover tied to CoA levels.
- Jackowski S, Rock CO. *Ratio of active to inactive forms of acyl carrier protein in E. coli.* **PMID 6317688** (1983) — apo-ACP not normally detected; rapid reconversion to holo-ACP.
- Supporting AcpS/PPTase context: **PMID 35337986**, **PMID 11032795**.

---

*Report generated through iterative literature review (PubMed) and bioinformatic analysis (UniProt sequence retrieval, pairwise alignment to characterized orthologs, KEGG orthology/pathway and genomic-context inspection).*


## Artifacts

- [OpenScientist final report](PP_0922-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0922-deep-research-openscientist_artifacts/final_report.pdf)