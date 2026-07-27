---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T20:22:03.705135'
end_time: '2026-07-26T21:50:06.817590'
duration_seconds: 5283.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: glgE
  gene_symbol: glgE
  uniprot_accession: Q88FM9
  protein_description: 'RecName: Full=Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase
    {ECO:0000256|HAMAP-Rule:MF_02124}; Short=GMPMT {ECO:0000256|HAMAP-Rule:MF_02124};
    EC=2.4.99.16 {ECO:0000256|HAMAP-Rule:MF_02124}; AltName: Full=(1->4)-alpha-D-glucan:maltose-1-phosphate
    alpha-D-maltosyltransferase {ECO:0000256|HAMAP-Rule:MF_02124};'
  gene_info: Name=glgE {ECO:0000256|HAMAP-Rule:MF_02124, ECO:0000313|EMBL:AAN69650.1};
    OrderedLocusNames=PP_4060 {ECO:0000313|EMBL:AAN69650.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glycosyl hydrolase 13 family. GlgE
  protein_domains: GH. (IPR017853); GH13_cat_dom. (IPR006047); GlgE. (IPR026585);
    GLGE_C. (IPR049171); GlgE_dom_N/S. (IPR021828)
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
  path: glgE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: glgE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FM9
- **Protein Description:** RecName: Full=Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase {ECO:0000256|HAMAP-Rule:MF_02124}; Short=GMPMT {ECO:0000256|HAMAP-Rule:MF_02124}; EC=2.4.99.16 {ECO:0000256|HAMAP-Rule:MF_02124}; AltName: Full=(1->4)-alpha-D-glucan:maltose-1-phosphate alpha-D-maltosyltransferase {ECO:0000256|HAMAP-Rule:MF_02124};
- **Gene Information:** Name=glgE {ECO:0000256|HAMAP-Rule:MF_02124, ECO:0000313|EMBL:AAN69650.1}; OrderedLocusNames=PP_4060 {ECO:0000313|EMBL:AAN69650.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glycosyl hydrolase 13 family. GlgE
- **Key Domains:** GH. (IPR017853); GH13_cat_dom. (IPR006047); GlgE. (IPR026585); GLGE_C. (IPR049171); GlgE_dom_N/S. (IPR021828)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glgE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glgE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glgE** (gene ID: glgE, UniProt: Q88FM9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of GlgE (gene *glgE* / PP_4060; UniProt Q88FM9) in *Pseudomonas putida* KT2440

## 1. Summary (answer to the research question)

**GlgE (Q88FM9, locus PP_4060) is α-maltose-1-phosphate:(1→4)-α-D-glucan 4-α-D-maltosyltransferase (GMPMT; EC 2.4.99.16), a cytoplasmic glycoside-hydrolase family 13 (GH13_3) enzyme.** Its primary function is to **elongate a linear α-1,4-glucan chain by transferring maltosyl (two-glucose) units from the phosphosugar donor α-maltose-1-phosphate (M1P) onto the non-reducing end of a maltooligosaccharide/α-glucan acceptor.** It is the committed polymerizing step of the cytoplasmic **TreS–Mak(Pep2)–GlgE–GlgB pathway**, an ADP-glucose-independent route that converts trehalose/maltose into a branched, glycogen-like α-glucan used for carbon/energy storage. In *P. putida* KT2440 this pathway is genomically complete and clustered (its M1P-supplying maltokinase is immediately adjacent to *glgE*), and — because the classical ADP-glucose enzyme GlgC is absent — it is most likely the organism's **primary** α-glucan biosynthetic route.

The gene identity is **confirmed**: the symbol *glgE*, the EC number, the GH13/GlgE family and domain set (IPR026585 GlgE; IPR006047 GH13 catalytic; IPR049171 GLGE_C; IPR021828 GlgE_dom_N/S) all match the well-characterized GlgE maltosyltransferase. There is no ambiguity with an unrelated gene of the same symbol.

---

## 2. Gene/Protein Identity Verification

| Attribute | Provided (UniProt/HAMAP MF_02124) | Literature consensus | Match |
|---|---|---|---|
| Enzyme name | GMPMT, maltosyltransferase | α-maltose-1-P:α-1,4-glucan maltosyltransferase | ✅ |
| EC number | 2.4.99.16 | 2.4.99.16 (Syson et al. 2014, PMID 24689960) | ✅ |
| Family | GH13, GlgE | CAZy GH13_3 (Syson et al. 2011/2014) | ✅ |
| Domains | GH13 cat., GlgE, GLGE_C, GlgE_N/S | 5-domain GlgE architecture (PMID 21914799) | ✅ |
| Organism | *P. putida* KT2440 | ortholog; function assigned by orthology | ✅ (see §6) |

**Caveat & strength of assignment:** The deep biochemical/structural characterization of GlgE comes from *Streptomyces coelicolor*, *Mycobacterium tuberculosis*, *M. thermoresistibile*, and *S. venezuelae*; the *P. putida* protein itself has not been enzymatically studied. Nonetheless the functional assignment is supported by **five convergent lines of evidence**: (i) the HAMAP rule MF_02124 + curated UniProt reaction/EC; (ii) strong orthology to biochemically/structurally solved GlgE; (iii) conservation of the exact GH13 catalytic triad (Asp391/Glu420/Asp478) in the *P. putida* sequence; (iv) a complete, operonically clustered TreS–Mak–GlgE–GlgB pathway with the M1P-supplying maltokinase adjacent to *glgE* and GlgC absent; and (v) organism-level evidence that *P. putida* makes and rapidly mobilizes α-1,4-glucan (glycogen). This is a high-confidence assignment despite the absence of a direct enzyme assay.

---

## 3. Primary Function and Substrate Specificity

- **Reaction:** α-maltose-1-phosphate + [(1→4)-α-D-glucosyl]ₙ → phosphate + [(1→4)-α-D-glucosyl]ₙ₊₂. GlgE was directly identified as "a maltosyltransferase that uses maltose 1-phosphate" (Kalscheuer et al. 2010, PMID 20305657) and formally defined as "an α-maltose 1-phosphate:(1→4)-α-d-glucan 4-α-d-maltosyltransferase of the CAZy glycoside hydrolase 13_3 family… the defining enzyme of a bacterial α-glucan biosynthetic pathway" (Syson et al. 2014, PMID 24689960).
- **Donor specificity:** α-**maltose-1-phosphate** — a phosphosugar, not ADP-/UDP-glucose. This distinguishes the GlgE route from the classical GlgC/GlgA glycogen pathway.
- **Acceptor specificity:** linear α-1,4-linked maltooligosaccharides/α-glucan. Ligand-bound structures mapped acceptor subsites +1 to +6; "the sugar residues in the acceptor subsites +1 to +5 are oriented such that they disfavor the binding of malto-oligosaccharides that bear branches at their 6-positions, consistent with the known acceptor chain specificity of GlgE" (Syson et al. 2016, PMID 27531751). GlgE therefore extends **unbranched** stretches, leaving α-1,6 branching to GlgB.

**P. putida-specific confirmation (this work).** UniProt Q88FM9 (661 aa) itself is annotated with the reaction "α-maltose 1-phosphate + [(1→4)-α-D-glucosyl]ₙ = [(1→4)-α-D-glucosyl]ₙ₊₂ + phosphate (EC 2.4.99.16)" and function "Maltosyltransferase that uses maltose 1-phosphate (M1P) as the sugar donor to elongate linear or branched alpha-(1→4)-glucans… together with TreS, Mak and GlgB," localized to a GH13 catalytic domain (residues 211–556), homodimeric. This directly ports the reaction/substrate specificity to the *P. putida* protein.

## 4. Catalytic Mechanism (evidence from structure + biochemistry)

- **α-retaining double-displacement.** GlgE "catalyzes the α-retaining transfer of maltosyl units from α-maltose 1-phosphate to maltooligosaccharides and is predicted to use a double-displacement mechanism" (Syson et al. 2014, PMID 24689960).
- **Covalent intermediate.** A trapped β-2-deoxy-2-fluoromaltosyl-enzyme intermediate and mass spectrometry showed the catalytic nucleophile is an aspartate: "The covalent modification of Asp394 was confirmed using mass spectrometry" (PMID 24689960); Glu423 acts as the general acid/base. This is classic GH13 (α-amylase clan) chemistry.
- **Two half-reactions:** (i) maltosyl transfer from M1P to the Asp nucleophile with release of inorganic phosphate; (ii) transfer of the maltosyl group to the 4-OH of the acceptor's non-reducing end, regenerating the α-anomer.
- **Catalytic residues are conserved in the P. putida enzyme (this work).** Direct inspection of Q88FM9 confirms the canonical GH13 Asp-Glu-Asp triad — **Asp391** (nucleophile, in the β4 "RVDNP" motif), **Glu420** (general acid/base, "AE" motif), and **Asp478** (transition-state stabilizer, "TPD" motif) — positionally equivalent to the experimentally validated *S. coelicolor* Asp394/Glu423. UniProt independently annotates residues 391 (nucleophile), 420 (proton donor) and 478 (transition-state stabilizer). This provides sequence-level evidence (beyond generic orthology) that the *P. putida* protein is catalytically competent with the same chemistry.

## 5. Structure and Localization

- **Quaternary/fold:** "The S. coelicolor enzyme forms a homodimer with each subunit comprising five domains, including a core catalytic α-amylase-type domain A with a (β/α)₈ fold" (Syson et al. 2011, PMID 21914799); it additionally contains an S-domain helix bundle not previously seen in GH13. High-resolution structures of *M. thermoresistibile* (1.96 Å; PMID 26616850) and *M. tuberculosis* (PMID 26245983) confirm the conserved architecture.
- **Localization: cytoplasmic (cytosolic).** "GlgE is a bacterial maltosyltransferase that catalyzes the elongation of a **cytosolic**, branched α-glucan" (Lindenberger et al. 2015, PMID 26245983); α-glucan is "exclusively assembled **intracellularly**" (Koliwer-Brandl et al. 2016, PMID 27513637). In mycobacteria a fraction of the polymer is subsequently exported to form a capsule, but the GlgE reaction itself occurs in the cytoplasm.
- **P. putida-specific localization evidence (this work).** UniProt Q88FM9 carries **no signal peptide and no transmembrane region** (features limited to catalytic Domain/Active-site/Binding-site; keywords "Carbohydrate metabolism, Glycosyltransferase, Transferase"), consistent with a **soluble cytoplasmic** enzyme — matching the cytosolic localization of characterized orthologs.

## 6. Pathway Context and Physiological Role

- **Pathway:** the four-step cytoplasmic GlgE pathway — "a new pathway from trehalose to alpha-glucan… comprising four enzymatic steps mediated by TreS, Pep2, GlgE" and GlgB (PMID 20305657). TreS interconverts trehalose ↔ α-maltose; maltose kinase Pep2/Mak makes M1P; GlgE polymerizes; GlgB branches (α-1,6). GlgE's substrate M1P is the pathway's key toxic intermediate.
- **Necessity/sufficiency:** in *S. venezuelae*, a Δ*glgE* mutant "accumulated α-maltose 1-phosphate and maltose but no α-glucan. Therefore, the GlgE pathway is necessary and sufficient for polymer biosynthesis" (Miah et al. 2016, PMID 27121970).
- **Toxic intermediate / drug-target biology (in pathogens):** in *M. tuberculosis*, GlgE inactivation causes self-poisoning through M1P accumulation and rapid death, validating GlgE as an anti-TB target (PMID 20305657). This is relevant mechanistically (explains why the M1P → polymer step is essential) but is a pathogen-specific consequence, not a role in *P. putida*.
- **Genomic pathway context in *P. putida* KT2440 (this work).** Mapping the KT2440 proteome (taxid 160488) places *glgE* (PP_4060) in a contiguous α-glucan/glycogen gene cluster: **glgA** glycogen synthase (PP_4050), **treZ** (PP_4051), **malQ** amylomaltase/4-α-glucanotransferase (PP_4052), **treY** (PP_4053), **glgX** debranching enzyme (PP_4055), **glgB** branching enzyme (PP_4058), **maltokinase treSB** (PP_4059) and **glgE** (PP_4060); **glgP** glucan phosphorylase (PP_5041) and **trehalose synthase treSA** (PP_2918) lie elsewhere. Crucially, the gene **immediately upstream of *glgE*** — maltokinase **treSB/PP_4059 (Q88FN0)** — carries the exact donor-supplying reaction **"D-maltose + ATP = α-maltose-1-phosphate + ADP + H⁺" (EC 2.7.1.175)**, i.e., the Mak/Pep2 step that feeds M1P to GlgE, plus a trehalose-synthase (maltose ↔ trehalose, EC 5.4.99.16) activity. Thus *P. putida* has a **complete, operonically clustered TreS–Mak–GlgE–GlgB pathway**, with GlgE's donor-generating enzyme encoded right next to it — strong genomic evidence the pathway operates in vivo.
- **GlgC is absent (two databases) → GlgE route is primary.** No glucose-1-phosphate adenylyltransferase / **GlgC (EC 2.7.7.27, KEGG K00975)** exists in KT2440 — confirmed independently by UniProt (gene/protein/EC search) and KEGG (org "ppu" returns no glgC gene). The resident **GlgA (PP_4050, Q88FN9)** is a *canonical* ADP-glucose–dependent glycogen synthase (EC 2.4.1.21, GT1 family) that strictly requires ADP-glucose; with GlgC absent, this classical route cannot run conventionally. Therefore the **M1P-dependent GlgE pathway is the primary α-glucan biosynthetic route** in *P. putida*. (This corrects the earlier assumption of an intact classical GlgC–GlgA route.)
- **The M1P supplier is a bifunctional TreS–maltokinase (this work).** PP_4059 (Q88FN0), immediately adjacent to *glgE*, is annotated with **both** trehalose-synthase (D-maltose ⇌ trehalose, EC 5.4.99.16) **and** maltokinase (D-maltose + ATP → α-maltose-1-phosphate + ADP, EC 2.7.1.175) activities — a fused TreS–Mak enzyme that both makes maltose from trehalose and phosphorylates it to GlgE's donor, tightly coupling substrate supply to GlgE.
- **Role in *P. putida*:** the physiological output is an intracellular **glycogen-like α-1,4/α-1,6-glucan** for **carbon/energy storage**. *P. putida* KT2440 "access[es] cellular PHA, amino acids and glycogen in few seconds under glucose starvation to obtain ATP" (Ankenbauer et al. 2020, PMID 32267616), and a P. putida polysaccharide was shown to be a "→4)-α-d-Glcp-(1→ glucan (bacterial glycogen)" (Zdorovenko et al. 2018, PMID 29304442).

---

## 7. Supported and Refuted Hypotheses

**Supported**
- H1: GlgE is a maltosyltransferase using M1P as donor (EC 2.4.99.16). ✅ (PMID 24689960, 20305657)
- H2: Mechanism is α-retaining double-displacement via a covalent maltosyl-Asp intermediate. ✅ (PMID 24689960)
- H3: GlgE extends linear α-1,4 chains; branching disfavored at acceptor site. ✅ (PMID 27531751)
- H4: Cytoplasmic homodimeric GH13 enzyme. ✅ (PMID 21914799, 26245983)
- H5: Acts in the TreS–Pep2–GlgE–GlgB trehalose→α-glucan pathway. ✅ (PMID 20305657, 27513637, 27121970)

**Refuted / not applicable**
- That GlgE uses ADP-glucose/UDP-glucose as donor — refuted; the donor is the phosphosugar M1P.
- That the *glgE* symbol is ambiguous — refuted; all identifiers converge on GlgE maltosyltransferase.
- Pathogen "self-poisoning/essentiality" is documented in mycobacteria and cannot be assumed to hold in *P. putida* (which is non-pathogenic); note, however, that *P. putida* KT2440 **lacks GlgC**, so the GlgE pathway is not obviously redundant here and may be the main α-glucan route (its essentiality/dispensability under given conditions remains to be tested experimentally).

## 8. Limitations and Future Directions

- No direct enzymatic, structural, or genetic characterization of the *P. putida* GlgE (PP_4060) protein exists; the functional assignment rests on HAMAP + orthology + conserved catalytic triad + genomic pathway completeness + organism-level glycogen physiology (all consistent).
- The M1P supply route is now genomically resolved: an adjacent maltokinase (treSB/PP_4059, EC 2.7.1.175) and a trehalose synthase (treSA/PP_2918) are present, and GlgC (EC 2.7.7.27) is absent — implying the GlgE route is primary. However, the *relative in vivo flux* and whether GlgA contributes M1P (as in mycobacteria) remain to be measured. Future work: Δ*glgE*/Δ*treSB* mutants, M1P quantification, and glycogen assays under carbon fluctuation.
- Direct proof of cytoplasmic localization and of the exact α-glucan product structure in *P. putida* (vs. inference from orthologs and a related *P. putida* strain) would require biochemical/cell-fractionation studies.

---

### Key References
- Kalscheuer et al. 2010, *Nat Chem Biol* — PMID 20305657
- Syson et al. 2011, *J Biol Chem* (first GlgE structure) — PMID 21914799
- Syson et al. 2014, *J Biol Chem* (mechanism, EC, covalent intermediate) — PMID 24689960
- Lindenberger et al. 2015 (Mtb GlgE structures, cytosolic α-glucan) — PMID 26245983
- Mendes et al. 2015 (M. thermoresistibile structure) — PMID 26616850
- Syson et al. 2016 (acceptor subsites/specificity) — PMID 27531751
- Koliwer-Brandl et al. 2016 (metabolic network, intracellular assembly) — PMID 27513637
- Miah et al. 2016 (ΔglgE necessity/sufficiency) — PMID 27121970
- Ankenbauer et al. 2020 (P. putida glycogen energy buffer) — PMID 32267616
- Zdorovenko et al. 2018 (P. putida α-glucan/glycogen) — PMID 29304442


## Artifacts

- [OpenScientist final report](glgE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](glgE-deep-research-openscientist_artifacts/final_report.pdf)