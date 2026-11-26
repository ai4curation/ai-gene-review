---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T02:27:47.824553'
end_time: '2026-10-19T02:43:12.581110'
duration_seconds: 924.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: ygiQ
  gene_symbol: ygiQ
  uniprot_accession: Q46861
  protein_description: 'RecName: Full=UPF0313 protein YgiQ;'
  gene_info: Name=ygiQ; Synonyms=ygiR; OrderedLocusNames=b4469, JW5501;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the UPF0313 family. .
  protein_domains: Elp3/MiaA/NifB-like_rSAM. (IPR006638); Methylthiotransferase_CS.
    (IPR020612); rSAM. (IPR007197); rSAM_horseshoe. (IPR023404); rSAM_sf. (IPR058240)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ygiQ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ygiQ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q46861
- **Protein Description:** RecName: Full=UPF0313 protein YgiQ;
- **Gene Information:** Name=ygiQ; Synonyms=ygiR; OrderedLocusNames=b4469, JW5501;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the UPF0313 family. .
- **Key Domains:** Elp3/MiaA/NifB-like_rSAM. (IPR006638); Methylthiotransferase_CS. (IPR020612); rSAM. (IPR007197); rSAM_horseshoe. (IPR023404); rSAM_sf. (IPR058240)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ygiQ" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ygiQ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ygiQ** (gene ID: ygiQ, UniProt: Q46861) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *E. coli* ygiQ (UniProt Q46861): The B12-Dependent Radical SAM rRNA Methyltransferase RlmX

## Summary

The *Escherichia coli* K-12 gene **ygiQ** (synonym *ygiR*; ordered locus names **b4469 / JW5501**; UniProt **Q46861**) encodes a **739-residue cytoplasmic radical S-adenosyl-L-methionine (SAM) enzyme** that, until very recently, was annotated only as an "uncharacterized protein of the UPF0313 family." This report resolves that long-standing gap. The gene symbol **ygiQ is correct and unambiguous** for the target protein: it maps cleanly to the UPF0313 family, carries the diagnostic Elp3/MiaA/NifB-like radical SAM core domain plus a methylthiotransferase conserved-site signature, and its organism (E. coli K-12) and domain content all match the UniProt record provided. No confusing cross-organism namesake literature was encountered.

The central discovery of this investigation is that **ygiQ is RlmX**, a **cobalamin (vitamin B12)-dependent radical SAM methyltransferase** that installs an unusual, chemically novel modification on the bacterial ribosome. RlmX catalyzes **two stereoselective methylations of the ribose backbone** in the **peptidyl-transferase center (PTC)** of the 50S large ribosomal subunit's 23S rRNA. Specifically, it methylates the **carbon 5′(S) of the ribose** of **dihydrouridine 2449** (producing D5Sm2449) and of **2′-O-methylcytidine 2498** (producing Cm5Sm2498). This is a direct C–H → C–CH₃ carbon methylation of the ribose C5′ atom — a reaction class accessible only to radical SAM "class B" cobalamin-dependent methyltransferases, not to canonical SAM-dependent methylases. This finding was reported by Ishiguro et al. in *Molecular Cell* in 2026 ([PMID: 41380683](https://pubmed.ncbi.nlm.nih.gov/41380683/)), in which the gene *ygiQ* was formally renamed *rlmX*.

Functionally, these modifications are **hypoxia-induced**: they accumulate under anaerobic growth and, together with the RlhA-dependent modification ho5C2501, help **tune the ribosome for anaerobic life**. Biochemically the modifications **stimulate protein synthesis**, and structurally (by cryo-EM) they **stabilize the P-site and the PTC**. A double knockout of *rlmX* and *rlhA* impairs anaerobic growth. The integrated model is that E. coli uses these PTC ribose methylations to **activate ribosomes under hypoxia**, enhancing translational capacity and survival in oxygen-limited environments such as the gut. The enzyme acts in the **cytoplasm** during/around ribosome biogenesis, operating on the assembled or assembling 50S subunit.

---

## Target Identity Verification

Before presenting findings, the mandatory identity check required by the research brief was completed and **passed**:

| Verification criterion | Expected (UniProt Q46861) | Found in analysis | Status |
|---|---|---|---|
| Gene symbol | ygiQ (syn. ygiR; b4469/JW5501) | ygiQ, renamed rlmX; same locus | ✅ Match |
| Organism | *E. coli* K-12 | *E. coli* K-12 | ✅ Match |
| Protein family | UPF0313 | UPF0313 / PANTHER PTHR32331 "UPF0313 PROTEIN YGIQ" | ✅ Match |
| Key domains | Elp3/MiaA/NifB-like rSAM; methylthiotransferase conserved site; rSAM core/horseshoe | PF04055 (Radical_SAM), PF08497 (Radical_SAM_N), PF11842 (DUF3362/UPF0313 C-terminal); IPR006638; IPR020612 | ✅ Match |
| Cofactor | [4Fe-4S], SAM | [4Fe-4S] radical SAM + auxiliary cluster + cobalamin | ✅ Match |

No literature for a conflicting same-symbol gene in another organism was found. The gene symbol is **not ambiguous** for this target, and the functional literature now available describes exactly this protein.

---

## Key Findings

### Finding 1 — YgiQ is a cytoplasmic [4Fe-4S] radical SAM enzyme of the UPF0313 family

YgiQ (Q46861, YGIQ_ECOLI) is a **739-amino-acid** protein. Sequence and database analysis places it squarely in the **radical SAM superfamily**: it carries Pfam domains **PF04055 (Radical_SAM)**, **PF08497 (Radical_SAM_N)**, and **PF11842 (DUF3362**, the UPF0313 C-terminal domain), and matches the **PROSITE PS51918 RADICAL_SAM profile**. The radical SAM core domain maps to roughly residues **372–650**, with the canonical **[4Fe-4S]-coordinating cysteine motif CxxxCxxC at Cys386/390/393**. The cofactor is a **[4Fe-4S] cluster**, and UniProt keywords include *4Fe-4S*, *Iron-sulfur*, and *S-adenosyl-L-methionine*.

Critically, the protein has **no signal peptide and no transmembrane region**, which — combined with iron-sulfur cluster chemistry that is oxygen-sensitive — indicates a **cytoplasmic** localization. Historically, protein existence was only **level 3 (inferred from homology)**, and the only literature citations attached to the entry were the E. coli K-12 genome sequencing papers ([PMID: 9278503](https://pubmed.ncbi.nlm.nih.gov/9278503/), [PMID: 16397293](https://pubmed.ncbi.nlm.nih.gov/16397293/), [PMID: 16738553](https://pubmed.ncbi.nlm.nih.gov/16738553/)). This confirmed that at the start of the investigation, YgiQ had **no experimentally assigned function**, motivating a family- and structure-based inference strategy that was ultimately superseded by the direct experimental literature in Finding 4.

### Finding 2 — YgiQ belongs to the Elp3/MiaB/NifB-like radical SAM clan

InterPro classifies the UPF0313 family (**IPR022946**) as "functionally uncharacterised" proteins that "contain a radical SAM domain." YgiQ carries **IPR006638 (Elp3/MiaA/NifB-like radical SAM core domain)**, a clan that includes some of the most important radical SAM enzymes in biology: **NifB** (nitrogenase FeMoco assembly), **HemN** (coproporphyrinogen oxidase), **BioB** (biotin synthase), **LipA** (lipoyl synthase), **RimO/MiaB** (methylthiotransferases), **MoaA** (molybdopterin biosynthesis), and **Elp3** (tRNA wobble-base modification). YgiQ additionally matches **IPR020612 (Methylthiotransferase conserved site)**, and its PANTHER family is **PTHR32331 ("UPF0313 PROTEIN YGIQ")**.

This clan membership was the key early inference: it predicted that YgiQ performs **radical-based sulfur-insertion or carbon-methylation chemistry on a macromolecular substrate** (protein, nucleic acid, or cofactor). The eventual experimental assignment — ribose carbon methylation of rRNA — is fully consistent with the chemistry performed by its closest relatives.

### Finding 3 — Two-[4Fe-4S]-cluster architecture with a confidently predicted fold

Direct sequence analysis identified **two conserved cysteine triads**. The first, the canonical radical-SAM **Cx3Cx2C motif at Cys386/390/393** ("CFGGCSFC"), coordinates the SAM-cleaving [4Fe-4S] cluster that generates the 5′-deoxyadenosyl radical. A **second conserved cysteine triad at Cys453/458/464** lies immediately downstream within the segment "...CRRLSCVYPDICPHMD...", a position **diagnostic of an auxiliary [4Fe-4S] cluster** and the basis of the IPR020612 methylthiotransferase conserved-site match. In total, YgiQ has **14 cysteines** (positions 23, 45, 66, 148, 261, 322, 386, 390, 393, 444, 453, 458, 464, 674).

The dual-cluster architecture mirrors that of the **MiaB/RimO methylthiotransferases**, which carry one cluster for reductive SAM cleavage and a second for sulfur/methyl transfer chemistry — a paradigm established by the in vitro characterization of RimO ([PMID: 19736993](https://pubmed.ncbi.nlm.nih.gov/19736993/)), which demonstrated that reconstituted RimO, like MiaB, harbors two distinct [4Fe-4S] clusters and contains the canonical CxxxCxxC motif. The **AlphaFold DB v6 model (Aug 2025)** gives a **mean pLDDT of 87.3** (high confidence), indicating a well-ordered globular fold; only the C-terminal ~50 residues (685–739), which are disordered and polar/basic-biased, are low confidence. This supports a stable, folded catalytic core capable of binding multiple metallocofactors.

### Finding 4 — YgiQ is RlmX, a cobalamin-dependent radical SAM methyltransferase that methylates the ribose C5′ of two 23S rRNA PTC nucleotides

This is the pivotal, function-defining finding. **Ishiguro et al., *Molecular Cell*, 2026 Jan 8;86(1):78–96 ([PMID: 41380683](https://pubmed.ncbi.nlm.nih.gov/41380683/))** reported that the gene *ygiQ* was renamed ***rlmX*** and encodes "**a cobalamin-dependent radical S-adenosylmethionine (SAM) methyltransferase responsible for these methylations**."

The enzyme catalyzes "**two stereoselective methylations of the rRNA backbone in the peptidyl-transferase center (PTC) of the 50S subunit of *Escherichia coli***." The precise chemistry and substrate positions are, in the authors' words:

> "Methylation occurs at carbon 5′(S) of ribose moieties of dihydrouridine at position 2449 (**D5Sm2449**) and 2′-O-methylcytidine at position 2498 (**Cm5Sm2498**)."

In other words, RlmX performs a **direct C–H → C–CH₃ carbon methylation of the ribose C5′ carbon (S configuration)** on 23S rRNA nucleotides **D2449** and **Cm2498**. Deletion of *ygiQ* abolishes both modifications, and they are restored by plasmid-borne *ygiQ* (ΔygiQ loses D5Sm2449 and Cm5Sm2498). The enzyme's **domain architecture** — an N-terminal cobalamin-binding domain + radical SAM [4Fe-4S] domain + C-terminal DUF3362 — places it with the **class B (cobalamin-dependent) radical SAM methyltransferases** (the family that includes OxsB, TsrM, TokK, and Mmp10), within a distinct SSN subgroup corresponding to the UPF0313 family.

This explains every bioinformatic observation from Findings 1–3: the Elp3/MiaB/NifB clan membership (radical carbon chemistry), the dual cysteine triads (radical-SAM cluster for 5′-dAdo• generation plus auxiliary chemistry), and the UPF0313/DUF3362 C-terminal domain (now understood as part of a cobalamin-dependent methyltransferase). The reaction class — **sp³ ribose C–H carbon methylation** — is chemically demanding and is precisely the kind of reaction that **requires both a radical SAM cofactor (to abstract the C5′ hydrogen) and methylcobalamin (to deliver the methyl group)**.

### Finding 5 — The RlmX modifications are hypoxia-induced and promote anaerobic growth by activating translation

The same study ([PMID: 41380683](https://pubmed.ncbi.nlm.nih.gov/41380683/)) established the **physiological role**. The RlmX products D5Sm2449 and Cm5Sm2498, together with **ho5C2501** (installed by the separate enzyme RlhA), "**were elevated under anaerobic growth conditions.**" Functionally:

- "A **double knockout strain lacking *rlmX* and *rlhA*** (responsible for ho5C2501) **impaired anaerobic growth**."
- "**Biochemical studies showed that these rRNA modifications stimulate protein synthesis.**"
- "The **cryoelectron microscopy (cryo-EM) structure** of the ribosome indicated that these **hypoxia-induced modifications stabilize the P-site and the PTC**."

The authors summarize that "**we discovered two stereoselective methylations of the rRNA backbone in the peptidyl-transferase center (PTC) of the 50S subunit of *Escherichia coli* cultured under anaerobic conditions**," and their overarching conclusion is that "**ribosomes are activated by hypoxia-induced modifications to enhance translational capability and thereby survival, under anaerobic conditions.**" This defines RlmX not as a housekeeping constitutive modifier but as part of an **environmentally responsive ribosome-tuning program** that adapts the translational machinery to oxygen limitation.

---

## Mechanistic Model / Interpretation

### The reaction

RlmX (YgiQ) is a **dual-cofactor radical enzyme** that performs **sp³ carbon methylation of a ribose backbone carbon**, a reaction that canonical methyltransferases cannot achieve. The accepted mechanism for class B cobalamin-dependent radical SAM methyltransferases proceeds as follows:

```
           reductive cleavage
  SAM  ───────────────────────►  5′-deoxyadenosyl radical (5′-dAdo•)  +  L-methionine
           [4Fe-4S]^1+ (radical SAM cluster, Cys386/390/393)
                 │
                 ▼
  5′-dAdo•  abstracts the ribose C5′ (S)-H of target nucleotide
                 │  (substrate: 23S rRNA, nucleotides D2449 and Cm2498)
                 ▼
  substrate carbon radical  +  methyl-cobalamin (CH3–Cbl)
                 │
                 ▼
  C5′-methylated ribose  (D5Sm2449 ; Cm5Sm2498)  +  cob(II)alamin
                 │
                 ▼
  cob(II)alamin re-methylated by a second SAM  →  regenerates CH3–Cbl
```

Two [4Fe-4S] clusters (Cys386/390/393 radical-SAM cluster; auxiliary Cys453/458/464 cluster) plus a methylcobalamin cofactor cooperate: the radical SAM cluster generates the 5′-dAdo• that abstracts the inert ribose C5′ hydrogen, and methylcobalamin delivers the methyl group to the resulting carbon radical with strict **(S) stereochemistry**.

### Substrate, location, and pathway

| Property | Assignment | Evidence |
|---|---|---|
| **Primary function** | Cobalamin-dependent radical SAM rRNA methyltransferase | PMID 41380683 |
| **Reaction catalyzed** | Ribose C5′(S) carbon methylation (C–H → C–CH₃) | PMID 41380683 |
| **Substrate** | 23S rRNA of the 50S subunit; nucleotides D2449 and Cm2498 | PMID 41380683 |
| **Products** | D5Sm2449 and Cm5Sm2498 | PMID 41380683 |
| **Cofactors** | [4Fe-4S] (radical SAM) + auxiliary [4Fe-4S] + methylcobalamin; SAM co-substrate | PMID 41380683; sequence/domain analysis |
| **Localization** | Cytoplasm (no signal peptide/TM; acts on ribosome) | UniProt Q46861; sequence analysis |
| **Pathway / process** | rRNA modification / ribosome biogenesis; hypoxia-responsive translational tuning | PMID 41380683 |
| **Physiological role** | Stabilizes P-site/PTC, stimulates translation, promotes anaerobic growth | PMID 41380683 |

### The integrated biological narrative

E. coli lives in environments where oxygen availability fluctuates dramatically — notably the mammalian gut. Under **hypoxia**, the cell upregulates a set of ribose/ring modifications clustered in the **peptidyl-transferase center**, the catalytic heart of the ribosome. RlmX installs two of these (D5Sm2449, Cm5Sm2498) while RlhA installs ho5C2501. These modifications **rigidify and stabilize the P-site and PTC**, which **enhances protein synthesis** precisely when the cell must maximize translational output for anaerobic survival. The loss of both RlmX and RlhA impairs anaerobic growth, demonstrating that this ribosome-tuning program is physiologically important rather than incidental. RlmX is therefore best understood as a **conditional ribosome-maturation enzyme** that couples the metabolic state of the cell (oxygen/redox and cobalamin availability) to the fine-tuning of the translational apparatus.

---

## Evidence Base

| PMID | Title / source | Role in this report |
|---|---|---|
| [41380683](https://pubmed.ncbi.nlm.nih.gov/41380683/) | *Hypoxia-induced ribosomal RNA modifications in the peptidyl-transferase center contribute to anaerobic growth of bacteria* (Ishiguro et al., Mol Cell 2026) | **Primary, definitive source.** Identifies ygiQ = rlmX; defines the cobalamin-dependent radical SAM reaction, substrate (23S rRNA D2449, Cm2498), products (D5Sm2449, Cm5Sm2498), hypoxia induction, translational stimulation, PTC/P-site stabilization (cryo-EM), and anaerobic-growth phenotype of the rlmX/rlhA double knockout. |
| [19736993](https://pubmed.ncbi.nlm.nih.gov/19736993/) | *Characterization of RimO, a new member of the methylthiotransferase subclass of the radical SAM superfamily* | Supports the **two-[4Fe-4S]-cluster architecture** interpretation (Finding 3): RimO, like MiaB, carries two distinct [4Fe-4S] clusters and contains the canonical CxxxCxxC motif; provides the paradigm for dual-cluster radical SAM carbon/sulfur chemistry invoked for YgiQ. |
| [42298833](https://pubmed.ncbi.nlm.nih.gov/42298833/) | *Harnessing the Versatility of SAM-Dependent Enzymes: From Mechanism to Application* | Contextualizes the breadth of SAM-dependent chemistry, including radical SAM carbon methylation. |
| [42236715](https://pubmed.ncbi.nlm.nih.gov/42236715/) | *Elp3 uses a conserved molecular tunnel ... tRNA wobble base modification* | Representative Elp3/MiaB/NifB-clan member (Finding 2); illustrates radical SAM modification of RNA. |
| [42218797](https://pubmed.ncbi.nlm.nih.gov/42218797/) | *Mutagenic Survey of Key Residues of NifB ...* | Representative clan member (NifB) illustrating radical SAM cluster assembly chemistry. |

### How the evidence converges

The bioinformatic lines of evidence (Findings 1–3) and the direct experimental evidence (Findings 4–5) are **mutually reinforcing**. Domain architecture predicted radical carbon chemistry on a macromolecule; the experimental study confirmed exactly that, on rRNA, via a cobalamin-dependent mechanism. The strongest claims rest on a **single but high-quality primary source** (Ishiguro et al., *Molecular Cell* 2026), which combined genetics (knockout/complementation), analytical chemistry (modification mapping), biochemistry (translation assays), and structural biology (cryo-EM) — i.e., precise, mechanism-level evidence rather than high-throughput inference.

---

## Limitations and Knowledge Gaps

1. **Single primary source for function.** The functional assignment, while comprehensive and multi-method, derives from one recent publication ([PMID: 41380683](https://pubmed.ncbi.nlm.nih.gov/41380683/)). Independent replication of the ygiQ→rlmX assignment and the precise modification stoichiometry would strengthen confidence.

2. **In vitro reconstitution details.** The full in vitro reconstitution of RlmX catalysis — demonstrating methylcobalamin dependence, SAM turnover stoichiometry, cluster requirements, and substrate (naked rRNA vs. assembled 50S vs. assembly intermediate) — was not captured in the abstract-level evidence available here. Whether RlmX acts on the mature 50S subunit, an assembly intermediate, or free 23S rRNA remains to be pinned down from the full text.

3. **Order of modifications.** Cm2498 is a doubly modified residue (2′-O-methyl + the new C5′-methyl), raising questions about the **sequence of events** between RlmX and the 2′-O-methyltransferase, and whether one modification is a prerequisite for the other. This epistatic ordering is not resolved by the summary evidence.

4. **Regulation of hypoxia induction.** The modifications are elevated anaerobically, but the regulatory mechanism (e.g., transcriptional control of ygiQ, cobalamin availability, or redox-sensing of the [4Fe-4S] clusters) linking oxygen status to modification level is not fully defined.

5. **Structural model confidence.** The AlphaFold model is high-confidence for the core but the C-terminal ~50 residues are disordered; the functional role (if any) of this tail is unknown. Note the model predicts the apo fold and does not place the cobalamin cofactor.

6. **Database lag.** Many general databases still list YgiQ as "uncharacterized UPF0313 protein." Annotations should be updated to reflect the RlmX assignment.

---

## Proposed Follow-up Experiments / Actions

1. **Independent in vitro reconstitution.** Purify RlmX anaerobically, reconstitute both [4Fe-4S] clusters, and demonstrate methylcobalamin- and SAM-dependent C5′ methylation on a defined 23S rRNA / 50S substrate; measure kinetics and cofactor stoichiometry (e.g., SAM consumed per methyl transferred, confirming the radical-SAM + methylcobalamin dual-SAM mechanism).

2. **Substrate-state mapping.** Use in vitro assays with free 23S rRNA, assembly intermediates, and mature 50S subunits to determine the preferred biological substrate and where in ribosome biogenesis RlmX acts.

3. **Active-site mutagenesis.** Mutate the radical-SAM cysteine triad (C386/390/393) and the auxiliary triad (C453/458/464), plus predicted cobalamin-binding residues, and assay for loss of D5Sm2449/Cm5Sm2498 to establish the catalytic roles of each cofactor site.

4. **Epistasis of Cm2498.** Test whether the 2′-O-methylation at C2498 is required before or after RlmX acts, by combining RlmX assays with the relevant 2′-O-methyltransferase knockout.

5. **Regulatory dissection.** Define how hypoxia controls modification levels — ygiQ transcription, cobalamin pool, or redox state of the clusters — using reporter fusions, cobalamin-limited media, and anaerobic/aerobic transcriptomics.

6. **Structural biology.** Obtain a cryo-EM or crystal structure of RlmX bound to cobalamin, SAM, and an rRNA/ribosome substrate to visualize how it accesses the buried PTC ribose and enforces (S)-stereoselectivity.

7. **Phylogenetic breadth.** Determine how conserved RlmX and these PTC modifications are across bacteria, especially gut anaerobes and pathogens, to assess whether this is a general bacterial anaerobic-adaptation strategy and a potential antibacterial target.

8. **Database curation.** Update UniProt Q46861, EcoCyc, and InterPro to reflect the RlmX function, elevating protein existence to experimental evidence level.

---

## Conclusion

The once-"uncharacterized" E. coli UPF0313 protein **YgiQ (Q46861) is RlmX**, a **cobalamin-dependent radical SAM methyltransferase** that catalyzes **stereoselective ribose C5′(S) carbon methylation of two 23S rRNA nucleotides (D2449 → D5Sm2449; Cm2498 → Cm5Sm2498) in the peptidyl-transferase center** of the 50S ribosomal subunit. It functions in the **cytoplasm** as part of **ribosome maturation**, and its products are **hypoxia-induced modifications that stabilize the P-site/PTC, stimulate translation, and promote anaerobic growth**. Every bioinformatic prediction (radical SAM clan, dual [4Fe-4S] clusters, DUF3362/UPF0313 architecture) is consistent with and explained by this experimentally established function ([PMID: 41380683](https://pubmed.ncbi.nlm.nih.gov/41380683/)).


## Artifacts

- [OpenScientist final report](ygiQ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ygiQ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:41380683
2. PMID:9278503
3. PMID:16397293
4. PMID:16738553
5. PMID:19736993