---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-31T00:36:28.893034'
end_time: '2026-10-31T00:38:47.286507'
duration_seconds: 138.39
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: atpD
  gene_symbol: atpD
  uniprot_accession: P0ABB4
  protein_description: 'RecName: Full=ATP synthase subunit beta {ECO:0000255|HAMAP-Rule:MF_01347};
    EC=7.1.2.2 {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=ATP synthase F1 sector
    subunit beta {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=F-ATPase subunit
    beta {ECO:0000255|HAMAP-Rule:MF_01347};'
  gene_info: Name=atpD {ECO:0000255|HAMAP-Rule:MF_01347}; Synonyms=papB, uncD; OrderedLocusNames=b3732,
    JW3710;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the ATPase alpha/beta chains family.
  protein_domains: AAA+_ATPase. (IPR003593); ATP-synt_VA_C. (IPR055190); ATP_synth_F1_bsu.
    (IPR005722); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains. (IPR050053)
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
  web_search_requests: 5
  num_turns: 11
  total_cost_usd: 0.7917151000000002
  session_id: ad2017fb-bc45-411b-9559-e1f8d6183617
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 16
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P0ABB4
- **Protein Description:** RecName: Full=ATP synthase subunit beta {ECO:0000255|HAMAP-Rule:MF_01347}; EC=7.1.2.2 {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=ATP synthase F1 sector subunit beta {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=F-ATPase subunit beta {ECO:0000255|HAMAP-Rule:MF_01347};
- **Gene Information:** Name=atpD {ECO:0000255|HAMAP-Rule:MF_01347}; Synonyms=papB, uncD; OrderedLocusNames=b3732, JW3710;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the ATPase alpha/beta chains family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ATP-synt_VA_C. (IPR055190); ATP_synth_F1_bsu. (IPR005722); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains. (IPR050053)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atpD" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atpD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atpD** (gene ID: atpD, UniProt: P0ABB4) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still working: two more literature searches (catalytic mechanism and ε-subunit inhibition), then I'll write the report.

# *Escherichia coli* atpD (UniProt P0ABB4): ATP synthase F1 subunit β

## 0. Identity check

- **Target:** UniProt P0ABB4, gene *atpD* (synonyms *uncD* and *papB*; b3732/JW3710), *E. coli* K-12. It is "ATP synthase subunit beta", EC 7.1.2.2, and "Belongs to the ATPase alpha/beta chains family" (local UniProt record, `genes/ECOLI/atpD/atpD-uniprot.txt`).
- **Literature match:** The older *E. coli* papers call this gene *uncD*. Senior et al. (1979) describe "uncoupled mutant strains of *Escherichia coli* carrying mutations in the uncD gene… the beta-subunit of the F1 portion of the membrane-bound adenosine triphosphatase is abnormal" [PMID:158358]. The name, organism, family and domains (Walker-A/P-loop, ATP_synth_F1_bsu) all agree.
- **A naming trap to avoid:** in some other bacteria, *atpD* has been used for a different subunit. Everything in this report is about the *E. coli* β subunit, which is encoded by *atpD/uncD* in the *atpIBEFHAGDC* operon.

## 1. Summary

AtpD is the catalytic subunit of the F-type ATP synthase (F1Fo-ATPase). This enzyme couples the inward flow of protons across the inner (cytoplasmic) membrane to making ATP from ADP and inorganic phosphate. It can also run backwards, using ATP hydrolysis to pump protons outward.

- **Stoichiometry:** three β subunits alternate with three α subunits (AtpA) to form the α3β3 hexamer of the soluble F1 sector. That hexamer surrounds the γ subunit of the central rotor.
- **Where catalysis happens:** UniProt states that the enzyme "Produces ATP from ADP in the presence of a proton gradient across the membrane. The catalytic sites are hosted primarily by the beta subunits." Each catalytic site sits at an α/β interface, and most of its residues come from β.
- **Reaction** (UniProt/Rhea RHEA:57720, EC 7.1.2.2, written in the hydrolysis direction): ATP + H2O + 4 H⁺(in) = ADP + phosphate + 5 H⁺(out).
- **Location:** UniProt places AtpD at the "Cell inner membrane; Peripheral membrane protein". It sits on the cytoplasmic face of the inner membrane, held to the membrane-embedded Fo sector by the central and peripheral stalks.
- **Pathway:** oxidative phosphorylation, i.e. proton-motive-force-driven ATP synthesis at the plasma membrane. When the cell grows fermentatively, the same enzyme can run in reverse and use ATP to generate the proton motive force.

## 2. Molecular function

### 2.1 Catalytic activity and substrate specificity

The β subunit carries the nucleotide-binding catalytic sites of the enzyme. It works with MgADP + Pi when making ATP, and with MgATP when hydrolysing it.

- **ATP-binding P-loop:** UniProt annotates ATP binding at residues 150–157. This is the Walker-A motif (GxxxxGKT) typical of the AAA+/RecA-like α/β-ATPase fold.
- **Thr-157:** mutation to Ala or Cys "Impairs ATPase activity" (UniProt MUTAGEN, ECO:0000269, PubMed:1832155). Thr-157 is the Walker-A residue that coordinates Mg²⁺.
- **Other catalytic residues, from mutagenesis by the Senior and Futai groups:**
  - Lys-155 (P-loop) lies near the γ-phosphate. Substitutions at Lys-155 or Thr-156 abolish activity, including uni-site catalysis.
  - Glu-181 is the DCCD-reactive carboxylate and acts as the catalytic base. The Glu181→Gln mutant reduced unisite Pi formation about seven-fold and lowered ATP affinity.
  - Arg-182 and Arg-246 from β, with αArg-376, form a "triangular" phosphate-binding site that binds Pi at the empty (βE) catalytic site. A Futai-group paper (title only seen) reported that the conserved Glu-181 and Arg-182 are "essential for catalysis".
  - Sources: [Wake Forest / Senior profile and abstracts](https://profiles.wakehealth.edu/display/72487); [PubMed 2859284](https://pubmed.ncbi.nlm.nih.gov/2859284); [PMC2667762](https://pmc.ncbi.nlm.nih.gov/articles/PMC2667762).
  - *Caveat:* these specific details come from search snippets and abstracts. Check the primary JBC and Biochemistry papers before quoting numbers.
- **Tyr-331 (adenine pocket):** Senior and coworkers replaced βTyr-331, which stacks against the adenine ring, with Trp to make a fluorescent probe. Measuring quenching of this Trp let them titrate nucleotide occupancy of each catalytic site directly. Those measurements showed that steady-state hydrolysis needs most or all of the three sites filled (tri-site catalysis) ([Frontiers in Chemistry 2023 perspective](https://www.frontiersin.org/articles/10.3389/fchem.2023.1058500/full)). Whether occupying a second site is already enough for rapid catalysis is still debated (Milgrom & Cross 2005, [PMC1236596](https://pmc.ncbi.nlm.nih.gov/articles/PMC1236596)).
- **Specificity:** physiologically, the sites use Mg-adenine nucleotides. Other NTPs such as GTP and ITP are hydrolysed in vitro, but ATP/ADP is the relevant substrate pair. This is general F1 biochemistry, not specific to the cited E. coli studies.

### 2.2 Activity belongs to the complex, not to β alone

An isolated β subunit binds nucleotide, but it neither synthesises nor hydrolyses ATP at physiological rates. Catalysis needs:

- the α3β3 hexamer, because the catalytic sites lie at α/β interfaces; and
- rotation of γ, which drives the cooperative conformational cycle of the binding-change mechanism.

The best GO description of β is therefore that it **contributes to** "proton-transporting ATP synthase activity, rotational mechanism" (GO:0046933). Both a `contributes_to` row and an `enables` row for this term exist in GOA for P0ABB4. ATP binding (GO:0005524) is a direct property of β.

### 2.3 Rotary mechanism

- **Rotation in E. coli F1:** Duncan, Bulygin, Zhou, Hutcheon & Cross (1995) built a direct test for rotation using disulfide cross-links between β and γ. They concluded that "the gamma subunit rotates relative to the beta subunits during catalysis" in soluble *E. coli* F1 (PNAS 92:10964; PMID:7479919; [PMC40551](https://pmc.ncbi.nlm.nih.gov/articles/PMC40551)). This was among the first biochemical demonstrations of rotational catalysis. Single-molecule imaging later visualised the rotation (Noji et al. 1997, Nature, *Bacillus* PS3 F1).
- **How β couples to the rotor:** in each catalytic cycle, every β subunit passes through three states: open/empty (βE), ADP-bound (βDP) and ATP-bound (βTP). The C-terminal domain of β, including the conserved acidic "DELSEED" loop, swings toward or away from the asymmetric γ shaft. This hinge motion is what couples rotation to the affinity changes at the catalytic site.
- **Sector architecture** (UniProt SUBUNIT): F1 = α3β3γδε; Fo = a1 b2 c(9–12) (c10 in *E. coli*). The α/β ring encloses γ. The central stalk is γ+ε; the peripheral stalk (stator) is δ+b2.

## 3. Structural evidence specific to *E. coli*

- **Cingolani & Duncan 2011, Nat Struct Mol Biol** [PMID:21602818; PDB 3OAA]:
  - This is the crystal structure of *E. coli* F1 in an autoinhibited state.
  - The C-terminal domain of subunit ε "adopts a novel, highly extended conformation that inserts deeply into the central cavity of the enzyme", where it touches both rotor and stator subunits ([RCSB 3OAA](https://www.rcsb.org/structure/3oaa); [PMC3109198](https://pmc.ncbi.nlm.nih.gov/articles/PMC3109198/)).
  - This ε-mediated inhibition occurs in bacteria and chloroplasts but not in mitochondria. The β subunits, including the region around the DELSEED loop, are among the stator surfaces that the extended ε contacts ([BRENDA summary](https://www.brenda-enzymes.org/literature.php?r=685315); I have not checked the exact residues in the primary paper).
- **Sobti et al. 2016, eLife** [PMID:28001127]: cryo-EM of the intact, autoinhibited *E. coli* F1Fo in three rotational states, at 6.9, 7.8 and 8.5 Å resolution. ε is in its extended inhibitory conformation in all three ([eLife 21598](https://elifesciences.org/articles/21598)).
- **Sobti et al. 2019, eLife:** under ATP, the enzyme takes distinct conformations, and ATP binding keeps the ε C-terminal domain out of the inhibitory "up" state ([PMC6449082](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449082/)).
- **Sobti et al. 2020, Nat Commun 11:2615** (doi:10.1038/s41467-020-16387-2; PDB 6PQV, 6VWK): nine cryo-EM structures at 3.1–3.4 Å, falling into four rotational sub-states. They reveal a rotary sub-step of the c-ring that elastically couples the Fo and F1 motors, which have different symmetries ([DOAJ record](https://doaj.org/article/0173de1fc389481f868feeaeaacc4180); [RCSB 6PQV](https://www2.rcsb.org/structure/6pqv)).
- **Regulation by ε:** the extended, inhibitory ε state forms after ATP hydrolysis at the catalytic dwell. Its N-terminal domain provides most of the binding energy to F1 (2013 kinetic study, via [PMC3133022](https://pmc.ncbi.nlm.nih.gov/articles/PMC3133022) and related work). Through this interaction, β's conformational cycle is coupled to a bacteria-specific way of limiting wasteful ATP hydrolysis.

## 4. Genetic evidence and assembly

- **uncD mutants** [PMID:158358, Senior et al. 1979]: five uncoupled *uncD* strains had abnormal β. In four of them, membrane ATPase activity was absent. The *uncD12* allele formed an aggregated F1 with low ATPase activity. The phenotype is loss of oxidative phosphorylation, so cells cannot grow on non-fermentable carbon sources such as succinate. This ties β directly to ATP synthesis in vivo.
- **Assembly** [PMID:2863270, Klionsky & Simoni 1985]: F1 subunits assemble into a complex without the Fo subunits. However, "Mutations of the uncA(alpha), uncG(gamma), or uncD(beta) genes result in a defective assembly of the F1 complex." By contrast, δ and ε are not needed for the core α3β3γ assembly. So β is a structural core subunit as well as the catalytic one.
- **Interaction data:** UniProt INTERACTION lists a binary interaction between P0ABB4 and P0ABB0 (AtpA), with 13 experiments (IntAct). This is consistent with the α/β interface. It underlies GOA's bare "protein binding" (GO:0005515) row, which the project removes as uninformative.
- **Localisation:** cell-envelope proteomics recovers AtpD among membrane-associated peripheral proteins [PMID:17137328, Huang et al. 2006, abstract only]. That fits its peripheral position on the cytoplasmic face of the inner membrane.
- **Processing:** the initiator Met is removed and the mature chain is residues 2–460 (UniProt, ECO:0000269 PubMed:9298646).

## 5. Evolution and bioinformatics

- **Family:** ATPase α/β chains family (UniProt, HAMAP MF_01347). β is related by ancient duplication to the non-catalytic α subunit, and to the A/V-type ATPase catalytic A subunit (InterPro IPR055190 ATP-synt_VA_C; IPR050053).
- **Domain layout:** N-terminal β-barrel, central nucleotide-binding domain (RecA/AAA+-like, Walker A and B), and C-terminal helical domain (with DELSEED).
- **Conservation:** high across bacteria, chloroplasts (CF1-β) and mitochondria (ATP5F1B). That conservation lets bovine and yeast structures be used to interpret the *E. coli* enzyme, as Duncan et al. 1995 did with the bovine F1 structure.
- **HAMAP signatures:** the β-specific signature (IPR005722) and the α/β-ATPase active-site signature (IPR020003) both match P0ABB4.

## 6. Biological process and localisation in context

- **Process:** proton-motive-force-driven plasma-membrane ATP synthesis (GO:0042777), the specific bacterial child of GO:0015986. This is the main physiological role during aerobic or anaerobic respiration.
- **Reverse mode:** during fermentation, the enzyme hydrolyses glycolytic ATP to keep up the proton motive force for transport and motility. It is still the complex that pumps protons, via Fo; β provides the chemistry.
- **"Proton transmembrane transport" (GO:1902600):** the proton path is in Fo (subunits a and c; see the Cain & Simoni 1986 *uncB* paper, PMID:2874137, which characterised proton conduction through subunit a, and the Wada et al. 1999 subunit a topology paper, PMID:10358096). β only takes part in proton transport through coupling inside the complex, so this term is best treated as non-core.
- **Location:**
  - Cellular component: the proton-transporting ATP synthase complex (GO:0045259), specifically its catalytic F1 sector (GO:0045261, proton-transporting ATP synthase complex, catalytic core F(1)).
  - Place in the cell: the cytoplasmic side of the plasma (inner) membrane, as a peripheral membrane protein. "Membrane" (GO:0016020) is correct but general; "plasma membrane" (GO:0005886) is the specific term.

## 7. Implications for the existing GOA annotations

| GO term | My assessment |
|---|---|
| GO:0046933 proton-transporting ATP synthase activity, rotational mechanism (contributes_to / enables) | Core function. `contributes_to` best reflects the β subunit's role inside the complex. |
| GO:0046961 proton-transporting ATPase activity, rotational mechanism | Correct reverse-mode activity of the complex. Non-core in physiological direction. |
| GO:0005524 ATP binding | Supported by the Walker-A motif, Thr-157 mutagenesis and the βY331W probe studies. |
| GO:0042777 / GO:0015986 PMF-driven (plasma membrane) ATP synthesis | Core process. GO:0042777 is the specific bacterial term. |
| GO:0046034 ATP metabolic process | True but general. |
| GO:1902600 proton transmembrane transport | Function of the complex via Fo. Non-core for β. |
| GO:0045259 ATP synthase complex | Accept. The F1 catalytic core (GO:0045261) is a more specific option. |
| GO:0005886 plasma membrane / GO:0016020 membrane | Plasma membrane is correct (peripheral, cytoplasmic face). "Membrane" is too general. |
| GO:0005515 protein binding | Uninformative. Removed under project policy. The underlying fact is the α–β interaction in the hexamer. |

## 8. Open questions

- Is occupancy of two or three catalytic sites required for rapid steady-state catalysis? The bi-site versus tri-site question is still debated for *E. coli* F1 (Senior Trp-probe data versus Milgrom & Cross 2005).
- What exact β residues and contacts does the extended ε CTD use for inhibition in vivo? And how does ε inhibition affect fitness when the enzyme switches between synthesis and hydrolysis modes?

## Sources

- UniProtKB P0ABB4 record (local cache `genes/ECOLI/atpD/atpD-uniprot.txt`); HAMAP MF_01347.
- Senior AE et al. (1979) Biochem J 180:111. PMID:158358.
- Klionsky DJ, Simoni RD (1985) J Biol Chem 260:11200. PMID:2863270.
- Cain BD, Simoni RD (1986) J Biol Chem 261:10043. PMID:2874137.
- Wada T et al. (1999) J Biol Chem 274:17353. PMID:10358096.
- Huang CZ et al. (2006) J Proteome Res 5:3268. PMID:17137328.
- [Duncan TM et al. (1995) PNAS 92:10964, PMC40551](https://pmc.ncbi.nlm.nih.gov/articles/PMC40551)
- [Cingolani G, Duncan TM (2011) Nat Struct Mol Biol 18:701, PMC3109198](https://pmc.ncbi.nlm.nih.gov/articles/PMC3109198/); [RCSB 3OAA](https://www.rcsb.org/structure/3oaa)
- [Sobti M et al. (2016) eLife 5:e21598](https://elifesciences.org/articles/21598)
- [Sobti M et al. (2019) eLife, PMC6449082](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449082/)
- [Sobti M et al. (2020) Nat Commun 11:2615](https://doaj.org/article/0173de1fc389481f868feeaeaacc4180); [RCSB 6PQV](https://www2.rcsb.org/structure/6pqv); [RCSB 6VWK](https://rcsb.org/structure/6vwk)
- [PMC3133022 (ε inhibition kinetics)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3133022)
- [Milgrom & Cross (2005) PNAS, PMC1236596](https://pmc.ncbi.nlm.nih.gov/articles/PMC1236596)
- [Frontiers in Chemistry (2023) 10.3389/fchem.2023.1058500](https://www.frontiersin.org/articles/10.3389/fchem.2023.1058500/full)
- Catalytic-residue mutagenesis (Senior and Futai groups): [Wake Forest profile](https://profiles.wakehealth.edu/display/72487), [PubMed 2859284](https://pubmed.ncbi.nlm.nih.gov/2859284), [PMC2667762](https://pmc.ncbi.nlm.nih.gov/articles/PMC2667762), [J Exp Biol 172:443](https://cob.silverchair.com/jeb/article-split/172/1/443/6555/Escherichia-coli-ATP-synthase-F-ATPase-catalytic)
- [BRENDA literature entry 685315](https://www.brenda-enzymes.org/literature.php?r=685315)

## Citations

1. https://profiles.wakehealth.edu/display/72487
2. https://pubmed.ncbi.nlm.nih.gov/2859284
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC2667762
4. https://www.frontiersin.org/articles/10.3389/fchem.2023.1058500/full
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC1236596
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC40551
7. https://www.rcsb.org/structure/3oaa
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC3109198/
9. https://www.brenda-enzymes.org/literature.php?r=685315
10. https://elifesciences.org/articles/21598
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449082/
12. https://doaj.org/article/0173de1fc389481f868feeaeaacc4180
13. https://www2.rcsb.org/structure/6pqv
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC3133022
15. https://rcsb.org/structure/6vwk
16. https://cob.silverchair.com/jeb/article-split/172/1/443/6555/Escherichia-coli-ATP-synthase-F-ATPase-catalytic