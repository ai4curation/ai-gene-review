---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:31:21.900776'
end_time: '2026-10-30T21:40:34.646956'
duration_seconds: 552.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_0658
  gene_symbol: VC_0658
  uniprot_accession: Q9KU65
  protein_description: 'RecName: Full=cyclic-guanylate-specific phosphodiesterase
    {ECO:0000256|ARBA:ARBA00012282}; EC=3.1.4.52 {ECO:0000256|ARBA:ARBA00012282};'
  gene_info: OrderedLocusNames=VC_0658 {ECO:0000313|EMBL:AAF93824.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: EAL_dom. (IPR001633); EAL_sf. (IPR035919); GGDEF_dom. (IPR000160);
    Nucleotide_cyclase. (IPR029787); Rev_trsase/Diguanyl_cyclase. (IPR043128)
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 15
  total_cost_usd: 2.074636115
  session_id: 1008ed82-0e04-47bb-909c-e7b55ac6dfae
  stop_reason: end_turn
  assistant_text_blocks: 5
citation_count: 21
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KU65
- **Protein Description:** RecName: Full=cyclic-guanylate-specific phosphodiesterase {ECO:0000256|ARBA:ARBA00012282}; EC=3.1.4.52 {ECO:0000256|ARBA:ARBA00012282};
- **Gene Information:** OrderedLocusNames=VC_0658 {ECO:0000313|EMBL:AAF93824.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** EAL_dom. (IPR001633); EAL_sf. (IPR035919); GGDEF_dom. (IPR000160); Nucleotide_cyclase. (IPR029787); Rev_trsase/Diguanyl_cyclase. (IPR043128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_0658" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_0658' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_0658** (gene ID: VC_0658, UniProt: Q9KU65) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Searching for any study that assays VC0658 directly before I write the report.

Continuing — the cAMP-CRP biofilm paper appears to name VC0658 as *cdgI*, so I'll verify that directly.

Let me pull the *cdgI* evidence from Europe PMC and check the catalytic motifs in the sequence myself.

Good — three 2025 papers hit on both "VC0658" and "cdgI". Fetching those plus running my own motif check.

# Research Report: *Vibrio cholerae* VC_0658 (UniProt Q9KU65) — a hybrid GGDEF–EAL protein (*cdgI*)

**Target verification.** The gene symbol here is a bare ordered-locus tag, `VC_0658`, from the N16961 genome (El Tor Inaba, NCBI:txid243277) ([Heidelberg et al. 2000, *Nature* 406:477–483, PMID:10952301](https://pubmed.ncbi.nlm.nih.gov/10952301/)). The UniProt entry is **unreviewed (TrEMBL)**, `Q9KU65_VIBCH`, 685 aa, with protein existence level `PE 4: Predicted` and a RecName assigned entirely by an automatic rule (`ECO:0000256|ARBA:ARBA00012282`). KEGG independently describes the locus as "c-di-GMP phosphodiesterase A-related protein" with Pfam EAL + GGDEF ([KEGG vch:VC_0658](https://www.genome.jp/entry/vch:VC_0658)). The domain architecture reported in the task header (EAL IPR001633 + GGDEF IPR000160) matches both the UniProt feature table and KEGG, so **the identity is consistent and the target is correctly identified.**

**Headline finding, stated up front: this protein is essentially uncharacterized experimentally.** No published study reports a purified-protein assay, a deletion phenotype, a c-di-GMP measurement, or a localization experiment for VC_0658 specifically. I searched for the locus tag and its gene name across Europe PMC's full-text index and read the papers that hit. Everything below is therefore either (a) a verbatim database/literature statement about the gene's *classification*, (b) a group-level observation in which VC_0658 appears only as a list member, or (c) my own sequence analysis, labelled as such. One caution: a similar-looking tag **VCA0658** (*aer-2*, an aerotaxis receptor on chromosome II) is a **different gene** ([Boin & Häse 2007, *FEMS Microbiol Lett* 276:193–201, PMID:17956426](https://pubmed.ncbi.nlm.nih.gov/17956426/)) and must not be conflated with VC_0658 on chromosome I.

---

## 1. Gene name and genomic context

The gene name **`cdgI`** ("c-di-GMP I") is used for this locus in the recent primary literature. The clearest statement is in the Discussion of [Trebino MA, Kitts G, Haycocks JRJ, Wheat R, Chaudry I, Park JH, Erill I, Grainger DC, Yildiz FH. "Parallel regulatory circuits orchestrate biofilm formation in response to c-di-GMP levels and growth phase." *PLoS Genet* 2025 Sep 15;21(9):e1011870, PMID:40953128, PMCID:PMC12456836](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1011870), which enumerates the *V. cholerae* hybrid enzymes verbatim as:

> "five hybrid GGDEF–EAL domain proteins (VC0658 - cdgI, VC1934, VC2750, VCA0080, VCA1082-83 - lapD)"

This is the best available anchor for the symbol, and it also fixes the protein's class: **VC_0658 is one of only five hybrid GGDEF–EAL proteins in the *V. cholerae* genome.** Note that UniProt does *not* carry this symbol — its only gene line is `GN OrderedLocusNames=VC_0658` — so `cdgI` is a literature name not yet reflected in the database record.

The locus sits on **chromosome I at complement(701,609..703,666)**, i.e. 2,058 bp encoding 685 aa, with protein ID AAF93824 ([KEGG vch:VC_0658](https://www.genome.jp/entry/vch:VC_0658)). Incidentally, the VC0658–VC0659 intergenic region is a documented **integrative conjugative element (ICE/SXT-family) insertion site** in clinical O1 isolates ([Morita D et al., *mBio* 2020;11:e01227-20, PMID:33172996](https://journals.asm.org/doi/full/10.1128/mbio.01227-20)) — relevant to strain-to-strain genome comparisons, not to the protein's function.

Genome-wide context: *V. cholerae* encodes roughly **62 putative c-di-GMP metabolic enzymes — 31 with GGDEF, 12 with EAL, 10 with both GGDEF and EAL, and 9 with HD-GYP domains** ([Liu X, Beyhan S, Lim B, Linington RG, Yildiz FH. *J Bacteriol* 2010;192:4541–4552, PMID:20622061](https://pmc.ncbi.nlm.nih.gov/articles/PMC2937418)). This extreme redundancy is the single most important interpretive fact about VC_0658: in such a network, individual enzymes commonly have **no detectable single-deletion phenotype**, which plausibly explains why a protein known since 2000 remains uncharacterized.

## 2. Predicted primary function: c-di-GMP phosphodiesterase (EC 3.1.4.52)

### 2.1 The reaction

UniProt assigns, by automatic rule only, the reaction:

> `Reaction=3',3'-c-di-GMP + H2O = 5'-phosphoguanylyl(3'->5')guanosine + H(+); Xref=Rhea:RHEA:24902 ... EC=3.1.4.52; Evidence={ECO:0000256|ARBA:ARBA00051114}; PhysiologicalDirection=left-to-right`

with **Mg²⁺** as cofactor (`ECO:0000256|ARBA:ARBA00001946`) (local UniProt flat file for Q9KU65; [Rhea:24902](https://www.rhea-db.org/rhea/24902)). This is the canonical EAL-domain chemistry: a **single, Mg²⁺(or Mn²⁺)-dependent hydrolysis of one phosphodiester bond of the cyclic dinucleotide**, opening the ring to give the linear dinucleotide **5′-pGpG**, *not* two GMP molecules. EAL enzymes are strictly specific for c-di-GMP and do not hydrolyse cAMP, cGMP or c-di-AMP; this substrate specificity is a defining property of the family and distinguishes EAL enzymes from the HD-GYP class, which proceeds all the way to 2 GMP.

An important downstream consequence, established in a related organism: pGpG is not an inert end-product. **Oligoribonuclease (Orn) is the primary pGpG-degrading enzyme and is required for c-di-GMP turnover**, because accumulating pGpG product-inhibits the EAL phosphodiesterases themselves ([Orr MW et al., *PNAS* 2015;112:E5048–57, PMID:26305945](https://pubmed.ncbi.nlm.nih.gov/26305945/)). So the physiological output of VC_0658 activity is expected to be coupled to Orn-mediated pGpG clearance.

**Evidence status (important caveat).** The EC number, the reaction, the cofactor and the protein name all rest on **ARBA automatic annotation**, as does the GO molecular-function IEA row (`GO:0071111`, `GO_REF:0000120`, `ARBA:ARBA00090497|EC:3.1.4.52`). Under standard evidence hygiene these are *unvetted predictions* — they repeat a rule, not a measurement. The **independent** support for phosphodiesterase activity is of two better kinds: (i) the curated InterPro/Pfam/PROSITE/SMART signature matches for a complete EAL domain (`PF00563`, `PS50883`, `SM00052`, `IPR001633`, plus `SSF141868` and the EAL FunFam `3.20.20.450:FF:000001` "Cyclic di-GMP phosphodiesterase yahA"), and (ii) the GO_Central **IBA** row for `GO:0071111`, which reflects a PAINT curator's judgement that the phosphodiesterase function was present at ancestral node `PANTHER:PTN002105365` and is inherited by this protein; its donor set is large and includes well-studied *E. coli* and *P. aeruginosa* EAL proteins (P21514/YahA, P77172, P76446, Q9HW35, Q9I1R7 and others).

### 2.2 My own motif analysis supports a catalytically competent EAL domain

Because the public annotation is rule-based, I checked the catalytic apparatus directly against the sequence (analysis run locally on the Q9KU65 sequence; residue numbers are my own and are reproducible from the flat file):

| Landmark | Expected role | Found in Q9KU65 |
|---|---|---|
| `E(A/V)L` signature | start of EAL fold; conserved Glu | **EAL at 447** (`IGVEALIRW`) |
| conserved Glu, loop 6 | Mg²⁺ coordination | **E at 541** (`IELEITESL`) |
| `DDFG(T/A)G` | Mg²⁺-binding, catalytic Asp pair | **DDFGTG at 571** |
| conserved Asp + `KIDRSF` | second metal site / substrate contact | **KIDRSF at 592** |
| `E` of the AEGV block | metal coordination | **AEGV at 627** |
| `QGY` / Gln-Gly-Tyr | catalytic base region | **QGY at 648** |

All six canonical EAL catalytic/metal-binding landmarks are present and intact, within the PROSITE-delimited EAL domain (**residues 413–669**). This is the signature of an **active, not degenerate, phosphodiesterase** — in contrast to the many "enzymatically dead" EAL domains that serve purely as c-di-GMP receptors (the paradigm being LapD, which the Trebino list places in the same five-member *V. cholerae* group as VC_0658). On sequence grounds, **VC_0658 is predicted to be a genuine hydrolase rather than a degenerate binding module.**

### 2.3 The GGDEF domain: intact A-site motif, but no I-site

The GGDEF domain spans **residues 272–404** (PROSITE PS50887) and contains an **intact `GGDEF` active-site motif at residue 321** (context `…LSARI**GGDEF**AVLIP…`) — not the degenerate `GGDxF`/`AGDEF`/`SGDEF` variants common in receptor-only proteins. For comparison, *V. cholerae* VCA0965 carries an **AGDEF** site and was nonetheless shown to synthesize c-di-GMP ([Hunter JL, Severin GB, Koestler BJ, Waters CM. "The *Vibrio cholerae* diguanylate cyclase VCA0965 has an AGDEF active site and synthesizes cyclic di-GMP." *BMC Microbiol* 2014;14:22, PMID:24490592](https://bmcmicrobiol.biomedcentral.com/track/pdf/10.1186/1471-2180-14-22)), so an intact motif is a fortiori permissive for cyclase chemistry.

However, I could **not** find a canonical **`RxxD` I-site** (the allosteric product-inhibition site) in the region upstream of the GGDEF motif. Its absence is consistent with a GGDEF domain that is either (i) catalytically active but not product-inhibited, or (ii) functioning primarily as a **regulatory/GTP-sensing module controlling the adjacent EAL domain** — the mechanism established for *Caulobacter* CC3396, where a degenerate GGDEF domain binds GTP and thereby activates the EAL phosphodiesterase in *cis*. This GGDEF-as-regulator arrangement is a recurring theme in composite GGDEF-EAL proteins and is the single most likely architecture for VC_0658, but **which domain dominates in vivo is unknown and is the key open experimental question.**

A relevant group-level observation: **VC0658 was among the GGDEF-domain genes whose ectopic expression was tested for effects on swimming motility** in the Hunter et al. study (the paper's panel lists "VC0398 VC0653 VC0658 VC0703 VC1934 VC2750 VCA0080…"), but no VC_0658-specific result is reported in the text, so this establishes only that it was screened, not what it did.

## 3. Subcellular localization: inner-membrane anchored, with a periplasmic sensory region

The only GO cellular-component annotation is **`GO:0005886` plasma membrane, `is_active_in`, IBA** from GO_Central (`GO_REF:0000033`, node `PANTHER:PTN002105365`, with donors including *E. coli* P13518/DosP-family and related membrane signalling proteins). There is **no experimental localization study.**

My own hydrophobicity analysis independently supports membrane anchoring. A Kyte–Doolittle scan (window 19) identifies exactly **two** strongly hydrophobic segments:

- **residues 17–36** (`SVFLVSVLLGLCFSFYHTLS`), max KD = 1.82
- **residues 162–181** (`VLLFDLLRNTLLTTILLLFF`), max KD = 1.84

and none thereafter. This yields the classic topology of a membrane-bound c-di-GMP signalling enzyme: a short cytoplasmic N-terminus (1–16), **TM1**, a **periplasmic region of ~125 residues (≈37–161)**, **TM2**, and then the entire catalytic module — GGDEF (272–404) followed by EAL (413–669) — in the **cytoplasm**. The UniProt record does not list TM features (it carries only the two PROSITE domains), so this is my inference, not a database claim; it is nonetheless mutually consistent with the IBA plasma-membrane call and with the donor proteins' architectures.

**Functional reading of the localization.** This topology means **the enzyme does its chemistry on the cytoplasmic face of the inner membrane**, acting on the cytoplasmic c-di-GMP pool, while the periplasmic 37–161 segment is positioned to act as an **extracytoplasmic sensor** — the standard arrangement by which bacteria couple an envelope-perceived cue to local c-di-GMP hydrolysis. The periplasmic region matches no recognized sensory family in InterPro (no PAS, no MASE, no CACHE/GAF signature appears in the cross-references), so **the input signal is unidentified** — this is the second major knowledge gap.

Membrane anchoring is mechanistically significant, not incidental: it is increasingly clear that c-di-GMP signalling in *V. cholerae* operates through spatially local pools rather than a single well-mixed cytoplasmic concentration, which is why individual enzymes can have specific outputs despite the 60-fold enzymatic redundancy ([Zamorano-Sánchez D, Xian W, Lee CK, Salinas M, Thongsomboon W, Cegelski L, Wong GCL, Yildiz FH. "Functional Specialization in *Vibrio cholerae* Diguanylate Cyclases: Distinct Modes of Motility Suppression and c-di-GMP Production." *mBio* 2019;10:e00670-19, PMID:31015332](https://pmc.ncbi.nlm.nih.gov/articles/PMC6479008/)).

## 4. Pathway context: the c-di-GMP motile↔sessile switch

The pathway VC_0658 belongs to is well defined even though the protein's own node in it is not. **c-di-GMP is the master second messenger of the *V. cholerae* motile-to-sessile transition: high c-di-GMP promotes *vps*-dependent biofilm matrix production and represses motility; low c-di-GMP favours flagellar motility and dispersal** ([Teschler JK et al., "Living in the matrix: assembly and control of *Vibrio cholerae* biofilms." *Nat Rev Microbiol* 2015;13:255–268, PMID:25895940](https://pubmed.ncbi.nlm.nih.gov/25895940/); [Conner JG, Zamorano-Sánchez D, Park JH, Sondermann H, Yildiz FH, "The ins and outs of cyclic di-GMP signaling in *Vibrio cholerae*," *Curr Opin Microbiol* 2017](https://www.sciencedirect.com/science/article/am/pii/S1369527416301606)). The signal is read out by effectors including the VpsT and VpsR transcription factors, the MshA pilus machinery and near-surface motility behaviour ([Zamorano-Sánchez et al., *PLoS Pathog* 2015;11:e1005068, PMID:26506097-adjacent work](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1005068)), and a class of c-di-GMP-binding ATPases associated with type II secretion ([Roelofs KG et al., "Systematic Identification of Cyclic-di-GMP Binding Proteins in *Vibrio cholerae*…", *PLoS Pathog* 2015, PMID:26506097](https://pubmed.ncbi.nlm.nih.gov/26506097/)). **As a predicted phosphodiesterase, VC_0658 is expected to sit on the c-di-GMP-lowering, motility-promoting/dispersal side of this switch.**

### 4.1 Transcriptional regulation — the two concrete pieces of gene-level evidence

**RpoS.** Trebino et al. (2025, PMID:40953128) performed ChIP-seq and transcriptomics on the general stress/stationary-phase sigma factor RpoS and report verbatim: *"Of this c-di-GMP RpoS regulon, we found that RpoS directly binds to the promoter of vpvABC and 18 other c-di-GMP-related genes."* VC_0658/*cdgI* is among the genes in that enumerated group, so **direct RpoS promoter binding at *cdgI* is supported by that dataset** — though the paper names VC_0658 only in the Discussion list, not in a VC_0658-specific Results passage, so this should be treated as a group-level, not gene-specific, claim. The biological implication is a **growth-phase/stress input onto *cdgI* expression**, which fits the paper's central thesis of parallel circuits tuning biofilm formation by c-di-GMP level *and* growth phase.

**cAMP–CRP.** The locus is also indexed in [Fong JCN & Yildiz FH, "Interplay between cyclic AMP-cyclic AMP receptor protein and cyclic di-GMP signaling in *Vibrio cholerae* biofilm formation," *J Bacteriol* 2008;190:6646–6659, PMID:18708497, PMCID:PMC2566190](https://pmc.ncbi.nlm.nih.gov/articles/PMC2566190/), which is where the *cdgI* designation appears to originate. Search indexing indicates that this paper reports VC_0658/*cdgI* expression **up ~3-fold in both Δ*cyaA* and Δ*crp* mutants** relative to wild type, and that **deleting *cdgI* in the Δ*crp* background further enhanced biofilm formation** in crystal-violet assays — a result directionally consistent with *cdgI* encoding a c-di-GMP-degrading enzyme whose loss raises c-di-GMP and hence matrix production. **I must flag this explicitly as unverified:** every route to the full text (PMC, Europe PMC, publisher) returned a reCAPTCHA interstitial or HTTP 403, so I could not read the sentences or tables myself, and these statements derive from search-engine indexing of the article rather than from text I confirmed. **They should be checked against the paper before being used as annotation evidence.**

### 4.2 The "cellular response to nitric oxide" annotation is not supported for this protein

GOA carries one biological-process row: **`GO:0071732` cellular response to nitric oxide, `involved_in`, IEA, `GO_REF:0000117`, `ARBA:ARBA00085315`**. In my judgement this annotation is **poorly supported for VC_0658 and should be treated with scepticism.** It is a purely automatic ARBA rule association with no underlying experiment on this protein, and nothing in the record — no NosP domain, no H-NOX domain, no heme-binding signature — gives VC_0658 a plausible NO-sensing module. The *V. cholerae* protein with a genuine, experimentally supported NO connection is a different one: **CdpA**, the NosP-domain-containing c-di-GMP phosphodiesterase ([Tamayo R, Schild S, Pratt JT, Camilli A, "Role of Cyclic Di-GMP during El Tor Biotype *Vibrio cholerae* Infection: Characterization of the In Vivo-Induced Cyclic Di-GMP Phosphodiesterase CdpA," *Infect Immun* 2008;76:1617–1627](https://iai.asm.org/content/76/4/1617)), and it is CdpA, not VC_0658, that figures in the recent demonstration that **NO lowers intracellular c-di-GMP and accelerates biofilm dispersal via rapid motility development** ([Esteves NC, Tao R, Pu Q, Banerjee A, Mathijssen AJTM, Zhu J, *PNAS* 2025 Dec 9;122(49):e2526864122, PMID:41329732, PMCID:PMC12704800](https://pubmed.ncbi.nlm.nih.gov/41329732/); its Fig 4B legend reads *"NO-induced dispersal of mutant lacking the NosP-domain-containing c-di-GMP phosphodiesterase CdpA"*). I searched that paper's abstract and all figure legends and found **no mention of VC0658 or cdgI**; its full text was not reachable (403 / reCAPTCHA), so I cannot exclude an appearance in its Results or supplement. Likewise, a related nitrate/colonization study ([James J, Santos RERS, Watnick PI, *mBio* 2025;16:e0406624, PMID:39998205](https://pubmed.ncbi.nlm.nih.gov/39998205/)) indexes the locus but does not mention it in its abstract or figure legends.

The most probable explanation for the GO row is **ARBA rule propagation from NO-responsive EAL/NosP proteins in other organisms to this unrelated EAL protein** — i.e. an over-propagated electronic inference.

## 5. Evidence summary and the state of knowledge

| Claim | Strength | Basis |
|---|---|---|
| Hybrid GGDEF–EAL protein, one of five in *V. cholerae*; gene name *cdgI* | **Strong** | Trebino 2025 (PMID:40953128) verbatim; KEGG; InterPro/Pfam/PROSITE/SMART |
| Membrane-anchored (inner membrane), catalytic domains cytoplasmic, ~125-aa periplasmic region | **Moderate** (inference) | IBA `GO:0005886` + my two-TM hydrophobicity analysis; no experiment |
| c-di-GMP phosphodiesterase (EC 3.1.4.52), c-di-GMP + H₂O → pGpG, Mg²⁺-dependent | **Moderate** (inference only) | Complete EAL domain with all six catalytic landmarks intact (my analysis); PANTHER IBA; KEGG. **EC/reaction/cofactor in UniProt are ARBA-only** |
| GGDEF domain has intact `GGDEF` motif but no `RxxD` I-site | **Moderate** (my analysis) | Sequence; suggests cyclase-competent or GTP-sensing *cis*-regulator of the EAL domain |
| RpoS binds the *cdgI* promoter | **Moderate, group-level** | Trebino 2025 ChIP-seq; gene named only in Discussion list |
| Repressed by cAMP–CRP; Δ*cdgI* enhances biofilm in Δ*crp* | **Unverified** | Fong & Yildiz 2008 (PMID:18708497) via search indexing only; **full text unreadable — must be confirmed** |
| Involved in cellular response to nitric oxide | **Weak / likely incorrect** | ARBA IEA only; no NO-sensing domain; the NO-responsive PDE in *V. cholerae* is CdpA |
| Any catalytic assay, deletion phenotype, c-di-GMP measurement or localization experiment on VC_0658 | **None found** | Searched Europe PMC full-text index for "VC0658" and "cdgI"; read all accessible hits |

### Open questions a wet-lab experiment would resolve

1. **Which domain is catalytically active in vivo?** Purify the cytoplasmic module (residues ~182–685) and assay c-di-GMP hydrolysis (→ pGpG, by HPLC/MS) and GTP→c-di-GMP synthesis side by side, with and without GTP, testing the CC3396-style model in which the GGDEF domain is a GTP-dependent activator of the EAL domain. Pair with `GGDEF→GGAAF` and `EAL→AAL` point mutants.
2. **What is the periplasmic input signal?** Residues ~37–161 match no known sensory family. A ligand screen, or a chimera swapping this region onto a reporter-coupled EAL protein, would identify the cue.
3. **Is there a phenotype at all, given 60-fold redundancy?** A single Δ*cdgI* mutant may be silent; the informative experiments are combinatorial deletions with the other hybrid enzymes (VC1934, VC2750, VCA0080, *lapD*) plus biofilm, motility and single-cell c-di-GMP biosensor readouts.
4. **Where in the membrane, and does it signal locally?** Fluorescent-fusion localization combined with a c-di-GMP FRET biosensor would test whether *cdgI* drains a local rather than a global pool — the mechanism Zamorano-Sánchez et al. (PMID:31015332) invoke for functional specialization.
5. **Is the cAMP–CRP repression real?** This needs confirmation directly from Fong & Yildiz 2008, since I could not read it.

### Methodological transparency

Primary literature full texts were frequently unreachable in this environment: PMC returned reCAPTCHA interstitials for PMC2566190, PMC12704800, PMC11980369, PMC1797307 and PMC2292854, and the PNAS and ASM publisher sites returned HTTP 403. The Fong & Yildiz 2008 and Esteves 2025 papers in particular warrant a manual read. The UniProt web entry returned an empty JavaScript fallback; I used the REST flat file (`rest.uniprot.org/uniprotkb/Q9KU65.txt`) and the local cached copy instead. All sequence-based claims (TM prediction, catalytic-motif inventory, I-site absence, residue numbering) are my own computations on the Q9KU65 sequence and are stated as inference, not as published results; they are reproducible from the flat file and would be worth formalizing as a reproducible script under `VC_0658-bioinformatics/` if this gene proceeds to full review.

---

**Sources:**
- [Heidelberg JF et al. DNA sequence of both chromosomes of the cholera pathogen Vibrio cholerae. *Nature* 2000;406:477–483 (PMID:10952301)](https://pubmed.ncbi.nlm.nih.gov/10952301/)
- [Trebino MA et al. Parallel regulatory circuits orchestrate biofilm formation in response to c-di-GMP levels and growth phase. *PLoS Genet* 2025;21(9):e1011870 (PMID:40953128)](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1011870)
- [Fong JCN & Yildiz FH. Interplay between cyclic AMP-cyclic AMP receptor protein and cyclic di-GMP signaling in Vibrio cholerae biofilm formation. *J Bacteriol* 2008 (PMID:18708497)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2566190/)
- [Liu X et al. Identification and Characterization of a Phosphodiesterase That Inversely Regulates Motility and Biofilm Formation in Vibrio cholerae. *J Bacteriol* 2010;192:4541–4552 (PMID:20622061)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2937418)
- [Hunter JL et al. The Vibrio cholerae diguanylate cyclase VCA0965 has an AGDEF active site and synthesizes cyclic di-GMP. *BMC Microbiol* 2014;14:22 (PMID:24490592)](https://bmcmicrobiol.biomedcentral.com/track/pdf/10.1186/1471-2180-14-22)
- [Zamorano-Sánchez D et al. Functional Specialization in Vibrio cholerae Diguanylate Cyclases. *mBio* 2019;10:e00670-19 (PMID:31015332)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6479008/)
- [Esteves NC et al. Nitric oxide promotes rapid development of motility to accelerate biofilm dispersal in Vibrio cholerae. *PNAS* 2025;122(49):e2526864122 (PMID:41329732)](https://pubmed.ncbi.nlm.nih.gov/41329732/)
- [James J et al. Carbon source, cell density, and the microbial community control inhibition of V. cholerae surface colonization by environmental nitrate. *mBio* 2025;16:e0406624 (PMID:39998205)](https://pubmed.ncbi.nlm.nih.gov/39998205/)
- [Roelofs KG et al. Systematic Identification of Cyclic-di-GMP Binding Proteins in Vibrio cholerae. *PLoS Pathog* 2015 (PMID:26506097)](https://pubmed.ncbi.nlm.nih.gov/26506097/)
- [Orr MW et al. Oligoribonuclease is the primary degradative enzyme for pGpG in Pseudomonas aeruginosa. *PNAS* 2015 (PMID:26305945)](https://pubmed.ncbi.nlm.nih.gov/26305945/)
- [Teschler JK et al. Living in the matrix: assembly and control of Vibrio cholerae biofilms. *Nat Rev Microbiol* 2015;13:255–268 (PMID:25895940)](https://pubmed.ncbi.nlm.nih.gov/25895940/)
- [Conner JG et al. The ins and outs of cyclic di-GMP signaling in Vibrio cholerae. *Curr Opin Microbiol* 2017](https://www.sciencedirect.com/science/article/am/pii/S1369527416301606)
- [Zamorano-Sánchez D et al. C-di-GMP Regulates Motile to Sessile Transition by Modulating MshA Pili Biogenesis and Near-Surface Motility Behavior. *PLoS Pathog* 2015;11:e1005068](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1005068)
- [Tamayo R et al. Role of Cyclic Di-GMP during El Tor Biotype Vibrio cholerae Infection: Characterization of CdpA. *Infect Immun* 2008;76:1617–1627](https://iai.asm.org/content/76/4/1617)
- [Morita D et al. Whole-Genome Analysis of Clinical Vibrio cholerae O1 in Kolkata and Dhaka. *mBio* 2020 (PMID:33172996)](https://journals.asm.org/doi/full/10.1128/mbio.01227-20)
- [Boin MA & Häse CC. Characterization of Vibrio cholerae aerotaxis. *FEMS Microbiol Lett* 2007;276:193–201 (PMID:17956426)](https://pubmed.ncbi.nlm.nih.gov/17956426/)
- [KEGG entry vch:VC_0658](https://www.genome.jp/entry/vch:VC_0658)
- [UniProtKB Q9KU65 (REST flat file)](https://rest.uniprot.org/uniprotkb/Q9KU65.txt)
- [Rhea:24902 — c-di-GMP hydrolysis](https://www.rhea-db.org/rhea/24902) · [Rhea:24903](https://www.rhea-db.org/rhea/24903)
- [Wikidata Q23435278 — C-di-GMP phosphodiesterase A-like protein VC0658](https://www.wikidata.org/wiki/Q23435278)

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/10952301/
2. https://www.genome.jp/entry/vch:VC_0658
3. https://pubmed.ncbi.nlm.nih.gov/17956426/
4. https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1011870
5. https://journals.asm.org/doi/full/10.1128/mbio.01227-20
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC2937418
7. https://www.rhea-db.org/rhea/24902
8. https://pubmed.ncbi.nlm.nih.gov/26305945/
9. https://bmcmicrobiol.biomedcentral.com/track/pdf/10.1186/1471-2180-14-22
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC6479008/
11. https://pubmed.ncbi.nlm.nih.gov/25895940/
12. https://www.sciencedirect.com/science/article/am/pii/S1369527416301606
13. https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1005068
14. https://pubmed.ncbi.nlm.nih.gov/26506097/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC2566190/
16. https://iai.asm.org/content/76/4/1617
17. https://pubmed.ncbi.nlm.nih.gov/41329732/
18. https://pubmed.ncbi.nlm.nih.gov/39998205/
19. https://rest.uniprot.org/uniprotkb/Q9KU65.txt
20. https://www.rhea-db.org/rhea/24903
21. https://www.wikidata.org/wiki/Q23435278