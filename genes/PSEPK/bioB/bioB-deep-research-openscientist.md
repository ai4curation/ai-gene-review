---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T07:06:03.675506'
end_time: '2026-07-17T07:29:57.218638'
duration_seconds: 1433.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: bioB
  gene_symbol: bioB
  uniprot_accession: Q88QX2
  protein_description: 'RecName: Full=Biotin synthase {ECO:0000255|HAMAP-Rule:MF_01694};
    EC=2.8.1.6 {ECO:0000255|HAMAP-Rule:MF_01694};'
  gene_info: Name=bioB {ECO:0000255|HAMAP-Rule:MF_01694}; OrderedLocusNames=PP_0362;
    ORFNames=PP0362;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the radical SAM superfamily. Biotin synthase
  protein_domains: Aldolase_TIM. (IPR013785); BATS_dom. (IPR010722); Biotin_synth/BioAB.
    (IPR002684); Biotin_synthase. (IPR024177); Elp3/MiaA/NifB-like_rSAM. (IPR006638)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bioB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bioB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QX2
- **Protein Description:** RecName: Full=Biotin synthase {ECO:0000255|HAMAP-Rule:MF_01694}; EC=2.8.1.6 {ECO:0000255|HAMAP-Rule:MF_01694};
- **Gene Information:** Name=bioB {ECO:0000255|HAMAP-Rule:MF_01694}; OrderedLocusNames=PP_0362; ORFNames=PP0362;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the radical SAM superfamily. Biotin synthase
- **Key Domains:** Aldolase_TIM. (IPR013785); BATS_dom. (IPR010722); Biotin_synth/BioAB. (IPR002684); Biotin_synthase. (IPR024177); Elp3/MiaA/NifB-like_rSAM. (IPR006638)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "bioB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'bioB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **bioB** (gene ID: bioB, UniProt: Q88QX2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *bioB* (Biotin Synthase, UniProt Q88QX2) in *Pseudomonas putida* KT2440

## Summary

The gene **bioB** (ordered locus **PP_0362**; UniProt accession **Q88QX2**) of *Pseudomonas putida* KT2440 encodes **biotin synthase** (EC 2.8.1.6), a member of the **radical S-adenosylmethionine (radical-SAM) superfamily**. Its primary and essentially exclusive function is to catalyze the **terminal step of de novo biotin (vitamin B7/H) biosynthesis**: the insertion of a single sulfur atom between the unactivated C6 and C9 carbons of **dethiobiotin (DTB)** to close the thiophane (thiolane) ring and produce **biotin**. This is the last chemical transformation in the conserved bacterial biotin biosynthetic pathway (pimeloyl-CoA → KAPA → DAPA → dethiobiotin → biotin), and BioB acts immediately downstream of dethiobiotin synthetase (BioD).

Mechanistically, BioB is a **cytoplasmic homodimer** in which each monomer carries **two distinct iron–sulfur clusters** housed within a partial (βα)₈ TIM-barrel fold. A catalytic **[4Fe-4S] cluster**, ligated by the diagnostic radical-SAM **CxxxCxxC motif** (Cys59/Cys63/Cys66 in Q88QX2), reductively cleaves two molecules of SAM to generate two highly oxidizing **5′-deoxyadenosyl radicals**. These radicals abstract hydrogen atoms from the substrate's saturated C6 and C9 carbons, producing dethiobiotinyl carbon radicals that are quenched by sulfur derived from an **auxiliary [2Fe-2S] cluster**. This second cluster — coordinated by an unusual **three-cysteine/one-arginine** ligand set (Cys103/Cys134/Cys194/Arg266 in Q88QX2) — is **sacrificed** during catalysis: its bridging μ-sulfide becomes the sulfur atom inserted into biotin, passing through the covalent intermediate **9-mercaptodethiobiotin (MDTB)**. Because the sulfur donor cluster is consumed rather than catalytically regenerated within a single active site, purified BioB behaves as a near single-turnover ("suicide") enzyme in vitro, and sustained biotin production in vivo requires continual **re-assembly of the [2Fe-2S] cluster by the cell's Fe-S biogenesis machinery** and a supply of reducing equivalents from an external electron donor (reduced ferredoxin/flavodoxin).

The physiological importance of BioB derives entirely from its product: **biotin is the essential prosthetic group of the biotin-dependent carboxylases** (e.g., acetyl-CoA carboxylase, pyruvate carboxylase) and transcarboxylases. Thus BioB indirectly but critically supports fatty-acid biosynthesis and central carbon/anaplerotic metabolism. The identity of Q88QX2 as a bona fide biotin synthase — rather than a mis-annotated paralog — is strongly supported by direct sequence analysis of the diagnostic motifs, by organism-specific database curation (UniProt/KEGG/BioCyc for PP_0362), and by extensive biochemical and structural characterization of the orthologous *Escherichia coli* and *Bacillus sphaericus* enzymes.

---

## Gene/Protein Identity Verification

The mandatory identity checks were completed and passed:

- **UniProt accession:** Q88QX2
- **Gene symbol:** *bioB* — matches the protein description "Biotin synthase."
- **Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950), locus PP_0362 — confirmed via KEGG (ppu:PP_0362), BioCyc, and eggNOG (COG0502).
- **Protein family:** radical SAM superfamily, biotin synthase family — confirmed by sequence motif analysis.
- **Key domains:** Aldolase_TIM (IPR013785), BATS_dom (IPR010722), Biotin_synth/BioAB (IPR002684), Biotin_synthase (IPR024177), Elp3/MiaA/NifB-like_rSAM (IPR006638) — all consistent with biotin synthase.

No conflicting literature for a different gene of the same symbol was encountered. The gene symbol *bioB* is unambiguous for biotin synthase across bacteria. The functional assignment below is drawn from direct biochemistry on orthologs plus sequence and database evidence specific to Q88QX2.

---

## Key Findings

### Finding 1 — BioB is biotin synthase, catalyzing the terminal step of biotin biosynthesis (dethiobiotin → biotin)

Q88QX2 is annotated (HAMAP-Rule MF_01694) as biotin synthase, EC 2.8.1.6, a member of the radical-SAM superfamily. The reaction it catalyzes is the conversion of dethiobiotin to biotin by insertion of a sulfur atom between C6 and C9 of the substrate in a SAM-dependent reaction. The overall stoichiometry is:

> **dethiobiotin + 2 SAM + sulfur source → biotin + 2 L-methionine + 2 5′-deoxyadenosine**

This chemistry is biochemically established for the orthologous enzymes. As stated directly in the primary literature: *"Biotin synthase (BioB) converts dethiobiotin into biotin by inserting a sulfur atom between C6 and C9 of dethiobiotin in an S-adenosylmethionine (SAM)-dependent reaction"* ([PMID: 14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/)). A second study confirms family membership and the reaction: *"Biotin synthase, a member of the 'radical-SAM' family, produces biotin by inserting a sulfur atom between C-6 and C-9 of dethiobiotin"* ([PMID: 15610037](https://pubmed.ncbi.nlm.nih.gov/15610037/)). These statements identify the substrate (dethiobiotin), the product (biotin), the chemistry (C6–C9 sulfur insertion), and the SAM dependence unambiguously.

### Finding 2 — A catalytic [4Fe-4S] cluster reductively cleaves SAM into 5′-deoxyadenosyl radicals that abstract H from DTB C6 and C9

The signature reaction of all radical-SAM enzymes is the reductive one-electron cleavage of SAM to generate a 5′-deoxyadenosyl radical. In BioB, Mössbauer and EPR studies of the *E. coli* enzyme show that a **[4Fe-4S]²⁺ cluster** is stable during turnover and present in the SAM-bound form. Its role is explicit: *"the functional role of the [4Fe-4S] cluster is to bind SAM and facilitate the reductive cleavage of SAM to generate the catalytically essential 5′-deoxyadenosyl radical"* ([PMID: 14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/)).

Because the substrate has **two** saturated carbons (C6 and C9) that must each be functionalized, **two** deoxyadenosyl radicals — and therefore two SAM molecules — are consumed per biotin produced: *"Each of the two saturated carbon atoms is activated through homolytic cleavage of a C-H bond by a deoxyadenosyl radical, issued from the monoelectronic reduction of S-adenosylmethionine (SAM or AdoMet)"* ([PMID: 15610037](https://pubmed.ncbi.nlm.nih.gov/15610037/)). This 2:1 SAM:biotin stoichiometry is a defining kinetic feature of the enzyme.

### Finding 3 — The inserted sulfur derives from a sacrificial auxiliary [2Fe-2S] cluster, via the intermediate 9-mercaptodethiobiotin

The origin of the sulfur atom inserted into biotin was historically contentious, but is now settled. As-purified recombinant *E. coli* BioB is a homodimer bearing one **[2Fe-2S]²⁺ cluster per monomer**, and during turnover a large fraction of these clusters are destroyed — consistent with the cluster's bridging sulfide being consumed as the sulfur source. The modern consensus is stated plainly in a 2024 review: *"it is now widely accepted that the sulfur atom inserted to form biotin stems from the sacrifice of the auxiliary 2Fe-2S cluster of BioB"* ([PMID: 38215281](https://pubmed.ncbi.nlm.nih.gov/38215281/)).

Mechanistically, the first carbon radical is quenched by sulfur to form a covalent monothio intermediate: *"which is then quenched by a sulfur atom to form a new carbon-sulfur bond in the intermediate 9-mercaptodethiobiotin (MDTB). We have proposed that this sulfur atom is the μ-sulfide of a [2Fe-2S]²⁺ cluster found near DTB in the enzyme active site"* ([PMID: 21859080](https://pubmed.ncbi.nlm.nih.gov/21859080/)). Direct evidence for cluster consumption comes from turnover experiments: *"approximately ⅔ of the [2Fe-2S] clusters are degraded by the end of the turnover experiment"* ([PMID: 14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/)). Because the sulfur-donor cluster is destroyed and not internally regenerated, the isolated enzyme is effectively a single-turnover catalyst: *"the enzyme produces only 1 mol of biotin per enzyme monomer"* ([PMID: 15610037](https://pubmed.ncbi.nlm.nih.gov/15610037/)). This "suicide enzyme" behavior in vitro is the basis for the in vivo dependence on Fe-S regeneration described in Finding 6.

### Finding 4 — BioB is a cytoplasmic homodimeric radical-SAM enzyme, each monomer binding one [4Fe-4S] and one [2Fe-2S] cluster

The quaternary structure and cofactor content are well defined: *"The as-purified recombinant BioB from Escherichia coli is a homodimeric molecule containing one [2Fe-2S]²⁺ cluster per monomer"* ([PMID: 14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/)); anaerobic reconstitution installs an additional [4Fe-4S]²⁺ per monomer to generate the fully active form. Biotin synthase was among the first soluble radical-SAM enzymes to be structurally characterized: *"the first X-ray structures of SAM radical enzymes, coproporphyrinogen-III oxidase, and biotin synthase have been solved"* ([PMID: 15381399](https://pubmed.ncbi.nlm.nih.gov/15381399/)), consistent with a soluble, cytoplasmic protein. UniProt/HAMAP assigns cytoplasmic localization to Q88QX2, and its InterPro domain architecture — Aldolase_TIM (TIM barrel, IPR013785), Biotin_synth/BioAB (IPR002684), BATS domain (IPR010722), and the Elp3/MiaA/NifB-like radical-SAM domain (IPR006638) — precisely matches the biotin synthase fold.

### Finding 5 — BioB catalyzes the terminal step of the bio-operon pathway; its product biotin is the essential prosthetic group of carboxylases

Biotin biosynthesis proceeds through a conserved multi-enzyme pathway (pimeloyl-CoA → 7-keto-8-aminopelargonic acid [KAPA] → 7,8-diaminopelargonic acid [DAPA] → dethiobiotin → biotin), with the genes typically clustered into *bio* operons that are tightly regulated because biotin synthesis is metabolically expensive. BioB acts **last**, converting dethiobiotin (the product of dethiobiotin synthetase, BioD) to biotin. The downstream role of the product is well established: *"The vitamin biotin is a ubiquitous prosthetic group of carboxylase and transcarboxylase enzymes. Biotin biosynthesis occurs by similar pathways in microorganisms and plants"* ([PMID: 8591031](https://pubmed.ncbi.nlm.nih.gov/8591031/)). The pathway's organization and regulation are also documented: *"Biotin is an essential metabolic cofactor and de novo biotin biosynthetic pathways are widespread in microorganisms and plants. Biotin synthetic genes are generally found clustered into bio operons to facilitate tight regulation since biotin synthesis is a metabolically expensive process"* ([PMID: 34597430](https://pubmed.ncbi.nlm.nih.gov/34597430/)). In *P. putida* KT2440, the biotin synthase ortholog is PP_0362 (*bioB*).

### Finding 6 — In vivo catalytic recycling requires Fe-S cluster regeneration and an external electron donor; BioB is a rate-limiting bottleneck

Because the [2Fe-2S] cluster is consumed as the sulfur donor, sustained biotin production in the cell requires cluster re-assembly by the **ISC/SUF Fe-S biogenesis systems**. Engineering studies establish BioB as the rate-limiting step and reveal the mechanistic basis of its overexpression toxicity: *"For biotin, the main bottleneck is biotin synthase, BioB, a S-adenosyl methionine-dependent radical enzyme that converts dethiobiotin (DTB) to biotin. BioB overexpression is toxic, though the mechanism remains unclear"* ([PMID: 32220614](https://pubmed.ncbi.nlm.nih.gov/32220614/)). The same study attributes toxicity to iron-sulfur demand: *"FeS-cluster depletion is the main reason for toxicity"* ([PMID: 32220614](https://pubmed.ncbi.nlm.nih.gov/32220614/)); mutating the global Fe-S regulator IscR relieved toxicity and increased DTB-to-biotin biocatalysis more than 2.2-fold.

The reductive half of the mechanism also requires an external one-electron donor to poise the catalytic cluster for SAM cleavage: *"An electron is transferred from an electron donor to the [4Fe-4S]²⁺-SAM complex to produce the catalytically active [4Fe-4S]⁺ state"* ([PMID: 21497584](https://pubmed.ncbi.nlm.nih.gov/21497584/)). In vivo this donor is reduced flavodoxin/ferredoxin.

### Finding 7 — The P. putida sequence carries the diagnostic radical-SAM and biotin-synthase-specific cluster-ligand motifs, confirming orthology

Direct sequence analysis of Q88QX2 (a 352-residue protein with a radical-SAM core spanning residues ~44–262) confirms it is a genuine biotin synthase and not a mis-annotated paralog. The canonical radical-SAM **CxxxCxxC** motif is present at Cys59–Cys63–Cys66 (in the region 57-GACPEDCKYCPQ-68), ligating the catalytic [4Fe-4S] cluster (matching UniProt binding-site annotations at residues 59/63/66). The auxiliary [2Fe-2S] cluster is coordinated by the biotin-synthase hallmark **three-cysteine/one-arginine** set: Cys103, Cys134, Cys194, and Arg266 — equivalent to *E. coli* Cys97/Cys128/Cys188/Arg260. The arginine ligand is an experimentally verified, unusual feature of this enzyme family: *"Mutation of Arg260, one of the ligands to the [2Fe-2S] cluster, causes a distinctive change in the EPR spectrum"* ([PMID: 21859080](https://pubmed.ncbi.nlm.nih.gov/21859080/)). The presence of both diagnostic motifs at the expected positions provides strong bioinformatic confirmation of orthology to characterized BioB enzymes.

### Finding 8 — The crystal structure places dethiobiotin between the two clusters, structurally rationalizing radical generation and sulfur insertion

The 3.4 Å X-ray structure of *E. coli* biotin synthase in complex with SAM and dethiobiotin (Berkovitch et al., *Science* 2004) resolved the spatial logic of the mechanism. The enzyme adopts a (βα)₈ TIM-barrel fold in which the substrate is sandwiched between the two metallocofactors: *"The structure places the substrates between the Fe4S4 cluster, essential for radical generation, and the Fe2S2 cluster, postulated to be the source of sulfur, with both clusters in unprecedented coordination environments"* ([PMID: 14704425](https://pubmed.ncbi.nlm.nih.gov/14704425/)). The same study confirms the reaction: *"Biotin synthase catalyzes the radical-mediated insertion of sulfur into dethiobiotin to form biotin"* ([PMID: 14704425](https://pubmed.ncbi.nlm.nih.gov/14704425/)). This arrangement explains how the deoxyadenosyl radical from SAM cleavage at the [4Fe-4S] side abstracts DTB C6/C9 hydrogens, and how the resulting carbon radicals are quenched by the μ-sulfide of the adjacent [2Fe-2S] cluster.

### Finding 9 — Organism-specific curation confirms Q88QX2/PP_0362 as the final-step biotin synthase in P. putida KT2440, with ferredoxin as electron donor

UniProt curation for Q88QX2 (cross-referenced to KEGG ppu:PP_0362, BioCyc PPUT160488:G1G01-396-MONOMER, eggNOG COG0502) assigns the following: GO:0004076 (biotin synthase activity), GO:0009102 (biotin biosynthetic process), GO:0051539 ([4Fe-4S] binding), and GO:0051537 ([2Fe-2S] binding); UniPathway UPA00078 "biotin from 7,8-diaminononanoate: step 2/2" (i.e., the final step); and SUBUNIT = homodimer. The curated catalytic reaction explicitly names reduced [2Fe-2S] ferredoxin as the physiological electron donor:

> (4R,5S)-dethiobiotin + (sulfur carrier)-SH + 2 reduced [2Fe-2S]-[ferredoxin] + 2 SAM → (sulfur carrier)-H + biotin + 2 5′-deoxyadenosine + 2 L-methionine + 2 oxidized [2Fe-2S]-[ferredoxin]

This organism-specific annotation aligns cleanly with the biochemical and structural findings above, sealing the conclusion for the *P. putida* enzyme.

---

## Mechanistic Model / Interpretation

### The catalytic cycle

BioB completes biotin biosynthesis by performing one of the most chemically demanding reactions in cofactor metabolism: the insertion of sulfur into two **unactivated, aliphatic C–H bonds**. This cannot be achieved by conventional polar chemistry, which is why the enzyme belongs to the radical-SAM superfamily and employs free-radical intermediates.

```
                          BioB (biotin synthase, EC 2.8.1.6)
                          homodimer; TIM-barrel (βα)8 fold

   Dethiobiotin (DTB)                                              Biotin
        |  C6-H, C9-H (unactivated)                                  |  thiophane ring closed
        v                                                            ^
   ┌─────────────────────────────────────────────────────────────────────┐
   │  [4Fe-4S]+  --- reductive cleavage --->  2x 5'-deoxyadenosyl radical  │
   │   (Cys59/63/66, CxxxCxxC)                    |  from 2x SAM            │
   │        ^                                     v                        │
   │        | 1 e- from reduced ferredoxin/   H-atom abstraction at        │
   │        | flavodoxin (external donor)     C9 then C6 of DTB            │
   │                                              |                        │
   │                                              v                        │
   │   [2Fe-2S]2+ ---- mu-sulfide donated ---> 9-mercaptodethiobiotin      │
   │   (Cys103/134/194 + Arg266)                  |  (MDTB intermediate)   │
   │        |  cluster degraded (sacrificed)      v                        │
   │        v                                second C-S bond -> biotin     │
   │   requires re-assembly by ISC/SUF Fe-S biogenesis for next turnover   │
   └─────────────────────────────────────────────────────────────────────┘
```

**Step-by-step:**

1. **Activation of SAM.** The catalytic [4Fe-4S]²⁺ cluster receives one electron from a physiological reductant (reduced ferredoxin/flavodoxin) to reach the [4Fe-4S]⁺ state. It binds SAM through the classic radical-SAM CxxxCxxC-ligated unique iron and reductively cleaves it, releasing L-methionine and a 5′-deoxyadenosyl radical (Findings 2, 6).

2. **First H-atom abstraction and C–S bond formation.** The deoxyadenosyl radical abstracts a hydrogen from C9 (the methyl carbon) of dethiobiotin. The resulting carbon radical is quenched by a bridging μ-sulfide from the auxiliary [2Fe-2S] cluster, forming the covalent intermediate **9-mercaptodethiobiotin (MDTB)** (Findings 3, 8).

3. **Second SAM turnover and ring closure.** A second SAM binds and is cleaved to generate a second deoxyadenosyl radical, which abstracts a hydrogen from C6. Ring closure between C6 and the newly installed sulfur completes the thiophane ring, yielding biotin (Findings 2, 3).

4. **Cluster sacrifice and regeneration.** Because the [2Fe-2S] cluster is destroyed to donate its sulfur, the isolated enzyme performs roughly one turnover per active site. In vivo, the cell's Fe-S assembly machinery (ISC/SUF) must rebuild the cluster before the next catalytic cycle — making BioB's throughput dependent on iron, sulfur, and reducing-equivalent supply (Findings 3, 6).

### Reaction summary table

| Feature | Detail | Key evidence |
|---|---|---|
| **EC number** | 2.8.1.6 | UniProt Q88QX2 / HAMAP MF_01694 |
| **Substrate** | (4R,5S)-dethiobiotin | [PMID: 14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/) |
| **Product** | biotin (vitamin B7/H) | [PMID: 15610037](https://pubmed.ncbi.nlm.nih.gov/15610037/) |
| **Co-substrate** | 2 × SAM (per biotin) | [PMID: 15610037](https://pubmed.ncbi.nlm.nih.gov/15610037/) |
| **Sulfur source** | μ-sulfide of sacrificial [2Fe-2S] cluster | [PMID: 38215281](https://pubmed.ncbi.nlm.nih.gov/38215281/) |
| **Reaction intermediate** | 9-mercaptodethiobiotin (MDTB) | [PMID: 21859080](https://pubmed.ncbi.nlm.nih.gov/21859080/) |
| **Catalytic cofactor** | [4Fe-4S] cluster (SAM cleavage) | [PMID: 14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/) |
| **Electron donor (in vivo)** | reduced [2Fe-2S] ferredoxin/flavodoxin | [PMID: 21497584](https://pubmed.ncbi.nlm.nih.gov/21497584/) |
| **Quaternary structure** | homodimer | [PMID: 14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/) |
| **Fold** | (βα)₈ TIM barrel | [PMID: 14704425](https://pubmed.ncbi.nlm.nih.gov/14704425/) |
| **Localization** | cytoplasm | UniProt Q88QX2 / HAMAP |

### Cofactor-ligand mapping (Q88QX2 vs. E. coli BioB)

| Cluster | Role | Q88QX2 ligands | E. coli ligands |
|---|---|---|---|
| [4Fe-4S] | SAM reductive cleavage → radical generation | Cys59, Cys63, Cys66 (CxxxCxxC) | Cys53, Cys57, Cys60 |
| [2Fe-2S] | Sacrificial sulfur donor | Cys103, Cys134, Cys194, **Arg266** | Cys97, Cys128, Cys188, **Arg260** |

The retention of the unusual arginine ligand (Arg266/Arg260) — experimentally validated by EPR in the *E. coli* enzyme ([PMID: 21859080](https://pubmed.ncbi.nlm.nih.gov/21859080/)) — is the single most diagnostic sequence feature distinguishing genuine biotin synthases from other radical-SAM thiolation enzymes.

### Physiological role and localization

BioB operates in the **cytoplasm** as the last enzyme of the *bio* pathway. Its product, biotin, is covalently attached (by biotin protein ligase) to the biotin carboxyl carrier domains of **biotin-dependent carboxylases** — most importantly acetyl-CoA carboxylase (the committed step of fatty-acid synthesis) and pyruvate carboxylase (anaplerosis). Consequently, although BioB itself catalyzes a single narrow reaction, its output is required for lipid biosynthesis and central carbon metabolism. This is why disruption of biotin synthesis is lethal or strongly growth-limiting in organisms that cannot scavenge exogenous biotin, and why the pathway is a validated antimicrobial target in pathogens such as *Mycobacterium tuberculosis* ([PMID: 20565114](https://pubmed.ncbi.nlm.nih.gov/20565114/)).

---

## Evidence Base

The functional assignment for Q88QX2 rests on a convergence of (i) direct biochemistry on orthologous enzymes, (ii) high-resolution structural biology, (iii) sequence/bioinformatic analysis of the *P. putida* protein itself, and (iv) organism-specific database curation. No primary biochemical study on the *P. putida* KT2440 enzyme specifically was identified; the assignment is therefore an inference by orthology, but a very strong one given the diagnostic motif conservation.

| PMID | Title (abbrev.) | Contribution | Supports / Challenges |
|---|---|---|---|
| [14967042](https://pubmed.ncbi.nlm.nih.gov/14967042/) | Role of the [2Fe-2S] cluster in recombinant E. coli BioB | Reaction, [4Fe-4S] role, homodimer, cluster degradation | Supports F1, F2, F3, F4 |
| [15610037](https://pubmed.ncbi.nlm.nih.gov/15610037/) | Turnover of E. coli BioB with DTB and MDTB | Radical-SAM family, 2 SAM per biotin, single-turnover | Supports F1, F2, F3 |
| [38215281](https://pubmed.ncbi.nlm.nih.gov/38215281/) | Biotin synthase with auxiliary 4Fe-5S cluster (2024 review) | Modern consensus: sulfur from sacrificed cluster | Supports F3 |
| [21859080](https://pubmed.ncbi.nlm.nih.gov/21859080/) | [2Fe-2S] reduction accompanies MDTB formation | MDTB intermediate; Arg is a genuine [2Fe-2S] ligand | Supports F3, F7 |
| [14704425](https://pubmed.ncbi.nlm.nih.gov/14704425/) | Crystal structure of biotin synthase (Science 2004) | Substrate between two clusters; TIM barrel | Supports F8, F4 |
| [15381399](https://pubmed.ncbi.nlm.nih.gov/15381399/) | S-adenosylmethionine radical enzymes (review) | Biotin synthase structure solved; soluble enzyme | Supports F4 |
| [8591031](https://pubmed.ncbi.nlm.nih.gov/8591031/) | Substrate binding by dethiobiotin synthetase | Biotin as carboxylase prosthetic group; pathway conservation | Supports F5 |
| [34597430](https://pubmed.ncbi.nlm.nih.gov/34597430/) | Anaerobic E. coli biotin gene | Biotin essential; bio-operon organization/regulation | Supports F5 |
| [32220614](https://pubmed.ncbi.nlm.nih.gov/32220614/) | Engineering IscR for biotin/thiamine/lipoate | BioB rate-limiting; Fe-S depletion causes toxicity | Supports F6 |
| [21497584](https://pubmed.ncbi.nlm.nih.gov/21497584/) | Generation of adenosyl radical in biotin synthase | External electron donor activates [4Fe-4S]⁺ | Supports F2, F6 |
| [7987699](https://pubmed.ncbi.nlm.nih.gov/7987699/) | Mechanism of B. sphaericus biotin synthase | Early evidence SAM required; sulfur not from SAM | Supports F1, F3 (historical) |
| [18690713](https://pubmed.ncbi.nlm.nih.gov/18690713/) | MDTB as competent catalytic intermediate | Confirms 2 SAM cleaved; MDTB tightly bound intermediate | Supports F2, F3 |
| [26369537](https://pubmed.ncbi.nlm.nih.gov/26369537/) | DFT of biotin synthase active site | Computational support for S transfer; Arg260 role | Supports F3, F7, F8 |
| [24991701](https://pubmed.ncbi.nlm.nih.gov/24991701/) | Paramagnetic intermediates in radical-SAM enzymes | EPR: auxiliary [FeS] bridging sulfide is co-substrate | Supports F2, F3 |

Related biotin-pathway structural and comparative studies ([PMID: 8081756](https://pubmed.ncbi.nlm.nih.gov/8081756/), [PMID: 20565114](https://pubmed.ncbi.nlm.nih.gov/20565114/), [PMID: 17993549](https://pubmed.ncbi.nlm.nih.gov/17993549/), [PMID: 20713166](https://pubmed.ncbi.nlm.nih.gov/20713166/)) place BioB in the broader biosynthetic context — confirming its position as the final, sulfur-inserting step downstream of BioD.

An informative comparator is **MiaB** ([PMID: 17407324](https://pubmed.ncbi.nlm.nih.gov/17407324/)), another radical-SAM thiolation enzyme that has been discussed alongside biotin synthase and lipoate synthase with respect to whether a second/auxiliary Fe-S cluster acts as a sacrificial sulfur donor. This comparison reinforces that the auxiliary-cluster-as-sulfur-donor strategy, definitively established for BioB, is a recurring theme among radical-SAM sulfur-insertion enzymes — but also that cluster architecture can vary (cf. the 4Fe-5S variant in [PMID: 38215281](https://pubmed.ncbi.nlm.nih.gov/38215281/)). Q88QX2's canonical 3Cys/1Arg [2Fe-2S] signature places it firmly in the classical BioB class.

---

## Limitations and Knowledge Gaps

1. **No direct study of the P. putida enzyme.** All biochemical and structural evidence comes from the *E. coli* and *B. sphaericus* orthologs. The assignment for Q88QX2/PP_0362 is an inference from sequence orthology (strong, given motif conservation) plus database curation, not from experimental characterization of the KT2440 protein itself. Kinetic parameters (kcat, Km for DTB and SAM), cluster content, and turnover number for the *P. putida* enzyme are unknown.

2. **Physiological electron donor not experimentally verified in P. putida.** UniProt curation names reduced [2Fe-2S] ferredoxin, and the *E. coli* physiological reductant is generally taken to be reduced flavodoxin; which specific ferredoxin/flavodoxin serves BioB in *P. putida* has not been established.

3. **In vivo turnover number and cluster-regeneration coupling remain debated.** The strict "one biotin per monomer" behavior is an in vitro observation; the degree to which BioB achieves multiple turnovers in vivo — and the precise coupling to ISC/SUF cluster reassembly — is still not fully quantified. A recently described biotin synthase variant using a 4Fe-5S auxiliary cluster ([PMID: 38215281](https://pubmed.ncbi.nlm.nih.gov/38215281/)) indicates the sulfur-donor architecture is not universal, though the 3Cys/1Arg [2Fe-2S] signature in Q88QX2 places it firmly in the canonical class.

4. **Regulation in P. putida not addressed.** Whether PP_0362 sits in a classical *bio* operon and how it is transcriptionally regulated (e.g., by a BirA/biotin-responsive repressor) in KT2440 was not investigated in detail.

5. **Localization is annotation-based.** Cytoplasmic localization follows from UniProt/HAMAP and the soluble character of characterized orthologs; it has not been experimentally confirmed for the *P. putida* protein (though there is no reason to expect otherwise).

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and reconstitution.** Overexpress PP_0362 in *E. coli*, anaerobically reconstitute the Fe-S clusters, and confirm homodimeric assembly and [4Fe-4S]/[2Fe-2S] content by UV-vis, EPR, and Mössbauer — directly validating the cofactor assignment for the *P. putida* enzyme.

2. **In vitro activity assay.** Measure DTB → biotin conversion (bioassay or LC-MS) with SAM, dithionite/reduced flavodoxin, and a sulfide/cluster-reconstitution system; quantify SAM:biotin stoichiometry and detect the MDTB intermediate to confirm the canonical mechanism.

3. **Genetic complementation.** Test whether PP_0362 complements an *E. coli* ΔbioB auxotroph, providing a clean functional confirmation of biotin synthase activity in vivo.

4. **Site-directed mutagenesis of Arg266.** Mutate the predicted [2Fe-2S] arginine ligand (Arg266) and monitor the EPR signature and activity, replicating the diagnostic *E. coli* Arg260 experiment to confirm cluster ligation in the *P. putida* enzyme.

5. **Identify the physiological reductant.** Use candidate *P. putida* ferredoxins/flavodoxins in reconstituted assays to determine the native electron donor.

6. **Metabolic engineering context.** Given BioB's role as the biosynthetic bottleneck, test whether IscR modulation or Fe-S pathway upregulation enhances biotin flux in *P. putida* — a chassis of interest for industrial biotechnology — mirroring the >2.2-fold improvement reported in *E. coli* ([PMID: 32220614](https://pubmed.ncbi.nlm.nih.gov/32220614/)).

7. **Structural confirmation.** Solve or model (AlphaFold + validation) the PP_0362 structure and superpose on the *E. coli* biotin synthase (PDB 1R30) to verify the TIM-barrel fold and dual-cluster active-site geometry.

---

## Conclusion

*bioB* (PP_0362, UniProt Q88QX2) in *Pseudomonas putida* KT2440 encodes **biotin synthase (EC 2.8.1.6)**, a cytoplasmic, homodimeric radical-SAM enzyme that catalyzes the **terminal step of de novo biotin biosynthesis**: the insertion of sulfur between C6 and C9 of dethiobiotin to close the thiophane ring and form biotin. Its catalytic [4Fe-4S] cluster (CxxxCxxC; Cys59/63/66) reductively cleaves two SAM molecules into 5′-deoxyadenosyl radicals that abstract the substrate's unactivated C–H hydrogens, while its auxiliary [2Fe-2S] cluster (Cys103/134/194/Arg266) is sacrificed as the inserted sulfur, passing through the 9-mercaptodethiobiotin intermediate. The identity is confirmed by diagnostic motif conservation in the *P. putida* sequence, by organism-specific curation, and by extensive biochemistry and structural biology on the *E. coli* ortholog. The product biotin is the essential prosthetic group of biotin-dependent carboxylases, linking BioB to fatty-acid and central carbon metabolism, and its in vivo function depends on reduced ferredoxin/flavodoxin as electron donor and on continual Fe-S cluster regeneration by the cell's ISC/SUF machinery.


## Artifacts

- [OpenScientist final report](bioB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bioB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:14967042
2. PMID:15610037
3. PMID:38215281
4. PMID:21859080
5. PMID:15381399
6. PMID:8591031
7. PMID:34597430
8. PMID:32220614
9. PMID:21497584
10. PMID:14704425
11. PMID:20565114
12. PMID:8081756
13. PMID:17993549
14. PMID:20713166
15. PMID:17407324