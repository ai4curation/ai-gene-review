---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T16:54:00.343066'
end_time: '2026-07-17T17:20:28.861916'
duration_seconds: 1588.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argF
  gene_symbol: argF
  uniprot_accession: Q88NX4
  protein_description: 'RecName: Full=Ornithine carbamoyltransferase; Short=OTCase;
    EC=2.1.3.3;'
  gene_info: Name=argF; OrderedLocusNames=PP_1079;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aspartate/ornithine carbamoyltransferase
  protein_domains: Asp/Orn_carbamoyltranf_P-bd. (IPR006132); Asp/Orn_carbamoylTrfase.
    (IPR006130); Asp/Orn_carbamoylTrfase_sf. (IPR036901); Asp_carbamoyltransf_Asp/Orn-bd.
    (IPR006131); Orn/put_carbamltrans. (IPR002292)
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
  path: argF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NX4
- **Protein Description:** RecName: Full=Ornithine carbamoyltransferase; Short=OTCase; EC=2.1.3.3;
- **Gene Information:** Name=argF; OrderedLocusNames=PP_1079;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aspartate/ornithine carbamoyltransferase
- **Key Domains:** Asp/Orn_carbamoyltranf_P-bd. (IPR006132); Asp/Orn_carbamoylTrfase. (IPR006130); Asp/Orn_carbamoylTrfase_sf. (IPR036901); Asp_carbamoyltransf_Asp/Orn-bd. (IPR006131); Orn/put_carbamltrans. (IPR002292)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argF** (gene ID: argF, UniProt: Q88NX4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *argF* (PP_1079, UniProt Q88NX4) — Ornithine Carbamoyltransferase of *Pseudomonas putida* KT2440

## Summary

The gene **argF** (ordered locus **PP_1079**; UniProt accession **Q88NX4**) of *Pseudomonas putida* strain KT2440 encodes the **anabolic ornithine carbamoyltransferase** (OTCase; also written ornithine transcarbamylase/transcarbamoylase, EC 2.1.3.3). This is a metabolic enzyme with a single, well-defined primary function: it catalyzes the reversible transfer of the carbamoyl group from **carbamoyl phosphate** to the side-chain (N-epsilon/N-delta) amino group of **L-ornithine**, producing **L-citrulline** and inorganic phosphate (Rhea reaction 19513: carbamoyl phosphate + L-ornithine = L-citrulline + phosphate + H⁺). This reaction is the sixth and committed step that channels ornithine into the **de novo L-arginine biosynthetic pathway**. The identity of the gene, its organism, and its protein family were all verified against the provided UniProt record: the gene symbol *argF*, the annotation "Ornithine carbamoyltransferase / OTCase / EC 2.1.3.3," the aspartate/ornithine carbamoyltransferase family, and the diagnostic InterPro P-binding and Asp/Orn-binding domains are all mutually consistent, and the supporting literature is drawn from *Pseudomonas* and closely related systems.

The ArgF protein is a **soluble, cytoplasmic homotrimer** of ~34.4 kDa subunits (306 residues in the mature chain, initiator Met removed, no signal peptide or transmembrane segment). Each subunit folds into two domains — an N-terminal carbamoyl-phosphate-binding domain and a C-terminal L-ornithine-binding domain — with the active site formed in the inter-domain cleft and completed by residues from a neighboring subunit of the trimer. Catalysis proceeds by an **ordered mechanism**: carbamoyl phosphate binds first and induces domain closure, after which ornithine binding brings a mobile "SMG" loop (the equivalent of the aspartate transcarbamoylase 240s loop) into the active site; the delta-amino group of ornithine then performs a nucleophilic attack on the carbonyl carbon of carbamoyl phosphate, assisted by a conserved active-site cysteine charge-relay system. Direct analysis of the Q88NX4 sequence confirms the presence of the ornithine-specific catalytic motifs (STRTR, SMG loop, HCLP), establishing substrate specificity for **L-ornithine** rather than aspartate or acylated ornithine derivatives.

Functionally and physiologically, *argF* sits within the **ArgR-controlled arginine regulon**, where it is transcriptionally repressed when arginine is abundant (canonical end-product feedback control), and it catalyzes an **essential, non-redundant** biosynthetic step: specific inhibition of the anabolic OTCase (for example by the natural product phaseolotoxin) produces an **arginine-auxotrophic** phenotype. Importantly, *P. putida* KT2440 encodes **two distinct OTCases** — the biosynthetic ArgF (PP_1079/Q88NX4, this report's target) and a separate **catabolic** paralog (PP_1000/Q88P53) belonging to the arginine deiminase/degradation pathway — mirroring the anabolic-ArgF / catabolic-ArcB duality biochemically characterized in the close relative *Pseudomonas aeruginosa*. ArgF is therefore the dedicated biosynthetic OTCase of *P. putida*.

---

## Key Findings

### Finding 1 — *argF* (PP_1079) encodes the anabolic ornithine carbamoyltransferase, the sixth step of L-arginine biosynthesis

The core annotation is robustly supported. UniProt Q88NX4 annotates *argF*/PP_1079 as **ornithine carbamoyltransferase (OTCase; EC 2.1.3.3)** in the aspartate/ornithine carbamoyltransferase family, carrying the diagnostic Asp/Orn carbamoyltransferase phosphate-binding and Asp/Orn-binding domains (InterPro IPR006132, IPR006131, IPR002292). The enzyme catalyzes the reaction **carbamoyl phosphate + L-ornithine → L-citrulline + phosphate**, which is the sixth step of *de novo* arginine biosynthesis. The *Pseudomonas argF* gene product is specifically the **anabolic (biosynthetic)** enzyme; its loss or inhibition results in arginine auxotrophy.

This is directly corroborated by the primary literature. A structural/evolutionary study of OTCases spanning psychrophiles to thermophiles states plainly that "**This OCTase catalyzes the formation of citrulline from carbamoyl phosphate (CP) and ornithine (ORN) in arginine biosynthesis pathway**" ([PMID: 33084979](https://pubmed.ncbi.nlm.nih.gov/33084979/)), establishing both the chemistry (CP + ornithine → citrulline) and the pathway context. Independently, work on the *Pseudomonas syringae* arginine regulon identifies "**the enzyme ornithine carbamoyltransferase (OCTase), encoded by argF**" ([PMID: 15150254](https://pubmed.ncbi.nlm.nih.gov/15150254/)), confirming that in *Pseudomonas* the *argF* gene specifically encodes the ornithine carbamoyltransferase.

### Finding 2 — ArgF is the trimeric, non-cooperative anabolic OTCase, functionally distinct from the catabolic ArcB

The distinction between anabolic and catabolic OTCases is a defining feature of *Pseudomonas* arginine metabolism. In *P. aeruginosa*, the close relative of *P. putida*, two OTCases coexist: the **anabolic ArgF** and the **catabolic ArcB**. Despite extensive sequence similarity, they operate **unidirectionally in vivo**. The anabolic ArgF is a **trimer** displaying Michaelis-Menten kinetics with **no homotropic cooperativity**, and it drives citrulline synthesis (biosynthesis). The catabolic ArcB is a **dodecamer** with strong homotropic cooperativity for carbamoyl phosphate that suppresses the synthetic reaction and instead favors the phosphorolytic direction (ornithine + carbamoyl phosphate production) during arginine catabolism. N-terminal residues and the C-terminus govern the dodecameric assembly and cooperativity that make the catabolic form catabolic.

This is directly documented: "**Pseudomonas aeruginosa has an anabolic (ArgF) and a catabolic (ArcB) ornithine carbamoyltransferase (OTCase). Despite extensive sequence similarities, these enzymes function unidirectionally in vivo**" ([PMID: 8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/)). This establishes ArgF as the anabolic OTCase acting unidirectionally in biosynthesis, distinct from the catabolic ArcB — a paradigm that maps directly onto *P. putida*'s two-OTCase genome (see Finding 9).

### Finding 3 — Active-site architecture and catalytic mechanism: two-domain trimer, ordered binding, Cys-Asp charge relay, SMG/240s loop closure

The catalytic mechanism of anabolic OTCases is well characterized through crystallographic studies of homologs (E. coli argF/argI-type enzymes, human OTC, and the *P. aeruginosa* catabolic trimer used as a molecular-replacement model). Each subunit folds into two domains — an **N-terminal carbamoyl phosphate (CP)-binding domain** and a **C-terminal L-ornithine-binding domain** — with the active site located in the inter-domain cleft and including residues contributed by an adjacent subunit of the trimer. Catalysis is **ordered**: CP binds first, inducing a global conformational change and domain closure, then ornithine binding recruits the flexible **SMG loop** (equivalent to the aspartate transcarbamoylase 240s loop) into the active site. In the chemical step, the **delta-amino group of L-ornithine performs a nucleophilic attack on the carbonyl carbon of carbamoyl phosphate**; an active-site cysteine (Cys303 in human OTC numbering) forms a charge-relay system with an aspartate (Asp263) and the alpha-amino group of ornithine to promote catalysis. These features map onto the conserved P-binding and Asp/Orn-binding InterPro domains present in Q88NX4.

Three crystallographic studies underpin this mechanistic model. First: "**Each polypeptide chain folds into two domains, a carbamoyl phosphate binding domain and an L-ornithine binding domain**" ([PMID: 9275160](https://pubmed.ncbi.nlm.nih.gov/9275160/)), establishing the conserved two-domain architecture. Second, for the chemistry: "**The side chain of Cys-303 is positioned so as to be able to interact with the delta-amino group of L-ornithine which attacks the carbonyl carbon of carbamoyl phosphate in the enzyme-catalyzed reaction**" ([PMID: 9852088](https://pubmed.ncbi.nlm.nih.gov/9852088/)). Third, for the ordered binding and loop dynamics: "**binding of the first substrate, CP, induces a global conformational change involving relative domain movement, whereas the binding of the second substrate brings the flexible SMG loop**" ([PMID: 11237854](https://pubmed.ncbi.nlm.nih.gov/11237854/)).

### Finding 4 — ArgF is a soluble cytoplasmic enzyme in the L-arginine-via-ornithine pathway

UniProt Q88NX4 curated annotations place the protein in the **cytoplasm** (GO cellular component) and assign the GO biological processes "**L-arginine biosynthetic process via ornithine**" and "**citrulline biosynthetic process**," with molecular functions "**ornithine carbamoyltransferase activity**" and "**amino acid binding**." The mature protein is **306 residues (~34.4 kDa)** with the initiator methionine removed and no signal peptide or transmembrane segment, all consistent with a soluble cytosolic protein. The curated functional statement reads: "Reversibly catalyzes the transfer of the carbamoyl group from carbamoyl phosphate (CP) to the N(epsilon) atom of ornithine (ORN) to produce L-citrulline." The reaction corresponds to **Rhea 19513** (carbamoyl phosphate + L-ornithine = L-citrulline + phosphate + H⁺). In the arginine biosynthetic route this is the step converting L-ornithine to L-citrulline en route to L-arginine.

### Finding 5 — Sequence-level confirmation of L-ornithine (not aspartate) specificity

Direct analysis of the Q88NX4 protein sequence identifies the diagnostic carbamoyltransferase and OTCase-specific catalytic motifs, providing sequence-based (not merely annotation-based) evidence of substrate specificity:

| Motif | Residues | Sequence context | Role |
|-------|----------|-------------------|------|
| **STRTR** | 53–57 | EKS**STRTR**VSF | Carbamoyl-phosphate-binding signature (P-binding domain, IPR006132) |
| **SMG loop** | 223–225 | VVTDVWT**SMG**QEEET | Mobile 240s-loop equivalent; closes over active site on ornithine binding |
| **HCLP** | 258–261 | LFM**HCLP**AHR | Ornithine-binding-domain motif; part of PROSITE OTCase pattern PS00097 |

These motifs map onto the InterPro P-binding (IPR006132) and Asp/Orn-binding (IPR006131) domains annotated for Q88NX4. Critically, the presence of the **ornithine-specific SMG loop and HCLP motif** — rather than the determinants of aspartate carbamoyltransferase — confirms that this enzyme is specific for **L-ornithine**. The presence of the canonical HCLP/PS00097 signature also distinguishes it from the specialized N-acetyl- and N-succinyl-ornithine transcarbamylases found in some other bacteria (see Evidence Base), reinforcing that ArgF uses free L-ornithine as its amine substrate.

### Finding 6 — Anabolic *argF* is transcriptionally repressed by the arginine repressor ArgR

The biosynthetic OTCase gene *argF* is under **negative control by the global arginine regulator ArgR**. In *P. syringae* pv. phaseolicola, *argF* is negatively regulated by ArgR, explicitly described as "similar to what has been reported for *Pseudomonas aeruginosa*." This is the canonical end-product feedback control of the pathway: when arginine is abundant, ArgR represses the anabolic *arg* genes. The carbamoyl phosphate substrate for the reaction is supplied by carbamoyl-phosphate synthetase (CarAB). Because this regulatory logic is conserved across the *Pseudomonas* genus, it applies to *P. putida argF* (PP_1079).

The supporting quote is explicit: "**the enzyme ornithine carbamoyltransferase (OCTase), encoded by argF, is negatively regulated by argR, similar to what has been reported for Pseudomonas aeruginosa**" ([PMID: 15150254](https://pubmed.ncbi.nlm.nih.gov/15150254/)).

### Finding 7 — The anabolic OTCase is physiologically essential for arginine prototrophy: phaseolotoxin inhibition causes arginine auxotrophy

The anabolic OTCase reaction is the essential, non-redundant route to citrulline for arginine biosynthesis. **Phaseolotoxin** and its active moiety, **(R)-N(delta)-(N'-sulfodiaminophosphinyl)-L-ornithine (PSorn)**, are potent **transition-state inhibitors** of the anabolic OTCase, binding the *E. coli* enzyme (ArgI) with a dissociation constant of **Kd = 1.6 pM**. Inhibition of this OTCase produces **arginine auxotrophy**, demonstrating that the ornithine → citrulline step is essential and cannot be bypassed. Bacteria that produce the toxin survive only by expressing a second, toxin-resistant OTCase (ROTCase/ArgK), which underscores that the housekeeping anabolic OTCase encoded by *argF* is normally the sole route to citrulline for biosynthesis.

The direct evidence: "**PSorn acts as a potent transition state (TS) inhibitor of ornithine transcarbamoylase (OTCase, E.C. 2.1.3.3) that binds to the OTCase from Escherichia coli (ARGI) with a dissociation constant of 1.6 pM. While inhibition of OTCase can lead to arginine auxotrophy**" ([PMID: 15766270](https://pubmed.ncbi.nlm.nih.gov/15766270/)). This is reinforced by studies of phaseolotoxin producers, in which the toxin "**inhibit[s] host cell Ornithine transcarbamylase (OTCase) activity and induce[s] Arginine auxotrophic phenotype**," with the resistant enzyme ArgK acting as "a functional replacement of housekeeping OTCase ArgF" ([PMID: 26256666](https://pubmed.ncbi.nlm.nih.gov/26256666/)).

### Finding 8 — Residue-level substrate-binding sites map to the two catalytic subdomains

UniProt Q88NX4 curates **nine substrate-binding residues** distributed across the two functional domains: positions **53, 80, 104, 131, 162** in the N-terminal carbamoyl-phosphate-binding domain, and positions **219, 223, 259, 287** in the C-terminal L-ornithine-binding domain. Position 53 coincides with the carbamoyl-phosphate-binding **STRTR** motif, position 223 with the mobile **SMG (240s) loop**, and position 259 with the **HCLP** ornithine-domain motif identified by direct sequence analysis (Finding 5). This bipartite distribution of contact residues is the structural signature of the ordered, inter-domain active site of trimeric ornithine carbamoyltransferases, and it internally cross-validates the motif assignments.

### Finding 9 — *P. putida* KT2440 encodes two distinct OTCases; PP_1079/*argF* is the anabolic one, separate from catabolic PP_1000

A UniProt query of all EC 2.1.3.3 proteins in *P. putida* KT2440 (taxon 160488) returns exactly **two** ornithine carbamoyltransferases:

| Locus | Accession | Recommended name | Role |
|-------|-----------|------------------|------|
| **PP_1079** | **Q88NX4** | Ornithine carbamoyltransferase | **Anabolic / biosynthetic (argF — this report's target)** |
| PP_1000 | Q88P53 | Ornithine carbamoyltransferase, catabolic | Catabolic (arcB-type; arginine deiminase / degradation pathway) |

This demonstrates, at the level of the *P. putida* genome itself, that *argF*/PP_1079 is the **dedicated anabolic OTCase**, mirroring the anabolic-ArgF / catabolic-ArcB duality established biochemically in *P. aeruginosa* (Finding 2). The existence of a separate catabolic paralog resolves any potential ambiguity: PP_1079 is unambiguously the biosynthetic enzyme.

---

## Mechanistic Model / Interpretation

### The reaction and its place in the pathway

ArgF catalyzes the committed carbamoylation of L-ornithine in the cytoplasm:

```
                                  ArgF (OTCase, EC 2.1.3.3)
   Carbamoyl phosphate  +  L-ornithine  ───────────────────────►  L-citrulline  +  Pi  +  H⁺
        (from CarAB)          (from N-acetyl-              (Rhea 19513)
                              glutamate pathway)
```

Positioned within *de novo* L-arginine biosynthesis, ArgF acts at the junction where the ornithine backbone acquires its ureido group:

```
 Glutamate
    │  (N-acetylation, phosphorylation, reduction, transamination, deacetylation)
    ▼
 L-Ornithine ───────[ ArgF / OTCase, PP_1079 ]───────► L-Citrulline
                     + carbamoyl phosphate (CarAB)
                                                              │  (ArgG: argininosuccinate synthase)
                                                              ▼
                                                       Argininosuccinate
                                                              │  (ArgH: argininosuccinate lyase)
                                                              ▼
                                                          L-Arginine ──┐
                                                                       │ (feedback)
                                                                       ▼
                                                              ArgR represses argF and the
                                                              rest of the arginine regulon
```

### Structural and catalytic logic

ArgF is a homotrimer; each ~34 kDa subunit is bilobal, with a CP-binding lobe and an ornithine-binding lobe, and the three active sites lie at subunit interfaces. The catalytic cycle is an **ordered sequential mechanism**:

```
 1. CP binds first  ──►  global domain closure (P-binding domain clamps down)
 2. L-ornithine binds ──►  SMG/240s loop folds over the active site, sequestering substrates from solvent
 3. Chemistry: ornithine δ-NH₂ (deprotonated via Cys–Asp charge relay) attacks CP carbonyl carbon
             → tetrahedral intermediate → collapse to citrulline + Pi
 4. Products released; loop reopens
```

This ordered mechanism, the two-domain closure, and the SMG-loop dynamics are conserved hallmarks of the transcarbamoylase superfamily and are directly documented in crystallographic studies of human OTC and trimeric bacterial OTCases (Finding 3). The sequence motifs found in Q88NX4 (STRTR, SMG, HCLP) and the nine curated binding residues place this enzyme firmly within the **free-L-ornithine-specific** branch of the family, as opposed to the N-acetyl-ornithine (AOTCase) or N-succinyl-ornithine (SOTCase) transcarbamylases that carbamoylate acylated ornithine derivatives in alternative bacterial arginine routes.

### Directionality and the anabolic/catabolic divide

A crucial mechanistic insight for *Pseudomonas* is that sequence similarity does not equal functional equivalence. ArgF (anabolic) is a non-cooperative trimer poised to run the **synthetic** direction (ornithine → citrulline), whereas the catabolic ArcB-type enzyme (PP_1000 in *P. putida*) is a cooperative dodecamer whose kinetics are tuned to run the **phosphorolytic** direction during arginine degradation via the arginine deiminase pathway. The quaternary structure (trimer vs. dodecamer) and cooperativity determine the physiological direction. ArgF is the biosynthetic workhorse; PP_1000 is its catabolic counterpart.

### Regulation and essentiality

ArgF is embedded in the **ArgR regulon** and repressed when arginine is plentiful — a textbook end-product feedback loop that prevents wasteful biosynthesis. Its essentiality for prototrophy is demonstrated pharmacologically: the picomolar transition-state inhibitor phaseolotoxin/PSorn shuts down the anabolic OTCase and forces arginine auxotrophy, and toxin-producing bacteria must carry a resistant OTCase (ArgK) to survive. Together these establish ArgF as the **single, non-redundant biosynthetic OTCase** under normal conditions.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [33084979](https://pubmed.ncbi.nlm.nih.gov/33084979/) | *OTCase from psychrophiles to thermophiles* | States the reaction (CP + ornithine → citrulline) and pathway (arginine biosynthesis) — Finding 1 |
| [15150254](https://pubmed.ncbi.nlm.nih.gov/15150254/) | *Global arginine regulator ArgR controls argF in P. syringae* | Confirms *argF* encodes OTCase in *Pseudomonas* and is repressed by ArgR — Findings 1, 6 |
| [8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/) | *Catabolic OTCase of P. aeruginosa: N-terminal region for dodecameric structure* | Establishes anabolic ArgF vs. catabolic ArcB, unidirectional in vivo — Findings 2, 9 |
| [9275160](https://pubmed.ncbi.nlm.nih.gov/9275160/) | *Substrate-induced conformational change in a trimeric OTCase* | Two-domain (CP-binding + ornithine-binding) subunit architecture — Finding 3 |
| [9852088](https://pubmed.ncbi.nlm.nih.gov/9852088/) | *1.85-Å human OTC with PALO* | Cys303 charge relay; ornithine δ-amino nucleophilic attack on CP carbonyl — Finding 3 |
| [11237854](https://pubmed.ncbi.nlm.nih.gov/11237854/) | *Human OTC: crystallographic insights* | Ordered binding (CP first) and SMG-loop closure — Finding 3 |
| [15766270](https://pubmed.ncbi.nlm.nih.gov/15766270/) | *Kinetics of PSorn-resistant L-ornithine transcarbamylase* | Phaseolotoxin/PSorn is a 1.6 pM TS inhibitor; OTCase inhibition → arginine auxotrophy — Finding 7 |
| [26256666](https://pubmed.ncbi.nlm.nih.gov/26256666/) | *ArgK dual role in phaseolotoxin producers* | Phaseolotoxin inhibits housekeeping OTCase ArgF, inducing arginine auxotrophy; ArgK is the resistant replacement — Finding 7 |
| [16741992](https://pubmed.ncbi.nlm.nih.gov/16741992/) | *N-acetylornithine transcarbamoylase from Xanthomonas* | Contrasting specificity (AOTCase) helps distinguish ArgF as a free-ornithine OTCase — Finding 5 |
| [16704984](https://pubmed.ncbi.nlm.nih.gov/16704984/) | *N-succinyl-L-ornithine transcarbamylase in Bacteroides* | Contrasting specificity (SOTCase); argF' disruption → arginine auxotrophy underscores pathway essentiality — Findings 5, 7 |
| [23056465](https://pubmed.ncbi.nlm.nih.gov/23056465/) | *argK expression depends on phtABC* | Confirms phaseolotoxin inhibits OCTase and causes an arginine requirement — Finding 7 |
| [21527339](https://pubmed.ncbi.nlm.nih.gov/21527339/) | *Pht cluster regulation by GacS/GacA* | Confirms phaseolotoxin inhibits the OTCase of arginine biosynthesis — Finding 7 |
| [17620711](https://pubmed.ncbi.nlm.nih.gov/17620711/) | *Catabolic OTC from L. hilgardii (crystallization)* | Reinforces the anabolic/catabolic OTCase distinction; uses P. aeruginosa catabolic OTC (1dxh) as MR model — Findings 2, 3 |

### Supporting context on the two-OTCase paradigm

The *P. aeruginosa* anabolic/catabolic OTCase dichotomy ([PMID: 8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/)) is the anchor for interpreting the *P. putida* genome, which likewise encodes two EC 2.1.3.3 enzymes (Finding 9). The catabolic branch is tied to arginine degradation (arginine deiminase pathway), which is metabolically and regulatorily separate from ArgF's biosynthetic role. This clean separation removes any ambiguity about PP_1079's function.

### Convergent evidence for essentiality

Multiple, mechanistically distinct lines converge on the essentiality of the anabolic OTCase reaction: (i) the picomolar transition-state inhibitor phaseolotoxin causes arginine auxotrophy in target cells ([PMID: 15766270](https://pubmed.ncbi.nlm.nih.gov/15766270/), [PMID: 26256666](https://pubmed.ncbi.nlm.nih.gov/26256666/)); (ii) toxin-producing bacteria require a dedicated resistant OTCase (ArgK) to survive their own toxin ([PMID: 26256666](https://pubmed.ncbi.nlm.nih.gov/26256666/)); and (iii) genetic disruption of the ornithine-transcarbamylase gene in a divergent system (*Bacteroides argF'*) renders the bacterium auxotrophic for arginine ([PMID: 16704984](https://pubmed.ncbi.nlm.nih.gov/16704984/)). These independently establish that the ornithine → citrulline step is a non-redundant, essential node for arginine prototrophy.

---

## Limitations and Knowledge Gaps

1. **No direct enzymological data on the *P. putida* KT2440 ArgF protein itself.** The functional assignment rests on (a) high-confidence UniProt curation of Q88NX4, (b) direct sequence-motif analysis of the Q88NX4 sequence, and (c) extensive biochemical/structural characterization of orthologs (human OTC, *E. coli* ArgI/ArgF, *P. aeruginosa* ArgF/ArcB). No published kinetic constants (Km, kcat), crystal structure, or in vitro assay of the specific PP_1079 gene product were located. The inference is strong by homology but not experimentally verified for this exact protein.

2. **Regulatory detail is extrapolated across species.** The ArgR repression of *argF* is directly demonstrated in *P. syringae* and reported for *P. aeruginosa*; its application to *P. putida* PP_1079 is by conservation of the arginine regulon, not by direct measurement in KT2440.

3. **Localization is annotation-based.** The cytoplasmic assignment follows from GO curation and from the absence of a signal peptide/transmembrane segment in the sequence. This is highly reliable for a family of soluble metabolic enzymes but has not been confirmed experimentally (e.g., by fractionation) for KT2440 ArgF.

4. **Quaternary structure inferred, not measured.** The homotrimeric, non-cooperative anabolic assembly is assigned by homology to characterized anabolic OTCases; the oligomeric state of PP_1079 has not been directly determined.

5. **Substrate specificity boundaries.** While motif analysis strongly supports free-L-ornithine specificity (excluding acetyl-/succinyl-ornithine variants), the enzyme's activity toward closely related amines (e.g., putrescine, lysine) has not been experimentally excluded for this protein — though the family and motifs make cross-reactivity unlikely.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_1079, express and purify the His-tagged protein, and measure kcat and Km for carbamoyl phosphate and L-ornithine, plus the reverse reaction, to confirm the anabolic (non-cooperative, Michaelis-Menten) kinetic signature and directionality predicted from ArgF orthologs.

2. **Genetic essentiality / auxotrophy test.** Construct a clean PP_1079 deletion in *P. putida* KT2440 and test for arginine auxotrophy on minimal medium ± arginine. Complementation with the wild-type gene should restore prototrophy. This directly confirms the non-redundant biosynthetic role in the native organism and distinguishes it from PP_1000.

3. **Substrate-specificity panel.** Assay the purified enzyme against L-ornithine versus N-acetyl-L-ornithine, N-succinyl-L-ornithine, putrescine, and L-aspartate to experimentally confirm free-L-ornithine specificity implied by the HCLP/SMG motifs.

4. **Oligomeric state and structure.** Determine the quaternary structure (size-exclusion chromatography / SEC-MALS) and, ideally, solve the crystal or cryo-EM structure — with and without the transition-state analog N-phosphonacetyl-L-ornithine (PALO) or phaseolotoxin — to visualize the ordered binding and SMG-loop closure directly in the *P. putida* enzyme.

5. **ArgR regulation in KT2440.** Verify ArgR-dependent repression of PP_1079 directly in *P. putida* via reporter fusions and RT-qPCR under arginine-replete versus -limited conditions, and by ArgR EMSA on the *argF* promoter.

6. **Phaseolotoxin sensitivity.** Test whether *P. putida* ArgF is inhibited by phaseolotoxin/PSorn (as expected for a housekeeping OTCase) to confirm mechanistic conservation and to benchmark inhibitor potency against the *E. coli* ArgI 1.6 pM Kd.

---

## Conclusion

All available evidence — UniProt curation, direct sequence-motif analysis of Q88NX4, the genome-level two-OTCase organization of *P. putida* KT2440, and a coherent body of biochemical, structural, and regulatory literature from *Pseudomonas* and orthologous systems — converges on a single, confident conclusion. **argF (PP_1079, Q88NX4) is the anabolic ornithine carbamoyltransferase of *Pseudomonas putida* KT2440**: a soluble cytoplasmic homotrimeric enzyme (EC 2.1.3.3) that carbamoylates L-ornithine to L-citrulline in the committed sixth step of *de novo* L-arginine biosynthesis, using an ordered two-domain mechanism with an active-site cysteine charge relay and SMG-loop closure, under ArgR feedback repression, and essential and non-redundant for arginine prototrophy. It is genomically and functionally distinct from the organism's separate catabolic OTCase paralog, PP_1000/Q88P53.


## Artifacts

- [OpenScientist final report](argF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33084979
2. PMID:15150254
3. PMID:8617277
4. PMID:9275160
5. PMID:9852088
6. PMID:11237854
7. PMID:15766270
8. PMID:26256666
9. PMID:16704984