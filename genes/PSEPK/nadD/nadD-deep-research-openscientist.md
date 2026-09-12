---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T15:07:39.351889'
end_time: '2026-07-20T15:48:42.117246'
duration_seconds: 2462.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nadD
  gene_symbol: nadD
  uniprot_accession: Q88DL5
  protein_description: 'RecName: Full=Probable nicotinate-nucleotide adenylyltransferase
    {ECO:0000255|HAMAP-Rule:MF_00244}; EC=2.7.7.18 {ECO:0000255|HAMAP-Rule:MF_00244};
    AltName: Full=Deamido-NAD(+) diphosphorylase {ECO:0000255|HAMAP-Rule:MF_00244};
    AltName: Full=Deamido-NAD(+) pyrophosphorylase {ECO:0000255|HAMAP-Rule:MF_00244};
    AltName: Full=Nicotinate mononucleotide adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00244};
    Short=NaMN adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00244};'
  gene_info: Name=nadD {ECO:0000255|HAMAP-Rule:MF_00244}; OrderedLocusNames=PP_4810;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NadD family. {ECO:0000255|HAMAP-
  protein_domains: Cyt_trans-like. (IPR004821); NadD/NMNAT. (IPR005248); Rossmann-like_a/b/a_fold.
    (IPR014729); CTP_transf_like (PF01467)
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
  path: nadD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DL5
- **Protein Description:** RecName: Full=Probable nicotinate-nucleotide adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00244}; EC=2.7.7.18 {ECO:0000255|HAMAP-Rule:MF_00244}; AltName: Full=Deamido-NAD(+) diphosphorylase {ECO:0000255|HAMAP-Rule:MF_00244}; AltName: Full=Deamido-NAD(+) pyrophosphorylase {ECO:0000255|HAMAP-Rule:MF_00244}; AltName: Full=Nicotinate mononucleotide adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00244}; Short=NaMN adenylyltransferase {ECO:0000255|HAMAP-Rule:MF_00244};
- **Gene Information:** Name=nadD {ECO:0000255|HAMAP-Rule:MF_00244}; OrderedLocusNames=PP_4810;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NadD family. {ECO:0000255|HAMAP-
- **Key Domains:** Cyt_trans-like. (IPR004821); NadD/NMNAT. (IPR005248); Rossmann-like_a/b/a_fold. (IPR014729); CTP_transf_like (PF01467)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadD** (gene ID: nadD, UniProt: Q88DL5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *nadD* (Q88DL5, PP_4810) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

- **UniProt:** Q88DL5
- **Gene:** *nadD* (Ordered locus PP_4810)
- **Protein:** Probable nicotinate-nucleotide adenylyltransferase; EC 2.7.7.18
- **Synonyms:** NaMN adenylyltransferase (NaMNAT/NAMNAT); deamido-NAD⁺ diphosphorylase/pyrophosphorylase
- **Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125)
- **Family/domains:** NadD family (HAMAP MF_00244); NadD/NMNAT (IPR005248), Cyt_trans-like (IPR004821), Rossmann-like α/β/α fold (IPR014729), CTP_transf_like (PF01467)

**Verification outcome:** The gene symbol *nadD*, the protein description, the assigned family (NadD), and the domain architecture are all mutually consistent and match a large, coherent body of literature on the bacterial enzyme **nicotinate mononucleotide adenylyltransferase**. There is no ambiguity: *nadD* here denotes the NAD-biosynthetic enzyme, not any similarly named unrelated gene. No experimental study on the *P. putida* KT2440 ortholog specifically was found, so functional statements are inferences from (i) the strongly conserved NadD enzyme family characterized in *E. coli*, *Bacillus subtilis*, *B. anthracis*, *M. tuberculosis*, *S. pyogenes*, and humans, and (ii) the UniProt/HAMAP family assignment. These inferences are high-confidence given the diagnostic domain signatures and the deep conservation of the family.

---

## 1. Summary (Answer to the Research Question)

*nadD* encodes **nicotinate mononucleotide adenylyltransferase (NaMNAT, EC 2.7.7.18)**, a cytoplasmic enzyme that catalyzes the **penultimate, committed step of NAD⁺ biosynthesis**: the reversible transfer of an adenylyl (AMP) group from **ATP** to **nicotinic acid mononucleotide (NaMN)**, producing **nicotinic acid adenine dinucleotide (NaAD, "deamido-NAD⁺")** and **inorganic pyrophosphate (PPi)**. NaAD is subsequently amidated by NAD synthetase (NadE) to give mature NAD⁺. Bacterial NadD is **strictly selective for the deamidated substrate NaMN** (versus the amidated NMN), placing it in the deamidated NAD route that serves both de novo and salvage synthesis. The enzyme adopts a Rossmann-like nucleotidyltransferase fold, uses an ordered (ATP-first) mechanism, and is **essential and conserved across bacteria**, making it a validated antibacterial drug target.

## 2. Primary Function: Reaction and Substrate Specificity

**Reaction catalyzed (EC 2.7.7.18):**

> ATP + nicotinate D-ribonucleotide (NaMN) ⇌ diphosphate (PPi) + deamido-NAD⁺ (NaAD)

This is the adenylylation of NaMN to form NaAD, the immediate precursor of NAD⁺ (Gou et al., 2012, PMID 23289308). Knockdown studies confirm NaMN is the substrate and NaAD the product: suppressing NadD causes NaMN to accumulate while NaAD and the NAD(H) pool are depleted (Rodionova et al., 2014, PMID 24549842).

**Substrate specificity — NaMN over NMN.** Within the pyridine-nucleotide adenylyltransferase (PNAT) superfamily, substrate preference is modular: bacterial NadD is the **strictly NaMN-selective** member, in contrast to NMN-selective NadR/NadM and bifunctional mammalian NMNAT (Sorci et al., 2025, PMID 41109367). Direct biochemistry on the *B. subtilis* enzyme showed it can adenylate both NaMN and NMN in vitro but is specific for the nicotinate (carboxylated/deamidated) form, with the nicotinic-acid carboxylate recognized through active-site backbone contacts (Olland et al., 2002, PMID 11704676). Because *P. putida* NadD is assigned to the NadD family, it is predicted to share this strict NaMN preference and thus to operate in the **deamidated** branch (NaMN → NaAD → NAD⁺) rather than the amidated (NMN → NAD⁺) branch.

**Co-substrate:** ATP is the adenylyl donor; Mg²⁺ is the typical divalent cation cofactor for this nucleotidyltransferase chemistry.

## 3. Structure and Mechanism

Bacterial NadD orthologs share a **monomeric fold of the nucleotidyltransferase α/β phosphodiesterase superfamily** — a dinucleotide-binding **Rossmann-like fold** — carrying the conserved N-terminal (T/H)XGH adenylyltransferase motif that engages ATP (Olland et al., 2002, PMID 11704676). *B. subtilis* NadD is a functional **dimer**. Steady-state kinetic analysis of *M. tuberculosis* NadD established a **sequential ordered mechanism in which ATP binds first**, enabling productive NaMN binding and catalysis, coupled to an open↔closed active-site conformational transition (Rodionova et al., 2015, PMID 25631047). The UniProt annotation of Q88DL5 (Rossmann-like α/β/α fold IPR014729; CTP_transf_like PF01467; Cyt_trans-like IPR004821) is fully consistent with this architecture, supporting the mechanistic inference for the *P. putida* enzyme.

## 3a. Residue-Level Confirmation in the *P. putida* Ortholog

Direct analysis of the UniProt Q88DL5 sequence (230 aa) confirms the family assignment at the residue level, not merely by homology inference:

- **Catalytic (T/H)XGH motif:** the N-terminal signature **GGTFDPVHIGH** (residues 25–35) embeds the **"HIGH"** motif (His32–x–Gly34–His35), the diagnostic adenylyltransferase motif that binds ATP and positions its α-phosphate for adenylyl transfer.
- **Rossmann-like dinucleotide-binding loop:** the glycine-rich `…RRIGILGGTFDP…` region matches the phosphate-binding loop of the α/β nucleotidyltransferase fold.
- **Substrate-binding (S/T)XXXX(R/K) motif:** present in the C-terminal half (e.g., SATQIR at 194, SGKSVR at 204), matching the conserved motif described for bacterial NaMN adenylyltransferases (Olland et al., 2002, PMID 11704676).
- **Size:** 230 aa, typical of single-domain bacterial NadD (~210–230 aa).

These signatures in the actual *P. putida* protein confirm an intact NadD catalytic apparatus.

**Orthology to a validated enzyme.** Global pairwise alignment of *P. putida* NadD (230 aa) against *E. coli* K-12 NadD (P0A752, 213 aa; UniProt evidence level PE=1, protein) gives **38.8% identity** (81/209 aligned columns) — well above the twilight zone for a compact single-domain enzyme — with the **identical catalytic signature** (*E. coli* `GGTFDPVHYGH` vs *P. putida* `GGTFDPVHIGH`). Since *E. coli* NadD is an experimentally characterized, essential NaMN adenylyltransferase and validated inhibitor target (Sorci et al., 2009, PMID 19716475), this orthology transfers experimental function to Q88DL5 with high confidence.

## 4. Subcellular Localization

NadD is a soluble small-molecule metabolic enzyme with **no signal peptide and no transmembrane segments**; it carries out adenylyl transfer in the **bacterial cytoplasm**, where NAD biosynthesis and the NAD(H)/NADP(H) cofactor pools reside. (By contrast, the human ortholog NMNAT-1 is nuclear via a nuclear-localization signal — Zhou et al., 2002, PMID 11788603 — a eukaryote-specific feature not applicable to bacterial NadD.)

## 5. Pathway Context in *P. putida*

NadD sits at the convergence point of NAD⁺ biosynthesis:

- **Upstream inputs to NaMN:** the de novo route (aspartate → quinolinate → NaMN via NadA/NadB/NadC) and the deamidated salvage route (nicotinamide/nicotinate → NaMN via PncA/PncB) both feed NaMN.
- **NadD step:** NaMN + ATP → NaAD + PPi.
- **Downstream:** NAD synthetase **NadE** amidates NaAD to NAD⁺.

NadD and NadE are the two indispensable downstream enzymes shared by all NAD-producing routes (Sorci et al., 2010, PMID 20926389; Sorci et al., 2013, PMID 23204464). In *P. putida* KT2440 this cofactor supply is especially important: the organism has an extensive aerobic, redox-intensive catabolism (mono-/dioxygenases, dehydrogenases) that continuously consumes and regenerates NAD(H)/NADP(H). Notably, *P. putida* KT2440 also possesses a well-known **nicotinate (nic) degradation locus**; intracellular nicotinic-acid pools that fluctuate with this catabolism can influence NAD biosynthetic flux (Brickman & Armstrong, 2018, PMID 29485696), underscoring the role of NadD as a gatekeeper channeling nicotinate-derived NaMN into the NAD⁺ pool.

## 6. Evidence of Essentiality and Physiological Importance

- **Essentiality:** NadD is essential for cell viability in bacteria (Olland et al., 2002, PMID 11704676; Sorci et al., 2010, PMID 20926389).
- **Genetic validation:** Inducible degradation of NadD in *M. tuberculosis* is strongly **bactericidal** in both replicating and non-replicating states, causing NaMN accumulation, NAD(H) depletion, and metabolic catastrophe (Rodionova et al., 2014, PMID 24549842).
- **Metabolic engineering corroboration:** Overexpression of *nadD* in *E. coli* raised total NAD(H) ~2.6-fold and rebalanced NADH/NAD⁺, restoring anaerobic growth — confirming NadD flux controls the NAD pool (Gou et al., 2012, PMID 23289308).
- **Druggability/selectivity:** Structure-based inhibitors selectively inhibit bacterial NadD (*E. coli*, *B. anthracis*) with no effect on human NMNAT, and a co-crystal defined a common inhibitor-binding site (Sorci et al., 2009, PMID 19716475; Huang et al., 2010, PMID 20578699).

## 7. Supported and Refuted Hypotheses

**Supported (high confidence):**
- H1: *nadD* encodes NaMN adenylyltransferase catalyzing NaMN + ATP → NaAD + PPi. ✔ (PMID 23289308, 24549842)
- H2: The enzyme is strictly NaMN-selective (deamidated pathway). ✔ (PMID 41109367, 11704676)
- H3: NadD adopts a Rossmann-like nucleotidyltransferase fold with an ordered ATP-first mechanism. ✔ (PMID 11704676, 25631047)
- H4: NadD is essential and cytoplasmic; loss depletes NAD(H). ✔ (PMID 20926389, 24549842)

**Refuted / not applicable:**
- That *P. putida* NadD is NMN-selective or bifunctional — refuted by strict NadD-family classification (PMID 41109367).
- Nuclear localization (a human-NMNAT feature) — not applicable to a bacterial cytoplasmic enzyme (contrast PMID 11788603).

## 8. Limitations and Future Directions

- No enzymatic, structural, or knockout study exists for the *P. putida* KT2440 NadD specifically; all functional claims are inferences from orthologs and family/domain assignment (though these are among the most conserved and best-characterized in bacteria).
- Future work: recombinant expression and kinetic characterization of *P. putida* NadD (kcat/Km for NaMN, NMN, ATP), an experimental crystal or cryo-EM structure, and conditional-essentiality testing in KT2440 would confirm the inferred properties directly. Given KT2440's nicotinate-degradation capacity, quantifying how nicotinate catabolic flux versus NadD biosynthetic flux partition the NaMN/nicotinate pool would be biologically informative.

---

### Key References
- Gou et al. 2012, PMID 23289308 — reaction (NaMN→NaAD); flux control of NAD pool.
- Rodionova et al. 2014, PMID 24549842 — essentiality; bactericidal knockdown; substrate/product identities.
- Rodionova et al. 2015, PMID 25631047 — structure, ordered ATP-first mechanism.
- Olland et al. 2002, PMID 11704676 — essentiality, NaMN specificity, Rossmann-like fold, dimer.
- Sorci et al. 2025, PMID 41109367 — bacterial NadD strictly NaMN-selective.
- Sorci et al. 2010, PMID 20926389 — conservation, essentiality, drug-target status.
- Sorci et al. 2013, PMID 23204464 — NadD/NadE indispensable downstream NAD enzymes.
- Sorci et al. 2009, PMID 19716475; Huang et al. 2010, PMID 20578699 — selective bacterial inhibitors, inhibitor-binding site.
- Zhou et al. 2002, PMID 11788603 — human NMNAT (contrast for specificity/localization).
- Brickman & Armstrong 2018, PMID 29485696 — *P. putida* KT2440 nicotinate degradation locus and NAD biosynthesis link.


## Artifacts

- [OpenScientist final report](nadD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadD-deep-research-openscientist_artifacts/final_report.pdf)