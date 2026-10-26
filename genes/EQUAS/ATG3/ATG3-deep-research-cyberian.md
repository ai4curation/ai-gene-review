---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:05:59.706560'
end_time: '2026-10-25T23:15:57.295443'
duration_seconds: 597.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: ATG3
  gene_symbol: ATG3
  uniprot_accession: A0A9L0IHI0
  protein_description: 'RecName: Full=Ubiquitin-like-conjugating enzyme ATG3 {ECO:0000256|ARBA:ARBA00017573};
    AltName: Full=Autophagy-related protein 3 {ECO:0000256|ARBA:ARBA00034553};'
  gene_info: Name=ATG3 {ECO:0000313|Ensembl:ENSEASP00005040400.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the ATG3 family.
  protein_domains: Atg3/Atg10. (IPR007135); Autophagy_act_C (PF03987)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3303
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 73
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IHI0
- **Protein Description:** RecName: Full=Ubiquitin-like-conjugating enzyme ATG3 {ECO:0000256|ARBA:ARBA00017573}; AltName: Full=Autophagy-related protein 3 {ECO:0000256|ARBA:ARBA00034553};
- **Gene Information:** Name=ATG3 {ECO:0000313|Ensembl:ENSEASP00005040400.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the ATG3 family.
- **Key Domains:** Atg3/Atg10. (IPR007135); Autophagy_act_C (PF03987)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATG3" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATG3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATG3** (gene ID: ATG3, UniProt: A0A9L0IHI0) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATG3 (Ubiquitin-like-conjugating enzyme ATG3) in the donkey, *Equus asinus* (UniProt A0A9L0IHI0)

## 1. Introduction and summary

The donkey protein A0A9L0IHI0 is an unreviewed TrEMBL entry (protein existence level 3, "inferred from homology"). It is predicted from the chromosome-level Dezhou donkey reference genome [wang-2020-donkeygenome-abstract] and annotated by automatic rules as ubiquitin-like-conjugating enzyme ATG3, a member of the ATG3 family carrying the Atg3/Atg10 domain (IPR007135; Pfam PF03987, Autophagy_act_C). There is no published experimental work on ATG3 from donkey or any other equid. A PubMed search for ATG3 in *Equus* found nothing, and the donkey genome paper that underlies the gene model does not mention ATG3 at all [wang-2020-donkeygenome-fulltext]. Everything this report says about function therefore rests on orthology. That inference is unusually safe in this case, because the gene symbol is not ambiguous and the donkey sequence is almost identical to human ATG3, as shown in Section 2.

The ATG3 family is the E2 of the Atg8/LC3 lipidation system. ATG3 takes an ATG8-family ubiquitin-like protein (LC3A/B/C, GABARAP, GABARAPL1, GABARAPL2/GATE-16) from the E1 enzyme ATG7 onto its active-site cysteine as a thioester. It then transfers the C-terminal glycine of that protein onto the amino group of phosphatidylethanolamine (PE), forming an amide-linked ATG8–PE conjugate [ichimura-2000-lipidation-abstract; tanida-2002-humanatg3-abstract]. This protein–lipid conjugation is unusual among ubiquitin-like pathways. It anchors LC3/GABARAP proteins in the growing isolation membrane (phagophore) and is needed for the membrane to elongate and close into an autophagosome [sou-2008-atg3knockout-abstract; mizushima-2011-review-abstract]. ATG3 works in the cytosol and on the surface of highly curved autophagic membranes. An N-terminal amphipathic helix senses lipid-packing defects [nath-2014-curvature-abstract; ye-2021-nterminal-abstract], and the ATG12–ATG5-ATG16L1 complex acts as an E3-like enhancer of the transfer step [hanada-2007-e3like-abstract]. ATG3 also has a second, autophagy-independent identity as a substrate of ATG12. The ATG12–ATG3 conjugate affects mitochondrial homeostasis and Alix-dependent late-endosome function [radoshevich-2010-atg12atg3-abstract; murrow-2015-alix-abstract].

## 2. Identity verification and sequence features of donkey ATG3

The UniProt record lists gene name ATG3 (Ensembl ENSEASG00005011413; NCBI GeneID 106829515; RefSeq XP_014694150.1) on donkey chromosome 5. Its CTD cross-reference (64422) is the human *ATG3* gene identifier, and its PANTHER family is PTHR12866:SF2 (ubiquitin-like-conjugating enzyme ATG3). The only experimental feature annotated is a disordered region at residues 145–166 (MobiDB-lite). Its automatic Gene Ontology annotations (TreeGrafter) are Atg8-family ligase activity, autophagosome assembly, cytosol and phagophore assembly site (UniProt entry A0A9L0IHI0, accessed for this report). These annotations fit the experimentally established function of the orthologs.

To check identity directly, I aligned the 342-residue donkey sequence with the 314-residue canonical isoform of human ATG3 (Q9NT62) [uniprot-Q9NT62-record]. The donkey protein contains one contiguous 28-residue insertion (donkey residues 223–250, VVADITKPCWTDFFLPPLLGVNFPPNNP) between the residues corresponding to human Glu222 and Gln223. With that segment removed, the donkey and human sequences differ at only five of 314 positions (human T117A, N130S, N133S, R135K and D148E, all in the acidic flexible region), about 98% identity. Every element of human ATG3 that has been characterised experimentally is conserved, at identical sequence, in the donkey protein. The N-terminal amphipathic, curvature-sensing helix keeps the Lys9 and Lys11 residues needed to recognise anionic lipids [hervas-2017-bilayers-abstract]. The EYLTP motif (residues 17–21), which couples that helix to the catalytic core, is intact [ye-2021-nterminal-fulltext]. The flexible region carries the non-canonical LC3-interacting region (LIR) DGGWVDT at residues 104–110 [farnung-2023-lir-abstract] and the caspase-8 cleavage site LETD at residues 166–169 [oral-2012-caspase8-abstract]. Downstream of the insertion, the lysine that accepts ATG12 (Lys243 in mouse and human; Lys271 in donkey, in the context DHVKKTVTIE) [murrow-2015-alix-fulltext] and the catalytic cysteine (human Cys264 [tanida-2002-humanatg3-abstract]; donkey Cys287, within the conserved HLPPPPMC motif) are both present.

The 28-residue insertion is the one real difference from human ATG3, and database records show that it is an alternatively included segment rather than a fixed feature of the equid protein. The same donkey gene (Ensembl ENSEASG00005011413, NCBI GeneID 106829515) also encodes a second annotated product, A0A9L0J149 (RefSeq XP_014694151.1). That protein is 314 residues long and identical to A0A9L0IHI0 except that it lacks the 28-residue segment, so it matches the human canonical isoform in length and organisation [uniprot-A0A9L0J149-record; uniprot-A0A9L0IHI0-record]. The horse gene model includes a 342-residue product (A0A3Q2L0A4, RefSeq XP_005602052.1) with the same insertion [uniprot-A0A3Q2L0A4-record]. However, the only horse ATG3 sequence supported by transcript evidence, L7MRX2 (a partial cDNA, EMBL HQ890113, from a normalized equine cDNA library), crosses the junction as LFGYDEQRQ, exactly as in human ATG3, and so lacks the insertion [uniprot-L7MRX2-record]. The best-supported equid ATG3 is therefore the 314-residue form, which is essentially the human protein. The 342-residue A0A9L0IHI0 is a predicted alternative isoform whose expression has not been shown in the sources examined here. The insertion lies just before the catalytic region; in the human protein, residues 262–277 and 291–300 contact membranes during catalysis [ye-2024-curvedmembranes-abstract]. It is proline-rich and hydrophobic and adds an extra cysteine, so if it is expressed it could change the catalytic or membrane-binding behaviour of that isoform. Even so, the conservation of the catalytic, E1-binding, E3-binding, LIR and membrane-sensing elements confirms that A0A9L0IHI0 is a product of the true donkey ortholog of ATG3. Literature on human, mouse and yeast ATG3 is the right basis for inferring its function.

## 3. Catalytic function: an E2 enzyme that conjugates ATG8-family proteins to phosphatidylethanolamine

ATG3's core biochemical function was defined in budding yeast. Ichimura and colleagues showed that Atg8, after its C-terminal arginine is removed by the protease Atg4, is attached to PE through an amide bond between its exposed C-terminal glycine and the amino group of the lipid head group. The reaction needs a ubiquitin-like cascade in which Atg7 activates Atg8 as an E1 and passes it to the E2 Atg3 (Apg3/Aut1). The same E1 hands the other ubiquitin-like protein, Atg12, to a different E2, Atg10 [ichimura-2000-lipidation-abstract]. The cascade therefore has two branches, and ATG3 is dedicated to the ATG8/LC3 branch.

Tanida and co-workers cloned human ATG3, which is 34% identical to yeast Atg3. Site-directed mutagenesis showed that Cys264 is the true active-site residue that forms thioester intermediates with each of the three human ATG8 homologues then known, GATE-16 (GABARAPL2), GABARAP and LC3. A C264S mutant trapped stable E2–substrate complexes, and LC3 was the preferred substrate [tanida-2002-humanatg3-abstract]. In the same work, ATG3 co-immunoprecipitated with ATG7, showing that the E1–E2 complex is conserved from yeast to mammals [tanida-2002-humanatg3-abstract]. The reaction catalysed by ATG3, and so by the donkey ortholog, can be written as a thioester-transfer cascade: ATG7~ATG8 + ATG3-SH → ATG7-SH + ATG3~ATG8, followed by ATG3~ATG8 + PE (in a membrane) → ATG3-SH + ATG8–PE (amide). The specificity is for the C-terminal glycine of mature (ATG4-processed) LC3/GABARAP-family proteins on the donor side and for the primary amine of PE on the acceptor side [ichimura-2000-lipidation-abstract; tanida-2002-humanatg3-abstract].

Structural work shows how a protein with a canonical E2 fold carries out this non-canonical lipid transfer. The 2.5 Å crystal structure of yeast Atg3 has an α/β core topologically similar to ubiquitin E2s, with two large insertions. One is a roughly 80-residue flexible region (FR) that is disordered in solution and binds Atg7. The other is a long α-helical "handle region" that projects about 30 Å from the core and binds Atg8. A sulfate ion bound next to the catalytic cysteine suggested where the phosphate of PE may sit [yamada-2007-atg3structure-abstract]. In donkey ATG3 the acidic, low-complexity stretch annotated as disordered (residues 145–166) lies inside the region corresponding to this flexible region. Mechanistic work on the yeast enzyme has since explained how this E2 fold is adapted to an unusual acceptor. Atg3 uses a threonine (Thr213 in yeast) in place of the asparagine that canonical E2s use at the active site. In free Atg3 the catalytic cysteine points away from this threonine in a catalytically incompetent orientation, which damps conjugase activity until the E3 reorients the cysteine toward the threonine [sakohnakatogawa-2013-catalyticsite-abstract; zheng-2019-switch-fulltext]. Tyr179 and His232 near the active site are also important for the lipidation reaction in yeast [zheng-2019-switch-fulltext]. These residues were mapped in yeast and have not been tested in mammalian or equid ATG3.

## 4. The conjugation cascade: hand-off from E1 (ATG7) and activation by the E3 (ATG12–ATG5-ATG16L1)

ATG3 does not bind its E1 in the canonical way. In the Atg7 N-terminal domain–Atg3 FR structure, hydrophobic residues of the Atg3 flexible region fit a conserved groove in Atg7. Modelling of the full (Atg7~Atg8–Atg3)₂ complex showed that Atg8 is passed in *trans* from the catalytic cysteine of one Atg7 protomer to an Atg3 bound to the other protomer of the homodimer [taherbhoy-2011-e1e2-abstract]. Crystal structures of (Atg7–Atg3)₂ confirmed this multisite, "backside" recognition, in which Atg7 holds Atg3 by surfaces away from its active site so that the two catalytic cysteines are brought together [kaiser-2012-atg7atg3-abstract]. In human cells the FAP motif (Phe15-Ala16-Pro17) of ATG7 is needed for ATG7 to bind ATG3 and to form the ATG3~LC3 intermediate [tanida-2012-fap-abstract]. NMR has mapped the human ATG3 region that binds ATG7 (RIA7) within the flexible region [ohashi-2015-atg7region-abstract]. A non-canonical LIR in the same region (residues 104–110 in human and donkey) binds the back side of LC3 as a β-strand. It is needed for ATG3~LC3 thioester formation, for efficient ATG7→ATG3 transfer and for LC3 lipidation in cells [farnung-2023-lir-abstract].

Once loaded, ATG3~LC3 is directed to the membrane and activated by the ATG12–ATG5-ATG16L1 complex. In vitro, the Atg12–Atg5 conjugate, but neither Atg12 nor Atg5 alone, strongly increases transfer of Atg8 from Atg3 to PE by stimulating Atg3 activity. It binds both Atg3 and PE-containing liposomes, which is E3-like behaviour [hanada-2007-e3like-abstract]. In higher eukaryotes the E2 is recruited by ATG12 itself. A 13-residue segment of the human ATG3 flexible region forms a short β-strand and α-helix that bind an ATG12-specific surface, and four contact residues in it are needed both for E3 binding and for LC3 lipidation. These residues are conserved across metazoans and plants [metlagel-2013-atg12atg3-abstract]. The E3-binding site on ATG3 overlaps the ATG7-binding site, so binding to the E1 and to the E3 is mutually exclusive. ATG3 is therefore thought to cycle between ATG7, where it is loaded, and the E3, where it delivers its cargo [qiu-2013-e1e3exclusive-abstract; ohashi-2015-atg7region-abstract]. A conformational switch adds further control. The E1/E2/E3-interacting region (E123IR) of Atg3 holds the catalytic loop in an inactive state, and binding of either the E1 or the E3 to this element releases it, activating Atg3 [zheng-2019-switch-abstract; qiu-2020-switch-abstract]. Zheng et al. proposed that this brace protects the reactive E2~UBL thioester from errant nucleophiles until Atg3 reaches the enzymes of the lipidation cascade [zheng-2019-switch-abstract]. Earlier cell studies fit this picture of cross-regulation: ATG3 binds free ATG12 and the ATG12–ATG5 conjugate, free ATG12 increases LC3 processing, and excess ATG12–ATG5 suppresses it [tanida-2002-atg12-abstract]. ATG3 also promotes formation of ATG12–ATG5 [tanida-2002-humanatg3-abstract].

## 5. Localization: a cytosolic enzyme that acts at highly curved autophagic membranes

Human ATG3 is cytoplasmic at steady state [tanida-2002-humanatg3-abstract], and the donkey entry carries an inferred "cytosol" annotation. Its products, however, are made on membranes, and several lines of evidence show how ATG3 chooses where to act. Nath et al. found that ATG3 lipidates LC3/GABARAP only on membranes with local lipid-packing defects, such as high curvature or a high proportion of conical lipids. This depends on an N-terminal amphipathic helix, formed by about the first 26 residues, that resembles motifs on proteins targeting curved membranes. Making the helix more or less hydrophobic increased or decreased lipidation in vitro and in rescue experiments in Atg3-knockout cells. The authors proposed that ATG3 acts at the highly curved rim of the growing phagophore [nath-2014-curvature-abstract]. Biophysical studies of human ATG3 showed that it binds anionic membranes (especially those containing cardiolipin or phosphatidic acid) more strongly than neutral ones, that curvature increases recruitment, and that Lys9 and Lys11 of the N-terminal helix are needed to recognise negatively charged lipids. ATG3 can also aggregate vesicles in vitro, and membrane binding promotes GABARAP lipidation [hervas-2017-bilayers-abstract].

Later work linked membrane sensing directly to catalysis. A conserved N-terminal region (residues 17–26, containing EYLTP) relays the membrane-binding state of the helix to the C-terminal catalytic core. Mutations there abolish LC3–PE conjugation in vitro and in cells and change the conformation of the membrane-bound protein [ye-2021-nterminal-abstract; ye-2021-nterminal-fulltext]. Catalytically important segments near the active site (human residues 262–277 and 291–300) also contact the membrane. Ye and colleagues have therefore suggested that highly curved phagophore rims act much like a classical E3, bringing substrates together and rearranging ATG3's catalytic centre [ye-2024-curvedmembranes-abstract]. Taken together, ATG3 is a cytosolic enzyme that functions transiently at the phagophore assembly site and on the expanding isolation membrane, where it deposits LC3/GABARAP–PE. All of these membrane-sensing residues are conserved in donkey ATG3 (Section 2). The protein E3 adds a second layer of spatial control. The Atg12–Atg5-Atg16 complex both enhances Atg3's E2 activity and specifies that Atg8–PE is made on autophagy-related membranes. The protease Atg4 later cleaves Atg8–PE to release Atg8 for reuse, so ATG3-generated conjugates turn over in a deconjugation cycle that can itself regulate autophagosome formation [nakatogawa-2013-review-abstract].

## 6. Physiological role in autophagosome biogenesis: genetic evidence

Mouse genetics established that ATG3 is essential in mammals. *Atg3*-deficient mice are born but die within a day. Conjugation of all mammalian ATG8 homologues to PE is completely lost. ATG12–ATG5 conjugation is also markedly reduced, and ATG12–ATG5 dissociates from isolation membranes more slowly. Isolation membranes fail to elongate and close normally, giving malformed autophagosomes [sou-2008-atg3knockout-abstract]. These results put ATG3, and the LC3/GABARAP lipidation it carries out, at the membrane elongation and closure step of macroautophagy, downstream of but feeding back on the ATG12 system [sou-2008-atg3knockout-abstract; mizushima-2011-review-abstract]. Because the donkey protein is conserved in every catalytic and regulatory element, its biological process can be assigned with confidence as autophagosome assembly (macroautophagy) through Atg8-family protein lipidation. Its UniProt process annotations for selective forms of autophagy (mitophagy, nucleophagy, glycophagy) follow from this general role and are not equid-specific findings.

## 7. Non-canonical roles and regulation: ATG12–ATG3, caspase cleavage and acetylation

ATG3 is itself a target of ubiquitin-like modification. Radoshevich et al. showed that ATG12 is covalently attached to a single lysine on ATG3. The reaction requires ATG7 as E1 and uses ATG3's own E2 activity, so it is autocatalytic. Blocking ATG12–ATG3 formation did not affect starvation-induced autophagy but expanded mitochondrial mass and blunted mitochondrial cell death [radoshevich-2010-atg12atg3-abstract]. In atg3⁻/⁻ fibroblasts reconstituted with the non-conjugatable K243R mutant, loss of ATG12–ATG3 reduced basal (but not starvation-induced) autophagic flux, caused perinuclear late endosomes to accumulate and impaired endolysosomal trafficking. ATG12–ATG3 binds the ESCRT-associated protein Alix (PDCD6IP) and controls Alix-dependent processes including late-endosome distribution, exosome biogenesis and viral budding [murrow-2015-alix-abstract; murrow-2015-alix-fulltext]. The acceptor lysine is conserved in donkey ATG3 (Lys271).

ATG3 is also a point where cell death and autophagy are coordinated. During TNFα- and TRAIL-induced death-receptor signalling, caspase-8 cleaves ATG3 directly. Mutating the cleavage site (LETD, conserved in donkey) or inhibiting caspases restores autophagy, which in that system protected cells from death [oral-2012-caspase8-abstract]. In yeast, the acetyltransferase Esa1 acetylates Atg3 at Lys19 and Lys48 on the pre-autophagosomal structure during starvation, which promotes Atg3–Atg8 binding and Atg8 lipidation. The deacetylase Rpd3 reverses the modification [yi-2012-acetylation-abstract]. Whether this acetylation control applies to the mammalian, and so the equid, protein is not established here; the yeast lysine numbers do not map directly onto the mammalian sequence.

## 8. Conclusions

Donkey ATG3 (A0A9L0IHI0) is, by sequence, the ortholog of human ATG3. Its predicted primary function is that of the E2-like enzyme of the ATG8/LC3 conjugation system: it accepts LC3/GABARAP-family proteins from ATG7 as a thioester on its active-site cysteine (Cys287 in donkey, equivalent to human Cys264) and transfers their C-terminal glycine to the amino group of PE in membranes [ichimura-2000-lipidation-abstract; tanida-2002-humanatg3-abstract]. It functions in the cytosol and at the highly curved rims of phagophores, recruited by curvature sensing through its N-terminal amphipathic helix and by the ATG12–ATG5-ATG16L1 E3 [nath-2014-curvature-abstract; hanada-2007-e3like-abstract; metlagel-2013-atg12atg3-abstract], and it is needed for autophagosome membrane elongation and closure [sou-2008-atg3knockout-abstract]. Secondary roles through the ATG12–ATG3 conjugate in mitochondrial and endolysosomal homeostasis are likely to be conserved [radoshevich-2010-atg12atg3-abstract; murrow-2015-alix-abstract]. All of these statements are inferences from orthologs; none have been tested in equids.

## Open Questions

The most immediate open question is whether the 342-residue isoform represented by A0A9L0IHI0 is actually expressed. The same donkey gene also encodes a 314-residue, human-like isoform (A0A9L0J149), and the only horse transcript evidence (L7MRX2) lacks the 28-residue insertion [uniprot-A0A9L0J149-record; uniprot-L7MRX2-record]. Mapping donkey and horse RNA-seq or long-read transcript data across the exon junction, and checking how the insertion sits in the AlphaFold model, would show whether the extra segment is a tissue-restricted equid exon or a gene-prediction artefact. If it is real, a useful experiment would be to test whether it changes LC3 lipidation, membrane curvature sensing or ATG12–ATG3 formation in *Atg3*-null cells rescued with donkey ATG3 with and without the insertion.

More generally, there are no biochemical or cell-biological data on any equid ATG3. Simple checks would confirm that donkey ATG3 forms an ATG3~LC3 thioester through Cys287, lipidates LC3/GABARAP on curved liposomes in an ATG12–ATG5-ATG16L1-stimulated manner, and forms an ATG12–ATG3 conjugate at Lys271. Unresolved mechanistic questions in the field also apply here. It is still unclear how the membrane-curvature mechanism (Section 5) and the protein E3 work together at the phagophore rim [ye-2024-curvedmembranes-abstract]. It is also unclear whether the acetylation control described in yeast [yi-2012-acetylation-abstract] operates on mammalian ATG3. Finally, the relative substrate preference of ATG3 among the six or more mammalian LC3/GABARAP paralogs, first examined by Tanida et al. [tanida-2002-humanatg3-abstract], has not been examined in equine tissues. That could matter for veterinary studies of autophagy in equine muscle, liver and reproductive physiology.

## References

- **farnung-2023-lir**: Farnung J, Muhar M, Liang JR, Tolmachova KA, Benoit RM, Corn JE, et al. (2023). Semisynthetic LC3 Probes for Autophagy Pathways Reveal a Noncanonical LC3 Interacting Region Motif Crucial for the Enzymatic Activity of Human ATG3. *ACS Cent Sci* 9:1025-1034. PMID: 37252361; PMCID: PMC10214526; DOI: 10.1021/acscentsci.3c00009 (https://doi.org/10.1021/acscentsci.3c00009). https://pubmed.ncbi.nlm.nih.gov/37252361/
- **hanada-2007-e3like**: Hanada T, Noda NN, Satomi Y, Ichimura Y, Fujioka Y, Takao T, et al. (2007). The Atg12-Atg5 conjugate has a novel E3-like activity for protein lipidation in autophagy. *J Biol Chem* 282:37298-302. PMID: 17986448; DOI: 10.1074/jbc.C700195200 (https://doi.org/10.1074/jbc.C700195200). https://pubmed.ncbi.nlm.nih.gov/17986448/
- **hervas-2017-bilayers**: Hervás JH, Landajuela A, Antón Z, Shnyrova AV, Goñi FM, Alonso A (2017). Human ATG3 binding to lipid bilayers: role of lipid geometry, and electric charge. *Sci Rep* 7:15614. PMID: 29142222; PMCID: PMC5688168; DOI: 10.1038/s41598-017-15057-6 (https://doi.org/10.1038/s41598-017-15057-6). https://pubmed.ncbi.nlm.nih.gov/29142222/
- **ichimura-2000-lipidation**: Ichimura Y, Kirisako T, Takao T, Satomi Y, Shimonishi Y, Ishihara N, et al. (2000). A ubiquitin-like system mediates protein lipidation. *Nature* 408:488-92. PMID: 11100732; DOI: 10.1038/35044114 (https://doi.org/10.1038/35044114). https://pubmed.ncbi.nlm.nih.gov/11100732/
- **kaiser-2012-atg7atg3**: Kaiser SE, Mao K, Taherbhoy AM, Yu S, Olszewski JL, Duda DM, et al. (2012). Noncanonical E2 recruitment by the autophagy E1 revealed by Atg7-Atg3 and Atg7-Atg10 structures. *Nat Struct Mol Biol* 19:1242-9. PMID: 23142976; PMCID: PMC3515690; DOI: 10.1038/nsmb.2415 (https://doi.org/10.1038/nsmb.2415). https://pubmed.ncbi.nlm.nih.gov/23142976/
- **metlagel-2013-atg12atg3**: Metlagel Z, Otomo C, Takaesu G, Otomo T (2013). Structural basis of ATG3 recognition by the autophagic ubiquitin-like protein ATG12. *Proc Natl Acad Sci U S A* 110:18844-9. PMID: 24191030; PMCID: PMC3839761; DOI: 10.1073/pnas.1314755110 (https://doi.org/10.1073/pnas.1314755110). https://pubmed.ncbi.nlm.nih.gov/24191030/
- **mizushima-2011-review**: Mizushima N, Yoshimori T, Ohsumi Y (2011). The role of Atg proteins in autophagosome formation. *Annu Rev Cell Dev Biol* 27:107-32. PMID: 21801009; DOI: 10.1146/annurev-cellbio-092910-154005 (https://doi.org/10.1146/annurev-cellbio-092910-154005). https://pubmed.ncbi.nlm.nih.gov/21801009/
- **murrow-2015-alix**: Murrow L, Malhotra R, Debnath J (2015). ATG12-ATG3 interacts with Alix to promote basal autophagic flux and late endosome function. *Nat Cell Biol* 17:300-10. PMID: 25686249; PMCID: PMC4344874; DOI: 10.1038/ncb3112 (https://doi.org/10.1038/ncb3112). https://pubmed.ncbi.nlm.nih.gov/25686249/
- **nakatogawa-2013-review**: Nakatogawa H (2013). Two ubiquitin-like conjugation systems that mediate membrane formation during autophagy. *Essays Biochem* 55:39-50. PMID: 24070470; DOI: 10.1042/bse0550039 (https://doi.org/10.1042/bse0550039). https://pubmed.ncbi.nlm.nih.gov/24070470/
- **nath-2014-curvature**: Nath S, Dancourt J, Shteyn V, Puente G, Fong WM, Nag S, et al. (2014). Lipidation of the LC3/GABARAP family of autophagy proteins relies on a membrane-curvature-sensing domain in Atg3. *Nat Cell Biol* 16:415-24. PMID: 24747438; PMCID: PMC4111135; DOI: 10.1038/ncb2940 (https://doi.org/10.1038/ncb2940). https://pubmed.ncbi.nlm.nih.gov/24747438/
- **ohashi-2015-atg7region**: Ohashi K, Otomo T (2015). Identification and characterization of the linear region of ATG3 that interacts with ATG7 in higher eukaryotes. *Biochem Biophys Res Commun* 463:447-52. PMID: 26043688; PMCID: PMC4507496; DOI: 10.1016/j.bbrc.2015.05.107 (https://doi.org/10.1016/j.bbrc.2015.05.107). https://pubmed.ncbi.nlm.nih.gov/26043688/
- **oral-2012-caspase8**: Oral O, Oz-Arslan D, Itah Z, Naghavi A, Deveci R, Karacali S, et al. (2012). Cleavage of Atg3 protein by caspase-8 regulates autophagy during receptor-activated cell death. *Apoptosis* 17:810-20. PMID: 22644571; DOI: 10.1007/s10495-012-0735-0 (https://doi.org/10.1007/s10495-012-0735-0). https://pubmed.ncbi.nlm.nih.gov/22644571/
- **qiu-2013-e1e3exclusive**: Qiu Y, Hofmann K, Coats JE, Schulman BA, Kaiser SE (2013). Binding to E1 and E3 is mutually exclusive for the human autophagy E2 Atg3. *Protein Sci* 22:1691-7. PMID: 24186333; PMCID: PMC3843624; DOI: 10.1002/pro.2381 (https://doi.org/10.1002/pro.2381). https://pubmed.ncbi.nlm.nih.gov/24186333/
- **qiu-2020-switch**: Qiu Y, Zheng Y, Grace CRR, Liu X, Klionsky DJ, Schulman BA (2020). Allosteric regulation through a switch element in the autophagy E2, Atg3. *Autophagy* 16:183-184. PMID: 31690182; PMCID: PMC6984587; DOI: 10.1080/15548627.2019.1688550 (https://doi.org/10.1080/15548627.2019.1688550). https://pubmed.ncbi.nlm.nih.gov/31690182/
- **radoshevich-2010-atg12atg3**: Radoshevich L, Murrow L, Chen N, Fernandez E, Roy S, Fung C, et al. (2010). ATG12 conjugation to ATG3 regulates mitochondrial homeostasis and cell death. *Cell* 142:590-600. PMID: 20723759; PMCID: PMC2925044; DOI: 10.1016/j.cell.2010.07.018 (https://doi.org/10.1016/j.cell.2010.07.018). https://pubmed.ncbi.nlm.nih.gov/20723759/
- **sakohnakatogawa-2013-catalyticsite**: Sakoh-Nakatogawa M, Matoba K, Asai E, Kirisako H, Ishii J, Noda NN, et al. (2013). Atg12-Atg5 conjugate enhances E2 activity of Atg3 by rearranging its catalytic site. *Nat Struct Mol Biol* 20:433-9. PMID: 23503366; DOI: 10.1038/nsmb.2527 (https://doi.org/10.1038/nsmb.2527). https://pubmed.ncbi.nlm.nih.gov/23503366/
- **sou-2008-atg3knockout**: Sou YS, Waguri S, Iwata J, Ueno T, Fujimura T, Hara T, et al. (2008). The Atg8 conjugation system is indispensable for proper development of autophagic isolation membranes in mice. *Mol Biol Cell* 19:4762-75. PMID: 18768753; PMCID: PMC2575156; DOI: 10.1091/mbc.e08-03-0309 (https://doi.org/10.1091/mbc.e08-03-0309). https://pubmed.ncbi.nlm.nih.gov/18768753/
- **taherbhoy-2011-e1e2**: Taherbhoy AM, Tait SW, Kaiser SE, Williams AH, Deng A, Nourse A, et al. (2011). Atg8 transfer from Atg7 to Atg3: a distinctive E1-E2 architecture and mechanism in the autophagy pathway. *Mol Cell* 44:451-61. PMID: 22055190; PMCID: PMC3277881; DOI: 10.1016/j.molcel.2011.08.034 (https://doi.org/10.1016/j.molcel.2011.08.034). https://pubmed.ncbi.nlm.nih.gov/22055190/
- **tanida-2002-atg12**: Tanida I, Nishitani T, Nemoto T, Ueno T, Kominami E (2002). Mammalian Apg12p, but not the Apg12p.Apg5p conjugate, facilitates LC3 processing. *Biochem Biophys Res Commun* 296:1164-70. PMID: 12207896; DOI: 10.1016/s0006-291x(02)02057-0 (https://doi.org/10.1016/s0006-291x(02)02057-0). https://pubmed.ncbi.nlm.nih.gov/12207896/
- **tanida-2002-humanatg3**: Tanida I, Tanida-Miyake E, Komatsu M, Ueno T, Kominami E (2002). Human Apg3p/Aut1p homologue is an authentic E2 enzyme for multiple substrates, GATE-16, GABARAP, and MAP-LC3, and facilitates the conjugation of hApg12p to hApg5p. *J Biol Chem* 277:13739-44. PMID: 11825910; DOI: 10.1074/jbc.M200385200 (https://doi.org/10.1074/jbc.M200385200). https://pubmed.ncbi.nlm.nih.gov/11825910/
- **tanida-2012-fap**: Tanida I, Yamasaki M, Komatsu M, Ueno T (2012). The FAP motif within human ATG7, an autophagy-related E1-like enzyme, is essential for the E2-substrate reaction of LC3 lipidation. *Autophagy* 8:88-97. PMID: 22170151; DOI: 10.4161/auto.8.1.18339 (https://doi.org/10.4161/auto.8.1.18339). https://pubmed.ncbi.nlm.nih.gov/22170151/
- **uniprot-A0A3Q2L0A4**: UniProtKB entry A0A3Q2L0A4. https://rest.uniprot.org/uniprotkb/A0A3Q2L0A4.txt (https://www.uniprot.org/uniprotkb/A0A3Q2L0A4); accessed 2026-10-25.
- **uniprot-A0A9L0IHI0**: UniProtKB entry A0A9L0IHI0. https://rest.uniprot.org/uniprotkb/A0A9L0IHI0.txt (https://www.uniprot.org/uniprotkb/A0A9L0IHI0); accessed 2026-10-25.
- **uniprot-A0A9L0J149**: UniProtKB entry A0A9L0J149. https://rest.uniprot.org/uniprotkb/A0A9L0J149.txt (https://www.uniprot.org/uniprotkb/A0A9L0J149); accessed 2026-10-25.
- **uniprot-L7MRX2**: UniProtKB entry L7MRX2. https://rest.uniprot.org/uniprotkb/L7MRX2.txt (https://www.uniprot.org/uniprotkb/L7MRX2); accessed 2026-10-25.
- **uniprot-Q9NT62**: UniProtKB entry Q9NT62. https://rest.uniprot.org/uniprotkb/Q9NT62.txt (https://www.uniprot.org/uniprotkb/Q9NT62); accessed 2026-10-25.
- **wang-2020-donkeygenome**: Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7 (https://doi.org/10.1038/s41467-020-19813-7). https://pubmed.ncbi.nlm.nih.gov/33293529/
- **yamada-2007-atg3structure**: Yamada Y, Suzuki NN, Hanada T, Ichimura Y, Kumeta H, Fujioka Y, et al. (2007). The crystal structure of Atg3, an autophagy-related ubiquitin carrier protein (E2) enzyme that mediates Atg8 lipidation. *J Biol Chem* 282:8036-43. PMID: 17227760; DOI: 10.1074/jbc.M611473200 (https://doi.org/10.1074/jbc.M611473200). https://pubmed.ncbi.nlm.nih.gov/17227760/
- **ye-2021-nterminal**: Ye Y, Tyndall ER, Bui V, Tang Z, Shen Y, Jiang X, et al. (2021). An N-terminal conserved region in human Atg3 couples membrane curvature sensitivity to conjugase activity during autophagy. *Nat Commun* 12:374. PMID: 33446636; PMCID: PMC7809043; DOI: 10.1038/s41467-020-20607-0 (https://doi.org/10.1038/s41467-020-20607-0). https://pubmed.ncbi.nlm.nih.gov/33446636/
- **ye-2024-curvedmembranes**: Ye Y, Bewley MC, Wang HG, Tian F, Flanagan JM (2024). What's in an E3: role of highly curved membranes in facilitating LC3-phosphatidylethanolamine conjugation during autophagy. *Autophagy* 20:709-711. PMID: 38032155; PMCID: PMC10936649; DOI: 10.1080/15548627.2023.2288527 (https://doi.org/10.1080/15548627.2023.2288527). https://pubmed.ncbi.nlm.nih.gov/38032155/
- **yi-2012-acetylation**: Yi C, Ma M, Ran L, Zheng J, Tong J, Zhu J, et al. (2012). Function and molecular mechanism of acetylation in autophagy regulation. *Science* 336:474-7. PMID: 22539722; DOI: 10.1126/science.1216990 (https://doi.org/10.1126/science.1216990). https://pubmed.ncbi.nlm.nih.gov/22539722/
- **zheng-2019-switch**: Zheng Y, Qiu Y, Grace CRR, Liu X, Klionsky DJ, Schulman BA (2019). A switch element in the autophagy E2 Atg3 mediates allosteric regulation across the lipidation cascade. *Nat Commun* 10:3600. PMID: 31399562; PMCID: PMC6689050; DOI: 10.1038/s41467-019-11435-y (https://doi.org/10.1038/s41467-019-11435-y). https://pubmed.ncbi.nlm.nih.gov/31399562/


## Citations

1. _metadata.json
2. farnung-2023-lir-abstract.md
3. farnung-2023-lir-fulltext.txt
4. farnung-2023-lir-summary.md
5. hanada-2007-e3like-abstract.md
6. hanada-2007-e3like-summary.md
7. hervas-2017-bilayers-abstract.md
8. hervas-2017-bilayers-fulltext.txt
9. hervas-2017-bilayers-summary.md
10. ichimura-2000-lipidation-abstract.md
11. ichimura-2000-lipidation-summary.md
12. kaiser-2012-atg7atg3-abstract.md
13. kaiser-2012-atg7atg3-fulltext.txt
14. kaiser-2012-atg7atg3-summary.md
15. metlagel-2013-atg12atg3-abstract.md
16. metlagel-2013-atg12atg3-summary.md
17. mizushima-2011-review-abstract.md
18. mizushima-2011-review-summary.md
19. murrow-2015-alix-abstract.md
20. murrow-2015-alix-fulltext.txt
21. murrow-2015-alix-summary.md
22. nakatogawa-2013-review-abstract.md
23. nakatogawa-2013-review-summary.md
24. nath-2014-curvature-abstract.md
25. nath-2014-curvature-fulltext.txt
26. nath-2014-curvature-summary.md
27. ohashi-2015-atg7region-abstract.md
28. ohashi-2015-atg7region-summary.md
29. oral-2012-caspase8-abstract.md
30. oral-2012-caspase8-summary.md
31. qiu-2013-e1e3exclusive-abstract.md
32. qiu-2013-e1e3exclusive-summary.md
33. qiu-2020-switch-abstract.md
34. qiu-2020-switch-summary.md
35. radoshevich-2010-atg12atg3-abstract.md
36. radoshevich-2010-atg12atg3-summary.md
37. sakohnakatogawa-2013-catalyticsite-abstract.md
38. sakohnakatogawa-2013-catalyticsite-summary.md
39. sou-2008-atg3knockout-abstract.md
40. sou-2008-atg3knockout-summary.md
41. taherbhoy-2011-e1e2-abstract.md
42. taherbhoy-2011-e1e2-summary.md
43. tanida-2002-atg12-abstract.md
44. tanida-2002-atg12-summary.md
45. tanida-2002-humanatg3-abstract.md
46. tanida-2002-humanatg3-summary.md
47. tanida-2012-fap-abstract.md
48. tanida-2012-fap-summary.md
49. uniprot-A0A3Q2L0A4-record.txt
50. uniprot-A0A3Q2L0A4-summary.md
51. uniprot-A0A9L0IHI0-record.txt
52. uniprot-A0A9L0IHI0-summary.md
53. uniprot-A0A9L0J149-record.txt
54. uniprot-A0A9L0J149-summary.md
55. uniprot-L7MRX2-record.txt
56. uniprot-L7MRX2-summary.md
57. uniprot-Q9NT62-record.txt
58. uniprot-Q9NT62-summary.md
59. wang-2020-donkeygenome-abstract.md
60. wang-2020-donkeygenome-fulltext.txt
61. wang-2020-donkeygenome-summary.md
62. yamada-2007-atg3structure-abstract.md
63. yamada-2007-atg3structure-summary.md
64. ye-2021-nterminal-abstract.md
65. ye-2021-nterminal-fulltext.txt
66. ye-2021-nterminal-summary.md
67. ye-2024-curvedmembranes-abstract.md
68. ye-2024-curvedmembranes-summary.md
69. yi-2012-acetylation-abstract.md
70. yi-2012-acetylation-summary.md
71. zheng-2019-switch-abstract.md
72. zheng-2019-switch-fulltext.txt
73. zheng-2019-switch-summary.md