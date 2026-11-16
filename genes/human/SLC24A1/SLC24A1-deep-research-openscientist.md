---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T05:22:05.244088'
end_time: '2026-11-14T05:35:48.224307'
duration_seconds: 822.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SLC24A1
  gene_symbol: SLC24A1
  uniprot_accession: O60721
  protein_description: 'RecName: Full=Sodium/potassium/calcium exchanger 1; AltName:
    Full=Na(+)/K(+)/Ca(2+)-exchange protein 1 {ECO:0000303|PubMed:9856482}; AltName:
    Full=Retinal rod Na-Ca+K exchanger {ECO:0000303|PubMed:9478004}; AltName: Full=Solute
    carrier family 24 member 1;'
  gene_info: Name=SLC24A1 {ECO:0000303|PubMed:20850105, ECO:0000312|HGNC:HGNC:10975};
    Synonyms=KIAA0702 {ECO:0000303|PubMed:9734811}, NCKX1 {ECO:0000303|PubMed:9856482};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the Ca(2+):cation antiporter (CaCA) (TC 2.A.19)
  protein_domains: K/Na/Ca-exchanger. (IPR004481); NaCa_Exmemb. (IPR004837); NCX_ion-bd_dom_sf.
    (IPR044880); SLC24A1. (IPR004817); Na_Ca_ex (PF01699)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SLC24A1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SLC24A1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O60721
- **Protein Description:** RecName: Full=Sodium/potassium/calcium exchanger 1; AltName: Full=Na(+)/K(+)/Ca(2+)-exchange protein 1 {ECO:0000303|PubMed:9856482}; AltName: Full=Retinal rod Na-Ca+K exchanger {ECO:0000303|PubMed:9478004}; AltName: Full=Solute carrier family 24 member 1;
- **Gene Information:** Name=SLC24A1 {ECO:0000303|PubMed:20850105, ECO:0000312|HGNC:HGNC:10975}; Synonyms=KIAA0702 {ECO:0000303|PubMed:9734811}, NCKX1 {ECO:0000303|PubMed:9856482};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the Ca(2+):cation antiporter (CaCA) (TC 2.A.19)
- **Key Domains:** K/Na/Ca-exchanger. (IPR004481); NaCa_Exmemb. (IPR004837); NCX_ion-bd_dom_sf. (IPR044880); SLC24A1. (IPR004817); Na_Ca_ex (PF01699)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SLC24A1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SLC24A1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SLC24A1** (gene ID: SLC24A1, UniProt: O60721) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: SLC24A1 (NCKX1)

**Gene symbol:** SLC24A1 (synonyms: NCKX1, KIAA0702)
**Protein:** Sodium/potassium/calcium exchanger 1; Na⁺/K⁺/Ca²⁺-exchange protein 1; Retinal rod Na–Ca+K exchanger; Solute carrier family 24 member 1
**UniProt:** O60721 · **Organism:** *Homo sapiens* (human)
**Family:** Ca²⁺:cation antiporter (CaCA) superfamily (TC 2.A.19); SLC24 family; Na_Ca_ex domain (PF01699); InterPro IPR004481, IPR004837, IPR044880, IPR004817

---

## 1. Summary (Answer to the Research Question)

SLC24A1 encodes **NCKX1, a potassium-dependent sodium/calcium exchanger** — a secondary-active plasma-membrane antiporter, not an enzyme. Its primary molecular function is to **extrude Ca²⁺ from the cell**, carrying **one Ca²⁺ and one K⁺ out in exchange for four Na⁺ in**, an electrogenic reaction (coupling ratio 4 Na⁺ : 1 Ca²⁺ + 1 K⁺) powered by both the inward Na⁺ gradient and the outward K⁺ gradient. NCKX1 operates in the **plasma membrane of the rod photoreceptor outer segment**, where it is the **only Ca²⁺-extrusion mechanism** and is physically coupled to the cGMP-gated (CNG) Ca²⁺-influx channel. Functionally it is the Ca²⁺-clearing arm of the **phototransduction negative-feedback loop**: after light closes the CNG channels, continued NCKX1 extrusion lowers outer-segment [Ca²⁺], which (via GCAP/guanylate-cyclase and other Ca²⁺ sensors) accelerates response termination, recovery, and light adaptation. Loss-of-function mutations in SLC24A1 cause **autosomal-recessive congenital stationary night blindness (CSNB, Riggs type)**.

The gene symbol unambiguously matches the UniProt identity: human SLC24A1 / NCKX1, the retinal rod Na–Ca+K exchanger of the SLC24/CaCA family. Literature is fully consistent with the provided annotation; no cross-species or paralog confusion was encountered.

---

## 2. Primary Molecular Function — A K⁺-dependent Na⁺/Ca²⁺ Exchanger

NCKX proteins are the K⁺-dependent branch of cellular Ca²⁺ exchangers: they "utilize both the inward Na⁺ and outward K⁺ gradients to extrude Ca²⁺ from cells" [Schnetkamp 2013, PMID 23506883]. This K⁺-coupling distinguishes the SLC24/NCKX family from the K⁺-independent SLC8/NCX family.

**Transport stoichiometry.** Direct radiotracer flux measurements of heterologously expressed retinal NCKX established a coupling ratio consistent with **4 Na⁺ : 1 Ca²⁺ + 1 K⁺**. Measured Na/Ca coupling ratios were ~4.0 (human 3.98 ± 0.34; chicken 4.11 ± 0.24) and Rb⁺/Ca²⁺ ratios (Rb⁺ as a K⁺ surrogate) were ~1.0 (human 0.92 ± 0.12; chicken 0.98 ± 0.12), so "these results are consistent with a 4Na/1Ca + 1K stoichiometry for retinal cone NCKX" [Szerencsei, Prinsen & Schnetkamp 2001, PMID 11352736]. The same study reported an external Ca²⁺ dissociation constant of ~1–2.5 µM.

**Consequences of the mechanism:**
- **Electrogenic:** four positive charges enter per one Ca²⁺ (2+) plus one K⁺ (1+) leaving → net inward charge movement, producing a measurable exchanger current used to assay NCKX1 in rods.
- **Bidirectional:** NCKX1 normally runs in "forward" mode (Ca²⁺ efflux) but can reverse to carry Ca²⁺ inward when the transmembrane Na⁺ gradient is reversed [Schnetkamp 2004, PMID 14770312].
- **No catalytic chemistry:** NCKX1 is a transporter; there is no bond-making/breaking reaction, only coupled ion translocation.

**Substrate specificity:** transported species are **Ca²⁺ and K⁺ (counter-transported with Na⁺)**. The family is defined by obligatory K⁺ dependence, differentiating it from NCX.

---

## 3. Structure and Molecular Architecture

NCKX1 belongs to the CaCA superfamily and carries the conserved **α-repeat** transmembrane motifs that form the cation-binding/translocation core (Na_Ca_ex / PF01699; InterPro IPR004837, IPR004481; NCX ion-binding domain fold IPR044880). Experimental topology mapping (substituted-cysteine accessibility and inserted N-glycosylation sites on the homologous cone NCKX2) established the arrangement: a **large N-terminal extracellular hydrophilic loop** (a cleaved, heavily glycosylated signal/anchor region), then **two sets of transmembrane segments, each containing five membrane-spanning helices**, separated by a **large cytoplasmic hydrophilic loop**, with the C-terminus facing the extracellular surface [Kinjo et al. 2003, PMID 12600216]. The two α-repeats within these TM sets are oriented antiparallel (α-1 extracellular-facing, α-2 intracellular-facing) [Uehara et al. 2005, PMID 15534861]. Topology and the residues that build the two cation-binding sites have been mapped chiefly on the closely related NCKX2 isoform, and "sequence similarity suggests that the results obtained with the NCKX2 isoform are likely to apply to all NCKX1–5 members" [Shibukawa et al. 2007, PMID 17303823; reviewed in Schnetkamp et al. 2014, PMID 24745986]. Computational/structural analysis of the NCKX2 cation sites has further defined how Na⁺, Ca²⁺ and K⁺ are coordinated [Zhekova et al. 2016, PMID 27805378].

**Transport mechanism — single shared Ca²⁺/K⁺ pocket, alternating access.** NCKX is thought to operate by a **consecutive (ping-pong/alternating-access) mechanism** in which one cation-binding pocket accommodates both Ca²⁺ and K⁺ and alternates between inward- and outward-facing conformations. Charge-conservative mutation of NCKX2 **Glu188 and Asp548** produced the largest shifts in both K⁺ and Ca²⁺ dependence, and size-conservative substitutions abolished function, identifying them as "the central residues of a single cation binding pocket that can accommodate both K⁺ and Ca²⁺… a single set of residues lines a transport pathway for both K⁺ and Ca²⁺" [Kang et al. 2005, PMID 15583008]. A systematic scan of 96 residues in the human cone NCKX2 found that **acidic (Glu/Asp), polar (Ser/Thr) and glycine** residues are most sensitive — 25 reduced activity to <20% of wild-type without disturbing membrane targeting — and these residues are conserved between rod NCKX1 and cone NCKX2 [Winkfein et al. 2003, PMID 12525183]. The two α-repeats are oriented antiparallel (α-1 extracellular-facing, α-2 intracellular-facing) [Uehara et al. 2005, PMID 15534861]. Recent combined structural/MD mapping has further resolved the Na⁺, Ca²⁺ and K⁺ coordination and ion-access pathways of the human NCKX2 exchanger [Zhekova et al. 2016, PMID 27805378; Szerencsei et al. 2025, PMID 40489227]. Because the implicated residues are conserved in NCKX1, this mechanism applies directly to SLC24A1.

**Evolutionary architecture.** Cross-species comparison shows the **transmembrane transport core is highly conserved (>95% identity among dolphin, human and bovine NCKX1)**, while the large extracellular (~50%) and cytosolic (<50%) loops diverge substantially [Cooper et al. 1999, PMID 10320357]. The large cytosolic loop is regulatory rather than catalytic: deleting a 114-aa segment from the functionally "silent" bovine NCKX1 restored K⁺-dependent exchange in HEK293 cells, whereas grafting the bovine loop onto functional dolphin NCKX1 silenced it [PMID 10320357]. This confirms the domain plan: a conserved, purifying-selected TM α-repeat cation-transport core flanked by a modulatory cytosolic loop and a glycosylated extracellular segment.

**Quaternary structure / complex.** In the native rod outer segment, NCKX1 assembles as a **homodimer** and co-assembles with the CNG channel: "in situ, a rod NCKX homodimer and a CNG heterotetramer are thought to be part of a single protein complex" [Kang et al. 2003, PMID 12693957]. Cross-linking and co-immunoprecipitation of heterologously expressed subunits confirmed both NCKX–NCKX homo-oligomerization and NCKX–CNG interaction. This co-localization physically unites the sole Ca²⁺-entry pathway (CNG) and the sole Ca²⁺-exit pathway (NCKX1) in one module.

---

## 4. Subcellular Localization and Site of Action

NCKX1 functions at the **plasma membrane of the rod photoreceptor outer segment (ROS)**. NCKX activity "was first discovered in the outer segments of vertebrate rod photoreceptors (ROS), where it is the only mechanism for extruding the Ca²⁺ that enters ROS via the light-sensitive and cGMP-gated channels" [Schnetkamp 2004, PMID 14770312]. It is the single NCKX family member studied extensively in its native tissue in situ. Immunohistochemistry of human and mouse retina localizes SLC24A1/Slc24a1 to the photoreceptor layer (inner segment, outer and inner nuclear layers, and ganglion cells by antibody staining), with retinal expression appearing around postnatal day 7 in mouse [Riazuddin et al. 2010, PMID 20850105]. The functionally critical pool, however, is in the ROS plasma membrane juxtaposed to the CNG channel.

**Extra-retinal expression.** NCKX1 is the most tissue-restricted NCKX paralog but is not strictly retina-exclusive: **human platelets express NCKX1** [Roberts et al. 2012, PMID 21790537], and human megakaryocytic cells (MEG01) transcribe NCKX1, with K⁺-dependent Na⁺/Ca²⁺ exchange activity that is up-regulated by TGFβ1 [Al-Maghout et al. 2017, PMID 28813704]. In these cells NCKX1 contributes to the Ca²⁺-efflux machinery that terminates cytosolic Ca²⁺ signals, consistent with its generic role as a plasma-membrane Ca²⁺ extruder, though its quantitative importance outside the retina is not well defined [reviewed in Schnetkamp et al. 2014, PMID 24745986].

---

## 5. Biochemical / Signaling Pathway — Phototransduction Ca²⁺ Feedback

NCKX1 is the Ca²⁺-extrusion node of the vertebrate **rod phototransduction cascade**:

1. **Dark state:** elevated cGMP holds CNG channels open; Na⁺ and Ca²⁺ flow in (the "dark current"). Ca²⁺ influx (CNG) and Ca²⁺ efflux (NCKX1) are balanced at a relatively high outer-segment [Ca²⁺].
2. **Light:** activated rhodopsin → transducin → PDE6 hydrolyzes cGMP → CNG channels close → Ca²⁺ influx stops.
3. **NCKX1 action:** with influx halted, continued NCKX1 extrusion rapidly lowers outer-segment [Ca²⁺]. "The extrusion-driven lowering of rod [Ca²⁺]i following light exposure controls their light adaptation and response termination" [Vinberg et al. 2015, PMID 26246500].
4. **Feedback:** the Ca²⁺ drop is read by Ca²⁺-sensor proteins — notably GCAPs, which switch from inhibiting to activating retinal guanylate cyclase to resynthesize cGMP, plus recoverin (rhodopsin kinase regulation) and CNG channel Ca²⁺/calmodulin modulation. This accelerates recovery and adapts sensitivity to background light [Dizhoor 2000, PMID 11152956; Olshevskaya et al. 2002, PMID 11952089]. Developmental increases in NCKX current track the strengthening of this Ca²⁺ feedback in rods [Solessio et al. 2004, PMID 15504902].

Because NCKX1 moves net inward charge (4 Na⁺ in vs 1 Ca²⁺ + 1 K⁺ out), its activity is itself a component of the rod **inward "dark current"**, alongside the CNG channel current, balanced by outward current from the inner segment [Fortenbach et al. 2021, PMID 33502442]. The exchange current is **voltage-dependent**: light-induced hyperpolarization increases the Ca²⁺-extrusion rate, so "the recovery of the dark level of Ca²⁺ … after intense light stimuli results accelerated," and the current is further modulated by Mg-ATP (~2.3-fold) and cAMP (~1.6-fold) [Vedovato & Rispoli 2007, PMID 17415556; Astakhova et al. 2012, PMID 23008435]. This provides a self-reinforcing mechanism that speeds restoration of dark Ca²⁺.

Thus NCKX1 does not itself transduce light; it sets the **kinetics and dynamic range** of the response by controlling the Ca²⁺ signal that drives transduction's negative-feedback loops. Broader SLC24 family roles (olfaction, melanocyte/skin pigmentation, brain memory consolidation) belong to paralogs NCKX2–5 and are not the function of NCKX1 [Schnetkamp 2013, PMID 23506883].

---

## 6. Genetic / Physiological Evidence of Function

- **Human disease (causal genetics):** A recessive frameshift, c.1613_1614del (p.F538CfsX23), in SLC24A1 segregated with night blindness in a large consanguineous family, mapping to chromosome 15q [Riazuddin et al. 2010, PMID 20850105]. Next-generation sequencing confirmed additional nonsense, missense, and compound-heterozygous deletion alleles causing **Riggs-type CSNB** with normal visual acuity, no myopia/nystagmus [Neuillé et al. 2016, PMID 26822852]. The phenotypic spectrum also includes autosomal-recessive retinitis pigmentosa in some SLC24A1 carriers [Millo et al. 2022, PMID 35486108].
- **Animal model (mechanism):** Slc24a1-knockout mice have malformed outer-segment disks, suppressed rod CNG channel expression/function, and ~100-fold reduced rod responses, while cone responses are preserved [Vinberg et al. 2015, PMID 26246500]. The compensating loss of CNG-mediated Ca²⁺ influx limits toxic Ca²⁺ accumulation, explaining the **non-progressive (stationary)** nature of the human disease. Notably, background light adaptation was largely preserved in null rods, implying additional (minor) Ca²⁺-extruding mechanisms exist.

These data provide strong, precise (single-gene, loss-of-function) evidence that NCKX1's Ca²⁺-extrusion activity is required for normal rod phototransduction and scotopic (night) vision.

---

## 7. Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| NCKX1 is a K⁺-dependent Na⁺/Ca²⁺ exchanger extruding Ca²⁺ | **Supported** | Direct flux stoichiometry (PMID 11352736); family definition (PMID 23506883) |
| Transport stoichiometry is 4Na⁺:1Ca²⁺+1K⁺ and electrogenic | **Supported** | PMID 11352736 |
| Site of action = rod outer-segment plasma membrane; sole Ca²⁺ extruder | **Supported** | PMID 14770312; PMID 12693957 |
| NCKX1 shapes phototransduction recovery/adaptation via Ca²⁺ feedback | **Supported** | PMID 26246500; PMID 11952089 |
| Loss of function causes recessive night blindness (CSNB) | **Supported** | PMID 20850105; PMID 26822852; PMID 26246500 |
| NCKX1 is an enzyme catalyzing a chemical reaction | **Refuted** | It is a transporter; no catalytic chemistry |
| NCKX1 mediates olfaction/pigmentation (its primary role) | **Refuted for NCKX1** | Those are paralog (NCKX2–4) roles (PMID 23506883) |

---

## 8. Limitations and Future Directions

- Most detailed **structure–function** data (topology, cation-binding residues) come from the NCKX2 paralog and are inferred to apply to NCKX1 by homology; a high-resolution experimental NCKX1 structure would confirm site architecture.
- Antibody localization in Riazuddin et al. labeled multiple retinal layers; the functionally decisive pool is the ROS plasma membrane, but quantitative distribution across rod compartments is incompletely resolved.
- The identity and magnitude of the **residual Ca²⁺-extrusion mechanism** apparent in Slc24a1-null rods (preserved adaptation) remain unknown.
- Genotype–phenotype breadth (CSNB vs. retinitis pigmentosa) for SLC24A1 variants deserves larger cohorts.

---

## References (PMIDs)

- 11352736 — Szerencsei, Prinsen & Schnetkamp (2001). Stoichiometry of retinal NCKX (4Na:1Ca+1K).
- 23506883 — Schnetkamp (2013). SLC24 Na⁺/Ca²⁺-K⁺ exchanger family review.
- 24745986 — Schnetkamp et al. (2014). SLC24 structure–function review.
- 14770312 — Schnetkamp (2004). SLC24 family: vision and beyond.
- 12693957 — Kang et al. (2003). NCKX homodimer / NCKX–CNG complex assembly.
- 17303823 — Shibukawa et al. (2007). NCKX2 topology and cation transport.
- 12600216 — Kinjo et al. (2003). Experimental NCKX2 membrane topology (5+5 TM, two hydrophilic loops).
- 27805378 — Zhekova et al. (2016). NCKX2 cation-binding sites.
- 15583008 — Kang et al. (2005). Single shared Ca²⁺/K⁺ binding pocket (Glu188/Asp548).
- 12525183 — Winkfein et al. (2003). Scanning mutagenesis of NCKX α-repeats.
- 15534861 — Uehara et al. (2005). Antiparallel α-motif topology; NCKX vs NCX cation sensitivity.
- 10320357 — Cooper et al. (1999). Dolphin NCKX1 cloning; TM conservation; cytosolic-loop regulation.
- 40489227 — Szerencsei et al. (2025). Structural/functional mapping of ion access pathways in human NCKX2.
- 33502442 — Fortenbach et al. (2021). NCKX transporters contribute to the rod dark current (Kv2.1 study).
- 17415556 — Vedovato & Rispoli (2007). Voltage/Mg-ATP modulation of the rod Na:Ca,K exchange current.
- 23008435 — Astakhova et al. (2012). cAMP increases rod Ca²⁺ exchanger current ~1.6-fold.
- 21790537 — Roberts et al. (2012). Human platelet Na⁺/Ca²⁺ exchangers; platelets express NCKX1.
- 28813704 — Al-Maghout et al. (2017). TGFβ1 up-regulates NCKX1 in megakaryocytes.
- 26246500 — Vinberg et al. (2015). Slc24a1 mouse model of stationary night blindness.
- 20850105 — Riazuddin et al. (2010). SLC24A1 mutation in autosomal-recessive CSNB.
- 26822852 — Neuillé et al. (2016). NGS confirmation of SLC24A1 in CSNB.
- 35486108 — Millo et al. (2022). SLC24A1 phenotypic spectrum (incl. ARRP).
- 11152956 — Dizhoor (2000). cGMP synthesis regulation / Ca²⁺ feedback.
- 11952089 — Olshevskaya et al. (2002). Ca²⁺ feedback on guanylate cyclase.
- 15504902 — Solessio et al. (2004). Developmental Ca²⁺ feedback and NCKX current.
- 18690016 — Altimimi & Schnetkamp (2007). NCKX functional properties & physiological roles.


## Artifacts

- [OpenScientist final report](SLC24A1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SLC24A1-deep-research-openscientist_artifacts/final_report.pdf)