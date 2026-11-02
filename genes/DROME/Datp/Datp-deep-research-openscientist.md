---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-08T14:27:41.223583'
end_time: '2026-10-08T14:53:14.080640'
duration_seconds: 1532.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Datp
  gene_symbol: Datp
  uniprot_accession: Q4V6M1
  protein_description: 'RecName: Full=Bis(5''-nucleosyl)-tetraphosphatase [asymmetrical]
    {ECO:0000256|ARBA:ARBA00018911}; AltName: Full=Diadenosine 5'',5''''''-P1,P4-tetraphosphate
    asymmetrical hydrolase {ECO:0000256|ARBA:ARBA00032644};'
  gene_info: Name=Datp {ECO:0000313|FlyBase:FBgn0287788}; ORFNames=CG31713 {ECO:0000313|EMBL:AAY54701.1,
    ECO:0000313|FlyBase:FBgn0287788};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the Nudix hydrolase family.
  protein_domains: NUDIX_hydrolase-like_dom_sf. (IPR015797); NUDIX_hydrolase_CS. (IPR020084);
    NUDIX_hydrolase_dom. (IPR000086); Nudix_hydrolase_domain. (IPR051325); Tetra_PHTase.
    (IPR003565)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Datp-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Datp-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q4V6M1
- **Protein Description:** RecName: Full=Bis(5'-nucleosyl)-tetraphosphatase [asymmetrical] {ECO:0000256|ARBA:ARBA00018911}; AltName: Full=Diadenosine 5',5'''-P1,P4-tetraphosphate asymmetrical hydrolase {ECO:0000256|ARBA:ARBA00032644};
- **Gene Information:** Name=Datp {ECO:0000313|FlyBase:FBgn0287788}; ORFNames=CG31713 {ECO:0000313|EMBL:AAY54701.1, ECO:0000313|FlyBase:FBgn0287788};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the Nudix hydrolase family.
- **Key Domains:** NUDIX_hydrolase-like_dom_sf. (IPR015797); NUDIX_hydrolase_CS. (IPR020084); NUDIX_hydrolase_dom. (IPR000086); Nudix_hydrolase_domain. (IPR051325); Tetra_PHTase. (IPR003565)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Datp" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Datp' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Datp** (gene ID: Datp, UniProt: Q4V6M1) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *Datp* (Q4V6M1 / CG31713) in *Drosophila melanogaster*

**Target:** Datp (gene symbol *Datp*; ORF CG31713; FlyBase FBgn0287788; UniProt **Q4V6M1**)
**Organism:** *Drosophila melanogaster* (fruit fly)
**Protein family:** Nudix hydrolase superfamily
**Common synonym used in the primary literature:** "Apf"

---

## Summary

**Datp encodes the *Drosophila melanogaster* asymmetrical bis(5′-nucleosyl)-tetraphosphatase (EC 3.6.1.17), a small, heat-stable, divalent-metal–dependent Nudix-superfamily pyrophosphohydrolase.** Its primary and well-defined biochemical function is to cleave diadenosine 5′,5′′′-polyphosphates — principally diadenosine tetraphosphate (Ap4A) — *asymmetrically*, so that the reaction always releases a nucleoside triphosphate: **Ap4A → ATP + AMP**. This identity rests on direct enzymology performed on the recombinant *Drosophila* protein itself (Winward et al., 2007, [PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)), which named the enzyme "Apf," measured a mass of 16.6 kDa consistent with the 142-residue Q4V6M1 sequence, and determined kinetic constants in the low-micromolar *Km* range with a *kcat* up to 43 s⁻¹.

**The enzyme acts predominantly in the nucleus.** Apf–EGFP fusion studies localized the protein to the nucleus with apparent preferential association with euchromatin and facultative heterochromatin, and the gene is expressed most highly in embryos and adult females ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)). This places Datp at the catabolic/terminating arm of a signaling axis: the substrate it destroys, Ap4A, is a stress-induced intracellular "alarmone" synthesized by lysyl-tRNA synthetase (LysRS) that, in characterized mammalian systems, regulates Hint1–MITF transcription and STING-dependent innate immunity ([PMID: 14975237](https://pubmed.ncbi.nlm.nih.gov/14975237/); [PMID: 19524539](https://pubmed.ncbi.nlm.nih.gov/19524539/); [PMID: 32494729](https://pubmed.ncbi.nlm.nih.gov/32494729/)). By setting the steady-state concentration of Ap4A, Datp performs the dual "friend-or-foe" biology described for this metabolite: terminating a signaling event and "house-cleaning" a potentially toxic ATP-mimetic back into normal cellular metabolites ([PMID: 11007992](https://pubmed.ncbi.nlm.nih.gov/11007992/); [PMID: 16359314](https://pubmed.ncbi.nlm.nih.gov/16359314/)).

**The functional assignment is supported by four convergent lines of evidence:** (1) direct enzymological characterization of the purified *Drosophila* protein; (2) a catalytic Nudix-box metal-binding motif present at the residue level in the Q4V6M1 sequence; (3) bona-fide orthology to the human asymmetrical Ap4A hydrolase NUDT2 (48.6% full-length identity with a conserved Nudix box); and (4) a high-confidence AlphaFold structural model (global pLDDT 94.9) displaying the canonical Nudix αβα-sandwich fold with an assembled three-glutamate metal-binding pocket. The gene symbol "Datp" and the UniProt protein description are fully consistent with the enzyme characterized in the literature; **no gene-identity ambiguity was encountered.**

---

## Gene / Protein Identity Verification

Before any functional claims, the identity of the target was confirmed against the UniProt record and the primary literature:

| Attribute | UniProt / FlyBase record | Literature / analysis match |
|---|---|---|
| Protein name | Bis(5′-nucleosyl)-tetraphosphatase (asymmetrical); diadenosine 5′,5′′′-P1,P4-tetraphosphate asymmetrical hydrolase | Winward et al. 2007 characterize exactly this activity in the *Drosophila* protein "Apf" ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)) |
| Gene symbol | *Datp* (FBgn0287788); ORF CG31713 | Consistent — "Datp" = **D**iadenosine **t**etra**p**hosphatase |
| Organism | *Drosophila melanogaster* | cDNA cloned and expressed from *D. melanogaster* ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)) |
| Family | Nudix hydrolase | Nudix box present in sequence; αβα-sandwich fold in AlphaFold model |
| Key domains | NUDIX hydrolase (IPR000086/IPR020084); Tetra_PHTase (IPR003565) | Tetra_PHTase signature is the dedicated Ap4A-hydrolase domain |

All attributes align. The symbol is **not** ambiguous: "Datp" maps cleanly to a diadenosine tetraphosphatase, and the organism, family, and domains are mutually consistent with the biochemistry in the literature.

---

## Key Findings

### 1. Datp is an asymmetrical Ap4A hydrolase that cleaves Ap4A into ATP + AMP (F001)

The defining study is Winward, McLennan and colleagues (2007), who **expressed and characterized a heat-stable, 16.6 kDa Nudix hydrolase ("Apf") from a *Drosophila melanogaster* cDNA** that "specifically metabolizes these nucleotides" ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)). The enzyme "always produces an NTP product, with substrate preference depending on pH and divalent ion (Zn²⁺ or Mg²⁺)." For the canonical substrate, **diadenosine tetraphosphate is hydrolysed to ATP and AMP** — the asymmetrical cleavage that gives the enzyme its name (symmetrical Ap4A hydrolases, by contrast, produce two molecules of ADP).

The kinetics place Datp firmly in the high-affinity, catalytically efficient regime expected of a dedicated metabolic hydrolase:

| Substrate | Conditions | *Km* | *kcat* | *kcat/Km* | Product(s) |
|---|---|---|---|---|---|
| Ap4A | pH 6.5, 0.1 mM Zn²⁺ | 9 µM | 43 s⁻¹ | 4.8 µM⁻¹s⁻¹ | ATP + AMP |
| Ap4A | pH 7.5, 20 mM Mg²⁺ | 12 µM | 13 s⁻¹ | 1.1 µM⁻¹s⁻¹ | ATP + AMP |
| Ap6A | pH 7.5, 20 mM Mg²⁺ | 15 µM | 4.0 s⁻¹ | — | ATP only |

Mechanistically, **fluoride potently inhibits Ap4A hydrolysis in the presence of Mg²⁺ (IC₅₀ = 20 µM) but is ineffective with Zn²⁺**, which the authors interpret as "inhibition involving a specific, MgF₃⁻-containing transition-state analogue complex" ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)). This is a diagnostic signature of metal-assisted phosphoryl-transfer chemistry, confirming the enzyme operates by divalent-cation-dependent nucleophilic attack on a phosphate of the Ap4A chain. This is the single strongest piece of evidence in the dossier: it is direct, precise, in-vitro enzymology performed on the exact protein encoded by Q4V6M1.

### 2. The enzyme is predominantly nuclear and enriched in embryos and adult females (F002)

Subcellular localization experiments using **Apf–EGFP fusion constructs reveal Apf to be predominantly nuclear, with apparent preferential association with euchromatin and facultative heterochromatin**, which the authors state "supports a nuclear function for diadenosine tetraphosphate" ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)). This is biologically important because it locates the enzyme's activity — and by inference the pool of Ap4A it regulates — in the compartment where transcriptional and chromatin-associated roles for Ap4A have been proposed.

Developmentally, **Apf mRNA levels are highest in embryos and adult females** ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)), a pattern consistent with a role in rapidly proliferating/early-developmental tissue and in the female germline, where nucleotide pool homeostasis is at a premium.

### 3. The substrate (Ap4A) is a signaling alarmone controlling transcription and innate immunity (F003)

Datp's function is best understood through the biology of its substrate. Ap4A is synthesized by **lysyl-tRNA synthetase (LysRS)**. In immunologically activated mast cells, **Ap4A accumulates intracellularly above 700 µM, binds the MITF repressor Hint-1, liberates MITF, and thereby activates MITF-dependent gene expression** ([PMID: 14975237](https://pubmed.ncbi.nlm.nih.gov/14975237/)). The upstream control of this axis was defined by Yannay-Cohen et al.: LysRS is phosphorylated on Ser207 in a MAPK-dependent manner, released from the multisynthetase complex, and translocated into the nucleus, where its production of Ap4A regulates MITF target genes ([PMID: 19524539](https://pubmed.ncbi.nlm.nih.gov/19524539/)).

Separately, **RNA:DNA hybrids stimulate LysRS-dependent production of Ap4A** to curb STING-dependent inflammation ([PMID: 32494729](https://pubmed.ncbi.nlm.nih.gov/32494729/)), tying the metabolite to innate-immune signaling. Together these establish Ap4A as an intracellular second messenger/alarmone whose steady-state level is determined by the balance of **synthesis (LysRS)** and **degradation (asymmetrical Ap4A hydrolases such as Datp / NUDT2)**. Datp is the degradation arm of this balance in the fly.

### 4. Structural / mechanistic basis: the αβα-sandwich Nudix fold and distal-phosphate cleavage (F004)

The crystal structure of the human orthologue (NUDT2/Ap4A hydrolase, EC 3.6.1.17) shows the **canonical Nudix αβα-sandwich fold** and demonstrates that the enzyme "cleaves the polyphosphate chain at the fourth phosphate from the bound adenosine moiety," which is precisely what produces the asymmetrical ATP + AMP outcome ([PMID: 23384440](https://pubmed.ncbi.nlm.nih.gov/23384440/)). The enzyme class is confirmed as **Nudix-superfamily members that "asymmetrically cleave the metabolite Ap4A into ATP and AMP while facilitating homeostasis"** ([PMID: 24354275](https://pubmed.ncbi.nlm.nih.gov/24354275/)). Datp carries the generic Nudix hydrolase domain (IPR000086/IPR020084) **plus the dedicated Ap4A-hydrolase "Tetra_PHTase" signature (IPR003565)**, and its Mg²⁺-dependent, fluoride-sensitive (MgF₃⁻ transition-state analogue) behavior is the expected fingerprint of this metal-assisted phosphoryl-transfer mechanism.

### 5. The Datp sequence contains the catalytic Nudix-box metal-binding loop (F005)

Residue-level analysis of the 142-amino-acid Q4V6M1 sequence (~15.6–16.6 kDa, matching the measured 16.6 kDa) identifies the **Nudix catalytic loop "RETKEEAG" at residues 50–57**, embedded in the extended Nudix box (G-E-D-D-F-T-T-A-L-R-E-T-K-E-E-A-G-Y, residues ~41–58). The paired glutamates of the **RExxEE** submotif are the canonical divalent-cation (Mg²⁺/Zn²⁺) coordinating residues of Nudix hydrolases. This directly ties the measured biochemistry to a specific catalytic motif in this exact protein.

### 6. Datp fulfills the dual "friend-or-foe" biology of Ap4A (F006)

Authoritative reviews frame dinucleoside polyphosphates as dual-natured: Ap4A/Ap3A "may have important signalling functions, both inside and outside the cell (friend)," but may also be "unavoidable by-products … potentially toxic through their structural similarity to ATP" (foe) (McLennan, 2000 — notably the same senior author as the *Drosophila* study; [PMID: 11007992](https://pubmed.ncbi.nlm.nih.gov/11007992/)). Ap4A is "produced by all cells" in response to "various environmental and genotoxic stresses" ([PMID: 33282915](https://pubmed.ncbi.nlm.nih.gov/33282915/)), and is an emerging signaling regulator and therapeutic target whose biosynthesis and degradation pathways govern its action ([PMID: 40807231](https://pubmed.ncbi.nlm.nih.gov/40807231/)). Nudix enzymes are the classic **"house-cleaning"** family that remove potentially harmful nucleotide by-products "through hydrolysis to normal cellular metabolites" ([PMID: 16359314](https://pubmed.ncbi.nlm.nih.gov/16359314/)). Datp's degradative activity therefore serves both to *terminate* Ap4A signaling and to *detoxify* an ATP mimic.

### 7. Datp is a bona-fide ortholog of human NUDT2 (48.6% identity) (F007)

A global Needleman–Wunsch alignment of full-length Datp (Q4V6M1, 142 aa) against human NUDT2/APAH1 (P50583, 147 aa) gives **68 of 140 aligned positions identical = 48.6% identity**, far above the ~25–30% "twilight zone," indicating confident orthology and functional equivalence. The catalytic Nudix box is essentially identical: Datp "RETKEEAG…" aligns to NUDT2 "RETQEEAG…," with the metal-coordinating RExxEE glutamates fully conserved. Because the human orthologue is the biochemically and structurally defined asymmetrical Ap4A hydrolase ([PMID: 23384440](https://pubmed.ncbi.nlm.nih.gov/23384440/)), this orthology transfers function confidently to Datp.

### 8. The AlphaFold model is a high-confidence single Nudix domain (F008)

The AlphaFold DB model AF-Q4V6M1-F1 (v6) has a **global pLDDT of 94.9** (89.4% of residues > 90; 97.9% > 70); only the C-terminal three residues (140–142) are low-confidence. The 142-residue model is a single compact domain, with the catalytic Nudix box (residues 50–57) in the high-confidence core. The predicted fold matches the family assignment: "similar to the canonical Nudix fold, human Ap4A hydrolase shows the common αβα-sandwich architecture" ([PMID: 23384440](https://pubmed.ncbi.nlm.nih.gov/23384440/)) — the exact architecture the Datp model recapitulates.

### 9. The AlphaFold active site assembles a three-glutamate metal-binding pocket (F009)

In the model, the Nudix-box loop is R50-E51-T52-K53-E54-E55-A56-G57. The side-chain carboxyl carbons of the three catalytic glutamates cluster tightly in 3D: **Glu51–Glu54 = 5.1 Å, Glu51–Glu55 = 5.4 Å, Glu54–Glu55 = 7.7 Å**, with all three ≤ 4.1 Å from a common centroid. This convergence is the hallmark geometry of a Nudix divalent-metal coordination site and provides a structural explanation for the experimentally observed metal-dependent, fluoride-sensitive catalysis ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)).

---

## Mechanistic Model / Interpretation

Datp sits at the **catabolic node** of diadenosine-polyphosphate metabolism in *Drosophila*. The coherent narrative across all nine findings is:

```
          STRESS / IMMUNE / GENOTOXIC STIMULUS
                        │
                        ▼
        Lysyl-tRNA synthetase (LysRS)  ── SYNTHESIS ──►   Ap4A  (alarmone)
                                                            │   │
         (nucleus: Hint1–MITF, STING signaling) ◄──────────┘   │
                                                                │
                              Datp / Apf (NUDT2 ortholog) ── DEGRADATION
                              Nudix αβα-sandwich; 3× Glu–Mg²⁺/Zn²⁺ site
                                                                │
                                                                ▼
                                                        ATP  +  AMP
                                        (asymmetrical cleavage at 4th phosphate;
                                         always yields an NTP product)
```

- **Reaction catalyzed:** Ap4A + H₂O → ATP + AMP (EC 3.6.1.17). The enzyme also hydrolyses higher diadenosine polyphosphates (e.g., Ap6A → ATP), always releasing an NTP — the defining feature of the *asymmetrical* subclass.
- **Substrate specificity:** diadenosine (and related dinucleoside) 5′,5′′′-polyphosphates; high affinity (*Km* ≈ 9–15 µM). Cleavage occurs at the fourth phosphate from one adenosine, explaining the asymmetrical ATP/AMP split (inferred from the NUDT2 orthologue structure).
- **Cofactor / mechanism:** divalent cation (Mg²⁺ or Zn²⁺) coordinated by the clustered Nudix-box glutamates; phosphoryl-transfer transition state trappable by MgF₃⁻ (fluoride inhibition).
- **Localization:** predominantly **nuclear**, associated with euchromatin/facultative heterochromatin — the site where it regulates the nuclear Ap4A pool.
- **Pathway role:** the **terminating/house-cleaning arm** opposing LysRS-driven Ap4A synthesis; it extinguishes Ap4A signaling (Hint1–MITF transcription; STING innate immunity, as defined in mammalian orthologous systems) and prevents accumulation of a toxic ATP-mimetic.

The four independent evidence streams — enzymology, sequence motif, orthology, and structure — converge on the same conclusion, giving this annotation very high confidence.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/) | *Characterisation of a bis(5′-nucleosyl)-tetraphosphatase (asymmetrical) from D. melanogaster* | **Primary, definitive.** Direct enzymology, kinetics, mechanism, localization, and expression of the exact protein (F001, F002, F005, F009) |
| [23384440](https://pubmed.ncbi.nlm.nih.gov/23384440/) | *Crystal structure of wild-type and mutant human Ap4A hydrolase* | Orthologue structure defines αβα fold and distal-phosphate cleavage (F004, F007, F008) |
| [24354275](https://pubmed.ncbi.nlm.nih.gov/24354275/) | *Chlamydia CT771 (nudH) is an asymmetric Ap4A hydrolase* | Confirms Nudix-superfamily identity and homeostatic role of the enzyme class (F004) |
| [14975237](https://pubmed.ncbi.nlm.nih.gov/14975237/) | *LysRS and Ap4A as signaling regulators of MITF in mast cells* | Establishes Ap4A → Hint1/MITF signaling that Datp terminates (F003) |
| [19524539](https://pubmed.ncbi.nlm.nih.gov/19524539/) | *LysRS as key signaling molecule regulating gene expression* | Upstream control of Ap4A synthesis (F003) |
| [32494729](https://pubmed.ncbi.nlm.nih.gov/32494729/) | *LysRS produces Ap4A to curb STING-dependent inflammation* | Links Ap4A to innate-immune pathway (F003) |
| [11007992](https://pubmed.ncbi.nlm.nih.gov/11007992/) | *Dinucleoside polyphosphates — friend or foe?* | Authoritative review; dual signaling/detox framework (F006) |
| [16359314](https://pubmed.ncbi.nlm.nih.gov/16359314/) | *House cleaning, a part of good housekeeping* | Defines the Nudix "house-cleaning" paradigm (F006) |
| [33282915](https://pubmed.ncbi.nlm.nih.gov/33282915/) | *Re-evaluation of Diadenosine Tetraphosphate (Ap4A)* | Ap4A as universal stress-induced alarmone (F006) |
| [40807231](https://pubmed.ncbi.nlm.nih.gov/40807231/) | *Ap4A in Cancer: A Multifaceted Regulator* | Modern synthesis of Ap4A biosynthesis/degradation significance (F006) |

The evidence is strongly **convergent and non-contradictory**. The only inferential (rather than directly measured) elements for Datp specifically are the exact fold/active-site geometry (from the AlphaFold model and the NUDT2 crystal structure) and the detailed cleavage position (from the human orthologue). The core catalytic assignment, kinetics, metal dependence, localization, and expression were all measured on the *Drosophila* protein itself.

---

## Limitations and Knowledge Gaps

1. **In-vivo physiology untested in the fly.** All *Drosophila*-specific data derive from a single biochemical/cell-biological study ([PMID: 17344088](https://pubmed.ncbi.nlm.nih.gov/17344088/)). There are no published loss-of-function (mutant/RNAi/CRISPR) phenotypes establishing what Datp does for the organism — e.g., effects on development, fertility, stress tolerance, or immunity.
2. **Signaling link is inferred, not demonstrated in fly.** The Hint1–MITF and STING connections are established in mammalian systems. Whether the *Drosophila* nuclear Ap4A pool regulated by Datp controls analogous transcriptional/immune outputs has not been directly shown.
3. **Structural data are predicted/orthologous.** The αβα fold, distal-phosphate cleavage geometry, and three-glutamate metal site for Datp come from an AlphaFold model and the NUDT2 crystal structure, not an experimental *Drosophila* structure. No metal ion or substrate was modeled.
4. **Substrate range only partially mapped.** Winward et al. characterized Ap4A and Ap6A; the full specificity profile (Ap3A, Ap5A, other NpₙN, mRNA-cap-like substrates) and any pH/metal switching in vivo is incompletely defined.
5. **Expression resolution is coarse.** "Highest in embryos and adult females" is a bulk-tissue mRNA observation; cell-type-specific and subcellular dynamics under stress are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a *Datp* null allele** (CRISPR/Cas9) and characterize viability, fertility (given female-biased expression), developmental timing, and sensitivity to genotoxic/oxidative/heat stress — directly testing the "alarmone homeostasis" model in vivo.
2. **Measure endogenous Ap4A pools** by LC-MS/MS in wild-type vs. *Datp* mutants, at baseline and under stress, to confirm Datp controls steady-state Ap4A levels in the fly.
3. **Test the nuclear-signaling hypothesis:** profile transcriptional changes (RNA-seq) in *Datp* mutants and examine whether a *Drosophila* Hint homolog / MITF-equivalent (Mitf) or STING/immune (IMD) pathway output shifts with Ap4A accumulation.
4. **Solve an experimental structure** of Datp with bound metal and a non-hydrolyzable Ap4A analogue (or capture the MgF₃⁻ transition-state complex) to validate the predicted three-glutamate active site and the distal-phosphate cleavage position.
5. **Complete the substrate-specificity panel** (Ap3A–Ap6A, Gp4G, Ap4-cap mimics) across physiological pH/metal conditions to delineate the enzyme's full catabolic scope.
6. **Mutagenesis of the Nudix box** (e.g., E54/E55 → Q) to confirm these glutamates are essential for catalysis and metal binding, closing the loop between sequence motif, predicted structure, and measured activity.

---

*Report generated from a 5-iteration autonomous investigation: 9 confirmed findings, 13 papers reviewed, across direct enzymology, sequence-motif analysis, orthology assessment, and AlphaFold structural modeling.*


## Artifacts

- [OpenScientist final report](Datp-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Datp-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17344088
2. PMID:14975237
3. PMID:19524539
4. PMID:32494729
5. PMID:11007992
6. PMID:16359314
7. PMID:23384440
8. PMID:24354275
9. PMID:33282915
10. PMID:40807231