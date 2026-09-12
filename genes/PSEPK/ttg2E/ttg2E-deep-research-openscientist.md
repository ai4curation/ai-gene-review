---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:37:33.812817'
end_time: '2026-09-01T03:52:55.834663'
duration_seconds: 4522.02
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ttg2E
  gene_symbol: ttg2E
  uniprot_accession: Q88P90
  protein_description: 'SubName: Full=Toluene-tolerance protein {ECO:0000313|EMBL:AAN66587.1};'
  gene_info: Name=ttg2E {ECO:0000313|EMBL:AAN66587.1}; OrderedLocusNames=PP_0962 {ECO:0000313|EMBL:AAN66587.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: STAS_dom. (IPR002645); STAS_dom_sf. (IPR036513); STAS_2 (PF13466)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
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
  path: ttg2E-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ttg2E-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P90
- **Protein Description:** SubName: Full=Toluene-tolerance protein {ECO:0000313|EMBL:AAN66587.1};
- **Gene Information:** Name=ttg2E {ECO:0000313|EMBL:AAN66587.1}; OrderedLocusNames=PP_0962 {ECO:0000313|EMBL:AAN66587.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** STAS_dom. (IPR002645); STAS_dom_sf. (IPR036513); STAS_2 (PF13466)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ttg2E" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ttg2E' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ttg2E** (gene ID: ttg2E, UniProt: Q88P90) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: ttg2E (PP_0962, UniProt Q88P90)
### *Pseudomonas putida* KT2440

## 1. Summary / Answer

**ttg2E (PP_0962; Q88P90) encodes the MlaB ortholog — a small (100-residue) cytoplasmic STAS-domain protein that is the auxiliary regulatory/assembly subunit of the inner-membrane ABC transporter MlaFEDB (the "Ttg2" system) in *Pseudomonas putida* KT2440.** It is not itself an enzyme or a transporter; instead it binds the MlaF ATPase on the cytoplasmic face of the inner membrane, where it is required for both the correct assembly and the ATP-hydrolytic activity of the transporter. The MlaFEDB complex powers **retrograde transport of mislocalized glycerophospholipids from the outer membrane (OM) back to the inner membrane (IM)**, thereby maintaining OM lipid asymmetry. This membrane-barrier function is the molecular basis for the historically observed "toluene-tolerance" phenotype and for low-level intrinsic resistance to lipid-permeant antibiotics.

## 2. Gene / Protein Identity Verification (mandatory)

The verification requested in the task was performed and **passed**:

- **Gene symbol match:** The gene is named `ttg2E` and is annotated "Toluene-tolerance protein." The "ttg" (toluene-tolerance genes) label originates from a transposon screen in *P. putida* that first identified `ttg` loci required to survive solvent exposure (Kim et al. 1998, PMID 9658016), in which Ttg1/Ttg2 were identified as ABC-transporter homologs. The label is a **phenotype-based historical name**, not a description of the biochemical activity.
- **Organism confirmed:** *Pseudomonas putida* strain KT2440 (taxid 160488); locus tag PP_0962.
- **Domain/family match:** UniProt/InterPro assign a single **STAS domain** (Pfam PF13466 `STAS_2`; InterPro IPR002645 / IPR036513; SUPFAM SSF52091 SpoIIaa-like; Gene3D 3.30.750.24). A ~100-aa protein consisting solely of a STAS domain is the diagnostic architecture of **MlaB**.
- **Operon context (decisive):** PP_0962 is the last gene of the operon **PP_0958–PP_0962**, which UniProt annotates as:

  | Locus | Gene | Len (aa) | Pfam | Mla component |
  |-------|------|----------|------|----------------|
  | PP_0958 | mlaF | 269 | PF00005 (ABC ATPase) | **MlaF** (ATPase / NBD) |
  | PP_0959 | mlaE | 266 | PF02405 | **MlaE** (permease / TMD) |
  | PP_0960 | mlaD | 161 | PF02470 (MCE) | **MlaD** (substrate-binding) |
  | PP_0961 | ttg2D | 215 | PF05494 | **MlaC** (periplasmic shuttle) |
  | **PP_0962** | **ttg2E** | **100** | **PF13466 (STAS)** | **MlaB** (regulatory subunit) |

  This gene order (F‑E‑D‑C‑B) is identical to the canonical *E. coli* `mlaFEDCB` operon, unambiguously assigning **ttg2E = MlaB**. The "Ttg2 = Mla" equivalence is independently confirmed by the demonstration that *P. aeruginosa* Ttg2D is the periplasmic phospholipid-binding (MlaC-type) component of this ABC system (Yero et al. 2021, PMID 33837253).

*No conflicting-gene ambiguity was encountered.* All lines of evidence converge on a single, well-characterized system.

## 3. Primary Function

### 3.1 Molecular role — a STAS-domain adapter/regulator, not an enzyme
MlaB is a cytoplasmic **STAS (Sulphate Transporter and Anti-Sigma-factor antagonist) domain** protein. Direct analysis of the *P. putida* sequence (Q88P90) shows a 100-residue protein consisting of a **single STAS domain (residues 13–100)** with **no signal peptide and no transmembrane segment** (longest hydrophobic stretch = 6 residues, well below the ~15–20 needed for a membrane helix) — i.e. a small, soluble, cytoplasmic protein. In the assembled transporter it clamps onto the nucleotide-binding (ATPase) domain MlaF (typically two MlaB copies per MlaFEDB complex). Functional dissection of the homologous *E. coli* complex showed that the transporter is built from canonical components MlaF and MlaE plus **auxiliary proteins MlaD and MlaB**, and that **"MlaB plays critical roles in both the assembly and activity of the transporter"** (Thong et al. 2016, PMID 27529189). A subsequent explosion of **cryo-EM structures** of MlaFEDB (apo, phospholipid-, ADP- and AMP-PNP-bound; 3.3–4.1 Å) resolves MlaB as an integral subunit of the complex, and mutagenesis mapped residues that "regulate the activity and structural stability of the MlaFEDB complex" (Tang et al. 2021, PMID 33199922; reviewed in Ekiert et al. 2022, PMID 35981415). Thus the precise role of ttg2E is:

- **Structural/assembly:** stabilizes the MlaFEDB complex; without MlaB the complex fails to assemble properly.
- **Regulatory:** modulates/couples ATP hydrolysis by MlaF that energizes lipid transport.

It has **no substrate specificity of its own** (it is not a catalytic or transport subunit); its "substrate" is effectively its protein partner MlaF.

### 3.2 Pathway — Maintenance of Lipid Asymmetry (Mla)
The MlaFEDB transporter is the inner-membrane engine of the cell-envelope-spanning **Mla pathway**, which comprises three assemblies: the OM lipoprotein complex MlaA–OmpC/F, the periplasmic phospholipid shuttle MlaC (= Ttg2D here), and the IM ABC transporter **MlaFEDB** (containing MlaB) (Abellon-Ruiz 2023, PMID 36459067). The pathway removes glycerophospholipids that become mislocalized in the OM outer leaflet and returns them to the inner membrane — i.e. **retrograde (OM→IM) phospholipid transport** — using energy from ATP hydrolysis to maintain OM lipid asymmetry (Thong et al. 2016, PMID 27529189). MlaB's function is therefore executed *within* this pathway by enabling the ATPase that drives the shuttle.

### 3.3 Physiological output — membrane barrier integrity
By preserving OM lipid asymmetry (LPS outer leaflet / phospholipid inner leaflet), the Ttg2/Mla system keeps the OM an effective permeability barrier. This explains the associated phenotypes:
- **Organic-solvent (toluene) tolerance** in *P. putida*: `ttg2` disruption yields toluene-hypersensitive mutants, and membrane integrity/repair — not solvent efflux per se — was identified as the key protective mechanism (Kim et al. 1998, PMID 9658016).
- **Intrinsic antibiotic resistance**: in *P. aeruginosa* the Ttg2 system contributes to low-level resistance against antibiotics that permeate via a lipid-mediated pathway (Yero et al. 2021, PMID 33837253).

## 4. Localization

- **Sub-cellular:** MlaB/ttg2E is a **cytoplasmic** protein peripherally associated with the **cytoplasmic face of the inner membrane**, as part of the MlaFEDB complex (the ATPase MlaF and its MlaB partner face the cytoplasm; MlaE spans the IM; MlaD projects into the periplasm) (PMID 36459067; PMID 27529189; visualized in cryo-EM structures PMID 33199922). This is directly supported by the sequence: a soluble single STAS domain (res 13–100) with no signal peptide and no transmembrane helix in the 100-aa protein.

## 5. Evidence Summary

| Claim | Evidence type | Source |
|-------|---------------|--------|
| ttg2E = MlaB (STAS subunit) | Genomic/operon mapping + domain annotation (UniProt/Pfam/InterPro) | This analysis; UniProt Q88P90 |
| Ttg2 system = Mla lipid-asymmetry ABC transporter in *Pseudomonas* | Crystal structure + biochemistry of Ttg2D=MlaC | Yero et al. 2021, PMID 33837253 |
| MlaB required for assembly + ATPase activity of MlaFEDB | Genetic + biochemical reconstitution (E. coli homolog) | Thong et al. 2016, PMID 27529189 |
| MlaB is an integral subunit of MlaFEDB; regulates complex activity/stability | Cryo-EM (3.3–4.1 Å) + mutagenesis (E. coli homolog) | Tang et al. 2021, PMID 33199922; Ekiert et al. 2022, PMID 35981415 |
| ttg2E is soluble/cytoplasmic (single STAS domain, no TM/signal) | Sequence/bioinformatic analysis of Q88P90 | This analysis (UniProt Q88P90) |
| Pathway = retrograde OM→IM phospholipid transport maintaining OM asymmetry | Review of structural/biochemical literature | Abellon-Ruiz 2023, PMID 36459067; Thong 2016 |
| ttg2 needed for toluene tolerance via membrane integrity | Tn5 mutagenesis in *P. putida* | Kim et al. 1998, PMID 9658016 |
| Ttg2/Mla → intrinsic antibiotic resistance | Gene knockouts in *P. aeruginosa* | Yero et al. 2021, PMID 33837253 |
| ttg2/Mla is distinct from RND solvent-efflux pumps (TtgABC etc.) | Authoritative review of solvent-tolerance mechanisms | Ramos et al. 2002, PMID 12142492 |

Evidence spans **direct experiment** (genetic reconstitution, crystallography, knockouts) in closely related orthologs and **bioinformatic inference** (operon synteny, conserved domain architecture) for the KT2440 protein specifically. No experimental study on the KT2440 MlaB protein itself was found; the annotation is by strong orthology.

## 6. Supported and Refuted Hypotheses

- **Supported:** ttg2E encodes MlaB, a cytoplasmic STAS-domain auxiliary subunit of the inner-membrane MlaFEDB (Ttg2) ABC transporter that maintains OM lipid asymmetry.
- **Refuted / clarified:** The literal annotation "toluene-tolerance protein" does **not** mean ttg2E is a solvent-efflux transporter or a solvent-sensing/detoxifying enzyme. The solvent-tolerance phenotype is an indirect consequence of maintaining OM barrier integrity. An authoritative review of Gram-negative solvent tolerance (Ramos et al. 2002, PMID 12142492) frames the phenomenon in terms of (a) membrane phospholipid/fatty-acid adaptation, (b) vesiculation, and (c) **RND-family** active efflux pumps that export solvents. ttg2E/MlaB contributes to the phospholipid-homeostasis arm (category a), whereas the well-known *P. putida* solvent-efflux pumps are the mechanistically **separate RND systems TtgABC / TtgDEF / TtgGHI** — a different protein superfamily that must not be conflated with the ttg2/Mla ABC transporter, despite the shared "ttg" (toluene-tolerance genes) label.

## 7. Limitations and Future Directions

- Functional data are from orthologs (*E. coli*, *P. aeruginosa*); the KT2440 MlaB has not been individually characterized experimentally, though orthology is unambiguous.
- The direction of net lipid transport (retrograde vs. anterograde) remains debated in the field, though current biochemistry favors retrograde; this affects mechanistic detail but not MlaB's role as an MlaF-regulatory subunit.
- Useful follow-up: co-purify/crystallize the *P. putida* MlaFEDB(ttg2E) complex; measure ATPase activity ± MlaB; test a clean PP_0962 deletion for OM permeability, vesiculation, solvent and antibiotic sensitivity.


## Artifacts

- [OpenScientist final report](ttg2E-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ttg2E-deep-research-openscientist_artifacts/final_report.pdf)