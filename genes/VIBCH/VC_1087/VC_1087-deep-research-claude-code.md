---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:31:35.924500'
end_time: '2026-10-30T21:35:37.733188'
duration_seconds: 241.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_1087
  gene_symbol: VC_1087
  uniprot_accession: Q9KT18
  protein_description: 'SubName: Full=Response regulator {ECO:0000313|EMBL:AAF94246.1};'
  gene_info: OrderedLocusNames=VC_1087 {ECO:0000313|EMBL:AAF94246.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: CheY-like_superfamily. (IPR011006); Cyclic_di-GMP/3'3'-cGAMP_PDE.
    (IPR052020); HD_GYP_dom. (IPR037522); Sig_transdc_resp-reg_receiver. (IPR001789);
    HD_5 (PF13487)
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
  num_turns: 10
  total_cost_usd: 0.8435922849999999
  session_id: 55286672-8378-4389-885e-c8d9640dc174
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 4
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KT18
- **Protein Description:** SubName: Full=Response regulator {ECO:0000313|EMBL:AAF94246.1};
- **Gene Information:** OrderedLocusNames=VC_1087 {ECO:0000313|EMBL:AAF94246.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CheY-like_superfamily. (IPR011006); Cyclic_di-GMP/3'3'-cGAMP_PDE. (IPR052020); HD_GYP_dom. (IPR037522); Sig_transdc_resp-reg_receiver. (IPR001789); HD_5 (PF13487)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_1087" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_1087' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_1087** (gene ID: VC_1087, UniProt: Q9KT18) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Two papers confirm VC_1087 is the HnoD-type degenerate HD-GYP response regulator. I'm checking a few details before I write the report.

I have enough verified material to write the report now — the second search hit a classifier error, so I'll proceed with what the two primary papers established.

# Research Report: VC_1087 (UniProt Q9KT18) — *Vibrio cholerae* O1 El Tor N16961

## Identity verification

Before research: the target is **Q9KT18**, locus **VC_1087**, 447 aa, from *Vibrio cholerae* serotype O1 str. N16961, annotated by UniProt only as "Response regulator" (`ECO:0000313|EMBL:AAF94246.1` — an unreviewed submitter-derived name, protein existence level 4: Predicted). Domain content from the local UniProt record: a **response-regulatory (REC/CheY-like) receiver domain at residues 12–126** (PROSITE PS50110) with a predicted phosphoacceptor **Asp60**, a **coiled coil at 135–187**, and an **HD-GYP domain at 195–391** (PROSITE PS51832; Pfam PF13487 HD_5; InterPro IPR037522). PANTHER places it in PTHR45228 ("cyclic di-GMP phosphodiesterase TM_0186-related"), subfamily SF8.

This architecture — REC + coiled coil + HD-GYP — is distinctive, and the literature identity is **unambiguous**: two independent primary papers name VC1087 explicitly by locus tag. The gene symbol used in the literature is **hnoD** ("H-NOX associated"). All the literature cited below concerns this protein or its direct orthologs; I found no competing gene with this symbol/locus in another organism. I did **not** find any gene named "VC_1087" in a different organism that could be confused with it.

The one genuine caution is that the two papers analyse the protein from two sides: McKee et al. assayed the *V. cholerae* protein itself, whereas Plate & Marletta characterised the *Shewanella oneidensis* ortholog biochemically and used the *V. cholerae* protein for phosphotransfer and operon-conservation experiments. I flag below which claims rest on which.

## Summary of the primary function

**VC_1087/HnoD is a response regulator whose HD-GYP domain is catalytically dead.** It is not a c-di-GMP phosphodiesterase. Its established function is **allosteric, phospho-switchable inhibition of a partner phosphodiesterase** — the EAL-domain response regulator HnoB (VC1086), encoded immediately upstream in the same operon — making it a negative regulatory node in a two-component c-di-GMP signalling circuit rather than an enzyme.

### It is one of nine HD-GYP proteins in *V. cholerae*, and one of the two inactive ones

McKee, Kariisa, Mudrak, Whitaker & Tamayo systematically dissected the full *V. cholerae* HD-GYP complement (BMC Microbiol. 2014 Oct 25;14:272, PMID:25343965, doi:10.1186/s12866-014-0272-9). Their conclusions place VC1087 clearly:

- Sequence analysis: *"Two, VC1087 and VCA0895, lack an intact HD motif and are expected to be enzymatically inactive."* The HD dyad is the metal-binding, catalytic core of the HD superfamily, so its loss predicts loss of hydrolase chemistry rather than merely reduced rate. (The paper states the motif is not intact but does not enumerate the substituted residues for VC1087.)
- **In vitro:** assayed in *E. coli* lysates with radiolabelled c-di-GMP and TLC readout — *"VC1087 and VCA0895, as expected, were inactive."*
- **In vivo:** assayed by overexpression and scoring the two canonical c-di-GMP outputs — *"As expected, VC1087 and VCA0895, which lack an intact HD motif, had no effects on motility or biofilm formation."* Reduction of cellular c-di-GMP de-represses motility and represses biofilm, so a functional PDE scores in both assays; VC1087 scored in neither.
- The four genuine phosphodiesterases of the family are **VC1295, VC1348, VCA0210 and VCA0681** — VC1087 is not among them.
- Architecture: *"Three HD-GYP domain proteins, VC1087, VC1348 and VCA0210, possess a phosphoreceiver (REC) domain."* This matches the PROSITE REC call at 12–126 in Q9KT18 and is the structural basis for calling it a response regulator.

This is the key negative result for annotation purposes: the UniProt GOA row asserting `GO:0008081 phosphoric diester hydrolase activity` for Q9KT18 is an **ARBA electronic prediction** (`GO_REF:0000117`, `ARBA:ARBA00029117`) propagated from the HD-GYP signature, and it is contradicted by direct biochemistry on this very protein in both lysate and whole-cell assays.

Genetically, loss of VC1087 alone has no detectable phenotype in the assays used. The paper reports that *"Mutation of individual HD-GYP domain genes, as well as combinatorial mutations of multiple HD-GYP domain genes, had no effect on motility or biofilm formation of V. cholerae under the conditions tested,"* and that *"no single HD-GYP domain gene affected intestinal colonization by V. cholerae in an infant mouse model. However, inactivation of multiple HD-GYP domain genes, including the four encoding functional phosphodiesterases, significantly attenuated colonization."* The colonization requirement therefore belongs to the family collectively, driven by the catalytically active members; it is not evidence of a colonization role for VC1087, and the single-mutant data give no positive functional assignment.

### Its actual role: a phosphorylation-controlled brake on the EAL phosphodiesterase HnoB

The positive function comes from Plate & Marletta, "Nitric oxide modulates bacterial biofilm formation through a multi-component cyclic-di-GMP signaling network" (Mol Cell. 2012 Apr 26;46(4):449–460, PMID:22542454, doi:10.1016/j.molcel.2012.03.023). The circuit was worked out in *S. oneidensis*, where the components are the NO sensor H-NOX (HnoX), the histidine kinase **HnoK** (SO2145), and three cognate response regulators: **HnoB** (SO2539, a PAS–EAL phosphodiesterase), **HnoC** (SO2540, a DNA-binding regulator), and **HnoD** (SO2541, the degenerate HD-GYP protein).

Mechanism of the degenerate domain, from that paper:

- *"HnoD includes an HD-GYP domain, which is also a predicted phosphodiesterase (PDE) for c-di-GMP, but the HD-GYP consensus residues crucial for activity are altered to SE-GEP in HnoD."*
- *"The degenerate HD-GYP domain of HnoD lacks phosphodiesterase activity."* Direct comparison against a bona fide HD-GYP enzyme: *"TM0186 completely hydrolyzed c-di-GMP, whereas HnoD displayed no detectable pGpG formation, even after 48 hours."* The 48 h endpoint is important — this is not a slow enzyme but an inactive one.
- Despite being dead as an enzyme, it acts **on** an enzyme: *"Addition of HnoD decreased the rate of HnoB catalyzed c-di-GMP hydrolysis by 40%."* HnoB itself is strongly phospho-activated — *"HK and ATP caused a 50-fold stimulation of HnoB PDE activity"* — and phosphorylation of HnoD by HnoK **abolishes** HnoD's inhibition of HnoB. The two response regulators thus form a feed-forward loop in which the same kinase both switches the PDE on and releases the brake, with c-di-GMP level as the output and biofilm formation as the phenotype.

Two experiments in that paper were performed on the **V. cholerae** proteins specifically, which is what ties VC1087 to this role rather than leaving it as an inference by homology:

- Operon conservation: *"V. cholerae harbors the hnoXK genes (VCA0720/VCA0719) in an isolated operon with hnoB (VC1086) and hnoD (VC1087) grouped into a separate operon containing two additional HKs."* Note *"V. cholerae does not contain an hnoC ortholog"* — the transcriptional arm of the *Shewanella* circuit is absent, so the *V. cholerae* version is the HnoB/HnoD enzymatic module without the DNA-binding output.
- **Direct phosphotransfer with the V. cholerae proteins:** *"Indeed, HnoK rapidly transferred its phosphoryl group to HnoB and HnoD (Figure 2B) consistent with a cognate interaction,"* with the figure legend reading *"Phosphotransfer assay of HnoK from Vibrio cholerae (VCA0719) to HnoB (VC1086) and HnoD (VC1087)."*

That last result is the strongest direct experimental evidence available for Q9KT18: the *V. cholerae* protein is a genuine phosphoacceptor in a two-component relay, receiving phosphoryl group from a specific cognate kinase, VCA0719/HnoK. It substantiates the `GO:0000160 phosphorelay signal transduction system` annotation (currently only IEA/InterPro in the GOA file) with real biochemistry, and it validates the predicted Asp60 phosphoacceptor site. Alignment Figure 4A of the same paper includes *"V. cholerae HnoD (VC1087)"* among the degenerate HD-GYP sequences, though the paper does not print VC1087's own substituted residues — the SE-GEP motif is stated for the *S. oneidensis* protein.

### Genomic context

Beyond the hnoB–hnoD pairing, VC1087 lies at the end of a cluster running from VC1080 to VC1087 that is enriched in two-component proteins carrying c-di-GMP-degrading domains, and this cluster has been studied as the "VC1080 operon" in relation to biofilm formation ([eScholarship](https://escholarship.org/uc/item/2v15p5n9)). I was unable to retrieve that document (the server returned an empty body), so I cannot report its findings for VC1087, and I have not guessed at them. The Plate & Marletta statement that the hnoB/hnoD operon *"contain[s] two additional HKs"* is consistent with this clustering and means VC1087's kinase input may not be restricted to HnoK.

A 2023 study of VC1795 (a Vibrio Pathogenicity Island-2 response regulator) listed VC1087 among predicted upstream regulators and built deletion mutants to test the prediction; I was not able to complete retrieval of that paper, so I report only that the prediction exists and note it is computational, not an established function. Treat it as a lead, not evidence.

## Localization

There is **no experimental localization data** for VC_1087. The inference from architecture is nonetheless firm and worth stating as such: the protein has **no transmembrane segment, no signal peptide, and no lipobox** in the UniProt feature table (only a coiled coil at 135–187 is annotated), and both its functional partners are soluble cytoplasmic enzymes acting on a cytoplasmic second messenger. Its demonstrated activities — accepting a phosphoryl group from a histidine kinase and binding/inhibiting the EAL phosphodiesterase HnoB — are cytoplasmic events. The expected location is therefore the **cytoplasm**, by inference from sequence features and from the compartment of its substrate-free protein–protein interaction, not by assay. The cognate kinase HnoK is itself soluble in this system (the NO sensor H-NOX is a soluble heme protein), so there is no membrane tether implied for the relay.

## Pathway placement

VC_1087 sits in **c-di-GMP turnover control downstream of a two-component relay**, specifically the HnoX/HnoK (NO-sensing) branch in the organisms where that linkage has been tested. Its position is regulatory and one step removed from chemistry:

1. HnoK (VCA0719) autophosphorylates; in *V. cholerae* H-NOX in the Fe(II)–NO state inhibits HnoK autophosphorylation.
2. HnoK phosphorylates **both** HnoB (VC1086, the EAL PDE) and **HnoD (VC1087)** — shown directly for the *V. cholerae* proteins.
3. Unphosphorylated HnoD binds HnoB and suppresses its c-di-GMP hydrolysis (~40% in the *Shewanella* system); phosphorylation of HnoD relieves the suppression, while phosphorylation of HnoB activates it ~50-fold.
4. Net output: modulation of cellular c-di-GMP, hence of biofilm formation and motility.

In GO terms, the well-supported claims are phosphorelay signal transduction (`GO:0000160`, now with direct phosphotransfer evidence), protein phosphorylation-dependent **negative regulation of phosphodiesterase/hydrolase activity**, and participation in **regulation of c-di-GMP metabolic process** — the last two by ortholog biochemistry rather than by assay on Q9KT18. The claim that should **not** be carried is the ARBA-predicted `GO:0008081` hydrolase activity, which the direct assays in McKee et al. refute for this protein.

## What remains unknown

- Whether *V. cholerae* HnoD (VC1087) itself inhibits VC1086/HnoB. The inhibition mechanism was measured on the *Shewanella* pair; for *V. cholerae* only the phosphotransfer step was shown. This is the single most valuable missing experiment: an in vitro PDE assay on purified VC1086 ± VC1087, ± phosphorylation.
- The identity of VC1087's degenerate residues in its own sequence (the SE-GEP motif is the *Shewanella* protein's). This is answerable bioinformatically from the Q9KT18 sequence against the HD-GYP alignment, and would be worth doing locally rather than quoting.
- Whether the two additional histidine kinases in the VC1086/VC1087 operon also feed VC1087, and whether NO regulates this module in *V. cholerae* as it does in *Shewanella*.
- Any physiological condition under which a VC1087 single mutant has a phenotype — none was found in motility, biofilm, or infant-mouse colonization.

## Sources

- [McKee RW, Kariisa A, Mudrak B, Whitaker C, Tamayo R. A systematic analysis of the in vitro and in vivo functions of the HD-GYP domain proteins of Vibrio cholerae. BMC Microbiol. 2014;14:272. PMID:25343965](https://pmc.ncbi.nlm.nih.gov/articles/PMC4212101/)
- [Plate L, Marletta MA. Nitric oxide modulates bacterial biofilm formation through a multi-component cyclic-di-GMP signaling network. Mol Cell. 2012;46(4):449–460. PMID:22542454](https://pmc.ncbi.nlm.nih.gov/articles/PMC3361614)
- [The Role of the VC1080 Operon in Vibrio Cholerae Biofilm Formation (eScholarship) — could not be retrieved](https://escholarship.org/uc/item/2v15p5n9)
- [Evolutional and functional diversification of HD-GYP proteins (Brandeis)](https://scholarworks.brandeis.edu/esploro/outputs/graduate/Evolutional-and-functional-diversification-of-HD-GYP/9923880075901921)
- Local UniProt record `genes/VIBCH/VC_1087/VC_1087-uniprot.txt` (Q9KT18, entry version 138, 28-JAN-2026) and `VC_1087-goa.tsv`.

Two notes on process, since they affect how you use this. First, the full text of the McKee paper was only partly retrievable verbatim — the quotes above are verified, but I did not see the single-mutant colonization result broken out for VC1087 specifically, so the colonization statement I quote is the paper's general one. Second, one search was cut short by a classifier error, which is why the VC1795 lead is reported as unverified rather than dropped or filled in.

## Citations

1. https://escholarship.org/uc/item/2v15p5n9
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC4212101/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC3361614
4. https://scholarworks.brandeis.edu/esploro/outputs/graduate/Evolutional-and-functional-diversification-of-HD-GYP/9923880075901921