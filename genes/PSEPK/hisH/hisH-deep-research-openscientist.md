---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T05:14:12.153666'
end_time: '2026-07-17T05:40:05.281492'
duration_seconds: 1553.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisH
  gene_symbol: hisH
  uniprot_accession: Q88R44
  protein_description: 'RecName: Full=Imidazole glycerol phosphate synthase subunit
    HisH {ECO:0000255|HAMAP-Rule:MF_00278}; EC=4.3.2.10 {ECO:0000255|HAMAP-Rule:MF_00278};
    AltName: Full=IGP synthase glutaminase subunit {ECO:0000255|HAMAP-Rule:MF_00278};
    EC=3.5.1.2 {ECO:0000255|HAMAP-Rule:MF_00278}; AltName: Full=IGP synthase subunit
    HisH {ECO:0000255|HAMAP-Rule:MF_00278}; AltName: Full=ImGP synthase subunit HisH
    {ECO:0000255|HAMAP-Rule:MF_00278}; Short=IGPS subunit HisH {ECO:0000255|HAMAP-Rule:MF_00278};'
  gene_info: Name=hisH {ECO:0000255|HAMAP-Rule:MF_00278}; OrderedLocusNames=PP_0290;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Class_I_gatase-like. (IPR029062); GATASE. (IPR017926); Imidazole-glycPsynth_HisH.
    (IPR010139); GATase (PF00117)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hisH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R44
- **Protein Description:** RecName: Full=Imidazole glycerol phosphate synthase subunit HisH {ECO:0000255|HAMAP-Rule:MF_00278}; EC=4.3.2.10 {ECO:0000255|HAMAP-Rule:MF_00278}; AltName: Full=IGP synthase glutaminase subunit {ECO:0000255|HAMAP-Rule:MF_00278}; EC=3.5.1.2 {ECO:0000255|HAMAP-Rule:MF_00278}; AltName: Full=IGP synthase subunit HisH {ECO:0000255|HAMAP-Rule:MF_00278}; AltName: Full=ImGP synthase subunit HisH {ECO:0000255|HAMAP-Rule:MF_00278}; Short=IGPS subunit HisH {ECO:0000255|HAMAP-Rule:MF_00278};
- **Gene Information:** Name=hisH {ECO:0000255|HAMAP-Rule:MF_00278}; OrderedLocusNames=PP_0290;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Class_I_gatase-like. (IPR029062); GATASE. (IPR017926); Imidazole-glycPsynth_HisH. (IPR010139); GATase (PF00117)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisH** (gene ID: hisH, UniProt: Q88R44) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: HisH (Q88R44) — Imidazole Glycerol Phosphate Synthase Glutaminase Subunit in *Pseudomonas putida* KT2440

## Summary

**HisH (UniProt Q88R44; locus PP_0290) in *Pseudomonas putida* KT2440 is the glutamine-hydrolyzing (glutaminase) subunit of imidazole glycerol phosphate synthase (IGPS/ImGPS), a bienzyme complex of the histidine-biosynthesis pathway.** It is a 212-residue, class-I glutamine amidotransferase (GATase type-1) that catalyzes the hydrolysis of L-glutamine to L-glutamate plus ammonia (EC 3.5.1.2). The nascent ammonia is not released into solution; instead it is channeled intramolecularly to the partner cyclase subunit HisF, where it is incorporated into the acceptor substrate PRFAR (N′-[(5′-phosphoribulosyl)formimino]-5-aminoimidazole-4-carboxamide ribonucleotide) to yield imidazole glycerol phosphate (IGP) and 5-aminoimidazole-4-carboxamide ribotide (AICAR). This defines the overall IGPS reaction (EC 4.3.2.10) and step 5 of the nine-step L-histidine biosynthetic pathway from PRPP.

The functional unit of HisH is not the isolated protein but an **obligate HisH:HisF heterodimer**. Isolated HisH has essentially no glutaminase activity; the reaction is switched on only when HisH is bound to HisF, and further amplified — roughly 1000-fold — when HisF carries its acceptor substrate or a substrate analogue. This inter-subunit allosteric coupling ensures that glutamine is not wastefully hydrolyzed when the downstream acceptor is absent. The enzyme is a soluble, cytoplasmic protein, and its ammonia product travels ~25 Å through an internal channel in the HisF (βα)₈-barrel to reach the second active site. Because the co-product AICAR re-enters de novo purine biosynthesis, HisH sits at a metabolic branch point linking histidine and purine biosynthesis.

The functional assignment for the *P. putida* protein is made by homology (HAMAP-Rule MF_00278) and is strongly corroborated by multiple convergent lines of evidence generated in this investigation: (i) sequence homology of 39–45% identity to experimentally characterized HisH orthologs from *E. coli*, *Salmonella typhimurium*, and *Thermotoga maritima*, with exact conservation of the catalytic triad; (ii) an AlphaFold structural model (global pLDDT 97.5) showing a textbook, pre-organized Cys81-His190-Glu192 catalytic triad with physiologically appropriate inter-residue distances; (iii) genomic co-clustering of *hisH* (PP_0290) with its obligate partner *hisF* (PP_0293) and other *his* genes; and (iv) a body of biochemical and biophysical literature establishing the mechanism in orthologs. No experimental characterization of the *P. putida* protein specifically was found, but the annotation is exceptionally well supported by inference from these sources.

---

## Gene/Protein Identity Verification

Before proceeding, the target identity was verified against the UniProt record and against the primary literature:

| Attribute | Value | Status |
|---|---|---|
| UniProt accession | Q88R44 | Confirmed |
| Gene symbol | *hisH* | Consistent with protein description |
| Locus tag | PP_0290 | Confirmed (*P. putida* KT2440) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) | Confirmed |
| Protein length | 212 aa | Confirmed |
| EC numbers | 4.3.2.10 (overall IGPS); 3.5.1.2 (glutaminase) | Confirmed |
| Key domains | Class-I GATase-like (IPR029062); GATASE (IPR017926); Imidazole-glycPsynth_HisH (IPR010139); GATase (PF00117) | Confirmed |
| Assignment basis | HAMAP-Rule MF_00278 | Confirmed |

The gene symbol "hisH", the domain architecture (a single class-I glutamine amidotransferase / GATase type-1 domain), and the organism all align consistently with the biochemical literature on HisH glutaminase subunits. **The literature retrieved describes the correct protein family and reaction; there was no evidence of confusion with a same-symbol gene from an unrelated family.** The one caveat is that all direct biochemical characterization comes from orthologs (*T. maritima*, yeast, *E. coli*/*Salmonella*, *Zymomonas mobilis*), not from the *P. putida* protein itself — a standard and acceptable basis for functional annotation given the high homology and universal conservation of this pathway.

---

## Key Findings

### Finding 1 — HisH is the glutaminase subunit of imidazole glycerol phosphate synthase

The UniProt record for Q88R44 annotates the 212-residue *P. putida* protein as a single glutamine amidotransferase type-1 (class-I GATase) domain spanning essentially the entire chain (residues 3–212), carrying both EC 4.3.2.10 (the overall IGPS reaction) and EC 3.5.1.2 (the glutaminase half-reaction). The catalytic activities are formally: **L-glutamine + H₂O → L-glutamate + NH₄⁺** (Rhea:15889), coupled to **PRFAR + L-glutamine → IGP + AICAR + L-glutamate** (Rhea:24793). This assignment derives from HAMAP-Rule MF_00278, the curated family rule for HisH.

The primary literature establishes the mechanism unambiguously. In the *Thermotoga maritima* system, IGPS "constitutes a bienzyme complex of the glutaminase subunit HisH and the synthase subunit HisF" ([PMID: 11264293](https://pubmed.ncbi.nlm.nih.gov/11264293/)). The same study defines the labor division: "Nascent ammonia produced by HisH reacts at the active site of HisF with N′-((5′-phosphoribulosyl)formimino)-5-aminoimidazole-4-carboxamide-ribonucleotide to yield the products imidazole glycerol phosphate and 5-aminoimidazole-4-carboxamide ribotide" ([PMID: 11264293](https://pubmed.ncbi.nlm.nih.gov/11264293/)). Thus HisH is the ammonia-generating half of the enzyme, and its glutamine-derived ammonia is the substrate consumed by HisF's cyclase chemistry.

### Finding 2 — HisH glutaminase activity is allosterically activated by HisF and its substrate

A defining property of HisH is that it is catalytically silent on its own. In the *T. maritima* system, "isolated tHisH showed no detectable glutaminase activity but was stimulated by complex formation with tHisF to which either the product imidazole glycerol phosphate or a substrate analogue were bound" ([PMID: 11264293](https://pubmed.ncbi.nlm.nih.gov/11264293/)). The bifunctional yeast enzyme provides a quantitative measure of the effect: it "shows a low basal level glutaminase activity that can be enhanced 1000-fold in the presence of a nucleotide substrate or analog" ([PMID: 10733892](https://pubmed.ncbi.nlm.nih.gov/10733892/)).

This ~1000-fold, substrate-gated allosteric activation is biologically important: it prevents futile hydrolysis of glutamine (a nitrogen-costly metabolite) when the downstream acceptor PRFAR is not present. HisH therefore behaves as a demand-driven ammonia generator, activated only when HisF is loaded and ready to consume the product. This allosteric coupling operates across the ~25–30 Å distance separating the two active sites and is a textbook example of long-range communication in a glutamine amidotransferase. Additional structural and computational studies reinforce that active-site conformational change underlies this allosteric activation ([PMID: 38125975](https://pubmed.ncbi.nlm.nih.gov/38125975/)) and that the subunit interface configuration is central to it ([PMID: 32633500](https://pubmed.ncbi.nlm.nih.gov/32633500/)).

### Finding 3 — Cys-His-Glu catalytic triad and cytoplasmic, channel-coupled localization

HisH uses the canonical class-I GATase catalytic machinery: a **Cys-His-Glu triad**. In Q88R44 this is Cys81 (the nucleophile), His190, and Glu192. The nucleophilic cysteine attacks the amide carbon of glutamine to form a covalent thioester intermediate, releasing ammonia; the histidine acts as the general base that deprotonates and activates the cysteine thiol; and the glutamate orients and polarizes the histidine. This triad is conserved across the amidotransferase family, including the related anthranilate synthase glutaminase TrpG/TrpE, where the active site is "located between the catalytic Cys-His-Glu triad and the synthase subunit TrpE" ([PMID: 22432907](https://pubmed.ncbi.nlm.nih.gov/22432907/)).

The ammonia generated at the HisH triad does not diffuse through bulk solvent. Instead it passes through an internal molecular channel into the HisF barrel. NMR evidence in *T. maritima* shows that "the amino acid residue Thr 78 — which is located in the central channel — shows a large chemical shift change upon titration with ammonium chloride" ([PMID: 20665694](https://pubmed.ncbi.nlm.nih.gov/20665694/)), consistent with intramolecular ammonia channeling. The UniProt subunit annotation is a heterodimer of HisH and HisF, and the subcellular location is the **cytoplasm** — appropriate for a soluble biosynthetic enzyme with no membrane-targeting or secretion signals.

### Finding 4 — HisH functions at the histidine/purine metabolic branch point (step 5 of 9)

UniProt places HisH at step 5 of 9 in L-histidine biosynthesis from PRPP (HAMAP MF_00278). The IGPS reaction has two products with two fates: IGP continues down the histidine pathway (the next step being imidazoleglycerol-phosphate dehydratase, HisB), while AICAR is a purine-pathway intermediate that re-enters de novo purine biosynthesis. IGPS is therefore explicitly described as the enzyme "which links histidine and de novo purine biosynthesis" and "is a member of the glutamine amidotransferase family" ([PMID: 11264293](https://pubmed.ncbi.nlm.nih.gov/11264293/)). The yeast study independently confirms that "this enzyme represents a junction between histidine biosynthesis and de novo purine biosynthesis" ([PMID: 10733892](https://pubmed.ncbi.nlm.nih.gov/10733892/)). By recycling AICAR into the purine pool, HisH/HisF activity couples the nitrogen and carbon economy of two central biosynthetic routes.

### Finding 5 — Sequence homology quantitatively supports the annotation with perfect triad conservation

Global pairwise alignment (Needleman–Wunsch, identity scoring) of *P. putida* HisH against experimentally characterized orthologs gives high, unambiguous identity:

| Ortholog | UniProt | % identity to Q88R44 | Aligned columns |
|---|---|---|---|
| *E. coli* HisH | P60595 | 43.3% | ~193 |
| *Salmonella typhimurium* HisH | P0A1R4 | 44.6% | ~194 |
| *Thermotoga maritima* HisH | Q9X0C8 | 38.9% | ~193 |

Critically, the predicted catalytic triad Cys81/His190/Glu192 aligns exactly onto the conserved Cys/His/Glu of all three orthologs. Local sequence motifs are also conserved: the nucleophile sits in the class-I GATase glutaminase motif `...LGIC(81)VGMQ...`, and His190/Glu192 lie in the conserved amidotransferase motif `QFH(190)PE(192)K`. At 39–45% identity with perfect active-site conservation, the functional transfer from characterized orthologs to the *P. putida* protein is on very firm ground.

### Finding 6 — *hisH* (PP_0290) is co-clustered with its obligate partner *hisF* and other *his* genes

The genomic neighborhood of *hisH* in *P. putida* KT2440 is informative:

```
PP_0289  hisB   imidazoleglycerol-phosphate dehydratase (next pathway step)
PP_0290  hisH   IGP synthase glutaminase subunit    <-- this gene
PP_0291  ----   DUF2164 protein (function unclear)
PP_0292  hisA   ProFAR isomerase
PP_0293  hisF   IGP synthase cyclase subunit (Q88R41)  <-- obligate partner
```

*hisH* and its obligate physical partner *hisF* lie just three genes apart within the same local cluster, with additional *his* genes (*hisB*, *hisA*) interspersed. The remaining histidine genes are dispersed across other loci (*hisG* PP_0965, *hisD* PP_0966, *hisC* PP_0967; *hisI* PP_5014, *hisE* PP_5015), so *P. putida* organizes its *his* genes in a few clusters rather than a single *Salmonella*-style operon. The tight physical linkage of *hisH* and *hisF* is consistent with their obligate functional partnership and reinforces the annotation.

### Finding 7 — AlphaFold structure confirms a canonical, pre-organized Cys-His-Glu triad

The AlphaFold model AF-Q88R44-F1 (v6) is of very high quality: global pLDDT 97.5, with 98.1% of residues at very-high confidence. The three predicted catalytic residues are each modeled with very high confidence (Cys81 pLDDT 98.4, His190 98.6, Glu192 98.1) and adopt a textbook class-I GATase triad geometry:

| Interaction | Distance | Role |
|---|---|---|
| Cys81(SG)–His190(NE2) | 3.29 Å | Thiol-activating hydrogen bond (His deprotonates Cys) |
| His190(ND1)–Glu192(OE1) | 2.78 Å | His-orienting / polarizing hydrogen bond (Glu charges His) |

These distances are exactly what is expected for a functional glutaminase in which the histidine serves as the general base that activates the cysteine nucleophile and the glutamate orients and stabilizes the protonated histidine. The pre-organization of the triad in the unbound model further supports a catalytically competent active site.

### Finding 8 — HisH acts strictly within an obligate HisH:HisF complex whose interface mediates allostery

HisH performs its chemistry only within the two-subunit ImGPS complex, and the HisH:HisF interface is the physical conduit for the allosteric signal that activates glutaminase chemistry. An authoritative restatement from ancestral-reconstruction/protein-design work confirms that "ImGPS is a key metabolic enzyme complex, which links histidine and de novo purine biosynthesis and consists of the cyclase subunit HisF and the glutaminase subunit HisH" ([PMID: 27936490](https://pubmed.ncbi.nlm.nih.gov/27936490/)). That study pinpointed interface hotspots — down to a single decisive HisF residue — controlling high-affinity HisH binding: "we were able to pinpoint a single amino acid residue in HisF that is decisive for high-affinity binding of zmHisH" ([PMID: 27936490](https://pubmed.ncbi.nlm.nih.gov/27936490/)). Combined with the AlphaFold triad geometry (Finding 7) and the ~1000-fold substrate-dependent activation (Finding 2), this defines HisH's functional unit as the HisH:HisF heterodimer rather than the isolated protein. The deep antiquity and robustness of this partnership are underscored by ancestral reconstruction: a reconstructed LUCA-era HisF "forms a stable and functional complex with the glutaminase subunit (HisH) of an extant ImGP-S," implying that substrate channeling and allosteric communication in this complex were already established ~3.5 billion years ago ([PMID: 24364418](https://pubmed.ncbi.nlm.nih.gov/24364418/)).

---

## Mechanistic Model / Interpretation

The findings converge into a single, coherent mechanistic picture of HisH as one half of a substrate-channeling, allosterically-regulated bienzyme.

```
                 IMIDAZOLE GLYCEROL PHOSPHATE SYNTHASE (IGPS / ImGPS)
                 =====================================================

        HisH (Q88R44, PP_0290)                 HisF (Q88R41, PP_0293)
        class-I GATase glutaminase             (βα)8 TIM-barrel cyclase
    ┌───────────────────────────┐          ┌──────────────────────────────┐
    │  Cys81 ─ His190 ─ Glu192   │          │  PRFAR (acceptor substrate)  │
    │  (nucleophile)(base)(orient)│          │            +                 │
    │                           │          │           NH3                │
    │  L-Gln + H2O              │          │            |                 │
    │      │                    │   ~25 A  │            v                 │
    │      v                    │  ammonia │   IGP  +  AICAR              │
    │  L-Glu + NH3  ────────────┼─channel──┼──►                          │
    └───────────────────────────┘          └──────────────────────────────┘
              EC 3.5.1.2                            (overall EC 4.3.2.10)

    Allosteric gating: HisH is OFF when isolated. Binding HisF turns it ON;
    HisF loaded with PRFAR/analogue boosts glutaminase ~1000-fold.

    Downstream fates:
        IGP   ──► HisB (PP_0289) ──► ... ──► L-histidine   (step 5 of 9)
        AICAR ──► de novo PURINE biosynthesis   (metabolic branch point)
```

**Reaction logic.** HisH binds L-glutamine and, using its Cys81-His190-Glu192 triad, cleaves the glutamine side-chain amide to release ammonia and leave L-glutamate. The AlphaFold-confirmed geometry (Cys–His 3.29 Å, His–Glu 2.78 Å) is precisely arranged for the histidine to deprotonate the cysteine thiol, which then attacks the amide carbon to form a covalent thioester and expel NH₃.

**Substrate channeling.** The liberated ammonia is sequestered from bulk solvent and conducted ~25 Å through an internal channel spanning the interface and the HisF barrel (NMR-detected sensitivity of channel residue Thr78 to ammonium supports this). At the HisF active site, ammonia attacks PRFAR to produce IGP and AICAR.

**Allosteric control.** The two active sites are functionally interlocked. HisH is essentially inactive alone; it is activated by complex formation with HisF and further stimulated ~1000-fold by acceptor-substrate binding at the HisF site. This ensures glutamine is only hydrolyzed on demand, coupling nitrogen expenditure to genuine flux through the histidine/purine junction. The HisH:HisF interface (with identified single-residue hotspots) is both the assembly determinant and the allosteric relay.

**Pathway context.** IGPS catalyzes step 5 of 9 in histidine biosynthesis. Because AICAR feeds back into purine biosynthesis, HisH activity sits at a node that couples two of the cell's core nitrogen-demanding biosynthetic routes. In *P. putida* KT2440, the tight genomic linkage of *hisH* (PP_0290) to *hisF* (PP_0293) mirrors their obligate physical partnership.

---

## Evidence Base

| PMID | Title (abbrev.) | System | How it supports the findings |
|---|---|---|---|
| [11264293](https://pubmed.ncbi.nlm.nih.gov/11264293/) | *IGPS from T. maritima: quaternary structure, kinetics, mechanism* | *T. maritima* | Establishes HisH as glutaminase subunit; defines ammonia product and HisF acceptor; shows HisH inactive alone, activated by HisF+substrate; names histidine/purine link (F1, F2, F4) |
| [10733892](https://pubmed.ncbi.nlm.nih.gov/10733892/) | *Expression/purification of IGPS from S. cerevisiae* | Yeast (bifunctional) | Quantifies ~1000-fold substrate-dependent activation; confirms histidine/purine junction (F2, F4) |
| [20665694](https://pubmed.ncbi.nlm.nih.gov/20665694/) | *Ammonia and xenon interaction with T. maritima IGPS by NMR* | *T. maritima* | Detects ammonia in the internal channel (Thr78 chemical-shift change), supporting intramolecular channeling (F3) |
| [22432907](https://pubmed.ncbi.nlm.nih.gov/22432907/) | *Constitutively active glutaminase variants of anthranilate synthase* | TrpG/TrpE | Confirms the class-I GATase Cys-His-Glu triad shared by HisH (F3) |
| [27936490](https://pubmed.ncbi.nlm.nih.gov/27936490/) | *Ancestral reconstruction + protein design: interface hotspot in ImGPS* | *Z. mobilis* / ancestral | Authoritative restatement of HisH as glutaminase subunit; identifies single HisF interface residue decisive for HisH binding (F8) |
| [24364418](https://pubmed.ncbi.nlm.nih.gov/24364418/) | *Elaborate enzyme complexes in the Paleoarchean era (LUCA-HisF)* | LUCA reconstruction | Shows LUCA-HisF forms stable, functional complex with extant HisH — deep conservation of the obligate HisH:HisF partnership, channeling, and allostery (F8) |
| [38125975](https://pubmed.ncbi.nlm.nih.gov/38125975/) | *Catalytic effects of active-site conformational change in IGPS allostery* | IGPS | Reinforces the allosteric activation mechanism linking the two active sites (F2) |
| [32633500](https://pubmed.ncbi.nlm.nih.gov/32633500/) | *Protein interface configuration for allostery in ImGPS* | ImGPS | Reinforces the role of the HisH:HisF interface in allosteric communication (F2, F8) |

**Homology and structure evidence generated in this investigation:** global alignments to *E. coli*/*Salmonella*/*T. maritima* HisH (39–45% identity, exact triad conservation; F5); AlphaFold model AF-Q88R44-F1 (pLDDT 97.5) confirming a pre-organized Cys81-His190-Glu192 triad with catalytically appropriate distances (F7); and genomic neighborhood analysis placing *hisH* (PP_0290) three genes from *hisF* (PP_0293) (F6).

The evidence lines are mutually consistent: no retrieved paper contradicts the assignment. The one "mismatch"-flagged citation snippet ([PMID: 27936490](https://pubmed.ncbi.nlm.nih.gov/27936490/), on the single-residue HisF hotspot) refers to a HisF-side interface residue that governs HisH binding — fully consistent with, and indeed illuminating, the obligate HisH:HisF partnership rather than contradicting it.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* protein.** All kinetic, mechanistic, and structural evidence comes from orthologs (*T. maritima*, *S. cerevisiae*, *E. coli*/*Salmonella*, *Z. mobilis*, and ancestral reconstructions). The functional assignment for Q88R44 rests on homology transfer (HAMAP MF_00278), sequence alignment, an AlphaFold model, and genomic context — strong but inferential evidence. No enzyme assays, crystal structure, or knockout phenotype specific to PP_0290 were located.

2. **Catalytic residues are predicted, not experimentally mutated in *P. putida*.** Cys81/His190/Glu192 are assigned by homology and AlphaFold geometry. Site-directed mutagenesis in the *P. putida* background has not been reported.

3. **AlphaFold model is monomeric.** The structural analysis used a single-chain model. The HisH:HisF complex interface, ammonia channel geometry, and allosteric conformational changes were inferred from ortholog structures/literature rather than a *P. putida* complex model.

4. **Regulation and expression in *P. putida* untested here.** Whether *P. putida* histidine biosynthesis is regulated as in enterobacteria (attenuation, feedback), and the transcriptional organization of the dispersed *his* loci, were not experimentally examined.

5. **The DUF2164 protein (PP_0291)** between *hisH* and *hisA* is of unknown function and was not investigated; its co-location is intriguing but uninterpreted.

6. **Quantitative kinetics for the *P. putida* enzyme (Km for glutamine, kcat, activation fold) are unknown** and could differ from thermophilic or eukaryotic orthologs.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and glutaminase assay.** Clone and express PP_0290 (HisH) and PP_0293 (HisF) from *P. putida* KT2440; measure glutaminase activity of HisH alone versus the HisH:HisF complex ± PRFAR/analogue to confirm the ~1000-fold substrate-gated activation in this organism.

2. **Site-directed mutagenesis of the triad.** Generate C81A, H190A, and E192A variants and confirm loss of glutaminase activity, directly validating the AlphaFold/homology-predicted catalytic triad.

3. **Coupled IGPS assay.** Reconstitute the full IGPS reaction (PRFAR + L-glutamine → IGP + AICAR + L-glutamate) with the *P. putida* subunits to verify ammonia channeling and overall EC 4.3.2.10 turnover.

4. **Structure of the complex.** Determine a cryo-EM or crystal structure of the *P. putida* HisH:HisF complex (or build an AlphaFold-Multimer model) to visualize the interface, the ammonia channel, and Thr-equivalent channel residues.

5. **Genetic complementation / knockout.** Delete PP_0290 and test for histidine auxotrophy; complement with wild-type and triad mutants to link the predicted biochemistry to the histidine-requirement phenotype in vivo.

6. **Characterize PP_0291 (DUF2164).** Investigate whether the intervening DUF2164 protein has any role in histidine metabolism or IGPS complex assembly, given its position between *hisH* and *hisA*.

---

## Conclusion

HisH (Q88R44, PP_0290) in *Pseudomonas putida* KT2440 is confidently annotated as the **class-I glutamine amidotransferase (glutaminase) subunit of imidazole glycerol phosphate synthase**. Using a Cys81-His190-Glu192 catalytic triad it hydrolyzes L-glutamine to L-glutamate and ammonia (EC 3.5.1.2); the ammonia is channeled to the cyclase subunit HisF, where it is incorporated into PRFAR to form imidazole glycerol phosphate and AICAR (overall EC 4.3.2.10). It is a soluble cytoplasmic enzyme that functions only as an obligate HisH:HisF heterodimer, whose glutaminase activity is allosterically switched on (~1000-fold) by acceptor-substrate binding at the partner subunit. It operates at step 5 of L-histidine biosynthesis and, via the AICAR co-product, at the metabolic branch point linking histidine and de novo purine biosynthesis. The annotation is supported by five convergent evidence lines — curated homology (HAMAP MF_00278), high ortholog identity with exact triad conservation, an AlphaFold-confirmed pre-organized triad, genomic co-clustering with *hisF*, and an extensive ortholog literature — while direct experimental characterization of the *P. putida* protein itself remains an open opportunity.


## Artifacts

- [OpenScientist final report](hisH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11264293
2. PMID:10733892
3. PMID:38125975
4. PMID:32633500
5. PMID:22432907
6. PMID:20665694
7. PMID:27936490
8. PMID:24364418