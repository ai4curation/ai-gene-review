---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:12:13.948449'
end_time: '2026-10-30T21:14:43.139067'
duration_seconds: 149.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2042
  gene_symbol: PP_2042
  uniprot_accession: Q88L93
  protein_description: 'RecName: Full=DUF1302 domain-containing protein {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_2042 {ECO:0000313|EMBL:AAN67656.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DUF1302. (IPR010727); DUF1302 (PF06980)
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
  web_search_requests: 4
  num_turns: 10
  total_cost_usd: 0.7312865
  session_id: 7730d9fc-ca94-49cb-bcd7-ac572804f6db
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 9
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88L93
- **Protein Description:** RecName: Full=DUF1302 domain-containing protein {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_2042 {ECO:0000313|EMBL:AAN67656.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF1302. (IPR010727); DUF1302 (PF06980)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2042" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2042' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2042** (gene ID: PP_2042, UniProt: Q88L93) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking for any experimental literature on the DUF1302/DUF1329 pair before writing.

# PP_2042 (Q88L93), a DUF1302 protein from *Pseudomonas putida* KT2440: research report

## 1. Identity check

| Field | Value | Source |
|---|---|---|
| UniProt | Q88L93 (TrEMBL, unreviewed; 617 aa; PE 4 "Predicted") | `PP_2042-uniprot.txt` |
| Locus | PP_2042, chromosome 2,321,455–2,323,308 (+ strand) | KEGG ppu:PP_2042 |
| Name | "DUF1302 domain-containing protein". UniProt's name comes from ProtNLM, a machine-learning model. GenBank calls it "conserved exported protein of unknown function". | UniProt DE; KEGG |
| Domain | DUF1302 (Pfam PF06980; InterPro IPR010727), spanning the whole protein | UniProt DR lines |
| Orthology | eggNOG COG3203 (Bacteria) | UniProt DR line |
| Signal peptide | Residues 1–27 (SignalP); mature chain 28–617 | UniProt FT SIGNAL |
| GO annotations | None. The GOA file has only a header row. | `PP_2042-goa.tsv` |

The locus tag, organism and domain all match the target. "PP_2042" is a locus tag, not a shared gene symbol, so there is no risk of picking up literature on a different gene. I found **no publication that studies PP_2042 itself**. Everything below is inferred from the domain family, from homologues studied in other species, and from genomic context.

## 2. Domain family: DUF1302 (PF06980)

- **What the family is.** Pfam/InterPro describe it as "a family of predicted outer membrane beta barrel proteins. These proteins remain uncharacterised. They are approximately 600 residues long." PP_2042, at 617 aa, fits that size ([InterPro PF06980](https://www.ebi.ac.uk/interpro/entry/pfam/PF06980); [NCBI CDD pfam06980](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980)).
- **Proposed system.** The same entry says: "These proteins are likely part of an exporter system that includes an MMPL exporter, a DUF1329 protein [PF07044] family protein that likely acts as a LolA-like chaperone." This is a prediction from genomic context, not an experimental result.
- **Size of the family.** InterPro lists about 4,085 proteins in about 1,779 proteomes, with about 2,576 AlphaFold models. No PDB structures exist and no Swiss-Prot entries are reviewed (InterPro API counters; a UniProt query for reviewed PF06980 entries returned nothing).
- **Fit with PP_2042's sequence.** PP_2042 has an N-terminal Sec signal peptide and no predicted inner-membrane helices. It is rich in glycine, serine and alternating aromatic residues (e.g. "…SLRWYVAALD…", "…LSVSYTDFIDGDY…"), and it ends in an aromatic C-terminal residue (…SLSLGVTF). That C-terminal motif is typical of β-barrel outer-membrane proteins recognised by BAM. These features are consistent with a β-barrel in the outer membrane, but this is my reading of the sequence, not a formal prediction.

## 3. The closest experimentally studied homologues: *P. aeruginosa* PA3923 and PA3422

UniProt classifies both *P. aeruginosa* PAO1 proteins **PA3923 (Q9HX90, 641 aa)** and **PA3422 (Q9HYI3, 585 aa)** as DUF1302 (PF06980) proteins.

- **Laminin binding.** Paulsson et al. (2019, *Sci Rep*, DOI 10.1038/s41598-019-54622-z; [PMC6890786](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6890786/)) identified PA3923 as one of four new high-affinity laminin receptors in the *P. aeruginosa* outer membrane, alongside EstA, OprD and OprG.
  - Mutants lacking these receptors adhered poorly to immobilised laminin.
  - The receptors bound the heparin-binding domains of the laminin α-chain.
  - This is the strongest experimental evidence that a DUF1302 protein sits in the outer membrane and is exposed at the cell surface.
- **Biofilms.** A University of Guelph MSc project ([abstract](https://www.uoguelph.ca/mcb/system/files/J%20Manek%20MSC%20announcement.pdf)) reported:
  - PA3923 is highly abundant in PAO1 biofilm proteomes.
  - Deleting it changed neither growth, morphology, biofilm formation nor antibiotic resistance.
  - Expression of its paralogue *pa3422* rose in the biofilm when *pa3923* was absent, which suggests the two compensate for each other.
  - Bioinformatics suggested these proteins might act as porins, but this remained unproven.
  - This is a thesis abstract, not peer-reviewed work.

Laminin binding is a host-interaction property of a pathogen. It is not evidence for the physiological role of PP_2042 in the soil bacterium *P. putida*.

## 4. Genomic context in KT2440

From KEGG:

| Locus | Position | Annotation |
|---|---|---|
| PP_2039 | 2,317,759–2,318,925 | Putative acyl-CoA dehydrogenase |
| PP_2040 | 2,318,988–2,320,283 | MFS transporter |
| PP_2041 | complement(2,320,296–2,321,240) | LysR-family regulator (K19338) |
| **PP_2042** | **2,321,455–2,323,308** | **DUF1302, exported** |
| **PP_2043** | **2,323,313–2,324,641** | **DUF1329 (PF07044) + "TP_0789-like" domain, "conserved exported protein"** |
| PP_2044 | 2,324,641–2,325,027 | DUF202 / YidH-like inner-membrane protein |
| PP_2045 | complement(2,325,342–2,327,303) | Linear primary-alkylsulfatase (EC 3.1.6.21) |

What the context shows:

- **A conserved DUF1302–DUF1329 pair.** PP_2042 and PP_2043 sit on the same strand only 4 bp apart, which points strongly to co-transcription as an operon. This is exactly the pairing Pfam describes.
- **The partner.** The DUF1329 protein is predicted to be a LolA/LolB-like periplasmic chaperone. Pfam calls it "LolA-like". A Fitness Browser reannotation of *Kangiella aquimarina* calls it distantly related to LolB, the protein that inserts lipoproteins into the outer membrane.
- **No MmpL exporter at this locus.** I saw no MMPL-family RND exporter among the nearby genes. The full Pfam "MMPL + DUF1302 + DUF1329" system is therefore not complete here. KT2440 has four other DUF1302 paralogues (PP_0765, PP_2785, PP_2811, PP_3200), and some of those loci may carry an MmpL.
- **Possible hydrophobic or lipid link.** Neighbouring genes include an acyl-CoA dehydrogenase, an MFS transporter and an alkylsulfatase that acts on long-chain alkyl sulfates such as SDS. The divergent LysR regulator PP_2041 may control the operon. This is weak circumstantial support for a link to lipids or hydrophobic compounds.

## 5. Fitness/cofitness inference from another organism

The [Fitness Browser reannotation page for *Kangiella aquimarina* DSM 16071](https://fitprivate.genomics.lbl.gov/cgi-bin/orgReanno.cgi?orgId=Kang) reports conserved cofitness among three genes. On that basis the curators:

- annotate the DUF1302 protein (B158DRAFT_0994) as a **putative adhesin**, by similarity to PA3923;
- predict that the DUF1329 partner sorts the adhesin to the outer membrane, given its distant relationship to LolB;
- speculate that the neighbouring MmpL exporter exports a lipid or saccharide attached to the adhesin.

These are expert predictions from mutant-fitness data, not biochemical results. I did not find a peer-reviewed paper behind them.

## 6. Synthesis

**Likely primary role.** PP_2042 is most likely a **surface-exposed outer-membrane β-barrel protein**. It probably works with the periplasmic DUF1329 protein PP_2043, which may act as a LolA/LolB-like chaperone or targeting factor. Possible functions are:

1. an adhesin or surface protein, by analogy to the laminin-binding PA3923; or
2. part of an export or uptake system for a lipid, saccharide or other hydrophobic molecule, as Pfam proposes.

No catalytic activity is predicted. There is no evidence that it is an enzyme, and no transported substrate has been identified.

**Localisation.** Several lines point to the outer membrane: the cleavable signal peptide, the absence of inner-membrane helices, the family-level prediction, the aromatic C-terminus, and the experimentally shown outer-membrane, laminin-binding location of PA3923. Before final placement, PP_2042 passes through the periplasm.

**Pathways.** None has been defined. Context hints at outer-membrane biogenesis or surface-molecule export, and possibly at handling of hydrophobic compounds or lipids. All of this is speculative.

**Implications for GO curation.**
- There are no existing annotations.
- At most, a cautious cellular-component term is defensible: "cell outer membrane" (GO:0009279), inferred from the family and sequence features and noted as predicted.
- Molecular-function and process terms (e.g. transporter activity, cell adhesion) are **not** supported for PP_2042. The laminin binding of PA3923 is a pathogen-specific observation and should not be transferred.

**Experiments that would resolve the function:**
- Separate outer and inner membranes on a sucrose gradient, or use surface proteolysis or labelling, to confirm outer-membrane, surface-exposed localisation.
- Compare ΔPP_2042, ΔPP_2043 and the double mutant for:
  - outer-membrane permeability, using detergent/SDS, bile and hydrophobic antibiotic sensitivity;
  - attachment and biofilm formation;
  - growth on hydrophobic carbon sources such as alkyl sulfates, fatty acids and aromatic compounds.
- Pull down PP_2043 to test whether it binds PP_2042 directly.
- Check RB-TnSeq fitness data for KT2440 on the Fitness Browser for conditions where PP_2042 and PP_2043 are cofit.

## 7. Confidence summary

| Claim | Evidence | Confidence |
|---|---|---|
| Secreted across the inner membrane (Sec signal peptide) | SignalP | High |
| Outer-membrane β-barrel | Pfam family description; homologue PA3923 is a surface laminin receptor | Moderate |
| Works with DUF1329 partner PP_2043 | Adjacent operon-like arrangement; Pfam; *Kangiella* cofitness | Moderate |
| Adhesin function | Homology to PA3923 only | Low |
| Lipid/saccharide export system with an MmpL | Pfam and Fitness Browser speculation; no MmpL at this locus | Low |
| Enzymatic activity or a specific substrate | None | Not supported |

## Sources
- UniProt Q88L93 flat file (local `genes/PSEPK/PP_2042/PP_2042-uniprot.txt`, entry version 89, 28 Jan 2026); genome papers Nelson et al. 2002 (PMID:12534463) and Belda et al. 2016 (PMID:26913973), sequence only
- InterPro/Pfam PF06980 (DUF1302): https://www.ebi.ac.uk/interpro/entry/pfam/PF06980
- NCBI CDD pfam06980: https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980
- KEGG gene entries ppu:PP_2039–PP_2045: https://www.kegg.jp/entry/ppu:PP_2042
- UniProt Q9HX90 (PA3923) and Q9HYI3 (PA3422): https://rest.uniprot.org/uniprotkb/Q9HX90
- Paulsson M. et al. (2019) "*Pseudomonas aeruginosa* uses multiple receptors for adherence to laminin during infection of the respiratory tract and skin wounds", *Sci Rep*: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6890786/
- University of Guelph MSc announcement on PA3923/PA3422: https://www.uoguelph.ca/mcb/system/files/J%20Manek%20MSC%20announcement.pdf
- Fitness Browser reannotations, *Kangiella aquimarina* DSM 16071: https://fitprivate.genomics.lbl.gov/cgi-bin/orgReanno.cgi?orgId=Kang
- Background on related hydrophobic-uptake outer-membrane channels, not the same family: [COG4313 channel structure, PMC4493636](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4493636/); [OprG structure, PMC2993939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2993939/)

## Citations

1. https://www.ebi.ac.uk/interpro/entry/pfam/PF06980
2. https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6890786/
4. https://www.uoguelph.ca/mcb/system/files/J%20Manek%20MSC%20announcement.pdf
5. https://fitprivate.genomics.lbl.gov/cgi-bin/orgReanno.cgi?orgId=Kang
6. https://www.kegg.jp/entry/ppu:PP_2042
7. https://rest.uniprot.org/uniprotkb/Q9HX90
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4493636/
9. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2993939/