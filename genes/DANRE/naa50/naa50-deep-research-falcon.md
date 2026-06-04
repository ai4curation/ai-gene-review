---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-30T15:32:33.069645'
end_time: '2026-05-30T15:41:09.065070'
duration_seconds: 516.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DANRE
  gene_id: naa50
  gene_symbol: naa50
  uniprot_accession: Q6DBY2
  protein_description: 'RecName: Full=N-alpha-acetyltransferase 50; EC=2.3.1.258 {ECO:0000250|UniProtKB:Q9GZZ1};
    AltName: Full=N-acetyltransferase NAT13; AltName: Full=N-epsilon-acetyltransferase
    50 {ECO:0000250|UniProtKB:Q9GZZ1}; EC=2.3.1.- {ECO:0000250|UniProtKB:Q9GZZ1};
    AltName: Full=NatE catalytic subunit;'
  gene_info: Name=naa50; Synonyms=mak3, nat13;
  organism_full: Danio rerio (Zebrafish) (Brachydanio rerio).
  protein_family: Belongs to the acetyltransferase family. GNAT subfamily.
  protein_domains: Acyl_CoA_acyltransferase. (IPR016181); GNAT_dom. (IPR000182); N-term/lysine_N-AcTrnsfr.
    (IPR051556); Acetyltransf_1 (PF00583)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: naa50-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q6DBY2
- **Protein Description:** RecName: Full=N-alpha-acetyltransferase 50; EC=2.3.1.258 {ECO:0000250|UniProtKB:Q9GZZ1}; AltName: Full=N-acetyltransferase NAT13; AltName: Full=N-epsilon-acetyltransferase 50 {ECO:0000250|UniProtKB:Q9GZZ1}; EC=2.3.1.- {ECO:0000250|UniProtKB:Q9GZZ1}; AltName: Full=NatE catalytic subunit;
- **Gene Information:** Name=naa50; Synonyms=mak3, nat13;
- **Organism (full):** Danio rerio (Zebrafish) (Brachydanio rerio).
- **Protein Family:** Belongs to the acetyltransferase family. GNAT subfamily.
- **Key Domains:** Acyl_CoA_acyltransferase. (IPR016181); GNAT_dom. (IPR000182); N-term/lysine_N-AcTrnsfr. (IPR051556); Acetyltransf_1 (PF00583)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "naa50" matches the protein description above**
2. **Verify the organism is correct:** Danio rerio (Zebrafish) (Brachydanio rerio).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'naa50' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **naa50** (gene ID: naa50, UniProt: Q6DBY2) in DANRE.

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
- **UniProt Accession:** Q6DBY2
- **Protein Description:** RecName: Full=N-alpha-acetyltransferase 50; EC=2.3.1.258 {ECO:0000250|UniProtKB:Q9GZZ1}; AltName: Full=N-acetyltransferase NAT13; AltName: Full=N-epsilon-acetyltransferase 50 {ECO:0000250|UniProtKB:Q9GZZ1}; EC=2.3.1.- {ECO:0000250|UniProtKB:Q9GZZ1}; AltName: Full=NatE catalytic subunit;
- **Gene Information:** Name=naa50; Synonyms=mak3, nat13;
- **Organism (full):** Danio rerio (Zebrafish) (Brachydanio rerio).
- **Protein Family:** Belongs to the acetyltransferase family. GNAT subfamily.
- **Key Domains:** Acyl_CoA_acyltransferase. (IPR016181); GNAT_dom. (IPR000182); N-term/lysine_N-AcTrnsfr. (IPR051556); Acetyltransf_1 (PF00583)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "naa50" matches the protein description above**
2. **Verify the organism is correct:** Danio rerio (Zebrafish) (Brachydanio rerio).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'naa50' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **naa50** (gene ID: naa50, UniProt: Q6DBY2) in DANRE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Functional Annotation of **naa50** (Danio rerio) / **NAA50 (NatE catalytic subunit)**

## Executive summary and identity verification
The target protein is **Danio rerio Naa50** (UniProt **Q6DBY2**), annotated in UniProt as **N‑alpha‑acetyltransferase 50 (NAA50)**, also known as **NAT13/MAK3**, and belonging to the **GNAT acetyltransferase family** (NatE catalytic subunit). In the retrieved literature corpus, **NAA50 is consistently defined as the catalytic subunit of the NatE N‑terminal acetyltransferase activity**, frequently functioning in association with the NatA core (NAA10/NAA15) as a NatA/E assembly; however, **no zebrafish primary study directly characterizing Q6DBY2** (expression, localization, loss‑of‑function phenotype, or substrates) was found in the retrieved papers. Accordingly, the functional annotation below is **conserved-function inference** from vertebrate/eukaryotic NAA50 studies and authoritative NAT reviews, not zebrafish-specific experimental validation (aksnes2023natsata pages 6-6, deng2021proteinnterminalacetylation pages 8-10).

## 1) Key concepts and definitions (current understanding)

### N-terminal acetylation (NTA)
**N‑terminal acetylation** is a widespread protein modification in eukaryotes in which an acetyl group is transferred from **acetyl‑CoA** to the **α‑amino group** of the extreme N‑terminus of a protein (mctiernan2025illuminatingtheimpact pages 1-2, deng2019structureandmechanism pages 1-4). Quantitatively, NTA is described as one of the most abundant eukaryotic protein modifications, affecting on the order of **~50–80% of the proteome depending on species** (deng2019structureandmechanism pages 1-4).

NTA is catalyzed by **N‑terminal acetyltransferases (NATs; NatA–NatH)**, and **substrate specificity is largely determined by the first 2–4 N‑terminal residues** (mctiernan2025illuminatingtheimpact pages 1-2).

### NatE / NAA50
**NAA50** is the catalytic subunit of **NatE**. In contrast to NatA, which typically acetylates N-termini **after initiator methionine excision (NME)**, NAA50 is notable for acetylating N‑termini that **retain the initiator methionine (iMet)** and therefore can compete with early nascent-chain processing events at the ribosome (klein2026nataengagesin pages 1-2, deng2019structureandmechanism pages 1-4).

## 2) Biochemical function: reaction, substrate specificity, and mechanism

### Core enzymatic reaction (reaction class)
Across NAT literature, NAA50/NatE is placed within the NAT class of enzymes that catalyze **acetyl‑CoA–dependent transfer of an acetyl moiety to protein N‑termini** (N‑alpha acetylation), consistent with GNAT-fold acetyltransferase chemistry (deng2019structureandmechanism pages 1-4, mctiernan2025illuminatingtheimpact pages 1-2). Structural studies of NatA/Naa50 complexes were explicitly motivated by this canonical NAT reaction, i.e., acetyl transfer from acetyl‑CoA to the N‑terminal amino group, largely occurring co‑translationally (deng2019structureandmechanism pages 1-4).

### Substrate specificity (N-termini motifs)
Evidence from structural/biochemical work indicates NAA50 has **strong preference for Met at position 1** with relatively **broad tolerance at position 2**:

* A tetrapeptide-library biochemical/structural analysis reports that **human Naa50 acetylates retained N‑terminal methionine** and that specificity is dominated by a **hydrophobic P1 pocket** with a more permissive **amphipathic/solvent-exposed P2 pocket**, supporting broad position‑2 tolerance (reddi2016humannaa50protein pages 2-3).
* The same study summarizes that Naa50 can acetylate N‑terminal methionine when followed by **many residues** (with proline disfavored), and that Met followed by hydrophobic residues (e.g., Leu/Ile/Phe/Trp) are accepted substrates (reddi2016humannaa50protein pages 4-6, reddi2016humannaa50protein pages 2-3).
* An authoritative review summarizes NatE specificity as **Met-starting** N‑termini (examples include **MK‑, MV‑, MY‑**), and notes NatE’s in vitro specificity partially overlaps with NatC (ree2018spotlightonprotein pages 2-4).

Together, these sources support the interpretation that **zebrafish Naa50 (Q6DBY2)** most likely acetylates **iMet-retaining N‑termini**, especially **Met‑hydrophobic** and more broadly **Met‑X** N-termini, consistent with NatE/NAA50 conserved enzymology (reddi2016humannaa50protein pages 4-6, reddi2016humannaa50protein pages 2-3, ree2018spotlightonprotein pages 2-4).

### Structural determinants and catalytic mechanism
Structural/biochemical synthesis indicates that NAA50 peptide recognition is driven **mostly by residues 1 and 2** of the N‑terminus, with extensive backbone interactions and side‑chain contacts in a pocket well-suited for **Met1** (deng2021proteinnterminalacetylation pages 8-10). Conserved catalytic residues (e.g., **Tyr73 and His112**, via an ordered water network) are implicated as acid/base participants in catalysis for active NAA50 enzymes (deng2021proteinnterminalacetylation pages 8-10). Comparative analyses emphasize **species divergence** in activity: yeast NAA50 has been described as catalytically compromised/inactive relative to human/Drosophila NAA50 (deng2021proteinnterminalacetylation pages 8-10, deng2019structureandmechanism pages 1-4).

### N‑alpha vs N‑epsilon acetylation
A 2023 “NATs at a glance” summary cites an early biochemical report claiming human NAA50 displays both **protein N‑alpha** and **N‑epsilon (lysine side-chain)** acetyltransferase activity (aksnes2023natsata pages 6-6). However, the dominant mechanistic and structural evidence in the retrieved corpus focuses on **N‑terminal acetylation** by NAA50 (NatE) rather than lysine acetylation (deng2019structureandmechanism pages 1-4, deng2021proteinnterminalacetylation pages 8-10). Therefore, for functional annotation, the best-supported primary function remains **N‑terminal (α‑amino) acetylation** (deng2019structureandmechanism pages 1-4, deng2021proteinnterminalacetylation pages 8-10).

## 3) Complex membership, interaction partners, and regulatory context

### NatA/E (NatE) assembly and NatA partners
NAA50 can operate as a **monomer** and also as part of a NatA-associated assembly often described as **NatA/E (NatE)**:

* NAA50 is described as the NatE catalytic subunit that can be accommodated by NatA; NatA comprises the auxiliary NAA15 and catalytic NAA10 (klein2026nataengagesin pages 1-2).
* Structural synthesis indicates **human NAA50 binds NatA with nanomolar affinity**, docking primarily onto a hydrophobic surface of **NAA15**, with more modest contact to **NAA10**, and that NAA10 and NAA50 can mutually influence each other’s activities within NatE (deng2021proteinnterminalacetylation pages 8-10).
* A review on acetyltransferases in cardiovascular disease and aging states that **Naa50 can interact with Naa15 to form a multienzyme complex known as NatA/E**, and characterizes NatA–E NATs as **cytoplasmic and ribosome-associated**, consistent with co-translational action (keller2024acetyltransferaseincardiovascular pages 17-19).

### Regulation by HYPK and competitive complex formation
Evidence indicates that NAA50’s association with NatA is part of a regulated interaction network:

* A mechanistic review notes that **HYPK and NAA50 can associate with NatA**, describing formation of **competing complexes**, consistent with a regulatory interplay between HYPK and NAA50 in access to NatA (deng2021proteinnterminalacetylation pages 5-8).
* A plant-focused review similarly describes that **HYPK and NAA50 can bind simultaneously to NatA**, but that binding of one can weaken the affinity of the other, supporting a model of dynamic and potentially competitive regulation (pozoga2022fromnucleusto pages 8-10).

## 4) Subcellular localization and where the gene product acts
The NAT system is described as largely **ribosome-associated** and **cytoplasmic** for the main co-translational NATs, including NatE/NAA50 (keller2024acetyltransferaseincardiovascular pages 17-19, deng2019structureandmechanism pages 1-4). NAA50 is discussed as functioning at or near the ribosomal tunnel exit as part of co-translational N‑terminus processing networks (klein2026nataengagesin pages 1-2).

Additionally, NAA50 can exist in a **free (monomeric) pool** as well as NatA-bound, indicating that some portion of activity/localization may not be strictly constrained to the NatA-bound ribosomal complex state (deng2021proteinnterminalacetylation pages 8-10).

## 5) Biological roles, pathways, and phenotypes (evidence-based)

### Roles inferred from NAT biology
NTA is reviewed as influencing protein folding, complex formation, targeting, and turnover; this establishes a plausible mechanistic link from NAA50 activity to proteostasis and protein biogenesis (mctiernan2025illuminatingtheimpact pages 1-2).

### Cell-division-related phenotypes and candidate substrates
A 2023 overview reports that **loss of NAA50** is associated with **sister chromatid cohesion defects**, attributed to lack of Nt‑acetylation of a proposed substrate (**Scc1/Vtd**), and that **NAA50 depletion in HeLa cells produces mitotic arrest** that can be rescued by co-depletion of NatA (aksnes2023natsata pages 3-4). This supports functional coupling between **NAA50/NatE** and **NatA** in regulating cell-cycle-relevant protein function (aksnes2023natsata pages 3-4).

## 6) Recent developments and latest research (prioritizing 2023–2024)

### Authoritative 2023 synthesis of NATs including NatE/NAA50
A 2023 peer-reviewed “at a glance” synthesis summarizes NAT enzymes, including NatE/NAA50, emphasizing (i) NatE’s identity as an N-terminal acetyltransferase, (ii) evidence for NatA/NAA50 dual-enzyme complexes, and (iii) regulatory involvement of HYPK (aksnes2023natsata pages 6-6).

### 2024 methodological development: antibody to acetylated N-termini
A 2024 methods paper reports an antibody approach specific for **N‑terminally acetylated methionine** and proposes its use as a tool to identify NAT substrates or analyze changes in NTA status, with explicit mention of NatE/NatF class enzymes in that context (keller2024acetyltransferaseincardiovascular pages 17-19). This is directly relevant to functional annotation workflows because it provides a practical route to **validate NatE-type iMet-acetylated substrates** experimentally.

### 2024 perspective on NATs in disease and aging
A 2024 review discussing acetyltransferases in cardiovascular disease and aging includes NAA50 within the NAT classification framework and emphasizes **NatA/E multienzyme complex formation** and cytoplasmic/ribosome association of NatA–E NATs (keller2024acetyltransferaseincardiovascular pages 17-19).

## 7) Current applications and real-world implementations

1. **Proteomics/terminomics for substrate discovery and functional annotation**: Modern NAT research uses N‑terminomics and related proteomic strategies to connect NAT enzymes to their substrate sets; recent tool development includes an antibody to acetylated N‑terminal methionine to help identify or track NatE/NatF/NatC-type substrates (keller2024acetyltransferaseincardiovascular pages 17-19).
2. **Structural biology for mechanism and inhibitor design**: Structural studies of NatA/Naa50 assemblies and substrate-binding pockets provide a foundation for understanding specificity and, in principle, developing selective modulators of NAT activity (deng2019structureandmechanism pages 1-4, deng2021proteinnterminalacetylation pages 8-10).
3. **Model systems to connect NTA to organismal phenotypes**: While not naa50-specific, zebrafish has been adopted for NAT functional studies, including recent zebrafish knockout work on a NAT (Naa80) demonstrating in vivo relevance of NTA to sensory development (aksnes2023natsata pages 6-6). This supports the feasibility of analogous zebrafish approaches for naa50/Q6DBY2, but does not itself provide evidence about naa50.

## 8) Statistics and quantitative data points from recent/reviewed studies

* **Proteome coverage**: N‑terminal acetylation is described as affecting **~50–80%** of the proteome depending on species (deng2019structureandmechanism pages 1-4).
* **NatA coverage**: NatA is described as acetylating **>40%** of eukaryotic proteins in co-translational fashion (deng2019structureandmechanism pages 1-4).
* **Specificity determinants**: NAT substrate specificity is primarily determined by **the first 2–4 N‑terminal residues**, a key quantitative rule of thumb for predicting NAT assignment (mctiernan2025illuminatingtheimpact pages 1-2).

## 9) Limitations and evidence gaps for Danio rerio naa50 (Q6DBY2)
No retrieved primary study directly connects **zebrafish naa50/Q6DBY2** to (i) in vivo substrates, (ii) subcellular localization in zebrafish tissues, (iii) developmental phenotypes in zebrafish, or (iv) pathway-level genetic interactions. Therefore, the zebrafish-specific annotation presented here should be treated as a **high-confidence conserved-function hypothesis** anchored in vertebrate NAA50 evidence, pending direct zebrafish experimental validation (aksnes2023natsata pages 6-6, deng2021proteinnterminalacetylation pages 8-10).

## 10) Summary table of key findings
The following table consolidates the main functional-annotation points and clearly distinguishes conserved evidence from missing zebrafish-specific validation.

| Topic | Key points | Strength/organism evidence | Best supporting citation IDs |
|---|---|---|---|
| Identity | Danio rerio target is UniProt Q6DBY2, annotated as N-alpha-acetyltransferase 50/NAT13, a GNAT-family acetyltransferase. In the provided literature snippets, NAA50 is consistently described as the catalytic subunit of NatE; however, no zebrafish-specific primary study for Q6DBY2 was retrieved, so functional annotation must be inferred from conserved vertebrate/eukaryotic NAA50 literature. | Strong for general/human NAA50 identity; zebrafish-specific primary evidence not found in retrieved snippets. | (aksnes2023natsata pages 6-6) |
| Complex | NAA50 can bind the NatA core to form a NatA/E (NatE) complex. Binding is centered on the NAA15 auxiliary subunit with more limited contacts to NAA10; human NAA50 binds NatA with nanomolar affinity. Some evidence also indicates NAA50 can exist as a monomer in addition to the NatA-bound state. | Strong in human; comparative evidence from yeast and plants. | (deng2021proteinnterminalacetylation pages 8-10, deng2021proteinnterminalacetylation pages 5-8, keller2024acetyltransferaseincardiovascular pages 17-19) |
| Function | Core reaction inferred for NAA50/NatE is N-terminal (N-alpha) acetylation: transfer of an acetyl group from acetyl-CoA to the alpha-amino group at the protein N-terminus, typically co-translationally. NAA50 is specifically distinguished from NatA in that it can acetylate retained initiator methionine-containing N-termini and does not require prior methionine excision. | Strong for general NAT chemistry and human NAA50/NatE; not directly shown in zebrafish in retrieved snippets. | (deng2019structureandmechanism pages 1-4, mctiernan2025illuminatingtheimpact pages 1-2, klein2026nataengagesin pages 1-2) |
| Substrates | Human NAA50 shows broad substrate specificity centered on retained initiator methionine. Evidence supports strong preference for Met at position 1, with broad tolerance at position 2; accepted examples include Met followed by hydrophobic residues (Leu, Ile, Phe, Trp) and table/examples also include MK-, MV-, MY-. A 2016 study summarized in snippets states NAA50 can acetylate retained initiator methionine followed by almost any residue except proline. NatE specificity overlaps partly with NatC/NatF. | Strong in human biochemical/structural studies; broader comparative support from reviews; plant in vitro support for broad Met-starting specificity. | (reddi2016humannaa50protein pages 4-6, reddi2016humannaa50protein pages 2-3, ree2018spotlightonprotein pages 2-4, pozoga2022fromnucleusto pages 8-10) |
| Structural determinants | Substrate recognition is driven mainly by the first two residues. Reported structural features include a hydrophobic pocket for Met1 and a more permissive/amphipathic, solvent-exposed pocket for residue 2. Conserved Tyr73 and His112 are implicated in catalysis. Human NAA50 is active, whereas yeast NAA50 is described as catalytically compromised/inactive in the cited reviews and structural work. | Strong in human structural biochemistry; comparative contrast with yeast. | (reddi2016humannaa50protein pages 2-3, deng2021proteinnterminalacetylation pages 8-10, deng2019structureandmechanism pages 1-4) |
| Localization | NatA-NAA50/NatE is described as cytoplasmic and ribosome-associated within the general NAT machinery, consistent with co-translational acetylation at the ribosomal peptide tunnel exit. Human NAA50 also exists in free/monomeric form in addition to NatA-bound form. No zebrafish localization study was identified in retrieved snippets. | Moderate-to-strong for human/general NAT context; no zebrafish-specific localization evidence retrieved. | (keller2024acetyltransferaseincardiovascular pages 17-19, deng2021proteinnterminalacetylation pages 8-10, klein2026nataengagesin pages 1-2) |
| Regulation | HYPK is a NatA-associated regulator, and snippets indicate that HYPK and NAA50 can both associate with NatA; binding may be competitive or mutually weakening depending on context. NatA-NAA50 interactions produce catalytic crosstalk, and NAA10/NAA50 can influence each other’s activities within NatE. | Strong in human structural/regulatory literature; some comparative plant review support. | (deng2021proteinnterminalacetylation pages 5-8, deng2021proteinnterminalacetylation pages 8-10, pozoga2022fromnucleusto pages 8-10) |
| Additional activity claim | One cited summary notes an early biochemical report that human NAA50 displays both protein N-alpha- and N-epsilon-acetyltransferase activity. However, the stronger and more consistent theme across later structural/biochemical snippets is N-terminal acetylation; the retrieved snippets do not provide comparable mechanistic support for lysine side-chain acetylation. | Limited/older human claim for N-epsilon activity; stronger consensus for N-alpha activity. | (aksnes2023natsata pages 6-6) |
| Phenotypes/biological roles | Loss or depletion of NAA50 is linked in cited snippets to sister chromatid cohesion defects, mitotic arrest in HeLa cells, and a proposed substrate relationship with Scc1/Vtd. Reviews also connect N-terminal acetylation machinery to proteostasis, folding, targeting, and turnover. These observations support a role for NAA50 in protein biogenesis and cell-division-related processes, but they are not zebrafish-specific. | Moderate in human/cell-based studies and reviews; no zebrafish naa50 phenotype retrieved. | (aksnes2023natsata pages 3-4, mctiernan2025illuminatingtheimpact pages 1-2) |
| Applications/relevance | Recent literature positions NAT enzymes, including NatE/NAA50, as important for understanding proteostasis, developmental biology, and disease mechanisms. Emerging applications include anti-Nt-acetylated methionine antibodies that may help identify NatC/NatE/NatF substrates or track changes in N-terminal acetylation status. No direct zebrafish-specific implementation was retrieved. | Moderate for current methodological and disease-context relevance; largely general/human-focused. | (mctiernan2025illuminatingtheimpact pages 1-2, keller2024acetyltransferaseincardiovascular pages 17-19) |
| Zebrafish evidence gap | No primary zebrafish functional, localization, or phenotype evidence for Danio rerio naa50/Q6DBY2 was identified in the retrieved snippets. Therefore, annotation for zebrafish should be treated as conserved-function inference from human/general eukaryotic NAA50/NatE studies, cross-checked against the UniProt identity and GNAT/NAT family assignment. | Important negative finding; prevents over-claiming organism-specific evidence. | (aksnes2023natsata pages 6-6, deng2021proteinnterminalacetylation pages 8-10) |


*Table: This table summarizes conserved functional-annotation points for zebrafish Naa50 (UniProt Q6DBY2) based on retrieved NAA50/NatE literature. It highlights what is well supported across species and explicitly notes the lack of zebrafish-specific primary evidence in the available snippets.*

## Key references (with URLs and publication dates)

* Aksnes H, McTiernan N, Arnesen T. **NATs at a glance.** *Journal of Cell Science* (Jul 2023). https://doi.org/10.1242/jcs.260766 (aksnes2023natsata pages 6-6)
* Deng S, Magin RS, Wei X, et al. **Structure and mechanism of acetylation by the N-terminal dual enzyme NatA/Naa50 complex.** *Structure* (Jul 2019). https://doi.org/10.1016/j.str.2019.04.014 (deng2019structureandmechanism pages 1-4)
* Deng S, Marmorstein R. **Protein N-terminal acetylation: structural basis, mechanism, versatility, and regulation.** *Trends in Biochemical Sciences* (Jan 2021). https://doi.org/10.1016/j.tibs.2020.08.005 (deng2021proteinnterminalacetylation pages 8-10, deng2021proteinnterminalacetylation pages 5-8)
* Ree R, Varland S, Arnesen T. **Spotlight on protein N-terminal acetylation.** *Experimental & Molecular Medicine* (Jul 2018). https://doi.org/10.1038/s12276-018-0116-z (ree2018spotlightonprotein pages 2-4)
* Keller MA, Nakamura M. **Acetyltransferase in cardiovascular disease and aging.** *Journal of Cardiovascular Aging* (Dec 2024). https://doi.org/10.20517/jca.2024.21 (keller2024acetyltransferaseincardiovascular pages 17-19)
* Reddi R, Saddanapu V, Chinthapalli DK. **Human Naa50 protein displays broad substrate specificity for amino-terminal acetylation…** (2016; journal not resolved in retrieved record). (reddi2016humannaa50protein pages 4-6, reddi2016humannaa50protein pages 2-3)



References

1. (aksnes2023natsata pages 6-6): Henriette Aksnes, Nina McTiernan, and Thomas Arnesen. Nats at a glance. Journal of cell science, Jul 2023. URL: https://doi.org/10.1242/jcs.260766, doi:10.1242/jcs.260766. This article has 20 citations and is from a domain leading peer-reviewed journal.

2. (deng2021proteinnterminalacetylation pages 8-10): Sunbin Deng and Ronen Marmorstein. Protein n-terminal acetylation: structural basis, mechanism, versatility, and regulation. Jan 2021. URL: https://doi.org/10.1016/j.tibs.2020.08.005, doi:10.1016/j.tibs.2020.08.005. This article has 114 citations and is from a domain leading peer-reviewed journal.

3. (mctiernan2025illuminatingtheimpact pages 1-2): Nina McTiernan, Ine Kjosås, and Thomas Arnesen. Illuminating the impact of n-terminal acetylation: from protein to physiology. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-55960-5, doi:10.1038/s41467-025-55960-5. This article has 55 citations and is from a highest quality peer-reviewed journal.

4. (deng2019structureandmechanism pages 1-4): Sunbin Deng, Robert S. Magin, Xuepeng Wei, Buyan Pan, E. James Petersson, and Ronen Marmorstein. Structure and mechanism of acetylation by the n-terminal dual enzyme nata/naa50 complex. Structure, 27:1057-1070.e4, Jul 2019. URL: https://doi.org/10.1016/j.str.2019.04.014, doi:10.1016/j.str.2019.04.014. This article has 53 citations and is from a domain leading peer-reviewed journal.

5. (klein2026nataengagesin pages 1-2): Marius Klein, Klemens Wild, Nina McTiernan, Thomas Arnesen, and Irmgard Sinning. Nata engages in multi-factor complexes at the ribosomal polypeptide tunnel exit. Nature Communications, Jan 2026. URL: https://doi.org/10.1038/s41467-026-68787-5, doi:10.1038/s41467-026-68787-5. This article has 1 citations and is from a highest quality peer-reviewed journal.

6. (reddi2016humannaa50protein pages 2-3): R Reddi, V Saddanapu, and DK Chinthapalli. Human naa50 protein displays broad substrate specificity for amino-terminal acetylation: detailed structural and biochemical analysis using tetrapeptide library. Unknown journal, 2016.

7. (reddi2016humannaa50protein pages 4-6): R Reddi, V Saddanapu, and DK Chinthapalli. Human naa50 protein displays broad substrate specificity for amino-terminal acetylation: detailed structural and biochemical analysis using tetrapeptide library. Unknown journal, 2016.

8. (ree2018spotlightonprotein pages 2-4): Rasmus Ree, Sylvia Varland, and Thomas Arnesen. Spotlight on protein n-terminal acetylation. Experimental & Molecular Medicine, 50:1-13, Jul 2018. URL: https://doi.org/10.1038/s12276-018-0116-z, doi:10.1038/s12276-018-0116-z. This article has 470 citations and is from a peer-reviewed journal.

9. (keller2024acetyltransferaseincardiovascular pages 17-19): Mariko Aoyagi Keller and Michinari Nakamura. Acetyltransferase in cardiovascular disease and aging. The journal of cardiovascular aging, Dec 2024. URL: https://doi.org/10.20517/jca.2024.21, doi:10.20517/jca.2024.21. This article has 11 citations.

10. (deng2021proteinnterminalacetylation pages 5-8): Sunbin Deng and Ronen Marmorstein. Protein n-terminal acetylation: structural basis, mechanism, versatility, and regulation. Jan 2021. URL: https://doi.org/10.1016/j.tibs.2020.08.005, doi:10.1016/j.tibs.2020.08.005. This article has 114 citations and is from a domain leading peer-reviewed journal.

11. (pozoga2022fromnucleusto pages 8-10): Marlena Pożoga, Laura Armbruster, and Markus Wirtz. From nucleus to membrane: a subcellular map of the n-acetylation machinery in plants. International Journal of Molecular Sciences, 23:14492, Nov 2022. URL: https://doi.org/10.3390/ijms232214492, doi:10.3390/ijms232214492. This article has 12 citations.

12. (aksnes2023natsata pages 3-4): Henriette Aksnes, Nina McTiernan, and Thomas Arnesen. Nats at a glance. Journal of cell science, Jul 2023. URL: https://doi.org/10.1242/jcs.260766, doi:10.1242/jcs.260766. This article has 20 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](naa50-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. deng2019structureandmechanism pages 1-4
2. mctiernan2025illuminatingtheimpact pages 1-2
3. ree2018spotlightonprotein pages 2-4
4. deng2021proteinnterminalacetylation pages 8-10
5. aksnes2023natsata pages 6-6
6. klein2026nataengagesin pages 1-2
7. keller2024acetyltransferaseincardiovascular pages 17-19
8. deng2021proteinnterminalacetylation pages 5-8
9. pozoga2022fromnucleusto pages 8-10
10. aksnes2023natsata pages 3-4
11. https://doi.org/10.1242/jcs.260766
12. https://doi.org/10.1016/j.str.2019.04.014
13. https://doi.org/10.1016/j.tibs.2020.08.005
14. https://doi.org/10.1038/s12276-018-0116-z
15. https://doi.org/10.20517/jca.2024.21
16. https://doi.org/10.1242/jcs.260766,
17. https://doi.org/10.1016/j.tibs.2020.08.005,
18. https://doi.org/10.1038/s41467-025-55960-5,
19. https://doi.org/10.1016/j.str.2019.04.014,
20. https://doi.org/10.1038/s41467-026-68787-5,
21. https://doi.org/10.1038/s12276-018-0116-z,
22. https://doi.org/10.20517/jca.2024.21,
23. https://doi.org/10.3390/ijms232214492,