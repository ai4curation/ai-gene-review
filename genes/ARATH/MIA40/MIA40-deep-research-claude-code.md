---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-11T23:46:47.205955'
end_time: '2026-11-11T23:51:34.836178'
duration_seconds: 287.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: MIA40
  gene_symbol: MIA40
  uniprot_accession: Q8GYJ4
  protein_description: 'RecName: Full=Mitochondrial intermembrane space import and
    assembly protein 40 homolog {ECO:0000305}; Short=AtMIA40 {ECO:0000303|PubMed:20829360};'
  gene_info: Name=MIA40 {ECO:0000303|PubMed:20829360}; OrderedLocusNames=At5g23395
    {ECO:0000312|Araport:AT5G23395};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Not specified in UniProt
  protein_domains: CHCH. (IPR010625); CHCHD4. (IPR039289); CHCH (PF06747)
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
  web_search_requests: 5
  num_turns: 30
  total_cost_usd: 1.4129325000000001
  session_id: fb76bad3-9ade-4e0c-8aa0-bcd17990311e
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 7
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8GYJ4
- **Protein Description:** RecName: Full=Mitochondrial intermembrane space import and assembly protein 40 homolog {ECO:0000305}; Short=AtMIA40 {ECO:0000303|PubMed:20829360};
- **Gene Information:** Name=MIA40 {ECO:0000303|PubMed:20829360}; OrderedLocusNames=At5g23395 {ECO:0000312|Araport:AT5G23395};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CHCH. (IPR010625); CHCHD4. (IPR039289); CHCH (PF06747)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MIA40" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MIA40' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MIA40** (gene ID: MIA40, UniProt: Q8GYJ4) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still gathering sources; next I'm reading the full text of the plant Erv1/Mia40 paper.

I'm trying to get the full text of Carrie et al. 2010 and the SLP2 paper it cites.

I have most sources now; one more try at the Carrie et al. 2010 full text before writing the report.

# MIA40 (At5g23395, UniProt Q8GYJ4) in *Arabidopsis thaliana*: research report

## Summary

**Identity check.** The symbol, organism and domains all match the target. Q8GYJ4 is the single *A. thaliana* homologue of the yeast/human Mia40/CHCHD4 oxidoreductase. Its locus is At5g23395. It carries the CHCH domain (PF06747, IPR010625) and belongs to the CHCHD4 family (IPR039289; PANTHER PTHR21622:SF0). The primary paper on this gene, Carrie et al. 2010 (PMID:20829360), studies this exact locus. I found no literature on a different gene sharing the symbol.

**Main findings.**
- **What it is:** a small (162 aa) oxidoreductase of the intermembrane-space (IMS) disulfide relay. Its sequence has the canonical features: an N-terminal CPC redox motif and a twin Cx9C helical hairpin.
- **Where it acts:** in two places, the mitochondrial IMS and the peroxisomal matrix. It has a C-terminal PTS1 tripeptide (–SKL) and has been shown experimentally in both organelles.
- **It is not required for IMS import in plants.** Unlike yeast and animal Mia40, it is not essential. *mia40* knockouts have no visible phenotype, while *erv1* knockouts are lethal.
- **Plant Erv1 can work alone.** AtErv1 can oxidise and import IMS substrates without Mia40, helped by glutathione.
- **What depends on it:** loss of MIA40 removes CSD1 and its copper chaperone CCS from mitochondria, lowers the amount and activity of complex I, and removes CSD3 and lowers AIM1 in peroxisomes.
- **A possible regulatory role:** MIA40 forms a complex with the IMS phosphatase SLP2 and is needed for its activity, which links it to the regulation of seed germination.

---

## 1. Gene and protein identity

| Feature | Value | Source |
|---|---|---|
| Locus | At5g23395 | UniProt Q8GYJ4 (`genes/ARATH/MIA40/MIA40-uniprot.txt`) |
| Length / mass | 162 aa, 17.4 kDa | UniProt |
| CHCH domain | residues 76–120 | UniProt FT DOMAIN (PROSITE PRU01150) |
| Twin Cx9C motifs | C79–C89 and C102–C112 (predicted structural disulfides C79–C112 and C89–C102) | UniProt FT MOTIF/DISULFID (PRU01150) |
| Redox-active CPC | C68-P69-C70 (disulfide inferred by similarity to human CHCHD4, Q8N4Q1) | UniProt FT DISULFID (ECO:0000250) |
| Disordered regions | 1–61 (acidic N-terminus) and 119–162 | MobiDB-lite |
| C-terminal tripeptide | –SKL (residues 160–162), a canonical PTS1 | sequence; Peleh et al. 2017; Carrie et al. 2010 |
| Family | CHCHD4 / Mia40 | InterPro IPR039289, PANTHER PTHR21622 |

**Sequence features.** There is no cleavable N-terminal presequence. This fits the IMS-targeting model in which Mia40-family proteins are imported by their own folding: the hairpin is oxidised and folded inside the IMS, which traps the protein there.

**Where AtMIA40 differs from the yeast protein:**
- It lacks the large N-terminal transmembrane anchor of yeast Mia40.
- It resembles human CHCHD4: a soluble core that contains a CPC motif and a hydrophobic cleft for binding substrates.

**General MIA40 structure.** Zannini et al. 2023 summarise the fold: "The core structure of MIA40 is formed by two disulfide-bridged helices", together with a hydrophobic cleft and an N-terminal CPC arm (PMID:38001802, PMC10669224).

## 2. Molecular function

### 2.1 Conserved mechanism, inferred from the family

In yeast and animals, Mia40 works as a "folding trap" (reviewed in PMID:38001802):
- It recognises incoming cysteine-rich IMS precursors, typically twin Cx9C and twin Cx3C proteins such as the small TIMs, COX17 and COX19.
- It transfers a disulfide from its CPC motif to the substrate, oxidising it.
- Erv1/ALR, a homodimeric FAD-dependent sulfhydryl oxidase, then reoxidises Mia40: "Its re-oxidation is achieved by the homodimeric FAD-dependent thiol oxidase, ERV1" (PMID:38001802).

The UniProt function statement, "Required for the import and folding of small cysteine-containing proteins in the mitochondrial intermembrane space", is flagged *(Probable)* (ECO:0000305). It is a family inference, not a measurement on AtMIA40.

### 2.2 Biochemistry of AtMIA40 itself

**Redox potential.** Recombinant AtMIA40 has a midpoint redox potential of about **−295 mV at pH 7**. Its structural organisation is "rather comparable" to that of yeast Mia40 (Zannini et al. 2023, PMID:38001802).

**Electron transfer to Erv1.** In reconstituted assays, "Using AtMia40, yeast Erv1 and AtErv1 could transfer electrons to cytochrome c with comparable efficiency" (Peleh et al. 2017, BMC Biol 15:106, PMC5679390). AtMIA40 can therefore donate electrons into an Erv1–cytochrome c relay. This is an indirect, coupled assay, not a direct measurement of AtErv1 reoxidising AtMIA40.

**Substrate oxidation in vitro** (Zannini et al. 2023):
- **COX19 without glutathione:** AtMIA40 was "critical to reach a good oxidation efficiency" with AtERV1.
- **COX19 with physiological glutathione:** "the reaction was not improved by the presence of AtMIA40". Glutathione at physiological concentration and redox potential was "sufficient to support the oxidation of COX19 by AtERV1". The authors offer this as a likely reason why MIA40 is dispensable in Arabidopsis.
- **CCMH:** AtMIA40 with AtERV1 gave "very inefficient reactions". Paired with yeast Erv1, however, "AtMIA40 was now able to oxidize AtCCMH efficiently". So AtMIA40 is competent to oxidise substrates, but it is poorly coupled to its own plant Erv1.

**Interpretation.** AtMIA40 has the expected CPC-dependent thiol–disulfide oxidoreductase chemistry (a protein-disulfide oxidoreductase, transferring disulfides to substrates). In plants, though, it is an auxiliary rather than obligatory component of IMS oxidative folding. Note that GOA carries IBA/IEA rows for **GO:0015035 "protein-disulfide reductase activity"**. Mia40's physiological direction is oxidation of substrates (disulfide donation), so a term reflecting oxidase/disulfide-transfer activity would be more accurate.

### 2.3 Plant Erv1 bypasses Mia40

Peleh et al. (2017) showed that AtErv1 differs structurally from fungal and animal Erv1:
- It lacks the N-terminal shuttle arm and has a C-terminal redox-active disulfide instead.
- It can oxidise IMS proteins directly and support import in yeast without redox-active Mia40.
- It cannot oxidise yeast Mia40, and even blocks its activity.

When AtErv1-expressing yeast showed growth and substrate defects, co-expressing AtMia40 did not rescue them.

From this the authors propose a stepwise evolutionary model: the relay "obviously started from an Erv1-only system", and "Mia40 was presumably added later, initially as a dispensable player", mainly to improve substrate specificity. Plants sit at this intermediate stage. The Discussion adds that "AtMia40 might still handle specific, non-essential substrates or carry out another function" (PMC5679390).

## 3. Subcellular localisation

**Experimentally shown in two compartments** (Carrie et al. 2010, PMID:20829360):
- **Location:** "A. thaliana Mia40 is targeted to and accumulates in mitochondria and peroxisomes."
- **Sub-compartments:** UniProt records them as **mitochondrial intermembrane space** and **peroxisome matrix**, both with ECO:0000269 evidence from this paper.
- **Relative amounts:** a review of dual targeting notes that more Mia40 accumulates in mitochondria than in peroxisomes (Carrie & Small-type dual-targeting review, Plant Signal Behav, doi:10.4161/psb.25034).

**Peroxisomal targeting.** Peroxisomal localisation depends on the C-terminal SKL PTS1. Peleh et al. 2017 state that "Mia40 (AtMia40) is located both in mitochondria and peroxisomes (due to a C-terminal SKL targeting signal)". AtMIA40 (At5g23395, SKL) also appears in compiled plant peroxisomal proteome tables (Frontiers in Plant Science review, doi:10.3389/fpls.2011.00103).

**GOA cellular-component rows and how well they are supported:**
- **Strongly supported:** GO:0005758 mitochondrial intermembrane space (IDA, IBA, IEA); GO:0005739 mitochondrion (IDA); GO:0005777 peroxisome (IDA); GO:0005782 peroxisomal matrix (IDA, IEA).
- **Weak and probably spurious:** GO:0009507 chloroplast (ECO:0000255, a sequence-based prediction). AtMIA40 has no transit peptide, and no experiment places it in plastids.

## 4. Biological roles: phenotypes and dependent proteins

**Mutant phenotype** (Carrie et al. 2010):
- "Although insertional inactivation of Erv1 leads to a lethal phenotype, inactivation of Mia40 results in no detectable deleterious phenotype."
- UniProt: "No visible phenotype under normal growth conditions."

**Mitochondrial proteins that depend on MIA40:**
- Inactivation causes "an absence of copper/zinc superoxide dismutase (CSD1), the chaperone for superoxide dismutase (Ccs1) that inserts copper into CSD1, and a decrease in capacity and amount of complex I" (PMID:20829360). In yeast, CCS and SOD1 are also IMS Mia40 substrates.
- The complex I effect probably reflects loss of the twin Cx9C accessory subunits. UniProt describes MIA40 as involved in oxidative folding of complex I subunits.
- Peleh et al. refer to the "decreased complex I activity observed in Mia40 plant mutant lines".

**Peroxisomal proteins that depend on MIA40:**
- "In peroxisomes the absence of Mia40 leads to an absence of CSD3 and a decrease in abnormal inflorescence meristem 1 (Aim1), a β-oxidation pathway enzyme" (PMID:20829360). AIM1 is the multifunctional protein of fatty-acid β-oxidation.
- These are the "novel functions" in the paper's title. They suggest MIA40 contributes to folding or Cu,Zn-SOD maturation in the peroxisomal matrix.
- How this works in an organelle that has no Erv1 is unresolved.

**Transcriptome:** "genes encoding peroxisomal proteins, redox functions, and biotic stress significantly changing in abundance" in *mia40* plants (PMID:20829360).

**GOA process rows** that rest on this work, by IMP:
- GO:0070585 protein localization to mitochondrion
- GO:0006625 protein targeting to peroxisome

Both carry the "acts_upstream_of_or_within" qualifier. The data show that certain proteins fail to accumulate in each organelle. They do not show that MIA40 performs the targeting step. A more precise reading is oxidative folding, maturation or stabilisation of imported proteins: GO:0051604 protein maturation (IBA), or GO:0045041 protein import into mitochondrial intermembrane space (IBA/IEA). Because mutants keep IMS import, GO:0045041 holds as a conserved family role, but MIA40 is not required for it in Arabidopsis.

**MIA40 and SLP2 in seed germination** (Uhrig et al. 2017, Plant Physiol 173:956–969, PMID:27923987):
- Arabidopsis SLP2 (Shewanella-like protein phosphatase 2) is an IMS serine/threonine phosphatase that "interacts with the mitochondrial oxidoreductase import and assembly protein 40" (AtMIA40).
- Binding to MIA40, which depends on SLP2 disulfide bridges, is required for SLP2 phosphatase activity.
- Mutant, complemented and overexpressor lines implicate the SLP2–MIA40 complex in suppressing gibberellin-related processes during germination.
- This makes SLP2 a candidate MIA40 client or partner in which MIA40 activates a regulatory enzyme, probably by oxidative folding.
- Caveat: I could read only the abstract. The interaction methods and any germination phenotype of *mia40* itself were not verified.

## 5. Pathway context

```
Mitochondrion (IMS):
  cytosolic precursors (Cx9C/Cx3C, CCS, CSD1, complex I accessory subunits, SLP2?)
      → TOM → IMS
      → AtMIA40 (CPC) oxidises → folded, trapped substrate
            ↑ reoxidised (inefficiently) by
      AtERV1 (FAD sulfhydryl oxidase; essential) → cytochrome c → complex IV
  Parallel route: AtERV1 + GSH oxidise substrates directly (MIA40-independent)

Peroxisome (matrix, PTS1-SKL import of MIA40):
  MIA40 needed for accumulation of CSD3 and full AIM1 levels (mechanism unknown)
```

## 6. Annotation-relevant synthesis

| Aspect | Best-supported statement | Evidence strength |
|---|---|---|
| MF | Protein-disulfide oxidoreductase that donates disulfides to substrates (CPC motif; redox potential −295 mV; oxidises COX19 and CCMH in vitro) | In vitro biochemistry + family; "reductase" labelling questionable |
| BP | Oxidative folding and maturation of IMS proteins (CSD1, CCS, complex I subunits); contributes to, but is not required for, IMS import | IMP proteomics; reconstitution |
| BP | Maturation of peroxisomal CSD3 and AIM1 | IMP proteomics (novel, mechanism unknown) |
| BP | Activation of SLP2 phosphatase; germination via gibberellin | Single study, abstract-level |
| CC | Mitochondrial IMS; peroxisomal matrix | IDA (GFP, fractionation, PTS1) |
| CC | Chloroplast | Prediction only; unsupported |

## 7. Open questions
1. What does MIA40 do mechanistically in peroxisomes, an organelle with no Erv1-type oxidase? What reoxidises it there, and does it need its CPC redox activity?
2. Which IMS substrates, if any, strictly need MIA40 in plants (CSD1 and CCS are candidates)? Would CPC→SPS mutant complementation of *mia40* answer this?
3. Is the complex I deficit caused directly by failed folding of Cx9C subunits?
4. Does *mia40* show a germination or GA phenotype like *slp2*, and is SLP2 a direct oxidative-folding substrate?

## Limitations

The full text of Carrie et al. 2010 (J Biol Chem 285:36138–48) could not be retrieved: PMC and JBC blocked access, and only the abstract is cached locally. Details such as T-DNA line names, GFP constructs, SKL-deletion experiments and small-TIM import assays therefore could not be checked directly. The Uhrig et al. 2017 claims rest on the abstract. The Peleh et al. 2017 and Zannini et al. 2023 statements come from Europe PMC full text.

## References
- Carrie C, Giraud E, Duncan O, … Whelan J. Conserved and novel functions for *Arabidopsis thaliana* MIA40 in assembly of proteins in mitochondria and peroxisomes. *J Biol Chem* 2010;285:36138–48. PMID:20829360; PMC2975236; doi:10.1074/jbc.M110.121202. https://pmc.ncbi.nlm.nih.gov/articles/PMC2975236
- Peleh V, Zannini F, Backes S, Rouhier N, Herrmann JM. Erv1 of *Arabidopsis thaliana* can directly oxidize mitochondrial intermembrane space proteins in the absence of redox-active Mia40. *BMC Biol* 2017;15:106. PMC5679390. https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-017-0445-8
- Zannini F, Herrmann JM, Couturier J, Rouhier N. Oxidation of *Arabidopsis thaliana* COX19 using the combined action of ERV1 and glutathione. *Antioxidants* 2023;12:1949. PMID:38001802; PMC10669224. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10669224/ ; https://hal.inrae.fr/hal-04592940
- Uhrig RG, Labandera AM, Tang LY, … Moorhead GB. Activation of mitochondrial protein phosphatase SLP2 by MIA40 regulates seed germination. *Plant Physiol* 2017;173:956–969. PMID:27923987. https://pubmed.ncbi.nlm.nih.gov/27923987/
- Plant peroxisomal proteome review listing MIA40/At5g23395 with SKL: *Front Plant Sci* 2011, doi:10.3389/fpls.2011.00103. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2011.00103/full
- Widespread dual targeting of proteins in land plants. *Plant Signal Behav*, doi:10.4161/psb.25034. https://www.tandfonline.com/doi/full/10.4161/psb.25034
- UniProtKB Q8GYJ4 (MIA40_ARATH) and the QuickGO annotation set, local copies in `genes/ARATH/MIA40/`.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC2975236
2. https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-017-0445-8
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10669224/
4. https://hal.inrae.fr/hal-04592940
5. https://pubmed.ncbi.nlm.nih.gov/27923987/
6. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2011.00103/full
7. https://www.tandfonline.com/doi/full/10.4161/psb.25034