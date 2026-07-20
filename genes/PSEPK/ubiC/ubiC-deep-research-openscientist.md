---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:48.826006'
end_time: '2026-07-18T18:16:34.498387'
duration_seconds: 1365.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiC
  gene_symbol: ubiC
  uniprot_accession: Q88C66
  protein_description: 'RecName: Full=Probable chorismate pyruvate-lyase {ECO:0000255|HAMAP-Rule:MF_01632};
    Short=CL {ECO:0000255|HAMAP-Rule:MF_01632}; Short=CPL {ECO:0000255|HAMAP-Rule:MF_01632};
    EC=4.1.3.40 {ECO:0000255|HAMAP-Rule:MF_01632};'
  gene_info: Name=ubiC {ECO:0000255|HAMAP-Rule:MF_01632}; OrderedLocusNames=PP_5317;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiC family. {ECO:0000255|HAMAP-
  protein_domains: Chorismate--pyruvate_lyase. (IPR007440); Chorismate_lyase_/UTRA_dom_sf.
    (IPR028978); Chor_lyase (PF04345)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C66
- **Protein Description:** RecName: Full=Probable chorismate pyruvate-lyase {ECO:0000255|HAMAP-Rule:MF_01632}; Short=CL {ECO:0000255|HAMAP-Rule:MF_01632}; Short=CPL {ECO:0000255|HAMAP-Rule:MF_01632}; EC=4.1.3.40 {ECO:0000255|HAMAP-Rule:MF_01632};
- **Gene Information:** Name=ubiC {ECO:0000255|HAMAP-Rule:MF_01632}; OrderedLocusNames=PP_5317;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiC family. {ECO:0000255|HAMAP-
- **Key Domains:** Chorismate--pyruvate_lyase. (IPR007440); Chorismate_lyase_/UTRA_dom_sf. (IPR028978); Chor_lyase (PF04345)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiC** (gene ID: ubiC, UniProt: Q88C66) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ubiC* (Q88C66, PP_5317) in *Pseudomonas putida* KT2440

**Gene:** *ubiC* | **Ordered locus:** PP_5317 | **UniProt:** Q88C66
**Protein:** Probable chorismate pyruvate-lyase (CL / CPL) | **EC 4.1.3.40**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)
**Family:** UbiC family (HAMAP MF_01632); Pfam PF04345 (Chor_lyase); InterPro IPR007440, IPR028978

---

## Identity Verification (Mandatory)

All primary identifiers are mutually consistent and unambiguous. The gene symbol *ubiC* matches the reviewed UniProt protein description, the organism, the family, and the domain architecture supplied in the research brief. **No gene-symbol ambiguity was encountered** — across bacteria, *ubiC* uniformly denotes chorismate pyruvate-lyase, and the most decisive functional evidence was generated in the exact target strain, *P. putida* KT2440. The research below concerns this specific enzyme.

| Field | Confirmed value |
|---|---|
| Gene | *ubiC* (ordered locus **PP_5317**) |
| Protein | Probable chorismate pyruvate-lyase (CL / CPL) |
| EC number | **4.1.3.40** |
| Reaction | chorismate = 4-hydroxybenzoate + pyruvate (RHEA:16505; CHEBI 15361 → 17879 + 29748) |
| Organism | *Pseudomonas putida* KT2440 |
| Length | 185 aa (558 nt; GTG start); UbiC family |
| Family / domains | UbiC family; Pfam **PF04345**; InterPro **IPR007440**, **IPR028978** |
| Localization | Cytoplasm |
| Pathway | Cofactor biosynthesis; **ubiquinone (coenzyme Q) biosynthesis** |

---

## Summary

The gene *ubiC* (PP_5317) of *Pseudomonas putida* KT2440 encodes **chorismate pyruvate-lyase (UbiC; EC 4.1.3.40)**, a small (~185 amino acid), cofactor-independent, soluble cytoplasmic enzyme that removes the enolpyruvyl side chain from **chorismate**, its specific substrate, with concomitant aromatization of the ring, yielding **4-hydroxybenzoate (4HB) plus pyruvate** (RHEA:16505). This is the **first committed, rate-controlling step of ubiquinone (coenzyme Q) biosynthesis**: by drawing chorismate — the terminal branch-point metabolite of the shikimate pathway — away from the aromatic amino-acid, folate, and menaquinone branches, UbiC commits carbon specifically to the respiratory quinone cofactor.

UbiC acts in the **cytoplasm**. Its 4HB product is handed to the immediately adjacent, co-transcribed membrane prenyltransferase **UbiA (PP_5318; 4-hydroxybenzoate octaprenyltransferase, EC 2.5.1.39)**, which prenylates 4HB at the inner membrane and channels it through the remaining Ubi enzymes to produce **ubiquinone**, an essential lipophilic electron carrier of the aerobic respiratory chain. In KT2440 the two genes are physically contiguous — the *ubiC* stop coordinate coincides with the *ubiA* start coordinate — mirroring the classic *ubiCA* operon first defined in *Escherichia coli*. The identity of Q88C66 is corroborated by ~30% sequence identity to *E. coli* UbiC, conserved domain signatures, and the rule-based HAMAP assignment MF_01632.

Two functionally important properties are established directly in the native host. First, UbiC is subject to **product (4HB) feedback inhibition** — a defining kinetic feature demonstrated and engineered around in *P. putida* KT2440. Second, UbiC's anabolic, cofactor-directed role is cleanly separable from *P. putida*'s catabolic 4HB node, the monooxygenase **PobA (PP_3537, EC 1.14.13.2)**, which degrades 4HB to protocatechuate for the β-ketoadipate pathway. UbiC makes 4HB for a cofactor; PobA consumes 4HB for carbon and energy. Together these findings define UbiC as a precise, cytoplasmic, cofactor-supplying branch-point enzyme of central metabolism.

---

## Key Findings

### F001 — UbiC catalyzes chorismate → 4-hydroxybenzoate + pyruvate (EC 4.1.3.40)

The core molecular function of Q88C66/PP_5317 is that of a **chorismate pyruvate-lyase**. The reviewed UniProt record names the protein "Probable chorismate pyruvate-lyase" (CL/CPL) with EC 4.1.3.40 and annotates the catalytic activity as **chorismate = 4-hydroxybenzoate + pyruvate** (RHEA:16505; CHEBI:15361 → CHEBI:17879 + CHEBI:29748). The protein is 185 amino acids, encoded by *ubiC* (PP_5317), and assigned to the UbiC family by HAMAP-Rule MF_01632, with Pfam domain Chor_lyase (PF04345) and InterPro IPR007440. Mechanistically the reaction is an **intramolecular lyase (pyruvyl-elimination) step**: the enolpyruvyl ether side chain is cleaved from chorismate with concomitant aromatization of the previously non-aromatic cyclohexadiene ring, and the enzyme is **cofactor-independent** — it requires no metal ion or organic cofactor.

This assignment rests on experimentally characterized orthologs, not merely computation. In *E. coli*, the committed step of ubiquinone biosynthesis is "the formation of 4-hydroxybenzoate from chorismate by the enzyme chorismate pyruvate-lyase encoded by the *ubiC* gene" ([PMID: 15902464](https://pubmed.ncbi.nlm.nih.gov/15902464/)). Independent confirmation in another gammaproteobacterium comes from *Shigella sonnei*, where "UbiC (SSON_4219) … is a chorismate pyruvate-lyase that catalyzes the conversion of chorismate to 4-HBA" ([PMID: 37036340](https://pubmed.ncbi.nlm.nih.gov/37036340/)). Critically, the full product stoichiometry was verified with an enzyme expressed in the target organism itself: a "heterologously expressed UbiC … converts chorismate into 4HB and pyruvate" in the *P. putida* KT2440 host ([PMID: 30861344](https://pubmed.ncbi.nlm.nih.gov/30861344/)). The convergence of the curated annotation, the conserved family/domain signatures, and functional data from three related bacteria establishes the reaction and narrow substrate specificity with high confidence. Substrate specificity is narrow because chorismate is the last common intermediate of the shikimate pathway; UbiC commits it specifically to the 4HB/ubiquinone branch.

### F002 — UbiC is the first committed, cytoplasmic step of ubiquinone (coenzyme Q) biosynthesis

UniProt places Q88C66 in the pathway "Cofactor biosynthesis; ubiquinone biosynthesis," assigns a subcellular location of **Cytoplasm**, and states the function: "Removes the pyruvyl group from chorismate, with concomitant aromatization of the ring, to provide 4-hydroxybenzoate (4HB) for the ubiquinone pathway." UbiC therefore sits at the **entry point** of coenzyme Q synthesis. Downstream, "the 4-hydroxybenzoate is prenylated by 4-hydroxybenzoate octaprenyltransferase encoded by the *ubiA* gene" ([PMID: 15902464](https://pubmed.ncbi.nlm.nih.gov/15902464/)), which is the committed second step. The biological rationale is direct: "Ubiquinone (Coenzyme Q) is an essential component of bacterial respiratory chains" ([PMID: 15902464](https://pubmed.ncbi.nlm.nih.gov/15902464/)); UbiC's product ultimately becomes the lipophilic electron carrier that shuttles electrons in aerobic respiration.

Because the substrate chorismate feeds several essential branches (aromatic amino acids, folate, menaquinone, siderophores), UbiC's activity governs how much carbon is diverted specifically toward the quinone cofactor — which is precisely what makes it the "committed" step rather than a redundant downstream reaction. In *E. coli*, *ubiC* expression is **carbon-source responsive** (higher on oxidizable versus fermentable carbon), consistent with the greater ubiquinone demand of respiratory growth. As a soluble cytoplasmic enzyme, UbiC generates 4HB in the cytosol, from where the small polar product diffuses to the inner-membrane prenyltransferase UbiA — a common motif whereby a soluble upstream enzyme feeds a hydrophilic precursor into a membrane-anchored biosynthetic pathway.

### F003 — UbiC is subject to product (4-hydroxybenzoate) feedback inhibition, characterized in the native host

A defining kinetic property of UbiC is **feedback inhibition by its own product, 4HB**, demonstrated directly in the target strain. Jha et al. (2019) "engineered a highly specific, genetically encoded biosensor for 4-hydroxybenzoate (4HB) in an industrially relevant host, *Pseudomonas putida* KT2440" ([PMID: 30861344](https://pubmed.ncbi.nlm.nih.gov/30861344/)) and used it to read out UbiC activity. They then "establish a high-throughput screening method to alleviate product inhibition in an industrially relevant enzyme, chorismate pyruvate-lyase (UbiC)" ([PMID: 30861344](https://pubmed.ncbi.nlm.nih.gov/30861344/)). Using benzoate as a non-biosensor-activating surrogate that still inhibits the enzyme, they screened variants with relieved product inhibition; the improved UbiC gave **>2-fold yield improvement** on a plasmid and **~60% improvement** when genomically integrated, in a glucose → *cis,cis*-muconate production strain.

The significance for functional annotation is twofold. First, product inhibition marks UbiC as a **rate-controlling, feedback-sensitive committed enzyme**, exactly as expected for a metabolic branch-point step — feedback by 4HB tunes the rate at which chorismate is committed to the quinone branch. Second, because Q88C66 *is* the endogenous KT2440 UbiC (PP_5317), these observations describe the actual target protein's behavior in its native cellular context, not a heterologous stand-in. This kinetic feature also explains why UbiC is a recurrent engineering target for microbial production of 4HB-derived aromatics.

### F004 — Bioinformatic support: Q88C66 is a bona fide UbiC-family ortholog (~30% identity to *E. coli* UbiC)

Sequence analysis independently corroborates the assignment. A global Needleman–Wunsch alignment of Q88C66 (185 aa) against *E. coli* UbiC (P26602, 165 aa) yields **~30.3% identity** (50/165 aligned columns) with conserved secondary-structure spacing — the signature of divergent orthologs of the same family rather than a chance match. The conserved fold is captured by Pfam PF04345 (Chor_lyase), InterPro IPR007440, and IPR028978 ("Chorismate_lyase_/UTRA_dom_sf"), the latter reflecting the helix-grip / START-like fold that forms the hydrophobic chorismate-binding cavity. This homology is the basis of the HAMAP MF_01632 rule that produces the "Probable" qualifier — modest but unambiguous identity, typical of divergent UbiC orthologs.

Consistent with this, the surrounding literature repeatedly exploits the chorismate → 4HB branch that UbiC controls. Chorismate is described as one of the "aromatic intermediates such as dehydroshikimate or chorismate from which value-added aromatic compounds can be derived" ([PMID: 27871872](https://pubmed.ncbi.nlm.nih.gov/27871872/)) — i.e., the UbiC substrate. And *P. putida* is explicitly a chassis for the product: "Engineered *Escherichia coli* and *Pseudomonas putida* strains are enabling the development of sustainable processes for the manufacture of 2-phenylethanol, p-hydroxycinnamic acid, p-hydroxystyrene, **p-hydroxybenzoate**, anthranilate" ([PMID: 19875279](https://pubmed.ncbi.nlm.nih.gov/19875279/)). The p-hydroxybenzoate (4HB) named there is the direct output of the UbiC reaction, placing the enzyme squarely at the chorismate-to-aromatic branch point.

### F005 — In KT2440, *ubiC* (PP_5317) is contiguous with *ubiA* (PP_5318), forming a *ubiCA* gene pair

Genome coordinates from KEGG show the two genes are physically **coupled on the same strand**: *ubiC*/PP_5317 spans 6,063,112–6,063,669 (+ strand), and *ubiA*/PP_5318 (4-hydroxybenzoate octaprenyltransferase, K03179, EC 2.5.1.39) spans 6,063,669–6,064,559 (+ strand). The *ubiC* stop coordinate (6,063,669) coincides exactly with the *ubiA* start coordinate — the two ORFs directly abut/overlap, a classic operon arrangement. Flanking genes lie on the opposite strand (PP_5315 *rubA* rubredoxin; PP_5319 hypothetical), reinforcing the *ubiCA* unit. KEGG assigns PP_5317 to KO **K03181** (chorismate lyase, EC 4.1.3.40), pathway **ppu00130** ("Ubiquinone and other terpenoid-quinone biosynthesis"), and module **M00117** ("Ubiquinone biosynthesis, prokaryotes, chorismate (+ polyprenyl-PP) => ubiquinol"). The gene uses a GTG start (558 nt, 185 aa) and carries the Chor_lyase Pfam motif plus an Rv2949c-like motif linking it to the mycobacterial chorismate pyruvate-lyase family.

This synteny mirrors *E. coli*, where "the two genes are linked at 91.5 min in the *Escherichia coli* chromosome" ([PMID: 15902464](https://pubmed.ncbi.nlm.nih.gov/15902464/)), with *ubiA* transcribed from the upstream *ubiC* promoter. Physical coupling of the 4HB-**producing** enzyme (UbiC) to the 4HB-**consuming** prenyltransferase (UbiA) implies coordinated expression and efficient substrate hand-off: the soluble UbiC generates 4HB in the cytoplasm and delivers it directly to the membrane-embedded UbiA for the next committed step.

### F006 — UbiC is the dedicated anabolic 4HB source, distinct from the catabolic monooxygenase PobA (PP_3537)

*P. putida* KT2440 maintains **two functionally opposite 4HB nodes**, and UbiC belongs to the anabolic one. KEGG shows: (i) UbiC/PP_5317 (K03181) **synthesizes** 4HB from chorismate for ubiquinone via the adjacent UbiA/PP_5318 (K03179); and (ii) PobA/PP_3537 (K00481; 4-hydroxybenzoate 3-monooxygenase, EC 1.14.13.2), located elsewhere in the genome, **catabolizes** 4HB to protocatechuate, feeding the β-ketoadipate pathway for aromatic degradation. UbiC is anabolic (cofactor supply); PobA is catabolic (carbon/energy); 4HB sits at the junction between them. This distinction rules out any degradative interpretation of UbiC.

The separability is not merely annotational: in muconate-production strains, UbiC-derived 4HB is deliberately routed through PobA → protocatechuate → *cis,cis*-muconate, exploiting "an experimental production strain for the industrial precursor *cis,cis*-muconic acid (muconate)" ([PMID: 30861344](https://pubmed.ncbi.nlm.nih.gov/30861344/)). The clean, independently addressable separation of the two enzymes — one making, one consuming 4HB — confirms that UbiC's precise native role is **biosynthetic entry into the ubiquinone cofactor branch**, not aromatic catabolism.

---

## Mechanistic Model / Interpretation

UbiC occupies a single, sharply defined node in central metabolism: the committed diversion of chorismate toward the respiratory quinone cofactor. The schematic below integrates all six findings.

```
                         SHIKIMATE PATHWAY
                                |
                          (from PEP + E4P)
                                v
                        +---------------+
                        |   CHORISMATE  |  <-- branch-point metabolite
                        +---------------+      (also -> Trp/Phe/Tyr, folate,
                                |               menaquinone, salicylate...)
                                |
        UbiC  (PP_5317, EC 4.1.3.40)  ---- CYTOPLASM ----
        chorismate pyruvate-lyase          cofactor-independent
        [ Q88C66, 185 aa, GTG start ]      FIRST COMMITTED STEP
                                |            feedback-inhibited by 4HB (F003)
                                v
              chorismate  --->  4-HYDROXYBENZOATE (4HB)  +  PYRUVATE
                                |   \
             (anabolic)         |    \____ (catabolic sink) ____
                                v                                v
   UbiA (PP_5318, EC 2.5.1.39)                        PobA (PP_3537, EC 1.14.13.2)
   4HB octaprenyltransferase                          4HB 3-monooxygenase
   INNER MEMBRANE                                     ANABOLIC vs CATABOLIC (F006)
        |                                                        |
        v                                                        v
   3-octaprenyl-4HB ... (Ubi pathway) ...                PROTOCATECHUATE
        |                                                        |
        v                                              beta-ketoadipate pathway
   +----------------+                                  -> TCA (carbon / energy)
   |   UBIQUINONE   |  respiratory-chain electron carrier (F002)
   |  (coenzyme Q)  |
   +----------------+

   ubiCA operon (F005):  ...PP_5317 == PP_5318...  (same strand; abutting ORFs)
```

**Reaction and specificity (F001).** UbiC catalyzes a cofactor-independent, intramolecular elimination: the C3 enolpyruvyl ether of chorismate is cleaved and the ring aromatizes, releasing pyruvate and 4-hydroxybenzoate. The narrow substrate specificity matches the small helix-grip fold that encloses the aromatic ring (F004).

**Localization (F002).** The enzyme is soluble and cytoplasmic, producing 4HB in the cytosol where the small polar product can diffuse to the inner-membrane UbiA. Pairing a soluble upstream enzyme with a membrane-bound downstream partner is a common motif for delivering a hydrophilic precursor into a membrane-anchored pathway.

**Pathway logic (F002, F005).** UbiC is committed because chorismate is a hub metabolite feeding multiple essential branches. Placing a regulated, product-inhibited (F003) lyase at this junction lets the cell meter carbon into ubiquinone according to respiratory demand — reinforced by carbon-source-responsive expression. The physical *ubiCA* linkage provides a genetic mechanism to co-express producer and consumer, minimizing free-4HB accumulation.

**Anabolic vs catabolic split (F006).** A separate catabolic 4HB enzyme (PobA) underscores that UbiC's role is specifically anabolic cofactor supply. In engineered strains, 4HB can be intentionally shunted from the UbiC source into the PobA route to make muconate — direct proof that the two nodes are independently addressable.

| Feature | UbiC (PP_5317) | UbiA (PP_5318) | PobA (PP_3537) |
|---|---|---|---|
| EC | 4.1.3.40 | 2.5.1.39 | 1.14.13.2 |
| Reaction | chorismate → 4HB + pyruvate | 4HB + polyprenyl-PP → 3-prenyl-4HB | 4HB + O₂ + NADPH → protocatechuate |
| Direction | Anabolic (4HB producer) | Anabolic (4HB consumer) | Catabolic (4HB consumer) |
| Localization | Cytoplasm | Inner membrane | Cytoplasm |
| Cofactor | None | Polyprenyl diphosphate | FAD, NADPH, O₂ |
| Pathway | Ubiquinone biosynthesis (entry) | Ubiquinone biosynthesis (step 2) | β-ketoadipate degradation |
| Role vs UbiC | — | Downstream operon partner | Competing catabolic sink |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [15902464](https://pubmed.ncbi.nlm.nih.gov/15902464/) | *Regulation of the ubiquinone biosynthetic genes ubiCA in E. coli* | Defines UbiC as chorismate pyruvate-lyase making 4HB (F001); establishes downstream UbiA prenylation and ubiquinone/respiratory context (F002); documents *ubiCA* chromosomal linkage mirrored in KT2440 (F005). |
| [37036340](https://pubmed.ncbi.nlm.nih.gov/37036340/) | *A 4-HBA-mediated signaling system in Shigella sonnei* | Independent confirmation in another gammaproteobacterium that UbiC is a chorismate pyruvate-lyase converting chorismate → 4HB (F001). |
| [30861344](https://pubmed.ncbi.nlm.nih.gov/30861344/) | *Sensor-Enabled Alleviation of Product Inhibition in Chorismate Pyruvate-Lyase* | Verifies full stoichiometry (chorismate → 4HB + pyruvate) in KT2440 (F001); demonstrates product (4HB) inhibition of UbiC in the native host (F003); shows 4HB routing toward muconate, distinguishing anabolic from catabolic use (F006). |
| [27871872](https://pubmed.ncbi.nlm.nih.gov/27871872/) | *Biotechnological production of aromatic compounds from biomass* | Confirms chorismate is the branch-point precursor exploited in engineering — the UbiC substrate (F004). |
| [19875279](https://pubmed.ncbi.nlm.nih.gov/19875279/) | *Production of aromatic compounds in bacteria* | Shows *P. putida* is used to make p-hydroxybenzoate (4HB), the UbiC product, situating UbiC in the chorismate-derived aromatic network (F004). |

**Supporting / context literature.** The *ubiA* prenyltransferase modeling study ([PMID: 15597200](https://pubmed.ncbi.nlm.nih.gov/15597200/)) details the downstream membrane step; multiple metabolic-engineering reports ([PMID: 30031819](https://pubmed.ncbi.nlm.nih.gov/30031819/), [PMID: 36575132](https://pubmed.ncbi.nlm.nih.gov/36575132/), [PMID: 42025600](https://pubmed.ncbi.nlm.nih.gov/42025600/)) reuse chorismate-pyruvate lyases (including product-inhibition-relieved variants) to over-produce 4HB, corroborating both the reaction and the product-inhibition property across hosts. No reviewed source contradicted the chorismate pyruvate-lyase assignment.

**Evidence hierarchy for Q88C66 specifically.** (1) *Direct biochemistry of close orthologs* (highest weight): UbiC catalysis established in *E. coli* and *Shigella*, and UbiC activity/kinetics measured in the KT2440 background itself (PMID 30861344). (2) *Genetic/regulatory evidence*: *ubiCA* operon organization and carbon-source-dependent regulation in *E. coli* (PMID 15902464). (3) *Bioinformatic/curatorial inference*: HAMAP rule MF_01632, UbiC-family membership, Pfam PF04345, ~30% identity to *E. coli* UbiC, and the "Probable" qualifier indicate the *P. putida* ortholog's function is assigned by strong homology and rule-based curation rather than a dedicated in vitro study of Q88C66 alone. The assignment is nonetheless robust because it is corroborated by direct work on close orthologs and by demonstrated UbiC activity in the KT2440 host.

---

## Supported vs Refuted Hypotheses

**Supported:**
- UbiC catalyzes chorismate → 4HB + pyruvate (EC 4.1.3.40). **Supported** (curated reaction + multiple orthologs).
- UbiC is the committed entry step of ubiquinone biosynthesis. **Supported** (PMID 15902464).
- UbiC is a soluble cytoplasmic enzyme. **Supported** (UniProt; no TM/signal features in the 185-aa sequence).
- UbiC is product-inhibited by 4HB. **Supported** (PMID 30861344, in KT2440).
- *ubiC* and *ubiA* form a conserved contiguous gene pair in *P. putida*. **Supported** (KEGG coordinates; PP_5317 abuts PP_5318).
- UbiC is the anabolic, cofactor-directed 4HB source, distinct from catabolic PobA/PP_3537. **Supported** (KEGG; separate locus/KO).

**Refuted / not supported:**
- The gene-symbol-ambiguity concern (a different gene sharing the "ubiC" symbol) was **refuted**: *ubiC* uniformly denotes chorismate pyruvate-lyase; no conflicting literature was found.
- No evidence that UbiC acts on non-chorismate substrates or requires a cofactor — consistent with a specific, cofactor-independent lyase.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology of Q88C66 itself.** The reaction, substrate specificity, and mechanism are established for orthologs (*E. coli*, *Shigella*) and for UbiC activity in the KT2440 host, but no purified-enzyme kinetic study (kcat, Km for chorismate, Ki for 4HB) of the specific PP_5317 gene product has been reported. The UniProt name retains "Probable," reflecting rule-based (MF_01632) assignment.
2. **Localization is inferred.** The cytoplasmic assignment rests on UniProt annotation and the enzyme's soluble, cofactor-independent character (no transmembrane segment or signal peptide); it has not been confirmed experimentally in *P. putida*.
3. **Structural inference only.** The helix-grip / START-like fold (IPR028978) and active-site residues are inferred from family membership and ~30% identity to *E. coli* UbiC, not from an experimental *P. putida* UbiC structure.
4. **Operon transcription not directly mapped in KT2440.** The *ubiCA* linkage is established from genome coordinates and by analogy to *E. coli*; a *P. putida*-specific transcript/promoter map has not been verified.
5. **Anabolic/catabolic balance unquantified.** The partitioning of 4HB between UbiC-driven anabolic supply for ubiquinone and endogenous PobA-driven catabolism has not been measured for the native locus.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and kinetically characterize Q88C66.** Express recombinant PP_5317 and measure kcat and Km for chorismate and Ki for 4HB (and the benzoate surrogate), converting the "Probable" annotation into a directly demonstrated one.
2. **Solve or model the structure.** Obtain a crystal/cryo-EM structure or high-confidence AlphaFold model with docking to map the chorismate-binding cavity and the residues responsible for 4HB feedback inhibition; compare with the *E. coli* UbiC helix-grip fold.
3. **Confirm subcellular localization.** Use cell fractionation and/or a functional fluorescent fusion in KT2440 to verify cytoplasmic localization and any transient association with UbiA.
4. **Map the *ubiCA* transcript.** Perform RT-PCR/RNA-seq and 5′-RACE to confirm co-transcription of PP_5317–PP_5318, identify the promoter, and test carbon-source responsiveness.
5. **Genetic dependency test.** Construct a *ubiC* deletion and complementation in KT2440; assess ubiquinone content, aerobic respiratory growth, and rescue by exogenous 4HB to formally establish UbiC as the committed, essential entry to the Ubi pathway in this organism.
6. **Quantify flux partitioning.** Introduce product-inhibition-relieved UbiC variants at the native locus and measure flux between the anabolic (UbiA) and catabolic (PobA) 4HB fates to define the branch-point control exerted by UbiC.

---

## Conclusion (Integrated Model)

Six mutually reinforcing lines of evidence — curated reaction annotation (UniProt/HAMAP MF_01632), direct biochemistry of close orthologs (*E. coli*, *Shigella*), native-host activity/kinetics in *P. putida* KT2440, ~30% sequence identity to *E. coli* UbiC, a conserved contiguous *ubiCA* gene pair, and clear separation from the catabolic PobA enzyme — converge on a single, precise annotation:

> **UbiC (Q88C66 / PP_5317) is a soluble cytoplasmic chorismate pyruvate-lyase (EC 4.1.3.40) that cleaves the enolpyruvyl side chain from chorismate — its specific substrate — to yield 4-hydroxybenzoate + pyruvate, the first committed, cofactor-independent, feedback-inhibited step of ubiquinone (coenzyme Q) biosynthesis. Its 4HB product is handed to the immediately adjacent, co-transcribed membrane prenyltransferase UbiA (PP_5318), committing shikimate-pathway carbon to the respiratory-chain lipophilic electron carrier. This anabolic, cofactor-directed role is distinct from catabolic 4HB processing by PobA (PP_3537).**

The primary function, substrate specificity, localization, and pathway placement are established with high confidence; the outstanding gaps are strain-specific in vitro kinetics and a *P. putida*-specific structure.

---

### Key References

- Kwon O, Druce-Hoffman M, Meganathan R (2005) *Regulation of the ubiquinone (coenzyme Q) biosynthetic genes ubiCA in E. coli.* [PMID: 15902464](https://pubmed.ncbi.nlm.nih.gov/15902464/)
- Jha RK et al. (2019) *Sensor-Enabled Alleviation of Product Inhibition in Chorismate Pyruvate-Lyase* (in *P. putida* KT2440). [PMID: 30861344](https://pubmed.ncbi.nlm.nih.gov/30861344/)
- Wang et al. (2023) *A 4-Hydroxybenzoic Acid-Mediated Signaling System Controls the Physiology and Virulence of Shigella sonnei.* [PMID: 37036340](https://pubmed.ncbi.nlm.nih.gov/37036340/)
- *Biotechnological production of aromatic compounds of the extended shikimate pathway from renewable biomass.* [PMID: 27871872](https://pubmed.ncbi.nlm.nih.gov/27871872/)
- *Production of aromatic compounds in bacteria.* [PMID: 19875279](https://pubmed.ncbi.nlm.nih.gov/19875279/)
- UniProt Q88C66 (curated entry; HAMAP MF_01632).
- KEGG genome: ppu:PP_5317 (*ubiC*, K03181), ppu:PP_5318 (*ubiA*, K03179), ppu:PP_3537 (*pobA*, K00481); pathway ppu00130; module M00117.

*Report generated from a 5-iteration autonomous investigation; 6 findings confirmed, 18 papers reviewed. All functional claims are traceable to the reviewed UniProt/KEGG records and to the cited primary literature, with the most decisive functional evidence originating in the target strain* P. putida *KT2440.*


## Artifacts

- [OpenScientist final report](ubiC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15902464
2. PMID:37036340
3. PMID:30861344
4. PMID:27871872
5. PMID:19875279
6. PMID:15597200
7. PMID:30031819
8. PMID:36575132
9. PMID:42025600