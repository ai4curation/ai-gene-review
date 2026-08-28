---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T01:44:13.825894'
end_time: '2026-08-13T02:00:55.554472'
duration_seconds: 1001.73
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: gshB
  gene_symbol: gshB
  uniprot_accession: Q88D35
  protein_description: 'RecName: Full=Glutathione synthetase {ECO:0000255|HAMAP-Rule:MF_00162};
    EC=6.3.2.3 {ECO:0000255|HAMAP-Rule:MF_00162}; AltName: Full=GSH synthetase {ECO:0000255|HAMAP-Rule:MF_00162};
    Short=GSH-S {ECO:0000255|HAMAP-Rule:MF_00162}; Short=GSHase {ECO:0000255|HAMAP-Rule:MF_00162};
    AltName: Full=Glutathione synthase {ECO:0000255|HAMAP-Rule:MF_00162};'
  gene_info: Name=gshB {ECO:0000255|HAMAP-Rule:MF_00162}; OrderedLocusNames=PP_4993;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the prokaryotic GSH synthase family.
  protein_domains: ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); Glut_synth_pro.
    (IPR006284); GSHS_ATP-bd. (IPR004218); GSHS_N. (IPR004215)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: gshB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: gshB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D35
- **Protein Description:** RecName: Full=Glutathione synthetase {ECO:0000255|HAMAP-Rule:MF_00162}; EC=6.3.2.3 {ECO:0000255|HAMAP-Rule:MF_00162}; AltName: Full=GSH synthetase {ECO:0000255|HAMAP-Rule:MF_00162}; Short=GSH-S {ECO:0000255|HAMAP-Rule:MF_00162}; Short=GSHase {ECO:0000255|HAMAP-Rule:MF_00162}; AltName: Full=Glutathione synthase {ECO:0000255|HAMAP-Rule:MF_00162};
- **Gene Information:** Name=gshB {ECO:0000255|HAMAP-Rule:MF_00162}; OrderedLocusNames=PP_4993;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the prokaryotic GSH synthase family.
- **Key Domains:** ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); Glut_synth_pro. (IPR006284); GSHS_ATP-bd. (IPR004218); GSHS_N. (IPR004215)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "gshB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'gshB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **gshB** (gene ID: gshB, UniProt: Q88D35) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *gshB* (Glutathione Synthetase, Q88D35) in *Pseudomonas putida* KT2440

**UniProt:** Q88D35 · **Gene:** *gshB* · **Locus:** PP_4993 · **EC:** 6.3.2.3
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440) — PSEPK
**Protein:** 317 aa, ~35.3 kDa soluble subunit; predicted **homotetramer** by homology to *E. coli* GshB (no signal peptide or transmembrane segment)

---

## Summary

The gene **gshB** (locus **PP_4993**; UniProt **Q88D35**) of *Pseudomonas putida* KT2440 encodes **glutathione synthetase** (**GSH-S / GSHase**, EC 6.3.2.3), the enzyme that catalyzes the second and final step of glutathione (GSH) biosynthesis. GshB is a cytoplasmic, Mg²⁺/Mn²⁺-dependent C–N (peptide) ligase of the **ATP-grasp superfamily** that joins glycine to the cysteinyl carboxylate of γ-L-glutamyl-L-cysteine (γ-Glu-Cys), consuming one molecule of ATP, to produce the tripeptide thiol glutathione (γ-L-glutamyl-L-cysteinyl-glycine) plus ADP and inorganic phosphate. This is the committed, GSH-completing reaction of a canonical two-enzyme pathway in which the upstream enzyme GshA (glutamate–cysteine ligase, PP_0243) first produces γ-Glu-Cys from L-glutamate and L-cysteine.

Functionally, the physiological purpose of GshB is to supply glutathione — the principal low-molecular-weight cytosolic thiol/redox buffer of Gram-negative bacteria. In *P. putida*, a soil and rhizosphere organism prized for its solvent and stress tolerance, GSH underpins defense against oxidative, solvent, and heavy-metal stress, and feeds specific downstream detoxification systems (glutathione peroxidases/reductase, glutathione S-transferases, and the glyoxalase I–II methylglyoxal-detoxification pathway). GshB is not itself a regulator or effector; it is the biosynthetic gatekeeper that enables this protective downstream chemistry.

The identification is **unambiguous** but the functional call is fundamentally a **high-confidence homology transfer** rather than an organism-specific biochemical characterization. The strongest lines of evidence are: (1) direct UniProt/HAMAP curation under rule MF_00162 assigning EC 6.3.2.3, the reaction, the Mg²⁺/Mn²⁺ cofactor requirement, and the "step 2/2" pathway position; (2) **66.5% amino-acid identity** to the *E. coli* GshB enzyme (P04425), whose 2.0 Å crystal structure and reaction mechanism are experimentally established; (3) conserved ATP-grasp domain signatures (InterPro IPR011761, IPR013815, IPR004218, IPR004215, IPR006284) and mapped active-site residues (ATP-binding region ~152–208; Mg²⁺ coordinated by Glu282 and Asn284); and (4) confirmed presence of the complete pathway, with the upstream partner *gshA* (PP_0243) also encoded in the genome. No primary study has yet characterized the *P. putida* GshB enzyme kinetically/structurally or reported a targeted *gshB* deletion mutant — the principal knowledge gap identified in this investigation.

---

## Key Findings

### F001 — GshB is glutathione synthetase, catalyzing the ATP-dependent final step of GSH biosynthesis

The core identity of the gene product is firmly established. UniProt entry Q88D35 (verified programmatically: 317 amino acids, ~35.3 kDa) assigns **EC 6.3.2.3** and the catalytic reaction:

> **γ-L-glutamyl-L-cysteine + glycine + ATP → glutathione + ADP + phosphate + H⁺**

The cofactor requirement is a divalent metal ion (Mg²⁺ or Mn²⁺), and the pathway annotation is explicit: "glutathione biosynthesis; glutathione from L-cysteine and L-glutamate: **step 2/2**." This places GshB as the terminal enzyme of the canonical two-step route to glutathione.

The two-step architecture is well established in the literature. In the general GSH-biosynthetic scheme, glutathione is made by "two consecutive enzymatic reactions catalyzed by γ-glutamylcysteine synthetase (Gsh1 or GshA) and glutathione synthetase (Gsh2 or GshB)" [PMID: 26377681](https://pubmed.ncbi.nlm.nih.gov/26377681/). Classic bacterial genetics in *E. coli* separated the pathway into two distinct, physically separable enzymes — "recombinant plasmids for gamma-glutamylcysteine synthetase (GSH-I) and glutathione synthetase (GSH-II)" — confirming that the *gshB* product (GSH-II) is a discrete second enzyme distinct from GshA [PMID: 6147339](https://pubmed.ncbi.nlm.nih.gov/6147339/). Both references are fully consistent with the UniProt "step 2/2" annotation for Q88D35. Note that some bacteria instead use a **bifunctional GshF** (γ-GCS + GS in one polypeptide); *P. putida* uses the classical **separate GshA/GshB** arrangement, and Q88D35 is the dedicated monofunctional GS.

### F002 — GshB is an ATP-grasp C–N ligase acting through an acyl-phosphate intermediate

Domain analysis of Q88D35 reveals the signatures of the **ATP-grasp superfamily**: ATP-grasp (IPR011761), ATP_grasp_subdomain_1 (IPR013815), GSHS_ATP-bd (IPR004218), GSHS_N (IPR004215), and Glut_synth_pro (IPR006284), with mapped ATP/substrate-binding sites around residues 152–208 and metal-binding residues at positions 282 and 284.

ATP-grasp enzymes — including D-Ala-D-Ala ligase, glutathione synthetase, biotin carboxylase, and carbamyl phosphate synthetase — share a conserved catalytic strategy and a set of conserved ATP-binding residues (Lys, His, Glu) essential for catalysis [PMID: 11346647](https://pubmed.ncbi.nlm.nih.gov/11346647/). The mechanistic hallmark of this family, when forming C–N (amide) bonds, is **phosphoryl transfer from ATP to a carboxylate substrate to generate a reactive acyl-phosphate intermediate**, which is then attacked by the incoming amine nucleophile. This chemistry is directly documented in the closely related *E. coli* glutathionylspermidine synthetase, where "GSH is likely phosphorylated at one of two GSH-binding sites to form an acylphosphate intermediate," and whose C-terminal domain adopts "a similar fold to the human glutathione synthetase" [PMID: 17124497](https://pubmed.ncbi.nlm.nih.gov/17124497/). Applied to GshB: ATP phosphorylates the cysteinyl carboxylate of γ-Glu-Cys to form γ-glutamyl-cysteinyl-phosphate, and the α-amino group of glycine then displaces phosphate to form the new peptide (amide) bond, releasing GSH, ADP, and Pᵢ. The divalent metal ion positions the ATP phosphates and stabilizes the transition state.

### F003 — GshB acts in the cytoplasm to supply glutathione for redox/oxidative-stress homeostasis

Glutathione is the dominant low-molecular-weight cytoplasmic thiol and redox buffer in Gram-negative bacteria, and its enzymatic synthesis (GshA then GshB) takes place in the cytosol. Q88D35 has no predicted signal peptide and no transmembrane segments (317-aa soluble protein), consistent with a monofunctional cytoplasmic enzyme.

The physiological relevance of this cytosolic redox function is documented in *P. putida* KT2440 itself. Under sub-lethal H₂O₂ challenge, "metabolic network-wide routes for NADPH generation — the metabolic currency that fuels redox-stress quenching mechanisms — were inspected when P. putida KT2440 was challenged with a sub-lethal H₂O₂" [PMID: 33432138](https://pubmed.ncbi.nlm.nih.gov/33432138/), placing GSH/NADPH-based redox-stress quenching squarely in the cytoplasm where GshB-derived GSH operates (NADPH regenerates reduced GSH via glutathione reductase). In the rhizosphere, genomic analysis shows that "the induction of efflux pumps and enzymes for glutathione metabolism indicates that adaptation to adverse conditions and stress (oxidative) response are crucial for bacterial life in this environment" [PMID: 17784941](https://pubmed.ncbi.nlm.nih.gov/17784941/), linking glutathione metabolism directly to the oxidative-stress adaptation that GSH supports.

### F004 — Q88D35 is a close ortholog (66.5% identity) of the crystallographically characterized *E. coli* GshB

A global pairwise Needleman-Wunsch alignment of *P. putida* GshB (Q88D35, 317 aa) against *E. coli* GshB (P04425, 316 aa) yields **210/316 = 66.5% identity** — far above the ~30% threshold generally used to infer confident orthology and function transfer. This means the extensively characterized *E. coli* structure and mechanism can be mapped onto the *P. putida* enzyme with high confidence.

The *E. coli* enzyme has been solved at 2.0 Å resolution: "the enzyme from Escherichia coli is a tetramer with four identical subunits of 316 amino acid residues," each composed of N-terminal, central, and C-terminal domains, and "the ATP molecule is located in the cleft between the central and C-terminal domains" — the defining architecture of the ATP-grasp fold [PMID: 8445637](https://pubmed.ncbi.nlm.nih.gov/8445637/). By homology, *P. putida* GshB is predicted to adopt the same three-domain fold, the same ATP-grasp catalytic cleft, and a comparable homotetrameric assembly.

### F005 — GSH produced by GshB feeds specific detoxification pathways, not only generic buffering

Beyond serving as a bulk redox buffer, glutathione is the required substrate for several defined enzymatic detoxification systems. A well-characterized example is methylglyoxal detoxification (methylglyoxal being a toxic electrophilic glycolysis by-product): "the glutathione-dependent glyoxalase I–II pathway is the primary route of methylglyoxal detoxification, and the glutathione conjugates formed can activate the KefB and KefC potassium channels" [PMID: 9732434](https://pubmed.ncbi.nlm.nih.gov/9732434/). This illustrates a precise, GSH-dependent biochemical circuit downstream of GshB: GSH spontaneously conjugates methylglyoxal to a hemithioacetal, glyoxalase I converts this to S-D-lactoylglutathione, glyoxalase II releases D-lactate and regenerates GSH, and the transient GSH-conjugates gate the KefB/KefC K⁺ channels to acidify the cytoplasm and protect against electrophilic damage. GSH additionally serves as the substrate for glutathione peroxidases, glutathione reductase, glutaredoxins, and glutathione S-transferases operating in the *P. putida* cytoplasm [PMID: 33432138](https://pubmed.ncbi.nlm.nih.gov/33432138/); [PMID: 17107553](https://pubmed.ncbi.nlm.nih.gov/17107553/).

### F006 — *P. putida* KT2440 encodes the complete two-step GSH pathway, with *gshA* and *gshB* unlinked

A UniProt query of *P. putida* KT2440 (taxid 160488) confirms that the upstream enzyme is present: **GshA = Q88R90**, gene *gshA*, locus **PP_0243**, annotated "Glutamate–cysteine ligase" (EC 6.3.2.2), which produces γ-glutamylcysteine — precisely the substrate of GshB. GshB itself is Q88D35 / PP_4993. The two loci (PP_0243 and PP_4993) are far apart on the chromosome, indicating the genes are **not organized in a shared operon** and are independently regulated — the same dispersed arrangement seen in *E. coli*. Functional-residue mapping for Q88D35 places the ATP-binding region at residues 152–208 and the Mg²⁺ coordination at Glu282 and Asn284.

### F007 — The assignment rests on high-confidence homology transfer, not organism-specific biochemistry

Targeted literature searches returned **no primary study** characterizing the *P. putida* KT2440 GshB enzyme kinetically/structurally, nor any targeted *gshB* deletion mutant. Accordingly, the functional annotation is supported by: (1) direct UniProt catalytic/pathway annotation curated under HAMAP rule MF_00162 (evidence code ECO:0000255, i.e., sequence-model-based); (2) 66.5% identity to the crystallographically and biochemically characterized *E. coli* GshB (P04425 / [PMID: 8445637](https://pubmed.ncbi.nlm.nih.gov/8445637/)); (3) conserved ATP-grasp domain signatures and mapped active-site residues (ATP region 152–208; Mg²⁺ at Glu282/Asn284); and (4) demonstrated presence of the complete pathway including the upstream GshA (PP_0243). This is a strong evidentiary base, but the confidence derives from homology and conserved-domain inference rather than a direct assay on the *P. putida* protein.

---

## Mechanistic Model / Interpretation

### The two-step glutathione biosynthetic pathway

```
   L-glutamate + L-cysteine + ATP
              │
              ▼   GshA  (PP_0243, Q88R90; EC 6.3.2.2)  [glutamate–cysteine ligase]
              │   ATP → ADP + Pi
   γ-L-glutamyl-L-cysteine  (γ-Glu-Cys)
              │
              +  glycine + ATP
              │
              ▼   GshB  (PP_4993, Q88D35; EC 6.3.2.3)  [glutathione synthetase]  ◄── TARGET
              │   ATP → ADP + Pi   (via acyl-phosphate intermediate; Mg²⁺/Mn²⁺)
              │
   GLUTATHIONE  (γ-L-glutamyl-L-cysteinyl-glycine, GSH)
              │
              ▼   recycled GSH ⇌ GSSG by glutathione reductase (NADPH-dependent)
```

### Reaction chemistry catalyzed by GshB (ATP-grasp mechanism)

```
Step 1 (phosphoryl transfer):
   γ-Glu-Cys–COO⁻  +  ATP  ──►  γ-Glu-Cys–CO–OPO₃²⁻  +  ADP
        (cysteinyl carboxylate)      (acyl-phosphate intermediate)

Step 2 (nucleophilic amide-bond formation):
   γ-Glu-Cys–CO–OPO₃²⁻  +  H₂N–CH₂–COO⁻ (glycine)  ──►  GSH  +  Pi
```

Both partial reactions occur in the ATP-grasp catalytic cleft between the central and C-terminal domains, with a Mg²⁺ (or Mn²⁺) ion — coordinated in the *P. putida* enzyme by Glu282 and Asn284 — stabilizing the ATP phosphates and the transition state.

### Downstream roles of GshB-derived GSH

```
                        ┌──────────────────────────────────────────┐
                        │   Glutathione (GSH) — cytosolic pool       │
                        └──────────────────────────────────────────┘
                              │            │              │
          ┌───────────────────┘            │              └────────────────────┐
          ▼                                ▼                                   ▼
  Redox buffering /               Methylglyoxal detox                 Xenobiotic / metal
  ROS scavenging                  (glyoxalase I → II;                 detox & tolerance
  (Gpx, Gr, Grx;                  KefB/KefC K⁺ gating)                (GST conjugation;
  NADPH-fueled)                                                       solvent/metal stress)
```

### Localization

All available evidence — the absence of any signal peptide or transmembrane segment in Q88D35, the soluble monofunctional nature of the enzyme, and the cytosolic location of the bacterial GSH-biosynthetic and GSH-utilizing machinery — points to GshB functioning in the **cytoplasm**. GSH itself is synthesized and predominantly retained in the cytosol, where it acts as the cell's chief thiol-redox buffer.

### Comparative summary table

| Property | *P. putida* KT2440 GshB (Q88D35) | *E. coli* GshB (P04425) |
|---|---|---|
| Gene / locus | *gshB* / PP_4993 | *gshB* |
| Length | 317 aa (~35.3 kDa) | 316 aa |
| EC number | 6.3.2.3 | 6.3.2.3 |
| Reaction | γ-Glu-Cys + Gly + ATP → GSH + ADP + Pi | Same |
| Cofactor | Mg²⁺ / Mn²⁺ | Mg²⁺ |
| Fold | ATP-grasp (3 domains; inferred) | ATP-grasp (N, central, C-terminal), 2.0 Å structure |
| Oligomer | Homotetramer (inferred) | Homotetramer (experimental) |
| Sequence identity | — | 66.5% identical to Q88D35 |
| Evidence level | Homology / HAMAP MF_00162 (ECO:0000255) | Experimental crystal structure + biochemistry |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [26377681](https://pubmed.ncbi.nlm.nih.gov/26377681/) | *Three-pathway combination for glutathione biosynthesis in S. cerevisiae* | Defines GshB as glutathione synthetase performing the second of two consecutive GSH-biosynthetic reactions; supports "step 2/2" (F001) |
| [6147339](https://pubmed.ncbi.nlm.nih.gov/6147339/) | *Construction of glutathione-producing strains of E. coli B* | Establishes GSH-II (gshB product) as an enzyme distinct from γ-glutamylcysteine synthetase (GSH-I) in the bacterial pathway (F001) |
| [11346647](https://pubmed.ncbi.nlm.nih.gov/11346647/) | *Site-directed mutagenesis of ATP binding residues of biotin carboxylase* | Places glutathione synthetase in the ATP-grasp superfamily with conserved, catalytically essential ATP-binding residues (F002) |
| [17124497](https://pubmed.ncbi.nlm.nih.gov/17124497/) | *Dual binding sites for translocation catalysis by E. coli glutathionylspermidine synthetase* | Demonstrates the acyl-phosphate intermediate mechanism shared by the glutathione-family ATP-grasp ligases (F002) |
| [8445637](https://pubmed.ncbi.nlm.nih.gov/8445637/) | *Three-dimensional structure of glutathione synthetase from E. coli B at 2.0 Å* | Provides experimental quaternary structure (homotetramer, 316-aa subunits) and ATP-grasp architecture of the ortholog 66.5% identical to Q88D35 (F004) |
| [33432138](https://pubmed.ncbi.nlm.nih.gov/33432138/) | *Reconfiguration of metabolic fluxes in P. putida under sub-lethal oxidative stress* | Shows GSH/NADPH-based redox-stress quenching operates in the P. putida KT2440 cytoplasm — the physiological context of GshB (F003, F005) |
| [17784941](https://pubmed.ncbi.nlm.nih.gov/17784941/) | *Genomic analysis reveals the major driving forces of bacterial life in the rhizosphere* | Links glutathione metabolism to oxidative-stress adaptation in P. putida (F003) |
| [9732434](https://pubmed.ncbi.nlm.nih.gov/9732434/) | *Methylglyoxal production in bacteria: suicide or survival?* | Documents the GSH-dependent glyoxalase I–II methylglyoxal-detox pathway and KefB/KefC gating downstream of GshB (F005) |
| [17107553](https://pubmed.ncbi.nlm.nih.gov/17107553/) | *OxyR regulated KatA, KatB, AhpC in P. putida* | Contextualizes the P. putida antioxidant network (glutathione reductase, glutaredoxins, thioredoxins) that consumes GSH (F005) |

Supporting/contextual literature also reviewed includes solvent-tolerance antioxidant studies in *Pseudomonas* [PMID: 24136354](https://pubmed.ncbi.nlm.nih.gov/24136354/), a glutathione-peroxidase/lignin role in *P. putida* KT2440 [PMID: 41529765](https://pubmed.ncbi.nlm.nih.gov/41529765/), and structural analyses of related ATP-grasp / trypanothione synthetase enzymes [PMID: 18420578](https://pubmed.ncbi.nlm.nih.gov/18420578/), [PMID: 25211225](https://pubmed.ncbi.nlm.nih.gov/25211225/).

### Gene-identity verification

The mandatory identity checks are satisfied: the gene symbol *gshB* matches the protein description (glutathione synthetase); the organism is confirmed as *Pseudomonas putida* KT2440 (locus PP_4993, taxid 160488); and the protein family (prokaryotic GSH synthase family) and ATP-grasp domain signatures align with the literature on the *E. coli* ortholog and the broader ATP-grasp superfamily. No conflicting literature for a different gene bearing the same symbol was encountered. One caution: "gshB" in *Bacillus subtilis* refers to a bifunctional GshAB enzyme — a distinct arrangement that does not apply to the monofunctional *P. putida* enzyme studied here.

---

## Supported vs. Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| Q88D35/*gshB* is glutathione synthetase (EC 6.3.2.3), final step of GSH synthesis | **Supported** | UniProt reaction + pathway; PMID 26377681, 6147339 |
| Enzyme is ATP-grasp C–N ligase using an acyl-phosphate intermediate, Mg²⁺/Mn²⁺-dependent | **Supported** | InterPro domains; PMID 17124497, 11346647 |
| Enzyme acts in the cytoplasm | **Supported** | Soluble protein, no signal/TM; cytosolic GSH biology |
| GSH product serves redox/oxidative-stress homeostasis in *P. putida* | **Supported** | PMID 33432138, 17784941, 17107553 |
| GSH feeds specific detox modules (e.g., glyoxalase methylglyoxal detox) | **Supported** | PMID 9732434 |
| *gshB* is bifunctional (γ-GCS+GS, GshF-type) | **Refuted** | It is monofunctional GS; bifunctional route is a separate GshF (PMID 26377681) |
| Gene symbol ambiguity / wrong-gene risk | **Refuted (no conflict)** | Symbol, organism, family, domains, and reaction all self-consistent |

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* enzyme.** All catalytic, kinetic, and cofactor parameters are transferred from *E. coli* and the HAMAP rule. There is no published kᶜᵃᵗ, Kₘ, substrate-specificity profile, or Mg²⁺-vs-Mn²⁺ preference measured on Q88D35 itself.
2. **No experimental structure.** The three-domain ATP-grasp fold and homotetrameric assembly are inferred from 66.5% identity to the *E. coli* crystal structure; no *P. putida* GshB structure has been experimentally validated.
3. **No targeted genetics.** There is no reported *gshB* (PP_4993) deletion/knockout phenotype in *P. putida*, so the specific physiological consequences of losing GSH synthesis in this organism remain inferential.
4. **Active-site residue numbering is model-derived.** The Mg²⁺-coordinating residues (Glu282, Asn284) and ATP-binding region (152–208) come from sequence-model mapping, not from a co-crystal with substrate/metal for the *P. putida* protein.
5. **Regulation is uncharacterized.** Although *gshA* and *gshB* are unlinked (not co-operonic), the transcriptional/post-translational control of PP_4993 specifically has not been studied.
6. **Evidence code caveat.** The UniProt functional assignment carries ECO:0000255 (inferred from sequence model), not experimental evidence codes — appropriately high-confidence but not organism-specific proof.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Clone PP_4993, purify the His-tagged protein, and measure glutathione-synthetase activity (ADP/Pi release or GSH formation) to obtain kᶜᵃᵗ, Kₘ for γ-Glu-Cys, glycine, and ATP, and to confirm the Mg²⁺/Mn²⁺ preference — converting the annotation from inferred to experimental.
2. **Targeted deletion phenotyping.** Construct a clean ΔgshB (PP_4993) mutant and assay GSH levels (DTNB/HPLC), plus sensitivity to H₂O₂, organic solvents (toluene), heavy metals (Cr, Pb, Cd), and methylglyoxal — directly testing the redox/detox roles inferred from F003 and F005.
3. **Substrate-specificity screen.** Test whether the enzyme can use alternative amino acids in place of glycine (e.g., β-alanine, L-Ser) and alternative dipeptide substrates, to define specificity and probe biotechnological potential (GSH-analog production).
4. **Structural determination.** Solve the crystal or cryo-EM structure (ideally with ATP/Mg²⁺ and substrate analogs) to confirm the ATP-grasp fold, oligomeric state, and the identities of the metal- and substrate-coordinating residues (validating Glu282/Asn284).
5. **Complementation test.** Express *P. putida gshB* in an *E. coli* ΔgshB (GSH-deficient) strain and score restoration of GSH synthesis and oxidative-stress resistance — a rapid functional confirmation.
6. **Regulation and flux analysis.** Use transcriptomics/proteomics under oxidative and solvent stress to determine whether PP_4993 is induced, and perform ¹³C metabolic-flux analysis to quantify GSH-pathway flux relative to NADPH supply during stress (extending [PMID: 33432138](https://pubmed.ncbi.nlm.nih.gov/33432138/)).

---

## Conclusion

*gshB* (PP_4993, Q88D35) of *Pseudomonas putida* KT2440 encodes **glutathione synthetase (EC 6.3.2.3)**, the cytoplasmic, Mg²⁺/Mn²⁺-dependent ATP-grasp C–N ligase that performs the final step of glutathione biosynthesis — ligating glycine onto γ-glutamylcysteine using Mg-ATP via an acyl-phosphate intermediate to make the tripeptide glutathione. Its biological purpose is to supply GSH, the cell's principal cytosolic thiol-redox buffer, which underpins oxidative-, solvent-, and heavy-metal-stress tolerance and feeds specific downstream detoxification pathways. The assignment is very high-confidence but derives from homology transfer (66.5% identity to the crystallized *E. coli* enzyme) and conserved-domain inference, not from organism-specific biochemistry; direct enzymatic, structural, and knockout studies of the *P. putida* protein remain the key outstanding work.


## Artifacts

- [OpenScientist final report](gshB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](gshB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26377681
2. PMID:6147339
3. PMID:11346647
4. PMID:17124497
5. PMID:33432138
6. PMID:17784941
7. PMID:8445637
8. PMID:9732434
9. PMID:17107553
10. PMID:24136354
11. PMID:41529765
12. PMID:18420578
13. PMID:25211225