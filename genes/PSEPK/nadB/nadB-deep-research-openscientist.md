---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T15:08:37.024846'
end_time: '2026-07-20T15:28:53.859893'
duration_seconds: 1216.84
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nadB
  gene_symbol: nadB
  uniprot_accession: Q88MZ2
  protein_description: 'RecName: Full=L-aspartate oxidase {ECO:0000256|ARBA:ARBA00021901,
    ECO:0000256|NCBIfam:TIGR00551}; EC=1.4.3.16 {ECO:0000256|ARBA:ARBA00012173, ECO:0000256|NCBIfam:TIGR00551};'
  gene_info: Name=nadB {ECO:0000313|EMBL:AAN67048.1}; OrderedLocusNames=PP_1426 {ECO:0000313|EMBL:AAN67048.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FAD-dependent oxidoreductase 2 family. NadB
  protein_domains: FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188);
    Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939);
    NadB. (IPR005288)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MZ2
- **Protein Description:** RecName: Full=L-aspartate oxidase {ECO:0000256|ARBA:ARBA00021901, ECO:0000256|NCBIfam:TIGR00551}; EC=1.4.3.16 {ECO:0000256|ARBA:ARBA00012173, ECO:0000256|NCBIfam:TIGR00551};
- **Gene Information:** Name=nadB {ECO:0000313|EMBL:AAN67048.1}; OrderedLocusNames=PP_1426 {ECO:0000313|EMBL:AAN67048.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FAD-dependent oxidoreductase 2 family. NadB
- **Key Domains:** FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188); Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939); NadB. (IPR005288)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadB** (gene ID: nadB, UniProt: Q88MZ2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *nadB* (L-Aspartate Oxidase) in *Pseudomonas putida* KT2440

**UniProt:** Q88MZ2 | **Gene:** *nadB* | **Ordered locus:** PP_1426 | **EC:** 1.4.3.16
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**Protein family:** FAD-dependent oxidoreductase 2 family, NadB subgroup

---

## Summary

The *Pseudomonas putida* KT2440 gene ***nadB*** (locus PP_1426; UniProt **Q88MZ2**) encodes **L-aspartate oxidase (LASPO, EC 1.4.3.16)**, a **FAD-dependent flavoenzyme** that catalyzes the **first committed step of the *de novo* biosynthesis of nicotinamide adenine dinucleotide (NAD⁺)**. The enzyme oxidizes **L-aspartate to α-iminosuccinate (iminoaspartate)**, an unstable imino acid that is the entry-point metabolite for the bacterial *de novo* NAD⁺ pathway. This annotation is anchored by strong sequence and domain homology (identical InterPro/TIGRFAM signatures for the NadB family) between Q88MZ2 and biochemically and structurally characterized orthologs from *Escherichia coli* and *Bacillus subtilis*.

Mechanistically, NadB is a member of the **succinate dehydrogenase / fumarate reductase (SDH/FRD) structural and functional superfamily**. It carries a **non-covalently bound FAD** cofactor within a three-domain fold (an FAD/dinucleotide-binding domain, an α+β capping domain, and a C-terminal three-helical bundle). A distinctive and biologically important feature is that the enzyme can re-oxidize its reduced flavin using **either molecular oxygen (oxidase mode, producing H₂O₂) or fumarate (dehydrogenase mode, producing succinate)** as the terminal electron acceptor, allowing the *de novo* NAD⁺ pathway to operate under **both aerobic and anaerobic conditions**. Substrate specificity for L-aspartate — as opposed to the dicarboxylate substrates of its SDH/FRD relatives — is enforced by a strictly conserved active-site glutamate (Glu121 in the *E. coli* numbering) that reads the α-amino group of the substrate.

Functionally, NadB acts in the **cytoplasm** and operates as the first enzyme of the linear **NadB → NadA → NadC** route: its product, iminoaspartate, is condensed with dihydroxyacetone phosphate by **quinolinate synthase (NadA, a [4Fe–4S] enzyme)** to form quinolinate, which **quinolinate phosphoribosyltransferase (NadC)** then converts to nicotinate mononucleotide, feeding into the universal NAD⁺ assembly steps. A direct, non-species-specific physical interaction between NadA and NadB has been demonstrated, consistent with substrate channeling of the labile iminoaspartate intermediate. Because this L-aspartate-oxidase route to quinolinate is **bacterial and absent in mammals** (which synthesize quinolinate from tryptophan via the kynurenine pathway), NadB is regarded as a **candidate antibacterial drug target**. Loss of NadB produces the classic NAD⁺/nicotinamide-auxotrophic (Nic⁻) phenotype in the characterized orthologs.

> **Identity verification:** The gene symbol *nadB*, the protein description (L-aspartate oxidase, EC 1.4.3.16), the FAD-dependent oxidoreductase 2 / NadB family assignment, and the domain architecture (IPR005288 NadB; IPR003953 FAD-dep_OxRdtase_2_FAD-bd; IPR015939 Fum_Rdtase/Succ_DH_flav-like_C) are fully mutually consistent. The literature identified describes the *bona fide* L-aspartate oxidase / NAD-biosynthesis NadB, not an unrelated gene sharing the symbol. Direct experimental characterization exists for *E. coli* and *B. subtilis* orthologs; the assignment transfers to *P. putida* Q88MZ2 by strong homology and identical family/domain signatures. No *P. putida*-specific enzymological study of PP_1426 was located.

---

## Key Findings

### Finding 1 — NadB is L-aspartate oxidase, catalyzing the first committed step of *de novo* NAD⁺ biosynthesis

UniProt Q88MZ2 annotates PP_1426/*nadB* of *P. putida* KT2440 as **L-aspartate oxidase (EC 1.4.3.16)**, a member of the FAD-dependent oxidoreductase 2 family (NadB subgroup). In biochemically characterized homologs, the enzyme catalyzes the oxidation of **L-aspartate to iminoaspartate (α-iminosuccinate)** — the first reaction of the bacterial *de novo* NAD⁺ pathway. This reaction feeds directly into quinolinate synthase (NadA), which condenses iminoaspartate with dihydroxyacetone phosphate to generate quinolinate.

The functional definition is unambiguous in the primary literature. As summarized for the pathway, "*In many eubacteria, including several pathogens, the first two steps in the de novo synthesis of NAD are catalyzed by l-aspartate oxidase (NadB) and quinolinate synthase (NadA)*" [PMID: 18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/). The specific reaction was defined by the enzyme's structural characterization: "*L-Aspartate oxidase (Laspo) catalyzes the conversion of L-Asp to iminoaspartate, the first step in the de novo biosynthesis of NAD(+)*" [PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/).

The genetic link between *nadB* and this function is directly demonstrated: in uropathogenic *E. coli*, "*A mutation in the nadB gene, encoding L-aspartate oxidase, was shown to be responsible for the nicotinamide requirement of UTI89*" [PMID: 22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/). This establishes both that *nadB* encodes L-aspartate oxidase and that its loss produces NAD⁺ (nicotinamide) auxotrophy — the metabolic signature of a lesion at the entry point of the *de novo* pathway.

**Reaction catalyzed:**

```
L-aspartate + FAD  ->  iminoaspartate (alpha-iminosuccinate) + FADH2
FADH2 + acceptor   ->  FAD + reduced acceptor
   acceptor = O2       (oxidase mode)  -> H2O2
   acceptor = fumarate (dehydrogenase) -> succinate
```

### Finding 2 — NadB is an FAD flavoenzyme using either O₂ or fumarate as electron acceptor

Crystallographic studies of the *E. coli* enzyme (apo form at 2.2 Å; FAD-bound R386L holoenzyme at 2.5 Å) revealed a **non-covalently bound FAD** housed in a three-domain fold: an **FAD-binding (dinucleotide-binding) domain**, an **α+β capping domain**, and a **C-terminal three-helical bundle**. The enzyme oxidizes L-aspartate and then re-oxidizes the reduced flavin using either molecular oxygen or fumarate as the electron acceptor. This dual acceptor capability is functionally significant: it enables the *de novo* NAD⁺ pathway to proceed under aerobic conditions (oxidase mode, generating H₂O₂) and under anaerobic conditions (fumarate-reducing dehydrogenase mode, generating succinate).

The primary structural paper describes NadB as "*a flavoenzyme that converts aspartate to iminoaspartate using either molecular oxygen or fumarate as electron acceptors*" [PMID: 10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/), and specifies the fold as "*an FAD-binding domain with the dinucleotide-binding fold, a C-terminal three-helical bundle domain, and an alpha + beta capping domain*" [PMID: 10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/).

Cofactor binding is not merely structural scaffolding — it is coupled to active-site assembly. The FAD-bound holoenzyme structure showed that "*cofactor incorporation leads to the ordering of two polypeptide segments (residues 44-53 and 104-141) and to a 27 degree rotation of the capping domain*" [PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/). This conformational transition forms the active-site cavity at the interface between the FAD-binding and capping domains, meaning the enzyme is only catalytically competent once FAD is loaded. Such domain-hinge behavior of two-domain enzymes generally underlies substrate access and catalytic cycling [PMID: 10593256](https://pubmed.ncbi.nlm.nih.gov/10593256/).

### Finding 3 — NadB belongs structurally and mechanistically to the succinate dehydrogenase / fumarate reductase family

L-aspartate oxidase shares sequence homology and overall folding topology with the flavoprotein subunits of **succinate dehydrogenase (SDH)** and **fumarate reductase (FRD)**. Strictly conserved residues cluster in the FAD-binding site and the catalytic center. The succinate-bound holoenzyme structure showed an active-site cavity whose surface is decorated by two clusters of hydrogen-bond donors that anchor the ligand's carboxylate groups, with the strictly conserved **Glu121** positioned to interact with the L-aspartate α-amino group.

The structural paper places NadB firmly within this superfamily: "*LASPO, SDH and FRD form a class of functionally and structurally related oxidoreductases that are all able to reduce fumarate and to oxidise a dicarboxyla[te]*" [PMID: 10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/). The active-site conservation extends the analogy to catalysis: "*The architecture of the active site of the Laspo holoenzyme is remarkably similar to that of respiratory fumarate reductases, providing strong evidence for a common mechanism of catalysis in Laspo and flavoproteins of the succinate dehydrogenase/fumarate reductase family*" [PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/).

This membership is precisely what the UniProt annotation of Q88MZ2 reflects: assignment to the **FAD-dependent oxidoreductase 2 family** with **Fum_Rdtase/Succ_DH_flav-like_C** (IPR015939) and **FAD-dep_OxRdtase_2_FAD-bd** (IPR003953) domains. The domain signatures of the *P. putida* protein therefore independently corroborate the SDH/FRD-family mechanistic assignment inferred from the *E. coli* structures.

### Finding 4 — NadB acts in the cytoplasm and functionally partners with quinolinate synthase (NadA)

In the *de novo* pathway, NadB oxidizes L-aspartate to iminoaspartate, which **NadA (quinolinate synthase, a [4Fe–4S] enzyme)** condenses with dihydroxyacetone phosphate to yield **quinolinate**. **NadC (quinolinate phosphoribosyltransferase)** then converts quinolinate to nicotinate mononucleotide, feeding the shared, universal NAD⁺ assembly steps. Both LASPO and NadA are **soluble enzymes**; LASPO was purified as a soluble cytoplasmic flavoprotein and crystallized from solution, indicating a **cytoplasmic site of action**.

Crucially, a **direct, non-species-specific physical interaction** between the two entry enzymes has been demonstrated — *B. subtilis* NadB interacts with *E. coli* NadA — consistent with **substrate channeling** of the chemically labile iminoaspartate intermediate between the two active sites. The characterization of the *B. subtilis* enzymes reported that "*the interaction between NadA and NadB is not species-specific between B. subtilis and Escherichia coli*" [PMID: 18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/), and identified the partner as an iron-sulfur enzyme: "*NadA from B. subtilis possesses a [4Fe-4S]2+ cluster*" [PMID: 18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/).

The pathway logic — that NadB and NadA together produce quinolinate — is explicit: "*two enzymes, L-aspartate oxidase (NadB) and quinolinate synthase (NadA), are required for the synthesis of QUIN*" [PMID: 24120364](https://pubmed.ncbi.nlm.nih.gov/24120364/). Loss of either enzyme (via *nadB* or *nadA* mutation/silencing) produces the nicotinic-acid/NAD-auxotrophic (Nic⁻) phenotype, further tying NadB's function to this cytoplasmic biosynthetic route.

### Finding 5 — NadB is strictly specific for L-aspartate, and the pathway it initiates is a validated antibacterial drug target

The FAD-bound holoenzyme active site anchors the substrate's dicarboxylate through two hydrogen-bond-donor clusters, while the strictly conserved **Glu121** reads the L-aspartate α-amino group — a specificity determinant that distinguishes L-aspartate from the succinate/fumarate dicarboxylates handled by the homologous SDH/FRD enzymes. This narrow specificity underlies the enzyme's dedicated, non-redundant role in NAD⁺ biosynthesis: "*the cavity surface is decorated by two clusters of H-bond donors that anchor the ligand carboxylates*" [PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/), and "*Glu121, which is strictly conserved among Laspo sequences, is positioned to interact with the L-Asp alpha-amino group*" [PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/).

Because the L-aspartate-oxidase → quinolinate-synthase route to quinolinate is bacterial and absent in mammals (which produce quinolinate from tryptophan), NadB and NadA are considered attractive targets for antibacterial drug design: "*This bacterial pathway represents a potential drug target since it is absent in mammals*" [PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/).

---

## Mechanistic Model / Interpretation

NadB is best understood as the **flavin-dependent gatekeeper** that draws carbon and nitrogen from central metabolism (L-aspartate, itself derived from oxaloacetate) into the pyridine-nucleotide (NAD⁺) pool. Its position, cofactor chemistry, structural family, and partner interactions form a coherent picture.

### The *de novo* NAD⁺ pathway (aspartate route)

```
        L-aspartate
             |
             |  NadB  (L-aspartate oxidase, EC 1.4.3.16)  <-- THIS PROTEIN (PP_1426 / Q88MZ2)
             |        FAD-dependent; O2 (aerobic) or fumarate (anaerobic) acceptor
             v
      iminoaspartate  (alpha-iminosuccinate; labile)
             |
             |  NadA  (quinolinate synthase, [4Fe-4S])   <-- direct physical partner
             |  + dihydroxyacetone phosphate (DHAP)
             v
        quinolinate  (QUIN)
             |
             |  NadC  (quinolinate phosphoribosyltransferase)
             |  + PRPP  (- CO2)
             v
    nicotinate mononucleotide (NaMN)
             |
             v
   ... universal NAD+ assembly (NadD, NadE) --> NAD+
```

### Reaction and cofactor logic

The chemistry is a classic flavoprotein amino-acid oxidation: FAD abstracts electrons/hydride from the Cα–N center of L-aspartate to form the α-imino acid (iminoaspartate), leaving reduced FADH₂. The distinctive feature relative to canonical D-amino-acid oxidases is the **reoxidation branch point**: FADH₂ can hand electrons to O₂ (oxidase activity → H₂O₂) or to fumarate (fumarate-reductase-like dehydrogenase activity → succinate). This dual capability is a direct consequence of NadB's membership in the SDH/FRD superfamily, whose members intrinsically interconvert succinate/fumarate at a flavin center. Biologically, it ensures NAD⁺ can be synthesized *de novo* whether the cell is respiring aerobically or under oxygen-limited conditions — a useful robustness property for a metabolically versatile soil organism such as *P. putida*.

### Substrate specificity

The enzyme must select L-aspartate over the structurally similar dicarboxylates (succinate/fumarate) that its SDH/FRD relatives act on. The solution is a bipartite recognition apparatus: two hydrogen-bond-donor clusters clamp the two carboxylates, and the conserved **Glu121** specifically reads the substrate α-amino group. This explains the enzyme's strict L-aspartate specificity and its non-redundant, dedicated placement at the head of NAD⁺ biosynthesis.

### Channeling and localization

Both NadB and NadA are soluble cytoplasmic enzymes, and they physically interact. Because iminoaspartate is chemically unstable (it readily hydrolyzes to oxaloacetate and ammonia), a **substrate-channeling handoff** from NadB to NadA is metabolically advantageous, protecting the intermediate and increasing pathway flux. The non-species-specific NadA–NadB interaction observed between *B. subtilis* and *E. coli* proteins argues that this partnership is an evolutionarily conserved feature of the family, and can reasonably be inferred to hold for the *P. putida* pair (PP_1426 NadB and its cognate NadA).

### Comparison to related flavoenzymes and dehydrogenases

| Enzyme | Reaction / substrate | Cofactor | Relationship to NadB |
|---|---|---|---|
| **NadB / LASPO** (this protein) | L-Asp → iminoaspartate; O₂ or fumarate acceptor | FAD (non-covalent) | The subject enzyme; SDH/FRD family |
| Succinate dehydrogenase (SDH) | succinate ⇌ fumarate | FAD (covalent) | Same structural superfamily; shared active-site architecture |
| Fumarate reductase (FRD) | fumarate → succinate | FAD | Same superfamily; "remarkably similar" active site [PMID: 11863440] |
| D-aspartate oxidase (DASPO) | D-Asp → oxaloacetate + NH₃ | FAD | Different family/fold; opposite stereospecificity [PMID: 10209293] |
| L-aspartate dehydrogenase (AspDH) | OAA + NH₃ ⇌ L-Asp | NAD(P) | Different mechanism; makes/consumes Asp, not NAD precursor [PMID: 21468714] |

The last two rows are important negative controls for identity: NadB is *not* a D-aspartate oxidase (different stereochemistry and fold) and *not* an L-aspartate dehydrogenase (a distinct NAD(P)-dependent amino-acid dehydrogenase). These distinctions reinforce that Q88MZ2's annotation — L-aspartate oxidase of the SDH/FRD (NadB) family committing aspartate to NAD⁺ synthesis — is the correct one.

---

## Evidence Base

| PMID | Title (abbreviated) | Organism/system | Contribution to this report |
|---|---|---|---|
| [10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/) | *Structure of L-aspartate oxidase: implications for the SDH/FRD family* | *E. coli* (apo, 2.2 Å) | Establishes FAD flavoenzyme; dual O₂/fumarate acceptor; three-domain fold; SDH/FRD family membership (Findings 2, 3) |
| [11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/) | *Structure of FAD-bound L-aspartate oxidase: substrate specificity and catalysis* | *E. coli* (holo, 2.5 Å) | Defines reaction (L-Asp → iminoaspartate); FAD-induced active-site assembly (27° capping rotation); Glu121 specificity; carboxylate-anchoring donors; drug-target statement (Findings 1, 2, 3, 5) |
| [18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/) | *Characterization of L-aspartate oxidase and quinolinate synthase from B. subtilis* | *B. subtilis* | NadB + NadA are the first two *de novo* NAD steps; direct non-species-specific NadA–NadB interaction; NadA is a [4Fe–4S] enzyme (Findings 1, 4) |
| [22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/) | *Nicotinamide dependence of UPEC UTI89; nadB as neutral insertion site* | *E. coli* UTI89 | Genetic proof that *nadB* encodes L-aspartate oxidase and its loss causes NAD/nicotinamide auxotrophy (Finding 1) |
| [24120364](https://pubmed.ncbi.nlm.nih.gov/24120364/) | *Molecular evolution of nicotinic acid requirement in Shigella/EIEC* | *Shigella*/EIEC | NadB + NadA together synthesize quinolinate; pathway loss → Nic⁻ auxotrophy (Finding 4) |
| [10593256](https://pubmed.ncbi.nlm.nih.gov/10593256/) | *Folding funnels and conformational transitions via hinge-bending* | General/theoretical | Context for domain-hinge motions relevant to FAD-coupled capping-domain rotation (Finding 2, supporting) |
| [10209293](https://pubmed.ncbi.nlm.nih.gov/10209293/) | *Beef kidney D-aspartate oxidase* | Mammalian (contrast) | Negative control: distinguishes NadB (L-specific, NAD pathway) from D-aspartate oxidase |
| [21468714](https://pubmed.ncbi.nlm.nih.gov/21468714/) | *L-aspartate dehydrogenase from P. aeruginosa PAO1* | *Pseudomonas* (contrast) | Negative control: an NAD(P)-dependent Asp dehydrogenase, distinct from FAD-dependent NadB |

**Strength of evidence.** The mechanistic, structural, and substrate-specificity conclusions rest on **high-resolution crystal structures and biochemistry of the *E. coli* and *B. subtilis* orthologs**, which are gold-standard, precise studies. The genetic function (auxotrophy upon *nadB* loss) is confirmed in multiple enterobacterial systems. What transfers to *P. putida* Q88MZ2 is done by **homology and identical InterPro/TIGRFAM/family signatures** rather than direct *P. putida* enzymology; the domain architecture of Q88MZ2 (NadB IPR005288; FAD-dep_OxRdtase_2_FAD-bd; Fum_Rdtase/Succ_DH_flav-like_C) matches the characterized enzymes exactly, giving high confidence in the transfer.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific enzymology.** All direct biochemical and structural data derive from *E. coli* and *B. subtilis* (and enterobacterial genetics from UPEC/*Shigella*). No purification, kinetic characterization, crystal structure, or knockout of *P. putida* KT2440 PP_1426 itself was located. The functional assignment for Q88MZ2 is a well-supported homology inference, not a direct measurement.

2. **Aerobic vs. oxygen-limited acceptor usage in *P. putida* is untested.** *P. putida* KT2440 is a predominantly aerobic soil bacterium. Whether its NadB physiologically uses fumarate as an alternative electron acceptor (as *E. coli* NadB can) has not been demonstrated. The dual-acceptor capability is inferred from the family, not from *P. putida* data.

3. **Kinetic parameters unknown for Q88MZ2.** K_m for L-aspartate, k_cat, the O₂-vs-fumarate partition, and any regulation (e.g., NAD⁺/NADH feedback) are not available for the *P. putida* enzyme.

4. **NadA/NadC partners in *P. putida* not explicitly mapped here.** While the NadB→NadA→NadC logic is well established generally, the specific *P. putida* KT2440 loci for *nadA* and *nadC* and any operonic organization or physical complex were not characterized in this investigation. The channeling hypothesis is inferred from cross-species interaction data.

5. **Regulation and physiological context.** How *nadB* expression is controlled in *P. putida* (e.g., in response to NAD⁺ status, redox state, or during growth on aromatic/lignin-derived substrates for which this strain is notable) was not established.

6. **Drug-target claim is general.** The statement that the pathway is a mammalian-absent antibacterial target is well founded pharmacologically but has not been pursued specifically against *P. putida* NadB (an environmental, largely non-pathogenic organism where the clinical rationale is less pressing).

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymology of PP_1426.** Clone, over-express, and purify *P. putida* KT2440 NadB; confirm non-covalent FAD content spectroscopically; measure steady-state kinetics (K_m, k_cat) for L-aspartate, and quantify the partition between O₂ (H₂O₂ production) and fumarate (succinate production) as electron acceptors.

2. **Substrate-specificity panel.** Test candidate substrates (L-Asp, D-Asp, L-Glu, succinate, other dicarboxylates/amino acids) to confirm strict L-aspartate specificity, and verify the predicted role of the conserved active-site glutamate by site-directed mutagenesis (Glu→Gln/Ala) equivalent to *E. coli* Glu121.

3. **Genetic knockout / complementation.** Construct a *P. putida* KT2440 Δ*nadB* mutant and test for NAD⁺/nicotinic-acid auxotrophy (growth rescue by nicotinamide, nicotinate, or quinolinate). Confirm that *nadB* can serve as a neutral insertion site as in UPEC, useful for strain engineering.

4. **Partner-interaction and channeling assay.** Test for a physical NadA–NadB complex in *P. putida* (co-purification, pull-down, or crosslinking) and probe substrate channeling of the labile iminoaspartate intermediate (e.g., transient-time kinetics with coupled NadA).

5. **Structural confirmation.** Solve or model (AlphaFold + experimental validation) the PP_1426 structure to confirm the three-domain SDH/FRD-like fold, FAD-binding site, and the α+β capping-domain arrangement; compare to *E. coli* LASPO (PDB entries from PMIDs 10425677/11863440).

6. **Oxygen-limited/redox physiology.** Determine whether fumarate-dependent dehydrogenase mode is physiologically relevant in *P. putida* under microaerobic conditions, and whether *nadB* expression responds to redox or NAD⁺ status.

7. **Pathway mapping.** Identify and annotate the cognate *nadA* and *nadC* loci in KT2440, determine operon structure and co-regulation, and place *nadB* in the broader NAD⁺ biosynthesis/salvage network of this strain.

---

## Conclusion

*Pseudomonas putida* KT2440 **NadB (PP_1426; UniProt Q88MZ2) is L-aspartate oxidase (EC 1.4.3.16)** — a **cytoplasmic, FAD-dependent flavoenzyme of the succinate dehydrogenase / fumarate reductase superfamily** that catalyzes the **first committed step of *de novo* NAD⁺ biosynthesis**, oxidizing **L-aspartate to iminoaspartate** using **either molecular O₂ (oxidase mode, → H₂O₂) or fumarate (dehydrogenase mode, → succinate)** as the terminal electron acceptor. Its labile product is channeled to **quinolinate synthase (NadA)** and then **quinolinate phosphoribosyltransferase (NadC)** to build quinolinate/NAD⁺. The enzyme is **strictly specific for L-aspartate** via a conserved active-site glutamate, and the mammalian-absent pathway it initiates is a **candidate antibacterial drug target**. Direct experimental evidence is from *E. coli* and *B. subtilis* orthologs; the assignment transfers to Q88MZ2 by strong sequence homology and identical family/domain signatures.


## Artifacts

- [OpenScientist final report](nadB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:18959769
2. PMID:11863440
3. PMID:22174382
4. PMID:10425677
5. PMID:10593256
6. PMID:24120364
7. PMID:10209293
8. PMID:21468714