---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T22:21:14.064840'
end_time: '2026-09-26T22:29:51.781393'
duration_seconds: 517.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: LCYE
  gene_symbol: LUT2
  uniprot_accession: Q38932
  protein_description: 'RecName: Full=Lycopene epsilon cyclase, chloroplastic {ECO:0000303|PubMed:8837512};
    EC=5.5.1.18 {ECO:0000269|PubMed:11226339, ECO:0000269|PubMed:8837512}; AltName:
    Full=Protein LUTEIN DEFICIENT 2 {ECO:0000303|PubMed:9789087}; Flags: Precursor;'
  gene_info: Name=LUT2 {ECO:0000303|PubMed:9789087}; OrderedLocusNames=At5g57030 {ECO:0000312|Araport:AT5G57030};
    ORFNames=MHM17.16 {ECO:0000312|EMBL:BAA97033.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the lycopene cyclase family. .
  protein_domains: FAD/NAD-bd_sf. (IPR036188); Lycopene_cyclase_b/e. (IPR010108);
    Lycopene_cycl (PF05834)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: LCYE-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q38932
- **Protein Description:** RecName: Full=Lycopene epsilon cyclase, chloroplastic {ECO:0000303|PubMed:8837512}; EC=5.5.1.18 {ECO:0000269|PubMed:11226339, ECO:0000269|PubMed:8837512}; AltName: Full=Protein LUTEIN DEFICIENT 2 {ECO:0000303|PubMed:9789087}; Flags: Precursor;
- **Gene Information:** Name=LUT2 {ECO:0000303|PubMed:9789087}; OrderedLocusNames=At5g57030 {ECO:0000312|Araport:AT5G57030}; ORFNames=MHM17.16 {ECO:0000312|EMBL:BAA97033.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the lycopene cyclase family. .
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); Lycopene_cyclase_b/e. (IPR010108); Lycopene_cycl (PF05834)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LUT2" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LUT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LUT2** (gene ID: LCYE, UniProt: Q38932) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q38932
- **Protein Description:** RecName: Full=Lycopene epsilon cyclase, chloroplastic {ECO:0000303|PubMed:8837512}; EC=5.5.1.18 {ECO:0000269|PubMed:11226339, ECO:0000269|PubMed:8837512}; AltName: Full=Protein LUTEIN DEFICIENT 2 {ECO:0000303|PubMed:9789087}; Flags: Precursor;
- **Gene Information:** Name=LUT2 {ECO:0000303|PubMed:9789087}; OrderedLocusNames=At5g57030 {ECO:0000312|Araport:AT5G57030}; ORFNames=MHM17.16 {ECO:0000312|EMBL:BAA97033.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the lycopene cyclase family. .
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); Lycopene_cyclase_b/e. (IPR010108); Lycopene_cycl (PF05834)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LUT2" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LUT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LUT2** (gene ID: LCYE, UniProt: Q38932) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# LUT2/LCYE (At5g57030; UniProt Q38932) functional-annotation report

## Executive summary

The requested identity is verified: **LUT2 in *Arabidopsis thaliana*** is the nuclear gene **At5g57030**, encoding the chloroplast-targeted **lycopene ε-cyclase** (LCYE, ε-LCY; EC 5.5.1.18; UniProt Q38932). The literature consistently associates Arabidopsis *lut2* with loss of lycopene ε-cyclization and lutein biosynthesis; no conflicting same-symbol protein was encountered. The supplied InterPro/Pfam assignments—FAD/NAD-binding-like fold, lycopene β/ε-cyclase family, and PF05834—are functionally coherent with plant lycopene cyclases, which are flavoproteins related through duplication and divergence. However, these database domain identifiers were not independently stated in the primary papers retrieved. (pogson1998alteredxanthophyllcompositions pages 1-2, gupta2022thegeneticcomponents pages 5-6, ruizsola2012carotenoidbiosynthesisin pages 8-9)

LUT2 catalyzes ε-ring formation at one end of **all-trans-lycopene**, ordinarily producing monocyclic **δ-carotene**. Lycopene β-cyclase (LCYB) then forms a β-ring at the other end, producing **α-carotene**, which is hydroxylated to **zeinoxanthin and lutein**. Thus, LUT2 is the committed branch-point enzyme directing carotenoid flux into the β,ε branch rather than the β,β branch that yields β-carotene and its derivatives. (pogson1998alteredxanthophyllcompositions pages 1-2, nisar2015carotenoidmetabolismin pages 2-3, ruizsola2012carotenoidbiosynthesisin pages 8-9)

## Evidence synopsis

| Topic | Best-supported conclusion | Evidence type/strength | Key quantitative result | Principal source/date/DOI |
|---|---|---|---|---|
| Identity | In *Arabidopsis thaliana*, LUT2 is LCYE/ε-LCY, the lycopene ε-cyclase represented by At5g57030 and UniProt Q38932; no conflicting LUT2 protein was identified in the reviewed literature. | Strong: Arabidopsis genetics and functional-pathway evidence; locus/accession supplied by curated UniProt record. | Loss of function eliminates detectable lutein and increases β-branch carotenoids. | Pogson et al., Oct. 1998, [10.1073/pnas.95.22.13324](https://doi.org/10.1073/pnas.95.22.13324); Gupta & Hirschberg, Jan. 2022, [10.3389/fpls.2021.806184](https://doi.org/10.3389/fpls.2021.806184) (pogson1998alteredxanthophyllcompositions pages 1-2, gupta2022thegeneticcomponents pages 5-6) |
| Catalytic reaction and substrate specificity | LUT2 catalyzes ε-ring formation at one end of all-trans-lycopene, yielding monocyclic δ-carotene; LCYB normally adds a β-ring at the other end to form α-carotene. Unlike LCYB, LCYE normally does not efficiently cyclize both ends. | Strong for plant cyclases and supported by Arabidopsis functional analysis; exact LUT2 kinetic constants were not found. | No reliable Arabidopsis LUT2-specific Km, kcat, or product-ratio measurements recovered. | Nisar et al., Jan. 2015, [10.1016/j.molp.2014.12.007](https://doi.org/10.1016/j.molp.2014.12.007); Ruiz-Sola & Rodríguez-Concepción, Jan. 2012, [10.1199/tab.0158](https://doi.org/10.1199/tab.0158) (nisar2015carotenoidmetabolismin pages 2-3, ruizsola2012carotenoidbiosynthesisin pages 8-9) |
| Pathway role | LUT2 defines entry into the β,ε-carotenoid branch: lycopene → δ-carotene → α-carotene → zeinoxanthin → lutein. It competes/cooperates with LCYB at the principal carotenoid branch point and thereby controls allocation between lutein and β,β-carotenoids. | Strong: biochemical pathway plus Arabidopsis loss-of-function genetics. | In lut2, lutein is absent and is largely replaced by violaxanthin and antheraxanthin. | Pogson et al., Oct. 1998, [10.1073/pnas.95.22.13324](https://doi.org/10.1073/pnas.95.22.13324); Gupta & Hirschberg, Jan. 2022, [10.3389/fpls.2021.806184](https://doi.org/10.3389/fpls.2021.806184) (pogson1998alteredxanthophyllcompositions pages 1-2, gupta2022thegeneticcomponents pages 5-6) |
| Localization | Q38932 is annotated as a chloroplast-targeted precursor, and carotenoid synthesis occurs in plastids; LUT2 therefore most plausibly functions in chloroplasts of green tissue. However, no LUT2-specific microscopy or biochemical fractionation experiment was found in the retrieved sources, so precise subplastid localization should not be treated as directly demonstrated here. | Moderate: curated targeting annotation and pathway compartmentation; direct target-specific localization evidence not recovered. | Not applicable. | Ruiz-Sola & Rodríguez-Concepción, Jan. 2012, [10.1199/tab.0158](https://doi.org/10.1199/tab.0158); Nisar et al., Jan. 2015, [10.1016/j.molp.2014.12.007](https://doi.org/10.1016/j.molp.2014.12.007) (nisar2015carotenoidmetabolismin pages 2-3, ruizsola2012carotenoidbiosynthesisin pages 8-9) |
| Arabidopsis lut2 phenotype | Loss of LUT2 abolishes lutein, redirects flux to β-branch xanthophylls, alters antenna organization and non-photochemical quenching, and can increase susceptibility to excess light. Nevertheless, single mutants remain soil-viable with near-wild-type photosynthetic rates under standard conditions. | Strong for pigment phenotype; moderate for physiological attribution because compensation by other xanthophylls is substantial. | Reported chlorophyll a/b ratios: 2.9–3.5. In a severely xanthophyll-depleted quadruple mutant containing lut2, PSI/PSII fell to about 22% of wild type; this value is not attributable to LUT2 alone. | Pogson et al., Oct. 1998, [10.1073/pnas.95.22.13324](https://doi.org/10.1073/pnas.95.22.13324); Fiore et al., Apr. 2012, [10.1186/1471-2229-12-50](https://doi.org/10.1186/1471-2229-12-50) (fiore2012aquadruplemutant pages 1-3, pogson1998alteredxanthophyllcompositions pages 1-2, fiore2012aquadruplemutant pages 7-9) |
| 2024 Arabidopsis regulation study | A 2024 preprint proposed that the LCYE promoter and structured 5′ untranslated leader mediate transcriptional/post-transcriptional responses to developmental, light, chemical, and carotenoid-derived plastid-feedback signals. | Emerging, target-specific evidence; preprint in 2024 and therefore not peer-reviewed at that date. Fragmented retrieved results precluded reliable effect-size extraction. | Reporter assays tested native and structure-altered 5′UTRs under norflurazon treatment and in a carotenoid-isomerization mutant background; exact robust fold changes were not recoverable. | Alagoz et al., posted July 2024, [10.1101/2024.07.19.604344](https://doi.org/10.1101/2024.07.19.604344) (alagoz2024thelycopeneepsilon pages 61-64, alagoz2024thelycopeneepsilon pages 56-59) |
| 2024 *Chlamydomonas* engineering | **Indirect homolog evidence for Arabidopsis.** CRISPR knockout of algal LCYE eliminated lutein and redirected carotenoid flux toward β-branch xanthophylls; subsequent pathway engineering increased astaxanthin without an observed growth penalty under the tested conditions. | Strong within the engineered algal strain, but not direct evidence about Arabidopsis LUT2. | Lutein: 2.27 mg/L to undetectable; zeaxanthin: 0.31→0.59 mg/L; antheraxanthin: 0.28→0.63 mg/L; violaxanthin: 1.3→2.3 mg/L. Engineered astaxanthin reached 1.8 ± 0.6 mg/L (2.3-fold), with up to 2.44 mg/L at 72 h; only 4/96 screened lines showed donor integration. | Kneip et al., 17 May 2024, [10.3390/plants13101393](https://doi.org/10.3390/plants13101393) (kneip2024crisprcas9mediatedknockoutof pages 4-6, kneip2024crisprcas9mediatedknockoutof pages 6-7, kneip2024crisprcas9mediatedknockoutof pages 1-2) |
| Potato crop engineering | **Indirect crop evidence for Arabidopsis.** Tuber-specific antisense suppression of potato LCYE redirected flux toward provitamin-A β,β-carotenoids, demonstrating LCYE as a practical metabolic-engineering control point; lutein did not decline, indicating species/tissue-specific pathway compensation. | Strong transgenic crop proof of concept, but not an Arabidopsis experiment or commercial deployment. | β-carotene increased by up to 14-fold and total carotenoids by up to 2.5-fold. | Diretto et al., June 2006, [10.1186/1471-2229-6-13](https://doi.org/10.1186/1471-2229-6-13) (ruizsola2012carotenoidbiosynthesisin pages 8-9) |


*Table: Evidence matrix separating direct Arabidopsis LUT2 findings from pathway inference and homolog/crop engineering results. It highlights quantitative outcomes and key limitations, especially the absence of recovered LUT2-specific localization experiments.*

## 1. Identity and nomenclature verification

The target is correctly specified as *A. thaliana* LUT2/LCYE rather than an unrelated LUT2-like symbol from another organism. Arabidopsis genetic literature identifies *lut2* as loss of LCYE function: the mutant lacks lutein and diverts carotenoid flux toward β-branch products. Authoritative pathway reviews likewise place LUT2 at the ε-cyclization step of Arabidopsis carotenoid biosynthesis. (pogson1998alteredxanthophyllcompositions pages 1-2, gupta2022thegeneticcomponents pages 5-6, ruizsola2012carotenoidbiosynthesisin pages 8-9)

The identifiers should be interpreted as follows:

- **Gene symbol:** *LUT2*; biochemical shorthand *LCYE* or *εLCY*.
- **Arabidopsis locus:** At5g57030.
- **Protein:** lycopene ε-cyclase, chloroplastic precursor.
- **UniProt:** Q38932.
- **EC classification:** 5.5.1.18, lycopene ε-cyclase.
- **Phenotype-derived name:** LUTEIN DEFICIENT 2.

The locus and UniProt identifiers come from the supplied curated record; the retrieved primary literature strongly verifies the biological identity but does not always print At5g57030 or Q38932 explicitly.

## 2. Primary biochemical function

### Reaction and substrate specificity

The physiologically relevant reaction is cyclization of one ψ-end of all-trans-lycopene to an ε-ring:

**all-trans-lycopene → δ-carotene**

This is followed in the normal leaf pathway by LCYB-dependent β-ring formation:

**δ-carotene → α-carotene → zeinoxanthin → lutein**

LCYE therefore supplies the ε-ring of α-carotene and lutein. In contrast, LCYB forms β-rings and can cyclize both ends of lycopene to produce β-carotene. Plant LCYE normally acts predominantly at one end, explaining why β,ε-carotenoids are common whereas ε,ε-carotenoids are uncommon. Reviews report residual β-cyclase capacity for LCYE, but its defining physiological specificity is ε-ring formation. (nisar2015carotenoidmetabolismin pages 2-3, ruizsola2012carotenoidbiosynthesisin pages 8-9)

This assignment is supported by convergent evidence: heterologous functional analysis of Arabidopsis cyclases, pathway chemistry, and the *lut2* loss-of-function phenotype. In *lut2*, lutein is eliminated while β-branch carotenoids increase or replace it, which is the expected outcome if ε-cyclization is blocked while LCYB remains active. (pogson1998alteredxanthophyllcompositions pages 1-2, gupta2022thegeneticcomponents pages 5-6)

### Cofactor and mechanism

Plant and bacterial lycopene cyclases are classified as flavoproteins requiring reduced FAD despite catalyzing a reaction with no net oxidation or reduction. The FAD/NAD-binding-like annotation of Q38932 is therefore mechanistically plausible. Current models invoke flavin-assisted protonation/carbocation chemistry and ring closure rather than net redox conversion. Nevertheless, the retrieved literature did not provide Arabidopsis LUT2-specific **Km**, **kcat**, cofactor stoichiometry, a solved experimental structure, or residue-level catalytic validation. Accordingly, detailed catalytic chemistry remains family-based inference rather than a complete biochemical description of purified Q38932. (ruizsola2012carotenoidbiosynthesisin pages 8-9)

## 3. Pathway and biological process

LUT2 operates at the principal branch point of plastid carotenoid biosynthesis. Upstream reactions generate all-trans-lycopene; competition and cooperation between LCYE and LCYB then determine allocation between:

1. the **β,ε branch**, producing α-carotene and lutein; and
2. the **β,β branch**, producing β-carotene, zeaxanthin, antheraxanthin, violaxanthin, and neoxanthin.

Lutein is a major green-leaf xanthophyll bound by photosynthetic antenna complexes. It contributes to light harvesting, stabilization and organization of light-harvesting complexes, chlorophyll-triplet quenching, and non-photochemical dissipation of excess excitation. LUT2 therefore affects photosynthesis primarily by controlling pigment composition, not by serving as a photosystem structural subunit or signaling receptor. (fiore2012aquadruplemutant pages 1-3, pogson1998alteredxanthophyllcompositions pages 1-2, nisar2015carotenoidmetabolismin pages 2-3)

LUT2 is not itself an ABA-biosynthetic enzyme. Its activity affects branch allocation upstream of β,β-xanthophylls, some of which are precursors to ABA and other apocarotenoids. Broad developmental or stress phenotypes should therefore be interpreted as downstream consequences of altered carotenoid pools rather than evidence that LUT2 directly synthesizes a hormone.

## 4. Cellular localization

Q38932 is annotated as a **chloroplastic precursor**, implying synthesis in the cytosol followed by import into plastids through an N-terminal transit peptide. This agrees with the established plastid localization of plant carotenoid biosynthesis and with LUT2’s use of the highly hydrophobic plastid metabolite lycopene. (nisar2015carotenoidmetabolismin pages 2-3, ruizsola2012carotenoidbiosynthesisin pages 8-9)

The defensible annotation is therefore **plastid/chloroplast localized**, especially in green tissue. However, the retrieved sources did not provide a LUT2-specific GFP experiment, immunoblot of chloroplast fractions, or high-resolution subplastid localization assay. The precise location within the chloroplast—envelope, thylakoid-associated region, plastoglobule, or another membrane-associated compartment—should consequently be regarded as unresolved here. “Chloroplastic” is strongly supported by targeting annotation and pathway compartmentation, but exact suborganellar placement is not directly verified by the evidence retrieved.

## 5. Genetic and physiological evidence

### Single-mutant evidence

The strongest direct functional evidence is the Arabidopsis *lut2* pigment phenotype. Lutein is absent and is replaced substantially by violaxanthin and antheraxanthin, demonstrating rerouting from the β,ε branch to β,β products. Mutants remain viable in soil, have reported chlorophyll a/b ratios of approximately **2.9–3.5**, and can maintain near-wild-type photosynthetic rates under standard conditions, showing considerable functional compensation by alternative xanthophylls. (pogson1998alteredxanthophyllcompositions pages 1-2)

Nevertheless, loss of lutein affects photosynthetic organization and regulation. Reported consequences include reduced antenna size, altered or monomerized LHCII, decreased non-photochemical quenching, impaired chlorophyll-triplet quenching, zeaxanthin overaccumulation under high light, and increased susceptibility to photodamage in some conditions. These findings support a specific role for LUT2-derived lutein in antenna organization and photoprotection rather than an absolute requirement for basal photosynthetic electron transport. (fiore2012aquadruplemutant pages 1-3)

The response is environmentally conditional. A 2022 study found that under six days of combined low temperature and high light, *lut2* showed lower electrolyte leakage, lower excitation pressure, and higher actual PSII photochemical efficiency than wild type, despite reduced qE-related measures. The authors proposed enhanced cyclic electron flow and PSI-dependent energy dissipation as compensatory protection. Thus, “lutein deficiency always increases stress sensitivity” is too broad; the phenotype depends on light, temperature, developmental state, and compensatory energy-dissipation routes.

### Higher-order mutants

In a *chy1 chy2 lut2 lut5* quadruple background, severe xanthophyll depletion caused complete loss of qE, reduced Lhcb accumulation, deficient PSI–LHCI supercomplexes, and a PSI/PSII ratio of about **22% of wild type**. Across 12 xanthophyll mutants, xanthophyll/carotenoid ratio correlated with LHCII/PSII and PSI/PSII, with **R² = 0.76 and 0.78**, respectively. These data reinforce the importance of xanthophyll composition for photosystem stoichiometry. They must not, however, be assigned specifically to LUT2 because three additional hydroxylase loci were disrupted. (fiore2012aquadruplemutant pages 7-9)

## 6. Regulation and recent research

Direct 2023–2024 mechanistic work specifically on the Arabidopsis LUT2 protein was limited in the retrieved literature. The most relevant target-specific development was a **July 2024 bioRxiv preprint** examining Arabidopsis LCYE expression. Reporter constructs, altered 5′-UTR structures, norflurazon treatment, developmental/light transitions, and a carotenoid-isomerization mutant background supported a model in which the LCYE promoter and structured untranslated leader mediate transcriptional and post-transcriptional responses to plastid carotenoid status. Because the 2024 source was a preprint and the retrieved figures did not permit robust extraction of effect sizes, this regulatory model should be considered emerging rather than settled evidence. URL: https://doi.org/10.1101/2024.07.19.604344; posted July 2024. (alagoz2024thelycopeneepsilon pages 61-64, alagoz2024thelycopeneepsilon pages 56-59)

The broader interpretation is that LUT2 is not merely a constitutive catalytic step: its expression may participate in plastid-to-nucleus feedback that stabilizes cyclic-carotenoid composition during chloroplast development and environmental change. A later peer-reviewed 2025 version further developed this promoter/5′UTR model, but it falls beyond the requested 2023–2024 priority window. (alagoz2025plastidmediatedfeedbackregulation pages 23-23)

## 7. Applications and real-world implementation

LCYE is an attractive engineering target because reducing ε-branch flux can increase β-carotene or other β,β-derived carotenoids. This is important for provitamin-A biofortification and production of high-value ketocarotenoids. These applications are based on LCYE homologs and should not be mistaken for direct engineering of Arabidopsis LUT2.

In potato, tuber-specific antisense suppression of LCYE increased β-carotene by as much as **14-fold** and total carotenoids by up to **2.5-fold**. Lutein did not decline, demonstrating that the consequences of LCYE suppression depend on species, tissue, competing enzymes, and pathway feedback. This was a transgenic proof of concept rather than evidence of broad commercial deployment. Publication: June 2006; URL: https://doi.org/10.1186/1471-2229-6-13.

A recent quantitative implementation used CRISPR/Cas9 to disrupt LCYE in *Chlamydomonas reinhardtii*. Lutein fell from **2.27 mg/L to undetectable**, while zeaxanthin increased from **0.31 to 0.59 mg/L**, antheraxanthin from **0.28 to 0.63 mg/L**, and violaxanthin from **1.3 to 2.3 mg/L**. Subsequent overexpression of ketolase, phytoene synthase, and β-carotene hydroxylase produced **1.8 ± 0.6 mg/L astaxanthin**, a **2.3-fold** increase, with a maximum of 2.44 mg/L at 72 hours. Growth was not detectably impaired under the tested conditions. Only **4 of 96** screened candidates showed donor integration, and NHEJ generated partial or rearranged integrations, illustrating practical editing limitations. Publication: 17 May 2024; URL: https://doi.org/10.3390/plants13101393. (kneip2024crisprcas9mediatedknockoutof pages 4-6, kneip2024crisprcas9mediatedknockoutof pages 6-7, kneip2024crisprcas9mediatedknockoutof pages 1-2)

These examples establish LCYE as a genuine metabolic-flux control point, but expert interpretation requires caution: complete suppression can compromise lutein-dependent antenna functions; effects vary sharply by tissue and species; and increasing β-branch substrate does not by itself guarantee accumulation of a desired endpoint without coordinated downstream engineering.

## 8. Confidence assessment and annotation gaps

**High-confidence annotation:** LUT2/At5g57030/Q38932 is Arabidopsis lycopene ε-cyclase; it acts on all-trans-lycopene at the β,ε branch point and is required for normal α-carotene/lutein synthesis. The loss-of-function pigment phenotype provides direct genetic confirmation. (pogson1998alteredxanthophyllcompositions pages 1-2, gupta2022thegeneticcomponents pages 5-6)

**Moderate-to-high confidence:** the protein functions in chloroplasts/plastids and uses reduced FAD in a lycopene-cyclase-family mechanism. This is supported by the precursor annotation, pathway compartmentation, family/domain architecture, and cyclase biochemistry, but a target-specific localization experiment and purified-Q38932 cofactor analysis were not recovered. (nisar2015carotenoidmetabolismin pages 2-3, ruizsola2012carotenoidbiosynthesisin pages 8-9)

**Outstanding questions:** precise subplastid localization; experimentally determined LUT2 kinetic constants and product ratios; an experimental three-dimensional structure; residue-level catalytic tests; composition of any native enzyme complex; and the quantitative importance of promoter/5′UTR feedback under field conditions.

## Key references

- Pogson BJ et al. “Altered xanthophyll compositions adversely affect chlorophyll accumulation and nonphotochemical quenching in Arabidopsis mutants.” *PNAS*, October 1998. https://doi.org/10.1073/pnas.95.22.13324. (pogson1998alteredxanthophyllcompositions pages 1-2)
- Ruiz-Sola MÁ, Rodríguez-Concepción M. “Carotenoid Biosynthesis in Arabidopsis: A Colorful Pathway.” *The Arabidopsis Book*, January 2012. https://doi.org/10.1199/tab.0158. (ruizsola2012carotenoidbiosynthesisin pages 8-9)
- Fiore A et al. “A quadruple mutant of Arabidopsis reveals a β-carotene hydroxylation activity for LUT1/CYP97C1 and a regulatory role of xanthophylls on determination of the PSI/PSII ratio.” *BMC Plant Biology*, April 2012. https://doi.org/10.1186/1471-2229-12-50. (fiore2012aquadruplemutant pages 1-3, fiore2012aquadruplemutant pages 7-9)
- Nisar N et al. “Carotenoid metabolism in plants.” *Molecular Plant*, January 2015. https://doi.org/10.1016/j.molp.2014.12.007. (nisar2015carotenoidmetabolismin pages 2-3)
- Gupta P, Hirschberg J. “The Genetic Components of a Natural Color Palette.” *Frontiers in Plant Science*, January 2022. https://doi.org/10.3389/fpls.2021.806184. (gupta2022thegeneticcomponents pages 5-6)
- Alagoz Y et al. “The LYCOPENE EPSILON CYCLASE untranslated mRNA leader modulates carotenoid feedback and post-transcriptional regulation.” bioRxiv, July 2024. https://doi.org/10.1101/2024.07.19.604344. (alagoz2024thelycopeneepsilon pages 61-64, alagoz2024thelycopeneepsilon pages 56-59)
- Kneip JS et al. “CRISPR/Cas9-Mediated Knockout of the Lycopene ε-Cyclase for Efficient Astaxanthin Production in the Green Microalga Chlamydomonas reinhardtii.” *Plants*, 17 May 2024. https://doi.org/10.3390/plants13101393. (kneip2024crisprcas9mediatedknockoutof pages 4-6, kneip2024crisprcas9mediatedknockoutof pages 6-7, kneip2024crisprcas9mediatedknockoutof pages 1-2)

References

1. (pogson1998alteredxanthophyllcompositions pages 1-2): Barry J. Pogson, Krishna K. Niyogi, Olle Björkman, and Dean DellaPenna. Altered xanthophyll compositions adversely affect chlorophyll accumulation and nonphotochemical quenching in arabidopsis mutants. Proceedings of the National Academy of Sciences of the United States of America, 95 22:13324-9, Oct 1998. URL: https://doi.org/10.1073/pnas.95.22.13324, doi:10.1073/pnas.95.22.13324. This article has 412 citations and is from a highest quality peer-reviewed journal.

2. (gupta2022thegeneticcomponents pages 5-6): Prateek Gupta and Joseph Hirschberg. The genetic components of a natural color palette: a comprehensive list of carotenoid pathway mutations in plants. Frontiers in Plant Science, Jan 2022. URL: https://doi.org/10.3389/fpls.2021.806184, doi:10.3389/fpls.2021.806184. This article has 25 citations.

3. (ruizsola2012carotenoidbiosynthesisin pages 8-9): M. Águila Ruiz-Sola and Manuel Rodríguez-Concepción. Carotenoid biosynthesis in arabidopsis: a colorful pathway. The Arabidopsis Book, 2012:e0158, Jan 2012. URL: https://doi.org/10.1199/tab.0158, doi:10.1199/tab.0158. This article has 742 citations and is from a peer-reviewed journal.

4. (nisar2015carotenoidmetabolismin pages 2-3): Nazia Nisar, Li Li, Shan Lu, Nay Chi Khin, and Barry J. Pogson. Carotenoid metabolism in plants. Molecular plant, 8 1:68-82, Jan 2015. URL: https://doi.org/10.1016/j.molp.2014.12.007, doi:10.1016/j.molp.2014.12.007. This article has 1544 citations and is from a highest quality peer-reviewed journal.

5. (fiore2012aquadruplemutant pages 1-3): Alessia Fiore, Luca Dall'Osto, Stefano Cazzaniga, Gianfranco Diretto, Giovanni Giuliano, and Roberto Bassi. A quadruple mutant of arabidopsis reveals a β-carotene hydroxylation activity for lut1/cyp97c1 and a regulatory role of xanthophylls on determination of the psi/psii ratio. BMC Plant Biology, 12:50-50, Apr 2012. URL: https://doi.org/10.1186/1471-2229-12-50, doi:10.1186/1471-2229-12-50. This article has 54 citations and is from a peer-reviewed journal.

6. (fiore2012aquadruplemutant pages 7-9): Alessia Fiore, Luca Dall'Osto, Stefano Cazzaniga, Gianfranco Diretto, Giovanni Giuliano, and Roberto Bassi. A quadruple mutant of arabidopsis reveals a β-carotene hydroxylation activity for lut1/cyp97c1 and a regulatory role of xanthophylls on determination of the psi/psii ratio. BMC Plant Biology, 12:50-50, Apr 2012. URL: https://doi.org/10.1186/1471-2229-12-50, doi:10.1186/1471-2229-12-50. This article has 54 citations and is from a peer-reviewed journal.

7. (alagoz2024thelycopeneepsilon pages 61-64): Yagiz Alagoz, Jwalit J. Nayak, Rishi Aryal, Jacinta L. Watkins, Sophie Holland, David T. Tissue, Barry J. Pogson, and Christopher I. Cazzonelli. The lycopene epsilon cyclase untranslated mrna leader modulates carotenoid feedback and post-transcriptional regulation. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.19.604344, doi:10.1101/2024.07.19.604344. This article has 1 citations.

8. (alagoz2024thelycopeneepsilon pages 56-59): Yagiz Alagoz, Jwalit J. Nayak, Rishi Aryal, Jacinta L. Watkins, Sophie Holland, David T. Tissue, Barry J. Pogson, and Christopher I. Cazzonelli. The lycopene epsilon cyclase untranslated mrna leader modulates carotenoid feedback and post-transcriptional regulation. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.19.604344, doi:10.1101/2024.07.19.604344. This article has 1 citations.

9. (kneip2024crisprcas9mediatedknockoutof pages 4-6): Jacob Sebastian Kneip, Niklas Kniepkamp, Junhwan Jang, Maria Grazia Mortaro, EonSeon Jin, Olaf Kruse, and Thomas Baier. Crispr/cas9-mediated knockout of the lycopene ε-cyclase for efficient astaxanthin production in the green microalga chlamydomonas reinhardtii. Plants, 13:1393, May 2024. URL: https://doi.org/10.3390/plants13101393, doi:10.3390/plants13101393. This article has 45 citations.

10. (kneip2024crisprcas9mediatedknockoutof pages 6-7): Jacob Sebastian Kneip, Niklas Kniepkamp, Junhwan Jang, Maria Grazia Mortaro, EonSeon Jin, Olaf Kruse, and Thomas Baier. Crispr/cas9-mediated knockout of the lycopene ε-cyclase for efficient astaxanthin production in the green microalga chlamydomonas reinhardtii. Plants, 13:1393, May 2024. URL: https://doi.org/10.3390/plants13101393, doi:10.3390/plants13101393. This article has 45 citations.

11. (kneip2024crisprcas9mediatedknockoutof pages 1-2): Jacob Sebastian Kneip, Niklas Kniepkamp, Junhwan Jang, Maria Grazia Mortaro, EonSeon Jin, Olaf Kruse, and Thomas Baier. Crispr/cas9-mediated knockout of the lycopene ε-cyclase for efficient astaxanthin production in the green microalga chlamydomonas reinhardtii. Plants, 13:1393, May 2024. URL: https://doi.org/10.3390/plants13101393, doi:10.3390/plants13101393. This article has 45 citations.

12. (alagoz2025plastidmediatedfeedbackregulation pages 23-23): Yagiz Alagoz, Jwalit J. Nayak, Rishi Aryal, Jacinta L. Watkins, Sophie Holland, David T. Tissue, Barry J. Pogson, and Christopher I. Cazzonelli. Plastid-mediated feedback regulation of arabidopsis lycopene epsilon cyclase is modulated by the promoter and a 5′utr structural variant harbouring a conserved ires. BMC Biology, Nov 2025. URL: https://doi.org/10.1186/s12915-025-02436-z, doi:10.1186/s12915-025-02436-z. This article has 1 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](LCYE-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. ruizsola2012carotenoidbiosynthesisin pages 8-9
2. pogson1998alteredxanthophyllcompositions pages 1-2
3. fiore2012aquadruplemutant pages 1-3
4. fiore2012aquadruplemutant pages 7-9
5. alagoz2025plastidmediatedfeedbackregulation pages 23-23
6. nisar2015carotenoidmetabolismin pages 2-3
7. gupta2022thegeneticcomponents pages 5-6
8. alagoz2024thelycopeneepsilon pages 61-64
9. alagoz2024thelycopeneepsilon pages 56-59
10. 10.1073/pnas.95.22.13324
11. 10.3389/fpls.2021.806184
12. 10.1016/j.molp.2014.12.007
13. 10.1199/tab.0158
14. 10.1186/1471-2229-12-50
15. 10.1101/2024.07.19.604344
16. 10.3390/plants13101393
17. 10.1186/1471-2229-6-13
18. https://doi.org/10.1073/pnas.95.22.13324
19. https://doi.org/10.3389/fpls.2021.806184
20. https://doi.org/10.1016/j.molp.2014.12.007
21. https://doi.org/10.1199/tab.0158
22. https://doi.org/10.1186/1471-2229-12-50
23. https://doi.org/10.1101/2024.07.19.604344
24. https://doi.org/10.3390/plants13101393
25. https://doi.org/10.1186/1471-2229-6-13
26. https://doi.org/10.1101/2024.07.19.604344;
27. https://doi.org/10.1186/1471-2229-6-13.
28. https://doi.org/10.3390/plants13101393.
29. https://doi.org/10.1073/pnas.95.22.13324.
30. https://doi.org/10.1199/tab.0158.
31. https://doi.org/10.1186/1471-2229-12-50.
32. https://doi.org/10.1016/j.molp.2014.12.007.
33. https://doi.org/10.3389/fpls.2021.806184.
34. https://doi.org/10.1101/2024.07.19.604344.
35. https://doi.org/10.1073/pnas.95.22.13324,
36. https://doi.org/10.3389/fpls.2021.806184,
37. https://doi.org/10.1199/tab.0158,
38. https://doi.org/10.1016/j.molp.2014.12.007,
39. https://doi.org/10.1186/1471-2229-12-50,
40. https://doi.org/10.1101/2024.07.19.604344,
41. https://doi.org/10.3390/plants13101393,
42. https://doi.org/10.1186/s12915-025-02436-z,