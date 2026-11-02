---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T23:41:16.095211'
end_time: '2026-10-30T23:47:14.442105'
duration_seconds: 358.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: GEOSL
  gene_id: GSU2359
  gene_symbol: GSU2359
  uniprot_accession: Q74AJ5
  protein_description: 'SubName: Full=Glycoside hydrolase, family 57, DUF3536 domain-containing
    {ECO:0000313|EMBL:AAR35733.2};'
  gene_info: OrderedLocusNames=GSU2359 {ECO:0000313|EMBL:AAR35733.2};
  organism_full: Geobacter sulfurreducens (strain ATCC 51573 / DSM 12127 / PCA).
  protein_family: Belongs to the glycosyl hydrolase 57 family.
  protein_domains: DUF3536. (IPR021923); GH57. (IPR052046); Glyco_hydro/deAcase_b/a-brl.
    (IPR011330); Glyco_hydro_38_N_sf. (IPR027291); Glyco_hydro_57_N. (IPR004300)
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
  num_turns: 27
  total_cost_usd: 1.3980545000000004
  session_id: 6e051e67-338a-4b20-8e58-231bfa0bce07
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 8
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q74AJ5
- **Protein Description:** SubName: Full=Glycoside hydrolase, family 57, DUF3536 domain-containing {ECO:0000313|EMBL:AAR35733.2};
- **Gene Information:** OrderedLocusNames=GSU2359 {ECO:0000313|EMBL:AAR35733.2};
- **Organism (full):** Geobacter sulfurreducens (strain ATCC 51573 / DSM 12127 / PCA).
- **Protein Family:** Belongs to the glycosyl hydrolase 57 family.
- **Key Domains:** DUF3536. (IPR021923); GH57. (IPR052046); Glyco_hydro/deAcase_b/a-brl. (IPR011330); Glyco_hydro_38_N_sf. (IPR027291); Glyco_hydro_57_N. (IPR004300)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GSU2359" matches the protein description above**
2. **Verify the organism is correct:** Geobacter sulfurreducens (strain ATCC 51573 / DSM 12127 / PCA).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GSU2359' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GSU2359** (gene ID: GSU2359, UniProt: Q74AJ5) in GEOSL.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I've confirmed that GSU2359 is an 817-aa GH57 + DUF3536 protein in PANTHER family PTHR36306. Next I'm searching the literature for what this domain architecture does.

Next I'm mapping GH57's conserved catalytic motifs onto the GSU2359 sequence, then searching for any Geobacter-specific data on this gene.

# GSU2359 (UniProt Q74AJ5), *Geobacter sulfurreducens* PCA: research report

## Summary

No published study has characterised GSU2359 by experiment. I found no enzyme assay, mutant phenotype, structure or localisation study for this protein. Everything below is inferred from sequence, domains, family and genome context. Evidence levels are stated throughout.

Identity checks out. The UniProt entry Q74AJ5 is locus GSU2359 (EMBL AAR35733.2) in strain PCA (ATCC 51573 / DSM 12127, NCBI taxon 243231). It is an unreviewed TrEMBL record of 817 residues, at evidence level "PE 3: Inferred from homology". It comes only from genome sequencing (Methé et al. 2003, *Science* 302:1967, PMID:14671304; Butler et al. 2012, *BMC Genomics* 13:471, PMID:22967216).

What the evidence supports:
- **Family:** GSU2359 is a glycoside hydrolase family 57 (GH57) protein. It has an N-terminal GH57 catalytic domain followed by a domain of unknown function, DUF3536.
- **Catalytic residues:** The two acidic residues GH57 uses for catalysis appear to be conserved. This suggests a working retaining α-glucan-active enzyme (a hydrolase or transglycosylase), not an inactive "like" homologue.
- **Location:** It is probably cytoplasmic, since there is no N-terminal signal peptide.
- **Genome context:** It sits in a probable operon with the trehalose-forming enzymes TreZ and TreY and a TreS–maltokinase fusion. That points to a role in converting glycogen or maltooligosaccharides into trehalose or maltose.
- **Unknown:** The exact reaction and substrate are not established. It could be a hydrolase (an amylase or amylopullulanase) or a 4-α-glucanotransferase.

---

## 1. Key concepts: the GH57 family

- **What GH57 is.** It is the second-largest "α-amylase family" in CAZy and is found only in prokaryotes, mostly in Bacteria. Characterised members include:
  - α-amylase
  - 4-α-glucanotransferase
  - amylopullulanase
  - α-glucan branching enzyme
  - α-galactosidase
  - amylopullulanase–cyclomaltodextrinase
  - non-specified amylase
  - maltogenic amylase

  Sources: Martinovičová & Janeček 2018, *3 Biotech* 8:307, PMID:29998051; [CAZypedia GH57](https://www.cazypedia.org/index.php/Glycoside_Hydrolase_Family_57).
- **Mechanism and structure.** The 2018 analysis states: "The family GH57 enzymes employ the retaining reaction mechanism, share five typical conserved sequence regions and possess catalytic (β/α)7-barrel succeeded by a four-helix bundle with the catalytic machinery consisting of catalytic nucleophile and proton donor (glutamic acid and aspartic acid at strands β4 and β7, respectively)" (PMID:29998051). Because the mechanism is retaining, these enzymes can transglycosylate as well as hydrolyse.
- **The five conserved sequence regions (CSRs).** These were defined in the *Thermococcus litoralis* 4-α-glucanotransferase: "13_HQP (region I), 76_GQLEIV (region II), 120_WLTERV (region III), 212_HDDGEKFGVW (region IV), and 350_AQCNDAYWH (region V)". Regions III and IV contain the nucleophile and the proton donor. Mutagenesis of the equivalent Glu and Asp in an amylopullulanase from *Thermococcus hydrothermalis* abolished activity (Zona et al. 2004, *Eur J Biochem* 271:2863, PMID:15233783). The *T. litoralis* crystal structure was published in Imamura et al. 2003, PMID:12618437.
- **Inactive "like" homologues.** Some GH57 groups lack one or both catalytic residues and "are very probably not able to play the role of a typical family GH57 enzyme" (PMID:29998051). So family membership alone does not show that a protein is active.
- **The 2025 subfamily scheme.** Poláček et al. 2025 (*Int J Biol Macromol* 309:142823, PMID:40187459) split more than 5000 GH57 sequences into ten subfamilies:
  - GH57_1: 4-α-glucanotransferases
  - GH57_2: amylopullulanases
  - GH57_3: α-amylases
  - GH57_4: α-galactosidases
  - GH57_5: branching enzymes
  - GH57_6: non-specified amylases
  - GH57_7: amylopullulanase–cyclomaltodextrinases
  - GH57_8: maltogenic amylases
  - GH57_9 and GH57_10: "not including any characterized members so far despite their conserved catalytic machinery"

  The cached abstract does not say which subfamily GSU2359 belongs to. Checking the subfamily assignment in CAZy would be the most informative next step.

## 2. Domain architecture of GSU2359

| Feature | Residues | Source / interpretation |
|---|---|---|
| GH57 N-terminal catalytic domain (Pfam PF03065) | 100–307 (Pfam core match) | InterPro API. The full (β/α)7 barrel probably starts near residue 1 (see the motif mapping below). |
| DUF3536 (Pfam PF12055, IPR021923) | 340–623 | InterPro: "This presumed domain is functionally uncharacterised… found in bacteria and archaea… typically between 274 to 285 amino acids… found associated with PF03065." No literature or GO terms are attached. |
| CDD cd10797 "GH57N_APU_like_1" | catalytic domain | "N-terminal putative catalytic domain of mainly uncharacterized prokaryotic proteins similar to archaeal thermoactive amylopullulanases" ([NCBI CDD cd10797](https://www.ncbi.nlm.nih.gov/Structure/cdd/cd10797)). |
| PANTHER PTHR36306:SF3 "Glycoside hydrolase family 57" | — | Same family as the characterised *Thermococcus* 4-α-glucanotransferases and the *Dictyoglomus* and *Pyrococcus* amylases (subfamily SF1). GSU2359 is in a different, uncharacterised subfamily. |
| Gene3D 3.20.110.10 / SUPFAM SSF88713 | — | Glycoside hydrolase/deacetylase β/α-barrel fold |
| Signal peptide / TM helix | none | The N-terminus (MERFICIHGHFYQPP…) runs straight into GH57 region I. There is no hydrophobic signal region (my own inspection). |

**Catalytic motif mapping.** This is my own string matching against the motifs from PMID:15233783, not a formal alignment.
- **Region I** (TLGT "HQP"): GSU2359 has **IHGHFYQPP** at residues 8–15. This places the start of the catalytic barrel at the N-terminus, as in other GH57 enzymes.
- **Region III** (TLGT "WLTERV", nucleophile Glu): GSU2359 has **MWLAETAV** at residues 150–157. This gives a candidate nucleophile **Glu154**.
- **Region IV** (TLGT "HDDGEKFGVW", proton-donor Asp): GSU2359 has **IATDGETYG** at residues 260–268. This gives a candidate proton donor **Asp263**, followed by the conserved GE…G pattern.
- **Regions II and V:** I could not assign these confidently by simple matching.

Both catalytic acids therefore appear to be kept. This argues that GSU2359 is a catalytically competent GH57 enzyme rather than an inactive "like" homologue. Confirming this needs a proper alignment (for example, against the GH57 subfamily logos in PMID:40187459) and mutagenesis.

## 3. Genomic context: a trehalose/maltose gene cluster

KEGG gene records for strain PCA (gsu; [KEGG gsu:GSU2359](https://www.kegg.jp/entry/gsu:GSU2359)) show these neighbours:

| Locus | Coordinates (+ strand) | Annotation (KEGG orthology) |
|---|---|---|
| GSU2357 | 2576710–2577756 | mechanosensitive channel |
| **GSU2358** | 2577758–2579650 | maltooligosyltrehalose trehalohydrolase **TreZ** (K01236, EC 3.2.1.141) |
| **GSU2359** | 2579674–2582127 | GH57 + DUF3536 (this protein, no KO) |
| **GSU2360** | 2582128–2585118 | maltooligosyltrehalose synthase **TreY** (K06044, EC 5.4.99.15) |
| **GSU2361** | 2585154–2588489 | trehalose synthase/maltokinase fusion **TreS–Mak** (K05343) |
| GSU2362 | complement | MarR regulator |

TreZ, GSU2359, TreY and TreS–Mak lie on the same strand, almost back to back. GSU2359 ends one nucleotide before TreY starts. This strongly suggests that GSU2359 is co-transcribed with the TreY/TreZ trehalose pathway. In that pathway:
- TreY converts the reducing end of an α-1,4-glucan (glycogen or maltooligosaccharides) into a terminal α,α-1,1 trehalosyl unit.
- TreZ releases trehalose from that end.
- TreS interconverts trehalose and maltose.
- Maltokinase (Mak) phosphorylates maltose to maltose-1-phosphate. In actinobacteria this feeds the GlgE α-glucan pathway (Roy et al. 2013, *Acta Cryst D*; PMID:25619172; Mendes et al. 2010, PMID:20507595; TreS:Pep2 complex structure, PMID:30877199).

Other relevant KEGG orthologue calls for strain PCA:
- **Present:** glycogen synthase GlgA (GSU1023, GSU3257), glycogen phosphorylase (GSU0371, GSU2066) and amylomaltase MalQ (GSU1182).
- **Absent:** no GH13 branching enzyme GlgB (K00700), no debranching enzyme GlgX (K01214), no GlgE (K16147) and no GlgC (K00975) are assigned.
- **The only other GH57 protein:** GSU3255 (Q747L0, 729 aa). It has a GH57 domain with CDD cd10796 (amylopullulanase-type) and no DUF3536. It sits next to glycogen synthase GSU3257, so it is the more likely partner of the glycogen synthesis/turnover genes.

**My interpretation (hypothesis, not established):**
- GSU2359 probably acts on α-1,4-glucan chains, either the substrates or the products of TreY/TreZ. Possible roles include trimming glycogen chains into maltooligosaccharides for TreY, transferring glucan segments (4-α-glucanotransferase-like) or releasing maltose.
- The cluster as a whole looks like it turns stored α-glucan into trehalose or maltose-1-phosphate. Trehalose is a common compatible solute and stress protectant.
- The ISB Network Portal lists GSU2359 with a computational "4-alpha-glucanotransferase activity" GO term and places it in co-regulated modules ([networks.systemsbiology.net/gsu/gene/GSU2359](https://networks.systemsbiology.net/gsu/gene/GSU2359)). That annotation has no experimental basis.

## 4. Function, process and location

| Aspect | Best-supported statement | Evidence type |
|---|---|---|
| **Molecular function** | A retaining GH57 enzyme acting on α-glucosidic bonds, with conserved catalytic residues (predicted Glu154 nucleophile, Asp263 acid/base). The specific activity (α-amylase, amylopullulanase-type hydrolysis or 4-α-glucanotransferase) is not determined. | Family/domain (Pfam, CDD, PANTHER); motif conservation |
| **Substrate** | Probably α-1,4-glucans (glycogen-derived maltooligosaccharides). Possibly α-1,6 (pullulan-type) bonds as well, if it behaves like its amylopullulanase-like CDD neighbours. Not tested. | Inference from the CDD subfamily and the TreY/TreZ context |
| **Biological process** | Probable α-glucan (glycogen/maltooligosaccharide) metabolism linked to trehalose formation via TreY/TreZ. More generally, carbohydrate metabolism. | Genome context (operon-like cluster) |
| **Cellular location** | Probably cytoplasm. There is no signal peptide or TM segment, and its probable substrate (glycogen/maltooligosaccharides) and pathway partners are intracellular. | Sequence inspection; pathway logic |
| **DUF3536 role** | Unknown. It may be a non-catalytic accessory or substrate-binding domain, by analogy with the C-terminal domains that tune specificity in other GH57 enzymes (for example, DUF1957 in GH57 branching enzymes; PMID:21097495). | Speculative |

**Existing GO annotations (GOA):** two InterPro2GO IEA rows, GO:0003824 *catalytic activity* and GO:0005975 *carbohydrate metabolic process*. Both are correct but very broad. At the evidence level available, GO:0016798 or GO:0004553 (*hydrolase activity, acting on/hydrolyzing O-glycosyl compounds*) would be defensible as a more specific molecular-function term, and a more specific α-glucan process term may be defensible too. Any specific enzyme term (EC 3.2.1.1, 3.2.1.41 or 2.4.1.25) would be over-annotation without biochemical data.

## 5. Related organisms and homologues

- *Anaeromyxobacter* sp. K (A2cp1_1916) has the same GH57 + DUF3536 architecture (cd10797) but sits in an unrelated neighbourhood (tyrosinase, MarC). So the TreY/TreZ link is not universal for this architecture.
- None of the PANTHER PTHR36306 members characterised so far (the *Thermococcus* 4-α-glucanotransferases, *Pyrococcus horikoshii* AmyA, *Dictyoglomus* AmyA) are in GSU2359's subfamily SF3.
- I found no characterised DUF3536-containing protein in the literature, the InterPro entry or the GH57 bioinformatics papers I checked (PMID:29998051, PMID:24109595, PMID:15233783).

## 6. Knowledge gaps and suggested experiments

1. **Activity and specificity:** Express GSU2359 recombinantly and test it against amylose, glycogen, pullulan, maltooligosaccharides (G2–G7) and maltooligosyltrehalose. Use TLC or HPAEC to tell hydrolysis apart from disproportionation (4-α-glucanotransferase).
2. **Catalytic residues:** Make E154A and D263A mutants to confirm the predicted catalytic machinery.
3. **Pathway role:** Delete GSU2359 and compare trehalose and glycogen levels with ΔtreY and ΔtreZ strains, including under osmotic or nutrient stress.
4. **DUF3536:** Express a construct with the domain truncated, and compare AlphaFold models (Q74AJ5) with GH57 crystal structures (PMID:12618437, PMID:21097495, PMID:40419759).
5. **Subfamily placement:** Check the GH57 subfamily assignment of GSU2359 in CAZy (PMID:40187459). If it falls in GH57_9 or GH57_10, it belongs to a group that is predicted to be active but has no characterised member.

## Sources

- Methé BA et al. 2003. Genome of *Geobacter sulfurreducens*. *Science* 302:1967. PMID:14671304
- Butler JE et al. 2012. *BMC Genomics* 13:471. PMID:22967216
- Zona R et al. 2004. Bioinformatics of GH57 and catalytic residues of *T. hydrothermalis* amylopullulanase. *Eur J Biochem* 271:2863. PMID:15233783
- Imamura H et al. 2003. Crystal structures of *T. litoralis* 4-α-glucanotransferase. PMID:12618437
- Palomo M et al. 2011. *Thermus thermophilus* GH57 branching enzyme structure. PMID:21097495
- Blesák K & Janeček Š 2013. *Microbiology* 159:2584. PMID:24109595
- Martinovičová M & Janeček Š 2018. *3 Biotech* 8:307. PMID:29998051 ([PMC6037648](https://pmc.ncbi.nlm.nih.gov/articles/PMC6037648/))
- Poláček A et al. 2025. GH57 subfamilies. *Int J Biol Macromol* 309:142823. PMID:40187459
- GH57 amylopullulanase structure (2025). PMID:40419759
- Maltokinase and TreS:Pep2 papers: PMID:20507595, PMID:25619172, PMID:30877199
- [CAZypedia: GH57](https://www.cazypedia.org/index.php/Glycoside_Hydrolase_Family_57)
- [InterPro IPR021923 DUF3536](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR021923/)
- [NCBI CDD cd10797](https://www.ncbi.nlm.nih.gov/Structure/cdd/cd10797)
- [KEGG gsu:GSU2359](https://www.kegg.jp/entry/gsu:GSU2359) and neighbours GSU2357–GSU2362, GSU3254–GSU3257
- [ISB Network Portal GSU2359](https://networks.systemsbiology.net/gsu/gene/GSU2359)
- [UniProt Q74AJ5](https://www.uniprot.org/uniprotkb/Q74AJ5)
- Sequence fingerprint background: [Blesák & Janeček 2012, *Extremophiles*](https://link.springer.com/article/10.1007/s00792-012-0449-9)

## Citations

1. https://www.cazypedia.org/index.php/Glycoside_Hydrolase_Family_57
2. https://www.ncbi.nlm.nih.gov/Structure/cdd/cd10797
3. https://www.kegg.jp/entry/gsu:GSU2359
4. https://networks.systemsbiology.net/gsu/gene/GSU2359
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6037648/
6. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR021923/
7. https://www.uniprot.org/uniprotkb/Q74AJ5
8. https://link.springer.com/article/10.1007/s00792-012-0449-9