---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T05:00:09.174340'
end_time: '2026-11-12T05:10:21.872593'
duration_seconds: 612.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P0A752
  gene_symbol: nadD
  uniprot_accession: P0A752
  protein_description: 'RecName: Full=Nicotinate-nucleotide adenylyltransferase; EC=2.7.7.18
    {ECO:0000269|PubMed:10894752}; AltName: Full=Deamido-NAD(+) diphosphorylase; AltName:
    Full=Deamido-NAD(+) pyrophosphorylase; AltName: Full=Nicotinate mononucleotide
    adenylyltransferase; Short=NaMN adenylyltransferase;'
  gene_info: Name=nadD; Synonyms=ybeN; OrderedLocusNames=b0639, JW0634;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the NadD family. .
  protein_domains: Cyt_trans-like. (IPR004821); NadD/NMNAT. (IPR005248); Rossmann-like_a/b/a_fold.
    (IPR014729); CTP_transf_like (PF01467)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P0A752
- **Protein Description:** RecName: Full=Nicotinate-nucleotide adenylyltransferase; EC=2.7.7.18 {ECO:0000269|PubMed:10894752}; AltName: Full=Deamido-NAD(+) diphosphorylase; AltName: Full=Deamido-NAD(+) pyrophosphorylase; AltName: Full=Nicotinate mononucleotide adenylyltransferase; Short=NaMN adenylyltransferase;
- **Gene Information:** Name=nadD; Synonyms=ybeN; OrderedLocusNames=b0639, JW0634;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the NadD family. .
- **Key Domains:** Cyt_trans-like. (IPR004821); NadD/NMNAT. (IPR005248); Rossmann-like_a/b/a_fold. (IPR014729); CTP_transf_like (PF01467)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadD" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadD** (gene ID: P0A752, UniProt: P0A752) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *nadD* (P0A752) — Nicotinate-Nucleotide Adenylyltransferase in *Escherichia coli* K-12

**Gene:** *nadD* (synonym *ybeN*; ordered locus names *b0639* / *JW0634*)
**Protein:** Nicotinate-nucleotide adenylyltransferase (NaMN adenylyltransferase; deamido-NAD⁺ pyrophosphorylase)
**UniProt:** P0A752 · **EC:** 2.7.7.18
**Organism:** *Escherichia coli* (strain K-12)
**Family:** NadD family — NadD/NMNAT (IPR005248); Cyt_trans-like / CTP_transf_like (PF01467, IPR004821); Rossmann-like α/β/α dinucleotide-binding fold (IPR014729)

---

## Summary

The *Escherichia coli* K-12 gene **nadD** (synonym *ybeN*; *b0639*, *JW0634*; UniProt **P0A752**) encodes **nicotinate-nucleotide adenylyltransferase** (also called nicotinate mononucleotide adenylyltransferase, NaMN adenylyltransferase, or deamido-NAD⁺ pyrophosphorylase; **EC 2.7.7.18**). The enzyme catalyzes the reversible transfer of the adenylyl (AMP) moiety of ATP onto the 5′-phosphate of nicotinate mononucleotide (NaMN), producing **deamido-NAD⁺** (nicotinate adenine dinucleotide, NaAD) and inorganic pyrophosphate. This is the **penultimate, committed step of NAD⁺ biosynthesis**: the NaAD product is subsequently amidated by NAD synthetase (NadE) to form the mature redox cofactor NAD⁺ ([PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/); [PMID: 23289308](https://pubmed.ncbi.nlm.nih.gov/23289308/)).

NadD is a small (~213-residue), single-domain, **soluble cytoplasmic enzyme** built on a Rossmann-like dinucleotide-binding (α/β/α) fold characteristic of the (T/H)XGH-motif nucleotidyltransferase superfamily. Its defining biochemical property is a strong preference for the **deamidated** substrate NaMN over the amidated analog nicotinamide mononucleotide (NMN): NaMN is adenylylated **at least 20-fold faster** than NMN ([PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/)). This specificity channels metabolic flux through the "deamidated" branch of NAD biosynthesis, where NadD sits at the **convergence point** of the de novo (aspartate → quinolinate → NaMN, via NadC) and the deamidated-salvage (nicotinate → NaMN, via PncB) pathways. The complementary amidated branch (NMN → NAD) in *E. coli* is handled by a chemically distinct activity, the NMNAT domain of the multifunctional regulatory protein **NadR** ([PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)).

Functionally, *nadD* is **essential for growth** in *E. coli*, and because NadD and NadE are the two indispensable downstream steps common to all deamidated NAD routes, NadD is a validated, **selective broad-spectrum antibacterial drug target**. Structure-based inhibitors have been developed that potently inhibit bacterial NadD enzymes (from *E. coli* and *Bacillus anthracis*) while sparing the functionally equivalent human enzymes ([PMID: 19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/); [PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)). The identification is unambiguous: all primary literature matches the target protein (NaMN adenylyltransferase), gene symbol (*nadD*/*ybeN*), organism (*E. coli* K-12), and the NadD/NMNAT family / Cyt_trans-like domain architecture specified by UniProt.

---

## Gene/Protein Identity Verification

Before research, the mandatory identity check was performed and **passed on all criteria**:

| Verification criterion | Expected (UniProt P0A752) | Found in literature | Match |
|---|---|---|---|
| Gene symbol | *nadD* (syn. *ybeN*; *b0639*) | *nadD*/*ybeN*/*b0639* consistently used | ✅ |
| Protein function | NaMN adenylyltransferase, EC 2.7.7.18 | NaMN → NaAD adenylyltransferase | ✅ |
| Organism | *E. coli* K-12 | *E. coli* (incl. K-12 strains) | ✅ |
| Family / domains | NadD family; Cyt_trans-like; Rossmann-like fold | Nucleotidyltransferase, Rossmann-like fold, NadD family | ✅ |

The gene symbol is **not** ambiguous for this protein in *E. coli*: multiple independent primary papers ([PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/), [PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/), [PMID: 12949168](https://pubmed.ncbi.nlm.nih.gov/12949168/)) explicitly tie *nadD* (= *ybeN*) to nicotinate mononucleotide adenylyltransferase activity in *E. coli*. The UniProt EC reference (PubMed 10894752) is itself a dedicated primary study of *E. coli ybeN*/*nadD*. Research proceeded with full confidence in the target identity.

---

## Key Findings

### Finding 1 — NadD catalyzes NaMN + ATP → deamido-NAD⁺ + PPi, the penultimate step of NAD biosynthesis

The core catalytic function of NadD is the adenylylation of nicotinate mononucleotide. Formally (EC 2.7.7.18):

> **nicotinate mononucleotide (NaMN) + ATP ⇌ deamido-NAD⁺ (NaAD) + pyrophosphate (PPi)**

This is an **adenylyl transfer** (nucleotidyl transfer): the 5′-phosphate oxygen of NaMN performs an in-line attack on the α-phosphate of ATP, displacing pyrophosphate and forming the NaAD dinucleotide via a new phosphoanhydride bond. The reaction is the **penultimate step of NAD⁺ synthesis** — immediately before the final amidation. The deamido-NAD⁺ product (NaAD) still carries a carboxylate at the pyridine 3-position rather than the amide group of mature NAD⁺; this carboxylate is converted to the amide by NAD synthetase (NadE), producing NAD⁺. Thus NadD performs the dinucleotide-forming condensation and NadE performs the final amidation.

Primary literature states this directly: "Adenylation of nicotinate mononucleotide to nicotinate adenine dinucleotide is the penultimate step in NAD+ synthesis. In *Escherichia coli*, the enzyme nicotinate mononucleotide adenylyltransferase is encoded by the nadD gene" ([PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/)); and independently: "Nicotinic acid mononucleotide adenylyltransferase (NAMNAT), encoded by the nadD gene, catalyzes the reaction from nicotinic acid mononucleotide (NaMN) to nicotinic acid adenine dinucleotide (NaAD) during the synthetic pathway of NAD(H)" ([PMID: 23289308](https://pubmed.ncbi.nlm.nih.gov/23289308/)). The enzyme's alternative names — *deamido-NAD⁺ diphosphorylase / pyrophosphorylase* — reflect the reversibility of this phosphoanhydride-forming reaction.

### Finding 2 — *nadD* is essential for growth and is a validated, selective antibacterial drug target

Genetic evidence establishes that *nadD* is **essential** in *E. coli*: gene disruption is not tolerated, and the enzyme cannot be bypassed because it performs a committed and unique step in the only route to NAD⁺. The authors of [PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/) state plainly: "We have also shown that the nadD gene is essential for growth in E. coli." Consistent with essentiality, hypomorphic (partial loss-of-function) alleles produce graded, NAD⁺-dependent growth defects. The temperature-sensitive mutant *fusB*/*nadD72* is a frameshift in *nadD* that alters the final 10 residues and appends 17 extra residues, leaving "very little NAD+ and NADPH synthesis at the permissive temperature and essentially no synthesis at the non-permissive temperature," producing a pleiotropic phenotype; a separate active-site (ATP-binding) point mutant *nadD74* causes a milder, temperature-sensitive deficit ([PMID: 12949168](https://pubmed.ncbi.nlm.nih.gov/12949168/)). These allelic series directly correlate NadD activity with intracellular NAD⁺ pools and viability. Conversely, overexpression raises NAD(H) pools and can restore redox balance ([PMID: 23289308](https://pubmed.ncbi.nlm.nih.gov/23289308/)), underscoring NadD's control over NAD⁺ supply.

Because NadD is essential and conserved across most bacteria — and because bacteria generally cannot import NAD⁺ — it was "selected as a target for structure-based inhibitor development," and researchers "identified small molecule compounds that efficiently inhibited target enzymes from Escherichia coli (ecNadD) and Bacillus anthracis (baNadD) but had no effect on functionally equivalent human enzymes" ([PMID: 19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/)). The selectivity over the human NMNAT isozymes — despite catalyzing an analogous reaction — makes NadD a particularly attractive **selective broad-spectrum antibacterial target**.

### Finding 3 — NadD prefers the deamidated substrate (NaMN over NMN); specificity resides in the carboxylate-binding pocket

NadD's substrate specificity is biologically decisive. The native *E. coli* enzyme strongly favors **nicotinic acid mononucleotide (NaMN, deamidated)** over **nicotinamide mononucleotide (NMN, amidated)**. The functional importance of this preference is demonstrated by protein-engineering studies: generating an *E. coli* NaMN-adenylyltransferase variant with high activity on NMN required deliberate engineering to enable a "fully active amidated NAD biosynthesis" route ([PMID: 28455340](https://pubmed.ncbi.nlm.nih.gov/28455340/)), confirming that the wild-type enzyme does not natively route amidated substrate efficiently. The two mononucleotide forms define the two branches: "the key reaction involves adenylylation of nicotinic acid mononucleotide (NaMN) and nicotinamide mononucleotide (NMN), respectively" ([PMID: 28455340](https://pubmed.ncbi.nlm.nih.gov/28455340/)).

Mutational analysis assigned catalytic/active-site roles to specific residues — "our data has lead us to assign amino acid residues His-19, Arg-46 and Asp-109 to the active site" ([PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/)). The active site discriminates the carboxylate of nicotinate (NaMN) from the carboxamide of nicotinamide. The contrast with dual-specificity family members further highlights NadD's selectivity: the NadM enzyme of some organisms "was shown to possess dual substrate specificity toward both nicotinate and nicotinamide mononucleotide substrates" ([PMID: 20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/)), whereas *E. coli* NadD is a dedicated NaMN enzyme.

### Finding 4 — Foundational characterization: reversible, product-inhibited, ≥20-fold NaMN preference

The defining enzymological study is Mehl, Kinsland & Begley (2000) — the paper UniProt cites for the EC 2.7.7.18 assignment (ECO:0000269|PubMed:10894752). This work: (1) identified the gene — "The gene (ybeN) coding for nicotinate mononucleotide adenylyltransferase, an NAD(P) biosynthetic enzyme, has been identified and overexpressed in Escherichia coli"; (2) demonstrated reversibility and feedback behavior — "This enzyme catalyzes the reversible adenylation of nicotinate mononucleotide and shows product inhibition"; and (3) quantified the specificity — "The rate of adenylation of nicotinate mononucleotide is at least 20 times faster than the rate of adenylation of nicotinamide mononucleotide" ([PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/)).

These three properties — **reversibility, product inhibition, and ≥20× NaMN preference** — define the enzyme's kinetic behavior and its placement in the pathway. Product inhibition (by NaAD and/or PPi) is consistent with a regulated node near the end of a biosynthetic route, and reversibility reflects the modest free-energy change of an adenylyl-transfer condensation.

| Property | Observation | Source |
|---|---|---|
| Reaction | NaMN + ATP ⇌ NaAD + PPi | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/) |
| Reversibility | Reversible | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/) |
| Regulation | Product inhibition | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/) |
| Substrate preference | NaMN ≥ 20× faster than NMN | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/) |
| Active-site residues | His-19, Arg-46, Asp-109 | [PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/) |
| Pathway position | Penultimate step (before NadE) | [PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/) |

### Finding 5 — Rossmann-like nucleotidyltransferase fold; conserved substrate/inhibitor pocket

NadD belongs to the **NadD/NMNAT family** (InterPro IPR005248), containing a **Cyt_trans-like / CTP_transf_like** domain (PF01467, IPR004821) built on a **Rossmann-like α/β/α dinucleotide-binding fold** (IPR014729). This is the signature architecture of the (T/H)XGH-motif nucleotidyltransferase superfamily, which binds a nucleotide (ATP) and transfers its nucleotidyl group. Crystallographic studies of the family member *Bacillus anthracis* NadD confirm this and reveal the substrate/inhibitor binding geometry: "Bacterial nicotinate mononucleotide adenylyltransferase encoded by the essential gene nadD plays a central role in the synthesis of the redox cofactor NAD(+)" ([PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)). Structures of baNadD "in complex with three NadD inhibitors" revealed "a common binding site shared by different classes of NadD inhibitors" ([PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)) — i.e., a conserved NaMN/ATP pocket that different inhibitor chemotypes exploit, informing structure-based drug design. The *E. coli* enzyme (ecNadD) shares this fold and was co-screened in the same inhibitor campaigns ([PMID: 19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/)).

### Finding 6 — NadD is the convergence point of de novo and salvage NAD synthesis

The substrate NaMN is produced by **two upstream routes that both feed NadD**:

1. **De novo pathway** — Aspartate is oxidized by L-aspartate oxidase (NadB) and condensed by quinolinate synthase (NadA) to form quinolinic acid, which is then decarboxylated/phosphoribosylated by quinolinate phosphoribosyltransferase (NadC, EC 2.4.2.19) using PRPP to yield NaMN. The NadC reaction products are explicitly "pyrophosphate CO2, and nicotinate mononucleotide" ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/)).
2. **Deamidated salvage pathway** — Nicotinate (niacin) is converted by nicotinate phosphoribosyltransferase (PncB) with PRPP to NaMN; this is one of the "two alternative, deamidating and nondeamidating, routes of nicotinamide salvage/recycling" ([PMID: 20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/)).

Both routes converge on **NaMN**, which only NadD adenylylates to NaAD, after which NadE amidates it to NAD⁺. Hence NadD and NadE are "the two indispensable downstream enzymes of NAD synthesis, nicotinate adenylyltransferase (NadD family) and NAD synthetase (NadE family)" ([PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/)). This topological position — a single mandatory funnel for all deamidated flux — explains both the enzyme's essentiality and its appeal as a drug target.

### Finding 7 — NadD is a soluble cytoplasmic enzyme

All evidence places NadD in the **cytosol**. The protein is small (~213 residues), single-domain, with no signal peptide or transmembrane segment, and it was readily overexpressed and purified as a **soluble recombinant enzyme** — "has been identified and overexpressed in Escherichia coli" ([PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/)) — behavior typical of cytoplasmic metabolic enzymes. Its substrates (NaMN, ATP) and product (NaAD → NAD⁺) are all cytosolic metabolites, and pathway partner enzymes behave as soluble cytosolic proteins; for example, the upstream NadC was expressed as "about 2% of the soluble protein" ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/)). UniProt likewise annotates NadD as cytoplasmic. NAD biosynthesis in bacteria is a cytoplasmic process, and NadD carries out its reaction there. (This localization is a robust inference from sequence features and the soluble behavior of the recombinant enzyme rather than from a dedicated subcellular-localization experiment.)

### Finding 8 — Division of labor: NadD (deamidated branch) vs NadR (amidated branch)

*E. coli* NadD is a **dedicated, monofunctional NaMN adenylyltransferase of the deamidated branch**. The complementary amidated branch (NMN → NAD⁺) is carried out by a chemically distinct activity: the central **NMNAT domain of the multifunctional NadR protein**. NadR "is composed of (i) an N-terminal DNA-binding domain involved in the transcriptional regulation of NAD biosynthesis, (ii) a central nicotinamide mononucleotide adenylyltransferase (NMNAT) domain, and (iii) a C-terminal RNK domain" ([PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)). NadR directly converts NMN → NAD⁺ in the Pnu/ribosylnicotinamide salvage route: "a model for the complete salvage pathway from exogenous N-ribosylnicotinamide to NAD which involves the concerted action of the PnuC transporter and NRK, followed by the NMNAT activity of the NadR protein" ([PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)).

This division of labor — NadD acting on **deamidated** NaMN, NadR acting on **amidated** NMN — is fully consistent with NadD's ≥20-fold kinetic preference for NaMN. The two enzymes act on chemically distinct mononucleotide substrates, keeping the deamidated and amidated branches enzymatically separate. It also confirms NadD's specialized, purely catalytic role: NadD carries no regulatory function, whereas transcriptional regulation of NAD biosynthesis resides in NadR.

---

## Mechanistic Model / Interpretation

### Reaction mechanism

NadD performs a nucleotidyl-transfer (adenylyl-transfer) reaction. The α-phosphate of ATP is attacked by the 5′-phosphate oxygen of NaMN, forming a new phosphoanhydride bond that joins the AMP moiety to the nicotinate mononucleotide — generating the dinucleotide NaAD and releasing pyrophosphate. The Rossmann-like fold positions ATP in the canonical nucleotide-binding cleft; the conserved (T/H)XGH motif of the superfamily and the assigned active-site residues (His-19, Arg-46, Asp-109; [PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/)) coordinate the phosphates and catalyze transfer. Specificity for NaMN over NMN is determined by a pocket that recognizes the pyridine **carboxylate** (3-COO⁻) of nicotinate rather than the amide of nicotinamide. The reaction is reversible and subject to product inhibition ([PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/)).

### Pathway topology

```
            DE NOVO (aspartate)                   DEAMIDATED SALVAGE (niacin)
   Asp --NadB--> iminoaspartate                        Nicotinate (NA)
        --NadA--> Quinolinate (QA)                           |
            |                                           PncB  | + PRPP
      NadC  | + PRPP, - CO2, - PPi                            |
            v                                                 v
         Nicotinate mononucleotide (NaMN) <--------------------
                            |
                            |   *** NadD (P0A752) ***   + ATP, - PPi
                            |   NaMN + ATP -> NaAD + PPi   [EC 2.7.7.18]
                            v
         Deamido-NAD+ (Nicotinate adenine dinucleotide, NaAD)
                            |
                            |   NadE (NAD synthetase)   + NH3/Gln, + ATP
                            v
                         NAD+   <--- (amidated branch, separate: NMN --NadR--> NAD+)
```

NadD is the **single funnel** through which all deamidated NAD flux must pass. De novo synthesis (from aspartate, via NadB/NadA/NadC) and deamidated salvage (from niacin, via PncB) both deliver NaMN to NadD; NadD converts it to NaAD; and NadE completes the pathway by amidation to NAD⁺. The parallel amidated salvage branch (exogenous nicotinamide riboside → NMN → NAD⁺) bypasses NadD entirely, relying instead on NadR's NMNAT activity ([PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)). This architecture explains why NadD is essential: its deamidated-branch role is not redundant with NadR, and no other *E. coli* enzyme efficiently adenylylates NaMN.

### Why it matters as a drug target

NadD and NadE are the two obligatory downstream steps common to de novo and deamidated-salvage routes ([PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/)). Inhibiting NadD collapses NAD⁺ supply from both routes simultaneously. The bacterial enzyme's active site differs enough from the human NMNAT isozymes to permit **selective inhibition** ([PMID: 19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/)), and crystal structures reveal a **conserved, druggable pocket** ([PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)), making structure-based design feasible.

---

## Supported and Refuted Hypotheses

| Claim | Status | Key evidence |
|---|---|---|
| *nadD*/*ybeN* encodes NaMN adenylyltransferase (EC 2.7.7.18) catalyzing NaMN + ATP → NaAD + PPi | **Supported** | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/); [16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/); [23289308](https://pubmed.ncbi.nlm.nih.gov/23289308/) |
| Reaction is reversible and product-inhibited | **Supported** | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/) |
| Enzyme strongly prefers NaMN over NMN (≥20×; deamidated route) | **Supported** | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/); [28455340](https://pubmed.ncbi.nlm.nih.gov/28455340/); [20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/) |
| Active-site residues include His-19, Arg-46, Asp-109; Rossmann-like / HXGH fold | **Supported** | [PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/); [20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/) |
| NadD is essential for growth and a validated antibacterial target | **Supported** | [PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/); [12949168](https://pubmed.ncbi.nlm.nih.gov/12949168/); [19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/) |
| NadD is the convergence point of de novo + deamidated salvage (penultimate step) | **Supported** | [PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/); [20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/); [23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/) |
| NadD is a soluble cytoplasmic enzyme | **Supported (by inference)** | [PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/); [8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/) |
| NadD itself is a transcriptional regulator | **Refuted** — regulation resides in the separate NadR protein | [PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/) |
| NadD efficiently adenylylates NMN in vivo | **Refuted for wild-type** — requires protein engineering | [PMID: 28455340](https://pubmed.ncbi.nlm.nih.gov/28455340/) |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/) | Identification of the *E. coli* NaMN adenylyltransferase gene | **Foundational.** Identifies *ybeN*/*nadD*; shows reversibility, product inhibition, ≥20× NaMN preference. UniProt's EC 2.7.7.18 reference. (F004) |
| [16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/) | Analysis of *E. coli* NaMN adenylyltransferase mutants | States reaction, penultimate-step role, *nadD* essentiality; assigns active-site residues His-19/Arg-46/Asp-109. (F001, F002, F003) |
| [23289308](https://pubmed.ncbi.nlm.nih.gov/23289308/) | Overexpression of NaMN adenylyltransferase & succinate | Independently states substrate/product (NaMN→NaAD), gene, pathway. (F001) |
| [12949168](https://pubmed.ncbi.nlm.nih.gov/12949168/) | *fusB* is an allele of *nadD* | Hypomorphic alleles (nadD72, nadD74) reduce NAD⁺/NADPH; links activity to viability. (F002) |
| [19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/) | Structure-based NadD inhibitors | Essential in most bacteria; selective inhibition of ecNadD/baNadD vs human enzymes. (F002, F005) |
| [20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/) | NadD–inhibitor complexes | Crystal structures reveal conserved inhibitor/substrate binding site. (F005) |
| [28455340](https://pubmed.ncbi.nlm.nih.gov/28455340/) | Engineering *E. coli* NaMN adenylyltransferase | Engineering required to make the enzyme active on NMN → confirms native NaMN preference. (F003) |
| [20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/) | *Acinetobacter* NAD metabolism genomics | Contrasts dual-specificity NadM with NadD; documents deamidating salvage route. (F003, F006) |
| [8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/) | Quinolinate phosphoribosyltransferase (NadC) kinetics | NadC produces NaMN (de novo source of NadD substrate); soluble cytosolic. (F006, F007) |
| [23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/) | Quinolinate salvage in group A streptococci | NadD + NadE = two indispensable downstream NAD-synthesis steps. (F006) |
| [12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/) | Ribosylnicotinamide kinase domain of NadR | Amidated NMN→NAD route handled by NadR's NMNAT domain, distinct from NadD. (F008) |

Supplementary context papers reviewed: comparative genomics of NAD(P) biosynthesis and antibiotic targets ([PMID: 20857400](https://pubmed.ncbi.nlm.nih.gov/20857400/)); a review of NNAT/NaMNAT in NAD⁺ biosynthesis ([PMID: 38182101](https://pubmed.ncbi.nlm.nih.gov/38182101/)). The convergent, mutually reinforcing picture across enzymology, genetics, structural biology, and comparative genomics gives **high confidence** in the functional annotation.

---

## Limitations and Knowledge Gaps

1. **No published high-resolution crystal structure of *E. coli* NadD itself** was found in the reviewed literature; the structural model (Rossmann fold, conserved pocket) is inferred from the *Bacillus anthracis* ortholog ([PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)) and from fold/family assignments. Although orthologs are structurally conserved, residue-level details of ecNadD's active site rest partly on mutational inference ([PMID: 16153292](https://pubmed.ncbi.nlm.nih.gov/16153292/)) rather than a direct ecNadD structure in this evidence set.
2. **Quantitative steady-state kinetics** (kcat, Km for NaMN and ATP, Ki for products) and Mg²⁺ dependence for ecNadD were not extracted; the ≥20× NaMN:NMN ratio is a relative rate, not a full kinetic parameterization ([PMID: 10894752](https://pubmed.ncbi.nlm.nih.gov/10894752/)).
3. **Direct experimental localization** (fractionation/imaging) for ecNadD was not found; the cytoplasmic assignment rests on sequence features, solubility of the recombinant enzyme, and the cytosolic nature of substrates/products.
4. **Transcriptional/metabolic regulation** of *nadD* was not deeply explored. NadR transcriptionally regulates NAD biosynthesis genes ([PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)); whether *nadD* expression responds to NadR or NAD⁺ status in *E. coli* K-12 remains to be documented here.
5. The **oligomeric state** of ecNadD and any allosteric interactions were not definitively established in this evidence set.

---

## Proposed Follow-up Experiments / Actions

1. **Determine the ecNadD crystal (or cryo-EM) structure**, ideally in ternary complex with NaMN and a non-hydrolyzable ATP analog, to confirm the carboxylate-recognition pocket and validate the His-19/Arg-46/Asp-109 roles directly in the *E. coli* enzyme.
2. **Full steady-state kinetic characterization** of purified ecNadD: measure kcat and Km for NaMN, NMN, and ATP, and Ki for NaAD and PPi, to quantify specificity (kcat/Km ratio) and the product-inhibition constants; include Mg²⁺ dependence.
3. **Structure-guided specificity swap**: test minimal mutations in the carboxylate-binding pocket that interconvert NaMN vs NMN preference, building on the engineering study ([PMID: 28455340](https://pubmed.ncbi.nlm.nih.gov/28455340/)) to pinpoint specificity determinants.
4. **Conditional-depletion / essentiality confirmation** under defined salvage conditions (± niacin, ± nicotinamide riboside) to map which upstream routes can and cannot bypass NadD, directly testing the convergence-funnel model and the NadD/NadR division of labor.
5. **Advance selective inhibitors** of ecNadD toward lead optimization using the conserved druggable pocket, with counter-screening against human NMNAT1/2/3 to preserve selectivity ([PMID: 19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/); [PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)).
6. **Transcriptional-regulation mapping**: test whether ecNadD expression responds to NadR and intracellular NAD⁺ status, to complete the pathway-regulation picture.

---

## Conclusion

*E. coli* K-12 **nadD** (*ybeN*; P0A752) encodes **nicotinate-nucleotide adenylyltransferase (NaMN adenylyltransferase, EC 2.7.7.18)**, a small soluble cytoplasmic enzyme that catalyzes the reversible, product-inhibited adenylylation of nicotinate mononucleotide (NaMN + ATP → deamido-NAD⁺ + PPi) — the penultimate, essential step of NAD⁺ biosynthesis. It is strongly specific for the **deamidated** substrate NaMN (adenylylated ≥20× faster than NMN), positioning it at the **convergence point** of the de novo (via NadC) and deamidated-salvage (via PncB) routes, upstream of the final amidation by NAD synthetase (NadE); the complementary amidated NMN branch is handled separately by NadR's NMNAT domain. Built on a Rossmann-like nucleotidyltransferase fold with a conserved, druggable active site (residues His-19, Arg-46, Asp-109), NadD is essential for growth and a validated, selective broad-spectrum antibacterial drug target.


## Artifacts

- [OpenScientist final report](nadD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16153292
2. PMID:23289308
3. PMID:10894752
4. PMID:12446641
5. PMID:19716475
6. PMID:20578699
7. PMID:12949168
8. PMID:28455340
9. PMID:20926389
10. PMID:8561507
11. PMID:23204464
12. PMID:20857400
13. PMID:38182101