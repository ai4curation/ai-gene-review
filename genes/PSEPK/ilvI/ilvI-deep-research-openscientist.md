---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T07:31:23.372594'
end_time: '2026-07-17T08:18:04.387455'
duration_seconds: 2801.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ilvI
  gene_symbol: ilvI
  uniprot_accession: Q88DY8
  protein_description: 'RecName: Full=Acetolactate synthase {ECO:0000256|ARBA:ARBA00013145,
    ECO:0000256|RuleBase:RU003591}; EC=2.2.1.6 {ECO:0000256|ARBA:ARBA00013145, ECO:0000256|RuleBase:RU003591};'
  gene_info: Name=ilvI {ECO:0000313|EMBL:AAN70253.1}; OrderedLocusNames=PP_4680 {ECO:0000313|EMBL:AAN70253.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the TPP enzyme family.
  protein_domains: Acetolactate_synth_lsu. (IPR012846); AHAS_TPP. (IPR039368); DHS-like_NAD/FAD-binding_dom.
    (IPR029035); THDP-binding. (IPR029061); Thiamin_PyroP_enz_cen_dom. (IPR012000)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ilvI-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ilvI-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DY8
- **Protein Description:** RecName: Full=Acetolactate synthase {ECO:0000256|ARBA:ARBA00013145, ECO:0000256|RuleBase:RU003591}; EC=2.2.1.6 {ECO:0000256|ARBA:ARBA00013145, ECO:0000256|RuleBase:RU003591};
- **Gene Information:** Name=ilvI {ECO:0000313|EMBL:AAN70253.1}; OrderedLocusNames=PP_4680 {ECO:0000313|EMBL:AAN70253.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the TPP enzyme family.
- **Key Domains:** Acetolactate_synth_lsu. (IPR012846); AHAS_TPP. (IPR039368); DHS-like_NAD/FAD-binding_dom. (IPR029035); THDP-binding. (IPR029061); Thiamin_PyroP_enz_cen_dom. (IPR012000)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ilvI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ilvI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ilvI** (gene ID: ilvI, UniProt: Q88DY8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *ilvI* (Q88DY8, PP_4680) in *Pseudomonas putida* KT2440

## 1. Summary / Answer

**Q88DY8 (gene *ilvI*, locus PP_4680) is the large, catalytic subunit of acetohydroxyacid synthase (AHAS; also called acetolactate synthase, EC 2.2.1.6)** — a thiamine-diphosphate (ThDP)-dependent enzyme that catalyzes the **first and committed step of branched-chain amino acid (BCAA) biosynthesis** (valine, leucine, isoleucine). Acting in the **cytoplasm** as part of an A₂B₂ holoenzyme with a small regulatory subunit (PP_4679/*ilvH*), it condenses two molecules of pyruvate into (2*S*)-2-acetolactate (the Val/Leu precursor), or condenses pyruvate with 2-ketobutyrate into 2-aceto-2-hydroxybutyrate (the Ile precursor), releasing CO₂. The reaction requires ThDP, a divalent metal (Mg²⁺), and FAD.

Gene-identity verification confirms this is the correct protein: UniProt, KEGG, GO, and InterPro all independently annotate Q88DY8/PP_4680 as the AHAS large subunit, and the surrounding literature on the AHAS enzyme family is fully consistent with the provided protein description, domains, and organism.

---

## 2. Gene / Protein Identity Verification (mandatory check)

| Attribute | Provided (UniProt) | Independently confirmed |
|---|---|---|
| Accession | Q88DY8 | UniProt REST ✔ |
| Protein | Acetolactate synthase, EC 2.2.1.6 | UniProt recommended name; KEGG "acetohydroxybutanoate synthase / acetolactate synthase" ✔ |
| Gene / locus | *ilvI* / PP_4680 | KEGG ppu:PP_4680 ✔ |
| Organism | *P. putida* KT2440 | ✔ |
| Family / domains | TPP enzyme family; AHAS_TPP, ThDP-binding, DHS-like NAD/FAD-binding | UniProt SIMILARITY + KEGG orthology K01652 ✔ |
| KEGG ortholog | — | **K01652** = "acetolactate synthase I/II/III **large subunit** [EC:2.2.1.6]" ✔ |
| Length | — | 574 aa |

**Note on nomenclature:** In enterobacteria (*E. coli*), there are three AHAS isozymes whose large catalytic subunits are named *ilvB* (AHAS I), *ilvG* (AHAS II), and *ilvI* (AHAS III); each pairs with a small regulatory subunit (*ilvN*, *ilvM*, *ilvH*, respectively) (Vyazmensky et al., 2009, PMID 19653643). The *P. putida* gene retains the *ilvI* name for its single AHAS large subunit. **The symbol is therefore unambiguous here and the literature on AHAS applies directly.** This is *not* the same as, e.g., unrelated genes that share the "ilvI" text in other contexts.

---

## 3. Primary Function: Reaction and Substrate Specificity

AHAS catalyzes a ThDP-dependent carboligation. UniProt records the canonical reaction (RHEA:25249):

> **2 pyruvate + H⁺ → (2S)-2-acetolactate + CO₂**  (EC 2.2.1.6)

The enzyme has two physiological condensations that partition flux between the BCAA branches (Liu, Li & Wang, 2016, PMID 27576495):

- **Pyruvate + pyruvate → (2S)-2-acetolactate** → downstream to **L-valine** and **L-leucine**.
- **Pyruvate + 2-ketobutyrate → 2-aceto-2-hydroxybutyrate** → downstream to **L-isoleucine**.

**Catalytic mechanism.** ThDP (activated by the divalent metal ion, Mg²⁺) is deprotonated at C2 to a reactive ylide; it attacks the first pyruvate and, after decarboxylation (loss of CO₂), forms a hydroxyethyl-ThDP (enamine/carbanion) intermediate. This carbanion then attacks the carbonyl of a second 2-oxoacid (pyruvate or 2-ketobutyrate), and product release regenerates the ylide (Gokhale & Tilak, 2015, PMID 25882218; Liu et al., 2016, PMID 27576495).

**Cofactors** (UniProt COFACTOR; GO): **ThDP** (1 per subunit), **Mg²⁺** (1 per subunit), and **FAD**. FAD is a non-catalytic, structurally required cofactor — a vestige of AHAS's evolutionary descent from the FAD/redox-dependent pyruvate oxidase family (Gokhale & Tilak, 2015, PMID 25882218; Liu et al., 2016, PMID 27576495).

**Substrate specificity (from a close bacterial homolog).** Kinetic characterization of the orthologous *Ralstonia eutropha* AHAS (ilvBH) shows the enzyme has weak affinity for the first substrate pyruvate (Kₘ ≈ 10.5 µM) but strong selectivity toward **2-ketobutyrate as the second substrate (specificity ratio R ≈ 140)**, explaining efficient isoleucine synthesis when 2-ketobutyrate is available (Lu et al., 2015, PMID 25081555). While measured in *R. eutropha*, this behavior is characteristic of the conserved bacterial AHAS catalytic subunit to which PP_4680 belongs.

**Substrate specificity inferred from conserved active-site residues.** A more ortholog-specific inference comes from the active site itself. *E. coli* AHAS isozyme I (IlvB) is unusual in being **non-specific** for 2-ketobutyrate versus pyruvate as the acceptor substrate; this is caused by two residues (Gln480 and Met476) that replace a **Trp and Leu conserved in the other AHAS isozymes**, accelerating the ligation/product-release steps (Belenky et al., 2012, PMID 22443469). Aligning Q88DY8 to these positions shows that **P. putida IlvI retains the conserved Trp (Trp486)** — exactly as in *E. coli* AHAS III (Trp484) — rather than the AHAS I Gln. It therefore mirrors the AHAS III active site and is predicted to be **specific for 2-ketobutyrate over pyruvate as the second substrate**, i.e., an efficient producer of the isoleucine precursor. This structure/evolution-based prediction is more reliable than generic family-level transfer because it is anchored on the specific catalytic residues of the 67%-identical AHAS III ortholog.

---

## 4. Quaternary Structure, Regulatory Subunit, and Localization

**Holoenzyme architecture.** Active AHAS is a **holoenzyme of a catalytic (large) subunit + a regulatory (small) subunit**. The crystal structure of the AHAS holoenzyme shows a **A₂B₂ arrangement** (two catalytic + two regulatory subunits), with the regulatory-subunit dimer clamping the catalytic dimer; a conserved salt bridge acts as a trigger that opens the catalytic activation loop, boosting catalytic-subunit activity (Zhang et al., 2020, PMID 32538427). The isolated large subunit has only a small fraction of full activity, and holoenzyme activity is fully restored upon reconstitution with the small subunit (Vyazmensky et al., 2009, PMID 19653643).

**The partner small subunit in *P. putida*.** Chromosomal context strongly corroborates this: PP_4680 (*ilvI*, K01652, large subunit) is immediately adjacent to **PP_4679 (K01653, "acetolactate synthase small subunit" = *ilvH*/regulatory subunit)**, and directly upstream lies **PP_4678 (K00053, ketol-acid reductoisomerase / *ilvC*)**, the enzyme catalyzing the *next* step of the pathway. This **ilvC–ilvH–ilvI clustering** is typical of co-regulated BCAA-biosynthesis genes and confirms the functional pairing of PP_4680 with PP_4679 (KEGG genome positions: PP_4680 5317649–5319373; PP_4679 5317156–5317647, same strand).

**Allosteric feedback inhibition.** The regulatory subunit carries paired **ACT domains**; the end-product amino acid(s) **valine (and/or leucine) bind at the interface between two ACT domains**, transmitting inhibition to the catalytic subunit (Barak & Chipman, 2012, PMID 22198286). This makes AHAS the **rate-controlling gatekeeper** of the pathway: BCAA end-products shut down their own synthesis at the first committed step. Homolog kinetics quantify the effect (R. eutropha AHAS: L-valine IC₅₀ ≈ 1.2 mM, L-isoleucine ≈ 2.3 mM, L-leucine ≈ 5.4 mM; Lu et al., 2015, PMID 25081555). Barak & Chipman also note that the regulatory subunits of "typical" single AHAS enzymes in non-enterobacteria resemble *E. coli* AHAS III (ilvIH) — consistent with the *P. putida* ilvIH-type system.

**Subcellular localization.** AHAS is a **soluble cytoplasmic enzyme** (GO:0005948, "acetolactate synthase complex"; no signal peptide or transmembrane region). Its function — a biosynthetic condensation feeding downstream cytoplasmic enzymes (ilvC, ilvD, and the transaminases/leucine-branch enzymes) — is carried out entirely within the cytoplasm.

**PP_4680 is the dedicated *biosynthetic* AHAS.** *P. putida* KT2440 encodes four TPP-family proteins that KEGG maps to the AHAS-large-subunit ortholog K01652 (PP_1157, PP_1394, PP_3365, PP_4680). However, several lines of evidence single out **PP_4680** as the true anabolic BCAA enzyme: (i) the genome contains **only one small regulatory-subunit gene, PP_4679 (K01653)**, and it sits **immediately adjacent to PP_4680** in the ilvC–ilvH–ilvI cluster; (ii) PP_4680 is uniquely annotated "**acetohydroxybutanoate synthase** / acetolactate synthase," i.e., competent for the 2-ketobutyrate→isoleucine branch that defines the biosynthetic enzyme; and (iii) the other three loci are standalone TPP enzymes with no cognate small subunit or *ilv*-operon context (likely catabolic acetolactate/2-oxoacid-decarboxylase-type activities). At the sequence level, Q88DY8 carries the canonical ThDP-binding fingerprint **GDG…N** (…YDK**GDG**NVIKP…, GDG at residue 369), the hallmark motif that coordinates the ThDP–Mg²⁺ cofactor in this enzyme family. Together these confirm PP_4680/*ilvI* as the correct, dedicated biosynthetic AHAS catalytic subunit.

**Orthology confirmed by sequence identity.** Global (Needleman–Wunsch) alignment shows Q88DY8 (574 aa) is **67.0% identical to the *E. coli* AHAS isozyme III large subunit (IlvI, P00893; also 574 aa)** — versus only **44.8% to the AHAS I large subunit (IlvB, P08142)**. This markedly higher identity to *E. coli* AHAS III, plus the identical chain length, establishes Q88DY8 as a **specific ortholog of the AHAS III (ilvIH) lineage** rather than a generic AHAS. This is fully consistent with the observation that "typical" single bacterial AHAS enzymes resemble *E. coli* AHAS III (Barak & Chipman, 2012, PMID 22198286), and it independently validates the *ilvI* gene name from evolutionary evidence.

---

## 5. Pathway Context

AHAS catalyzes **step 1 of 4** in two parallel routes (UniProt PATHWAY; KEGG ppu00290 "Valine, leucine and isoleucine biosynthesis"):

- **L-valine from pyruvate:** step 1/4 → acetolactate → (ilvC) → (ilvD) → 2-ketoisovalerate → (ilvE/transaminase) → valine. 2-Ketoisovalerate also branches to **leucine** (leuABCD) and is a precursor for **pantothenate/CoA**.
- **L-isoleucine from 2-oxobutanoate (2-ketobutyrate):** step 1/4 → 2-aceto-2-hydroxybutyrate → (ilvC) → (ilvD) → 2-keto-3-methylvalerate → (ilvE) → isoleucine. (2-Ketobutyrate itself derives from threonine via threonine dehydratase, *ilvA*.)

Because it initiates all three BCAAs and their derived cofactor precursors, and because the pathway is **absent in animals**, AHAS is the well-known molecular target of >50 commercial herbicides (sulfonylureas, imidazolinones, triazolopyrimidines) and an antimicrobial/anti-tuberculosis drug target (Liu et al., 2016, PMID 27576495; Gokhale & Tilak, 2015, PMID 25882218; Lonhienne et al., 2018, PMID 29440497).

---

## 6. Hypotheses: Supported and Refuted

**Supported**
1. *ilvI*/PP_4680 encodes the AHAS **large catalytic subunit** — supported by UniProt, KEGG K01652, GO, InterPro, and direct concordance with AHAS literature.
2. It catalyzes ThDP/Mg²⁺/FAD-dependent condensation of pyruvate (±2-ketobutyrate) as the committed step of BCAA biosynthesis — supported (UniProt reaction, PMID 27576495, 25882218).
3. It functions as a **cytoplasmic holoenzyme** with the adjacent small subunit PP_4679 (*ilvH*) and is feedback-inhibited by valine via ACT-domain sites — supported by structural/kinetic literature (PMID 32538427, 22198286, 19653643) and by the P. putida ilvC–ilvH–ilvI gene cluster.

**Refuted / ruled out**
- That the *ilvI* symbol refers to an unrelated non-AHAS gene — refuted; all databases and family/domain evidence converge on AHAS.
- That the large subunit alone constitutes the physiologically regulated enzyme — refuted; full activity and valine sensitivity require the small subunit (PMID 19653643, 22198286).

---

## 7. Evidence Quality and Limitations

- **Enzyme identity, reaction, cofactors, pathway, and localization** rest on strong, convergent database annotation (UniProt/KEGG/GO/InterPro) plus authoritative reviews and primary structural studies of the AHAS family — high confidence.
- **Direct biochemical characterization of the *P. putida* KT2440 enzyme specifically was not located** in the searchable literature; the quantitative substrate-specificity and feedback-inhibition parameters cited (Kₘ, IC₅₀, selectivity R) come from a **close bacterial homolog** (*R. eutropha* ilvBH, PMID 25081555) and from *E. coli* isozyme studies. These are transferable by strong homology but are inferences, not measurements on Q88DY8.
- **Future directions:** heterologous expression and kinetic assay of PP_4680 + PP_4679 to measure its own Kₘ/kcat and valine IC₅₀; verification that PP_4679 is the cognate regulatory subunit by co-purification; and testing whether *P. putida* encodes any second AHAS large subunit (an *ilvBN*-type paralog) elsewhere on the chromosome.

---

## References (PMIDs)
- Vyazmensky et al., 2009 — Interactions between large and small AHAS subunits (PMID 19653643)
- Liu, Li & Wang, 2016 — AHAS evolution, structure, and function (review) (PMID 27576495)
- Gokhale & Tilak, 2015 — Mechanisms of bacterial AHAS; drug target (PMID 25882218)
- Zhang et al., 2020 — Molecular architecture of the AHAS holoenzyme (A₂B₂) (PMID 32538427)
- Barak & Chipman, 2012 — Allosteric regulation / ACT-domain feedback sites (PMID 22198286)
- Lu et al., 2015 — Kinetics of *R. eutropha* AHAS (substrate specificity, feedback) (PMID 25081555)
- Belenky et al., 2012 — Active-site residues controlling AHAS I vs III specificity/kinetics (PMID 22443469)
- Lonhienne et al., 2018 — Structural basis of AHAS herbicide inhibition (PMID 29440497)
- Platko, Willins & Calvo, 1990 — *ilvIH* operon regulation in *E. coli* (PMID 2115869)
- Database sources: UniProt Q88DY8; KEGG ppu:PP_4680 / K01652 / ppu00290; InterPro IPR012846, IPR039368, IPR029035, IPR029061, IPR012000.


## Artifacts

- [OpenScientist final report](ilvI-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ilvI-deep-research-openscientist_artifacts/final_report.pdf)