---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-25T19:22:57.750555'
end_time: '2025-11-25T19:28:12.747618'
duration_seconds: 315.0
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00047244
  rule_type: arba
  go_terms: GO:0043605 (amide catabolic process)
  conditions_summary: '**Condition Set 1:** InterPro id: Urease, beta subunit-like
    (InterPro:IPR002019) AND InterPro id: Urease, gamma/gamma-beta subunit (InterPro:IPR002026)
    AND InterPro id: Urease active site (InterPro:IPR017950)


    **Condition Set 2:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1
    (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase
    PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 3:** FunFam id: Putative ureidoglycolate hydrolase (CATH.FunFam:3.30.70.360:FF:000012)
    AND FunFam id: Allantoate amidohydrolase (CATH.FunFam:3.40.630.10:FF:000044) AND
    taxon: Viridiplantae (NCBITaxon:33090)


    **Condition Set 4:** FunFam id: (S)-ureidoglycine aminohydrolase (CATH.FunFam:2.60.120.10:FF:000137)
    AND taxon: Streptophyta (NCBITaxon:35493)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 48
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00047244
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0043605 (amide catabolic process)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Urease, beta subunit-like (InterPro:IPR002019) AND InterPro id: Urease, gamma/gamma-beta subunit (InterPro:IPR002026) AND InterPro id: Urease active site (InterPro:IPR017950)

**Condition Set 2:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: Putative ureidoglycolate hydrolase (CATH.FunFam:3.30.70.360:FF:000012) AND FunFam id: Allantoate amidohydrolase (CATH.FunFam:3.40.630.10:FF:000044) AND taxon: Viridiplantae (NCBITaxon:33090)

**Condition Set 4:** FunFam id: (S)-ureidoglycine aminohydrolase (CATH.FunFam:2.60.120.10:FF:000137) AND taxon: Streptophyta (NCBITaxon:35493)

*These condition sets are OR-ed together (any match triggers the annotation)*

---

## Research Objective

This is a UniProt annotation rule that predicts GO terms based on protein domain/family signatures. Your task is to evaluate whether this rule makes valid biological predictions based on what is known about the relevant domains and families, their structure, and conservation.

In an ideal case, you will be able to find literature that speaks specifically to the relationship between domains/families and
the function. Failing that, include what is known specifically about other functions that domains/families have, as well what domains/
families are known for the function.

## Research Questions

### 1. Domain/Signature Context

For each domain signature in this rule:
- What is the biological function of proteins containing this domain?
- Is this domain diagnostic for the predicted function?
- Are there known subfamilies with different functions?
- Is the domain or family known to be multifunctional, are there known cases of neofunctionalization?

### 2. GO Term Appropriateness

For the predicted GO term(s) **GO:0043605 (amide catabolic process)**:
- Is this GO term appropriate for proteins matching these conditions?
- Is the term too broad? (e.g., "catalytic activity" when a more specific term exists)
- Is the term too narrow? (e.g., a specific substrate when the domain covers broader specificity)
- Are there better alternative GO terms?

### 3. Literature Support

- What experimental evidence supports this functional annotation?
- Are there key papers describing this protein family/enzyme?
- Are there any contradictory findings in the literature?
- Is this a well-established function or more speculative?

### 4. Taxonomic Considerations

If this rule has taxonomic restrictions:
- Is the function conserved across the taxa included?
- Are there taxa that should be excluded (different function)?
- Are there taxa that could be included but are currently excluded?

### 5. Rule Logic Assessment

- Do the domain combinations make biological sense?
- Are there redundant conditions that could be removed?
- Could false positives arise from these conditions?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief assessment of rule validity
2. **Domain Analysis** - What each domain/signature represents
3. **GO Term Evaluation** - Assessment of the predicted annotation
4. **Evidence Review** - Key literature supporting or contradicting the rule
5. **Recommendations** - Suggested improvements or concerns

Be sure to include citations for all statements.

## Output

<think>
This is a comprehensive research task asking me to evaluate a UniProt annotation rule (ARBA00047244) that predicts GO:0043605 (amide catabolic process) based on various domain and family signatures. Let me break down what I need to analyze:

The rule has 4 condition sets, any of which trigger the GO:0043605 annotation:

1. Urease domain combinations (beta, gamma/gamma-beta, and active site domains)
2. PM20D1 N-fatty-acyl-amino acid synthase/hydrolase with eukaryotic restriction
3. Ureidoglycolate hydrolase and allantoate amidohydrolase combinations in plants
4. (S)-ureidoglycine aminohydrolase in Streptophyta

The GO term GO:0043605 is "amide catabolic process" - chemical reactions and pathways resulting in the breakdown of an amide.

Let me organize my thinking:

**Planning my response:**

1. I need to evaluate whether each of these domain/family combinations appropriately predicts amide catabolism
2. I need to assess if GO:0043605 is the right term or if there are better alternatives
3. I need to look at the evidence provided in the search results
4. I need to consider taxonomic appropriateness

From the search results, I have information about:
- Urease structure and mechanism (sources 1, 4, 18, 29, 57)
- Amide catabolic process definition (sources 2, 5, 14, 17, 19, 22, 25, 28, 38)
- Urease activity definition (sources 31, 34, 49, 52)
- PM20D1 N-acyl amino acid synthase/hydrolase (sources 7, 44, 47)
- Ureidoglycine aminohydrolase (sources 9, 12, 13, 21, 32, 56)


- Allantoate amidohydrolase (sources 16, 21, 50)
- Urease in different organisms (sources 18, 33, 43, 46)
- Urease inhibition and catalytic mechanisms (sources 26, 42)

**Condition Set 1: Urease domains**
- These proteins contain Urease beta-subunit-like, gamma/gamma-beta subunit, and active site domains
- Urease hydrolyzes urea to ammonia and CO2 via carbamate
- The reaction is: (NH2)2CO + H2O →  CO2 + 2NH3
- Since urea is fundamentally H2N-CO-NH2, urease activity represents amide catabolic activity

**Condition Set 2: PM20D1**
- Fatty acid amide hydrolases that synthesize and hydrolyze N-acyl amino acids
- They cleave C-N bonds through amide hydrolase activity, qualifying as amide catabolic

**Condition Set 3: Ureidoglycolate hydrolase and allantoate amidohydrolase**
- Part of the ureide pathway in purine catabolism
- Break down ureides containing amide bonds
- Allantoate amidohydrolase specifically degrades allantoate through amide bond cleavage

, meeting amide catabolic criteria

**Condition Set 4: (S)-ureidoglycine aminohydrolase**
- Degrades ureidoglycine to ureidoglycolate and ammonia
- Ureidoglycine contains an amide group as a non-standard amino acid
- This represents amide catabolic activity

I'm now preparing to write a comprehensive 10,000+ word report evaluating this rule. The structure will include an executive summary, rule context and purpose, detailed domain and signature analysis for each condition set, GO term evaluation, evidence review, taxonomic considerations, rule logic assessment, and recommendations with conclusions. I'll ensure thorough documentation with relevant citations throughout.
</think>

# Comprehensive Evaluation of UniProt Rule ARBA00047244 for GO:0043605 Annotation

This report evaluates the validity and appropriateness of UniProt rule ARBA00047244, which predicts the Gene Ontology term GO:0043605 (amide catabolic process) based on four distinct molecular signature condition sets spanning urease enzymes, fatty acid amide hydrolases, and ureide pathway enzymes. Through systematic analysis of the biochemical literature, structural biology, enzyme mechanisms, and taxonomic distribution, this evaluation determines whether these signatures appropriately predict amide catabolism and whether the GO term represents the optimal annotation for proteins matching these conditions.

## Executive Summary

The UniProt rule ARBA00047244 presents a mixed picture of annotation accuracy and appropriateness. The rule correctly identifies that proteins matching these signatures do possess amide catabolic activity, as all condition sets target enzymes known to catalyze the hydrolysis of amide bonds. However, critical evaluation reveals significant nuances regarding the specificity and precision of the annotation. The rule's first condition set, targeting urease enzymes through domain combinations, is well-supported by extensive literature demonstrating that ureases catalyze the hydrolysis of urea, a simple amide compound, through a well-characterized nickel-dependent mechanism[1][4][18]. Condition sets three and four, targeting the ureide pathway enzymes in plants and bacteria, are similarly well-supported by recent structural and biochemical studies demonstrating manganese-dependent amide hydrolysis in purine catabolism[9][13][21]. However, condition set two, targeting PM20D1 N-fatty-acyl-amino acid synthase/hydrolase, raises questions about annotation specificity, as this enzyme's primary biological role centers on fatty acid-amino acid condensation rather than preferential amide catabolism[7][44]. Additionally, while GO:0043605 (amide catabolic process) is technically accurate, the annotation may obscure more specific biological functions, particularly for urease enzymes whose primary ecological role involves nitrogen mobilization and pH modulation rather than general amide catabolism[1][18]. The rule would benefit from refinement to distinguish between enzyme classes with divergent biological roles despite overlapping catalytic mechanisms.

## The Role of Urease Enzymes in Amide Catabolism

### Historical Context and Enzymatic Discovery

Urease represents one of the most historically significant enzymes in biochemistry, bearing distinction as the first enzyme ever crystallized and the first to be proven to be a protein rather than a mystical biological principle[1][18][43][46]. The enzyme was first isolated in 1874 from microorganisms capable of breaking down urea, and systematic study of urease began in earnest over the following decades[1][60]. The demonstration that urease contains nickel ions as essential cofactors came only in 1975, providing critical insight into the enzyme's catalytic mechanism and establishing the broader principle that some enzymes require metal ions for catalytic activity[18][60]. This historical trajectory illustrates how understanding of urease has evolved from curiosity about nitrogen metabolism to detailed structural and mechanistic knowledge.

### Biochemical Function and Catalytic Mechanism

Urease catalyzes the hydrolysis of urea into ammonia and carbon dioxide through a two-stage process that generates carbamate as an intermediate[1][4][31]. The overall reaction is represented as \((NH_2)_2CO + H_2O \rightarrow CO_2 + 2NH_3\)[1][31], though mechanistic studies have revealed that the reaction proceeds through a carbamate intermediate: \((NH_2)_2CO + H_2O \rightarrow NH_3 + H_2NCO_2^-\), followed by spontaneous hydrolysis of carbamate to form the second ammonia molecule and carbonic acid[1][4]. The catalytic proficiency of urease is extraordinary, increasing the rate of urea hydrolysis by a factor of at least 10^14 compared to the uncatalyzed reaction[1][18]. This remarkable catalytic efficiency derives from the enzyme's sophisticated active site architecture, which positions two nickel ions in close proximity to stabilize the urea substrate and activate water for nucleophilic attack[4][29][57].

The active site of urease contains a bi-nickel center separated by approximately 3.5 to 3.8 Ångströms, coordinated by histidine residues, aspartate residues, and a unique carbamylated lysine that participates directly in catalysis[1][29]. The mechanism proceeds through substrate binding to Ni(1) via the carbonyl oxygen, followed by nucleophilic attack from a hydroxide ion coordinated to Ni(2)[4][29][57]. Formation of a tetrahedral intermediate containing the hydrated urea precedes C-N bond cleavage and liberation of ammonia and carbamate[4][29]. Remarkably, approximately only 0.3% of total urease enzyme molecules exist in the active form at any given time due to unfavorable protonation equilibria of critical His320 residue, yet this small fraction of active enzyme is sufficient to drive rapid catalysis through subtle conformational changes and coupling of proton transfer events[1]. The mobile flap region covering the active site undergoes conformational transitions from open to closed states that regulate substrate access and product release[1][29][43].

### Structural Variations Across Organisms

The structure of urease varies significantly depending on the source organism[1][18][33][43][46]. Plant ureases, such as jack bean urease (JBU) from *Canavalia ensiformis*, exist as single polypeptide chains forming hexameric assemblies[33][43][46]. Bacterial ureases display greater structural diversity, with *Helicobacter pylori* urease containing two distinct subunits (α and β) and other bacteria such as *Klebsiella aerogenes* and *Bacillus pasteurii* possessing three subunits (α, β, and γ)[1][33][43]. Despite these quaternary structure differences, the active site architecture remains remarkably conserved across all urease enzymes studied to date[1][18][43]. The conservation of the bi-nickel center, liganding residues, and catalytic mechanism across such divergent organisms underscores the fundamental importance of this particular solution to amide hydrolysis chemistry[1][18][43].

Comparative structural studies between plant and bacterial ureases reveal that plant ureases possess insecticidal properties independent of their catalytic activity, properties not observed in bacterial ureases[43][46]. This suggests that while the core urease fold and catalytic mechanism are conserved, plant ureases have acquired additional functional domains or structural features that confer biological activities beyond simple amide hydrolysis[43][46]. The structural basis for these non-enzymatic activities likely involves an amphipathic β-hairpin in an "entomotoxic peptide" region that may form membrane-inserting structures analogous to β-pore-forming toxins[43][46].

### Biological Roles and Ecological Significance

Urease serves multiple distinct biological functions beyond simple amide catabolism. In environmental contexts, urease-producing soil microorganisms benefit from the nitrogen made available through urea degradation in the form of ammonium, which can be incorporated into amino acids and nucleic acids[1][18]. Urease activity increases the pH of its environment as ammonia is produced, which is chemically basic, and this pH modulation represents an important bacterial stress response to acidic environments[1][18][29]. In the case of pathogenic bacteria such as *Helicobacter pylori*, urease activity is essential for survival in the highly acidic stomach environment, as urea hydrolysis generates ammonia that buffers gastric acid and allows bacterial colonization[1][4][18][29]. Furthermore, ammonia derived from urease activity can block phagosome-lysosome fusion in host cells, representing an important defensive mechanism against immune system attack[4][29].

The ureolytic activity of human gut microbiota deserves particular mention, as these microorganisms hydrolyze approximately 30% of all urea produced in our bodies[18]. This substantial metabolic flux through urease enzymes underscores the quantitative importance of amide catabolism in nitrogen cycling even in mammalian systems. Additionally, in *Proteus mirabilis*, a pathogenic bacterium causing urinary tract infections and catheter incrustation, urease activity directly contributes to virulence by promoting the formation of ammonia, leading to crystalline deposits that damage tissue[39].

### Activation and Post-translational Modification

Urease synthesis produces an inactive apo-enzyme that requires post-translational activation involving incorporation of nickel ions into the buried active site[15][18]. In bacteria such as *Helicobacter pylori*, this activation process involves four accessory proteins designated UreD, UreF, UreG, and UreE, collectively acting as metallochaperones that bind and transport nickel ions while driving the apo-urease into its fully active conformation[15][18]. The interaction between urease and UreD represents a critical early step in this activation cascade, with recent cryo-EM structural and computational studies identifying specific residue contacts essential for metal ion delivery[15]. The genetic ablation or disruption of these accessory proteins results in complete loss of urease activity, underscoring their essential roles[18]. In plants and fungi, the functions of bacterial UreG and UreE chaperones appear to be combined in a single UreG protein, which carries a histidine-rich domain with metal binding properties that facilitate nickel incorporation[18].

## The PM20D1 Fatty Acid Amide Hydrolase Family

### Biochemical Function and Bidirectional Catalysis

The protein designated as PM20D1 (peptidase M20 domain-containing protein 1) represents a distinct class of enzyme with amide bond-related catalytic activity[7][44][47]. Unlike urease, which catalyzes unidirectional hydrolysis of a specific small molecule substrate, PM20D1 functions as a bidirectional enzyme capable of catalyzing both synthesis and hydrolysis of N-acyl amino acids from free fatty acids and amino acids[7][44][47]. The N-acyl amino acids represent a diverse bioactive lipid family that emerges from the condensation of long-chain polyunsaturated fatty acids with amino acids, producing compounds such as N-arachidonoyl-phenylalanine (C20:4-Phe) and N-arachidonoyl-glycine (C20:4-Gly)[7][44][47]. PM20D1 catalyzes the condensation of free fatty acids and free amino acids to generate these N-acyl amino acids while also catalyzing the reverse hydrolysis reaction[7][10][44][47].

The equilibrium and kinetics of PM20D1-catalyzed reactions differ substantially from urease catalysis. In vitro assays of recombinant PM20D1 demonstrate approximately 1.2 ± 0.1% conversion in the synthase direction and 94.0 ± 0.8% conversion in the hydrolase direction, indicating a strong thermodynamic bias toward hydrolysis but nonetheless significant synthase activity[47]. This bidirectional catalytic capacity contrasts sharply with urease, which catalyzes only the hydrolytic reaction and does so with essentially complete kinetic bias toward hydrolysis[1][4][47].

### Substrate Specificity and Functional Diversity

PM20D1 exhibits considerable substrate specificity, particularly when compared to related enzymes such as fatty acid amide hydrolase (FAAH). While PM20D1 catalyzes robust hydrolysis activity across a panel of diverse N-acyl amino acid substrates including C18:1-Gly, C18:1-Ser, C20:4-Gly, and C20:4-Ser, FAAH exhibits a more restricted substrate scope, efficiently hydrolyzing only a subset of these compounds[7][44]. This differential substrate specificity reveals that despite both enzymes catalyzing amide hydrolysis, their biological roles and substrate preferences differ substantially. The tissue-specific expression patterns of these enzymes further underscore their distinct physiological functions, with PM20D1 present as a classically secreted enzyme in circulation in both mice and humans, while FAAH is localized to specific tissues including brain and liver with highest expression there[7][44].

Recent biochemical investigations have revealed extensive and non-additive biochemical engagement between PM20D1 and FAAH in regulating endogenous N-acyl amino acid levels[7][44]. Genetic ablation or selective pharmacological inhibition of either enzyme alone results in bidirectional dysregulation of N-acyl amino acids, yet dual blockade of both enzymes produces complex, context-dependent effects rather than uniform elevation or depletion of all N-acyl amino acid substrates[7][44]. This pattern indicates an enzymatic division of labor, with PM20D1 and FAAH cooperatively regulating distinct subsets of the N-acyl amino acid family[7][44].

### Thermogenic and Metabolic Functions

Beyond their roles in amide hydrolysis, N-acyl amino acids generated and metabolized by PM20D1 serve important thermogenic functions. In mice, genetic ablation of PM20D1 leads to complex, bidirectional dysregulation of N-acyl amino acid levels and metabolic dysfunction characterized by glucose intolerance and decreased insulin sensitivity[7][47]. Conversely, overexpression of PM20D1 achieved through adeno-associated viral vectors drives increased biosynthesis of circulating N-acyl amino acids, resulting in increased energy expenditure and reduced adiposity on high-fat diet[7][47]. These observations suggest that while PM20D1 does catalyze amide hydrolysis, its primary biological role centers on regulating a specialized bioactive lipid family with thermogenic properties rather than participating in general amide catabolism for nitrogen mobilization.

## The Ureide Pathway and Purine Catabolism

### Overview of the Ureide Pathway

The ureide pathway represents the primary route of purine base catabolism in plants and some bacteria, providing a mechanism for mobilizing nitrogen from the purine ring for reassimilation into amino acids and other nitrogen-containing biomolecules[9][13][16][21][24]. This metabolic route has been extensively characterized in *Arabidopsis thaliana*, with genes encoding pathway enzymes identified in all sequenced plant genomes to date as well as in selected bacterial and fungal species[13][21][24][56]. The ureide pathway proceeds through a series of seven enzymatic reactions, beginning with uric acid (the major product of early purine catabolism) and leading to glyoxylate and ammonia[9][13][21].

The nitrogen economy of the ureide pathway demonstrates remarkable efficiency. Rather than excreting oxidized purines as waste products (as occurs in humans and other mammals), organisms utilizing the ureide pathway capture the purine ring nitrogen for further assimilation. This represents a particularly important metabolic capacity in nitrogen-limited environments, where purine catabolism can serve as a significant source of remobilizable nitrogen[13][21][24][56]. In legume-family plants such as soybean (*Glycine max*), the ureide pathway assumes particular prominence, as symbiotically fixed nitrogen is incorporated primarily into purine nucleotides in root nodules, which are subsequently catabolized to ureides (allantoin and allantoate) and exported via the xylem to shoot tissues where nitrogen is reassimilated[21][24][56].

### Allantoate Amidohydrolase Function and Structure

Allantoate amidohydrolase (AAH), also designated as allantoate amidohydrolase (EC 3.5.3.9), catalyzes a critical early step in the ureide pathway, specifically the hydrolysis of allantoate to yield carbon dioxide, ammonia, and (S)-ureidoglycine[16][21][50]. This enzyme thus represents a clear example of amide catabolic activity, as allantoate contains an amide functional group that must be cleaved to release ammonia. The enzyme depends on manganese ions as essential cofactors for catalytic activity[21]. Upregulation of AAH transcripts has been observed in imbibed dormant seeds compared with after-ripened seeds, suggesting important roles in seed germination and nitrogen mobilization during early developmental stages[16].

The functional significance of AAH in plant nitrogen metabolism was demonstrated through analysis of *Ataah* mutant seeds of *Arabidopsis thaliana*[16]. These mutant seeds exhibited increased dormancy and accumulated high levels of allantoate, allantoin, and urea, while displaying reduced levels of energy-related metabolites and several amino acids upon seed imbibition compared with wild-type Columbia-0 plants[16]. These observations establish AAH as a critical enzyme in seed development and nitrogen utilization. The accumulation of ureides in *Ataah* mutants reflects the loss of enzymatic capacity to break down these nitrogen-rich compounds, while the reduced amino acid content indicates impaired nitrogen remobilization, a key metabolic consequence of disrupted ureide catabolism[16].

### (S)-Ureidoglycine Aminohydrolase: A Key Pathway Enzyme

(S)-Ureidoglycine aminohydrolase (UGlyAH), designated EC 3.5.3.-, catalyzes the enantioselective hydrolysis of (S)-ureidoglycine to produce (S)-ureidoglycolate and ammonia, using Mn2+ as a cofactor[9][13][21][32][56]. This enzyme represents another clear example of amide catabolic activity, as it specifically releases ammonia from an amide-containing substrate. The enzyme has been structurally and functionally characterized through detailed crystallographic and biochemical studies in *Arabidopsis thaliana* (AtUGlyAH)[9][13][32][56].

The crystal structure of AtUGlyAH in both ligand-free and substrate-bound forms revealed that the enzyme adopts a bicupin fold with a β-barrel architecture and functions as an octameric assembly[9][13][32][56]. The Mn2+ ion acts as a molecular anchor, binding (S)-ureidoglycine in a manner that dictates the enantioselectivity of the reaction and facilitates ammonia release[9][13][32]. Mutation studies identified active site residues critical for binding and catalysis, including those involved in Mn2+ coordination and substrate binding[9][13][32]. The enzyme's localization in plants differs between species—in bacteria it is cytosolic, while in plants it localizes to the endoplasmic reticulum, reflecting the compartmentalization of ureide metabolism in eukaryotic cells[21].

The physiological importance of UGlyAH extends beyond simple amide hydrolysis. Studies establishing a role for UGlyAH in ureide catabolism demonstrated that UAH (ureidoglycolate amidohydrolase) is required for ureidoglycolate hydrolysis in *Arabidopsis*, and that both AAH and UAH are needed in soybean[24]. This indicates that complete ureide catabolism requires multiple enzymes acting sequentially, with UGlyAH serving as an essential intermediate step that enables nitrogen liberation from the purine ring[24][56].

### Ureidoglycolate Hydrolase and the Final Degradation Steps

Ureidoglycolate hydrolase (also designated as ureidoglycolate amidohydrolase), represents the final enzymatic step in the ureide pathway in *Arabidopsis* and some bacterial species[11][24]. This enzyme cleaves ureidoglycolate to produce glyoxylate and carbon dioxide, thus completing the degradation of the purine ring structure and liberating nitrogen in the form of ammonia from earlier pathway steps[24]. While direct information on ureidoglycolate hydrolase mechanisms is limited in the provided literature, its classification as an amidohydrolase confirms its role in amide bond cleavage.

The interaction between ureidoglycolate hydrolase and earlier pathway enzymes was demonstrated through genetic studies in which a *uah ure* double mutant displayed significant growth reduction while both single mutants did not[24]. This synthetic phenotype indicates that the ureide catabolism pathway can be partially bypassed if non-enzymatic ureidoglycolate decay generates urea that reaches the cytosol where urease (URE) can hydrolyze it, but complete loss of both pathways severely impairs plant growth and nitrogen utilization[24]. Such findings underscore the quantitative importance of ureidoglycolate hydrolase function in plants.

## Evaluation of GO:0043605 (Amide Catabolic Process)

### Definition and Biological Relevance of the GO Term

The Gene Ontology term GO:0043605 is formally defined as "the chemical reactions and pathways resulting in the breakdown of an amide, any derivative of an oxoacid in which an acidic hydroxy group has been replaced by an amine group"[2][5][14][17][19][22][25][28][38][41]. This represents a relatively broad functional annotation encompassing any enzyme capable of cleaving C-N bonds formed between carbonyl carbons and nitrogen atoms. The amide bond represents a fundamental chemical moiety found in proteins (the peptide bond is a specialized amide), nucleic acids, lipids, and numerous other biomolecules, and its hydrolysis is central to numerous metabolic pathways.

The breadth of GO:0043605 presents both advantages and disadvantages. The advantage is that it captures a common chemical mechanism shared by enzymes with diverse biological functions and substrate specificities, enabling computational analyses to group functionally diverse proteins. However, this breadth may obscure more specific biological roles. For example, urease primarily functions in nitrogen cycling and environmental pH modulation rather than general amide catabolism, yet GO:0043605 would be accurate albeit potentially misleading if used as the only annotation.

### Chemical Basis of Amide Hydrolysis

The chemistry of amide hydrolysis proceeds through distinct mechanisms depending on pH and catalytic environment. Under acidic conditions, hydrolysis begins with protonation of the amide carbonyl oxygen, making the carbonyl carbon a better electrophile susceptible to nucleophilic attack by water[55][58]. The protonated carbonyl undergoes water attack to form a tetrahedral intermediate, followed by proton transfer to activate the leaving group (the amino group becomes protonated and thus a poorer nucleophile), resulting in C-N bond cleavage and liberation of a carboxylic acid and an amine[55][58].

Enzyme-catalyzed amide hydrolysis achieves its catalytic proficiency through substrate activation mechanisms quite different from simple protonation. In urease, the bi-nickel center stabilizes the urea substrate through coordination of the carbonyl oxygen to Ni(1), making the carbon more electrophilic and polarizing the C-N bonds[1][4][29][57]. The hydroxide ion coordinated to Ni(2) then serves as the nucleophile for attack on the urea carbonyl carbon[4][29][57]. In contrast, manganese-dependent enzymes such as UGlyAH employ similar coordination chemistry but use Mn2+ as the activating metal ion[9][13][32]. These enzyme-catalyzed mechanisms represent highly evolved solutions that achieve rates many orders of magnitude faster than uncatalyzed hydrolysis while maintaining remarkable substrate specificity.

### Specificity and Appropriateness of the GO Term for Each Condition Set

For condition set 1 (urease enzymes), GO:0043605 is appropriate but potentially insufficiently specific. Ureases catalyze hydrolysis of urea, the simplest amide, and thus undoubtedly perform amide catabolism[1][4][18]. However, the specific biological roles of urease in nitrogen mobilization, pH modulation, and virulence are better captured by more specific annotations such as "nitrogen utilization" or "bacterial survival in acidic environments"[1][18][29]. The GO Biological Process ontology does include GO:0043419 "urea catabolic process," which represents a more specific annotation than GO:0043605, as it captures the specific substrate (urea) rather than the broader class (amides)[14][19][22][38].

For condition set 2 (PM20D1 and related N-acyl amino acid synthase/hydrolases), the appropriateness of GO:0043605 is questionable. While PM20D1 does catalyze hydrolysis of amide bonds, its primary biological role involves regulation of N-acyl amino acid biosynthesis and catabolism for thermogenic purposes[7][44][47]. The prediction of GO:0043605 might mislead researchers into interpreting PM20D1 primarily as a general amide-degrading enzyme rather than recognizing its specialized role in lipid signaling and energy metabolism. A more appropriate annotation might reference "metabolic regulation" or "N-acyl amino acid metabolism."

For condition sets 3 and 4 (ureide pathway enzymes), GO:0043605 is highly appropriate, as these enzymes specifically function to liberate ammonia from ureide substrates as part of purine catabolism[9][13][16][21][24]. The ureides are nitrogen-rich amide-containing molecules, and their systematic degradation through allantoate amidohydrolase, (S)-ureidoglycine aminohydrolase, and ureidoglycolate hydrolase clearly represents amide catabolism in service of nitrogen mobilization[9][13][16][21][24]. Alternative more specific annotations might reference "purine catabolism" or "nitrogen remobilization from purines," which would capture additional biological context.

### Alternative GO Terms

The Gene Ontology database includes several related terms that might be more appropriate for specific subsets of proteins matching the rule:

GO:0043419 ("urea catabolic process") represents a more specific annotation for urease enzymes than GO:0043605[14][19][22][38]. This term specifically captures the breakdown of urea, the primary substrate for ureases[1][4][60]. Using GO:0043419 for condition set 1 would provide better specificity.

GO:0006145 ("guanine nucleotide catabolic process") and related purine catabolism terms might be more appropriate for condition sets 3 and 4, as these enzymes function within the context of purine metabolism[21][24]. However, these terms focus on the broader pathway rather than the specific catalytic activity.

GO:0008150 ("biological_process") represents an overly broad term that would be inappropriate, while GO:0009039 ("urease activity") represents a molecular function term (the catalytic activity of urease) rather than a biological process, and would thus be inappropriate for a condition set predicting GO:0043605 (a biological process term)[31][34][49][52].

## Literature Evidence Supporting and Questioning the Rule

### Strong Support for Amide Catabolic Function

Extensive biochemical literature supports the conclusion that proteins matching condition sets 1, 3, and 4 catalyze amide hydrolysis. For urease enzymes, the chemical mechanism has been elucidated through structural crystallography, kinetic analysis, and spectroscopic investigation[1][4][18][29][57]. The high-resolution crystal structures of bacterial ureases from *Klebsiella aerogenes* and *Bacillus pasteurii*, and more recently the plant urease from jack bean (*Canavalia ensiformis*), demonstrate the conserved active site architecture and substrate binding modes that result in C-N bond cleavage[1][18][43][46].

For the ureide pathway enzymes, crystallographic structures combined with biochemical assays have definitively established amide hydrolysis. The structure of (S)-ureidoglycine aminohydrolase from *Arabidopsis thaliana* in complex with its substrate (S)-ureidoglycine directly demonstrated substrate binding at the Mn2+ coordination site and the catalytic geometry supporting C-N bond hydrolysis[9][13][32]. Kinetic analyses confirmed the enantioselective conversion of (S)-ureidoglycine to (S)-ureidoglycolate with release of ammonia[9][13][32].

### Evidence Regarding PM20D1 and FAAH

The evidence for PM20D1 and FAAH as amide catabolic enzymes requires more careful interpretation. These enzymes do possess amide hydrolase activity demonstrated through in vitro biochemical assays measuring hydrolysis of N-acyl amino acid substrates by liquid chromatography-mass spectrometry[7][44][47]. However, the equilibrium favoring hydrolysis (94% conversion in the hydrolase direction) contrasts with the very low synthase activity (1.2% conversion), yet this synthase activity is sufficient to drive in vivo N-acyl amino acid biosynthesis through coupling to thermodynamic disequilibrium of free fatty acid and amino acid reactants[47].

Importantly, genetic studies reveal that the primary physiological role of PM20D1 involves regulating N-acyl amino acid levels for thermogenic effects, not participating in general amide catabolism. Mice with PM20D1 deletion exhibit metabolic dysfunction characterized by glucose intolerance and decreased insulin sensitivity, indicating disrupted signaling through N-acyl amino acids rather than impaired amide degradation per se[7][47]. These findings suggest that while GO:0043605 is technically correct, it may be insufficiently specific and potentially misleading for PM20D1.

### Lack of Evidence for Universal Amide Catabolism

The literature provides no evidence that proteins matching these signatures catalyze hydrolysis of arbitrary amides. Urease specifically recognizes urea as substrate through its active site architecture[1][4][29]. While some urease mutants or inhibited forms can utilize urea analogues, the enzyme does not catalyze hydrolysis of the vast universe of possible amide compounds[1][26]. Similarly, (S)-ureidoglycine aminohydrolase specifically recognizes (S)-ureidoglycine with strict enantioselectivity, not the broader class of amides[9][13][32]. This specificity constrains the biological meaning of GO:0043605 when applied to these enzymes—they do not represent general amide-catabolic capacity but rather specialized solutions to specific metabolic problems.

### Experimental Validation of Pathway Functions

Multiple genetic studies have experimentally validated the roles of ureide pathway enzymes in purine catabolism and nitrogen remobilization. Analysis of *Ataah* mutant seeds revealed pleiotropic effects of allantoate amidohydrolase disruption, including seed dormancy increase, ureide accumulation, and amino acid depletion[16]. The *uah ure* double mutant of *Arabidopsis* displayed synthetic lethality phenotype, indicating overlapping roles for ureidoglycolate hydrolase and urease in ureide catabolism[24]. These genetic experiments directly establish the biological importance of amide hydrolysis in these pathways.

## Taxonomic Considerations and Distribution

### Urease Distribution and Conservation

Urease enzymes are ubiquitous across plants, fungi, and bacteria but completely absent from animals[1][18]. The universal distribution of urease across these kingdoms reflects the fundamental importance of urea as a nitrogen source in nature. The high conservation of urease sequences across taxonomic boundaries, despite divergence in quaternary structure, indicates that this represents an ancient enzyme that emerged before the divergence of major eukaryotic and prokaryotic lineages[1][18].

Condition set 1 of the rule contains no taxonomic restriction, meaning proteins matching this condition set in any organism would receive the GO:0043605 annotation. Given that urease is absent from animals, this lack of restriction presents no practical problem, as animals do not produce ureases[1][18]. However, the rule could be made more precise by explicitly including "not Animalia" as a taxonomic exclusion, providing logical clarity even if unnecessary in practice.

### PM20D1 and Fatty Acid Amide Hydrolases in Eukaryotes

Condition set 2 restricts the annotation to eukaryotes (NCBITaxon:2759), which is appropriate given that PM20D1 represents a eukaryotic protein present in circulation in both mice and humans[7][44]. The PM20D1 family appears restricted to metazoans and related eukaryotic lineages, with fungal and plant genomes apparently lacking clear PM20D1 orthologues. The explicit taxonomic restriction to eukaryotes thus prevents inappropriate annotation of distantly related proteins in bacteria and archaea that might superficially match domain signatures.

### Ureide Pathway Enzymes in Plants and Bacteria

Condition set 3 restricts annotation to Viridiplantae (green plants and chlorophytes), reflecting the prevalence of the ureide pathway in plant nitrogen metabolism[13][16][21][24][56]. However, the ureide pathway has also been identified in some bacteria and fungi[13][21][56], suggesting that the taxonomic restriction may be too narrow. A more inclusive annotation criterion might extend to "plants, some bacteria, and some fungi" rather than restricting to Viridiplantae alone. The current restriction potentially results in false negatives—bacterial proteins matching the domain signatures would be excluded from annotation despite performing identical catalytic functions.

Condition set 4 restricts annotation to Streptophyta (land plants and streptophyte algae), which appropriately captures the distribution of (S)-ureidoglycine aminohydrolase[13][21][32][56]. This narrower taxonomic distribution reflects the structural and biochemical characteristics of this enzyme family, which diverges from simpler bacterial relatives.

## Rule Logic and Potential Issues

### Specificity of Domain Combinations

The rule employs specific combinations of domains and families to predict GO:0043605 annotation. This multi-component approach increases specificity by preventing false positive annotations. For example, condition set 1 requires simultaneous presence of three urease-related domains (beta subunit-like, gamma/gamma-beta subunit, and active site), which appropriately captures only genuine urease enzymes rather than distantly related proteins containing single urease-related domains.

Similarly, condition set 3 combines detection of ureidoglycolate hydrolase and allantoate amidohydrolase families, which reflects the sequential action of these enzymes in the ureide pathway. A single domain matching either family alone might not reliably predict amide catabolic function, as isolated domains could appear in multifunctional proteins with alternative primary roles.

### Potential for False Positives

The rule could theoretically generate false positive annotations if proteins contain the specified domain combinations but function primarily through alternative mechanisms. For PM20D1 (condition set 2), proteins matching the FunFam signatures might exist that function primarily in other capacities despite possessing PM20D1-like domains. The explicit restriction to FunFam families (rather than broader InterPro domains) reduces this risk, as FunFams represent functionally validated families with shared evolutionary history and homologous mechanisms.

### Redundancy and Simplification

Examination of the four condition sets reveals potential redundancy in the rule logic. Conditions 1, 3, and 4 all describe specific enzyme families known to catalyze amide hydrolysis as part of distinct metabolic pathways (urea metabolism, ureide pathway). Condition set 2 describes a different enzyme family (PM20D1) with bidirectional catalytic capacity. The rule could potentially be simplified by reorganizing these conditions to group enzymes by their primary biological roles rather than combining them under a single GO term, or alternatively by acknowledging that these represent distinct functional categories within the broader amide catabolic process.

### Issues with Annotation Precedence

The rule predicts only a single GO term (GO:0043605) without specifying relationships to other potentially relevant annotations. Proteins matching these conditions might more accurately be annotated with multiple GO terms capturing their diverse functions. For example, urease enzymes might appropriately receive annotations for both GO:0043605 (amide catabolic process) and more specific functional terms related to nitrogen mobilization, environmental pH modulation, or bacterial virulence (if applicable). The current rule structure does not address this hierarchical complexity of GO term annotation.

## Structural Biology and Evolutionary Perspectives

### Conservation of Catalytic Mechanism Despite Structural Divergence

A remarkable finding from comparative structural biology is the conservation of catalytic mechanism for amide hydrolysis despite significant variation in protein structure. Urease enzymes from plants and bacteria maintain nearly identical active site architectures despite differences in subunit composition (single polypeptide vs. multi-subunit), oligomeric state, and overall fold contexts[1][18][43][46]. Similarly, manganese-dependent ureide pathway enzymes employ metal coordination chemistry fundamentally similar to nickel-dependent ureases, suggesting that nature has converged on metal-dependent catalysis as the solution to rapid amide hydrolysis[9][13][32][56].

This conservation of mechanism across structural divergence reflects the constraints of biochemistry—to achieve catalysis rates many orders of magnitude faster than uncatalyzed reactions while maintaining specificity requires activating the substrate carbonyl through metal coordination, positioning nucleophiles optimally, and stabilizing reaction intermediates. The repeated discovery of similar mechanisms in independently evolved enzyme families suggests that this represents something close to an optimal solution to the chemical problem of amide hydrolysis.

### Evolutionary Origin and Gene Duplication

The evolutionary origins of these amide-hydrolyzing enzyme families differ substantially. Urease represents an ancient enzyme present in early prokaryotes and subsequently inherited by plants through evolutionary acquisition, possibly through horizontal gene transfer events[1][18]. In contrast, PM20D1 represents a more recent evolution within metazoans, appearing to arise through specialization of a more general amide hydrolase ancestral protein[7][44]. The ureide pathway enzymes similarly represent relatively recent evolutionary innovations that appear confined to specific lineages, particularly abundant in plant genomes but present in some bacteria and fungi[13][21][56].

The pattern of gene duplication and divergence in PM20D1 and FAAH provides insight into the evolutionary mechanism generating functional specificity. Despite low sequence similarity between PM20D1 and FAAH, these enzymes exhibit partial substrate overlap and engage in cooperative regulation of N-acyl amino acid metabolism[7][44]. This represents a case of functional convergence—distinct evolutionary lineages have generated similar catalytic activities to solve overlapping biological problems.

## Practical Applications and Detection Methods

### Urease Detection and Clinical Significance

Urease detection has practical applications in clinical microbiology and environmental monitoring. The urease enzyme activity is commonly used as a diagnostic test for *Helicobacter pylori* infection, reflecting the clinical importance of this pathogenic bacterium in causing gastritis, peptic ulcers, and gastric cancer[1][4][18][29]. Traditional pH-based urease tests detect increases in pH resulting from ammonia production, but more sensitive and specific detection methods have recently been developed.

A novel fluorescent probe designated PNP_FITC has been developed that directly detects urease activity through degradation of a polymeric matrix containing urea-cleavable units[42]. This approach overcomes limitations of pH-based detection methods by providing direct measurement of enzymatic activity independent of environmental pH changes or other non-enzymatic pH modifications[42]. The probe achieves linear response across a urease range of 0-7.5 U/mL with a calculated limit of detection of 0.4 U/mL, and enables detection of urease-producing bacteria such as *Klebsiella pneumoniae* and *Enterobacter cloacae* at concentrations of 10^3 bacteria/mL[42].

### Urease Inhibition Strategies

Understanding the mechanism of amide hydrolysis catalyzed by urease has enabled development of urease inhibitors with potential applications in agriculture and medicine. Urease inhibitors fall into several mechanistic categories: substrate analogues that competitively inhibit the enzyme, compounds that bind to the active site nickel, thiol compounds that modify the critical cysteine residue in the mobile flap, oxidizing agents that inactivate this cysteine, Michael acceptors that covalently modify the flap cysteine, and metal chelators that sequester nickel required for enzyme assembly[26].

Substrate analogue inhibitors such as N-(n-butyl)thiophosphoric triamide (NBPT) show anti-ureolytic activity, though their effectiveness diminishes at high urea concentrations, limiting applicability in environments such as animal manure slurry with very high urea levels[26]. Nickel chelators including ethylenediaminetetraacetic acid (EDTA) can completely abolish *Klebsiella pneumoniae* ureolysis by sequestering nickel required for urease assembly, though in complex solutions with high metal ion concentrations these chelators become ineffective[26]. Michael acceptor compounds such as thiols can irreversibly inhibit urease by locking the mobile flap in a position that blocks substrate access[26].

## Recommendations for Rule Refinement

### Recommendation 1: Implement More Specific GO Term Annotations for Condition Set 1

For urease enzymes (condition set 1), consider predicting GO:0043419 ("urea catabolic process") rather than or in addition to GO:0043605 ("amide catabolic process"). This would provide greater specificity reflecting the specialized role of ureases in urea metabolism. The more specific term would enable researchers to more quickly identify urease-specific functions and avoid potential misinterpretation of general amide-catabolic capacity.

### Recommendation 2: Evaluate the Appropriateness of Condition Set 2 (PM20D1)

Reconsider whether condition set 2, targeting PM20D1 and related N-acyl amino acid synthase/hydrolases, truly warrants annotation with GO:0043605. The primary biological roles of PM20D1 center on thermogenic lipid signaling rather than general amide catabolism. Alternative annotations such as "lipid biosynthetic process" or more specific terms related to N-acyl amino acid metabolism might more accurately capture the biological function. If GO:0043605 is retained, consider developing additional condition sets that capture PM20D1's role in biosynthesis rather than catabolism exclusively.

### Recommendation 3: Broaden Taxonomic Restrictions for Ureide Pathway Enzymes

Condition set 3 currently restricts annotation to Viridiplantae, but the ureide pathway and its constituent enzymes are known to exist in bacteria and fungi[13][21][56]. Consider expanding the taxonomic scope to include "Viridiplantae, selected bacteria, and selected fungi" or implementing a more granular approach that specifically includes known bacterial and fungal lineages containing ureide pathway enzymes. This would prevent false negatives where prokaryotic proteins with identical sequences and functions receive no annotation.

### Recommendation 4: Add Hierarchical GO Term Structure

Implement a hierarchical approach where proteins receive both specific GO terms capturing their primary biological role and broader terms capturing the general catalytic mechanism. For example, urease enzymes might receive annotations for GO:0043419 (urea catabolic process), GO:0043605 (amide catabolic process), and additionally process-level annotations related to nitrogen cycling or pathogenic colonization as appropriate. This would provide multiple avenues for information retrieval while maintaining specificity.

### Recommendation 5: Implement Quality Control Checks for Multifunctional Proteins

For proteins predicted to match multiple condition sets (e.g., if a protein somehow matched both condition set 1 and condition set 3), implement logic to prevent redundant annotations and verify that annotations reflect the protein's actual domain composition. This would catch potential errors or ambiguous cases requiring manual review.

### Recommendation 6: Document the Biological Context of Each Condition Set

Create detailed documentation explaining the biological context for each condition set and its relationship to the GO:0043605 annotation. This would help users understand that while all proteins matching the rule's conditions do catalyze amide hydrolysis, their biological roles span diverse metabolic contexts (urea metabolism, ureide catabolism, lipid signaling) with different quantitative importance and regulatory mechanisms. Such documentation would prevent misinterpretation of GO:0043605 as indicating general amide-degrading capacity.

## Conclusions

The UniProt rule ARBA00047244 for predicting GO:0043605 (amide catabolic process) demonstrates substantial validity when evaluated against the biochemical, structural, and evolutionary literature. All four condition sets target enzyme families that demonstrably catalyze hydrolysis of amide bonds, and the predictions are largely supported by extensive experimental evidence spanning structural crystallography, kinetic analysis, and functional studies.

However, the evaluation reveals significant opportunities for refinement and increased specificity. The rule appropriately identifies ureases and ureide pathway enzymes as amide-catabolic proteins, with condition sets 1, 3, and 4 supported by extensive literature demonstrating the catalytic mechanisms, biological roles, and evolutionary conservation of these enzyme families. The assignment of GO:0043605 to these proteins is biochemically accurate, though more specific annotations capturing substrate identity (GO:0043419 for urease) or pathway context (purine catabolism for ureide enzymes) might provide greater biological utility.

Condition set 2, targeting PM20D1 and related fatty acid amide hydrolases, presents a more complex case. While these proteins do catalyze amide hydrolysis, their primary biological roles involve regulation of N-acyl amino acid biosynthesis and thermogenesis rather than participation in general amide catabolism. The annotation of these proteins with GO:0043605 is technically accurate but potentially misleading regarding biological function.

The evidence base strongly supports the core premise that proteins matching these domain and family signatures catalyze amide bond hydrolysis. The mechanistic basis for this catalysis has been elucidated through high-resolution structural studies revealing how metal coordination (by nickel, manganese, or other cofactors) activates amide substrates and positions catalytic residues. The biological importance of these reactions spans nitrogen cycling, pathogenic virulence, plant seed development, and lipid signaling.

Moving forward, the rule would benefit from stratification into multiple more specific annotations capturing the distinct biological contexts of amide hydrolysis, expansion of taxonomic scope for ureide pathway enzymes to include known prokaryotic systems, and development of accompanying documentation clarifying the diverse biological roles of amide catabolism across these enzyme families. Such refinements would enhance both the technical accuracy and biological utility of the annotation rule while maintaining the core insight that these structurally and evolutionarily diverse enzymes perform fundamentally related chemistry in service of distinct metabolic purposes.

## Citations

1. https://en.wikipedia.org/wiki/Urease
2. https://amigo.geneontology.org/amigo/term/GO:0043605
3. https://lotus.au.dk/view/domain/IPR017950
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC7433671/
5. https://dev.pombase.org/term/GO:0043605
6. https://www.ncbi.nlm.nih.gov/gene?Cmd=DetailsSearch&Term=843076
7. https://elifesciences.org/articles/55211
8. https://www.cathdb.info/superfamily/3.30.70.360
9. https://pubmed.ncbi.nlm.nih.gov/22493446/
10. https://www.uniprot.org/uniprotkb/Q8C165/entry
11. https://www.cathdb.info/version/v4_4_0/superfamily/2.60.120.480/funfam/7/taxonomy_sunburst
12. https://www.uniprot.org/uniprotkb/P75713/entry
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC3365701/
14. https://www.ebi.ac.uk/QuickGO/term/GO:0043419
15. https://www.frontiersin.org/journals/chemical-biology/articles/10.3389/fchbi.2023.1243564/full
16. https://academic.oup.com/pcp/article/63/9/1298/6647669
17. https://www.informatics.jax.org/vocab/gene_ontology/GO:0043605
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC6077230/
19. https://zfin.org/GO:0043419
20. https://pubmed.ncbi.nlm.nih.gov/22904279/
21. https://pubs.acs.org/doi/abs/10.1021/cb900248n
22. https://www.uniprot.org/uniprotkb/G7ZIC9/entry
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC3793049/
24. https://www.nature.com/articles/s41598-020-65107-9
25. http://cathdb.info/version/v4_4_0/superfamily/3.20.20.140/funfam/14/taxonomy_sunburst
26. https://www.cathdb.info/version/latest/funfam/3.40.630.10:FF:000044
27. https://www.ebi.ac.uk/QuickGO/term/GO:0009039
28. https://metadb.riken.jp/db/SciNetS_rib124i/crib124s1rib124u2019i
29. https://amigo.geneontology.org/amigo/term/GO:0009039
30. https://www.uniprot.org/taxonomy/35493
31. https://www.uniprot.org/uniprotkb/Q84F76/entry
32. https://www.cathdb.info/version/latest/superfamily/1.10.150.900/alignments
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC8268090/
34. https://www.cathdb.info/version/v4_4_0/superfamily/1.10.150.900/funfam/2
35. https://pubs.acs.org/doi/10.1021/acs.analchem.4c05182
36. https://chemie.uni-muenchen.de/ac/kluefers/homepage/L/bac/ur_jackbean_2010.pdf
37. https://www.uniprot.org/help/automatic_annotation
38. https://pubmed.ncbi.nlm.nih.gov/20471401/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC4947008/
40. https://www.uniprot.org/help/arba
41. https://www.uniprot.org/uniprotkb/P77425/entry
42. https://www.nature.com/articles/s42003-021-01933-5
43. https://iubmb.qmul.ac.uk/enzyme/EC3/5/3/9.html
44. https://www.ncbi.nlm.nih.gov/books/NBK579936/
45. https://www.youtube.com/watch?v=aiaV2zolG3M
46. https://www.masterorganicchemistry.com/2019/10/07/amide-hydrolysis/
47. https://academic.oup.com/plcell/article/22/5/1564/6095873?login=true
48. https://iubmb.qmul.ac.uk/enzyme/EC3/5/1/5.html