---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T12:17:26.797050'
end_time: '2026-07-23T12:43:15.711442'
duration_seconds: 1548.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaD
  gene_symbol: paaD
  uniprot_accession: Q88HS8
  protein_description: 'SubName: Full=Subunit of phenylacetate degradation enzyme
    {ECO:0000313|EMBL:AAN68882.1};'
  gene_info: Name=paaD {ECO:0000313|EMBL:AAN68882.1}; OrderedLocusNames=PP_3275 {ECO:0000313|EMBL:AAN68882.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Fe-S_Maturation_MIP18. (IPR052339); FSCA_dom_sf. (IPR034904); MIP18-like.
    (IPR002744); PaaD-like. (IPR011883); Zn_ribbon_PaaD. (IPR056572)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: paaD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS8
- **Protein Description:** SubName: Full=Subunit of phenylacetate degradation enzyme {ECO:0000313|EMBL:AAN68882.1};
- **Gene Information:** Name=paaD {ECO:0000313|EMBL:AAN68882.1}; OrderedLocusNames=PP_3275 {ECO:0000313|EMBL:AAN68882.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Fe-S_Maturation_MIP18. (IPR052339); FSCA_dom_sf. (IPR034904); MIP18-like. (IPR002744); PaaD-like. (IPR011883); Zn_ribbon_PaaD. (IPR056572)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaD** (gene ID: paaD, UniProt: Q88HS8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PaaD (Q88HS8 / PP_3275) in *Pseudomonas putida* KT2440

## Summary

**PaaD (gene *paaD*, ordered locus PP_3275; UniProt Q88HS8) is an accessory subunit of the ring-1,2-phenylacetyl-CoA epoxidase (phenylacetyl-CoA oxygenase) that carries out the committed oxygenation step of the aerobic phenylacetic acid (PAA) catabolic pathway in *Pseudomonas putida* KT2440.** The identity is unambiguous: the UniProt annotation ("Subunit of phenylacetate degradation enzyme"), the KEGG orthology assignment (K02612, "ring-1,2-phenylacetyl-CoA epoxidase subunit PaaD"), and the genomic context (PaaD sits inside the *paa* epoxidase gene cluster PP_3274–PP_3278) all converge on the same conclusion. This is the correct gene — a genuine *paaD* orthologue of the well-studied *Escherichia coli paaABCDE* multicomponent oxygenase, in the specified strain and pathway.

The oxygenase complex to which PaaD belongs catalyzes the epoxidation of the aromatic ring of phenylacetyl-CoA (PA-CoA), converting it to ring-1,2-epoxyphenylacetyl-CoA (2,3-epoxy-2,3-dihydrophenylacetyl-CoA) using molecular O₂ and NAD(P)H-derived reducing equivalents. This dearomatizing epoxidation is the hallmark first oxidative step of the "hybrid" aerobic PAA pathway, which is distinct from classical dioxygenase-based ring cleavage. The physiological product is subsequently isomerized to an oxepin-CoA and processed through a β-oxidation-like sequence, ultimately yielding acetyl-CoA and succinyl-CoA that feed the TCA cycle.

Within this complex, PaaD occupies a specialized, non-catalytic role. In vitro reconstitution of the *E. coli* oxygenase demonstrated that PaaA (catalytic α subunit bearing the non-heme di-iron center), PaaB (accessory bridging subunit), PaaC (structural β subunit), and PaaE (NAD(P)H:flavin/[2Fe-2S] reductase) are each necessary for catalysis, whereas **PaaD is not essential for in vitro turnover**. Instead, PaaD's domain architecture — an N-terminal DUF59/MIP18 iron-sulfur (Fe-S) maturation domain fused to a C-terminal PaaD-type zinc ribbon — strongly implicates it in metallocenter assembly, Fe-S cluster trafficking, and/or maturation of the oxygenase in vivo. PaaD therefore is best described as a metallocenter-maturation/assembly accessory factor of the phenylacetyl-CoA oxygenase, functioning in the bacterial cytoplasm as part of the PAA catabolon.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks were completed and **all passed**:

| Verification item | Result |
|---|---|
| Gene symbol "paaD" matches protein description | ✅ UniProt Q88HS8 gene name = *paaD*; description = "Subunit of phenylacetate degradation enzyme" |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950); locus PP_3275 |
| Protein family/domains align with literature | ✅ DUF59/MIP18 (IPR002744), PaaD-like (IPR011883), Zn_ribbon_PaaD (IPR056572), Fe-S maturation MIP18 (IPR052339) — consistent with the *paaD* accessory subunit of the PA-CoA oxygenase |
| No confusion with a same-symbol gene in another organism | ✅ Literature retrieved concerns bacterial *paa* PAA catabolism, matching the target |

The gene is well-placed in the aerobic PAA degradation pathway and is a bona fide orthologue of *E. coli paaD*, so research proceeded with confidence.

---

## Key Findings

### Finding 1 — PaaD is a subunit of the ring-1,2-phenylacetyl-CoA epoxidase of the PAA catabolic pathway

PaaD (Q88HS8 / PP_3275) is a 177-amino-acid protein encoded within the phenylacetate (*paa*) gene cluster of *P. putida* KT2440. KEGG assigns ppu:PP_3275 to KEGG Orthology **K02612**, "ring-1,2-phenylacetyl-CoA epoxidase subunit PaaD," and maps it to phenylalanine metabolism (ppu00360). The genomic neighborhood forms a coherent epoxidase operon:

| Locus | Role in the oxygenase / pathway | *E. coli* equivalent |
|---|---|---|
| PP_3274 | Epoxidase reductase subunit | PaaE |
| **PP_3275** | **PaaD — accessory subunit (this protein)** | **PaaD** |
| PP_3276 | Epoxidase β (structural) subunit | PaaC |
| PP_3277 | Epoxidase accessory/regulatory subunit | PaaB |
| PP_3278 | Epoxidase α (catalytic) subunit | PaaA |
| PP_3279 | Phenylacetate–CoA ligase | PaaK |
| PP_3283 | 1,2-epoxyphenylacetyl-CoA isomerase | PaaG |
| PP_3270 | Oxepin-CoA hydrolase / aldehyde dehydrogenase | PaaZ |
| PP_3280 | Thiolase | PaaJ |

This five-gene core (PP_3274–PP_3278) corresponds to the *E. coli* **paaABCDE** multicomponent oxygenase. The foundational characterization of the *E. coli* pathway established that "the paaABCDE gene products, which may constitute a multicomponent oxygenase, are involved in PA-CoA hydroxylation" ([PMID: 9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/)). Subsequent mechanistic work clarified the chemistry: rather than a simple hydroxylation, "the aromatic ring of phenylacetyl-CoA becomes activated to a ring 1,2-epoxide by a distinct multicomponent oxygenase" ([PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/)), in a pathway conserved between *E. coli* and *P. putida*. PaaD is one subunit of this epoxidase complex.

### Finding 2 — The complex epoxidizes the aromatic ring; PaaD is an accessory subunit dispensable for in vitro catalysis

The definitive biochemical dissection of the oxygenase came from Grishin et al. (2011), who cloned and expressed all five *E. coli* subunits (PaaA, B, C, D, E) and reconstituted the enzyme in vitro. Their key result: "**In vitro reconstitution of the oxygenase subunits showed that each of the PaaA, B, C, and E subunits are necessary for catalysis, whereas PaaD is not essential**" ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/)). This is direct experimental evidence that PaaD is an accessory, non-catalytic subunit.

The same study assigned roles to the catalytic subunits: "PaaAC forms a catalytic core with a monooxygenase fold with PaaA being the catalytic α subunit and PaaC, the structural β subunit" ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/)). PaaA harbors the non-heme carboxylate-bridged di-iron center that activates O₂; PaaC is a catalytically inert structural partner; PaaE is the NAD(P)H:flavin/[2Fe-2S] reductase that supplies electrons to the iron center; and PaaB is a homodimer that bridges two PaaAC heterodimers. A later structural study confirmed that the functional oxygenase is a four-subunit assembly: "the four-subunit phenylacetyl-coenzyme A monooxygenase complex (PA-CoA MO, PaaACBE) that catalyzes the insertion of an oxygen in the aromatic ring of PA" ([PMID: 24055609](https://pubmed.ncbi.nlm.nih.gov/24055609/)). Notably, this active PaaACBE assembly **does not include PaaD**, reinforcing that PaaD acts outside the minimal catalytic machinery.

The reaction catalyzed by the complex is:

```
phenylacetyl-CoA + O2 + NAD(P)H + H+
        │  (PaaABCE oxygenase; di-iron center at PaaA, electrons via PaaE)
        ▼
ring-1,2-epoxyphenylacetyl-CoA (2,3-epoxy-2,3-dihydrophenylacetyl-CoA) + NAD(P)+ + H2O
```

The epoxide product is chemically reactive/toxic, and downstream enzymes act rapidly to process it — the PaaFG hydratase-isomerase complex, for example, is thought to "speed up the steps of the pathway following the conversion of phenylacetyl-CoA to a toxic and unstable epoxide-CoA by PaaABCE monooxygenase" ([PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/)).

### Finding 3 — PaaD carries a DUF59/MIP18 Fe-S maturation domain plus a PaaD zinc ribbon, implicating it in metallocenter/Fe-S maturation

The molecular clue to PaaD's specific accessory role lies in its domain architecture. Q88HS8 contains:

- **N-terminal DUF59/MIP18 domain** — Pfam PF01883 (FeS_assembly_P); InterPro IPR002744 (MIP18-like), IPR052339 (Fe-S_Maturation_MIP18); SUPFAM SSF117916 (Fe-S cluster assembly domain-like). The domain carries the DUF59 hallmark conserved cysteine at **Cys68** within an S-G-C-P motif (…TYSGCPATE…).
- **C-terminal PaaD-type zinc ribbon** — Pfam PF23451 (Zn_ribbon_PaaD); InterPro IPR056572, IPR011883 (PaaD-like). It contains two CxxC pairs (C138-C139…C142 in "CCPQC"; C164…C167 in "RCREC"; plus C158, C176), consistent with a metal-binding zinc ribbon.

eggNOG places PaaD in COG2151, the metallocenter-assembly/DUF59 family. The DUF59 family is functionally well characterized as an Fe-S maturation module. As reviewed for the family: "proteins containing a DUF59, or those composed solely of DUF59, function in FeS protein maturation and/or intracellular Fe homeostasis" ([PMID: 28589301](https://pubmed.ncbi.nlm.nih.gov/28589301/)). The closest bacterial functional analogue is *Staphylococcus aureus* SufT, a DUF59-only protein: "A *S. aureus* ΔsufT mutant was defective in the assembly of FeS proteins" ([PMID: 27517714](https://pubmed.ncbi.nlm.nih.gov/27517714/)). Critically, the conserved DUF59 cysteine — the residue equivalent to PaaD's Cys68 — is mechanistically central: in *Mycobacterium tuberculosis* SufT, "a hyperactive cysteine in the DUF59 domain mediates interaction of SufT with SufS, SufU, aconitase, and SufR" ([PMID: 35427399](https://pubmed.ncbi.nlm.nih.gov/35427399/)).

Taken together, PaaD's architecture strongly suggests it functions in vivo to help assemble or deliver metal/Fe-S cofactors required by the oxygenase — most plausibly supporting maturation of the PaaE [2Fe-2S] reductase center and/or the PaaA di-iron site — which reconciles its in vitro dispensability (cofactors were pre-loaded during heterologous expression) with retention of a dedicated *paaD* gene in the operon across bacteria.

---

## Mechanistic Model / Interpretation

PaaD is best understood as a **cofactor-maturation accessory subunit** embedded in the phenylacetyl-CoA oxygenase module of the aerobic PAA catabolon. The overall pathway and PaaD's place in it:

```
 Phenylalanine / 2-phenylethylamine / styrene / phenylacetaldehyde
                          │  (upper "funnel" routes)
                          ▼
                  Phenylacetic acid (PAA)
                          │  PaaK / phenylacetate–CoA ligase (PP_3279)
                          ▼
                  Phenylacetyl-CoA (PA-CoA)
                          │
   ┌──────────────────────┴───────────────────────────┐
   │   RING-1,2-EPOXIDASE (multicomponent oxygenase)   │
   │   Catalytic core:  PaaA (α, di-Fe) + PaaC (β)     │
   │   Bridging:        PaaB (homodimer)               │
   │   Electron supply: PaaE (NAD(P)H / [2Fe-2S])      │
   │   ── PaaD (this protein): Fe-S/metallocenter ──   │
   │       maturation accessory; DUF59 + Zn-ribbon;    │
   │       NOT required for in vitro catalysis         │
   └──────────────────────┬───────────────────────────┘
                          ▼  + O2, NAD(P)H
        ring-1,2-epoxyphenylacetyl-CoA  (reactive epoxide)
                          │  PaaG isomerase (PP_3283)
                          ▼
                    oxepin-CoA
                          │  PaaZ (PP_3270), PaaFG hydratase-isomerase, PaaJ thiolase
                          ▼
             acetyl-CoA + succinyl-CoA  →  TCA cycle
```

The functional logic: the epoxidase installs a strained, toxic epoxide on the aromatic ring — the committed and chemically demanding step. This requires a properly matured di-iron center (PaaA) and a functional [2Fe-2S]/flavin reductase (PaaE). The DUF59/MIP18 family, to which PaaD belongs, is dedicated precisely to the biogenesis and trafficking of iron-sulfur cofactors under conditions of high cofactor demand. It is therefore mechanistically coherent that a DUF59-plus-zinc-ribbon protein is co-encoded in the oxygenase operon: PaaD likely acts as a pathway-dedicated maturation factor that ensures the oxygenase is correctly metallated in vivo. Its dispensability in a purified in vitro system — where subunits were expressed and folded with their cofactors already loaded — is fully consistent with a maturation/chaperone role rather than a catalytic one.

**Localization.** All evidence indicates PaaD functions in the **bacterial cytoplasm**, where PAA catabolism occurs. The pathway is soluble/cytoplasmic: PA-CoA is generated by a cytoplasmic ligase, the oxygenase and downstream β-oxidation-like enzymes are soluble complexes, and DUF59/Fe-S maturation factors act in the cytosol. (Upstream transport steps such as the PaaL permease are membrane-associated, but the catabolic core — including PaaD — is cytoplasmic.)

---

## Evidence Base

| PMID | Title (abridged) | How it supports the findings |
|---|---|---|
| [9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/) | *Catabolism of phenylacetic acid in E. coli — a new aerobic hybrid pathway* | Establishes paaABCDE as a multicomponent oxygenase acting on PA-CoA (Finding 1) |
| [20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/) | *Bacterial phenylalanine and phenylacetate catabolic pathway revealed* | Defines the ring-1,2-epoxide reaction of the oxygenase; pathway shared by *E. coli* and *P. putida* (Findings 1–2) |
| [21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/) | *Structural and functional studies of the E. coli phenylacetyl-CoA monooxygenase complex* | Direct in vitro proof that PaaA/B/C/E are required but **PaaD is not essential**; assigns catalytic (PaaA) and structural (PaaC) roles (Finding 2) |
| [24055609](https://pubmed.ncbi.nlm.nih.gov/24055609/) | *Family of phenylacetyl-CoA monooxygenases differs in subunit organization* | Confirms active oxygenase is the four-subunit PaaACBE inserting O into the ring — PaaD excluded from the minimal catalytic assembly (Finding 2) |
| [22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/) | *Crystal structure of the PaaF-PaaG hydratase-isomerase complex* | Frames the downstream handling of the toxic epoxide product of PaaABCE (mechanistic context) |
| [28589301](https://pubmed.ncbi.nlm.nih.gov/28589301/) | *Investigating the role(s) of SufT and DUF59 in Fe-S protein maturation* | Establishes the DUF59/MIP18 domain's function in Fe-S maturation / Fe homeostasis (Finding 3) |
| [27517714](https://pubmed.ncbi.nlm.nih.gov/27517714/) | *DUF59 protein SufT in maturation of Fe-S proteins in S. aureus* | ΔsufT is defective in Fe-S protein assembly — closest experimental analogue for PaaD's domain (Finding 3) |
| [35427399](https://pubmed.ncbi.nlm.nih.gov/35427399/) | *M. tuberculosis requires SufT for Fe-S cluster maturation* | Conserved DUF59 cysteine (≈ PaaD Cys68) mediates interactions central to Fe-S maturation (Finding 3) |
| [23104832](https://pubmed.ncbi.nlm.nih.gov/23104832/) | *DUF59 gene AE7 in cytosolic Fe-S cluster assembly (Arabidopsis)* | Broader confirmation that DUF59 proteins are central CIA/Fe-S assembly factors (Finding 3 context) |
| [29057997](https://pubmed.ncbi.nlm.nih.gov/29057997/) | *Domains of Cia2 required for its essential function* | Eukaryotic DUF59 (Cia2) as central Fe-S targeting factor — supports domain-function inference (Finding 3 context) |
| [17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/) | *Last step of aerobic PA degradation* | Confirms succinyl-CoA/acetyl-CoA as pathway end products in *P. putida* and *E. coli* (pathway context) |
| [23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/) | *Taxis of P. putida F1 toward PAA (Aer2)* | Shows PAA pathway is widespread funnel for aromatics in *P. putida* (ecological/pathway context) |
| [21995721](https://pubmed.ncbi.nlm.nih.gov/21995721/) | *σ54-dependent regulation of PAA uptake (PaaL)* | Distinguishes membrane transport (PaaL) from the cytoplasmic catabolic core (localization context) |

---

## Limitations and Knowledge Gaps

1. **No direct biochemical study of *P. putida* PaaD.** The strongest mechanistic evidence (in vitro dispensability, subunit roles) derives from the *E. coli* orthologue. Given the high conservation of the *paa* cluster and KEGG orthology, transfer of function is well justified, but PP_3275 itself has not been individually purified or assayed.

2. **The maturation role is inferred, not demonstrated for PaaD.** The DUF59/MIP18 + zinc-ribbon architecture and the behavior of homologous DUF59 proteins (SufT, Cia2, AE7) provide strong circumstantial evidence for an Fe-S/metallocenter maturation function, but no experiment has directly shown that PaaD matures the PaaE [2Fe-2S] or PaaA di-iron center. Its exact target (PaaE reductase vs. PaaA di-iron site vs. general operon-wide role) remains unresolved.

3. **In vitro dispensability ≠ in vivo dispensability.** PaaD being unnecessary in a reconstituted assay with pre-loaded cofactors does not establish that a *paaD* deletion strain grows normally on PAA; an in vivo phenotype (especially under high Fe-S demand or metal limitation) has not been tested for this gene.

4. **No experimental structure or metal-loading data for Q88HS8.** Cysteine assignments (Cys68 DUF59 hallmark; C-terminal CxxC zinc-ribbon motifs) are sequence-derived; the metal identity and coordination of the zinc ribbon are predicted, not measured.

5. **Localization is inferred** from pathway biochemistry (soluble cytoplasmic catabolism) rather than from direct fractionation/imaging of PaaD.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted deletion phenotyping.** Construct a clean *paaD* (PP_3275) knockout in *P. putida* KT2440 and assay growth on PAA (and on styrene/2-phenylethylamine that funnel through PA-CoA) versus succinate/glucose controls — including under iron-limited conditions and elevated Fe-S demand, where DUF59 factors like SufT become essential.

2. **Cofactor-maturation test.** Compare specific activity and metal/Fe-S content (EPR, Mössbauer, ICP-MS, iron/labile-sulfide assays) of the PaaABCE oxygenase purified from wild-type vs. Δ*paaD* backgrounds to test whether PaaD is required for correct metallation of PaaE and/or PaaA in vivo.

3. **Interaction mapping.** Use pulldown/BACTH/crosslinking-MS to determine whether PaaD physically contacts PaaE, PaaA, or the SUF/ISC Fe-S assembly machinery — mirroring the SufT–SufS/SufU interactions reported in mycobacteria.

4. **Cysteine mutagenesis.** Mutate the conserved DUF59 Cys68 (SGCP motif) and the C-terminal zinc-ribbon cysteines individually to Ala/Ser and assess effects on PAA growth and oxygenase maturation, testing the hypothesized "hyperactive cysteine" mechanism.

5. **Structural characterization.** Solve or accurately model (AlphaFold + metal validation) the PaaD structure to confirm the DUF59 fold, the zinc-ribbon metal site, and the surface likely engaged in cofactor handoff.

6. **Heterologous complementation.** Test whether *E. coli paaD*, *S. aureus sufT*, or other DUF59 factors can complement a *P. putida* Δ*paaD* strain, probing functional interchangeability of the domain.

---

*Report generated from an autonomous literature-and-database investigation (1 iteration, 3 confirmed findings, 21 papers reviewed). All claims are attributed to the cited primary literature and to UniProt/KEGG/InterPro/Pfam/eggNOG database annotations as indicated.*


## Artifacts

- [OpenScientist final report](paaD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9748275
2. PMID:20660314
3. PMID:21247899
4. PMID:24055609
5. PMID:22961985
6. PMID:28589301
7. PMID:27517714
8. PMID:35427399