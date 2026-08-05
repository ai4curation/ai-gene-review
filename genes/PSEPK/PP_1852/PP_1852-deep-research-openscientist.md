---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T16:47:16.917161'
end_time: '2026-07-23T17:13:39.836700'
duration_seconds: 1582.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_1852
  gene_symbol: PP_1852
  uniprot_accession: Q88LS6
  protein_description: 'SubName: Full=Enoyl-[acyl-carrier-protein] reductase (NADPH,
    B-specific) {ECO:0000313|EMBL:AAN67471.1}; EC=1.3.1.10 {ECO:0000313|EMBL:AAN67471.1};'
  gene_info: OrderedLocusNames=PP_1852 {ECO:0000313|EMBL:AAN67471.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the short-chain dehydrogenases/reductases (SDR)
  protein_domains: KR_dom. (IPR057326); NAD(P)-bd_dom_sf. (IPR036291); SDR_fam. (IPR002347);
    adh_short_C2 (PF13561)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 2
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_1852-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_1852-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LS6
- **Protein Description:** SubName: Full=Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific) {ECO:0000313|EMBL:AAN67471.1}; EC=1.3.1.10 {ECO:0000313|EMBL:AAN67471.1};
- **Gene Information:** OrderedLocusNames=PP_1852 {ECO:0000313|EMBL:AAN67471.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the short-chain dehydrogenases/reductases (SDR)
- **Key Domains:** KR_dom. (IPR057326); NAD(P)-bd_dom_sf. (IPR036291); SDR_fam. (IPR002347); adh_short_C2 (PF13561)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_1852" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_1852' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_1852** (gene ID: PP_1852, UniProt: Q88LS6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_1852 (Q88LS6) — Pseudomonas putida KT2440

## Summary

**PP_1852 (UniProt Q88LS6) of *Pseudomonas putida* KT2440 is a soluble, cytoplasmic NADPH-dependent oxidoreductase of the short-chain dehydrogenase/reductase (SDR) superfamily.** Its 249-residue sequence carries the complete classical SDR catalytic tetrad (Asn118, Ser144, Tyr158, Lys162) together with the signature YxxxK motif (Y158-A-M-S-K162) and an N-terminal Rossmann glycine-rich cofactor loop diagnostic of NADP(H) rather than NAD(H) preference. On the basis of these structural features, its ketoreductase (KR) domain, and its independent KEGG orthology assignment (K00059, FabG-type 3-oxoacyl-[ACP] reductase, EC 1.1.1.100), the protein is best described as a **carbonyl/ketoreductase that reduces a 3-oxoacyl (β-keto) thioester or ketone carbonyl using NADPH as the hydride donor.**

**The protein's legacy database name — "Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific), EC 1.3.1.10" — is an automated misannotation.** This name was propagated computationally from the original 2002 GenBank coding-sequence submission (evidence tag ECO:0000313|EMBL:AAN67471.1) and is not supported by any experimental study. The SDR/ketoreductase fold catalyzes carbonyl reduction (an alcohol-dehydrogenase-type chemistry), not the enoyl double-bond reduction implied by EC 1.3.1.10. Indeed, KEGG and eggNOG independently assign this protein to a different reaction class (EC 1.1.1.100 / COG1028), and the two EC numbers are mutually inconsistent — neither being experimentally verified.

**PP_1852 is not the housekeeping fatty-acid-synthase (FAS) ketoreductase.** That role is filled by FabG (PP_1914), a 51.5%-identical paralog located in the core *fabD–fabG–fabF* cluster, while the enoyl-ACP reductase step of core FAS in this organism is performed by FabV (PP_4635). Instead, PP_1852 sits divergently from a LysR-type transcriptional regulator (PP_1853) and adjacent to a putative membrane transporter (PP_1850) — a genomic architecture that in *Pseudomonas* is the hallmark of a substrate-inducible catabolic locus. This strongly suggests PP_1852 is a **specialized, likely inducible reductase acting on a specific small-molecule substrate within a dedicated catabolic or secondary-metabolic pathway**, rather than a component of core lipid biosynthesis. No direct biochemical or genetic characterization of this specific protein currently exists; its physiological substrate remains unknown.

> **Identity verification (mandatory).** The target is confirmed as locus **PP_1852** (OrderedLocusName; GenBank AAN67471.1) of *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950; UniProt Q88LS6, 249 aa, PE=3 "Inferred from homology"). The UniProt protein family (SDR) and domains (KR_dom IPR057326, NAD(P)-bd_dom_sf IPR036291, SDR_fam IPR002347, PF13561 adh_short_C2) all match the analysis in this report. There is **no organism or gene-symbol confusion** — "PP_1852" is merely a locus tag. There IS genuine annotation ambiguity about the exact *reaction*, which this report resolves as far as the evidence allows.

---

## Key Findings

### Finding 1 — The "enoyl-ACP reductase EC 1.3.1.10" label is an automated misannotation; PP_1852 is an uncharacterized NADPH-dependent SDR

UniProt entry Q88LS6 (249 amino acids, protein-existence level **PE=3, "Inferred from homology"**) carries only a **SubName** annotation — "Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific), EC 1.3.1.10" — bearing the evidence tag **ECO:0000313|EMBL:AAN67471.1**. This tag is critical: it indicates the name was propagated directly from the original 2002 GenBank CDS submission for the KT2440 genome, i.e., it is an automated electronic annotation, not the product of experimental study or expert curation. The only family-level assignment UniProt makes is membership in the **short-chain dehydrogenases/reductases (SDR) family**.

Crucially, three independent annotation systems disagree with the UniProt name and with each other:

| Source | Assignment | Reaction / EC | Reaction class |
|---|---|---|---|
| UniProt (SubName) | Enoyl-ACP reductase (NADPH, B-specific) | EC 1.3.1.10 | C=C double-bond reduction |
| KEGG (ppu:PP_1852) | K00059 = 3-oxoacyl-[ACP] reductase (FabG) | EC 1.1.1.100 | C=O carbonyl (keto) reduction |
| eggNOG | COG1028 | generic SDR/FabG-like dehydrogenase | C=O carbonyl reduction |
| InterPro/SMART/Pfam | KR domain (SM00822 PKS_KR, IPR057326); PF13561 adh_short_C2 | ketoreductase | C=O carbonyl reduction |

The domain assignments are decisive. The protein carries a **Ketoreductase (KR) domain** (SMART SM00822, PKS_KR; InterPro IPR057326) and the Pfam **adh_short_C2 (PF13561)** signature. These are ketoreductase folds — enzymes that reduce a carbonyl (C=O → C–OH), i.e., an alcohol-dehydrogenase-type chemistry. They are structurally distinct from a dedicated enoyl-reductase (which saturates a C=C double bond). The two EC numbers — EC 1.3.1.10 (from UniProt) and EC 1.1.1.100 (from KEGG) — describe fundamentally different chemistry and cannot both be correct. Since neither is experimentally supported, and since the fold evidence uniformly points to carbonyl reduction, the balance of evidence favors classifying PP_1852 as an **NADPH-dependent carbonyl/ketoreductase, with the "enoyl-ACP reductase" name being a misleading automated artifact.**

### Finding 2 — The intact SDR catalytic tetrad and an NADPH-type Rossmann motif support NADPH-dependent carbonyl reductase activity

Direct inspection of the Q88LS6 sequence confirms all of the structural machinery expected of a functional, NADPH-utilizing classical SDR:

- **Cofactor-binding (Rossmann) motif:** The N-terminal glycine-rich loop is **G16-G17-S18-R19-G20-I21-G22**, matching the canonical TGxxxGxG dinucleotide-binding pattern. The presence of a **basic Arg19** in the phosphate-binding loop, together with the **absence of any acidic residue (Asp/Glu) at the C-terminus of the β2 strand** (positions 36–40 read V-A-F-T-Y), is the diagnostic signature that this enzyme binds **NADP(H) rather than NAD(H)**. In classical SDRs, an acidic residue at that β2 position hydrogen-bonds the 2′-OH of NAD and excludes the 2′-phosphate of NADP; its replacement by neutral/basic residues (as here) accommodates and often requires the extra phosphate of NADP(H). This structural call is fully consistent with both the "NADPH" descriptor in the legacy name and the NADPH-using FabG-type reaction.
- **Catalytic tetrad:** The full canonical SDR tetrad is conserved — **Asn118, Ser144, Tyr158, and Lys162** — with the hallmark **YxxxK motif** present as **Y158-A-M-S-K162**. In this catalytic machinery, the tyrosine acts as the catalytic acid/base that protonates/deprotonates the substrate oxygen, the lysine lowers the tyrosine pKa and binds the nicotinamide ribose, the serine stabilizes and orients the substrate carbonyl, and the asparagine helps maintain the proton-relay water network. All four residues are present and correctly spaced — the exact arrangement required for hydride transfer from NADPH to a substrate carbonyl.
- **Localization signals:** The protein begins **MSKQ…** with no N-terminal signal peptide, lipobox, or membrane anchor, indicating a **soluble cytoplasmic protein**.
- **Size and quaternary structure:** ~25.5 kDa monomer; classical SDRs characteristically assemble into homotetramers.

Together, these features constitute strong structural/bioinformatic evidence that PP_1852 is a catalytically competent, NADPH-dependent oxidoreductase operating in the cytoplasm on a carbonyl-bearing substrate.

### Finding 3 — PP_1852 is a FabG paralog embedded in a LysR-regulated, transporter-associated locus, implying a specialized rather than core-FAS role

Global pairwise alignment shows PP_1852 shares **51.5% identity (117/227 aligned columns)** with the canonical fatty-acid-synthase 3-oxoacyl-ACP reductase **FabG (PP_1914)**. This level of identity places PP_1852 firmly in the FabG/SDR clade but well outside the range of a simple allelic duplicate — it is a divergent paralog.

Importantly, *P. putida* KT2440 already encodes the complete dedicated core-FAS reductase set elsewhere in the genome:

| Core-FAS step | Enzyme | Locus | Context |
|---|---|---|---|
| 3-oxoacyl-ACP reductase (β-ketoreductase) | FabG | **PP_1914** | in the *fabD–fabG–fabF* cluster (PP_1913 / 1914 / 1916) |
| Enoyl-ACP reductase | FabV | **PP_4635** | dedicated core-FAS enoyl reductase (non-SDR) |

Because these housekeeping activities are already provided, **PP_1852 is not required for the essential fatty-acid biosynthesis pathway** — freeing it to serve a more specialized function. The existence of a dedicated FabV enoyl-ACP reductase (PP_4635) also independently reinforces that the "enoyl-ACP reductase" name on PP_1852 is misapplied: that step already has its own enzyme.

The genomic context reinforces the specialized-role interpretation. From KEGG POSITION data, PP_1852 lies on the minus strand (2,076,409–2,077,158) and is **divergently transcribed** from **PP_1853, a LysR-type transcriptional regulator** on the plus strand (2,077,277–2,078,215), the two genes sharing a compact ~119 bp intergenic promoter region. Nearby **PP_1850** is a putative membrane transporter (YgaY-like). STRING lists PP_1853 as a genomic-neighborhood partner (neighborhood score 0.557).

```
     minus strand  <----------------  |  ---------------->  plus strand
   [ PP_1850 ]   [ PP_1852 (SDR/KR) ] | [ PP_1853 (LysR regulator) ]
   transporter     ~25.5 kDa reductase|   divergent, ~119 bp promoter
   (YgaY-like)                         ^
                          shared intergenic promoter region
```

This **divergent LysR-regulator + transporter + oxidoreductase** arrangement is the classic architecture of inducible catabolic loci in *Pseudomonas*. It is directly analogous to well-characterized systems: the *tcbR* LysR regulator controlling the divergent *tcbCDEF* chlorocatechol oxidative operon in *Pseudomonas* sp. P51 [PMID: 2050630](https://pubmed.ncbi.nlm.nih.gov/2050630/), and the *antR*/*antABC* anthranilate-degradation module in *P. aeruginosa*, where the LysR-type AntR binds the intergenic region between *antA* and *antR* to activate transcription [PMID: 22609066](https://pubmed.ncbi.nlm.nih.gov/22609066/). By analogy, PP_1853 (LysR) plausibly senses a small-molecule inducer and activates transcription of PP_1852 (and possibly the PP_1850 transporter), consistent with a **substrate-specific, inducible catabolic or tailoring role** for the PP_1852 reductase rather than a core-metabolic one.

A caveat on interpretation: STRING also lists PP_1852's highest-scoring partners as FAS enzymes (FabF, FabZ, FabB, FabA, FabD, FabV). However, these edges are dominated by the *database* channel, which simply reflects the shared KEGG "fatty acid biosynthesis" pathway annotation and is therefore partly circular. They should not be over-interpreted as evidence of a physical role in core FAS.

---

## Mechanistic Model / Interpretation

Integrating the three findings yields a coherent, evidence-based model of PP_1852's likely function, while being explicit about what is well-supported versus inferred.

**Catalytic chemistry (well-supported by structure).** PP_1852 is a classical SDR carbonyl reductase. Its active site (Ser144–Tyr158–Lys162–Asn118) and NADP(H)-selective Rossmann loop indicate it transfers a hydride from **NADPH** to a **substrate carbonyl (C=O)**, generating a hydroxyl (C–OH) product — the canonical reaction:

```
   R–C(=O)–R'  +  NADPH + H+   -->   R–CH(OH)–R'  +  NADP+
     (ketone / β-keto-thioester)         (secondary alcohol)
```

This is chemically the same reaction class as FabG (3-oxoacyl-ACP → 3-hydroxyacyl-ACP) and distinct from the enoyl (C=C) reduction its legacy EC number implies.

**Substrate specificity (unknown, but constrained).** The substrate is not experimentally defined. Two broad possibilities are consistent with the evidence:

1. A **3-oxoacyl / β-keto thioester** (acyl-ACP or acyl-CoA), per the KEGG K00059/FabG-type orthology. Given that core FAS is already served by PP_1914, this would point to a specialized acyl-processing role — e.g., in a secondary-metabolite, polyketide-like, or β-oxidation-linked pathway.
2. A **small-molecule ketone/aldehyde/keto-acid/keto-sugar** carbonyl typical of the broad substrate range of catabolic SDRs. The divergent LysR regulator and adjacent transporter favor this interpretation: an inducer is imported (PP_1850), sensed by the regulator (PP_1853), and the reductase (PP_1852) performs a redox tailoring step in that compound's assimilation.

**Localization (well-supported).** The absence of any signal peptide or membrane anchor, and the soluble SDR fold, place the enzyme's activity in the **cytoplasm** — the compartment where both fatty-acid biosynthesis and most NADPH-dependent reductive metabolism occur.

**Pathway context (inferred).** The genomic synteny — transporter + divergent LysR regulator + SDR reductase — is the textbook signature of an **inducible catabolic module**. The most parsimonious model is that PP_1852 catalyzes an NADPH-dependent reduction step within a specific, regulator-controlled small-molecule catabolic (or tailoring) pathway, with the substrate likely imported by the neighboring transporter and the pathway induced only when that substrate is present.

```
   substrate in  --[PP_1850 transporter]-->  cytoplasmic substrate
                                                     |
                              (inducer sensed by PP_1853 LysR regulator
                               -> activates divergent promoter)
                                                     |
                                                     v
                     NADPH  --[ PP_1852 SDR ketoreductase ]-->  NADP+
                     carbonyl substrate  ------------------->  hydroxyl product
                                                     |
                                          downstream catabolism / assimilation
```

**Summary judgment.** PP_1852 should be re-annotated away from "enoyl-ACP reductase (EC 1.3.1.10)" toward a generic **NADPH-dependent SDR carbonyl/ketoreductase (FabG-like; EC 1.1.1.–)** of currently undetermined physiological substrate, most plausibly functioning as a specialized, inducible enzyme in a LysR-regulated catabolic locus.

---

## Evidence Base

The two directly supporting citations concern the regulatory-architecture inference (Finding 3). Both were verified against their abstracts:

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [2050630](https://pubmed.ncbi.nlm.nih.gov/2050630/) | *Characterization of the Pseudomonas sp. strain P51 gene tcbR, a LysR-type transcriptional activator of the tcbCDEF chlorocatechol oxidative operon* | Establishes the canonical *Pseudomonas* architecture — a divergently transcribed LysR regulator controlling an adjacent oxidative/catabolic gene cluster — the exact pattern seen for PP_1853/PP_1852. Verbatim: *"A regulatory gene, tcbR, was located upstream and divergently transcribed from the chlorocatechol oxidative gene cluster tcbCDEF."* |
| [22609066](https://pubmed.ncbi.nlm.nih.gov/22609066/) | *AntR-mediated bidirectional activation of antA and antR, anthranilate degradative genes in Pseudomonas aeruginosa* | Confirms the divergent LysR-regulator/catabolic-operon promoter logic, with the LysR protein binding the intergenic region to activate transcription — supporting an inducible catabolic role for the PP_1852/PP_1853 pair. Verbatim: *"In P. aeruginosa, antABC and antR are divergently located and AntR binds to the intergenic region between antA and antR to activate the antABC transcription."* |

**Note on the broader literature corpus.** A total of 12 papers were reviewed. The majority (e.g., PMIDs 41921592, 41672327, 41117507, 41081329, 41046915, 40969383, 40706765, 40141183, 42393666, 42107196) concern metabolic engineering of *P. putida* KT2440 as a chassis for rhamnolipids, polyhydroxyalkanoates (PHA), free fatty acids, and aromatics valorization. **None of these studies characterize PP_1852 specifically.** They are relevant only as background: they confirm that *P. putida* KT2440 possesses an active, well-studied fatty-acid and acyl-metabolism network within which SDR/ketoreductase enzymes operate, but they provide no direct experimental evidence about the function of PP_1852. This absence of targeted literature is itself an important finding: **PP_1852 is an experimentally uncharacterized protein.**

Database records underpinning the molecular-identity and structural analyses include UniProt Q88LS6; KEGG ppu:PP_1852 (K00059); eggNOG COG1028; InterPro IPR002347 / IPR036291 / IPR057326; Pfam PF13561; and STRING 160488.PP_1852.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization exists.** There is no published enzymatic assay, structure, knockout phenotype, or transcriptomic study specifically defining PP_1852's substrate, kinetics, or physiological role. All functional conclusions here are inferences from sequence, domain architecture, cofactor-motif analysis, orthology, and genomic context.
2. **Both database EC assignments are unverified and contradictory.** UniProt (EC 1.3.1.10, enoyl-ACP reductase) and KEGG (EC 1.1.1.100, FabG-type ketoreductase) disagree, and neither is experimentally grounded. The fold evidence favors carbonyl reduction, but the *precise* substrate (β-keto-thioester vs. free small-molecule carbonyl) is not resolvable from bioinformatics alone.
3. **The physiological substrate is unknown.** The transporter–regulator–reductase synteny strongly suggests an inducible catabolic substrate, but its chemical identity has not been determined.
4. **Cofactor preference is inferred, not measured.** The NADP(H)-selectivity call rests on the absence of an acidic β2 residue and the presence of Arg19; this is a robust heuristic but should be confirmed enzymatically.
5. **Quaternary structure is assumed.** Homotetramer assembly is inferred from the SDR family default, not demonstrated for this protein.
6. **STRING FAS associations are partly circular.** The top STRING partners derive largely from the database channel (shared KEGG pathway annotation), and should not be taken as independent evidence of a physical FAS role.

---

## Proposed Follow-up Experiments / Actions

1. **Substrate screening of purified enzyme.** Heterologously express and purify His-tagged PP_1852; run NADPH-consumption (A340) assays against panels of candidate carbonyl substrates — 3-oxoacyl-CoA/ACP thioesters of varying chain length, aromatic/aliphatic ketones and aldehydes, keto-sugars, and keto-acids. This directly tests the FabG-like (K00059) vs. broad-carbonyl-reductase hypotheses.
2. **Confirm cofactor specificity.** Measure kinetics with NADPH vs. NADH to validate the NADP(H)-preference predicted from the Rossmann motif.
3. **Define the regulon.** Use RNA-seq or reporter-fusion assays under candidate inducers (aromatics, keto-fatty acids, unusual carbon sources) to identify conditions that activate the PP_1853-controlled divergent promoter, thereby narrowing the physiological substrate. Test co-transcription/co-regulation of PP_1850–PP_1852.
4. **Genetic loss-of-function.** Construct a clean PP_1852 deletion and, separately, a PP_1853 (LysR) deletion; phenotype across carbon-source arrays (e.g., Biolog) to find growth substrates dependent on this locus.
5. **Structural determination / AlphaFold-guided docking.** Solve or model the structure (an AlphaFold model for Q88LS6 is available) with a bound cofactor and dock candidate substrates to test whether the substrate-binding pocket accommodates ACP-bound acyl chains (buried, tunnel-like) or free small molecules (open pocket).
6. **Formal re-annotation.** Regardless of the above, the UniProt "enoyl-ACP reductase (EC 1.3.1.10)" name should be flagged for correction to a generic "NADPH-dependent SDR carbonyl/ketoreductase (FabG-like)" pending experimental data, to prevent further propagation of the misannotation.

---

*Report generated from an autonomous multi-iteration functional-annotation investigation of PP_1852 / Q88LS6. All functional conclusions are explicitly labeled as inference from sequence, structure, orthology, and genomic context, as no protein-specific experimental literature exists.*


## Artifacts

- [OpenScientist final report](PP_1852-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_1852-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2050630
2. PMID:22609066