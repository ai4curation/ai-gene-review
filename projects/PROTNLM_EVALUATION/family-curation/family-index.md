---
title: "ProtNLM benchmark family assessments"
autolink_gene_symbols: false
---

# Family assessments

[Overview](../family-curation.md) · [Gene index](gene-index.md)

An unresolved family grant can coexist with strong evidence for a particular member. Listed subfamilies and representatives are a scoped set, not an exhaustive phylogeny.

## PTHR10102

**DNA-DIRECTED RNA POLYMERASE, MITOCHONDRIAL** — MOSTLY_COHERENT; COMPLETE

Phage-type RNA polymerases are single-chain enzymes that synthesize RNA from DNA templates. Mitochondrial members combine the conserved polymerase core with lineage-specific targeting and transcription-factor interactions.

Purified pombe Rpo41 and Mtf1 transcribe mitochondrial promoters in vitro (PMID:21357609). The family inventory also includes phage enzymes and plant chloroplastic or dual-targeted polymerases. DNA-directed RNA synthesis is the conserved reaction, while mitochondrial localization and dependence on a particular initiation factor are lineage-specific properties of the transcription system.

**Exact benchmark/reference members:** SCHPO/rpo41 (O13993)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-directed RNA polymerase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003899) (GO:0003899) | FAMILY_WIDE | The conserved function represented by DNA-directed RNA polymerase activity is the family core for intact members. DNA-dependent RNA synthesis is the conserved biochemical role; mitochondrial residence and dependence on a particular initiation factor are not properties of every phage-type polymerase. For Rpo41, distinguish the polymerase reaction from mitochondrial promoter recognition by the holoenzyme. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10102/PTHR10102-review.yaml)

## PTHR10131

**TNF RECEPTOR ASSOCIATED FACTOR** — HETEROGENEOUS; COMPLETE

TRAF proteins organize receptor-associated signaling assemblies through conserved interaction domains and variable amino-terminal regions. Their roles include recruiting ubiquitin-system components and controlling inflammatory and survival pathways.

TRAF2 recruits cIAP proteins through its coiled-coil region, as shown by reconstitution, structure and binding-site mutagenesis (PMID:20447407). This directly supports signaling adaptor activity independently of whether TRAF2 has intrinsic E3 ligase activity. The PANTHER grouping also includes plant and other divergent TRAF-type proteins whose receptor partners and adaptor mechanism are not defined by the TRAF2 experiment. The exhaustive signaling-adaptor grant boundary remains unresolved; RING-dependent ubiquitination is a separate assessment.

**Exact benchmark/reference members:** HORSE/TRAF2 (F7BIV4), human/TRAF2 (Q12933)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [signaling adaptor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0035591) (GO:0035591) | UNRESOLVED | TRAF2 recruits cIAP proteins through its coiled-coil region, as shown by reconstitution, structure and binding-site mutagenesis (PMID:20447407). This directly supports signaling adaptor activity independently of whether TRAF2 has intrinsic E3 ligase activity. The PANTHER grouping also includes plant and other divergent TRAF-type proteins whose receptor partners and adaptor mechanism are not defined by the TRAF2 experiment. The exhaustive signaling-adaptor grant boundary remains unresolved; RING-dependent ubiquitination is a separate assessment. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10131/PTHR10131-review.yaml)

## PTHR10139

**DOUBLE-STRAND BREAK REPAIR PROTEIN MRE11** — MOSTLY_COHERENT; COMPLETE

Mre11/Rad32 proteins are DNA-end-processing nucleases that cooperate with Rad50-containing complexes in DNA repair. Their conserved nuclease functions are coupled to DNA-end recognition and organism-specific checkpoint and meiotic programs.

Purified Mre11 and human MRN experiments establish both endonuclease and 3-prime-to-5-prime exonuclease activities (PMID:9651580; PMID:9705271). Pombe structures establish the Mre11-Nbs1 interface, and pombe genetics demonstrate nuclease-dependent Rec12 removal (PMID:22705791; PMID:19139281). These support a conserved DNA-end-processing nuclease while separating catalytic chemistry from organism-specific checkpoint and meiotic outcomes.

**Exact benchmark/reference members:** SCHPO/mre11 (Q09683)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA endonuclease activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004520) (GO:0004520) | FAMILY_WIDE | The conserved function represented by DNA endonuclease activity is the family core for intact members. Nuclease chemistry and DNA-end processing provide a defensible core, while repair-pathway usage, checkpoint outputs and meiotic phenotypes require the relevant organism and complex context. Exonuclease directionality and endonuclease activity must remain separate claims. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10139/PTHR10139-review.yaml)

## PTHR10177

**CYCLINS** — HETEROGENEOUS; COMPLETE

Cyclins are regulatory proteins that control cyclin-dependent kinases. Different cyclin groups specify cell-cycle transitions and other transcriptional or regulatory programs through distinct partners and expression patterns.

Fly CycA contributes to mitotic cell-cycle progression and cyclin-mediated CDK substrate recognition (PMID:2564316; PMID:17431409). The native CycA-PC sequence differs from the reviewed 491-residue form by only Gln66 and retains the entire cyclin domain, supporting kinase regulation for this isoform. The broader family includes cyclins with distinct partners and regulatory outputs; kinase regulation is not intrinsic kinase catalysis. The complete set with direct CDK-regulator activity is unresolved beyond these positively supported branches.

**Exact benchmark/reference members:** DROME/CycA (M9NFR3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [cyclin-dependent protein serine/threonine kinase regulator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016538) (GO:0016538) | UNRESOLVED | Fly CycA contributes to mitotic cell-cycle progression and cyclin-mediated CDK substrate recognition (PMID:2564316; PMID:17431409). The native CycA-PC sequence differs from the reviewed 491-residue form by only Gln66 and retains the entire cyclin domain, supporting kinase regulation for this isoform. The broader family includes cyclins with distinct partners and regulatory outputs; kinase regulation is not intrinsic kinase catalysis. The complete set with direct CDK-regulator activity is unresolved beyond these positively supported branches. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10177/PTHR10177-review.yaml)

## PTHR10194

**Ras and Rap GTPase-activating proteins** — MOSTLY_COHERENT; COMPLETE

RasGAP-related proteins accelerate GTP hydrolysis by small GTPases rather than hydrolyzing free GTP as the principal catalyst themselves. Ras versus Rap preference and regulatory localization vary across the group.

The mosquito target carries a RasGAP domain and conserved-site signature. General GTPase-activator activity is mechanistically consistent, while a specific GTPase substrate or signaling pathway needs branch-specific evidence. A conserved domain does not dispense with checking the catalytic interface in divergent members.

**Exact benchmark/reference members:** AEDAE/A0A6I8TLE4 (A0A6I8TLE4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [GTPase activator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0005096) (GO:0005096) | UNRESOLVED | Neurofibromin and p120GAP mutagenesis directly establish Ras GTPase activation through a catalytic interface that positions the arginine-finger region. The mosquito RasGAP domain and conserved-site signature support a comparable GAP mechanism. Ras versus Rap preference and inactive interface variants require branch-specific analysis; the complete functional set is not restricted to the benchmark Raskol subfamily. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10194/PTHR10194-review.yaml)

## PTHR10196

**SUGAR KINASE** — HETEROGENEOUS; COMPLETE

FGGY-family carbohydrate kinases contain paired domains that support ATP-dependent phosphorylation of carbohydrate substrates. Members differ in the small molecules they recognize and the metabolic pathways they serve.

The inventory spans glycerol, xylulose, rhamnulose, ribulose and sedoheptulose kinases. NCU06005 has a specific glycerol-kinase signature and SF69 assignment, providing stronger substrate inference than the generic FGGY fold. The classical Neurospora study maps cytosolic glycerokinase genetically to glp-4 (PMID:6284716); without a verified molecular bridge to NCU06005 it is organism-level enzymatic context, not a direct assay of this accession.

**Exact benchmark/reference members:** NEUCR/NCU06005 (Q7S2F2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [glycerol kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004370) (GO:0004370) | UNRESOLVED | The inventory spans glycerol, xylulose, rhamnulose, ribulose and sedoheptulose kinases. NCU06005 has a specific glycerol-kinase signature and SF69 assignment, providing stronger substrate inference than the generic FGGY fold. The classical Neurospora study maps cytosolic glycerokinase genetically to glp-4 (PMID:6284716); without a verified molecular bridge to NCU06005 it is organism-level enzymatic context, not a direct assay of this accession. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10196/PTHR10196-review.yaml)

## PTHR10283

**SOLUTE CARRIER FAMILY 13 MEMBER** — HETEROGENEOUS; COMPLETE

This transporter family includes membrane proteins with citrate-transporter-like architecture and diverse solute preferences. Fungal SPX-containing members connect transport with phosphate homeostasis.

The inventory includes sodium-dependent organic-acid transporters and fungal Pho87/90/91 phosphate-related proteins. NCU01540 has an SF92 Pho91 assignment and SPX/transporter architecture. Budding-yeast Pho91 localization and polyphosphate phenotypes support vacuolar phosphate mobilization (PMID:17804816), but that study presents export direction as a mechanistic hypothesis rather than a direct flux measurement. Citrate specificity and plasma-membrane import cannot be transferred to this branch.

**Exact benchmark/reference members:** NEUCR/NCU01540 (Q7RWZ3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [phosphate transmembrane transporter activity](https://www.ebi.ac.uk/QuickGO/term/GO:0005315) (GO:0005315) | UNRESOLVED | The inventory includes sodium-dependent organic-acid transporters and fungal Pho87/90/91 phosphate-related proteins. NCU01540 has an SF92 Pho91 assignment and SPX/transporter architecture. Budding-yeast Pho91 localization and polyphosphate phenotypes support vacuolar phosphate mobilization (PMID:17804816), but that study presents export direction as a mechanistic hypothesis rather than a direct flux measurement. Citrate specificity and plasma-membrane import cannot be transferred to this branch. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10283/PTHR10283-review.yaml)

## PTHR10380

**CUTICLE PROTEIN** — MOSTLY_COHERENT; COMPLETE

Arthropod cuticle proteins contribute to extracellular cuticular structures, with sequence groups associated with different tissues and developmental stages. Rebers-Riddiford chitin-binding signatures characterize the cuticle-protein branch represented by Drosophila Lcp3.

The exact Lcp3 polypeptide is identical to the reviewed larval cuticle protein, supporting its larval-cuticle role. Related structural cuticle proteins are also directly isolated from pupal cuticle, with stage-dependent expression (PMID:12609518). Thus the broad cuticle structural role is coherent but a specifically larval term cannot be granted universally. Chitin-binding signatures alone do not resolve developmental stage or tissue-specific incorporation.

**Exact benchmark/reference members:** DROME/Lcp3 (A0A0B4KEF3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [structural constituent of chitin-based larval cuticle](https://www.ebi.ac.uk/QuickGO/term/GO:0008010) (GO:0008010) | UNRESOLVED | The exact Lcp3 polypeptide is identical to the reviewed larval cuticle protein, supporting its larval-cuticle role. Related structural cuticle proteins are also directly isolated from pupal cuticle, with stage-dependent expression (PMID:12609518). Thus the broad cuticle structural role is coherent but a specifically larval term cannot be granted universally. Chitin-binding signatures alone do not resolve developmental stage or tissue-specific incorporation. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10380/PTHR10380-review.yaml)

## PTHR10383

**SERINE INCORPORATOR** — HETEROGENEOUS; COMPLETE

SERINC/Tms proteins are multipass membrane proteins associated with membrane-lipid organization. Mammalian SERINC3 and SERINC5 have experimentally characterized lipid-scrambling and antiviral functions, while other members are less specifically characterized.

Purified human SERINC proteins flip phospholipids in reconstituted membranes (PMID:37474505). Experiments manipulating viral phosphatidylserine exposure separate that activity from the mechanism of HIV restriction (PMID:38785977). The fly M9PCT1 record has the SERINC domain and SF9 assignment, but neither a direct lipid assay nor a fly antiviral mechanism follows from the mammalian experiments. Serine incorporation is not an established intrinsic biosynthetic reaction.

**Exact benchmark/reference members:** DROME/Serinc (M9PCT1)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10383/PTHR10383-review.yaml)

## PTHR10410

**EUKARYOTIC TRANSLATION INITIATION FACTOR 3 -RELATED** — HETEROGENEOUS; COMPLETE

JAMM/MPN-family proteins occur in protein-modification and proteostasis complexes. Catalytic members use metal-dependent hydrolysis, but modifier specificity and activity depend on the protein and its complex context.

The exact fly CSN5 PB isoform retains the complete MPN domain and JAMM catalytic region despite two deletions outside that domain. This supports a COP9 component with NEDD8-deconjugation architecture, not synaptic-vesicle residence. A developmental or synaptic phenotype is not a localization assay. The broader grouping contains proteasomal, COP9 and translation-associated MPN proteins with different complexes, so synaptic vesicle is not a shared compartment and no exhaustive positive subfamily set is established.

**Exact benchmark/reference members:** DROME/CSN5 (A0A0B4KHM2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [synaptic vesicle](https://www.ebi.ac.uk/QuickGO/term/GO:0008021) (GO:0008021) | UNRESOLVED | The exact fly CSN5 PB isoform retains the complete MPN domain and JAMM catalytic region despite two deletions outside that domain. This supports a COP9 component with NEDD8-deconjugation architecture, not synaptic-vesicle residence. A developmental or synaptic phenotype is not a localization assay. The broader grouping contains proteasomal, COP9 and translation-associated MPN proteins with different complexes, so synaptic vesicle is not a shared compartment and no exhaustive positive subfamily set is established. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10410/PTHR10410-review.yaml)

## PTHR10414

**ETHANOLAMINEPHOSPHOTRANSFERASE** — HETEROGENEOUS; COMPLETE

Choline/ethanolamine phosphotransferases use activated CDP-aminoalcohol donors to synthesize membrane phospholipids. The family contains choline-selective enzymes, ethanolamine-selective enzymes and dual-specificity CEPT enzymes. Donor specificity and the lipid acceptor define the reaction more precisely than the shared membrane phosphotransferase fold.

The family spans phosphobase-transfer enzymes with different donor specificity, including CHPT1, SELENOI/EPT1 and dual-specificity CEPT1 branches. Human CEPT1 catalyzes phosphatidylcholine and phosphatidylethanolamine synthesis using CDP-choline or CDP-ethanolamine and diacylglycerol; mixed-micelle assays also resolve acceptor-lipid preferences (PMID:12216837). Thus phosphatidylethanolamine synthesis is supported for characterized ethanolamine-accepting branches, but not for every choline-preferring relative. The fly CG33116 assignment alone does not establish donor specificity or a ceramide rather than diacylglycerol acceptor.

**Exact benchmark/reference members:** DROME/CG33116 (Q9VIU4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ethanolaminephosphotransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004307) (GO:0004307) | UNRESOLVED | The family spans phosphobase-transfer enzymes with different donor specificity, including CHPT1, SELENOI/EPT1 and dual-specificity CEPT1 branches. Human CEPT1 catalyzes phosphatidylcholine and phosphatidylethanolamine synthesis using CDP-choline or CDP-ethanolamine and diacylglycerol; mixed-micelle assays also resolve acceptor-lipid preferences (PMID:12216837). Thus phosphatidylethanolamine synthesis is supported for characterized ethanolamine-accepting branches, but not for every choline-preferring relative. The fly CG33116 assignment alone does not establish donor specificity or a ceramide rather than diacylglycerol acceptor. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10414/PTHR10414-review.yaml)

## PTHR10472

**D-TYROSYL-TRNA TYR  DEACYLASE** — MOSTLY_COHERENT; COMPLETE

DTD-family enzymes remove inappropriate amino acids from aminoacyl-tRNAs, providing a trans-editing checkpoint during translation. The characterized DTD mechanism rejects L-chiral amino acids and can also act on glycine-charged tRNAs; tRNA identity helps distinguish productive proofreading from misediting. The historical D-tyrosyl name is narrower than the established substrate class.

Direct DTD structural and biochemical studies establish an invariant cross-subunit Gly-cisPro substrate-selection mechanism. Human DUE-B/DTD1 has an enzymatically active N-terminal core and a separable C-terminal DNA-binding contribution. The selected 127-residue product ends before the human reference Gly139-Pro140 motif, so DTD1 family identity does not establish a complete editing site in that product.

**Exact benchmark/reference members:** human/DTD1 (A0A2R8YCT7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003677) (GO:0003677) | UNRESOLVED | Human DUE-B has a C-terminal DNA-binding contribution demonstrated experimentally, but that function is not established for all DTD proteins. The benchmark product ends before the relevant C-terminal portion, and its DNA binding is not established. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10472/PTHR10472-review.yaml)

## PTHR10489

**CELL ADHESION MOLECULE** — HETEROGENEOUS; COMPLETE

This chemokine-receptor family includes receptors with different chemokine specificities and signaling outputs. CXCR3 recognizes C-X-C chemokines, but other branches recognize C-C or XC ligands, and atypical receptors handle chemokines without the same canonical signaling response. Even CXCR3 splice isoforms can differ in their effects on cell migration and proliferation.

Human CXCR3 experiments cited in the reviewed UniProt record support CXCL9/CXCL10/CXCL11 responsiveness and distinguish isoform-dependent responses. These findings do not justify C-X-C receptor specificity across the CCR and atypical-receptor branches. Horse transfer should retain orthology and isoform constraints.

**Exact benchmark/reference members:** HORSE/CXCR3 (A0A9L0T1D1), human/CXCR3 (P49682)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [C-X-C chemokine receptor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016494) (GO:0016494) | UNRESOLVED | C-X-C chemokine receptor activity is directly supported for CXCR3 by the cited ligand-response studies, but it is not exclusive to the CXCR3 subfamily: the broader family also contains CXCR1, CXCR2, CXCR4, CXCR5 and CXCR6 branches. CCR and atypical-receptor groups must be distinguished by ligand and signaling mechanism. The available CXCR3 representatives do not establish an exhaustive allowed-subfamily set, so family-wide applicability remains unresolved without denying the characterized CXCR3 activity. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10489/PTHR10489-review.yaml)

## PTHR10553

**SMALL NUCLEAR RIBONUCLEOPROTEIN** — HETEROGENEOUS; COMPLETE

SmG/Lsm7-family proteins are small RNA-associated subunits of heptameric ribonucleoprotein rings. SmG participates in the canonical Sm ring of several spliceosomal snRNPs. Lsm7 instead participates in Lsm complexes, including the U6-associated ring and the cytoplasmic mRNA-decapping ring.

Curated IPR044641 distinguishes the canonical Sm ring from nuclear Lsm2-8 and cytoplasmic Lsm1-7 rings. The inventory contains both SmG and Lsm7; NCU09880 maps to the SmG branch. RNA association is conserved, whereas decapping and U6-specific membership cannot be assigned to all SmG/Lsm7 relatives.

**Exact benchmark/reference members:** NEUCR/NCU09880 (Q7S234)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [RNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003723) (GO:0003723) | FAMILY_WIDE | The distinction between SmG and Lsm7 is explicit in IPR044641 and in the family subfamily names. RNA association is conserved, but U1/U2/U4/U5 complex membership cannot be transferred to Lsm7, nor can cytoplasmic decapping be made a universal SmG function. NCU09880 maps to a SmG subfamily. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10553/PTHR10553-review.yaml)

## PTHR10589

**UBIQUITIN CARBOXYL-TERMINAL HYDROLASE** — MOSTLY_COHERENT; COMPLETE

UCH-family cysteine proteases hydrolyze bonds at the ubiquitin C terminus. Their conserved catalytic framework serves different biological settings: small-conjugate processing, proteasome-associated deubiquitination and chromatin-associated deubiquitination. Regulatory extensions and partner complexes help determine substrate access.

The inventory separates small UCH enzymes, UCH37/UCHL5 and BAP1/Calypso chromatin deubiquitinases. The pombe Uch2 evidence supports cleavage at the ubiquitin C terminus and its UCHL5 branch assignment. Partner-dependent substrate access distinguishes proteasome and chromatin contexts; activity on one small ubiquitin conjugate does not establish every linkage specificity or NEDD8 processing.

**Exact benchmark/reference members:** SCHPO/uch2 (Q9UUB6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [cysteine-type deubiquitinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004843) (GO:0004843) | FAMILY_WIDE | IPR001578 describes the C12 catalytic family; the experimentally supported pombe Uch2 record identifies a ubiquitin-protein hydrolase. Uch2/UCH37 proteasome association is a branch property, whereas BAP1 and small UCH enzymes have different contexts. NEDD8 processing observed for particular UCH enzymes is not sufficient to grant deneddylation family-wide. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10589/PTHR10589-review.yaml)

## PTHR10623

**MICROTUBULE-ASSOCIATED PROTEIN RP/EB FAMILY MEMBER** — HETEROGENEOUS; COMPLETE

RP/EB-related proteins use a calponin-homology region to associate with microtubules. Canonical end-binding proteins organize growing microtubule ends and recruit partner proteins, while specialized members can connect stable microtubule bundles to other cellular structures. The fly Mst27D example links nuclear pores to bundled microtubules during sperm nuclear elongation.

Mst27D binds microtubules through its N-terminal calponin-homology domain and Nup358 through its C terminus, linking nuclear pores to microtubule bundles during sperm nuclear elongation (PMID:37428798). This specialized linkage does not establish canonical growing-plus-end tracking. Even canonical EB paralogs differ in catastrophe suppression, and their effects in vitro differ from those in cells (PMID:19255245). Microtubule association is better conserved than a uniform plus-end or dynamic-instability function; no exhaustive subfamily boundary for GO:0051010 is established.

**Exact benchmark/reference members:** DROME/Mst27D (Q8IPI4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [microtubule plus-end binding](https://www.ebi.ac.uk/QuickGO/term/GO:0051010) (GO:0051010) | UNRESOLVED | Mst27D binds microtubules through its N-terminal calponin-homology domain and Nup358 through its C terminus, linking nuclear pores to microtubule bundles during sperm nuclear elongation (PMID:37428798). This specialized linkage does not establish canonical growing-plus-end tracking. Even canonical EB paralogs differ in catastrophe suppression, and their effects in vitro differ from those in cells (PMID:19255245). Microtubule association is better conserved than a uniform plus-end or dynamic-instability function; no exhaustive subfamily boundary for GO:0051010 is established. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10623/PTHR10623-review.yaml)

## PTHR10638

**COPPER AMINE OXIDASE** — HETEROGENEOUS; COMPLETE

Copper amine oxidases oxidatively deaminate primary amines, producing an aldehyde, ammonia and hydrogen peroxide through copper/topaquinone-dependent chemistry. Family members differ in their preferred monoamine, diamine or polyamine substrates and in whether they act intracellularly, at membranes or extracellularly.

Pombe Cao1 has primary experimental support for copper-dependent oxidative deamination of primary amines. Heterologous budding-yeast assays support ethylamine utilization; native copper-loading experiments identify Atx1 as a copper source, and microscopy directly places Cao1 in meiotic forespores. These observations do not establish mammalian histamine clearance, vascular adhesion or identical substrate preferences across the family.

**Exact benchmark/reference members:** SCHPO/cao1 (Q9P7F2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [amine catabolic process](https://www.ebi.ac.uk/QuickGO/term/GO:0009310) (GO:0009310) | UNRESOLVED | Cao1 directly oxidizes primary amines and supports their utilization in the tested system. Family members differ in substrate spectrum, cellular location and physiological role, so neither a particular amine substrate nor every downstream physiological process is family-wide. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10638/PTHR10638-review.yaml)

## PTHR10648

**PP2A/PP4 regulatory scaffold proteins** — HETEROGENEOUS; COMPLETE

HEAT-repeat regulatory scaffolds organize phosphatase complexes. PP2A A subunits assemble catalytic and regulatory partners; the retrieved family also includes PP4 regulatory proteins. Scaffold binding is distinct from catalytic dephosphorylation.

PP2A holoenzyme assembly supports heteromeric protein association for the wheat target. Neuronal locations cannot be transferred into wheat, although they may describe animal family members. Centromeric and chromosome-segregation roles require the relevant complex and organism; antigen binding is not implied by a viral protein binding a phosphatase scaffold.

**Exact benchmark/reference members:** WHEAT/F6LAX4 (F6LAX4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein heterodimerization activity](https://www.ebi.ac.uk/QuickGO/term/GO:0046982) (GO:0046982) | UNRESOLVED | PP2A structures directly establish a scaffold-catalytic-subunit heterodimer, and both alpha and beta A-subunit branches have that association role. The wider family includes PP4 regulatory proteins and distinct assemblies. Protein association is supported beyond the wheat exemplar, but a complete set of branches satisfying the particular heterodimerization relation has not been delimited. |
| [neuronal cell body](https://www.ebi.ac.uk/QuickGO/term/GO:0043025) (GO:0043025) | UNRESOLVED | Neuronal cell-body localization can apply to animal phosphatase scaffolds expressed in neurons, but wheat has no neuronal cell body. The conserved PP2A assembly interface does not establish this tissue-specific location. The animal branches with localization evidence need separate delimitation from the plant and fungal members. |
| [chromosome segregation](https://www.ebi.ac.uk/QuickGO/term/GO:0007059) (GO:0007059) | UNRESOLVED | PP2A and PP4 complexes can regulate chromosome segregation through different substrates and targeting partners. The holoenzyme structures establish assembly, not chromosome-segregation involvement of every scaffold in every tissue. A partner- and branch-resolved physiological assignment is required. |
| [neuron projection](https://www.ebi.ac.uk/QuickGO/term/GO:0043005) (GO:0043005) | UNRESOLVED | Neuron projections are animal cellular structures and cannot be transferred to the wheat member. A phosphatase scaffold may be recruited to them by neuronal partners, but that recruitment is separate from conserved holoenzyme assembly. No exhaustive set of projection-localized family branches is established. |
| [chromosome, centromeric region](https://www.ebi.ac.uk/QuickGO/term/GO:0000775) (GO:0000775) | UNRESOLVED | Centromeric localization requires the appropriate chromosome-targeting complex; it is not entailed by being the PP2A A scaffold. The available structural evidence identifies subunit interfaces without establishing centromere residence for the wheat protein or all PP4-related members. Specific localization and partner evidence are needed. |
| [protein antigen binding](https://www.ebi.ac.uk/QuickGO/term/GO:1990405) (GO:1990405) | UNRESOLVED | SV40 small t antigen directly binds PP2A A subunit, but that interaction does not by itself establish immune antigen-recognition activity. The substrate name antigen must not be used as the functional definition of protein antigen binding. No family-wide antigen-recognition mechanism is supported, while the ordinary viral-protein/scaffold interaction remains valid. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10648/PTHR10648-review.yaml)

## PTHR10680

**Peptide-amidation PHM/PAL proteins** — HETEROGENEOUS; COMPLETE

Peptide amidation proceeds through monooxygenase and lyase reactions, carried in separate proteins or combined in bifunctional PAM. Copper/ascorbate-dependent monooxygenase chemistry and PAL lyase chemistry reside in different structural modules.

The quail target contains both monooxygenase and PAL-associated architecture. PAL activity and ascorbate interaction must be assigned to their respective modules, not inferred from the other reaction. The retrieved family includes separate PHM and PAL proteins and therefore neither module-specific activity is universal.

**Exact benchmark/reference members:** COTJA/A0A8C2TBA7 (A0A8C2TBA7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [peptidylamidoglycolate lyase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004598) (GO:0004598) | UNRESOLVED | PAL structural and mutagenesis data establish the lyase reaction in a zinc-containing beta-propeller module. Bifunctional PAM and separate PAL proteins can retain this module, whereas PHM-only proteins cannot inherit the lyase activity from their monooxygenase domain. The complete set of PAL-bearing functional branches, including shortened products, is not delimited. |
| [L-ascorbic acid binding](https://www.ebi.ac.uk/QuickGO/term/GO:0031418) (GO:0031418) | UNRESOLVED | PHM kinetic experiments establish interaction with ascorbate during reduction and activation. That evidence belongs to the copper monooxygenase module, not to the PAL lyase module. Bifunctional PAM can combine both functions, but the full set of ascorbate-interacting PHM-bearing branches is not established by the quail exemplar. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10680/PTHR10680-review.yaml)

## PTHR10724

**S1-domain RNA-binding proteins** — HETEROGENEOUS; COMPLETE

This group contains bacterial ribosomal S1 proteins alongside S1-domain proteins such as Tex and other RNA-associated proteins. RNA-binding architecture is shared more broadly than incorporation into a ribosomal subunit.

The Deinococcus protein has repeated S1 domains and bS1 placement, supporting mRNA binding and ribosomal participation. A ribosome term cannot be extended to every S1-domain protein, and the presence of an S1 fold alone does not identify the RNA substrate.

**Exact benchmark/reference members:** DEIRA/Q9RSY6 (Q9RSY6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [nucleic acid binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003676) (GO:0003676) | UNRESOLVED | Purified E. coli S1 binds poly(A) and poly(C), directly establishing nucleic-acid binding in the ribosomal S1 branch. The repeated S1 domains in the Deinococcus target support that RNA-binding comparison. Other S1-domain proteins recognize different RNA substrates; the complete distribution of experimentally competent binding modules is not delimited. |
| [ribosome](https://www.ebi.ac.uk/QuickGO/term/GO:0005840) (GO:0005840) | UNRESOLVED | Ribosomal S1 is directly identified as a 30S subunit protein in the cited biochemical study. This supports ribosome membership for bS1 orthologs, while Tex and other S1-domain-containing proteins need not be ribosomal constituents. The S1 fold cannot define an exhaustive ribosome-member boundary across this broader family. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10724/PTHR10724-review.yaml)

## PTHR10746

**50S RIBOSOMAL PROTEIN L4** — MOSTLY_COHERENT; COMPLETE

uL4-family proteins are structural components of the large ribosomal subunit. Bacterial and organellar homologues share the ribosome-associated role, but the cellular location and translation system depend on lineage and targeting. Pombe Yml6 belongs to the mitochondrial uL4 group.

The inventory overwhelmingly identifies uL4 proteins but also assigns the Xenopus magainin precursor P11006 to SF6. Its reviewed sequence and processing record describe repeated secreted antimicrobial peptides, not a ribosomal uL4 protein. This is an apparent classification outlier, not evidence that ribosomal uL4 evolved an antimicrobial precursor function. Yml6 remains a supported uL4m member, but an unconditional grant to every catalogued sequence is unsafe.

**Exact benchmark/reference members:** SCHPO/yml6 (O74801)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [structural constituent of ribosome](https://www.ebi.ac.uk/QuickGO/term/GO:0003735) (GO:0003735) | UNRESOLVED | The inventory overwhelmingly identifies uL4 proteins but also assigns the Xenopus magainin precursor P11006 to SF6. Its reviewed sequence and processing record describe repeated secreted antimicrobial peptides, not a ribosomal uL4 protein. This is an apparent classification outlier, not evidence that ribosomal uL4 evolved an antimicrobial precursor function. Yml6 remains a supported uL4m member, but an unconditional grant to every catalogued sequence is unsafe. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10746/PTHR10746-review.yaml)

## PTHR10807

**Active and inactive myotubularins** — HETEROGENEOUS; COMPLETE

Myotubularins include phosphoinositide phosphatases and inactive partners such as MTMR9 and MTMR12. Inactive homologs can stabilize and regulate active partners while lacking the intrinsic catalytic reaction.

Experiments on MTMR6-MTMR9 distinguish partner stabilization and increased phosphatase output from MTMR9 catalysis. The mussel target's catalytic-site status and the horse MTMR9 internal deletion require sequence-level scrutiny. Catalytic activity, phosphatase regulation, binding and autophagy phenotypes must not be transferred as one package.

**Exact benchmark/reference members:** MYTGA/A0A8B6GS20 (A0A8B6GS20), HORSE/MTMR9 (A0A9L0T3C1), human/MTMR9 (Q96QG7), rat/Mtmr12 (A0A8I5ZMD5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [phosphatidylinositol-3-phosphate phosphatase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004438) (GO:0004438) | UNRESOLVED | For phosphatidylinositol-3-phosphate phosphatase activity: Experiments on MTMR6-MTMR9 distinguish partner stabilization and increased phosphatase output from MTMR9 catalysis. The mussel target's catalytic-site status and the horse MTMR9 internal deletion require sequence-level scrutiny. Catalytic activity, phosphatase regulation, binding and autophagy phenotypes must not be transferred as one package. The evidence does not establish a safe grant to every family member or a complete set of applicable PANTHER subfamilies. |
| [positive regulation of phosphatase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0010922) (GO:0010922) | UNRESOLVED | MTMR9 experiments establish increased catalytic output of active myotubularin partners, and this is a regulatory action rather than intrinsic phosphatase activity. The family contains several other inactive myotubularins and diverse active/inactive partner combinations. The inspected MTMR9 experiments do not establish that positive regulation is absent from every other branch or enumerate all positive regulators. Applicability therefore remains unresolved at the complete family-boundary level, with the horse MTMR9 deletion an additional target-specific qualification. |
| [negative regulation of autophagy](https://www.ebi.ac.uk/QuickGO/term/GO:0010507) (GO:0010507) | UNRESOLVED | For negative regulation of autophagy: Experiments on MTMR6-MTMR9 distinguish partner stabilization and increased phosphatase output from MTMR9 catalysis. The mussel target's catalytic-site status and the horse MTMR9 internal deletion require sequence-level scrutiny. Catalytic activity, phosphatase regulation, binding and autophagy phenotypes must not be transferred as one package. The evidence does not establish a safe grant to every family member or a complete set of applicable PANTHER subfamilies. |
| [protein stabilization](https://www.ebi.ac.uk/QuickGO/term/GO:0050821) (GO:0050821) | UNRESOLVED | Protein stabilization is directly supported for MTMR6-MTMR9 and for the MTM1-MTMR12 pair. The latter primarily affects MTM1 abundance rather than intrinsic enzyme activity. These positive systems do not establish universal stabilization of every family member or enumerate all relevant branches. The altered N-terminus of the selected rat MTMR12 product adds an exact-product trafficking qualification. |
| [protein-containing complex](https://www.ebi.ac.uk/QuickGO/term/GO:0032991) (GO:0032991) | UNRESOLVED | For protein-containing complex: Experiments on MTMR6-MTMR9 distinguish partner stabilization and increased phosphatase output from MTMR9 catalysis. The mussel target's catalytic-site status and the horse MTMR9 internal deletion require sequence-level scrutiny. Catalytic activity, phosphatase regulation, binding and autophagy phenotypes must not be transferred as one package. The evidence does not establish a safe grant to every family member or a complete set of applicable PANTHER subfamilies. |
| [protein phosphatase binding](https://www.ebi.ac.uk/QuickGO/term/GO:0019903) (GO:0019903) | UNRESOLVED | For protein phosphatase binding: Experiments on MTMR6-MTMR9 distinguish partner stabilization and increased phosphatase output from MTMR9 catalysis. The mussel target's catalytic-site status and the horse MTMR9 internal deletion require sequence-level scrutiny. Catalytic activity, phosphatase regulation, binding and autophagy phenotypes must not be transferred as one package. The evidence does not establish a safe grant to every family member or a complete set of applicable PANTHER subfamilies. |
| [enzyme regulator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0030234) (GO:0030234) | UNRESOLVED | MTMR9 is a positive experimentally supported example of an enzyme regulator in this family. Inactive homologs can regulate active partners without executing their reaction, but activity status alone does not establish each homolog's regulatory effect. Other myotubularin partner combinations have not been comprehensively adjudicated here. The MTMR9 example cannot be used as an exhaustive set of enzyme-regulatory subfamilies. |
| [regulation of phosphatidylinositol dephosphorylation](https://www.ebi.ac.uk/QuickGO/term/GO:0060304) (GO:0060304) | UNRESOLVED | MTMR9-mediated changes in active myotubularin output support regulation of phosphatidylinositol dephosphorylation in that partner system. The relevant mechanism is partner regulation rather than intrinsic catalysis. The family contains other active/inactive pairs, and the inspected evidence does not delimit all branches capable of regulating the process. Family-level applicability remains unresolved without excluding those unenumerated branches. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10807/PTHR10807-review.yaml)

## PTHR10809

**VESICLE-ASSOCIATED MEMBRANE PROTEIN-ASSOCIATED PROTEIN** — MOSTLY_COHERENT; COMPLETE

VAP proteins provide membrane-associated docking surfaces for lipid-transfer and other trafficking proteins. Canonical VAPA/VAPB and yeast Scs proteins use an MSP domain to recognize FFAT-containing partners, helping organize membrane contacts rather than transporting lipids through an intrinsic catalytic site.

IPR016763 and the reviewed human VAPA record support ER-associated partner recruitment. Plant VAP-related proteins and variant architectures require separate assessment of membrane anchoring and partner specificity. VAPA family membership is insufficient evidence for plasma-membrane residence, tight-junction membership or lipid-transfer activity of VAPA itself.

**Exact benchmark/reference members:** HORSE/VAPA (A0A3Q2H1L9), human/VAPA (Q9P0L0)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [endoplasmic reticulum membrane](https://www.ebi.ac.uk/QuickGO/term/GO:0005789) (GO:0005789) | UNRESOLVED | The FFAT-contact study directly identifies VAP-A and VAP-B as ER receptors, supporting ER residence in both canonical mammalian branches rather than only VAPA. The family also contains yeast Scs proteins and plant/variant architectures with different membrane anchors. A complete localization boundary is not defined, but ER-membrane residence is well supported for the anchored VAPA/VAPB mechanism. Contact with another organelle does not relocate the VAP anchor to that organelle. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10809/PTHR10809-review.yaml)

## PTHR10859

**GLYCOSYL TRANSFERASE** — HETEROGENEOUS; COMPLETE

This dolichol-phosphate glycosyltransferase family contains enzymes producing different lipid-linked sugar donors. ALG5 transfers glucose from UDP-glucose to dolichyl phosphate, whereas DPM-type enzymes generate dolichyl-phosphate mannose. Both feed glycosylation pathways but the sugar donor and product are different.

The frozen PANTHER classification separates dolichyl-phosphate beta-glucosyltransferase and beta-D-mannosyltransferase subfamilies. The reviewed human ALG5 reaction establishes glucose transfer for the ALG5 branch, including the matched horse target by orthology. Mannose transfer is not an interchangeable annotation.

**Exact benchmark/reference members:** HORSE/ALG5 (A0A5F5PM72), human/ALG5 (Q9Y673)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [dolichyl-phosphate beta-glucosyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004581) (GO:0004581) | UNRESOLVED | Glucose transfer to dolichyl phosphate is experimentally supported for human ALG5 and is distinct from the mannose transfer performed by DPM relatives. The PANTHER vocabulary contains more than one glucosyltransferase-labelled subfamily, so the two benchmark ALG5 representatives do not define an exhaustive list of glucose-transferring branches. Exact substrate specificity and full catalytic architecture must delimit the applicable set; the ALG5 reaction itself is not in doubt. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10859/PTHR10859-review.yaml)

## PTHR10871

**30S RIBOSOMAL PROTEIN S13/40S RIBOSOMAL PROTEIN S18** — MOSTLY_COHERENT; COMPLETE

uS13-related proteins contribute to the structure and function of the small ribosomal subunit. The family includes bacterial-type and mitochondrial uS13 proteins as well as eukaryotic cytosolic counterparts. The mitochondrial small-subunit protein Sws2 therefore shares a ribosomal function without sharing the localization of every family member.

All 848 inspected entry names identify uS13 proteins, including cytosolic, mitochondrial and other organellar variants. The official vocabulary contains a topoisomerase-like label, but the member inventory provides no corresponding topoisomerase protein evidence. Sws2 has a reviewed uS13m assignment supporting mitochondrial small-subunit function. Ribosomal structure is coherent across the inspected proteins; mitochondrial targeting remains branch-dependent.

**Exact benchmark/reference members:** SCHPO/sws2 (O59772)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [mitochondrial small ribosomal subunit](https://www.ebi.ac.uk/QuickGO/term/GO:0005763) (GO:0005763) | UNRESOLVED | Mitochondrial small-subunit membership is supported for Sws2/uS13m, but mitochondrial uS13-related proteins occupy multiple subfamilies in the classification. Cytosolic and bacterial counterparts have the same broad structural role in different translation systems. A single pombe uS13m subfamily is not an exhaustive mitochondrial allowed set; targeting, architecture and ribosome membership must determine the branch boundary. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10871/PTHR10871-review.yaml)

## PTHR10913

**FOLLISTATIN-RELATED** — HETEROGENEOUS; COMPLETE

This domain-rich family contains extracellular proteins with distinct inhibitory and signaling roles. Kazal-containing protease inhibitors coexist in the classification with follistatin-related proteins and larger extracellular organizers. A shared cysteine-rich domain does not identify either the inhibited protease or the growth-factor ligand.

The actual family inventory spans follistatin growth-factor antagonists and Kazal protease inhibitors. Human follistatin binds activin and occludes receptor-binding surfaces (PMID:16482217), whereas Phytophthora EPI1 inhibits the tomato P69B subtilisin-like protease (PMID:15096512). These are different molecular targets despite related extracellular modules. The seven-Kazal-domain fly CG32354 product also has a membrane-spanning segment, so it cannot be assigned a freely secreted follistatin mechanism or a specific inhibited protease solely from its family. Neither activin antagonism nor serine-protease inhibition is a universal family grant.

**Exact benchmark/reference members:** DROME/CG32354 (Q9VSK1)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10913/PTHR10913-review.yaml)

## PTHR10920

**RIBOSOMAL RNA METHYLTRANSFERASE** — HETEROGENEOUS; COMPLETE

FtsJ/RlmE-related methyltransferases modify ribose groups in RNA. The family includes bacterial ribosomal RNA enzymes, mitochondrial Mrm2 and eukaryotic enzymes acting on tRNA or preribosomal RNA. RNA type, modified nucleotide and subcellular location define the important functional boundaries. Human MRM2 also has a ribosome-assembly function that does not require its methyltransferase activity, and disrupting its fly ortholog causes mitochondrial developmental defects.

The inventory separates bacterial RlmE, mitochondrial MRM2, FTSJ3/Spb1 prerRNA factors and tRNA methyltransferases. PMID:35177605 directly demonstrates human MRM2-dependent assembly that persists with methyltransferase-defective variants, and also tests the Drosophila ortholog in developmental arrest. Human catalytic independence is not itself a fly catalytic-mutant experiment. RNA substrate, nucleotide numbering and organellar targeting remain branch-specific.

**Exact benchmark/reference members:** DROME/Mrm2 (Q9VDT6)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10920/PTHR10920-review.yaml)

## PTHR10937

**GLUCOSAMINE--FRUCTOSE-6-PHOSPHATE AMINOTRANSFERASE, ISOMERIZING** — HETEROGENEOUS; COMPLETE

GFAT enzymes couple glutamine hydrolysis to conversion of fructose-6-phosphate into glucosamine-6-phosphate, supplying the hexosamine biosynthetic pathway. Related sugar-isomerase domains also occur in glucosamine deamination and other reactions, so a broad structural grouping extends beyond the complete two-domain GFAT reaction.

Full-length GFAT1/GFAT2-type proteins conserve the coupled glutaminase and sugar-isomerase reaction, whereas related deaminase branches perform different chemistry. The native Gfat1-PF isoform A8Y5A1 retains the isomerase region but only a small part of the glutaminase module, so catalytic capability is not uniform even among gene products assigned to a single subfamily.

**Exact benchmark/reference members:** DROME/Gfat1 (A8Y5A1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [L-glutamine:D-fructose-6-phosphate transaminase (isomerizing) activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004360) (GO:0004360) | UNRESOLVED | The complete glutamine-dependent reaction is established for human GFPT1 and GFPT2 by structural and enzyme-kinetic studies (PMID:32019926; PMID:35229715), and thus is not exclusive to the fly-associated SF0. Within that SF0, however, benchmark A8Y5A1 is the native 434-residue Gfat1-PF isoform: the reproducible comparison retains only 40 of 299 glutamine-amidotransferase-domain residues while preserving the sugar-isomerase domains. This contradicts intrinsic execution of the complete two-module reaction by that exact protein, without contradicting the activity of full-length Gfat1. A safe scope therefore depends on both reaction branch and isoform/domain completeness; an unconditional subfamily grant cannot express it. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10937/PTHR10937-review.yaml)

## PTHR10985

**BASIC HELIX-LOOP-HELIX TRANSCRIPTION FACTOR, HES-RELATED** — HETEROGENEOUS; COMPLETE

HES/HEY-related bHLH proteins regulate developmental transcription through partner-dependent dimerization, DNA recognition and corepressor interactions. Direct zebrafish experiments show that Her7:Hes6 heterodimers bind cyclic-gene promoters strongly whereas Hes6 homodimers do not. Developmental process, DNA-binding competence and repressive output vary among family members and dimer combinations.

The common bHLH/Orange architecture permits dimerization but does not ensure identical DNA recognition or transcriptional output. Primary zebrafish experiments separate promiscuous protein interactions from selective promoter binding and establish a Hes6-dependent segmentation-clock mechanism. A blanket non-DNA-binding designation for HES6 would discard the experimentally demonstrated heterodimer contribution.

**Exact benchmark/reference members:** DANRE/hes6 (Q6P0J1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-binding transcription factor activity, RNA polymerase II-specific](https://www.ebi.ac.uk/QuickGO/term/GO:0000981) (GO:0000981) | UNRESOLVED | Zebrafish Hes6 contributes to a DNA-binding repressor with Her7. This does not imply autonomous Hes6 homodimer binding, and the evidence does not grant identical activity to all HES/HEY products or all possible dimer combinations. |
| [somitogenesis](https://www.ebi.ac.uk/QuickGO/term/GO:0001756) (GO:0001756) | UNRESOLVED | Zebrafish Hes6 has direct perturbation and biochemical support in the segmentation clock. Neural, somitic and other developmental functions must be resolved by lineage and expression context rather than transferred to the entire HES/HEY family. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10985/PTHR10985-review.yaml)

## PTHR10997

**IMPORTIN-7, 8, 11** — HETEROGENEOUS; COMPLETE

Importin/exportin relatives are soluble transport receptors that carry selected proteins through the nuclear pore. Importin-7/Moleskin belongs to an import-receptor branch, while other members of this family include importin-8/9/11 and exportin-2. Cargo recognition and transport direction are central functional distinctions.

Importin-beta-like receptors mediate Ran-dependent transport but recognize different cargoes. Fly DIM-7/Msk binds phosphorylated ERK and is required for its nuclear accumulation, with rescue restoring the phenotype (PMID:11262240). This is direct support for one fly cargo pathway; it does not establish that every importin-7/8/11-related member transports activated ERK or Smads. Nuclear import is a strong mechanism for characterized receptors, while the exact exhaustive family/subfamily grant remains unresolved rather than treating incomplete cargo coverage as a negative result.

**Exact benchmark/reference members:** DROME/msk (Q9VSD6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein import into nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0006606) (GO:0006606) | UNRESOLVED | Importin-beta-like receptors mediate Ran-dependent transport but recognize different cargoes. Fly DIM-7/Msk binds phosphorylated ERK and is required for its nuclear accumulation, with rescue restoring the phenotype (PMID:11262240). This is direct support for one fly cargo pathway; it does not establish that every importin-7/8/11-related member transports activated ERK or Smads. Nuclear import is a strong mechanism for characterized receptors, while the exact exhaustive family/subfamily grant remains unresolved rather than treating incomplete cargo coverage as a negative result. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10997/PTHR10997-review.yaml)

## PTHR11012

**PROTEIN KINASE-LIKE DOMAIN-CONTAINING** — UNKNOWN; COMPLETE

This family groups insect CHK/ecdysteroid-kinase-like proteins. The kinase-like architecture raises a specific hypothesis of small-molecule phosphorylation, including ecdysteroid phosphorylation, rather than automatically implying phosphorylation of proteins. Individual members remain unevenly characterized.

The insect EcKL phylogeny identifies at least 13 subfamilies and places the two experimentally characterized ecdysteroid kinases in different subfamilies (PMID:38291829). Most members lack a known substrate; expression and comparative-genomic associations with xenobiotic metabolism are hypotheses rather than phosphorylation assays (PMID:32540344). CG31099 and CG6830 share SF6, but this does not establish conservation of an ecdysteroid substrate or its 22-hydroxyl acceptor. Small-molecule kinase chemistry is the supported family-level hypothesis, while the distribution of steroid specificity remains unresolved.

**Exact benchmark/reference members:** DROME/CG31099 (Q8IMT2), DROME/CG6830 (Q9VGJ8)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ecdysteroid 22-kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0106389) (GO:0106389) | UNRESOLVED | The insect EcKL phylogeny identifies at least 13 subfamilies and places the two experimentally characterized ecdysteroid kinases in different subfamilies (PMID:38291829). Most members lack a known substrate; expression and comparative-genomic associations with xenobiotic metabolism are hypotheses rather than phosphorylation assays (PMID:32540344). CG31099 and CG6830 share SF6, but this does not establish conservation of an ecdysteroid substrate or its 22-hydroxyl acceptor. Small-molecule kinase chemistry is the supported family-level hypothesis, while the distribution of steroid specificity remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11012/PTHR11012-review.yaml)

## PTHR11021

**SMALL NUCLEAR RIBONUCLEOPROTEIN F  SNRNP-F** — HETEROGENEOUS; COMPLETE

SmF/Lsm6 proteins are related small subunits of RNA-associated rings. SmF belongs to canonical spliceosomal Sm particles; Lsm6 is shared by the nuclear U6-associated Lsm2-8 ring and the cytoplasmic Lsm1-7 mRNA-decapping ring. Complex identity therefore changes the biological process assigned to a member.

The actual inventory and curated IPR016487 include both SmF and Lsm6 proteins. Lsm6 participates in the U6-associated Lsm2-8 ring and the Lsm1-7 mRNA-decapping ring, while canonical SmF participates in other spliceosomal snRNPs. Shared RNA-ring architecture supports RNA association, but U2/U5 complex membership and cytoplasmic decay are not interchangeable across these branches.

**Exact benchmark/reference members:** SCHPO/lsm6 (Q9UUI1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [RNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003723) (GO:0003723) | FAMILY_WIDE | IPR016487 explicitly includes SmF, Lsm6 and plant LSM36B. RNA binding is the shared role; membership in a particular snRNP or in the cytoplasmic decapping apparatus is branch-dependent. Pombe Lsm6 should not inherit U2 or U5 membership merely from the SmF family name. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11021/PTHR11021-review.yaml)

## PTHR11034

**N-MYC DOWNSTREAM REGULATED** — UNKNOWN; COMPLETE

NDRG-family proteins are alpha/beta-hydrolase-fold interaction proteins with diverse regulatory roles. Human and mouse NDRG2 structures support a nonenzymatic scaffold rather than a conventional hydrolase; the shared fold does not specify a conserved enzymatic substrate or signaling pathway.

NDRG2 structures lack catalytic signature residues and have an occluded substrate-binding site, while structure-guided mutagenesis supports a role in molecular interactions affecting TCF/beta-catenin signaling (PMID:21247902). This is a concrete fold-retaining nonenzyme example, not evidence that every homolog is an active hydrolase. The family also includes plant NDL/SF21 and other animal NDRG branches with different biological contexts. A universal molecular-interaction partner or tumor-suppressor mechanism is unresolved, and the exact fly MESK2 product is not assigned human NDRG2 substrates or residue losses without its own sequence evidence.

**Exact benchmark/reference members:** DROME/MESK2 (Q8T0V2)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11034/PTHR11034-review.yaml)

## PTHR11042

**EUKARYOTIC TRANSLATION INITIATION FACTOR 2-ALPHA KINASE  EIF2-ALPHA KINASE -RELATED** — HETEROGENEOUS; COMPLETE

This kinase family combines cell-cycle inhibitory kinases with stress-responsive translation-control kinases and other related enzymes. WEE1-family proteins inhibit CDK-driven mitotic entry, whereas eIF2-alpha kinases control translation during specific stresses. Shared protein-kinase chemistry does not imply common substrates or phosphoacceptor specificity.

The curated human WEE1 record and primary studies support CDK1 inhibitory tyrosine phosphorylation. PANTHER also contains GCN2, PKR, PERK and other eIF2-alpha kinase branches. WEE1 tyrosine-kinase and G2/M-control annotations should therefore be scoped to the WEE1 branch rather than propagated from kinase-fold similarity.

**Exact benchmark/reference members:** HORSE/WEE1 (F6TY09), human/WEE1 (P30291)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein tyrosine kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004713) (GO:0004713) | UNRESOLVED | Tyrosine-directed inhibitory CDK phosphorylation is supported for human WEE1 and for pombe Wee1: purified pombe Wee1 directly phosphorylates cyclin-associated Cdc2 on Tyr15 (PMID:1372994). These proteins occupy different PANTHER subfamilies, and additional Wee1-related regulators require the same substrate-level assessment. The broader family also includes eIF2-alpha-directed serine/threonine kinases. Human WEE1 SF72 is therefore a verified positive branch, not the exhaustive boundary of protein tyrosine kinase activity; the complete applicable set remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11042/PTHR11042-review.yaml)

## PTHR11085

**NAD-DEPENDENT PROTEIN DEACYLASE SIRTUIN-5, MITOCHONDRIAL-RELATED** — HETEROGENEOUS; COMPLETE

Sirtuins couple NAD consumption to removal of acyl groups from protein lysines, with substantial variation in acyl-group preference and cellular substrate selection. SIRT5 is specialized toward negatively charged lysine acylations such as succinylation, malonylation and glutarylation. Nuclear histone regulation and mitochondrial metabolic control are different branch contexts.

The experimentally annotated SIRT5 record supports acidic-acyl lysine hydrolysis. Other sirtuins differ in deacetylation efficiency, longer-chain deacylation and reported ADP-ribosyl transfer reactions. A family label of deacetylase cannot replace substrate-specific evidence, and mitochondrial localization does not apply to the entire family.

**Exact benchmark/reference members:** HORSE/SIRT5 (F6S899), human/SIRT5 (Q9NXA8)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein-succinyllysine desuccinylase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0036055) (GO:0036055) | UNRESOLVED | SIRT5 is experimentally established as a protein desuccinylase, but this reaction is not exclusive to SIRT5: primary work reports SIRT7-dependent histone H3K122 desuccinylation (PMID:27436229). Substrate preference and assay context differ among sirtuins. The SIRT5 subfamily consequently cannot be used as an exhaustive allowed set, and neither its evidence nor the SIRT7 result warrants a universal desuccinylase grant to all sirtuins. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11085/PTHR11085-review.yaml)

## PTHR11134

**ADAPTOR COMPLEX SUBUNIT BETA FAMILY MEMBER** — HETEROGENEOUS; COMPLETE

Beta adaptins are large subunits of heterotetrameric adaptor complexes that sort membrane cargo. AP-1, AP-2, AP-3 and AP-4 operate at different membrane-trafficking steps and differ in coat partnerships. The beta-adaptin fold identifies a trafficking component without fixing a single organelle or vesicle coat.

The inventory explicitly contains beta subunits of AP-1 through AP-4. Their cargo-adaptor architecture supports vesicle-trafficking participation, while coat recruitment and membrane compartment depend on the complex. The broad curated description overgeneralizes clathrin recruitment; AP-4 membership is not equivalent to a clathrin-binding beta-adaptin. NCU09721 needs its AP-1-specific comparison rather than a universal plasma-membrane endocytosis label.

**Exact benchmark/reference members:** NEUCR/NCU09721 (Q7S2Q5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [clathrin binding](https://www.ebi.ac.uk/QuickGO/term/GO:0030276) (GO:0030276) | UNRESOLVED | IPR026739 and the subfamily list distinguish AP-complex branches. The common description overgeneralizes clathrin recruitment across all AP complexes: clathrin binding and plasma-membrane endocytosis must be scoped to the appropriate complex. NCU09721 needs AP-1 placement evidence for a trans-Golgi/endosome interpretation. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11134/PTHR11134-review.yaml)

## PTHR11200

**INOSITOL 5-PHOSPHATASE** — HETEROGENEOUS; COMPLETE

Inositol 5-phosphatases remove the phosphate at the 5 position of soluble inositol phosphates or membrane phosphoinositides. Synaptojanins combine this activity with an additional Sac1-like phosphatase region and regulatory domains. Different family architectures target distinct lipid pools and cellular trafficking events.

Synaptojanin/OCRL-related proteins share phosphoinositide 5-phosphatase chemistry but differ in auxiliary domains and localization. Fly synaptojanin functions with endophilin in synaptic-vesicle recycling (PMID:14622578). Synaptojanin additionally contains a Sac1 phosphatase domain with distinct substrate chemistry; selective impairment of Sac1 and combined impairment of both phosphatase domains produce different experimental and disease associations (PMID:27435091). Sac1-dependent 4-phosphate removal cannot be assigned to relatives that possess only the 5-phosphatase module, and neuronal vesicle recycling is not the function of all OCRL/INPP5-like members.

**Exact benchmark/reference members:** DROME/Synj (Q5U0V7)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11200/PTHR11200-review.yaml)

## PTHR11208

**RNA-BINDING PROTEIN RELATED** — HETEROGENEOUS; COMPLETE

KH-domain RNA-binding proteins in this family regulate RNA maturation and expression. SF1/branchpoint-binding proteins recognize intronic branchpoint regions during early spliceosome assembly, whereas STAR/QKI/KHDRBS-related proteins regulate selected RNA targets through alternative splicing and other post-transcriptional mechanisms.

The shared KH-containing RNA-recognition machinery supports broad RNA binding, with different recognition mechanisms in STAR/QKI and SF1 branches. QKI/GLD-1 structures show how Qua1 dimerization and the KH-Qua2 unit recognize a specific RNA element (PMID:23630077). This does not make every KH protein an identical sequence-specific translational regulator, nor does it transfer the SF1 splice-branchpoint role to qkr58E-1. RNA binding is the conserved broad molecular activity; target sequences, oligomerization requirements and splicing versus translational outputs remain branch-specific.

**Exact benchmark/reference members:** DROME/qkr58E-1 (Q9W255)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [RNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003723) (GO:0003723) | FAMILY_WIDE | The shared KH-containing RNA-recognition machinery supports broad RNA binding, with different recognition mechanisms in STAR/QKI and SF1 branches. QKI/GLD-1 structures show how Qua1 dimerization and the KH-Qua2 unit recognize a specific RNA element (PMID:23630077). This does not make every KH protein an identical sequence-specific translational regulator, nor does it transfer the SF1 splice-branchpoint role to qkr58E-1. RNA binding is the conserved broad molecular activity; target sequences, oligomerization requirements and splicing versus translational outputs remain branch-specific. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11208/PTHR11208-review.yaml)

## PTHR11223

**Exportin-1 and exportin-5 transport receptors** — HETEROGENEOUS; COMPLETE

Exportins mediate nuclear export of distinct cargo classes. Exportin-1 recognizes protein export signals, whereas exportin-5 and related receptors export structured RNAs and selected other cargos.

The Drosophila virilis target has exportin-5 architecture. Cytoplasmic residence is compatible with the transport cycle, but it does not identify cargo specificity or mean that the protein is excluded from the nucleus. Exportin-1 cargo biology should not be inherited by exportin-5 solely from the combined family.

**Exact benchmark/reference members:** DROVI/B4MAQ2 (B4MAQ2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [cytoplasm](https://www.ebi.ac.uk/QuickGO/term/GO:0005737) (GO:0005737) | UNRESOLVED | Exportins shuttle cargo through a nucleus-to-cytoplasm transport cycle; cytoplasmic cargo detection alone is not a direct localization assay of every exportin. The Drosophila Exp5 study establishes RNA binding and export, and the virilis target has exportin-5 architecture. This supports a nucleocytoplasmic context without treating cytoplasm as exclusive or transferring exportin-1 protein-cargo specificity to exportin-5. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11223/PTHR11223-review.yaml)

## PTHR11347

**CYCLIC NUCLEOTIDE PHOSPHODIESTERASE** — HETEROGENEOUS; COMPLETE

Cyclic-nucleotide phosphodiesterases terminate or shape second-messenger signals by hydrolyzing cyclic nucleotides. Members differ in cAMP versus cGMP preference, dual specificity and regulatory domains. PDE4/Dunce-type enzymes belong to a cAMP-directed branch, distinct from retinal cGMP phosphodiesterases.

Cyclic-nucleotide phosphodiesterases share hydrolysis of a cyclic phosphodiester bond but include cAMP-selective, cGMP-selective and dual-specificity enzymes. The reviewed fly Pde4 record assigns the PDE4 subfamily and cAMP hydrolysis by similarity to a characterized homolog; the actual family inventory separately includes cGMP-directed PDEs. A general phosphodiesterase label therefore cannot determine the cyclic-nucleotide substrate. Learning, phototransduction and reproductive phenotypes remain substrate-, cell- and branch-dependent.

**Exact benchmark/reference members:** DROME/Pde4 (Q9W4S9)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11347/PTHR11347-review.yaml)

## PTHR11349

**NUCLEOSIDE DIPHOSPHATE KINASE** — MOSTLY_COHERENT; COMPLETE

Nucleoside diphosphate kinases redistribute terminal phosphate among nucleotide pools through a phosphohistidine intermediate. The Awd/NM23-type catalytic role contributes to nucleotide homeostasis, while individual proteins can also participate in trafficking and developmental regulation. Those cellular roles need not imply a different phosphotransfer reaction.

Awd and classical NDKs catalyze nucleoside-diphosphate phosphorylation; the Awd killer-of-prune mutation changes protein stability without abolishing catalytic efficiency (PMID:1320004). The classification also includes NDK-like/domain-containing branches for which this source does not resolve a complete active-site and biochemical boundary. Awd activity is supported, but an unconditional grant to all classified NDK-like proteins remains unresolved. Notch regulation and other Awd-specific pathways are not universal NDK functions.

**Exact benchmark/reference members:** DROME/awd (A0A0B4LHX6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [nucleoside diphosphate kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004550) (GO:0004550) | UNRESOLVED | Awd and classical NDKs catalyze nucleoside-diphosphate phosphorylation; the Awd killer-of-prune mutation changes protein stability without abolishing catalytic efficiency (PMID:1320004). The classification also includes NDK-like/domain-containing branches for which this source does not resolve a complete active-site and biochemical boundary. Awd activity is supported, but an unconditional grant to all classified NDK-like proteins remains unresolved. Notch regulation and other Awd-specific pathways are not universal NDK functions. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11349/PTHR11349-review.yaml)

## PTHR11473

**AROMATIC AMINO ACID HYDROXYLASE** — HETEROGENEOUS; COMPLETE

Aromatic amino-acid hydroxylases use reduced pterin and oxygen to hydroxylate aromatic substrates. Phenylalanine hydroxylase produces tyrosine, tyrosine hydroxylase produces L-DOPA and tryptophan hydroxylase produces 5-hydroxytryptophan. These homologous reactions feed different metabolic and signaling pathways.

Phenylalanine, tyrosine and tryptophan hydroxylases retain related oxygenation chemistry with different substrates. Within the phenylalanine-hydroxylase-associated group, the native Hn-PD input E8NH57 contains only a C-terminal portion of the catalytic domain. Retained iron ligands do not restore the missing substrate/cofactor architecture, so neither family nor subfamily identity can grant the complete reaction to every isoform.

**Exact benchmark/reference members:** DROME/Hn (E8NH57)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [phenylalanine 4-monooxygenase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004505) (GO:0004505) | UNRESOLVED | Phenylalanine hydroxylation is supported for full-length PAH/Hn-type proteins, but a subfamily assignment is insufficient for every isoform. The exact fly E8NH57 input is Hn-PD, a native 178-residue isoform matching the C-terminal part of full-length Hn. The reproducible human-PAH comparison preserves metal ligands but retains only 149 of 307 catalytic-domain positions and lacks mapped substrate/cofactor-binding architecture. Thus the gene-level removal concerns this incomplete catalytic architecture, not inactivity of full-length Hn or the entire PAH branch. The safe family grant must resolve both substrate-specific branches and complete catalytic domains; it remains unresolved at the unconditional subfamily level. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11473/PTHR11473-review.yaml)

## PTHR11475

**OXIDASE/PEROXIDASE** — HETEROGENEOUS; COMPLETE

Animal-type heme-peroxidase relatives use or resemble enzymes that use peroxide in diverse extracellular reactions. Thyroid hormone synthesis, antimicrobial oxidant production, chorion modification and extracellular matrix cross-linking are distinct physiological contexts. Additional extracellular domains and active-site integrity are essential for distinguishing these roles.

The inventory includes thyroid, leukocyte, lacto-, chorion- and peroxidasin proteins and peroxidase-like relatives. CG42331/Q9VC41 maps to SF109, officially chorion-peroxidase-like, while its automated name suggests peroxidasin. These conflicting names do not resolve substrate choice. An extracellular peroxidase-fold comparison is justified; collagen cross-linking, thyroid hormone production and proteolysis require separate architecture and biochemical evidence.

**Exact benchmark/reference members:** DROME/CG42331 (Q9VC41)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11475/PTHR11475-review.yaml)

## PTHR11527

**Small heat-shock and alpha-crystallin proteins** — MOSTLY_COHERENT; COMPLETE

Small heat-shock proteins and alpha-crystallins form oligomeric assemblies that interact with non-native proteins. Client recognition, oligomer structure, expression response and cellular localization vary among organisms and paralogs.

The diatom target has the small-HSP domain, and biochemical small-HSP studies establish unfolded-client binding and oligomerization. Heat, salt and hydrogen-peroxide responses require the relevant organism and conditions. Holdase-mediated protection is not proof that the target independently refolds denatured clients.

**Exact benchmark/reference members:** PHATC/B7FXQ8 (B7FXQ8)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [response to salt stress](https://www.ebi.ac.uk/QuickGO/term/GO:0009651) (GO:0009651) | UNRESOLVED | A small-HSP domain supports a proteostasis comparison, not a salt-response phenotype. The cited Hsp16.5 oligomer/client study does not assay diatom salinity response. Salt induction, protection or loss-of-function effects in the relevant organism are needed to resolve this process across family branches. |
| [protein complex oligomerization](https://www.ebi.ac.uk/QuickGO/term/GO:0051259) (GO:0051259) | UNRESOLVED | The Hsp16.5 study directly demonstrates 24-, 48- and engineered intermediate oligomeric assemblies, establishing oligomerization in characterized small HSPs. Their variable oligomeric states and specialized alpha-crystallin relatives prevent a fixed assembly stoichiometry or unconditional grant to every detected fragment. The complete assembly-competent set is unresolved. |
| [protein folding](https://www.ebi.ac.uk/QuickGO/term/GO:0006457) (GO:0006457) | UNRESOLVED | Binding unfolded clients and preventing aggregation can assist productive folding through a chaperone network, but neither proves autonomous refolding or an exact folding pathway for the diatom target. The cited work measures client binding and oligomer plasticity. It supports a holdase-related hypothesis while leaving the broad protein-folding process and its complete branch distribution unresolved. |
| [response to heat](https://www.ebi.ac.uk/QuickGO/term/GO:0009408) (GO:0009408) | UNRESOLVED | Heat response is common in small-HSP biology but must be established physiologically, especially for constitutive alpha-crystallins and lineage-specific proteins. The cited structural study does not test heat-induced expression or thermotolerance of the diatom protein. The family fold alone does not identify the heat-responsive branches. |
| [response to hydrogen peroxide](https://www.ebi.ac.uk/QuickGO/term/GO:0042542) (GO:0042542) | UNRESOLVED | Hydrogen-peroxide response is a stimulus-specific physiological claim distinct from generic client aggregation suppression. The cited oligomer/client experiment does not measure peroxide exposure or a peroxide-defense phenotype. The diatom target and the full family cannot receive this process from the small-HSP domain alone. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11527/PTHR11527-review.yaml)

## PTHR11586

**TRNA-AMINOACYLATION COFACTOR ARC1 FAMILY MEMBER** — HETEROGENEOUS; COMPLETE

This family combines cytoplasmic tyrosyl-tRNA synthetases with related tRNA-binding or regulatory proteins, including AIMP1-type factors. Complete TyrRS enzymes activate tyrosine with ATP and transfer it to cognate tRNA. Shared ancillary RNA-binding domains do not confer that aminoacylation reaction on a protein lacking the synthetase module.

Complete TyrRS proteins combine tyrosine activation and tRNA charging domains, whereas related ancillary RNA-binding/EMAP-containing proteins need not catalyze aminoacylation. Fly TyrRS additionally has a context-specific extracellular role during cell competition, with proteolytic products affecting hemocyte attraction (PMID:26658841). This signaling activity is not the definition of all TyrRS or AIMP1/Arc1 relatives. Tyrosine-tRNA ligase activity requires the complete catalytic architecture; a shared ancillary domain or a secreted fragment does not suffice, and an exhaustive active-subfamily boundary is not established here.

**Exact benchmark/reference members:** DROME/TyrRS (Q9VV60)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [tyrosine-tRNA ligase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004831) (GO:0004831) | UNRESOLVED | Complete TyrRS proteins combine tyrosine activation and tRNA charging domains, whereas related ancillary RNA-binding/EMAP-containing proteins need not catalyze aminoacylation. Fly TyrRS additionally has a context-specific extracellular role during cell competition, with proteolytic products affecting hemocyte attraction (PMID:26658841). This signaling activity is not the definition of all TyrRS or AIMP1/Arc1 relatives. Tyrosine-tRNA ligase activity requires the complete catalytic architecture; a shared ancillary domain or a secreted fragment does not suffice, and an exhaustive active-subfamily boundary is not established here. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11586/PTHR11586-review.yaml)

## PTHR11588

**TUBULIN** — HETEROGENEOUS; COMPLETE

Tubulin-family GTP-binding proteins form or organize microtubule structures. Alpha/beta heterodimers make the microtubule lattice, whereas gamma-tubulin supports nucleation and other tubulin classes have specialized centriole or basal-body roles. Isotype-specific expression and lattice properties add a further level of divergence.

Tubulins diversify into alpha, beta, gamma, delta, epsilon and zeta subfamilies with distinct polymer, nucleation and basal-body roles; a phylogenomic analysis of 3524 tubulins documents their duplication and loss (PMID:25169981). GTP binding is not equivalent to GTP hydrolysis, especially for alpha versus beta tubulin in the heterodimer. Fly betaTub97EF increases microtubule stability under low-temperature conditions (PMID:29084803); that isoform-specific property is not a property of all tubulins. A universal GTPase grant is therefore unresolved without distinguishing nucleotide-site chemistry and branch architecture.

**Exact benchmark/reference members:** DROME/betaTub97EF (Q8MST5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [GTPase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003924) (GO:0003924) | UNRESOLVED | Tubulins diversify into alpha, beta, gamma, delta, epsilon and zeta subfamilies with distinct polymer, nucleation and basal-body roles; a phylogenomic analysis of 3524 tubulins documents their duplication and loss (PMID:25169981). GTP binding is not equivalent to GTP hydrolysis, especially for alpha versus beta tubulin in the heterodimer. Fly betaTub97EF increases microtubule stability under low-temperature conditions (PMID:29084803); that isoform-specific property is not a property of all tubulins. A universal GTPase grant is therefore unresolved without distinguishing nucleotide-site chemistry and branch architecture. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11588/PTHR11588-review.yaml)

## PTHR11592

**Glutathione-peroxidase-fold peroxide enzymes** — HETEROGENEOUS; COMPLETE

GPX-fold proteins reduce peroxide substrates using distinct electron-donor systems. The family includes glutathione-dependent enzymes, thioredoxin-supported enzymes, cysteine and selenocysteine forms, and specialized secretory-pathway members.

BtuE biochemical peroxide reduction is relevant to the Xanthomonas BtuE-like target, supporting an oxidative-stress role. Glutathione specificity must not be inferred for every homolog, and general oxidative-stress participation does not establish lipid-peroxide substrate preference or ferroptosis regulation.

**Exact benchmark/reference members:** XANCP/Q8P365 (Q8P365)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [response to oxidative stress](https://www.ebi.ac.uk/QuickGO/term/GO:0006979) (GO:0006979) | UNRESOLVED | BtuE is induced by oxidative-stress elicitors and reduces several peroxide substrates; characterized GPX4 provides an additional lipid-peroxide-defense branch. Neither difference in electron donor nor substrate specialization excludes a general oxidative-stress role. Secretory and specialized GPX-fold proteins still require physiological evidence, so the complete stress-response-positive set is unresolved rather than restricted to BtuE. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11592/PTHR11592-review.yaml)

## PTHR11615

**NITRATE, FORMATE, IRON DEHYDROGENASE** — UNKNOWN; COMPLETE

NARF and NARFL/Nar1-related proteins illustrate functional divergence among hydrogenase-related proteins. Human NARF binds prenylated prelamin A, whereas NARFL/IOP1 has direct support in cytosolic iron-sulfur protein maturation. Broad structural relationships do not establish respiratory hydrogenase chemistry or identical Fe-S assembly roles.

Comparative human knockdown experiments distinguish IOP1/NARFL from IOP2/NARF: IOP1 depletion impairs cytosolic aconitase activity, while IOP2 depletion does not. The frozen PANTHER vocabulary also contains discordant membrane-protein labels, so the uniformity and evolutionary meaning of the entire grouping remain unresolved. The selected NARF product has extensive deletions relative to the experimentally characterized larger protein.

**Exact benchmark/reference members:** human/NARF (J3KS48)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0005634) (GO:0005634) | UNRESOLVED | Nuclear localization is directly established for expressed human NARF constructs, but the selected 217-residue product differs extensively from the 456-residue reference. This localization cannot be granted across the broad family or assumed for every NARF product. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11615/PTHR11615-review.yaml)

## PTHR11630

**DNA REPLICATION LICENSING FACTOR MCM FAMILY MEMBER** — HETEROGENEOUS; COMPLETE

MCM-family ATPases include the MCM2-7 replicative helicase subunits and MCM8/9-associated DNA repair factors. Eukaryotic MCM2-7 functions as a heterohexamer within the active replisome, with different subunits contributing to an assembled motor. Related MCM8/9 proteins do not simply substitute for replication-licensing subunits.

The inventory contains MCM2-7, MCM8/9 and MCM-domain proteins. Curated IPR031327 separates the replicative MCM2-7 motor from repair-associated MCM8/9. NCU02539 maps to MCM4 and contributes to an assembled helicase; this does not demonstrate autonomous helicase activity by the isolated chain or establish that every family member participates in origin licensing.

**Exact benchmark/reference members:** NEUCR/NCU02539 (Q7SHS5)

**Separate canonical gene context:** A0A061AL94; exact inputs remain unassigned. See [identity evidence](unassigned-cases.md).

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA helicase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003678) (GO:0003678) | UNRESOLVED | Helicase function is supported for assembled MCM complexes, but the family-level term cannot encode the distinction between a contributing subunit and an independently active helicase. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11630/PTHR11630-review.yaml)

## PTHR11640

**NEPHRIN** — HETEROGENEOUS; COMPLETE

Immunoglobulin-domain extracellular and cell-surface proteins in this grouping mediate adhesion, recognition or tissue organization. The nephrin/Sns branch contributes to specialized cell junctions and, in flies, myoblast recognition and fusion. Other branches include different adhesion receptors and larger extracellular matrix proteins.

The classification extends beyond nephrin to kin-of-irre proteins, adhesion molecules and multidomain extracellular proteins. Thus nephrocyte diaphragm, muscle fusion, homophilic binding and kidney filtration cannot be universal family functions. Sns experimental findings should be interpreted with its nephrin-like architecture and relevant heterophilic partner, rather than generic adhesion prose.

**Exact benchmark/reference members:** DROME/sns (Q0E9F2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [heterophilic cell-cell adhesion](https://www.ebi.ac.uk/QuickGO/term/GO:0007157) (GO:0007157) | UNRESOLVED | The classification extends beyond nephrin to kin-of-irre proteins, adhesion molecules and multidomain extracellular proteins. Thus nephrocyte diaphragm, muscle fusion, homophilic binding and kidney filtration cannot be universal family functions. Sns experimental findings should be interpreted with its nephrin-like architecture and relevant heterophilic partner, rather than generic adhesion prose. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11640/PTHR11640-review.yaml)

## PTHR11644

**CYTIDINE DEAMINASE** — HETEROGENEOUS; COMPLETE

Cytidine-deaminase-related proteins use a zinc-dependent deamination scaffold with divergent substrates. The grouping includes conventional nucleoside deaminases and blasticidin-S deaminases, as well as plant relatives whose catalytic competence is uncertain.

The actual SF2 inventory contains Aspergillus blasticidin-S deaminase P0C2P0 alongside cytidine deaminases. Substrate/intermediate/product structures establish deamination of the antibiotic's cytosine moiety (PMID:17959604), demonstrating that the same broad family and SF2 label do not uniquely identify free-cytidine salvage. Plant CDA4/CDA9 inactive labels remain hypotheses unless their catalytic architecture is independently verified; they are not used as proof of exact-target loss. CG8353's cytidine-deaminase assignment supports a deamination hypothesis but does not license RNA editing, dCMP deamination or every antibiotic substrate.

**Exact benchmark/reference members:** DROME/CG8353 (Q9VLR2)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11644/PTHR11644-review.yaml)

## PTHR11669

**REPLICATION FACTOR C / DNA POLYMERASE III GAMMA-TAU SUBUNIT** — HETEROGENEOUS; COMPLETE

Clamp-loader-related ATPases assemble sliding clamps on nucleic acids to support processive DNA synthesis and repair. Eukaryotic RFC complexes combine several small subunits with alternative large subunits; related bacterial clamp-loader components and plant Stichel proteins broaden the family beyond one canonical replication complex.

The inventory combines RFC small subunits with bacterial gamma/tau and delta-prime clamp-loader components; the broader classification also includes plant Stichel. Pombe rfc3 maps to the official RFC5 subfamily, so symbol numbers do not identify orthologous subunits. Clamp loading is coordinated by an assembled complex, and ATP binding, ATP hydrolysis and autonomous clamp loading cannot be assigned identically to every component.

**Exact benchmark/reference members:** SCHPO/rfc3 (O14003)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA clamp loader activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003689) (GO:0003689) | UNRESOLVED | RFC clamp loading is a complex activity. A gene-level contributes_to interpretation is appropriate for core small subunits; family-wide autonomous clamp loading would overstate both mechanism and scope. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11669/PTHR11669-review.yaml)

## PTHR11711

**Arf/Arl small GTPases and associated domain fusions** — HETEROGENEOUS; COMPLETE

Arf and Arl proteins are nucleotide-regulated molecular switches associated with membrane traffic and other spatially organized processes. The wider group includes divergent Arl proteins and multidomain fusions such as TRIM23.

The Xenopus sequence's Arf-family placement supports a small-GTPase comparison. ADP-ribosylation is not its enzymatic reaction despite the family name. Vesicle coat recruitment, ciliary traffic and E3 activity of a fused TRIM protein are separable branch-specific functions.

**Exact benchmark/reference members:** XENTR/F6WPT1 (F6WPT1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [GTPase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003924) (GO:0003924) | UNRESOLVED | The Xenopus ARL5-related protein has an Arf small-GTPase domain, supporting a guanine-nucleotide switch hypothesis. Hydrolysis requires a complete catalytic G-domain and may depend strongly on the appropriate GAP; GTP binding alone is insufficient. Divergent Arl proteins and TRIM fusions require separate catalytic assessment, and neither ADP-ribosylation nor E3 activity follows from the shared family name. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11711/PTHR11711-review.yaml)

## PTHR11712

**POLYKETIDE SYNTHASE-RELATED** — HETEROGENEOUS; COMPLETE

Beta-ketoacyl synthases extend acyl chains by condensation with activated malonyl donors. Related enzymes serve bacterial and organellar fatty-acid synthesis as well as specialized polyketide pathways. Product length and pathway context depend on the enzyme and its surrounding biosynthetic machinery. Related noncatalytic chain-length factors partner with the catalytic ketosynthase in aromatic polyketide synthesis.

The inventory includes mitochondrial Cem1, bacterial and plastid fatty-acid ketosynthases, and aromatic polyketide synthase alpha and beta components. Experimental chain-length-factor work separates the noncatalytic beta component from the condensing enzyme (PMID:14558809). Thus even the shared ketosynthase architecture does not confer condensation chemistry on every member. Pombe Cem1 is an SF336 mitochondrial fatty-acid-synthesis comparison, not a polyketide antibiotic assignment.

**Exact benchmark/reference members:** SCHPO/cem1 (O94297)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [3-oxoacyl-[acyl-carrier-protein] synthase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004315) (GO:0004315) | UNRESOLVED | The inventory includes mitochondrial Cem1, bacterial and plastid fatty-acid ketosynthases, and aromatic polyketide synthase alpha and beta components. Experimental chain-length-factor work separates the noncatalytic beta component from the condensing enzyme (PMID:14558809). Thus even the shared ketosynthase architecture does not confer condensation chemistry on every member. Pombe Cem1 is an SF336 mitochondrial fatty-acid-synthesis comparison, not a polyketide antibiotic assignment. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11712/PTHR11712-review.yaml)

## PTHR11728

**GLYCEROL-3-PHOSPHATE DEHYDROGENASE** — MOSTLY_COHERENT; COMPLETE

NAD(P)-dependent glycerol-3-phosphate dehydrogenases interconvert dihydroxyacetone phosphate and glycerol-3-phosphate while coupling to pyridine-nucleotide redox chemistry. Related paralogs serve glycerolipid metabolism, redox shuttling or lineage-specific glycerol production. They are distinct from the FAD-dependent mitochondrial shuttle enzyme.

The inventory contains both NAD- and NADP-using glycerol-3-phosphate dehydrogenases in cytosolic, glycosomal, plastid and mitochondrial contexts. Gpdh3/E1JIT1 has both N- and C-terminal NAD-dependent G3P-dehydrogenase domain signatures, supporting the enzymatic class despite its extension. Those signatures do not establish identical substrate affinity, regulation or physiological flux to Gpdh1, and NAD specificity cannot be granted to every family member.

**Exact benchmark/reference members:** DROME/Gpdh3 (E1JIT1)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11728/PTHR11728-review.yaml)

## PTHR11733

**ZINC METALLOPROTEASE FAMILY M13 NEPRILYSIN-RELATED** — HETEROGENEOUS; COMPLETE

M13 metallopeptidase relatives include neprilysins, endothelin-converting enzymes, PHEX and other extracellular or membrane-associated proteins. Characterized enzymes share a zinc-dependent proteolytic framework while differing substantially in peptide substrate selection and biological role.

M13 proteins include active zinc endopeptidases and divergent neprilysin-like proteins. The fly family analysis distinguishes seven Nep genes retaining the catalytic motifs from 21 Nepl genes predicted to lack catalytic competence; biochemical activity had been demonstrated for only a subset of Nep proteins (PMID:34189422). Metal-site mutagenesis establishes that altered ligands can abolish or greatly reduce NEP catalysis (PMID:8099556), while ECE-1 structure documents a related fold with a distinct peptide-processing role (PMID:18992253). Thus Nepl19 cannot inherit peptidase activity solely from its M13 assignment. Exact-target motif integrity and sequence completeness are separate requirements; neither universal activity nor universal inactivity is asserted.

**Exact benchmark/reference members:** DROME/Nepl19 (Q9VAS1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [peptidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008233) (GO:0008233) | UNRESOLVED | M13 proteins include active zinc endopeptidases and divergent neprilysin-like proteins. The fly family analysis distinguishes seven Nep genes retaining the catalytic motifs from 21 Nepl genes predicted to lack catalytic competence; biochemical activity had been demonstrated for only a subset of Nep proteins (PMID:34189422). Metal-site mutagenesis establishes that altered ligands can abolish or greatly reduce NEP catalysis (PMID:8099556), while ECE-1 structure documents a related fold with a distinct peptide-processing role (PMID:18992253). Thus Nepl19 cannot inherit peptidase activity solely from its M13 assignment. Exact-target motif integrity and sequence completeness are separate requirements; neither universal activity nor universal inactivity is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11733/PTHR11733-review.yaml)

## PTHR11742

**MANNOSYL-OLIGOSACCHARIDE ALPHA-1,2-MANNOSIDASE-RELATED** — MOSTLY_COHERENT; COMPLETE

Class I alpha-mannosidases trim alpha-1,2-linked mannose residues from N-linked glycans. Related enzymes act at different stages of secretory-pathway glycan maturation and quality control. Their location and preferred glycan branch determine whether a particular trimming event supports productive maturation or disposal of a substrate.

Class I/GH47 alpha-mannosidases differ in secretory-pathway location and glycan-trimming specificity. Recombinant fly mas-1 was active on oligomannosidic glycans in a study that explicitly distinguished GH47 class I enzymes from GH38 class II enzymes (PMID:23979800). This establishes a characterized fly class I branch without transferring the properties of ManIIb or acidic class II enzymes to alpha-Man-Ia. The target's reviewed IA-related classification is consistent with secretory-pathway glycan processing, while ER versus Golgi residence, individual linkage preferences and completion of a whole trimming pathway are not universal family properties.

**Exact benchmark/reference members:** DROME/alpha-Man-Ia (P53624)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11742/PTHR11742-review.yaml)

## PTHR11753

**ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY** — HETEROGENEOUS; COMPLETE

Sigma adaptins are small subunits of heterotetrameric adaptor complexes involved in membrane cargo sorting. AP-1, AP-2, AP-3 and AP-4 complexes use related sigma subunits at different membrane compartments. Their shared structural role does not identify a single vesicle destination.

The inventory contains sigma subunits of AP-1 through AP-4, which share cargo-adaptor architecture but operate in different trafficking pathways. The curated pombe Vas2 assignment supports AP-1 participation at the Golgi/endosome interface. Neither plasma-membrane endocytosis nor clathrin recruitment can be inherited as a universal sigma-adaptin function, and an isolated sigma chain is not the entire cargo-sorting complex.

**Exact benchmark/reference members:** SCHPO/vas2 (Q9P7N2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [AP-1 adaptor complex](https://www.ebi.ac.uk/QuickGO/term/GO:0030121) (GO:0030121) | UNRESOLVED | IPR016635 emphasizes AP-1, but the PANTHER subfamily list also contains AP-2, AP-3 and AP-4 sigma chains. Pombe Vas2 should be assigned AP-1-specific Golgi/endosome functions from its complex evidence. Plasma-membrane endocytosis, clathrin association and specialized cell-to-cell transport are not automatic family functions. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11753/PTHR11753-review.yaml)

## PTHR11782

**ADENOSINE/GUANOSINE DIPHOSPHATASE** — HETEROGENEOUS; COMPLETE

NTPDase/apyrase-related enzymes hydrolyze nucleoside di- and triphosphates. Members operate extracellularly or in secretory compartments, with different preferences for ATP, ADP, UDP, GDP and other nucleotides. These differences connect the family to either extracellular nucleotide signaling or organellar glycosylation and nucleotide metabolism.

NTPDase/apyrase proteins share nucleotide-phosphate hydrolysis but differ in substrate preference and membrane orientation. Direct characterization of the single fly NTPase/NTPDase6 found an intracellular, primarily ER-localized enzyme that hydrolyzes UDP, GDP and IDP efficiently, with other NDPs/NTPs poor substrates (PMID:19467631). Thus the family does not imply a cell-surface ATP-removing ectoenzyme for every member. The fly result supports a nucleotide-diphosphatase mechanism in an endomembrane context, while ATP preference, extracellular purinergic signaling and an exact glycosylation role require separate evidence.

**Exact benchmark/reference members:** DROME/NTPase (O76268)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11782/PTHR11782-review.yaml)

## PTHR11814

**SLC26/SulP anion transport and motor proteins** — HETEROGENEOUS; COMPLETE

SLC26/SulP proteins share a membrane transport fold and commonly a STAS domain. Members transport different anions with different coupling modes; the family also includes the specialized mammalian prestin motor.

The bonobo target has a multipass membrane architecture consistent with its assigned SLC26 subgroup. Sulfate, chloride, bicarbonate and organic-anion specificities cannot be interchanged. The prestin branch prevents treating ordinary anion transport as an invariant physiological function of every family member.

**Exact benchmark/reference members:** PANPA/A0A2R9CAF4 (A0A2R9CAF4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [monoatomic anion transmembrane transporter activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008509) (GO:0008509) | UNRESOLVED | SLC26A11 has direct evidence for both sulfate transport and chloride conductance. Sulfate is polyatomic, so sulfate transport alone would not support the monoatomic-anion term; the measured chloride conductance does. Other SLC26/SulP branches differ in substrate and in exchange, channel or motor specialization, so an unconditional family-wide monoatomic-anion transfer is not justified. |
| [membrane](https://www.ebi.ac.uk/QuickGO/term/GO:0016020) (GO:0016020) | UNRESOLVED | The SLC26/SulP membrane domain and the benchmark transmembrane features support a membrane-associated protein. The particular membrane can be plasma membrane or an intracellular compartment, including the demonstrated lysosomal setting of SLC26A11. The complete inventory of intact membrane-spanning products versus fragments is not resolved; no specific membrane compartment is inherited from the family label. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11814/PTHR11814-review.yaml)

## PTHR11824

**VOLTAGE-DEPENDENT CALCIUM CHANNEL BETA SUBUNIT** — COHERENT; COMPLETE

Voltage-gated calcium-channel beta subunits are cytosolic auxiliary proteins that regulate channel assembly, trafficking and gating through interaction with pore-forming alpha1 subunits. Their SH3/guanylate-kinase-like architecture supports protein interactions. It does not create a calcium-conducting pore or establish guanylate-kinase catalysis.

The reviewed human CACNB3 record and calcium-channel-beta classification support channel regulation. Different beta paralogs and splice forms tune different channel complexes, so an L-type complex cannot be assumed for all members. The distinction between regulatory-subunit activity and contributing to a channel complex is mechanistically essential.

**Exact benchmark/reference members:** HORSE/CACNB3 (A0A5F5PZM5), human/CACNB3 (P54284)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [calcium channel regulator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0005246) (GO:0005246) | FAMILY_WIDE | The reviewed human CACNB3 record and calcium-channel-beta classification support channel regulation. Different beta paralogs and splice forms tune different channel complexes, so an L-type complex cannot be assumed for all members. The distinction between regulatory-subunit activity and contributing to a channel complex is mechanistically essential. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11824/PTHR11824-review.yaml)

## PTHR11825

**SUBGROUP IIII AMINOTRANSFERASE** — MOSTLY_COHERENT; COMPLETE

Branched-chain amino-acid aminotransferases reversibly exchange amino groups between branched-chain amino acids and their ketoacids using pyridoxal phosphate. Cytosolic, mitochondrial and microbial members retain related chemistry while serving different metabolic directions and compartments.

The PANTHER subfamily inventory comprises branched-chain aminotransferase, BCAT1 and BCAT2 groups. Rat BCAT2 expression directly produces branched-chain aminotransferase activity with processing of its mitochondrial targeting sequence (PMID:9165094); the human ortholog and reviewed substrate chemistry support the same broad reaction. This supports the reaction across intact members, while the shared class-IV PLP fold alone would not: mitochondrial location, catabolic direction and physiological substrate flux differ among lineages.

**Exact benchmark/reference members:** HORSE/BCAT2 (A0A9L0TSN4), human/BCAT2 (O15382)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [branched-chain-amino-acid:2-oxoglutarate transaminase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004084) (GO:0004084) | FAMILY_WIDE | The PANTHER subfamily inventory comprises branched-chain aminotransferase, BCAT1 and BCAT2 groups. Rat BCAT2 expression directly produces branched-chain aminotransferase activity with processing of its mitochondrial targeting sequence (PMID:9165094); the human ortholog and reviewed substrate chemistry support the same broad reaction. This supports the reaction across intact members, while the shared class-IV PLP fold alone would not: mitochondrial location, catabolic direction and physiological substrate flux differ among lineages. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11825/PTHR11825-review.yaml)

## PTHR11863

**STEROL DESATURASE** — HETEROGENEOUS; COMPLETE

This membrane oxidoreductase grouping includes cholesterol hydroxylases, sterol desaturases and other lipid-modifying enzymes. CH25H converts cholesterol to 25-hydroxycholesterol, a reaction distinct from sterol C4 demethylation or introduction of a sterol double bond. Related metal-dependent architectures do not make these reactions interchangeable.

Mouse and human CH25H cDNAs encode cholesterol 25-hydroxylases with experimentally required histidine clusters (PMID:9852097). This side-chain hydroxylation differs from C4 methylsterol oxidation and C5 desaturation in other branches of the sterol-enzyme grouping. C4 methylsterol oxidase activity is therefore not a family-wide grant and is not supported for CH25H; the exact positively supported sterol-oxidase subfamily set remains unresolved.

**Exact benchmark/reference members:** HORSE/CH25H (F6T000), human/CH25H (O95992)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [C-4 methylsterol oxidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0000254) (GO:0000254) | UNRESOLVED | Mouse and human CH25H cDNAs encode cholesterol 25-hydroxylases with experimentally required histidine clusters (PMID:9852097). This side-chain hydroxylation differs from C4 methylsterol oxidation and C5 desaturation in other branches of the sterol-enzyme grouping. C4 methylsterol oxidase activity is therefore not a family-wide grant and is not supported for CH25H; the exact positively supported sterol-oxidase subfamily set remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11863/PTHR11863-review.yaml)

## PTHR11935

**BETA LACTAMASE DOMAIN** — HETEROGENEOUS; COMPLETE

Glyoxalase-II-related metallohydrolases include hydroxyacylglutathione hydrolases and divergent PNKD proteins. Classical glyoxalase II hydrolyzes S-lactoylglutathione in methylglyoxal detoxification. Human PNKD-L shows very low turnover of this substrate and fails to restore its metabolism in a fly HAGH-null background, establishing a functional boundary despite the related fold.

The PNKD study (PMID:21487022) directly compares purified HAGH and PNKD-L and tests transgenic complementation. Low residual in vitro activity does not establish physiological S-lactoylglutathione metabolism. Rat Pnkd belongs to the PNKD-related subfamily, making this a specific ortholog-supported warning against glyoxalase-II substrate transfer, rather than a claim that all catalytic activity has been lost.

**Exact benchmark/reference members:** rat/Pnkd (B4F7D2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [hydroxyacylglutathione hydrolase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004416) (GO:0004416) | UNRESOLVED | HAGH is a genuine positive enzyme example, whereas PNKD-L has very low residual activity and fails physiological complementation of HAGH. A family-wide substrate grant is therefore unsafe. The complete set of substrate-competent branches is not established; low residual in-vitro turnover is not equivalent to absolute catalytic loss. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11935/PTHR11935-review.yaml)

## PTHR11952

**UDP- GLUCOSE PYROPHOSPHORYLASE** — HETEROGENEOUS; COMPLETE

UDP-sugar pyrophosphorylase relatives activate sugar phosphates with UTP to supply nucleotide-sugar donors. UAP1-type proteins act on N-acetylhexosamine phosphates, while other branches use different sugars. The identity and stereochemistry of the sugar phosphate determine the biochemical annotation.

Direct recombinant UAP1 enzymology and human UDP-GlcNAc/UDP-GalNAc-bound structures establish an N-acetylhexosamine branch distinct from UDP-glucose pyrophosphorylase. The frog target retains all annotated human nucleotide-sugar contacts and lacks a 17-residue segment present in the longer human isoform; that difference does not establish a frog-specific substrate ratio.

**Exact benchmark/reference members:** XENLA/uap1.S (Q6DCZ6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [UDP-N-acetylglucosamine diphosphorylase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003977) (GO:0003977) | UNRESOLVED | The UAP1 branch has direct enzymatic support and the frog SF4 representative preserves its substrate-pocket architecture. The broad family also includes different UDP-sugar specificities, and the complete set of GlcNAc-active subfamilies is not enumerated. Thus no universal or falsely exhaustive subfamily grant is made. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11952/PTHR11952-review.yaml)

## PTHR11972

**NADPH OXIDASE** — HETEROGENEOUS; COMPLETE

NADPH oxidase and ferric-reductase relatives transfer electrons across membranes through flavin and heme cofactors. NOX/DUOX branches generate reactive oxygen species, whereas ferric reductases reduce extracellular or organellar metal substrates. DUOX proteins additionally carry extracellular peroxidase-like regions and calcium-responsive regulatory elements.

The reviewed DUOX1 record supports peroxide production, but a peroxidase-like region is not proof of intrinsic heme-peroxidase activity. Ferric reduction, superoxide production and hydrogen-peroxide production must be assigned to the appropriate branch. Oxidant generation should not be reinterpreted as oxidant detoxification solely because both involve reactive oxygen species.

**Exact benchmark/reference members:** HORSE/DUOX1 (A0A9L0SQG9), human/DUOX1 (Q9NRD9)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [peroxidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004601) (GO:0004601) | UNRESOLVED | The human DUOX1 record explicitly records conflicting studies: an isolated peroxidase-like domain showed activity in one study (PMID:11514595), whereas a later study found no heme binding or intrinsic peroxidase activity (PMID:19460756). Thus the inference is contested by experimental evidence, not merely unsupported by the domain label. The broad NOX/ferric-reductase family cannot carry this activity universally; species, construct and heme incorporation must be resolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11972/PTHR11972-review.yaml)

## PTHR12064

**CNNM/ACDP membrane proteins** — HETEROGENEOUS; COMPLETE

CNNM/ACDP proteins contain a membrane region and cytosolic regulatory architecture associated with metal-ion homeostasis. Mammalian CNNMs and fungal or plant homologs differ in membrane destination and physiological context.

CNNM4 basolateral localization supports a mammalian CNNM4 comparison for the dog target. A family signature alone cannot distinguish direct ion translocation from regulation of a transport system or establish the transported ion and coupling mechanism. Plasma membrane localization is not a universal conclusion for the fungal and plant homologs.

**Exact benchmark/reference members:** CANLF/A0A8I3PI07 (A0A8I3PI07)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [plasma membrane](https://www.ebi.ac.uk/QuickGO/term/GO:0005886) (GO:0005886) | UNRESOLVED | CNNM4 localization to basolateral membranes in intestinal epithelia and ameloblasts supplies direct plasma-membrane evidence. Other CNNM homologs differ in cell type and membrane targeting. The dog architecture supports a membrane protein but does not independently establish its organelle or sidedness. |
| [transmembrane transporter activity](https://www.ebi.ac.uk/QuickGO/term/GO:0022857) (GO:0022857) | UNRESOLVED | The CNNM4 study reports Mg2+ extrusion and exchange with extracellular Na+, providing functional transport evidence. Direct permeation versus regulation of another transporter must be distinguished when transferring mechanism to other CNNMs. The presence of membrane-spanning regions and CBS-associated architecture does not settle that mechanistic boundary across the family. |
| [monoatomic ion transport](https://www.ebi.ac.uk/QuickGO/term/GO:0006811) (GO:0006811) | UNRESOLVED | The CNNM4 knockout and imaging experiments support a role in Mg2+ transport and organismal magnesium homeostasis. That process can remain valid whether a homolog directly conducts ions or regulates the conducting machinery. Conservation of a specific ion and physiological transport role across all CNNM branches is not established. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12064/PTHR12064-review.yaml)

## PTHR12210

**DULLARD PROTEIN PHOSPHATASE** — HETEROGENEOUS; COMPLETE

FCP/SCP-like phosphatase-domain proteins in this family serve distinct cellular roles. CTD small phosphatases such as CTDSP2 dephosphorylate protein substrates associated with transcriptional regulation, whereas TIM50-family proteins participate in mitochondrial precursor import. Shared phosphatase-like architecture does not make all members mitochondrial translocase subunits.

Small CTD phosphatases preferentially dephosphorylate RNAPII CTD Ser5 in biochemical assays, with the most detailed mechanism established for SCP1 (PMID:12721286). CTDSP2 belongs to this phosphatase branch, whereas TIM50-related members participate in mitochondrial precursor import. Neither phosphatase catalysis nor import-complex participation follows universally from the shared phosphatase-like fold; the exact CTD-phosphatase branch set remains unresolved.

**Exact benchmark/reference members:** human/CTDSP2 (O14595)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [RNA polymerase II CTD heptapeptide repeat phosphatase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008420) (GO:0008420) | UNRESOLVED | Small CTD phosphatases preferentially dephosphorylate RNAPII CTD Ser5 in biochemical assays, with the most detailed mechanism established for SCP1 (PMID:12721286). CTDSP2 belongs to this phosphatase branch, whereas TIM50-related members participate in mitochondrial precursor import. Neither phosphatase catalysis nor import-complex participation follows universally from the shared phosphatase-like fold; the exact CTD-phosphatase branch set remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12210/PTHR12210-review.yaml)

## PTHR12242

**OS02G0130600 PROTEIN-RELATED** — UNKNOWN; COMPLETE

This membrane-protein grouping includes fly Headbutt and Rolling stone in distinct subfamilies, alongside plant membrane-protein descriptors. Rolling stone is required for myoblast fusion; no common transport reaction or lipid substrate is established across the grouping.

Fly Rolling stone is a membrane-associated protein whose mesodermal expression is required for myoblast fusion (PMID:9230076). This direct genetic result provides a positive biological role for the verified SF46 member O44252, while Headbutt Q9VK03 belongs to SF49 and has a multipass membrane architecture. Neither membrane topology nor the TLC/MARVEL-related labels establish an intrinsic solute transporter or lipid enzyme. A conserved molecular mechanism linking these branches remains unknown; the phenotype of Rolling stone is not treated as evidence that Headbutt is itself a fusogen.

**Exact benchmark/reference members:** DROME/hbt (Q9VK03)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12242/PTHR12242-review.yaml)

## PTHR12311

**ACTIVATOR OF BASAL TRANSCRIPTION 1** — MOSTLY_COHERENT; COMPLETE

ABT1/Esf2 proteins are nuclear interaction factors linked to RNA production and ribosome biogenesis. Yeast Esf2 binds pre-rRNA, participates in U3/90S small-subunit biogenesis and stimulates the helicase Dbp8. The conserved molecular role is better defined by these RNA-processing interactions than by a generic transcription-associated name.

Yeast Esf2 is a nucleolar U3/90S-associated factor required for early pre-rRNA cleavage and 18S production (PMID:15964808). It binds pre-rRNA and stimulates the ATPase activity of the interacting helicase Dbp8 (PMID:16772403), distinguishing an assembly/RNA cofactor from an intrinsic ATPase or nuclease. These experiments support an SSU-biogenesis mechanism for the characterized branch; the ABT1-associated transcription narrative and uncharacterized fly CG32706 do not establish an exhaustive family-wide processome-assembly grant.

**Exact benchmark/reference members:** DROME/CG32706 (Q8IRM9)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [small-subunit processome assembly](https://www.ebi.ac.uk/QuickGO/term/GO:0034462) (GO:0034462) | UNRESOLVED | Yeast Esf2 is a nucleolar U3/90S-associated factor required for early pre-rRNA cleavage and 18S production (PMID:15964808). It binds pre-rRNA and stimulates the ATPase activity of the interacting helicase Dbp8 (PMID:16772403), distinguishing an assembly/RNA cofactor from an intrinsic ATPase or nuclease. These experiments support an SSU-biogenesis mechanism for the characterized branch; the ABT1-associated transcription narrative and uncharacterized fly CG32706 do not establish an exhaustive family-wide processome-assembly grant. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12311/PTHR12311-review.yaml)

## PTHR12363

**TRANSPORTIN 3 AND IMPORTIN 13** — HETEROGENEOUS; COMPLETE

Importin-beta-like receptors bind selected cargoes and mediate nucleocytoplasmic transport. This family includes importin-13 and transportin-3/Mtr10-related branches, with different cargo preferences and potentially different transport directions for particular substrates. Ran-dependent cargo exchange couples transport to the nuclear compartment.

Importin-13 is a bidirectional Ran-dependent transport receptor whose import and export cargoes differ (PMID:11447110); its MAGO-Y14 import complex has a defined structural recognition mechanism (PMID:20122403). Related transport receptors recognize different cargo surfaces. Bidirectional nuclear transport is not synonymous with recognition of a canonical nuclear-export-signal peptide, and Ran supplies the GTPase cycle rather than an intrinsic receptor ATPase. The distribution of GO:0005049 across this family remains unresolved despite positive evidence for transport by characterized members.

**Exact benchmark/reference members:** DROME/cdm (Q9VEC5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [nuclear export signal receptor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0005049) (GO:0005049) | UNRESOLVED | Importin-13 is a bidirectional Ran-dependent transport receptor whose import and export cargoes differ (PMID:11447110); its MAGO-Y14 import complex has a defined structural recognition mechanism (PMID:20122403). Related transport receptors recognize different cargo surfaces. Bidirectional nuclear transport is not synonymous with recognition of a canonical nuclear-export-signal peptide, and Ran supplies the GTPase cycle rather than an intrinsic receptor ATPase. The distribution of GO:0005049 across this family remains unresolved despite positive evidence for transport by characterized members. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12363/PTHR12363-review.yaml)

## PTHR12444

**PROTEIN EFR3 HOMOLOG CMP44E** — MOSTLY_COHERENT; COMPLETE

EFR3 proteins anchor phosphatidylinositol-4-kinase-associated assemblies at the plasma membrane. Their conserved role is recruitment and organization of a lipid-kinase complex, allowing membrane phosphoinositide synthesis to occur at the correct location. EFR3A and EFR3B represent closely related mammalian branches.

The experimentally annotated human EFR3A record supports plasma-membrane recruitment of the PI4K complex. Participation in phosphatidylinositol-phosphate synthesis does not confer intrinsic lipid-kinase or lipase activity on EFR3. Effects on receptor signaling or synaptic physiology require the relevant organism and cellular context.

**Exact benchmark/reference members:** HORSE/EFR3A (A0A9L0S4L8), human/EFR3A (Q14156)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein localization to plasma membrane](https://www.ebi.ac.uk/QuickGO/term/GO:0072659) (GO:0072659) | FAMILY_WIDE | The experimentally annotated human EFR3A record supports plasma-membrane recruitment of the PI4K complex. Participation in phosphatidylinositol-phosphate synthesis does not confer intrinsic lipid-kinase or lipase activity on EFR3. Effects on receptor signaling or synaptic physiology require the relevant organism and cellular context. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12444/PTHR12444-review.yaml)

## PTHR12449

**DEATH DOMAIN-CONTAINING PROTEIN** — UNKNOWN; COMPLETE

NOL4-family proteins are nuclear interaction proteins with isoform-dependent regulatory activities demonstrated in mammals. Mouse NOL4 splice variants bind the Mlr1/Mlr2 transcription factors and alter their transcriptional output; the conserved molecular role of the divergent fly CG46301 product remains unresolved.

Mouse NOL4 variants interact differently with Mlr1 and Mlr2, and deletion of an NLS-containing region changes both binding and the direction of transcriptional regulation (PMID:25366156). The reporter host was Drosophila S2 cells, but the assayed regulatory proteins were mouse proteins; this is not a direct fly CG46301 functional experiment. The long fly protein shares family classification, without evidence that it uses the same partners or is a death receptor despite the domain-dominated family label. Coherence remains unknown at the level of a conserved molecular mechanism, rather than implying that no member has been studied.

**Exact benchmark/reference members:** DROME/CG46301 (A0A1W5PXH3)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12449/PTHR12449-review.yaml)

## PTHR12450

**DENTIN MATRIX PROTEIN 4  PROTEIN FAM20** — HETEROGENEOUS; COMPLETE

FAM20 proteins share a secretory-pathway kinase-like architecture but diverge in catalytic output. FAM20B phosphorylates xylose in the glycosaminoglycan linkage region; FAM20C phosphorylates secreted proteins; FAM20A is a regulatory pseudokinase that supports FAM20C function. Sugar phosphorylation and protein phosphorylation are distinct activities.

Human FAM20B enzymology directly establishes phosphorylation of glycan-linked xylose (PMID:19473117), whereas FAM20C acts on proteins and FAM20A is its regulatory pseudokinase partner. CG3631/Q95T10 has an SF14 assignment and a curated inference from human FAM20B O75063, not a fly substrate assay. The inventory also contains fly CG31145 and worm CeFam20 protein kinases; SF11 is therefore not an exhaustive protein-kinase boundary.

**Exact benchmark/reference members:** DROME/CG3631 (Q95T10)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein serine/threonine kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004674) (GO:0004674) | UNRESOLVED | FAM20C protein phosphorylation is supported directly by structural and biochemical studies, whereas FAM20B phosphorylates glycan-bound xylose and FAM20A regulates FAM20C without supplying that catalytic reaction. The classification also includes a separate fly CG31145 protein-kinase branch and less characterized FAM20-domain proteins. The human-named FAM20C subfamily is therefore not established as an exhaustive allowed set. A complete phylogenetic and substrate-evidence boundary is needed for the machine-readable scope; the protein-kinase versus glycan-kinase versus pseudokinase distinction remains well supported. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12450/PTHR12450-review.yaml)

## PTHR12469

**PROTEIN EMI5 HOMOLOG, MITOCHONDRIAL** — COHERENT; COMPLETE

SDHAF2/Sdh5/SdhE proteins promote maturation of the succinate-dehydrogenase flavoprotein, particularly covalent flavinylation. They help establish a catalytically competent flavoprotein rather than serving as the respiratory substrate-oxidizing enzyme. The same assembly principle spans mitochondrial and bacterial systems.

The conserved biological role is flavoprotein maturation, supported by human SDHA-SDHAF2 structure/reconstitution and mouse myocyte rescue experiments. Assembly-factor action is distinct from the electron-transfer reaction of the mature complex. The selected short mouse product retains its targeting peptide but has an altered C-terminal region, so full assembly activity cannot be assumed for that product.

**Exact benchmark/reference members:** mouse/Sdhaf2 (A0A494B8X4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein-FAD linkage](https://www.ebi.ac.uk/QuickGO/term/GO:0018293) (GO:0018293) | UNRESOLVED | Covalent flavin attachment is directly supported for characterized intact SDHAF2 proteins. The family-level maturation mechanism is coherent, but the selected mouse product lacks the intact reference C-terminal segment. This assessment does not grant full activity to every partial or alternative product and does not assert catalytic loss solely from shorter length. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12469/PTHR12469-review.yaml)

## PTHR12480

**JMJD4/JMJD6/JMJD8-related JmjC proteins** — HETEROGENEOUS; COMPLETE

This family includes JMJD4, JMJD6, JMJD8 and plant JMJ20/JMJ22-like proteins. JmjC architecture unites the group but does not establish a common substrate, chromatin role or developmental pathway.

The wheat target and Arabidopsis JMJ22 share an F-box/JmjC architecture and an assigned subfamily, supporting a focused comparison. Plant light and gibberellin phenotypes require orthology and regulatory-context evidence; they do not apply to animal JMJD4/JMJD6/JMJD8. Histone arginine demethylation must be distinguished from other oxygenase activities.

**Exact benchmark/reference members:** WHEAT/A0A3B6RKV1 (A0A3B6RKV1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [regulation of photomorphogenesis](https://www.ebi.ac.uk/QuickGO/term/GO:0010099) (GO:0010099) | UNRESOLVED | Arabidopsis JMJ20/JMJ22 act downstream of light-activated PHYB in the cited germination experiments. The wheat F-box/JmjC architecture makes this plant branch a relevant comparison, while JMJD4/6/8 and other JmjC proteins are not thereby assigned a photomorphogenesis role. Conservation of the PHYB-regulated circuit and the complete positive plant branch boundary remain unresolved. |
| [gibberellin mediated signaling pathway](https://www.ebi.ac.uk/QuickGO/term/GO:0010476) (GO:0010476) | UNRESOLVED | The JMJ20/JMJ22 study links these proteins to increased gibberellic acid through GA3ox1/GA3ox2 regulation. That establishes a hormone-metabolism connection; it does not automatically identify every homolog as a component of the gibberellin signal-transduction pathway. Resolve biosynthesis versus signal reception/transduction and conserved plant regulatory context before transfer. |
| [epigenetic regulation of gene expression](https://www.ebi.ac.uk/QuickGO/term/GO:0040029) (GO:0040029) | UNRESOLVED | The cited plant study reports removal of repressive histone arginine methylation at GA3ox loci, providing a specific chromatin-regulatory example. JmjC fold conservation alone does not establish histone substrate choice or an epigenetic mechanism in the wheat target or the animal JMJD branches. The biochemical substrate and locus-specific regulation delimit this hypothesis. |
| [response to red light](https://www.ebi.ac.uk/QuickGO/term/GO:0010114) (GO:0010114) | UNRESOLVED | PHYB activation supplies a direct red-light pathway context for Arabidopsis JMJ20/JMJ22. It is an organism-level upstream input, not a shared light-sensing property of a JmjC catalytic domain. A red-light response cannot be granted across nonplant branches or untested plant paralogs. |
| [positive regulation of seed germination](https://www.ebi.ac.uk/QuickGO/term/GO:0010030) (GO:0010030) | UNRESOLVED | The Arabidopsis paper directly identifies redundant positive effects of JMJ20 and JMJ22 on seed germination. That is stronger than a generic JmjC analogy but remains a plant regulatory-branch result. The wheat comparison requires orthology and preservation of seed expression and the GA3ox/PHYB context; no exhaustive germination-positive subfamily set is established. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12480/PTHR12480-review.yaml)

## PTHR12514

**ENY2/Sus1 transcription and mRNA export adaptors** — COHERENT; COMPLETE

ENY2/Sus1 proteins couple transcription and nuclear mRNA export through membership in SAGA and TREX-2. Within SAGA they support the histone H2B deubiquitination module; within TREX-2 they help connect export machinery to the nuclear pore. These are small noncatalytic complex subunits, so SAGA membership does not confer intrinsic histone acetyltransferase or deubiquitinase activity.

The ENY2/Sus1 inventory and curated IPR018783 support shared roles in SAGA and TREX-2. Sus1 is a noncatalytic component of the H2B deubiquitination module and an export-associated interaction scaffold. Calling it a transcription factor does not establish sequence-specific DNA binding; SAGA membership does not establish intrinsic acetyltransferase or deubiquitinase activity.

**Exact benchmark/reference members:** SCHPO/sus1 (Q7LL15)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [mRNA export from nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0006406) (GO:0006406) | FAMILY_WIDE | The curated InterPro entry and the ENY2/Sus1 member inventory consistently identify the same dual complex-associated function in fungi and animals. Individual developmental phenotypes and gene targets are more restricted than this conserved molecular role. |
| [SAGA complex](https://www.ebi.ac.uk/QuickGO/term/GO:0000124) (GO:0000124) | FAMILY_WIDE | The curated InterPro entry and the ENY2/Sus1 member inventory consistently identify the same dual complex-associated function in fungi and animals. Individual developmental phenotypes and gene targets are more restricted than this conserved molecular role. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12514/PTHR12514-review.yaml)

## PTHR12563

**GPAT/DAPAT lipid acyltransferases** — HETEROGENEOUS; COMPLETE

This family contains glycerol-3-phosphate acyltransferases and dihydroxyacetone phosphate acyltransferases, which initiate different branches of glycerolipid synthesis. Human GPAM/GPAT1 transfers an acyl group to glycerol-3-phosphate at the mitochondrial outer membrane. Its experimentally determined membrane association uses an amphipathic surface rather than the transmembrane topology formerly proposed.

The member inventory includes bacterial PlsB, mitochondrial GPAT1/GPAT2 and DAPAT proteins. Shared acyl transfer does not establish identical acceptor specificity, organelle localization or acyl-chain preference. The GPAT1 structure supports GPAM inference but does not establish the same substrate preference for every family member.

**Exact benchmark/reference members:** HORSE/GPAM (A0A9L0TTC1), human/GPAM (Q9HCL2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [acyltransferase activity, transferring groups other than amino-acyl groups](https://www.ebi.ac.uk/QuickGO/term/GO:0016747) (GO:0016747) | FAMILY_WIDE | The member inventory includes bacterial PlsB, mitochondrial GPAT1/GPAT2 and DAPAT proteins. Shared acyl transfer does not establish identical acceptor specificity, organelle localization or acyl-chain preference. The GPAT1 structure supports GPAM inference but does not establish the same substrate preference for every family member. |
| [glycerol-3-phosphate O-acyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004366) (GO:0004366) | UNRESOLVED | The GPAM/GPAT1 branch in SF16 has directly demonstrated glycerol-3-phosphate acyltransferase activity. The family also contains GPAT2 and bacterial PlsB proteins, so this activity is not exclusive to SF16. DAPAT proteins introduce a different acceptor specificity. The exhaustive set of substrate-compatible branches remains unresolved; the GPAT1 experiment establishes a positive example rather than an exclusion of other GPAT enzymes. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12563/PTHR12563-review.yaml)

## PTHR12566

**CPEB translational regulators** — MOSTLY_COHERENT; COMPLETE

CPEB proteins bind regulatory elements in mRNA 3-prime untranslated regions and control translation through cytoplasmic polyadenylation and repression mechanisms. Their conserved RNA-binding region combines RNA recognition motifs with a zinc-binding domain. Orb and the CPEB paralogs have different mRNA targets and developmental deployments, while the shared activity is post-transcriptional regulation rather than transcription factor activity.

CPEB proteins regulate translation through sequence-selective RNA recognition and assembly of regulatory complexes. Human CPEB structures establish the tandem-RRM/ZZ RNA-recognition architecture (PMID:24990967), and fly Orb/Orb2 CLIP establishes CPE-like RNA targets (PMID:27791065). Mechanisms differ even between Orb2 isoforms: Orb2A can supply a glutamine-rich assembly function without requiring its RNA-binding domain, whereas Orb2B requires RNA binding for memory (PMID:23083740). Broad translation regulation is conserved; direct RNA engagement by every isoform, particular target transcripts and neuronal or germline phenotypes are not interchangeable family properties.

**Exact benchmark/reference members:** DROME/orb (Q8IMZ2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [translation regulator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0045182) (GO:0045182) | FAMILY_WIDE | CPEB proteins regulate translation through sequence-selective RNA recognition and assembly of regulatory complexes. Human CPEB structures establish the tandem-RRM/ZZ RNA-recognition architecture (PMID:24990967), and fly Orb/Orb2 CLIP establishes CPE-like RNA targets (PMID:27791065). Mechanisms differ even between Orb2 isoforms: Orb2A can supply a glutamine-rich assembly function without requiring its RNA-binding domain, whereas Orb2B requires RNA binding for memory (PMID:23083740). Broad translation regulation is conserved; direct RNA engagement by every isoform, particular target transcripts and neuronal or germline phenotypes are not interchangeable family properties. |
| [regulation of translation](https://www.ebi.ac.uk/QuickGO/term/GO:0006417) (GO:0006417) | FAMILY_WIDE | CPEB proteins regulate translation through sequence-selective RNA recognition and assembly of regulatory complexes. Human CPEB structures establish the tandem-RRM/ZZ RNA-recognition architecture (PMID:24990967), and fly Orb/Orb2 CLIP establishes CPE-like RNA targets (PMID:27791065). Mechanisms differ even between Orb2 isoforms: Orb2A can supply a glutamine-rich assembly function without requiring its RNA-binding domain, whereas Orb2B requires RNA binding for memory (PMID:23083740). Broad translation regulation is conserved; direct RNA engagement by every isoform, particular target transcripts and neuronal or germline phenotypes are not interchangeable family properties. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12566/PTHR12566-review.yaml)

## PTHR12618

**PHD/RING-containing Asr1-related proteins** — UNKNOWN; COMPLETE

PHRF1-related PHD/RING proteins include poorly characterized eukaryotic interaction proteins and a Komagataella micropexophagic-apparatus component catalogued as Atg36/Atg35. Shared zinc-binding domains do not establish identical ubiquitin-ligase substrates or a conserved autophagy-receptor mechanism.

Curated IPR047157 identifies PHRF1-related proteins and a Komagataella protein catalogued as Atg36/Atg35 that contributes to micropexophagic apparatus formation. This naming does not identify the Saccharomyces Atg36 pexophagy receptor. Pombe Asr1/C126.07c lies with the PHRF1 group; RING/PHD architecture alone neither establishes its ubiquitin-ligase substrate nor transfers a distinct budding-yeast Asr1 RNA-polymerase-II mechanism.

**Exact benchmark/reference members:** SCHPO/asr1 (O94400)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12618/PTHR12618-review.yaml)

## PTHR12632

**NF-YA/Hap2 CCAAT-binding complex subunits** — COHERENT; COMPLETE

NF-YA/Hap2 proteins form the sequence-recognition component of the heteromeric CCAAT-binding transcription factor. DNA binding and transcriptional regulation depend on assembly with the other NF-Y subunits. Fungal iron and oxidative-stress responses and plant developmental functions represent deployment of this conserved transcriptional machinery in different regulatory networks.

The inventory consistently identifies NF-YA/Hap2, the CCAAT-recognition subunit of a heteromeric transcription factor. Curated IPR001289 separates its subunit-association and DNA-recognition regions. DNA recognition and transcriptional regulation require the assembled NF-Y/Hap complex; mitochondrial respiratory targets in yeast or iron-responsive circuits in particular fungi are not universal target regulons.

**Exact benchmark/reference members:** NEUCR/NCU03033 (Q7SGY4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [regulation of DNA-templated transcription](https://www.ebi.ac.uk/QuickGO/term/GO:0006355) (GO:0006355) | FAMILY_WIDE | The inventory consistently contains NF-YA or Hap2 proteins. The relevant conserved property is CCAAT-binding complex participation, not a particular iron-responsive circuit or an ability to bind promoter DNA as an isolated polypeptide. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12632/PTHR12632-review.yaml)

## PTHR12654

**GBA2 nonlysosomal glucosylceramidases** — MOSTLY_COHERENT; COMPLETE

GBA2 proteins hydrolyze glucosylceramide outside the lysosomal GBA pathway. Human isoform-expression experiments show strong activity and altered ceramide balance for isoform 1, whereas the other tested isoforms had activity near background. An assignment of the family therefore supports a glycosphingolipid-metabolism hypothesis but is insufficient to declare every alternative protein record catalytically active.

GBA2 is a nonlysosomal glucosylceramidase family whose complete membrane-associated architecture matters for activity. Expression of nine human GBA2 isoforms found only isoform 1 active in the tested fluorogenic-substrate and lipid assays (PMID:33261081), providing a direct counterexample to treating every GBA2 gene product as catalytically equivalent. The altered N terminus of the fly CG33090 benchmark isoform does not by itself prove catalytic loss, particularly when its catalytic-region sequence is retained. Conserved family chemistry is supported, but activity, substrate access and topology must be assessed on the exact product.

**Exact benchmark/reference members:** DROME/CG33090 (X2JE45)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12654/PTHR12654-review.yaml)

## PTHR12728

**Rpf2 large-subunit ribosome assembly factors** — COHERENT; COMPLETE

Rpf2 proteins are conserved Brix-domain ribosome assembly factors. Together with Rrs1 and ribosomal proteins, they participate in incorporation and maturation of the large-subunit ribonucleoprotein particle. Their role is RNA binding and preribosome assembly rather than peptide synthesis or an intrinsic rRNA-processing nuclease reaction.

Curated IPR039770 and the inventory specifically identify Rpf2, rather than an arbitrary Brix-domain protein. The conserved role is assembly of the large-subunit preribosome with Rrs1 and the 5S-ribonucleoprotein components. This supports NCU08595 large-subunit assembly by orthology, while exact pre-rRNA intermediate numbers and a catalytic nuclease activity cannot be supplied by the Brix domain.

**Exact benchmark/reference members:** NEUCR/NCU08595 (Q7SCN3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ribosomal large subunit assembly](https://www.ebi.ac.uk/QuickGO/term/GO:0000027) (GO:0000027) | FAMILY_WIDE | The curated InterPro entry specifically identifies Rpf2 rather than all Brix-domain proteins, and the sampled members are Rpf2 orthologs. Large-subunit assembly is transferable within that group; precise pre-rRNA intermediate names can differ among organisms. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12728/PTHR12728-review.yaml)

## PTHR12959

**PIGT/Gpi16 GPI transamidase subunits** — COHERENT; COMPLETE

PIGT/Gpi16 proteins are components of the endoplasmic-reticulum GPI transamidase complex that attaches glycosylphosphatidylinositol anchors to proteins. Complex membership explains participation in the attachment reaction, while the catalytic chemistry belongs to the assembled machinery and its catalytic subunit. PIGT is not a generic soluble protease simply because the complex processes a protein precursor.

Budding-yeast Gpi16 co-purifies with Gaa1 and Gpi8, and depletion blocks GPI attachment. Mammalian PIGT knockout and complex experiments establish stabilization of GAA1 and GPI8, while the human structure identifies PIGK as the catalytic subunit. These independent primary experiments support a conserved PIGT/Gpi16 accessory role, not intrinsic protease activity.

**Exact benchmark/reference members:** SCHPO/gpi16 (O94380)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [attachment of GPI anchor to protein](https://www.ebi.ac.uk/QuickGO/term/GO:0016255) (GO:0016255) | FAMILY_WIDE | The conserved role of intact PIGT/Gpi16 proteins is participation in the GPI-anchor attachment machinery, grounded by yeast purification/depletion, mammalian knockout and human structural experiments. This family-level functional inference does not transfer the intrinsic catalytic chemistry of PIGK/Gpi8 to PIGT/Gpi16. |
| [GPI-anchor transamidase complex](https://www.ebi.ac.uk/QuickGO/term/GO:0042765) (GO:0042765) | FAMILY_WIDE | The conserved role of intact PIGT/Gpi16 proteins is participation in the GPI-anchor attachment machinery, grounded by yeast purification/depletion, mammalian knockout and human structural experiments. This family-level functional inference does not transfer the intrinsic catalytic chemistry of PIGK/Gpi8 to PIGT/Gpi16. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12959/PTHR12959-review.yaml)

## PTHR13085

**SPCS2/Spc2 signal peptidase accessory subunits** — MOSTLY_COHERENT; COMPLETE

SPCS2/Spc2 proteins are membrane-associated accessory components of the eukaryotic signal peptidase complex. They promote complex activity and coordination with protein translocation, while SEC11-related subunits supply signal-peptide cleavage catalysis.

Human substrate-bound signal-peptidase structures distinguish accessory SPCS2 from catalytic SEC11A/SEC11C. The conserved family role is complex participation rather than autonomous proteolysis. The short mouse benchmark sequence is only an N-terminal segment and lacks the canonical membrane helices, so same-gene identity does not establish its incorporation into the complex.

**Separate canonical gene context:** A0A140LHW5; exact inputs remain unassigned. See [identity evidence](unassigned-cases.md).

| Function / process / component | Scope | Boundary |
|---|---|---|
| [signal peptidase complex](https://www.ebi.ac.uk/QuickGO/term/GO:0005787) (GO:0005787) | FAMILY_WIDE | Membership in the eukaryotic signal peptidase complex is the conserved family role for intact SPCS2/Spc2 proteins. This complex-membership grant does not assert intrinsic peptidase activity and cannot establish that the short benchmark product is incorporated. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13085/PTHR13085-review.yaml)

## PTHR13131

**Cystinosin cystine transporters** — COHERENT; COMPLETE

Cystinosins are membrane proteins that export cystine from the lysosomal or vacuolar lumen. The experimentally annotated Drosophila Ctns record supports a cystine/proton transport function and a role in maintaining cysteine availability during fasting. Effects on mTORC1, autophagy and metabolism follow from this transport role and are not independent transport substrates.

The cystinosin inventory, curated IPR005282 description and experimentally supported fly lysosomal transport record agree on cystine export. Cysteine availability and TORC1 responses during fasting are consequences of mobilizing lysosomal cystine; they do not establish transport of unrelated amino acids. The ERS1 comparison supports the transporter family but does not make mammalian cystinosis phenotypes universal. PMID:35175796 directly tests the fly response to cystine mobilization; proton coupling in the reaction record is separately inferred from human CTNS.

**Exact benchmark/reference members:** DROME/Ctns (Q9VCR7)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13131/PTHR13131-review.yaml)

## PTHR13195

**TRUB2-related RNA pseudouridylation proteins** — MOSTLY_COHERENT; COMPLETE

TRUB2-related proteins are associated with mitochondrial RNA pseudouridylation. Family membership supports an RNA-modification hypothesis but does not identify the RNA substrate or guarantee catalytic competence of a fragment.

The pigeon protein is only 142 residues with an N-terminal pseudouridine-synthase annotation. Published TRUB2 evidence concerns specific mitochondrial mRNA residues; it does not by itself establish tRNA pseudouridine synthase activity for this short sequence. Full-domain completeness and substrate assignment remain unresolved.

**Exact benchmark/reference members:** COLLI/A0A2I0M3K7 (A0A2I0M3K7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [tRNA pseudouridine synthase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0106029) (GO:0106029) | UNRESOLVED | The cited human TRUB2 depletion and pseudouridine-Seq study identifies specific mitochondrial mRNA targets, not a tRNA substrate. It therefore supports RNA pseudouridylation while leaving this particular tRNA activity unestablished. The pigeon product is only 142 residues with an N-terminal synthase-associated region, adding a domain-completeness problem independent of RNA substrate choice. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13195/PTHR13195-review.yaml)

## PTHR13205

**Polyprenol kinases including dolichol kinase** — MOSTLY_COHERENT; COMPLETE

Dolichol kinases phosphorylate the polyprenol carrier used in protein glycosylation and GPI-anchor synthesis, using CTP as donor. The integrated InterPro group also includes plant phytol kinases involved in tocopherol biosynthesis. The lipid substrate and metabolic pathway therefore need to be resolved independently of the shared membrane-associated kinase architecture.

Yeast sec59 mutant complementation with human DOLK and biochemical assays establish CTP-dependent dolichol phosphorylation while distinguishing it from diacylglycerol kinase. The pombe assignment is a curated ortholog inference to this experimentally grounded enzyme. The integrated polyprenol-kinase group includes other lipid substrates, so its wider structural definition is not a universal dolichol-specific grant.

**Exact benchmark/reference members:** SCHPO/sec59 (Q9Y7T6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [dolichol kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004168) (GO:0004168) | UNRESOLVED | Direct yeast and human experiments establish dolichol kinase activity, and curated pombe orthology supports its transfer to Sec59. Other polyprenol kinase branches and substrates must be distinguished rather than inferred from a broad membrane-kinase fold. The complete set of substrate-specific branches is not asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13205/PTHR13205-review.yaml)

## PTHR13283

**KRIT1 and FRMD8 FERM-domain adaptors** — HETEROGENEOUS; COMPLETE

KRIT1 and FRMD8 are FERM-domain interaction proteins with distinct partners. KRIT1 participates in the cerebral cavernous malformation signaling machinery and stabilizes endothelial junctions. FRMD8 binds iRhom proteins and protects the iRhom/ADAM17 sheddase complex from endolysosomal degradation, sustaining inflammatory and growth-factor ligand release.

KRIT1 stabilizes endothelial cell junctions through Rap1-associated interactions (PMID:21633110), whereas FRMD8 stabilizes cell-surface iRhom/ADAM17 complexes and thereby sustains ligand shedding (PMID:29897336). Both are FERM-domain interaction proteins, but neither KRIT1-specific CCM signaling nor FRMD8-dependent sheddase stability is a family-wide process.

**Exact benchmark/reference members:** HORSE/KRIT1 (A0A9L0SR44), human/KRIT1 (O00522)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13283/PTHR13283-review.yaml)

## PTHR13301

**Plant cellulose synthase and cellulose-synthase-like glycosyltransferases** — HETEROGENEOUS; COMPLETE

Plant cellulose synthases and related glycosyltransferases synthesize different glycan products. The retrieved group contains cellulose synthases, mixed-linkage glucan synthases and specialized small-molecule glycosyltransferases; the PANTHER X-box transcription-factor label is misleading for these members.

The peanut target has CSLD3-like placement. Reconstitution distinguishes UDP-glucose-dependent beta-1,4-glucan synthesis by Arabidopsis CSLD3 from GDP-mannose use by CSLA9, so mannan activity is not validated by a CSLD label. Membrane architecture supports glycan synthesis but does not specify donor or polymer.

**Exact benchmark/reference members:** ARAHY/A0A444Z7V7 (A0A444Z7V7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [mannan synthase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0051753) (GO:0051753) | UNRESOLVED | Reconstituted Arabidopsis CSLD3 uses UDP-glucose to synthesize beta-1,4-glucan, whereas CSLA9 in the same study uses GDP-mannose. Earlier CSLD mutant and heterologous-membrane assays linked CSLDs to mannan, but the purified-protein comparison is stronger evidence for CSLD3 donor/product specificity. The peanut CSLD3-like placement therefore does not validate mannan synthase activity. Other glycosyltransferase branches differ, so this CSLD3 counterexample is not encoded as a family-wide negative. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13301/PTHR13301-review.yaml)

## PTHR13393

**RlmF/METTL16 and related SAM-dependent methyltransferases** — HETEROGENEOUS; COMPLETE

Members include bacterial rRNA methyltransferase RlmF, eukaryotic METTL16/U6 RNA methyltransferases and psilocybin synthase PsiM proteins. METTL16-dependent U6 modification connects RNA methylation to splicing; vertebrate MAT2A regulation is an additional regulatory deployment. Neither a U6 substrate nor RNA methylation itself follows automatically from this broad PANTHER assignment.

Both curated IPR010286 and the member inventory explicitly include RlmF, METTL16 and psilocybin synthase PsiM. Thus substrate divergence is documented in the curated source itself, not inferred from names alone. SF0 contains multiple substrate classes, so its METTL16 label is not a safe grant of U6 methylation. NCU11362 requires a METTL16-specific comparison, and vertebrate MAT2A regulation is an additional restricted function.

**Exact benchmark/reference members:** NEUCR/NCU11362 (A7UX10)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [methyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008168) (GO:0008168) | FAMILY_WIDE | The member inventory contains RlmF, METTL16 and small-molecule methyltransferases, whereas the integrated InterPro prose emphasizes the first two groups. Substrate class and RNA target therefore require subfamily-level evidence. Fungal NCU11362 should be compared with the METTL16 branch, not bacterial RlmF or specialized-metabolite enzymes. SF0 itself contains RlmF, METTL16 and PsiM entries, so this boundary cannot be represented by granting a substrate-specific term to SF0. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13393/PTHR13393-review.yaml)

## PTHR13408

**RPC4/C53 RNA polymerase III subunits** — COHERENT; COMPLETE

RPC4/C53 proteins are noncatalytic subunits of RNA polymerase III. They help organize the transcription complex and its initiation, termination and reinitiation behavior through association with other polymerase subunits. Participation in RNA synthesis does not mean that an isolated RPC4 protein catalyzes phosphodiester-bond formation.

All six inspected inventory entries identify RPC4/C53, consistent with curated IPR007811 assignment to RNA polymerase III. This supports polymerase-III complex membership and contribution to its transcription process. The catalytic reaction belongs to the assembled polymerase; RPC4 is an accessory component, not an autonomous DNA-directed RNA polymerase.

**Exact benchmark/reference members:** NEUCR/NCU01245 (Q1K6K5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [RNA polymerase III complex](https://www.ebi.ac.uk/QuickGO/term/GO:0005666) (GO:0005666) | FAMILY_WIDE | The sampled entries consistently identify RPC4, and the curated InterPro entry assigns this group to polymerase III. Complex membership and transcription by polymerase III are transferable; generic RNA polymerase catalytic activity is not an intrinsic activity of this subunit. |
| [transcription by RNA polymerase III](https://www.ebi.ac.uk/QuickGO/term/GO:0006383) (GO:0006383) | FAMILY_WIDE | The sampled entries consistently identify RPC4, and the curated InterPro entry assigns this group to polymerase III. Complex membership and transcription by polymerase III are transferable; generic RNA polymerase catalytic activity is not an intrinsic activity of this subunit. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13408/PTHR13408-review.yaml)

## PTHR13547

**Proteinaceous RNase P catalytic proteins** — COHERENT; COMPLETE

Proteinaceous RNase P proteins use an RNA-recognition region and a nuclease domain to remove precursor tRNA 5-prime leaders. Plant PRORPs and animal mitochondrial RNase P catalytic subunits differ in compartment and partner dependence.

The curated member set contains plant PRORP1/2/3 and metazoan PRORP/MRPP3 proteins, including human O15091 and Arabidopsis Q66GI4, Q680B9 and F4JKB6. Plant biochemical and genetic experiments establish precursor-tRNA 5-prime processing in organelles and the nucleus; reconstituted human mitochondrial RNase P and its substrate-bound structure establish the homologous cleavage function in animals. Conserved RNA-recognition and nuclease architecture supports a coherent tRNA-processing family despite differences in compartment and partner dependence.

**Exact benchmark/reference members:** TOBAC/A0A1S3Y076 (A0A1S3Y076)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [tRNA processing](https://www.ebi.ac.uk/QuickGO/term/GO:0008033) (GO:0008033) | FAMILY_WIDE | tRNA processing is the shared broad function of plant PRORP enzymes and animal mitochondrial PRORP/MRPP3 catalytic subunits. Arabidopsis experiments establish RNase P activity in organelles and the nucleus (PMID:22549728); human reconstitution and the precursor-tRNA-bound structure establish PRORP-dependent 5-prime leader cleavage in the mitochondrial complex (PMID:18984158; PMID:34489609). The member set includes these plant and metazoan proteins, and the tobacco target retains the PPR recognition region and PRORP catalytic region. The family-wide process assignment does not transfer autonomous single-protein activity, a particular compartment, or tRNA methyltransferase activity: human PRORP requires TRMT10C and SDR5C1, and methylation is performed by its partner TRMT10C. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13547/PTHR13547-review.yaml)

## PTHR13667

**Fritz/WDPCP polarity and ciliogenesis effectors** — COHERENT; COMPLETE

Fritz/WDPCP proteins organize cytoskeletal and membrane-associated machinery involved in cell polarity and ciliogenesis. Mammalian WDPCP participates in the CPLANE machinery that recruits intraflagellar transport components, while fly Fritz is associated with patterned wing-cell protrusions. These are related cellular organization functions, not evidence for a catalytic activity encoded by the WD-repeat fold.

Human and mouse WDPCP form the structurally resolved CPLANE complex with Inturned and Fuzzy (PMID:35427153). Fly Fritz functions downstream of core planar-polarity proteins to position and limit wing prehairs (PMID:15654087). These observations support a conserved cytoskeletal-organization effector family, while cilium assembly and wing-hair morphogenesis are distinct cellular implementations; a WD-repeat fold is not evidence of catalytic activity.

**Exact benchmark/reference members:** HORSE/WDPCP (A0A3Q2KRK8), human/WDPCP (O95876)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13667/PTHR13667-review.yaml)

## PTHR13976

**ESRP, hnRNP H/F and related RNA-binding proteins** — HETEROGENEOUS; COMPLETE

ESRP and hnRNP H/F-related proteins use RNA-recognition motifs in transcript processing and regulation. The retrieved family also includes GRSF1 and other RNA-binding proteins with distinct RNA targets and subcellular destinations.

The shark target has ESRP-type RRM architecture and the fly benchmark includes glo. Nuclear residence is compatible with splicing regulators, but mitochondrial GRSF1 and localization-dependent isoforms prevent a universal nuclear assignment. Epithelial splicing programs must not be transferred to every RRM-containing member.

**Exact benchmark/reference members:** CALMI/A0A4W3GVU1 (A0A4W3GVU1), DROME/glo (Q8INJ6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0005634) (GO:0005634) | UNRESOLVED | ESRP-type RRMs in the shark protein support comparison to nuclear splicing regulators, while the fly Glo branch has its own RNA-localization biology. Direct GRSF1 studies identify a mitochondrial-matrix isoform, providing a concrete counterexample to universal nuclear localization. The complete isoform/targeting boundary among ESRP, hnRNP H/F and GRSF1-like branches is unresolved; RNA-binding fold conservation does not fix the compartment. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13976/PTHR13976-review.yaml)

## PTHR13980

**Spt16 FACT histone chaperones** — COHERENT; COMPLETE

Spt16 is the large subunit of FACT, a histone chaperone that reorganizes nucleosomes while preserving chromatin integrity. Its amino-terminal aminopeptidase-like fold binds histones H3 and H4. Structural and biochemical work on pombe Spt16 establishes a nonenzymatic histone-binding function for that fold, rather than aminopeptidase catalysis.

All 26 inspected entries identify Spt16 orthologs. Direct pombe structural and mutational studies show that the aminopeptidase-like N-terminal domain binds histone H3-H4 cores and tails rather than catalyzing proteolysis (PMID:18579787). FACT membership is a coherent family assignment; histone binding does not confer histone-modifying enzymatic activity or aminopeptidase activity.

**Exact benchmark/reference members:** SCHPO/spt16 (O94267)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [FACT complex](https://www.ebi.ac.uk/QuickGO/term/GO:0035101) (GO:0035101) | FAMILY_WIDE | The family members are Spt16 orthologs, and direct pombe structural evidence separates the conserved histone-binding module from the ancestral-looking enzyme fold. FACT participation is a strong family-level assignment; peptidase activity is not supported by the fold resemblance. |
| [histone chaperone activity](https://www.ebi.ac.uk/QuickGO/term/GO:0140713) (GO:0140713) | FAMILY_WIDE | Spt16 proteins are FACT histone-chaperone subunits. Direct pombe structural and binding assays identify the aminopeptidase-like region as a histone-binding module. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR13980/PTHR13980-review.yaml)

## PTHR14338

**AFAP actin-associated signaling adaptors** — HETEROGENEOUS; COMPLETE

AFAP1, AFAP1L1 and AFAP1L2/XB130 are PH-domain-containing adaptor proteins associated with actin and membrane signaling. Their interaction regions recruit different signaling partners rather than catalyzing a shared chemical reaction. AFAP1L2 evidence for signal transduction should be interpreted in the context of that paralog's architecture and partners.

Human XB130/AFAP1L2 interacts with SRC, and deletion or depletion experiments affect SRC signaling (PMID:17412687), providing direct adaptor evidence. AFAP1, AFAP1L1 and AFAP1L2 share PH-domain-associated scaffolding architecture but differ in actin and signaling partners. SRC activation and a particular phosphoinositide preference are not universal family properties.

**Exact benchmark/reference members:** HORSE/AFAP1L2 (A0A9L0RQI4), human/AFAP1L2 (Q8N4X5)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR14338/PTHR14338-review.yaml)

## PTHR14440

**Rpa49 RNA polymerase I accessory subunits** — COHERENT; COMPLETE

Rpa49 is an accessory subunit of RNA polymerase I that supports efficient ribosomal DNA transcription. The polymerase can retain activity when Rpa49 is deleted, indicating a stimulatory and organizational role rather than independent RNA polymerase catalysis. Its conserved function is linked to the specialized rRNA transcription machinery.

All six inspected inventory entries identify RPA49. Curated IPR009668 reports retained Pol I activity after A49 deletion but reduced transcriptional efficiency, supporting an accessory transcription role. This is compatible with participation in the Pol I complex and rRNA synthesis; it does not establish an independent RNA polymerase catalytic center in Rpa49.

**Exact benchmark/reference members:** SCHPO/rpa49 (O14086)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR14440/PTHR14440-review.yaml)

## PTHR14495

**SHLD2 shieldin DNA-repair subunits** — COHERENT; COMPLETE

SHLD2 is a component of shieldin, a DNA-end protection complex acting in double-strand-break repair. Its DNA-associated and complex-assembly functions regulate access of repair machinery to damaged DNA. Shieldin participation is mechanistically distinct from DNA synthesis, helicase activity or nuclease activity.

Shieldin interaction mapping identifies SHLD2/FAM35A within the complex, and perturbation links shieldin to protection of DNA ends from resection and promotion of end joining (PMID:29656893). The coherent family role is an end-protection complex component. Effects on repair-pathway choice do not make SHLD2 a nuclease, DNA polymerase or helicase; immunoglobulin class switching is a vertebrate cellular context rather than a universal property.

**Exact benchmark/reference members:** HORSE/SHLD2 (A0A9L0RGD6), human/SHLD2 (Q86V20)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR14495/PTHR14495-review.yaml)

## PTHR14773

**DRS1-related WD-repeat DNA-associated proteins** — MOSTLY_COHERENT; COMPLETE

WDR76/CMR1-related WD40 proteins have experimentally supported nuclear/chromatin associations in characterized homologs. Arabidopsis DRS1 has direct drought and ABA-dependent leaf-water-loss phenotypes, while its biochemical connection to chromatin remains unresolved. Broad DNA/chromatin association must be distinguished from a particular modified-base-reader mechanism.

Human WDR76 colocalizes with heterochromatin proteins and responds rapidly to DNA damage, whereas two Arabidopsis drs1 alleles establish a physiological drought/ABA role. This supports related nuclear interaction biology without assigning the same modified-DNA specificity, checkpoint regulation or ligase substrates to every member. Sensitive Arabidopsis chemical assays constrain genomic 5hmC abundance, so an animal-like 5hmC reader is not a safe family-wide default.

**Exact benchmark/reference members:** ARATH/DRS1 (Q9SAI7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0005634) (GO:0005634) | UNRESOLVED | Nuclear localization is experimentally grounded in human WDR76 and is a reasonable conserved inference for plant DRS1. The inspected evidence does not establish an exclusive nuclear location or a complete compartment map for all family products. |
| [response to water deprivation](https://www.ebi.ac.uk/QuickGO/term/GO:0009414) (GO:0009414) | UNRESOLVED | Two independent Arabidopsis DRS1 alleles support drought-response function directly. This plant physiological phenotype does not follow automatically for animal or fungal WDR76/CMR1 homologs and is not used as a universal family annotation. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR14773/PTHR14773-review.yaml)

## PTHR15245

**Symplekin/Pta1 RNA 3-prime processing scaffolds** — COHERENT; COMPLETE

Symplekin and Pta1 are scaffolding components of eukaryotic RNA 3-prime-end processing machinery. They organize cleavage/polyadenylation factors and associated regulatory components. Historical names referring to pre-tRNA processing do not define an intrinsic endonuclease reaction for the family.

The inventory and curated IPR021850 connect animal symplekin to fungal Pta1. These proteins scaffold mRNA 3-prime-end-processing complexes; animal histone-mRNA cleavage can be uncoupled from polyadenylation. The historical pre-tRNA-processing name does not establish a catalytic tRNA endonuclease, and complex membership does not confer poly(A) polymerase chemistry on Pta1.

**Exact benchmark/reference members:** SCHPO/pta1 (Q10222)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR15245/PTHR15245-review.yaml)

## PTHR15256

**DGCR2-related membrane adhesion proteins** — UNKNOWN; COMPLETE

DGCR2-related proteins are membrane-associated interaction proteins with extracellular-domain architecture. Mouse DGCR2 participates in cortical-neuron migration and associates with the Reelin signaling complex; the conserved ligand and signaling role of divergent fly CG42404 remain unresolved.

In utero mouse Dgcr2 depletion disrupts radial locomotion and terminal translocation, and biochemical observations connect DGCR2 to the Reelin complex and downstream phosphorylation (PMID:29305086). This is mechanistic evidence beyond a disease-locus association, but it does not establish a direct enzymatic activity or a universal Reelin receptor function. The long fly product shares a family assignment and membrane-associated domains without a demonstrated conserved signaling partner. Functional coherence is unknown at that more specific molecular level.

**Exact benchmark/reference members:** DROME/CG42404 (Q9VFA8)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR15256/PTHR15256-review.yaml)

## PTHR15921

**Pcf11 transcription-termination and RNA-processing factors** — COHERENT; COMPLETE

Pcf11 couples RNA polymerase II termination to pre-mRNA 3-prime-end processing through interactions with the polymerase and cleavage/polyadenylation machinery. Its function depends on a multidomain protein and association with factors such as Clp1. A short fragment matching part of Pcf11 cannot be assumed to carry all functions of the intact protein.

Pcf11 proteins couple RNA polymerase II transcription to RNA-end processing through separable interaction domains. Yeast experiments distinguish CTD binding from other 3-prime-processing functions (PMID:12727883). Reconstituted mammalian CFII contains Pcf11 and Clp1; Pcf11 zinc fingers bind RNA, while the kinase is Clp1 and its kinase activity is dispensable for the tested cleavage reaction (PMID:30139799). The 86-residue fly benchmark product represents only a limited portion of this multidomain mechanism; family identity does not establish all full-length Pcf11 functions on that short exact product.

**Exact benchmark/reference members:** DROME/Pcf11 (C0P8M6)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR15921/PTHR15921-review.yaml)

## PTHR16515

**Diverse C2H2 zinc-finger regulatory proteins** — HETEROGENEOUS; COMPLETE

This broad group contains multiple zinc-finger transcription regulators, including Krueppel-like proteins, PLAG proteins and PRDM proteins. Some branches carry additional chromatin-regulatory domains, whereas others primarily recognize DNA through zinc-finger arrays. Drosophila Dati has a demonstrated role in specific neuronal circuits, but this behavior is not a family-wide property.

Shared C2H2 zinc fingers span PRDM, KLF-like and other transcriptional regulators with different auxiliary domains and DNA targets. Fly dati genetics localizes female receptivity and locomotion phenotypes to distinguishable neuronal circuits, including a cholinergic requirement for receptivity (PMID:25291190). This supports a neuronal transcription-regulatory context for DATI, not a family-wide behavioral function. PR-domain-dependent histone methylation cannot be assigned to all zinc-finger members or to DATI merely from the broad family name.

**Exact benchmark/reference members:** DROME/dati (Q9V4C9)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR16515/PTHR16515-review.yaml)

## PTHR18896

**Classical phospholipase D lipid-signaling enzymes** — MOSTLY_COHERENT; COMPLETE

Classical phospholipase D proteins hydrolyze glycerophospholipids to phosphatidic acid and a released head group. The family includes animal PLD1/PLD2 and multiple plant PLD classes with different regulatory and membrane-interaction features. Lipid hydrolysis is the common mechanistic theme, while stimulus dependence, preferred substrates and cellular signaling outputs vary.

The inventory contains classical animal and plant PLDs with conserved phospholipase architecture. Fly Pld loss and rescue experiments link phosphatidic-acid signaling to phototransduction (PMID:15883198), while separate experiments support vesicle trafficking during cellularization (PMID:17156430). These physiological outputs differ from the common lipid-hydrolysis reaction and should not be generalized to all PLDs. No catalytic-loss claim is supported for the exact fly input.

**Exact benchmark/reference members:** DROME/Pld (A4UZ54)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR18896/PTHR18896-review.yaml)

## PTHR18901

**Diverse HAD-like phosphatases and phosphomutases** — HETEROGENEOUS; COMPLETE

This HAD-like family contains pseudouridine-5-prime-phosphatases, glycerol-3-phosphatases, carbohydrate phosphatases and beta-phosphoglucomutase. The shared fold supports phosphate-group chemistry but does not specify the physiological substrate or distinguish hydrolysis from intramolecular phosphate transfer. Human HDHD1/PUDP is experimentally selective for pseudouridine 5-prime-phosphate.

HAD-superfamily phosphatases share a catalytic scaffold but vary in their cap domains and phosphometabolite recognition. Recombinant human HDHD1/PUDP hydrolyzes pseudouridine 5-prime-phosphate with high specificity, exceeding its activity on UMP by over three orders of magnitude (PMID:20722631). This is positive evidence for one substrate-specific branch, not a license to transfer pseudouridine-phosphate or 2-deoxyglucose-6-phosphate hydrolysis to every HAD member. CG5565 remains a phosphatase-family protein with unresolved physiological substrate.

**Exact benchmark/reference members:** DROME/CG5565 (Q9VQ04)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR18901/PTHR18901-review.yaml)

## PTHR18934

**DEAH-related nucleic-acid helicases** — HETEROGENEOUS; COMPLETE

This family spans DEAH-related helicases with roles in RNA processing, genome defense and other nucleic-acid transactions, as well as viral proteins. Distinct accessory domains and interaction partners determine substrate choice and biological deployment. The YTHDC2 branch couples helicase activity to modified-RNA recognition, but that specialization is not shared by all family members.

DEAH helicase relatives diversify in auxiliary domains and RNA pathways. Mammalian YTHDC2 combines an RNA-stimulated ATPase/helicase module with m6A recognition and ankyrin-mediated XRN1 recruitment (PMID:29033321). Related helicases instead participate in splicing, germline RNA regulation or viral transcription. CG8915's verified YTHDC2-related classification supports a branch hypothesis, but m6A recognition, XRN1 recruitment and a particular RNA substrate require their relevant domains and cannot be inherited from the shared helicase core alone.

**Exact benchmark/reference members:** DROME/CG8915 (Q9VX63)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR18934/PTHR18934-review.yaml)

## PTHR19143

**Fibrinogen-domain extracellular interaction proteins** — HETEROGENEOUS; COMPLETE

This family groups proteins carrying a fibrinogen C-terminal interaction domain, including ficolins, fibroleukin, microfibril-associated proteins and angiopoietin-related proteins. Their functions range from ligand recognition to extracellular structural and signaling roles. The domain name does not imply that every member contributes to fibrin clot formation.

Fibrinogen-like domains occur in secreted signaling and recognition proteins with different receptors and outputs. Fly CG10359 was identified as an angiopoietin-like candidate with radiation-responsive expression in a study of systemic radioprotection (PMID:24675716); this does not establish direct Tie binding, a GPCR mechanism or a fibrin polymerization reaction. Its signal peptide and fibrinogen domain support an extracellular interaction protein, while receptor identity and the conservation of angiopoietin-like signaling remain unresolved. Domain homology cannot replace a ligand-receptor experiment.

**Exact benchmark/reference members:** DROME/CG10359 (B7Z0B2)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR19143/PTHR19143-review.yaml)

## PTHR19303

**CENP-B and transposon-derived DNA-binding proteins** — HETEROGENEOUS; COMPLETE

CENP-B-related proteins illustrate evolutionary recruitment of transposon-derived DNA-binding machinery into host chromatin regulation. Pombe Cbh1 binds centromeric repeat DNA, and related pombe proteins participate in retrotransposon silencing and genome organization. The broader group also includes other domesticated transposon-derived regulators, so centromere binding and active transposition are separate hypotheses.

Direct pombe Cbh1 purification and footprinting establish binding to centromeric K-type repeat DNA (PMID:9237993), and CENP-B homolog experiments establish retrotransposon silencing (PMID:18094683). The inventory also includes PDC2, Jerky and other transposon-derived host regulators. Shared transposon ancestry does not establish active transposition or uniform centromeric DNA specificity; the Cbh1 SF73 label PDC2 does not override its direct assay.

**Exact benchmark/reference members:** SCHPO/cbh1 (O14423)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR19303/PTHR19303-review.yaml)

## PTHR19847

**DCAF11/WDR23 ubiquitin-ligase substrate adaptors** — MOSTLY_COHERENT; COMPLETE

DCAF11/WDR23 proteins serve as substrate receptors in CUL4-DDB1-associated protein regulation. Direct C. elegans experiments identify SKN-1 and GEN-1 regulatory relationships, with different outcomes for nuclear and cytoplasmic isoforms. The common WD-repeat architecture supports substrate recruitment, while exact substrates and regulatory outcomes cannot be assumed identical across products.

Primary worm experiments establish WDR-23 association with CUL-4/DDB-1 and isoform-dependent regulation of SKN-1 and GEN-1. The selected S6FN32 product retains every annotated WD repeat and the common 498-residue core but lacks the distinct N termini of both assayed isoforms. Thus a qualified adaptor assignment is supported, while localization and substrate fate remain product-specific.

**Exact benchmark/reference members:** worm/wdr-23 (S6FN32)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [molecular adaptor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0060090) (GO:0060090) | UNRESOLVED | Direct WDR-23 interaction and substrate experiments support an adaptor mechanism in characterized worm isoforms; the selected product retains the common WD-repeat region. The evidence does not delimit every functional product across the family or establish identical substrate specificity. |
| [nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0005634) (GO:0005634) | UNRESOLVED | Nuclear WDR-23B and cytoplasmic WDR-23A have experimentally distinct outcomes. S6FN32 is not identical to either tested isoform, so a universal nuclear-location grant is not justified. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR19847/PTHR19847-review.yaml)

## PTHR19861

**Swd2/WDR82 RNA and chromatin complex adaptors** — MOSTLY_COHERENT; COMPLETE

Swd2/WDR82 proteins are WD-repeat components of Set1/COMPASS-associated transcription and chromatin machinery. Fungal proteins can also participate in RNA 3-prime processing complexes. Their presence in a histone methyltransferase complex does not confer methyltransferase catalysis on the WD-repeat protein itself.

Swd2/WDR82 proteins are regulatory WD-repeat subunits rather than methyltransferases. Human WDR82 associates with SET1A/B complexes but not the other tested MLL complexes and influences H3K4 trimethylation (PMID:18838538). Yeast Swd2 participates in both Set1 and CPF-related functions; depletion affects transcription termination without abolishing cleavage/polyadenylation activity in the tested extract (PMID:15024081). Histone methylation and RNA-end-processing roles therefore have distinct complex and organism boundaries, and catalytic activities of partner enzymes cannot be attributed to Swd2/WDR82 itself.

**Exact benchmark/reference members:** DROME/CG3515 (Q9VQD1)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR19861/PTHR19861-review.yaml)

## PTHR19876

**Coatomer, LIS1 and other WD-repeat interaction proteins** — HETEROGENEOUS; COMPLETE

This PANTHER group combines coatomer subunits with LIS1/NudF, mitochondrial-division factors and Crt10-related proteins. These proteins use related interaction scaffolds in distinct cellular machines. Budding-yeast Crt10 recruits a cullin-E3 ligase pathway to nonfunctional large-subunit rRNA decay rather than acting as a COPI coat subunit.

The inventory contains coatomer alpha/beta-prime, LIS1/NudF and Mdv1-related scaffolds. Direct budding-yeast Crt10 experiments establish a distinct Rtt101-dependent nonfunctional 25S rRNA decay role (PMID:25534857). Pombe crt10 is therefore compared to the Crt10 branch, not assigned Golgi vesicle coating from the family name or pre-mRNA splicing from its SF20 label. This comparison is ortholog inference, not a pombe rRNA-decay assay.

**Exact benchmark/reference members:** SCHPO/crt10 (O42996)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR19876/PTHR19876-review.yaml)

## PTHR19970

**eL39 large-ribosomal-subunit proteins** — COHERENT; COMPLETE

eL39 is a small structural protein of the eukaryotic large ribosomal subunit. Its location in the assembled ribosome supports translation and influences the environment encountered by a nascent chain. Its short length is normal for this ribosomal protein family and is not itself evidence of a truncated nonfunctional protein.

The 43-member inventory consistently identifies eL39 relatives, and NCU08990/Q7S2X9 has both the specific eL39 InterPro and Pfam signatures. Its 51-residue length is compatible with this naturally small structural ribosomal protein. This supports a large-subunit structural role by family evidence, not a direct Neurospora functional assay or proof of a paralog-specific translational program.

**Exact benchmark/reference members:** NEUCR/NCU08990 (Q7S2X9)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR19970/PTHR19970-review.yaml)

## PTHR20837

**CC2D2A/CC2D2B ciliary-associated proteins** — MOSTLY_COHERENT; COMPLETE

CC2D2A participates in the transition-zone machinery that maintains the ciliary membrane as a distinct signaling compartment. Disruption of the complex alters cilia formation and receptor retention. The family also contains CC2D2B-related proteins, whose presence does not by itself establish the same transition-zone role.

Direct mammalian complex studies support CC2D2A-dependent organization of the ciliary diffusion barrier. The member inventory includes the CC2D2B paralog, so a blanket grant of every CC2D2A function is premature without comparative localization and domain evidence for that branch.

**Exact benchmark/reference members:** HORSE/CC2D2A (A0A5F5PJ44), human/CC2D2A (Q9P2K1)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR20837/PTHR20837-review.yaml)

## PTHR20898

**DUF1091/Daedalus-related proteins** — UNKNOWN; COMPLETE

This group contains small DUF1091-domain proteins, including fly CG33453. The available sequence-domain assignments establish a conserved protein family but do not identify a biochemical reaction, interaction partner or organelle-specific mechanism. The Daedalus-related name is not a functional assay.

There is no integrated InterPro functional description or experimental reference in the available target evidence, and the 174-residue target is annotated with DUF1091. Functional coherence cannot be resolved from an uncharacterized-domain label; a conserved-domain alignment and experimentally characterized ortholog are needed.

**Exact benchmark/reference members:** DROME/CG33453 (A0A0B4LFV5)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR20898/PTHR20898-review.yaml)

## PTHR21255

**Tctex-type dynein light chains** — HETEROGENEOUS; COMPLETE

Tctex-type proteins are small noncatalytic dynein-associated subunits with distinct roles in cytoplasmic and ciliary transport assemblies. DYNLT2B/TCTEX1D2 is an accessory component of dynein-2 required for efficient retrograde intraflagellar transport. ATP-driven motility belongs to the dynein motor machinery rather than the light chain itself.

The member inventory contains several Tctex paralogs, and direct TCTEX1D2 experiments define its dynein-2 specialization. Rhodopsin-binding observations for Tctex-1 cannot be used to assign that cargo or a photoreceptor-specific role to DYNLT2B or every family member.

**Exact benchmark/reference members:** HORSE/DYNLT2B (A0A9L0SWY1), human/DYNLT2B (Q8WW35)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR21255/PTHR21255-review.yaml)

## PTHR21467

**PPP4R4 phosphatase regulatory subunits** — COHERENT; COMPLETE

PPP4R4 proteins are noncatalytic partners of protein phosphatase 4. Human PP4R4 forms a stable cytosolic complex with PP4c that is distinct from other PP4 assemblies and modulates the catalytic subunit’s activity. The regulatory component itself is not a phosphoprotein phosphatase, and its physiological substrate-targeting roles remain incompletely defined.

Affinity purification and interaction mutagenesis establish PP4R4 as a stable, specific PP4c partner in a cytosolic complex (PMID:18715871). It does not bridge PP4c to the previously characterized regulatory subunits. The complex has lower phosphatase activity than free PP4c in the reported assays; this is regulatory-complex evidence, not intrinsic phosphatase catalysis by PP4R4. A shared PP4 regulatory role is supported, while physiological substrate selection remains unresolved.

**Exact benchmark/reference members:** HORSE/PPP4R4 (A0A9L0S961), human/PPP4R4 (Q6NUP7)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR21467/PTHR21467-review.yaml)

## PTHR21575

**HID1-family Golgi and secretory-pathway proteins** — MOSTLY_COHERENT; COMPLETE

HID1-family proteins organize Golgi-associated membrane traffic. Mammalian HID1 is a peripheral Golgi protein with N-terminal myristoylation, and a fission-yeast homolog contributes to Golgi organization; specialized dense-core-vesicle functions occur in metazoan cells.

Direct mammalian localization and biochemical experiments identify HID1 as a peripheral membrane protein associated with medial/trans-Golgi and cytosol, rather than the multipass topology suggested by hydrophobicity prediction (PMID:21337012). Comparative phylogeny and fission-yeast genetics support a conserved relationship to Golgi organization, including disruption of Golgi stacks in the tested mutant (PMID:40899782). Dense-core-vesicle neurosecretion is a metazoan specialization, not a universal fungal function.

**Exact benchmark/reference members:** DROME/CG8841 (Q0E9B5)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR21575/PTHR21575-review.yaml)

## PTHR21600

**RluA-related RNA pseudouridine synthases** — HETEROGENEOUS; COMPLETE

RluA-related enzymes isomerize uridine to pseudouridine in RNA, but family branches act on different rRNAs, tRNAs and other RNA substrates. The inventory includes RluC, RluD, TruC and organellar RNA-modification proteins. Fly RluA-1 and RluA-2 have experimentally demonstrated neuronal phenotypes without those phenotypes identifying their modified RNA nucleotide.

RluA-like pseudouridine synthases share uridine-isomerization chemistry but differ in RNA class, modification site and compartment across RluC/RluD/TruC and RPUSD-related branches. Fly RluA-1 and RluA-2 loss-of-function and rescue establish roles in nociceptive behavior (PMID:33028630), without identifying their modified RNA or nucleotide. The phenotype is therefore not evidence for an inherited bacterial rRNA site or a specific tRNA position. Exact substrate-site assignments remain branch-specific.

**Exact benchmark/reference members:** DROME/RluA-1 (Q9VKV0)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR21600/PTHR21600-review.yaml)

## PTHR21646

**Diverse ubiquitin-specific proteases** — HETEROGENEOUS; COMPLETE

Ubiquitin-specific proteases remove ubiquitin from proteins and ubiquitin chains, with paralog-specific substrate selection and regulatory interactions. USP8/UBPY acts on endosomal ubiquitin dynamics and receptor trafficking. Its deubiquitination can facilitate receptor down-regulation, so ubiquitin removal should not be equated universally with stabilization of the target protein.

The inventory spans USP4, USP5, USP8, USP13, USP20, USP22 and other paralogs. Shared ubiquitin-processing chemistry does not justify transferring an EGFR substrate, an endosomal localization or a particular linkage preference to every family member.

**Exact benchmark/reference members:** HORSE/USP8 (A0A9L0T7K6), human/USP8 (P40818)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [cysteine-type deubiquitinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004843) (GO:0004843) | UNRESOLVED | USP8/UBPY in SF27 has experimentally demonstrated cysteine-type deubiquitinase activity, and independent human USP21 experiments also demonstrate ubiquitin-conjugate cleavage in a different branch. Thus the activity is not exclusive to USP8. The complete set of active versus catalytically divergent members across this broad family has not been established; substrate specificity and endosomal deployment also differ. Family-wide activity coverage remains unresolved without denying the supported USP8 or USP21 activities or the curated UBP11 annotation. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR21646/PTHR21646-review.yaml)

## PTHR21738

**Rrp36 small-subunit ribosome biogenesis factors** — COHERENT; COMPLETE

Rrp36 proteins participate in early pre-rRNA processing and small-ribosomal-subunit biogenesis. They are preribosomal assembly factors rather than structural constituents of the mature ribosome. A requirement for cleavage at an early processing step does not establish intrinsic nuclease activity.

The 72 inspected inventory entries consistently identify Rrp36, and curated IPR009292 supports early prerRNA processing. This is a ribosome-assembly role rather than membership in the mature translating ribosome. A depletion phenotype at a cleavage step would establish a requirement for Rrp36 but not the chemistry of an autonomous RNA nuclease.

**Exact benchmark/reference members:** SCHPO/rrp36 (Q9P6P2)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR21738/PTHR21738-review.yaml)

## PTHR22591

**Xin actin-associated repeat proteins** — MOSTLY_COHERENT; COMPLETE

Xin proteins contain actin-associated repeats and participate in cytoskeletal organization. XIRP1 and XIRP2 share this architectural role while differing in tissue context, binding partners and isoforms.

The bovine target has Xin repeats and XIRP2 placement, and experimental XIRP2 work supports the repeat-mediated actin relationship. Junctional residence requires the relevant cell type and isoform; a generic family assignment does not establish a particular junction or auditory versus cardiac function.

**Exact benchmark/reference members:** BOVIN/E1BL04 (E1BL04)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [actin cytoskeleton organization](https://www.ebi.ac.uk/QuickGO/term/GO:0030036) (GO:0030036) | UNRESOLVED | Xin-repeat expression and actin-binding assays show stabilization of the actin cytoskeleton, with corresponding repeats in XIRP2. This supports an actin-organizing mechanism across characterized Xin proteins rather than an XIRP2-exclusive effect. Shortened isoforms and other architectures require separate assessment before defining a complete positive set. |
| [cell junction](https://www.ebi.ac.uk/QuickGO/term/GO:0030054) (GO:0030054) | UNRESOLVED | Xin immunolocalization identifies intercalated discs and myotendinous junctions in muscle, giving concrete junctional evidence. It does not establish identical junctional residence for every XIRP isoform or tissue, including auditory contexts. Junction localization follows preserved targeting architecture and cellular expression, not repeats alone. |
| [actin binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003779) (GO:0003779) | UNRESOLVED | Purified-repeat and cell-expression assays directly support Xin-mediated actin binding; XIRP2 repeats share those properties. The repeated actin-binding module is the relevant transferable feature. The full set of products retaining a functional repeat array has not been delimited, so no exclusive XIRP2-only or unconditional family-wide grant is made. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22591/PTHR22591-review.yaml)

## PTHR22594

**Aspartyl/asparaginyl tRNA synthetase-related proteins** — HETEROGENEOUS; COMPLETE

This group joins related class-II aminoacyl-tRNA synthetases with aspartate or asparagine specificity. Human mitochondrial DARS2 directly catalyzes aspartylation of tRNA and is distinct from the cytosolic translation machinery. Similar catalytic architecture does not establish the same amino acid, tRNA substrate or cellular compartment for every member.

The official family definition explicitly spans Asp/Asn ligases, while biochemical characterization establishes DARS2 as mitochondrial AspRS. A DARS2 annotation should be scoped to the mitochondrial AspRS lineage rather than transferred across the amino-acid specificity boundary. DARS2 can also be assayed for misacylation of tRNA-Asn; that is a separate substrate question and does not make it an asparagine-activating enzyme.

**Exact benchmark/reference members:** HORSE/DARS2 (A0A9L0SB67), human/DARS2 (Q6PI48)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22594/PTHR22594-review.yaml)

## PTHR22726

**OMA1 and bacterial membrane-associated metalloproteases** — HETEROGENEOUS; COMPLETE

OMA1 is a mitochondrial membrane metalloprotease involved in stress-responsive protein processing. Mammalian OMA1 cleaves OPA1 and participates in pathways that couple mitochondrial damage to cellular responses. Related bacterial proteins act in outer-membrane protein quality control, providing a distinct substrate and compartment context.

The inventory contains OMA1, YggG/LoiP/YcaL and beta-barrel assembly-enhancing proteases. Shared metalloprotease ancestry does not transfer OPA1 processing, DELE1 signaling or a mitochondrial location to bacterial members. Exact catalytic-residue claims require an anchored sequence analysis beyond the family name.

**Exact benchmark/reference members:** HORSE/OMA1 (A0A9L0R9P8), human/OMA1 (Q96E52)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22726/PTHR22726-review.yaml)

## PTHR22808

**Ncl1/Trm4-related RNA cytosine methyltransferases** — HETEROGENEOUS; COMPLETE

SAM-dependent RNA cytosine-C5 methyltransferases with branch-specific RNA substrates and nucleotide positions. In fission yeast, Trm4b/Trm402 modifies tRNA C49/C50 in vivo, whereas Trm4a supplies C48 and physiological C34 modification. Trm4b has additional C34 activity on precursor tRNA in vitro; that capability does not establish a physiological C34 role.

The conserved RNA-C5 methylation chemistry does not define a universal RNA target or nucleotide position. Direct paralog-resolved knockout methylomes and recombinant-enzyme assays distinguish Trm4a and Trm4b specificity, so a C34 or rRNA assignment cannot be inherited solely from the broad NOP/NOL/Trm4 family label.

**Exact benchmark/reference members:** SCHPO/trm402 (O13935)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [tRNA wobble base cytosine methylation](https://www.ebi.ac.uk/QuickGO/term/GO:0002127) (GO:0002127) | UNRESOLVED | No family-wide or complete subfamily grant is established. The physiological process is supported for Trm4a but directly excluded for Trm4b, although the latter can perform C34 methylation in vitro. Precise ancestral placement is not inferred without the complete tree and experimental mapping. |
| [tRNA (cytidine-N5)-methyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016428) (GO:0016428) | UNRESOLVED | Directly established in the Trm4a/Trm4b members, but a universal grant to a family containing other RNA-target branches is not justified by these target experiments alone. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22808/PTHR22808-review.yaml)

## PTHR22872

**RCC1-repeat multidomain proteins** — HETEROGENEOUS; COMPLETE

RCC1-like repeats occur in HERC ubiquitin ligases, RCC1/BTB proteins, RPGR and secretion-associated exchange-factor architectures. Their common repeat fold does not supply the catalytic domains of these distinct full-length proteins.

The Drosophila pseudoobscura target is a short RCC1-repeat protein without evidence for a HECT catalytic module. Ligase activity is therefore not justified for that sequence, although it occurs in HERC members of the wider family. A target-level negative must not become a denial of ligase function throughout the family.

**Exact benchmark/reference members:** DROPS/A0A6I8W8A2 (A0A6I8W8A2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ligase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016874) (GO:0016874) | UNRESOLVED | HERC members possess a catalytic HECT domain in addition to RCC1-like repeats, whereas the 169-residue Drosophila target contains only RCC1-repeat material. This architecture does not support intrinsic ligase catalysis in that selected product. Because full HERC proteins genuinely are ligases, the member-level refutation cannot become a family-wide negative; the complete HECT-competent branch boundary remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22872/PTHR22872-review.yaml)

## PTHR22883

**DHHC protein S-acyltransferases** — MOSTLY_COHERENT; COMPLETE

DHHC-family proteins catalyze protein S-acylation at membranes. Distinct paralogs act on different protein substrates and membrane compartments. Human ZDHHC23 has evidence for palmitoylation-dependent regulation of KCNMA1 localization, which is a specific substrate relationship rather than a universal property of DHHC enzymes.

Structural and biochemical work on DHHC enzymes establishes membrane-interface thioester-exchange chemistry and acyl-chain selectivity (PMID:29326245). The family contains multiple palmitoyltransferase branches with different protein substrates, acyl-chain preferences and partner requirements. ZDHHC23 placement supports this enzyme-family comparison, but a substrate reported for ZDHHC20, ZDHHC16 or fungal Erf2 cannot be assigned to ZDHHC23 from shared DHHC architecture.

**Exact benchmark/reference members:** HORSE/ZDHHC23 (A0A9L0T4E4), human/ZDHHC23 (Q8IYP9)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22883/PTHR22883-review.yaml)

## PTHR22896

**CABLES cyclin-dependent kinase-associated regulators** — MOSTLY_COHERENT; COMPLETE

CABLES proteins contain a cyclin-like interaction fold and have context-dependent regulatory functions. Fly Cables1 is a basal-body-associated protein required for neuronal and sperm ciliary architecture. Mammalian CDK-associated, cell-cycle and cell-death observations do not establish the same pathways in every CABLES member or imply intrinsic kinase activity.

Direct Drosophila experiments establish Cables1 basal-body recruitment and ciliary ultrastructural phenotypes. The shared cyclin fold supports an interaction-protein relationship with mammalian CABLES, but it does not establish a conserved cell-cycle mechanism or identical localization. Basal-body biology is primary evidence on the fly representative, not an inference from the mammalian gene name.

**Exact benchmark/reference members:** DROME/Cables1 (A0A0B4KF19)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ciliary basal body](https://www.ebi.ac.uk/QuickGO/term/GO:0036064) (GO:0036064) | UNRESOLVED | Fly Cables1 is directly recruited to maturing sperm basal bodies. This does not define the location of all CABLES1/2 products or exclude additional nuclear or cytoplasmic pools in other contexts. |
| [motile cilium assembly](https://www.ebi.ac.uk/QuickGO/term/GO:0044458) (GO:0044458) | UNRESOLVED | Fly Cables1 depletion/deletion disrupts sperm axonemal architecture, supporting motile ciliogenesis for that member. The complete evolutionary distribution of this role across CABLES1/2 branches has not been established. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22896/PTHR22896-review.yaml)

## PTHR22969

**IKK/TBK1-related serine-threonine kinases** — HETEROGENEOUS; COMPLETE

IKK-related kinases share protein-phosphorylation machinery but act in distinct signaling circuits. Canonical IKK subunits, TBK1 and IKK-epsilon differ in partners and substrates. Fly IKK-epsilon has direct evidence for regulation of actin turnover and polarized morphogenesis, showing that an immune-pathway-only family description is incomplete.

IKK-family serine/threonine kinases have conserved kinase chemistry but different substrate and pathway relationships. Fly IKKepsilon regulates actin turnover, membrane ruffling and nonapoptotic DIAP1-dependent morphogenesis in tracheal and bristle cells (PMID:16887350). These direct fly experiments support a cytoskeletal signaling branch; they do not make I-kappaB phosphorylation, mammalian interferon induction or a single ubiquitin-pathway substrate universal across IKKalpha/beta and IKKepsilon/TBK1 relatives.

**Exact benchmark/reference members:** DROME/IKKepsilon (Q9V3Y8)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR22969/PTHR22969-review.yaml)

## PTHR23023

**FMO-related flavin-dependent oxidative enzymes** — HETEROGENEOUS; COMPLETE

FMO-related proteins catalyze diverse oxidative reactions, including heteroatom oxygenation and specialized-metabolite transformations. The family includes trimethylamine oxidases, thiol-oxidizing enzymes and proteins catalogued as brominating enzymes. Yeast FMO experiments link thiol oxidation to endoplasmic-reticulum redox balance, but that substrate and pathway are not a default for all fungal homologs.

The inventory spans thiol monooxygenases, trimethylamine oxidases and specialized-metabolite oxidative enzymes. Direct yeast yFMO experiments establish thiol oxidation and a role at the cytoplasmic face of the ER (PMID:10077572); those data do not specify the Neurospora NCU06296 substrate. A family-level flavin-oxidation comparison is appropriate, while ER-lumen residence, glutathione specificity and mammalian trimethylamine metabolism remain separate claims.

**Exact benchmark/reference members:** NEUCR/NCU06296 (Q7SAD4)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23023/PTHR23023-review.yaml)

## PTHR23031

**Rhophilin Rho-associated cytoskeletal adaptors** — COHERENT; COMPLETE

Rhophilin proteins bind Rho-family signaling proteins and organize downstream cytoskeletal interactions. Characterized vertebrate RHPN1 and RHPN2 connect Rho signaling to actin-associated structures. Their role as Rho effectors is distinct from GTP hydrolysis or nucleotide exchange catalyzed by other parts of the signaling system.

Rhophilins are Rho-associated interaction scaffolds with Bro1/PDZ-containing architecture. Direct comparison found both RHPN1 and RHPN2 binding GDP- and GTP-bound RhoA in vitro, whereas only RHPN2 produced the tested stress-fiber-loss phenotype (PMID:12221077). Thus exclusive binding to activated RhoA and uniform inhibition of actin assembly are not family-wide properties. The common scaffold mechanism is coherent, but the nucleotide-state preference, downstream partners and actin outcome of fly Rhp remain distinct questions.

**Exact benchmark/reference members:** DROME/Rhp (Q9XYY9)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23031/PTHR23031-review.yaml)

## PTHR23049

**Myosin regulatory light chains** — HETEROGENEOUS; COMPLETE

Myosin regulatory light chains modulate actomyosin assemblies through association with myosin heavy chains and regulatory phosphorylation. The group contains muscle-specific and nonmuscle paralogs with different expression and contractile contexts. The light chain is not the ATPase motor, and an EF-hand-like fold does not establish equivalent calcium sensing by every paralog.

Regulatory-light-chain phosphorylation controls nonmuscle myosin filament organization in HeLa experiments (PMID:11942626). Muscle and nonmuscle paralogs differ in myosin partner, expression and contractile context. MYL10 has no comparable direct partner or phosphorylation assay in the retrieved sources, so the family supports a regulatory-light-chain comparison without establishing cardiac contraction, a specific heavy chain or identical calcium sensing for MYL10.

**Exact benchmark/reference members:** HORSE/MYL10 (A0A9L0TJE1), human/MYL10 (Q9BUA6)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23049/PTHR23049-review.yaml)

## PTHR23065

**F-BAR membrane and cytoskeletal scaffolds** — HETEROGENEOUS; COMPLETE

F-BAR proteins organize membrane-associated assemblies and connect membranes to cytoskeletal or trafficking machinery. The group includes GAS7, PACSIN, PSTPIP, cytokinesis proteins and Rho-GAP-containing proteins with distinct accessory domains.

The pufferfish target has GAS7-related F-BAR architecture, and GAS7 membrane-sheet assembly is a relevant physical mechanism. Cytoplasmic and peripheral-membrane activity is compatible with this branch, but the family includes spatially specialized proteins and does not imply phosphatase catalysis despite the historical name.

**Exact benchmark/reference members:** TAKRU/A0A674PKV4 (A0A674PKV4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [cytoplasm](https://www.ebi.ac.uk/QuickGO/term/GO:0005737) (GO:0005737) | UNRESOLVED | GAS7 forms sheets on the cytoplasmic face of membranes and is recruited to phagocytic cups, supporting a peripheral membrane/cytoplasmic context for that branch. The F-BAR module in the pufferfish target is compatible with the mechanism. Other family members differ in targeting and accessory activities, so neither a specific organelle nor a universally diffuse cytoplasmic distribution follows. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23065/PTHR23065-review.yaml)

## PTHR23068

**DNMT3/DRM methyltransferases and noncatalytic relatives** — HETEROGENEOUS; COMPLETE

This family includes active DNMT3 DNA methyltransferases together with regulatory relatives such as DNMT3L and inactive DRM proteins. DNMT3L recognizes chromatin and stimulates methyltransferase partners without supplying an independent DNA-methylation active site. The group also contains proteins catalogued as PWWP2B, underscoring that shared domains do not ensure conserved methyltransferase activity.

The primary DNMT3A-DNMT3L structure contains two DNMT3A catalytic sites in a heterotetramer, with DNMT3L providing activating interfaces rather than extra catalytic centers. This establishes catalytic versus regulatory subunit roles independently of family names. Other DNMT3 and DRM branches prevent an exhaustive catalytic grant restricted to the sampled DNMT3A subfamily.

**Exact benchmark/reference members:** HORSE/DNMT3L (A0A9L0T837), HORSE/DNMT3A (A0A9L0TK01), human/DNMT3L (Q9UJW3), human/DNMT3A (Q9Y6K1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA (cytosine-5-)-methyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003886) (GO:0003886) | UNRESOLVED | DNMT3A in SF10 is a demonstrated catalytic DNA methyltransferase, while DNMT3L in SF13 is a catalytically inactive regulator. DNMT3B and active DRM proteins show that catalytic activity is not exclusive to the DNMT3A branch. The full boundary across DNMT3, DRM and other domain-related proteins has not been established, so no exhaustive allowed-subfamily set is asserted. This uncertainty concerns family-wide coverage; it does not weaken the established DNMT3A activity or the DNMT3L noncatalytic distinction. |
| [enzyme activator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008047) (GO:0008047) | UNRESOLVED | DNMT3L in SF13 activates DNMT3 methyltransferase partners through complex formation. This is a positive regulatory function distinct from DNA methyltransferase catalysis. The available evidence does not establish that enzyme-activator activity is exclusive to SF13 across all noncatalytic and regulatory relatives, so the complete family-wide scope remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23068/PTHR23068-review.yaml)

## PTHR23122

**MPP/CASK MAGUK interaction scaffolds** — HETEROGENEOUS; COMPLETE

MPP-like and CASK-like MAGUK proteins assemble membrane-associated interaction complexes using conserved PDZ, SH3 and guanylate-kinase-like modules. Fly Metro stabilizes a perisynaptic complex with Dlg and DLin-7 through L27-domain interactions. The guanylate-kinase-like domain is an interaction module and does not establish GMP phosphorylation.

The inventory includes MPP/PALS and CASK/LIN-2 proteins with different amino-terminal architectures. A kinase-domain property of CASK cannot be transferred to Metro, while guanylate-kinase catalysis must not be inferred from the MAGUK acronym. Synaptic and epithelial polarity complexes also require member-specific assignment.

**Exact benchmark/reference members:** DROME/metro (A1Z8G0)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23122/PTHR23122-review.yaml)

## PTHR23172

**Auxilin and GAK-related J-domain proteins** — HETEROGENEOUS; COMPLETE

Auxilin-related proteins couple recognition of membrane-associated assemblies to Hsp70 chaperone recruitment. GAK adds a kinase domain, while auxilin contains a phosphatase-like region with a noncatalytic binding role.

The zebrafish sequence has tensin-like phosphatase/C2 regions and a terminal J domain. The experimentally characterized auxilin P-loop geometry explains lack of phosphatase activity, so a phosphatase-like domain does not license intrinsic dephosphorylation. Participation in a dephosphorylation process remains distinct from catalysis and requires partner evidence.

**Exact benchmark/reference members:** DANRE/A0A8M9QG43 (A0A8M9QG43)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [dephosphorylation](https://www.ebi.ac.uk/QuickGO/term/GO:0016311) (GO:0016311) | UNRESOLVED | Bovine auxilin has a PTEN-like fold but a P-loop geometry incompatible with phosphatase catalysis, providing a direct noncatalytic-domain counterexample. The zebrafish protein has the corresponding phosphatase/C2/J-domain architecture. This rejects a catalytic inference from the fold, while the broader biological process dephosphorylation could still involve an unestablished partner-mediated role; family-wide process membership is unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23172/PTHR23172-review.yaml)

## PTHR23192

**Olfactomedin-domain extracellular proteins** — HETEROGENEOUS; COMPLETE

Olfactomedin-domain proteins include OLFML2A/2B, noelins, myocilin and gliomedin. Extracellular and membrane-associated architectures occur, with distinct ligand interactions, tissue distributions and matrix or signaling roles.

Mouse OLFML2A/photomedin experiments support extracellular localization and glycosaminoglycan binding. This is a justified starting point for OLFML2A ortholog comparison, but matrix residence, matrix assembly and specific binding each require their own evidence. The short primate target and the horse gene-model differences require separate completeness checks; no single matrix function is safe across the entire olfactomedin family.

**Exact benchmark/reference members:** 9PRIM/A0A8C9H4D2 (A0A8C9H4D2), HORSE/OLFML2A (A0A9L0SKW1), human/OLFML2A (Q68BL7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [extracellular matrix](https://www.ebi.ac.uk/QuickGO/term/GO:0031012) (GO:0031012) | UNRESOLVED | Photomedins are experimentally secreted extracellular proteins that bind selected glycosaminoglycans. Extracellular presence and matrix binding support an ECM-associated hypothesis for OLFML2A orthologs but do not establish stable ECM membership for every olfactomedin protein. The short primate sequence and altered horse leader require product-specific secretion checks. |
| [extracellular matrix organization](https://www.ebi.ac.uk/QuickGO/term/GO:0030198) (GO:0030198) | UNRESOLVED | An ECM-screening study measured matrix assembly among several distinct candidate functions, but the fact that a protein was screened is not a positive assembly result. The photomedin binding study establishes extracellular interactions, not by itself extracellular-matrix organization. An actual assembly phenotype or member-specific functional result is required before extending this process. |
| [identical protein binding](https://www.ebi.ac.uk/QuickGO/term/GO:0042802) (GO:0042802) | UNRESOLVED | Photomedin-1 is experimentally secreted as disulfide-bonded dimers, providing a concrete OLFML2A self-association result. Other olfactomedins have different oligomeric architectures and proteolytic processing. Retention of the relevant association region, not merely the olfactomedin domain, determines whether this interaction transfers. |
| [extracellular matrix binding](https://www.ebi.ac.uk/QuickGO/term/GO:0050840) (GO:0050840) | UNRESOLVED | Photomedins preferentially bind chondroitin sulfate-E and heparin among tested ECM components. This directly supports matrix-component binding for those characterized proteins without specifying all olfactomedin ligands or functions. The complete binding-positive branch boundary and integrity of the selected products remain unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23192/PTHR23192-review.yaml)

## PTHR23211

**TGN38-related membrane trafficking proteins** — UNKNOWN; COMPLETE

The TGN38-related grouping includes the divergent fly regeneration protein Regeneration (Rgn). Fly rgn genetics supports a role in the formation of a proliferative regeneration blastema, while the relationship between that function and the intracellular trafficking mechanism associated with TGN38 remains unresolved.

Fly rgn regulates the timing of blastema formation and regenerative cellular plasticity in imaginal discs (PMID:18485344). This is direct positive genetic evidence for the fly branch, not merely an uncharacterized sequence. However, the signal peptide and C-type-lectin-like architecture of the exact long rgn product do not by themselves establish trans-Golgi residence or a conserved TGN38 trafficking cycle. Neither the family name nor a regeneration phenotype specifies the molecular ligand, compartment or vesicular mechanism.

**Exact benchmark/reference members:** DROME/rgn (M9PFV8)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23211/PTHR23211-review.yaml)

## PTHR23415

**NIP7 and CKS proteins grouped by PANTHER** — HETEROGENEOUS; COMPLETE

This PANTHER group combines NIP7 ribosome-biogenesis proteins with cyclin-dependent kinase regulatory subunits. NIP7 supports large-subunit pre-rRNA processing, whereas CKS proteins regulate kinase-associated cell-cycle machinery. These roles are biologically distinct despite their grouping under one family identifier.

PANTHER groups NIP7 and CKS entries together, but their functions differ. The exact pombe Nip7 accession Q1MTQ9 is identified as entity 43/chain l in the experimentally determined early pre-60S structure 8ESQ. This directly supports its preribosome association and separates it from mature-ribosome structural proteins and CKS cell-cycle regulators.

**Exact benchmark/reference members:** SCHPO/nip7 (Q1MTQ9)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [preribosome, large subunit precursor](https://www.ebi.ac.uk/QuickGO/term/GO:0030687) (GO:0030687) | UNRESOLVED | Pombe Nip7 is present in the experimentally determined early pre-60S particle 8ESQ. This establishes the target assembly-factor context, not membership of all CKS-containing family products in preribosomes. The complete set of NIP7-bearing subfamilies is not enumerated. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23415/PTHR23415-review.yaml)

## PTHR23423

**OST-alpha/TMEM184/Hfl1 membrane proteins** — HETEROGENEOUS; COMPLETE

This membrane-protein group includes OST-alpha transporters, TMEM184 proteins and fungal Hfl1. Characterized mammalian OST-alpha works with OST-beta in organic-solute transport, while Hfl1 recruits Atg8 during vacuolar membrane-protein turnover. A membrane-transport name therefore does not specify a conserved substrate or even the same cellular mechanism for every member.

Curated IPR005178 explicitly includes OST-alpha, TMEM184 proteins and fungal Hfl1, while the inventory also contains plant LAZ1 proteins. OST-alpha/OST-beta bile-acid export and Hfl1-mediated Atg8 recruitment are distinct mechanisms. CG6836 is an OST-alpha-like sequence with inferred transport function; the evidence does not identify its substrate or require a mammalian intestinal transport mechanism.

**Exact benchmark/reference members:** DROME/CG6836 (Q9VVV2)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR23423/PTHR23423-review.yaml)

## PTHR24055

**MAP kinases and related CMGC kinases** — HETEROGENEOUS; COMPLETE

MAPK-related proteins include classical ERK, JNK, p38/Hog1 and plant MAPKs alongside other CMGC branches such as NLK-related kinases. They share phosphorylation chemistry but differ in activation systems and substrates.

For the cucumber target, kinase-domain and MAPK placement support a protein-phosphorylation comparison. Animal growth-factor pathways and fungal osmotic-stress pathways are not interchangeable with plant MAPK functions. Resolve the relevant plant paralog before transferring a named signaling pathway.

**Exact benchmark/reference members:** CUCME/A0A1S3BTE3 (A0A1S3BTE3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [MAP kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004707) (GO:0004707) | UNRESOLVED | The cucumber target has a MAP-kinase conserved-site signature, supporting MAPK-type phosphotransfer rather than an arbitrary kinase label. Classical MAPKs and divergent CMGC relatives nevertheless differ in activation-loop regulation and upstream kinases. The complete functional boundary cannot be inferred from a rule-generated catalytic equation or extended to every CMGC-like member without catalytic and activation-mechanism evidence. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24055/PTHR24055-review.yaml)

## PTHR24056

**CDK and CDK-like protein kinases** — HETEROGENEOUS; COMPLETE

CDKs and CDK-like kinases regulate cell-cycle events, transcription and other processes through protein phosphorylation. Cyclin or other activator requirements and substrate repertoires differ among paralogs.

Human CDK7 has direct biochemical support for cyclin-H/MAT1-dependent activity; the horse sequence aligns over the complete human CDK7 sequence with an additional region. This supports a bounded CDK7 comparison, not extension of TFIIH or CDK-activating-kinase functions to all CDKs. Cyclin dependence itself requires distinguishing classical CDKs from divergent CDK-like proteins.

**Exact benchmark/reference members:** BALMU/A0A8B8WEG2 (A0A8B8WEG2), HORSE/CDK7 (A0A9L0R074), human/CDK7 (P50613)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [cyclin-dependent protein serine/threonine kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004693) (GO:0004693) | UNRESOLVED | CDK7 kinase assays and its cyclin-H/MAT1 requirement provide direct cyclin-dependent activity evidence; CDK1 and CDK2 supply distinct positive cell-cycle branches. Divergent CDK-like kinases can have other activators, so the complete cyclin-dependent set is not identical to CDK7 or all kinase-domain members. Neither different substrates nor a different tissue context is evidence against the shared reaction in established CDKs. |
| [protein phosphorylation](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) (GO:0006468) | UNRESOLVED | Protein phosphorylation is directly established for CDK7 and other CDK branches. The human-horse alignment supports the horse CDK7 comparison without assigning every CDK the TFIIH or CDK-activating-kinase role. Catalytic competence in divergent CDK-like proteins and incomplete products remains the unresolved limit on a universal family grant. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24056/PTHR24056-review.yaml)

## PTHR24061

**Class-C GPCR ligand-recognition proteins** — HETEROGENEOUS; COMPLETE

This group links class-C receptor proteins whose extracellular ligand-recognition regions support distinct sensory functions. Calcium-sensing, glutamate-responsive and vomeronasal receptors cannot be assigned each other's ligands from shared receptor architecture. For mouse Vmn2r73, receptor-family placement is a starting point for investigating vomeronasal signaling, not proof of a particular pheromone or peptide ligand.

Class C receptor proteins share extracellular ligand-recognition architecture but differ in ligand specificity. The selected Vmn2r73 product retains its ligand-binding region and lacks the intact seven-transmembrane module, as established by exact comparison with the longer same-gene product. The primary mGlu5 structural study distinguishes extracellular ligand binding from seven-transmembrane G-protein coupling.

**Exact benchmark/reference members:** mouse/Vmn2r73 (A0A3B2WCZ5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [G protein-coupled receptor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004930) (GO:0004930) | UNRESOLVED | Full-length class C receptors require a seven-transmembrane G-protein-coupling module. The selected 496-residue Vmn2r73 product lacks that module and cannot receive the activity merely from family membership. This target counterexample does not delimit all receptor-competent products across the family. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24061/PTHR24061-review.yaml)

## PTHR24067

**E2 ubiquitin-like modifier conjugases and E2-like regulators** — HETEROGENEOUS; COMPLETE

The E2 fold includes enzymes for ubiquitin, SUMO, NEDD8 and ISG15 conjugation as well as noncatalytic E2-like regulators. Catalytic thiol chemistry and modifier recognition must both be considered when transferring enzyme functions.

NCU04302 aligns across its full length to experimentally characterized Ubc9 proteins, and Ubc9 forms a SUMO thioester. Rabbit G1TUN6 instead belongs to a ubiquitin/ISG15-associated comparison. Generic transferase activity does not identify the modifier, and cannot be assigned to every E2-like regulator. SUMO, NEDD8 and ubiquitin reaction labels are not interchangeable.

**Exact benchmark/reference members:** RABIT/G1TUN6 (G1TUN6), NEUCR/NCU04302 (Q1K772)

**Separate canonical gene context:** F8WDQ9; exact inputs remain unassigned. See [identity evidence](unassigned-cases.md).

| Function / process / component | Scope | Boundary |
|---|---|---|
| [transferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016740) (GO:0016740) | UNRESOLVED | Thioester formation and modifier transfer are demonstrated for Ubc9/SUMO and UbcH8/ISG15 branches, whereas noncatalytic E2-like proteins can retain the fold without transfer. The Hus5.62 experiment further shows that even formation of a SUMO thioester does not guarantee productive substrate conjugation. The complete catalytic/noncatalytic branch boundary is unresolved; ubiquitin, SUMO and NEDD8 specificity require separate evidence. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24067/PTHR24067-review.yaml)

## PTHR24072

**RHO FAMILY GTPASE** — HETEROGENEOUS; COMPLETE

Rho-family proteins share a small-GTPase fold and regulate cellular organization through nucleotide-dependent interactions. Their catalytic and regulatory properties vary among conventional and atypical branches.

Direct full-length RHOJ/TCL experiments establish GDP/GTP exchange and intrinsic GTP hydrolysis, while mutational analysis identifies N-terminal and distal-loop determinants of exchange and membrane association. This does not establish identical kinetics for other Rho branches. The selected 153-residue RHOJ product preserves only the first 103 residues continuously and has a divergent remainder lacking the complete reference nucleotide-recognition architecture.

**Exact benchmark/reference members:** human/RHOJ (G3V4H1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [GTPase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003924) (GO:0003924) | UNRESOLVED | Full-length RHOJ is directly demonstrated to hydrolyze GTP, so RHOJ must not be labelled GTPase-deficient simply by analogy to atypical Rnd proteins. The benchmark product has a disrupted distal sequence and cannot inherit intact RHOJ kinetics. Across the broader family, nucleotide regulation and catalytic competence require branch- and product-specific evidence. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24072/PTHR24072-review.yaml)

## PTHR24086

**NUCLEAR RECEPTOR SUBFAMILY 5 GROUP A** — MOSTLY_COHERENT; COMPLETE

NR5-family nuclear receptors are DNA-binding transcriptional regulators that include vertebrate steroidogenic and metabolic regulators and insect FTZ-F1 proteins. They share nuclear-receptor domain architecture while controlling lineage-specific developmental and physiological programs.

FTZ-F1 was purified as a sequence-specific DNA-binding factor and binding-site mutation reduced target-gene expression (PMID:2113881). Mammalian NR5A proteins rescued fly ftz-f1 mutants and activated the fly target gene (PMID:23340581), providing unusually strong cross-species evidence for conserved DNA-binding transcriptional regulation. This supports the broad molecular function across intact NR5 DNA-binding/receptor architecture. Steroid ligand responsiveness, steroidogenesis, bile-acid regulation and developmental timing remain branch-specific properties.

**Exact benchmark/reference members:** DROME/ftz-f1 (M9NFK2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-binding transcription factor activity, RNA polymerase II-specific](https://www.ebi.ac.uk/QuickGO/term/GO:0000981) (GO:0000981) | FAMILY_WIDE | FTZ-F1 was purified as a sequence-specific DNA-binding factor and binding-site mutation reduced target-gene expression (PMID:2113881). Mammalian NR5A proteins rescued fly ftz-f1 mutants and activated the fly target gene (PMID:23340581), providing unusually strong cross-species evidence for conserved DNA-binding transcriptional regulation. This supports the broad molecular function across intact NR5 DNA-binding/receptor architecture. Steroid ligand responsiveness, steroidogenesis, bile-acid regulation and developmental timing remain branch-specific properties. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24086/PTHR24086-review.yaml)

## PTHR24177

**Caskin-associated family with unresolved plant placement** — UNKNOWN; COMPLETE

The PANTHER family carries a Caskin name, but the benchmark member is a maize sequence. A cross-kingdom match needs architectural verification before the functions of animal neuronal scaffolds can be assigned to the plant protein.

The maize sequence has PGG domains rather than an experimentally established Caskin scaffold architecture. The PANTHER match is retained as a database relationship without assigning neuronal signaling, enzyme activity or a channel function. The broad molecular-function root does not resolve its biological activity.

**Exact benchmark/reference members:** MAIZE/A0A804UIX9 (A0A804UIX9)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [molecular_function](https://www.ebi.ac.uk/QuickGO/term/GO:0003674) (GO:0003674) | UNRESOLVED | GO:0003674 is the molecular-function root and supplies no testable specific activity. The maize protein has PGG domains rather than evidence for the neuronal Caskin scaffold mechanism suggested by the PANTHER label. Its family match is recorded, but neither a particular molecular function nor absence of function is asserted; architecture and functional characterization remain unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24177/PTHR24177-review.yaml)

## PTHR24198

**ANKYRIN REPEAT AND PROTEIN KINASE DOMAIN-CONTAINING PROTEIN** — HETEROGENEOUS; COMPLETE

Ankyrin-repeat proteins form a broad interaction-module grouping spanning cytoskeletal ankyrins, kinase-containing signaling proteins, ubiquitin-system adaptors and toxins. The repeats provide protein-contact surfaces; the surrounding domains determine the biological mechanism.

Giant fly Ank2 organizes presynaptic microtubules and stabilizes synapses (PMID:18439405; PMID:18439406). The actual member inventory also contains latrotoxins, ASB proteins, RIPK4 and viral ankyrin proteins, including disparate architectures within SF165. Consequently neither toxin activity nor kinase activity is a family-wide property. The exact 697-residue Ank2 benchmark product requires isoform-specific interpretation; its placement does not make every function of a giant ankyrin experimentally established on that product.

**Exact benchmark/reference members:** DROME/Ank2 (Q3KN55)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [toxin activity](https://www.ebi.ac.uk/QuickGO/term/GO:0090729) (GO:0090729) | UNRESOLVED | Giant fly Ank2 organizes presynaptic microtubules and stabilizes synapses (PMID:18439405; PMID:18439406). The actual member inventory also contains latrotoxins, ASB proteins, RIPK4 and viral ankyrin proteins, including disparate architectures within SF165. Consequently neither toxin activity nor kinase activity is a family-wide property. The exact 697-residue Ank2 benchmark product requires isoform-specific interpretation; its placement does not make every function of a giant ankyrin experimentally established on that product. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24198/PTHR24198-review.yaml)

## PTHR24221

**ATP-BINDING CASSETTE SUB-FAMILY B** — HETEROGENEOUS; COMPLETE

ABCB-related transporters combine ATP-binding domains with membrane-spanning regions to move chemically diverse substrates. Members occur in different membranes and include bacterial exporters and eukaryotic organellar and cellular transport systems.

Intact ABCB-type transporters couple an ATP-binding cassette to membrane transport, but their substrates and compartments vary. Drosophila HMT1 rescues cadmium sensitivity and localizes to the vacuolar membrane in the tested yeast system, yet it does not transport cadmium-phytochelatin complexes (PMID:19001374). Human ABCB6 structures instead establish porphyrin/hemin recognition (PMID:35950458). These results support the broad ABC-type transporter mechanism while excluding a family-wide phytochelatin, cadmium or heme substrate assignment; complete transporter architecture remains necessary.

**Exact benchmark/reference members:** DROME/Hmt-1 (Q9VF20)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ABC-type transporter activity](https://www.ebi.ac.uk/QuickGO/term/GO:0140359) (GO:0140359) | FAMILY_WIDE | Intact ABCB-type transporters couple an ATP-binding cassette to membrane transport, but their substrates and compartments vary. Drosophila HMT1 rescues cadmium sensitivity and localizes to the vacuolar membrane in the tested yeast system, yet it does not transport cadmium-phytochelatin complexes (PMID:19001374). Human ABCB6 structures instead establish porphyrin/hemin recognition (PMID:35950458). These results support the broad ABC-type transporter mechanism while excluding a family-wide phytochelatin, cadmium or heme substrate assignment; complete transporter architecture remains necessary. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24221/PTHR24221-review.yaml)

## PTHR24243

**G-PROTEIN COUPLED RECEPTOR** — HETEROGENEOUS; COMPLETE

This rhodopsin-like receptor family contains membrane receptors that couple ligand recognition to cellular signaling. The GHSR branch recognizes ghrelin and growth-hormone secretagogues and regulates endocrine and feeding responses.

GHSR recognition of ghrelin is supported by ligand isolation (PMID:10604470) and a ghrelin-bound receptor–G-protein structure (PMID:35027551). The experimentally anchored SF7 branch supports this activity, but other GHSR-like and broader receptor branches have not been resolved into an exhaustive ligand-specific set. Seven-transmembrane architecture alone does not specify growth-hormone-secretagogue recognition, G-protein preference or an endocrine phenotype.

**Exact benchmark/reference members:** HORSE/GHSR (F6QF00), human/GHSR (Q92847)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [growth hormone secretagogue receptor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0001616) (GO:0001616) | UNRESOLVED | GHSR recognition of ghrelin is supported by ligand isolation (PMID:10604470) and a ghrelin-bound receptor–G-protein structure (PMID:35027551). The experimentally anchored SF7 branch supports this activity, but other GHSR-like and broader receptor branches have not been resolved into an exhaustive ligand-specific set. Seven-transmembrane architecture alone does not specify growth-hormone-secretagogue recognition, G-protein preference or an endocrine phenotype. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24243/PTHR24243-review.yaml)

## PTHR24250

**CHYMOTRYPSIN-RELATED** — HETEROGENEOUS; COMPLETE

Chymotrypsin-related proteins include active serine proteases and noncatalytic protease-fold proteins. Drosophila Scarface is a secreted regulator of epithelial morphogenesis and laminin organization that lacks the canonical protease catalytic triad. Its retained fold does not establish endopeptidase activity.

The inventory contains active chymotrypsins alongside inactive serine protease 54 and Scarface. Scarface Q7K5M0 is secreted and controls epithelial laminin distribution, with published sequence-based loss of the canonical catalytic triad (PMID:20379222). Thus catalytic activity is not family-wide. Its official SF27 elastase-like label is a classification label, not evidence that Scarface cleaves elastin or other proteins.

**Exact benchmark/reference members:** DROME/scaf (Q7K5M0)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [serine-type endopeptidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004252) (GO:0004252) | UNRESOLVED | The inventory contains active chymotrypsins alongside inactive serine protease 54 and Scarface. Scarface Q7K5M0 is secreted and controls epithelial laminin distribution, with published sequence-based loss of the canonical catalytic triad (PMID:20379222). Thus catalytic activity is not family-wide. Its official SF27 elastase-like label is a classification label, not evidence that Scarface cleaves elastin or other proteins. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24250/PTHR24250-review.yaml)

## PTHR24251

**CUB-domain extracellular and membrane proteins** — HETEROGENEOUS; COMPLETE

CUB domains occur in extracellular recognition proteins, cubilin, procollagen-processing factors, metalloproteases and membrane receptors. A common extracellular interaction module is distinct from the activity of additional catalytic domains or a reproductive role.

The sponge target is a short CUB-domain protein. The domain is compatible with an extracellular interaction, but single fertilization is not a family-wide process. Ovomucin/ovochymase-style names must not imply protease activity or fertilization for cubilin, procollagen enhancers and unrelated CUB architectures.

**Exact benchmark/reference members:** AQUCT/A0A2G9RZF1 (A0A2G9RZF1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [single fertilization](https://www.ebi.ac.uk/QuickGO/term/GO:0007338) (GO:0007338) | UNRESOLVED | CUB domains occur in reproductive recognition proteins but also in complement, matrix processing and other extracellular systems. The short sponge CUB-domain target does not establish a fertilization role, and the original CUB comparison explicitly describes functionally diverse proteins. The full set of reproductive branches is unresolved; sperm-associated examples cannot define the whole family. |
| [extracellular region](https://www.ebi.ac.uk/QuickGO/term/GO:0005576) (GO:0005576) | UNRESOLVED | The original CUB-domain comparison and the benchmark domain architecture support an extracellular interaction-module hypothesis. Secreted proteins and membrane-receptor ectodomains must still be distinguished from truncated or untargeted products. An extracellular CUB module supports location by comparison, but does not establish every full-length family architecture as a soluble extracellular protein. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24251/PTHR24251-review.yaml)

## PTHR24256

**TRYPTASE-RELATED** — HETEROGENEOUS; COMPLETE

This insect protease-related family contains proteins with serine-protease-like domains and variable additional architecture. Catalytic enzymes and noncatalytic protease homologues can participate in immune or developmental systems through different mechanisms.

The insect SP/SPH classification separates catalytic serine proteases from homologues lacking the canonical active-site constellation (PMID:30367934). The CG43124 and CG4793 sequence analyses evaluate complete native isoforms rather than treating short proteins as pipeline truncations. The immune phenotype of CG4793 (PMID:33644706) establishes biological participation, not a measured peptide-cleavage reaction. Intrinsic serine endopeptidase activity remains branch- and architecture-dependent, so a universal or exhaustive subfamily grant is not established.

**Exact benchmark/reference members:** DROME/CG43124 (A0A0B4K7P3), DROME/CG4793 (Q8IP30), DROME/CG34171 (X2JEK1), DROME/CG43742 (A0A0B4KFF2), DROME/CG30288 (Q8IRK6), DROME/CG30287 (Q8MLV8), DROME/CG17404 (Q9VGC0)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [serine-type endopeptidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004252) (GO:0004252) | UNRESOLVED | The insect SP/SPH classification separates catalytic serine proteases from homologues lacking the canonical active-site constellation (PMID:30367934). The CG43124 and CG4793 sequence analyses evaluate complete native isoforms rather than treating short proteins as pipeline truncations. The immune phenotype of CG4793 (PMID:33644706) establishes biological participation, not a measured peptide-cleavage reaction. Intrinsic serine endopeptidase activity remains branch- and architecture-dependent, so a universal or exhaustive subfamily grant is not established. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24256/PTHR24256-review.yaml)

## PTHR24324

**HOMEOBOX PROTEIN HHEX** — HETEROGENEOUS; COMPLETE

Homeobox proteins share a compact DNA-recognition domain and have diversified into regulators of many cellular and developmental programs. Fungal members include transcriptional regulators with functions that differ from animal developmental homeobox proteins.

The inventory contains animal HHEX and fungal Pho2, Yox1/Yhp1 and Phx1-related regulators. Neurospora kal-1/NCU03593 has a homeodomain and a directly described colony-morphology deletion phenotype (PMID:16801547, Figure 3). These support a fungal developmental-regulatory interpretation, but the phenotype does not determine a DNA recognition sequence or activator versus repressor mechanism, and the HHEX subfamily label does not establish vertebrate development.

**Exact benchmark/reference members:** NEUCR/kal-1 (Q7S7W0)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-binding transcription factor activity, RNA polymerase II-specific](https://www.ebi.ac.uk/QuickGO/term/GO:0000981) (GO:0000981) | UNRESOLVED | The inventory contains animal HHEX and fungal Pho2, Yox1/Yhp1 and Phx1-related regulators. Neurospora kal-1/NCU03593 has a homeodomain and a directly described colony-morphology deletion phenotype (PMID:16801547, Figure 3). These support a fungal developmental-regulatory interpretation, but the phenotype does not determine a DNA recognition sequence or activator versus repressor mechanism, and the HHEX subfamily label does not establish vertebrate development. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24324/PTHR24324-review.yaml)

## PTHR24351

**AGC-related protein kinases** — HETEROGENEOUS; COMPLETE

This family includes PKC, PKN, SGK, AKT and ribosomal-S6-kinase-related proteins. Regulatory domains, activating inputs and physiological substrates diverge markedly despite shared kinase chemistry.

The Xenopus target's kinase classification supports analysis of intrinsic phosphotransfer, but S6 phosphorylation is not a universal property of the family. Calcium, diacylglycerol, cyclic-nucleotide and growth-factor regulation each require the corresponding regulatory architecture and paralog placement.

**Exact benchmark/reference members:** XENTR/A0A8J1IYX6 (A0A8J1IYX6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein serine/threonine kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004674) (GO:0004674) | UNRESOLVED | The Xenopus member has PKC-delta-related kinase architecture, making serine/threonine phosphotransfer a plausible core reaction. PKC, AKT, SGK, PKN and S6-kinase branches differ in activators and regulatory domains; these differences do not by themselves refute the broad catalytic reaction. The available family-wide evidence does not inventory catalytic losses or truncated domains, so a universal grant remains unestablished; S6 substrate specificity is not inferred. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24351/PTHR24351-review.yaml)

## PTHR24381

**C2H2 zinc-finger regulatory proteins** — HETEROGENEOUS; COMPLETE

This large family collects C2H2 zinc-finger proteins with diverse DNA-recognition sequences, transcriptional effects and accessory domains. Activators, repressors and proteins with specialized architectural roles cannot be summarized by a common transcriptional direction.

The Xenopus target has repeated C2H2 fingers and a curated transcription-factor inference. This supports a focused nuclear DNA-regulatory hypothesis but cannot establish activation rather than repression. Nuclear localization and RNA-polymerase-II regulation remain branch-level claims, not consequences of any isolated zinc finger.

**Exact benchmark/reference members:** XENTR/A0A8J0SCI2 (A0A8J0SCI2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [RNA polymerase II cis-regulatory region sequence-specific DNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0000978) (GO:0000978) | UNRESOLVED | An array of C2H2 fingers is compatible with sequence-specific DNA recognition, but it does not identify a RNA-polymerase-II cis-regulatory site, and some related fingers participate in RNA or protein interactions. The Xenopus array supports a targeted DNA-binding hypothesis without specifying the bound motif or a universal family-wide regulatory sequence. |
| [regulation of transcription by RNA polymerase II](https://www.ebi.ac.uk/QuickGO/term/GO:0006357) (GO:0006357) | UNRESOLVED | The family includes zinc-finger activators, repressors and proteins with other interaction roles. RNA-polymerase-II regulation requires an experimentally anchored regulatory branch and appropriate effector interactions, not simply metal-coordinating fingers. The available target architecture does not establish an exhaustive Pol-II-regulatory set. |
| [nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0005634) (GO:0005634) | UNRESOLVED | Many characterized zinc-finger transcription factors act in nuclei, but the C2H2 fold is not a localization signal in itself. The Xenopus sequence has a plausible nuclear DNA-regulatory architecture; the complete distribution of nuclear localization across the large heterogeneous family remains unresolved. |
| [DNA-binding transcription activator activity, RNA polymerase II-specific](https://www.ebi.ac.uk/QuickGO/term/GO:0001228) (GO:0001228) | UNRESOLVED | Activation is a direction-specific transcriptional claim. An intact zinc-finger array, absence of a KRAB motif, or a generic transcription-factor inference does not demonstrate recruitment of coactivators rather than repression. A direct reporter, transcriptional perturbation or established activating branch is required for this narrower term. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24381/PTHR24381-review.yaml)

## PTHR24419

**INTERLEUKIN-1 RECEPTOR-ASSOCIATED KINASE** — HETEROGENEOUS; COMPLETE

This kinase-related family contains signaling proteins with differing catalytic competence and regulatory roles. The IRAK3 branch regulates signaling downstream of IL-1 and Toll-like receptors and has a noncanonical kinase active-site configuration.

The original IRAK-M paper reports negligible autophosphorylation while retaining signaling complementation, and the later primary structure documents a conserved noncanonical CGS catalytic loop and DFA Mg-binding loop. The horse sequence preserves those motifs at 249–251 and 269–271 respectively. This supports a pseudokinase regulatory architecture while leaving possible alternative chemistry distinct from conventional IRAK1/4 kinase activity.

**Exact benchmark/reference members:** HORSE/IRAK3 (A0A3Q2HDT6), human/IRAK3 (Q9Y616)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004672) (GO:0004672) | UNRESOLVED | Canonical kinase activity is directly established for IRAK1/4 but cannot be granted to the whole IRAK family. IRAK3 has a noncanonical active-site configuration and negligible autophosphorylation in the original report; its role in phosphorylation-dependent signaling does not establish intrinsic phosphate transfer. Horse IRAK3 retains the human CGS/DFA configuration. This rejects an unqualified catalytic default without claiming that every alternative reaction has been experimentally excluded. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR24419/PTHR24419-review.yaml)

## PTHR28518

**TRNA-SPLICING ENDONUCLEASE SUBUNIT SEN15** — MOSTLY_COHERENT; COMPLETE

Sen15 proteins are structural components of eukaryotic tRNA-splicing endonuclease complexes. They support the assembly and function of a complex whose catalytic subunits cleave intron-containing precursor tRNAs.

Sen15 is a structural subunit of the eukaryotic tRNA-splicing endonuclease, whereas primary yeast experiments locate the two cleavage active sites in Sen2 and Sen34 (PMID:9200603). Pombe Sen15 has the fungal Sen15 signature. Participation in tRNA intron removal is conserved, but isolated Sen15 endonuclease activity is not supported. The evidence does not require a Sen15/Sen34-only alpha2-beta2 model of the functional heterotetramer.

**Exact benchmark/reference members:** SCHPO/sen15 (Q7LKV3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [tRNA splicing, via endonucleolytic cleavage and ligation](https://www.ebi.ac.uk/QuickGO/term/GO:0006388) (GO:0006388) | FAMILY_WIDE | The conserved function represented by tRNA splicing, via endonucleolytic cleavage and ligation is the family core for intact members. Participation in tRNA intron removal is compatible with Sen15's structural role. Intrinsic tRNA endonuclease activity belongs to the catalytic subunits and should not be inherited by Sen15 merely because the protein is part of the endonuclease complex. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR28518/PTHR28518-review.yaml)

## PTHR30173

**ECF sigma factors** — COHERENT; COMPLETE

These bacterial extracytoplasmic-function sigma factors direct promoter recognition by RNA polymerase during transcription initiation. Their promoter targets and inducing conditions vary among lineages.

The sigma-factor domain architecture and PAINT sigma-factor annotation support transcription initiation. Neither an exact regulon nor a particular stress response follows from the shared family.

**Exact benchmark/reference members:** STRCO/Q9KZ33 (Q9KZ33)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-templated transcription initiation](https://www.ebi.ac.uk/QuickGO/term/GO:0006352) (GO:0006352) | FAMILY_WIDE | The ECF sigma-70 architecture and the PAINT IBD for sigma factor activity support recruitment of RNA polymerase to promoters for transcription initiation. This broad initiation role is the conserved function of intact ECF sigma factors in the retrieved family. Promoter sequence preference, regulon, inducing stress and anti-sigma partner are not part of this family-wide grant. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR30173/PTHR30173-review.yaml)

## PTHR31193

**TRANSMEMBRANE PROTEIN C9ORF91** — UNKNOWN; COMPLETE

TMEM268-family proteins contain a conserved DUF4481-associated membrane-protein architecture. In human gastric cancer cells, TMEM268 binds integrin beta4 and helps maintain integrin-associated adhesion machinery; its conserved biochemical activity and the corresponding role of fly CG18507 are unresolved.

Human TMEM268 interacts through its C terminus with ITGB4; knockout increases ITGB4 ubiquitin-mediated degradation and destabilizes ITGB4 and filamin A (PMID:30361615). This supports a protein-stability/adhesion mechanism in the tested cells, not an intrinsic ubiquitin-ligase or transport activity. Fly CG18507 shares the family/domain grouping but differs in length and membrane architecture, and no evidence identifies ITGB4 as its conserved partner. Functional coherence is unknown beyond the membrane-protein scaffold because the demonstrated mammalian mechanism is not yet established across the family.

**Exact benchmark/reference members:** DROME/CG18507 (M9PBB3)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR31193/PTHR31193-review.yaml)

## PTHR31458

**Polygalacturonase-associated BURP proteins** — HETEROGENEOUS; COMPLETE

BURP-domain proteins in this group include polygalacturonase-associated noncatalytic subunits and related plant proteins. A BURP domain does not itself establish glycoside hydrolase activity or a conserved reproductive phenotype.

The rice target has a signal peptide and BURP domain, consistent with a secreted protein. Pollen maturation needs gene-specific or well-resolved ortholog evidence; neither secretion nor a polygalacturonase-associated family name establishes it.

**Exact benchmark/reference members:** ORYSI/B8BAB0 (B8BAB0)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [pollen maturation](https://www.ebi.ac.uk/QuickGO/term/GO:0010152) (GO:0010152) | UNRESOLVED | The rice target is a secretory PG-associated BURP protein, not identified as a pollen-maturation factor by the domain evidence. BURP proteins participate in diverse cell-wall and developmental contexts, and PG1 beta-subunit family assignment does not supply a reproductive phenotype. Pollen expression alone would also be insufficient to establish involvement in maturation; member-specific perturbation evidence is required. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR31458/PTHR31458-review.yaml)

## PTHR31716

**PROTEIN FMC1 HOMOLOG** — UNKNOWN; COMPLETE

This grouping contains animal FMC1-related proteins with a proposed relationship to mitochondrial ATP synthase assembly factors. Yeast Fmc1 is a soluble mitochondrial-matrix protein that helps F1 assembly under heat stress; equivalent activity of the fly CG34117 family branch is not directly established.

The primary yeast study describes a nuclear-encoded mitochondrial-matrix protein, not a nuclear-localized protein. Fmc1 becomes important for F1 assembly at elevated temperature, and increased Atp12 dosage suppresses its deficiency (PMID:11096112). These observations define an assembly-factor mechanism rather than ATP synthesis or ATP hydrolysis by Fmc1 itself. The animal PANTHER grouping and the yeast experimental protein are not assumed to be identical subfamily assignments; transfer to fly CG34117 remains a homology-supported hypothesis with an unresolved conserved mechanism.

**Exact benchmark/reference members:** DROME/CG34117 (Q0KI97)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR31716/PTHR31716-review.yaml)

## PTHR31859

**TTC39/IML2 scaffold proteins** — HETEROGENEOUS; COMPLETE

TTC39/IML2-related proteins include metazoan TTC39 paralogs and fungal proteins associated with inclusion-body handling. Repeat-mediated interactions support distinct cellular functions in different branches.

The macaque target is assigned TTC39C. The primary screen explicitly includes zebrafish ttc39c, so the gene-level comparison is supported; the remaining question is whether the exact heart-asymmetry phenotype and ciliary mechanism transfer to this product. Fungal IML2 and other TTC39 paralogs do not inherit vertebrate laterality roles.

**Exact benchmark/reference members:** MACFA/A0A2K5UJ34 (A0A2K5UJ34)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [determination of heart left/right asymmetry](https://www.ebi.ac.uk/QuickGO/term/GO:0061371) (GO:0061371) | UNRESOLVED | The cited zebrafish screen explicitly tests ttc39c along with ttc4, ttc9c and ttc36, and reports cilia-related left-right-patterning defects. Thus the TTC39C comparison is supported at the gene level, but a pooled ciliopathy/laterality statement must be separated from a gene-specific heart-asymmetry measurement. This organismal process cannot be extended to fungal IML2 or all TTC39 paralogs, and the exact heart-specific positive branch boundary remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR31859/PTHR31859-review.yaml)

## PTHR32176

**Patatin-like lipolytic acyl hydrolases** — HETEROGENEOUS; COMPLETE

Patatin-like proteins include plant lipid hydrolases and bacterial phospholipase effectors. Intact catalytic domains support lipid ester hydrolysis, whereas truncated or inactive members retain family resemblance without the reaction. The current PANTHER vocabulary label 'xylose isomerase' does not describe the retrieved members.

A0A3B6GK97 lacks the N-terminal serine-containing catalytic region in the reproducible alignment. This blocks intrinsic lipase transfer to that deposited sequence, not lipid metabolism in every patatin homolog. Distinguish gene-model truncation from evolutionary catalytic loss.

**Exact benchmark/reference members:** WHEAT/A0A3B6GK97 (A0A3B6GK97)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [lipase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016298) (GO:0016298) | UNRESOLVED | Pat17 mutagenesis establishes a Ser-Asp-dependent lipid acyl hydrolase, and the wheat alignment shows deletion of the serine-containing half of that catalytic domain. This is positive family evidence with a specific incomplete-product exception. Lipase activity cannot be granted from a surviving patatin fragment, and the available member set does not delimit all catalytically competent branches. |
| [lipid catabolic process](https://www.ebi.ac.uk/QuickGO/term/GO:0016042) (GO:0016042) | UNRESOLVED | Lipid hydrolysis by intact patatins can contribute to lipid catabolism. Loss of the catalytic region in the wheat product argues against intrinsic hydrolysis but does not exclude every indirect lipid-metabolic interaction. A physiological lipid-catabolic role, its substrate and the complete distribution of active versus noncatalytic family members remain unestablished. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR32176/PTHR32176-review.yaml)

## PTHR33050

**Reverse-transcriptase-containing proteins** — HETEROGENEOUS; COMPLETE

Reverse-transcriptase domains occur in different mobile-element and viral architectures. The retrieved reviewed entries emphasize hepadnaviral polymerases, which do not establish the life cycle or integration mechanism of a metazoan repeat-associated sequence.

The mussel target contains a reverse-transcriptase domain, consistent with nucleic-acid engagement. DNA recombination and integration require additional machinery and cannot be inferred from reverse transcription alone. Distinguish hepadnavirus-like polymerase homology from a complete DIRS-like retroelement and verify companion domains before assigning an integration mechanism.

**Exact benchmark/reference members:** MYTGA/A0A8B6BFL6 (A0A8B6BFL6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003677) (GO:0003677) | UNRESOLVED | Reverse-transcriptase architecture supports binding a nucleic-acid template/product during polymerization, but an isolated domain annotation does not establish catalytic integrity or DNA-binding competence of this mussel product. The DIRS study is an element-level comparison in Dictyostelium, not a direct assay of the selected protein. The complete functional architecture and family-wide binding boundary remain unresolved. |
| [DNA recombination](https://www.ebi.ac.uk/QuickGO/term/GO:0006310) (GO:0006310) | UNRESOLVED | DIRS elements encode a tyrosine-recombinase-based integration system, but reverse transcriptase alone does not carry out DNA recombination. The mussel product has a reverse-transcriptase domain without an established companion recombinase system. A mobile-element comparison therefore cannot supply this process to every family member or to the selected sequence. |
| [DNA integration](https://www.ebi.ac.uk/QuickGO/term/GO:0015074) (GO:0015074) | UNRESOLVED | The DIRS experiments demonstrate productive retrotransposition requiring the internal complementary region and element-encoded machinery. These are requirements of a complete element, not consequences of any reverse-transcriptase domain. The mussel target and the hepadnaviral-like comparison set have no shared demonstrated integration mechanism, leaving the relevant branch boundary unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR33050/PTHR33050-review.yaml)

## PTHR33164

**MarR-family DNA regulators** — HETEROGENEOUS; COMPLETE

MarR-related helix-turn-helix regulators recognize distinct promoters and respond to different ligands or redox states. The group includes antibiotic-response regulators and many regulators of other physiological systems.

The Chromobacterium target's MarR-family placement supports a DNA-regulatory comparison. It does not establish antibiotic resistance, a particular ligand or the sign of regulation. Genomic context and direct operator/ligand evidence are needed for these narrower functions.

**Exact benchmark/reference members:** CHRVO/Q7NUH2 (Q7NUH2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-binding transcription factor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003700) (GO:0003700) | UNRESOLVED | Purified E. coli MarR binds its operator preferentially and represses the mar operon, directly validating the DNA-binding transcription-factor mechanism in a characterized branch. The Chromobacterium protein has the corresponding MarR-type winged-helix domain. Operator specificity, ligand response and complete functional competence of all branches are unresolved; antibiotic resistance is not implied by the generic TF function. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR33164/PTHR33164-review.yaml)

## PTHR34524

**CALCYPHOSIN** — MOSTLY_COHERENT; COMPLETE

Calcyphosin and calcyphosin-like proteins are EF-hand proteins with a calcium-sensing architecture. Human calcyphosin binds calcium in four EF-hand motifs and is largely monomeric; the related CAPSL branch retains calcium-binding-associated sequence signatures. Their specific cellular partners and conserved physiological outputs are incompletely characterized.

Human calcyphosin (CAPS, Q13938; verified SF2) has a calcium-loaded crystal structure with two pairs of calcium-binding EF hands (PMID:18775726). CAPSL proteins in SF5 retain paired EF-hand and calcium-binding-site signatures, supporting calcium binding by homology. The exact calcium affinities, ligand partners and physiological regulatory mechanism of CAPSL are not established. Calcium binding is a credible shared property, but its unconditional grant across the classified sequences remains unresolved without resolving EF-hand integrity; calcium transport or a specific signaling pathway does not follow from it.

**Exact benchmark/reference members:** HORSE/CAPSL (A0A3Q2I3U9), human/CAPSL (Q8WWF8)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [calcium ion binding](https://www.ebi.ac.uk/QuickGO/term/GO:0005509) (GO:0005509) | UNRESOLVED | Human calcyphosin (CAPS, Q13938; verified SF2) has a calcium-loaded crystal structure with two pairs of calcium-binding EF hands (PMID:18775726). CAPSL proteins in SF5 retain paired EF-hand and calcium-binding-site signatures, supporting calcium binding by homology. The exact calcium affinities, ligand partners and physiological regulatory mechanism of CAPSL are not established. Calcium binding is a credible shared property, but its unconditional grant across the classified sequences remains unresolved without resolving EF-hand integrity; calcium transport or a specific signaling pathway does not follow from it. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR34524/PTHR34524-review.yaml)

## PTHR35936

**Family-3 solute-binding and MltF-associated modules** — HETEROGENEOUS; COMPLETE

The family includes amino-acid-binding proteins and solute-binding modules associated with lytic transglycosylases. Binding-domain conservation does not establish either a membrane pore or the enzymatic activity of a fused domain.

The bacterial target is a small signal-peptide-bearing solute-binding protein without a multipass pore architecture. This argues against the proposed ligand-gated ion-channel activity for the target. MltF transglycosylase activity also cannot be assigned to isolated substrate-binding modules.

**Exact benchmark/reference members:** XENNA/D3VIU4 (D3VIU4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ligand-gated monoatomic ion channel activity](https://www.ebi.ac.uk/QuickGO/term/GO:0015276) (GO:0015276) | UNRESOLVED | The Xenorhabdus product is a signal-peptide-bearing soluble solute-binding module, without the transmembrane pore architecture required for a ligand-gated ion channel. MltF relatives combine such binding modules with a lytic transglycosylase domain, which is also not a channel. These observations refute the proposed mechanism for the inspected architectures but do not substitute for a complete domain inventory of every family branch. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR35936/PTHR35936-review.yaml)

## PTHR36695

**AGAP008648-PA** — UNKNOWN; COMPLETE

NtR belongs to an insect branch of the Cys-loop ligand-gated ion-channel superfamily. The neuronal-channel ligand-binding architecture and C-terminal membrane region support a channel-subunit role, while its gating ligand and ion selectivity remain unidentified.

The published Cys-loop phylogeny places Dmel NTR outside both nicotinic acetylcholine-receptor groups (PMID:30429615, Extended Data Figure 10d), and FlyBase classifies it with unclassified ligand-gated ion-channel subunits. This supports a channel-family mechanism without identifying acetylcholine, another transmitter or a particular ion as its ligand/substrate. No exact-target electrophysiological gating assay is available in the inspected sources, so the exhaustive activity grant remains unresolved. The additional methyltransferase-domain match is not evidence for a methyltransferase reaction.

**Exact benchmark/reference members:** DROME/NtR (Q9W288)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [extracellular ligand-gated monoatomic ion channel activity](https://www.ebi.ac.uk/QuickGO/term/GO:0005230) (GO:0005230) | UNRESOLVED | The published Cys-loop phylogeny places Dmel NTR outside both nicotinic acetylcholine-receptor groups (PMID:30429615, Extended Data Figure 10d), and FlyBase classifies it with unclassified ligand-gated ion-channel subunits. This supports a channel-family mechanism without identifying acetylcholine, another transmitter or a particular ion as its ligand/substrate. No exact-target electrophysiological gating assay is available in the inspected sources, so the exhaustive activity grant remains unresolved. The additional methyltransferase-domain match is not evidence for a methyltransferase reaction. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR36695/PTHR36695-review.yaml)

## PTHR38710

**Plant glucuronokinases** — COHERENT; COMPLETE

Glucuronokinases use ATP to phosphorylate glucuronic acid in a route for recycling uronic acids into nucleotide-sugar metabolism. They have GHMP-kinase architecture rather than the reaction implied by a uridyl-pyrophosphorylase name.

The wheat target has both GHMP-kinase regions and glucuronokinase-family placement. Biochemical ATP-dependent phosphate donation supports phosphorylation as a conserved reaction class; a complete substrate-specific assignment should retain the glucuronic-acid context.

**Exact benchmark/reference members:** WHEAT/A0A3B6NKR6 (A0A3B6NKR6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [phosphorylation](https://www.ebi.ac.uk/QuickGO/term/GO:0016310) (GO:0016310) | FAMILY_WIDE | Purified lily enzyme and recombinant Arabidopsis glucuronokinase establish ATP-dependent phosphorylation of glucuronic acid. The wheat target retains both GHMP-kinase regions and the glucuronokinase-specific family signature, supporting the shared broad phosphorylation process for intact glucuronokinase-family members. This does not grant uridyl-pyrophosphorylase activity or establish a tissue-specific role. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR38710/PTHR38710-review.yaml)

## PTHR40621

**TRANSCRIPTION FACTOR KAPC-RELATED** — HETEROGENEOUS; COMPLETE

Fungal Yap/AP-1-related bZIP transcription factors regulate stress-responsive gene expression. Their shared DNA-binding and dimerization architecture is used in distinct oxidative, chemical and metabolic response programs.

The inventory includes multiple Yap paralogs, HapX, Cap1 and arsenic-response Arr1 proteins. Primary Yap1 experiments establish AP-1-element-dependent transcriptional activation (PMID:2542125). NCU07379 has a fungal bZIP-family placement supporting transcriptional regulation, but cysteine-based peroxide sensing, iron regulation and arsenic resistance are different branch-specific programs, not a universal oxidative-stress annotation.

**Exact benchmark/reference members:** NEUCR/NCU07379 (V5IQW8)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-binding transcription factor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003700) (GO:0003700) | FAMILY_WIDE | The conserved function represented by DNA-binding transcription factor activity is the family core for intact members. DNA-binding transcriptional regulation is the common framework, but oxidative-stress sensing, metal resistance and a particular target regulon need branch-specific evidence. NCU07379 should not inherit every phenotype of yeast Yap1 or other fungal paralogs. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR40621/PTHR40621-review.yaml)

## PTHR42686

**GH17980P-RELATED** — HETEROGENEOUS; COMPLETE

This AKR-related group contains experimentally named sugar and pyridoxal dehydrogenases with divergent substrate preferences. The conserved barrel and nucleotide-binding architecture support oxidoreductase chemistry, while substrate-recognition loops distinguish individual reactions. A broad aldo-keto-reductase superfamily description does not determine the physiological direction or substrate of each member.

The narrow PANTHER inventory contains L-galactose, D-arabinose, D-threo-aldose and pyridoxal dehydrogenases, demonstrating substrate divergence within an oxidative AKR-related group. The broad integrated AKR entry also describes reductases and regulatory proteins outside this narrow inventory. CG18547 has AKR and LGALDH-like signatures; these support an oxidoreductase hypothesis without identifying a plant ascorbate pathway or a physiological sugar substrate in fly.

**Exact benchmark/reference members:** DROME/CG18547 (Q9VGF3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [oxidoreductase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016491) (GO:0016491) | UNRESOLVED | The narrow PANTHER inventory contains L-galactose, D-arabinose, D-threo-aldose and pyridoxal dehydrogenases, demonstrating substrate divergence within an oxidative AKR-related group. The broad integrated AKR entry also describes reductases and regulatory proteins outside this narrow inventory. CG18547 has AKR and LGALDH-like signatures; these support an oxidoreductase hypothesis without identifying a plant ascorbate pathway or a physiological sugar substrate in fly. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR42686/PTHR42686-review.yaml)

## PTHR42884

**PROPROTEIN CONVERTASE SUBTILISIN/KEXIN-RELATED** — HETEROGENEOUS; COMPLETE

Subtilisin/kexin-related serine proteases process protein precursors in diverse organisms. Animal proprotein convertases include enzymes that mature peptide hormones; fungal and bacterial members act in other proteolytic settings. Substrate recognition, maturation and trafficking distinguish their biological roles.

The inventory includes PC1/PC2, furins, fungal Kexin and bacterial Mycosin/NalP proteins. Proteolytic processing is coherent, but neither animal hormone substrates nor dibasic-site specificity is universal across these branches. In Drosophila, cell-specific rescue and mass spectrometry directly connect amon to mature AKH production (PMID:20523747). The separate disputed Slit substrate does not undermine this established hormone-processing function.

**Exact benchmark/reference members:** DROME/amon (Q9VBC7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [serine-type endopeptidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004252) (GO:0004252) | UNRESOLVED | The inventory includes PC1/PC2, furins, fungal Kexin and bacterial Mycosin/NalP proteins. Proteolytic processing is coherent, but neither animal hormone substrates nor dibasic-site specificity is universal across these branches. In Drosophila, cell-specific rescue and mass spectrometry directly connect amon to mature AKH production (PMID:20523747). The separate disputed Slit substrate does not undermine this established hormone-processing function. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR42884/PTHR42884-review.yaml)

## PTHR43398

**DOLICHOL-PHOSPHATE MANNOSYLTRANSFERASE SUBUNIT 1** — HETEROGENEOUS; COMPLETE

DPM1-related glycosyltransferases transfer mannose from nucleotide-sugar donors to lipid-linked acceptors. Eukaryotic dolichol-phosphate mannose synthases differ in membrane-anchoring and subunit organization, while related microbial proteins supply other lipid-linked mannose donors.

Lipid-linked mannose synthesis is supported for characterized members, but lipid acceptor, subunit organization and downstream pathways vary. The exact worm benchmark protein U4PF58 is only the final 51 residues of Q9TYJ7 and lacks the entire annotated glycosyltransferase domain. Sequence identity establishes its same-gene origin, while domain absence refutes assignment of the full catalytic reaction to that isolated peptide.

**Exact benchmark/reference members:** worm/dpm-1 (U4PF58)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [dolichyl-phosphate beta-D-mannosyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004582) (GO:0004582) | UNRESOLVED | The DPM1 dolichol-phosphate mannose reaction is directly established for intact eukaryotic catalytic proteins. It does not apply to the selected U4PF58 C-terminal peptide, which lacks the glycosyltransferase domain; broader family members may also differ in lipid acceptor. A family-wide activity grant is therefore unsupported. This is an exact-product exclusion, not rejection of DPM1 activity for the worm locus. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43398/PTHR43398-review.yaml)

## PTHR43512

**LepA/GUF1 translation-factor GTPases** — HETEROGENEOUS; COMPLETE

LepA/GUF1 proteins act with bacterial or organellar ribosomes in translation. Mitochondrial, chloroplast and bacterial forms share translation-factor architecture but differ in targeting and translation system.

The Artemisia protein has chloroplastic GUF1 placement and is relevant to the characterized chloroplast translation factor. Chloroplast residence is plausible for that branch but is false as a universal location across bacterial and mitochondrial homologs. Transit-peptide evidence and gene-model completeness qualify the plant transfer.

**Exact benchmark/reference members:** ARTAN/A0A2U1PS28 (A0A2U1PS28)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [chloroplast](https://www.ebi.ac.uk/QuickGO/term/GO:0009507) (GO:0009507) | UNRESOLVED | Arabidopsis cpLEPA loss impairs chloroplast protein synthesis and photosynthetic performance, supporting the plastid branch of LepA/GUF1. Bacterial LepA and mitochondrial GUF1 have different translation systems and are not chloroplast-localized. Correct plant orthology and retention of targeting sequences bound the Artemisia transfer; the complete set of plastid-targeted branches is not defined by one exemplar. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43512/PTHR43512-review.yaml)

## PTHR43521

**ALPHA-AMINOADIPIC SEMIALDEHYDE DEHYDROGENASE** — HETEROGENEOUS; COMPLETE

This aldehyde-dehydrogenase family contains ALDH7/aminoadipate-semialdehyde and ALDH4/pyrroline-5-carboxylate dehydrogenase branches. These enzymes share a dehydrogenase framework while acting on different semialdehydes in amino-acid metabolism; individual members also contribute to protection from reactive aldehydes.

Recombinant human ALDH7A1 metabolizes aminoadipic semialdehyde and additional aldehydes (PMID:20207735), supporting the aminoadipate-semialdehyde reaction in its branch. ALDH4/P5C-related members act on a different semialdehyde in proline metabolism. The complete substrate-specific boundary is unresolved across these branches; lysine catabolism, proline catabolism, cofactor preferences and stress responses are not interchangeable universal functions.

**Exact benchmark/reference members:** HORSE/ALDH7A1 (A0A9L0RRL6), human/ALDH7A1 (P49419)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [L-aminoadipate-semialdehyde dehydrogenase [NAD(P)+] activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004043) (GO:0004043) | UNRESOLVED | Recombinant human ALDH7A1 metabolizes aminoadipic semialdehyde and additional aldehydes (PMID:20207735), supporting the aminoadipate-semialdehyde reaction in its branch. ALDH4/P5C-related members act on a different semialdehyde in proline metabolism. The complete substrate-specific boundary is unresolved across these branches; lysine catabolism, proline catabolism, cofactor preferences and stress responses are not interchangeable universal functions. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43521/PTHR43521-review.yaml)

## PTHR43655

**ATP-DEPENDENT PROTEASE** — HETEROGENEOUS; COMPLETE

FtsH-related proteins combine AAA-type ATPase machinery with a protease-related region and occur in membrane-associated protein-handling systems. The chloroplast import machinery illustrates diversification of these components beyond a simple assignment of protein degradation.

FtsH-related proteins separate ATPase-driven protein handling from protease chemistry. FTSH12 has a retained HEXXH zinc motif, but an H769Y mutant supports normal growth and import, demonstrating that zinc-site catalysis is dispensable for its essential role. The selected 991-residue product retains the reference targeting, transmembrane and catalytic-site segments. No endogenous FTSH12 proteolytic substrate is established in the inspected experiments.

**Exact benchmark/reference members:** ARATH/FTSH12 (A0A1P8ARD2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [metalloendopeptidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004222) (GO:0004222) | UNRESOLVED | Protease ancestry and the retained FTSH12 motif make metalloendopeptidase activity plausible, but they do not demonstrate a physiological substrate. H769Y complementation establishes dispensability of the zinc site for import rather than absolute absence of peptidase activity. A broad catalytic grant is therefore unsafe, while a blanket denial would overstate the experiment. |
| [protein import into chloroplast stroma](https://www.ebi.ac.uk/QuickGO/term/GO:0045037) (GO:0045037) | UNRESOLVED | The FTSH12-containing Ycf2-FtsHi complex has direct biochemical and structural support as a chloroplast import motor. This function belongs to a specialized plant complex and cannot be transferred to every FtsH-like protease. The full set of import-capable family branches is not asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43655/PTHR43655-review.yaml)

## PTHR43709

**Aconitate and related organic-acid isomerases** — HETEROGENEOUS; COMPLETE

This family includes aconitate-delta-isomerases and enzymes assigned to methylitaconate and oxalomesaconate interconversion. A shared enzyme fold does not identify the substrate or physiological pathway.

PrpF-family placement supports comparison to the experimentally characterized Shewanella methylaconitate isomerase. The exact methylitaconate GO reaction is chemically distinct and requires substrate-specific evidence. The Bordetella record name and an electronic EC assignment cannot substitute for that evidence.

**Exact benchmark/reference members:** BORPE/Q7VZI5 (Q7VZI5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [methylitaconate delta-isomerase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0050100) (GO:0050100) | UNRESOLVED | Biochemical work on Shewanella PrpF establishes a methylaconitate-isomerization role in the AcnD-dependent methylcitrate pathway, with in vitro aconitate activity in an earlier assay. These reactions must not be equated to methylitaconate delta-isomerization simply because the protein or EC label is similar. Q7VZI5 has PrpF-family architecture but no substrate assay or verified pathway context establishing this exact GO reaction, and the complete substrate-specific family boundary remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43709/PTHR43709-review.yaml)

## PTHR43802

**ENOYL-COA HYDRATASE** — HETEROGENEOUS; COMPLETE

Crotonase-fold proteins catalyze chemically distinct reactions on acyl-CoA and non-CoA substrates. This grouping includes enoyl-CoA-hydratase-related proteins and a characterized 6-oxocamphor hydrolase that cleaves a carbon-carbon bond. Active-site geometry and substrate recognition determine the reaction more precisely than the common fold.

This crotonase-fold grouping spans annotated enoyl-CoA hydratases and experimentally characterized carbon-carbon bond-cleaving enzymes. The actual SF1 inventory contains Rhodococcus Q93TU6, whose 6-oxocamphor hydrolase catalyzes a retro-Claisen ring-opening reaction demonstrated by product structures and mutagenesis (PMID:15138275). SF1 membership therefore does not identify an enoyl-CoA hydration reaction. Fly CG5611 retains a fold-based catalytic hypothesis, but its substrate and reaction cannot be resolved from this heterogeneous subfamily.

**Exact benchmark/reference members:** DROME/CG5611 (Q9VB17)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [enoyl-CoA hydratase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004300) (GO:0004300) | UNRESOLVED | This crotonase-fold grouping spans annotated enoyl-CoA hydratases and experimentally characterized carbon-carbon bond-cleaving enzymes. The actual SF1 inventory contains Rhodococcus Q93TU6, whose 6-oxocamphor hydrolase catalyzes a retro-Claisen ring-opening reaction demonstrated by product structures and mutagenesis (PMID:15138275). SF1 membership therefore does not identify an enoyl-CoA hydration reaction. Fly CG5611 retains a fold-based catalytic hypothesis, but its substrate and reaction cannot be resolved from this heterogeneous subfamily. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43802/PTHR43802-review.yaml)

## PTHR43884

**ACYL-COA DEHYDROGENASE** — HETEROGENEOUS; COMPLETE

Acyl-CoA-dehydrogenase-fold relatives perform diverse reactions, including fatty-acyl dehydrogenation and specialized oxidative or desulfinating chemistry. ACAD9 is additionally recruited to mitochondrial complex-I assembly; ECSIT binding releases its FAD and suppresses dehydrogenase activity in the assembly state. This state-dependent switch differs from constitutive catalytic inactivity.

The inventory extends beyond acyl-CoA dehydrogenases to nitroalkane oxidases, monooxygenases and desulfinases; even SF12 mixes different reactions. Within the ACAD9 branch, direct protein-interaction studies show ECSIT-induced deflavination and loss of dehydrogenase activity during complex-I assembly (PMID:34646991). Catalytic potential and assembly function are alternative biochemical states, not evidence of constitutive pseudoenzyme inactivity. Neither substrate specificity nor complex-I assembly transfers to the entire family.

**Exact benchmark/reference members:** human/ACAD9 (A0A7P0T7Z1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [acyl-CoA dehydrogenase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003995) (GO:0003995) | UNRESOLVED | The inventory extends beyond acyl-CoA dehydrogenases to nitroalkane oxidases, monooxygenases and desulfinases; even SF12 mixes different reactions. Within the ACAD9 branch, direct protein-interaction studies show ECSIT-induced deflavination and loss of dehydrogenase activity during complex-I assembly (PMID:34646991). Catalytic potential and assembly function are alternative biochemical states, not evidence of constitutive pseudoenzyme inactivity. Neither substrate specificity nor complex-I assembly transfers to the entire family. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43884/PTHR43884-review.yaml)

## PTHR44140

**LD25575P** — MOSTLY_COHERENT; COMPLETE

DNAJC3/P58IPK-related proteins combine repeat-mediated protein interactions with a J-domain cochaperone module. Their protein-folding roles are coupled to cellular stress responses and the chaperone systems present in their compartment.

TPR/J-domain cochaperones bind nonnative proteins and communicate with an Hsp70 partner. Direct P58/DNAJC3 experiments show that most molecules enter the ER lumen, its TPR-containing region binds misfolded clients, and BiP plus ATP promotes client release through a functional J-domain (PMID:18923430). ATPase chemistry belongs to BiP rather than the cochaperone. The related Jem1 and animal branches can differ in membrane attachment and clients; the broad cochaperone mechanism is coherent, but universal PKR inhibition, a cytosolic localization or one substrate is not established by the family name.

**Exact benchmark/reference members:** DROME/P58IPK (Q9VHA8)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR44140/PTHR44140-review.yaml)

## PTHR44167

**Diverse checkpoint, replication and signaling kinases** — HETEROGENEOUS; COMPLETE

This broad kinase group includes CHK2/Cds1, CDC7, viral and microbial kinases, and probable inactive kinase-like proteins. Shared kinase architecture does not unify the regulated biological processes.

The Paramecium target's kinase-domain evidence supports a phosphorylation hypothesis, but autophagy, checkpoint signaling and DNA-replication initiation belong to different branches. The retrieved inactive kinase-like members prevent assuming that every detected homolog executes protein phosphorylation.

**Exact benchmark/reference members:** PARTE/A0BFB4 (A0BFB4)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein phosphorylation](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) (GO:0006468) | UNRESOLVED | The Paramecium sequence has protein-kinase, ATP-binding and serine/threonine active-site signatures, supporting an intrinsic phosphorylation hypothesis. The retrieved family also includes divergent and probable inactive kinase-like proteins. Regulatory pathway differences do not negate phosphorylation, but catalytic-domain competence must be checked before a universal family grant; no autophagy or checkpoint substrate is inferred here. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR44167/PTHR44167-review.yaml)

## PTHR44252

**D-ERYTHRULOSE REDUCTASE** — MOSTLY_COHERENT; COMPLETE

DCXR-related short-chain dehydrogenases/reductases reduce small carbonyl substrates, including L-xylulose and alpha-dicarbonyls in characterized mammalian members. The common SDR catalytic framework does not establish the ACP-bound fatty-acid substrate of FabG.

Mammalian recombinant enzymology establishes the DCXR carbonyl/sugar chemistry. Zebrafish Q567K5 aligns without gaps to human DCXR (169/244 identities), retaining the catalytic residues and most NADP contacts, despite a different PANTHER subfamily label. Quantitative sugar/dicarbonyl specificity may vary; the substrate domain of an unrelated FabG branch is not transferred from the generic SDR fold.

**Exact benchmark/reference members:** DANRE/dcxr (Q567K5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004316) (GO:0004316) | UNRESOLVED | No inspected DCXR evidence supports an ACP-dependent beta-ketoacyl reductase role for the zebrafish representative. Its full-length DCXR-like sequence and ortholog enzymology support a different substrate context. This rejects the benchmark transfer without asserting that every unexamined family member is incapable of ACP-substrate chemistry. |
| [L-xylulose reductase (NADPH) activity](https://www.ebi.ac.uk/QuickGO/term/GO:0050038) (GO:0050038) | UNRESOLVED | L-xylulose reduction is directly established for mammalian DCXR and supported for the zebrafish sequence by conserved architecture. This does not delimit every substrate-specific branch in the family or establish identical activities for all proteins carrying a D-erythrulose-related label. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR44252/PTHR44252-review.yaml)

## PTHR44942

**METHYLTRANSF_11 DOMAIN-CONTAINING PROTEIN** — MOSTLY_COHERENT; COMPLETE

Methyltransferase type-11 proteins including fission-yeast SPAC25B8.09 and budding-yeast Tmt1. Tmt1 catalyzes trans-aconitate methylation and also modifies 3-isopropylmalate, its major endogenous substrate in yeast extracts. PomBase transfers trans-aconitate activity to SPAC25B8.09 by curated orthology, while its predominant physiological substrate remains unresolved.

The characterized Tmt1 member supports SAM-dependent small-molecule methylation within this sequence group. Even that enzyme accepts more than one biologically relevant substrate. Conservation of a particular acceptor, detoxification function or starvation-response pathway throughout the complete family is not established.

**Exact benchmark/reference members:** SCHPO/SPAC25B8.09 (Q9UTA9)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [methyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008168) (GO:0008168) | UNRESOLVED | SAM-dependent methyltransferase activity is established in the Tmt1 member and reasonably inferred for SPAC25B8.09. A universal family grant has not been established because the full family has not been functionally delimited. The unresolved scope does not mean that the characterized Tmt1 activity or curated target inference is unsupported. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR44942/PTHR44942-review.yaml)

## PTHR45080

**CONTACTIN 5** — HETEROGENEOUS; COMPLETE

This sequence-classification family includes the PTK7 receptor pseudokinase branch. PTK7 preserves an intracellular kinase fold but has a structurally occluded ATP pocket; it organizes partner-mediated signaling at cell contacts. Related fly Off-track developmental functions cannot be projected wholesale into vertebrate anatomy.

The official CONTACTIN 5 family label is broader than the PTK7 branch and does not imply a shared kinase or adhesion mechanism. PTK7 is experimentally distinguished from active kinases by ATP-site occlusion and from generic cell-adhesion proteins by its noncatalytic intracellular signaling role. Family membership does not establish calcium dependence, a specific ligand, or conservation of fly photoreceptor targeting.

**Exact benchmark/reference members:** rat/Ptk7 (A0A8I6ALM9)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004672) (GO:0004672) | UNRESOLVED | Protein kinase activity is refuted for the PTK7 representative: the orthologous human structure has an occluded ATP site and noncanonical ALG motif, all retained in rat. This rules out a family-wide catalytic grant. It does not establish that every other branch of this broad classification family is catalytically inactive, so a family-wide NOT_APPLICABLE claim is not made. |
| [molecular adaptor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0060090) (GO:0060090) | UNRESOLVED | Mammalian PTK7 organizes Src signaling at cell contacts and provides a supported noncatalytic signaling example. These experiments do not enumerate all adaptor-capable members of this heterogeneous family or justify assigning the same partners to contactins and other branches. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45080/PTHR45080-review.yaml)

## PTHR45496

**ADMETOS-related J-domain proteins** — UNKNOWN; COMPLETE

The family includes plant ADMETOS-related proteins with a J domain. A J domain provides a potential chaperone-interaction module, but full-protein targeting and specialized biological functions require additional evidence.

The Abrus target has a J domain but this does not specify endoplasmic-reticulum residence. Resolve targeting signals and the relationship to experimentally localized ADMETOS-family proteins before assigning an organelle to the whole group.

**Exact benchmark/reference members:** ABRPR/A0A8B8L1Z3 (A0A8B8L1Z3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [endoplasmic reticulum](https://www.ebi.ac.uk/QuickGO/term/GO:0005783) (GO:0005783) | UNRESOLVED | The Abrus target contains a J domain, which supports an Hsp70-cochaperone comparison, but no signal peptide or transmembrane targeting feature establishes ER residence. A J domain is shared by cochaperones in several compartments. Cytosolic-face ER association remains possible through partners, so the absence of an ER-lumen targeting signal is not a universal negative for the broad ER term. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45496/PTHR45496-review.yaml)

## PTHR45618

**MITOCHONDRIAL DICARBOXYLATE CARRIER-RELATED** — HETEROGENEOUS; COMPLETE

Mitochondrial carrier-related proteins use a repeated membrane-transport architecture to exchange diverse metabolites. Substrate specificity and physiological coupling differ among carrier branches.

The mitochondrial-carrier fold accommodates different anions, metabolites and uncoupling mechanisms. Direct reconstitution of fly Dic paralogs found typical dicarboxylate transport by DmDic1, narrower phosphate/sulfur-substrate transport by DmDic3, and no detectable transport by DmDic4 in the tested substrate panel (PMID:21130726). The Dic4 negative result is bounded by that panel and assay system; it neither establishes universal inactivity nor provides positive evidence for thiamine-pyrophosphate transport. Shared carrier architecture cannot select the substrate for the benchmark Dic4 protein.

**Exact benchmark/reference members:** DROME/Dic4 (Q9VVS1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [thiamine pyrophosphate transmembrane transporter activity](https://www.ebi.ac.uk/QuickGO/term/GO:0090422) (GO:0090422) | UNRESOLVED | The mitochondrial-carrier fold accommodates different anions, metabolites and uncoupling mechanisms. Direct reconstitution of fly Dic paralogs found typical dicarboxylate transport by DmDic1, narrower phosphate/sulfur-substrate transport by DmDic3, and no detectable transport by DmDic4 in the tested substrate panel (PMID:21130726). The Dic4 negative result is bounded by that panel and assay system; it neither establishes universal inactivity nor provides positive evidence for thiamine-pyrophosphate transport. Shared carrier architecture cannot select the substrate for the benchmark Dic4 protein. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45618/PTHR45618-review.yaml)

## PTHR45633

**60 KDA HEAT SHOCK PROTEIN, MITOCHONDRIAL** — HETEROGENEOUS; COMPLETE

The family includes ATP-dependent group I chaperonins such as Hsp60/GroEL and the divergent mitochondrial chaperone Tcm62. These proteins assist protein biogenesis, but their folding mechanisms and dependence on ATP are not uniform.

Hsp60/GroEL uses ATP-dependent folding cycles, whereas Tcm62 is a divergent chaperonin-related assembly and antiaggregation factor whose ATP-dependent folding mechanism is not established. Mitochondrial residence, antigenicity and particular imported substrates are lineage-specific contexts; chaperone-assisted import is not membrane-channel activity.

**Exact benchmark/reference members:** HORSE/HSPD1 (F6Z587), human/HSPD1 (P10809)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [ATP-dependent protein folding chaperone](https://www.ebi.ac.uk/QuickGO/term/GO:0140662) (GO:0140662) | UNRESOLVED | Hsp60/GroEL uses ATP-dependent folding cycles, whereas Tcm62 is a divergent chaperonin-related assembly and antiaggregation factor whose ATP-dependent folding mechanism is not established. Mitochondrial residence, antigenicity and particular imported substrates are lineage-specific contexts; chaperone-assisted import is not membrane-channel activity. ATP-dependent folding cannot be granted family-wide without resolving the Tcm62 boundary and defining the supported chaperonin branches. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45633/PTHR45633-review.yaml)

## PTHR45639

**HSC70CB, ISOFORM G-RELATED** — HETEROGENEOUS; COMPLETE

Hsp70-related chaperones share nucleotide-binding and substrate-interaction architecture but differ in compartment and dominant chaperone-system role. Hsp110-related proteins provide an important boundary within this broader structural group.

HSPA4 must be distinguished from conventional Hsp70 substrate-cycling proteins and ribosome-associated chaperones. Nucleotide exchange, substrate binding, ATP hydrolysis and membership in a particular folding complex are separate claims, and none follows solely from an Hsp70-family name.

**Exact benchmark/reference members:** HORSE/HSPA4 (A0A9L0S5Z5), human/HSPA4 (P34932)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [adenyl-nucleotide exchange factor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0000774) (GO:0000774) | UNRESOLVED | HSPA4/Apg2 in SF6 supports nucleotide-exchange activity. HSPH1, LHS1/GRP170 and other Hsp110-related branches also have nucleotide-exchange evidence, so the HSPA4 branch is not the only applicable group. The complete boundary among the diverse family members remains unresolved. HSPA4 must be distinguished from conventional Hsp70 substrate-cycling proteins and ribosome-associated chaperones. Nucleotide exchange, substrate binding, ATP hydrolysis and membership in a particular folding complex are separate claims, and none follows solely from an Hsp70-family name. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45639/PTHR45639-review.yaml)

## PTHR45688

**AGXT2-related PLP enzymes: aminotransferases, phospholyases and related reactions** — HETEROGENEOUS; COMPLETE

Class-III PLP-enzyme relatives catalyze several distinct reactions. AGXT2 is a transaminase, ETNPPL degrades phosphoethanolamine and PHYKPL degrades phosphohydroxylysine; other classified proteins have decarboxylase or racemase functions. Absence of transaminase activity in a relative does not establish a catalytically inactive protein.

The actual inventory contains AGXT2 transaminases, ETNPPL and PHYKPL phospholyases, and decarboxylase/racemase proteins. Purified human AGXT2L1/ETNPPL Q8TBG4 degrades phosphoethanolamine, while AGXT2L2/PHYKPL acts on phosphohydroxylysine (PMID:22241472). Q8TBG4 is the source of the CG8745 caution, so that caution argues against transamination, not against catalysis generally. CG8745 lies in mixed SF13, not the dedicated vertebrate ETNPPL SF1; its precise substrate is unresolved.

**Exact benchmark/reference members:** DROME/CG8745 (Q9VU95)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [transaminase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008483) (GO:0008483) | UNRESOLVED | The actual inventory contains AGXT2 transaminases, ETNPPL and PHYKPL phospholyases, and decarboxylase/racemase proteins. Purified human AGXT2L1/ETNPPL Q8TBG4 degrades phosphoethanolamine, while AGXT2L2/PHYKPL acts on phosphohydroxylysine (PMID:22241472). Q8TBG4 is the source of the CG8745 caution, so that caution argues against transamination, not against catalysis generally. CG8745 lies in mixed SF13, not the dedicated vertebrate ETNPPL SF1; its precise substrate is unresolved. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45688/PTHR45688-review.yaml)

## PTHR45751

**Plant RGLG ubiquitin ligases and copine-related proteins** — HETEROGENEOUS; COMPLETE

The retrieved group includes RGLG RING-type ubiquitin ligases and proteins carrying copine-related names. Ligase activity depends on the RING-containing architecture and its E2 partner; membrane association and substrate choice differ among paralogs.

Rice Q6YYC5 has an annotated RING domain and RGLG4 placement. Experiments establish ligase activity for RGLG3/RGLG4, supporting that bounded inference. K63-chain formation is a narrower E2/E3-dependent reaction and cannot follow merely from general ubiquitin-ligase activity.

**Exact benchmark/reference members:** ORYSJ/Q6YYC5 (Q6YYC5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein K63-linked ubiquitination](https://www.ebi.ac.uk/QuickGO/term/GO:0070534) (GO:0070534) | UNRESOLVED | RGLG3 and RGLG4 have demonstrated ubiquitin ligase activity, but the cited activity assay does not establish K63 linkage specificity. Linkage choice depends on the E2/E3 combination and chain-extension mechanism, not the RING motif alone. K63 transfer to rice or across the family requires an actual linkage assay or an experimentally anchored isofunctional branch. |
| [ubiquitin protein ligase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0061630) (GO:0061630) | UNRESOLVED | Both Arabidopsis RGLG3 and RGLG4 provide direct positive E3 evidence, and the rice RING domain is compatible with that reaction. The family also contains proteins with different domain combinations, so a copine-like name or shared interaction domain is not sufficient. Retention of the functional RING/E2 interface and the complete catalytic branch boundary remain unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45751/PTHR45751-review.yaml)

## PTHR45755

**FAMILY NOT NAMED** — MOSTLY_COHERENT; COMPLETE

This zinc-transporter group includes fungal Cis4/Msc2, animal ZNT5/ZNT7 and related plant proteins. Members connect secretory-pathway metal supply with zinc homeostasis and the maturation of zinc-dependent cellular functions.

Direct pombe experiments establish a Cis4/Zrg17 heteromer that supplies zinc to the cis-Golgi, especially under zinc deficiency. This contrasts with Zhf1-dependent ER zinc handling in the same organism. Zinc transport is conserved across characterized related proteins, but partner dependence, exact organelle and physiological conditions are branch-specific.

**Exact benchmark/reference members:** SCHPO/cis4 (Q9HGQ3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [zinc ion transmembrane transporter activity](https://www.ebi.ac.uk/QuickGO/term/GO:0005385) (GO:0005385) | UNRESOLVED | Cis4/Zrg17-dependent cis-Golgi zinc transport is supported directly, with cytosolic zinc accumulation in deletion mutants under low-zinc conditions. This establishes target zinc transport but not identical membrane location, transport partners or specificity of every unexamined family member. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR45755/PTHR45755-review.yaml)

## PTHR46106

**IA-2 PROTEIN TYROSINE PHOSPHATASE, ISOFORM C** — MOSTLY_COHERENT; COMPLETE

IA-2/PTPRN-related proteins are secretory-vesicle membrane proteins with phosphatase-like intracellular domains. Their conserved roles concern vesicle abundance and secretion, with catalytic claims requiring attention to substrate and assay conditions.

Primary experiments distinguish phosphoprotein substrates from phosphoinositides. Rat phogrin/PTPRN2 has low lipid activity as an isolated catalytic-domain fusion but substantially greater activity in the purified transmembrane form, with catalytic-cysteine and antibody controls. Human breast-cancer experiments connect PTPRN2 to membrane PI(4,5)P2 and actin regulation. These data do not restore conventional protein-tyrosine phosphatase activity or establish the same substrate activity in the horse product with an altered distal domain.

**Exact benchmark/reference members:** HORSE/PTPRN2 (A0A9L0T4W6), human/PTPRN2 (Q92932)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein dephosphorylation](https://www.ebi.ac.uk/QuickGO/term/GO:0006470) (GO:0006470) | UNRESOLVED | A phosphatase-like fold does not establish protein dephosphorylation. The primary phogrin lipid-substrate assays and human membrane-PI(4,5)P2 experiments address a distinct substrate class, so they cannot validate a protein-phosphatase annotation. Conversely, protein-phosphatase impairment cannot be used to deny all enzymatic activity. The altered horse C-terminal domain creates a further exact-product transfer limit. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46106/PTHR46106-review.yaml)

## PTHR46140

**VACUOLAR TRANSPORTER CHAPERONE 1-RELATED** — HETEROGENEOUS; COMPLETE

VTC-related proteins participate in fungal vacuolar polyphosphate systems. The complex combines polyphosphate synthesis, membrane translocation and regulatory inputs through distinct subunit roles.

The inventory contains Vtc1, Vtc2/3, Vtc4 and Vtc5; notably SF1 mixes catalytic Vtc4 with short Vtc1 and regulatory Vtc5 entries. Primary Vtc4 structural enzymology supports polyphosphate synthesis (PMID:19390046), and Neurospora microscopy places VTC-4 in prevacuolar compartments and the tubular vacuolar network (PMID:26453652). Neither SF1 nor VTC complex membership is a sufficient boundary for polyphosphate kinase activity in every subunit.

**Exact benchmark/reference members:** NEUCR/vtc-4 (Q7SCX0)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [polyphosphate kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0008976) (GO:0008976) | UNRESOLVED | The inventory contains Vtc1, Vtc2/3, Vtc4 and Vtc5; notably SF1 mixes catalytic Vtc4 with short Vtc1 and regulatory Vtc5 entries. Primary Vtc4 structural enzymology supports polyphosphate synthesis (PMID:19390046), and Neurospora microscopy places VTC-4 in prevacuolar compartments and the tubular vacuolar network (PMID:26453652). Neither SF1 nor VTC complex membership is a sufficient boundary for polyphosphate kinase activity in every subunit. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46140/PTHR46140-review.yaml)

## PTHR46205

**LOQUACIOUS, ISOFORM B** — HETEROGENEOUS; COMPLETE

Double-stranded-RNA-binding cofactors regulate small-RNA processing and loading by cooperating with RNA-silencing enzymes. Different proteins and isoforms recruit or tune distinct processing pathways.

Loquacious isoforms act as double-stranded-RNA pathway cofactors rather than RNases. Loqs-PB uses different dsRNA-binding motifs for pre-miRNA and Dicer-1 interactions (PMID:17666393), while alternative isoforms partition miRNA and endogenous-siRNA biogenesis (PMID:19644447). Exact-target domain analysis supports retention of the three dsRNA-binding motifs in the benchmark product. The family also includes related cofactors with different partners, so direct dsRNA binding and pathway membership require the appropriate motif/isoform context; an exhaustive positive subfamily set is not inferred from these exemplars.

**Exact benchmark/reference members:** DROME/loqs (X2J5X6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [double-stranded RNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0003725) (GO:0003725) | UNRESOLVED | Loquacious isoforms act as double-stranded-RNA pathway cofactors rather than RNases. Loqs-PB uses different dsRNA-binding motifs for pre-miRNA and Dicer-1 interactions (PMID:17666393), while alternative isoforms partition miRNA and endogenous-siRNA biogenesis (PMID:19644447). Exact-target domain analysis supports retention of the three dsRNA-binding motifs in the benchmark product. The family also includes related cofactors with different partners, so direct dsRNA binding and pathway membership require the appropriate motif/isoform context; an exhaustive positive subfamily set is not inferred from these exemplars. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46205/PTHR46205-review.yaml)

## PTHR46362

**GEM-ASSOCIATED PROTEIN 5** — COHERENT; COMPLETE

Gemin5-related proteins recognize RNA and contribute to ribonucleoprotein assembly. Mammalian Gemin5 delivers snRNAs to the SMN assembly machinery and also has RNA- and translation-associated functions outside a single assembly step.

Gemin5 WD40-domain structures, binding calorimetry and mutagenesis establish recognition of the Sm site of pre-snRNAs (PMID:27881600). The classified family comprises Gemin5 orthologs rather than unrelated WD-repeat proteins, supporting snRNA binding as the shared function of intact RNA-recognition architecture. This broad activity does not require identical affinities for each snRNA or identical cap recognition; SMN assembly partnership and other translation functions are separate claims. Gemin5 is not itself the spliceosome’s RNA-splicing catalyst.

**Exact benchmark/reference members:** HORSE/GEMIN5 (A0A9L0R5P7), human/GEMIN5 (Q8TEQ6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [snRNA binding](https://www.ebi.ac.uk/QuickGO/term/GO:0017069) (GO:0017069) | FAMILY_WIDE | Gemin5 WD40-domain structures, binding calorimetry and mutagenesis establish recognition of the Sm site of pre-snRNAs (PMID:27881600). The classified family comprises Gemin5 orthologs rather than unrelated WD-repeat proteins, supporting snRNA binding as the shared function of intact RNA-recognition architecture. This broad activity does not require identical affinities for each snRNA or identical cap recognition; SMN assembly partnership and other translation functions are separate claims. Gemin5 is not itself the spliceosome’s RNA-splicing catalyst. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46362/PTHR46362-review.yaml)

## PTHR46432

**F-BOX ONLY PROTEIN 42** — MOSTLY_COHERENT; COMPLETE

FBXO42 proteins are F-box substrate-recognition components of SCF ubiquitin-ligase complexes. In fly oocytes, Fbxo42 controls PP2A-B56 abundance and supports synaptonemal-complex maintenance; substrate choice varies among organismal contexts.

Direct fly experiments connect Fbxo42 to the SCF complex, PP2A-B56 regulation and maintenance of the synaptonemal complex (PMID:33382409). This provides evidence for the fly ubiquitin-system mechanism independently of a human p53 narrative. Fbxo42 recognizes substrates rather than catalyzing ubiquitin transfer itself. Broad substrate-adaptor architecture is coherent, while the distribution of specific substrates and an exhaustive protein-ubiquitination grant across all classified sequences remain unresolved; the positive fly evidence is retained without asserting unsupported exclusions of other branches.

**Exact benchmark/reference members:** DROME/Fbxo42 (Q9W281)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein ubiquitination](https://www.ebi.ac.uk/QuickGO/term/GO:0016567) (GO:0016567) | UNRESOLVED | Direct fly experiments connect Fbxo42 to the SCF complex, PP2A-B56 regulation and maintenance of the synaptonemal complex (PMID:33382409). This provides evidence for the fly ubiquitin-system mechanism independently of a human p53 narrative. Fbxo42 recognizes substrates rather than catalyzing ubiquitin transfer itself. Broad substrate-adaptor architecture is coherent, while the distribution of specific substrates and an exhaustive protein-ubiquitination grant across all classified sequences remain unresolved; the positive fly evidence is retained without asserting unsupported exclusions of other branches. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46432/PTHR46432-review.yaml)

## PTHR46622

**DNA-DEPENDENT METALLOPROTEASE WSS1** — MOSTLY_COHERENT; COMPLETE

Wss1-related metalloproteases act in the resolution of DNA-associated protein obstacles, including DNA-protein crosslinks. DNA association and recruitment mechanisms couple proteolysis to genome-maintenance pathways.

Budding-yeast Wss1 experiments directly demonstrate DNA-dependent proteolysis of topoisomerase substrates and protection against DNA-protein crosslinks (PMID:24998930). Pombe Wss1 has the WLM metalloprotease domain and a Wss1-family assignment, supporting a conserved mechanistic inference. It is not a DNA nuclease, and particular SUMO-dependent recruitment mechanisms or lesion preferences are not established merely by membership.

**Exact benchmark/reference members:** SCHPO/wss1 (Q9P7B5)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [metalloendopeptidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004222) (GO:0004222) | UNRESOLVED | Budding-yeast Wss1 experiments directly demonstrate DNA-dependent proteolysis of topoisomerase substrates and protection against DNA-protein crosslinks (PMID:24998930). Pombe Wss1 has the WLM metalloprotease domain and a Wss1-family assignment, supporting a conserved mechanistic inference. It is not a DNA nuclease, and particular SUMO-dependent recruitment mechanisms or lesion preferences are not established merely by membership. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46622/PTHR46622-review.yaml)

## PTHR46721

**FORKHEAD BOX PROTEIN N1** — HETEROGENEOUS; COMPLETE

FOXN-related transcription factors share a forkhead DNA-binding domain but regulate distinct developmental programs. The family includes vertebrate FOXN regulators and related invertebrate proteins such as fly Jumu.

Forkhead/winged-helix factors share sequence-specific DNA recognition but regulate different developmental programs. Fly jumu experiments establish chromatin/nucleolar localization and developmental requirements (PMID:10887088; PMID:20213139). Xenopus Foxn4 instead co-regulates multiciliated-cell genes with Foxj1, with distinct promoter and enhancer occupancy (PMID:27864379). These results support broad DNA-binding transcription-factor activity while preventing transfer of vertebrate thymic or multiciliogenesis programs to every jumu/FOXN-related protein.

**Exact benchmark/reference members:** DROME/jumu (Q9XTP7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [DNA-binding transcription factor activity](https://www.ebi.ac.uk/QuickGO/term/GO:0003700) (GO:0003700) | FAMILY_WIDE | Forkhead/winged-helix factors share sequence-specific DNA recognition but regulate different developmental programs. Fly jumu experiments establish chromatin/nucleolar localization and developmental requirements (PMID:10887088; PMID:20213139). Xenopus Foxn4 instead co-regulates multiciliated-cell genes with Foxj1, with distinct promoter and enhancer occupancy (PMID:27864379). These results support broad DNA-binding transcription-factor activity while preventing transfer of vertebrate thymic or multiciliogenesis programs to every jumu/FOXN-related protein. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46721/PTHR46721-review.yaml)

## PTHR46896

**SENTRIN-SPECIFIC PROTEASE** — MOSTLY_COHERENT; COMPLETE

Ulp2/SENP-related proteases regulate SUMO modification by processing SUMO conjugates and chains. Their catalytic framework is coupled to different cellular substrates and localization mechanisms across lineages.

The inventory spans SENP6/7 and Ulp2-like proteins. Pombe Ulp2 has direct SUMO-deconjugation evidence and predominantly nuclear foci with a smaller cytoplasmic fraction (PMID:24818994). eIF4G sumoylation and co-purification identify a relevant substrate context, whereas eIF3h co-purification did not establish its sumoylation. Vertebrate SUMO2/3 preference and cGAS-STING control are not universal properties of this protease family.

**Exact benchmark/reference members:** SCHPO/ulp2 (O13769)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [deSUMOylase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016929) (GO:0016929) | UNRESOLVED | The inventory spans SENP6/7 and Ulp2-like proteins. Pombe Ulp2 has direct SUMO-deconjugation evidence and predominantly nuclear foci with a smaller cytoplasmic fraction (PMID:24818994). eIF4G sumoylation and co-purification identify a relevant substrate context, whereas eIF3h co-purification did not establish its sumoylation. Vertebrate SUMO2/3 preference and cGAS-STING control are not universal properties of this protease family. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR46896/PTHR46896-review.yaml)

## PTHR47174

**BRIDGING INTEGRATOR 3** — HETEROGENEOUS; COMPLETE

BIN3/Rvs-related BAR-domain proteins couple membrane organization to cytoskeletal and cellular processes. Related fungal proteins differ in their contributions to endocytosis, actin organization and stress responses.

Purified budding-yeast Rvs161/Rvs167 binds and tubulates liposomes (PMID:20610658), supporting direct membrane remodeling. Curated IPR046982 distinguishes these endocytic proteins from pombe Hob1/Hob3, which lack the same endocytic requirement. NCU04637 maps to the Rvs167 branch; its BAR-domain association supports a membrane/cytoskeleton comparison but does not establish neuronal function or every yeast endocytosis phenotype.

**Exact benchmark/reference members:** NEUCR/NCU04637 (Q7S3B9)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [lipid binding](https://www.ebi.ac.uk/QuickGO/term/GO:0008289) (GO:0008289) | UNRESOLVED | Purified budding-yeast Rvs161/Rvs167 binds and tubulates liposomes (PMID:20610658), supporting direct membrane remodeling. Curated IPR046982 distinguishes these endocytic proteins from pombe Hob1/Hob3, which lack the same endocytic requirement. NCU04637 maps to the Rvs167 branch; its BAR-domain association supports a membrane/cytoskeleton comparison but does not establish neuronal function or every yeast endocytosis phenotype. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR47174/PTHR47174-review.yaml)

## PTHR47219

**TBC-domain trafficking regulators** — HETEROGENEOUS; COMPLETE

TBC-domain proteins include Rab GTPase-activating enzymes and noncatalytic trafficking regulators. Rab preference, organelle recruitment and catalytic competence vary among branches.

TBC1D14 regulates autophagosome formation from a recycling-endosome/Golgi context and is not a Rab11 GAP in the cited assays. The cod member is assigned TBC1D12-like, so both paralog identity and actual autophagosome residence remain unresolved. Neither the TBC fold nor an autophagy phenotype establishes the proposed compartment.

**Exact benchmark/reference members:** GADMO/A0A8C5FPT8 (A0A8C5FPT8)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [autophagosome](https://www.ebi.ac.uk/QuickGO/term/GO:0005776) (GO:0005776) | UNRESOLVED | The TBC1D14 paper localizes the regulator to recycling endosomes and reports relocalization toward Golgi on starvation; regulation of autophagosome formation is not itself residence on an autophagosome. The cod target is assigned TBC1D12-like, whereas the prediction lead is TBC1D14. The location therefore requires both correct paralog placement and direct compartment evidence; the TBC fold and autophagy phenotype do not resolve it. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR47219/PTHR47219-review.yaml)

## PTHR47448

**DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE DSOR1-LIKE PROTEIN** — MOSTLY_COHERENT; COMPLETE

MAP kinase kinases phosphorylate downstream MAP kinases as components of conserved signaling cascades. Different branches specify different kinase partners and connect the conserved catalytic step to distinct cellular responses.

Dual-specificity MAP-kinase activation should be separated from an unrestricted protein kinase annotation. Human/horse MAP2K2 and Neurospora mek-1 cannot automatically share ERK partners or physiological outputs; partner specificity and pathway wiring need branch-level evidence.

**Exact benchmark/reference members:** HORSE/MAP2K2 (A0A9L0SHX8), human/MAP2K2 (P36507), NEUCR/mek-1 (Q7RYZ6)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [MAP kinase kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004708) (GO:0004708) | FAMILY_WIDE | The conserved function represented by MAP kinase kinase activity is the family core for intact members. Dual-specificity MAP-kinase activation should be separated from an unrestricted protein kinase annotation. Human/horse MAP2K2 and Neurospora mek-1 cannot automatically share ERK partners or physiological outputs; partner specificity and pathway wiring need branch-level evidence. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR47448/PTHR47448-review.yaml)

## PTHR47593

**Plant ZFP7-related zinc-finger proteins** — UNKNOWN; COMPLETE

These plant proteins contain C2H2-type zinc-finger domains. The retrieved characterized-member set is sparse, so specific transcriptional targets, signaling roles and localization boundaries remain incompletely resolved.

The soybean target has a C2H2 zinc finger, whereas the cited ABA and nuclear-localization experiment concerns ZFP3. ZFP3 evidence is a related-protein lead, not demonstration of all ZFP7-related proteins. Establish the target's relationship to the tested branch before transferring ABA inhibition.

**Exact benchmark/reference members:** SOYBN/C6T1A2 (C6T1A2)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [negative regulation of abscisic acid-activated signaling pathway](https://www.ebi.ac.uk/QuickGO/term/GO:0009788) (GO:0009788) | UNRESOLVED | The Arabidopsis ZFP3 study also tests related ZFP1, ZFP4, ZFP6 and ZFP7 overexpression, and the zfp3 zfp4 double mutant supports a negative ABA-response role. This is positive evidence for several related plant branches, not ZFP3 alone. Soybean transfer still requires paralog placement and preservation of that regulatory context; the complete active set is unresolved. |
| [nucleus](https://www.ebi.ac.uk/QuickGO/term/GO:0005634) (GO:0005634) | UNRESOLVED | ZFP3 is explicitly reported as a nuclear C2H2 zinc-finger protein. The soybean protein has a compatible zinc-finger architecture, but nuclear localization is not established by the metal-binding fold alone or by every family member sharing it. Localization determinants and plant branch conservation bound the inference. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR47593/PTHR47593-review.yaml)

## PTHR47821

**PHOSPHOGLYCERATE MUTASE FAMILY PROTEIN** — UNKNOWN; COMPLETE

The Arabidopsis member AT4G38370 is associated with a phosphoglycerate-mutase-related enzyme fold. Its physiological substrate and the functional uniformity of its PANTHER family are unresolved from the available target evidence.

The selected plant protein retains the RHG catalytic-histidine motif of the histidine-phosphatase fold. Exploratory alignment to experimentally characterized zebrafish TIGAR preserves two catalytic positions but is too divergent to establish a complete pocket or substrate specificity. Primary TIGAR enzymology illustrates substrate discrimination within the structural superfamily; no target-specific reaction is established.

**Exact benchmark/reference members:** ARATH/AT4G38370 (Q0WW53)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [phosphoglycerate mutase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004619) (GO:0004619) | UNRESOLVED | The target phosphoglycerate-mutase-like name denotes a fold relationship and does not demonstrate phosphoglycerate turnover. Its catalytic motif supports plausible enzymatic activity, but neither a target assay nor a resolved substrate-specific evolutionary inference establishes this reaction for the plant branch. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR47821/PTHR47821-review.yaml)

## PTHR48004

**Plant leucine-rich-repeat receptor-like proteins** — MOSTLY_COHERENT; COMPLETE

The retrieved family includes plant receptor-like proteins RLP19 and PII-2. Extracellular leucine-rich repeats provide a recognition surface; receptor-associated signaling can occur without an intrinsic protein kinase domain.

F4JLB7 is an LRR receptor-like sequence, and its OpenScientist domain analysis finds no kinase domain. Kinase activity is therefore contradicted for that sequence; participation in phosphorylation-mediated signaling is a separate unresolved question. Ligand recognition and partner kinases require member-specific evidence.

**Exact benchmark/reference members:** ARATH/F4JLB7 (F4JLB7)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [phosphorylation](https://www.ebi.ac.uk/QuickGO/term/GO:0016310) (GO:0016310) | UNRESOLVED | An extracellular LRR receptor-like protein can regulate a phosphorylation pathway through a partner kinase without itself phosphorylating a substrate. F4JLB7 lacks the kinase domain in the sequence/domain analysis, but no partner-dependent phosphorylation mechanism is established for it. The family evidence therefore does not support a universal phosphorylation-process grant or a universal negative. |
| [kinase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016301) (GO:0016301) | UNRESOLVED | The F4JLB7 analysis finds an LRR solenoid and no complete protein-kinase domain or ordered catalytic motif arrangement; isolated short DFG-like strings are not a kinase active site. This refutes intrinsic kinase activity for that sequence. An exhaustive domain-architecture inventory across the family is absent, so this member-level refutation is not encoded as a family-wide NOT_APPLICABLE claim. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48004/PTHR48004-review.yaml)

## PTHR48022

**PLASTIDIC GLUCOSE TRANSPORTER 4** — HETEROGENEOUS; COMPLETE

This major-facilitator-superfamily group contains membrane proteins associated with sugar and related-solute handling. Transported substrates, affinity and coupling mechanisms differ among branches.

PMID:24581151 directly identifies and tests Neurospora GLT-1/NCU01633 as a glucose transporter alongside different pentose transporters. The family inventory also contains quinate, alpha-glucoside and other sugar permeases. GLT-1 glucose transport is therefore directly supported, whereas family-wide glucose specificity, proton coupling, affinity and plastid localization are not. The low-affinity MstE subfamily label cannot supply a measured GLT-1 kinetic constant.

**Exact benchmark/reference members:** NEUCR/glt-1 (Q1K4S3)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [D-glucose transmembrane transporter activity](https://www.ebi.ac.uk/QuickGO/term/GO:0055056) (GO:0055056) | UNRESOLVED | PMID:24581151 directly identifies and tests Neurospora GLT-1/NCU01633 as a glucose transporter alongside different pentose transporters. The family inventory also contains quinate, alpha-glucoside and other sugar permeases. GLT-1 glucose transport is therefore directly supported, whereas family-wide glucose specificity, proton coupling, affinity and plastid localization are not. The low-affinity MstE subfamily label cannot supply a measured GLT-1 kinetic constant. A complete set of function-bearing branches is not delimited, so no exhaustive family or subfamily grant is asserted. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48022/PTHR48022-review.yaml)

## PTHR48047

**Diverse small-molecule UDP-glycosyltransferases** — HETEROGENEOUS; COMPLETE

These glycosyltransferases act on diverse plant metabolites, with variation in sugar donor, acceptor and modified position. The retrieved family includes enzymes for flavonoids, terpenoids and other specialized metabolites.

The walnut target's glycosyltransferase fold is compatible with glycosyl transfer. Identifying one family member's anthocyanin, hormone or triterpene substrate does not specify the walnut reaction. Evolutionary analysis should compare characterized acceptor-specific clades rather than assign the family name as an EC reaction.

**Exact benchmark/reference members:** JUGRE/A0A2I4G8T1 (A0A2I4G8T1)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [UDP-glucosyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0035251) (GO:0035251) | UNRESOLVED | The walnut protein retains N-terminal glycosyltransferase and UDP-glycosyltransferase signatures. These support nucleotide-sugar transfer as a hypothesis, but donor glucose is narrower than UDP-sugar use, and closely related plant enzymes can differ in both donor and acceptor. Direct substrate testing or an established donor-specific branch is needed before delimiting UDP-glucosyltransferase activity across the family. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48047/PTHR48047-review.yaml)

## PTHR48162

**YALI0A06930P** — UNKNOWN; COMPLETE

This sparse grouping contains the divergent fly uL1-like protein CG13096 and varicella-zoster-virus UL47/ORF11 tegument proteins. The shared L1-like domain suggests an RNA-contact architecture, but does not establish a common ribosomal, viral or transport mechanism across these proteins.

The actual SF1 member inventory places fly CG13096 alongside VZV ORF11 proteins P09263 and Q4JQW4. Direct ORF11 characterization establishes a viral tegument context (PMID:21276599), which cannot be transferred to a fly cellular protein. Conversely an L1-like domain does not demonstrate incorporation of CG13096 into the large ribosomal subunit. The exact benchmark accession H0RNN8 and the separately listed Q9VLK2 are not interchangeable sequence identifiers. A conserved molecular role remains unresolved because the available experiments and domain classification do not bridge these very different protein contexts.

**Exact benchmark/reference members:** DROME/CG13096 (H0RNN8)

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48162/PTHR48162-review.yaml)

## PTHR48169

**DED DOMAIN-CONTAINING PROTEIN** — HETEROGENEOUS; COMPLETE

Death-effector-domain-associated regulatory proteins organize signaling interactions rather than sharing one universal enzymatic reaction. PEA15 regulates kinase localization and signaling outputs through protein interactions.

PEA15 directly docks to ERK2, disrupts features of its active conformation and protects bound ERK2 from dephosphorylation (PMID:23575685). This establishes kinase regulation for the PEA15 branch. Other death-effector-domain proteins recruit different signaling partners; a common DED does not establish ERK regulation, protease activity or identical apoptotic wiring. The complete set with protein kinase regulator activity remains unresolved.

**Exact benchmark/reference members:** HORSE/PEA15 (A0A9L0RWM8), human/PEA15 (Q15121)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [protein kinase regulator activity](https://www.ebi.ac.uk/QuickGO/term/GO:0019887) (GO:0019887) | UNRESOLVED | PEA15 directly docks to ERK2, disrupts features of its active conformation and protects bound ERK2 from dephosphorylation (PMID:23575685). This establishes kinase regulation for the PEA15 branch. Other death-effector-domain proteins recruit different signaling partners; a common DED does not establish ERK regulation, protease activity or identical apoptotic wiring. The complete set with protein kinase regulator activity remains unresolved. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48169/PTHR48169-review.yaml)

## PTHR48261

**ACETYLGLUCOSAMINYLTRANSFERASE** — HETEROGENEOUS; COMPLETE

EXT-related glycosyltransferases contribute to extracellular polysaccharide biosynthesis. The broader family includes animal heparan-sulfate enzymes and plant glycosyltransferases associated with different cell-wall glycans.

Mammalian EXT1/EXT2 structures and catalytic mutants distinguish active sites within a two-protein, four-domain co-polymerase (PMID:36593275). Native fly ttv-PC retains the C-terminal GT-A region and its mapped nucleotide-sugar/metal-binding residues, but lacks the N-terminal membrane anchor and GT-B region. The retained region has catalytic potential; isolated-domain behavior and missing targeting prevent inference of full physiological competence. Plant glycosyltransferases in the broader family act on different glycans. Consequently neither heparan-sulfate synthesis nor unconditional intrinsic glycosyltransferase activity is established for every classified protein.

**Exact benchmark/reference members:** DROME/ttv (D5SHU8)

| Function / process / component | Scope | Boundary |
|---|---|---|
| [glycosyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0016757) (GO:0016757) | UNRESOLVED | Mammalian EXT1/EXT2 structures and catalytic mutants distinguish active sites within a two-protein, four-domain co-polymerase (PMID:36593275). Native fly ttv-PC retains the C-terminal GT-A region and its mapped nucleotide-sugar/metal-binding residues, but lacks the N-terminal membrane anchor and GT-B region. The retained region has catalytic potential; isolated-domain behavior and missing targeting prevent inference of full physiological competence. Plant glycosyltransferases in the broader family act on different glycans. Consequently neither heparan-sulfate synthesis nor unconditional intrinsic glycosyltransferase activity is established for every classified protein. |

[Structured review and supporting sources](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48261/PTHR48261-review.yaml)

