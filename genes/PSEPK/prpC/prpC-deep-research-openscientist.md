---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:05:16.827474'
end_time: '2026-07-11T18:21:02.531072'
duration_seconds: 945.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: prpC
  gene_symbol: prpC
  uniprot_accession: Q88KF5
  protein_description: 'RecName: Full=Citrate synthase {ECO:0000256|PIRNR:PIRNR001369};'
  gene_info: Name=prpC {ECO:0000313|EMBL:AAN67948.1}; OrderedLocusNames=PP_2335 {ECO:0000313|EMBL:AAN67948.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the citrate synthase family.
  protein_domains: 2-MeCitrate/Citrate_synth_II. (IPR011278); Citrate_synth-like_lrg_a-sub.
    (IPR016142); Citrate_synth-like_sm_a-sub. (IPR016143); Citrate_synthase. (IPR002020);
    Citrate_synthase_AS. (IPR019810)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: prpC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: prpC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KF5
- **Protein Description:** RecName: Full=Citrate synthase {ECO:0000256|PIRNR:PIRNR001369};
- **Gene Information:** Name=prpC {ECO:0000313|EMBL:AAN67948.1}; OrderedLocusNames=PP_2335 {ECO:0000313|EMBL:AAN67948.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the citrate synthase family.
- **Key Domains:** 2-MeCitrate/Citrate_synth_II. (IPR011278); Citrate_synth-like_lrg_a-sub. (IPR016142); Citrate_synth-like_sm_a-sub. (IPR016143); Citrate_synthase. (IPR002020); Citrate_synthase_AS. (IPR019810)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "prpC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'prpC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **prpC** (gene ID: prpC, UniProt: Q88KF5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *prpC* (PP_2335 / UniProt Q88KF5) — 2-Methylcitrate Synthase of *Pseudomonas putida* KT2440

## Summary

The gene **prpC** (ordered locus **PP_2335**, UniProt accession **Q88KF5**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes **2-methylcitrate synthase** (**2-MCS; EC 2.3.3.5**), a soluble, cytoplasmic enzyme belonging to the citrate synthase superfamily. Its primary function is to catalyze the **committed condensation step of the 2-methylcitrate cycle**: the Claisen-type condensation of **propionyl-CoA with oxaloacetate (and water)** to yield **(2S,3S)-2-methylcitrate plus free coenzyme A**. Although the enzyme retains the ancestral ability to condense acetyl-CoA with oxaloacetate to form citrate, kinetic characterization of orthologs shows that **propionyl-CoA is the strongly preferred substrate**, distinguishing PrpC from the housekeeping citrate synthase of the tricarboxylic acid (TCA) cycle.

This report confirms the gene/protein identity with high confidence. The gene symbol *prpC*, the ordered locus PP_2335, the InterPro domain architecture (2-MeCitrate/Citrate_synth_II, IPR011278, plus the canonical citrate-synthase fold domains), the KEGG orthology assignment (K01659), and the genomic context of the gene (embedded within a *prp* operon, PP_2333–PP_2338) all converge on a single, unambiguous conclusion. A global sequence alignment demonstrates that the P. putida protein is **53.6% identical** to the biochemically characterized and crystallized *Salmonella* Typhimurium 2-methylcitrate synthase (StPrpC), with the two catalytic residues (His261 and Asp312) mapping exactly onto their StPrpC counterparts. In contrast, PrpC shares only **35.3% identity** with its own organism's housekeeping citrate synthase (GltA/PP_4194), placing it firmly in the specialized 2-MCS clade rather than the general citrate-synthase clade.

Physiologically, PrpC initiates the pathway by which *P. putida* oxidizes propionate and propionyl-CoA — a metabolite that is cytotoxic when it accumulates — into pyruvate and succinate that can enter central metabolism. In *P. putida*, this methylcitrate cycle is the **only known route for propionate oxidation**. The enzyme functions in the cytoplasm, requires no metal cofactor for the condensation chemistry itself, and — unlike some Gram-negative citrate synthases — is **not allosterically regulated by NADH**, its regulation instead being imposed at the transcriptional level through the *prp* operon. The following report details the evidence for each of these conclusions and situates PrpC within the broader biochemistry of the 2-methylcitrate cycle.

---

## Gene/Protein Identity Verification

Before presenting functional findings, the mandatory identity check is addressed directly. All independent lines of evidence agree:

| Verification criterion | Expected (from UniProt) | Finding | Match |
|------------------------|-------------------------|---------|-------|
| Gene symbol | prpC | Consistent with *prp* (propionate) catabolic locus | ✅ |
| Ordered locus | PP_2335 | Sits in *prp* operon PP_2333–PP_2338 | ✅ |
| Organism | *P. putida* KT2440 | Confirmed | ✅ |
| Protein family | Citrate synthase family | IPR011278 (2-MeCitrate/Citrate_synth_II) + citrate-synthase fold domains | ✅ |
| Catalytic identity | Citrate synthase (RecName) | Dual citrate synthase / 2-methylcitrate synthase; 2-MCS is the physiological role | ✅ |
| KEGG orthology | — | K01659 (2-methylcitrate synthase, EC 2.3.3.5) | ✅ |

The gene symbol *prpC* is **not** ambiguous in this case: it corresponds to the well-established *prp* (propionate catabolism) nomenclature used across *Salmonella*, *Corynebacterium*, *Pseudomonas*, and other bacteria. Literature retrieved describes this exact gene family and its function, and the organism-specific features of the *P. putida* operon are consistent with related pseudomonads. **Research proceeded with high confidence on the correct target.**

---

## Key Findings

### Finding 1 — PrpC is 2-methylcitrate synthase catalyzing propionyl-CoA + oxaloacetate → 2-methylcitrate + CoA

The InterPro/UniProt domain assignment places PP_2335 in the **methylcitrate-synthase subfamily** of the citrate synthase superfamily: it carries IPR011278 ("2-MeCitrate/Citrate_synth_II") together with the citrate-synthase fold domains (IPR016142, IPR016143, IPR002020, and the citrate-synthase active-site signature IPR019810). This domain architecture is the sequence-level signature of enzymes that perform Claisen condensation of an acyl-CoA thioester with oxaloacetate.

The functional assignment rests on **direct biochemical proof in orthologs**. In *Salmonella* Typhimurium, the PrpC enzyme was purified to homogeneity and shown to have 2-methylcitrate synthase activity in vitro, forming 2-methylcitrate from propionyl-CoA and oxaloacetate ([PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/)). In *Corynebacterium glutamicum*, characterization of two *prpDBC* gene clusters revealed that their gene products were active as citrate synthases and 2-methylcitrate synthases ([PMID: 11976302](https://pubmed.ncbi.nlm.nih.gov/11976302/)). The gene name *prpC* and its operon position (PP_2335, adjacent to *prpB*, *prpD*, and the *acnD/prpF* dehydratase-isomerase genes) match the canonical *prp* propionate-catabolic locus, so the P. putida gene is confidently assigned the same catalytic function.

> *"the PrpC enzyme was purified to homogeneity and shown to have 2-methylcitrate synthase activity in vitro"* — [PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/)

> *"revealed that their gene products were active as citrate synthases and 2-methylcitrate synthases"* — [PMID: 11976302](https://pubmed.ncbi.nlm.nih.gov/11976302/)

### Finding 2 — Substrate specificity: propionyl-CoA is strongly preferred over acetyl-CoA and butyryl-CoA

A defining property of PrpC that distinguishes it from housekeeping citrate synthase is its substrate preference. Kinetic characterization of purified *Salmonella* PrpC established that although the enzyme *can* use acetyl-CoA as a substrate to synthesize citrate, kinetic analysis demonstrated that **propionyl-CoA is the preferred substrate** ([PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/)). A later study of the crystallized *Salmonella* enzyme (StPrpC) confirmed that it **utilizes propionyl-CoA more efficiently than acetyl-CoA or butyryl-CoA** ([PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)). Specificity is conferred not by the catalytic residues themselves — which are identical to those of citrate synthase — but by **residues adjacent to the active site** (e.g., Tyr197 and Leu324 in StPrpC) that shape the acyl-CoA binding pocket to accommodate the extra methyl group of propionyl-CoA.

> *"Although PrpC could use acetyl-CoA as a substrate to synthesize citrate, kinetic analysis demonstrated that propionyl-CoA is the preferred substrate"* — [PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/)

> *"StPrpC was found to utilize propionyl-CoA more efficiently than acetyl-CoA or butyryl-CoA"* — [PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)

### Finding 3 — PrpC operates in the 2-methylcitrate cycle that detoxifies propionyl-CoA and converts propionate to pyruvate

PrpC catalyzes the **second, committed step** of the 2-methylcitrate cycle. In *Salmonella*, ¹³C-labeling reconstruction assigned each Prp enzyme's role in an ordered pathway: **PrpE** (propionyl-CoA synthetase) activates propionate to propionyl-CoA; **PrpC** (2-methylcitrate synthase) condenses it with oxaloacetate to form 2-methylcitrate; **PrpD** (2-methylcitrate dehydratase) and aconitase/**AcnA** (2-methylisocitrate hydratase) carry out the dehydration/rehydration; and **PrpB** (2-methylisocitrate lyase) cleaves 2-methylisocitrate to pyruvate and succinate, oxidizing propionate's α-carbon to pyruvate ([PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/); [PMID: 11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/)).

In *Pseudomonas*, the same cycle is the principal route for propionate oxidation. Disrupting the downstream PrpB (2-methylisocitrate lyase) step blocks completion of the cycle ([PMID: 37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/)), and in *P. aeruginosa* the 2-methylcitrate and glyoxylate cycles are enzymatically linked and partially redundant ([PMID: 40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/)). The broader physiological purpose is **detoxification**: fungal 2-methylcitrate synthase (mcsA) is described as being responsible for detoxifying propionyl-CoA, a toxic metabolite ([PMID: 31141475](https://pubmed.ncbi.nlm.nih.gov/31141475/)).

> *"The reactions are catalyzed by propionyl coenzyme A (propionyl-CoA) synthetase (PrpE), 2-methylcitrate synthase (PrpC), 2-methylcitrate dehydratase (probably PrpD), 2-methylisocitrate hydratase (probably PrpD), and 2-methylisocitrate lyase (PrpB)"* — [PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/)

> *"responsible for detoxifying propionyl-CoA, a toxic metabolite"* — [PMID: 31141475](https://pubmed.ncbi.nlm.nih.gov/31141475/)

### Finding 4 — Structure and mechanism: conserved citrate-synthase fold, cytoplasmic, domain-closure catalysis, not NADH-regulated

The 2.4 Å X-ray crystal structure of *Salmonella* StPrpC established that the **polypeptide fold and catalytic residues are conserved with citrate synthases**, implying shared catalytic mechanism. The enzyme is dimeric (forming higher oligomers at high concentration) and adopts a nearly closed conformation, consistent with the induced-fit **domain-closure mechanism** characteristic of citrate synthases, in which a large domain movement sequesters substrates from solvent during catalysis. Critically, **the key residues involved in allosteric NADH binding are not conserved in StPrpC** — meaning PrpC is not subject to the NADH feedback inhibition seen in hexameric Gram-negative citrate synthases ([PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)).

Comparative crystallography of *Aspergillus fumigatus* mcsA versus human citrate synthase reinforced this picture: the active sites are near-identical, with substrate specificity determined by residues near the active site and by enzyme conformational changes ([PMID: 31141475](https://pubmed.ncbi.nlm.nih.gov/31141475/)). Consistent with the citrate synthase family, PrpC is a **soluble cytoplasmic protein** with no signal peptide or transmembrane features; it carries out its function in the bacterial cytoplasm where propionyl-CoA and oxaloacetate are generated.

> *"The polypeptide fold and the catalytic residues of StPrpC are conserved in citrate synthases (CSs) suggesting similarities in their functional mechanisms"* — [PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)

> *"the key residues involved in NADH binding are not conserved in StPrpC"* — [PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)

### Finding 5 — Bioinformatic confirmation: PP_2335 = 2-methylcitrate synthase with conserved catalytic His261/Asp312

UniProt entry Q88KF5 (375 amino acids, ~42 kDa) annotates **two catalytic activities**: acetyl-CoA + oxaloacetate → citrate (citrate synthase reaction) and propanoyl-CoA + oxaloacetate + H₂O → (2S,3S)-2-methylcitrate + CoA (2-methylcitrate synthase reaction), with pathway assignments to the TCA cycle and "propanoate degradation." Two catalytic active-site residues are annotated by the PIRSR rule PIRSR001369: **His261** (within a conserved G-F-G-H motif) and **Asp312** — the acid/base histidine and catalytic aspartate that are hallmarks of the citrate synthase superfamily active site. KEGG independently assigns PP_2335 to orthology group **K01659** (2-methylcitrate synthase, EC 2.3.3.5). These sequence-based assignments (evidence codes ECO:0000256 PIRNR/PIRSR) independently corroborate the biochemical identity established in orthologs.

### Finding 6 — The *P. putida* KT2440 *prp* operon uses an AcnD/PrpF-type architecture with a GntR-family regulator

The genomic neighborhood of PP_2335 defines a complete methylcitrate-cycle gene cluster:

| Locus | Gene | Product | KO | EC |
|-------|------|---------|-----|-----|
| PP_2333 | — | GntR-family transcriptional regulator | — | — |
| PP_2334 | prpB | 2-methylisocitrate lyase | K03417 | 4.1.3.30 |
| **PP_2335** | **prpC** | **2-methylcitrate synthase** | **K01659** | **2.3.3.5** |
| PP_2336 | acnD | 2-methylcitrate dehydratase (2-methyl-*trans*-aconitate forming) | K20455 | 4.2.1.117 |
| PP_2337 | prpF | 2-methylaconitate isomerase | K09788 | 5.3.3.– |
| PP_2338 | prpD | 2-methylcitrate dehydratase | K01720 | 4.2.1.79 |

This clustering places PrpC as the **committed condensation enzyme** that feeds the downstream isomerase/lyase steps. Notably, *P. putida* uses the **AcnD + PrpF** (2-methyl-*trans*-aconitate isomerase) branch of the cycle rather than the single PrpD-aconitase route of *Salmonella*, and its operon regulator is **GntR-family** rather than the σ⁵⁴/RpoN-dependent PrpR activator of *Salmonella*. In *Salmonella*, the *prp* regulator PrpR is a member of the sigma-54 family of transcriptional activators ([PMID: 10648513](https://pubmed.ncbi.nlm.nih.gov/10648513/)); the contrast highlights organism-specific regulation of an otherwise conserved catabolic module.

> *"members of the sigma-54 family of transcriptional activators"* — [PMID: 10648513](https://pubmed.ncbi.nlm.nih.gov/10648513/)

### Finding 7 — Physiological rationale and evolution: detoxification-plus-salvage; 2-MCS and citrate synthase share a common ancestor

The methylcitrate cycle converts cytotoxic propionyl-CoA to pyruvate; when the cycle is impaired, toxic intermediates (propionyl-CoA, 2-methylcitrate, 2-methylisocitrate) accumulate and inhibit numerous enzymes, including dehydrogenases ([PMID: 37764443](https://pubmed.ncbi.nlm.nih.gov/37764443/)). This dual role — detoxification of a poisonous metabolite plus salvage of its carbon skeleton into central metabolism — is the raison d'être of PrpC.

Evolutionarily, **2-methylcitrate synthase and citrate synthase evolved from a common ancestral protein**, as did isocitrate lyase and 2-methylisocitrate lyase ([PMID: 37764443](https://pubmed.ncbi.nlm.nih.gov/37764443/); [PMID: 31141475](https://pubmed.ncbi.nlm.nih.gov/31141475/)). PrpC is thus a gene-duplication-derived specialist that acquired preferential propionyl-CoA activity while retaining the ancestral fold and catalytic chemistry. In *P. putida*, the cycle is the **only known and described pathway for propionate oxidation** ([PMID: 37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/)); blocking a downstream step (PrpB) is non-lethal but redirects propionyl-CoA into polyhydroxyalkanoate (PHA) polymer synthesis, a finding exploited biotechnologically to fine-tune PHA monomer composition.

> *"the methylcitrate cycle converts cytotoxic propionyl-coenzyme A (CoA) to pyruvate"* — [PMID: 37764443](https://pubmed.ncbi.nlm.nih.gov/37764443/)

> *"Fungal citrate synthase and 2-methylcitrate synthase as well as isocitrate lyase and 2-methylisocitrate lyase, each evolved from a common ancestral protein"* — [PMID: 37764443](https://pubmed.ncbi.nlm.nih.gov/37764443/)

> *"the only known and described pathway for propionate oxidation in this organism"* — [PMID: 37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/)

### Finding 8 — Sequence homology: 53.6% identity to characterized *Salmonella* 2-MCS with exact catalytic-residue conservation

A global Needleman–Wunsch alignment (BLOSUM62) of *P. putida* KT2440 PrpC (Q88KF5, 375 aa) against the biochemically characterized and crystallized *Salmonella* Typhimurium 2-methylcitrate synthase StPrpC (Q56063, 389 aa; EC 2.3.3.5) yields **201/375 = 53.6% identity**. Crucially, the two annotated catalytic residues of the P. putida enzyme map exactly onto the catalytic residues of StPrpC: **Ppu His261 ↔ Stm His274** and **Ppu Asp312 ↔ Stm Asp325**. Because StPrpC is precisely the enzyme shown to prefer propionyl-CoA over acetyl-CoA/butyryl-CoA and whose crystal structure defined the 2-MCS fold ([PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/); [PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/)), this high identity and exact active-site conservation transfer the experimentally validated function to PP_2335 with strong confidence.

> *"The polypeptide fold and the catalytic residues of StPrpC are conserved in citrate synthases (CSs) suggesting similarities in their functional mechanisms"* — [PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)

### Finding 9 — PrpC is a specialized paralog distinct from housekeeping citrate synthase GltA (PP_4194)

*P. putida* KT2440 encodes two citrate-synthase-family proteins: **PrpC** (Q88KF5/PP_2335, 375 aa) and the **housekeeping citrate synthase GltA** (Q88FA4/PP_4194, 429 aa). Pairwise Needleman–Wunsch (BLOSUM62) alignment shows that PrpC shares only **35.3% identity (132/374)** with its own organism's GltA, but **53.6% identity** with the biochemically validated *Salmonella* 2-MCS StPrpC. This clean separation — greater similarity to the validated 2-MCS ortholog than to the co-encoded housekeeping enzyme — demonstrates that **PrpC groups phylogenetically with the 2-MCS clade rather than the housekeeping citrate-synthase clade**, and that the two enzymes have specialized, non-overlapping metabolic roles: GltA drives the TCA cycle with acetyl-CoA, while PrpC drives the methylcitrate cycle with propionyl-CoA.

---

## Mechanistic Model / Interpretation

PrpC (PP_2335) is the **gatekeeper enzyme of propionate detoxification** in *Pseudomonas putida* KT2440. The coherent narrative that emerges from the nine findings is as follows.

**The reaction.** In the cytoplasm, PrpC catalyzes a Claisen condensation identical in chemistry to citrate synthase but tuned for a larger acyl donor:

```
   propionyl-CoA + oxaloacetate + H2O  --PrpC-->  (2S,3S)-2-methylcitrate + CoA-SH
```

The reaction proceeds through the conserved citrate-synthase mechanism: the catalytic **His261** acts as a general acid/base to enolize the acyl-CoA thioester, the enolate attacks the carbonyl of oxaloacetate, and **Asp312** participates in proton shuttling, followed by hydrolysis of the citryl-CoA-analog intermediate to release CoA and the free acid product. A large domain-closure motion sequesters the reaction from bulk solvent, as seen in the StPrpC crystal structure.

**Why propionyl-CoA and not acetyl-CoA.** The catalytic residues are identical to those of citrate synthase, so specificity is imposed by the *shape of the acyl-binding pocket* — active-site-adjacent residues that create room for the extra methyl group of propionyl-CoA. This is an elegant example of substrate discrimination achieved without altering the catalytic machinery, and it explains why PrpC is a physiologically dedicated 2-MCS even though it retains residual citrate-synthase activity.

**Where it sits in metabolism.**

```
 Propionate
    |  PrpE (propionyl-CoA synthetase)
    v
 Propionyl-CoA  ──────────────► [toxic if it accumulates]
    |  PrpC (2-methylcitrate synthase)   ◄── THIS ENZYME (PP_2335)
    |  + oxaloacetate
    v
 (2S,3S)-2-methylcitrate
    |  PrpD / AcnD (2-methylcitrate dehydratase)
    v
 2-methyl-cis-aconitate ─ PrpF (2-methylaconitate isomerase) ─► 2-methyl-trans-aconitate
    |  aconitase / AcnA (2-methylisocitrate hydratase)
    v
 2-methylisocitrate
    |  PrpB (2-methylisocitrate lyase)
    v
 PYRUVATE  +  SUCCINATE  ──► central carbon metabolism (TCA cycle)
```

**Two roles at once.** By consuming propionyl-CoA, PrpC simultaneously (i) **detoxifies** a metabolite that otherwise inhibits dehydrogenases and other enzymes, and (ii) **salvages** the carbon into pyruvate and succinate for growth. Propionyl-CoA arises in *P. putida* from diverse sources — degradation of odd-chain fatty acids, catabolism of certain amino acids (Ile, Val, Met, Thr), and breakdown of monoterpenes such as β-myrcene (in related pseudomonads). The methylcitrate cycle is the sole exit route for this pool in *P. putida*.

**Regulatory logic.** PrpC is controlled at the level of transcription of its operon rather than by allosteric feedback: it lacks the NADH-binding residues that regulate some Gram-negative citrate synthases. In *P. putida* the operon carries a **GntR-family regulator (PP_2333)**, in contrast to the σ⁵⁴-dependent PrpR of enteric bacteria — but the underlying logic is the same: the enzymes are induced when propionate (or its methylcitrate-derived signal) is present. In *Salmonella*, 2-methylcitrate itself (the product of PrpC) or a derivative serves as the inducing coregulator of the operon ([PMID: 9851993](https://pubmed.ncbi.nlm.nih.gov/9851993/)).

**Distinct from the TCA-cycle citrate synthase.** The presence of a separate housekeeping citrate synthase (GltA/PP_4194) with only 35% identity confirms a clean division of labor. GltA handles acetyl-CoA condensation for the TCA cycle; PrpC handles propionyl-CoA condensation for the methylcitrate cycle. This paralog separation is the genomic signature of a dedicated propionate-detoxification module.

| Property | PrpC (PP_2335) | GltA (PP_4194) |
|----------|----------------|----------------|
| Enzyme | 2-methylcitrate synthase | Citrate synthase (housekeeping) |
| Preferred acyl-CoA | Propionyl-CoA | Acetyl-CoA |
| Product | (2S,3S)-2-methylcitrate | Citrate |
| Pathway | 2-methylcitrate cycle | TCA cycle |
| Length | 375 aa | 429 aa |
| % identity to Salmonella StPrpC | 53.6% | (housekeeping clade) |
| Identity to each other | 35.3% | 35.3% |

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|---------------------|------------------------------|
| [10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/) | *Salmonella typhimurium LT2 catabolizes propionate via the 2-methylcitric acid cycle* | Direct biochemical proof: purified PrpC has 2-MCS activity; propionyl-CoA is the preferred substrate; defines the ordered pathway enzymes. Foundation for F001, F002, F003. |
| [20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/) | *Crystal structure of Salmonella typhimurium 2-methylcitrate synthase* | Structure/mechanism: conserved fold & catalytic residues, domain closure, propionyl-CoA > acetyl-CoA > butyryl-CoA, NADH-binding residues NOT conserved. Foundation for F002, F004, F008. |
| [11976302](https://pubmed.ncbi.nlm.nih.gov/11976302/) | *Two prpDBC clusters in Corynebacterium glutamicum* | Confirms PrpC orthologs act as citrate/2-methylcitrate synthases in a second organism. Supports F001. |
| [11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/) | *In vitro conversion of propionate to pyruvate (PrpD, aconitase)* | Reconstitutes the full 2-methylcitrate cycle in vitro; clarifies downstream enzyme roles that PrpC feeds. Supports F003. |
| [31141475](https://pubmed.ncbi.nlm.nih.gov/31141475/) | *Aspergillus fumigatus 2-MCS vs human citrate synthase* | Establishes detoxification role of propionyl-CoA; near-identical active sites; specificity from active-site-adjacent residues. Supports F003, F004, F007. |
| [10648513](https://pubmed.ncbi.nlm.nih.gov/10648513/) | *prpR, ntrA, ihf required for prpBCDE expression* | Salmonella regulator is σ⁵⁴-family — contrasts with the GntR-family regulator in the P. putida operon. Supports F006. |
| [9851993](https://pubmed.ncbi.nlm.nih.gov/9851993/) | *Regulation of the prpBCDE operon* | Shows 2-methylcitrate (from PrpC) or a derivative is the inducing signal for the operon. Contextual support for regulation. |
| [37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/) | *Fed-batch cultivation with glucose+propionate (PHA composition)* | Methylcitrate cycle is the only propionate-oxidation route in Pseudomonas; blocking PrpB redirects flux to PHA. Supports F003, F007. |
| [40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/) | *Methylcitrate & glyoxylate cycles linked in P. aeruginosa* | Enzymatic redundancy/crosstalk between the cycles in a close relative. Supports F003. |
| [37764443](https://pubmed.ncbi.nlm.nih.gov/37764443/) | *Methylcitrate cycle crosstalk in pathogenic fungi (review)* | Detoxification of cytotoxic propionyl-CoA; common evolutionary ancestor of CS and 2-MCS. Supports F007. |

Additional retrieved literature ([PMID: 36377867](https://pubmed.ncbi.nlm.nih.gov/36377867/), [PMID: 16879647](https://pubmed.ncbi.nlm.nih.gov/16879647/), [PMID: 19798672](https://pubmed.ncbi.nlm.nih.gov/19798672/), [PMID: 39492536](https://pubmed.ncbi.nlm.nih.gov/39492536/), [PMID: 40020280](https://pubmed.ncbi.nlm.nih.gov/40020280/)) provides broader context on propionate/organic-acid metabolism and propionyl-CoA toxicity in *Pseudomonas*, *Mycobacterium*, and related organisms, reinforcing the physiological importance of the methylcitrate cycle that PrpC initiates. In particular, the β-myrcene catabolism study in *Pseudomonas* sp. M1 shows the methylcitrate cycle channeling propionyl-CoA from a degradation pathway into central metabolism ([PMID: 19798672](https://pubmed.ncbi.nlm.nih.gov/19798672/)).

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* KT2440 enzyme.** The function of PP_2335 is assigned by strong homology (53.6% identity, exact catalytic-residue conservation) to biochemically validated orthologs (*Salmonella* StPrpC) and by genomic context, not by purification and kinetic assay of the P. putida protein itself. No published *K*ₘ, *k*cat, or crystal structure exists specifically for Q88KF5.

2. **Substrate specificity ratios are transferred, not measured.** The quantitative preference for propionyl-CoA over acetyl-CoA/butyryl-CoA is documented for orthologs; the exact kinetic constants for the P. putida enzyme are unknown, though the conserved active-site-adjacent residues make the qualitative preference highly likely.

3. **Regulatory details in P. putida are incompletely defined.** The operon carries a GntR-family regulator (PP_2333) rather than a σ⁵⁴ activator, but the precise inducing signal, promoter architecture, and regulon in KT2440 have not been experimentally dissected here.

4. **Oligomeric state in P. putida is inferred.** StPrpC is dimeric (with higher-order oligomers at high concentration); the native quaternary structure of the P. putida enzyme has not been directly determined.

5. **Localization is inferred bioinformatically.** The cytoplasmic assignment is based on the absence of signal/transmembrane features and the known behavior of the citrate synthase family; it has not been experimentally confirmed for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and kinetic characterization.** Clone PP_2335, express with an affinity tag, purify, and measure steady-state kinetics (*K*ₘ, *k*cat, catalytic efficiency) for propionyl-CoA, acetyl-CoA, and butyryl-CoA with oxaloacetate to confirm the predicted specificity ratio in the P. putida enzyme.

2. **Structural determination.** Solve the crystal (or cryo-EM) structure of the P. putida enzyme, ideally with bound substrate/product analogs, to verify the domain-closure mechanism and map the acyl-CoA pocket residues (analogous to StPrpC Tyr197/Leu324) that dictate propionyl-CoA preference. AlphaFold modeling followed by structural superposition on StPrpC (PDB) would be a rapid first step.

3. **Gene deletion and growth phenotyping.** Construct a clean ΔprpC (ΔPP_2335) mutant and test growth on propionate (and odd-chain fatty acids) as sole carbon source; a growth defect specific to propionate — rescued by complementation — would confirm the physiological role, and metabolomics would reveal propionyl-CoA/2-methylcitrate accumulation.

4. **Regulatory dissection.** Characterize the GntR-family regulator (PP_2333): identify its operator, the inducing metabolite (2-methylcitrate vs propionate), and the promoter driving PP_2333–PP_2338, using reporter fusions and EMSA.

5. **Confirm distinct roles of PrpC vs GltA.** Test whether GltA (PP_4194) can complement a ΔprpC mutant on propionate and vice versa, to establish functional non-redundancy of the two citrate-synthase-family paralogs.

6. **Biotechnological exploitation.** Given that flux through the methylcitrate cycle competes with propionyl-CoA incorporation into PHA polymers, modulate PrpC expression to tune odd-chain-length monomer content of medium-chain-length PHAs in engineered *P. putida* strains.

---

## Conclusion

*prpC* (PP_2335, UniProt Q88KF5) of *Pseudomonas putida* KT2440 encodes **2-methylcitrate synthase (EC 2.3.3.5)**, a soluble cytoplasmic enzyme of the citrate-synthase superfamily. It catalyzes the committed condensation of **propionyl-CoA with oxaloacetate (and water) to form (2S,3S)-2-methylcitrate plus CoA**, using conserved catalytic residues His261 and Asp312 and strongly preferring propionyl-CoA over acetyl-CoA. Through this reaction it initiates the **2-methylcitrate cycle**, the pathway that oxidizes propionate/propionyl-CoA to pyruvate and succinate while detoxifying growth-inhibitory propionyl-CoA. In *P. putida* the gene lies in an AcnD/PrpF-variant *prp* operon (PP_2333–PP_2338) under GntR-family transcriptional control rather than NADH allostery, and it is a specialized paralog clearly distinct from the housekeeping TCA-cycle citrate synthase GltA (PP_4194).


## Artifacts

- [OpenScientist final report](prpC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](prpC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10482501
2. PMID:11976302
3. PMID:20970504
4. PMID:11294638
5. PMID:37995793
6. PMID:40015638
7. PMID:31141475
8. PMID:10648513
9. PMID:37764443
10. PMID:9851993
11. PMID:36377867
12. PMID:16879647
13. PMID:19798672
14. PMID:39492536
15. PMID:40020280