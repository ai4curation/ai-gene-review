---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-15T06:58:57.379211'
end_time: '2026-11-15T07:00:57.584243'
duration_seconds: 120.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: HAT1
  gene_symbol: HAT1
  uniprot_accession: Q12341
  protein_description: 'RecName: Full=Histone acetyltransferase type B catalytic subunit;
    EC=2.3.1.48 {ECO:0000269|PubMed:24835250};'
  gene_info: Name=HAT1; OrderedLocusNames=YPL001W; ORFNames=LPA16W, YP8132.12;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the HAT1 family. .
  protein_domains: Acyl_CoA_acyltransferase. (IPR016181); GNAT_dom. (IPR000182); Hat1_N.
    (IPR019467); Hat1_N_sf. (IPR037113); Hist_AcTrfase_B-typ_cat-su. (IPR017380)
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
  - claude-fable-5-2
  - claude-haiku-5-5
  web_search_requests: 7
  num_turns: 11
  total_cost_usd: 1.8422939
  session_id: 1e1f019d-abca-4664-b9e4-8c0e2f9ff6b4
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q12341
- **Protein Description:** RecName: Full=Histone acetyltransferase type B catalytic subunit; EC=2.3.1.48 {ECO:0000269|PubMed:24835250};
- **Gene Information:** Name=HAT1; OrderedLocusNames=YPL001W; ORFNames=LPA16W, YP8132.12;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the HAT1 family. .
- **Key Domains:** Acyl_CoA_acyltransferase. (IPR016181); GNAT_dom. (IPR000182); Hat1_N. (IPR019467); Hat1_N_sf. (IPR037113); Hist_AcTrfase_B-typ_cat-su. (IPR017380)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HAT1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HAT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HAT1** (gene ID: HAT1, UniProt: Q12341) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# HAT1 (YPL001W; UniProt Q12341) in *Saccharomyces cerevisiae*: Research Report for Functional Annotation

## 0. Identity verification

The gene symbol, organism and protein family all match the target; no ambiguity was found.

- **Symbol and protein:** *S. cerevisiae* HAT1 (YPL001W, also called KAT1) encodes the catalytic subunit of the type B histone acetyltransferase, EC 2.3.1.48, matching UniProt Q12341.
- **Family and domains:** The literature describes a GNAT-fold acetyltransferase with a Hat1-specific N-terminal domain, consistent with IPR000182, IPR016181, IPR019467 and IPR017380.
- **Orthologs:** Human HAT1 (KAT1) is the ortholog. Human and mouse findings are marked as such below and should not be transferred uncritically.

**Provenance note.** I verified the claims by web search in this session (mostly abstracts and search excerpts, not full text) and against the UniProt record in the repository. Items in sections 2–8 marked "(recalled)" come from my memory of the literature and were not re-checked. PMIDs are those in the UniProt record or returned by search.

---

## 1. Summary

Hat1 is the founding type B histone acetyltransferase. It transfers an acetyl group from acetyl-CoA to the ε-amino group of lysine 12 (and, as a minor site, lysine 5) on the N-terminal tail of newly synthesized, non-nucleosomal histone H4. It does not acetylate nucleosomal H4.

Hat1 works as an obligate partner of the WD40 histone chaperone Hat2 (the HAT-B complex). In the nucleus the two join the H3–H4 chaperone Hif1 to form the NuB4 complex, which hands acetylated H3–H4 to Asf1 for chromatin assembly.

The best-supported biological roles are:

- acetylation of new H4 before deposition;
- chromatin reassembly linked to recombinational repair of DNA double-strand breaks;
- telomeric silencing, a role that is redundant with the histone H3 N-terminal tail.

Hat1 is found in both cytoplasm and nucleus, and later work shows it is predominantly nuclear.

---

## 2. Molecular function

### 2.1 Reaction catalyzed

acetyl-CoA + L-lysyl-[histone H4] → CoA + H⁺ + N⁶-acetyl-L-lysyl-[histone H4] (EC 2.3.1.48; RHEA:45948). UniProt assigns the catalytic activity with experimental evidence from PMID:24835250.

### 2.2 Discovery and substrate specificity

- **Gene identification (Kleff et al., 1995, *J Biol Chem*; PMID:7559580).** HAT1 was the first histone acetyltransferase gene identified, as a yeast histone H4 acetyltransferase. Deleting it gave no obvious growth phenotype (recalled).
- **Native enzyme (Parthun, Widom & Gottschling, 1996, *Cell*; PMID:8858151).** The major cytoplasmic histone acetyltransferase in yeast was purified as a Hat1–Hat2 complex. Hat2 is the yeast homolog of mammalian RbAp46/48. Hat2 strengthens binding to H4 and raises specific activity about 10-fold, and the native enzyme is specific for H4 K12 (recalled).
- **Free versus nucleosomal histone (Ruiz-García et al., 1998, *J Biol Chem*; PMID:9575221).** The Hat1/Hat2 enzyme is specific for free histone H4, the defining property of a type B enzyme. This paper already described the enzyme as nuclear.
- **Site preference.** Current work treats K12 as the primary site and K5 as a minor one. The 2022 structural study states that "H4K5 is a minor Hat1–Hat2 site" and used an H4 truncation to focus on K12 ([Yue et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401)). The HAT1-dependent rise in H4 acetylation at a DNA break is confined to K12 (Qin & Parthun, 2006; PMID:16612003).
- **Recognition motif.** UniProt records an intrinsic specificity for lysine in the sequence G-X-G-K-X-G, which matches the sequence around H4 K12 (and K5).
- **H2A.** Recombinant Hat1 was reported to acetylate H2A weakly in vitro (recalled). No in vivo relevance has been established; this should be treated as a promiscuous in vitro activity.

The K5/K12 diacetylation pattern on newly made H4 is among the most conserved histone modifications in eukaryotes, yet its essential function is still unresolved ([Haigney et al., 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284); [Yue et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401)).

### 2.3 Structure and mechanism

- **Hat1 alone (Dutnall et al., 1998, *Cell*; PMID:9727486).** The crystal structure of Hat1 bound to acetyl-CoA was the first histone acetyltransferase structure and became the paradigm for the GCN5-related N-acetyltransferase (GNAT) superfamily. It was solved on a C-terminally truncated fragment at 2.3 Å (recalled). UniProt maps acetyl-CoA binding to residues 220–222 and 227–233.
- **Hat1/Hat2 with substrates (Li et al., 2014, *Genes Dev*; PMID:24835250; PDB 4PSW, 4PSX).** A 2.0 Å structure of Hat1p/Hat2p/CoA/H4 peptide shows the H4 tail contacting both subunits. The H3 N-terminal tail binds the Hat2 WD40 domain, and this requires unmodified Arg2/Lys4 and Lys9. That explains selectivity for newly synthesized H3–H4 ([abstract](https://genesdev.cshlp.org/content/28/11/1217.abstract)).
- **Hat1–Hat2 with Asf1–H3–H4 (Yue et al., 2022, *Genes Dev*).** A 3.3 Å structure with CoA shows one copy of each protein. The H3 and H4 core domains contact Hat1 and Hat2, and the H4 N-terminal helix binds Hat2 in a new mode ([PMC9067401](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401)).
- **Catalytic residue: conflicting evidence.** UniProt annotates an active site at residue 255, and Glu255 was proposed as the catalytic base. Mersfelder & Parthun (2008; PMID:18753131) found that neither Glu255 nor other nearby acidic residues is essential for activity. They concluded that Hat1p, unlike most histone acetyltransferases, does not use an acidic residue as its catalytic base ([PMC2570870](https://pmc.ncbi.nlm.nih.gov/articles/PMC2570870)).

---

## 3. Complexes and partners

| Complex | Composition | Location | Evidence |
|---|---|---|---|
| HAT-B | Hat1 + Hat2 | Cytoplasm and nucleus | PMID:8858151, PMID:9575221 |
| NuB4 | Hat1 + Hat2 + Hif1 | Nucleus | PMID:14761951, PMID:15099519 |
| HAT-B/NuB4 with Asf1 | Bridged by H3–H4 | Nucleus | [Haigney 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284); [Yue 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401) |

- **Hat2** is a WD40-repeat histone chaperone, the yeast homolog of RbAp46/48. It bridges Hat1 to Hif1.
- **Hif1** is an H3–H4 chaperone of the NASP/N1 family. It was identified independently by two groups as a nuclear Hat1/Hat2 partner (Poveda et al., 2004, PMID:14761951; Ai & Parthun, 2004, PMID:15099519). Hif1 binds Hat2 directly, and the three subunits are roughly stoichiometric in NuB4.
- **Asf1** does not bind HAT-B on its own. It associates only through shared contacts with H3–H4 ([Haigney et al., 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284)).
- **Open question:** how NuB4 transfers H3–H4 to Asf1 is still unknown ([Yue et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401)). My search found no published structure of the full Hif1-containing NuB4 complex.

---

## 4. Subcellular localization

- **Original view: cytoplasm.** Hat1–Hat2 was purified as the major cytoplasmic histone acetyltransferase (PMID:8858151), which fits acetylation of H4 soon after synthesis.
- **Revised view: mainly nucleus.** Poveda et al. (2004) titled their paper "a complex mainly localized in the nucleus" (PMID:14761951). Mersfelder & Parthun (2008) found Hat1p to be a predominantly nuclear protein ([PMC2570870](https://pmc.ncbi.nlm.nih.gov/articles/PMC2570870)).
- **Where the function is needed.** Keeping Hat1p out of the nucleus caused telomeric silencing defects similar to a deletion. Catalytically active Hat1p in the cytoplasm was not sufficient for normal silencing (PMID:18753131).
- **Chromatin.** Hat1p and Hif1p are recruited to a small chromatin domain around an HO-induced double-strand break (PMID:16612003).

In short, Hat1 shuttles with its H3–H4 cargo: it can act on soluble H4 in the cytoplasm, but its demonstrated phenotypic roles require nuclear localization.

---

## 5. Biological processes

### 5.1 Acetylation of newly synthesized histones and chromatin assembly

This is the primary role. Hat1 marks new H4, held in an H3–H4 dimer, on K12 and K5 before deposition. The histones then pass through NuB4 to Asf1 and on to assembly factors. Hif1 has chromatin assembly activity in vitro, linking type B acetyltransferases to assembly (Ai & Parthun, 2004; PMID:15099519). The marks are removed after deposition during chromatin maturation ([Capone et al., 2023 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137880)).

Hat1 is not essential in yeast, and hat1Δ alone has little phenotype. This implies redundancy with other acetylation of new histones, notably on the H3 tail.

### 5.2 DNA double-strand break repair

- **Genetic evidence (Qin & Parthun, 2002; PMID:12417736).** Combining hat1Δ with H3 N-terminal lysine substitutions causes DNA damage sensitivity and a defect in recombinational repair of a double-strand break. The authors proposed this acts through Asf1-dependent chromatin assembly.
- **Recruitment (Qin & Parthun, 2006; PMID:16612003).** Hat1p arrives at an HO break after H2A S129 phosphorylation and together with Rad52p. It is recruited even in strains that cannot repair the break. Acetylation of all four H4 tail lysines rises during repair, but only the K12 rise depends on HAT1.
- **Reassembly (Ge, Wang & Parthun, 2011, *J Biol Chem* 286:16790; PMID:21454479).** Deleting HAT1 causes a significant defect in chromatin reassembly after repair. Hif1p plays a larger role than Hat1p or Hat2p, and the Hat1p and Hif1p roles are partly redundant with Asf1p ([PMC3089522](https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522)).

The mechanistic reading is that Hat1 contributes to repair by supplying acetylated histones for chromatin restoration, not by acting in the repair reaction itself.

### 5.3 Telomeric silencing

- **Kelly et al., 2000 (*Mol Cell Biol*; PMID:10982821).** hat1Δ on its own does not disturb silencing. Combined with H3 N-terminal lysine substitutions it causes loss of telomeric silencing. An H4 K12 substitution reproduces the effect, pointing to K12 acetylation as the relevant event (details recalled; UniProt states that H4 K12 acetylation is required for telomeric silencing).
- **Mersfelder & Parthun, 2008 (PMID:18753131).** Both catalytic activity and nuclear localization are required for this role.

This is a synthetic, redundancy-dependent phenotype, most likely a downstream consequence of histone supply and assembly at telomeres, not a dedicated silencing mechanism.

---

## 6. Recent developments (2022–2024)

- **Structural (2022).** The Hat1–Hat2–Asf1–H3–H4 structure gives the first view of the enzyme engaged with a folded H3–H4 dimer and a downstream chaperone ([Yue et al., 2022](https://genesdev.cshlp.org/content/36/7-8/408.full)).
- **Review (2023).** Capone et al., "Understanding HAT1: A Comprehensive Review of Noncanonical Roles and Connection with Disease" (*Genes* 14:915), covers canonical and noncanonical roles, largely in mammals ([PMC10137880](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137880)).
- **Mammalian context, not yeast.** Human HAT1 pairs with RbAp46 and passes H3–H4 to Asf1. It is described as mainly active in S phase. Mammalian studies report additional roles, including links to cancer. None of these should be assumed for yeast Hat1 without yeast evidence.
- I did not find a 2023–2024 primary paper specifically on *S. cerevisiae* Hat1. The search was limited, so this is not proof that none exists.

---

## 7. Notes for GO annotation review

These are my judgments based on the evidence above, set against the GO terms listed in the UniProt record.

| Term in UniProt record | Assessment |
|---|---|
| Histone H4 acetyltransferase activity (GO:0010485, IBA) | Core function; strongly supported. A K12-specific child term, if one exists, would be more precise. |
| Histone acetyltransferase activity (GO:0004402, IDA) | Correct but general; the evidence supports H4 specificity. |
| Protein-lysine-acetyltransferase activity (GO:0061733, EXP) | Correct but more general still. |
| Histone acetyltransferase complex (GO:0000123, IDA) | Supported (HAT-B and NuB4). |
| Nucleus (GO:0005634, IDA) | Well supported; the site where function is required. |
| Cytoplasm (GO:0005737, IDA) | Supported by purification of the native enzyme. |
| Double-strand break repair (GO:0006302, IDA) | Supported, though the role is in repair-linked chromatin reassembly and is redundant with the H3 tail. |
| Subtelomeric heterochromatin formation (GO:0031509, IDA) | Supported by synthetic genetics; probably non-core. |
| Chromatin binding (GO:0003682, IDA) | Consistent with recruitment at break sites (ChIP). |
| Histone binding (GO:0042393, IEA) | Plausible; structures show direct H4 tail contacts. |
| Chromosome, telomeric region (GO:0000781, IEA) | Weakest; I found no direct evidence of telomere localization. |

Two source-record points are worth checking: the UniProt active-site annotation at residue 255 conflicts with the mutagenesis in PMID:18753131, and the UniProt function text emphasizes cytoplasmic action although later work shows the protein is predominantly nuclear.

---

## 8. Open questions

- What is the essential function of H4 K5/K12 acetylation, given that hat1Δ cells are viable and largely normal?
- How does NuB4 hand H3–H4 to Asf1, and what does the Hif1-containing complex look like?
- What is the true catalytic mechanism, if no acidic residue serves as the general base?
- Does Hat1 acetylate H4 in the cytoplasm, the nucleus, or both under normal conditions?

---

## Sources

- [Yue et al., 2022, Topography of histone H3–H4 interaction with the Hat1–Hat2 acetyltransferase complex (PMC9067401)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401) and [Genes & Development](https://genesdev.cshlp.org/content/36/7-8/408.full)
- [Haigney et al., 2015, Dissecting the molecular roles of histone chaperones in histone acetylation by type B HATs (PMC4683284)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284)
- [Li et al., 2014, Hat2p recognizes the histone H3 tail… (Genes Dev abstract; PMID:24835250)](https://genesdev.cshlp.org/content/28/11/1217.abstract), [PMC4052767](https://pmc.ncbi.nlm.nih.gov/articles/PMC4052767), [PDB 4PSW](https://rcsb.org/structure/4PSW), [PDB 4PSX](https://rcsb.org/structure/4psx)
- [Ge, Wang & Parthun, 2011, Nuclear Hat1p complex (NuB4) components participate in DNA repair-linked chromatin reassembly (PMC3089522; PMID:21454479)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522)
- [Mersfelder & Parthun, 2008, Involvement of Hat1p (Kat1p) catalytic activity and subcellular localization in telomeric silencing (PMC2570870; PMID:18753131)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2570870)
- [Qin & Parthun, 2006, Recruitment of the type B histone acetyltransferase Hat1p to chromatin is linked to DNA double-strand breaks (PMC1447429; PMID:16612003)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429) and [SGD reference page](https://www.yeastgenome.org/reference/16612003)
- [Qin & Parthun, 2002, Histone H3 and the histone acetyltransferase Hat1p contribute to DNA double-strand break repair (PMC134061; PMID:12417736)](https://pmc.ncbi.nlm.nih.gov/articles/PMC134061)
- [Kelly et al., 2000, Type B histone acetyltransferase Hat1p participates in telomeric silencing (PMC86239; PMID:10982821)](https://pmc.ncbi.nlm.nih.gov/articles/PMC86239) and [SGD reference page](https://www.yeastgenome.org/reference/10982821)
- [Capone et al., 2023, Understanding HAT1: A Comprehensive Review of Noncanonical Roles and Connection with Disease (PMC10137880)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137880) and [MDPI](https://www.mdpi.com/2073-4425/14/4/915)
- [GeneCards: HAT1 (human ortholog context)](https://www.genecards.org/card/HAT1)
- UniProt Q12341 (local copy `genes/yeast/HAT1/HAT1-uniprot.txt`), which cites PMID:7559580, PMID:8858151, PMID:9575221, PMID:9727486, PMID:14761951 and PMID:15099519. These six papers were not opened in this session.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC4683284
3. https://genesdev.cshlp.org/content/28/11/1217.abstract
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC2570870
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC10137880
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522
7. https://genesdev.cshlp.org/content/36/7-8/408.full
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC4052767
9. https://rcsb.org/structure/4PSW
10. https://rcsb.org/structure/4psx
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429
12. https://www.yeastgenome.org/reference/16612003
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC134061
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC86239
15. https://www.yeastgenome.org/reference/10982821
16. https://www.mdpi.com/2073-4425/14/4/915
17. https://www.genecards.org/card/HAT1