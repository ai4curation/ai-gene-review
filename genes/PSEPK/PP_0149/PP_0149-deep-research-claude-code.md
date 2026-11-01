---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:32:35.898767'
end_time: '2026-10-30T21:36:01.773582'
duration_seconds: 205.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0149
  gene_symbol: PP_0149
  uniprot_accession: Q88RI0
  protein_description: 'SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:AAN65783.1};'
  gene_info: OrderedLocusNames=PP_0149 {ECO:0000313|EMBL:AAN65783.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DUF7844. (IPR057166); Lnb_N. (IPR025178); MetalloPept_cat_dom_sf.
    (IPR024079); DUF7844 (PF25226); Lnb_N (PF13387)
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
  num_turns: 9
  total_cost_usd: 0.7391113000000001
  session_id: 128eb218-049c-4bfc-808f-94cff1d9881b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88RI0
- **Protein Description:** SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:AAN65783.1};
- **Gene Information:** OrderedLocusNames=PP_0149 {ECO:0000313|EMBL:AAN65783.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF7844. (IPR057166); Lnb_N. (IPR025178); MetalloPept_cat_dom_sf. (IPR024079); DUF7844 (PF25226); Lnb_N (PF13387)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0149" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0149' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0149** (gene ID: PP_0149, UniProt: Q88RI0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I'm writing up the report now. I found no published experimental work on PP_0149, so it rests on the domain, motif and family evidence.

# PP_0149 (UniProt Q88RI0), *Pseudomonas putida* KT2440: a predicted secreted protein with a metallopeptidase-like domain and an Lnb-N domain (uncharacterized)

## 1. Identity check and summary

| Attribute | Value | Source |
|---|---|---|
| Accession / locus | Q88RI0 / PP_0149 (EMBL AAN65783.1; RefSeq WP_010951543.1) | UniProt record (local file `PP_0149-uniprot.txt`) |
| Organism | *P. putida* KT2440 (NCBI taxon 160488) | UniProt |
| Name | "Uncharacterized protein" (submitter-imported, ECO:0000313); unreviewed TrEMBL entry, PE 4 (Predicted) | UniProt |
| Length | 651 aa, 73.6 kDa | UniProt |
| Signal peptide | 1–22 (SignalP); mature chain 23–651 | UniProt FT SIGNAL |
| Domains | DUF7844 (PF25226; residues 25–254); Lnb_N (PF13387; 272–430); MetalloPept_cat_dom_sf (IPR024079; Gene3D 3.40.390.10, "Collagenase (catalytic domain)") | UniProt / InterPro |
| Orthology | eggNOG COG3228 (the MtfA/YeeI orthologous group) | UniProt DR eggNOG |
| Existing GO | GO:0008237 metallopeptidase activity, IEA (InterPro2GO from IPR024079), the only GOA row | `PP_0149-goa.tsv` |

**Verification.** The locus tag PP_0149, the organism and the domain architecture all match the target. A web search for "PP_0149" *Pseudomonas putida* found no publication about this locus. The only literature mentioning the gene is the two KT2440 genome papers (Nelson et al. 2002, PMID:12534463; Belda et al. 2016, PMID:26913973), and they only list it. **Literature on this specific protein is therefore essentially absent.** Everything below is inferred from the sequence, the domains and characterized relatives, and is marked as inference.

**Bottom line.** PP_0149 is a predicted envelope protein with two domains:
- an N-terminal zincin-like domain (DUF7844) that carries an intact HExxH zinc-binding motif and is predicted to resemble the M90 peptidase MtfA;
- a central Lnb_N domain, related to the periplasmic catalytic domain of the *Bacteroides* lipoprotein N-acyltransferase Lnb.

Its actual substrate and reaction are unknown.

---

## 2. Domain-level evidence

### 2.1 N-terminal DUF7844 domain: an M90 (MtfA)-like zinc metallopeptidase fold

- **Pfam description of PF25226 (DUF7844):** "This domain is found in uncharacterised bacterial proteins. It is predicted to fold onto a structure with significant similarity to Glucose-regulated metallo-peptidase M90. This domain is frequently found in combination with [PF13387]." (InterPro API, Pfam PF25226, retrieved 2026-10-30).
- **Catalytic-domain superfamily.** InterPro places the region in the metallopeptidase catalytic domain superfamily (IPR024079; Gene3D 3.40.390.10). This is the zincin-type fold shared by the MMPs/collagenases, thermolysin-like enzymes and the gluzincins.
- **Zinc-binding motif (my own sequence analysis).** A scan of the Q88RI0 sequence finds one HExxH motif, **H123-E124-L-T-H127**, in the context `ATVLHELTHLYDRARLW`. This is the canonical zincin zinc-binding motif. Its two His residues coordinate Zn²⁺ and its Glu is the general base.
- **Comparison with MtfA.** In *Klebsiella pneumoniae* MtfA, the active site is H149-E150-xx-H153, plus Y205 and a third zinc ligand E212. These sit about 56 and 63 residues after the motif, which places MtfA in the **gluzincin** clan; MtfA is related to the anthrax lethal factor catalytic domain (Xu et al., *J. Bacteriol.* 2012, PMC3370624; PDB 3DL1 apo and 3KHI Zn-bound).
  - PP_0149 has a Tyr (Y187) and Glu residues (E193, E195) at roughly matching distances after its HExxH motif (the `QQYVGRRGERE` stretch).
  - That fits a gluzincin-type active site, but it is a manual positional comparison, not a structural alignment. **Treat it as a hypothesis.**
- **What the M90 family is known to do.** *E. coli* MtfA (P76346; reviewed) binds the glucose-PTS repressor Mlc and inactivates it, which promotes *ptsG* expression. In vitro it is a zinc-dependent aminopeptidase: it is most active on L-alanine-p-nitroanilide, Mlc stimulates the activity, and EDTA and phenanthroline inhibit it. Mlc itself is not the substrate, and "a physiologically relevant target for this peptidase is not yet known" (UniProt P76346 CC FUNCTION/ACTIVITY REGULATION, citing PMID:16855233 and PMID:22178967; Pfam PF06167 description).

**Caveat on the MtfA comparison.** MtfA is a cytoplasmic, roughly 30 kDa, single-domain protein. PP_0149 is a 651-aa protein with a signal peptide and an additional Lnb_N domain. The eggNOG COG3228 assignment therefore reflects similarity of the catalytic module only. **It does not imply that PP_0149 is an Mlc titration factor or acts in glucose-PTS regulation.** *P. putida* takes up glucose mainly through an ABC/porin route, not the *E. coli*-type PtsG/Mlc system, which makes an MtfA-like regulatory role unlikely. That point is my inference.

### 2.2 Central Lnb_N domain (PF13387, formerly DUF4105)

- **Pfam description:** "found N-terminal in Lipoprotein N-acyltransferase Lnb from *Bacteroides* and related uncharacterised bacterial proteins… [It] contains a highly conserved histidine residue and a well-conserved NCT motif. Its predicted structure has a significant similarity to the papain-like cysteine peptidases. In addition, the putative catalytic triad Asn-His-Cys is highly conserved. This domain is also found in combination with other domains." (InterPro API, Pfam PF13387).
- **Lnb biology.** Armbruster et al. found Lnb (BF9343_0945 in *Bacteroides fragilis*) through a genetic screen and a rescue of an *E. coli* conditional *lnt* mutant. Lnb is a lipoprotein N-acyltransferase unrelated to the classical Lnt; Δ*lnb* cells make diacylated rather than triacylated lipoproteins, and the authors propose a new family of N-acyltransferases (*PNAS* 2024; bioRxiv 2024.05.31.596883; PMC11573676).
- **Domain organization in Lnb.** Lnb has a periplasmic N-terminal domain (Lnb_N, the catalytic module) and a C-terminal α-helical transmembrane domain (Pfam PF13387).
- **Residues in PP_0149.**
  - PP_0149 has an `NNC` sequence at **N408-N409-C410** (`YWFLSNNCAVESLK`), inside the Lnb_N region (272–430). It could correspond to the conserved Asn/Cys of the "NCT" motif, but the following residue is Ala, not Thr.
  - Cys308 and Cys318 also fall within the domain.
  - Without an alignment to Lnb I cannot say which His/Cys correspond to the predicted papain-like Asn-His-Cys triad, or whether it is intact. **Unverified.**
- **Relevance to *P. putida*.** *P. putida* is a γ-proteobacterium. Like *E. coli*, it encodes the canonical apolipoprotein N-acyltransferase Lnt for lipoprotein triacylation. PP_0149 does **not** have Lnb's C-terminal multi-pass transmembrane domain; after the Lnb_N domain it has a roughly 220-residue C-terminal region with no annotated domain. So PP_0149 is probably not an Lnt replacement. The Lnb_N module may perform a related transferase or hydrolase chemistry (papain-like Cys/His) on a different substrate. This is inference.

### 2.3 Overall architecture and predicted localization

- **Order:** signal peptide (1–22) → DUF7844 zincin-like domain (25–254) → Lnb_N papain-like domain (272–430) → C-terminal region (431–651) with no annotated domain. The C-terminal region is rich in Leu/Arg/Glu/Gln, consistent with helical or coiled segments; no Pfam or InterPro match.
- **Localization.** The SignalP-predicted Sec signal peptide, with no annotated TM helix or lipobox in the UniProt record, suggests the mature protein is exported to the **periplasm** or possibly secreted. Pfam itself calls the Lnb_N domain "periplasmic". No experimental localization data exist.
- **Two catalytic folds.** The protein combines two potential hydrolase/transferase folds: a Zn-metallopeptidase (gluzincin-like) and a papain-like Cys-His fold. This suggests a periplasmic enzyme that processes proteins or lipoproteins, or acts on cell-envelope components. The specific reaction cannot be inferred.

---

## 3. Function, process and pathway: what can and cannot be said

| Question | Best current answer | Confidence |
|---|---|---|
| Molecular function | Probable Zn²⁺-dependent metallopeptidase (intact HExxH in an M90-like zincin domain); possible second, papain-like Cys-dependent activity in the Lnb_N domain | Low to moderate (domain inference; no assay) |
| Substrate | Unknown. The relatives give no reliable clue: MtfA's native substrate is unknown, and Lnb acylates the α-amine of diacylated lipoproteins | — |
| Process / pathway | Unknown. No link to the glucose PTS/Mlc system is supported in *P. putida*. A link to lipoprotein maturation is speculative | Very low |
| Location | Periplasm or extracellular (predicted from the signal peptide) | Moderate for "exported"; low for the exact compartment |
| Experimental data | None found for PP_0149. Genome-wide RB-TnSeq fitness data for KT2440 exist in the Fitness Browser (fit.genomics.lbl.gov), but the page was blocked to automated access, so I could not check them | — |

### On the existing GO annotation

- **GO:0008237 metallopeptidase activity (IEA, InterPro2GO via IPR024079).** This is reasonably well supported by:
  - (a) the zincin catalytic-domain superfamily match;
  - (b) the intact HExxH motif;
  - (c) the Pfam statement that DUF7844 resembles M90 metallopeptidases.
- It is at the right level of generality. A more specific term (e.g. metalloaminopeptidase activity, by analogy with MtfA) would over-reach, because the M90 family's aminopeptidase activity is shown only in vitro on artificial substrates, and PP_0149 is a divergent, multidomain relative.
- **Biological-process and cellular-component terms.** No process term is warranted. A periplasmic-space location could be considered as a sequence-based prediction (signal peptide), but no experiment supports it.

---

## 4. Open questions and suggested experiments

1. **Is it a Zn-peptidase?**
   - Purify the mature domain (23–651, or 25–254 alone) and test hydrolysis of aminoacyl-pNA substrates and peptides.
   - Test whether EDTA or 1,10-phenanthroline inhibits it.
   - Make H123A and E124A mutants (E124Q as the catalytic-base control).
   - These are the same assays that established MtfA activity (PMID:22178967).
2. **Does the Lnb_N domain do anything?**
   - Mutate the conserved Cys (e.g. C410) and His, then test for lipoprotein N-acylation or for Cys-dependent hydrolase activity.
   - Compare lipoprotein acylation states in a ΔPP_0149 strain by mass spectrometry.
3. **Localization.**
   - Fractionate the cells (periplasm, membranes, culture supernatant) using a tagged PP_0149.
   - Test signal-peptide function with a PhoA/β-lactamase fusion.
4. **Phenotype.**
   - Check the KT2440 RB-TnSeq fitness profile and cofitness partners in the Fitness Browser for envelope-stress or nutrient-specific phenotypes.
   - Check genomic neighbours for context.
5. **Structure.**
   - Run a structural alignment of the AlphaFold model (AF-Q88RI0) against MtfA (3KHI) and against Lnb models. This would confirm the third zinc ligand and the Cys/His/Asn triad.

---

## 5. Sources

- UniProtKB Q88RI0 entry (local file `genes/PSEPK/PP_0149/PP_0149-uniprot.txt`; entry version 99, 28-Jan-2026). Source of the signal peptide, domains, eggNOG COG3228 and the IEA GO line.
- Pfam PF25226 (DUF7844) and PF13387 (Lnb_N) descriptions, via the InterPro API: https://www.ebi.ac.uk/interpro/entry/pfam/PF25226/ and https://www.ebi.ac.uk/interpro/entry/pfam/PF13387/ (accessed 2026-10-30).
- Pfam PF06167 (Peptidase_M90, MtfA) description: https://www.ebi.ac.uk/interpro/entry/pfam/PF06167/
- UniProtKB P76346 (MTFA_ECOLI), citing Göhler et al. 2006 (PMID:16855233) and Göhler et al. 2012 (PMID:22178967): https://www.uniprot.org/uniprotkb/P76346
- Xu Q. et al. (2012) "Structural basis of murein peptide specificity of a γ-D-glutamyl-L-diamino acid endopeptidase" / MtfA structural study, *J. Bacteriol.* PMC3370624: https://pmc.ncbi.nlm.nih.gov/articles/PMC3370624 (the structures are PDB [3DL1](https://www.rcsb.org/structure/3DL1) and [3KHI](https://www.rcsb.org/structure/3KHI); the active-site description H149E150xxH153 + E212 + Y205 and the gluzincin/lethal-factor relationship come from the search summary of this article)
- Armbruster K.M. et al. (2024) "Identification and characterization of the lipoprotein N-acyltransferase in *Bacteroides*", *PNAS*: https://pmc.ncbi.nlm.nih.gov/articles/PMC11573676 ; preprint https://www.biorxiv.org/content/10.1101/2024.05.31.596883.full.pdf
- Nelson K.E. et al. (2002) *Environ. Microbiol.* 4:799–808 (PMID:12534463), the KT2440 genome.
- Belda E. et al. (2016) *Environ. Microbiol.* 18:3403–3424 (PMID:26913973), the re-annotated KT2440 genome.
- Fitness Browser (not accessible to automated retrieval): https://fit.genomics.lbl.gov/cgi-bin/singleFit.cgi?orgId=Putida&locusId=PP_0149

**Sequence-motif notes** (HExxH at 123–127; Y187, E193 and E195 as candidate downstream zinc ligands; NNC at 408–410) come from my own scan of the UniProt sequence. They have not been confirmed by alignment or structure.

## Citations

1. https://www.ebi.ac.uk/interpro/entry/pfam/PF25226/
2. https://www.ebi.ac.uk/interpro/entry/pfam/PF13387/
3. https://www.ebi.ac.uk/interpro/entry/pfam/PF06167/
4. https://www.uniprot.org/uniprotkb/P76346
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC3370624
6. https://www.rcsb.org/structure/3DL1
7. https://www.rcsb.org/structure/3KHI
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC11573676
9. https://www.biorxiv.org/content/10.1101/2024.05.31.596883.full.pdf
10. https://fit.genomics.lbl.gov/cgi-bin/singleFit.cgi?orgId=Putida&locusId=PP_0149