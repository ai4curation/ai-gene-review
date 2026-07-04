---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-03T23:16:28.826874'
end_time: '2026-07-03T23:34:16.355059'
duration_seconds: 1067.53
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEAE
  gene_id: Q9HTB8
  gene_symbol: wzm
  uniprot_accession: Q9HTB8
  protein_description: 'RecName: Full=Transport permease protein {ECO:0000256|RuleBase:RU361157};'
  gene_info: Name=wzm {ECO:0000313|EMBL:AAG08836.1}; OrderedLocusNames=PA5451 {ECO:0000313|EMBL:AAG08836.1};
  organism_full: Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116
    / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
  protein_family: Belongs to the ABC-2 integral membrane protein family.
  protein_domains: ABC2_TM. (IPR013525); ABC2_TM_bact-type. (IPR047817); ABC_2_transport.
    (IPR000412); ABC2_membrane (PF01061)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Q9HTB8-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Q9HTB8-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9HTB8
- **Protein Description:** RecName: Full=Transport permease protein {ECO:0000256|RuleBase:RU361157};
- **Gene Information:** Name=wzm {ECO:0000313|EMBL:AAG08836.1}; OrderedLocusNames=PA5451 {ECO:0000313|EMBL:AAG08836.1};
- **Organism (full):** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
- **Protein Family:** Belongs to the ABC-2 integral membrane protein family.
- **Key Domains:** ABC2_TM. (IPR013525); ABC2_TM_bact-type. (IPR047817); ABC_2_transport. (IPR000412); ABC2_membrane (PF01061)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "wzm" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'wzm' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **wzm** (gene ID: Q9HTB8, UniProt: Q9HTB8) in PSEAE.

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
- **UniProt Accession:** Q9HTB8
- **Protein Description:** RecName: Full=Transport permease protein {ECO:0000256|RuleBase:RU361157};
- **Gene Information:** Name=wzm {ECO:0000313|EMBL:AAG08836.1}; OrderedLocusNames=PA5451 {ECO:0000313|EMBL:AAG08836.1};
- **Organism (full):** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
- **Protein Family:** Belongs to the ABC-2 integral membrane protein family.
- **Key Domains:** ABC2_TM. (IPR013525); ABC2_TM_bact-type. (IPR047817); ABC_2_transport. (IPR000412); ABC2_membrane (PF01061)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "wzm" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'wzm' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **wzm** (gene ID: Q9HTB8, UniProt: Q9HTB8) in PSEAE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Wzm (PA5451) in *Pseudomonas aeruginosa* PAO1

## 1. Gene and Protein Identity

The gene **wzm** (ordered locus name **PA5451**) in *Pseudomonas aeruginosa* strain PAO1 (UniProt accession Q9HTB8) encodes a **transport permease protein** belonging to the **ABC-2 integral membrane protein family** (InterPro domains: IPR013525, IPR047817, IPR000412; Pfam: PF01061). Wzm functions as the **transmembrane domain (TMD)** component of the Wzm–Wzt ATP-binding cassette (ABC) transporter, which is essential for the export of the common polysaccharide antigen (CPA) O-polysaccharide across the inner membrane of *P. aeruginosa* (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15).

The following table summarizes the key properties of Wzm:

| Property | Details |
|---|---|
| Gene name/locus | **wzm**; ordered locus **PA5451** in *Pseudomonas aeruginosa* PAO1 (from the target UniProt record; gene-function linkage to CPA export supported in *P. aeruginosa*) (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15) |
| UniProt ID | **Q9HTB8** (target UniProt accession provided by user) |
| Protein name | Transport permease protein; functionally the **integral membrane permease (TMD) subunit** of the Wzm-Wzt ABC transporter for O-polysaccharide export (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15) |
| Protein family | **ABC-2 integral membrane protein family** / O-antigen polysaccharide ABC transporter permease; Wzm is the membrane component of a two-subunit ABC exporter (valvano2003exportofospecific pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 25-27) |
| Organism | *Pseudomonas aeruginosa* strain PAO1 (ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101) |
| Substrate transported | **UndPP-linked common polysaccharide antigen (CPA; formerly A-band)**, a **D-rhamnose homopolymer/rhamnan O-polysaccharide** assembled on the cytosolic face of the inner membrane before export to the periplasmic side (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 25-27, king2009reviewlipopolysaccharidebiosynthesis pages 21-23) |
| Transport partner | **Wzt**, the cytosolic ATP-binding/nucleotide-binding domain partner; together Wzm-Wzt form the ABC transporter required for CPA export (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15, caffalette2021cryoemstructureof pages 1-2) |
| Localization | **Inner membrane** integral membrane protein; exports substrate from the **cytoplasmic side** to the **periplasmic side** for subsequent ligation to lipid A-core (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, caffalette2021cryoemstructureof pages 1-2, king2009reviewlipopolysaccharidebiosynthesis pages 21-23) |
| Topology (number of TM helices) | Wzm homologs form the transporter TMD with **6 transmembrane helices per protomer**, plus an N-terminal amphipathic/interface helix and periplasmic gate helices in structural studies of homologous Wzm-Wzt systems (bi2018architectureofa pages 1-2, bi2018architectureofa pages 2-3, caffalette2021cryoemstructureof pages 2-2) |
| Biosynthetic pathway | **ABC transporter-dependent CPA/A-band O-antigen biosynthesis pathway**; distinct from the **Wzy-dependent** pathway used for O-specific antigen (OSA/B-band). CPA is synthesized on a lipid carrier in the cytoplasm, exported by Wzm-Wzt, then ligated to lipid A-core in the periplasm (king2009reviewlipopolysaccharidebiosynthesis pages 20-21, king2009reviewlipopolysaccharidebiosynthesis pages 21-23) |
| Biological function | Required for **export of CPA to the cell surface**. Loss of **wzm** blocks export and core ligation but not polymer synthesis, causing CPA to accumulate intracellularly on lipid carrier and preventing surface display (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15) |
| Key structural features (gate helices, aromatic belt, channel) | Structural studies of Wzm-Wzt homologs show Wzm forms a **continuous transmembrane channel** wide enough for linear polysaccharides; contains **cytosolic and periplasmic gate helices**, **aromatic residues/aromatic belt** near the periplasmic exit, and channel-lining aromatic/hydrophilic residues that coordinate the polymer during translocation (bi2018architectureofa pages 1-2, caffalette2021cryoemstructureof pages 1-2, caffalette2021cryoemstructureof pages 2-4) |
| Transport mechanism | Best-supported current model is an **ATP-driven processive channel mechanism**, not classical alternating access: the lipid-linked O-polysaccharide is recruited, loaded into a continuous Wzm channel, and moved stepwise across the membrane as ATP binding/hydrolysis at Wzt drives conformational changes (spellmon2022molecularbasisfor pages 9-11, bi2018architectureofa pages 4-5, caffalette2021cryoemstructureof pages 4-6, bi2018architectureofa pages 1-2) |


*Table: This table summarizes the core identity, function, localization, substrate, and mechanism of the Wzm permease encoded by PA5451 in *Pseudomonas aeruginosa* PAO1. It is useful as a compact reference linking the PAO1 gene to the CPA/A-band O-antigen export pathway and to modern structural models of Wzm-Wzt transport.*

## 2. Primary Function: ABC Transporter Permease for CPA O-Antigen Export

### 2.1 Substrate Specificity

Wzm is the **integral membrane permease** subunit of the Wzm–Wzt ABC transporter. Its substrate is the **undecaprenyl-pyrophosphate (UndPP)-linked common polysaccharide antigen (CPA)**, also historically referred to as the **A-band O-polysaccharide** (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, lam2011geneticandfunctional pages 8-9). The CPA is a **neutral homopolymer of D-rhamnose (D-Rha)**, consisting of a trisaccharide repeating unit with the structure [→3)-α-D-Rha-(1→3)-α-D-Rha-(1→2)-α-D-Rha-(1→]ₙ (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 23-24). This D-rhamnan polymer is assembled on the cytoplasmic face of the inner membrane on a lipid carrier (UndPP), and Wzm–Wzt transports the completed polymer across the membrane to the periplasmic face (king2009reviewlipopolysaccharidebiosynthesis pages 21-23, king2009reviewlipopolysaccharidebiosynthesis pages 25-27).

### 2.2 Transport Function

Wzm works in obligate partnership with **Wzt**, the cytosolic **ATP-binding/nucleotide-binding domain (NBD)** subunit. Together, Wzm (TMD) and Wzt (NBD) form a functional ABC transporter heterodimer that mediates the energy-dependent export of lipid-linked CPA from the cytoplasm to the periplasm (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15, caffalette2021cryoemstructureof pages 1-2). The Wzm protein contains approximately six transmembrane domains and is responsible for forming the polysaccharide translocation channel (valvano2003exportofospecific pages 8-9, bi2018architectureofa pages 1-2).

Experimental evidence directly demonstrates the essential role of Wzm: **allele replacement mutagenesis** of *wzm* in *P. aeruginosa* prevents export of CPA to the cell surface, although the polysaccharide is still synthesized intracellularly and remains attached to its isoprenyl-pyrophosphate lipid carrier in the cytoplasm (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15). This intracellular accumulation can be detected by immunoelectron microscopy (rocchetta1999geneticsofoantigen pages 14-15). The inability to export CPA prevents its ligation to lipid A-core, which normally occurs only in the periplasm (rocchetta1999geneticsofoantigen pages 14-15, king2009reviewlipopolysaccharidebiosynthesis pages 25-27).

## 3. Subcellular Localization

Wzm is an **integral inner membrane protein** of *P. aeruginosa*. It is embedded in the cytoplasmic (inner) membrane with its transmembrane helices spanning the lipid bilayer, forming a translocation channel that connects the cytoplasmic and periplasmic faces of the membrane (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, caffalette2021cryoemstructureof pages 1-2, bi2018architectureofa pages 1-2). The transporter exports its substrate from the **cytoplasmic side** to the **periplasmic side** of the inner membrane, where the CPA polymer is subsequently ligated to the lipid A-core oligosaccharide by the O-antigen ligase WaaL (king2009reviewlipopolysaccharidebiosynthesis pages 21-23).

## 4. Biosynthetic Pathway: ABC Transporter-Dependent CPA Biosynthesis

### 4.1 Pathway Overview

*P. aeruginosa* produces two structurally and serologically distinct O-antigen polysaccharides on its lipopolysaccharide (LPS): the **CPA (A-band)**, a D-rhamnose homopolymer, and the **O-specific antigen (OSA, B-band)**, a heteropolymer that varies between serotypes (king2009reviewlipopolysaccharidebiosynthesis pages 20-21, rocchetta1999geneticsofoantigen pages 6-8). These two O-antigens are synthesized through fundamentally different pathways. The CPA is produced via the **ABC transporter-dependent pathway** (Wzy-independent), whereas the OSA follows the **Wzy-dependent pathway** (rocchetta1999geneticsofoantigen pages 14-15, king2009reviewlipopolysaccharidebiosynthesis pages 20-21).

In the ABC transporter-dependent pathway, the CPA polymer is fully assembled on the cytoplasmic face of the inner membrane on an UndPP lipid anchor. After complete assembly, the entire lipid-linked polymer is exported across the inner membrane by the Wzm–Wzt ABC transporter, and then ligated to lipid A-core in the periplasm (king2009reviewlipopolysaccharidebiosynthesis pages 21-23, lam2011geneticandfunctional pages 8-9).

### 4.2 Gene Cluster and Enzymatic Steps

The CPA biosynthesis genes are organized in a cluster. The following table summarizes the roles of the key genes in this pathway:

| Gene | PA locus (PAO1) | Function | Role in CPA pathway |
|---|---|---|---|
| wbpL | PA3146 | Undecaprenyl-phosphate HexNAc-1-phosphate transferase that initiates O-polysaccharide assembly on the lipid carrier | Initiates CPA synthesis on the cytoplasmic face of the inner membrane by adding the first sugar-phosphate to UndP; also required for initiation of OSA synthesis (king2009reviewlipopolysaccharidebiosynthesis pages 21-23) |
| algC | not specified in retrieved evidence | Phosphomannomutase/phosphoglucomutase contributing precursor formation for GDP-D-rhamnose biosynthesis | Supplies mannose-1-phosphate precursor used upstream in GDP-D-rhamnose production for CPA assembly (lam2011geneticandfunctional pages 8-9) |
| wbpW | not specified in retrieved evidence | Phosphomannose isomerase | Converts fructose-6-phosphate to mannose-6-phosphate in the precursor pathway leading to GDP-D-rhamnose for CPA biosynthesis (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 23-24) |
| gmd | not specified in retrieved evidence | GDP-mannose 4,6-dehydratase | Converts GDP-mannose toward GDP-4-keto-6-deoxymannose in the GDP-D-rhamnose biosynthetic pathway that supplies CPA sugar donor (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 23-24) |
| rmd | not specified in retrieved evidence | GDP-4-keto-6-deoxymannose reductase | Completes GDP-D-rhamnose synthesis, generating the activated sugar donor required for the D-rhamnan CPA polymer (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 23-24) |
| wbpX | not specified in retrieved evidence | Rhamnosyltransferase | Adds D-rhamnose residues during assembly of the CPA trisaccharide repeat/polymer on the lipid carrier (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 25-27) |
| wbpY | not specified in retrieved evidence | Rhamnosyltransferase | Adds D-rhamnose residues during assembly of the CPA trisaccharide repeat/polymer on the lipid carrier (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 25-27) |
| wbpZ | not specified in retrieved evidence | Rhamnosyltransferase | Adds D-rhamnose residues during assembly of the CPA trisaccharide repeat/polymer on the lipid carrier; together with WbpX/WbpY builds the characteristic α-linked D-rhamnan structure (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 25-27) |
| wzm | PA5451 | ABC transporter permease / transmembrane domain (TMD) subunit | Exports completed UndPP-linked CPA across the inner membrane to the periplasmic face for ligation to lipid A-core; loss blocks export but not polymer synthesis (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15) |
| wzt | not specified in retrieved evidence | ABC transporter ATP-binding cassette ATPase / nucleotide-binding domain (NBD) subunit | Provides ATP-driven energy for Wzm-Wzt-mediated export of completed CPA across the inner membrane; loss phenocopies wzm mutants with intracellular accumulation of lipid-linked CPA (king2009reviewlipopolysaccharidebiosynthesis pages 25-27, rocchetta1999geneticsofoantigen pages 14-15) |


*Table: This table summarizes the core genes requested for CPA/A-band O-antigen biosynthesis in P. aeruginosa PAO1, linking each gene to its enzymatic or transport role in the pathway. It is useful for mapping Wzm into the broader precursor synthesis, polymer assembly, and export steps of CPA production.*

The biosynthetic pathway proceeds through: (1) synthesis of GDP-D-rhamnose from central metabolic precursors via AlgC, WbpW, Gmd, and Rmd; (2) initiation of polymer assembly on UndP by WbpL; (3) polymerization of the D-rhamnose trisaccharide repeating units by rhamnosyltransferases WbpX, WbpY, and WbpZ; (4) **export of the completed UndPP-linked polymer by the Wzm–Wzt ABC transporter**; and (5) ligation to lipid A-core in the periplasm (lam2011geneticandfunctional pages 8-9, king2009reviewlipopolysaccharidebiosynthesis pages 25-27, king2009reviewlipopolysaccharidebiosynthesis pages 21-23). Additional genes (PA5455–PA5459) encoding methyltransferases and acetyltransferases are also required for CPA biosynthesis (lam2011geneticandfunctional pages 9-10).

## 5. Structural Biology of the Wzm–Wzt Transporter

While structural studies have not been performed directly on *P. aeruginosa* Wzm, extensive structural characterization of homologous Wzm–Wzt transporters from *Aquifex aeolicus* and *Mycobacterium abscessus* provides detailed insight into the architecture of this transporter family, which is directly relevant to understanding the *P. aeruginosa* protein.

### 5.1 Transmembrane Architecture

The crystal structure of the *A. aeolicus* Wzm–Wzt homolog revealed that **each Wzm protomer contains six transmembrane helices (TM1–TM6)**, preceded by an N-terminal amphipathic interface helix (bi2018architectureofa pages 1-2, bi2018architectureofa pages 2-3, caffalette2021cryoemstructureof pages 2-2). Two Wzm protomers interact closely through TM1 and TM5 to form a **large continuous transmembrane channel** spanning the entire membrane width, which is sufficiently wide (accessible to a ~3.5 Å radius probe) to accommodate linear polysaccharide chains (bi2018architectureofa pages 2-3). The channel features three layers of aromatic residues that coordinate the polysaccharide substrate through CH–π stacking interactions (bi2018architectureofa pages 2-3).

### 5.2 Gate Helices and Aromatic Belt

Key structural features include **gate helices** at both the cytosolic and periplasmic membrane interfaces, which serve as substrate entry and exit points, respectively (bi2018architectureofa pages 1-2). The periplasmic gate helices (PG1 and PG2) are formed by the TM5/TM6 loop, while the cytosolic gate helix is contributed by the Wzt NBD and packs against the Wzm protomer interface (bi2018architectureofa pages 1-2, caffalette2021cryoemstructureof pages 2-2). An **aromatic belt** near the periplasmic channel exit, composed of conserved residues such as Tyr39, Phe180, and Trp181, seals the transporter in its resting ATP-bound state (caffalette2021cryoemstructureof pages 1-2, caffalette2021cryoemstructureof pages 2-4). These aromatic residues dilate during substrate translocation to form the open channel (spellmon2022molecularbasisfor pages 7-8).

### 5.3 Conformational States

Cryo-EM structures have revealed multiple conformational states of the transporter. In the ATP-bound resting state, the channel is closed with an asymmetric architecture showing one open and one closed portal at both cytosolic and periplasmic sides (caffalette2021cryoemstructureof pages 1-2). The nucleotide-free (apo) state shows the widest channel diameter, suggesting that conformational cycling between these states drives polysaccharide translocation (caffalette2021cryoemstructureof pages 4-6). Recent cryo-EM studies of the mycobacterial Wzm–Wzt homolog have confirmed that the cytosolic gate helix plays a key functional role in polysaccharide transport, and that the hydrophobic polyprenyl lipid moiety is translocated first, followed by the polysaccharide chain (garaeva2026structuralbasisof pages 2-3).

## 6. Transport Mechanism

### 6.1 Processive Channel Mechanism

The Wzm–Wzt transporter operates through a **processive channel-forming mechanism** that is distinct from the classical alternating access mechanism used by most ABC transporters (bi2018architectureofa pages 1-2, spellmon2022molecularbasisfor pages 9-11). This mechanism is better suited for translocating high-molecular-mass polysaccharides. The transporter forms a continuous transmembrane channel, and the polysaccharide is ratcheted through this channel at the expense of **ATP hydrolysis** (spellmon2022molecularbasisfor pages 9-11, caffalette2021cryoemstructureof pages 4-6).

### 6.2 Role of ATP Hydrolysis

ATP hydrolysis at the Wzt NBDs drives repeated cycles of conformational changes in the Wzm TMDs that energize processive polymer translocation (bi2018architectureofa pages 4-5, caffalette2021cryoemstructureof pages 4-6). ATP-induced NBD closure triggers rigid-body movements of the Wzm protomers around a central helix axis, modulating channel width and facilitating stepwise translocation (caffalette2021cryoemstructureof pages 4-6). Notably, studies on the *A. aeolicus* system showed that O-antigen cap binding to the carbohydrate-binding domain (CBD) of Wzt causes **stalling of ATPase activity**, which may position the lipid moiety at the channel entrance before the transport cycle begins (spellmon2022molecularbasisfor pages 9-11). Multiple rounds of ATP hydrolysis then drive the actual polymer translocation process (spellmon2022molecularbasisfor pages 9-11).

### 6.3 Substrate Recognition via the Carbohydrate-Binding Domain

In many Wzm–Wzt systems, the Wzt subunit possesses a **carbohydrate-binding domain (CBD)** that recognizes the chemically modified nonreducing terminus of the O-antigen polymer (spellmon2022molecularbasisfor pages 9-11). In *P. aeruginosa*, the CPA polymer appears to have modifications at its nonreducing terminal residue, likely methylation, which may serve as a signal for recognition and translocation competency (king2009reviewlipopolysaccharidebiosynthesis pages 25-27). The CBD recruits the lipid-linked substrate to the transporter, increasing local concentration and facilitating channel loading (spellmon2022molecularbasisfor pages 9-11).

## 7. Biological Significance and Role in Pathogenesis

### 7.1 CPA in Chronic Infection

CPA is produced by the majority of *P. aeruginosa* isolates and is particularly significant in chronic infections. In cystic fibrosis (CF) patients with chronic *P. aeruginosa* lung infections, clinical isolates characteristically **maintain CPA expression while losing B-band (OSA) O-antigen expression** (rocchetta1999geneticsofoantigen pages 3-4). A study of 250 CF patient isolates found that 68% expressed A-band LPS but none expressed B-band O-antigen (rocchetta1999geneticsofoantigen pages 3-4). This selective enrichment of CPA during chronic CF infection suggests it provides a survival advantage in the host environment (lam2011geneticandfunctional pages 9-10).

### 7.2 CPA and Bacterial Adherence

CPA contributes to **bacterial adherence to human epithelial cells**. A CPA-deficient mutant (*rmd* knockout, defective in GDP-D-rhamnose synthesis) showed significantly reduced efficiency in adhering to cultured human bronchial epithelial cells, with mutant bacteria attaching as isolated bacteria rather than forming microcolonies (king2009reviewlipopolysaccharidebiosynthesis pages 4-5, lam2011geneticandfunctional pages 9-10).

### 7.3 CPA and Immune Modulation

Unlike B-band O-antigen, CPA alone **does not confer serum resistance** or protect against complement-mediated lysis (rocchetta1999geneticsofoantigen pages 3-4). Antibodies against A-band LPS are not protective in animal models, in contrast to anti-B-band antibodies that are highly protective (rocchetta1999geneticsofoantigen pages 3-4). However, CPA serves as a **receptor for bacteriophage A7**, indicating its significance as a cell surface determinant co-evolving with phage predation (lam2011geneticandfunctional pages 8-9).

### 7.4 CPA and Virulence Regulation

Interestingly, when both OSA and CPA are absent from *P. aeruginosa*, there are pronounced increases in expression of type III secretion system (T3SS) effector genes (*exoS*, *exoT*) and associated regulatory genes (*exsA*, *pcrV*), along with increased cytotoxicity in both *in vitro* and *in vivo* models (lam2011geneticandfunctional pages 18-19). This suggests that the presence of CPA on the cell surface functions as a **negative modulator of T3SS-mediated virulence** (lam2011geneticandfunctional pages 18-19).

## 8. Evolutionary Context

The Wzm–Wzt transporter system is broadly conserved across Gram-negative and Gram-positive bacteria for the export of diverse cell surface glycoconjugates. Homologous systems have been characterized in *Escherichia coli*, *Klebsiella pneumoniae*, *Rhizobium etli*, *Myxococcus xanthus*, and *Mycobacterium* species, where they transport structurally diverse polysaccharides including O-antigens, capsular polysaccharides, and arabinogalactan precursors (valvano2003exportofospecific pages 8-9, garaeva2026structuralbasisof pages 2-3). The functional interchangeability of Wzm components between different bacterial species has been demonstrated, underscoring the conservation of this transport mechanism (king2009reviewlipopolysaccharidebiosynthesis pages 25-27). The ABC-2 family classification of Wzm proteins reflects their shared evolutionary origin and conserved structural architecture across diverse bacterial lineages.

## 9. Summary

Wzm (PA5451) in *P. aeruginosa* PAO1 is an essential **inner membrane ABC transporter permease** that exports the **UndPP-linked D-rhamnose homopolymer (CPA/A-band O-antigen)** from the cytoplasm to the periplasm. It functions as a homodimeric transmembrane channel in partnership with the Wzt ATPase, using a **processive, ATP-driven channel mechanism** to translocate the polysaccharide substrate. Structural studies of homologs reveal a channel formed by six transmembrane helices per protomer, with gate helices and an aromatic belt controlling substrate access. CPA export by Wzm–Wzt is essential for surface display of A-band LPS, which plays roles in epithelial cell adherence, chronic infection maintenance in cystic fibrosis, and modulation of virulence factor expression in *P. aeruginosa*.

References

1. (king2009reviewlipopolysaccharidebiosynthesis pages 25-27): Jerry D. King, Dana Kocíncová, Erin L. Westman, and Joseph S. Lam. Review: lipopolysaccharide biosynthesis in pseudomonas aeruginosa. Innate Immunity, 15:261-312, Aug 2009. URL: https://doi.org/10.1177/1753425909106436, doi:10.1177/1753425909106436. This article has 451 citations and is from a peer-reviewed journal.

2. (rocchetta1999geneticsofoantigen pages 14-15): H. L. Rocchetta, L. L. Burrows, and J. S. Lam. Genetics of o-antigen biosynthesis inpseudomonas aeruginosa. Microbiology and Molecular Biology Reviews, 63:523-553, Sep 1999. URL: https://doi.org/10.1128/mmbr.63.3.523-553.1999, doi:10.1128/mmbr.63.3.523-553.1999. This article has 488 citations and is from a domain leading peer-reviewed journal.

3. (valvano2003exportofospecific pages 8-9): Miguel A Valvano. Export of o-specific lipopolysaccharide. Frontiers in bioscience : a journal and virtual library, 8:s452-71, May 2003. URL: https://doi.org/10.2741/1079, doi:10.2741/1079. This article has 194 citations.

4. (lam2011geneticandfunctional pages 8-9): Joseph S. Lam, Véronique L. Taylor, Salim T. Islam, Youai Hao, and Dana Kocíncová. Genetic and functional diversity of pseudomonas aeruginosa lipopolysaccharide. Frontiers in Microbiology, Apr 2011. URL: https://doi.org/10.3389/fmicb.2011.00118, doi:10.3389/fmicb.2011.00118. This article has 386 citations and is from a peer-reviewed journal.

5. (king2009reviewlipopolysaccharidebiosynthesis pages 21-23): Jerry D. King, Dana Kocíncová, Erin L. Westman, and Joseph S. Lam. Review: lipopolysaccharide biosynthesis in pseudomonas aeruginosa. Innate Immunity, 15:261-312, Aug 2009. URL: https://doi.org/10.1177/1753425909106436, doi:10.1177/1753425909106436. This article has 451 citations and is from a peer-reviewed journal.

6. (caffalette2021cryoemstructureof pages 1-2): Christopher A. Caffalette and Jochen Zimmer. Cryo-em structure of the full-length wzmwzt abc transporter required for lipid-linked o antigen transport. Dec 2021. URL: https://doi.org/10.1073/pnas.2016144118, doi:10.1073/pnas.2016144118. This article has 32 citations and is from a highest quality peer-reviewed journal.

7. (bi2018architectureofa pages 1-2): Yunchen Bi, Evan Mann, Chris Whitfield, and Jochen Zimmer. Architecture of a channel-forming o-antigen polysaccharide abc transporter. Jan 2018. URL: https://doi.org/10.1038/nature25190, doi:10.1038/nature25190. This article has 118 citations and is from a highest quality peer-reviewed journal.

8. (bi2018architectureofa pages 2-3): Yunchen Bi, Evan Mann, Chris Whitfield, and Jochen Zimmer. Architecture of a channel-forming o-antigen polysaccharide abc transporter. Jan 2018. URL: https://doi.org/10.1038/nature25190, doi:10.1038/nature25190. This article has 118 citations and is from a highest quality peer-reviewed journal.

9. (caffalette2021cryoemstructureof pages 2-2): Christopher A. Caffalette and Jochen Zimmer. Cryo-em structure of the full-length wzmwzt abc transporter required for lipid-linked o antigen transport. Dec 2021. URL: https://doi.org/10.1073/pnas.2016144118, doi:10.1073/pnas.2016144118. This article has 32 citations and is from a highest quality peer-reviewed journal.

10. (king2009reviewlipopolysaccharidebiosynthesis pages 20-21): Jerry D. King, Dana Kocíncová, Erin L. Westman, and Joseph S. Lam. Review: lipopolysaccharide biosynthesis in pseudomonas aeruginosa. Innate Immunity, 15:261-312, Aug 2009. URL: https://doi.org/10.1177/1753425909106436, doi:10.1177/1753425909106436. This article has 451 citations and is from a peer-reviewed journal.

11. (caffalette2021cryoemstructureof pages 2-4): Christopher A. Caffalette and Jochen Zimmer. Cryo-em structure of the full-length wzmwzt abc transporter required for lipid-linked o antigen transport. Dec 2021. URL: https://doi.org/10.1073/pnas.2016144118, doi:10.1073/pnas.2016144118. This article has 32 citations and is from a highest quality peer-reviewed journal.

12. (spellmon2022molecularbasisfor pages 9-11): Nicholas Spellmon, Artur Muszyński, Ireneusz Górniak, Jiri Vlach, David Hahn, Parastoo Azadi, and Jochen Zimmer. Molecular basis for polysaccharide recognition and modulated atp hydrolysis by the o antigen abc transporter. Nature Communications, Sep 2022. URL: https://doi.org/10.1038/s41467-022-32597-2, doi:10.1038/s41467-022-32597-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (bi2018architectureofa pages 4-5): Yunchen Bi, Evan Mann, Chris Whitfield, and Jochen Zimmer. Architecture of a channel-forming o-antigen polysaccharide abc transporter. Jan 2018. URL: https://doi.org/10.1038/nature25190, doi:10.1038/nature25190. This article has 118 citations and is from a highest quality peer-reviewed journal.

14. (caffalette2021cryoemstructureof pages 4-6): Christopher A. Caffalette and Jochen Zimmer. Cryo-em structure of the full-length wzmwzt abc transporter required for lipid-linked o antigen transport. Dec 2021. URL: https://doi.org/10.1073/pnas.2016144118, doi:10.1073/pnas.2016144118. This article has 32 citations and is from a highest quality peer-reviewed journal.

15. (king2009reviewlipopolysaccharidebiosynthesis pages 23-24): Jerry D. King, Dana Kocíncová, Erin L. Westman, and Joseph S. Lam. Review: lipopolysaccharide biosynthesis in pseudomonas aeruginosa. Innate Immunity, 15:261-312, Aug 2009. URL: https://doi.org/10.1177/1753425909106436, doi:10.1177/1753425909106436. This article has 451 citations and is from a peer-reviewed journal.

16. (rocchetta1999geneticsofoantigen pages 6-8): H. L. Rocchetta, L. L. Burrows, and J. S. Lam. Genetics of o-antigen biosynthesis inpseudomonas aeruginosa. Microbiology and Molecular Biology Reviews, 63:523-553, Sep 1999. URL: https://doi.org/10.1128/mmbr.63.3.523-553.1999, doi:10.1128/mmbr.63.3.523-553.1999. This article has 488 citations and is from a domain leading peer-reviewed journal.

17. (lam2011geneticandfunctional pages 9-10): Joseph S. Lam, Véronique L. Taylor, Salim T. Islam, Youai Hao, and Dana Kocíncová. Genetic and functional diversity of pseudomonas aeruginosa lipopolysaccharide. Frontiers in Microbiology, Apr 2011. URL: https://doi.org/10.3389/fmicb.2011.00118, doi:10.3389/fmicb.2011.00118. This article has 386 citations and is from a peer-reviewed journal.

18. (spellmon2022molecularbasisfor pages 7-8): Nicholas Spellmon, Artur Muszyński, Ireneusz Górniak, Jiri Vlach, David Hahn, Parastoo Azadi, and Jochen Zimmer. Molecular basis for polysaccharide recognition and modulated atp hydrolysis by the o antigen abc transporter. Nature Communications, Sep 2022. URL: https://doi.org/10.1038/s41467-022-32597-2, doi:10.1038/s41467-022-32597-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

19. (garaeva2026structuralbasisof pages 2-3): Alisa A. Garaeva, Viktória Fabianová, Karin Savková, Stanislav Huszár, Xiaochao Xue, Todd L. Lowary, Katarína Mikušová, and Markus A. Seeger. Structural basis of lipid-linked galactan export by the mycobacterial abc transporter wzm-wzt. Nature Communications, Mar 2026. URL: https://doi.org/10.1038/s41467-026-70429-9, doi:10.1038/s41467-026-70429-9. This article has 0 citations and is from a highest quality peer-reviewed journal.

20. (rocchetta1999geneticsofoantigen pages 3-4): H. L. Rocchetta, L. L. Burrows, and J. S. Lam. Genetics of o-antigen biosynthesis inpseudomonas aeruginosa. Microbiology and Molecular Biology Reviews, 63:523-553, Sep 1999. URL: https://doi.org/10.1128/mmbr.63.3.523-553.1999, doi:10.1128/mmbr.63.3.523-553.1999. This article has 488 citations and is from a domain leading peer-reviewed journal.

21. (king2009reviewlipopolysaccharidebiosynthesis pages 4-5): Jerry D. King, Dana Kocíncová, Erin L. Westman, and Joseph S. Lam. Review: lipopolysaccharide biosynthesis in pseudomonas aeruginosa. Innate Immunity, 15:261-312, Aug 2009. URL: https://doi.org/10.1177/1753425909106436, doi:10.1177/1753425909106436. This article has 451 citations and is from a peer-reviewed journal.

22. (lam2011geneticandfunctional pages 18-19): Joseph S. Lam, Véronique L. Taylor, Salim T. Islam, Youai Hao, and Dana Kocíncová. Genetic and functional diversity of pseudomonas aeruginosa lipopolysaccharide. Frontiers in Microbiology, Apr 2011. URL: https://doi.org/10.3389/fmicb.2011.00118, doi:10.3389/fmicb.2011.00118. This article has 386 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Q9HTB8-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Q9HTB8-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. rocchetta1999geneticsofoantigen pages 14-15
2. king2009reviewlipopolysaccharidebiosynthesis pages 21-23
3. lam2011geneticandfunctional pages 8-9
4. lam2011geneticandfunctional pages 9-10
5. bi2018architectureofa pages 2-3
6. bi2018architectureofa pages 1-2
7. spellmon2022molecularbasisfor pages 7-8
8. caffalette2021cryoemstructureof pages 1-2
9. caffalette2021cryoemstructureof pages 4-6
10. garaeva2026structuralbasisof pages 2-3
11. spellmon2022molecularbasisfor pages 9-11
12. king2009reviewlipopolysaccharidebiosynthesis pages 25-27
13. rocchetta1999geneticsofoantigen pages 3-4
14. lam2011geneticandfunctional pages 18-19
15. valvano2003exportofospecific pages 8-9
16. caffalette2021cryoemstructureof pages 2-2
17. king2009reviewlipopolysaccharidebiosynthesis pages 20-21
18. caffalette2021cryoemstructureof pages 2-4
19. bi2018architectureofa pages 4-5
20. king2009reviewlipopolysaccharidebiosynthesis pages 23-24
21. rocchetta1999geneticsofoantigen pages 6-8
22. king2009reviewlipopolysaccharidebiosynthesis pages 4-5
23. →3)-α-D-Rha-(1→3)-α-D-Rha-(1→2)-α-D-Rha-(1→
24. https://doi.org/10.1177/1753425909106436,
25. https://doi.org/10.1128/mmbr.63.3.523-553.1999,
26. https://doi.org/10.2741/1079,
27. https://doi.org/10.3389/fmicb.2011.00118,
28. https://doi.org/10.1073/pnas.2016144118,
29. https://doi.org/10.1038/nature25190,
30. https://doi.org/10.1038/s41467-022-32597-2,
31. https://doi.org/10.1038/s41467-026-70429-9,