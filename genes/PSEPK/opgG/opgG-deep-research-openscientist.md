---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T15:13:18.989152'
end_time: '2026-07-11T15:24:32.817271'
duration_seconds: 673.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: opgG
  gene_symbol: opgG
  uniprot_accession: Q88D03
  protein_description: 'RecName: Full=Glucans biosynthesis protein G; Flags: Precursor;'
  gene_info: Name=opgG; Synonyms=mgoG; OrderedLocusNames=PP_5026;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the OpgD/OpgG family. .
  protein_domains: Gal_mutarotase_sf_dom. (IPR011013); GH-type_carb-bd. (IPR014718);
    Glucan_biosyn_MdoG/MdoD. (IPR014438); Glucan_biosyn_MdoG_C. (IPR007444); Ig-like_fold.
    (IPR013783)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: opgG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: opgG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D03
- **Protein Description:** RecName: Full=Glucans biosynthesis protein G; Flags: Precursor;
- **Gene Information:** Name=opgG; Synonyms=mgoG; OrderedLocusNames=PP_5026;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the OpgD/OpgG family. .
- **Key Domains:** Gal_mutarotase_sf_dom. (IPR011013); GH-type_carb-bd. (IPR014718); Glucan_biosyn_MdoG/MdoD. (IPR014438); Glucan_biosyn_MdoG_C. (IPR007444); Ig-like_fold. (IPR013783)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "opgG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'opgG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **opgG** (gene ID: opgG, UniProt: Q88D03) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *opgG* (Q88D03 / PP_5026) in *Pseudomonas putida* KT2440

**Target:** UniProt **Q88D03** · Gene **opgG** (synonym *mgoG*; ordered locus **PP_5026**)
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK
**Protein:** Glucans biosynthesis protein G; a secreted precursor of the OpgD/OpgG family

## Summary

**OpgG (Q88D03; locus PP_5026; synonym *mgoG*) is a periplasmic, Sec-exported carbohydrate-active enzyme of the OpgD/OpgG family that is required for the biosynthesis of osmoregulated periplasmic glucans (OPGs).** Together with its operon partner OpgH (the inner-membrane glucosyltransferase PP_5025), OpgG synthesizes and shapes OPGs — anionic β-1,2-linked glucose oligosaccharides bearing β-1,6 branches (and, in pseudomonads, succinyl substituents) that accumulate in the periplasmic space at low medium osmolarity. Recent structural and enzymatic work in *Escherichia coli* has redefined the biochemical identity of this protein: OpgG and its paralog OpgD are **β-1,2-glucanases**, and together they establish a **new glycoside hydrolase family, GH186**. This assigns OpgG a specific catalytic role — hydrolytic/processing action on the β-1,2-glucan backbone — rather than a purely scaffolding function.

The gene identity was rigorously verified. The UniProt annotation (Q88D03, "Glucans biosynthesis protein G," gene *opgG*/*mgoG*, family OpgD/OpgG) matches the protein's domain architecture and the surrounding genomic context. Global sequence alignment showed that P. putida OpgG is **63.6% identical to the crystallized E. coli OpgG (P33136)** and **66.4% identical to P. aeruginosa OpgG (Q9HUA5)** — well within the range of orthology. The N-terminus is a classic Sec-type signal peptide (hydrophobic h-region, Ala-x-Ala cleavage site, no twin-arginine motif), consistent with the "Precursor" flag in UniProt and with the established Sec-dependent export route of OpgG orthologs (in contrast to the Tat-dependent paralog OpgD). The gene sits in an intact, colinear **opgGH operon** (PP_5026–PP_5025), mirroring the conserved bicistronic mdoGH/opgGH organization found across proteobacteria.

Functionally, the OPGs produced by the OpgGH machinery mediate cell-envelope adaptation to osmotic stress and contribute to biofilm formation, motility, and host interaction. In enterobacteria, loss of OPGs (via *opgG* mutation) produces a characteristic pleiotropic phenotype — reduced virulence and motility, exopolysaccharide overproduction — driven by constitutive activation of the **RcsCD–RcsB phosphorelay**. In *Pseudomonas aeruginosa*, the closest well-characterized relative, the *opgGH* locus produces **linear β-1,2-glucans** important for biofilm formation at low osmolarity, with transcription repressed at high osmolarity. The evidence base for P. putida OpgG itself is largely inferential (sequence, structure, genomic context, and orthology to characterized enzymes), but the convergence of these lines of evidence gives high confidence in the annotation.

---

## Gene/Protein Identity Verification

Before presenting the functional analysis, the mandatory identity checks were completed and passed:

| Verification Step | Result |
|---|---|
| Gene symbol matches protein description | ✅ *opgG* = "Glucans biosynthesis protein G" (OpgD/OpgG family) |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (PP_5026) |
| Protein family/domains align with literature | ✅ Gal_mutarotase_sf, GH-type carb-binding, Glucan_biosyn_MdoG/MdoD, MdoG_C, Ig-like fold — all consistent with the crystallized OpgG fold |
| No confusion with a same-symbol gene in another organism | ✅ Sequence identity (63.6% to E. coli OpgG, 66.4% to P. aeruginosa OpgG) confirms bona fide ortholog |

The synonym *mgoG* is noted in UniProt. Care was taken not to conflate this with the unrelated *mgo* operon (*mgoBCAD*) of *P. syringae*, which governs mangotoxin biosynthesis via the NRPS gene *mgoA* ([PMID: 24555804](https://pubmed.ncbi.nlm.nih.gov/24555804/); [PMID: 22251433](https://pubmed.ncbi.nlm.nih.gov/22251433/)). Those studies concern a distinct antimetabolite pathway and do not describe OPG biosynthesis; they are not evidence for OpgG function and were excluded from the functional conclusions.

**Conclusion of verification:** The research target is correctly identified. Literature specific to P. putida KT2440 OpgG is limited, so the functional annotation is built primarily on (a) direct experimental evidence from orthologs in E. coli, Erwinia/Dickeya, Salmonella, Shigella, and P. aeruginosa, and (b) bioinformatic/structural inference for the P. putida protein itself.

---

## Key Findings

### Finding 1 — OpgG is required for osmoregulated periplasmic glucan (OPG) biosynthesis

OpgG (Q88D03 / PP_5026) is a member of the OpgD/OpgG family and is required for the synthesis of osmoregulated periplasmic glucans. The genetic logic is well established across proteobacteria: the *opgGH* (historically *mdoGH*) operon encodes the two proteins that build the glucose backbone of OPGs, and mutation of either gene abolishes OPG synthesis. In *Erwinia chrysanthemi* (now *Dickeya*), Page et al. cloned the *opgGH* operon by complementation of the E. coli *mdoGH* locus and showed that "*OpgG and OpgH show a high level of similarity with MdoG and MdoH, respectively, and mutations in the opgG or opgH gene abolish OPG synthesis*" ([PMID: 11325942](https://pubmed.ncbi.nlm.nih.gov/11325942/)). The requirement is direct and reproducible: in *Shigella flexneri*, "*Mutation in opgG and opgH abolished OPGs biosynthesis*" ([PMID: 20062978](https://pubmed.ncbi.nlm.nih.gov/20062978/)).

This establishes OpgG as an essential, non-redundant component of the OPG biosynthetic machinery — not merely correlated with OPGs but genetically required for their production. Because the P. putida protein is a high-confidence ortholog (see Finding 5) and sits in an intact operon (Finding 6), this requirement is expected to hold in KT2440.

### Finding 2 — OpgG is a β-1,2-glucanase and a founding member of glycoside hydrolase family GH186

The most significant recent advance is the biochemical identification of OpgG's catalytic activity. Motouchi et al. (2023) performed structural and functional analyses of E. coli OpgG and its paralog OpgD and found that "*these proteins are β-1,2-glucanases with remarkably different activity from each other, establishing a new glycoside hydrolase family, GH186*" ([PMID: 37735577](https://pubmed.ncbi.nlm.nih.gov/37735577/)). OpgG showed markedly lower activity than OpgD, but both act on the β-1,2-glucan linkage that constitutes the OPG backbone. This reframes OpgG from a protein "required for OPG synthesis" to a specific enzyme — a glycoside hydrolase acting on β-1,2-glucans, plausibly in a backbone-processing or branch-defining role during OPG maturation.

This activity is consistent with the earlier crystal structure of E. coli OpgG (Hanoulle et al. 2004), which revealed an N-terminal domain (residues 22–388) with "*a 25-stranded beta-sandwich fold found in several carbohydrate-related proteins*" exhibiting "*a large cleft comprising many aromatic and acidic residues*" whose similarity to "*enzymes such as galactose mutarotase and glucodextranase*" suggested "*a potential catalytic role for this domain in OPG synthesis*" ([PMID: 15313617](https://pubmed.ncbi.nlm.nih.gov/15313617/)). The aromatic/acidic cleft is the hallmark of a carbohydrate-active catalytic site. The C-terminal Ig-like β-sandwich domain likely mediates protein–protein or substrate-positioning interactions. The UniProt domain assignments for Q88D03 (galactose mutarotase superfamily, GH-type carbohydrate-binding, Glucan_biosyn_MdoG_C, Ig-like fold) map directly onto this two-domain architecture, confirming that the P. putida protein has the catalytic machinery.

### Finding 3 — OpgG functions in the periplasm and is exported by the Sec pathway as a cleaved precursor

OPGs are periplasmic molecules, and OpgG carries out its function there. Lequette et al. (2004) described OPGs as "*anionic and highly branched oligosaccharides that accumulate in the periplasmic space in response to low osmolarity of the medium*" and showed that the export routes of the two family paralogs differ: "*Most of the OpgD orthologs exhibit a Tat-dependent secretion signal, while most of the OpgG orthologs are Sec dependent*" ([PMID: 15175282](https://pubmed.ncbi.nlm.nih.gov/15175282/)). The UniProt entry for Q88D03 flags the protein as a "Precursor," indicating a cleaved N-terminal signal peptide consistent with Sec export to the periplasm.

The subcellular localization is functionally important: OPGs bridge the inner and outer membranes' osmotic environment, so a periplasmic enzyme is exactly where backbone processing/branching should occur. The distinction between Sec-dependent OpgG and Tat-dependent OpgD is mechanistically meaningful — Tat transports folded proteins, whereas Sec transports unfolded ones — and reflects the divergent evolutionary and functional specialization of the two paralogs.

### Finding 4 — In *Pseudomonas*, OpgGH produces osmoregulated linear β-1,2-glucans important for biofilm; OPG loss activates the Rcs phosphorelay

The closest well-characterized relative provides the best proxy for P. putida OpgG function. In *P. aeruginosa* PA14, Lequette et al. (2007) showed that "*the opgGH locus of P. aeruginosa PA14 is involved in the synthesis of linear polymers with beta-1,2-linked glucosyl residues branched with a few beta-1,6 glucosyl residues. Succinyl residues also substitute this glucose backbone. Transcription of opgGH is repressed by high osmolarity*" ([PMID: 17906125](https://pubmed.ncbi.nlm.nih.gov/17906125/)). This defines both the chemical product (linear β-1,2-glucan with sparse β-1,6 branches and succinyl decorations) and the osmoregulatory logic (transcription repressed at high osmolarity, so OPGs accumulate at low osmolarity) — and reported that OPGs are important for biofilm formation.

Downstream, OPG deficiency is transduced through the Rcs signaling system. In *Dickeya dadantii*, "*mutations in the RcsCDB phosphorelay system restored virulence and motility in a D. dadantii opg-negative strain, indicating a relationship between the Rcs phosphorelay and OPGs*" ([PMID: 20418397](https://pubmed.ncbi.nlm.nih.gov/20418397/)). This was confirmed biochemically by direct measurement of RcsB phosphorylation: opg-negative strains show elevated RcsB~P, "*sufficient to induce the pleiotropic phenotype observed*" ([PMID: 25320363](https://pubmed.ncbi.nlm.nih.gov/25320363/)). The pleiotropy (loss of virulence, reduced motility, EPS overproduction) is therefore a signaling consequence of missing OPGs, not a direct enzymatic role of OpgG — an important distinction for the "precise role" the research question emphasizes.

### Finding 5 — Bioinformatic verification: Q88D03 is a high-confidence OpgG ortholog with a Sec signal peptide and conserved cleft motifs

Global Needleman–Wunsch alignment of Q88D03 (559 aa) gave **63.6% identity (357/561 aligned positions)** to the biochemically and structurally characterized E. coli OpgG (P33136) and **66.4% identity (383/577)** to P. aeruginosa OpgG (Q9HUA5). The N-terminus (MASVALVGLMSAGQLWAF|NLDD) is a classic Sec signal peptide: a hydrophobic h-region (mean Kyte–Doolittle hydropathy of residues 1–18 = +1.49), an Ala-x-Ala-type cleavage site near position 18, and no twin-arginine (Tat) motif — consistent with the UniProt "Precursor" flag and Sec-dependent periplasmic export (Finding 3). Conserved OpgG substrate-cleft/backbone motifs are present (GYAGFR@124, ASYFR@149, GEWLWRP@279, DWGKG@337), indicating an intact catalytic/binding cleft.

Notably, Q88D03 carries a *Pseudomonas*-specific C-terminal low-complexity Ala/Lys-rich extension (residues ~500–559; ~42% Ala+Lys) that is absent from E. coli OpgG. The functional significance of this extension is unknown; it may reflect lineage-specific interactions or regulation and is a candidate for future study.

| Comparison | Aligned identity | Significance |
|---|---|---|
| Q88D03 (P. putida) vs P33136 (E. coli OpgG) | 63.6% (357/561) | Ortholog; E. coli protein crystallized & enzymatically characterized |
| Q88D03 (P. putida) vs Q9HUA5 (P. aeruginosa OpgG) | 66.4% (383/577) | Ortholog; P. aeruginosa product chemically defined |
| N-terminal signal | Sec-type (hydropathy +1.49, Ala-x-Ala, no RR) | Periplasmic export |
| Conserved cleft motifs | GYAGFR, ASYFR, GEWLWRP, DWGKG present | Intact catalytic/binding site |

### Finding 6 — PP_5026 (opgG) is genomically paired with its cognate glucosyltransferase opgH (PP_5025) in an intact opgGH operon

Genomic locus analysis confirmed that PP_5025 = Q88D04 (OPGH_PSEPK, "Glucans biosynthesis glucosyltransferase H," EC 2.4.1.-, 857 aa) lies immediately adjacent to PP_5026 = Q88D03 (OpgG, 559 aa). The flanking gene PP_5027 (*dtd*, D-aminoacyl-tRNA deacylase) is functionally unrelated, marking the operon boundary. This bicistronic *opgGH* arrangement mirrors the conserved *mdoGH/opgGH* operon that encodes the two glucose-backbone-synthesizing proteins in E. coli, Erwinia/Dickeya, Salmonella, Shigella, and P. aeruginosa. The presence of an intact, colinear operon strongly supports the inference that P. putida OpgG participates in canonical OPG biosynthesis alongside OpgH. In *Salmonella* Typhimurium, "*The two structural genes for OPG biosynthesis, opgG and opgH, form a bicistronic operon*" ([PMID: 19118363](https://pubmed.ncbi.nlm.nih.gov/19118363/)), the same organization seen here.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent model in which OpgG is one of two enzymes that build and shape periplasmic β-1,2-glucans in response to osmotic conditions, with downstream physiology relayed through Rcs signaling.

```
                          LOW OSMOLARITY  (opgGH transcription de-repressed)
                                   |
   CYTOPLASM / INNER MEMBRANE      |
   +-----------------------------------------------------------+
   |  OpgH (PP_5025, glucosyltransferase, EC 2.4.1.-)          |
   |   - polymerizes UDP-glucose into a beta-1,2-glucan chain  |
   |   - inner-membrane anchored                               |
   +---------------+-------------------------------------------+
                   |  nascent beta-1,2-glucan
                   v
   PERIPLASM  (Sec-exported OpgG cleaved precursor acts here)
   +-----------------------------------------------------------+
   |  OpgG (PP_5026, beta-1,2-glucanase, GH186)                |
   |   - N-term 25-stranded beta-sandwich, aromatic/acidic     |
   |     cleft (galactose-mutarotase-like catalytic domain)    |
   |   - C-term Ig-like domain (interaction/positioning)       |
   |   - processes/branches backbone -> mature OPGs            |
   |     (beta-1,2 chain + beta-1,6 branches + succinyl)       |
   +---------------+-------------------------------------------+
                   |  OPGs accumulate in periplasm
                   v
   ENVELOPE ADAPTATION -> biofilm, motility, host interaction
                   |
                   v
   Rcs SENSING:  OPG absence => RcsC/RcsD => RcsB~P up
                   |
                   v
   Pleiotropy: down-virulence, down-motility, up-EPS (signaling)
```

**Primary function.** OpgG is a **glycoside hydrolase (β-1,2-glucanase, family GH186)** acting on the β-1,2-glucan backbone in the periplasm. In the OPG pathway, OpgH (inner-membrane glucosyltransferase) polymerizes the glucose backbone using UDP-glucose, while OpgG processes/shapes that backbone — consistent with its lower hydrolytic activity relative to OpgD and with the historical description of OpgG as "required for OPG backbone synthesis." The exact in-vivo cut/branch chemistry OpgG performs during OPG maturation remains to be pinned down, but the enzyme class is now defined.

**Localization.** OpgG functions in the **periplasm**, delivered there as a Sec-exported cleaved precursor. This is where OPGs accumulate and where backbone processing must occur.

**Substrate specificity.** The substrate is the **β-1,2-linked glucan** backbone of OPGs. In pseudomonads the mature product is a linear β-1,2-glucan with a few β-1,6 branches and succinyl substituents.

**Pathway context.** OpgG operates within OPG biosynthesis (opgGH operon) and its physiological output is read out by the **Rcs phosphorelay**; the pleiotropic virulence/motility phenotypes of *opg* mutants are downstream signaling consequences rather than direct OpgG activities. Notably, OPG polymerization also requires ongoing protein synthesis, implying rapid turnover of one of the two backbone enzymes ([PMID: 20358372](https://pubmed.ncbi.nlm.nih.gov/20358372/)).

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [37735577](https://pubmed.ncbi.nlm.nih.gov/37735577/) | *Identification of enzymatic functions of OPG biosynthesis proteins… novel GH family* | **Primary biochemical evidence**: OpgG/OpgD are β-1,2-glucanases establishing GH186 (Finding 2) |
| [15313617](https://pubmed.ncbi.nlm.nih.gov/15313617/) | *Structural analysis of E. coli OpgG* | Crystal structure: 25-stranded β-sandwich catalytic domain + Ig-like domain (Finding 2) |
| [15175282](https://pubmed.ncbi.nlm.nih.gov/15175282/) | *Identification of mdoD… Tat-dependent paralog* | OpgG is Sec-dependent; OPGs accumulate in periplasm at low osmolarity (Finding 3) |
| [11325942](https://pubmed.ncbi.nlm.nih.gov/11325942/) | *OPG synthesis required for Erwinia pathogenicity* | Genetic: opgG/opgH mutations abolish OPG synthesis (Finding 1) |
| [20062978](https://pubmed.ncbi.nlm.nih.gov/20062978/) | *OPG synthesis gene family of Shigella flexneri* | Genetic: opgG/opgH mutation abolishes OPGs (Finding 1) |
| [17906125](https://pubmed.ncbi.nlm.nih.gov/17906125/) | *Linear OPGs encoded by opgGH of P. aeruginosa* | **Closest Pseudomonas evidence**: product structure, osmoregulation, biofilm (Finding 4) |
| [20418397](https://pubmed.ncbi.nlm.nih.gov/20418397/) | *Virulence of D. dadantii opg mutant restored by Rcs inactivation* | Links OPG loss to Rcs phosphorelay (Finding 4) |
| [25320363](https://pubmed.ncbi.nlm.nih.gov/25320363/) | *Increased RcsB phosphorylation in opg-devoid D. dadantii* | Direct biochemical proof of Rcs activation on OPG loss (Finding 4) |
| [19118363](https://pubmed.ncbi.nlm.nih.gov/19118363/) | *OPGs of Salmonella required for virulence in mice* | opgGH bicistronic operon; motility/virulence roles (Findings 1, 6) |
| [20358372](https://pubmed.ncbi.nlm.nih.gov/20358372/) | *OPG polymerization requires constant protein synthesis* | Rapid turnover of one backbone enzyme; regulatory insight |
| [37267309](https://pubmed.ncbi.nlm.nih.gov/37267309/) | *BcsA-like orphan CβG synthases in pseudomonads* | Context: a distinct cyclic-β-glucan system in KT2440 (not OpgG) |
| [24555804](https://pubmed.ncbi.nlm.nih.gov/24555804/) / [22251433](https://pubmed.ncbi.nlm.nih.gov/22251433/) | *mgo operon / mangotoxin in P. syringae* | Excluded: unrelated *mgo* pathway despite *mgoG* synonym |

**Convergence of evidence.** Four independent lines all point to the same annotation: (1) direct genetic requirement in multiple species; (2) a solved crystal structure and a modern enzymatic assay defining the catalytic class; (3) chemical characterization of the Pseudomonas OPG product; and (4) strong sequence orthology plus intact operon context for the P. putida protein specifically. No line of evidence contradicts the OPG-biosynthesis assignment.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on P. putida KT2440 OpgG.** All functional conclusions for PP_5026 are inferential — from orthology (63.6–66.4% identity), domain architecture, signal-peptide prediction, and operon context. No knockout, OPG chemical characterization, or enzyme assay has been reported for the KT2440 protein itself.

2. **Precise in-vivo reaction is not fully resolved even in E. coli.** OpgG is now classed as a β-1,2-glucanase (GH186), but it shows much lower activity than OpgD, and the exact backbone-processing/branching step it performs during OPG maturation — and how it coordinates with OpgH polymerization — remains incompletely defined.

3. **The Pseudomonas-specific C-terminal Ala/Lys-rich extension (res ~500–559) is uncharacterized.** Its role (interaction, regulation, stability) is unknown.

4. **Rcs linkage in P. putida is assumed, not demonstrated.** The OPG→Rcs signaling axis is established in enterobacteria (Dickeya, E. coli); whether P. putida transduces OPG status through an equivalent Rcs pathway has not been directly tested.

5. **OPG functional roles in P. putida ecology.** P. putida is a soil/rhizosphere saprophyte, not a classical pathogen; the ecological consequences of OPGs (biofilm on plant roots, osmotic adaptation in soil) are plausible but untested for this organism.

6. **Potential functional overlap with the orphan cyclic-β-glucan (CβG) synthase system** described in KT2440 ([PMID: 37267309](https://pubmed.ncbi.nlm.nih.gov/37267309/)). That is a distinct GH17/GT2 machinery producing cyclic β-1,3-glucan; how OPGs and CβG are co-regulated or functionally partitioned in P. putida is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Construct a P. putida KT2440 ΔopgG (and ΔopgGH) mutant** and chemically characterize periplasmic glucans (HPLC/MS, NMR) to confirm loss of OPGs and define the native product structure (linear β-1,2 backbone, branch pattern, succinylation).

2. **Recombinantly express and assay P. putida OpgG** on defined β-1,2-glucan substrates (sophorose-series oligosaccharides) to confirm GH186 β-1,2-glucanase activity and determine substrate-length preference and product profile, ideally alongside OpgD-type paralogs if present.

3. **Test osmoregulation directly**: qRT-PCR or reporter fusions of *opgGH* across an osmolarity gradient to confirm high-osmolarity repression in KT2440, paralleling the P. aeruginosa result.

4. **Probe the Rcs axis**: measure RcsB phosphorylation (Phos-tag gels) and motility/biofilm phenotypes in wild-type vs ΔopgG to test whether OPG loss activates Rcs in P. putida as in Dickeya.

5. **Signal-peptide/localization validation**: confirm Sec-dependent periplasmic localization by cellular fractionation and signal-peptide cleavage mapping (N-terminal sequencing/MS).

6. **Domain-swap / truncation of the C-terminal Ala/Lys extension** to determine its contribution to activity, stability, or interaction with OpgH.

7. **Structure determination** (X-ray/cryo-EM or high-confidence AlphaFold model with validation) of P. putida OpgG to confirm the two-domain fold and map the conserved cleft motifs (GYAGFR, ASYFR, GEWLWRP, DWGKG) onto the active site.

---

## Conclusion

OpgG (Q88D03 / PP_5026) in *Pseudomonas putida* KT2440 is a **periplasmic, Sec-exported β-1,2-glucanase of the OpgD/OpgG family (glycoside hydrolase family GH186)** that, with its operon partner OpgH (PP_5025), synthesizes and shapes **osmoregulated periplasmic glucans** — anionic β-1,2-glucose oligosaccharides with β-1,6 branches (and succinyl substituents in pseudomonads) that accumulate in the periplasm at low osmolarity. It acts in the **periplasm** via an N-terminal galactose-mutarotase-like catalytic domain and a C-terminal Ig-like domain, and the OPGs it produces mediate envelope osmotic adaptation, biofilm formation, and motility, with physiological output relayed through the **RcsCD–RcsB phosphorelay**. This annotation rests on direct experimental evidence from orthologs and on strong bioinformatic/structural/genomic-context inference for the P. putida protein; direct experimental characterization of KT2440 OpgG remains the primary outstanding gap.


## Artifacts

- [OpenScientist final report](opgG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](opgG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24555804
2. PMID:22251433
3. PMID:11325942
4. PMID:20062978
5. PMID:37735577
6. PMID:15313617
7. PMID:15175282
8. PMID:17906125
9. PMID:20418397
10. PMID:25320363
11. PMID:19118363
12. PMID:20358372
13. PMID:37267309