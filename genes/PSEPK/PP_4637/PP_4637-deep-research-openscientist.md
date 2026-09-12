---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.847592'
end_time: '2026-07-11T16:49:47.224187'
duration_seconds: 1805.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4637
  gene_symbol: PP_4637
  uniprot_accession: Q88E31
  protein_description: 'SubName: Full=5-methyltetrahydropteroyltriglutamate-homocysteine
    S-methyltransferase family protein {ECO:0000313|EMBL:AAN70210.1};'
  gene_info: OrderedLocusNames=PP_4637 {ECO:0000313|EMBL:AAN70210.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Cbl-indep_Met_Synth_N. (IPR013215); UROD/MetE-like_sf. (IPR038071);
    Meth_synt_1 (PF08267)
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
  path: PP_4637-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4637-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E31
- **Protein Description:** SubName: Full=5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase family protein {ECO:0000313|EMBL:AAN70210.1};
- **Gene Information:** OrderedLocusNames=PP_4637 {ECO:0000313|EMBL:AAN70210.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Cbl-indep_Met_Synth_N. (IPR013215); UROD/MetE-like_sf. (IPR038071); Meth_synt_1 (PF08267)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4637" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4637' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4637** (gene ID: PP_4637, UniProt: Q88E31) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_4637 (Q88E31) in *Pseudomonas putida* KT2440

## 1. Summary / Answer

**PP_4637 (Q88E31) is not a full methionine synthase, but the N-terminal (βα)₈-barrel subunit of a *split* cobalamin-independent methionine synthase (MetE, EC 2.1.1.14).** In *P. putida* KT2440 the two domains that make up a canonical single-chain MetE enzyme are encoded as two separate genes: **PP_4637** provides the N-terminal folate‑polyglutamate‑binding / structural barrel (Pfam PF08267, Meth_synt_1), and **PP_2698** provides the C-terminal catalytic barrel (Pfam PF01717, Meth_synt_2) that holds the active-site zinc and homocysteine. Together they catalyze the terminal step of *de novo* methionine biosynthesis — transfer of a methyl group from 5-methyl-tetrahydropteroyl-poly-γ-glutamate to L-homocysteine, yielding L-methionine — in the cytoplasm. PP_4637 itself is **non-catalytic**; its role is to bind the polyglutamylated methyl-folate donor and stabilize the catalytic loop of the PP_2698 subunit.

## 2. Identity verification (this is the correct target)

- **UniProt:** Q88E31_PSEPK; **locus:** PP_4637; **organism:** *Pseudomonas putida* KT2440 (taxid 160488). ✔ matches the requested target.
- **Length:** 274 aa — far shorter than a canonical MetE (~750 aa).
- **Domain content:** only **PF08267 (Meth_synt_1)** / InterPro **IPR013215 (Cbl-indep_Met_Synth_N)**, **IPR038071 (UROD/MetE-like_sf)**; SUPFAM SSF51726; PANTHER PTHR30519. UniProt annotates a single "Cobalamin-independent methionine synthase MetE N-terminal" domain (residues 50–232).
- **Missing:** PF01717 (Meth_synt_2), the C-terminal catalytic barrel — confirming this protein is *only* the N-terminal half.
- **Orthology:** KEGG **K00549** (EC **2.1.1.14**), COG0620, pathway ppu00270 (Cysteine and methionine metabolism).

The gene symbol/description are therefore consistent with the sequence, but the standard "5-methyltetrahydropteroyltriglutamate–homocysteine S-methyltransferase" name **over-calls** the protein: the electronic (IEA) GO/EC annotations describe the full enzyme, whereas Q88E31 is a domain fragment.

## 3. Key findings and evidence

### 3.1 PP_4637 is a truncated MetE N-terminal barrel, lacking catalytic machinery
Canonical MetE is a monomer of two face-to-face (βα)₈ barrels; the **C-terminal barrel** carries the catalytic zinc (ligands His/Cys/Cys — e.g. *A. thaliana* His647/Cys649/Cys733; *E. coli* His641/Cys643/Cys726) that binds and activates homocysteine (Pejchal & Ludwig 2005, PMID 15630480; Ferrer et al. 2004, PMID 15326182). The **N-terminal barrel arose by gene duplication of the C-terminal barrel and its ancestral binding sites are "obliterated"** (PMID 15630480). Q88E31 contains only this N-terminal barrel (PF08267) and none of the zinc/homocysteine catalytic residues — so it cannot, on its own, methylate homocysteine.

### 3.2 *P. putida* KT2440 has a *split* MetE (PP_4637 + PP_2698)
A genome-wide survey found **no single-chain ~750-aa MetE**. Instead:
- **PP_4637 / Q88E31** (274 aa, PF08267, N-terminal barrel) — KEGG K00549 / EC 2.1.1.14.
- **PP_2698 / Q88JF1** (344 aa, PF01717 "MetE C-terminal/archaeal" barrel; conserved catalytic Cys/His including a C-terminal CxxC "CTNCG" zinc motif) — also KEGG K00549 / EC 2.1.1.14.

Both are annotated as the same MetE reaction. The two loci are distant (PP_4637 ≈ 5.26 Mb; PP_2698 ≈ 3.09 Mb; not an operon), yet in the **STRING functional-association network the PP_4637–metE(PP_2698) edge is the single highest-scoring interaction of the whole methionine module (0.989)** — strong evidence that the two barrels partner to reconstitute the enzyme. PP_4637 is also tightly coupled to the rest of the sulfur/methionine module (metH, metK/SAM synthase, ahcY/SAH hydrolase, metB, metZ, hom, metG).

A **separate, cobalamin-DEPENDENT** methionine synthase, **MetH (PP_2375 / Q88KB5, 1235 aa, K00548 / EC 2.1.1.13)**, provides the B12-dependent route — so *P. putida* has both the B12-independent (split MetE) and B12-dependent (MetH) branches.

### 3.3 Genomic context, one-to-one pairing, and fold quality (corroborating evidence)
- **No fused MetE in KT2440:** the strain has exactly **one** PF08267 protein (PP_4637), exactly **one** PF01717 protein (PP_2698), and **zero** fused (both-domain) MetE proteins — so these two genes constitute the organism's entire cobalamin-independent methionine-synthase capacity. (Most other *Pseudomonas* carry a fused single-chain MetE, making KT2440's split arrangement notable.)
- **metF–metE co-localization:** PP_4637's immediate chromosomal neighbor **PP_4638 is methylenetetrahydrofolate reductase (MetF/MTHFR)** — the enzyme that *produces 5-methyl-tetrahydrofolate, the exact methyl-donor substrate of MetE*. The next gene, PP_4639, is a P-loop GTPase-dependent **zinc chaperone** (relevant to the zinc-dependent MetE reaction). This classic *metF*/*metE* juxtaposition is strong functional-context evidence.
- **Confidently folded barrel:** the AlphaFold model AF-Q88E31-F1 has **mean pLDDT 91.8** (95% of residues >70, 77% >90) across all 274 residues — a well-ordered (βα)₈ barrel, i.e. a genuine functional domain, not a decaying pseudogene fragment.
- **STRING identity confirmed:** the STRING "metE" node that partners PP_4637 (edge 0.989) resolves to locus **160488.PP_2698**, and "metH" to PP_2375.

### 3.4 Direct sequence proof of the split (each subunit = one half of a canonical MetE)
Smith–Waterman alignment (BLOSUM62) against *E. coli* MetE (P25665, 753 aa) maps the two *P. putida* proteins to **non-overlapping halves** of one canonical MetE:
- **PP_4637 → E. coli MetE residues 134–335** (its own residues 51–255), score 454, **47% identity over 202 residues** — the **N-terminal barrel**.
- **PP_2698 → E. coli MetE residues 427–631** (its own residues 6–210), score 260, **33% identity over 204 residues** — the **C-terminal catalytic barrel**.

Both retain the barrel-diagnostic DExP motif (PP_4637 'VQIDEP'; PP_2698 'IQFDEP'). This is direct, quantitative evidence — beyond family-level annotation — that KT2440's MetE is a genuine split of the canonical two-barrel enzyme.

### 3.5 Precise role, localization, and pathway
- **Reaction (reconstituted enzyme):** 5-methyl-H₄-pteroyl-poly-γ-glutamate + L-homocysteine → L-methionine + H₄-pteroyl-poly-γ-glutamate (EC 2.1.1.14); no intermediate methyl carrier, cobalamin-independent.
- **PP_4637's specific contribution:** the N-terminal barrel **binds the poly-γ-glutamate tail of the methyl-folate substrate and stabilizes the catalytic (folate-binding) loop of the C-terminal domain** ("a structural role of the N-terminal domain … in the stabilization of loop 507–529 and in the interaction with the poly-glutamate chain of CH₃-H₄PteGluₙ" — PMID 15326182). Catalysis (methyl transfer, zinc-activated thiolate) occurs on the **C-terminal (PP_2698) subunit**.
- **Substrate specificity note:** MetE strongly prefers **polyglutamylated** methyl-tetrahydrofolate; the N-terminal barrel is a key determinant of that polyglutamate preference.
- **Localization:** cytoplasmic — Q88E31 is a soluble 274-aa protein with no signal peptide or transmembrane segment, consistent with the cytosolic MetE family.
- **Pathway:** final step of **de novo L-methionine biosynthesis** within sulfur assimilation; methionine feeds **S-adenosylmethionine (SAM)** synthesis (metK) and one-carbon/folate cycling (regenerated tetrahydrofolate; SAH recycled via ahcY).

## 4. Hypotheses — supported and refuted

**Supported**
- PP_4637 is the N-terminal barrel of MetE (domain, orthology, structure). ✔
- *P. putida* KT2440 uses a two-gene (split) MetE; PP_4637 partners with the PP_2698 catalytic subunit (STRING top edge 0.989; shared K00549). ✔
- PP_4637 acts in the cytoplasm in methionine/SAM biosynthesis. ✔ (family localization + module context)

**Refuted / corrected**
- PP_4637 is a standalone, catalytically complete 5-methyl-THF-triglutamate–homocysteine methyltransferase. ✗ Refuted — it lacks the entire C-terminal catalytic barrel and the zinc/homocysteine site; the database EC/GO calls reflect family membership, not verified activity of this fragment.

## 5. Limitations and future directions
- Evidence is bioinformatic/structural-homology based; there is **no direct biochemical or genetic study of PP_4637 itself**. No PubMed literature exists for this specific *P. putida* protein.
- Direct physical association of PP_4637 with PP_2698 is inferred from STRING co-occurrence/context, not demonstrated experimentally. Whether the two barrels form a stable heterocomplex, or whether PP_2698 functions as an autonomous "archaeal-type" C-terminal-only synthase with PP_4637 as an auxiliary folate-binding factor, remains to be tested.
- **Suggested experiments:** (i) ΔPP_4637 and ΔPP_2698 growth phenotypes on minimal medium ± methionine ± vitamin B12 (to test whether the split MetE is the sole B12-independent route); (ii) co-purification / pull-down of PP_4637 with PP_2698; (iii) in vitro reconstitution of EC 2.1.1.14 activity from the two subunits with mono- vs poly-glutamate methyl-folate; (iv) AlphaFold-Multimer modeling of the PP_4637:PP_2698 heterodimer to confirm the face-to-face double-barrel interface.

## 6. Primary references
- Pejchal R, Ludwig ML (2005) *Cobalamin-independent methionine synthase (MetE): a face-to-face double barrel that evolved by gene duplication.* PLoS Biol. PMID **15630480**.
- Ferrer J-L, Ravanel S, Robert M, Dumas R (2004) *Crystal structures of cobalamin-independent methionine synthase complexed with zinc, homocysteine, and methyltetrahydrofolate.* J Biol Chem. PMID **15326182**.
- Fu T-M et al. (2011) *Crystal structures of cobalamin-independent methionine synthase (MetE) from Streptococcus mutans: a dynamic zinc-inversion model.* PMID **21840320**.
- Database sources: UniProt Q88E31 / Q88JF1 / Q88KB5; KEGG ppu:PP_4637, PP_2698, PP_2375; Pfam PF08267/PF01717; InterPro IPR013215/IPR038071; STRING (taxid 160488).


## Artifacts

- [OpenScientist final report](PP_4637-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4637-deep-research-openscientist_artifacts/final_report.pdf)