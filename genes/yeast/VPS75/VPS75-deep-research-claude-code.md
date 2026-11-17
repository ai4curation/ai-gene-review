---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-17T06:43:41.908996'
end_time: '2026-11-17T06:45:13.887605'
duration_seconds: 91.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: VPS75
  gene_symbol: VPS75
  uniprot_accession: P53853
  protein_description: 'RecName: Full=Vacuolar protein sorting-associated protein
    75;'
  gene_info: Name=VPS75; OrderedLocusNames=YNL246W; ORFNames=N0890;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the nucleosome assembly protein (NAP) family.
  protein_domains: NAP. (IPR002164); NAP-like_sf. (IPR037231); NAP (PF00956)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 8
  total_cost_usd: 0.8863132
  session_id: d31a778c-ecc5-474d-b449-82aa3a0de791
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P53853
- **Protein Description:** RecName: Full=Vacuolar protein sorting-associated protein 75;
- **Gene Information:** Name=VPS75; OrderedLocusNames=YNL246W; ORFNames=N0890;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the nucleosome assembly protein (NAP) family.
- **Key Domains:** NAP. (IPR002164); NAP-like_sf. (IPR037231); NAP (PF00956)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VPS75" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VPS75' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VPS75** (gene ID: VPS75, UniProt: P53853) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I've checked the local UniProt and GOA records and two web searches. Writing up the report now.

# VPS75 (YNL246W, UniProt P53853): research report

## 0. Identity check

- **Symbol and protein match.** VPS75 is the standard SGD name for ORF YNL246W in *S. cerevisiae* S288c, and UniProt P53853 is "Vacuolar protein sorting-associated protein 75" in the NAP family (Pfam PF00956, InterPro IPR002164). All the literature below is on this budding-yeast protein.
- **The name is misleading.** It comes from a genome-wide screen for vacuolar protein sorting (*vps*) mutants [PMID:12134085, Bonangelino et al. 2002, *Mol Biol Cell*, "Genomic screen for vacuolar protein sorting genes in *Saccharomyces cerevisiae*"]. All later work shows that Vps75 is a nuclear histone chaperone. No study shows a direct role in vacuolar sorting.
- **Search scope.** I did not find dedicated Vps75 papers from 2023–2024. The main body of work dates from 2007 to 2019. GOA also lists a protein-binding IPI from a 2023 paper (PMID:37968396) that I did not read.

## 1. Summary

Vps75 is a homodimeric histone chaperone in the NAP family. It forms a stable complex with the fungal lysine acetyltransferase Rtt109 and works as Rtt109's activating cofactor.

- **Activation.** In the Rtt109–Vps75 complex, a Vps75 dimer binds two Rtt109 subunits. Vps75 raises Rtt109's catalytic rate (kcat) on histone H3 by about 100-fold.
- **Site specificity.** Vps75 steers acetylation toward the N-terminal tail of H3, mainly K9, and also K23 and K27.
- **Division of labour with Asf1.** The other Rtt109 chaperone, Asf1, steers acetylation to K56 in the H3 core.
- **Chaperone activity.** Vps75 binds H3–H4 dimers and tetramers through H3. In vitro it assembles nucleosomes and can move H3–H4 between tetramers and Asf1-bound complexes.
- **Location.** It acts in the nucleus, on chromatin.
- **Rtt109-independent role.** Vps75 also supports histone exchange during transcription. This is linked to RNA polymerase II (RNAPII) and the RSC remodeller.
- **DNA repair.** Genetic data link it to repair of double-strand breaks by non-homologous end joining (NHEJ).

## 2. Molecular function

### 2.1 Activating cofactor for Rtt109 (core function)

Vps75 is not an enzyme. Its main function is to activate and target the histone acetyltransferase Rtt109.

- **Discovery of the complex (2007).** Two groups showed that Rtt109 acetylates H3K56 and co-purifies with Vps75. They also showed that histone chaperones, either Asf1 or Vps75, stimulate this activity [PMID:17320445, Tsubota et al. 2007, *Mol Cell*, "Histone H3-K56 acetylation is catalyzed by histone chaperone-dependent complexes"; PMID:17272723, Driscoll et al. 2007, *Science*, "Rtt109 acetylates histone H3 lysine 56 and functions in DNA replication"]. Further 2007 work confirmed a stable Rtt109–Vps75 complex (PMID:17314980; PMID:18723682, the latter a 2008 paper; both cited as IntAct rows in GOA).
- **Size of the effect.** Vps75 raises the kcat of Rtt109 histone acetylation about 100-fold and increases acetylation at H3K9 [PMID:19172748, Berndsen et al. 2008, *Nat Struct Mol Biol*, "Molecular functions of the histone acetyltransferase chaperone complex Rtt109-Vps75"; https://www.nature.com/articles/nsmb.1459].
- **Kinetics.** Kinetic work describes how the complex binds acetyl-CoA and histone substrate [PMID:20560668, *Biochemistry* 2010, "Kinetic mechanism of the Rtt109-Vps75 histone acetyltransferase-chaperone complex"].
- **Site specificity in cells.**
  - Loss of *vps75* lowers H3K9ac and H3K23ac [PMID:19172748].
  - Loss of both *vps75* and *gcn5* abolishes H3K9ac and H3K27ac [PMID:21256037, Tang et al. 2011, *Structure*].
  - Vps75 is needed for H3K9/K27 acetylation but not for H3K56; Asf1 is needed for H3K56 [PMID:21256037; PMID:29300933, Zhang et al. 2018, *NAR*, "Structural characterization of the Asf1-Rtt109 interaction and its role in histone acetylation"].
  - Fillingham et al. 2008 (*Mol Cell Biol*, "Chaperone control of the activity and specificity of the histone H3 acetyltransferase Rtt109") showed the same two-chaperone split. I recall this paper but did not verify its PMID here.
  - UniProt summarises the role this way: "Preferentially stimulates histone H3 'Lys-9' acetylation by RTT109 … May also stimulate histone H3 'Lys-56' acetylation" (P53853, CC FUNCTION, ECO:0000269).
- **Autoregulation.** Rtt109 autoacetylation and Vps75 binding together shape the enzyme's activity [PMID:18719104, Albaugh et al. 2008, *PNAS*, "Molecular basis for the autoregulation of the protein acetyl transferase Rtt109"].
- **Relevant GO terms.**
  - GO:0010698 *acetyltransferase activator activity*: IDA and IMP rows from PMID:19172748, 19172749, 21256037. This best captures the core function.
  - GO:0070775 *H3 histone acetyltransferase complex*: rows from PMID:21256037, 31387991, 31194870, 20560668.

### 2.2 Histone H3–H4 chaperone activity

- **Binding.** Vps75 binds H3/H4 dimers and tetramers through H3 (UniProt SUBUNIT; PMID:21454705; PMID:27036862; PMID:31387991). SGD records histone-binding IPIs with H3 and H4 gene products [PMID:17344218, Selth & Svejstrup 2007, *J Biol Chem*, "Vps75, a new yeast member of the NAP histone chaperone family"].
- **Nucleosome assembly.** In vitro, Vps75 assembles nucleosomes (PMID:17344218; PMID:19172748).
- **Oligomers and histone exchange.** Vps75 forms dimers and also tetramers. These can move histones between H3–H4 tetramers and Asf1–H3–H4 complexes, consistent with handing histones between chaperones [PMID:27036862, Hammond et al. 2016, *NAR*, PDB 5AGC].
- **GO terms.** GO:0000510 *H3-H4 histone complex chaperone activity* (IDA, PMID:21329878) and GO:0042393 *histone binding* are both well supported.

### 2.3 Structure

- **Fold.** Vps75 has the NAP fold: a long dimerisation helix, an "earmuff" β-domain, and acidic regions. Crystal structures exist for Vps75 alone and with Rtt109 (PDB 3C9B/3C9D, PMID:19172748).
- **Complex shape.** In the Rtt109–Vps75 complex (PDB 3Q66/3Q68, PMID:21454705; 3Q33/3Q35, PMID:21256037), two Rtt109 molecules sit on one Vps75 dimer. They form a ring-like assembly with the Rtt109 active sites facing a central cavity.
- **Asf1–H3:H4–Rtt109–Vps75 model.** One Vps75 subunit holds Rtt109 while the other binds the Asf1–H3:H4 substrate. Together they form a doughnut-like structure with a ~25 Å cavity lined by the catalytic site [PMID:31387991, Danilenko et al. 2019, *Nat Commun*, "Histone chaperone exploits intrinsic disorder to switch acetylation specificity", PDB 6O22; https://pmc.ncbi.nlm.nih.gov/articles/PMC6684614].
- **How specificity switches to H3K9.** Vps75's disordered C-terminal acidic tail binds the H3 N-terminus. This positions the H3 tail, rather than the K56-bearing core, in the Rtt109 active site and favours H3K9ac (UniProt DOMAIN, PMID:31387991).
- **In other fungi.** In *Pneumocystis carinii*, Vps75 dimers may control H3K9/K27 acetylation by binding (H3–H4)2 tetramers directly, rather than by forming a stable Vps75–Rtt109 complex. This suggests the mechanism differs between fungi (https://pmc.ncbi.nlm.nih.gov/articles/PMC6103222).

## 3. Biological processes

1. **Chromatin assembly linked to DNA replication.** Vps75 delivers or presents newly made H3–H4 for acetylation by Rtt109. GOA has IDA/IMP rows for GO:0006335 *DNA replication-dependent chromatin assembly* (PMID:19172748, 21256037). The replication link is stronger for Rtt109 and Asf1 through H3K56ac. Vps75's own contribution is more modest and centres on H3 tail acetylation.
2. **Histone exchange during transcription, independent of Rtt109.**
   - In genetic interaction profiles, *VPS75* clusters with transcription regulators, while *RTT109* clusters with replication and repair genes.
   - Vps75 is recruited to activated genes without needing Rtt109, and its genome-wide occupancy tracks transcription rate.
   - It is functionally and physically linked to RNAPII.
   - In a reconstituted system, Vps75 and RSC together remove H2A/H2B dimers from nucleosomes.

   Source: Selth et al. 2009, *Mol Cell Biol*, "An Rtt109-independent role for Vps75 in transcription-associated nucleosome dynamics" (https://pmc.ncbi.nlm.nih.gov/articles/PMC2715805). Later work found that Vps75 and Rtt109 together limit cryptic transcription in a Ctk1-dependent setting. So Vps75 acts in transcription both on its own and with Rtt109 (https://pmc.ncbi.nlm.nih.gov/articles/PMC3624251).
3. **DSB repair by NHEJ.** *rtt109Δ* and *vps75Δ* mutants rejoin breaks less efficiently in plasmid-repair assays [PMID:18036332, Jessulat et al. 2008, *J Biol Chem*; GOA GO:0006303, IMP/IPI]. The effect is probably indirect, through chromatin state, so this is best treated as a non-core process.
4. **Vacuolar protein sorting.** This comes only from the high-throughput mutant screen (PMID:12134085) and is almost certainly an indirect effect. GOA has no vacuolar-sorting annotation.

## 4. Where it acts in the cell

- **Nucleus:** shown by GFP localisation [PMID:14562095, Huh et al. 2003, *Nature*] and by IDA (PMID:22932476).
- **Chromatin:** shown by ChIP and chromatin association (PMID:17344218; PMID:21463458), and Vps75 is recruited to transcribed genes (Selth et al. 2009).
- **Cytosol:** an IDA row exists (PMID:22932476). This probably reflects a pool that binds newly made histones or Rtt109 before nuclear import. It is minor compared with the nuclear location.
- **Abundance:** about 3,120 molecules per cell in log phase [PMID:14562106].

## 5. Evolution and bioinformatics

- **Family.** Vps75 belongs to the NAP family (IPR002164) alongside yeast Nap1 and the human NAP1L and SET/TAF-Iβ proteins.
- **Fungal-specific partner.** The Vps75–Rtt109 partnership is specific to fungi; Rtt109 itself is a fungal acetyltransferase related to p300/CBP. This makes the complex a candidate antifungal target (UniProt FUNCTION, structural literature).
- **IBA rows.** The PANTHER IBA rows (nucleus, chromatin, histone binding, chromatin binding; node PTN000221934) follow from general NAP-family traits. They agree with the direct evidence.

## 6. Notes for annotation review

- **Core MF:** GO:0010698 acetyltransferase activator activity, GO:0000510 H3-H4 histone complex chaperone activity, and GO:0042393 histone binding.
- **Core CC:** nucleus, chromatin, and GO:0070775 H3 histone acetyltransferase complex (the Rtt109–Vps75 complex).
- **Core BP:** nucleosome assembly and chromatin organization. DNA replication-dependent chromatin assembly is supported but weaker for Vps75 than for Asf1.
- **Non-core BP:** NHEJ.
- **Not annotated in GOA:** Rtt109-independent histone exchange during transcription (Selth et al. 2009) could be a candidate new process annotation.
- **Low-information MF:** bare *protein binding* (GO:0005515) rows with Rtt109 and with Vps75 itself add nothing. *Identical protein binding* reflects homodimerisation.

## Sources

- UniProt P53853 (local file `genes/yeast/VPS75/VPS75-uniprot.txt`) and GOA file `genes/yeast/VPS75/VPS75-goa.tsv`
- Selth et al. 2009, MCB: https://pmc.ncbi.nlm.nih.gov/articles/PMC2715805 ; SGD reference: https://www.yeastgenome.org/reference/S000135151 ; BioGRID: https://thebiogrid.org/115343/publication/an-rtt109-independent-role-for-vps75-in-transcription-associated-nucleosome-dynamics.html
- Vps75/Rtt109 in cryptic transcription: https://pmc.ncbi.nlm.nih.gov/articles/PMC3624251
- Berndsen et al. 2008, NSMB: https://www.nature.com/articles/nsmb.1459 ; https://www.osti.gov/biblio/1007143
- Danilenko et al. 2019, Nat Commun: https://pmc.ncbi.nlm.nih.gov/articles/PMC6684614
- Tang et al. 2011, Structure (BioGRID): https://thebiogrid.org/112665/publication/structure-of-the-rtt109-accoavps75-complex-and-implications-for-chaperone-mediated-histone-acetylation.html ; Proteopedia 3Q33: https://proteopedia.org/w/3q33
- Su et al. 2011, JBC: https://ouci.dntb.gov.ua/works/4YMX12P4
- *Pneumocystis* Vps75: https://pmc.ncbi.nlm.nih.gov/articles/PMC6103222
- Other search hits: https://pmc.ncbi.nlm.nih.gov/articles/PMC5291247 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6509256 ; https://repository.escholarship.umassmed.edu/entities/publication/563fa894-9d4f-4b15-827e-95c6aad207c1 ; https://www.omicsdi.org/dataset/biostudies-literature/S-EPMC2715805 ; https://www.omicsdi.org/dataset/geo/GSE15607 ; https://www.yeastgenome.org/reference/23401858 ; https://web4.library.adelaide.edu.au/dspace/handle/2440/65896 ; https://digital.library.adelaide.edu.au/items/33d0e8b7-ff84-4bc5-b1b0-33e7f5599b27 ; https://researchnow.flinders.edu.au/en/publications/an-rtt109-independent-role-for-vps75-in-transcription-associated-/

## Citations

1. https://www.nature.com/articles/nsmb.1459
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6684614
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC6103222
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC2715805
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC3624251
6. https://www.yeastgenome.org/reference/S000135151
7. https://thebiogrid.org/115343/publication/an-rtt109-independent-role-for-vps75-in-transcription-associated-nucleosome-dynamics.html
8. https://www.osti.gov/biblio/1007143
9. https://thebiogrid.org/112665/publication/structure-of-the-rtt109-accoavps75-complex-and-implications-for-chaperone-mediated-histone-acetylation.html
10. https://proteopedia.org/w/3q33
11. https://ouci.dntb.gov.ua/works/4YMX12P4
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC5291247
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC6509256
14. https://repository.escholarship.umassmed.edu/entities/publication/563fa894-9d4f-4b15-827e-95c6aad207c1
15. https://www.omicsdi.org/dataset/biostudies-literature/S-EPMC2715805
16. https://www.omicsdi.org/dataset/geo/GSE15607
17. https://www.yeastgenome.org/reference/23401858
18. https://web4.library.adelaide.edu.au/dspace/handle/2440/65896
19. https://digital.library.adelaide.edu.au/items/33d0e8b7-ff84-4bc5-b1b0-33e7f5599b27
20. https://researchnow.flinders.edu.au/en/publications/an-rtt109-independent-role-for-vps75-in-transcription-associated-/