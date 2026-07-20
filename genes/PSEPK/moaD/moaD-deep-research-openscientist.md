---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T14:20:29.825966'
end_time: '2026-07-20T14:38:45.845585'
duration_seconds: 1096.02
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moaD
  gene_symbol: moaD
  uniprot_accession: Q88NB9
  protein_description: 'RecName: Full=Molybdopterin synthase sulfur carrier subunit
    {ECO:0000256|ARBA:ARBA00024247};'
  gene_info: Name=moaD {ECO:0000313|EMBL:AAN66917.1}; OrderedLocusNames=PP_1293 {ECO:0000313|EMBL:AAN66917.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MoaD family.
  protein_domains: Beta-grasp_dom_sf. (IPR012675); MoaD_arc-typ. (IPR010038); MOCS2A.
    (IPR044672); Mopterin_synth/thiamin_S_b. (IPR016155); ThiS/MoaD-like. (IPR003749)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: moaD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moaD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NB9
- **Protein Description:** RecName: Full=Molybdopterin synthase sulfur carrier subunit {ECO:0000256|ARBA:ARBA00024247};
- **Gene Information:** Name=moaD {ECO:0000313|EMBL:AAN66917.1}; OrderedLocusNames=PP_1293 {ECO:0000313|EMBL:AAN66917.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MoaD family.
- **Key Domains:** Beta-grasp_dom_sf. (IPR012675); MoaD_arc-typ. (IPR010038); MOCS2A. (IPR044672); Mopterin_synth/thiamin_S_b. (IPR016155); ThiS/MoaD-like. (IPR003749)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moaD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moaD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moaD** (gene ID: moaD, UniProt: Q88NB9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *moaD* (Q88NB9, PP_1293) in *Pseudomonas putida* KT2440

## Identity Verification (mandatory)

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88NB9 | UniProtKB |
| Protein | Molybdopterin synthase sulfur carrier subunit | UniProtKB |
| Gene / locus | *moaD* / PP_1293 | EMBL AAN66917.1 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) | UniProtKB |
| Length | 82 aa | UniProtKB |
| Family | MoaD family (ThiS/MoaD-like, β-grasp/ubiquitin-like fold) | InterPro IPR003749, IPR012675, IPR010038 |
| C-terminus | …DEVAFFPPV**TGG** (reactive Gly-Gly) | UniProtKB |

**Verification outcome — CONFIRMED, unambiguous.** The gene symbol *moaD*, the "molybdopterin synthase sulfur carrier subunit" description, the MoaD-family/β-grasp domain assignments, and the diagnostic C-terminal **Gly-Gly motif** are all mutually consistent. No gene-symbol ambiguity was encountered, and Q88NB9 is the single molybdopterin-type MoaD sulfur carrier in the *P. putida* KT2440 genome. Because Q88NB9 itself has not been the subject of dedicated primary studies, its function is assigned by strong family membership plus the well-characterized biochemistry of near-identical *E. coli*/*S. aureus* MoaD orthologs (the pathway is highly conserved across all domains of life) and by *P. putida*-specific genomic evidence.

---

## Summary

The gene **moaD** (UniProt **Q88NB9**; ordered locus **PP_1293**) of *Pseudomonas putida* strain KT2440 encodes the **small sulfur-carrier subunit of molybdopterin (MPT) synthase**, the enzyme that catalyzes the **second of the four conserved steps of molybdenum cofactor (Moco) biosynthesis**. The 82-residue protein belongs to the **MoaD family** of the ubiquitin/ThiS β-grasp fold superfamily and terminates in the diagnostic C-terminal **double-glycine (Gly-Gly) motif** (…FFPPVTGG). This terminal glycine is chemically activated as a **thiocarboxylate (–COSH)** and serves as the immediate sulfur donor for installing the *cis*-dithiolene group of molybdopterin. MoaD's role is not classical catalysis but **sulfur delivery** into a composite active site formed with its catalytic partner MoaE.

Mechanistically, MoaD operates within a **MoaD₂–MoaE₂ heterotetramer**. Each MoaD subunit inserts its reactive C-terminus deep into a MoaE catalytic subunit, positioning the C-terminal Gly-thiocarboxylate adjacent to the substrate **cyclic pyranopterin monophosphate (cPMP / precursor Z)**. Sulfur is transferred from the MoaD thiocarboxylate to the C1′ and C2′ positions of precursor Z, converting it to molybdopterin (EC 2.8.1.12; Rhea:26333). Because each thiocarboxylate carries a single sulfur, **two loading/transfer cycles** are required to build the dithiolene. After each transfer, spent MoaD (now carboxylated, ending in Gly-Gly) is regenerated by the **MoeB adenylyltransferase** (PP_0735; EC 2.7.7.80), which adenylates the C-terminal carboxylate to form an acyl-adenylate that is then resolved to the thiocarboxylate using sulfur from cysteine-desulfurase/persulfide systems.

Functionally, MoaD acts as a **soluble cytoplasmic protein** and is a **non-redundant gatekeeper** of the entire molybdoenzyme repertoire of *P. putida*. The molybdopterin it helps synthesize is the scaffold that, after molybdenum insertion (MoeA) and nucleotide attachment (MobA), becomes Moco — the essential cofactor of assimilatory nitrate reductase, xanthine and nicotinate dehydrogenases, formate dehydrogenase, periplasmic methionine-sulfoxide reductase MsrP, and other oxidoreductases spanning carbon, nitrogen, and sulfur metabolism. In the genome, *moaD* lies within a tightly coupled **moaC–moaD–moaE operon**, is 49% identical to the biochemically characterized *E. coli* MoaD with a perfectly conserved reactive C-terminus, and its cognate recharge enzyme MoeB is present. This report consolidates eight confirmed findings supported by primary enzymology, crystallography, comparative genomics, and curated reaction databases.

---

## Key Findings

### F001 — Q88NB9 is the sulfur-carrier small subunit of molybdopterin synthase

Q88NB9 is an 82-residue protein annotated as the "Molybdopterin synthase sulfur carrier subunit" and assigned to the MoaD family. Its sequence terminates in a **Gly-Gly motif** (…FFPPVTGG), the diagnostic C-terminal double-glycine shared across MoaD/ThiS/ubiquitin-superfamily sulfur carriers. This terminal glycine is the residue that becomes **thiocarboxylated** and carries the sulfur atom destined for the cofactor. The functional assignment rests on classical biochemical reconstitution work performed on the *E. coli* ortholog: only when MoaD carries a **C-terminal thiocarboxylate** and is combined with MoaE does the resulting MPT synthase complex convert precursor Z to molybdopterin in vitro; the carboxylated (spent) form is catalytically inactive.

As stated in the primary study, *"Only the thiocarboxylated MPT synthase complex was found to be able to convert precursor Z in vitro to MPT"* and *"a thiocarboxylation of the C terminus of MoaD is proposed that would serve as the source of sulfur that is transferred to precursor Z"* ([PMID: 11459846](https://pubmed.ncbi.nlm.nih.gov/11459846/)). The Gly-Gly terminus of Q88NB9 exactly matches the chemically reactive motif characterized in that work, establishing MoaD's role as the sulfur donor of MPT synthesis.

### F002 — Sulfur is transferred from the MoaD C-terminal thiocarboxylate to C1′/C2′ of precursor Z at the MoaE active site

Crystallographic studies of MPT synthase reveal a **heterotetramer** in which each MoaD C-terminus is deeply inserted into a MoaE subunit, forming a composite active site. Precursor Z (cPMP) binds in a pocket at the MoaE dimer interface, positioned in close proximity to the C-terminal glycine of MoaD. Anomalous-signal experiments localized the thiocarboxylate sulfur and captured the enzyme–precursor complex with the first dithiolene sulfur added at C2′. Because molybdopterin's dithiolene requires **two** sulfur atoms, two MoaD thiocarboxylates from a single tetramer are consumed in a two-step reaction.

The structural study reports *"the transfer of sulfur atoms from a C-terminal MoaD thiocarboxylate to the C-1′ and C-2′ positions of precursor Z"* and that *"precursor Z is bound by strictly conserved residues in a pocket at the MoaE dimer interface in close proximity of the C-terminal glycine of MoaD"* ([PMID: 18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/)). An earlier structure established that *"the C terminus of each MoaD subunit is deeply inserted into a MoaE subunit to form the active site"* ([PMID: 12571227](https://pubmed.ncbi.nlm.nih.gov/12571227/)). Together these define the precise atoms of the substrate that receive sulfur and the structural basis for MoaD–MoaE cooperation.

### F003 — MoaD is a ubiquitin/ThiS-fold sulfur carrier reactivated by MoeB-catalyzed C-terminal adenylation

MoaD adopts the **β-grasp (ubiquitin) fold** (InterPro IPR012675) and shares its 3D architecture, surface features, and C-terminal Gly-Gly with ubiquitin, ThiS, and Urm1. This structural kinship is not coincidental: the **MoaD–MoeB pair is the prokaryotic evolutionary antecedent** of the eukaryotic Urm1–Uba4 system and, more broadly, the ubiquitin–E1 conjugation machinery. MoeB is an **E1-like activating enzyme** that adenylates the MoaD C-terminal carboxylate to form an acyl-adenylate; this intermediate is then converted to the thiocarboxylate, with sulfur supplied by cysteine-desulfurase/persulfide systems (e.g., IscS). This ATP-dependent activation **regenerates active MoaD** after each sulfur-transfer cycle.

The Urm1 structural study documents that *"similarities between Urm1-Uba4 and MoaD-MoeB establish an evolutionary link between ATP-dependent protein conjugation in eukaryotes and ATP-dependent cofactor sulfuration"* ([PMID: 16864801](https://pubmed.ncbi.nlm.nih.gov/16864801/)). A complementary review notes that *"the pathways for FeS cluster assembly and thio-modifications of tRNA are connected to Moco biosynthesis by sharing the same protein components"* ([PMID: 28284029](https://pubmed.ncbi.nlm.nih.gov/28284029/)), showing MoaD-mediated sulfur chemistry is integrated with shared cellular sulfur-trafficking machinery. Consistent with an adenylation step, UniProt annotates Q88NB9 with a **nucleotide-binding** keyword.

### F004 — MoaD acts in the cytoplasm at step 2 of the conserved Moco biosynthetic pathway

Moco biosynthesis is a **highly conserved cytoplasmic pathway** in bacteria, archaea, and eukaryotes, comprising three universal steps plus a bacterial/archaeal fourth: (1) formation of cyclic pyranopterin monophosphate (cPMP/precursor Z) from GTP; (2) formation of molybdopterin (MPT) by MPT synthase; (3) insertion of molybdenum into MPT to form Mo-MPT (Moco); and (4) attachment of a nucleotide (GMP or CMP) to form dinucleotide Moco variants. **MoaD/MoaE (MPT synthase) execute step 2.** The molybdopterin product ultimately becomes Moco, the essential cofactor of more than 50 molybdoenzymes (nitrate reductase, DMSO reductase, formate dehydrogenase, sulfite oxidase, xanthine-type oxidoreductases) that catalyze redox reactions in carbon, nitrogen, and sulfur metabolism.

The authoritative review describes the pathway as *"formation of the cyclic pyranopterin monophosphate, (2) formation of MPT, (3) insertion of molybdenum into molybdopterin to form Moco"* and states that *"Moco is the essential component of a group of redox enzymes"* ([PMID: 24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/)). The broader metabolic context is captured by the observation that *"Bacterial molybdoenzymes are key enzymes involved in the global sulphur, nitrogen and carbon cycles"* ([PMID: 31517366](https://pubmed.ncbi.nlm.nih.gov/31517366/)).

### F005 — *moaD* lies in an overlapping *moaC–moaD–moaE* operon (steps 1–2 of Moco biosynthesis)

Genome coordinates for *P. putida* KT2440 place three co-oriented (+ strand) genes contiguously, indicating an operon:

| Locus | Gene | KEGG orthology | Function (EC) | Coordinates |
|-------|------|----------------|---------------|-------------|
| PP_1292 | *moaC* | K03637 | cyclic pyranopterin monophosphate synthase (EC 4.6.1.17) | 1,478,937–1,479,407 |
| PP_1293 | *moaD* | K03636 | molybdopterin-synthase sulfur-carrier protein | 1,479,404–1,479,652 |
| PP_1294 | *moaE* | K03635 | molybdopterin synthase catalytic subunit (EC 2.8.1.12) | 1,479,655–1,480,101 |

*moaC* and *moaD* **overlap by 4 bp** (…1479407 / 1479404…) and *moaD*–*moaE* are separated by only **2 bp** — hallmarks of translational coupling within a single operon. This synteny is decisive organism-specific evidence: MoaD is co-encoded with (i) its obligate catalytic partner **MoaE** (which carries the EC 2.8.1.12 activity) and (ii) **MoaC**, which produces the precursor Z substrate that MoaD/MoaE act upon. The *moaD* ORF encodes exactly 82 amino acids ending in the C-terminal Gly-Gly (…VTGG), and KEGG maps it to the **Sulfur relay system** (ppu04122), reflecting its ThiS/MoaD-type sulfur-transfer chemistry rather than classical catalysis.

### F006 — Q88NB9 is 49% identical to characterized *E. coli* MoaD with a perfectly conserved reactive C-terminus, and its MoeB activator is present

Global pairwise alignment of *P. putida* MoaD (Q88NB9, 82 aa) against the experimentally characterized *E. coli* K-12 MoaD (P30748, 81 aa) yields **49.4% identity** (39/79 aligned columns). Critically, the functionally essential C-terminal segment is **essentially invariant**: both proteins end in "…DEVAFFPPVTGG," including the reactive C-terminal Gly-Gly. This conservation of the catalytically decisive motif justifies transferring the detailed *E. coli*/*S. aureus* enzymology to the *P. putida* ortholog with high confidence.

A UniProt survey of *P. putida* KT2440 (taxid 160488) confirms the complete cognate machinery is present: **MoaC** (Q88NC0/PP_1292, EC 4.6.1.17), **MoaE** (Q88NB8/PP_1294, EC 2.8.1.12), and the MoaD-activating enzyme **MoeB** (Q88PW3/PP_0735, annotated "Molybdopterin-synthase adenylyltransferase, EC 2.7.7.80 / MoaD protein adenylase / Sulfur carrier protein MoaD adenylyltransferase"). Importantly, MoaD (Q88NB9) is the **only molybdopterin-type MoaD sulfur carrier** in the genome; the other β-grasp sulfur carriers present (ThiS Q88CS5, TusA Q88L21, ThiI, FdhD) belong to distinct families serving thiamine biosynthesis and tRNA-thiolation, not molybdopterin. This rules out functional redundancy and confirms a single, unambiguous gene identity.

### F007 — MoaD-derived molybdopterin feeds a complete Moco pathway and a diverse molybdoenzyme repertoire

A UniProt survey (keyword Molybdenum/Molybdopterin) shows the full downstream pathway that consumes MoaD's product, plus the molybdate-uptake system that supplies molybdenum:

| Step / role | Gene(s) / locus | Enzyme (EC) |
|-------------|-----------------|-------------|
| GTP 3′,8-cyclase (step 1) | *moaA* PP_4597 (+ paralogs PP_2482, PP_1969) | EC 4.1.99.22 |
| cPMP synthase (step 1) | *moaC* PP_1292 | EC 4.6.1.17 |
| **MPT synthase (step 2)** | ***moaD*/*moaE* PP_1293/PP_1294** | **EC 2.8.1.12** |
| Mo insertion (step 3) | *moeA* PP_2123 | EC 2.10.1.1 |
| Mo-MPT guanylyltransferase (step 4, bis-MGD) | *mobA* PP_3457 | EC 2.7.7.77 |
| MogA-type paralogs | PP_2122, PP_4600 | — |
| Molybdate uptake (ABC transporter) | *modA* PP_3828, *modB* PP_3829, *modC* PP_3830 | EC 7.3.2.5 |
| Uptake regulator | *modR* PP_0360 | — |

Moco-dependent molybdoenzymes present in *P. putida* KT2440 include: assimilatory **nitrate reductase / sulfite reductase** (PP_1703, EC 1.7.99.4), **xanthine dehydrogenase** (*xdhB* PP_4279, EC 1.17.1.4), **nicotinate dehydrogenase** (*nicB* PP_3948, EC 1.17.2.1), **formate dehydrogenase-O** (*fdoG* PP_0489, EC 1.2.1.2), periplasmic **methionine-sulfoxide reductase MsrP** (PP_4676), aromatic aldehyde dehydrogenase **PaoC** (PP_3310, EC 1.2.99.7), and additional molybdopterin oxidoreductases (PP_0256, PP_4596, PP_1080). Because MoaD is the sole molybdopterin sulfur carrier, its activity is an **obligatory, non-redundant upstream node** for all of these enzymes — spanning nitrogen assimilation, purine/nicotinate catabolism, C1 metabolism, periplasmic oxidative-stress repair, and aromatic aldehyde oxidation, consistent with *P. putida*'s versatile catabolic lifestyle.

### F008 — The precise MPT synthase reaction defines MoaD's Gly-thiocarboxylate → Gly-Gly catalytic cycle

The balanced reaction catalyzed by MPT synthase (MoaD/MoaE), curated as EC 2.8.1.12 and Rhea:26333, is:

```
2 [MPT-synthase sulfur-carrier protein]-C-terminal-Gly-aminoethanethioate
  + cyclic pyranopterin phosphate + H2O
      →  molybdopterin
         + 2 [MPT-synthase sulfur-carrier protein]-C-terminal-Gly-Gly
         + 2 H(+)
```

The systematic name is *thiocarboxylated molybdopterin synthase:cyclic pyranopterin phosphate sulfurtransferase* (KEGG R09395). The EC subclass **2.8.1 designates sulfurtransferases**. This stoichiometry makes explicit that **two** MoaD thiocarboxylate equivalents are consumed per molybdopterin, each converted from the active "C-terminal-Gly-aminoethanethioate" (thiocarboxylate) form to the spent "C-terminal-Gly-Gly" (carboxylate) form — precisely the cycle that MoeB then reverses via adenylation (F003).

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent, well-supported model of MoaD as a **regenerable molecular sulfur shuttle** at the heart of Moco biosynthesis.

### The catalytic cycle

```
                         ┌─────────────────────────────────────────┐
                         │        MPT SYNTHASE (MoaD2–MoaE2)        │
                         │                                          │
  precursor Z (cPMP) ───►│  MoaD–C(=O)–S⁻  ──sulfur──► C2′ of cPMP  │
   (from MoaA + MoaC)    │  (thiocarboxylate)                       │
                         │  MoaD–C(=O)–S⁻  ──sulfur──► C1′          │──► MOLYBDOPTERIN
                         │      (2 sulfurs = cis-dithiolene)        │        (MPT)
                         │                                          │
                         │  MoaD–C(=O)–O⁻  (spent, Gly-Gly)         │
                         └───────────────┬─────────────────────────┘
                                         │
                                         ▼
                         ┌─────────────────────────────────────────┐
                         │   RECHARGE:  MoeB (E1-like, ATP)         │
                         │   MoaD–COO⁻ + ATP → MoaD–CO–AMP          │
                         │   + persulfide sulfur (IscS/L-Cys)       │
                         │        → MoaD–C(=O)–S⁻  (recharged)      │
                         └─────────────────────────────────────────┘
```

**Step 2 in context.** Upstream, MoaA (a radical-SAM GTP 3′,8-cyclase) and MoaC convert GTP into cyclic pyranopterin monophosphate (precursor Z), which already contains all the carbon and nitrogen atoms of the eventual pterin but **lacks the sulfur-bearing dithiolene**. MoaD's task is to install those two sulfur atoms. Working as a **MoaD₂–MoaE₂ heterotetramer**, each MoaD threads its C-terminus into a MoaE catalytic pocket where precursor Z is bound (F002). Sulfur is delivered from the MoaD C-terminal thiocarboxylate to C2′ first, then C1′, generating the **cis-dithiolene** that will chelate molybdenum. Two thiocarboxylate equivalents are consumed per molybdopterin (F008).

**Regeneration.** Each transfer leaves MoaD carboxylated (C-terminal Gly-Gly). MoeB (PP_0735) then adenylates this carboxylate in an ATP-dependent reaction, and persulfide sulfur (from cysteine-desulfurase systems such as IscS) resolves the acyl-adenylate to the thiocarboxylate, recharging MoaD (F003). This E1-like activation chemistry is evolutionarily continuous with ubiquitin/Urm1 activation, underscoring that MoaD is a bona fide ubiquitin-superfamily protein used for **cofactor sulfuration rather than protein conjugation**.

**Downstream fate and physiology.** Molybdopterin is handed to MoeA (Mo insertion → Moco) and, in bacteria, MobA (nucleotide attachment → bis-MGD/MCD variants). The mature cofactor is inserted into the apo-forms of the organism's molybdoenzymes (F007). Because MoaD is the **only** molybdopterin-type sulfur carrier in the genome (F006), loss of MoaD would abolish molybdopterin synthesis and thereby inactivate the entire downstream molybdoenzyme repertoire. In this sense MoaD is a **low-flux but non-redundant bottleneck**: it is required only in catalytic/stoichiometric amounts relative to precursor Z, yet its function gates a broad slice of redox metabolism.

### Localization

All evidence places MoaD's activity in the **cytoplasm**. Moco biosynthesis is a conserved cytoplasmic pathway (F004), MoaD lacks any signal peptide, transmembrane segment, or export signal, and its partners (MoaE, MoaC, MoeB) are soluble cytoplasmic enzymes. Notably, several *downstream* molybdoenzymes it ultimately serves are periplasmic or membrane-associated (e.g., MsrP, respiratory formate dehydrogenases), but those enzymes acquire mature Moco after cytoplasmic synthesis; MoaD itself does not leave the cytosol.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|---------------------|------------------------------|
| [11459846](https://pubmed.ncbi.nlm.nih.gov/11459846/) | *Thiocarboxylation of molybdopterin synthase…* | Direct biochemical proof that only thiocarboxylated MoaD converts precursor Z to MPT; identifies the C-terminal thiocarboxylate as the sulfur source (F001). |
| [18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/) | *Crystal structure of a molybdopterin synthase–precursor Z complex…* | Localizes sulfur transfer to C1′/C2′ of precursor Z at the MoaE dimer interface adjacent to MoaD's C-terminal glycine (F002). |
| [12571227](https://pubmed.ncbi.nlm.nih.gov/12571227/) | *Structural studies of molybdopterin synthase…* | Shows MoaD's C-terminus inserts into MoaE to form the composite active site (F002). |
| [16864801](https://pubmed.ncbi.nlm.nih.gov/16864801/) | *Solution structure of Urm1 and origin of protein modifiers* | Establishes MoaD's ubiquitin-superfamily fold and MoeB-dependent ATP activation underpinning thiocarboxylate regeneration (F003). |
| [28284029](https://pubmed.ncbi.nlm.nih.gov/28284029/) | *Shared function and moonlighting proteins in Moco biosynthesis* | Connects MoaD sulfur chemistry to shared FeS/tRNA-thiolation sulfur-trafficking machinery (F003). |
| [24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/) | *The biosynthesis of the molybdenum cofactors* | Defines the four-step Moco pathway and places MPT synthase at step 2; establishes downstream importance of the product (F004). |
| [31517366](https://pubmed.ncbi.nlm.nih.gov/31517366/) | *Regulation of Moco biosynthesis…in bacteria* | Contextualizes molybdoenzymes in global S/N/C cycles (F004). |
| [25514355](https://pubmed.ncbi.nlm.nih.gov/25514355/) | *Assembly and catalysis of Mo/W formate dehydrogenases* | Illustrates a specific Moco-dependent enzyme class ultimately served by MoaD (context for F007). |
| [23317461](https://pubmed.ncbi.nlm.nih.gov/23317461/) | *Molybdenum cofactor…in M. tuberculosis pathogenesis* | Independent confirmation that Moco enables redox reactions in C/N/S metabolism (context for F004/F007). |
| [42253079](https://pubmed.ncbi.nlm.nih.gov/42253079/) | *Emerging roles of pterins as signaling molecules in bacteria* | Broader pterin biology; molybdopterin/Moco as a redox-active pterin cofactor (context for F004). |

**Note on evidence provenance.** The detailed enzymology and crystallography (F001–F003) derive from studies of the *E. coli* and *S. aureus* orthologs, not from direct experiments on the *P. putida* protein. Their transfer to Q88NB9 is justified by high sequence identity (49.4%) and, decisively, by the **perfect conservation of the reactive C-terminal motif** (…PVTGG) and the presence of the complete cognate machinery (MoaC, MoaE, MoeB) in *P. putida* KT2440 (F005, F006). The genomic and reaction-database evidence (F005–F008) is specific to *P. putida* and its curated pathways.

---

## Supported and Refuted Hypotheses

**Supported**
- Q88NB9 is the MoaD sulfur-carrier subunit of MPT synthase — supported by family assignment, the diagnostic C-terminal Gly-Gly, and ortholog biochemistry/structures (PMID 11459846, 18092812, 12571227).
- MoaD donates sulfur via a C-terminal thiocarboxylate to precursor Z to form MPT's dithiolene — supported (PMID 11459846, 18092812).
- MoaD is a recyclable ubiquitin-like carrier reactivated by MoeB adenylation — supported (PMID 16864801); MoeB (PP_0735) present in *P. putida*; nucleotide-binding annotation on Q88NB9 consistent.
- MoaD acts in the cytoplasm at step 2 of the conserved Moco pathway, upstream of all molybdoenzymes — supported (PMID 24980677, 31517366).

**Refuted / ruled out**
- Not a classical metabolic enzyme acting on small-molecule substrates (it is a protein-based sulfur carrier/adapter contributing to a composite active site).
- Not a transporter, membrane protein, or secreted/structural protein.
- Symbol ambiguity ruled out: sequence, family, and reactive C-terminal Gly-Gly all converge on MoaD, the sole molybdopterin sulfur carrier in the genome.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein.** The assignment for Q88NB9 rests on **homology transfer and genomic/bioinformatic evidence**, not on purified-protein enzymology, structure, or knockout phenotyping of the KT2440 ortholog specifically. While the inference is strong (invariant catalytic C-terminus, complete cognate operon and machinery), it remains an inference.

2. **Sulfur-source details are model-derived.** The identity of the immediate sulfur donor(s) that convert MoeB-adenylated MoaD to the thiocarboxylate in *P. putida* (e.g., which cysteine desulfurase — IscS vs. others — and whether a rhodanese/relay is used) has not been experimentally mapped in this organism.

3. **Operon regulation and expression conditions.** Operon synteny (*moaC–moaD–moaE*) is established, but transcriptional regulation, induction conditions (molybdate/anaerobiosis responsiveness), and promoter architecture in *P. putida* remain uncharacterized.

4. **Quantitative kinetics unknown.** No *P. putida*-specific kinetic parameters (turnover, MoaD–MoaE affinity, MoeB recharge rate) are available, so flux control through this step cannot be quantified.

5. **Possible moonlighting/cross-talk.** Given documented sharing of sulfur-relay components across Moco, FeS, and tRNA-thiolation pathways (F003), the degree to which *P. putida* MoaD or its sulfur supply competes with other pathways is unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic validation.** Construct a clean *moaD* (PP_1293) deletion in KT2440 and test loss of all Moco-dependent activities (nitrate reductase, xanthine dehydrogenase, formate dehydrogenase); complement with wild-type *moaD* and with a C-terminal Gly→Ala/ΔGly mutant. Predicted: null mutant loses molybdoenzyme activities; C-terminal mutant fails to complement.

2. **In vitro reconstitution with native proteins.** Co-express and purify *P. putida* MoaD (Q88NB9) and MoaE (Q88NB8); thiocarboxylate MoaD (chemically or via MoeB/IscS) and assay conversion of precursor Z to molybdopterin using the established Form-A fluorescent derivative assay — the first organism-specific enzymological confirmation.

3. **MoeB partnership assay.** Verify that PP_0735 (MoeB) adenylates *P. putida* MoaD in an ATP-dependent manner (AMP release, mass shift on the MoaD C-terminus) and identify the physiological sulfur donor.

4. **Structural confirmation.** Solve the crystal/cryo-EM structure (or generate an AlphaFold model) of the *P. putida* MoaD₂–MoaE₂ complex, ideally with bound precursor Z, to confirm the C-terminal insertion geometry and C1′/C2′ sulfur-transfer arrangement.

5. **Expression/regulation profiling.** Use RT-qPCR or RNA-seq under varied molybdate, nitrogen, and oxygen conditions to define *moaCDE* operon regulation and confirm the translational coupling implied by the overlapping ORFs.

6. **Sulfur-pathway cross-talk.** Test whether depletion of shared sulfur-relay components (e.g., IscS) simultaneously impairs Moco, FeS, and tRNA-thiolation outputs, quantifying MoaD's dependence on shared machinery.

---

## Conclusion

*moaD* (Q88NB9, PP_1293) of *Pseudomonas putida* KT2440 encodes the **sulfur-carrier subunit of molybdopterin synthase**, a soluble cytoplasmic enzyme executing step 2 of molybdenum-cofactor biosynthesis. Its C-terminal glycine, activated as a thiocarboxylate, donates the two sulfur atoms of molybdopterin's *cis*-dithiolene to cyclic pyranopterin monophosphate at the MoaE active site (EC 2.8.1.12), and the spent carboxylated protein is recharged by the E1-like MoeB adenylyltransferase. The assignment is unambiguous and non-redundant: MoaD is the sole molybdopterin-type sulfur carrier in the genome, is encoded in a coupled *moaC–moaD–moaE* operon, is 49% identical to the biochemically characterized *E. coli* MoaD with a perfectly conserved reactive C-terminus, and gates the maturation of the organism's entire molybdoenzyme repertoire — spanning nitrogen assimilation, purine and nicotinate catabolism, formate oxidation, and periplasmic methionine-sulfoxide repair.


## Artifacts

- [OpenScientist final report](moaD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moaD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11459846
2. PMID:18092812
3. PMID:12571227
4. PMID:16864801
5. PMID:28284029
6. PMID:24980677
7. PMID:31517366