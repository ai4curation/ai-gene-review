---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:57:13.800080'
end_time: '2026-07-11T19:10:25.646206'
duration_seconds: 791.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sdhD
  gene_symbol: sdhD
  uniprot_accession: Q88FA6
  protein_description: 'RecName: Full=Succinate dehydrogenase hydrophobic membrane
    anchor subunit {ECO:0000256|ARBA:ARBA00019425, ECO:0000256|PIRNR:PIRNR000169};'
  gene_info: Name=sdhD {ECO:0000313|EMBL:AAN69773.1}; OrderedLocusNames=PP_4192 {ECO:0000313|EMBL:AAN69773.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: SQR/QFR_C/D. (IPR034804); Succ_DH_anchor. (IPR014312); SuccDH_FuR_B_TM-su.
    (IPR000701); Sdh_cyt (PF01127)
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
  path: sdhD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sdhD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FA6
- **Protein Description:** RecName: Full=Succinate dehydrogenase hydrophobic membrane anchor subunit {ECO:0000256|ARBA:ARBA00019425, ECO:0000256|PIRNR:PIRNR000169};
- **Gene Information:** Name=sdhD {ECO:0000313|EMBL:AAN69773.1}; OrderedLocusNames=PP_4192 {ECO:0000313|EMBL:AAN69773.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** SQR/QFR_C/D. (IPR034804); Succ_DH_anchor. (IPR014312); SuccDH_FuR_B_TM-su. (IPR000701); Sdh_cyt (PF01127)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sdhD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sdhD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sdhD** (gene ID: sdhD, UniProt: Q88FA6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sdhD* (PP_4192, UniProt Q88FA6) in *Pseudomonas putida* KT2440

## Summary

**The gene *sdhD* (locus PP_4192; UniProt Q88FA6) of *Pseudomonas putida* KT2440 encodes SdhD, the "D" membrane-anchor subunit of succinate dehydrogenase (SDH), also known as respiratory Complex II or succinate:ubiquinone oxidoreductase (EC 1.3.5.1).** The gene symbol, the UniProt description, the InterPro/Pfam domain architecture (IPR014312 Succ_DH_anchor; IPR000701 SuccDH_FuR_B_TM-su; IPR034804 SQR/QFR_C/D; PF01127 Sdh_cyt), and the genomic context all converge unambiguously on this identity. This is the correct gene — the target gene symbol, organism, and domain complement are mutually consistent, and no ambiguity with an unrelated same-symbol gene was encountered.

SdhD is a small (122-residue) polytopic integral protein of the cytoplasmic (inner) membrane, predicted to span the bilayer three times (transmembrane helices at approximately residues 21–39, 59–77, and 98–120). It has no catalytic activity of its own. Instead, together with its partner anchor subunit SdhC, it (i) tethers the soluble catalytic head of the enzyme — the SdhA flavoprotein and the SdhB iron–sulfur protein — to the cytoplasmic face of the inner membrane; (ii) supplies one axial ligand (His71) for a single bridging *b*-type heme shared with SdhC; and (iii) contributes a conserved residue (Tyr83) to the proximal ubiquinone-binding (Qp) site. Through these structural and cofactor-holding roles, SdhD completes the physical electron-transfer conduit that carries electrons from succinate, via FAD and the iron–sulfur clusters, to membrane ubiquinone. Its membrane-side substrate is therefore **ubiquinone**, which it helps reduce to ubiquinol.

Biologically, SdhD sits precisely at the junction between the tricarboxylic acid (TCA/Krebs) cycle and the aerobic respiratory chain: the reaction its complex catalyzes (succinate + ubiquinone ⇌ fumarate + ubiquinol) is simultaneously the succinate-oxidizing step of the TCA cycle and an electron-donating step to the quinone pool of oxidative phosphorylation. The gene lies in a conserved *sdhCDAB* operon, itself embedded in the *gltA–sdhCDAB–sucAB* gene cluster that co-locates SDH with citrate synthase and 2-oxoglutarate dehydrogenase — a genomic arrangement inherited essentially intact from the canonical *Escherichia coli* organization. On the basis of its two-anchor-subunit, single-heme architecture, *P. putida* Complex II belongs to the *E. coli*-like (type C) class of the Complex II superfamily.

---

## Key Findings

### Finding 1 — Q88FA6 is the membrane-anchor subunit D of succinate dehydrogenase (Complex II)

The primary identity of the gene product is firmly established. UniProt Q88FA6 describes a 122-amino-acid integral membrane protein carrying three predicted helical transmembrane segments, annotated with the FUNCTION "Membrane-anchoring subunit of succinate dehydrogenase (SDH)," a heme COFACTOR, membership in the tricarboxylic acid cycle pathway (UniPathway UPA00223), and a SUBCELLULAR LOCATION of "cell inner membrane." Its domain signatures — InterPro IPR014312 (Succ_DH_anchor), IPR000701 (SuccDH_FuR_B_TM-su), IPR034804 (SQR/QFR_C/D), and Pfam PF01127 (Sdh_cyt) — are precisely the diagnostic domains of the cytochrome-*b* / membrane-anchor module of the Complex II superfamily. The gene maps to KEGG entry ppu:PP_4192 and orthology group eggNOG COG2142.

Complex II is a highly conserved four-subunit enzyme. As stated directly in the literature, "*Complex II consists of four subunits including a catalytic flavoprotein (SdhA), an iron-sulphur subunit (SdhB) and two hydrophobic membrane anchors (SdhC and SdhD)*" ([PMID: 22985599](https://pubmed.ncbi.nlm.nih.gov/22985599/)). SdhD is one of those two hydrophobic membrane anchors. The source organism and genome are likewise confirmed: sequencing of "*the 6.18 Mb genome of strain KT2440*" ([PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/)) documents the *P. putida* KT2440 chromosome that encodes PP_4192/*sdhD*.

### Finding 2 — SdhD provides a heme *b* axial ligand (His71) and, with SdhC, builds the ubiquinone-reduction site

Q88FA6 carries an annotated axial heme-binding residue at **His71** (UniProt binding site 71, "axial binding residue"), with a second annotated binding site at residue 83. His71 maps exactly onto *E. coli* SdhD-His71, which was experimentally identified by systematic mutagenesis as one of the two histidine axial ligands of the enzyme's *b*-type heme. As reported, "*SDHC-His84 and SDHD-His71 have been identified as the most likely heme axial ligands in the E. coli enzyme, suggesting that the heme bridges these two subunits in the membrane*" ([PMID: 9521736](https://pubmed.ncbi.nlm.nih.gov/9521736/)). A single heme *b* thus sits at the SdhC/SdhD interface, held on one side by SdhD-His71 and on the other by SdhC-His84.

The heme-ligating histidine lies within a transmembrane helix — consistent with the position of His71 inside the predicted TM helix (residues 59–77) of Q88FA6: "*Histidine residues, which are possible heme axial ligands in cytochrome b of complex II, were found in the second transmembrane segment of each subunit*" ([PMID: 9533030](https://pubmed.ncbi.nlm.nih.gov/9533030/)). The crystal structure of the homologous *E. coli* enzyme traces the complete electron path "*revealing the electron transport pathway from the electron donor, succinate, to the terminal electron acceptor, ubiquinone*" ([PMID: 12560550](https://pubmed.ncbi.nlm.nih.gov/12560550/)). In this pathway, the quinone site is formed at the SdhC/SdhD membrane interface, and although the four subunits can assemble even without heme, heme is required for full electron transfer.

### Finding 3 — *sdhD* lies in a conserved *sdhCDAB–sucAB* operon linking Complex II to the TCA cycle

Genomic mapping of the KT2440 chromosome places *sdhD* in an intact, canonical operon. Reading along the complement strand (high→low coordinate): PP_4193 *sdhC* (KEGG K00241, cytochrome *b*-556 subunit) → **PP_4192 *sdhD*** (K00242, membrane anchor) → PP_4191 *sdhA* (K00239, flavoprotein, EC 1.3.5.1) → PP_4190 *sdhB* (K00240, Fe–S subunit) → PP_4189 *sucA* (2-oxoglutarate dehydrogenase E1) → PP_4188 *sucB* (E2). Citrate synthase *gltA* (PP_4194, K01647) sits immediately adjacent on the opposite strand. Notably, *sdhC* (coordinates 4738735–4739121) and *sdhD* (4738373–4738741) overlap/abut by ~7 bp, an arrangement indicative of translational coupling. KEGG assigns PP_4192 to Module M00149 (Succinate dehydrogenase, prokaryotes) and to pathways ppu00020 (TCA cycle) and ppu00190 (oxidative phosphorylation).

This gene order reproduces the classic *E. coli* organization: "*Together with the iron-sulphur protein gene (sdhB) these genes form an operon (sdhCDAB) situated between the citrate synthase gene (gltA) and the 2-oxoglutarate dehydrogenase complex genes (sucAB): gltA-sdhCDAB-sucAB*" ([PMID: 6383359](https://pubmed.ncbi.nlm.nih.gov/6383359/)). The conservation of both the *sdhCDAB* internal order and the flanking *gltA*/*sucAB* genes strongly implies a co-regulated, co-inherited TCA/respiration gene module in *P. putida*.

### Finding 4 — *P. putida* Complex II is an *E. coli*-type (type C) single-heme enzyme catalyzing succinate:ubiquinone oxidoreduction (EC 1.3.5.1)

The enzyme SdhD anchors catalyzes the reaction succinate + ubiquinone ⇌ fumarate + ubiquinol, which "*couples the oxidation of succinate in the matrix / cytoplasm to the reduction of quinone in the membrane. This function directly connects the Krebs cycle and the aerobic respiratory chain*" ([PMID: 15078221](https://pubmed.ncbi.nlm.nih.gov/15078221/)). The architecture of the membrane anchor varies across the Complex II superfamily: some organisms (e.g., *Bacillus subtilis* SQR, *Wolinella succinogenes* QFR) use a single hydrophobic subunit with two heme *b* groups, whereas "*SQR and QFR of Escherichia coli contain two hydrophobic subunits (C and D) which bind either one (SQR) or no haem b group (QFR)*" ([PMID: 11004459](https://pubmed.ncbi.nlm.nih.gov/11004459/)).

*P. putida* KT2440 encodes the two-subunit configuration — SdhC (K00241, "cytochrome *b*-556") plus SdhD (K00242) — with a single bridging heme *b* whose axial ligand His71 is contributed by Q88FA6. This places its Complex II squarely in the *E. coli*-like (type C) class: a two-anchor, single-heme succinate:ubiquinone reductase operating in the forward (aerobic, succinate-oxidizing) direction. SdhD's transmembrane helices and its share of the heme thus complete the physiological aerobic electron-transfer enzyme.

### Finding 5 — Both functional residues of *P. putida* SdhD (His71, Tyr83) are conserved with *E. coli* SdhD

A global Needleman–Wunsch alignment of Q88FA6 (122 aa) against *E. coli* K-12 SdhD (P0AC44, 115 aa) gives roughly 36.5% identity (42/115 over the aligned length) — a modest overall value that is typical of the poorly conserved membrane-anchor subunits and stands in contrast to the far higher conservation of the soluble catalytic SdhA/SdhB subunits. Despite the low global identity, the two functionally critical residues align exactly:

- **His71 ↔ His71** (heme *b* axial ligand), within a conserved "…HAW-x-GMW…" motif (*P. putida* GAHAWVGMW vs *E. coli* IHAWIGMW).
- **Tyr83 ↔ Tyr83** (quinone binding), within a conserved "TDY" motif.

In the *E. coli* SQR crystal structure, SdhD-Tyr83 hydrogen-bonds the ubiquinone at the proximal quinone (Qp) site, cooperating with SdhB-His207 and SdhC residues, while SdhD-His71 axially ligates the heme *b*. The heme role is anchored by the mutagenesis result that "*SDHC-His84 and SDHD-His71 have been identified as the most likely heme axial ligands in the E. coli enzyme*" ([PMID: 9521736](https://pubmed.ncbi.nlm.nih.gov/9521736/)), and the quinone role by the structural definition of the pathway "*from the electron donor, succinate, to the terminal electron acceptor, ubiquinone*" ([PMID: 12560550](https://pubmed.ncbi.nlm.nih.gov/12560550/)). The precise conservation of both residues justifies confidently transferring the *E. coli* mechanistic assignments to *P. putida* SdhD.

### Finding 6 — SdhD localizes to and functions within the cytoplasmic (inner) membrane, orienting the catalytic head toward the cytoplasm

UniProt Q88FA6 gives a SUBCELLULAR LOCATION of "Cell inner membrane," with keywords Cell inner membrane / Cell membrane / Membrane / Transmembrane helix. With three predicted transmembrane α-helices (~21–39, 59–77, 98–120), SdhD is a polytopic integral membrane protein. Together, SdhC and SdhD form the membrane-embedded cytochrome-*b* module, from which the soluble SdhA/SdhB dimer protrudes into the cytoplasm — an orientation consistent with the enzyme coupling "*the oxidation of succinate in the matrix / cytoplasm to the reduction of quinone in the membrane*" ([PMID: 15078221](https://pubmed.ncbi.nlm.nih.gov/15078221/)). The three-transmembrane-helix anchor topology is a general feature of these subunits: "*both cybL and cybS appear to have three transmembrane segments, indicating their role as membrane-anchors for the enzyme complex*" ([PMID: 9533030](https://pubmed.ncbi.nlm.nih.gov/9533030/)). No secretion signal or periplasmic domain is present, so SdhD carries out its function entirely within, and on the cytoplasmic side of, the inner membrane.

---

## Mechanistic Model / Interpretation

### The reaction and where each event happens

Complex II performs a single, spatially organized redox reaction:

```
     CYTOPLASM (matrix side)
     ┌──────────────────────────────────────────────┐
     │   succinate  ──►  fumarate                     │
     │        │  (2e⁻, 2H⁺)                           │
     │        ▼                                        │
     │      FAD (SdhA, flavoprotein)                   │
     │        │                                        │
     │        ▼                                        │
     │   [2Fe-2S]→[4Fe-4S]→[3Fe-4S]  (SdhB, Fe–S)      │
     │        │                                        │
=====│========▼======= INNER MEMBRANE ================│=====
     │     heme b  ◄── His71 (SdhD) + His84 (SdhC)     │
     │        │                                        │
     │        ▼                                        │
     │   ubiquinone ──► ubiquinol   (Qp site:          │
     │                   SdhD-Tyr83 + SdhB-His207 +    │
     │                   SdhC residues)                │
     └──────────────────────────────────────────────┘
        SdhC + SdhD = membrane anchor / cytochrome b module
```

Electrons are abstracted from succinate at the FAD site of the SdhA flavoprotein on the cytoplasmic side, passed through the iron–sulfur relay of SdhB, and delivered across the membrane interface to ubiquinone. **SdhD's contribution is structural and electron-conducting, not catalytic:** its transmembrane helices anchor the soluble catalytic dimer to the membrane and, with SdhC, sculpt the cytochrome-*b* module; its His71 supplies one of the two axial ligands to the single bridging heme *b*; and its Tyr83 helps form and hydrogen-bond the substrate at the proximal quinone site. The heme is not strictly required for assembly of the four subunits, but it is required for full electron transfer, so SdhD's cofactor-holding role is functionally essential to the physiological enzyme.

### Placement in the Complex II superfamily

| Feature | *P. putida* KT2440 SdhCD | *E. coli* SQR | *B. subtilis* SQR / *W. succinogenes* QFR | Type A (e.g., *T. thermophilus*, *S. acidocaldarius*) |
|---|---|---|---|---|
| Number of membrane anchors | **2 (SdhC + SdhD)** | 2 (C + D) | 1 (single subunit C) | 2 (C + D) |
| Heme *b* content | **1 (bridging C/D)** | 1 (SQR) / 0 (QFR) | 2 | 2 (or non-canonical) |
| Class | **Type C (E. coli-like)** | Type C | Diheme single-anchor types | Type A |
| Direction (physiological) | **Succinate → ubiquinone (aerobic)** | Succinate → UQ | Variable | Succinate → menaquinone/caldariellaquinone |

*P. putida* thus falls in the same class as the well-characterized *E. coli* enzyme, which is why the *E. coli* structural and mutagenesis data transfer so cleanly. Evolutionary analyses suggest that single-heme type C complexes (including mitochondrial Complex II) may have arisen from diheme two-anchor ancestors, consistent with the two-subunit/single-heme configuration seen here.

### Placement in cellular physiology

SdhD's enzyme is the physical hinge between two metabolic subsystems:

- **TCA cycle (ppu00020):** the succinate → fumarate step is catalyzed here, so Complex II is a bona fide cycle enzyme.
- **Oxidative phosphorylation (ppu00190):** the same step feeds electrons into the ubiquinone pool, from which they travel to terminal oxidases.

The conserved *gltA–sdhCDAB–sucAB* gene cluster reinforces this integration at the genetic level, co-locating (and likely co-regulating) succinate dehydrogenase with the neighboring citrate synthase and 2-oxoglutarate dehydrogenase steps of the cycle. In the metabolically versatile *P. putida*, which oxidizes a wide range of carbon sources through central metabolism, a functional Complex II provides the conduit for succinate-derived reducing equivalents to enter aerobic respiration.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [22985599](https://pubmed.ncbi.nlm.nih.gov/22985599/) | *Prokaryotic assembly factors for the attachment of flavin to complex II* | States the four-subunit composition of Complex II, defining SdhD as one of the two hydrophobic membrane anchors (F001). |
| [12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/) | *Complete genome sequence… P. putida KT2440* | Confirms the source organism/genome that encodes PP_4192/*sdhD* (F001). |
| [9521736](https://pubmed.ncbi.nlm.nih.gov/9521736/) | *Localization of histidine residues responsible for heme axial ligation in cytochrome b556… E. coli* | Experimental mutagenesis identifying SdhD-His71 as a heme *b* axial ligand — directly supports the His71 role in *P. putida* (F002, F005). |
| [12560550](https://pubmed.ncbi.nlm.nih.gov/12560550/) | *Architecture of succinate dehydrogenase and reactive oxygen species generation* | Crystal structure establishing the succinate→ubiquinone electron path and quinone site (F002, F005). |
| [9533030](https://pubmed.ncbi.nlm.nih.gov/9533030/) | *Cytochrome b in human complex II… SDHC/SDHD* | Confirms heme-ligating His in a TM helix and the three-TM-helix anchor topology (F002, F006). |
| [6383359](https://pubmed.ncbi.nlm.nih.gov/6383359/) | *Nucleotide sequence encoding… succinate dehydrogenase of E. coli* | Defines the canonical *gltA–sdhCDAB–sucAB* operon matching the KT2440 arrangement (F003). |
| [15078221](https://pubmed.ncbi.nlm.nih.gov/15078221/) | *Complex II from a structural perspective* | States the reaction catalyzed and its role bridging the Krebs cycle and aerobic respiration; defines cytoplasm/membrane orientation (F004, F006). |
| [11004459](https://pubmed.ncbi.nlm.nih.gov/11004459/) | *Succinate:quinone oxidoreductases: new insights from X-ray crystal structures* | Establishes the two-anchor (C+D) single-heme SQR architecture that *P. putida* shares (F004). |
| [36171656](https://pubmed.ncbi.nlm.nih.gov/36171656/) | *Structural Insight into Evolution of the Quinone Binding Site in Complex II* | Supports the type-A–F classification and the evolutionary origin of single-heme type C complexes from diheme ancestors (context for F004). |
| [20951673](https://pubmed.ncbi.nlm.nih.gov/20951673/) | *…succinate:quinone reductase from Thermus thermophilus* | Comparative type A SQR (four subunits, two heme *b*), contrasting with the *E. coli*-like single-heme *P. putida* enzyme (context for F004). |
| [9287013](https://pubmed.ncbi.nlm.nih.gov/9287013/) | *…succinate dehydrogenase… Sulfolobus acidocaldarius* | Illustrates divergent anchor subunits lacking typical TM helices, underscoring anchor variability across the family (context for F004/F005). |

The *P. putida*-specific physiology papers in the literature set (e.g., PHA metabolism [PMID: 22225632](https://pubmed.ncbi.nlm.nih.gov/22225632/); glyoxylate-shunt/TCA rearrangements [PMID: 10698750](https://pubmed.ncbi.nlm.nih.gov/10698750/), [PMID: 22416130](https://pubmed.ncbi.nlm.nih.gov/22416130/); lignin carbon metabolism [PMID: 40883435](https://pubmed.ncbi.nlm.nih.gov/40883435/)) provide the metabolic backdrop in which a functional TCA cycle — and therefore Complex II — operates, but none characterizes SdhD directly.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of Q88FA6/PP_4192.** Every mechanistic claim about *P. putida* SdhD is an inference by orthology from *E. coli* (and, for topology, from human) SDH. There is no published purification, spectroscopy, crystal structure, or mutagenesis of the *P. putida* enzyme itself. The evidence is therefore strong by homology but not by direct experiment in this organism.

2. **Modest sequence identity of the anchor.** Global identity between *P. putida* and *E. coli* SdhD is only ~36.5%. While the two functional residues (His71, Tyr83) are exactly conserved, the low overall identity means fine details — exact heme redox potential, precise quinone-site geometry, and any accessory residues — cannot be assumed identical.

3. **Quinone identity assumed, not measured.** Ubiquinone is inferred as the physiological acceptor from the aerobic, *E. coli*-like classification and KEGG pathway assignment. The actual quinone pool used by *P. putida* Complex II (ubiquinone-9 versus other species, or menaquinone under specific conditions) has not been directly verified here.

4. **Operon transcription not experimentally confirmed in KT2440.** The *sdhCDAB* operon structure and the *sdhC*/*sdhD* overlap are derived from genome coordinates and orthology to *E. coli*; the actual transcript boundaries, promoter, and regulation in *P. putida* have not been experimentally mapped in this investigation.

5. **Predicted (not experimentally determined) membrane topology.** The three-TM-helix model and residue boundaries come from UniProt predictions; no experimental topology mapping for *P. putida* SdhD exists in the reviewed literature.

6. **Assembly-factor and heme-insertion pathway not examined.** Complex II requires assembly factors for flavin attachment (per [PMID: 22985599](https://pubmed.ncbi.nlm.nih.gov/22985599/)); the analogous factors and heme-insertion machinery in *P. putida* were not investigated.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical characterization.** Purify *P. putida* KT2440 Complex II (e.g., via an affinity-tagged SdhC or SdhB), confirm the four-subunit stoichiometry, and quantify heme *b* content and its reduction midpoint potential(s) by UV-visible and EPR spectroscopy — testing the predicted single-heme, *E. coli*-like configuration.

2. **Site-directed mutagenesis of His71 and Tyr83.** Introduce His71→Ala/Met and Tyr83→Phe substitutions in the chromosomal *sdhD* and measure succinate:ubiquinone oxidoreductase activity, heme retention, and quinone-site occupancy, directly testing the inferred heme-ligation and quinone-binding roles in the native organism.

3. **Quinone-species determination.** Extract and identify the quinone(s) reduced by *P. putida* Complex II under aerobic growth to confirm ubiquinone as the physiological acceptor and determine its isoprenoid chain length.

4. **Operon and regulation mapping.** Use RT-PCR/RNA-seq and 5′-RACE to confirm the *sdhCDAB* (and *gltA*, *sucAB*) transcript structure, promoter, and any carbon-source-dependent regulation, verifying the co-transcription implied by the ~7-bp *sdhC*/*sdhD* overlap.

5. **Deletion phenotyping.** Construct a Δ*sdhD* mutant and assay growth on succinate (and other TCA-dependent carbon sources) versus glycolytic substrates, plus whole-cell succinate oxidase activity, to establish the physiological consequence of losing the anchor.

6. **Experimental topology and structure.** Determine SdhD membrane topology (e.g., reporter fusions) and, ideally, obtain a cryo-EM structure of the assembled *P. putida* complex to resolve the heme and quinone sites definitively.

---

## Conclusion

The evidence — UniProt annotation, InterPro/Pfam domain architecture, genomic operon context, and exact conservation of the two catalytically important residues with the experimentally characterized *E. coli* enzyme — converges on a single, well-supported conclusion. *sdhD* (PP_4192, Q88FA6) encodes the D membrane-anchor subunit of *Pseudomonas putida* KT2440 succinate dehydrogenase (Complex II, EC 1.3.5.1): a small, three-TM-helix integral inner-membrane protein that, with SdhC, anchors the soluble SdhA/SdhB catalytic dimer to the cytoplasmic face of the membrane, provides an axial ligand (His71) for the single bridging heme *b*, and contributes to the ubiquinone-reduction (Qp) site (Tyr83). Its role is structural and electron-conducting rather than catalytic; its membrane-side substrate is ubiquinone; and it functions to couple the succinate-oxidizing step of the TCA cycle to the aerobic respiratory chain.


## Artifacts

- [OpenScientist final report](sdhD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sdhD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22985599
2. PMID:12534463
3. PMID:9521736
4. PMID:9533030
5. PMID:12560550
6. PMID:6383359
7. PMID:15078221
8. PMID:11004459
9. PMID:22225632
10. PMID:10698750
11. PMID:22416130
12. PMID:40883435