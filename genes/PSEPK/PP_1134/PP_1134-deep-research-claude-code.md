---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:33:18.995567'
end_time: '2026-10-30T21:38:16.648387'
duration_seconds: 297.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_1134
  gene_symbol: PP_1134
  uniprot_accession: Q88NS1
  protein_description: 'RecName: Full=NAD(P)/FAD-dependent oxidoreductase {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_1134 {ECO:0000313|EMBL:AAN66759.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DUF8436. (IPR059480); FAD-binding_protein. (IPR028348); FAD-depend_C.
    (IPR049516); FAD/NAD-bd_sf. (IPR036188); DUF8436 (PF28550)
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
  web_search_requests: 3
  num_turns: 16
  total_cost_usd: 0.9508546999999998
  session_id: aebcfa9b-b512-4766-a66e-09a00480600f
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88NS1
- **Protein Description:** RecName: Full=NAD(P)/FAD-dependent oxidoreductase {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_1134 {ECO:0000313|EMBL:AAN66759.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF8436. (IPR059480); FAD-binding_protein. (IPR028348); FAD-depend_C. (IPR049516); FAD/NAD-bd_sf. (IPR036188); DUF8436 (PF28550)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_1134" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_1134' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_1134** (gene ID: PP_1134, UniProt: Q88NS1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking InterPro/structure and fitness data for this uncharacterized COG2509 family.

Checking the one Swiss-Prot family member's references, then writing the report.

# PP_1134 (Q88NS1) in *Pseudomonas putida* KT2440: an uncharacterized FAD-binding oxidoreductase of the COG2509 / PIRSF038984 family

## Summary

- **Identity checked.** Locus tag PP_1134 in *P. putida* KT2440 maps to UniProt Q88NS1 (TrEMBL, unreviewed; 535 aa, 58.4 kDa). It is encoded on the complementary strand at 1,298,570–1,300,177. Both GenBank and KEGG call it a "conserved protein of unknown function". The UniProt name "NAD(P)/FAD-dependent oxidoreductase" comes from the ProtNLM machine-learning model (ECO:0008006), not from curation.
- **No published experimental study of PP_1134 turned up.** Targeted web searches on the locus tag, COG2509 and PIRSF038984 found no work on this protein or on any characterized member of its family. The **literature on this gene is effectively absent**, and everything below is inferred from domain, family and structure data.
- **Most likely function:** a cytoplasmic protein that binds FAD and has the Rossmann-fold architecture of the FAD/NAD(P)-binding oxidoreductase superfamily. Its **reaction, substrate and pathway are unknown.** InterPro, Pfam and KEGG all describe the family as functionally unknown.
- **Strongest structural evidence:** PP_1134 is **69% identical over residues 1–533** to *Vibrio parahaemolyticus* VP0956 (UniProt Q87R42). VP0956's crystal structure (PDB 3NLC, a structural genomics target) was solved **with FAD bound**.
- **No GO annotations exist** for Q88NS1 in GOA (the downloaded `PP_1134-goa.tsv` has only a header row).

---

## 1. Identity and verification

| Attribute | Value | Source |
|---|---|---|
| Accession | Q88NS1 (Q88NS1_PSEPK), TrEMBL, PE 4 (Predicted) | UniProt flat file (local `PP_1134-uniprot.txt`) |
| Locus | PP_1134; RefSeq WP_010952294.1; EMBL AAN66759.1 | UniProt |
| Length / mass | 535 aa / 58,399 Da | UniProt |
| Genome position | complement(1298570..1300177) | KEGG ppu:PP_1134 (https://www.kegg.jp/entry/ppu:PP_1134) |
| KEGG orthology | K07137 "uncharacterized protein" (BRITE: "Poorly characterized → Function unknown"), linked to COG2509 | KEGG KO K07137 (https://www.kegg.jp/entry/K07137) |
| eggNOG | COG2509 (Bacteria) | UniProt DR line |
| PANTHER | PTHR42842 "FAD/NAD(P)-BINDING OXIDOREDUCTASE"; subfamily SF3 "FAD_NAD(P)-BINDING OXIDOREDUCTASE FAMILY PROTEIN" | UniProt; local `interpro/panther/panther.obo` |
| PIRSF | PIRSF038984 "FAD_binding_protein" | UniProt |
| InterPro / Pfam | IPR028348 FAD-binding protein; IPR036188 FAD/NAD(P)-binding domain superfamily; IPR049516/PF21688 FAD-dependent C-terminal domain (residues 285–481); IPR059480/PF28550 DUF8436 (residues 1–60) | UniProt FT/DR lines |
| CATH/Gene3D | 3.50.50.60 FAD/NAD(P)-binding domain (×2); 3.30.70.2700 | UniProt |

The locus tag, organism and domain content all point to the same protein. The gene symbol is not ambiguous, because PP_1134 is a unique ordered locus name. Genome sources: Nelson et al. 2002, *Environ. Microbiol.* 4:799 (PMID:12534463), and the re-annotation by Belda et al. 2016, *Environ. Microbiol.* 18:3403 (PMID:26913973). Neither paper characterizes this gene.

## 2. What the family databases say

The family is named as an oxidoreductase, but no member has been studied.

- **InterPro IPR028348 ("FAD dependent protein"):** *"This entry represents uncharacterised FAD dependent proteins. Their function is not clear."* (InterPro API, https://www.ebi.ac.uk/interpro/entry/InterPro/IPR028348/, accessed 2026-10-30)
- **Pfam PF21688 ("FAD-dependent protein, C-terminal domain-like"):** *"This domain is found towards the C-terminal of a group of bacterial and archaeal FAD-linked dehydrogenases, whose exact function is not yet clear."* (https://www.ebi.ac.uk/interpro/entry/pfam/PF21688/)
- **COG2509:** NCBI CDD calls it "FAD-dependent dehydrogenase [General function prediction only]" (https://www.ncbi.nlm.nih.gov/Structure/cdd/COG2509). The FFAS profile database lists it as "Uncharacterized FAD-dependent dehydrogenases".
- **KEGG K07137:** "uncharacterized protein", filed under *Function unknown*.
- **PANTHER PTHR42842:** about 6,160 proteins in about 5,800 proteomes, bacterial and archaeal (local `interpro/panther/PTHR42842/PTHR42842-metadata.yaml`). The family has no PANTHER GO terms, and the only Swiss-Prot member is *Clostridium beijerinckii* Cbei_0202 (Q05627). Q05627 is still named "Uncharacterized protein". It was sequenced only in passing, as "ORF1" next to the butyrate kinase genes (PMID:8396545), and its record has no function comment.
- **Members in model organisms:** querying KEGG K07137 for *E. coli*, *B. subtilis*, *P. aeruginosa*, *S. enterica* and *M. tuberculosis* returned no members. Members were found in *V. cholerae* (VC_0806) and *C. beijerinckii*. Missing from *E. coli* and *B. subtilis* helps explain why the family has no experimental characterization.

## 3. Structural and sequence evidence that it binds FAD

### 3.1 A close homolog crystallized with FAD (PDB 3NLC)

- PDB **3NLC**: "Crystal structure of the VP0956 protein from *Vibrio parahaemolyticus*", Northeast Structural Genomics Consortium target VpR147. Deposited 2010-06-21, released 2010-08-18, and used as a CASP target (RCSB, https://www.rcsb.org/structure/3NLC).
- Ligand entity 2 in 3NLC is **FAD (flavin-adenine dinucleotide)** (RCSB REST API, nonpolymer entity 3NLC/2).
- **My own alignment:** a local Smith–Waterman alignment (Biopython, BLOSUM62, gap open −11 / extend −1) of PP_1134 against the 3NLC chain A sequence gives **368 identical residues, 69.2% identity, covering PP_1134 residues 1–533 of 535**. At this identity over the full length, the fold, the FAD cofactor and the domain arrangement almost certainly carry over to PP_1134. No primary paper on the structure turned up, so no substrate or activity was reported for VP0956.

### 3.2 Conserved dinucleotide-binding motifs

A motif scan of the PP_1134 sequence found the classic signatures of the FAD/NAD(P)-binding Rossmann fold:

| Motif | PP_1134 position | Context | Interpretation |
|---|---|---|---|
| GxGxxG | Gly104–Gly109 | ERPIVV**G**F**G**PC**G**IFAGLL | N-terminal βαβ ADP-binding fingerprint, typical of the FAD-binding domain in the glutathione reductase / D-amino acid oxidase superfamilies |
| GxGxxG (second) | Gly157–Gly162 | ESNVQF**G**E**G**GA**G**TFSDGK | Possible second dinucleotide-binding element, consistent with Gene3D assigning two 3.50.50.60 domains |
| C-terminal GD/GE-type motif | ~500–527 | …GLFP**AGE**GAGYAGGILSAGVDG… | Resembles the C-terminal FAD-ribityl/pyrophosphate-binding motif (the "GD" motif) found in FAD-dependent oxidoreductases |

All three motifs are conserved in VP0956: GFGPCG, GEGGAG and **YPAGEGAGYAGGILSAG** are present nearly verbatim. That conservation supports their role in binding FAD.

KEGG's Pfam scan also gives weaker hits to DAO (D-amino acid oxidase), HI0933_like, GIDA (MnmG), Pyr_redox_2/3, FAD_binding_2/3, Amino_oxidase and NAD_binding_9. These are **superfamily-level similarities across the FAD/NAD(P)-binding Rossmann clan**, not evidence for any of those specific activities. Several of those families do mutually exclusive chemistry: amine oxidation, tRNA modification, disulfide reduction, flavin monooxygenation.

### 3.3 N-terminal DUF8436 domain

Residues 1–60 form Pfam PF28550 (DUF8436), a newly defined domain of unknown function. It is also conserved in VP0956: compare MLRITELKLPLDHPDEALREAIVQRLGI… in PP_1134 with MIRINEIKLPLDHEEGALLDAITKKLGI… in VP0956. It may be a substrate-recognition or partner-binding module that sets this family apart from other FAD oxidoreductases. That is speculation.

## 4. Possible reaction and substrates

- **Established:** binding of FAD, with high confidence from the homologous FAD-bound crystal structure and the conserved motifs. The matching GO molecular function term is "flavin adenine dinucleotide binding" (GO:0050660).
- **Not established:** the catalytic activity. The protein might be a dehydrogenase, oxidase or reductase, using NAD(P)H or an organic substrate, but there is **no direct evidence for any specific reaction**. The ProtNLM name "NAD(P)/FAD-dependent oxidoreductase" and the COG label "FAD-dependent dehydrogenase" are generic assignments at superfamily level. The most a GO annotation could defensibly say is the broad "oxidoreductase activity" (GO:0016491), and even that is inferred from the fold rather than shown.
- **Substrate specificity:** unknown.

## 5. Where it acts in the cell

- UniProt has no signal-peptide or transmembrane features for Q88NS1. VP0956 was expressed and crystallized as a soluble protein, consistent with a soluble cytoplasmic oxidoreductase.
- **Inference: cytoplasm**, from the absence of export or membrane signals and the soluble homolog structure. I ran no signal-peptide or topology predictor here; SignalP or DeepTMHMM would confirm it.

## 6. Genomic context and possible pathway

Neighbouring genes from KEGG (https://www.kegg.jp/entry/ppu:PP_1131 … PP_1137):

| Locus | Strand | Annotation |
|---|---|---|
| PP_1131 | + | outer membrane lipoprotein SlyB (K06077) |
| PP_1132 | − | Na⁺/H⁺ antiporter NhaA 1 (K03313) |
| PP_1133 | + | IS110-family transposase |
| **PP_1134** | **−** | **COG2509 FAD-binding protein (K07137)** |
| PP_1135 | − | conserved exported protein / putative lipoprotein (K08985, UCP028175) |
| PP_1136 | + | conserved protein of unknown function (DUF5122) |
| PP_1137 | − | branched-chain amino acid ABC transporter ATP-binding protein (K01996) |

- PP_1134 and PP_1135 sit on the same strand with a short intergenic gap (1,300,177 → 1,300,281, about 100 bp), so they could be co-transcribed. However, PP_1135 is itself uncharacterized and points to no pathway.
- There is an IS110 transposase immediately upstream (PP_1133), but no metabolic operon around the gene to suggest a substrate class. **No pathway can be assigned from genomic context.**
- No KEGG pathway, BioCyc pathway or Reactome-type assignment exists for PP_1134 (KEGG BRITE puts K07137 under "Function unknown"; BioCyc lists only a monomer, PPUT160488:G1G01-1212-MONOMER).

## 7. Experimental and high-throughput data

- **Targeted studies:** none found for PP_1134 in web searches on the locus tag. The only hit, a 2025 bioRxiv preprint on GenBank versus RefSeq annotation differences in KT2440, concerns locus-tag nomenclature, not this gene (https://www.biorxiv.org/content/10.1101/2025.05.27.656432.full.pdf).
- **Genome-wide fitness (RB-TnSeq):** *P. putida* KT2440 is in the Fitness Browser (Price et al.; https://fit.genomics.lbl.gov, org "Putida"), but **the page could not be retrieved** because it is behind a bot challenge. Fitness phenotypes for PP_1134 were therefore **not assessed** here and should be checked manually. A specific carbon-source, nitrogen-source or stress phenotype would be the most useful clue to its substrate.
- **Proteomics:** a PaxDb entry exists (160488-PP_1134), which suggests the protein is detected in KT2440 proteomes. Abundance values were not retrieved.

## 8. Annotation implications

| Aspect | Supportable claim | Basis | Confidence |
|---|---|---|---|
| MF | flavin adenine dinucleotide binding (GO:0050660) | FAD-bound structure of a 69%-identical homolog (3NLC); conserved GxGxxG and C-terminal motifs; InterPro IPR028348/IPR036188 | High (inferred) |
| MF | oxidoreductase activity (GO:0016491) | Fold and superfamily membership only | Low to moderate; no specific activity shown |
| CC | cytoplasm (GO:0005737) | No signal peptide or TM features; soluble homolog | Moderate (inferred) |
| BP | — | No basis | None should be assigned |

Assigning any specific enzyme activity would be over-annotation. Candidates such as D-amino acid oxidase, MnmG-like tRNA modification or glutathione reductase-like chemistry come only from weak cross-family Pfam hits within the shared Rossmann clan.

## 9. Open questions and suggested experiments

1. **Confirm the flavin:** purify recombinant PP_1134 and check its UV-visible spectrum for flavin bound in the 370/450 nm region. Use HPLC to tell FAD from FMN.
2. **Find the electron partners:** measure NADH and NADPH oxidase or diaphorase activity with artificial acceptors (DCPIP, ferricyanide, cytochrome c).
3. **Screen for substrates:** use metabolite-library activity screens (thermal-shift ligand screening, untargeted metabolomics of a ΔPP_1134 strain) and RB-TnSeq phenotypes from the Fitness Browser.
4. **Use the structure:** dock ligands into the 3NLC active-site cavity next to the FAD isoalloxazine ring, and compare with the AlphaFold model of Q88NS1 (AF-Q88NS1-F1), to narrow down substrate chemistry.
5. **Map the N-terminal domain:** determine the role of DUF8436 (residues 1–60), for example by deletion constructs and pull-downs.

---

## Sources

- UniProtKB Q88NS1 (local copy `genes/PSEPK/PP_1134/PP_1134-uniprot.txt`, entry version 106, 10 Jun 2026): https://www.uniprot.org/uniprotkb/Q88NS1
- UniProtKB Q87R42 (VP0956) and Q05627 (Cbei_0202): https://rest.uniprot.org/uniprotkb/Q05627.txt
- KEGG gene entries ppu:PP_1131–PP_1137: https://www.kegg.jp/entry/ppu:PP_1134
- KEGG KO K07137: https://www.kegg.jp/entry/K07137
- InterPro IPR028348: https://www.ebi.ac.uk/interpro/entry/InterPro/IPR028348/
- Pfam PF21688: https://www.ebi.ac.uk/interpro/entry/pfam/PF21688/
- PANTHER PTHR42842 (InterPro metadata, fetched 2026-10-30): https://www.ebi.ac.uk/interpro/entry/panther/PTHR42842/
- NCBI CDD COG2509: https://www.ncbi.nlm.nih.gov/Structure/cdd/COG2509
- FFAS COG profile listing: https://ffas.godziklab.org/ffas-cgi/cgi/get_mu.pl?rv=COG1018*COG1018*re*KOG2404
- RCSB PDB 3NLC (VP0956, FAD-bound; released 2010-08-18): https://www.rcsb.org/structure/3NLC
- Nelson KE et al. (2002) Complete genome sequence and comparative analysis of the metabolically versatile *Pseudomonas putida* KT2440. *Environ Microbiol* 4:799–808. PMID:12534463
- Belda E et al. (2016) The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis. *Environ Microbiol* 18:3403–3424. PMID:26913973
- PMID:8396545 (1993), cloning of the *C. acetobutylicum/beijerinckii* NCIMB 8052 phosphotransbutyrylase and butyrate kinase genes; source of the Q05627 "ORF1" fragment
- bioRxiv preprint (2025), GenBank vs RefSeq annotation differences in KT2440: https://www.biorxiv.org/content/10.1101/2025.05.27.656432.full.pdf
- Fitness Browser, *P. putida* KT2440 (not retrievable in this session): https://fit.genomics.lbl.gov/cgi-bin/singleFit.cgi?orgId=Putida&locusId=PP_1134

**About this report:** sources from 2023–2024 were prioritized, but none exist for this gene or family. The literature search was limited to web search because the PubMed connector needs authorization in claude.ai connector settings and was unavailable. The alignment and motif analyses are my own quick computations, run during this session and not saved to the repository.

## Citations

1. https://www.kegg.jp/entry/ppu:PP_1134
2. https://www.kegg.jp/entry/K07137
3. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR028348/
4. https://www.ebi.ac.uk/interpro/entry/pfam/PF21688/
5. https://www.ncbi.nlm.nih.gov/Structure/cdd/COG2509
6. https://www.rcsb.org/structure/3NLC
7. https://www.kegg.jp/entry/ppu:PP_1131
8. https://www.biorxiv.org/content/10.1101/2025.05.27.656432.full.pdf
9. https://fit.genomics.lbl.gov
10. https://www.uniprot.org/uniprotkb/Q88NS1
11. https://rest.uniprot.org/uniprotkb/Q05627.txt
12. https://www.ebi.ac.uk/interpro/entry/panther/PTHR42842/
13. https://ffas.godziklab.org/ffas-cgi/cgi/get_mu.pl?rv=COG1018*COG1018*re*KOG2404
14. https://fit.genomics.lbl.gov/cgi-bin/singleFit.cgi?orgId=Putida&locusId=PP_1134