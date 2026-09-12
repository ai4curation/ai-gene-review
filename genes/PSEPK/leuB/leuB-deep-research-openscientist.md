---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T13:12:01.948716'
end_time: '2026-07-17T13:43:00.714385'
duration_seconds: 1858.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: leuB
  gene_symbol: leuB
  uniprot_accession: Q88LE5
  protein_description: 'RecName: Full=3-isopropylmalate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01033};
    EC=1.1.1.85 {ECO:0000255|HAMAP-Rule:MF_01033}; AltName: Full=3-IPM-DH {ECO:0000255|HAMAP-Rule:MF_01033};
    AltName: Full=Beta-IPM dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01033}; Short=IMDH
    {ECO:0000255|HAMAP-Rule:MF_01033};'
  gene_info: Name=leuB {ECO:0000255|HAMAP-Rule:MF_01033}; OrderedLocusNames=PP_1988;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the isocitrate and isopropylmalate
  protein_domains: IsoCit/isopropylmalate_DH_CS. (IPR019818); IsoPropMal-DH-like_dom.
    (IPR024084); Isopropylmalate_DH. (IPR004429); Iso_dh (PF00180)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: leuB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: leuB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LE5
- **Protein Description:** RecName: Full=3-isopropylmalate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01033}; EC=1.1.1.85 {ECO:0000255|HAMAP-Rule:MF_01033}; AltName: Full=3-IPM-DH {ECO:0000255|HAMAP-Rule:MF_01033}; AltName: Full=Beta-IPM dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01033}; Short=IMDH {ECO:0000255|HAMAP-Rule:MF_01033};
- **Gene Information:** Name=leuB {ECO:0000255|HAMAP-Rule:MF_01033}; OrderedLocusNames=PP_1988;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the isocitrate and isopropylmalate
- **Key Domains:** IsoCit/isopropylmalate_DH_CS. (IPR019818); IsoPropMal-DH-like_dom. (IPR024084); Isopropylmalate_DH. (IPR004429); Iso_dh (PF00180)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "leuB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'leuB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **leuB** (gene ID: leuB, UniProt: Q88LE5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *leuB* (3-Isopropylmalate Dehydrogenase) in *Pseudomonas putida* KT2440

**Gene:** *leuB* | **Ordered Locus:** PP_1988 | **UniProt:** Q88LE5 (LEU3_PSEPK)
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**Enzyme:** 3-Isopropylmalate dehydrogenase (3-IPM-DH; β-IPM dehydrogenase; IMDH) | **EC 1.1.1.85**

---

## Summary

The gene *leuB* (locus PP_1988; UniProt Q88LE5) of *Pseudomonas putida* KT2440 encodes **3-isopropylmalate dehydrogenase (3-IPMDH, EC 1.1.1.85)**, a soluble cytoplasmic enzyme that catalyzes the **third step of the L-leucine biosynthetic pathway**. The enzyme performs the **NAD⁺-dependent oxidative decarboxylation of (2R,3S)-3-isopropylmalate (3-IPM) to 2-ketoisocaproate (2-oxo-4-methylpentanoate)**, releasing CO₂ and generating NADH. The 2-ketoisocaproate product is subsequently transaminated by a branched-chain aminotransferase to yield L-leucine. This assignment is anchored by the UniProt/HAMAP annotation (HAMAP-Rule MF_01033) and is strongly corroborated by direct sequence-motif analysis of Q88LE5 together with an extensive body of biochemical and structural literature on orthologous IPMDH enzymes from bacteria, archaea, and plants.

Mechanistically, LeuB belongs to the **β-decarboxylating dehydrogenase family** (which also includes isocitrate dehydrogenase and homoisocitrate dehydrogenase). The functional unit is a **homodimer**, and catalysis requires a **divalent metal ion (Mg²⁺ or Mn²⁺)** plus a **monovalent cation (K⁺)**. The reaction proceeds by metal-assisted deprotonation of the substrate hydroxyl by a conserved active-site **lysine acting as the general base**, followed by **hydride transfer from the substrate C2 atom to the C4N atom of the NAD⁺ nicotinamide ring**, and finally β-decarboxylation. Substrate specificity for the isopropyl moiety of 3-IPM is set by a small **hydrophobic active-site pocket**; only a few residues distinguish IPMDH from its isocitrate/homoisocitrate-processing relatives. The strong NAD⁺ (over NADP⁺) preference is an evolutionarily conserved and adaptively constrained feature of the enzyme family.

Importantly, **no *P. putida* KT2440-specific primary study of LeuB exists**; the functional annotation rests on (i) direct verification of the Q88LE5 sequence, which carries all family-diagnostic catalytic and metal-binding motifs intact, and (ii) inference from highly conserved, experimentally characterized orthologs. Because the catalytic and kinetic properties of IPMDH are remarkably conserved across species, this cross-species inference is robust. Within the pathway, LeuB is *not* the committed regulatory step — flux control resides upstream with LeuA (2-isopropylmalate synthase, subject to L-leucine feedback inhibition) and with transcriptional regulation of the *leuBCD* genes; LeuB itself displays product (NADH) inhibition. Because leucine biosynthesis is absent in humans but essential in many bacteria, IPMDH is an established target for antibacterial drug development.

---

## Gene/Protein Identity — Verified

The gene symbol, organism, EC number, family, and domain architecture are internally consistent, and all retrieved literature concerns the same enzyme (LeuB / 3-isopropylmalate dehydrogenase). The UniProt sequence was retrieved directly and confirmed to carry every catalytic residue conserved in enzymatically characterized orthologs (see Finding 4). **There is no evidence of gene-symbol ambiguity for this protein.**

| Attribute | Value |
|---|---|
| UniProt | Q88LE5 (LEU3_PSEPK) |
| Gene | *leuB* (ordered locus PP_1988) |
| Organism | *Pseudomonas putida* strain KT2440 |
| Enzyme | 3-Isopropylmalate dehydrogenase; 3-IPM-DH; β-IPM dehydrogenase; IMDH |
| EC | 1.1.1.85 |
| Length | 360 aa |
| Family | β-decarboxylating dehydrogenase family; Pfam PF00180 (Iso_dh); InterPro IPR004429, IPR019818, IPR024084 |

---

## Key Findings

### Finding 1 — LeuB catalyzes the NAD⁺-dependent oxidative decarboxylation of 3-isopropylmalate to 2-ketoisocaproate (F001)

The core functional assignment for Q88LE5 is 3-isopropylmalate dehydrogenase (EC 1.1.1.85), the third enzyme of leucine biosynthesis. The reaction catalyzed is:

> **(2R,3S)-3-isopropylmalate + NAD⁺ → 2-oxo-4-methylpentanoate (2-ketoisocaproate) + CO₂ + NADH**

This is an irreversible oxidative decarboxylation. Miggiano et al. (2020) explicitly state that "3-isopropylmalate dehydrogenases (LeuB) belong to the leucine biosynthetic pathway and catalyze the irreversible oxidative decarboxylation of 3IPM to 2-ketoisocaproate that is finally converted into leucine by a branched-chain aminotransferase" [PMID: 32059844](https://pubmed.ncbi.nlm.nih.gov/32059844/). The position of the enzyme as the third step in the pathway is independently confirmed by Martignon et al. (2007), who describe "3-isopropylmalate dehydrogenase (3IPMDH)" as "the third enzyme in leucine biosynthesis" [PMID: 17979826](https://pubmed.ncbi.nlm.nih.gov/17979826/). The UniProt annotation of Q88LE5 (EC 1.1.1.85, leuB, PP_1988, governed by HAMAP-Rule MF_01033) is fully consistent with this reaction, which has been confirmed biochemically and structurally across multiple orthologs.

### Finding 2 — Catalytic mechanism: metal- and K⁺-assisted hydride transfer with a lysine general base (F002)

The catalytic mechanism of IPMDH has been dissected in atomic detail in orthologs, and it applies directly to LeuB by virtue of conserved active-site architecture. Catalysis requires a **divalent metal ion (Mg²⁺ or Mn²⁺)** that coordinates the substrate, and a **monovalent cation (K⁺)** that activates the hydride-transfer step. The chemistry centers on the "transfer of a hydride from the C2 atom of 3-isopropylmalate to the C4N atom of the pyridine ring of NAD" [PMID: 25211160](https://pubmed.ncbi.nlm.nih.gov/25211160/). A high-resolution (2.0 Å) *Thermus thermophilus* IPMDH structure with Mn²⁺, 3-isopropylmalate, and NADH positions the substrate C2 roughly 3.0 Å from the NAD⁺ C4N atom, and QM/MM calculations give a hydride-transfer activation energy of ~15 kcal/mol, raised by 4–6 kcal/mol in the absence of K⁺ (Palló et al. 2014).

Site-directed mutagenesis pinpoints the essential catalytic residues. Gráczer et al. (2016) showed by alanine-scanning that K185A and D241A reduce kcat to ~0.06% of wild type, and concluded that "K185 and D241 may constitute a proton relay system that can assist in the abstraction of a proton from the OH group of IPM during catalysis" [PMID: 26731489](https://pubmed.ncbi.nlm.nih.gov/26731489/) — establishing the lysine as the catalytic base and the aspartate as an assisting residue. The role of the monovalent cation was defined by studies of Glu270: "E270 seems to position K(+) into close proximity of the nicotinamide ring of NAD(+) and the electron-withdrawing effect of K(+) may help to polarise the aromatic ring in order to aid the hydride-transfer" [PMID: 25497013](https://pubmed.ncbi.nlm.nih.gov/25497013/). In the plant ortholog, Arabidopsis IPMDH2 structures show that Lys-232 activates a catalytic water molecule (Lee et al. 2016, [PMID: 27137927](https://pubmed.ncbi.nlm.nih.gov/27137927/)), reinforcing the general lysine-based mechanism across the family.

### Finding 3 — Homodimeric β-decarboxylating dehydrogenase with a hydrophobic substrate pocket (F003)

LeuB is a member of the **β-decarboxylating dehydrogenase family**, which also contains isocitrate dehydrogenase and homoisocitrate dehydrogenase; these enzymes diverged from a broad-specificity common ancestor (Shimizu et al. 2017; Chen & Jeong 2000). The functional unit is a **homodimer**; in *T. thermophilus* the dimer is markedly more thermostable than the isolated monomer (Sharma et al. 2020, [PMID: 31986322](https://pubmed.ncbi.nlm.nih.gov/31986322/)).

Substrate specificity for 3-isopropylmalate is set by a small **hydrophobic active-site pocket**. Work on the ancestral-type enzyme TK0280 from *Thermococcus kodakarensis* demonstrated that "the hydrophobic region consisting of Ile82 and Leu83 was responsible for the recognition of 3-isopropylmalate" [PMID: 27831491](https://pubmed.ncbi.nlm.nih.gov/27831491/), whereas polar residues (Thr71/Ser80) confer recognition of isocitrate/homoisocitrate. This illustrates a key principle for confident functional inference: "substitutions of only a few amino acid residues in these enzymes are sufficient to exchange substrate and coenzyme specificities" [PMID: 11206056](https://pubmed.ncbi.nlm.nih.gov/11206056/). Additionally, LeuB is subject to **product inhibition by NADH**; Martignon et al. (2007) noted that "the observed enzyme inhibition by the reaction product NADH could represent a regulatory mechanism for 3IPMDH" [PMID: 17979826](https://pubmed.ncbi.nlm.nih.gov/17979826/).

### Finding 4 — The Q88LE5 sequence carries intact IPMDH catalytic/metal-binding motifs and lacks any secretion/membrane signal (F004)

Direct analysis of the 360-residue Q88LE5 sequence — a typical length for a bacterial IPMDH — confirms that all family-diagnostic motifs are present and intact:

| Motif / region | Sequence feature | Functional role | *T. thermophilus* homolog |
|---|---|---|---|
| N-terminal glycine-rich loop | G10-DGIG | substrate / metal region | — |
| Catalytic-lysine segment | C-S-V-D-**K**-A-N (Lys195) | general base | Lys185 |
| Metal-coordinating acidic cluster | G-D-I-L-S-**D**-E (Asp248/Asp252) | divalent metal binding | Asp241 / Asp245 |
| Cofactor-binding segment | CHGSAPD | NAD⁺ binding | — |

These features match InterPro signatures **IPR004429** (Isopropylmalate_DH), **IPR019818** (IsoCit/isopropylmalate_DH conserved site), and Pfam **PF00180** (Iso_dh). The conservation of the K185/D241 proton-relay pair — corresponding to Q88LE5's DKAN Lys195 and GDILSDE Asp cluster — directly supports catalytic competence, given that "K185 and D241 may constitute a proton relay system" in the characterized ortholog [PMID: 26731489](https://pubmed.ncbi.nlm.nih.gov/26731489/). The use of conserved specificity determinants as reliable orthology markers is justified because "the few major specificity determinants can serve as reliable markers for determining orthologous or paralogous relationships" [PMID: 11206056](https://pubmed.ncbi.nlm.nih.gov/11206056/).

Regarding **subcellular localization**, UniProt Q88LE5 annotates **no signal peptide and no transmembrane segment**, consistent with a **soluble cytosolic (cytoplasmic) enzyme** — the expected location for a central amino-acid biosynthetic enzyme, whose substrate 3-isopropylmalate is generated cytoplasmically by the upstream LeuCD isopropylmalate isomerase.

### Finding 5 — Pathway regulation: LeuB is not the committed control point (F005)

Within L-leucine biosynthesis, the **committed and rate-controlling step is the first enzyme, 2-isopropylmalate synthase (LeuA)**, which is allosterically feedback-inhibited by L-leucine. In *Corynebacterium glutamicum*, "the leuA-encoded 2-isopropylmalate synthase (IPMS) is inhibited by low L-leucine concentrations with a K(i) of 0.4 mM" [PMID: 24333966](https://pubmed.ncbi.nlm.nih.gov/24333966/). LeuB, by contrast, catalyzes an intermediate step and is not the primary flux-control node. Pathway output is additionally governed at the transcriptional level: leucine overproduction in *C. glutamicum* required "deletion of the gene encoding the repressor LtbR to increase expression of leuBCD" [PMID: 24333966](https://pubmed.ncbi.nlm.nih.gov/24333966/), demonstrating that *leuB* is co-regulated with *leuC* and *leuD* under repressor control. The only intrinsic regulatory feature attributed to LeuB itself is **NADH product inhibition** [PMID: 17979826](https://pubmed.ncbi.nlm.nih.gov/17979826/).

### Finding 6 — LeuB/IPMDH is an established antibacterial drug target with conserved kinetics (F006)

Because leucine biosynthesis is absent in humans but required by many bacterial pathogens, LeuB is regarded as a target for broad-spectrum antibacterials: "the enzymes belonging to this pathway can be considered as potential target sites for designing of a new class of antibacterial agents" [PMID: 32059844](https://pubmed.ncbi.nlm.nih.gov/32059844/). Characterized transition-state-analog inhibitors include **O-isobutenyl oxalylhydroxamate** (co-crystallized with *Haemophilus influenzae* LeuB), **O-methyl oxalohydroxamate**, and **3-methylmercaptomalate**. Crucially, the potency of these inhibitors and the enzyme's kinetics are strongly conserved across species; Gráczer et al. (2014) concluded that "experiments with either Ec or Tt IPMDH would be equally relevant for designing specific inhibitory drugs against Mtb IPMDH" [PMID: 24909230](https://pubmed.ncbi.nlm.nih.gov/24909230/). Notably, even where quaternary structure differs (*M. tuberculosis* IPMDH is tetrameric rather than the usual dimer), the kcat, Km, and pH-dependence remain very similar to the *E. coli* and *T. thermophilus* enzymes. This deep conservation is precisely what makes cross-species functional inference to *P. putida* LeuB reliable.

### Finding 7 — NAD⁺ specificity is evolutionarily conserved and adaptively constrained (F007)

IPMDH is physiologically **NAD⁺-specific**, not NADP⁺-dependent, and this specificity is a conserved and adaptively constrained feature. Miller, Lunzer & Dean (2006) demonstrated that although directed evolution can switch coenzyme specificity toward NADP⁺, such mutants invariably have lower NADP affinity, and concluded that "high intracellular NADPH abundance and the cost of compensatory protein synthesis, have ensured the conserved use of NAD by IMDH throughout evolution" [PMID: 17053145](https://pubmed.ncbi.nlm.nih.gov/17053145/). Coenzyme and substrate specificities are conserved even across large phylogenetic distances: in a thermoacidophilic archaeon, "the substrate and coenzyme specificities of the archaeal enzyme resembled those of the bacterial counterparts" [PMID: 9023199](https://pubmed.ncbi.nlm.nih.gov/9023199/). Kinetically, *E. coli* IPMDH catalysis is gated by a **hinge-bending domain closure** that occurs upon IPM binding (Hajdú et al. 2009, [PMID: 19527660](https://pubmed.ncbi.nlm.nih.gov/19527660/)), a conformational feature common to the family. Physiologically, using the oxidized NAD⁺ pool rather than the biosynthetic NADPH pool is consistent with a cytoplasmic anabolic dehydrogenase.

### Finding 8 — No *P. putida*-specific primary study exists; annotation rests on sequence verification plus conserved orthologs (F008)

Targeted literature searches for *P. putida* KT2440-specific characterization of LeuB/IPMDH — including leucine auxotrophy, gene essentiality/fitness, and *leuABCD* operon organization — returned **no primary papers on the *P. putida* enzyme itself**. The functional assignment is therefore based on two complementary pillars: (i) **direct retrieval and motif analysis of the Q88LE5 sequence**, confirming intact catalytic Lys195, metal-binding Asp248/Asp252, and cofactor-binding CHGSAPD (Pfam PF00180); and (ii) **experimentally and structurally characterized orthologs** whose active-site chemistry and NAD⁺/substrate specificity are strongly conserved and evolutionarily constrained ([PMID: 25211160](https://pubmed.ncbi.nlm.nih.gov/25211160/), [PMID: 26731489](https://pubmed.ncbi.nlm.nih.gov/26731489/), [PMID: 27831491](https://pubmed.ncbi.nlm.nih.gov/27831491/), [PMID: 17053145](https://pubmed.ncbi.nlm.nih.gov/17053145/), [PMID: 9023199](https://pubmed.ncbi.nlm.nih.gov/9023199/), [PMID: 24909230](https://pubmed.ncbi.nlm.nih.gov/24909230/)). Given the exceptional conservation of IPMDH properties documented across bacteria, archaea, and plants, this homology-based annotation is considered reliable.

---

## Mechanistic Model / Interpretation

### Position of LeuB in L-leucine biosynthesis

```
  2-Ketoisovalerate (branch point from valine pathway)
                    │
                    ▼
        ┌────────────────────────────┐
   [1]  │ LeuA: 2-isopropylmalate     │  ◄── COMMITTED STEP
        │ synthase                    │      Feedback-inhibited by L-leucine
        └────────────────────────────┘      (Ki ≈ 0.4 mM in C. glutamicum)
                    │  2-isopropylmalate
                    ▼
        ┌────────────────────────────┐
   [2]  │ LeuC/LeuD: isopropylmalate  │  (isomerization)
        │ isomerase                   │
        └────────────────────────────┘
                    │  (2R,3S)-3-isopropylmalate
                    ▼
        ┌════════════════════════════┐
   [3]  ║ LeuB (PP_1988, Q88LE5):     ║  ◄── THIS ENZYME
        ║ 3-isopropylmalate           ║      NAD⁺, Mg²⁺/Mn²⁺, K⁺
        ║ dehydrogenase (EC 1.1.1.85) ║      Product-inhibited by NADH
        └════════════════════════════┘
                    │  2-ketoisocaproate + CO₂ + NADH
                    ▼
        ┌────────────────────────────┐
   [4]  │ Branched-chain             │  (transamination)
        │ aminotransferase (IlvE)    │
        └────────────────────────────┘
                    │
                    ▼
                L-LEUCINE
```

### Catalytic cycle at the LeuB active site

The reaction is a classic β-decarboxylating dehydrogenase two-part chemistry — oxidation followed by decarboxylation — organized around the divalent metal and coordinated by conserved residues:

```
   Step A (Oxidation / hydride transfer):
     Substrate C2–OH  ──[Lys195 abstracts proton; D248/252 assists]──►  C2=O (keto)
     Substrate C2–H   ──[hydride transferred to NAD⁺ C4N]──►  NADH
                        (K⁺ polarizes nicotinamide ring; activation ~15 kcal/mol)

   Step B (β-Decarboxylation):
     β-keto acid intermediate  ──►  enol  ──►  2-ketoisocaproate + CO₂
                        (Mg²⁺/Mn²⁺ stabilizes the enolate intermediate)

   Conformational gating:
     IPM binding triggers hinge-bending domain closure that assembles
     the catalytically competent active site.
```

### Structure–function summary

| Property | Assignment | Basis |
|---|---|---|
| Reaction | (2R,3S)-3-IPM + NAD⁺ → 2-ketoisocaproate + CO₂ + NADH | UniProt/HAMAP; PMID 32059844 |
| EC number | 1.1.1.85 | UniProt Q88LE5 |
| Coenzyme | NAD⁺ (not NADP⁺) | PMID 17053145, 9023199 |
| Cofactors | Mg²⁺ or Mn²⁺ (divalent) + K⁺ (monovalent) | PMID 25211160, 25497013 |
| Catalytic base | Lysine (Lys195 in Q88LE5; Lys185 in Tt) | PMID 26731489 |
| Substrate recognition | Hydrophobic pocket (isopropyl group) | PMID 27831491 |
| Quaternary structure | Homodimer (functional unit) | PMID 31986322 |
| Localization | Soluble cytoplasm (no signal/TM) | UniProt Q88LE5 |
| Regulation of enzyme | NADH product inhibition | PMID 17979826 |
| Regulation of pathway | Upstream at LeuA + transcriptional (leuBCD) | PMID 24333966 |
| Family | β-decarboxylating dehydrogenase | PMID 27831491, 11206056 |

---

## Evidence Base

| PMID | Study (abbreviated) | How it supports the annotation |
|---|---|---|
| [32059844](https://pubmed.ncbi.nlm.nih.gov/32059844/) | Crystal structure of *H. influenzae* LeuB with inhibitor | Defines the reaction (irreversible oxidative decarboxylation of 3-IPM → 2-ketoisocaproate), pathway position, and drug-target status |
| [17979826](https://pubmed.ncbi.nlm.nih.gov/17979826/) | Expression/characterisation of *H. influenzae* LeuB | Confirms LeuB as the third enzyme of leucine biosynthesis; documents NADH product inhibition |
| [25211160](https://pubmed.ncbi.nlm.nih.gov/25211160/) | Structural and energetic basis of IPMDH catalysis | Defines the hydride-transfer chemistry (C2 → C4N of NAD) with metal and K⁺ |
| [26731489](https://pubmed.ncbi.nlm.nih.gov/26731489/) | Dual role of active-site residues of Tt IPMDH | Identifies catalytic Lys185/Asp241 proton relay (homologous to Q88LE5 Lys195/Asp cluster) |
| [25497013](https://pubmed.ncbi.nlm.nih.gov/25497013/) | Glu270 in K⁺-activation and domain closure | Documents monovalent K⁺ activation of hydride transfer |
| [27137927](https://pubmed.ncbi.nlm.nih.gov/27137927/) | Structure/mechanism of *Arabidopsis* IPMDH2 | Lys-232 catalytic role; common mechanism across leucine/glucosinolate IPMDH enzymes |
| [27831491](https://pubmed.ncbi.nlm.nih.gov/27831491/) | Ancestral β-decarboxylating dehydrogenase (TK0280) | Hydrophobic Ile82/Leu83 pocket recognizes the isopropyl group; substrate specificity determinants |
| [11206056](https://pubmed.ncbi.nlm.nih.gov/11206056/) | Functional prediction: orthologs and paralogs | Establishes that few residues determine specificity and serve as reliable orthology markers |
| [17053145](https://pubmed.ncbi.nlm.nih.gov/17053145/) | Direct demonstration of an adaptive constraint | Evolutionary/enzymological evidence for conserved NAD⁺ (not NADP⁺) use |
| [9023199](https://pubmed.ncbi.nlm.nih.gov/9023199/) | IPMDH of thermoacidophilic archaeon *Sulfolobus* | Substrate and NAD⁺ specificity conserved across bacteria and archaea |
| [24909230](https://pubmed.ncbi.nlm.nih.gov/24909230/) | Drugs against Mtb IPMDH using surrogate enzymes | Strong conservation of kinetics across species justifies cross-species inference |
| [24333966](https://pubmed.ncbi.nlm.nih.gov/24333966/) | Metabolic engineering of *C. glutamicum* for L-leucine | Defines pathway regulation: LeuA feedback + transcriptional control of leuBCD |
| [31986322](https://pubmed.ncbi.nlm.nih.gov/31986322/) | Dimeric vs monomeric Tt IPMDH thermal stability | Confirms homodimer as the functional, stable unit |
| [19527660](https://pubmed.ncbi.nlm.nih.gov/19527660/) | Hinge-bending domain motions in *E. coli* IPMDH | Conformational gating of catalysis by IPM-induced domain closure |

Together, these papers form a coherent and mutually consistent picture. There are **no contradictory findings** in the literature reviewed; the sources agree on the reaction, coenzyme, cofactor requirements, catalytic residues, quaternary structure, and pathway role. The primary caveat is that all direct experimental evidence comes from **orthologs**, not the *P. putida* enzyme itself.

---

## Supported vs. Refuted Hypotheses

- **Supported:** *leuB* encodes a catalytically competent 3-IPMDH (all catalytic residues intact); reaction = oxidative decarboxylation of 3-IPM → 2-KIC; NAD⁺/divalent-metal/K⁺ dependence; homodimer; cytoplasmic localization; NADH product inhibition; role as the third step of leucine biosynthesis.
- **No hypotheses refuted** — this is a canonical, highly conserved enzyme, and every line of evidence (biochemical, structural, evolutionary, bioinformatic) converges on the same function.

---

## Limitations and Knowledge Gaps

1. **No organism-specific experimental data.** No primary study has characterized *P. putida* KT2440 LeuB (Q88LE5) directly — no purified-enzyme kinetics, no crystal structure, no knockout/auxotrophy phenotype. All functional claims are inferences from conserved orthologs plus sequence-motif analysis of Q88LE5.

2. **Residue numbering is inferred.** The specific catalytic residue positions cited for Q88LE5 (Lys195, Asp248/Asp252) are assigned by homology/alignment to characterized enzymes (e.g., *T. thermophilus* Lys185/Asp241) rather than confirmed by mutagenesis in *P. putida*.

3. **Localization is predictive.** The cytoplasmic assignment is based on the absence of a signal peptide or transmembrane region in the sequence, not on experimental fractionation of *P. putida*.

4. **Operon structure unverified in *P. putida*.** Although *leuB* co-regulation with *leuCD* is established in other bacteria, the exact *leu* gene arrangement and transcriptional regulators in *P. putida* KT2440 were not confirmed from primary literature.

5. **Quaternary structure assumed.** The homodimer assignment derives from orthologs; note that some IPMDHs (e.g., *M. tuberculosis*) are tetrameric, so the oligomeric state of the *P. putida* enzyme should not be taken as definitively dimeric without confirmation.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_1988, express and purify the enzyme, and determine kcat, Km(3-IPM), Km(NAD⁺), and metal/K⁺ dependence to confirm predicted activity and specificity directly for the *P. putida* enzyme.

2. **Coenzyme specificity assay.** Compare activity with NAD⁺ vs NADP⁺ to experimentally confirm the predicted strict NAD⁺ preference.

3. **Structural determination.** Solve a crystal or cryo-EM structure (ideally with 3-IPM + Mg²⁺/Mn²⁺ + NAD(H)) to verify active-site geometry, the Lys195/Asp proton relay, and the quaternary state (dimer vs tetramer).

4. **Genetic knockout / auxotrophy test.** Delete PP_1988 and test for leucine auxotrophy (growth rescue by exogenous L-leucine) to confirm the essential biosynthetic role in vivo.

5. **Product-inhibition characterization.** Measure NADH inhibition constants for the *P. putida* enzyme to confirm the predicted regulatory feature.

6. **Operon and regulation mapping.** Use RNA-seq / transcript mapping to define the *leu* operon structure and identify transcriptional regulators controlling *leuB* expression in *P. putida* KT2440.

7. **Inhibitor testing.** Evaluate known IPMDH transition-state analogs (e.g., O-isobutenyl oxalylhydroxamate) against the *P. putida* enzyme to assess conservation of inhibitor binding and its relevance for antibacterial development.

---

*Report compiled from 8 confirmed findings and 24 reviewed papers over 5 investigation iterations. All functional claims are supported either by direct analysis of the Q88LE5 sequence or by experimentally characterized orthologous enzymes, as cited above.*


## Artifacts

- [OpenScientist final report](leuB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](leuB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32059844
2. PMID:17979826
3. PMID:25211160
4. PMID:26731489
5. PMID:25497013
6. PMID:27137927
7. PMID:31986322
8. PMID:27831491
9. PMID:11206056
10. PMID:24333966
11. PMID:24909230
12. PMID:17053145
13. PMID:9023199
14. PMID:19527660