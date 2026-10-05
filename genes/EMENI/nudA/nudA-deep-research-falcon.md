---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T18:24:16.967841'
end_time: '2026-09-27T18:31:10.159478'
duration_seconds: 413.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EMENI
  gene_id: nudA
  gene_symbol: nudA
  uniprot_accession: P45444
  protein_description: 'RecName: Full=Dynein heavy chain, cytoplasmic; AltName: Full=Dynein
    heavy chain, cytosolic; Short=DYHC;'
  gene_info: Name=nudA; ORFNames=AN0118;
  organism_full: Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL
    194 / M139) (Aspergillus nidulans).
  protein_family: Belongs to the dynein heavy chain family. .
  protein_domains: AAA+_ATPase. (IPR003593); AAA_9. (IPR035706); AAA_lid_11. (IPR041658);
    AAA_lid_11_sf. (IPR042219); DHC. (IPR026983)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 53
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: nudA-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P45444
- **Protein Description:** RecName: Full=Dynein heavy chain, cytoplasmic; AltName: Full=Dynein heavy chain, cytosolic; Short=DYHC;
- **Gene Information:** Name=nudA; ORFNames=AN0118;
- **Organism (full):** Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL 194 / M139) (Aspergillus nidulans).
- **Protein Family:** Belongs to the dynein heavy chain family. .
- **Key Domains:** AAA+_ATPase. (IPR003593); AAA_9. (IPR035706); AAA_lid_11. (IPR041658); AAA_lid_11_sf. (IPR042219); DHC. (IPR026983)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nudA" matches the protein description above**
2. **Verify the organism is correct:** Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL 194 / M139) (Aspergillus nidulans).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nudA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nudA** (gene ID: nudA, UniProt: P45444) in EMENI.

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
- **UniProt Accession:** P45444
- **Protein Description:** RecName: Full=Dynein heavy chain, cytoplasmic; AltName: Full=Dynein heavy chain, cytosolic; Short=DYHC;
- **Gene Information:** Name=nudA; ORFNames=AN0118;
- **Organism (full):** Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL 194 / M139) (Aspergillus nidulans).
- **Protein Family:** Belongs to the dynein heavy chain family. .
- **Key Domains:** AAA+_ATPase. (IPR003593); AAA_9. (IPR035706); AAA_lid_11. (IPR041658); AAA_lid_11_sf. (IPR042219); DHC. (IPR026983)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nudA" matches the protein description above**
2. **Verify the organism is correct:** Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL 194 / M139) (Aspergillus nidulans).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nudA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nudA** (gene ID: nudA, UniProt: P45444) in EMENI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Aspergillus nidulans nudA* (UniProt P45444)

## Executive conclusion

The identity check is affirmative. In *Aspergillus nidulans*—the organism also historically named *Emericella nidulans*—**nudA** encodes **NUDA, the cytoplasmic dynein heavy chain**. Organism-specific studies consistently use “nudA,” “NUDA,” and “GFP–NUDA” for this heavy-chain motor. Mutations have been mapped to its N-terminal stem and AAA motor region, and endogenous tagged protein has been visualized in living *A. nidulans* hyphae. This agrees with the supplied UniProt accession P45444, ORF AN0118, dynein-heavy-chain family assignment, and AAA+/DHC domain annotations. The similarly named **nudE, nudF, nudG, and nudC genes encode different proteins** and were not treated as the target gene. (efimov2003rolesofnude pages 1-2, zhuang2007pointmutationsin pages 3-4, zhuang2007pointmutationsin pages 1-2, beckwith1998the“8kd”cytoplasmic pages 3-4)

The best-supported primary annotation is:

> **NudA is the catalytic heavy chain of cytoplasmic dynein, an ATP-dependent, microtubule-minus-end-directed motor complex. In multinucleate fungal hyphae it generates or transmits forces required for nuclear migration/distribution and drives retrograde, basipetal transport of early endosomes. Its activity and spatial targeting are controlled by dynactin, the HookA cargo adapter, NudF/LIS1, NudE, and the dynein intermediate, light-intermediate, and light chains.**

It is not best described as a conventional soluble enzyme with a small-molecule substrate. Its biochemical substrates are **ATP and polymerized microtubules**: ATP binding and hydrolysis in the heavy-chain AAA ring are coupled to cyclic changes in microtubule affinity and mechanical stepping toward microtubule minus ends. Cargo specificity is not intrinsic to the catalytic site; it is imposed by dynactin and cargo adapters such as HookA. (zhuang2007pointmutationsin pages 1-2, xiang2020cargomediatedactivationof pages 3-4, qiu2021dyneinactivationin pages 1-4)

## Evidence summary

| Annotation aspect | Conclusion | Evidence type | Directness | Key source/date/DOI URL |
|---|---|---|---|---|
| Identity | In *Aspergillus nidulans*, **nudA** encodes NUDA, the cytoplasmic dynein heavy chain; this matches the supplied P45444/AN0118 identity and dynein-family annotation. NudE, NudF and NudC are distinct proteins and must not be conflated with NudA. | Locus mapping, sequencing, endogenous GFP fusion and organism-specific nomenclature | **Direct target evidence** | Zhuang et al., March 2007, [doi:10.1534/genetics.106.069013](https://doi.org/10.1534/genetics.106.069013) (zhuang2007pointmutationsin pages 3-4, zhuang2007pointmutationsin pages 1-2) |
| Molecular motor and ATPase architecture | NUDA has the characteristic dynein heavy-chain organization: an N-terminal stem/tail and a motor region containing six AAA modules plus the microtubule-binding stalk. The heavy chain supplies ATPase and microtubule-binding motor functions; AAA1 is the principal hydrolysis site, while other AAA sites regulate activity. | Domain-specific mutagenesis, dynein purification and ATPase assay, interpreted with conserved dynein architecture | **Direct for NUDA architecture and ATPase activity; partly family-level for individual AAA-site assignments** | Zhuang et al., March 2007, [doi:10.1534/genetics.106.069013](https://doi.org/10.1534/genetics.106.069013) (zhuang2007pointmutationsin pages 1-2, zhuang2007pointmutationsin pages 7-9); Qiu et al., 2021, [doi:10.1016/j.cub.2021.08.030](https://doi.org/10.1016/j.cub.2021.08.030) (qiu2021dyneinactivationin pages 1-4) |
| ATPase regulation | The nudA-R3086C change near AAA4 lowered basal dynein ATPase activity to approximately **50% of wild type** and redistributed NUDA along microtubules. Later AAA3 nucleotide-state mutations altered activation, cargo coupling and the requirement for NudF/LIS1. | Biochemical ATPase assay, live-cell imaging and targeted nucleotide-site mutations | **Direct target evidence** | Zhuang et al., March 2007, [doi:10.1534/genetics.106.069013](https://doi.org/10.1534/genetics.106.069013) (zhuang2007pointmutationsin pages 7-9); Qiu et al., October 2021, [doi:10.1016/j.cub.2021.08.030](https://doi.org/10.1016/j.cub.2021.08.030) (qiu2021dyneinactivationin pages 6-7, qiu2021dyneinactivationin pages 9-12) |
| Dynein complex membership | NUDA sediments in an approximately **20-S** complex and co-immunoprecipitates with the NUDG/LC8 light chain. This establishes membership in the multisubunit cytoplasmic dynein complex, although it does not prove direct heavy-chain–light-chain contact. | Sucrose-gradient sedimentation and reciprocal co-immunoprecipitation | **Direct target evidence** | Beckwith et al., November 1998, [doi:10.1083/jcb.143.5.1239](https://doi.org/10.1083/jcb.143.5.1239) (beckwith1998the“8kd”cytoplasmic pages 4-6) |
| Subcellular localization | GFP-NUDA forms motile comet-like accumulations at dynamic microtubule plus ends near hyphal tips. Activated or nucleotide-state-mutant dynein can accumulate at septal microtubule minus ends, decorate microtubules and occasionally appear at spindle-pole bodies. | Live-cell GFP imaging, microtubule colocalization and mutant analysis | **Direct target evidence** | Zhang et al., April 2002, [doi:10.1046/j.1365-2958.2002.02900.x](https://doi.org/10.1046/j.1365-2958.2002.02900.x) (zhang2002cytoplasmicdyneinintermediate pages 7-8); Qiu et al., October 2021, [doi:10.1016/j.cub.2021.08.030](https://doi.org/10.1016/j.cub.2021.08.030) (qiu2021dyneinactivationin pages 6-7) |
| Nuclear migration and distribution | NudA-dependent dynein moves or positions nuclei along multinucleate hyphae. Loss of dynein leaves dividing nuclei clustered near the spore end instead of distributing them into the germ tube; dynein-pathway nulls remain viable but form compact colonies and fail to conidiate efficiently. | Deletion/conditional genetics, microscopy and epistasis with the NUDG light chain | **Direct target/pathway evidence** | Beckwith et al., November 1998, [doi:10.1083/jcb.143.5.1239](https://doi.org/10.1083/jcb.143.5.1239) (beckwith1998the“8kd”cytoplasmic pages 3-4); Efimov, March 2003, [doi:10.1091/mbc.e02-06-0359](https://doi.org/10.1091/mbc.e02-06-0359) (efimov2003rolesofnude pages 1-2) |
| Early-endosome and HookA pathway | Early endosomes are a major fungal dynein cargo. HookA acts as the cargo adapter: an activating HookA fragment relocates dynein/dynactin from plus-end comets toward septal minus ends, whereas the nudA-F208V tail mutation blocks this relocation. The evidence establishes adapter-mediated activation, although the cited passages do not provide transport velocity or run-length values. | Live-cell cargo/motor imaging, adapter overexpression and nudA tail-mutant analysis | **Direct *A. nidulans* dynein/NudA evidence** | Qiu et al., September 2019, [doi:10.1083/jcb.201905178](https://doi.org/10.1083/jcb.201905178) (qiu2019lis1regulatescargoadapter–mediated pages 2-3); Xiang and Qiu, October 2020, [doi:10.3389/fcell.2020.598952](https://doi.org/10.3389/fcell.2020.598952) (xiang2020cargomediatedactivationof pages 3-4) |
| Dynactin regulation | Dynactin is required for normal NUDA plus-end accumulation and activated minus-end targeting. Conditional loss of Arp1 makes one AAA3 mutant diffuse and abolishes septal accumulation of another despite increased microtubule decoration, demonstrating that microtubule binding alone is insufficient for productive targeting. | Dynactin-subunit deletion or conditional depletion, live-cell localization and genetic comparison | **Direct target/pathway evidence** | Zhang et al., July 2008, [doi:10.1111/j.1600-0854.2008.00748.x](https://doi.org/10.1111/j.1600-0854.2008.00748.x) (zhang2008arp11affectsdynein–dynactin pages 2-3); Qiu et al., October 2021, [doi:10.1016/j.cub.2021.08.030](https://doi.org/10.1016/j.cub.2021.08.030) (qiu2021dyneinactivationin pages 9-12) |
| NudF/LIS1 regulation | NudF, the *A. nidulans* LIS1 homolog, interacts with the heavy-chain motor region and promotes HookA-mediated activation. nudA stem/AAA4 or AAA3 mutations can partially bypass NudF loss, showing that the heavy-chain nucleotide/conformational state controls LIS1 dependence. | Protein-interaction assays, suppressor genetics, ATPase analysis and live-cell activation assays | **Direct target evidence** | Efimov, March 2003, [doi:10.1091/mbc.e02-06-0359](https://doi.org/10.1091/mbc.e02-06-0359) (efimov2003rolesofnude pages 1-2); Zhuang et al., March 2007, [doi:10.1534/genetics.106.069013](https://doi.org/10.1534/genetics.106.069013) (zhuang2007pointmutationsin pages 1-2); Qiu et al., October 2021, [doi:10.1016/j.cub.2021.08.030](https://doi.org/10.1016/j.cub.2021.08.030) (qiu2021dyneinactivationin pages 9-12) |
| NudE and other dynein subunits | NudE regulates NUDA comet behavior but is not required to create plus-end comets. Heavy- and intermediate-chain localization are mutually dependent, while loss of the NUDG light chain removes NUDA from the hyphal tip, indicating that assembly/regulatory subunits control motor localization and function. | Gene deletion, tagged-protein imaging, co-immunoprecipitation and epistasis | **Direct target/pathway evidence** | Beckwith et al., November 1998, [doi:10.1083/jcb.143.5.1239](https://doi.org/10.1083/jcb.143.5.1239) (beckwith1998the“8kd”cytoplasmic pages 3-4, beckwith1998the“8kd”cytoplasmic pages 4-6); Zhang et al., April 2002, [doi:10.1046/j.1365-2958.2002.02900.x](https://doi.org/10.1046/j.1365-2958.2002.02900.x) (zhang2002cytoplasmicdyneinintermediate pages 7-8); Efimov, March 2003, [doi:10.1091/mbc.e02-06-0359](https://doi.org/10.1091/mbc.e02-06-0359) (efimov2003rolesofnude pages 1-2) |
| 2023–2024 mechanistic context | Current work supports a conserved model in which heavy-chain homodimers are catalytic, whereas intermediate/light chains organize and regulate the complex; dynactin and cargo adapters activate processive motility, and Nde1/Ndel1 helps coordinate LIS1 delivery and activated-complex assembly. These studies did **not** directly test P45444 and therefore refine interpretation rather than annotate new NudA-specific functions. | Modern biochemical, structural and single-molecule studies plus authoritative review | **Family-level inference; not direct P45444 evidence** | Okada et al., September 2023, [doi:10.1038/s41467-023-41466-5](https://doi.org/10.1038/s41467-023-41466-5) (okada2023conservedrolesfor pages 1-2); Rao and Gennerich, February 2024, [doi:10.3390/cells13040330](https://doi.org/10.3390/cells13040330) (rao2024structureandfunction pages 2-4, rao2024structureandfunction pages 21-22) |


*Table: Evidence supporting the functional annotation of *A. nidulans* nudA/P45444, with direct organism-specific findings separated from conserved dynein-family inference. The table also highlights quantitative observations and target-specific evidence gaps.*

## 1. Molecular function and architecture

NudA is both the catalytic and force-producing subunit of the cytoplasmic dynein complex. Its N-terminal stem/tail mediates heavy-chain dimerization and association with accessory subunits and regulators. The C-terminal motor contains a ring of six AAA modules and a protruding microtubule-binding stalk located between AAA4 and AAA5. This organization agrees closely with the supplied InterPro assignments—AAA+ ATPase, AAA_9, AAA-lid, and DHC—and strongly excludes an unrelated Nud-family protein. (zhuang2007pointmutationsin pages 3-4, zhuang2007pointmutationsin pages 1-2)

The principal chemical reaction can be represented as:

**ATP + H₂O → ADP + Pi**, coupled to conformational changes, microtubule-binding cycles, and minus-end-directed mechanical work.

AAA1 is considered the principal ATP-hydrolysis site; AAA3 and AAA4 exert important regulatory effects on motor activation and microtubule release. The assignment of individual AAA sites partly draws on conserved dynein-family biochemistry, but *A. nidulans* mutagenesis directly demonstrates that the nucleotide state of NudA’s AAA3/AAA4 region controls localization, activation, cargo coupling, and dependence on NudF/LIS1. (zhuang2007pointmutationsin pages 1-2, qiu2021dyneinactivationin pages 6-7, qiu2021dyneinactivationin pages 9-12, qiu2021dyneinactivationin pages 1-4)

A particularly informative mutation, **nudA-R3086C**, lies at the end of AAA4 near the microtubule-binding stalk. Purified mutant dynein exhibited approximately **50% of wild-type basal ATPase activity** and redistributed from predominantly plus-end comets onto microtubule-like filaments. Thus, its partial suppression of NudF/LIS1 loss does not result from increased ATP turnover; rather, the mutation changes the motor’s mechanochemical or conformational regulation. The stem mutation L1098F did not significantly reduce basal ATPase activity. (zhuang2007pointmutationsin pages 1-2, zhuang2007pointmutationsin pages 7-9)

NUDA sediments in an approximately **20-S complex** in fungal extracts. Reciprocal co-immunoprecipitation with the NUDG/LC8 light chain confirms incorporation into the multisubunit cytoplasmic dynein complex, although those experiments do not prove a direct heavy-chain–LC8 contact because other subunits could bridge the association. (beckwith1998the“8kd”cytoplasmic pages 4-6)

## 2. Cellular localization

In living hyphae, GFP-tagged NUDA forms motile, comet-like accumulations at dynamic **microtubule plus ends**, especially near growing hyphal tips. Heavy-chain and intermediate-chain localization are mutually dependent, indicating that assembled dynein rather than an isolated heavy chain is normally targeted to these ends. Loss of the NUDG light chain likewise removes NUDA from the mycelial tip. (zhang2002cytoplasmicdyneinintermediate pages 7-8, beckwith1998the“8kd”cytoplasmic pages 3-4, efimov2003rolesofnude pages 1-2)

This plus-end pool is best understood as a staging or cargo-encounter site, not as the destination of dynein-driven motility. Following activation, dynein moves toward microtubule minus ends and can accumulate at **septa**, which function as minus-end-associated sites in the hypha. Activated or nucleotide-state-mutant dynein can also decorate microtubules and occasionally localize to interphase spindle-pole bodies or the nuclear envelope. Cell-cycle-dependent spindle-pole localization is therefore a secondary, regulated localization rather than NudA’s only site of action. (qiu2021dyneinactivationin pages 6-7, qiu2019lis1regulatescargoadapter–mediated pages 2-3, qiu2021dyneinactivationin pages 9-12)

NudA is consequently a **cytosolic, microtubule-associated motor**, not a secreted, membrane-spanning, nuclear-resident, or organellar lumen protein. It acts on cytoplasmic microtubules and transiently associates with cargo, septal minus ends, and microtubule-organizing centers.

## 3. Principal biological processes

### 3.1 Nuclear migration and distribution

The classical *A. nidulans* “nud” phenotype established the motor’s role in nuclear distribution. In dynein-pathway mutants, nuclei can divide but remain clustered near the spore end rather than migrating into and becoming evenly distributed through the elongating germ tube. A nudG light-chain mutation and a nudA deletion are epistatic—the double mutant is no worse than the more severe single mutant—placing both proteins in the same dynein-dependent motility pathway. (beckwith1998the“8kd”cytoplasmic pages 3-4)

Dynein-pathway null mutants are viable, which is important for functional interpretation: NudA is not absolutely required for basal cellular viability under laboratory conditions. Nevertheless, mutants display severe defects in nuclear distribution, compact colony morphology, reduced growth, and failed or strongly impaired conidiation. These developmental consequences are most parsimoniously downstream of defective intracellular organization rather than evidence that NudA directly regulates transcription or sporulation signaling. (efimov2003rolesofnude pages 1-2)

### 3.2 Early-endosome transport

Early endosomes are a major cytoplasmic-dynein cargo in filamentous fungi. In *A. nidulans*, they undergo rapid bidirectional transport: kinesins support plus-end-directed movement, whereas NudA-containing dynein drives retrograde or **basipetal movement toward microtubule minus ends and the cell interior**. This long-range circulation distributes endosomal signaling and membrane-trafficking machinery through highly polarized hyphae. (xiang2020cargomediatedactivationof pages 3-4)

The relevant cargo adapter is **HookA**. Its N-terminal dynein/dynactin-binding portion activates the motor, while its cargo-binding region associates with early endosomes. Overexpression of a cargo-binding-deficient activating HookA fragment causes dynein and dynactin to leave plus-end comets and accumulate at septal minus ends. A NudA tail mutation, **F208V**, blocks this relocation, directly connecting the NudA tail to adapter-mediated activation. The retrieved passages establish pathway membership and directionality but do not supply reliable NudA-specific velocity, run-length, or endosomal-flux values; such numbers should therefore not be invented. (qiu2019lis1regulatescargoadapter–mediated pages 2-3, xiang2020cargomediatedactivationof pages 3-4, xiang2020cargomediatedactivationof pages 5-6)

## 4. Regulatory pathway

A concise pathway model is:

1. Assembled NudA dynein and dynactin accumulate at microtubule plus ends near the hyphal tip.
2. HookA links early endosomes to dynein–dynactin and helps convert dynein from an autoinhibited state into an active transport complex.
3. NudF/LIS1 and NudE facilitate the conformational and assembly steps needed for efficient activation.
4. ATPase cycling in NudA—especially coordination among AAA1, AAA3, and AAA4—drives minus-end stepping.
5. Activated dynein transports the HookA-associated endosome basipetally or generates force for nuclear positioning.

### Dynactin

Dynactin is required for effective dynein function and localization. Arp11 loss produces a colony-growth defect comparable to a nudA-null phenotype and disrupts dynein plus-end accumulation. Conditional depletion of dynactin Arp1 causes one NudA AAA3 mutant to become diffuse and eliminates septal accumulation of another despite enhanced microtubule decoration. These results distinguish simple microtubule binding from productive dynactin-dependent motor targeting and activation. The latter analysis compared **31 versus 35 cells** and reported **p < 0.0001**. (zhang2008arp11affectsdynein–dynactin pages 2-3, qiu2021dyneinactivationin pages 9-12)

### NudF/LIS1

NudF is the fungal LIS1 homolog and an upstream regulator of NudA. It interacts with the heavy-chain motor region, including the first AAA repeat, and is required for efficient HookA-driven departure from plus ends. Stem-, AAA4-, and AAA3-state mutations in nudA can partly bypass NudF loss, demonstrating that LIS1 dependence is encoded in the heavy chain’s conformational and nucleotide cycle. (efimov2003rolesofnude pages 1-2, zhuang2007pointmutationsin pages 1-2, qiu2019lis1regulatescargoadapter–mediated pages 2-3, qiu2021dyneinactivationin pages 9-12)

The strongest AAA3 hydrolysis-blocking state can drive dynein toward septal minus ends even without NudF/LIS1, while early endosomes remain near plus ends. This uncoupling is mechanistically important: motor activation or minus-end localization alone does not guarantee productive cargo loading. Conversely, blocking AAA3 ATP binding can retain abnormal LIS1 association. These findings indicate that AAA3 coordinates motor activation, LIS1 release, and cargo engagement. Mutants also retained more nuclei in spore heads than wild type (**p < 0.0001**), consistent with impaired physiological motor function despite altered activation. (qiu2021dyneinactivationin pages 6-7, qiu2021dyneinactivationin pages 9-12)

### NudE and dynein accessory chains

Deleting nudE does not abolish NUDA plus-end comets but changes their behavior, indicating a regulatory rather than strictly targeting role. NudF overproduction can suppress nudE deletion yet inhibit a conditional nudA allele, illustrating dosage- and conformation-sensitive regulation. Intermediate- and heavy-chain plus-end localization are interdependent, while NUDG/LC8 is needed for normal heavy-chain tip localization. Thus, P45444 should be annotated as the motor within an obligate functional assembly, not as an independently acting monomer. (zhang2002cytoplasmicdyneinintermediate pages 7-8, beckwith1998the“8kd”cytoplasmic pages 3-4, efimov2003rolesofnude pages 1-2)

## 5. Recent developments, 2023–2024

No retrieved 2023–2024 primary study directly re-characterized UniProt P45444 or introduced a new *A. nidulans* NudA-specific biological function. The most recent target-specific mechanistic evidence in the retrieved corpus is the 2021 AAA3 study. The 2023–2024 literature is nevertheless useful for interpreting NudA within the conserved dynein mechanism.

A 2023 *Nature Communications* study supports an evolutionarily conserved model in which dynein heavy chains provide catalytic motor activity, while the intermediate-chain N-terminus coordinates dynactin and Nde1/Ndel1 interactions. LIS1-assisted transition from autoinhibited dynein to a dynein–dynactin–adapter assembly occurs through ordered regulatory steps; dynactin can organize as many as two parallel dynein dimers. This work tested mammalian and yeast systems, not P45444, so its application to NudA is comparative inference. Published September 2023: https://doi.org/10.1038/s41467-023-41466-5. (okada2023conservedrolesfor pages 1-2)

A February 2024 review places the heavy-chain homodimer at the catalytic center of an approximately **1.4-MDa mammalian cytoplasmic dynein-1 complex**, with intermediate, light-intermediate, and light chains providing assembly, localization, interaction, and enzymatic-regulatory functions. The 1.4-MDa value is not a measured mass for fungal NudA dynein and should not replace the direct approximately 20-S sedimentation observation in *A. nidulans*. Published February 2024: https://doi.org/10.3390/cells13040330. (rao2024structureandfunction pages 2-4, rao2024structureandfunction pages 21-22)

Recent Nde1/Ndel1 studies differ in some details of whether the factor promotes or restrains particular assembly intermediates, but converge on its role as a non-catalytic coordinator of dynein, LIS1, and dynactin engagement. This is consistent with the older *A. nidulans* NudE/NudF genetics, while not constituting new direct evidence about P45444. (okada2023conservedrolesfor pages 1-2, garrott2023ndel1modulatesdynein pages 11-12)

## 6. Current applications and real-world relevance

The principal current implementation is as a **mechanistic model system**. *A. nidulans* offers genetically tractable multinucleate hyphae, spatially separated plus- and minus-end sites, visible early-endosome cargo, and viable dynein mutants. GFP–NUDA localization, HookA-fragment activation, conditional dynactin depletion, suppressor genetics, and AAA-site mutations provide in-vivo assays for dynein activation, cargo loading, and LIS1 dependence. (zhuang2007pointmutationsin pages 3-4, qiu2019lis1regulatescargoadapter–mediated pages 2-3, qiu2021dyneinactivationin pages 9-12)

This model has broader biomedical relevance because LIS1/NDE1/NDEL1–dynein regulation is conserved and is central to animal nucleokinesis and intracellular transport. However, there is no evidence in the retrieved literature that P45444 itself is a clinical target, approved drug target, industrial transport component, or diagnostic biomarker. Likewise, the evidence does not establish a NudA-specific antifungal application. Such possibilities would be speculative.

## 7. Confidence-ranked annotation

**High confidence, direct evidence**

- Cytoplasmic dynein heavy-chain identity in *A. nidulans*.
- ATPase-containing, microtubule-binding motor architecture.
- Incorporation into an approximately 20-S multisubunit complex.
- Localization to microtubule plus-end comets and, after activation, septal minus-end regions.
- Requirement for normal nuclear migration/distribution.
- Participation in HookA/dynactin-dependent early-endosome transport.
- Regulation by NudF/LIS1, NudE, dynactin, and accessory dynein chains.

**High-to-moderate confidence, mixed direct and conserved inference**

- ATP hydrolysis is coupled to minus-end-directed mechanical stepping.
- AAA1 is the dominant hydrolysis site, while AAA3/AAA4 regulate mechanochemical state.
- Adapter/dynactin engagement converts an autoinhibited dynein dimer into a processive complex.

**Not established for P45444 from the retrieved evidence**

- A precise purified NudA stepping velocity, force, run length, or ATP-turnover constant.
- A complete P45444-specific high-resolution structure.
- Direct binding constants for NudA–HookA, NudA–NudF, or NudA–dynactin interactions.
- A clinical, agricultural, or industrial application specific to NudA.
- A new target-specific functional discovery published in 2023–2024.

## Selected primary and authoritative sources

- Beckwith SM et al. “The ‘8-kD’ Cytoplasmic Dynein Light Chain Is Required for Nuclear Migration and for Dynein Heavy Chain Localization in *Aspergillus nidulans*.” *Journal of Cell Biology*, November 1998. https://doi.org/10.1083/jcb.143.5.1239. (beckwith1998the“8kd”cytoplasmic pages 3-4, beckwith1998the“8kd”cytoplasmic pages 4-6)
- Zhang J, Han G, Xiang X. “Cytoplasmic dynein intermediate chain and heavy chain are dependent upon each other for microtubule end localization in *Aspergillus nidulans*.” *Molecular Microbiology*, April 2002. https://doi.org/10.1046/j.1365-2958.2002.02900.x. (zhang2002cytoplasmicdyneinintermediate pages 7-8)
- Efimov VP. “Roles of NUDE and NUDF proteins of *Aspergillus nidulans*.” *Molecular Biology of the Cell*, March 2003. https://doi.org/10.1091/mbc.e02-06-0359. (efimov2003rolesofnude pages 1-2)
- Zhuang L, Zhang J, Xiang X. “Point Mutations in the Stem Region and the Fourth AAA Domain of Cytoplasmic Dynein Heavy Chain Partially Suppress the Phenotype of NUDF/LIS1 Loss.” *Genetics*, March 2007. https://doi.org/10.1534/genetics.106.069013. (zhuang2007pointmutationsin pages 3-4, zhuang2007pointmutationsin pages 1-2, zhuang2007pointmutationsin pages 7-9)
- Qiu R, Zhang J, Xiang X. “LIS1 regulates cargo-adapter–mediated activation of dynein by overcoming its autoinhibition in vivo.” *Journal of Cell Biology*, September 2019. https://doi.org/10.1083/jcb.201905178. (qiu2019lis1regulatescargoadapter–mediated pages 2-3)
- Xiang X, Qiu R. “Cargo-Mediated Activation of Cytoplasmic Dynein in vivo.” *Frontiers in Cell and Developmental Biology*, October 2020. https://doi.org/10.3389/fcell.2020.598952. (xiang2020cargomediatedactivationof pages 3-4, xiang2020cargomediatedactivationof pages 5-6)
- Qiu R et al. “Dynein activation in vivo is regulated by the nucleotide states of its AAA3 domain.” *Current Biology*, 2021. https://doi.org/10.1016/j.cub.2021.08.030. (qiu2021dyneinactivationin pages 6-7, qiu2021dyneinactivationin pages 9-12, qiu2021dyneinactivationin pages 1-4)
- Okada K et al. “Conserved roles for the dynein intermediate chain and Ndel1 in assembly and activation of dynein.” *Nature Communications*, September 2023. https://doi.org/10.1038/s41467-023-41466-5. (okada2023conservedrolesfor pages 1-2)
- Rao L, Gennerich A. “Structure and Function of Dynein’s Non-Catalytic Subunits.” *Cells*, February 2024. https://doi.org/10.3390/cells13040330. (rao2024structureandfunction pages 2-4, rao2024structureandfunction pages 21-22)

References

1. (efimov2003rolesofnude pages 1-2): Vladimir P. Efimov. Roles of nude and nudf proteins of aspergillus nidulans: insights from intracellular localization and overexpression effects. Molecular biology of the cell, 14 3:871-88, Mar 2003. URL: https://doi.org/10.1091/mbc.e02-06-0359, doi:10.1091/mbc.e02-06-0359. This article has 76 citations and is from a domain leading peer-reviewed journal.

2. (zhuang2007pointmutationsin pages 3-4): L. Zhuang, Jun Zhang, and Xin Xiang. Point mutations in the stem region and the fourth aaa domain of cytoplasmic dynein heavy chain partially suppress the phenotype of nudf/lis1 loss in aspergillus nidulans. Genetics, 175:1185-1196, Mar 2007. URL: https://doi.org/10.1534/genetics.106.069013, doi:10.1534/genetics.106.069013. This article has 35 citations and is from a domain leading peer-reviewed journal.

3. (zhuang2007pointmutationsin pages 1-2): L. Zhuang, Jun Zhang, and Xin Xiang. Point mutations in the stem region and the fourth aaa domain of cytoplasmic dynein heavy chain partially suppress the phenotype of nudf/lis1 loss in aspergillus nidulans. Genetics, 175:1185-1196, Mar 2007. URL: https://doi.org/10.1534/genetics.106.069013, doi:10.1534/genetics.106.069013. This article has 35 citations and is from a domain leading peer-reviewed journal.

4. (beckwith1998the“8kd”cytoplasmic pages 3-4): Susan M. Beckwith, Christian H. Roghi, Bo Liu, and N. Ronald Morris. The “8-kd” cytoplasmic dynein light chain is required for nuclear migration and for dynein heavy chain localization in aspergillus nidulans. The Journal of Cell Biology, 143:1239-1247, Nov 1998. URL: https://doi.org/10.1083/jcb.143.5.1239, doi:10.1083/jcb.143.5.1239. This article has 115 citations.

5. (xiang2020cargomediatedactivationof pages 3-4): Xin Xiang and Rongde Qiu. Cargo-mediated activation of cytoplasmic dynein in vivo. Frontiers in Cell and Developmental Biology, Oct 2020. URL: https://doi.org/10.3389/fcell.2020.598952, doi:10.3389/fcell.2020.598952. This article has 43 citations.

6. (qiu2021dyneinactivationin pages 1-4): Rongde Qiu, Jun Zhang, Jeremy D. Rotty, and Xin Xiang. Dynein activation in vivo is regulated by the nucleotide states of its aaa3 domain. Current Biology, 31:4486-4498.e6, Apr 2021. URL: https://doi.org/10.1101/2021.04.12.439451, doi:10.1101/2021.04.12.439451. This article has 17 citations and is from a highest quality peer-reviewed journal.

7. (zhuang2007pointmutationsin pages 7-9): L. Zhuang, Jun Zhang, and Xin Xiang. Point mutations in the stem region and the fourth aaa domain of cytoplasmic dynein heavy chain partially suppress the phenotype of nudf/lis1 loss in aspergillus nidulans. Genetics, 175:1185-1196, Mar 2007. URL: https://doi.org/10.1534/genetics.106.069013, doi:10.1534/genetics.106.069013. This article has 35 citations and is from a domain leading peer-reviewed journal.

8. (qiu2021dyneinactivationin pages 6-7): Rongde Qiu, Jun Zhang, Jeremy D. Rotty, and Xin Xiang. Dynein activation in vivo is regulated by the nucleotide states of its aaa3 domain. Current Biology, 31:4486-4498.e6, Apr 2021. URL: https://doi.org/10.1101/2021.04.12.439451, doi:10.1101/2021.04.12.439451. This article has 17 citations and is from a highest quality peer-reviewed journal.

9. (qiu2021dyneinactivationin pages 9-12): Rongde Qiu, Jun Zhang, Jeremy D. Rotty, and Xin Xiang. Dynein activation in vivo is regulated by the nucleotide states of its aaa3 domain. Current Biology, 31:4486-4498.e6, Apr 2021. URL: https://doi.org/10.1101/2021.04.12.439451, doi:10.1101/2021.04.12.439451. This article has 17 citations and is from a highest quality peer-reviewed journal.

10. (beckwith1998the“8kd”cytoplasmic pages 4-6): Susan M. Beckwith, Christian H. Roghi, Bo Liu, and N. Ronald Morris. The “8-kd” cytoplasmic dynein light chain is required for nuclear migration and for dynein heavy chain localization in aspergillus nidulans. The Journal of Cell Biology, 143:1239-1247, Nov 1998. URL: https://doi.org/10.1083/jcb.143.5.1239, doi:10.1083/jcb.143.5.1239. This article has 115 citations.

11. (zhang2002cytoplasmicdyneinintermediate pages 7-8): Jun Zhang, Gongshe Han, and Xin Xiang. Cytoplasmic dynein intermediate chain and heavy chain are dependent upon each other for microtubule end localization in aspergillus nidulans. Molecular Microbiology, 44:381-392, Apr 2002. URL: https://doi.org/10.1046/j.1365-2958.2002.02900.x, doi:10.1046/j.1365-2958.2002.02900.x. This article has 51 citations and is from a domain leading peer-reviewed journal.

12. (qiu2019lis1regulatescargoadapter–mediated pages 2-3): Rongde Qiu, Jun Zhang, and Xin Xiang. Lis1 regulates cargo-adapter–mediated activation of dynein by overcoming its autoinhibition in vivo. The Journal of Cell Biology, 218:3630-3646, Sep 2019. URL: https://doi.org/10.1083/jcb.201905178, doi:10.1083/jcb.201905178. This article has 82 citations.

13. (zhang2008arp11affectsdynein–dynactin pages 2-3): Jun Zhang, Liqin Wang, Lei Zhuang, Liang Huo, Shamsideen Musa, Shihe Li, and Xin Xiang. Arp11 affects dynein–dynactin interaction and is essential for dynein function in aspergillus nidulans. Traffic, 9:1073-1087, Jul 2008. URL: https://doi.org/10.1111/j.1600-0854.2008.00748.x, doi:10.1111/j.1600-0854.2008.00748.x. This article has 38 citations and is from a peer-reviewed journal.

14. (okada2023conservedrolesfor pages 1-2): Kyoko Okada, Bharat R. Iyer, Lindsay G. Lammers, Pedro A. Gutierrez, Wenzhe Li, Steven M. Markus, and Richard J. McKenney. Conserved roles for the dynein intermediate chain and ndel1 in assembly and activation of dynein. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41466-5, doi:10.1038/s41467-023-41466-5. This article has 27 citations and is from a highest quality peer-reviewed journal.

15. (rao2024structureandfunction pages 2-4): Lu Rao and Arne Gennerich. Structure and function of dynein’s non-catalytic subunits. Cells, 13:330, Feb 2024. URL: https://doi.org/10.3390/cells13040330, doi:10.3390/cells13040330. This article has 15 citations.

16. (rao2024structureandfunction pages 21-22): Lu Rao and Arne Gennerich. Structure and function of dynein’s non-catalytic subunits. Cells, 13:330, Feb 2024. URL: https://doi.org/10.3390/cells13040330, doi:10.3390/cells13040330. This article has 15 citations.

17. (xiang2020cargomediatedactivationof pages 5-6): Xin Xiang and Rongde Qiu. Cargo-mediated activation of cytoplasmic dynein in vivo. Frontiers in Cell and Developmental Biology, Oct 2020. URL: https://doi.org/10.3389/fcell.2020.598952, doi:10.3389/fcell.2020.598952. This article has 43 citations.

18. (garrott2023ndel1modulatesdynein pages 11-12): Sharon R Garrott, John P Gillies, Aravintha Siva, Saffron R Little, Rita El Jbeily, and Morgan E DeSantis. Ndel1 modulates dynein activation in two distinct ways. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.25.525437, doi:10.1101/2023.01.25.525437. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](nudA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. qiu2021dyneinactivationin pages 1-4
2. zhuang2007pointmutationsin pages 7-9
3. zhang2002cytoplasmicdyneinintermediate pages 7-8
4. qiu2021dyneinactivationin pages 6-7
5. efimov2003rolesofnude pages 1-2
6. xiang2020cargomediatedactivationof pages 3-4
7. qiu2021dyneinactivationin pages 9-12
8. zhuang2007pointmutationsin pages 1-2
9. okada2023conservedrolesfor pages 1-2
10. zhuang2007pointmutationsin pages 3-4
11. rao2024structureandfunction pages 2-4
12. rao2024structureandfunction pages 21-22
13. xiang2020cargomediatedactivationof pages 5-6
14. doi:10.1534/genetics.106.069013
15. doi:10.1016/j.cub.2021.08.030
16. doi:10.1083/jcb.143.5.1239
17. doi:10.1046/j.1365-2958.2002.02900.x
18. doi:10.1091/mbc.e02-06-0359
19. doi:10.1083/jcb.201905178
20. doi:10.3389/fcell.2020.598952
21. doi:10.1111/j.1600-0854.2008.00748.x
22. doi:10.1038/s41467-023-41466-5
23. doi:10.3390/cells13040330
24. https://doi.org/10.1534/genetics.106.069013
25. https://doi.org/10.1016/j.cub.2021.08.030
26. https://doi.org/10.1083/jcb.143.5.1239
27. https://doi.org/10.1046/j.1365-2958.2002.02900.x
28. https://doi.org/10.1091/mbc.e02-06-0359
29. https://doi.org/10.1083/jcb.201905178
30. https://doi.org/10.3389/fcell.2020.598952
31. https://doi.org/10.1111/j.1600-0854.2008.00748.x
32. https://doi.org/10.1038/s41467-023-41466-5
33. https://doi.org/10.3390/cells13040330
34. https://doi.org/10.1038/s41467-023-41466-5.
35. https://doi.org/10.3390/cells13040330.
36. https://doi.org/10.1083/jcb.143.5.1239.
37. https://doi.org/10.1046/j.1365-2958.2002.02900.x.
38. https://doi.org/10.1091/mbc.e02-06-0359.
39. https://doi.org/10.1534/genetics.106.069013.
40. https://doi.org/10.1083/jcb.201905178.
41. https://doi.org/10.3389/fcell.2020.598952.
42. https://doi.org/10.1016/j.cub.2021.08.030.
43. https://doi.org/10.1091/mbc.e02-06-0359,
44. https://doi.org/10.1534/genetics.106.069013,
45. https://doi.org/10.1083/jcb.143.5.1239,
46. https://doi.org/10.3389/fcell.2020.598952,
47. https://doi.org/10.1101/2021.04.12.439451,
48. https://doi.org/10.1046/j.1365-2958.2002.02900.x,
49. https://doi.org/10.1083/jcb.201905178,
50. https://doi.org/10.1111/j.1600-0854.2008.00748.x,
51. https://doi.org/10.1038/s41467-023-41466-5,
52. https://doi.org/10.3390/cells13040330,
53. https://doi.org/10.1101/2023.01.25.525437,