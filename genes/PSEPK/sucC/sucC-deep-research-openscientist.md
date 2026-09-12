---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:32:17.508327'
end_time: '2026-07-11T18:57:11.392469'
duration_seconds: 1493.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sucC
  gene_symbol: sucC
  uniprot_accession: Q88FB2
  protein_description: 'RecName: Full=Succinate--CoA ligase [ADP-forming] subunit
    beta {ECO:0000255|HAMAP-Rule:MF_00558}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_00558};
    AltName: Full=Succinyl-CoA synthetase subunit beta {ECO:0000255|HAMAP-Rule:MF_00558};
    Short=SCS-beta {ECO:0000255|HAMAP-Rule:MF_00558};'
  gene_info: Name=sucC {ECO:0000255|HAMAP-Rule:MF_00558}; OrderedLocusNames=PP_4186;
    ORFNames=PP4186;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the succinate/malate CoA ligase beta subunit
  protein_domains: ATP-grasp. (IPR011761); ATP-grasp_succ-CoA_synth-type. (IPR013650);
    ATP_grasp_subdomain_1. (IPR013815); Succ-CoA_synthase_bsu_CS. (IPR017866); SUCC_ACL_C.
    (IPR005811)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: sucC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sucC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FB2
- **Protein Description:** RecName: Full=Succinate--CoA ligase [ADP-forming] subunit beta {ECO:0000255|HAMAP-Rule:MF_00558}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_00558}; AltName: Full=Succinyl-CoA synthetase subunit beta {ECO:0000255|HAMAP-Rule:MF_00558}; Short=SCS-beta {ECO:0000255|HAMAP-Rule:MF_00558};
- **Gene Information:** Name=sucC {ECO:0000255|HAMAP-Rule:MF_00558}; OrderedLocusNames=PP_4186; ORFNames=PP4186;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the succinate/malate CoA ligase beta subunit
- **Key Domains:** ATP-grasp. (IPR011761); ATP-grasp_succ-CoA_synth-type. (IPR013650); ATP_grasp_subdomain_1. (IPR013815); Succ-CoA_synthase_bsu_CS. (IPR017866); SUCC_ACL_C. (IPR005811)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sucC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sucC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sucC** (gene ID: sucC, UniProt: Q88FB2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sucC* (Q88FB2) — Succinyl-CoA Synthetase β-Subunit in *Pseudomonas putida* KT2440

## Summary

The gene **sucC** (locus **PP_4186**; UniProt **Q88FB2**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes the **β-subunit of succinyl-CoA synthetase (SCS)**, also called succinate–CoA ligase [ADP-forming] (EC 6.2.1.5). This enzyme catalyzes the reversible, Mg²⁺-dependent reaction **succinate + ATP + CoA ⇌ succinyl-CoA + ADP + Pᵢ** (with a parallel GTP/GDP reaction), which is the **only substrate-level phosphorylation step of the tricarboxylic acid (TCA / Krebs) cycle**. The identity of Q88FB2 as this enzyme is secure: it carries the HAMAP-Rule MF_00558 annotation, belongs to orthologous group COG0045 / NCBIfam TIGR01016 (succinate/malate CoA-ligase β-subunit), and shares **76.8% amino-acid identity with the biochemically and structurally characterized *Escherichia coli* SucC** (P0A836), a close γ-proteobacterial relative. There was no ambiguity in gene identification — the symbol, organism, protein family, and domain architecture are fully mutually consistent.

Functionally, the β-subunit is the **substrate-specificity and energy-capture module** of the α₂β₂ heterotetramer. Its N-terminal **ATP-grasp fold** binds the Mg-nucleotide and dictates nucleotide preference (ADP/ATP vs GDP/GTP); the P. putida enzyme is annotated as the **[ADP-forming]** variant, i.e., it preferentially produces ATP. Its C-terminal **CoA-ligase (SUCC_ACL_C) domain** forms the succinate-binding site and confers strict dicarboxylate specificity — the enzyme reacts with succinate but not appreciably with the other C4-dicarboxylates of the cycle (fumarate, oxaloacetate) or with citrate. Catalysis proceeds through a **single phospho-histidine intermediate** (on the partner α-subunit), which is physically shuttled ~29 Å between two spatially separated active sites by a swinging phosphohistidine loop.

The enzyme is a **soluble, cytosolic protein** (bacterial SCS lacks the cleavable mitochondrial targeting presequence of the mammalian β-subunit). In P. putida it is encoded within a *sucDC* operon embedded in a contiguous TCA-cycle gene cluster flanked by the 2-oxoglutarate dehydrogenase complex (which produces its substrate, succinyl-CoA) and succinate dehydrogenase (which consumes its product, succinate). Because P. putida is a γ-proteobacterium that makes 5-aminolevulinate via the glutamate (C5) route rather than the succinyl-CoA-dependent Shemin pathway, SucC-derived succinyl-CoA is **not** committed to heme biosynthesis; instead SCS acts as a **reversible metabolic node** linking the oxidative TCA cycle to succinyl-CoA-dependent biosynthesis and to CoA/succinate catabolism.

---

## Key Findings

### F001 — sucC encodes the SCS β-subunit that performs the TCA cycle's sole substrate-level phosphorylation

UniProt Q88FB2 (P. putida KT2440, PP_4186, EC 6.2.1.5) is annotated under HAMAP-Rule MF_00558 as **Succinate--CoA ligase [ADP-forming] subunit beta**. The complete enzyme catalyzes the reversible reaction:

> succinyl-CoA + Pᵢ + NDP ⇌ succinate + CoA + NTP  (N = adenosine or guanosine)

via a phosphorylated histidine intermediate. This is the **single substrate-level phosphorylation of the citric acid cycle**, directly converting the thioester-bond energy of succinyl-CoA into a high-energy nucleoside triphosphate. The reaction was defined biochemically and structurally in *E. coli* SCS, where the phosphoryl group resides on His246α ([PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)): *"Succinyl-CoA synthetase (SCS) catalyzes the following reversible reaction via a phosphorylated histidine intermediate (His 246alpha): succinyl-CoA + P(i) + NDP <--> succinate + CoA + NTP."* The enzyme's unique status in the cycle is confirmed independently: *"Succinyl-CoA synthetase (SCS) catalyzes a reversible reaction that is the only substrate-level phosphorylation in the citric acid cycle"* ([PMID: 33645539](https://pubmed.ncbi.nlm.nih.gov/33645539/)).

### F002 — The β-subunit carries the ATP-grasp nucleotide site and sets nucleotide specificity

X-ray crystallography of *E. coli* SCS localized an **ADP-Mg²⁺ complex bound in the ATP-grasp fold of the N-terminal domain of each β-subunit** ([PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)): *"X-ray diffraction data revealed an ADP-Mg(2+) complex bound in the ATP-grasp fold of the N-terminal domain of each beta-subunit."* This is precisely the domain architecture annotated for Q88FB2 (ATP-grasp IPR011761; ATP-grasp_succ-CoA_synth-type IPR013650; ATP_grasp_subdomain_1 IPR013815). Nucleotide preference is set by a small number of β-subunit residues at this site. In *Thermus aquaticus*, a Pro20β/water replaces the Gln20β of the GTP-specific pig enzyme, explaining GDP/GTP preference; by contrast *E. coli* SCS *"uses GDP/GTP but prefers ADP/ATP"* ([PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/)). Because Q88FB2 is annotated as the **[ADP-forming]** enzyme, the P. putida SCS is expected to preferentially generate **ATP**, consistent with its close *E. coli* relative.

### F003 — The β-subunit C-terminal domain provides the succinate-binding site and dicarboxylate specificity

Crystallography of the pig GTP-specific SCS with succinate + Mg²⁺ + CoA (2.2 Å) demonstrated that **succinate binds in the carboxy-terminal domain of the β-subunit** ([PMID: 27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/)): *"Succinate binds in the carboxy-terminal domain of the β-subunit."* The same study explained the strict substrate selectivity: *"The structure shows why succinyl-CoA synthetase is specific for succinate and does not react appreciably with citrate nor with the other C4-dicarboxylic acids of the citric acid cycle, fumarate and oxaloacetate, but shows some activity with L-malate."* Q88FB2 contains the corresponding C-terminal modules — SUCC_ACL_C (IPR005811) and the Succ-CoA_synthase β-subunit conserved site (IPR017866) — confirming it carries this specificity determinant.

### F004 — SCS is a cytoplasmic α₂β₂ heterotetramer using a swinging phosphohistidine loop across ~29 Å

Native gel filtration and sedimentation equilibrium established that bacterial SCS (*T. aquaticus*) is a **heterotetramer of two α- and two β-subunits (α₂β₂)** ([PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/)): *"the enzyme is a heterotetramer of two α-subunits and two β-subunits."* Catalysis requires phosphoryl transfer between two spatially distinct active sites: site I (CoA / succinate / phosphate) and site II (nucleotide, in the β-subunit ATP-grasp fold). This is accomplished by movement of a phospho-histidine loop that carries the phosphorylated active-site histidine between the sites, spanning ~29 Å ([PMID: 33645539](https://pubmed.ncbi.nlm.nih.gov/33645539/)): *"The phosphoryl transfer bridges a distance of 29 Å between the binding sites for phosphohistidine in site I and site II."* Crucially, the mammalian β-subunit is synthesized with a **cleavable 22-residue mitochondrial targeting presequence** ([PMID: 8401211](https://pubmed.ncbi.nlm.nih.gov/8401211/)), whereas the bacterial homolog Q88FB2 lacks such a signal and therefore functions as a **soluble cytoplasmic enzyme**.

### F005 — Q88FB2 catalyzes the ligase-route TCA step succinyl-CoA→succinate, is Mg²⁺-dependent, and localizes to the cytosol

UniProt Q88FB2 (388 aa, 41.2 kDa) documents the catalytic activity **succinate + ATP + CoA ⇌ succinyl-CoA + ADP + phosphate** (Rhea:17661, EC 6.2.1.5) with a parallel GTP/GDP reaction (Rhea:22120). The annotated **PhysiologicalDirection is right-to-left** (succinyl-CoA → succinate + NTP), consistent with its role in the oxidative TCA cycle. It requires **1 Mg²⁺ per subunit** and is assigned to UniPathway UPA00223/UER00999: *"tricarboxylic acid cycle; succinate from succinyl-CoA (ligase route): step 1/1."* The β-subunit N-terminal ATP-grasp domain (residues 9–244) carries the annotated ATP-binding residues (Lys46, Gly53–55, Glu99/Thr102/Glu107) and Mg²⁺-binding residues (~199, 213); succinate-binding residues (264, 321–323) are shared with the α-subunit at the interface. GO annotations place it in the **cytosol (GO:0005829)** as part of the **succinate-CoA ligase complex (GO:0042709)**. The sequence contains the diagnostic SCS-β motifs (ATP-grasp EVNPLV at ~197; CoA-ligase GGGATKER at ~290; conserved VNGAGLAMG at ~263; PROSITE PS01217/PS50975 hits). Independent primary literature confirms the single-step TCA role ([PMID: 27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/)): *"Succinyl-CoA synthetase catalyzes the only step in the citric acid cycle that provides substrate-level phosphorylation."*

### F006 — Catalysis runs through a single phospho-histidine intermediate via a three-step mechanism

Mechanistic studies establish that SCS follows a **three-step mechanism involving a single phosphoenzyme (phospho-histidine) intermediate** — explicitly contrasted with the four-step, two-phosphohistidine mechanism proposed for the related ADP-forming acetyl-CoA synthetase ([PMID: 28129670](https://pubmed.ncbi.nlm.nih.gov/28129670/)): *"The related succinyl-CoA synthetase follows a three-step mechanism involving a single phosphoenzyme."* The phosphoryl group is carried on the α-subunit active-site histidine (His246α in *E. coli*). A conserved α-subunit cysteine (Cys123α) near the CoA/His site is important for optimal activity but is **not** covalently acylated during turnover — a thioester intermediate on Cys123α was ruled out by mutagenesis and crystallography ([PMID: 17642514](https://pubmed.ncbi.nlm.nih.gov/17642514/)): *"This proved that the specific formation of a thioester bond with Cys123alpha is not part of the catalytic mechanism."* Although the phospho-histidine sits on the α-subunit, the β-subunit is an obligate partner because it provides site II (the nucleotide/ATP-grasp site) to which the loop delivers the phosphoryl group.

### F007 — The β-subunit is the prototype of the NDP-forming acyl-CoA synthetase superfamily

Q88FB2 maps to COG0045 and NCBIfam TIGR01016 (sucCoAbeta), in the family "succinate/malate CoA ligase β subunit." Sequence and structural comparisons place SCS at the root of a superfamily of **nucleoside-diphosphate-forming acyl-CoA synthetases**. Three lines of evidence anchor this: (i) ADP-forming acetyl-CoA synthetase homologs whose N-/C-terminal regions align to the SCS α- and β-subunits, defining a *"new superfamily of acyl-CoA synthetases (nucleoside diphosphate-forming) and its signature motifs"* ([PMID: 10681568](https://pubmed.ncbi.nlm.nih.gov/10681568/)); (ii) human ATP-citrate lyase, in which *"residues 2-425 form three domains homologous to the beta-subunit of succinyl-CoA synthetase (SCS), while residues 487-820 form two domains homologous to the alpha-subunit of SCS"* ([PMID: 20558738](https://pubmed.ncbi.nlm.nih.gov/20558738/)); and (iii) citryl-CoA synthetase from *Hydrogenobacter thermophilus*, where *"Citryl-CoA synthetase and SCS were homologous, but showed different substrate specificity"* ([PMID: 15101981](https://pubmed.ncbi.nlm.nih.gov/15101981/)). The β-subunit's two-module architecture — N-terminal ATP-grasp (Pfam PF08442) plus C-terminal CoA-ligase domain (Pfam PF00549, Ligase_CoA) — is the shared scaffold across this superfamily.

### F008 — In P. putida, SucC-derived succinyl-CoA is a reversible biosynthetic/catabolic node, not a heme precursor

The succinyl-CoA-consuming C4/Shemin heme route (5-aminolevulinate synthase, ALAS, condensing glycine + succinyl-CoA) is **restricted to non-plant eukaryotes and α-proteobacteria** ([PMID: 16121195](https://pubmed.ncbi.nlm.nih.gov/16121195/)): *"5-Aminolevulinate synthase (ALAS) is the first and rate-limiting enzyme of heme biosynthesis in humans, animals, other non-plant eukaryotes, and alpha-proteobacteria."* P. putida is a **γ-proteobacterium** and makes 5-aminolevulinate via the glutamate (C5) pathway, so its succinyl-CoA pool is **not** committed to tetrapyrrole synthesis. Because SCS catalyzes a fully reversible reaction, it acts as a **bidirectional node**: in the oxidative/catabolic direction it converts 2-oxoglutarate-dehydrogenase-derived succinyl-CoA to succinate (handed off to succinate dehydrogenase / complex II) while conserving energy as ATP; in the anabolic direction it regenerates succinyl-CoA from succinate + ATP + CoA as the acyl donor for downstream biosynthesis (e.g., succinylated intermediates in the diaminopimelate/lysine and methionine pathways) and as the convergence point of propionyl-CoA/methylmalonyl-CoA and branched-/odd-chain catabolism.

### F009 — sucC is genomically clustered with sucD and the 2-oxoglutarate/succinate dehydrogenase genes

The KEGG genome context for P. putida KT2440 shows **PP_4186 (sucC, β-subunit; complement 4,728,669–4,729,835) is immediately adjacent to and contiguous with PP_4185 (sucD, SCS α-subunit; complement 4,727,785–4,728,669)** on the same strand — a *sucDC* operon encoding both subunits of the functional α₂β₂ enzyme. The surrounding cluster (all on the complement strand) comprises PP_4187 (dihydrolipoyl dehydrogenase, E3), PP_4188 (2-oxoglutarate dehydrogenase E2, dihydrolipoyltranssuccinylase), PP_4189 (2-oxoglutarate decarboxylase E1), PP_4190 (succinate dehydrogenase iron–sulfur subunit, SdhB), and PP_4191 (succinate dehydrogenase flavoprotein, SdhA). Thus the immediate genomic neighborhood encodes the enzyme that **produces** SCS's substrate (2-oxoglutarate dehydrogenase complex → succinyl-CoA) and the enzyme that **consumes** its product (succinate dehydrogenase → fumarate). This synteny is a strong contextual confirmation of SucC's TCA-cycle role.

### F010 — P. putida SucC is 76.8% identical to E. coli SucC, licensing transfer of structural/mechanistic data

A global Needleman–Wunsch alignment of Q88FB2 (P. putida KT2440 SucC, 388 aa) against P0A836 (*E. coli* K-12 SucC, 388 aa) gives **298/388 = 76.8% amino-acid identity with no length difference**. The functionally critical residues annotated in Q88FB2 (ATP-binding Lys46, Gly53–55, Glu99/Thr102/Glu107; Mg²⁺-binding ~199/213; succinate-binding 264/321–323) fall within the conserved ATP-grasp module (residues 9–244) and the C-terminal CoA-ligase module — both diagnostic of the succinate/malate CoA-ligase β-subunit family (COG0045; TIGR01016). This high identity to an extensively characterized ortholog is the formal justification for applying *E. coli* and mammalian SCS structural/mechanistic conclusions to the P. putida enzyme.

---

## Mechanistic Model / Interpretation

### The reaction and the division of labor between subunits

Succinyl-CoA synthetase is an α₂β₂ heterotetramer in which each αβ half carries a complete catalytic unit. **SucC (β-subunit) and SucD (α-subunit) are functionally inseparable**; SucC contributes the nucleotide chemistry and the dicarboxylate specificity, while SucD carries the catalytic histidine and part of the CoA/succinate site.

```
                Succinyl-CoA synthetase (α2β2)  —  cytosolic, Mg2+-dependent
   ┌──────────────────────────────────────────────────────────────────────┐
   │   α-subunit (SucD, PP_4185)          β-subunit (SucC, PP_4186)        │
   │   ─────────────────────────          ────────────────────────         │
   │   • Active-site His (P-His)          • N-term ATP-grasp fold           │
   │   • CoA / phosphate site (site I)      → binds Mg-nucleotide (site II) │
   │   • Cys123α (assists, not acylated)    → sets ADP/ATP vs GDP/GTP pref. │
   │                                       • C-term CoA-ligase domain       │
   │                                         → succinate-binding site       │
   │                                         → dicarboxylate specificity    │
   └──────────────────────────────────────────────────────────────────────┘

   Phospho-His loop swings the ~29 Å between:
        site I (CoA · succinate · Pi, on α)  ⇄  site II (nucleotide, on β)
```

### Catalytic cycle (three steps, one phospho-enzyme)

```
   1)  E-His  +  ATP            →  E-His~P  +  ADP          (β-subunit ATP-grasp site, site II)
   2)  E-His~P  +  succinate    →  E  +  succinyl-phosphate (loop swings ~29 Å to site I)
   3)  succinyl-phosphate + CoA →  succinyl-CoA  +  Pi
   ───────────────────────────────────────────────────────
   Net (physiological, catabolic):  succinyl-CoA + Pi + ADP  →  succinate + CoA + ATP
```

The reaction is fully reversible; the P. putida enzyme is annotated with the physiological (catabolic) direction succinyl-CoA → succinate, but under biosynthetic demand it can run in reverse to regenerate succinyl-CoA.

### Position in metabolism

```
   Isocitrate ─► 2-oxoglutarate ─►(OGDH: PP_4187/4188/4189)─► SUCCINYL-CoA
                                                                   │
                                                    SucCD (SCS, PP_4185/4186)
                                                    succinyl-CoA + Pi + ADP
                                                       ⇅  (Mg2+, substrate-level phosphorylation → ATP)
                                                    succinate + CoA + ATP
                                                                   │
                                        SUCCINATE ─►(SDH: PP_4190/4191)─► fumarate ─► ... ─► oxaloacetate
```

The genomic operon structure (F009) mirrors this metabolic adjacency: the gene making the substrate and the gene consuming the product flank *sucCD* on the chromosome. Because P. putida uses the C5/glutamate route for 5-aminolevulinate (F008), the SCS node is dedicated to energy conservation and general succinyl-CoA supply rather than to heme, distinguishing it from the mitochondrial/α-proteobacterial context where succinyl-CoA feeds ALAS.

### Comparative context table

| Feature | P. putida SucC (Q88FB2) | E. coli SucC (P0A836) | Pig heart β (GTP-specific) |
|---|---|---|---|
| Length | 388 aa | 388 aa | 395 aa mature (+22 aa targeting presequence) |
| Identity to Q88FB2 | 100% | 76.8% | ~45% (E. coli–pig comparison) |
| Nucleotide preference | ADP/ATP-forming (annotated) | GDP/GTP-capable, prefers ADP/ATP | GTP-specific |
| Localization | Cytosol (no targeting signal) | Cytosol | Mitochondrial matrix (cleavable presequence) |
| Oligomer | α₂β₂ | α₂β₂ | αβ dimer |
| Catalytic His | On α-subunit | His246α | On α-subunit |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/) | *ADP-binding site of E. coli SCS revealed by X-ray crystallography* | Defines the exact reversible reaction and localizes ADP-Mg²⁺ to the β-subunit ATP-grasp fold (F001, F002) |
| [27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/) | *Structural basis for the binding of succinate to SCS* | Localizes succinate to β C-terminal domain; explains dicarboxylate specificity; confirms sole SLP step (F003, F005) |
| [33645539](https://pubmed.ncbi.nlm.nih.gov/33645539/) | *Second conformation of the phosphohistidine loop in SCS* | Establishes the ~29 Å swinging phospho-His mechanism and unique SLP role (F001, F004) |
| [22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/) | *GTP-preferring SCS from Thermus aquaticus* | Documents α₂β₂ quaternary structure and β-subunit control of nucleotide preference (F002, F004) |
| [28129670](https://pubmed.ncbi.nlm.nih.gov/28129670/) | *ADP-forming acetyl-CoA synthetase mechanism* | States SCS uses a three-step, single-phospho-enzyme mechanism (F006) |
| [17642514](https://pubmed.ncbi.nlm.nih.gov/17642514/) | *Participation of Cys123α of E. coli SCS* | Rules out a covalent Cys-thioester intermediate, refining the mechanism (F006) |
| [8401211](https://pubmed.ncbi.nlm.nih.gov/8401211/) | *Cloning of pig heart SCS β-subunit* | Documents the cleavable mitochondrial presequence absent in bacteria; ~45% identity bacteria↔pig (F004) |
| [10681568](https://pubmed.ncbi.nlm.nih.gov/10681568/) | *Acetyl-CoA synthetase / NDP-forming superfamily* | Defines the NDP-forming acyl-CoA synthetase superfamily to which SucC belongs (F007) |
| [20558738](https://pubmed.ncbi.nlm.nih.gov/20558738/) | *Citrate-binding site of human ATP-citrate lyase* | Shows ACL is built from SCS β- and α-subunit homologous domains (F007) |
| [15101981](https://pubmed.ncbi.nlm.nih.gov/15101981/) | *Citryl-CoA synthetase from H. thermophilus* | Homologous to SCS but with altered substrate specificity — superfamily diversification (F007) |
| [16121195](https://pubmed.ncbi.nlm.nih.gov/16121195/) | *Crystal structure of ALAS / link to XLSA* | Confines the succinyl-CoA→heme (ALAS) route to eukaryotes/α-proteobacteria (F008) |

Supporting/contextual literature reviewed but not central to the core annotation: [21638627](https://pubmed.ncbi.nlm.nih.gov/21638627/) (physiological significance of the two nucleotide-specific SCS isoforms in animals), [7669763](https://pubmed.ncbi.nlm.nih.gov/7669763/) (phospho-His chemistry in NDP kinase, a mechanistic comparison point), [12135479](https://pubmed.ncbi.nlm.nih.gov/12135479/) (bacterial ATP-citrate lyase mechanism), and several P. putida KT2440 genomics/bioremediation studies (e.g., [38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)) that establish organism context but do not address sucC directly.

**Consistency of the evidence:** All primary structural/mechanistic studies (from *E. coli*, *T. aquaticus*, and pig) converge on the same subunit division of labor, and all directly annotated domains of Q88FB2 (ATP-grasp, SUCC_ACL_C, conserved β-site) match the residues shown crystallographically to bind nucleotide and succinate. No contradictory evidence was encountered. The single caveat — that most mechanistic data derive from orthologs — is strongly mitigated by the 76.8% identity to *E. coli* SucC (F010).

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the P. putida enzyme.** All catalytic, kinetic, and structural conclusions are transferred by homology from *E. coli*, *T. aquaticus*, and mammalian SCS. There is no published crystal structure, purified-enzyme kinetics, or Km/kcat measurement specifically for Q88FB2. The high sequence identity (76.8% to *E. coli*) makes this transfer safe but not a substitute for direct data.

2. **Nucleotide specificity is inferred, not measured.** The "[ADP-forming]" annotation follows HAMAP-Rule MF_00558 and the *E. coli* precedent. Whether P. putida SucCD uses ADP/ATP exclusively, or also accepts GDP/GTP (as *E. coli* does), has not been experimentally determined for this strain.

3. **Physiological direction and flux control unquantified.** The annotated physiological direction (succinyl-CoA → succinate) reflects the oxidative TCA cycle, but the extent to which P. putida runs SCS in reverse for biosynthetic succinyl-CoA supply — particularly under gluconeogenic or aromatic-compound-catabolizing growth (a hallmark of P. putida metabolism) — is not established.

4. **Operon regulation unknown.** While the *sucCD* / TCA gene cluster (F009) is documented at the sequence level, its transcriptional regulation, promoter structure, and any conditional expression (e.g., under carbon-source shifts) were not investigated here.

5. **Metabolic-node claims (F008) are inferential.** The assignment of biosynthetic succinyl-CoA uses (diaminopimelate, methionine pathways) is based on general bacterial metabolism, not P. putida-specific flux or genetic data.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic characterization.** Clone P. putida *sucC* + *sucD* (PP_4186/PP_4185), co-express in an *E. coli* SCS-deletion background, purify the α₂β₂ complex, and measure Km/kcat for succinate, CoA, and both ADP and GDP to experimentally confirm the ADP-forming preference.

2. **Structural determination.** Solve the crystal or cryo-EM structure of P. putida SucCD (or generate a high-confidence AlphaFold model with PAE analysis) and superpose against *E. coli* SCS to verify conservation of the ATP-grasp nucleotide site and the succinate-binding C-terminal domain.

3. **Nucleotide-specificity mutagenesis.** Probe the residues homologous to the Gln20β/Pro20β determinant (identified in the pig vs *T. aquaticus* comparison) to test their control of ATP vs GTP output in the P. putida enzyme.

4. **Flux and reversibility assays.** Use ¹³C-labeled substrates and metabolic flux analysis under different carbon sources (glucose, succinate, aromatic compounds) to quantify the net direction and biosynthetic vs catabolic partitioning of the SCS node in vivo.

5. **Genetic essentiality / regulation.** Examine RB-TnSeq fitness data (e.g., the P. putida functional-genomics resources already noted in the literature) for the *sucC* locus to assess essentiality and condition-dependent fitness, and map the *sucCD* operon's transcriptional organization and regulation.

---

## Conclusion

The gene identification is unambiguous and fully supported. **sucC (Q88FB2, PP_4186) encodes the β-subunit of succinyl-CoA synthetase (EC 6.2.1.5)** in *Pseudomonas putida* KT2440. The β-subunit is the substrate-specificity and energy-capture module of a soluble, cytosolic, Mg²⁺-dependent α₂β₂ enzyme that catalyzes the only substrate-level phosphorylation of the TCA cycle (succinate + ATP + CoA ⇌ succinyl-CoA + ADP + Pᵢ, ADP/ATP-forming), operating through a single swinging phospho-histidine intermediate and functioning as a reversible succinyl-CoA↔succinate metabolic node.


## Artifacts

- [OpenScientist final report](sucC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sucC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10625475
2. PMID:33645539
3. PMID:22751660
4. PMID:27487822
5. PMID:8401211
6. PMID:28129670
7. PMID:17642514
8. PMID:10681568
9. PMID:20558738
10. PMID:15101981
11. PMID:16121195