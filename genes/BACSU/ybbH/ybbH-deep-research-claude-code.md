---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T22:29:17.095519'
end_time: '2026-10-30T22:33:11.682053'
duration_seconds: 234.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: BACSU
  gene_id: ybbH
  gene_symbol: ybbH
  uniprot_accession: Q45581
  protein_description: 'RecName: Full=Uncharacterized HTH-type transcriptional regulator
    YbbH;'
  gene_info: Name=ybbH; OrderedLocusNames=BSU01690;
  organism_full: Bacillus subtilis (strain 168).
  protein_family: Not specified in UniProt
  protein_domains: Homeodomain-like_sf. (IPR009057); HTH_RpiR. (IPR000281); RpiR-like.
    (IPR047640); RpiR-like_SIS. (IPR035472); SIS_dom. (IPR001347)
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
  num_turns: 10
  total_cost_usd: 0.8032468100000001
  session_id: e7228c73-ac88-4e32-adaf-eb7b79d77104
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q45581
- **Protein Description:** RecName: Full=Uncharacterized HTH-type transcriptional regulator YbbH;
- **Gene Information:** Name=ybbH; OrderedLocusNames=BSU01690;
- **Organism (full):** Bacillus subtilis (strain 168).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Homeodomain-like_sf. (IPR009057); HTH_RpiR. (IPR000281); RpiR-like. (IPR047640); RpiR-like_SIS. (IPR035472); SIS_dom. (IPR001347)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ybbH" matches the protein description above**
2. **Verify the organism is correct:** Bacillus subtilis (strain 168).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ybbH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ybbH** (gene ID: ybbH, UniProt: Q45581) in BACSU.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still researching. I have the operon and structural context and am now checking the companion MurNAc-recycling papers and the GOA evidence.

# Research report: *ybbH* / *murR* (UniProt Q45581; BSU01690), *Bacillus subtilis* strain 168

## 1. Identity check

| Field | Value | Source |
|---|---|---|
| UniProt accession | Q45581 (YBBH_BACSU), 283 aa, Swiss-Prot reviewed | local `ybbH-uniprot.txt` |
| UniProt name | "Uncharacterized HTH-type transcriptional regulator YbbH" | UniProt |
| Locus | BSU01690 | UniProt; SubtiWiki |
| Current name | **MurR** (formerly YbbH) | Borisova et al. 2016 ([PMC5061867](https://pmc.ncbi.nlm.nih.gov/articles/PMC5061867/)); SubtiWiki ([YbbH→MurR redirect](https://www.subtiwiki.uni-goettingen.de/wiki//index.php?title=YbbH)) |
| Domains | N-terminal HTH RpiR-type domain (aa 3–79; H-T-H motif aa 39–58), C-terminal SIS domain (aa 123–264) | UniProt (PROSITE PS51071, PS51464; Pfam PF01418 HTH_6, PF01380 SIS; CDD cd05013 SIS_RpiR) |
| Family | RpiR/MurR family; PANTHER PTHR30514:SF10 "MURR_RPIR FAMILY TRANSCRIPTIONAL REGULATOR" | UniProt |

- **Symbol:** in *B. subtilis*, "ybbH" is the old name of the gene now called *murR*. *E. coli* has a separate, unrelated gene also named *ybbH*. All literature used here concerns the *B. subtilis* 168 protein, or names *E. coli* MurR (the former YfeT) explicitly as a homolog.
- **Domains:** the domain content (an HTH_RpiR DNA-binding domain plus a sugar-phosphate-binding SIS domain) matches what is expected of a MurR-type regulator.

## 2. Summary

YbbH/MurR is a cytoplasmic, one-component transcription factor of the RpiR family. It is encoded in the *B. subtilis* operon for recycling N-acetylmuramic acid (MurNAc) from the cell wall, *murQ–murR–murP–amiE–nagZ–ybbC*.

Its role is inferred from three things:
- its domain architecture;
- where it sits on the chromosome;
- its homology to *E. coli* MurR, which has been characterised experimentally.

Together these suggest that YbbH/MurR represses the MurNAc-recycling genes and lets go of them when it binds the pathway intermediate MurNAc-6-phosphate (MurNAc-6P).

**This is not confirmed in *B. subtilis*.** No published study shows that *B. subtilis* MurR binds DNA, names its operator, measures its effect on *murQ* transcription, or identifies its inducer. UniProt still calls it "Uncharacterized". The only experimental data on the protein itself is a structural-genomics crystal structure of its DNA-binding domain (PDB 2O3F).

## 3. Genomic context: the MurNAc-recycling cluster

Borisova et al. (2016, *mBio* 7:e00923-16; PMID 27729505) describe the cluster:

> "The schematic for *B. subtilis* 168 … shows the putative promoter PσA in front of the recycling cluster of 6 genes, including *murQ* (formerly *ybbI*), *murR* (formerly *ybbH*), *murP* (formerly *ybbF*), encoding the MurP EII-BC domain, *amiE* (formerly *ybbE*), encoding the MurNAc-l-alanine amidase AmiE, *nagZ* (formerly *ybbD*), encoding the *N*-acetylglucosaminidase NagZ, and *ybbC*, encoding a protein whose function is unknown." ([PMC5061867](https://pmc.ncbi.nlm.nih.gov/articles/PMC5061867/))

> "A putative MurNAc-recycling operon was also identified on the genome of *B. subtilis* strain 168, containing the genes *murQ*, *murR*, and *murP* (formerly *ybbI*, *ybbH*, and *ybbF*, respectively), which encode proteins with amino acid sequence identities of 48%, 27%, and 38% to the respective *E. coli* enzymes." (same source)

SubtiWiki lists the operon as *murQ–murR–murP–amiE–nagZ–ybbC*, citing the 2012 condition-dependent transcriptome study (Nicolas et al., *Science* 2012; PMID 22383849) ([SubtiWiki MurR](https://subtiwiki.uni-goettingen.de/wiki//index.php?title=MurR)).

What the other genes in the operon do:

| Gene (old name) | Product and activity | Evidence |
|---|---|---|
| *nagZ* (*ybbD*) | Secreted β-N-acetylglucosaminidase; removes terminal GlcNAc from muropeptides | Litzinger et al. 2010, *J Bacteriol* 192:3132; PMID 20400549 ([PMC2901692](https://pmc.ncbi.nlm.nih.gov/articles/PMC2901692)) |
| *amiE* (*ybbE*) | MurNAc-L-Ala amidase; cuts MurNAc-peptides only after NagZ has acted, releasing MurNAc | Litzinger et al. 2010 |
| *murP* (*ybbF*) | MurNAc-specific PTS EIIBC; takes up MurNAc and phosphorylates it to MurNAc-6P | Borisova et al. 2016 |
| *murQ* (*ybbI*) | MurNAc-6P etherase; converts MurNAc-6P to GlcNAc-6P and D-lactate | Borisova et al. 2016 |
| *ybbC* | Function unknown | Borisova et al. 2016 |
| *murR* (*ybbH*) | Putative RpiR-family regulator (this protein) | inferred |

Litzinger et al. (2010) also report that NagZ expression starts in late exponential phase and is about six-fold higher in stationary phase ([DrugBank summary of PMID 20400549](https://go.drugbank.com/articles/A130492)).

Borisova et al. (2016) found that:
- *B. subtilis* recycles about 10% of its cell-wall MurNAc per generation, mostly around the entry into stationary phase.
- Δ*murQ* mutants accumulate MurNAc-6P in the cytoplasm (1.36 ± 0.31 nmol after 24 h).
- These mutants grow normally in rich medium but have "a severe survival disadvantage in late stationary phase".
- "*cre* sites" (catabolite-responsive elements, the binding sites of the global carbon-catabolite regulator CcpA) lie upstream of *murQ* in *B. subtilis* and *S. aureus*. ([PMC5061867](https://pmc.ncbi.nlm.nih.gov/articles/PMC5061867/))

The operon therefore seems to be under two layers of control:
- global carbon-catabolite repression through the *cre* site;
- probably also pathway-specific control by MurR.

The study did make a Δ*murQRP* strain, but it did not report a phenotype that would separate *murR*'s own role from that of *murQ* and *murP*.

## 4. Molecular function, by inference

### 4.1 Domains and structure
- **N-terminal HTH_RpiR domain (Pfam PF01418, aa 3–79):** a winged-helix DNA-binding domain (Gene3D 1.10.10.10).
  - The crystal structure PDB 2O3F (Midwest Center for Structural Genomics, 1.75 Å, deposited December 2006) covers residues 1–108, with three chains in the asymmetric unit. It shows an all-helical HTH fold ([RCSB 2O3F](https://rcsb.org/structure/2O3F); [PDBsum](https://www.ebi.ac.uk/pdbsum/2o3f)).
  - There is no associated publication, and no DNA was bound in the crystal.
- **C-terminal SIS domain (Pfam PF01380, aa 123–264; CDD cd05013 SIS_RpiR):** SIS domains bind phosphorylated sugars. They occur both in enzymes (e.g. GlmS, phosphosugar isomerases) and in regulators of the RpiR family, where the SIS domain is the effector-sensing module.
- **Overall architecture:** HTH plus SIS is the standard layout of an RpiR/MurR-type one-component regulator, in which binding of a sugar-phosphate effector changes how strongly the protein binds DNA.

### 4.2 The *E. coli* homolog
*E. coli* MurR (formerly YfeT) shares about 27% identity with YbbH (Borisova et al. 2016).

- **Repression and operator binding.** Jaeger & Mayer (2008, *J Bacteriol*; PMID 18723630; [PMC2566201](https://pmc.ncbi.nlm.nih.gov/articles/PMC2566201)) showed that MurR:
  - forms a stable multimer;
  - binds two adjacent inverted repeats in the *murQ–murR* intergenic operator;
  - represses the *murQP* operon and its own gene.
- **Inducer.** In the same study, MurNAc-6P, the substrate of MurQ, was the specific inducer that weakens MurR's binding to the operator ([EcoliWiki PMID:18723630](https://ecoliwiki.org/colipedia/index.php/PMID:18723630)).
- **Structures.** Structures of *E. coli* MurR from 2022 (PDB 7EN5/7EN6/7EN7; [Proteopedia 7en7](https://proteopedia.org/w/7en7)) show that MurNAc-6P and GlcNAc-6P both bind the SIS domain and both weaken DNA binding in vitro. In cells, however, only MurNAc-6P derepresses *murQP*.
- **Activation.** In *E. coli*, *murQ* is also activated by cAMP–CAP. In *B. subtilis* the matching global input is probably CcpA acting at the *cre* site, which here would mediate repression.

**Inferred model for *B. subtilis*:** MurR binds an operator near the *murQ* promoter and represses the operon. When cell-wall MurNAc is taken up and phosphorylated by MurP, the resulting MurNAc-6P binds the SIS domain of MurR and relieves repression. MurQ and the other operon enzymes are then made.

**Caveats:**
1. The two proteins are only about 27% identical.
2. Gene layout differs. *E. coli murR* is transcribed divergently from *murQP*, whereas *B. subtilis murR* sits inside the operon between *murQ* and *murP*. This suggests autoregulation within one transcript, but nobody has tested it.
3. Neither the operator sequence nor the effector has been determined for the *B. subtilis* protein.

## 5. Biological process

- **Most likely process:** negative regulation of transcription of the MurNAc / peptidoglycan-recycling genes. This places MurR in cell-wall (peptidoglycan) turnover and recycling, and in using MurNAc as a carbon source, mainly at the transition into stationary phase.
- **No direct evidence:** no *murR*-specific transcriptome, DNA-binding or reporter data has been published.
- **Expression timing:** SubtiWiki reports *murR* expression in late exponential and early stationary phase. This matches the timing of recycling and of NagZ expression ([SubtiWiki](https://subtiwiki.uni-goettingen.de/wiki//index.php?title=MurR)).
- **Mutants:** single *murR* knockouts exist — *ybbH::erm* (NBRP strain MGNA-B951) and the BKE01690/BKK01690 strains from the Bacillus Genetic Stock Center deletion library. No published phenotype specific to *murR* was found.

## 6. Cellular location

The protein has no signal peptide and no transmembrane segment; UniProt shows only HTH and SIS domains. It should therefore be **cytoplasmic** and act on chromosomal DNA in the nucleoid. A cytoplasmic location also matches where the predicted effector would be: MurNAc-6P is made inside the cell by the PTS transporter MurP. No experimental localisation has been reported.

## 7. Current GO annotations (GOA)

| GO term | Evidence | Comment |
|---|---|---|
| GO:0003700 DNA-binding transcription factor activity | IBA (ECO:0000318) and InterPro IEA (ECO:0000256) | Consistent with the HTH_RpiR domain. More specifically, it is probably a repressor (DNA-binding transcription repressor activity). |
| GO:0006355 regulation of DNA-templated transcription | IBA; IEA (ECO:0000501, UniProt keyword) | Consistent. "Negative regulation" is likely but not shown in *B. subtilis*. |
| GO:0032993 protein-DNA complex | IBA | Generic family-level propagation. |
| GO:0003677 DNA binding | IEA (InterPro) | Supported by the domain and the 2O3F HTH fold. |
| GO:0097367 carbohydrate derivative binding | IEA (SIS domain) | Plausible. The *E. coli* homolog binds MurNAc-6P and GlcNAc-6P. |
| GO:1901135 carbohydrate derivative metabolic process | IEA (SIS domain) | A mapping from the SIS domain, which is shared with enzymes. MurR is a regulator rather than a metabolic enzyme, so this term over-reads its role. |

No GO annotation for this protein uses experimental evidence.

## 8. Open questions and suggested experiments

1. **Operator binding.** Use EMSA or DNase I footprinting with purified MurR and the *murQ* promoter or the *murQ–murR* intergenic region, to find the operator. Check whether it resembles the *E. coli* inverted repeats.
2. **Effector.** Test MurNAc-6P, GlcNAc-6P and other sugar phosphates for binding (ITC or thermal shift) and for release of DNA in EMSA.
3. **In vivo regulation.** Measure P*murQ–lacZ* or *gfp* reporter expression in wild type versus Δ*murR*, with and without MurNAc. If MurR is a repressor, expression should be constitutively high without it. Test interaction with CcpA by comparing growth on glucose with growth without it.
4. **Autoregulation.** Map the transcripts to determine whether *murR* is co-transcribed only from the *murQ* promoter or also has its own internal promoter.
5. **Structure.** Solve the full-length structure with an effector bound, to extend 2O3F to the SIS domain.

## 9. Conclusion

YbbH/MurR (BSU01690) is almost certainly a cytoplasmic RpiR-family transcription factor, made of an N-terminal winged-HTH DNA-binding domain (crystal structure 2O3F) and a C-terminal SIS sugar-phosphate-sensing domain. It is encoded inside the *murQ–murR–murP–amiE–nagZ–ybbC* operon, which recycles MurNAc from the cell wall. By homology to *E. coli* MurR, it is predicted to repress this operon and to be relieved by MurNAc-6P, linking transcription to peptidoglycan turnover around the entry into stationary phase. This role has not been shown experimentally in *B. subtilis*. Annotations beyond "DNA-binding transcription factor activity / regulation of transcription" and "carbohydrate derivative (sugar phosphate) binding" should be treated as inferences.

## References

1. Borisova M, Gaupp R, Duckworth A, et al. Peptidoglycan recycling in Gram-positive bacteria is crucial for survival in stationary phase. *mBio* 2016;7(5):e00923-16. PMID 27729505. https://pmc.ncbi.nlm.nih.gov/articles/PMC5061867/
2. Litzinger S, Duckworth A, Nitzsche K, Risinger C, Wittmann V, Mayer C. Muropeptide rescue in *Bacillus subtilis* involves sequential hydrolysis by β-N-acetylglucosaminidase and N-acetylmuramyl-L-alanine amidase. *J Bacteriol* 2010;192(12):3132–3143. PMID 20400549. https://pmc.ncbi.nlm.nih.gov/articles/PMC2901692 ; https://go.drugbank.com/articles/A130492 ; https://kops.uni-konstanz.de/bitstreams/bb08b47f-fd2e-449e-bbf6-775fdae64e50/download
3. Jaeger T, Mayer C. The transcriptional factors MurR and catabolite activator protein regulate N-acetylmuramic acid catabolism in *Escherichia coli*. *J Bacteriol* 2008. PMID 18723630. https://pmc.ncbi.nlm.nih.gov/articles/PMC2566201 ; https://ecoliwiki.org/colipedia/index.php/PMID:18723630
4. *E. coli* MurR structures (2022), PDB 7EN5/7EN6/7EN7. https://proteopedia.org/w/7en7 ; https://proteopedia.org/w/7en5
5. RCSB PDB 2O3F: N-terminal domain of putative transcriptional regulator YbbH from *B. subtilis* (MCSG, released 2 January 2007). https://rcsb.org/structure/2O3F ; https://www.ebi.ac.uk/pdbsum/2o3f
6. SubtiWiki entry for MurR/YbbH. https://subtiwiki.uni-goettingen.de/wiki//index.php?title=MurR ; https://www.subtiwiki.uni-goettingen.de/wiki//index.php?title=YbbH ; https://subtiwiki.uni-goettingen.de/v3/gene/view/125872506C400CB6B3DAEA8B5130B064DFBA4494
7. Nicolas P, et al. Condition-dependent transcriptome reveals high-level regulatory architecture in *Bacillus subtilis*. *Science* 2012. PMID 22383849 (the operon definition cited by SubtiWiki).
8. UniProtKB Q45581 (YBBH_BACSU), entry version 146 (2 September 2026); InterPro, Pfam, PROSITE, CDD and PANTHER cross-references as listed there.

**Source limitations:**
- The SubtiWiki wiki pages returned only an empty page shell when fetched. The SubtiWiki facts above (operon composition, expression timing, mutant strains) come from search-result snippets and could not be checked against the page itself.
- For Borisova et al. 2016, only the Introduction, figure legends and early Results were read verbatim. Discussion-level statements were not used.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC5061867/
2. https://www.subtiwiki.uni-goettingen.de/wiki//index.php?title=YbbH
3. https://subtiwiki.uni-goettingen.de/wiki//index.php?title=MurR
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC2901692
5. https://go.drugbank.com/articles/A130492
6. https://rcsb.org/structure/2O3F
7. https://www.ebi.ac.uk/pdbsum/2o3f
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC2566201
9. https://ecoliwiki.org/colipedia/index.php/PMID:18723630
10. https://proteopedia.org/w/7en7
11. https://kops.uni-konstanz.de/bitstreams/bb08b47f-fd2e-449e-bbf6-775fdae64e50/download
12. https://proteopedia.org/w/7en5
13. https://subtiwiki.uni-goettingen.de/v3/gene/view/125872506C400CB6B3DAEA8B5130B064DFBA4494