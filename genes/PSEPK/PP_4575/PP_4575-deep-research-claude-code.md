---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:32:27.153243'
end_time: '2026-10-30T21:39:27.750634'
duration_seconds: 420.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4575
  gene_symbol: PP_4575
  uniprot_accession: Q88E91
  protein_description: 'SubName: Full=Urea amidolyase-related protein {ECO:0000313|EMBL:AAN70148.1};'
  gene_info: OrderedLocusNames=PP_4575 {ECO:0000313|EMBL:AAN70148.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: CT_A_B. (IPR003778); Cyclophilin-like_dom_sf. (IPR029000); PxpC.
    (IPR052708); CT_A_B (PF02626)
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
  web_search_requests: 3
  num_turns: 21
  total_cost_usd: 1.303056
  session_id: d07b311e-5dc7-4990-b9e9-3fdc7ae9e394
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 7
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88E91
- **Protein Description:** SubName: Full=Urea amidolyase-related protein {ECO:0000313|EMBL:AAN70148.1};
- **Gene Information:** OrderedLocusNames=PP_4575 {ECO:0000313|EMBL:AAN70148.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CT_A_B. (IPR003778); Cyclophilin-like_dom_sf. (IPR029000); PxpC. (IPR052708); CT_A_B (PF02626)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4575" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4575' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4575** (gene ID: PP_4575, UniProt: Q88E91) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Neighbour check: PP_4576 is PxpB (ybgJ) and its coding sequence overlaps PP_4575's. Next I'm looking for PxpA and any paralogous PxpC copies.

Europe PMC returned an error. I'm getting the full text from NCBI PMC instead.

# PP_4575 (UniProt Q88E91) in *Pseudomonas putida* KT2440: probable 5-oxoprolinase subunit C (PxpC)

## Summary

PP_4575 is almost certainly the **C subunit of the bacterial three-subunit, ATP-dependent 5-oxoprolinase (PxpABC)**, even though UniProt still names it only "urea amidolyase-related protein". The complex converts 5-oxo-L-proline (pyroglutamate) to L-glutamate:

> 5-oxo-L-proline + ATP + 2 H₂O → L-glutamate + ADP + phosphate + H⁺ (EC 3.5.2.9; RHEA:10348)

Several lines of evidence agree on this:

- **Domains:** it has a PF02626 "CT_A_B" (AHS2, SMART SM00797) domain on a cyclophilin-like fold.
- **Family:** it carries the InterPro "PxpC" signature (IPR052708), the PANTHER family named "5-oxoprolinase subunit C" (PTHR43309), and the NCBIfam model TIGR00724 ("urea_amlyse_rel").
- **Sequence similarity:** it is about 41% identical to experimentally characterised *E. coli* PxpC and about 38% identical to *B. subtilis* PxpC.
- **Genome context:** it is the last gene of an apparent *pxpA–pxpB–pxpC* operon (PP_4577–PP_4576–PP_4575) whose reading frames overlap.

No experiment has been done on PP_4575 or the KT2440 *pxp* operon itself, so the function is a **strong homology- and synteny-based inference**. GOA currently holds **no GO annotations** for Q88E91. Its UniProt protein-existence level is "4: Predicted".

---

## 1. Identity check

| Item | Value | Source |
|---|---|---|
| Accession / locus | Q88E91 / PP_4575 (EMBL AAN70148.1; RefSeq WP_010955244.1) | UniProt record, local `PP_4575-uniprot.txt` |
| Organism | *P. putida* KT2440 (taxon 160488) | UniProt |
| Length | 305 aa, 32.5 kDa | UniProt |
| UniProt name | "Urea amidolyase-related protein" (imported from the EMBL submission, ECO:0000313) | UniProt |
| Domain | Carboxyltransferase domain at residues 25–304 (SMART SM00797 / AHS2) | UniProt FT, ECO:0000259 |
| Signatures | IPR003778 CT_A_B; IPR029000 cyclophilin-like domain superfamily; **IPR052708 PxpC**; PF02626; TIGR00724; PANTHER PTHR43309 ("5-OXOPROLINASE SUBUNIT C"), subfamily SF4 | UniProt DR lines |
| Orthology group | eggNOG COG1984 | UniProt |

The symbol "PP_4575" is a locus tag that refers to only one gene, so it is not ambiguous. The UniProt keywords ATP-binding and Hydrolase come from ARBA rules only, so they are not counted as independent evidence here.

## 2. Key concepts

### 2.1 5-Oxoproline as a damage metabolite

5-Oxoproline (OP, pyroglutamate) forms spontaneously, without an enzyme, when glutamine and glutamate cyclise. It also comes from pyroglutamyl peptides.

- In eukaryotes, OP is an intermediate of the γ-glutamyl cycle and is cleared by a large ATP-dependent 5-oxoprolinase (OPLAH).
- Most prokaryotes have neither OPLAH homologs nor that cycle.
- Niehaus et al. (2017) found the prokaryotic replacement. They named the genes after their homologs: *pxpA* (fungal LamB lactamase homolog) and *pxpB/pxpC* (homologs of allophanate hydrolase subunits). They concluded that "OP is a major universal metabolite damage product and that OP disposal systems are common in all domains of life" [PMID:28830929; Niehaus TD et al., *J Biol Chem* 2017; doi:10.1074/jbc.M117.805028; PMC5625064].

### 2.2 The PxpABC enzyme

- **Genetic evidence (*B. subtilis*):** knocking out *pxpA*, *pxpB* or *pxpC* "slowed growth, caused OP accumulation in cells and medium, and prevented use of OP as a nitrogen source". ATP-dependent 5-oxoprolinase activity in cell lysates disappeared when any one of the three genes was inactivated [PMID:28830929].
- **Biochemical evidence:** activity "could be reconstituted *in vitro* by mixing recombinant *B. subtilis* PxpA, PxpB, and PxpC proteins". Overexpressing *E. coli pxpABC* raised lysate activity at least 1700-fold [PMID:28830929].
- **Curated record for *E. coli* PxpC** (P75745, YbgK, Swiss-Prot): "Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate". It "forms a complex composed of PxpA, PxpB and PxpC", and deleting the gene slows growth on minimal medium. The catalytic activity and EC number are tagged with experimental evidence (ECO:0000269, PMID:28830929). A crystal structure, PDB 5DUD (2.8 Å), contains PxpC chains [UniProt P75745].

### 2.3 How the work divides among the subunits (proposed)

- **First step:** PxpB and PxpC (the "PxpBC" pair) are thought to phosphorylate 5-oxoproline, using ATP.
- **Later steps:** PxpA is proposed to open the phosphorylated ring to γ-glutamyl phosphate and then remove the phosphate to give L-glutamate. The evidence for PxpA's role is structural bioinformatics, not enzymology. The same study suggests the complex may pass its unstable intermediates directly between subunits (substrate channelling) [PMID:31520514; Oke M et al., *Biochem Mol Biol Educ* 2019; doi:10.1002/bmb.21300].
- A 2026 study restates this model: "It is assumed that PxpB and PxpC are responsible for ATP-dependent phosphorylation of 5-OP, whereas PxpA catalyzes the decyclization to γ-glutamyl phosphate and subsequent dephosphorylation to L-glutamate" [PMID:42212642; *Appl Environ Microbiol* 2026; doi:10.1128/aem.02181-25; PMC13274462].
- The precise catalytic residues in PxpC, and whether PxpC binds the nucleotide or mainly acts as a scaffold for PxpB, have **not been established**.

### 2.4 Structure: the KipI–KipA / "bicyclophilin" fold

PxpB and PxpC are the same proteins that *B. subtilis* sporulation studies call **KipI** and **KipA**.

- **Domain structure:** the TTHA0988 structure from *Thermus thermophilus*, a natural KipI–KipA fusion, showed that both proteins have two domains. Their C-terminal domains belong to the cyclophilin family and face each other to form a large "bicyclophilin" cleft [PMID:21050859; Jacques DA et al., *J Mol Biol* 2011; doi:10.1016/j.jmb.2010.10.047].
- **Allophanate hydrolase label is wrong:** the same protein is "incorrectly annotated as an allophanate hydrolase"; "no such activity could be identified" [PMID:21245531; *Acta Cryst D* 2011; doi:10.1107/S0907444910051127].
- **Link to urea carboxylase:** the carboxyltransferase domain of urea carboxylase (urea amidolyase) belongs to the same large family as the KipA–KipI complex [PMID:22277658; *J Biol Chem* 2012; doi:10.1074/jbc.M111.319475].

This shared domain explains the "urea amidolyase-related" name. That name reflects domain homology only: PP_4575 is a 305-aa standalone protein with no biotin carboxylase or biotin-carrier domain, so it cannot be a urea carboxylase.

### 2.5 Regulatory roles in other species, and why they don't transfer

- **In *B. subtilis*:** KipI (PxpB) inhibits the sporulation kinase KinA through its cyclophilin-like C-domain [PMID:18823995; Jacques DA et al., *J Mol Biol* 2008]. KipA (PxpC) binds KipI and blocks that inhibition [PMID:21050859].
- **In *C. difficile*:** the PxpB/PxpC homologs have no significant effect on sporulation. The *pxpAGBC* operon "encodes a functional oxoprolinase that facilitates detoxification of OP" and lets OP serve as a nutrient [PMID:40342073; Lee CD et al., *Mol Microbiol* 2025; doi:10.1111/mmi.15373; PMC12245574].

The sporulation role is a *Bacillus*-specific adaptation. *P. putida* does not sporulate and has no KinA phosphorelay, so that regulatory role should **not** be transferred to PP_4575.

## 3. Evidence specific to PP_4575

### 3.1 Genome context: the *pxpABC* operon

I took locus coordinates and orthology assignments from KEGG REST (`rest.kegg.jp/get/ppu:…`):

| Locus | Coordinates (all on the complementary strand) | Annotation / KO | Assigned role |
|---|---|---|---|
| PP_4578 | 5197297–5198583 | MFS transporter | possible transporter (no evidence on substrate) |
| PP_4577 | 5196511–5197287 | UPF0271; **K07160 PxpA** (LamB_YcsF) | PxpA |
| PP_4576 (*ybgJ*) | 5195825–5196514 | **K23123 PxpB** (CT_C_D) | PxpB |
| **PP_4575** | 5194911–5195828 | CT_A_B; no KO assigned | **PxpC** |

- The three genes overlap by 4 nt at each junction (PP_4577/PP_4576 at 5196511–5196514; PP_4576/PP_4575 at 5195825–5195828). This is the typical ATGA overlap of genes that are translated together, which strongly suggests one transcript in the same A-B-C order as the *E. coli* and *B. subtilis* clusters [PMID:28830929].
- KEGG has not yet assigned PP_4575 to KO K23124 (pxpC). That is an assignment gap, not evidence against the function.
- **Speculation:** PP_4578 might take up OP, since *C. glutamicum* needs a dedicated OP transporter (PxpT, a different superfamily) next to its *pxpABC* genes [PMID:42212642]. I have no data to support this for PP_4578.

### 3.2 Sequence similarity (my own analysis)

I ran a global Needleman–Wunsch alignment (BLOSUM62, gap open −10, extend −0.5; Biopython):

| Comparison | Identity over aligned positions |
|---|---|
| PP_4575 vs *E. coli* PxpC P75745 (310 aa) | **41.1%** (285 positions) |
| PP_4575 vs *B. subtilis* PxpC Q7WY77 (335 aa) | **38.2%** (293 positions) |
| PP_4575 vs PP_2922, a KT2440 paralog (323 aa) | 37.9% (293 positions) |

About 40% identity across the full length to two experimentally characterised PxpC proteins from distant phyla, plus conserved gene order, is strong support that the function is conserved.

### 3.3 A second *pxp*-like cluster in KT2440

KT2440 has a second cluster on the forward strand:

| Locus | Annotation | Likely role |
|---|---|---|
| PP_2920 (*ybgL*) | K07160 PxpA | PxpA-like |
| PP_2921 | CT_C_D | PxpB-like |
| PP_2922 | "urea amidolyase-related", CT_A_B | PxpC-like |

PP_2922 is about 38% identical to PP_4575.

- **Interpretation:** KT2440 probably has two PxpABC-type systems. Which one clears OP in vivo, whether they are redundant, and whether the PP_2920–2922 system has drifted to another substrate (some members of the family are thought to act on other lactams) is **unknown**.
- **Consequence for knockout experiments:** a single PP_4575 deletion may show only a mild phenotype if the paralogous system compensates.

### 3.4 The historical "*Pseudomonas putida* 5-oxoprolinase" (Meister lab)

The original description of a bacterial 5-oxoprolinase came from a ***P. putida* soil isolate obtained by enrichment culture**, not from strain KT2440:

- The enzyme consisted of two dissociable components. Component A catalyses 5-oxoproline-dependent ATP cleavage; Component B "is required for the coupling of ATP cleavage to ring-opening of 5-oxoproline to form glutamate". Together they form an A₂B₂ complex in the presence of substrates [PMID:3360791; Li LY, Seddon AP, Meister A, *J Biol Chem* 1988; citing Seddon et al., *J Biol Chem* 1984, 259:8091].
- Later papers cite this enzyme as the first bacterial 5-oxoprolinase, and the *C. difficile* paper states that PxpB and PxpC associate with PxpA "in *B. subtilis*, *Escherichia coli*, and *Pseudomonas putida*" [PMID:42212642; PMID:40342073].
- **Caution:** the subunit masses reported for the soil-isolate enzyme are large (roughly 50–82 kDa polypeptides, from BRENDA summaries of the Meister papers). PxpA, PxpB and PxpC are each only about 25–33 kDa. So it is **not certain** that the Meister enzyme is a PxpABC complex. It could instead be a different two-component bacterial 5-oxoprolinase (an OPLAH-like split enzyme). The Meister biochemistry should not be taken as direct experimental evidence for PP_4575.

## 4. Inferred function, pathway and location

**Molecular function (inferred).** PP_4575 is a subunit of ATP-hydrolysing 5-oxoprolinase (EC 3.5.2.9). Within the PxpBC pair it probably contributes to the ATP-dependent phosphorylation of 5-oxoproline, the first step, and depends on PxpA for ring opening and dephosphorylation. Because PxpC alone has no shown activity, a GO annotation should use *contributes_to* "5-oxoprolinase (ATP-hydrolyzing) activity" (GO:0017168; check the ID and label against the current ontology before use). A plain *enables* would overstate the evidence.

**Complex membership.** It is expected to form a heteromeric PxpA–PxpB–PxpC complex, based on *E. coli* and *B. subtilis* [UniProt P75745; PMID:28830929]. TTHA0988 shows that PxpB and PxpC (KipI and KipA) interact through a cyclophilin-domain "bicyclophilin" interface [PMID:21050859].

**Biological process.**

- *Primary role:* clearing the damage metabolite 5-oxoproline by converting it to L-glutamate, which recovers the glutamate (glutamine) carbon and nitrogen it came from. This is a metabolite repair/damage-control process [PMID:28830929; PMID:40342073].
- *Secondary role (possible):* in other bacteria the same enzyme lets cells use external OP as a nitrogen and/or carbon source [PMID:28830929; PMID:42212642]. KT2440 is metabolically very versatile, so a role in catabolising environmental pyroglutamate is plausible, but it has not been tested.
- *Excluded:* sporulation control by KinA inhibition does not apply to *P. putida* [PMID:40342073].

**Location.** Cytoplasm (inferred). The protein has no predicted signal peptide or transmembrane segment; the UniProt record lists none. All characterised Pxp proteins are soluble cytoplasmic enzymes, and the substrate it handles is generated inside the cell.

## 5. Annotation status and caveats

- **GOA:** no annotations exist for Q88E91. Possible new annotations are the 5-oxoprolinase activity (with *contributes_to*), cytoplasm, and a 5-oxoproline/glutamate metabolic process. The evidence would be ISS from P75745 or Q7WY77, together with the synteny and family evidence above.
- **Name:** "Urea amidolyase-related protein" is a historical name based only on the shared domain. The protein lacks the biotin-dependent machinery of urea carboxylase. Similar proteins were wrongly labelled "allophanate hydrolase" [PMID:21245531]. "5-oxoprolinase subunit C (PxpC)" is the better name.
- **No direct experiments:** I found no paper that knocks out, purifies or tests PP_4575 or the KT2440 *pxp* operon. I tried to check the LBL Fitness Browser (where large-scale KT2440 transposon fitness data are hosted) but it blocked automated access, so I could not see that data.
- **Redundancy:** the paralogous PP_2920–PP_2922 cluster means the roles of the two systems remain to be separated.

## 6. Suggested experiments

1. Delete PP_4575 alone, PP_2920–2922 alone, and both together. Grow the strains on 5-oxo-L-proline as the sole nitrogen or carbon source, and measure OP accumulation inside and outside the cells, following the approach of Niehaus et al. 2017 and Lee et al. 2025.
2. Purify PP_4577, PP_4576 and PP_4575 and reconstitute the enzyme. Measure OP-dependent ATP hydrolysis and glutamate formation, with any one subunit left out at a time. Test the PP_2920–2922 proteins against other lactams to see whether they specialise in a different substrate.
3. Use pulldown or SEC-MALS to measure how many PxpA, PxpB and PxpC subunits make up the complex. Mutate conserved residues in the PxpC cyclophilin-like cleft to find out whether PxpC takes part in catalysis.

---

## References

1. Niehaus TD et al. (2017) Discovery of a widespread prokaryotic 5-oxoprolinase that was hiding in plain sight. *J Biol Chem* 292:16360. PMID:28830929. https://pmc.ncbi.nlm.nih.gov/articles/PMC5625064 · https://escholarship.org/uc/item/50g9h8k4
2. Lee CD, Rizvi A, Carter ZA, Edwards AN, McBride SM (2025) The Pxp complex detoxifies 5-oxoproline and promotes the growth of *Clostridioides difficile*. *Mol Microbiol* 124:66–76. PMID:40342073. doi:10.1111/mmi.15373 (PMC12245574)
3. (2026) Growth of *Corynebacterium glutamicum* on 5-oxo-L-proline requires the PxpR-controlled *pxpTABC* genes. *Appl Environ Microbiol*. PMID:42212642. doi:10.1128/aem.02181-25 (PMC13274462)
4. Oke M et al. (2019) Structure-function relationships of the 5-oxoprolinase subunit A. *Biochem Mol Biol Educ* 47:620–631. PMID:31520514. doi:10.1002/bmb.21300 · https://cpi.vm.uni-freiburg.de/cpril/article_relationships_table/pmid=31520514cid=819pid=10508
5. Li LY, Seddon AP, Meister A (1988) Interaction of the protein components of 5-oxoprolinase. *J Biol Chem* 263:6495–6501. PMID:3360791 (cites Seddon, Li & Meister 1984, *J Biol Chem* 259:8091). BRENDA summaries: https://www.brenda-enzymes.info/literature.php?r=209373
6. Jacques DA et al. (2011) A novel structure of an antikinase and its inhibitor. *J Mol Biol*. PMID:21050859. doi:10.1016/j.jmb.2010.10.047
7. (2011) The structure of TTHA0988 from *Thermus thermophilus*, a KipI-KipA homologue incorrectly annotated as an allophanate hydrolase. *Acta Cryst D*. PMID:21245531. doi:10.1107/S0907444910051127
8. Jacques DA et al. (2008) Histidine kinase regulation by a cyclophilin-like inhibitor. *J Mol Biol*. PMID:18823995. doi:10.1016/j.jmb.2008.09.017
9. Fan C et al. (2012) Crystal structure of urea carboxylase provides insights into the carboxyltransfer reaction. *J Biol Chem*. PMID:22277658. doi:10.1074/jbc.M111.319475
10. UniProtKB Q88E91 (PP_4575), P75745 (PXPC_ECOLI) and Q7WY77 (PXPC_BACSU): https://rest.uniprot.org/uniprotkb/P75745.txt · PDB 5DUD: https://proteopedia.org/w/5dud
11. KEGG GENES ppu:PP_4575, PP_4576, PP_4577, PP_4578, PP_2920–PP_2922: https://www.kegg.jp/entry/ppu:PP_4576
12. Nelson KE et al. (2002) Complete genome sequence of *P. putida* KT2440. *Environ Microbiol* 4:799. PMID:12534463. Belda E et al. (2016) The revisited genome of *P. putida* KT2440. *Environ Microbiol* 18:3403. PMID:26913973.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC5625064
2. https://escholarship.org/uc/item/50g9h8k4
3. https://cpi.vm.uni-freiburg.de/cpril/article_relationships_table/pmid=31520514cid=819pid=10508
4. https://www.brenda-enzymes.info/literature.php?r=209373
5. https://rest.uniprot.org/uniprotkb/P75745.txt
6. https://proteopedia.org/w/5dud
7. https://www.kegg.jp/entry/ppu:PP_4576