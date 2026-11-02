---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:24:58.440184'
end_time: '2026-10-26T01:35:46.739115'
duration_seconds: 648.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: BCAT2
  gene_symbol: BCAT2
  uniprot_accession: A0A9L0TSN4
  protein_description: 'RecName: Full=Branched-chain-amino-acid aminotransferase {ECO:0000256|RuleBase:RU004517};
    EC=2.6.1.42 {ECO:0000256|RuleBase:RU004517};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the class-IV pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_IV. (IPR001544); Aminotrans_IV_CS. (IPR018300); Aminotransferase-like.
    (IPR036038); B_amino_transII. (IPR005786); BCAT-like_C. (IPR043132)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3302
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 83
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0TSN4
- **Protein Description:** RecName: Full=Branched-chain-amino-acid aminotransferase {ECO:0000256|RuleBase:RU004517}; EC=2.6.1.42 {ECO:0000256|RuleBase:RU004517};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the class-IV pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_IV. (IPR001544); Aminotrans_IV_CS. (IPR018300); Aminotransferase-like. (IPR036038); B_amino_transII. (IPR005786); BCAT-like_C. (IPR043132)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "BCAT2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'BCAT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **BCAT2** (gene ID: BCAT2, UniProt: A0A9L0TSN4) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Horse BCAT2 (UniProt A0A9L0TSN4): mitochondrial branched-chain amino acid aminotransferase

## 1. Introduction and summary

UniProt A0A9L0TSN4 is an unreviewed (TrEMBL, protein existence level 3, "inferred from homology") entry for a branched-chain-amino-acid aminotransferase (EC 2.6.1.42) from the domestic horse, *Equus caballus*. The entry is derived from the Ensembl annotation of the Thoroughbred reference genome [wade-2009-horse-genome-abstract]. UniProt itself gives no gene name. However, the Ensembl gene from which the protein is predicted (ENSECAG00000011310, equine chromosome 10) carries the VGNC-approved symbol *BCAT2* ("branched chain amino acid transaminase 2", VGNC:15785). The protein carries the class-IV PLP-dependent aminotransferase signatures (Pfam PF01063, InterPro IPR001544/IPR018300/IPR005786, PANTHER PTHR11825:SF39 "branched-chain-amino-acid aminotransferase, mitochondrial"). These facts were checked directly against the UniProt and Ensembl records (see `SEQUENCE_ANALYSIS.md`). The gene symbol supplied in the task is therefore correct and unambiguous. This protein is the horse ortholog of mammalian mitochondrial BCAT (BCATm), the product of the gene that Bledsoe and colleagues named *BCAT2* to distinguish it from the cytosolic, largely brain-restricted *BCAT1* [bledsoe-1997-bcatm-cloning-abstract].

No experimental study of the horse BCAT2 protein itself was found. Its function must therefore be inferred from orthology, and here the inference is strong. Once a 59-residue N-terminal extension (discussed below) is set aside, the horse sequence is 83% identical over its full length to human BCAT2 (O15382). Every residue identified by crystallography and mutagenesis as important for catalysis, substrate binding and redox regulation is conserved (`SEQUENCE_ANALYSIS.md`). On that basis, horse BCAT2 should be a pyridoxal 5′-phosphate (PLP)-dependent homodimeric enzyme of the mitochondrial matrix. It catalyses the reversible transfer of the α-amino group of L-leucine, L-isoleucine and L-valine to 2-oxoglutarate, giving the corresponding branched-chain α-keto acids (BCKAs: 4-methyl-2-oxopentanoate, (S)-3-methyl-2-oxopentanoate and 3-methyl-2-oxobutanoate) and L-glutamate [hall-1993-rat-bcat-abstract; davoodi-1998-human-bcat-kinetics-abstract; yennawar-2001-bcatm-structure-abstract]. This is the first, shared step of BCAA catabolism. Its keto-acid products are passed, partly by direct channelling within a multienzyme "metabolon", to the branched-chain α-keto acid dehydrogenase complex (BCKDC) for irreversible oxidative decarboxylation [islam-2007-bcaa-metabolon-abstract; islam-2010-gdh-metabolon-abstract]. A conserved CXXC motif near the active site works as a peroxide-sensitive redox switch that can turn the enzyme off [conway-2002-cxxc-redox-switch-abstract; conway-2004-cxxc-cysteines-abstract]. Loss of the enzyme in mice and humans raises plasma BCAAs and, in mice, changes energy balance [she-2007-bcatm-knockout-abstract; wu-2004-enu-bcatm-mice-abstract; wang-2015-bcat2-deficiency-abstract]. In horses specifically, a branched-chain aminotransferase is thought to catalyse the first activation step of the sycamore-maple protoxins that cause equine atypical myopathy [sander-2023-atypical-myopathy-abstract]. This gives the enzyme a direct veterinary relevance.

## 2. Gene and protein identity, and the predicted horse sequence

The human and rat BCATm cDNAs encode precursors with 27-residue mitochondrial presequences and mature proteins of about 41 kDa. Expressed in COS-1 cells, rat BCATm is catalytically active and correctly processed. The human gene lies on chromosome 19 and the cytosolic isoenzyme gene on chromosome 12, which led to the BCAT1/BCAT2 nomenclature [bledsoe-1997-bcatm-cloning-abstract]. The same orthology group has been characterised biochemically in another domesticated ungulate, the sheep. Ovine BCATm is a 41-kDa homodimer that shares 82–85% identity with other mammalian BCATm sequences but only about 60% with the cytosolic isoenzymes [faure-1999-sheep-placenta-bcatm-abstract]. The 83% identity of the horse protein to human BCAT2 is entirely in line with these mammalian orthologs.

One feature of the horse entry needs attention. A0A9L0TSN4 is 452 residues long, whereas human BCAT2 is 392. The extra length is a Gly/Pro/Arg-rich N-terminal segment (residues 1–59) that UniProt flags as disordered. Horse Met60 aligns with human Met1, and the following sequence (MATASVGQICARKLLPVTWLLCGPRRYASS…) closely matches the human transit peptide (MAAAALGQIWARKLLSVPWLLCGPRRYASS…) (`SEQUENCE_ANALYSIS.md`). Ensembl models six protein-coding transcripts for horse *BCAT2* (300, 405, 427, 427, 452 and 480 residues), and none is 392 residues. This suggests that the 5′ ends of these models are uncertain. Whether translation in horse cells starts at the upstream methionine or at Met60 is unknown. Most likely, the native mitochondrial precursor resembles the human one, with an N-terminal presequence of about 27 residues starting at Met60. In that case the mature horse enzyme would be about 366 residues, the same length as the mature sheep enzyme [faure-1999-sheep-placenta-bcatm-abstract]. This remains an inference rather than an observation.

Isoform diversity at this locus is not unique to the horse. Human BCAT2 was independently identified as "placental tissue protein 18". Its full-length form, PP18a, is the 392-residue precursor with a 27-residue mitochondrial targeting sequence. It matures to a 365-residue, 41.3-kDa protein that is expressed ubiquitously and found in the mitochondrial fraction. A second form, PP18b, is an alternatively spliced variant of 300 residues (33.8 kDa). It was found only in the cytosolic fraction of term placenta and at lower levels in nearly all tissues [than-2001-pp18-bcatm-abstract]. One of the horse *BCAT2* gene products in UniProt (A0A5F5PUM8, 300 residues) aligns without gaps along its whole length to human isoform B (O15382-2) and shares 84% identity with it. It uses the same exon junction, which removes residues 9–100 of the precursor (`SEQUENCE_ANALYSIS.md`). The PP18b-type isoform therefore appears conserved between primates and perissodactyls. It lacks most of the presequence and part of the small domain, including the Tyr70 that helps form the substrate pocket of the partner subunit [yennawar-2001-bcatm-structure-abstract]. Whether the short isoform is catalytically active, and what it does in the cytosol, has not been established in either species. The target entry A0A9L0TSN4 corresponds to the full-length, mitochondrial, PP18a-type isoform.

## 3. Catalytic reaction, mechanism and substrate specificity

Mammalian BCATs are fold-type IV PLP enzymes. They work by a ping-pong (double-displacement) mechanism. In the first half-reaction a branched-chain L-amino acid gives its amino group to enzyme-bound PLP, which releases the BCKA and forms pyridoxamine 5′-phosphate (PMP). In the second half-reaction the amino group passes from PMP to 2-oxoglutarate, regenerating PLP and releasing glutamate [hall-1993-rat-bcat-abstract; yennawar-2002-bcatm-intermediates-abstract]. With purified rat BCAT, the apparent Km values were about 1 mM for leucine and isoleucine and about 5 mM for valine, and 0.6–3 mM for 2-oxoglutarate depending on the amino-acid co-substrate. Besides the three BCAAs, the enzyme also transaminated their straight-chain analogues, L-alloisoleucine and glutamate. It accepted a broader range of α-keto acids, including 2-oxobutanoate and the keto acid of methionine [hall-1993-rat-bcat-abstract]. Recombinant human BCATm is a dimer with substrate specificity comparable to the rat enzyme and turns over 2–5 times more slowly than human BCATc. Both isoenzymes need a reducing environment for full activity [davoodi-1998-human-bcat-kinetics-abstract]. Because the Km values for BCKAs are about 100 µM, compared with millimolar values for BCAAs, and intracellular glutamate is high, the reaction runs close to equilibrium in vivo. It can operate in either direction, so the enzyme acts both as a catabolic entry point and as a means of re-aminating BCKAs [neinast-2019-bcaa-review-fulltext].

The structural basis of these properties comes from crystal structures of human BCATm. The enzyme is a homodimer, and each subunit has a small N-terminal domain and a large C-terminal domain. The active site lies near the dimer interface, and the PLP 4′-aldehyde is bound by a Schiff base to Lys202 (mature numbering). A hydrogen bond between Arg143 of one subunit and Tyr70 of the other helps build the substrate pocket, so dimerisation is needed for catalysis [yennawar-2001-bcatm-structure-abstract]. Structures of the isoleucine-ketimine and PMP intermediates showed that Lys202 moves substantially and that the pyridine ring tilts by about 18° during catalysis. Three hydrophobic surfaces lock the branched side chain in place and account for the specificity for L-BCAAs. Short aliphatic side chains make too few van der Waals contacts, and aromatic side chains clash sterically. For the dicarboxylate substrate, glutamate can form the required hydrogen bonds but aspartate cannot [yennawar-2002-bcatm-intermediates-abstract; conway-2003-substrate-specificity-abstract]. A β-turn (residues 311–314) positions Thr313 to contact the PLP phosphate oxygens and the substrate α-carboxylate [yennawar-2002-bcatm-intermediates-abstract].

All these determinants are conserved in the horse protein. The PLP lysine (human K202 mature/K229 precursor) corresponds to horse K289. Arg143 and Tyr70 correspond to R230 and Y157, Thr313 to T400, and the six isoleucine-contacting residues annotated in human BCAT2 (R126, Y168, Y234, V296, V297 and T340, precursor numbering) all map to identical residues in horse (`SEQUENCE_ANALYSIS.md`). Horse BCAT2 is therefore expected to have the same L-branched-chain substrate specificity, with 2-oxoglutarate/glutamate as the amino acceptor/donor pair. This matches the three Rhea reactions (RHEA:18321, RHEA:24801 and RHEA:24813) that UniProt assigns to the entry through its rule-based annotation.

## 4. Redox regulation through the CXXC centre

A distinctive feature of mammalian BCATs is a CXXC motif in the large domain, about 10 Å from the active site. Conway and colleagues showed that human BCATm has two reactive thiols, Cys315 and Cys318. In the reduced enzyme these are joined by a thiol–thiolate hydrogen bond. Hydrogen peroxide converts them into an intrasubunit disulfide that abolishes activity, and dithiothreitol fully restores it. Cys315 also anchors Tyr173, which controls access to the active site [conway-2002-cxxc-redox-switch-abstract]. Site-directed mutagenesis assigned distinct roles to the two cysteines. Mutating Cys315 cut kcat to 26–33% of wild type and made the enzyme insensitive to H2O2, so C315 is the redox sensor. Mutating Cys318 had little kinetic effect but made oxidation largely irreversible: Cys315 became over-oxidised to sulfonic acid via a sulfenic-acid intermediate. Cys318 is thus the "resolving" cysteine that allows reversible disulfide formation [conway-2004-cxxc-cysteines-abstract; hutson-2008-sulfenic-acid-abstract].

Structures of the oxidised enzyme and of CXXC mutants showed that the CXXC hydrogen-bond network orients the substrate correctly. Oxidation disorders the N-terminal loop (residues 15–32), disrupts the side-chain-binding pocket and mainly blocks the second half-reaction. The fully oxidised enzyme is completely inactive [yennawar-2006-cxxc-catalysis-abstract]. A more recent structure of the oxidised C318A variant supports a model in which the Cys315 side chain switches between active and inactive conformations [herbert-2020-oxidized-mutant-abstract]. Redox titrations showed that BCATm has a more oxidising redox potential than BCATc, about 30 mV higher overall and about 80 mV higher at the CXXC motif. Both isoenzymes can be S-glutathionylated in a manner that tracks the GSH:GSSG ratio [coles-2012-redox-potential-abstract]. Conway and colleagues noted that the residues around the CXXC motif are conserved in prokaryotic and eukaryotic BCATs, but the CXXC motif itself occurs only in the mammalian proteins [conway-2003-substrate-specificity-abstract]. The horse sequence keeps both cysteines (C402 and C405 in A0A9L0TSN4, matching human C315/C318 mature) and the preceding β-turn including T400. Equine BCAT2 is therefore expected to share this redox sensitivity, although no horse study has tested it.

## 5. Subcellular location and the branched-chain amino acid metabolon

UniProt places A0A9L0TSN4 in the mitochondrion by automatic annotation. The experimental basis comes from the orthologs. BCATm was defined biochemically as the mitochondrial isoenzyme, and its N-terminal presequence is correctly processed when expressed in mammalian cells [bledsoe-1997-bcatm-cloning-abstract; hall-1993-rat-bcat-abstract]. Within the matrix, BCATm does not act alone. Human BCATm binds the E1 (branched-chain α-keto acid decarboxylase) component of BCKDC with a KD of about 2.8 µM but does not bind the E2 or E3 components. NADH dissociates the complex. In the presence of BCATm, the kcat for E1-catalysed decarboxylation of BCKAs rises 12-fold. Complex formation needs both the BCATm CXXC centre and the phosphorylation loop of E1. This is evidence for substrate channelling within a "branched-chain amino acid metabolon" that the mitochondrial redox state can influence [islam-2007-bcaa-metabolon-abstract]. A later study found that the complex also contains glutamate dehydrogenase 1 (GDH1), NIPSNAP1, pyruvate carboxylase and BCKDC kinase. GDH1 binds selectively to the PMP form of BCATm and regenerates the PLP form. That is the form that binds E1, so GDH1 couples BCAA transamination to nitrogen release from glutamate and to continued BCAA oxidation [islam-2010-gdh-metabolon-abstract]. Because BCAT2 binding and BCKDK-mediated phosphorylation compete for the same loop on BCKDHA, BCAT2 association favours BCKDH activity, whereas phosphorylation destabilises the complex [neinast-2019-bcaa-review-fulltext]. The redox-sensitive CXXC centre therefore links mitochondrial redox status not only to transamination but to metabolon assembly as a whole [herbert-2020-oxidized-mutant-fulltext].

An older observation is that purified rat heart BCATm, reconstituted into phospholipid vesicles, transports branched-chain α-keto acids (Km about 10 µM for α-ketoisocaproate) but not pyruvate. Across tissues, BCKA transport activity tracks BCATm [hutson-1993-bcka-transport-abstract]. This underlies the UniProt statement that the enzyme "may also function as a transporter of branched chain alpha-keto acids". The proposal has not been widely confirmed, and BCAT2 is not a membrane protein. This function should be treated as tentative.

## 6. Tissue distribution, physiology and genetic evidence

In rats, monkeys and humans, mitochondrial BCAT is expressed in most tissues, while BCATc mRNA is barely detectable outside the brain. Skeletal muscle and liver together account for more than 70% of whole-body BCAA oxidative capacity. The high ratio of transamination to oxidation in the primate gastrointestinal tract suggests that the gut supplies BCKAs to the circulation while conserving BCAA carbon [suryawan-1998-bcaa-model-abstract]. Hepatocytes have relatively little transaminase activity. Consequently, most dietary BCAAs bypass first-pass hepatic metabolism, are transaminated in extrahepatic tissues (above all muscle) by BCAT2, and the resulting BCKAs can be oxidised locally or exported to the liver [neinast-2019-bcaa-review-fulltext; neinast-2019-bcaa-fate-abstract]. Isotope tracing in mice shows that muscle, brown fat, liver, kidney and heart oxidise the most BCAA, and that insulin resistance shifts oxidation towards muscle [neinast-2019-bcaa-fate-abstract]. Because BCAT2 transamination runs much faster than BCKA oxidation, BCAA amino groups feed into the general transamination pool. Leucine alone supplies about 20% of the nitrogen in alanine released from muscle, which links BCAT2 to the inter-organ nitrogen and gluconeogenic-carbon transport between muscle and liver [neinast-2019-bcaa-review-fulltext]. Species differ in this organisation. In sheep, BCATm is the only BCAT isoenzyme in placenta and supplies 57–71% of skeletal-muscle BCAT activity, yet muscle BCAT activity is much lower than in rats. This led Faure and colleagues to conclude that "the metabolic scheme for branched-chain amino acid catabolism is specific to each species" [faure-1999-sheep-placenta-bcatm-abstract]. No equivalent measurements exist for horse tissues. This is a significant gap, given the size of the horse's skeletal muscle mass and its specialisation for athletic performance.

In the brain, BCATm is found mainly in astrocytes, whereas BCKDC is found in neurons [cole-2012-brain-bcatm-abstract]. In cultured rat brain cells, BCATm predominates in astrocytes and BCATc in neurons. BCKAs drive glutamate transamination and oxidation in astrocytes, which supports a BCAA/BCKA shuttle that supplies nitrogen for glutamate and glutamine synthesis. The anticonvulsant gabapentin inhibits BCATc but not BCATm [hutson-1998-bcat-neurotransmitter-abstract].

Genetic studies in mice and humans confirm that BCAT2 is the main enzyme of peripheral BCAA transamination. Mice with a *Bcat2* splice-site mutation lacking BCAT2 protein have high blood BCAAs and an MSUD-like illness that BCAA restriction corrects [wu-2004-enu-bcatm-mice-abstract]. BCATm-null mice have raised plasma BCAAs, lower adiposity and body weight despite eating more, higher energy expenditure, better glucose and insulin tolerance and resistance to diet-induced obesity. These changes were linked to a futile cycle of protein degradation and synthesis [she-2007-bcatm-knockout-abstract]. In humans, biallelic loss-of-function *BCAT2* variants cause hypervalinemia and hyperleucine-isoleucinemia. Plasma valine is predominantly raised, while allo-isoleucine and urinary BCKAs stay normal, which distinguishes the condition from MSUD. Many patients show white-matter changes on MRI, and plasma BCAAs fall with pyridoxine (vitamin B6) supplementation. This is consistent with partial rescue of a PLP-dependent enzyme [wang-2015-bcat2-deficiency-abstract; mondesert-2025-bcat2-deficiency-abstract; filipic-2026-bcat2-deficiency-review-abstract]. The clinical picture is variable, and some people with the same homozygous genotype are asymptomatic. The pathogenicity of BCAT2 deficiency is therefore still debated [filipic-2026-bcat2-deficiency-review-abstract]. The residues affected by the first reported patient variants (p.Arg170Gln and p.Glu264Lys) and by the recurrent p.Tyr200Ter variant are all conserved in horse (R230, E324 and Y260), so the horse can be used to interpret equine variants by analogy.

## 7. Signalling-linked and tissue-specific roles beyond catabolism

Several studies show that BCAT2 activity affects cell programmes through the metabolites it makes, not only through BCAA disposal. In white adipose tissue, adipocyte-specific deletion of *Bcat2* in mice increases browning and thermogenesis of inguinal fat and protects against diet-induced obesity. The mechanism is that acetyl-CoA derived from BCKAs is used to acetylate PRDM16 at K915, which disrupts its interaction with PPARγ and maintains the white-fat programme. BCKA supplementation restores obesity in the knockout mice. The antihypertensive drug telmisartan was reported to bind and inhibit Bcat2 [ma-2022-prdm16-browning-abstract]. This study is the source of the adipocyte-related functional statement in the UniProt record for A0A9L0TSN4. In muscle-cell culture, BCAT2 and BCKD expression rise during myoblast differentiation, and BCAT2 knockdown abolishes myotube formation. Adding BCKAs does not rescue the defect, but co-depleting BCKD kinase partly does. This suggests that BCAT2 is needed for myogenesis for reasons beyond simply supplying keto acids [dhanani-2019-bcat2-myoblast-abstract]. These are murine and cell-line results, and their transfer to the horse remains to be shown.

## 8. Equine context: atypical myopathy and nutrition

The main horse-specific link to BCAT2 biology is equine atypical myopathy, a frequently fatal rhabdomyolysis caused by eating seeds or seedlings of sycamore maple (*Acer pseudoplatanus*). The protoxins hypoglycin A (HGA) and methylenecyclopropylglycine (MCPrG) are non-proteinogenic amino acids. They are metabolised by the same first two steps as the BCAAs: deamination by a branched-chain aminotransferase, then conversion to acyl-CoA derivatives (MCPA-CoA and MCPF-CoA). These inhibit short-chain, medium-chain and branched-chain acyl-CoA dehydrogenases. In tissues from affected horses, protoxin activation, measured as MCPA- and MCPF-carnitine, took place mainly in skeletal muscle. The authors proposed inhibiting the mitochondrial BCAT as a therapy [sander-2023-atypical-myopathy-abstract; sander-2023-atypical-myopathy-fulltext]. That transamination is the activating step is supported by older work in rat hepatocytes. There, the transamination product of hypoglycin, methylenecyclopropylpyruvate ("ketohypoglycin"), inhibited gluconeogenesis more strongly than hypoglycin itself, consistent with inhibition of butyryl-CoA dehydrogenase and CoA trapping [kean-1979-ketohypoglycin-abstract]. Work on a zebrafish embryo model of the poisoning likewise attributes protoxin activation to the BCAT–BCKDC pair. It also notes that equine primary myoblasts in vitro fail to reproduce HGA toxicity, which currently limits direct tests in horse cells [wouters-2024-zebrafish-sapindaceae-fulltext; wouters-2024-zebrafish-sapindaceae-abstract]. The muscle localisation fits the dominance of BCATm in peripheral, especially muscle, transamination [suryawan-1998-bcaa-model-abstract]. However, the gabapentin they mention as an existing veterinary inhibitor inhibits the cytosolic isoenzyme BCATc but not BCATm in rat brain cells [hutson-1998-bcat-neurotransmitter-abstract; sander-2023-atypical-myopathy-fulltext]. Whether horse BCAT2 actually transaminates HGA and MCPrG, and whether a BCAT2-selective inhibitor would protect horses, has not been tested. Beyond this disease, equine exercise studies show that circulating BCAAs respond to work in horses. In sport horses, serum leucine and valine changed in ways that depended on whether the exercise was jumping, reining or an endurance ride of 32 or 72 km [arfuso-2019-horse-bcaa-exercise-abstract]. In eventing horses, most plasma amino acids, together with ammonia and urea, rose within 30 minutes of cross-country exercise and returned to baseline by the next day [reemtsma-2025-eventing-amino-acids-abstract]. Such changes are consistent with active muscle BCAA transamination and inter-organ nitrogen transfer of the kind BCAT2 mediates in other mammals [neinast-2019-bcaa-review-fulltext]. However, none of these studies measured BCAT2 expression or activity, and transcriptomic studies of starvation in horses do not report BCAT2-specific findings [austin-2025-emaciated-horses-abstract].

## Open Questions

The most basic open question concerns the horse gene model. Is the native translation start of horse BCAT2 at Met60 of A0A9L0TSN4, giving a canonical mitochondrial presequence and a mature protein of about 366 residues like sheep BCATm, or is the Gly/Pro-rich upstream segment real? If it were real, it would bury the presequence internally and could alter import. Long-read RNA sequencing, ribosome profiling or N-terminal proteomics of horse muscle and liver would settle this, and the result should be fed back to Ensembl and UniProt. A related question is whether the conserved 300-residue, PP18b-type splice isoform predicted for horse (A0A5F5PUM8) is actually expressed, where it is located and whether it has any activity. It lacks part of the dimer-interface substrate pocket, so it might act as a dominant-negative or non-catalytic partner rather than an enzyme. A second gap is the lack of any enzymology on the equine protein. Recombinant horse BCAT2 could be expressed and its kinetic constants for leucine, isoleucine, valine and 2-oxoglutarate measured, along with its sensitivity to H2O2 and its redox potential. That would replace inference from human and rat data with direct evidence. Tissue profiles of BCAT activity and protein in horse skeletal muscle (by fibre type), liver, gut, adipose tissue and brain would also be valuable, given the clear species differences seen in sheep. Such profiles would show whether the "muscle transaminates, liver oxidises" model holds in a hindgut-fermenting herbivore athlete. For veterinary medicine, the key question is whether horse BCAT2 transaminates hypoglycin A and MCPrG. Related questions are what its kinetics are compared with BCAT1, and whether a BCATm-selective inhibitor (rather than the BCATc-selective gabapentin) could limit toxin activation in atypical myopathy. Finally, it remains open whether the metabolon interactions (with BCKDHA, GDH1 and BCKDK), the PRDM16 acetylation axis in adipose tissue and the requirement for BCAT2 in myogenesis seen in rodents also operate in horse tissues. Equine BCAT2 coding or regulatory variants could be screened against plasma BCAA profiles or performance and metabolic phenotypes such as equine metabolic syndrome.

## References

- [arfuso-2019-horse-bcaa-exercise] Arfuso F, Assenza A, Fazio F, Rizzo M et al. Dynamic Change of Serum Levels of Some Branched-Chain Amino Acids and Tryptophan in Athletic Horses After Different Physical Exercises. *J Equine Vet Sci* 2019; 77:12-16. PMID 31133304; DOI 10.1016/j.jevs.2019.02.006.
- [austin-2025-emaciated-horses] Austin MMP, Ivey JLZ, Shepherd EA, Myer et al. Methodologies to Identify Metabolic Pathway Differences Between Emaciated and Moderately Conditioned Horses: A Review of Multiple Gene Expression Techniques. *Animals* 2025. PMID 41153862; PMCID PMC12560892; DOI 10.3390/ani15202933.
- [bledsoe-1997-bcatm-cloning] Bledsoe RK, Dawson PA, Hutson SM. Cloning of the rat and human mitochondrial branched chain aminotransferases (BCATm). *Biochim Biophys Acta* 1997. PMID 9165094; DOI 10.1016/s0167-4838(97)00044-7.
- [cole-2012-brain-bcatm] Cole JT, Sweatt AJ, Hutson SM. Expression of mitochondrial branched-chain aminotransferase and α-keto-acid dehydrogenase in rat brain: implications for neurotransmitter metabolism. *Front Neuroanat* 2012. PMID 22654736; PMCID PMC3361127; DOI 10.3389/fnana.2012.00018.
- [coles-2012-redox-potential] Coles SJ, Hancock JT, Conway ME. Differential redox potential between the human cytosolic and mitochondrial branched-chain aminotransferase. *Acta Biochim Biophys Sin* 2012. PMID 22107788; DOI 10.1093/abbs/gmr103.
- [conway-2002-cxxc-redox-switch] Conway ME, Yennawar N, Wallin R, Poole LB, Hutson SM. Identification of a peroxide-sensitive redox switch at the CXXC motif in the human mitochondrial branched chain aminotransferase. *Biochemistry* 2002. PMID 12119021; DOI 10.1021/bi020200i.
- [conway-2003-substrate-specificity] Conway ME, Yennawar N, Wallin R, Poole LB, Hutson SM. Human mitochondrial branched chain aminotransferase: structural basis for substrate specificity and role of redox active cysteines. *Biochim Biophys Acta* 2003. PMID 12686109; DOI 10.1016/s1570-9639(03)00051-7.
- [conway-2004-cxxc-cysteines] Conway ME, Poole LB, Hutson SM. Roles for cysteine residues in the regulatory CXXC motif of human mitochondrial branched chain aminotransferase enzyme. *Biochemistry* 2004. PMID 15182179; DOI 10.1021/bi0498050.
- [davoodi-1998-human-bcat-kinetics] Davoodi J, Drown PM, Bledsoe RK, Wallin R et al. Overexpression and characterization of the human mitochondrial and cytosolic branched-chain aminotransferases. *J Biol Chem* 1998. PMID 9478945; DOI 10.1074/jbc.273.9.4982.
- [dhanani-2019-bcat2-myoblast] Dhanani ZN, Mann G, Adegoke OAJ. Depletion of branched-chain aminotransferase 2 (BCAT2) enzyme impairs myoblast survival and myotube formation. *Physiol Rep* 2019. PMID 31833233; PMCID PMC6908738; DOI 10.14814/phy2.14299.
- [faure-1999-sheep-placenta-bcatm] Faure M, Glomot F, Bledsoe R, Hutson S et al. Purification and cloning of the mitochondrial branched-chain amino acid aminotransferase from sheep placenta. *Eur J Biochem* 1999. PMID 9914481; DOI 10.1046/j.1432-1327.1999.00009.x.
- [filipic-2026-bcat2-deficiency-review] Filipic M, Remec ZI, Torkar AD, Sustar N et al. Branched-chain amino acid transferase 2 (BCAT2) deficiency: A case series and systematic review. *Mol Genet Metab Rep* 2026. PMID 41623317; PMCID PMC12853772; DOI 10.1016/j.ymgmr.2026.101291.
- [hall-1993-rat-bcat] Hall TR, Wallin R, Reinhart GD, Hutson SM. Branched chain aminotransferase isoenzymes. Purification and characterization of the rat brain isoenzyme. *J Biol Chem* 1993. PMID 8381418; DOI 10.1016/s0021-9258(18)53663-2.
- [herbert-2020-oxidized-mutant] Herbert D, Gibbs S, Riddick A, Conway M et al. Crystal structure of an oxidized mutant of human mitochondrial branched-chain aminotransferase. *Acta Crystallogr F* 2020. PMID 31929181; PMCID PMC6957111; DOI 10.1107/s2053230x19016480.
- [hutson-1993-bcka-transport] Hutson SM, Hall TR. Identification of the mitochondrial branched chain aminotransferase as a branched chain alpha-keto acid transport protein. *J Biol Chem* 1993. PMID 8428987; DOI 10.1016/s0021-9258(18)53662-0.
- [hutson-1998-bcat-neurotransmitter] Hutson SM, Berkich D, Drown P, Xu B et al. Role of branched-chain aminotransferase isoenzymes and gabapentin in neurotransmitter metabolism. *J Neurochem* 1998. PMID 9681479; DOI 10.1046/j.1471-4159.1998.71020863.x.
- [hutson-2008-sulfenic-acid] Hutson SM, Poole LB, Coles S, Conway ME. Redox regulation and trapping sulfenic acid in the peroxide-sensitive human mitochondrial branched chain aminotransferase. *Methods Mol Biol* 2008. PMID 19157014; DOI 10.1007/978-1-59745-129-1_10.
- [islam-2007-bcaa-metabolon] Islam MM, Wallin R, Wynn RM, Conway M et al. A novel branched-chain amino acid metabolon. Protein-protein interactions in a supramolecular complex. *J Biol Chem* 2007. PMID 17314104; DOI 10.1074/jbc.m700198200.
- [islam-2010-gdh-metabolon] Islam MM, Nautiyal M, Wynn RM, Mobley JA et al. Branched-chain amino acid metabolon: interaction of glutamate dehydrogenase with the mitochondrial branched-chain aminotransferase (BCATm). *J Biol Chem* 2010. PMID 19858196; PMCID PMC2804173; DOI 10.1074/jbc.m109.048777.
- [kean-1979-ketohypoglycin] Kean EA, Pogson CI. Inhibition of gluconeogenesis in isolated rat liver cells by methylenecyclopropylpyruvate (ketohypoglycin). *Biochem J* 1979; 182:789-796. PMID 518564; PMCID PMC1161413; DOI 10.1042/bj1820789.
- [ma-2022-prdm16-browning] Ma QX, Zhu WY, Lu XC, Jiang D, Xu F et al. BCAA-BCKA axis regulates WAT browning through acetylation of PRDM16. *Nat Metab* 2022. PMID 35075301; DOI 10.1038/s42255-021-00520-6.
- [mondesert-2025-bcat2-deficiency] Mondésert E, Bouchereau J, Schiff M et al. Branched-chain amino acid transferase type 2 (BCAT2) deficiency: Report of an eighth case and literature review. *Mol Genet Metab Rep* 2025. PMID 40248769; PMCID PMC12005323; DOI 10.1016/j.ymgmr.2025.101213.
- [neinast-2019-bcaa-fate] Neinast MD, Jang C, Hui S, Murashige DS et al. Quantitative Analysis of the Whole-Body Metabolic Fate of Branched-Chain Amino Acids. *Cell Metab* 2019. PMID 30449684; PMCID PMC6365191; DOI 10.1016/j.cmet.2018.10.013.
- [neinast-2019-bcaa-review] Neinast M, Murashige D, Arany Z. Branched Chain Amino Acids. *Annu Rev Physiol* 2019. PMID 30485760; PMCID PMC6536377; DOI 10.1146/annurev-physiol-020518-114455.
- [reemtsma-2025-eventing-amino-acids] Reemtsma FP, Giers J, Horstmann S et al. Concentration Changes in Plasma Amino Acids and Their Metabolites in Eventing Horses During Cross-Country Competitions. *Animals* 2025; 15:1840. PMID 40646739; PMCID PMC12249093; DOI 10.3390/ani15131840.
- [sander-2023-atypical-myopathy] Sander J, Terhardt M, Janzen N, Renaud B et al. Tissue Specific Distribution and Activation of *Sapindaceae* Toxins in Horses Suffering from Atypical Myopathy. *Animals* 2023. PMID 37570219; PMCID PMC10417358; DOI 10.3390/ani13152410.
- [she-2007-bcatm-knockout] She P, Reid TM, Bronson SK, Vary TC et al. Disruption of BCATm in mice leads to increased energy expenditure associated with the activation of a futile protein turnover cycle. *Cell Metab* 2007. PMID 17767905; PMCID PMC2693888; DOI 10.1016/j.cmet.2007.08.003.
- [suryawan-1998-bcaa-model] Suryawan A, Hawes JW, Harris RA, Shimomura Y et al. A molecular model of human branched-chain amino acid metabolism. *Am J Clin Nutr* 1998. PMID 9665099; DOI 10.1093/ajcn/68.1.72.
- [than-2001-pp18-bcatm] Than NG, Sümegi B, Than GN, Bellyei S et al. Molecular cloning and characterization of placental tissue protein 18 (PP18a)/human mitochondrial branched-chain aminotransferase (BCATm) and its novel alternatively spliced PP18b variant. *Placenta* 2001; 22:235-243. PMID 11170829; DOI 10.1053/plac.2000.0603.
- [wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, Zoli M et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009. PMID 19892987; PMCID PMC3785132; DOI 10.1126/science.1178158.
- [wang-2015-bcat2-deficiency] Wang XL, Li CJ, Xing Y, Yang YH, Jia JP. Hypervalinemia and hyperleucine-isoleucinemia caused by mutations in the branched-chain-amino-acid aminotransferase gene. *J Inherit Metab Dis* 2015. PMID 25653144; DOI 10.1007/s10545-015-9814-z.
- [wouters-2024-zebrafish-sapindaceae] Wouters CP, Klein B, Price N, Boemer F et al. A Zebrafish Embryo Model to Screen Potential Therapeutic Compounds in *Sapindaceae* Poisoning. *Molecules* 2024; 29:4954. PMID 39459322; PMCID PMC11510690; DOI 10.3390/molecules29204954.
- [wu-2004-enu-bcatm-mice] Wu JY, Kao HJ, Li SC, Stevens R, Hillman et al. ENU mutagenesis identifies mice with mitochondrial branched-chain aminotransferase deficiency resembling human maple syrup urine disease. *J Clin Invest* 2004. PMID 14755340; PMCID PMC324540; DOI 10.1172/jci19574.
- [yennawar-2001-bcatm-structure] Yennawar N, Dunbar J, Conway M, Hutson S, Farber G. The structure of human mitochondrial branched-chain aminotransferase. *Acta Crystallogr D* 2001. PMID 11264579; DOI 10.1107/s0907444901001925.
- [yennawar-2002-bcatm-intermediates] Yennawar NH, Conway ME, Yennawar HP, Farber GK, Hutson SM. Crystal structures of human mitochondrial branched chain aminotransferase reaction intermediates: ketimine and pyridoxamine phosphate forms. *Biochemistry* 2002. PMID 12269802; DOI 10.1021/bi020221c.
- [yennawar-2006-cxxc-catalysis] Yennawar NH, Islam MM, Conway M, Wallin R et al. Human mitochondrial branched chain aminotransferase isozyme: structural role of the CXXC center in catalysis. *J Biol Chem* 2006. PMID 17050531; DOI 10.1074/jbc.m607552200.
- Database records consulted: UniProtKB A0A9L0TSN4 (https://rest.uniprot.org/uniprotkb/A0A9L0TSN4.txt), UniProtKB O15382 (human BCAT2), Ensembl gene ENSECAG00000011310 (https://rest.ensembl.org/lookup/id/ENSECAG00000011310).


## Citations

1. arfuso-2019-horse-bcaa-exercise-abstract.md
2. arfuso-2019-horse-bcaa-exercise-summary.md
3. austin-2025-emaciated-horses-abstract.md
4. austin-2025-emaciated-horses-fulltext.txt
5. austin-2025-emaciated-horses-summary.md
6. bledsoe-1997-bcatm-cloning-abstract.md
7. bledsoe-1997-bcatm-cloning-summary.md
8. cole-2012-brain-bcatm-abstract.md
9. cole-2012-brain-bcatm-fulltext.txt
10. cole-2012-brain-bcatm-summary.md
11. coles-2012-redox-potential-abstract.md
12. coles-2012-redox-potential-summary.md
13. conway-2002-cxxc-redox-switch-abstract.md
14. conway-2002-cxxc-redox-switch-summary.md
15. conway-2003-substrate-specificity-abstract.md
16. conway-2003-substrate-specificity-summary.md
17. conway-2004-cxxc-cysteines-abstract.md
18. conway-2004-cxxc-cysteines-summary.md
19. davoodi-1998-human-bcat-kinetics-abstract.md
20. davoodi-1998-human-bcat-kinetics-summary.md
21. dhanani-2019-bcat2-myoblast-abstract.md
22. dhanani-2019-bcat2-myoblast-fulltext.txt
23. dhanani-2019-bcat2-myoblast-summary.md
24. faure-1999-sheep-placenta-bcatm-abstract.md
25. faure-1999-sheep-placenta-bcatm-summary.md
26. filipic-2026-bcat2-deficiency-review-abstract.md
27. filipic-2026-bcat2-deficiency-review-fulltext.txt
28. filipic-2026-bcat2-deficiency-review-summary.md
29. hall-1993-rat-bcat-abstract.md
30. hall-1993-rat-bcat-summary.md
31. herbert-2020-oxidized-mutant-abstract.md
32. herbert-2020-oxidized-mutant-fulltext.txt
33. herbert-2020-oxidized-mutant-summary.md
34. hutson-1993-bcka-transport-abstract.md
35. hutson-1993-bcka-transport-summary.md
36. hutson-1998-bcat-neurotransmitter-abstract.md
37. hutson-1998-bcat-neurotransmitter-summary.md
38. hutson-2008-sulfenic-acid-abstract.md
39. hutson-2008-sulfenic-acid-summary.md
40. islam-2007-bcaa-metabolon-abstract.md
41. islam-2007-bcaa-metabolon-summary.md
42. islam-2010-gdh-metabolon-abstract.md
43. islam-2010-gdh-metabolon-summary.md
44. kean-1979-ketohypoglycin-abstract.md
45. kean-1979-ketohypoglycin-summary.md
46. ma-2022-prdm16-browning-abstract.md
47. ma-2022-prdm16-browning-summary.md
48. mondesert-2025-bcat2-deficiency-abstract.md
49. mondesert-2025-bcat2-deficiency-fulltext.txt
50. mondesert-2025-bcat2-deficiency-summary.md
51. neinast-2019-bcaa-fate-abstract.md
52. neinast-2019-bcaa-fate-fulltext.txt
53. neinast-2019-bcaa-fate-summary.md
54. neinast-2019-bcaa-review-abstract.md
55. neinast-2019-bcaa-review-fulltext.txt
56. neinast-2019-bcaa-review-summary.md
57. reemtsma-2025-eventing-amino-acids-abstract.md
58. reemtsma-2025-eventing-amino-acids-fulltext.txt
59. reemtsma-2025-eventing-amino-acids-summary.md
60. sander-2023-atypical-myopathy-abstract.md
61. sander-2023-atypical-myopathy-fulltext.txt
62. sander-2023-atypical-myopathy-summary.md
63. she-2007-bcatm-knockout-abstract.md
64. she-2007-bcatm-knockout-summary.md
65. suryawan-1998-bcaa-model-abstract.md
66. suryawan-1998-bcaa-model-summary.md
67. than-2001-pp18-bcatm-abstract.md
68. than-2001-pp18-bcatm-summary.md
69. wade-2009-horse-genome-abstract.md
70. wade-2009-horse-genome-summary.md
71. wang-2015-bcat2-deficiency-abstract.md
72. wang-2015-bcat2-deficiency-summary.md
73. wouters-2024-zebrafish-sapindaceae-abstract.md
74. wouters-2024-zebrafish-sapindaceae-fulltext.txt
75. wouters-2024-zebrafish-sapindaceae-summary.md
76. wu-2004-enu-bcatm-mice-abstract.md
77. wu-2004-enu-bcatm-mice-summary.md
78. yennawar-2001-bcatm-structure-abstract.md
79. yennawar-2001-bcatm-structure-summary.md
80. yennawar-2002-bcatm-intermediates-abstract.md
81. yennawar-2002-bcatm-intermediates-summary.md
82. yennawar-2006-cxxc-catalysis-abstract.md
83. yennawar-2006-cxxc-catalysis-summary.md