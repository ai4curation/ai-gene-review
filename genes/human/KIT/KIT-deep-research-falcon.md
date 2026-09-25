---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T03:56:34.291508'
end_time: '2026-09-25T04:08:16.534272'
duration_seconds: 702.24
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KIT
  gene_symbol: KIT
  uniprot_accession: P10721
  protein_description: 'RecName: Full=Mast/stem cell growth factor receptor Kit; Short=SCFR;
    EC=2.7.10.1; AltName: Full=Piebald trait protein; Short=PBT; AltName: Full=Proto-oncogene
    c-Kit; AltName: Full=Tyrosine-protein kinase Kit; AltName: Full=p145 c-kit; AltName:
    Full=v-kit Hardy-Zuckerman 4 feline sarcoma viral oncogene homolog; AltName: CD_antigen=CD117;
    Flags: Precursor;'
  gene_info: Name=KIT; Synonyms=SCFR;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. Tyr protein
  protein_domains: Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold.
    (IPR013783); Ig_sub. (IPR003599); Ig_sub2. (IPR003598)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 54
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: KIT-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P10721
- **Protein Description:** RecName: Full=Mast/stem cell growth factor receptor Kit; Short=SCFR; EC=2.7.10.1; AltName: Full=Piebald trait protein; Short=PBT; AltName: Full=Proto-oncogene c-Kit; AltName: Full=Tyrosine-protein kinase Kit; AltName: Full=p145 c-kit; AltName: Full=v-kit Hardy-Zuckerman 4 feline sarcoma viral oncogene homolog; AltName: CD_antigen=CD117; Flags: Precursor;
- **Gene Information:** Name=KIT; Synonyms=SCFR;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783); Ig_sub. (IPR003599); Ig_sub2. (IPR003598)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KIT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KIT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KIT** (gene ID: KIT, UniProt: P10721) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P10721
- **Protein Description:** RecName: Full=Mast/stem cell growth factor receptor Kit; Short=SCFR; EC=2.7.10.1; AltName: Full=Piebald trait protein; Short=PBT; AltName: Full=Proto-oncogene c-Kit; AltName: Full=Tyrosine-protein kinase Kit; AltName: Full=p145 c-kit; AltName: Full=v-kit Hardy-Zuckerman 4 feline sarcoma viral oncogene homolog; AltName: CD_antigen=CD117; Flags: Precursor;
- **Gene Information:** Name=KIT; Synonyms=SCFR;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783); Ig_sub. (IPR003599); Ig_sub2. (IPR003598)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KIT" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KIT' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KIT** (gene ID: KIT, UniProt: P10721) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human KIT (UniProt P10721): Functional-Annotation Research Report

## Executive summary and identity verification

The requested target is unambiguously **human KIT**, not a similarly named protein from another organism. The supplied UniProt accession **P10721**, gene symbol **KIT** (synonym **SCFR**), and aliases **c-KIT/CD117/mast–stem-cell growth-factor receptor** agree with literature describing a 976-amino-acid, approximately 145-kDa type III receptor tyrosine kinase encoded at human chromosome 4q12. Its five extracellular immunoglobulin-like domains, single transmembrane segment, autoinhibitory juxtamembrane region, split cytoplasmic kinase domain and C-terminal tail match the supplied InterPro Ig-like-domain and tyrosine-kinase annotations. No literature concerning a different “KIT” gene was used. (ledoux2023receptortyrosinekinase pages 1-2, foster2018cd117ckitincancer pages 1-3)

**Primary functional annotation:** KIT is the cell-surface receptor for **stem cell factor** (SCF, encoded by **KITLG**). SCF-induced receptor dimerization activates KIT’s intrinsic protein-tyrosine kinase, causing reciprocal autophosphorylation and recruitment of signaling proteins. KIT thereby converts an extracellular SCF signal into PI3K–AKT, RAS–MAPK, SRC, PLCγ and JAK–STAT responses controlling survival, proliferation, differentiation and migration in selected progenitor and differentiated lineages. (ledoux2023receptortyrosinekinase pages 1-2, r�nnstrand2004signaltransductionvia pages 1-2, foster2018cd117ckitincancer pages 3-6)

The detailed evidence map is provided below.

| Feature | Precise annotation/evidence | Evidence type | Key source/date/DOI URL |
|---|---|---|---|
| Identity, aliases, organism | **Human KIT**, UniProt **P10721**; gene **KIT** (synonym **SCFR**); protein aliases include mast/stem-cell growth-factor receptor, c-KIT, SCFR and **CD117**. Literature independently identifies the same 976-aa KIT/CD117 receptor encoded at 4q12; no conflicting same-symbol protein was used. | Supplied UniProt identity cross-checked against literature | Foster et al., 8 Mar 2018, [doi:10.3390/biomedicines6010031](https://doi.org/10.3390/biomedicines6010031) (foster2018cd117ckitincancer pages 1-3) |
| Family and architecture | Type III, single-pass receptor tyrosine kinase: N-terminal extracellular region with **five Ig-like domains**, one transmembrane helix, cytosolic juxtamembrane autoinhibitory region, split bilobed kinase domain containing a kinase insert, activation loop and C-terminal tail. Reported cytosolic boundaries include TM L525–Y545, JMR K546–K581, kinase W582–S931 and tail T932–R946. | Sequence/topology annotation, structural literature and molecular modeling | Ledoux et al., Jan 2022, [doi:10.3390/ijms23031589](https://doi.org/10.3390/ijms23031589); Ledoux et al., 25 Sep 2023, [doi:10.3390/kinasesphosphatases1040014](https://doi.org/10.3390/kinasesphosphatases1040014) (ledoux2023receptortyrosinekinase pages 1-2, ledoux2022theinherentcoupling pages 2-4) |
| Ligand and activation | **Stem cell factor (SCF/KITLG) is the cognate ligand.** Dimeric SCF brings two KIT ectodomains together; receptor contacts stabilize the dimer, displace juxtamembrane/activation-loop autoinhibition and enable reciprocal trans-autophosphorylation. Phosphotyrosines then recruit SH2/PTB-containing effectors. | Biochemical and crystallographic mechanism summarized in authoritative reviews | Rönnstrand, Oct 2004, [doi:10.1007/s00018-004-4189-6](https://doi.org/10.1007/s00018-004-4189-6); Ledoux et al., Sep 2023 (ledoux2023receptortyrosinekinase pages 1-2, r�nnstrand2004signaltransductionvia pages 1-2) |
| Catalytic reaction and substrate scope | EC **2.7.10.1**, a receptor protein-tyrosine kinase: **ATP + protein-L-tyrosine → ADP + protein-L-tyrosine phosphate**. KIT first phosphorylates tyrosines on the paired receptor and can phosphorylate recruited signaling proteins. It is therefore a protein/peptide-tyrosine kinase—not an enzyme with one unique small-molecule substrate; sequence context, docking and colocalization confer physiological selectivity. | Enzyme-class annotation supported by ligand-induced intrinsic kinase activity and substrate-phosphorylation evidence; no single exclusive protein substrate established | Rönnstrand, Oct 2004; Foster et al., Mar 2018 (r�nnstrand2004signaltransductionvia pages 1-2, foster2018cd117ckitincancer pages 3-6) |
| pY568 and pY570 | Juxtamembrane sites phosphorylated early after activation; experimentally recognized SH2 docking sites, especially for Src-family kinases. They help release autoinhibition and support migration/chemotaxis signaling. Assignments to every individual Src-family member are cell-context dependent. | In-vivo phosphosite mapping and interaction/function studies summarized in reviews | Ledoux et al., Jan 2022; Foster et al., Mar 2018 (foster2018cd117ckitincancer pages 13-14, ledoux2022theinherentcoupling pages 2-4) |
| pY703 | Kinase-insert docking site for **GRB2**; couples KIT to SOS–RAS–RAF–MEK–ERK/MAPK signaling. | Reported biochemical interaction summarized in phosphosite review | Ledoux & Tchertanov, Feb 2023, [doi:10.3390/kinasesphosphatases1010005](https://doi.org/10.3390/kinasesphosphatases1010005) (ledoux2023sitespecificphosphorylationof pages 1-2) |
| pY721 | Principal **PI3K p85** recognition site; activates PI3K–PIP3–AKT signaling. Direct structural evidence is strong: PDB **2IUH**, a 2.0-Å co-crystal of PI3K-p85 SH2 with a KIT pY721 peptide. Full-length KID–SH2 orientations proposed in 2023 remain computational models. | X-ray crystallography plus biochemical studies; full-domain geometry modeled | Ledoux & Tchertanov, Feb 2023, [doi:10.3390/kinasesphosphatases1010005](https://doi.org/10.3390/kinasesphosphatases1010005) (ledoux2023sitespecificphosphorylationof pages 8-10, ledoux2023sitespecificphosphorylationof pages 2-4, ledoux2023sitespecificphosphorylationof pages 25-26) |
| pY730 | Recognized as a **PLCγ** recruitment site, linking KIT to phosphoinositide hydrolysis, Ca²⁺ mobilization and PKC signaling. A modeled pY721–PI3K complex also predicts a nearby Y730 contact, but that contact is computational and should not be treated as proof that Y730 directly binds PI3K. | Functional interaction assignment from prior experiments/review; adjacent PI3K contact is molecular-modeling inference | Ledoux & Tchertanov, Feb 2023 (ledoux2023sitespecificphosphorylationof pages 1-2, ledoux2023sitespecificphosphorylationof pages 24-25) |
| pY823 | Activation-loop phosphosite associated with the active kinase conformation. A proposed intramolecular/pseudosubstrate relationship involving D792 is structural/computational inference; a definitive downstream binding partner remains unidentified. | In-vivo phosphosite; mechanistic inference from structure and molecular dynamics | Ledoux et al., Jan 2022 (ledoux2022theinherentcoupling pages 2-4) |
| pY900 | C-lobe site reported to mediate phosphorylation-dependent **CrkII/c-Crk** association, potentially involving PI3K-p85. Because an indirect bridge is possible, direct one-to-one binding should not be overstated. | Phosphosite and interaction evidence summarized in structural/signaling reviews | Ledoux et al., Jan 2022; Foster et al., Mar 2018 (foster2018cd117ckitincancer pages 13-14, ledoux2022theinherentcoupling pages 2-4) |
| pY936 | C-terminal docking site associated with **GRB2/GRB7** and RAS–MAPK activation. The exact partner usage varies with cell type and experimental system. | Biochemical association/function studies summarized in reviews | Foster et al., Mar 2018; Ledoux et al., Jan 2022 (foster2018cd117ckitincancer pages 13-14, ledoux2022theinherentcoupling pages 2-4) |
| Major pathways | Activated KIT engages **PI3K–AKT**, **RAS–RAF–MEK–ERK/MAPK**, Src-family kinases, **PLCγ–Ca²⁺/PKC**, JAK–STAT, RAC/JNK and cytoskeletal signaling. These networks mediate survival, proliferation, differentiation, adhesion and directed migration; PI3K–AKT is a prominent survival arm. | Biochemical pathway studies and authoritative reviews | Foster et al., Mar 2018; Ledoux et al., Sep 2023 (ledoux2023receptortyrosinekinase pages 1-2, foster2018cd117ckitincancer pages 3-6) |
| Localization and trafficking | Mature KIT functions primarily at the **plasma membrane**, with extracellular SCF recognition and a cytosolic catalytic domain. Ligand stimulation induces internalization and degradation; CBL-family ubiquitin ligases and HSP90-dependent stability regulate receptor abundance. Oncogenic KIT can be retained and signal from intracellular organelles, including Golgi-associated compartments, making trafficking a resistance target. Explicit KIT-specific lysosomal routing is less firmly documented in the retrieved evidence than internalization/degradation. | Membrane topology plus cell-biological and therapeutic-resistance evidence | Zhou et al., Feb 2024, [doi:10.1186/s12964-023-01411-x](https://doi.org/10.1186/s12964-023-01411-x) (zhou2024kitmutationsand pages 12-13, ledoux2022theinherentcoupling pages 2-4) |
| Physiological roles | SCF–KIT is essential for survival, proliferation, migration and/or differentiation of **hematopoietic stem/progenitor cells, mast cells, melanocytes, germ cells and interstitial cells of Cajal**. Human loss-of-function variants cause pigmentation/developmental phenotypes such as piebaldism, supporting these lineage functions. | Human genetics, cell biology and comparative physiology | Rönnstrand, Oct 2004; Open Targets evidence synthesis (OpenTargets Search: -KIT, r�nnstrand2004signaltransductionvia pages 1-2) |
| Disease variants | Gain-of-function variants uncouple activity from SCF. Major classes include extracellular variants, juxtamembrane exon 11 variants, ATP-binding-pocket variants and activation-loop variants such as **D816V/D816H**. They drive GIST, systemic mastocytosis and subsets of AML, germ-cell tumors and melanoma; loss-of-function KIT causes piebaldism. | Human tumor sequencing, functional studies and clinical-genetic association | Lennartsson et al., Jan 2005, [doi:10.1634/stemcells.2004-0117](https://doi.org/10.1634/stemcells.2004-0117); Open Targets (OpenTargets Search: -KIT, lennartsson2005normalandoncogenic pages 19-20, r�nnstrand2004signaltransductionvia pages 1-2) |
| 2023 structural/interactome advances | Long-timescale simulations of the full KIT cytoplasmic domain found that **D816V** reshapes interdomain coupling, conformational disorder and the free-energy landscape, exposing candidate mutant-selective allosteric pockets. Separate 2023 work modeled multisite-phosphorylated kinase-insert conformations; these generate testable interaction hypotheses but are not substitutes for binding experiments. | Molecular dynamics, free-energy analysis, pocket detection and docking | Ledoux et al., 25 Sep 2023, [doi:10.3390/kinasesphosphatases1040014](https://doi.org/10.3390/kinasesphosphatases1040014); Ledoux & Tchertanov, Feb 2023 (ledoux2023receptortyrosinekinase pages 26-28, ledoux2023sitespecificphosphorylationof pages 1-2, ledoux2023sitespecificphosphorylationof pages 24-25) |
| 2024 GIST statistics | Approximately **80–90%** of treatment-naïve GISTs carry a primary KIT mutation. Acquired resistance commonly appears after **18–24 months** of imatinib, and about **90%** of imatinib resistance in the cited review was attributed to secondary KIT mutations. These figures establish continuing KIT dependence while highlighting intratumoral mutation heterogeneity. | 2024 evidence review synthesizing molecular and clinical studies | Zhou et al., Feb 2024, [doi:10.1186/s12964-023-01411-x](https://doi.org/10.1186/s12964-023-01411-x) (zhou2024kitmutationsand pages 1-2) |
| Current therapeutic implementation | KIT-directed/multikinase TKIs are routine precision therapy in GIST: **imatinib** is the standard adjuvant and usual first-line agent; **sunitinib**, **regorafenib** and **ripretinib** are established later-line agents. **Avapritinib** has mutation-selective activity against activation-loop targets and an approved GIST role centered on PDGFRA exon 18 disease; it also inhibits KIT D816V and is used in advanced systemic mastocytosis. Genotype—not KIT immunostaining alone—should guide drug selection. | Regulatory/clinical implementation summarized in 2024 treatment reviews | Huang et al., Jan 2024, [doi:10.2174/1567201820666221122120657](https://doi.org/10.2174/1567201820666221122120657); Zhou et al., Feb 2024 (zhou2024kitmutationsand pages 12-13, huang2024drugsinthe pages 7-8, huang2024drugsinthe pages 1-1) |
| 2024 late-line real-world evidence | In 34 advanced-GIST patients receiving both ripretinib and avapritinib, response rates were **12–18%**. Median TTP was **3.65–4.73 months** for ripretinib and **4.11–5.39 months** for avapritinib; median OS after starting the two-drug sequence was **29.63 vs 33.7 months**. Investigators found no evidence that sequence materially changed efficacy, but the retrospective 17-patient groups limit certainty. | Two-center retrospective clinical cohort | Thirasastr et al., Feb 2024, [doi:10.3390/cancers16050904](https://doi.org/10.3390/cancers16050904) (thirasastr2024outcomesoflateline pages 13-14) |
| Drug-development landscape | A 2024 analysis of data through 2021 identified **75 drugs**, **225 GIST drug trials** and **57 targets**; KIT was the most frequent target (**25 occurrences**), ahead of PDGFRA (16) and VEGFR2/KDR (13). Five marketed GIST TKIs were identified: imatinib, sunitinib, regorafenib, ripretinib and avapritinib. | Quantitative pipeline/database analysis | Huang et al., Jan 2024, [doi:10.2174/1567201820666221122120657](https://doi.org/10.2174/1567201820666221122120657) (huang2024drugsinthe pages 1-1, huang2024drugsinthe pages 6-7) |


*Table: Concise evidence map for human KIT/SCFR/CD117 (UniProt P10721), integrating molecular function, site-specific signaling, localization, disease biology and 2023–2024 clinical developments. Experimental and crystallographic findings are explicitly separated from computational or review-level inference.*

## 1. Molecular function and catalytic activity

KIT belongs to the **class III receptor tyrosine kinase** family. The mature receptor is oriented with its ligand-binding Ig-like ectodomain outside the cell, one membrane-spanning helix, and its catalytic apparatus in the cytosol. A structural annotation places the transmembrane segment at approximately residues 525–545, the juxtamembrane region at 546–581, the kinase region at 582–931 and the C-terminal tail at 932–946; minor boundary differences among databases reflect annotation conventions rather than conflicting topology. (ledoux2023receptortyrosinekinase pages 1-2, ledoux2022theinherentcoupling pages 2-4)

As an EC **2.7.10.1 receptor protein-tyrosine kinase**, KIT catalyzes the general reaction:

**ATP + protein-L-tyrosine → ADP + protein-L-tyrosine phosphate.**

Its substrates are tyrosine residues in proteins or peptides, not one exclusive small molecule. The first physiologically decisive substrates are tyrosines on the paired KIT receptor itself; KIT can also phosphorylate recruited signaling proteins. Effective specificity is determined by peptide sequence around the tyrosine, docking interactions, receptor conformation and cellular colocalization. Thus, “protein tyrosine” is the substrate class, whereas autophosphorylation and pathway-protein phosphorylation provide biological selectivity. Ligand-induced intrinsic kinase activation and autophosphorylation are experimentally established, although the retrieved literature does not support defining one unique downstream protein as KIT’s sole substrate. (r�nnstrand2004signaltransductionvia pages 1-2, foster2018cd117ckitincancer pages 3-6)

## 2. Activation mechanism

SCF/KITLG is KIT’s cognate ligand and occurs in membrane-associated and soluble forms. SCF binding assembles and stabilizes a KIT homodimer. In inactive KIT, the cytoplasmic juxtamembrane region restrains the kinase, together with the αC helix and activation loop. Dimerization permits reciprocal phosphorylation—initially including juxtamembrane tyrosines—displacing this inhibitory arrangement and opening access to ATP and protein substrates. Additional phosphorylated tyrosines become docking sites for SH2- or PTB-domain-containing proteins. (ledoux2023receptortyrosinekinase pages 1-2, r�nnstrand2004signaltransductionvia pages 1-2, foster2018cd117ckitincancer pages 3-6)

The principal human phosphosites provide a modular signaling surface:

- **Y568/Y570:** early juxtamembrane phosphosites and SH2 docking sites, prominently coupling KIT to Src-family kinases and migration/chemotaxis signaling; they also participate in release of autoinhibition. (foster2018cd117ckitincancer pages 13-14, ledoux2022theinherentcoupling pages 2-4)
- **Y703:** GRB2-associated site connecting KIT to SOS–RAS–RAF–MEK–ERK signaling. (ledoux2023sitespecificphosphorylationof pages 1-2)
- **Y721:** principal PI3K-p85 docking site. This assignment has direct structural support from the 2.0-Å PDB 2IUH structure of a p85 SH2 domain bound to a KIT pY721 peptide. The broader full-length kinase-insert/PI3K geometries proposed in 2023 are computational models, not equivalent to full-receptor crystallographic validation. (ledoux2023sitespecificphosphorylationof pages 8-10, ledoux2023sitespecificphosphorylationof pages 2-4, ledoux2023sitespecificphosphorylationof pages 25-26)
- **Y730:** associated with PLCγ recruitment and phosphoinositide/Ca²⁺ signaling. A modeled contact involving Y730 in a pY721–PI3K complex remains computational inference. (ledoux2023sitespecificphosphorylationof pages 1-2, ledoux2023sitespecificphosphorylationof pages 24-25)
- **Y823:** activation-loop phosphosite associated with catalytic activation. Its proposed intramolecular structural role is plausible, but a definitive downstream binding partner has not been established. (ledoux2022theinherentcoupling pages 2-4)
- **Y900:** supports phosphorylation-dependent Crk/c-Crk association, potentially involving PI3K-p85; indirect complex formation remains possible. (foster2018cd117ckitincancer pages 13-14, ledoux2022theinherentcoupling pages 2-4)
- **Y936:** C-terminal signaling site associated with GRB2/GRB7 and MAPK activation, with partner usage depending on cellular context. (foster2018cd117ckitincancer pages 13-14, ledoux2022theinherentcoupling pages 2-4)

## 3. Pathways and biological consequences

The best-supported signaling branches are:

1. **PI3K–AKT:** PI3K p85 binds pY721, enabling p110-mediated PIP3 production and AKT activation. This is a major survival pathway; AKT suppresses pro-apoptotic machinery such as BAD. Oncogenic D816 variants retain strong PI3K signaling, and disruption of the Y721 interaction reduces mutant KIT-driven growth and tumorigenicity. (lennartsson2005normalandoncogenic pages 19-20, foster2018cd117ckitincancer pages 3-6, ledoux2023sitespecificphosphorylationof pages 8-10)
2. **RAS–RAF–MEK–ERK/MAPK:** GRB2-associated sites, particularly Y703 and Y936, connect KIT to RAS/MAPK, supporting proliferation and differentiation. Signal magnitude varies with splice isoform and cellular context. (r�nnstrand2004signaltransductionvia pages 1-2, ledoux2023sitespecificphosphorylationof pages 1-2, ledoux2022theinherentcoupling pages 2-4)
3. **SRC-family signaling:** juxtamembrane pY568/pY570 recruit SRC-family proteins, linking KIT to cytoskeletal remodeling, calcium signaling, adhesion and directional migration. (foster2018cd117ckitincancer pages 13-14)
4. **PLCγ–Ca²⁺/PKC:** PLCγ recruitment, associated with Y730, promotes phosphoinositide hydrolysis and calcium mobilization. (foster2018cd117ckitincancer pages 3-6, ledoux2023sitespecificphosphorylationof pages 1-2)
5. **JAK–STAT and auxiliary RAC/JNK pathways:** KIT can activate STAT proteins and stress/cytoskeletal pathways. Constitutively active mutants frequently sustain STAT3, although ERK output can be cell-context dependent. (ledoux2023receptortyrosinekinase pages 1-2, lennartsson2005normalandoncogenic pages 19-20)

These branches explain KIT’s precise signaling role better than a broad list of pleiotropic phenotypes: KIT is a ligand-regulated membrane kinase that builds a phosphotyrosine docking platform and coordinates survival, cell-cycle entry, differentiation, adhesion and motility.

## 4. Cellular and tissue localization

KIT carries out ligand recognition at the **plasma membrane**: SCF binds extracellularly while ATP binding, phosphorylation and effector recruitment occur on the cytoplasmic face. Following activation, receptor internalization and degradation limit signal duration. CBL-family ubiquitin-ligase activity and HSP90-dependent stabilization regulate KIT abundance; HSP90 or HDAC-directed interventions can lower total and phosphorylated KIT. (zhou2024kitmutationsand pages 12-13, ledoux2022theinherentcoupling pages 2-4)

Localization is altered in some cancers. Mutant KIT can be retained in intracellular organelles, including Golgi-associated compartments, and remain signaling competent. This has motivated organelle-directed inhibitors and strategies that alter KIT folding, trafficking or degradation. The retrieved KIT-specific evidence supports internalization and degradation, but is less definitive about the exact lysosomal itinerary than the broader receptor-tyrosine-kinase literature; a KIT-specific lysosomal route should therefore not be asserted without qualification. (zhou2024kitmutationsand pages 12-13)

Physiologically important KIT-expressing lineages include hematopoietic stem/progenitor cells, mast cells, melanocytes, germ cells and gastrointestinal interstitial cells of Cajal. Human loss-of-function genetics, including piebaldism, supports roles in melanocyte development and migration; gain-of-function genetics demonstrates the receptor’s growth and survival functions in GIST, mastocytosis and subsets of leukemia. (OpenTargets Search: -KIT, r�nnstrand2004signaltransductionvia pages 1-2)

## 5. Disease mechanisms and functional genetic evidence

**Loss-of-function KIT** disrupts SCF-dependent developmental or lineage maintenance programs and can cause piebaldism. **Gain-of-function KIT** bypasses normal ligand control. Juxtamembrane mutations weaken autoinhibition, whereas activation-loop mutations such as **D816V/D816H** stabilize active or signaling-competent conformations and can be relatively insensitive to inhibitors that preferentially bind inactive kinase conformations. (OpenTargets Search: -KIT, lennartsson2005normalandoncogenic pages 19-20, r�nnstrand2004signaltransductionvia pages 1-2)

Disease associations are strongest for GIST and mastocytosis, with additional involvement in AML, germ-cell tumors and melanoma. Open Targets identifies human KIT, approved name “KIT proto-oncogene, receptor tyrosine kinase,” as strongly associated with GIST, piebaldism, AML and cutaneous mastocytosis, providing orthogonal genetic, literature and clinical evidence that the researched protein is the intended target. (OpenTargets Search: -KIT)

## 6. Developments in 2023–2024

### Structural and mechanistic research

A September 2023 molecular-dynamics study compared wild-type KIT with KIT D816V across the full cytoplasmic domain. It reported mutation-associated changes in disorder, interdomain coupling and free-energy landscapes and identified candidate mutant-selective allosteric pockets. These results offer hypotheses for inhibitors that discriminate D816V from wild-type KIT, but they are computational and require biochemical and pharmacological validation. [Ledoux et al., published 25 September 2023; DOI/URL: https://doi.org/10.3390/kinasesphosphatases1040014.] (ledoux2023receptortyrosinekinase pages 1-2, ledoux2023receptortyrosinekinase pages 26-28)

A February 2023 study analyzed phosphorylation-dependent conformations of KIT’s kinase-insert domain and modeled its interaction with PI3K SH2 domains. Its key strength is explicit benchmarking against the experimental pY721 peptide–PI3K crystal structure; proposed full-domain interfaces remain testable models. [Ledoux and Tchertanov, February 2023; https://doi.org/10.3390/kinasesphosphatases1010005.] (ledoux2023sitespecificphosphorylationof pages 1-2, ledoux2023sitespecificphosphorylationof pages 8-10, ledoux2023sitespecificphosphorylationof pages 25-26)

### Current clinical implementation

KIT inhibition is a real-world standard of care in molecularly selected GIST. Imatinib is the principal adjuvant and usual first-line agent; sunitinib, regorafenib and ripretinib are established later-line therapies. Avapritinib has strong activation-loop activity and an approved GIST role centered on PDGFRA exon 18 disease; it also inhibits KIT D816V and is clinically used in advanced systemic mastocytosis. Therapy should be selected by the precise driver and resistance genotype rather than CD117 immunostaining alone. (zhou2024kitmutationsand pages 12-13, huang2024drugsinthe pages 7-8, huang2024drugsinthe pages 1-1)

A 2024 pipeline analysis using data through 2021 found **75 drugs**, **225 GIST drug-treatment trials** and **57 therapeutic targets**. KIT was the most frequent target, occurring 25 times, followed by PDGFRA at 16 and VEGFR2/KDR at 13. Five marketed GIST TKIs were identified: imatinib, sunitinib, regorafenib, ripretinib and avapritinib. [Huang et al., January 2024; https://doi.org/10.2174/1567201820666221122120657.] (huang2024drugsinthe pages 1-1, huang2024drugsinthe pages 6-7)

### Recent quantitative findings

A February 2024 review estimates that **80–90% of treatment-naïve GISTs harbor primary KIT mutations**. Acquired imatinib resistance often develops after **18–24 months**, and approximately **90%** of resistance in the review was attributed to secondary KIT mutations. The authors’ expert interpretation is that GIST commonly remains KIT-dependent after progression; resistance may therefore require simultaneous control of heterogeneous kinase mutations, KIT protein abundance and bypass pathways rather than abandoning KIT as a target. [Zhou et al., February 2024; https://doi.org/10.1186/s12964-023-01411-x.] (zhou2024kitmutationsand pages 12-13, zhou2024kitmutationsand pages 1-2)

In a two-center retrospective cohort of **34** advanced-GIST patients who received both ripretinib and avapritinib, each treatment sequence contained 17 patients. Response rates were **12–18%**; median time to progression was **3.65–4.73 months** with ripretinib and **4.11–5.39 months** with avapritinib. Median overall survival after sequence initiation was **29.63 versus 33.7 months**. Investigators found no evidence that giving one drug first materially reduced the other’s later activity, but the small retrospective groups limit causal conclusions. [Thirasastr et al., February 2024; https://doi.org/10.3390/cancers16050904.] (thirasastr2024outcomesoflateline pages 13-14)

## 7. Expert assessment and annotation confidence

The highest-confidence annotation is that KIT is an **SCF-activated, plasma-membrane receptor protein-tyrosine kinase** whose central biochemical action is ATP-dependent phosphorylation of receptor and signaling-protein tyrosines. Structural, biochemical, genetic and pharmacological evidence converge on this function. The pY721–PI3K interaction has unusually strong site-specific structural support, while several other phosphosite-partner assignments rely on biochemical studies summarized in reviews and may vary among cell types. (ledoux2023sitespecificphosphorylationof pages 1-2, ledoux2023sitespecificphosphorylationof pages 8-10)

The major translational lesson from 2023–2024 research is that “KIT-positive” is not a single therapeutic state. Juxtamembrane, ATP-pocket and activation-loop variants occupy different conformational ensembles and display different inhibitor sensitivities. Secondary-mutation heterogeneity and altered intracellular trafficking further complicate inhibition. Current expert strategy therefore emphasizes mutation-resolved sequencing, inhibitors covering multiple KIT conformations, degradation or expression-control strategies, and mutant-selective allosteric pockets. (ledoux2023receptortyrosinekinase pages 1-2, zhou2024kitmutationsand pages 12-13, yu2024molecularcharacteristicsand pages 10-11, zhou2024kitmutationsand pages 1-2)

## Conclusion

Human KIT/P10721 is a well-validated class III receptor tyrosine kinase rather than a transporter, structural protein or adaptor. Its extracellular Ig-like region detects SCF, its membrane-spanning architecture transmits ligand-induced dimerization, and its cytoplasmic kinase phosphorylates protein tyrosines to assemble a signaling platform. The receptor acts chiefly at the plasma membrane, with internalization, organelle retention and degradation controlling signal duration and drug response. This mechanism explains its indispensable roles in selected stem/progenitor, mast-cell, melanocyte, germ-cell and interstitial-cell lineages, as well as why activating mutations create therapeutically actionable dependence in GIST and systemic mastocytosis. Recent work is refining KIT annotation from a simple on/off kinase model toward a mutation-, conformation-, phosphosite- and compartment-specific signaling system.

References

1. (ledoux2023receptortyrosinekinase pages 1-2): Julie Ledoux, Marina Botnari, and Luba Tchertanov. Receptor tyrosine kinase kit: mutation-induced conformational shift promotes alternative allosteric pockets. Kinases and Phosphatases, 1:220-250, Sep 2023. URL: https://doi.org/10.3390/kinasesphosphatases1040014, doi:10.3390/kinasesphosphatases1040014. This article has 4 citations.

2. (foster2018cd117ckitincancer pages 1-3): Brittni M. Foster, Danish Zaidi, Tyler R. Young, Mary E. Mobley, and Bethany A. Kerr. Cd117/c-kit in cancer stem cell-mediated progression and therapeutic resistance. Biomedicines, Feb 2018. URL: https://doi.org/10.3390/biomedicines6010031, doi:10.3390/biomedicines6010031. This article has 162 citations.

3. (r�nnstrand2004signaltransductionvia pages 1-2): L. R�nnstrand. Signal transduction via the stem cell factor receptor/c-kit. Cellular and Molecular Life Sciences CMLS, 61:2535-2548, Oct 2004. URL: https://doi.org/10.1007/s00018-004-4189-6, doi:10.1007/s00018-004-4189-6. This article has 643 citations.

4. (foster2018cd117ckitincancer pages 3-6): Brittni M. Foster, Danish Zaidi, Tyler R. Young, Mary E. Mobley, and Bethany A. Kerr. Cd117/c-kit in cancer stem cell-mediated progression and therapeutic resistance. Biomedicines, Feb 2018. URL: https://doi.org/10.3390/biomedicines6010031, doi:10.3390/biomedicines6010031. This article has 162 citations.

5. (ledoux2022theinherentcoupling pages 2-4): Julie Ledoux, Alain Trouvé, and Luba Tchertanov. The inherent coupling of intrinsically disordered regions in the multidomain receptor tyrosine kinase kit. International Journal of Molecular Sciences, 23:1589, Jan 2022. URL: https://doi.org/10.3390/ijms23031589, doi:10.3390/ijms23031589. This article has 10 citations.

6. (foster2018cd117ckitincancer pages 13-14): Brittni M. Foster, Danish Zaidi, Tyler R. Young, Mary E. Mobley, and Bethany A. Kerr. Cd117/c-kit in cancer stem cell-mediated progression and therapeutic resistance. Biomedicines, Feb 2018. URL: https://doi.org/10.3390/biomedicines6010031, doi:10.3390/biomedicines6010031. This article has 162 citations.

7. (ledoux2023sitespecificphosphorylationof pages 1-2): Julie Ledoux and Luba Tchertanov. Site-specific phosphorylation of rtk kit kinase insert domain: interactome landscape perspectives. Kinases and Phosphatases, 1:39-71, Feb 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010005, doi:10.3390/kinasesphosphatases1010005. This article has 1 citations.

8. (ledoux2023sitespecificphosphorylationof pages 8-10): Julie Ledoux and Luba Tchertanov. Site-specific phosphorylation of rtk kit kinase insert domain: interactome landscape perspectives. Kinases and Phosphatases, 1:39-71, Feb 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010005, doi:10.3390/kinasesphosphatases1010005. This article has 1 citations.

9. (ledoux2023sitespecificphosphorylationof pages 2-4): Julie Ledoux and Luba Tchertanov. Site-specific phosphorylation of rtk kit kinase insert domain: interactome landscape perspectives. Kinases and Phosphatases, 1:39-71, Feb 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010005, doi:10.3390/kinasesphosphatases1010005. This article has 1 citations.

10. (ledoux2023sitespecificphosphorylationof pages 25-26): Julie Ledoux and Luba Tchertanov. Site-specific phosphorylation of rtk kit kinase insert domain: interactome landscape perspectives. Kinases and Phosphatases, 1:39-71, Feb 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010005, doi:10.3390/kinasesphosphatases1010005. This article has 1 citations.

11. (ledoux2023sitespecificphosphorylationof pages 24-25): Julie Ledoux and Luba Tchertanov. Site-specific phosphorylation of rtk kit kinase insert domain: interactome landscape perspectives. Kinases and Phosphatases, 1:39-71, Feb 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010005, doi:10.3390/kinasesphosphatases1010005. This article has 1 citations.

12. (zhou2024kitmutationsand pages 12-13): Shishan Zhou, Omar Abdihamid, Fengbo Tan, Haiyan Zhou, Heli Liu, Zhi Li, Sheng Xiao, and Bin Li. Kit mutations and expression: current knowledge and new insights for overcoming im resistance in gist. Cell Communication and Signaling : CCS, Feb 2024. URL: https://doi.org/10.1186/s12964-023-01411-x, doi:10.1186/s12964-023-01411-x. This article has 81 citations.

13. (OpenTargets Search: -KIT): Open Targets Query (-KIT, 35 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

14. (lennartsson2005normalandoncogenic pages 19-20): Johan Lennartsson, Tanya Jelacic, Diana Linnekin, and R. Shivakrupa. Normal and oncogenic forms of the receptor tyrosine kinase kit. STEM CELLS, 23:16-43, Jan 2005. URL: https://doi.org/10.1634/stemcells.2004-0117, doi:10.1634/stemcells.2004-0117. This article has 381 citations and is from a highest quality peer-reviewed journal.

15. (ledoux2023receptortyrosinekinase pages 26-28): Julie Ledoux, Marina Botnari, and Luba Tchertanov. Receptor tyrosine kinase kit: mutation-induced conformational shift promotes alternative allosteric pockets. Kinases and Phosphatases, 1:220-250, Sep 2023. URL: https://doi.org/10.3390/kinasesphosphatases1040014, doi:10.3390/kinasesphosphatases1040014. This article has 4 citations.

16. (zhou2024kitmutationsand pages 1-2): Shishan Zhou, Omar Abdihamid, Fengbo Tan, Haiyan Zhou, Heli Liu, Zhi Li, Sheng Xiao, and Bin Li. Kit mutations and expression: current knowledge and new insights for overcoming im resistance in gist. Cell Communication and Signaling : CCS, Feb 2024. URL: https://doi.org/10.1186/s12964-023-01411-x, doi:10.1186/s12964-023-01411-x. This article has 81 citations.

17. (huang2024drugsinthe pages 7-8): Chen Huang, Xinli Ma, Ming Wang, and Hui Cao. Drugs in the gist field (therapeutic targets and clinical trial staging). Jan 2024. URL: https://doi.org/10.2174/1567201820666221122120657, doi:10.2174/1567201820666221122120657. This article has 5 citations and is from a peer-reviewed journal.

18. (huang2024drugsinthe pages 1-1): Chen Huang, Xinli Ma, Ming Wang, and Hui Cao. Drugs in the gist field (therapeutic targets and clinical trial staging). Jan 2024. URL: https://doi.org/10.2174/1567201820666221122120657, doi:10.2174/1567201820666221122120657. This article has 5 citations and is from a peer-reviewed journal.

19. (thirasastr2024outcomesoflateline pages 13-14): Prapassorn Thirasastr, Thomas L. Sutton, Cissimol P. Joseph, Heather Lin, Behrang Amini, Skye C. Mayo, Dejka Araujo, Robert S. Benjamin, Anthony P. Conley, John A. Livingston, Joseph Ludwig, Shreyaskumar Patel, Ravin Ratan, Vinod Ravi, Maria A. Zarzour, Elise F. Nassif Haddad, Michael S. Nakazawa, Xiao Zhou, Michael C. Heinrich, and Neeta Somaiah. Outcomes of late-line systemic treatment in gist: does sequence matter? Cancers, 16:904, Feb 2024. URL: https://doi.org/10.3390/cancers16050904, doi:10.3390/cancers16050904. This article has 1 citations.

20. (huang2024drugsinthe pages 6-7): Chen Huang, Xinli Ma, Ming Wang, and Hui Cao. Drugs in the gist field (therapeutic targets and clinical trial staging). Jan 2024. URL: https://doi.org/10.2174/1567201820666221122120657, doi:10.2174/1567201820666221122120657. This article has 5 citations and is from a peer-reviewed journal.

21. (yu2024molecularcharacteristicsand pages 10-11): Yang Yu, Mengdie Yu, Lijie Luo, Zijing Zhang, Haiping Zeng, Yan Chen, Zeyu Lin, Mengnan Chen, and Wei Wang. Molecular characteristics and immune microenvironment of gastrointestinal stromal tumours: targets for therapeutic strategies. Frontiers in Oncology, Jul 2024. URL: https://doi.org/10.3389/fonc.2024.1405727, doi:10.3389/fonc.2024.1405727. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](KIT-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. ledoux2023sitespecificphosphorylationof pages 1-2
2. ledoux2022theinherentcoupling pages 2-4
3. zhou2024kitmutationsand pages 1-2
4. thirasastr2024outcomesoflateline pages 13-14
5. zhou2024kitmutationsand pages 12-13
6. ledoux2023receptortyrosinekinase pages 1-2
7. ledoux2023sitespecificphosphorylationof pages 8-10
8. ledoux2023sitespecificphosphorylationof pages 2-4
9. ledoux2023sitespecificphosphorylationof pages 25-26
10. ledoux2023sitespecificphosphorylationof pages 24-25
11. lennartsson2005normalandoncogenic pages 19-20
12. ledoux2023receptortyrosinekinase pages 26-28
13. huang2024drugsinthe pages 7-8
14. huang2024drugsinthe pages 1-1
15. huang2024drugsinthe pages 6-7
16. yu2024molecularcharacteristicsand pages 10-11
17. doi:10.3390/biomedicines6010031
18. doi:10.3390/ijms23031589
19. doi:10.3390/kinasesphosphatases1040014
20. doi:10.1007/s00018-004-4189-6
21. doi:10.3390/kinasesphosphatases1010005
22. doi:10.1186/s12964-023-01411-x
23. doi:10.1634/stemcells.2004-0117
24. doi:10.2174/1567201820666221122120657
25. doi:10.3390/cancers16050904
26. Ledoux et al., published 25 September 2023; DOI/URL: https://doi.org/10.3390/kinasesphosphatases1040014.
27. Ledoux and Tchertanov, February 2023; https://doi.org/10.3390/kinasesphosphatases1010005.
28. Huang et al., January 2024; https://doi.org/10.2174/1567201820666221122120657.
29. Zhou et al., February 2024; https://doi.org/10.1186/s12964-023-01411-x.
30. Thirasastr et al., February 2024; https://doi.org/10.3390/cancers16050904.
31. https://doi.org/10.3390/biomedicines6010031
32. https://doi.org/10.3390/ijms23031589
33. https://doi.org/10.3390/kinasesphosphatases1040014
34. https://doi.org/10.1007/s00018-004-4189-6
35. https://doi.org/10.3390/kinasesphosphatases1010005
36. https://doi.org/10.1186/s12964-023-01411-x
37. https://doi.org/10.1634/stemcells.2004-0117
38. https://doi.org/10.2174/1567201820666221122120657
39. https://doi.org/10.3390/cancers16050904
40. https://doi.org/10.3390/kinasesphosphatases1040014.]
41. https://doi.org/10.3390/kinasesphosphatases1010005.]
42. https://doi.org/10.2174/1567201820666221122120657.]
43. https://doi.org/10.1186/s12964-023-01411-x.]
44. https://doi.org/10.3390/cancers16050904.]
45. https://doi.org/10.3390/kinasesphosphatases1040014,
46. https://doi.org/10.3390/biomedicines6010031,
47. https://doi.org/10.1007/s00018-004-4189-6,
48. https://doi.org/10.3390/ijms23031589,
49. https://doi.org/10.3390/kinasesphosphatases1010005,
50. https://doi.org/10.1186/s12964-023-01411-x,
51. https://doi.org/10.1634/stemcells.2004-0117,
52. https://doi.org/10.2174/1567201820666221122120657,
53. https://doi.org/10.3390/cancers16050904,
54. https://doi.org/10.3389/fonc.2024.1405727,