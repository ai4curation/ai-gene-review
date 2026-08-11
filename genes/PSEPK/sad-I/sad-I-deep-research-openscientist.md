---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T04:22:52.388895'
end_time: '2026-08-11T05:27:05.531778'
duration_seconds: 3853.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sad-I
  gene_symbol: sad-I
  uniprot_accession: Q88K05
  protein_description: 'SubName: Full=NAD+-dependent succinate semialdehyde dehydrogenase
    {ECO:0000313|EMBL:AAN68100.1}; EC=1.2.1.24 {ECO:0000313|EMBL:AAN68100.1};'
  gene_info: Name=sad-I {ECO:0000313|EMBL:AAN68100.1}; OrderedLocusNames=PP_2488 {ECO:0000313|EMBL:AAN68100.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aldehyde dehydrogenase family.
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_N.
    (IPR016162); Aldehyde_DH_dom. (IPR015590); ALDH_GabD1-like. (IPR044148)
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
  path: sad-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sad-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K05
- **Protein Description:** SubName: Full=NAD+-dependent succinate semialdehyde dehydrogenase {ECO:0000313|EMBL:AAN68100.1}; EC=1.2.1.24 {ECO:0000313|EMBL:AAN68100.1};
- **Gene Information:** Name=sad-I {ECO:0000313|EMBL:AAN68100.1}; OrderedLocusNames=PP_2488 {ECO:0000313|EMBL:AAN68100.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aldehyde dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590); ALDH_GabD1-like. (IPR044148)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sad-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sad-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sad-I** (gene ID: sad-I, UniProt: Q88K05) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sad-I* (PP_2488, UniProt Q88K05)
### NAD⁺-dependent succinic semialdehyde dehydrogenase of *Pseudomonas putida* KT2440

---

## 0. Identity verification (mandatory)

| Attribute | Value | Source |
|---|---|---|
| UniProt | Q88K05 (*Q88K05_PSEPK*, TrEMBL, PE-3 inferred from homology) | UniProt |
| Gene symbol | *sad-I* | UniProt / KEGG |
| Locus | PP_2488 (position complement 2,835,657–2,837,048) | KEGG |
| Protein | NAD⁺-dependent succinate semialdehyde dehydrogenase, **EC 1.2.1.24** | UniProt / GenBank AAN68100 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) | UniProt |
| Length / mass | 463 aa / 50.3 kDa | UniProt |
| Family / domains | Aldehyde dehydrogenase (ALDH) superfamily; Pfam PF00171 (Aldedh); CDD cd07100 (ALDH_SSADH1_GabD1); InterPro IPR044148 (ALDH_GabD1-like), IPR047110 (GABD/Sad-like); eggNOG COG1012 | UniProt / KEGG |

**Verification result: CONFIRMED.** The gene symbol (*sad-I*), organism (*P. putida* KT2440), EC number (1.2.1.24), and ALDH-family/GabD1-like domains all match the provided target identity and are internally consistent across UniProt, KEGG and GenBank. There is no gene-symbol ambiguity: "*sad*" denotes **s**uccinic **a**ldehyde **d**ehydrogenase, and KT2440 explicitly carries two *sad* genes (*sad-I*/PP_2488 and *sad-II*/PP_3151) plus two *gabD* genes, all consistent with the SSADH function. This report describes PP_2488.

> **Evidence caveat.** No study has, to my knowledge, purified or genetically dissected PP_2488 *specifically*. The functional assignment below rests on: (i) authoritative database annotation; (ii) direct biochemistry of the *P. putida* NAD-preferring SSADH enzyme class; (iii) crystallography + mutagenesis of the close ortholog *Sad*/YneI; and (iv) my own sequence/structure bioinformatic analysis. Confidence is high for the reaction, cofactor and localization; moderate for the precise dominant physiological pathway (see §5).

---

## 1. Summary (answer to the research question)

*sad-I* encodes a **soluble, cytoplasmic, NAD⁺-preferring succinic semialdehyde dehydrogenase (SSADH; EC 1.2.1.24)** of the aldehyde-dehydrogenase superfamily. Its primary reaction is the essentially irreversible, NAD⁺-dependent oxidation of the reactive aldehyde **succinic semialdehyde (SSA) → succinate**, feeding carbon into the TCA cycle. It is the terminal enzyme of the **GABA "shunt"** (the pathway 4‑aminobutyrate → SSA → succinate) and, more generally, oxidizes SSA produced by several converging catabolic routes (GABA, polyamine/putrescine, and aromatic 4‑hydroxyphenylacetate catabolism), also serving a housekeeping **aldehyde-detoxification** role. It is one of four SSADH paralogs in KT2440 and belongs to the NAD⁺-specific *sad*/*yneI* clade, distinct from the NADP⁺-specific *gabD* clade that sits in the dedicated GABA-nitrogen operon.

---

## 2. Primary function: reaction catalyzed

**Reaction:** succinate semialdehyde + NAD⁺ + H₂O → succinate + NADH + H⁺ (EC 1.2.1.24; UniProt/KEGG annotation; KEGG Orthology K00135).

SSADHs are ubiquitous enzymes that "catalyze the oxidation of succinic semialdehyde (SSA) to succinic acid in the presence of NAD(P)⁺" (Jang et al., *Biochem. Biophys. Res. Commun.* 2015; **PMID 25888791**). Because the aldehyde is oxidized to a carboxylate with concomitant hydride transfer to NAD⁺, the reaction is thermodynamically favorable and physiologically unidirectional (biosynthetic/degradative "clean-up" direction).

**Catalytic mechanism (inferred from the fold and conserved residues).** The ALDH mechanism proceeds via a catalytic cysteine nucleophile that attacks the aldehyde carbonyl to form a thiohemiacetal, hydride transfer to NAD⁺, and hydrolysis of the resulting thioester, with a conserved glutamate acting as general base. My alignment of sad-I to the crystallographically characterized ortholog *Sad*/YneI (see §4) locates all of these elements:

- **Catalytic nucleophile Cys265** (in the "G‑Q‑V‑**C**‑I‑S‑S" motif), equivalent to the catalytic Cys268 of *Salmonella*/E. coli YneI whose side chain sits next to the NAD⁺ nicotinamide ring (Zheng et al., *FEBS J.* 2013; **PMID 23229889**).
- **Catalytic general base Glu362** (≡ YneI Glu365).
- **Substrate-orienting Trp133** (≡ YneI Trp136).
- ALDH cofactor/substrate-binding motifs EPWNFP (131), TGSEGAG (208) and ELGGAD (231).

---

## 3. Substrate specificity and cofactor preference

**Cofactor: NAD⁺-preferring.** The gene is annotated NAD⁺-dependent (EC 1.2.1.24). This is supported by two independent lines of evidence:
- **Biochemistry of the enzyme class in *P. putida*.** Sànchez et al. (*Biochem. J.* / Int. J. Biochem. 1988; **PMID 3355840**) separated two SSADHs from *P. putida*. The smaller dimeric enzyme (≈100 kDa; 53 kDa subunit) "acts preferentially with NAD but reduces NADP at 9% of the rate observed for NAD," i.e., a strongly NAD-preferring SSADH — the biochemical counterpart of the *sad* class to which PP_2488 belongs. (The larger ≈200 kDa enzyme was NADP-dependent and putrescine-induced — the *gabD* counterpart.)
- **Conserved cofactor determinant.** The residue shown by mutagenesis to confer NAD⁺ preference in YneI (**Lys160**) is conserved in sad-I as **Lys157** (**PMID 23229889**; my alignment).

**Substrate: succinic semialdehyde, with promiscuity toward related semialdehydes.** The physiological substrate is SSA (a 4-carbon ω-aldehyde-carboxylate). NAD-specific SSADHs of this class are, however, catalytically promiscuous:
- Classic work on the *E. coli* NAD- vs NADP-specific SSADHs found that "the NADP-specific enzyme catalyzes only the oxidation of succinate-semialdehyde… whereas the NAD-specific form is active also towards n-butyraldehyde" (Cozzani et al. 1980; **PMID 7004491**) — i.e., the NAD-type enzyme (sad-I's class) has broader aldehyde tolerance.
- In engineered *E. coli*, the native *Sad* had to be deleted because it oxidizes **malate semialdehyde**, a non-native C4 semialdehyde, diverting flux from 2,4-dihydroxybutyrate production (Nguyen et al. 2025; **PMID 40421117**).
- SSADH promiscuity has been repeatedly recruited during adaptive laboratory evolution to repair distinct metabolic deficiencies (He et al., 2024; **PMID 39406738**).

This promiscuity underlies a general **detoxification** function: SSADHs "play an important role in… the detoxification of accumulated SSA" (**PMID 25888791**).

---

## 4. Structural and evolutionary evidence

- **Fold/oligomer.** sad-I is a two-domain (Rossmann-like NAD-binding + catalytic) ALDH-superfamily protein (Gene3D 3.40.605.10 / 3.40.309.10; SSF53720). ALDH-family SSADHs function as homodimers/homotetramers; the *P. putida* NAD-preferring SSADH was characterized as a ≈100 kDa dimer of 53 kDa subunits (**PMID 3355840**).
- **Orthology.** By global alignment, sad-I is most similar to *E. coli* **Sad/YneI** (P76149, the NAD⁺-specific SSADH; **41.9–42.4 % identity**) and less similar to *E. coli* **GabD** (P25526, NADP⁺-specific; 37.5 %). *E. coli* Sad is explicitly "the succinate-semialdehyde dehydrogenase, Sad (also known as YneI)" (Rodionova et al. 2022; **PMID 35508583**).
- **Paralog family in KT2440.** Four SSADHs (all KO K00135): NAD-type **sad-I/PP_2488** and **sad-II/PP_3151** (43.6 % mutual identity) form one clade; NADP-type **gabD-I/PP_0213** and **gabD-II/PP_4422** (53.4 % mutual identity) form the other. gabD-I sits immediately downstream of **gabT/PP_0214** (4-aminobutyrate aminotransferase), i.e., in the canonical GABA-degradation operon; **sad-I does not** — it lies in a cluster of other aldehyde/xenobiotic-processing enzymes (adjacent aldehyde dehydrogenase PP_2487; OYE-family N-ethylmaleimide reductase PP_2486; xenobiotic reductases).
- **Active-site conservation** (my alignment to Sad/YneI): catalytic **Cys265** (≡Cys268), general base **Glu362** (≡Glu365), substrate **Trp133** (≡Trp136), NAD⁺-preference **Lys157** (≡Lys160). All four are conserved (one YneI residue, Asp426, aligns to Arg423 near an indel — the only divergence).

---

## 5. Biological process / pathway context

The unifying theme is that **succinic semialdehyde is a metabolic hub aldehyde** produced by several catabolic routes, and sad-I oxidizes it to succinate for entry into the TCA cycle:

1. **GABA shunt (4-aminobutyrate degradation).** GABA is transaminated (GABA aminotransferase) to SSA, which SSADH then oxidizes to succinate — the terminal, committed step (established across taxa; human SSADH, Kim et al. 2009, **PMID 19300440**; *E. coli* NAD-SSADH induced on GABA as sole N-source, **PMID 7004491**). KEGG maps PP_2488 to *butanoate metabolism* and *alanine/aspartate/glutamate metabolism* (GABA node).
2. **Polyamine (putrescine) catabolism.** Putrescine degradation converges on GABA/SSA. In *P. putida* the NADP-dependent SSADH is putrescine-induced (**PMID 3355840**); the NAD-preferring sad-I provides an alternative/parallel SSA-oxidizing activity.
3. **Aromatic 4-hydroxyphenylacetate (4-HPA) / tyrosine catabolism.** The 4-HPA *meta*-cleavage pathway yields SSA as an end product; notably, the *P. putida* NAD-preferring SSADH is specifically **induced by growth on 4-hydroxyphenylacetate** (**PMID 3355840**), and KEGG lists PP_2488 under *tyrosine metabolism*. This is the most distinctive candidate physiological role separating the *sad* enzymes from the GABA-operon *gabD*.
4. **General aldehyde detoxification.** Given its promiscuity and its genomic neighborhood of aldehyde/reductase genes, sad-I also acts as a housekeeping scavenger of reactive C4 (and related) semialdehydes (**PMID 25888791, 40421117, 39406738**).

Regulatorily, in *E. coli* the *sad*/*yneI* gene is controlled by the LysR-type regulator **PtrR/YneJ** (**PMID 35508583**), distinct from the GabR/σ-based control of *gabTD*, reinforcing that *sad*- and *gabD*-type SSADHs are separately deployed.

---

## 6. Localization

sad-I is a **soluble cytoplasmic** enzyme. Bioinformatic analysis found no transmembrane segment (max Kyte-Doolittle hydropathy 0.96, below the ~1.6–2.0 TM threshold; zero windows >1.6), a net-hydrophilic GRAVY of −0.071, and a polar N-terminus with no signal-peptide core; UniProt reports no signal peptide, transmembrane region or targeting sequence. Its substrate SSA is generated by soluble cytoplasmic transaminases/ring-cleavage enzymes, consistent with cytosolic action. (In eukaryotes the orthologous SSADH is mitochondrial-matrix, **PMID 19300440**; bacteria lack that compartment and the enzyme is cytosolic.)

---

## 7. Supported and refuted hypotheses

**Supported**
- H1 — sad-I is a NAD⁺-dependent SSADH catalyzing SSA→succinate. *(DB annotation + conserved catalytic Cys265/Glu362 + NAD-preference Lys157 + class biochemistry.)*
- H2 — sad-I belongs to the NAD-preferring *sad*/*yneI* clade, distinct from NADP-type *gabD*. *(Sequence orthology 41.9 % to Sad vs 37.5 % to GabD; clade structure of the 4 paralogs.)*
- H3 — sad-I is soluble/cytoplasmic. *(No TM/signal; net-hydrophilic.)*
- H4 — Broader/promiscuous aldehyde specificity + detoxification role. *(n-butyraldehyde, malate semialdehyde activity of the class.)*

**Refuted / disfavored**
- sad-I is *not* the dedicated GABA-nitrogen operon SSADH — that role is filled by gabD-I/PP_0213 (in operon with gabT/PP_0214). sad-I is not gene-linked to gabT.
- sad-I is not a membrane or secreted protein.

---

## 8. Limitations and future directions

- **No PP_2488-specific enzymology.** Km/kcat, exact cofactor ratio, oligomeric state and substrate scope of the *specific* protein are inferred, not measured. Recombinant expression + steady-state kinetics on SSA, glutarate-semialdehyde, malate-semialdehyde and n-butyraldehyde would define specificity directly.
- **sad-I vs sad-II division of labor** is unresolved; a clean knockout/complementation and growth phenotyping on GABA, putrescine and 4-HPA would assign the dominant in-vivo pathway.
- **Structure.** An AlphaFold model exists (AlphaFoldDB Q88K05); experimental structure with NAD⁺/SSA would confirm the modeled active site.
- KEGG additionally lists the generic K00135 ortholog under *lysine degradation* (glutarate-semialdehyde dehydrogenase, EC 1.2.1.20); whether sad-I contributes to glutarate metabolism in vivo (vs the dedicated CoA-independent pathway) remains to be tested.

---

### Key references
- PMID 3355840 — Two SSADHs in *P. putida* (NAD-preferring vs NADP; induction by 4-HPA vs putrescine).
- PMID 7004491 — *E. coli* NAD- vs NADP-specific SSADH; substrate range; GABA induction.
- PMID 23229889 — Crystal structure + mutagenesis of NAD(P)⁺ SSADH YneI (catalytic Cys268, Trp136, Glu365; Lys160 NAD⁺ preference).
- PMID 25888791 — SSADH reaction and detoxification role.
- PMID 19300440 — SSADH as terminal GABA-degradation enzyme (human, mitochondrial).
- PMID 35508583 — *E. coli* Sad ≡ YneI; PtrR/YneJ regulation.
- PMID 40421117, 39406738 — SSADH substrate promiscuity.
- PMID 12534463 (Nelson 2002), 26913973 (Belda 2016) — KT2440 genome/annotation.


## Artifacts

- [OpenScientist final report](sad-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sad-I-deep-research-openscientist_artifacts/final_report.pdf)