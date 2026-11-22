---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:25:15.203485'
end_time: '2026-08-31T21:39:50.301427'
duration_seconds: 875.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3199
  gene_symbol: PP_3199
  uniprot_accession: Q88I03
  protein_description: 'SubName: Full=Monooxygenase {ECO:0000313|EMBL:AAN68807.1};'
  gene_info: OrderedLocusNames=PP_3199 {ECO:0000313|EMBL:AAN68807.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: FAD-bd. (IPR002938); FAD-dep_Monooxygenase_BioMet. (IPR050493);
    FAD/NAD-bd_sf. (IPR036188); FAD_binding_3 (PF01494)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3199-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3199-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I03
- **Protein Description:** SubName: Full=Monooxygenase {ECO:0000313|EMBL:AAN68807.1};
- **Gene Information:** OrderedLocusNames=PP_3199 {ECO:0000313|EMBL:AAN68807.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** FAD-bd. (IPR002938); FAD-dep_Monooxygenase_BioMet. (IPR050493); FAD/NAD-bd_sf. (IPR036188); FAD_binding_3 (PF01494)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3199" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3199' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3199** (gene ID: PP_3199, UniProt: Q88I03) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_3199 (UniProt Q88I03)
### *Pseudomonas putida* KT2440 — a FAD-dependent flavonoid (naringenin) C-8 monooxygenase (FdeE ortholog)

---

## 1. Summary / Answer to the Research Question

**PP_3199 (Q88I03) is a soluble, cytoplasmic, single-component FAD-dependent aromatic monooxygenase that catalyzes the committed first step of aerobic flavonoid (flavanone) catabolism in *Pseudomonas putida* KT2440.** It is the ortholog (41.4 % full-length identity, conserved synteny) of the experimentally characterized **FdeE** enzyme of *Herbaspirillum seropedicae* SmR1, a **flavonoid C-8 hydroxylase (F8H)**. The enzyme uses FAD and NAD(P)H to activate molecular O₂ and inserts one oxygen atom as a hydroxyl group at the **C-8 position of the flavonoid A-ring**, converting **naringenin → 8-hydroxynaringenin (5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one)**. This introduces an *ortho*-dihydroxy (catechol/pyrogallol-type) A-ring that is the substrate for the adjacent ring-cleaving dioxygenase FdeC, funneling plant-derived flavonoids into central metabolism (ultimately oxaloacetate → TCA cycle). The enzyme has **broad substrate tolerance** across flavonoid subclasses (flavanones, flavones, isoflavones, flavonols). Its gene sits in a **flavonoid-inducible `fde` operon** controlled by a NodD-like LysR-type regulator (FdeR; KT2440 ortholog **PP_3196**), tying its function to a plant-associated/rhizosphere lifestyle.

> **Identity verification:** The UniProt record (SubName "Monooxygenase", *P. putida* KT2440, OrderedLocusNames PP_3199, Pfam FAD_binding_3/PF01494; InterPro IPR002938, IPR050493, IPR036188) is fully consistent with all evidence gathered here. There is **no ambiguity** — PP_3199/Q88I03 corresponds to a specific FAD-dependent monooxygenase in the KT2440 flavonoid-degradation gene cluster. The direct enzymatic characterization derives from the *Herbaspirillum* ortholog; the KT2440 assignment rests on strong orthology, conserved gene-cluster synteny, and a conserved regulator (see Limitations).

---

## 2. Molecular Identity and Domain Architecture

| Property | Value | Source |
|---|---|---|
| UniProt | Q88I03 (unreviewed/TrEMBL) | UniProtKB |
| Gene / locus | PP_3199 (GenBank AAN68807) | UniProt/KEGG |
| Organism | *P. putida* KT2440 | UniProt |
| Length | 374 aa | UniProt |
| Genome position | chr 3,628,211–3,629,335 (+ strand) | KEGG ppu:PP_3199 |
| Pfam | **PF01494 (FAD_binding_3)** ×2 | UniProt/KEGG |
| InterPro | IPR002938 (FAD-bd); IPR036188 (FAD/NAD-binding superfamily); IPR050493 (FAD-dep_Monooxygenase_BioMet) | UniProt |
| Fold (Gene3D/SUPFAM) | 3.50.50.60 / SSF51905 — FAD/NAD(P)-binding (Rossmann) domain | UniProt |
| PANTHER | PTHR13789 (MONOOXYGENASE) | UniProt |
| GO (inferred) | FAD binding (GO:0071949); monooxygenase activity (GO:0004497) | InterPro/UniProt-KW |

**Class A single-component flavoprotein aromatic hydroxylase (p-hydroxybenzoate-hydroxylase, PHBH, family).** The sequence carries the three diagnostic conserved fingerprints of this family:

1. **N-terminal Rossmann dinucleotide-binding motif GxGxxG** at residues 11–16 (`GGGIGG`) — binds the ADP moiety of FAD.
2. **Internal "GD/DG" fingerprint** `GADG` at residue 157 — part of the FAD/substrate-binding core.
3. **C-terminal "GD" motif** `GDAAH` at residue 287 — the hallmark motif of PHBH-family aromatic hydroxylases.

These features unambiguously place PP_3199 among the **Group A flavoprotein monooxygenases**, which are self-sufficient (single-polypeptide) enzymes that bind one tightly associated FAD, use NAD(P)H to reduce the flavin, and react the reduced flavin with O₂ to form a **C4a-(hydro)peroxyflavin** that performs electrophilic aromatic hydroxylation of an activated (typically phenolic) substrate, releasing the second O atom as water.

---

## 3. Genomic Context: the `fde` (flavonoid degradation) Cluster

PP_3199 is embedded in a syntenic flavonoid-catabolic gene cluster in KT2440 (KEGG orthology in parentheses):

| Locus | Annotation | KEGG KO / Fde name |
|---|---|---|
| PP_3195 | conserved protein | K26184 — **FdeB** |
| **PP_3196** | **Nodulation protein d1 (LysR_substrate + HTH_1)** | **FdeR-type NodD/LysR regulator** |
| PP_3197 | Glyoxalase-family (VOC-superfamily) protein | K26181 — **FdeC** (ring-cleaving dioxygenase) |
| PP_3198 | **2Fe-2S ferredoxin** | K26179 — **FdeD** |
| **PP_3199** | **putative Monooxygenase** | **FdeE ortholog** (K26180 unassigned in KEGG) |
| PP_3200 | exported protein of unknown function | — |
| PP_3204 | — | K26182 — FdeH |
| PP_3205 | — | K26185 — FdeI |
| PP_3206 | — | K26183 — FdeJ |

The cluster's monooxygenase KO (FdeE, K26180) was not auto-assigned to any KT2440 gene by KEGG, yet PP_3199 is the **only** monooxygenase in the cluster and is the direct sequence ortholog of *Herbaspirillum* FdeE. The presence of the divergently transcribed **NodD-like LysR regulator PP_3196** mirrors the *Herbaspirillum* `fdeR` arrangement, showing the whole flavonoid-responsive regulatory + catabolic module is conserved.

---

## 4. Primary Function: Reaction, Substrate Specificity, and Regioselectivity

### 4.1 Reaction catalyzed
**Naringenin + NAD(P)H + O₂ → 8-hydroxynaringenin (5,7,8-trihydroxyflavanone) + NAD(P)⁺ + H₂O.**

Genetic and metabolite evidence in *H. seropedicae*: a Tn5 insertion in `fdeE` abolished growth on naringenin, and LC-MS/MS showed **naringenin remained unaltered** in the *fdeE* mutant, establishing FdeE as the enzyme performing the **initial step**. In the wild type, naringenin is "first mono-oxygenated by the FdeE protein, to produce 5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one, that is subsequently dioxygenated and cleaved at the A-ring by the FdeC dioxygenase" (Marin et al. 2016, PMID 27059806).

### 4.2 Regioselectivity and substrate range (biochemical)
Purified FdeE was directly characterized as a **flavin-dependent monooxygenase (FMO) that regioselectively introduces a hydroxyl at C-8** and is "active towards a wide range of flavonoids—flavanones, flavones, isoflavones, and flavonols"; it clusters with other **flavonoid-C8-hydroxylase (F8H)** FMOs, and was used preparatively to make 8-hydroxyquercetin (gossypetin) from quercetin (Dulak et al. 2024, PMID 39107441).

**Interpretation:** PP_3199's catalytic chemistry is **aromatic C–H hydroxylation at the C-8 carbon of the flavonoid A-ring**. On naringenin (A-ring = 5,7-dihydroxy resorcinol type), C-8 hydroxylation yields the 7,8-*ortho*-diol (a catechol), the electronic prerequisite for the subsequent **extradiol/meta ring cleavage** by the VOC-superfamily dioxygenase FdeC. Substrate specificity is **broad within the flavonoid scaffold** but scaffold-restricted (a "peripheral" aromatic-catabolism hydroxylase rather than a generalist).

### 4.3 Cofactors / accessory proteins
- **FAD** (bound; PF01494) and **NAD(P)H** (electron donor) are required for Group-A FMO turnover.
- The clustered **2Fe-2S ferredoxin FdeD (PP_3198)** and the flavin/redox partners encoded in the operon may support electron supply/flavin reduction and downstream redox chemistry of the pathway.

---

## 5. Biological Process and Pathway

PP_3199 initiates a **peripheral aromatic-catabolic (funneling) pathway** for plant flavonoids:

```
Naringenin (plant flavanone)
   │  PP_3199 (FdeE, FAD-dependent C-8 monooxygenase)  + O2, NAD(P)H
   ▼
8-Hydroxynaringenin (5,7,8-trihydroxyflavanone; A-ring catechol)
   │  FdeC (PP_3197, VOC/glyoxalase-superfamily dioxygenase)  A-ring meta-cleavage
   ▼
ring-opened intermediates  →  … (FdeB/D/H/I/J) …
   ▼
oxaloacetate  →  TCA cycle (carbon/energy)
```

The downstream steps and final production of oxaloacetate feeding the TCA cycle were defined for the *Herbaspirillum* pathway (Marin et al. 2016, PMID 27059806). Thus PP_3199 enables the bacterium to **use plant-exuded flavonoids as carbon/energy sources** (and/or to detoxify them).

### Regulation
The `fde` operon is a **flavonoid-inducible catabolic operon**. In *H. seropedicae*, transcription is activated by flavonoids (naringenin, chrysin, apigenin, luteolin) via the **NodD-like LysR-type regulator FdeR**, which is divergently transcribed from the operon (Wassem et al. 2017, PMID 27878922); mutating `fdeR` (or the first structural gene `fdeA`) abolishes naringenin degradation (Marin et al. 2013, PMID 23125118). KT2440 conserves this architecture (regulator **PP_3196**, "Nodulation protein d1", LysR family). Consequently PP_3199 is expressed **on demand** when flavonoids are encountered — consistent with a rhizosphere/plant-associated ecological role (flavonoids are major root exudates and rhizobial nod-gene inducers).

---

## 6. Subcellular Localization

**Cytoplasmic.** PP_3199 has no signal peptide and no predicted transmembrane segments, and Group-A flavoprotein hydroxylases (e.g., p-hydroxybenzoate hydroxylase) are classic **soluble cytoplasmic enzymes**. A Kyte–Doolittle scan (window 19) gives a maximum hydropathy of only **1.72** (below the ~1.9 transmembrane threshold), and this single mildly hydrophobic stretch (res 4–22) **coincides exactly with the N-terminal GxGxxG FAD-binding Rossmann motif** — a buried structural element, *not* a membrane anchor or signal peptide. The overall **GRAVY = 0.011** is typical of a soluble globular protein. Flavonoid catabolism therefore proceeds intracellularly after uptake; a clustered putative transporter (PP_3202) and exported protein (PP_3200) may participate in substrate handling.

---

## 7. Evidence Summary

| Claim | Evidence type | Strength |
|---|---|---|
| Class A FAD-dependent aromatic hydroxylase; FAD + NAD(P)H; C4a-peroxyflavin mechanism | Domain architecture (PF01494; IPR002938/036188/050493) + 3 conserved sequence fingerprints (GxGxxG, GADG, GDAAH) | Strong (bioinformatic) |
| Ortholog of characterized FdeE | Needleman-Wunsch global alignment: **41.4 % identity, 379 aligned positions** vs Hsero_1007/D8J0W9; conserved synteny | Strong |
| Catalyzes naringenin → 8-hydroxynaringenin (first, committed step) | Genetics + LC-MS/MS in *H. seropedicae* (PMID 27059806) | Strong (ortholog, experimental) |
| Regioselective **C-8** flavonoid hydroxylase (F8H), broad flavonoid range | In vitro biochemistry of purified FdeE (PMID 39107441) | Strong (ortholog, experimental) |
| Product feeds A-ring dioxygenase FdeC → TCA (oxaloacetate) | Metabolite profiling (PMID 27059806) | Strong (ortholog) |
| Flavonoid-inducible operon via NodD-like LysR FdeR | Genetics/transcription (PMID 27878922, 23125118); KT2440 PP_3196 conserved | Strong (ortholog) + genomic (KT2440) |
| Cytoplasmic localization | Sequence (no signal/TM) + family precedent | Moderate–strong (inference) |

---

## 8. Supported and Refuted Hypotheses

**Supported**
- H1: PP_3199 is a single-component FAD-dependent aromatic (phenolic) hydroxylase of the PHBH/Group-A family. ✔ (domains + motifs)
- H2: Its physiological substrate is a plant flavonoid (naringenin), which it hydroxylates at C-8 as the committed step of flavonoid catabolism. ✔ (orthology + experimental data on FdeE)
- H3: It functions in the cytoplasm within a flavonoid-inducible operon regulated by a NodD-like LysR regulator. ✔ (conserved synteny + regulator PP_3196)

**Refuted / excluded**
- PP_3199 is *not* a two-component (flavin-reductase-dependent) monooxygenase system requirement mis-annotation, nor a generic "unknown monooxygenase": the specific F8H/PHBH-family fingerprints and cluster context define a precise reaction.
- It is *not* a membrane or secreted protein (no signal peptide/TM).

---

## 9. Limitations and Future Directions

- **Direct KT2440 data are lacking:** all enzymatic/genetic characterization comes from the *H. seropedicae* ortholog (41.4 % identity) plus KT2440 genomic context. Direct heterologous expression/kinetics of PP_3199 itself, and a KT2440 `PP_3199` knockout tested for growth on naringenin/flavones/isoflavones/flavonols, would confirm the assignment and quantify substrate preference (Km/kcat) and cofactor (NADH vs NADPH) selectivity.
- **Exact downstream enzymology** (roles of FdeB/D/H/I/J, ring-opened intermediates) remains partly inferred.
- **Regioselectivity in KT2440** (C-8 vs C-6) should be verified by product identification, as some biotransformations yield 6- and 8-hydroxy products.
- A predicted structure exists (AlphaFoldDB Q88I03); docking naringenin into the active site and mapping the FAD/NAD(P)H pockets could pinpoint substrate-determining residues.

---

## 10. Key References
- Marin et al. 2016, *Appl Environ Microbiol* — PMID **27059806** (FdeE monooxygenase catalyzes first step; naringenin → 8-hydroxynaringenin; FdeC A-ring cleavage → oxaloacetate/TCA).
- Dulak et al. 2024 — PMID **39107441** (purified FdeE = regioselective flavonoid **C-8 hydroxylase (F8H)** FMO; broad flavonoid substrate range).
- Wassem et al. 2017 — PMID **27878922** (NodD-like LysR regulator FdeR; flavonoid-inducible `fde` operon).
- Marin et al. 2013 — PMID **23125118** (identification of the `fde` operon; `fdeA`/`fdeR` required for naringenin degradation).
- Supporting database evidence: UniProt Q88I03; KEGG ppu:PP_3199 and neighbors; InterPro IPR002938/IPR050493/IPR036188; Pfam PF01494.


## Artifacts

- [OpenScientist final report](PP_3199-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3199-deep-research-openscientist_artifacts/final_report.pdf)