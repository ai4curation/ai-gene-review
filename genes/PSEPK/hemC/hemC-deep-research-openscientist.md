---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:55:27.579017'
end_time: '2026-07-20T17:59:21.232258'
duration_seconds: 3833.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemC
  gene_symbol: hemC
  uniprot_accession: Q88RE5
  protein_description: 'RecName: Full=Porphobilinogen deaminase {ECO:0000255|HAMAP-Rule:MF_00260};
    Short=PBG {ECO:0000255|HAMAP-Rule:MF_00260}; EC=2.5.1.61 {ECO:0000255|HAMAP-Rule:MF_00260};
    AltName: Full=Hydroxymethylbilane synthase {ECO:0000255|HAMAP-Rule:MF_00260};
    Short=HMBS {ECO:0000255|HAMAP-Rule:MF_00260}; AltName: Full=Pre-uroporphyrinogen
    synthase {ECO:0000255|HAMAP-Rule:MF_00260};'
  gene_info: Name=hemC {ECO:0000255|HAMAP-Rule:MF_00260}; OrderedLocusNames=PP_0186;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HMBS family. {ECO:0000255|HAMAP-
  protein_domains: HemC. (IPR000860); Porphobilin_deaminase_cofac_BS. (IPR022419);
    Porphobilin_deaminase_N. (IPR022417); Porphobilinogen_deaminase_C. (IPR022418);
    Porphobilinogen_deaminase_C_sf. (IPR036803)
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
  path: hemC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RE5
- **Protein Description:** RecName: Full=Porphobilinogen deaminase {ECO:0000255|HAMAP-Rule:MF_00260}; Short=PBG {ECO:0000255|HAMAP-Rule:MF_00260}; EC=2.5.1.61 {ECO:0000255|HAMAP-Rule:MF_00260}; AltName: Full=Hydroxymethylbilane synthase {ECO:0000255|HAMAP-Rule:MF_00260}; Short=HMBS {ECO:0000255|HAMAP-Rule:MF_00260}; AltName: Full=Pre-uroporphyrinogen synthase {ECO:0000255|HAMAP-Rule:MF_00260};
- **Gene Information:** Name=hemC {ECO:0000255|HAMAP-Rule:MF_00260}; OrderedLocusNames=PP_0186;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HMBS family. {ECO:0000255|HAMAP-
- **Key Domains:** HemC. (IPR000860); Porphobilin_deaminase_cofac_BS. (IPR022419); Porphobilin_deaminase_N. (IPR022417); Porphobilinogen_deaminase_C. (IPR022418); Porphobilinogen_deaminase_C_sf. (IPR036803)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemC** (gene ID: hemC, UniProt: Q88RE5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *hemC* (Q88RE5) — Porphobilinogen Deaminase / Hydroxymethylbilane Synthase in *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**hemC** (UniProt **Q88RE5**; ordered locus **PP_0186**) of *Pseudomonas putida* KT2440 encodes **porphobilinogen deaminase (PBGD)**, also called **hydroxymethylbilane synthase (HMBS)** or **pre‑uroporphyrinogen synthase** (**EC 2.5.1.61**). It is the **third enzyme of the tetrapyrrole (heme) biosynthetic pathway**. The enzyme catalyzes the ordered, head‑to‑tail condensation of **four molecules of the monopyrrole porphobilinogen (PBG)** into the **linear tetrapyrrole 1‑hydroxymethylbilane (pre‑uroporphyrinogen)**, releasing four molecules of ammonia. Catalysis occurs on a **covalently bound dipyrromethane (DPM) cofactor** attached through a thioether bond to an invariant active‑site cysteine. It is a **soluble, cytoplasmic** enzyme, and *hemC* is an **essential gene** whose product supplies the linear tetrapyrrole precursor for heme (and siroheme) biosynthesis.

### Gene/Protein Identity Verification
- **Symbol vs. description:** The symbol *hemC* matches the UniProt description ("Porphobilinogen deaminase … Hydroxymethylbilane synthase … EC 2.5.1.61"). ✔
- **Organism:** *Pseudomonas putida* strain KT2440 (PSEPK); locus PP_0186. ✔
- **Family/domains:** InterPro annotations — HemC (IPR000860), Porphobilinogen_deaminase_N (IPR022417), Porphobilinogen_deaminase_C (IPR022418/IPR036803), Porphobilin_deaminase_cofac_BS (IPR022419) — are precisely the signatures of the **HMBS family** described in the structural and mechanistic literature below. ✔
- No ambiguity: *hemC* is a universally conserved heme‑pathway gene; the literature cited concerns exactly this enzyme family. Because *P. putida* PBGD is highly conserved with the crystallographically characterized *E. coli*, human and *Arabidopsis* enzymes, mechanistic and structural inferences transfer directly.

---

## 2. Primary Function: Reaction and Substrate Specificity

**Reaction (EC 2.5.1.61):**
> 4 porphobilinogen + H₂O → hydroxymethylbilane (pre‑uroporphyrinogen) + 4 NH₃

PBGD "catalyses the polymerization of four molecules of porphobilinogen to form the 1‑hydroxymethylbilane, preuroporphyrinogen, a key intermediate in the biosynthesis of tetrapyrroles" (Louie *et al.*, 1996, PMID 8727319). HMBS "combines four porphobilinogen (PBG) molecules to form a linear tetrapyrrole, hydroxymethylbilane" (Sato *et al.*, 2021, PMID 33600566).

- **Substrate:** the monopyrrole **porphobilinogen (PBG)**, itself produced by the preceding enzyme PBG synthase / ALA dehydratase (HemB). Each PBG bears an acetate, a propionate, and an aminomethyl group.
- **Product:** **1‑hydroxymethylbilane (pre‑uroporphyrinogen)**, an unstable linear tetrapyrrole.
- **Chemistry:** deamination coupled to C–C bond formation. During each of the four condensations an aminomethyl group is lost as ammonia and a methylene bridge links successive pyrrole units, extending the chain in a strictly ordered A‑B‑C‑D fashion.
- **Substrate recognition:** a single binding pocket recognizes the PBG side chains. In the human enzyme these contacts involve Arg26/Ser28 (acetate), Arg173 (propionate), Gln34 (aminomethyl) and Asp99 (pyrrole nitrogen) (Sato *et al.*, 2021, PMID 33600566); the equivalent residues are conserved in bacterial orthologs including *P. putida*.

---

## 3. Catalytic Mechanism

**The dipyrromethane (DPM) cofactor.** Uniquely among enzymes, PBGD builds its product on its **own covalently attached DPM cofactor**, which acts as a **primer**. The cofactor "is linked covalently to the enzyme through a thioether bridge to the invariant Cys254" (*Arabidopsis* numbering; Roberts *et al.*, 2013, PMID 23519422) and "is covalently attached to a cysteine side‑chain borne on a flexible loop of domain 3 … [and] serves as a primer for the assembly of the tetrapyrrole product" (Louie *et al.*, 1996, PMID 8727319). The invariant catalytic cysteine corresponds to Cys242 in *E. coli* and Cys261 in human PBGD, with the equivalent conserved cysteine present in the *P. putida* sequence. Bacterial HemC directly carries this cofactor: in *Desulfovibrio vulgaris*, "PBG deaminase (HemC) was shown to contain the dipyrromethane cofactor" (Lobo *et al.*, 2009, PMID 19267692).

**Single site, four steps.** High‑resolution complexes of holo‑HMBS with the reaction intermediate carrying two bound PBG (the "ES2" state) show that "each of the four PBG molecules covalently binds to the cofactor (or oligopyrrole chain) consecutively, ultimately forming a hexapyrrole chain" at **a single substrate‑binding site** (Sato *et al.*, 2021, PMID 33600566). Thus one active site sequentially elongates the chain from the DPM primer (2 pyrroles) up to a covalently tethered **hexapyrrole**, after which the four newly added pyrroles are released as the tetrapyrrole product, regenerating the DPM cofactor.

**Key catalytic residues (mutagenesis evidence).**
- **Asp99** is catalytically essential: the D99G mutant is "an inactive holo‑protein that exists as a complex with two substrate molecules covalently bound to the dipyrromethane cofactor" (Shoolingin‑Jordan *et al.*, 2003, PMID 12773194).
- **Arg149 and Arg173** are required for **DPM cofactor assembly**; R149Q and R173Q cannot reconstitute the holo‑enzyme (PMID 12773194).
- **Arg167** is required for the catalytic cycle; R167Q accumulates stable enzyme–substrate intermediates (PMID 12773194).

**Cofactor self‑assembly.** The DPM cofactor is generated by the apo‑enzyme itself from pre‑uroporphyrinogen; binding of the cofactor increases the thermal stability of the enzyme, and the structure "loosens" as the pyrrole chain elongates, priming product release (Bustad *et al.*, 2013, PMID 23815679).

---

## 4. Structure and Structural Role

PBGD is a **monomeric, three‑domain α/β protein**. In *E. coli*, "the polypeptide chain of PBGD is folded into three alpha/beta domains" (Louie *et al.*, 1996, PMID 8727319): domains 1 and 2 share a five‑stranded mixed β‑sheet topology and form an extensive **active‑site cleft** at their interface, connected by two hinge segments; domain 3 (a three‑stranded antiparallel sheet) carries the flexible cofactor loop. Inter‑domain **hinge motion** accommodates the growing tetrapyrrole chain — mutation of the hinge residue His120 (human) to proline abolishes activity (Song *et al.*, 2009, PMID 18936296). The fold is conserved across the *E. coli* (1.76 Å), human (2.2 Å) and *Arabidopsis* (1.45 Å) structures, providing a reliable template for the *P. putida* enzyme.

### Sequence-level confirmation for the *P. putida* protein (this study)
A pairwise alignment of **Q88RE5 (313 aa)** with the crystallographically defined *E. coli* PBGD (**P06983**, 313 aa) gives **66.6 % identity over the full length** — the two proteins are the same size and clearly orthologous. Critically, **every catalytically important residue is conserved at the identical aligned position** in the *P. putida* enzyme:

| Residue (E. coli) | *P. putida* (Q88RE5) | Role |
|---|---|---|
| **Cys242** | **Cys242** | Thioether anchor of the dipyrromethane cofactor |
| **Asp84** (= human Asp99) | **Asp84** | Key catalytic aspartate for deamination/condensation |
| **Arg11, Arg131, Arg132, Arg149, Arg155** | conserved (all Arg) | Substrate side‑chain / cofactor binding, cofactor assembly |
| SSLRRQ cofactor‑binding motif | present | Cofactor/oligopyrrole anchoring loop |

This is direct sequence evidence — beyond family inference — that Q88RE5 has an **intact PBGD active site** and operates by the same DPM‑cofactor mechanism as the structurally characterized enzymes.

---

## 5. Localization

PBGD/HemC is a **soluble cytoplasmic enzyme**. It carries no signal peptide, transmembrane segment, or membrane‑anchor, consistent with the general biochemistry of the "common" (early) tetrapyrrole pathway, which operates in the cytosol up to the membrane‑associated terminal steps (e.g., ferrochelatase HemH, which is membrane‑associated — Guégan *et al.*, 2003, PMID 12864856). The reaction — a soluble small‑molecule polymerization producing a diffusible linear bilane — takes place in the cytoplasm, where its product is immediately channeled to the next (cytosolic) enzyme.

---

## 6. Pathway Context

*hemC* functions in the **common tetrapyrrole / heme biosynthesis pathway**, the branch point that supplies heme, siroheme, and (in relevant organisms) cobalamin and chlorophyll:

```
Glutamate →(C5 pathway: GltX/HemA/HemL)→ 5‑aminolevulinic acid (ALA)
   → (HemB, ALA dehydratase) → porphobilinogen (PBG)
      → (HemC, PBGD)  → 1‑hydroxymethylbilane      ← THIS ENZYME
         → (HemD, uroporphyrinogen III synthase) → uroporphyrinogen III
            → ... → protoporphyrin IX → (HemH) → heme
```

The product of HemC is normally passed to **HemD (uroporphyrinogen III synthase)**, which cyclizes and rearranges the D‑ring to form the physiological **uroporphyrinogen III** (Shoolingin‑Jordan, 1995, PMID 7592565). In *P. putida* KT2440 this partner enzyme is encoded by a **dedicated, adjacent gene — *hemD* (Q88RE4, locus PP_0187, EC 4.2.1.75, 255 aa) — immediately downstream of *hemC* (PP_0186)**, forming a *hemC–hemD* gene pair. The presence of a separate HemD establishes that *P. putida* HemC is the **monofunctional** deaminase (the bifunctional PBGD/UROS arrangement is found only in organisms lacking *hemD*, e.g., *Leptospira* — Guégan *et al.*, 2003, PMID 12864856), and the genomic adjacency is consistent with hand‑off/channeling of the labile bilane to HemD.

UniProt/HAMAP (rule MF_00260) annotation of Q88RE5 independently corroborates every functional assignment in this report: the catalytic activity **"4 porphobilinogen + H₂O = hydroxymethylbilane + 4 NH₄⁺"** (Rhea RHEA:13185; EC 2.5.1.61), a covalently bound **dipyrromethane cofactor** (ChEBI:60342; "Binds 1 dipyrromethane group covalently"), and the pathway assignment **"protoporphyrin-IX biosynthesis; coproporphyrinogen-III from 5‑aminolevulinate: step 2/4."** Without HemD, the labile 1‑hydroxymethylbilane cyclizes non‑enzymatically to the useless uroporphyrinogen I isomer — underscoring that HemC's role is the ordered assembly of the linear precursor, while ring closure/isomer selection is HemD's job. In bacteria the reconstituted HemC+HemD system converts PBG to uroporphyrinogen III in vitro (Raux *et al.*, 2003, PMID 12408752), and HemC activity governs flux of porphyrin intermediates in engineered pathways (Kim *et al.*, 2009, PMID 19473249; Lee *et al.*, 2013, PMID 23648857).

**Essentiality.** *hemC* is essential for heme synthesis. A psychrophilic *hemC* was used to render *Francisella novicida* temperature‑sensitive by substituting the essential gene (Pankowski, 2016, PMID 27248501), and a *hemC* mutation in *Salmonella* produces a growth‑restricted small‑colony variant that is compensated by gene amplification/second‑site mutation (Pränting & Andersson, 2011, PMID 21219453). This predicts that *P. putida* PP_0186 is required for normal aerobic growth, since heme is the cofactor of its respiratory cytochromes and catalases.

---

## 7. Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| Q88RE5 = porphobilinogen deaminase (HMBS), EC 2.5.1.61 | **Supported** | Domain architecture (IPR000860 etc.) + conserved HMBS family literature |
| Substrate is porphobilinogen; product is 1‑hydroxymethylbilane | **Supported** | PMID 8727319, 33600566 |
| Catalysis uses a covalent DPM cofactor on an invariant Cys | **Supported** | PMID 23519422, 8727319, 19267692 |
| A single active site performs all four condensations | **Supported** | PMID 33600566 |
| Asp/Arg residues are catalytic / cofactor‑assembly determinants | **Supported** | PMID 12773194, 18936296 |
| Cytoplasmic localization | **Supported (inference)** | No targeting signals; soluble‑enzyme biochemistry |
| Enzyme is essential for heme synthesis / growth | **Supported** | PMID 27248501, 21219453 |
| *P. putida* HemC is bifunctional (also HemD activity) | **Refuted** | *P. putida* KT2440 encodes a separate, adjacent HemD (Q88RE4/PP_0187, EC 4.2.1.75); bifunctionality reported only for organisms lacking HemD (e.g., *Leptospira*, PMID 12864856) |
| Catalytic residues (Cys242, Asp84, Arg cluster) conserved in Q88RE5 | **Supported** | Pairwise alignment vs. *E. coli* P06983 (66.6% id): all catalytic residues conserved (this study) |

---

## 8. Limitations and Future Directions

- **Direct experimental data for the *P. putida* KT2440 protein specifically are sparse;** functional and structural conclusions are inferred from its unambiguous membership in the highly conserved HMBS family and from crystallographic/mutagenesis work on the *E. coli*, human, *Arabidopsis* and other bacterial orthologs. The reaction, cofactor chemistry, and essentiality are so conserved that these inferences are robust.
- Localization is inferred from sequence features (no signal/TM segments) and general pathway biochemistry rather than a *P. putida*‑specific fractionation experiment.
- **Future work:** (i) recombinant expression and kinetic characterization of PP_0186 (kcat/Km for PBG, DPM cofactor content); (ii) crystal/cryo‑EM structure to confirm the conserved catalytic Asp/Arg constellation; (iii) targeted knockout/complementation in *P. putida* to confirm essentiality and any conditional heme‑auxotrophy; (iv) test for possible HemC–HemD complex formation/substrate channeling.

---

## References (PMIDs)
- 8727319 — Louie *et al.* 1996, *E. coli* PBGD structure at 1.76 Å.
- 7592565 — Shoolingin‑Jordan 1995, PBGD & UROS structure/mechanism review.
- 33600566 — Sato *et al.* 2021, HMBS–substrate‑analog complexes, single binding site.
- 23519422 — Roberts *et al.* 2013, *Arabidopsis* PBGD, DPM thioether to Cys254.
- 18936296 — Song *et al.* 2009, human PBGD structure; hinge residue.
- 12773194 — Shoolingin‑Jordan *et al.* 2003, catalytic Asp99/Arg mutagenesis.
- 23815679 — Bustad *et al.* 2013, cofactor/stability during elongation.
- 19267692 — Lobo *et al.* 2009, *Desulfovibrio* HemC contains DPM cofactor.
- 27248501 — Pankowski 2016, *hemC* essential gene (temperature‑sensitivity).
- 21219453 — Pränting & Andersson 2011, *hemC* mutation growth restriction (*Salmonella*).
- 12408752 — Raux *et al.* 2003, HemC+HemD in vitro uroporphyrinogen III synthesis.
- 19473249 / 23648857 — HemC controls porphyrin flux in engineered *E. coli*.
- 12864856 — Guégan *et al.* 2003, *Leptospira* heme genes; bifunctional HemC only where HemD absent.


## Artifacts

- [OpenScientist final report](hemC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemC-deep-research-openscientist_artifacts/final_report.pdf)