---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:36:46.149969'
end_time: '2026-07-11T17:50:28.150974'
duration_seconds: 822.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mdh
  gene_symbol: mdh
  uniprot_accession: Q88Q44
  protein_description: 'RecName: Full=Probable malate dehydrogenase {ECO:0000305};
    EC=1.1.1.37 {ECO:0000250|UniProtKB:P61889};'
  gene_info: Name=mdh; OrderedLocusNames=PP_0654;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the LDH/MDH superfamily. .
  protein_domains: L-lactate/malate_DH. (IPR001557); Lactate/malate_DH_C. (IPR022383);
    Lactate/malate_DH_N. (IPR001236); Lactate_DH/Glyco_Ohase_4_C. (IPR015955); Malate_DH_type3.
    (IPR011275)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mdh-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mdh-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q44
- **Protein Description:** RecName: Full=Probable malate dehydrogenase {ECO:0000305}; EC=1.1.1.37 {ECO:0000250|UniProtKB:P61889};
- **Gene Information:** Name=mdh; OrderedLocusNames=PP_0654;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the LDH/MDH superfamily. .
- **Key Domains:** L-lactate/malate_DH. (IPR001557); Lactate/malate_DH_C. (IPR022383); Lactate/malate_DH_N. (IPR001236); Lactate_DH/Glyco_Ohase_4_C. (IPR015955); Malate_DH_type3. (IPR011275)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mdh" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mdh' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mdh** (gene ID: mdh, UniProt: Q88Q44) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *mdh* (Q88Q44 / PP_0654) — NAD-dependent Malate Dehydrogenase of *Pseudomonas putida* KT2440

## Summary

The gene **mdh** (UniProt **Q88Q44**; ordered locus **PP_0654**) of *Pseudomonas putida* KT2440 encodes a **cytoplasmic, NAD⁺-dependent malate dehydrogenase (MDH; EC 1.1.1.37)**. Its primary function is to catalyze the **reversible, NAD⁺-dependent oxidation of L-(S)-malate to oxaloacetate**, the final oxidative step of the tricarboxylic acid (TCA) cycle, coupled to the reduction of NAD⁺ to NADH. This is a core, house-keeping reaction of central carbon metabolism, and the enzyme is a member of the ubiquitous **LDH/MDH superfamily**, specifically the **type-3 (bacterial/archaeal) MDH subfamily** with the classic bilobal fold — an N-terminal Rossmann NAD-binding domain and a C-terminal α+β substrate-binding/dimerization domain.

Multiple lines of evidence converge on this assignment. UniProt annotates Q88Q44 as a probable malate dehydrogenase with the TCA-cycle and NAD keywords, and the InterPro domain architecture (IPR001557, IPR001236, IPR022383, IPR011275, IPR015955) places it squarely in the malate/lactate dehydrogenase fold with the type-3 MDH signature. A global sequence alignment against the biochemically characterized *E. coli* MDH (P61889, the ECO:0000250 annotation anchor) shows **34.8 % identity** with **complete conservation of the catalytic and substrate-binding machinery**: the proton-acceptor histidine and a substrate-carboxylate-binding arginine triad, including the specificity-determining active-site loop arginine that discriminates the C4 dicarboxylate (malate/oxaloacetate) from the C3 substrate (lactate/pyruvate) of the homologous lactate dehydrogenases.

Functionally, the enzyme operates as a **soluble homodimer in the cytoplasm** (bacteria lack organelles; there is no signal peptide or transmembrane segment). It is distinct from the unrelated membrane-associated, FAD-dependent malate:quinone oxidoreductase (MQO, EC 1.1.99.16), which performs the same net chemistry but feeds electrons directly into the quinone pool. Because the reaction is freely reversible, *mdh* supports both directions of flux: in the **oxidative TCA direction** it regenerates oxaloacetate for citrate synthase and supplies cytosolic NADH to the respiratory chain, while in the **reductive direction** it supports oxaloacetate reduction for redox balancing and **anaplerotic/gluconeogenic** malate formation. In the closely related Gammaproteobacterium *E. coli*, deletion of the orthologous NAD-MDH severely impairs growth on several substrates — establishing that this enzyme class, rather than MQO, is the physiologically dominant malate-oxidizing activity in this lineage, which includes *P. putida*.

## Gene Identity Verification

The target identity was verified against every available identifier, and **all lines of evidence are mutually consistent** — there is no ambiguity in this case:

- **Gene symbol vs. protein description:** the symbol *mdh* is the standard symbol for malate dehydrogenase and matches the UniProt description "Probable malate dehydrogenase, EC 1.1.1.37."
- **Organism:** UniProt Q88Q44 organism is *Pseudomonas putida* KT2440 (PSEPK), exactly the target strain.
- **Family/domains:** the InterPro domains (IPR001557, IPR001236, IPR022383, IPR011275, IPR015955) and the LDH/MDH superfamily assignment align with the malate dehydrogenase literature retrieved.

No conflicting literature for a different gene with the same symbol in a different organism affected the analysis. The report proceeds with high confidence in the identity.

---

## Key Findings

### F001 — *mdh* encodes NAD-dependent malate dehydrogenase (EC 1.1.1.37) catalyzing reversible L-malate ⇌ oxaloacetate

The core identity of the gene product is firmly established. UniProt entry Q88Q44 assigns gene *mdh*, ordered locus name PP_0654, the description "Probable malate dehydrogenase," EC number 1.1.1.37, and the organism *Pseudomonas putida* KT2440 — matching the target identity exactly. The canonical reaction catalyzed by MDH is the **reversible NAD⁺-dependent interconversion of L-malate and oxaloacetate**. This is corroborated by a comprehensive 2024 review of MDH catalytic mechanism and kinetics ([PMID: 38721782](https://pubmed.ncbi.nlm.nih.gov/38721782/)), which states plainly that the enzyme "catalyzes the reversible NAD⁺-dependent reduction of L-malate to oxaloacetate."

The family assignment is fully consistent with this catalytic role. Q88Q44 carries the InterPro signatures of the LDH/MDH superfamily — L-lactate/malate_DH (IPR001557), the N-terminal Lactate/malate_DH_N domain (IPR001236), the C-terminal Lactate/malate_DH_C domain (IPR022383), and, critically, the Malate_DH_type3 signature (IPR011275). Together, the database annotation and the canonical enzymology define the reaction:

```
(S)-malate + NAD⁺  ⇌  oxaloacetate + NADH + H⁺        (EC 1.1.1.37)
```

### F002 — Substrate specificity is set by an active-site loop arginine (Arg102), distinguishing MDH from lactate dehydrogenase

MDHs and lactate dehydrogenases (LDHs) are homologous core-metabolic enzymes that **share a common fold and catalytic mechanism yet possess strict specificity for their respective substrates** ([PMID: 24966208](https://pubmed.ncbi.nlm.nih.gov/24966208/); [PMID: 31301348](https://pubmed.ncbi.nlm.nih.gov/31301348/)). The molecular basis of this discrimination is remarkably economical: **a single residue in the active-site loop governs substrate specificity — an arginine (Arg102) in MDHs versus a glutamine (Gln102) in LDHs** (Boucher et al., [PMID: 24966208](https://pubmed.ncbi.nlm.nih.gov/24966208/)). The arginine provides a positively charged contact for the second (C4) carboxylate of the dicarboxylic substrate malate/oxaloacetate, whereas the neutral glutamine in LDHs accommodates the smaller, mono-carboxylate lactate/pyruvate.

This principle is directly relevant to Q88Q44 because it provides a structural rule for inferring substrate selectivity from sequence. The 2024 review further notes that mutations in and around the substrate-enclosing active-site loop can alter substrate/cosubstrate specificity ([PMID: 38721782](https://pubmed.ncbi.nlm.nih.gov/38721782/)), underscoring that this loop is the decisive specificity element.

### F003 — Catalytic and substrate-binding residues are fully conserved in Q88Q44 (34.8 % identity to characterized *E. coli* MDH)

A global Needleman–Wunsch alignment of Q88Q44 (278 aa) against its ECO:0000250 annotation anchor, the biochemically characterized *E. coli* MDH P61889 (312 aa), gives **34.8 % identity over 270 aligned positions**. More important than the overall identity is that the **entire MDH catalytic constellation is conserved** at the aligned positions:

| Functional role | Q88Q44 residue | *E. coli* MDH (P61889) equivalent |
|---|---|---|
| Catalytic proton acceptor | His144 | His177 |
| Substrate-carboxylate arginine triad | Arg51 / Arg57 / Arg120 | Arg81 / Arg87 / Arg153 |
| Additional substrate/cofactor contacts | Asn64, Ser88, Asn89 | Asn94, Thr118, Asn119 |

UniProt lists His144 as the active-site proton acceptor and these positions as binding sites. The substrate-binding **Arg120** (corresponding to *E. coli* Arg153) is the second-carboxylate/specificity arginine that discriminates the C4 dicarboxylate malate/oxaloacetate from the C3 lactate/pyruvate. Because MDH and LDH share fold and mechanism but differ in specificity ([PMID: 24966208](https://pubmed.ncbi.nlm.nih.gov/24966208/)), the conservation of the full arginine constellation is strong sequence-based evidence that Q88Q44 is a bona fide malate — not lactate — dehydrogenase, catalytically equivalent to the well-studied enteric enzyme.

### F004 — *mdh* functions in the cytoplasm as the TCA-cycle malate→oxaloacetate step

UniProt Q88Q44 carries the keywords "Tricarboxylic acid cycle" and "NAD," with the FUNCTION line "Catalyzes the reversible oxidation of malate to oxaloacetate" and the catalytic activity (S)-malate + NAD⁺ = oxaloacetate + NADH + H⁺ (EC 1.1.1.37). As a soluble bacterial NAD-dependent MDH with **no signal peptide or transmembrane segment**, it necessarily operates in the **cytoplasm** — bacteria have no membrane-bound organelles, and MDHs are canonically soluble cytoplasmic enzymes ([PMID: 38721782](https://pubmed.ncbi.nlm.nih.gov/38721782/): "MDH ... plays vital roles in the cytoplasm and various organelles").

In the specific physiological context of *P. putida* KT2440, the TCA cycle forms part of a tightly regulated, transcriptionally invariant central carbon metabolism, while glucose is catabolized primarily through the **Entner–Doudoroff** pathway rather than the classical Embden–Meyerhof–Parnas (EMP) glycolysis (Sudarsan et al., [PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/): "the canonical Entner-Doudoroff and EMP pathways sensu stricto are not a part of central carbon metabolism in P. putida"). Within this network, *mdh* performs the last oxidative step of the TCA cycle, regenerating oxaloacetate to condense with acetyl-CoA at citrate synthase.

### F005 — Q88Q44 is a type-3 MDH with a two-domain architecture: N-terminal Rossmann NAD-binding fold + C-terminal α+β substrate domain

InterPro classifies the diagnostic signature **IPR011275 "Malate dehydrogenase, type 3"** as encompassing "bacterial and archaeal malate dehydrogenases, which convert malate into oxaloacetate in the citric acid cycle," a group defined by "the critical residues which discriminate malate dehydrogenase from lactate dehydrogenase." The enzyme adopts the canonical LDH/MDH **bilobal fold**: the N-terminal domain (IPR001236) is a **Rossmann-type dinucleotide (NAD)-binding fold**, and the C-terminal domain (IPR022383; with IPR015955 describing the C-terminal α+β region) provides substrate binding and dimerization. The sequence begins MDVQGELAQGKALDVWQ…, consistent with an N-terminal dinucleotide-binding lobe. This architecture explains the mechanism: NAD⁺ binds in the Rossmann lobe, malate/oxaloacetate binds in the C-terminal lobe, and catalysis proceeds via hydride transfer to/from the nicotinamide C4 with the conserved histidine acting as the general acid/base.

### F006 — Q88Q44 is the cytoplasmic NAD-MDH, distinct from membrane MQO, and physiologically dominant for malate oxidation in Gammaproteobacteria

Bacteria can oxidize L-malate to oxaloacetate by **two unrelated enzymes**: the cytoplasmic NAD-dependent MDH (EC 1.1.1.37) and the membrane-associated, FAD-dependent **malate:quinone oxidoreductase (MQO; EC 1.1.99.16; gene *mqo*/*yojH*)**, which donates electrons directly to quinones of the electron-transport chain (van der Rest et al., [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/): "Oxidation of malate to oxaloacetate in Escherichia coli can be catalyzed by two enzymes: the well-known NAD-dependent malate dehydrogenase (MDH; EC 1.1.1.37) and the membrane-associated malate:quinone-oxidoreductase (MQO; EC 1.1.99.16)"; Kather et al., [PMID: 10809701](https://pubmed.ncbi.nlm.nih.gov/10809701/)). Q88Q44 is annotated EC 1.1.1.37 (NAD-dependent) and lacks any FAD-binding or membrane features, unambiguously identifying it as **the cytoplasmic NAD-MDH, not MQO**.

Crucially, gene-deletion experiments in *E. coli* establish which enzyme dominates physiologically: "a defined deletion of the *mdh* gene led to severely decreased rates of growth on several substrates. Deletion of the *mqo* gene did not produce a distinguishable effect on the growth rate" ([PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/)). This demonstrates that in this Gammaproteobacterial lineage — which includes *P. putida* — the **NAD-MDH is the physiologically dominant malate-oxidizing enzyme** and is important for growth. Notably, the picture differs in the Actinobacterium *Corynebacterium glutamicum*, where MQO is dominant and an *mdh* deletion alone shows no phenotype ([PMID: 11092846](https://pubmed.ncbi.nlm.nih.gov/11092846/)) — highlighting that the *E. coli* result is the more appropriate model for *P. putida*.

### F007 — Q88Q44 is a homodimeric NAD(H)-dependent MDH contributing cytosolic NADH to respiration and supporting reversible anaplerotic/gluconeogenic flux

Within the LDH/MalDH superfamily, the canonical LDHs and the LDH-like group of malate dehydrogenases are "primarily tetrameric enzymes that diverged from a common ancestor" ([PMID: 31301348](https://pubmed.ncbi.nlm.nih.gov/31301348/)), whereas the **non-LDH-like (type-3 / "mitochondrial-like") MDH group — to which Q88Q44 belongs, and which includes *E. coli* MDH and mitochondrial MDH — forms homodimers**. Characterized NAD-MDHs of this class are indeed homodimers in solution (e.g., plastidial NAD-MDH shown by gel filtration and glutaraldehyde cross-linking, [PMID: 26095832](https://pubmed.ncbi.nlm.nih.gov/26095832/)). Q88Q44 is therefore predicted to be a **homodimer**.

Directionally, because the reaction (S)-malate + NAD⁺ ⇌ oxaloacetate + NADH + H⁺ is freely reversible ([PMID: 38721782](https://pubmed.ncbi.nlm.nih.gov/38721782/): "It catalyzes the reversible NAD⁺-dependent reduction of L-malate to oxaloacetate"), the enzyme performs two physiological roles. In the **oxidative TCA direction** it generates cytosolic NADH, which is reoxidized by the respiratory NADH dehydrogenases feeding the electron-transport chain. In the **reductive direction** it supports oxaloacetate reduction for redox balancing and **gluconeogenesis**. KM values of MDH isozymes are generally tuned to physiological substrate concentrations ([PMID: 38721782](https://pubmed.ncbi.nlm.nih.gov/38721782/)), consistent with an enzyme poised to operate near equilibrium in either direction depending on cellular demand.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent, well-supported model of *mdh* (PP_0654) as a canonical cytoplasmic NAD-dependent malate dehydrogenase performing the terminal oxidative step of the TCA cycle in *P. putida* KT2440.

**Catalytic cycle and role in the TCA cycle:**

```
         acetyl-CoA
             │  (citrate synthase)
             ▼
   oxaloacetate ──────────────► citrate
        ▲                          │
        │                          ▼
  ┌─────┴──────┐              (TCA cycle)
  │  mdh /     │                    │
  │  PP_0654   │  NAD⁺→NADH         ▼
  │ (NAD-MDH,  │◄───────────── L-malate
  │  cytoplasm)│
  └────────────┘
        │
   NADH → respiratory chain (NADH dehydrogenases) → proton-motive force → ATP
```

The enzyme takes L-malate, abstracts a hydride from its C2 carbon to NAD⁺ (yielding NADH), with the conserved active-site **His144** acting as the general base that deprotonates the substrate hydroxyl; the resulting oxaloacetate is stabilized by the **arginine triad (Arg51/Arg57/Arg120)**. Arg120 in particular anchors the C4 carboxylate that defines dicarboxylate (malate/OAA) specificity, the feature that distinguishes MDH from its LDH cousins. The oxaloacetate produced is the obligatory co-substrate for citrate synthase, closing the TCA cycle, while the NADH produced is oxidized by the respiratory chain to drive ATP synthesis.

**Two malate-oxidizing enzymes, one dominant:**

| Property | NAD-MDH (Q88Q44, *mdh*/PP_0654) | MQO (*mqo*/*yojH*) |
|---|---|---|
| EC number | 1.1.1.37 | 1.1.99.16 |
| Cofactor | NAD⁺ (soluble) | FAD (membrane-bound) |
| Electron acceptor | NAD⁺ → NADH | quinone pool directly |
| Localization | Cytoplasm | Membrane-associated |
| Reversibility | Reversible (TCA + gluconeogenic) | Effectively irreversible (oxidative) |
| Oligomeric state | Homodimer (type-3) | — |
| Phenotype of deletion in *E. coli* | Severe growth defect | No distinguishable effect |

The comparison makes the physiological logic explicit: *P. putida*, like *E. coli*, relies on the **reversible NAD-MDH** as its principal malate/oxaloacetate interconverting enzyme. Reversibility is the key functional advantage — it lets the same enzyme serve TCA-cycle oxidation when carbon flows toward respiration, and oxaloacetate reduction (malate formation) when the cell runs gluconeogenesis or needs to balance the NADH/NAD⁺ pool. This dual capacity is especially relevant in *P. putida*, a metabolically versatile soil organism whose central carbon metabolism must accommodate diverse carbon sources (sugars via Entner–Doudoroff, plus organic and aromatic acids that feed the TCA cycle at oxaloacetate and other nodes).

**Structural summary:** Q88Q44 is a two-domain, Rossmann-fold NAD-binding + α/β substrate-binding homodimer of the type-3 MDH subfamily, cytoplasmic, ~278 residues, with a fully conserved catalytic and specificity apparatus. Every layer of evidence — database annotation, domain architecture, residue-level sequence conservation against a characterized ortholog, family-level oligomeric rules, and comparative gene-deletion physiology — is mutually consistent.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [38721782](https://pubmed.ncbi.nlm.nih.gov/38721782/) | *Catalytic mechanism and kinetics of malate dehydrogenase* | Establishes the canonical reversible NAD⁺-dependent malate⇌oxaloacetate reaction (F001, F007), cytoplasmic localization (F004), active-site loop role in specificity (F002), and KM tuning to physiological substrate levels (F007). |
| [24966208](https://pubmed.ncbi.nlm.nih.gov/24966208/) | *An atomic-resolution view of neofunctionalization in the evolution of apicomplexan lactate dehydrogenases* | Identifies the active-site loop Arg102 (MDH) vs Gln102 (LDH) as the specificity determinant, and that MDH/LDH share fold and mechanism but differ in specificity (F002, F003). |
| [31301348](https://pubmed.ncbi.nlm.nih.gov/31301348/) | *The archaeal LDH-like malate dehydrogenase from Ignicoccus islandicus…* | Distinguishes tetrameric LDH-like MalDHs from the dimeric type-3/mitochondrial-like MDH group to which Q88Q44 belongs (F007), and reiterates strict substrate specificity (F002). |
| [11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/) | *Functions of the membrane-associated and cytoplasmic malate dehydrogenases in the citric acid cycle of E. coli* | Defines the two malate-oxidizing enzymes (NAD-MDH vs MQO) and provides gene-deletion evidence that NAD-MDH is physiologically dominant in a Gammaproteobacterium related to *P. putida* (F006). |
| [10809701](https://pubmed.ncbi.nlm.nih.gov/10809701/) | *Another unusual type of citric acid cycle enzyme in H. pylori: the malate:quinone oxidoreductase* | Documents the FAD-dependent, membrane-associated MQO as an alternative malate oxidase feeding quinones, contrasting with the NAD-MDH class of Q88Q44 (F006). |
| [11092846](https://pubmed.ncbi.nlm.nih.gov/11092846/) | *Functions of … malate dehydrogenases in the citric acid cycle of C. glutamicum* | Contrasting case: in an Actinobacterium, MQO dominates and *mdh* deletion has no phenotype — underscores that the *E. coli* result is the correct model for *P. putida* (F006, context). |
| [26095832](https://pubmed.ncbi.nlm.nih.gov/26095832/) | *Purification and characterization of the plastid-localized NAD-dependent MDH from Arabidopsis* | Empirical example of an NAD-MDH that is a homodimer in solution with submillimolar KM values, supporting the homodimer/kinetics inference (F007). |
| [24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/) | *The functional structure of central carbon metabolism in P. putida KT2440* | Establishes the pathway context — Entner–Doudoroff rather than EMP glycolysis, tightly regulated TCA cycle — in which *mdh* operates (F004). |

Supporting/contextual literature reviewed includes structural studies of human mitochondrial MDH2 (phosphate binding and active conformation, [PMID: 36139014](https://pubmed.ncbi.nlm.nih.gov/36139014/)), enzyme promiscuity/HGT in metabolic evolution ([PMID: 31858709](https://pubmed.ncbi.nlm.nih.gov/31858709/)), and *P. putida* systems-level metabolic studies ([PMID: 30936206](https://pubmed.ncbi.nlm.nih.gov/30936206/), [PMID: 41176845](https://pubmed.ncbi.nlm.nih.gov/41176845/)). None of these contradict the assignment; they reinforce the enzyme's placement in central carbon metabolism.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88Q44 itself.** The functional assignment rests on (a) UniProt/InterPro annotation, (b) sequence conservation against the characterized *E. coli* ortholog (34.8 % identity), and (c) family-level generalizations. There is, to our knowledge, no published purification, kinetic measurement (kcat, KM for malate/OAA/NAD⁺/NADH), or crystal structure of the specific *P. putida* KT2440 PP_0654 protein. The enzyme is annotated "Probable."

2. **Oligomeric state is inferred, not measured.** The homodimer prediction is based on subfamily membership (type-3, non-LDH-like), not on gel filtration or crystallography of Q88Q44.

3. **Directional/kinetic preference in vivo is unquantified.** While the reaction is thermodynamically reversible, the actual net flux direction in *P. putida* under given growth conditions (respiratory vs gluconeogenic) has not been directly measured for this enzyme.

4. **Gene-essentiality/phenotype data are extrapolated from *E. coli*.** The severe growth defect of Δ*mdh* was demonstrated in *E. coli*, not in *P. putida*. Although both are Gammaproteobacteria, *P. putida* has distinctive central metabolism (Entner–Doudoroff dominance), so a direct *P. putida* Δ*mdh* phenotype would strengthen the physiological claim.

5. **Possible redundancy with MQO in *P. putida* is uncharacterized.** *P. putida* likely also encodes an MQO; the relative contributions of PP_0654 (NAD-MDH) and any MQO to malate oxidation in this organism have not been experimentally partitioned.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymology.** Clone PP_0654, express in *E. coli*, purify, and measure steady-state kinetics in both directions (malate oxidation and OAA reduction), determining kcat and KM for malate, oxaloacetate, NAD⁺, and NADH, and confirming strict NAD (not NADP) preference. This would convert the "Probable" annotation to experimentally validated (evidence code EXP).

2. **Oligomeric state and structure.** Determine the oligomeric state by size-exclusion chromatography and/or SEC-MALS, and pursue a crystal or cryo-EM structure (ideally with NAD and a substrate analogue) to confirm the type-3 dimeric fold and the roles of His144 and the Arg51/Arg57/Arg120 triad.

3. **Targeted gene deletion in *P. putida* KT2440.** Construct a clean Δ*PP_0654* mutant and assay growth on TCA-feeding substrates (e.g., succinate, malate, aromatic-derived intermediates that funnel to oxaloacetate) versus glucose. Compare with a Δ*mqo* single mutant and the Δ*mdh* Δ*mqo* double mutant to partition malate-oxidizing activity and test whether the *E. coli*-like dominance of NAD-MDH holds in *P. putida*.

4. **Site-directed mutagenesis of the specificity arginine (Arg120).** Mutate Arg120→Gln and test whether substrate preference shifts toward pyruvate/lactate, experimentally validating the MDH-vs-LDH specificity determinant in this specific enzyme.

5. **¹³C metabolic flux analysis.** Use isotope tracing under respiratory and gluconeogenic conditions to measure the net directional flux through the malate/oxaloacetate node and quantify the enzyme's contribution to cytosolic NADH generation versus anaplerotic malate formation.

---

## Conclusion

All available evidence — UniProt/InterPro annotation, the type-3 MDH domain signature, 34.8 % identity with complete conservation of the catalytic His and specificity arginine triad relative to characterized *E. coli* MDH, family-level oligomeric rules, and comparative gene-deletion physiology in Gammaproteobacteria — consistently identifies **Q88Q44 / PP_0654 (*mdh*) as a cytoplasmic, homodimeric, NAD⁺-dependent malate dehydrogenase (EC 1.1.1.37)** performing the terminal oxidative step of the TCA cycle in *P. putida* KT2440. It catalyzes the reversible oxidation of L-(S)-malate to oxaloacetate, regenerating oxaloacetate for citrate synthase and supplying NADH to the respiratory chain, while its reversibility supports anaplerotic/gluconeogenic flux. It is distinct from, and physiologically dominant over, the membrane FAD-dependent MQO in this lineage. The gene symbol, organism, and protein family are all internally consistent — this is the correct target, and no ambiguity was encountered.


## Artifacts

- [OpenScientist final report](mdh-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mdh-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:38721782
2. PMID:24966208
3. PMID:31301348
4. PMID:24951791
5. PMID:11092847
6. PMID:10809701
7. PMID:11092846
8. PMID:26095832
9. PMID:36139014
10. PMID:31858709
11. PMID:30936206
12. PMID:41176845