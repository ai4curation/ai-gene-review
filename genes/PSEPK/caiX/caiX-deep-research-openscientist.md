---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:25:28.512233'
end_time: '2026-08-13T06:34:58.237912'
duration_seconds: 4169.73
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: caiX
  gene_symbol: caiX
  uniprot_accession: Q88R30
  protein_description: 'SubName: Full=Carnitine uptake ABC transporter, periplasmic
    component {ECO:0000313|EMBL:AAN65935.2};'
  gene_info: Name=caiX {ECO:0000313|EMBL:AAN65935.2}; OrderedLocusNames=PP_0304 {ECO:0000313|EMBL:AAN65935.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ABC_choline_sub-bd. (IPR017783); ABC_Gly_betaine_transp_sub-bd.
    (IPR007210); OpuAC (PF04069)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: caiX-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: caiX-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R30
- **Protein Description:** SubName: Full=Carnitine uptake ABC transporter, periplasmic component {ECO:0000313|EMBL:AAN65935.2};
- **Gene Information:** Name=caiX {ECO:0000313|EMBL:AAN65935.2}; OrderedLocusNames=PP_0304 {ECO:0000313|EMBL:AAN65935.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ABC_choline_sub-bd. (IPR017783); ABC_Gly_betaine_transp_sub-bd. (IPR007210); OpuAC (PF04069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "caiX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'caiX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **caiX** (gene ID: caiX, UniProt: Q88R30) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *caiX* (Q88R30 / PP_0304) in *Pseudomonas putida* KT2440

## Summary

**caiX** (gene ID *caiX*; ordered locus name **PP_0304**; UniProt **Q88R30**) of *Pseudomonas putida* KT2440 encodes a **periplasmic substrate-binding protein (SBP)** that functions as the high-affinity recognition/capture component of a **Cbc-type (choline/betaine/carnitine) ATP-binding cassette (ABC) importer**. It is **not an enzyme**: it catalyzes no chemical reaction. Its molecular job is to bind its ligand — **L-carnitine** — in the periplasmic space with micromolar affinity and deliver it to a shared membrane-embedded permease/ATPase core (the **CbcWV** transporter), which then uses ATP hydrolysis to translocate the substrate across the inner membrane into the cytoplasm. This is the first, committed step of carnitine uptake feeding a dedicated carnitine-catabolic pathway.

The identification is robust and reconciles multiple independent lines of evidence. At the sequence/structure level, Q88R30 is a 314-residue protein with a cleaved N-terminal Sec signal peptide and a single **OpuAC domain (Pfam PF04069; InterPro IPR007210/IPR017783)** that folds into the classic **Venus-flytrap, two-lobe "periplasmic binding protein-like II"** architecture (class F SBP) used by compatible-solute/quaternary-ammonium-compound ABC transporters. At the genomic level, PP_0304 sits inside a coherent **carnitine-catabolic gene cluster** (carnitine 3-dehydrogenase PP_0302, dehydrocarnitine cleavage enzyme PP_0303, and the AraC-family regulator CdhR PP_0305), pinpointing carnitine as the physiological cargo. At the orthology level, PP_0304 is **~58–62% identical** to the *P. aeruginosa* protein **CaiX (PA5388)**, which has been directly characterized biochemically as a **carnitine-specific SBP (K_m ≈ 24 µM)** that recruits the shared **CbcWV** membrane core. The cognate CbcWV core (PP_0294/PP_0295) is present in KT2440 ~10 kb upstream of *caiX*, exactly reproducing the experimentally established Pseudomonas "orphan SBP + shared core" paradigm.

Functionally, therefore, CaiX in *P. putida* is best described as the **carnitine-specific periplasmic gatekeeper** of quaternary-ammonium-compound import. Its localization is the **periplasm**; its role is **substrate recognition and delivery**, not transport energetics or catalysis; and it operates at the head of a pathway that allows *P. putida* to use L-carnitine (and short-chain O-acylcarnitines) as carbon, nitrogen and energy sources, and as an osmoprotectant. The conclusion rests on strong bioinformatic and comparative-genomic evidence anchored to direct biochemical characterization of the closely related *P. aeruginosa* ortholog; no *P. putida*-specific biochemical assay of PP_0304 itself has yet been published, which is the principal residual uncertainty.

---

## Key Findings

### Finding 1 — caiX is a periplasmic substrate-binding protein of a betaine/carnitine ABC importer

UniProt Q88R30 describes a **314-amino-acid protein** carrying a cleaved **N-terminal Sec-type signal peptide** (residues 1–24), yielding a mature chain (residues 25–314) that is exported to and functions in the **periplasmic space** rather than the cytoplasm. The protein consists of a single annotated domain (residues ~31–284) identified as an **"ABC-type glycine betaine transport system substrate-binding" domain** — **Pfam PF04069 (OpuAC)**, matched by **InterPro IPR007210** (ABC glycine-betaine transport, substrate-binding) and **IPR017783** (ABC choline substrate-binding). Structural classifiers assign it to the **Gene3D 3.40.190.100** "Glycine betaine-binding periplasmic protein" fold and **SUPFAM SSF53850** "Periplasmic binding protein-like II," i.e., the **Venus-flytrap, two-lobe class F SBP** architecture. Orthology databases are consistent: **eggNOG COG2113** (ABC-type proline/glycine-betaine transport, periplasmic component) and **KEGG ortholog K02002** (glycine betaine/proline ABC transporter substrate-binding protein). GO terms confirm the picture: periplasmic space (GO:0042597), ABC transporter complex (GO:0043190), and choline/quaternary-ammonium-compound binding (GO:0033265).

This constellation of features unambiguously places CaiX in the family of **compatible-solute / quaternary-ammonium-compound ABC-transporter substrate-binding proteins**. The architecture of this transporter class was defined for the *Listeria monocytogenes* OpuC system, described as "an ATP binding protein (OpuCA), an extracellular substrate binding protein (OpuCC), and two membrane-associated proteins presumed to form the permease (OpuCB and OpuCD)" ([PMID: 11055912](https://pubmed.ncbi.nlm.nih.gov/11055912/)). CaiX is the homolog of the **OpuCC/OpuAC-type substrate-binding subunit** — the dedicated recognition component. The mechanistic behaviour of this SBP family is likewise well established: the *Bacillus subtilis* OpuCC structure shows that "OpuCC is composed of two α/β/α globular sandwich domains linked by two hinge regions, with a substrate-binding pocket located at the interdomain cleft. Upon substrate binding, the two domains shift towards each other to trap the substrate" ([PMID: 21366542](https://pubmed.ncbi.nlm.nih.gov/21366542/)). CaiX, sharing the same OpuAC/PF04069 fold, is therefore expected to capture its ligand in the interdomain cleft by this Venus-flytrap closure and present it to the membrane permease.

### Finding 2 — caiX sits in a carnitine-catabolic gene cluster, identifying L-carnitine as its physiological import substrate

The genomic neighbourhood of PP_0304 in *P. putida* KT2440 is not random: it forms a **coherent carnitine-degradation module**, all encoded on the complement strand around *caiX*:

| Locus | Gene / product | KO / EC | Role |
|-------|----------------|---------|------|
| PP_0301 | betainyl-CoA thioesterase | K27492 / EC 3.1.2.33 | CoA-thioester processing |
| PP_0302 | L-carnitine / carnitine 3-dehydrogenase | K17735 / EC 1.1.1.108 | Carnitine oxidation |
| PP_0303 | 3-dehydrocarnitine:acetyl-CoA trimethylamine transferase (dehydrocarnitine cleavage) | K27837 / EC 2.3.1.317 | C–N bond cleavage |
| **PP_0304** | **caiX (SBP)** | **K02002** | **Substrate binding / uptake** |
| PP_0305 | CdhR (AraC-family activator) | K17736 | Carnitine-catabolism regulator |

Nearby genes reinforce the quaternary-ammonium-compound context: PP_0298 is a glycine-betaine-responsive AraC-family activator (K21826), and PP_0310/PP_0311 are dimethylglycine/sarcosine dehydrogenases (K21833/K21834), consistent with downstream demethylation of the betaine/carnitine-derived carbon and nitrogen. The colocalization of the substrate-binding protein with **carnitine 3-dehydrogenase** and a **dehydrocarnitine cleavage** enzyme is the strongest genomic signature that the imported substrate is **L-carnitine**, since these enzymes act specifically on carnitine and its immediate oxidation product.

The substrate assignment is directly supported by structural biochemistry of the same SBP family: crystallographers "determined crystal structures of OpuCC in the apo-form and in complex with carnitine, glycine betaine, choline and ectoine respectively" ([PMID: 21366542](https://pubmed.ncbi.nlm.nih.gov/21366542/)), demonstrating that this OpuAC/PF04069 fold physically binds L-carnitine. At the whole-transporter level, OpuC-type ABC systems "encode an ABC compatible solute transporter which is capable of transporting L-carnitine" ([PMID: 11055912](https://pubmed.ncbi.nlm.nih.gov/11055912/)). The combination of family biochemistry (this SBP fold binds carnitine) and gene context (carnitine-catabolic operon) makes **L-carnitine** the physiological import substrate of CaiX.

### Finding 3 — P. putida caiX is an ortholog of the biochemically characterized carnitine-specific SBP CaiX of the Cbc (CbcWV) ABC transporter

A pairwise global alignment (Needleman–Wunsch) of *P. putida* PP_0304 (Q88R30, 314 aa) against *P. aeruginosa* PAO1 **CaiX / PA5388** (312 aa) gives **192 identical positions (~58–62% amino-acid identity)** — well above the threshold for confident orthology — with the two proteins sharing the same gene symbol (*caiX*) and the same operon architecture (*caiX* adjacent to the carnitine-catabolic *cdh* genes). This is functionally decisive because the *P. aeruginosa* / *P. syringae* CaiX has been **directly characterized as a periplasmic, carnitine-specific substrate-binding protein**.

The defining biochemical study reports that "the core transporter CbcWV also interacts with the carnitine-specific SBP CaiX (K_m, 24 microM) and the betaine-specific SBP BetX (K_m, 0.6 microM)" ([PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/)). This establishes three things simultaneously: (i) CaiX is **carnitine-specific**; (ii) it binds with **micromolar affinity (K_m ≈ 24 µM)**; and (iii) it functions as an **"orphan" SBP** that recruits a **shared membrane core, CbcWV**, which is also used by other substrate-specific SBPs (CbcX for choline, BetX for betaine). The same work notes that "the orphan SBP genes common to bacterial genomes can encode functional SBPs" ([PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/)), which explains why *caiX* in *P. putida* is genomically separated from its permease/ATPase partners yet fully functional.

The substrate range of the CaiX–CbcWV system extends slightly beyond free carnitine: "Short-chain acylcarnitines are imported by the ABC transporter CaiX-CbcWV" ([PMID: 29517479](https://pubmed.ncbi.nlm.nih.gov/29517479/)), whereas medium- and long-chain O-acylcarnitines are hydrolysed extracytoplasmically to free carnitine before uptake. The genetic definition of the operon in *Pseudomonas* — "we previously identified the genes required for carnitine catabolism as the first four genes in the carnitine operon (caiX-cdhCAB; PA5388 to PA5385)" ([PMID: 23524670](https://pubmed.ncbi.nlm.nih.gov/23524670/)) — is precisely mirrored by the *P. putida* PP_0304 / PP_0302–PP_0303 cluster, linking CaiX-mediated transport directly to downstream carnitine catabolism.

### Finding 4 — The cognate CbcWV membrane core (PP_0294/PP_0295) for orphan SBP caiX is present in KT2440

Because CaiX is an orphan SBP, a functional model requires that KT2440 also encode the shared **CbcWV** permease/ATPase core. KEGG KO mapping confirms this: **PP_0294 = choline/betaine/carnitine ABC transporter ATP-binding subunit (K02000, CbcV)** and **PP_0295 = choline/betaine/carnitine ABC transporter membrane/permease subunit (K02001, CbcW)**, located ~10 kb upstream of *caiX* (PP_0304) and carrying an explicit "choline/betaine/carnitine ABC transporter" annotation. The KT2440 genome encodes **multiple K02002 substrate-binding proteins** (PP_0076, PP_0296, PP_0304 = *caiX*, PP_1741, PP_2775, PP_3558), with **PP_0296** — a CbcX-type choline SBP — sitting immediately adjacent to the PP_0294/PP_0295 core. This layout **exactly reproduces the experimentally established Pseudomonas Cbc paradigm** in which a single CbcWV membrane core is shared by several genomically dispersed, substrate-specific SBPs, one of which is the carnitine-specific CaiX. The interpretation that PP_0304, located away from the core, is an orphan SBP recruiting shared CbcWV is directly supported by the finding that "the orphan SBP genes common to bacterial genomes can encode functional SBPs" ([PMID: 19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/)).

---

## Mechanistic Model / Interpretation

CaiX is the **substrate-recognition module** of a modular, "mix-and-match" ABC import system. The Pseudomonas Cbc transporter is unusual and elegant: a **single membrane core (CbcWV)** is shared by **several interchangeable periplasmic SBPs**, each conferring specificity for a different quaternary-ammonium compound. CaiX is the carnitine-dedicated member of this SBP set.

```
        PERIPLASM                          INNER MEMBRANE                 CYTOPLASM
   ------------------------------------------------------------------------------------

   L-carnitine (and short-chain
      O-acylcarnitines)
            │
            ▼
      ┌───────────┐   substrate capture
      │   CaiX    │   (Venus-flytrap closure,
      │ (PP_0304) │    Km ≈ 24 µM)
      └─────┬─────┘
            │ delivers ligand
            ▼
      ╔═══════════════════════╗   CbcW permease (PP_0295, K02001)
      ║   CbcWV core           ║   + CbcV ATPase (PP_0294, K02000)
      ║  (shared by CbcX/BetX/ ║──── ATP → ADP + Pi ───────────►  L-carnitine (cytoplasm)
      ║   CaiX SBPs)           ║
      ╚═══════════════════════╝                                          │
                                                                         ▼
                                            ┌──────────── carnitine catabolic operon ────────────┐
                                            │ PP_0302  carnitine 3-dehydrogenase (EC 1.1.1.108)   │
                                            │ PP_0303  dehydrocarnitine cleavage (EC 2.3.1.317)   │
                                            │ PP_0301  betainyl-CoA thioesterase (EC 3.1.2.33)    │
                                            │ PP_0305  CdhR (AraC-family activator)               │
                                            └──────► carbon / nitrogen / energy + osmoprotection ─┘
```

**Step-by-step:**

1. **Recognition (periplasm).** L-carnitine diffuses through the outer membrane into the periplasm, where CaiX (PP_0304) binds it in the interdomain cleft between its two α/β/α lobes, closing around the ligand (Venus-flytrap mechanism, per the OpuCC structural paradigm). CaiX discriminates carnitine from the chemically similar betaine and choline, which are handled by the sibling SBPs BetX and CbcX.
2. **Delivery and translocation (inner membrane).** The liganded, closed CaiX docks onto the **CbcWV** core (PP_0295 permease + PP_0294 ATPase). ATP binding/hydrolysis at CbcV drives conformational cycling of the CbcW permease, opening a translocation pathway that moves L-carnitine across the inner membrane into the cytoplasm.
3. **Catabolism (cytoplasm).** Imported carnitine enters the adjacent catabolic operon: **carnitine 3-dehydrogenase (PP_0302)** oxidizes it to 3-dehydrocarnitine, which is cleaved by **PP_0303**, ultimately yielding trimethylamine/glycine-betaine-derived carbon and nitrogen that feed central metabolism. **CdhR (PP_0305)** transcriptionally activates the operon in response to carnitine, coupling transport capacity to substrate availability.
4. **Physiological outcome.** The pathway lets *P. putida* exploit L-carnitine (abundant in soil, rhizosphere and animal-associated niches) and short-chain O-acylcarnitines as a **carbon, nitrogen and energy source**, and — because carnitine is also a compatible solute — potentially as an **osmoprotectant**.

The key conceptual point is that CaiX has **no catalytic activity and no transport-energizing activity of its own**. It is a specificity/affinity determinant. Its "reaction" is a reversible binding equilibrium (carnitine + CaiX ⇌ CaiX·carnitine), and its "product" is a loaded receptor primed to trigger ATP-driven import. Its localization is strictly **periplasmic**, defined by its cleaved Sec signal peptide.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the model |
|------|-----------------|---------------------------|
| [19919675](https://pubmed.ncbi.nlm.nih.gov/19919675/) | *The ABC transporter Cbc recruits multiple SBPs with strong specificity for distinct QACs* | **Primary, direct.** Defines CaiX as the carnitine-specific SBP (K_m 24 µM) recruiting the shared CbcWV core; establishes the orphan-SBP paradigm. Anchors the functional assignment of the *P. putida* ortholog. |
| [21366542](https://pubmed.ncbi.nlm.nih.gov/21366542/) | *Structures of the SBP of the B. subtilis OpuC transporter* | **Structural/mechanistic.** Same OpuAC/PF04069 fold as CaiX; crystal structures with carnitine, betaine, choline, ectoine bound; shows two-lobe Venus-flytrap closure. Explains binding mode and demonstrates carnitine binding by this family. |
| [11055912](https://pubmed.ncbi.nlm.nih.gov/11055912/) | *ABC L-carnitine transporter in L. monocytogenes (OpuC)* | **Architectural.** Defines the four-component OpuC transporter and confirms this family transports L-carnitine; positions CaiX as the OpuCC/OpuAC-type SBP homolog. |
| [29517479](https://pubmed.ncbi.nlm.nih.gov/29517479/) | *Processing/transport of short- vs long-chain O-acylcarnitines in P. aeruginosa* | **Substrate range.** Shows CaiX–CbcWV imports free carnitine and short-chain acylcarnitines; long-chain species hydrolysed first. Defines cargo scope. |
| [23524670](https://pubmed.ncbi.nlm.nih.gov/23524670/) | *P. aeruginosa growth on O-acylcarnitines; short-chain acylcarnitine hydrolase* | **Genetic/operon.** Defines the *caiX-cdhCAB* carnitine operon (PA5388–PA5385), mirrored by the *P. putida* PP_0304/PP_0302–0303 cluster; links transport to catabolism. |

**Supporting family/context literature (from the reviewed set):** studies of OpuC in *B. subtilis* and *L. monocytogenes* ([PMID: 12076811](https://pubmed.ncbi.nlm.nih.gov/12076811/), [PMID: 12676677](https://pubmed.ncbi.nlm.nih.gov/12676677/), [PMID: 9925583](https://pubmed.ncbi.nlm.nih.gov/9925583/), [PMID: 33757219](https://pubmed.ncbi.nlm.nih.gov/33757219/)) collectively confirm that OpuC-type ABC systems import carnitine and structurally related betaines with high affinity, and that the SBP determines specificity — consistent with CaiX's assigned role. Pseudomonas-specific betaine/choline-metabolism papers ([PMID: 18156257](https://pubmed.ncbi.nlm.nih.gov/18156257/), [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)) document the broader quaternary-ammonium-compound uptake and catabolism landscape in *P. putida* into which the Cbc/CaiX system fits.

**Note on the ⚠️ identity check:** The mandatory verification is satisfied. The gene symbol *caiX*, the OpuAC/PF04069 domain, the periplasmic SBP fold, the carnitine-operon context, and the ~60% identity to the biochemically characterized *P. aeruginosa* CaiX **all converge**. Importantly, this *caiX* is **NOT** the *Escherichia coli* *cai* system (CaiABCDT, involved in anaerobic carnitine/crotonobetaine metabolism and the CaiT antiporter) — those genes are unrelated in sequence and mechanism. The Pseudomonas *caiX* is specifically the substrate-binding protein of an ABC importer, which is the correct target here.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on PP_0304 itself.** The functional assignment is inferred from (a) the strongly characterized *P. aeruginosa* ortholog CaiX and (b) family/structural biochemistry of OpuCC/OpuAC proteins. There is **no published binding assay, K_d/K_m measurement, or transport reconstitution using the *P. putida* KT2440 protein specifically.** The ~58–62% identity, while comfortably in the orthology range, leaves open the possibility of subtly shifted affinity or specificity.

2. **Specificity fine-structure untested locally.** Whether *P. putida* CaiX excludes betaine/choline as cleanly as *P. aeruginosa* CaiX, and its exact affinity for short-chain O-acylcarnitines, has not been measured in this organism.

3. **Core-partner interaction not experimentally demonstrated in KT2440.** The pairing of PP_0304 with the PP_0294/PP_0295 (CbcWV) core is inferred from KEGG annotation, genomic layout, and the Pseudomonas paradigm — not from co-purification, in vitro reconstitution, or genetics in KT2440.

4. **Regulation and induction not directly verified.** The role of CdhR (PP_0305) in inducing *caiX* in KT2440, and any osmotic/σ-factor control (as seen for OpuC in Gram-positives), remain inferred rather than measured for this locus.

5. **Signal peptide handling.** Whether the mature protein is soluble periplasmic or lipoprotein-anchored has not been experimentally confirmed for PP_0304 (UniProt annotates a cleaved Sec signal, consistent with a soluble periplasmic SBP, typical of Gram-negative ABC importers).

---

## Proposed Follow-up Experiments / Actions

1. **Direct ligand-binding assay of recombinant PP_0304.** Express and purify the mature CaiX (residues 25–314) and measure binding to L-carnitine, glycine betaine, choline, ectoine, crotonobetaine, γ-butyrobetaine, and short-chain O-acylcarnitines by **isothermal titration calorimetry (ITC)** or **intrinsic tryptophan fluorescence**. Expected: high-affinity (low-µM K_d) binding to carnitine, weak/no binding to betaine/choline — confirming carnitine specificity in KT2440.

2. **Transport reconstitution / genetics.** Construct a KT2440 **ΔPP_0304 mutant** and test growth on L-carnitine (and short-chain acylcarnitines) as sole C/N source; complement to restore. Combine with **ΔPP_0294/ΔPP_0295 (CbcWV core)** deletions to confirm the shared-core dependency and the orphan-SBP model. Radiolabelled [¹⁴C]carnitine uptake assays would quantify the transport phenotype.

3. **In vitro CaiX–CbcWV interaction.** Co-purify or cross-link PP_0304 with the reconstituted PP_0294/PP_0295 core (proteoliposomes) and measure ATPase stimulation upon addition of carnitine-loaded CaiX — the direct test of functional recruitment.

4. **Structural determination.** Solve the CaiX crystal or cryo-EM structure in apo and carnitine-bound states to visualize the Venus-flytrap closure and the carnitine-binding pocket residues; compare to the OpuCC and *P. aeruginosa* CaiX structures.

5. **Regulatory analysis.** Use RT-qPCR / reporter fusions to test induction of the PP_0301–PP_0305 operon by carnitine and its dependence on CdhR (PP_0305); assess any osmotic modulation.

6. **Substrate-range profiling.** Test whether the KT2440 system, like *P. aeruginosa*, imports short-chain but not long-chain O-acylcarnitines, and identify any dedicated extracytoplasmic acylcarnitine hydrolase in the KT2440 genome (analogous to the *P. aeruginosa* enzyme in [PMID: 23524670](https://pubmed.ncbi.nlm.nih.gov/23524670/)).

---

## Conclusion

CaiX (Q88R30 / PP_0304) is the **periplasmic, carnitine-specific substrate-binding protein** of a Cbc-type quaternary-ammonium-compound ABC importer in *Pseudomonas putida* KT2440. It binds **L-carnitine** (and short-chain O-acylcarnitines) with micromolar affinity in the periplasm and delivers it to the shared **CbcWV** permease/ATPase core (PP_0294/PP_0295) for ATP-driven import — the committed first step feeding an adjacent carnitine-catabolic operon (PP_0301–PP_0305). The assignment is supported by the OpuAC/PF04069 Venus-flytrap SBP fold, a cleaved Sec signal peptide fixing periplasmic localization, an intact carnitine-catabolic gene cluster, and ~58–62% identity to the biochemically characterized *P. aeruginosa* CaiX (K_m ≈ 24 µM). The main gap is the absence of direct biochemical characterization of the *P. putida* protein itself.


## Artifacts

- [OpenScientist final report](caiX-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](caiX-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11055912
2. PMID:21366542
3. PMID:19919675
4. PMID:29517479
5. PMID:23524670
6. PMID:12076811
7. PMID:12676677
8. PMID:9925583
9. PMID:33757219
10. PMID:18156257
11. PMID:17116241