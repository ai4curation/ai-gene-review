---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-02T19:42:23.210396'
end_time: '2026-11-02T19:53:10.729328'
duration_seconds: 647.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: RHIME
  gene_id: betC
  gene_symbol: betC
  uniprot_accession: O69787
  protein_description: 'RecName: Full=Choline-sulfatase; EC=3.1.6.6;'
  gene_info: Name=betC; OrderedLocusNames=R00949; ORFNames=SMc00127;
  organism_full: Rhizobium meliloti (strain 1021) (Ensifer meliloti) (Sinorhizobium
    meliloti).
  protein_family: Belongs to the sulfatase family. .
  protein_domains: Alkaline_phosphatase_core_sf. (IPR017850); Choline-sulfatase. (IPR017785);
    Choline_sulf_C_dom. (IPR025863); Sulfatase_CS. (IPR024607); Sulfatase_N. (IPR000917)
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
  path: betC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: betC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O69787
- **Protein Description:** RecName: Full=Choline-sulfatase; EC=3.1.6.6;
- **Gene Information:** Name=betC; OrderedLocusNames=R00949; ORFNames=SMc00127;
- **Organism (full):** Rhizobium meliloti (strain 1021) (Ensifer meliloti) (Sinorhizobium meliloti).
- **Protein Family:** Belongs to the sulfatase family. .
- **Key Domains:** Alkaline_phosphatase_core_sf. (IPR017850); Choline-sulfatase. (IPR017785); Choline_sulf_C_dom. (IPR025863); Sulfatase_CS. (IPR024607); Sulfatase_N. (IPR000917)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "betC" matches the protein description above**
2. **Verify the organism is correct:** Rhizobium meliloti (strain 1021) (Ensifer meliloti) (Sinorhizobium meliloti).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'betC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **betC** (gene ID: betC, UniProt: O69787) in RHIME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *betC* (Choline-O-sulfatase, O69787) in *Sinorhizobium meliloti* 1021

## Gene/Protein Identity (verified)

- **UniProt:** O69787 — Choline-sulfatase, **EC 3.1.6.6**
- **Gene:** *betC* (ordered locus **R00949**; ORF **SMc00127**)
- **Organism:** *Rhizobium meliloti* strain 1021 (*Ensifer / Sinorhizobium meliloti*)
- **Family:** Sulfatase (formylglycine-dependent) family; domains: Sulfatase_N (IPR000917), Sulfatase_CS (IPR024607), Choline-sulfatase (IPR017785), Choline_sulf_C_dom (IPR025863), Alkaline-phosphatase-core superfamily (IPR017850)

**Identity confirmation:** The gene symbol *betC*, the organism, the EC number (3.1.6.6), and the sulfatase family/domain architecture are mutually consistent and are directly supported by primary literature on the *S. meliloti* *betICBA* operon (Osterås et al. 1998, PMID 9736747; Mandon et al. 2003, PMID 12906115). This is the correct target; literature matches precisely. (Note: a *betC* with the same name and function exists in *Pseudomonas putida* and *Bacillus subtilis*; these are genuine orthologs/analogs, not mis-identifications — see "Comparative context.")

---

## 1. Summary (answer to the research question)

**BetC is a choline-O-sulfatase (EC 3.1.6.6), a cytoplasmic, formylglycine-dependent sulfatase that hydrolyzes the sulfate-ester bond of choline-O-sulfate to yield free choline plus inorganic sulfate** (it also acts, more slowly, on phosphorylcholine). It is the first (entry) enzyme of the *betICBA* pathway in *S. meliloti*: the choline it releases is oxidized by choline dehydrogenase (BetA) and betaine-aldehyde dehydrogenase (BetB) to the osmoprotectant **glycine betaine**. BetC therefore routes plant/fungal-derived choline-O-sulfate into (i) osmoprotection via glycine betaine and (ii) nutrient catabolism, enabling *S. meliloti* to use choline-O-sulfate as a sole carbon, nitrogen, **and** sulfur source. It functions in the bacterial cytoplasm and is expressed symbiotically within infection threads and nodule bacteroids.

---

## 2. Primary Function — Reaction and Substrate Specificity

**Catalyzed reaction (EC 3.1.6.6):**

> choline-O-sulfate + H₂O → choline + sulfate

Osterås et al. (1998) identified *betC* as "encoding a choline sulfatase catalyzing the conversion of choline-O-sulfate and, at a lower rate, phosphorylcholine, into choline" (PMID 9736747). Thus:

- **Primary substrate:** choline-O-sulfate (the physiologically relevant substrate).
- **Secondary substrate:** phosphorylcholine (hydrolyzed at a lower rate), indicating the active site accommodates the choline moiety with different anionic leaving groups (sulfate vs. phosphate ester).
- **Products:** free choline + inorganic sulfate (or phosphate from phosphorylcholine).

**Genetic assignment of the activity:** Choline sulfatase activity was "absent from *betC* but not from *betB* mutants" (PMID 9736747), unambiguously assigning the enzymatic activity to the *betC* gene product rather than to other *bet* enzymes. The activity is enzymatically **inducible** — induced "indifferently by choline or choline-O-sulfate," in parallel with the other pathway enzymes (PMID 9736747).

### Catalytic mechanism (by family/structural inference)

BetC is a member of the **formylglycine (FGly)-dependent sulfatase family** (Sulfatase_N / Sulfatase_CS domains; alkaline-phosphatase-core superfamily). Although BetC itself has not been crystallized, the mechanism is firmly established for the family from high-resolution structures of close bacterial and human relatives:

- A strictly conserved active-site cysteine (within the sulfatase C-X-P-X-R signature) is **post-translationally oxidized to Cα-formylglycine (FGly)**; this modification "is strictly conserved in prokaryotic and eukaryotic sulfatases" (Ghosh 2007, PMID 17558559).
- The 1.3 Å structure of *Pseudomonas aeruginosa* arylsulfatase (PAS) showed that "the resting state of the key catalytic residue in sulfatases is a formylglycine hydrate" and established "a mechanism for sulfate ester cleavage involving an aldehyde hydrate as the functional group that initiates the reaction through a nucleophilic attack on the sulfur atom in the substrate" (Boltes et al. 2001, PMID 11435113).
- Catalysis requires a divalent metal cation (Ca²⁺ in PAS) that positions the substrate sulfate and stabilizes the transition state (PMID 11435113).

**Mechanistic inference for BetC:** the FGly-hydrate gem-diol performs nucleophilic attack on the sulfur of the choline sulfate ester, transiently forming a covalent sulfo-enzyme intermediate; elimination releases choline (the alcohol), and hydrolysis regenerates the enzyme while liberating inorganic sulfate. This explains both the measured choline-sulfatase activity and the ability of the enzyme to also process the analogous phosphate ester (phosphorylcholine), albeit less efficiently.

**BetC-specific sequence evidence (this work):** Direct analysis of the 512-residue O69787 sequence confirms the mechanism is not merely homology-inferred. The conserved sulfatase FGly-directing signature **C-X-P-X-R is present as C54-A-P-A-R** (residues 54–58). UniProt feature annotation marks **residue 54 as the catalytic active-site nucleophile, post-translationally modified to 3-oxoalanine (Cα-formylglycine) from cysteine**, with a second active-site residue at position 104 and metal/substrate-binding residues at positions 14, 15, 296 and 297 (the divalent-cation/sulfate-binding pocket typical of the family). A Kyte–Doolittle hydrophobicity scan (19-residue window) yields a maximum of only 0.94 with **zero windows exceeding the 1.6 transmembrane threshold**, indicating no membrane-spanning segment — consistent with a soluble, cytoplasmic enzyme.

---

### Domain architecture and evolutionary classification (bioinformatic evidence)

InterPro/Pfam/TIGRFAM analysis of O69787 (512 aa) reveals a two-module enzyme:

| Module | Database IDs | Residues | Role |
|--------|-------------|----------|------|
| Catalytic sulfatase domain | PF00884 / IPR000917, in alkaline-phosphatase-like core superfamily IPR017850 | ~6–352 (core 5–486) | FGly/metal catalytic machinery |
| Sulfatase signature 1 | PS00523 / IPR024607 | 52–64 | Contains catalytic **Cys54→formylglycine** |
| Sulfatase signature 2 | PS00149 / IPR024607 | 94–104 | Second active-site residue (104) |
| Choline-sulfatase C-terminal domain | PF12411 / IPR025863 | 457–508 | Choline-sulfatase-specific; candidate specificity/structural determinant |

Critically, the whole protein is assigned to **dedicated choline-sulfatase families — InterPro IPR017785, TIGRFAM TIGR03417 ("choline-sulfatase", an equivalog family whose members share the same specific function), and NCBI CDD cd16032** — not merely to the generic arylsulfatase class. This provides **evolution/orthology-based evidence** that BetC's specific physiological substrate is choline-O-sulfate, consistent with the direct enzymatic assays. The dedicated C-terminal domain (res 457–508), present in choline-sulfatases but absent from generic arylsulfatases, is a plausible determinant for recognition of the bulky quaternary-ammonium (choline) moiety.

## 3. Pathway Context — the *betICBA* operon

BetC is the committed entry enzyme of the glycine betaine biosynthesis/catabolism pathway:

| Gene | Product | Step |
|------|---------|------|
| *betI* | TetR-family repressor | Regulation (choline-responsive) |
| **betC** | **Choline-O-sulfatase** | **choline-O-sulfate → choline + sulfate** |
| *betB* | Betaine-aldehyde dehydrogenase | betaine aldehyde → glycine betaine |
| *betA* | Choline dehydrogenase | choline → betaine aldehyde |

Pathway: **choline-O-sulfate →(BetC)→ choline →(BetA)→ betaine aldehyde →(BetB)→ glycine betaine.**

- The four genes "constitute a single operon," comprising regulator *betI* plus structural *betC*, *betB*, *betA* (Mandon et al. 2003, PMID 12906115; Osterås et al. 1998, PMID 9736747).
- The operon is organized with 130-bp mosaic elements between *betI*–*betC* and *betB*–*betA* (PMID 9736747).

### Regulation
Transcription shows "strong induction by choline at concentrations as low as 25 µM and to a lesser extent by choline-O-sulfate and acetylcholine but not by osmotic stress or oxygen" (Mandon et al. 2003, PMID 12906115). BetI is a repressor that senses the endogenous choline pool; repression is relieved when choline accumulates. Importantly, *betC* is **substrate-induced, not osmotically induced** — consistent with a metabolic entry role rather than a direct osmotic-stress gene.

---

## 4. Biological Role and Physiological Significance

1. **Osmoprotection (indirectly).** The choline liberated by BetC feeds glycine betaine synthesis. Glycine betaine is "a potent osmoprotectant accumulated by *S. meliloti* to cope with osmotic stress" (PMID 9736747). Notably, in *S. meliloti* choline-O-sulfate is **not** used as an osmoprotectant per se; it must be metabolized by BetC into choline and then glycine betaine (PMID 9736747).

2. **Nutrient catabolism (C, N, and S).** *S. meliloti* "can use this compound [choline-O-sulfate] as the sole carbon, nitrogen, and sulfur source for growth and that depends on a functional *bet* locus" (PMID 9736747). BetC specifically liberates the **sulfate** (sulfur source) by cleaving the sulfate ester, and unlocks the choline carbon/nitrogen skeleton for downstream catabolism.

3. **Ecological/symbiotic relevance.** Choline-O-sulfate and phosphorylcholine "are found in higher plants and fungi" (PMID 9736747); BetC lets the rhizobium scavenge these host/soil-derived metabolites. *bet* genes (including *betC*) are expressed "within the infection threads, in young and in mature nodules" during symbiosis with *Medicago sativa* (PMID 12906115), indicating the pathway operates in planta where plant-derived choline compounds are available.

---

### Transport context (how the substrate reaches BetC)

BetC acts on intracellular choline-O-sulfate; *S. meliloti* uses dedicated transporters to supply the relevant quaternary-ammonium metabolites to the cytoplasm:

- **ChoXWV** — a high-affinity, highly specific **choline** ABC transporter (ChoX binding protein K_D ≈ 2.7 µM for choline; low affinity for acetylcholine; does **not** bind betaines). It is induced by choline (not salt) and is present in *Medicago sativa* bacteroids (Dupont et al. 2004, PMID 15342567). This supplies free choline (either imported directly or liberated by BetC) to the BetA/BetB steps.
- **BetS** — a Na⁺-driven BCCT-family high-affinity **glycine betaine/proline betaine** transporter (K_m ≈ 16 µM for glycine betaine) required for early osmotic adjustment; choline is not a BetS substrate (Boscari et al. 2002, PMID 11976294).

Thus imported **choline-O-sulfate is hydrolyzed in the cytoplasm by BetC** to choline + sulfate; choline (from BetC or from ChoXWV) is oxidized to glycine betaine, which can additionally be scavenged directly via BetS. All of these components are choline-inducible and bacteroid-expressed, defining a coordinated choline/choline-O-sulfate catabolic and osmoadaptive module.

## 5. Subcellular Localization

- **Cytoplasmic / soluble enzyme.** Choline sulfatase activity was assayed in cell extracts, and choline-O-sulfate is taken up and metabolized intracellularly in *S. meliloti* (PMID 9736747). Water-soluble, cytosolic localization is the norm for non-membrane sulfatases of this family (e.g., human ARSA/ARSB and bacterial PAS are water-soluble enzymes; only steroid sulfatase carries a membrane-anchoring hydrophobic domain — Ghosh 2007, PMID 17558559). **Sequence analysis of BetC confirms no transmembrane helix (max 19-residue Kyte–Doolittle hydrophobicity 0.94; 0 windows above the 1.6 TM threshold) and no strongly hydrophobic cleavable N-terminal signal peptide**, supporting soluble, cytoplasmic localization consistent with intracellular metabolism of transported choline-O-sulfate.
- The downstream glycine betaine biosynthetic steps (BetA/BetB) and glycine betaine accumulation occur in the cytoplasm, consistent with BetC acting cytoplasmically as the first step.

---

## 6. Comparative Context (orthologs/analogs)

- ***Bacillus subtilis*** and ***S. meliloti***: *betC* is linked to osmoprotection (choline-O-sulfate feeds glycine betaine) (PMID 9736747; PMID 17116241).
- ***Pseudomonas putida* KT2440**: *betC* (choline sulfatase) lies next to an ABC transporter and a LysR regulator, separate from *betBA*; there a *betC* deletion "still accumulated intact COS but failed to use this compound as carbon or nitrogen source," and *betC* "was downregulated at high salt concentrations, showing that the principal role of this gene lied in COS metabolism, not in osmoprotection" (Galvão et al. 2006, PMID 17116241). This highlights that the **conserved biochemical function (choline-O-sulfate hydrolysis) is the same**, but the physiological coupling to osmoprotection vs. pure catabolism differs by organism. In *S. meliloti*, BetC is coupled to both.

---

## 7. Supported vs. Refuted Hypotheses

**Supported:**
- H1: BetC is a choline-O-sulfatase hydrolyzing choline-O-sulfate → choline + sulfate. ✔ (direct enzymatic + genetic evidence, PMID 9736747)
- H2: BetC also hydrolyzes phosphorylcholine, at lower rate. ✔ (PMID 9736747)
- H3: BetC is the entry enzyme of the *betICBA* glycine-betaine pathway and is choline-inducible via BetI. ✔ (PMID 12906115)
- H4: BetC enables use of choline-O-sulfate as a sulfur (and C/N) source. ✔ (PMID 9736747)
- H5: BetC uses the conserved formylglycine-dependent sulfatase mechanism. ✔ (strong family/structural inference, PMID 11435113, 17558559)

**Refuted / not supported:**
- That choline-O-sulfate itself serves as an osmoprotectant in *S. meliloti* — refuted; it must be converted by BetC to glycine betaine (PMID 9736747).
- That *betC* is induced by osmotic/oxygen stress — not supported; induction is by choline, not osmotic stress (PMID 12906115).

---

## 8. Limitations and Future Directions

- No experimental 3D structure or kinetic constants (Km/kcat) for *S. meliloti* BetC are available; the catalytic residue/mechanism is inferred from family homologs (PAS, human ARSA/ARSB). AlphaFold modeling and direct identification of the FGly-bearing cysteine and metal site would confirm the mechanism.
- The formylglycine-generating machinery (FGE/anSME) responsible for maturing BetC in *S. meliloti* has not been explicitly linked; verifying the maturation route would complete the mechanistic picture.
- Precise subcellular localization (cytoplasm vs. periplasm) and the choline-O-sulfate uptake transporter in *S. meliloti* warrant direct experimental confirmation.

---

## 9. Consolidated Evidence Summary

| Claim about BetC | Evidence type | Key support |
|---|---|---|
| Choline-O-sulfatase: choline-O-sulfate → choline + sulfate (EC 3.1.6.6) | Experimental (enzyme assay) | Osterås 1998 (PMID 9736747) |
| Activity assigned to *betC* gene | Experimental (mutant: activity lost in *betC*, retained in *betB*) | PMID 9736747 |
| Also hydrolyzes phosphorylcholine (lower rate) | Experimental | PMID 9736747 |
| Enables use of choline-O-sulfate as sole C/N/S source | Experimental (growth, *bet*-dependent) | PMID 9736747 |
| Entry enzyme of *betICBA* operon; choline-inducible via BetI; bacteroid-expressed | Experimental (operon mapping, *lacZ* fusions, in planta) | Mandon 2003 (PMID 12906115) |
| Formylglycine-dependent catalytic mechanism (FGly hydrate nucleophile + metal) | Structural (family homologs) | Boltes 2001 (PMID 11435113); Ghosh 2007 (PMID 17558559) |
| Catalytic Cys54→formylglycine; 2nd active site 104; metal site; no TM helix | Bioinformatic (sequence + UniProt features + hydrophobicity) | This work (O69787 analysis) |
| Dedicated choline-sulfatase equivalog family; 2-domain architecture | Evolution/bioinformatic (InterPro/TIGR03417/cd16032) | This work |
| Cytoplasmic; substrate delivered by ChoXWV (choline) / BetS (betaine) | Experimental + inference | Dupont 2004 (PMID 15342567); Boscari 2002 (PMID 11976294) |

## References (PMIDs)
- Osterås M, Boncompagni E, Vincent N, Poggi MC, Le Rudulier D. *Presence of a gene encoding choline sulfatase in Sinorhizobium meliloti bet operon: choline-O-sulfate is metabolized into glycine betaine.* PNAS 1998. **PMID 9736747**.
- Mandon K, Osterås M, Boncompagni E, Trinchant JC, Spennato G, Poggi MC, Le Rudulier D. *The Sinorhizobium meliloti glycine betaine biosynthetic genes (betICBA) are induced by choline and highly expressed in bacteroids.* J Bacteriol 2003. **PMID 12906115**.
- Galvão TC, de Lorenzo V, Cánovas D. *Uncoupling of choline-O-sulphate utilization from osmoprotection in Pseudomonas putida.* 2006. **PMID 17116241**.
- Boltes I et al. *1.3 Å structure of arylsulfatase from Pseudomonas aeruginosa establishes the catalytic mechanism of sulfate ester cleavage in the sulfatase family.* 2001. **PMID 11435113**.
- Ghosh D. *Human sulfatases: a structural perspective to catalysis.* 2007. **PMID 17558559**.
- Dupont L, Garcia I, Poggi MC, Alloing G, Mandon K, Le Rudulier D. *The Sinorhizobium meliloti ABC transporter Cho is highly specific for choline and expressed in bacteroids from Medicago sativa nodules.* J Bacteriol 2004. **PMID 15342567**.
- Boscari A, Mandon K, Dupont L, Poggi MC, Le Rudulier D. *BetS is a major glycine betaine/proline betaine transporter required for early osmotic adjustment in Sinorhizobium meliloti.* J Bacteriol 2002. **PMID 11976294**.


## Artifacts

- [OpenScientist final report](betC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](betC-deep-research-openscientist_artifacts/final_report.pdf)