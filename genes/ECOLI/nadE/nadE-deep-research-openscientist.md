---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T05:10:26.774318'
end_time: '2026-11-12T05:20:37.829354'
duration_seconds: 611.06
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P18843
  gene_symbol: nadE
  uniprot_accession: P18843
  protein_description: 'RecName: Full=NH(3)-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_00193,
    ECO:0000303|PubMed:8195100}; EC=6.3.1.5 {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000269|PubMed:8195100};
    AltName: Full=Nicotinamide adenine dinucleotide synthetase; Short=NADS; AltName:
    Full=Nitrogen regulatory protein;'
  gene_info: Name=nadE {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000303|PubMed:8195100};
    Synonyms=efg {ECO:0000303|PubMed:1512214}, ntrL; OrderedLocusNames=b1740, JW1729;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the NAD synthetase family. {ECO:0000255|HAMAP-
  protein_domains: NAD/GMP_synthase. (IPR022310); NAD_synthase. (IPR003694); NH(3)-dep_NAD(+)_synth.
    (IPR022926); Rossmann-like_a/b/a_fold. (IPR014729); NAD_synthase (PF02540)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P18843
- **Protein Description:** RecName: Full=NH(3)-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000303|PubMed:8195100}; EC=6.3.1.5 {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000269|PubMed:8195100}; AltName: Full=Nicotinamide adenine dinucleotide synthetase; Short=NADS; AltName: Full=Nitrogen regulatory protein;
- **Gene Information:** Name=nadE {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000303|PubMed:8195100}; Synonyms=efg {ECO:0000303|PubMed:1512214}, ntrL; OrderedLocusNames=b1740, JW1729;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the NAD synthetase family. {ECO:0000255|HAMAP-
- **Key Domains:** NAD/GMP_synthase. (IPR022310); NAD_synthase. (IPR003694); NH(3)-dep_NAD(+)_synth. (IPR022926); Rossmann-like_a/b/a_fold. (IPR014729); NAD_synthase (PF02540)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadE" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadE** (gene ID: P18843, UniProt: P18843) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# NadE (P18843) — NH₃-dependent NAD⁺ synthetase of *Escherichia coli* K-12

## Functional Annotation Report

**UniProt:** P18843 · **Gene:** *nadE* (synonyms *efg*, *ntrL*; ordered locus b1740 / JW1729) · **EC 6.3.1.5** · **Organism:** *Escherichia coli* strain K-12

---

## Summary

**NadE (UniProt P18843; gene *nadE*, synonyms *efg*, *ntrL*; ordered locus b1740/JW1729) encodes the ammonia-dependent NAD⁺ synthetase of *Escherichia coli* K-12 (EC 6.3.1.5).** It is the enzyme that catalyzes the final, obligatory step of nicotinamide adenine dinucleotide (NAD⁺) biosynthesis: the ATP-dependent amidation of nicotinic acid adenine dinucleotide (NaAD, also called deamido-NAD⁺) to yield NAD⁺. The reaction uses free ammonia as the nitrogen donor and requires Mg²⁺, consuming ATP and releasing AMP and pyrophosphate (PPi). This is the terminal chemistry of NAD⁺ production in the cell, and because NAD⁺/NADP⁺ participate in roughly 12% of all biochemical reactions in the *E. coli* K-12 metabolic model, NadE sits at a metabolic chokepoint of exceptional importance.

The enzyme is a soluble, cytoplasmic homodimer with an α/β (Rossmann-like) single-domain fold that places it in the "N-type" ATP pyrophosphatase (adenine-nucleotide α-hydrolase) superfamily, alongside GMP synthetase, asparagine synthetase, and argininosuccinate synthetase. Crystal structures of the *E. coli* enzyme — captured alone, with natural substrates, and with the product NAD⁺ — reveal two NaAD/NAD binding sites at the dimer interface and one ATP site within each subunit, and they document a two-state conformational cycle ("catalysis" and "substrate/product exchange" states) driven by Mg²⁺ coordination. Mechanistically, NadE operates by two chemical steps: (1) ATP activates the carboxylate of NaAD to form a covalent NAD-adenylate intermediate (releasing PPi), and (2) ammonia performs a nucleophilic attack on this intermediate to form the amide, releasing AMP. The *E. coli* enzyme, unlike the glutamine-dependent NAD synthetases of eukaryotes and some bacteria (e.g., *Mycobacterium tuberculosis*), lacks an N-terminal glutamine amidotransferase (nitrilase-superfamily) domain and is strictly ammonia-dependent.

NadE is the single convergence point of all NAD⁺ biosynthetic routes in *E. coli*: both the *de novo* pathway (*nadA/nadB/nadC*) and the Preiss–Handler salvage pathway (*pncA/pncB*) funnel into nicotinate mononucleotide (NaMN), which NadD adenylylates to NaAD, which NadE then amidates to NAD⁺. Loss of NadE function is lethal — temperature-sensitive *nadE* mutants accumulate large internal pools of NaAD and cannot make NAD⁺ at the non-permissive temperature — establishing the gene as essential and validating the enzyme as an antibacterial drug target with exploitable species-specific active-site differences.

---

## Key Findings

### 1. NadE catalyzes the terminal amidation step of NAD⁺ biosynthesis

NadE is the structural gene for NAD⁺ synthetase, the enzyme that performs the last metabolic step of NAD⁺ biosynthesis. The reaction is the amidation of nicotinic acid adenine dinucleotide (NaAD/deamido-NAD⁺) to produce NAD⁺. This was established both biochemically and genetically. Structural studies of NAD synthetases describe the core chemistry directly: "*Nicotinamide adenine dinucleotide synthetases (NADS) catalyze the amidation of nicotinic acid adenine dinucleotide (NAAD) to yield the enzyme cofactor nicotinamide adenine dinucleotide (NAD)*" ([PMID: 15699042](https://pubmed.ncbi.nlm.nih.gov/15699042/)).

The genetic identification came from the orthologous system in *Salmonella typhimurium*, where the gene "*designated nadE*" was shown to encode "*NAD synthetase, which catalyzes the final metabolic step in NAD biosynthesis*" ([PMID: 2834324](https://pubmed.ncbi.nlm.nih.gov/2834324/)). Crucially, that same study showed that loss-of-function strains "*accumulate large internal pools of nicotinic acid adenine dinucleotide, the substrate for NAD synthetase*" ([PMID: 2834324](https://pubmed.ncbi.nlm.nih.gov/2834324/)) — a direct in vivo demonstration that NaAD is the substrate and that NadE is responsible for its conversion to NAD⁺.

**Overall reaction:**

```
NaAD (deamido-NAD⁺) + ATP + NH₃  ──Mg²⁺──▶  NAD⁺ + AMP + PPi
```

### 2. NadE is a homodimer with substrate sites at the dimer interface and an ATP site per subunit

Crystal structures of the ammonia-dependent *E. coli* enzyme — solved alone, with natural substrates, and with the product NAD⁺ — established its quaternary architecture. "*The structures disclosed two NAAD/NAD binding sites at the dimer interface and an adenosine triphosphate (ATP) binding site within each subunit*" ([PMID: 15699042](https://pubmed.ncbi.nlm.nih.gov/15699042/)). The pyridine (NaAD/NAD) sites are therefore built from both subunits, consistent with the obligate dimeric organization of the enzyme.

These structures also captured the enzyme in motion. "*The E. coli NADS structures revealed unexpected dynamical rearrangements in the NAAD/NAD binding pocket upon NAAD-to-NAD conversion, which define a catalysis state and a substrate/product exchange state*" ([PMID: 15699042](https://pubmed.ncbi.nlm.nih.gov/15699042/)). The conversion is driven by concerted movement of the nicotinysyl moiety together with Phe-170 and residues 224–228, triggered by differential Mg²⁺ coordination — explaining how the active site reconfigures between performing chemistry and exchanging substrate for product.

### 3. A two-step mechanism: ATP-driven adenylation of NaAD, then ammonia attack

The catalytic chemistry of NH₃-dependent NAD⁺ synthetases proceeds via a covalent reaction intermediate. An atomic-resolution (1 Å) structure of the homologous *Bacillus subtilis* enzyme co-crystallized with NaAD and ATP showed that "*Both binding sites are occupied by the NAD-adenylate intermediate, pyrophosphate and two magnesium ions*" ([PMID: 12077433](https://pubmed.ncbi.nlm.nih.gov/12077433/)). This captures the key intermediate: ATP activates the carboxylate of NaAD to form NAD-adenylate, releasing pyrophosphate.

The second step is amide-bond formation. The same study proposed "*a mechanism... for the second catalytic step, which includes a nucleophilic attack by the ammonia molecule on the intermediate*" ([PMID: 12077433](https://pubmed.ncbi.nlm.nih.gov/12077433/)). Ammonia attacks the activated acyl-adenylate carbon, displacing AMP and forming the carboxamide that defines NAD⁺. This two-step chemistry (adenylation then amidation) is conserved across NH₃-dependent bacterial NAD synthetases, including *E. coli* NadE.

### 4. Membership in the ATP pyrophosphatase family and strict ammonia dependence

NadE belongs to the ATP pyrophosphatase (adenine-nucleotide α-hydrolase, "N-type") family. The defining structural work on GMP synthetase noted the conserved nucleotide-binding fingerprint "*common to a family of ATP pyrophosphatases, including NAD synthetase, asparagine synthetase and argininosuccinate synthetase*" ([PMID: 8548458](https://pubmed.ncbi.nlm.nih.gov/8548458/)). These enzymes share a nucleotide-binding fold and the mechanistic logic of adenylating a substrate carboxylate before nucleophilic substitution.

A central distinction defines the *E. coli* enzyme's substrate specificity for the nitrogen donor. Many bacterial NAD synthetases, including *E. coli*'s, are ammonia-dependent: "*many purified prokaryotic NAD+ synthetases are ammonia-dependent*" ([PMID: 12771147](https://pubmed.ncbi.nlm.nih.gov/12771147/)). In contrast, the *M. tuberculosis* enzyme "*utilizes both glutamine and ammonia to catalyze NAD(+) production, in contrast to the corresponding NH(3)-dependent enzymes from other prokaryotes*" ([PMID: 15748981](https://pubmed.ncbi.nlm.nih.gov/15748981/)). The glutamine-utilizing enzymes carry an N-terminal nitrilase-superfamily glutamine amidotransferase (GAT) domain that generates ammonia in situ from glutamine; the single-domain *E. coli* NadE lacks this domain and therefore depends on exogenous free ammonium as its nitrogen source.

### 5. Biochemical requirements: Mg²⁺ dependence and alkaline pH optimum

Recombinant *E. coli* NAD synthetase purified to homogeneity was characterized enzymatically. The enzyme "*required approximately 1.5 mM magnesium for optimal activity. The pH optimum was found to be 8.0-8.5*" ([PMID: 10544053](https://pubmed.ncbi.nlm.nih.gov/10544053/)). The Mg²⁺ requirement is consistent with the two-metal coordination seen in the atomic-resolution intermediate structure (two Mg²⁺ ions at the active site), and the alkaline pH optimum is consistent with a mechanism that relies on the neutral/unprotonated ammonia species as the nucleophile. The protein was crystallized with substrates NaAD and ATP, diffracting to 2.0 Å in space group P3₁21.

### 6. NadE is the common terminal convergence point of all NAD⁺ biosynthetic routes

In *E. coli* (and *Salmonella*), NAD⁺ can be made by two upstream routes that converge on a single shared terminal sequence. The *de novo* pathway (*nadA*, *nadB*, *nadC*) and the salvage/Preiss–Handler pathway both produce nicotinate mononucleotide (NaMN); NaMN is adenylylated by NadD to NaAD; and NadE then amidates NaAD to NAD⁺. Thus every route to NAD⁺ passes through the NadE step.

The conserved *de novo* gene set is well established: "*the de novo pathway to nicotinamide adenine dinucleotide and the genes governing the enzymes involved in this pathway in S. typhimurium are very similar to those in E. coli*" ([PMID: 203571](https://pubmed.ncbi.nlm.nih.gov/203571/)). The salvage contribution is described in the context of NAD homeostasis: NadE, "*together with nicotinamide deamidase (PncA), compose the major pathway for utilization of the pyridine ring in the form of amidated (Nm) or deamidated (Na) precursors*" ([PMID: 26443758](https://pubmed.ncbi.nlm.nih.gov/26443758/)). The broad metabolic weight of the product underscores why this chokepoint matters: NAD and NADP "*collectively contribute to approximately 12% of all biochemical reactions included in the metabolic model of Escherichia coli K-12*" ([PMID: 26443758](https://pubmed.ncbi.nlm.nih.gov/26443758/)).

### 7. Subcellular localization: a soluble cytoplasmic enzyme

NadE functions in the bacterial cytoplasm. It was "*overexpressed and purified to homogeneity. The recombinant protein was active in an in vitro enzyme assay*" ([PMID: 10544053](https://pubmed.ncbi.nlm.nih.gov/10544053/)), behaving as a soluble protein crystallized from aqueous conditions. Its substrates and product (NaAD, ATP, Mg²⁺, ammonium, NAD⁺) are exclusively cytoplasmic small molecules, and the protein is a single-domain soluble α/β enzyme with no signal peptide or transmembrane segment. The combined evidence places NadE firmly in the cytosol, where it carries out its reaction as part of soluble central metabolism.

### 8. Catalytic site at a β-sheet switch point with a conserved P-loop serine

The founding crystallographic analysis of an NH₃-dependent NAD⁺ synthetase (the *B. subtilis* ortholog, as the free form and ATP complex at 2.6/2.0 Å) defined the architectural basis of catalysis. "*The enzyme consists of a tight homodimer with alpha/beta subunit topology. The catalytic site is located at the parallel beta-sheet topological switch point, where one AMP molecule, one pyrophosphate and one Mg2+ ion are observed*" ([PMID: 8895556](https://pubmed.ncbi.nlm.nih.gov/8895556/)).

A conserved active-site serine from the "P-loop" was implicated in the first chemical step: "*Residue Ser46, part of the neighboring 'P-loop', is hydrogen bonded to the pyrophosphate group, and may play a role in promoting the adenylation of deamido-NAD+ during the first step of the catalyzed reaction*" ([PMID: 8895556](https://pubmed.ncbi.nlm.nih.gov/8895556/)). On the basis of its conserved catalytic fingerprint, the study concluded that "*NAD+ synthetase belongs to the newly discovered family of 'N-type' ATP pyrophosphatases*" ([PMID: 8895556](https://pubmed.ncbi.nlm.nih.gov/8895556/)). This architecture — interfacial NaAD/NAD sites, per-subunit ATP sites, and a P-loop serine — is shared by the *E. coli* enzyme, whose own structures confirmed the same arrangement.

### 9. NadE is essential and a validated antibacterial drug target

Because NAD⁺ is indispensable and NadE catalyzes its sole terminal biosynthetic step, loss of the enzyme is lethal. "*Mutants of nadE include those with a temperature-sensitive lethal phenotype*" ([PMID: 2834324](https://pubmed.ncbi.nlm.nih.gov/2834324/)); at the non-permissive temperature these cells accumulate NaAD and cannot complete NAD⁺ synthesis. This essentiality, combined with structural knowledge, makes NadE an attractive drug target. The *E. coli* structural study emphasized that cross-species active-site differences are "*relevant for designing species-specific antibiotics*" ([PMID: 15699042](https://pubmed.ncbi.nlm.nih.gov/15699042/)), and work on the *M. tuberculosis* ortholog independently concluded that "*the enzyme represents a valid target for the development of new antimycobacterial agents*" ([PMID: 12182838](https://pubmed.ncbi.nlm.nih.gov/12182838/)).

---

## Mechanistic Model / Interpretation

### The reaction and its two chemical steps

NadE converts the metabolic precursor NaAD into the ubiquitous redox cofactor NAD⁺ by installing an amide nitrogen on the pyridine carboxylate. The transformation is energetically coupled to ATP hydrolysis and proceeds through a covalent acyl-adenylate intermediate:

```
Step 1 — Adenylation (activation)
   NaAD–COO⁻ + ATP·Mg²⁺  ─▶  NaAD–CO–O–AMP (NAD-adenylate) + PPi
        │                                   (P-loop Ser stabilizes PPi;
        │                                    two Mg²⁺ coordinate phosphates)
Step 2 — Amidation (nucleophilic substitution)
   NaAD–CO–O–AMP + NH₃   ─▶  NAD⁺ (NaAD–CO–NH₂) + AMP
```

The first step activates the otherwise unreactive carboxylate by converting it into a high-energy mixed anhydride with AMP; the second step uses ammonia as the nucleophile to displace AMP and form the amide. This logic is the shared signature of the N-type ATP pyrophosphatase family (GMP synthetase, asparagine synthetase, argininosuccinate synthetase), all of which adenylate a substrate before nucleophilic substitution.

### Architecture ↔ mechanism

```
        ┌─────────────── Homodimer (tight α/β) ───────────────┐
        │                                                     │
   Subunit A                                             Subunit B
   [ ATP site ]                                         [ ATP site ]
        \                                                   /
         \________ NaAD/NAD site 1  ·  NaAD/NAD site 2 _____/
                   (at the dimer interface, built from both subunits)

   Catalytic site = parallel β-sheet topological switch point
   P-loop Ser (e.g., Ser46 in B. subtilis) H-bonds pyrophosphate
   Two Mg²⁺ ions coordinate the phosphates of the adenylate intermediate
```

The *E. coli* structures add a dynamic dimension: as NaAD is converted to NAD⁺, the pocket toggles between a **catalysis state** and a **substrate/product exchange state**, with the nicotinysyl moiety, Phe-170, and residues 224–228 moving in concert under the control of Mg²⁺ coordination. This conformational cycling reconciles the need for a tightly organized active site during chemistry with the need to release product and load fresh substrate.

### Pathway context — the metabolic chokepoint

```
 DE NOVO (from aspartate)                 SALVAGE / Preiss–Handler
   nadB ─▶ nadA ─▶ nadC                    Nicotinamide ─pncA▶ Nicotinate
                      │                                            │ pncB
                      ▼                                            ▼
                    NaMN  ◀───────────────────────────────────── NaMN
                      │
                   nadD (adenylylation)
                      ▼
                    NaAD  (deamido-NAD⁺)
                      │
             ┌────────┴─────────┐
             │   nadE  (NadE)   │  ATP + NH₃, Mg²⁺ ─▶ AMP + PPi
             └────────┬─────────┘
                      ▼
                    NAD⁺   ──▶ ~12% of all E. coli biochemical reactions
```

Every biosynthetic route to NAD⁺ in *E. coli* — whether built *de novo* from aspartate or salvaged from pyridine precursors — must pass through the NadE-catalyzed amidation of NaAD. This single-point convergence explains both the strict essentiality of *nadE* and why its inhibition is lethal regardless of nutrient availability.

### Nitrogen-donor specificity

| Property | *E. coli* NadE (P18843) | Glutamine-dependent NADS (e.g., *M. tuberculosis*, eukaryotes) |
|---|---|---|
| Nitrogen donor | Free ammonia (NH₃/NH₄⁺) | Glutamine (and ammonia) |
| GAT (nitrilase) domain | Absent — single domain | Present — N-terminal amidotransferase |
| Domain organization | One catalytic synthetase domain | Two-domain (GAT + synthetase) |
| Family | N-type ATP pyrophosphatase | N-type ATP pyrophosphatase + nitrilase superfamily |

The *E. coli* enzyme's reliance on free ammonia is a defining biochemical feature and a point of mechanistic and evolutionary contrast with the glutamine-hydrolyzing enzymes.

---

## Evidence Base

| PMID | Title (abbrev.) | Organism / enzyme | How it supports the findings |
|---|---|---|---|
| [15699042](https://pubmed.ncbi.nlm.nih.gov/15699042/) | *Structures of E. coli NAD synthetase with substrates and products reveal mechanistic rearrangements* | *E. coli* NadE | Direct structural evidence for the reaction (NaAD→NAD amidation), the homodimer with two interfacial NaAD/NAD sites + per-subunit ATP site, the catalysis/exchange conformational cycle, and species-specific inhibitor design (F001, F002, F009). |
| [2834324](https://pubmed.ncbi.nlm.nih.gov/2834324/) | *Structural gene for NAD synthetase in Salmonella typhimurium* | *Salmonella* (ortholog) | Genetic identification of *nadE* as the final-step gene; NaAD accumulation in mutants proves substrate identity; temperature-sensitive lethal alleles prove essentiality (F001, F009). |
| [12077433](https://pubmed.ncbi.nlm.nih.gov/12077433/) | *NH3-dependent NAD+ synthetase from B. subtilis at 1 Å resolution* | *B. subtilis* (ortholog) | Atomic-resolution capture of the NAD-adenylate intermediate + PPi + two Mg²⁺; proposes ammonia nucleophilic attack as step 2 (F003). |
| [8895556](https://pubmed.ncbi.nlm.nih.gov/8895556/) | *Crystal structure of NH3-dependent NAD+ synthetase from B. subtilis* | *B. subtilis* (ortholog) | Founding structure: tight α/β homodimer; catalytic site at β-sheet switch point with AMP/PPi/Mg²⁺; P-loop Ser46 promotes adenylation; assigns N-type ATP pyrophosphatase family (F008). |
| [8548458](https://pubmed.ncbi.nlm.nih.gov/8548458/) | *Crystal structure of GMP synthetase...* | Structural paradigm | Defines the ATP pyrophosphatase family (NAD synthetase, asparagine synthetase, argininosuccinate synthetase) sharing the nucleotide-binding fold (F004). |
| [15748981](https://pubmed.ncbi.nlm.nih.gov/15748981/) | *Glutamine amidotransferase activity of NAD+ synthetase from M. tuberculosis...* | *M. tuberculosis* | Contrasts glutamine-dependent enzymes with the NH₃-dependent prokaryotic enzymes (e.g., *E. coli*); defines the N-terminal nitrilase/GAT domain absent in NadE (F004). |
| [12771147](https://pubmed.ncbi.nlm.nih.gov/12771147/) | *Eukaryotic NAD+ synthetase Qns1 contains... thiol glutamine amidotransferase domain* | Eukaryotic Qns1 | Confirms that many prokaryotic NAD synthetases are ammonia-dependent, in contrast to the eukaryotic glutamine-utilizing enzyme (F004). |
| [10544053](https://pubmed.ncbi.nlm.nih.gov/10544053/) | *Structural study of E. coli NAD synthetase: overexpression, purification, crystallization* | *E. coli* NadE | Biochemical characterization: soluble active recombinant enzyme; ~1.5 mM Mg²⁺ optimum; pH optimum 8.0–8.5; crystallized with NaAD + ATP (F005, F007). |
| [26443758](https://pubmed.ncbi.nlm.nih.gov/26443758/) | *Biogenesis and Homeostasis of NAD Cofactor* | Review (*E. coli* K-12) | Quantifies NAD/NADP's ~12% of metabolic reactions; situates NadE + PncA in the salvage route converging on the shared terminal sequence (F006). |
| [203571](https://pubmed.ncbi.nlm.nih.gov/203571/) | *Mapping and characterization of the nad genes in S. typhimurium* | *Salmonella* / *E. coli* | Establishes the conserved *de novo* *nadA/B/C* gene set feeding the precursor to the NadE step (F006). |
| [12182838](https://pubmed.ncbi.nlm.nih.gov/12182838/) | *Heterologous expression... of M. tuberculosis NAD(+) synthetase* | *M. tuberculosis* | Independent validation of NAD synthetase as an antibacterial drug target (F009). |

**Supporting / contextual literature:** *Structural adaptation of an interacting non-native C-terminal helical extension... NAD+ synthetase from Bacillus anthracis* ([PMID: 17642516](https://pubmed.ncbi.nlm.nih.gov/17642516/)) compares *B. anthracis*, *B. subtilis*, *E. coli*, and *H. pylori* enzyme structures and corroborates the conserved fold and loop ordering; *Structural biology of enzymes involved in NAD and molybdenum cofactor biosynthesis* ([PMID: 12504674](https://pubmed.ncbi.nlm.nih.gov/12504674/)) frames the pathway-level structural context and drug-design rationale; *Using genomic information to investigate the function of ThiI* ([PMID: 10595545](https://pubmed.ncbi.nlm.nih.gov/10595545/)) illustrates the shared "P-loop"/adenylation motif of the PPi synthetase family relevant to the mechanism; and *The MTCY428.08 gene of M. tuberculosis codes for NAD+ synthetase* ([PMID: 9620974](https://pubmed.ncbi.nlm.nih.gov/9620974/)) confirms the ortholog's activity.

---

## Identity Verification

The research target was confirmed to be the correct gene/protein throughout:

- **Gene symbol ↔ protein:** The symbol *nadE* corresponds precisely to NH₃-dependent NAD⁺ synthetase (EC 6.3.1.5), matching the UniProt description for P18843.
- **Organism:** All primary functional and structural data for the *E. coli* enzyme (PMIDs 15699042, 10544053) are from *E. coli* K-12; genetic identification is from the closely related, essentially identical *Salmonella* ortholog (PMID 2834324), with mechanistic detail from conserved *Bacillus* orthologs.
- **Family/domains:** Literature places NadE in the NAD synthetase family / N-type ATP pyrophosphatase superfamily with a Rossmann-like α/β fold — consistent with the listed InterPro/Pfam domains (IPR003694, IPR022926, IPR014729, PF02540).
- **No ambiguity encountered.** The *efg/ntrL* synonyms reflect historical naming (the "nitrogen regulatory protein" AltName), but the biochemical identity as the terminal NAD⁺ synthetase is unambiguous and well supported.

---

## Limitations and Knowledge Gaps

1. **Direct enzymological parameters for the *E. coli* enzyme are sparse in the reviewed set.** Precise kinetic constants (kcat, Km for NaAD, ATP, and ammonium) and the quantitative preference for ammonia over glutamine were not captured in the cited abstracts. While ammonia dependence is well established for prokaryotic NadE as a class, quantitative substrate-affinity data specific to P18843 would strengthen the annotation.

2. **Atomic-resolution intermediate capture is from orthologs, not *E. coli* itself.** The NAD-adenylate intermediate was visualized at 1 Å in *B. subtilis* (PMID 12077433). The *E. coli* structures (PMID 15699042) show substrate/product states and conformational dynamics, but the covalent intermediate structure cited is from the ortholog. Family-wide conservation makes the extrapolation sound, but an *E. coli*-specific intermediate structure would close the gap.

3. **The *ntrL*/"nitrogen regulatory protein" alternative name is unexplained by the reviewed literature.** Whether NadE has any genuine regulatory/moonlighting role connected to nitrogen metabolism (beyond consuming ammonia as a substrate) was not resolved. This historical annotation deserves scrutiny.

4. **Regulation of *nadE* expression and NAD⁺ pool homeostasis** at the physiological level was addressed only broadly (PMID 26443758). How NadE activity is tuned to NAD⁺ demand in *E. coli* is not detailed here.

5. **In vivo flux and metabolic control analysis** quantifying how much NadE actually limits NAD⁺ flux under various growth conditions was not examined.

---

## Proposed Follow-up Experiments / Actions

1. **Determine steady-state kinetics for the *E. coli* enzyme (P18843):** measure kcat and Km for NaAD, ATP, and NH₄⁺, and quantitatively test for any glutamine-dependent activity to formally confirm strict ammonia dependence in the *E. coli* context.

2. **Solve or retrieve an *E. coli*-specific NAD-adenylate intermediate structure** (co-crystallization or cryo-trapping with NaAD + non-hydrolyzable ATP analog + Mg²⁺) to directly visualize the covalent intermediate in P18843 and validate the two Mg²⁺ coordination seen in orthologs.

3. **Site-directed mutagenesis of the conserved P-loop serine and the mobile Phe-170/residues 224–228** in the *E. coli* enzyme to test their proposed roles in adenylation and in the catalysis/exchange conformational switch.

4. **Resolve the *ntrL* "nitrogen regulatory protein" annotation:** perform transcriptomic/phenotypic analysis of defined *nadE* conditional mutants under varied nitrogen regimes to determine whether any regulatory role exists beyond ammonia consumption, or formally retire the annotation.

5. **Structure-guided, species-selective inhibitor discovery:** exploit the documented cross-species active-site differences (PMID 15699042) to design *E. coli*-selective NadE inhibitors, using essentiality (PMID 2834324) as target validation and the orthologous drug-target precedent (PMID 12182838) as a template.

6. **Metabolic flux / control analysis** of NAD⁺ biosynthesis across growth conditions to quantify NadE's contribution to pathway flux and confirm its status as the terminal chokepoint under physiological demand.

---

## Conclusion

*E. coli* **NadE (P18843)** is the ammonia-dependent NAD⁺ synthetase (EC 6.3.1.5), a soluble cytoplasmic homodimer that catalyzes the final, essential step of NAD⁺ biosynthesis — the ATP- and Mg²⁺-dependent amidation of nicotinic acid adenine dinucleotide (NaAD) to NAD⁺, using free ammonia as the nitrogen donor and proceeding through an NAD-adenylate intermediate. As a member of the N-type ATP pyrophosphatase family with substrate sites at the dimer interface and a per-subunit ATP site, it functions as the single convergence point of both the *de novo* (*nadA/B/C*) and salvage/Preiss–Handler (*pncA/pncB*) pathways. Its essentiality, demonstrated by lethal *nadE* mutants that accumulate NaAD, makes it a validated antibacterial drug target with exploitable species-specific active-site features.


## Artifacts

- [OpenScientist final report](nadE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15699042
2. PMID:2834324
3. PMID:12077433
4. PMID:8548458
5. PMID:12771147
6. PMID:15748981
7. PMID:10544053
8. PMID:26443758
9. PMID:8895556
10. PMID:12182838
11. PMID:17642516
12. PMID:12504674
13. PMID:10595545
14. PMID:9620974