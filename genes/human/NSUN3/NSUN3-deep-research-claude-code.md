---
provider: claude_code
model: claude-sonnet-5-5
cached: true
start_time: '2026-10-14T23:21:36.796111'
end_time: '2026-10-14T23:21:36.798509'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: NSUN3
  gene_symbol: NSUN3
  uniprot_accession: Q9H649
  protein_description: 'RecName: Full=tRNA (cytosine(34)-C(5))-methyltransferase,
    mitochondrial; EC=2.1.1.- {ECO:0000269|PubMed:27214402, ECO:0000269|PubMed:27356879,
    ECO:0000269|PubMed:27497299}; AltName: Full=NOL1/NOP2/Sun domain family member
    3 {ECO:0000312|HGNC:HGNC:26208};'
  gene_info: Name=NSUN3 {ECO:0000312|HGNC:HGNC:26208}; ORFNames=MSTP077 {ECO:0000303|Ref.2},
    UG0651E06 {ECO:0000303|Ref.4};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the class I-like SAM-binding methyltransferase
  protein_domains: MeTrfase_RsmB-F_NOP2_cat. (IPR049560); MeTrfase_RsmB-F_NOP2_dom.
    (IPR001678); RCMT. (IPR023267); SAM-dependent_MTases_sf. (IPR029063); Methyltr_RsmB-F
    (PF01189)
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
  - claude-sonnet-5-5
  num_turns: 1
  total_cost_usd: 0.17021219999999998
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9H649
- **Protein Description:** RecName: Full=tRNA (cytosine(34)-C(5))-methyltransferase, mitochondrial; EC=2.1.1.- {ECO:0000269|PubMed:27214402, ECO:0000269|PubMed:27356879, ECO:0000269|PubMed:27497299}; AltName: Full=NOL1/NOP2/Sun domain family member 3 {ECO:0000312|HGNC:HGNC:26208};
- **Gene Information:** Name=NSUN3 {ECO:0000312|HGNC:HGNC:26208}; ORFNames=MSTP077 {ECO:0000303|Ref.2}, UG0651E06 {ECO:0000303|Ref.4};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the class I-like SAM-binding methyltransferase
- **Key Domains:** MeTrfase_RsmB-F_NOP2_cat. (IPR049560); MeTrfase_RsmB-F_NOP2_dom. (IPR001678); RCMT. (IPR023267); SAM-dependent_MTases_sf. (IPR029063); Methyltr_RsmB-F (PF01189)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NSUN3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NSUN3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NSUN3** (gene ID: NSUN3, UniProt: Q9H649) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# NSUN3 (Q9H649), human mitochondrial tRNA (cytosine-34-C5)-methyltransferase: research report

**Provenance note.** I wrote this from memory of the primary literature. I did not run live searches or fetch the papers in this session. PMIDs are the ones I am confident of, and the three core papers (PMID:27214402, 27356879, 27497299) match the UniProt evidence codes in the record supplied. Check every quotation and citation against `publications/PMID_*.md` before using them as `supporting_text`. Items I could not pin down are marked "unverified".

## 1. Identity check

The symbol NSUN3 (HGNC:26208, "NOL1/NOP2/Sun domain family member 3") matches the supplied UniProt record. The record describes a class I-like SAM-binding methyltransferase of the NOP2/Sun (RsmB/F-type) family. It carries the InterPro RsmB-F/NOP2 catalytic domain (IPR049560) and the RCMT signature (IPR023267, RNA cytosine-C5-methyltransferase), and Pfam PF01189. The literature below concerns this same human mitochondrial enzyme, so the gene symbol is not ambiguous.

## 2. Primary function

NSUN3 is a **mitochondrial RNA m5C methyltransferase with a single well-established substrate: cytosine 34 (C34) of mitochondrial tRNA-Met (mt-tRNA^Met).**

- **Position and target.** C34 is the wobble (first anticodon) position of the CAU anticodon of mt-tRNA^Met. NSUN3 transfers a methyl group from S-adenosyl-L-methionine (SAM) to C5 of this cytosine, giving 5-methylcytidine (m5C34) and S-adenosyl-homocysteine.
- **Reaction.** SAM + cytidine-34 in mt-tRNA^Met → S-adenosyl-L-homocysteine + 5-methylcytidine-34 in mt-tRNA^Met. This is the tRNA (cytosine-5-)-methyltransferase activity class (GO:0016428), applied to mitochondrial tRNA.
- **Downstream modification.** m5C34 is not the end product.
  - The Fe(II)/2-oxoglutarate-dependent dioxygenase ALKBH1 (ABH1) oxidizes m5C34 to 5-hydroxymethylcytidine (hm5C) and then to **5-formylcytidine (f5C34)**.
  - f5C34 is the mature modification in mammalian mitochondria.
  - NSUN3 therefore acts first in a two-enzyme pathway (NSUN3 → ALKBH1).
- **Physiological role.** Human mitochondria decode AUA (and AUU) as well as the standard AUG as methionine, using a single tRNA^Met. The f5C34 wobble modification lets mt-tRNA^Met read AUG and AUA, so it expands codon recognition. Without it, mitochondrial translation of AUA-containing mRNAs is impaired. The tRNA^Met is also used for initiation, and the modification is needed for efficient mitochondrial protein synthesis overall.

### Key experimental evidence

1. **Nakano et al., Nat Chem Biol 2016, PMID:27214402.** The paper is titled "NSun3 methyltransferase catalyzes 5-formylcytidine modification of mitochondrial tRNAMet via 5-methylcytidine".
   - It identified NSUN3 as the enzyme that installs the m5C intermediate on mt-tRNA^Met at position 34.
   - It showed that the f5C34 modification is generated via m5C.
   - Knockdown reduced f5C and impaired mitochondrial translation. Recombinant enzyme methylated mt-tRNA^Met in vitro.
2. **Haag et al., EMBO J 2016, PMID:27497299.** The paper is titled "NSUN3 and ABH1 modify the wobble position of mt-tRNAMet to expand codon recognition in mitochondrial translation".
   - NSUN3 is localized to mitochondria.
   - It methylates C34 of mt-tRNA^Met, and ABH1 subsequently converts the m5C to f5C.
   - Loss of the modification impaired mitochondrial translation.
   - In vitro, NSUN3 is selective for mt-tRNA^Met, and the modified tRNA is needed for decoding AUA codons.
3. **Van Haute et al., Nat Commun 2016, PMID:27356879.** The paper is titled "Mutations in NSUN3 cause combined oxidative phosphorylation deficiency and mitochondrial disease".
   - A patient with a homozygous or compound-heterozygous loss-of-function NSUN3 variant had early-onset mitochondrial disease: combined OXPHOS deficiency, developmental delay and neurological features.
   - Patient cells lacked m5C34 and f5C34 in mt-tRNA^Met and showed reduced mitochondrial translation.
   - Re-expression of wild-type NSUN3 rescued the defect.
   - This is the key human-genetics evidence that the activity is physiologically required.
4. **Kawarada et al., Nucleic Acids Res 2017, PMID:28531326.** This paper is titled "ALKBH1 is an RNA dioxygenase responsible for cytoplasmic and mitochondrial tRNA modifications". It confirms the downstream ALKBH1 step and the m5C → f5C route.
5. **Delaunay et al., Nature 2022, PMID:35768510.** The paper is titled "Mitochondrial RNA modifications shape metabolic plasticity in metastasis".
   - In head and neck squamous cell carcinoma models, NSUN3/ALKBH1 and f5C34 in mt-tRNA^Met support mitochondrial translation and the metabolic plasticity needed for invasion and metastasis.
   - Loss of NSUN3 reduced invasive and metastatic capacity.
6. **Mouse embryonic stem cells (Trixl et al., Cell Mol Life Sci, about 2018; PMID not verified).** Nsun3 depletion lowered mitochondrial activity and impaired differentiation. This supports a broader developmental dependence on mitochondrial function rather than a separate function of the protein.

## 3. Substrate specificity

- **Substrate.** It is highly specific for mt-tRNA^Met (mt-tRNA-Met, encoded by MT-TM). The target is C34 in the anticodon loop.
- **Other RNAs.** I am not aware of strong evidence that NSUN3 methylates other mt-tRNAs or rRNAs.
- **Division of labor among human m5C methyltransferases.**
  - NSUN2 methylates cytosolic tRNAs and other nuclear-encoded RNAs.
  - NSUN4 methylates mt-rRNA (12S) and also acts as a ribosome-assembly cofactor with MTERF4.
  - NSUN3 is the dedicated mt-tRNA^Met wobble enzyme.
- **Mechanism.** NSUN3 follows the canonical RNA m5C methyltransferase mechanism:
  - SAM-binding Rossmann-like fold;
  - a catalytic cysteine that forms a transient covalent bond at C6 of the target cytosine;
  - a second conserved cysteine that releases the product.

  Haag et al. used catalytic-dead mutants to show that activity is needed for function. I could not verify the exact residue numbers. I know of no experimental human NSUN3 structure, so the mechanism is inferred from NOP2/Sun family structures.

## 4. Localization

- **Where it acts.** NSUN3 acts in the mitochondrial matrix, where mt-tRNA^Met is transcribed and processed from the mtDNA polycistronic transcript. Mitochondrial import and localization were shown by Haag et al. (PMID:27497299) and Nakano et al. (PMID:27214402). The product is an N-terminal mitochondrial-targeted protein.
- **Other compartments.** I know of no robust evidence for a cytosolic or nuclear function.

## 5. Pathway context

1. mtDNA transcription and processing releases mt-tRNA^Met.
2. NSUN3 forms m5C34 (SAM-dependent).
3. ALKBH1 (Fe²⁺/2-OG, O₂) oxidizes m5C34 to hm5C34 and then f5C34.
4. Mature mt-tRNA^Met decodes AUG and AUA during initiation and elongation.
5. Mitochondrial translation then produces the 13 mtDNA-encoded OXPHOS subunits.
6. OXPHOS function (complexes I, III, IV and V) is maintained.

NSUN3 is therefore part of mitochondrial tRNA modification and mitochondrial translation, not a signaling pathway.

## 6. Disease relevance

- **Mitochondrial disease.** Biallelic NSUN3 loss of function causes combined OXPHOS deficiency with a neurodevelopmental/Leigh-like presentation (PMID:27356879).
- **Cancer.** NSUN3/f5C34 supports metastatic metabolic reprogramming in some tumors (PMID:35768510).

## 7. Suggested GO-style interpretation (for the review)

These are my proposals, based on the evidence above. They are not drawn from the GOA file, which I did not open.

| Aspect | Suggested term | Basis |
|---|---|---|
| Molecular function | tRNA (cytosine-5-)-methyltransferase activity (GO:0016428), or a mitochondrial-tRNA-specific child term | Direct enzymology (PMID:27214402, 27497299) |
| Biological process | tRNA C5-cytosine methylation (GO:0002101) | Same |
| Biological process | Mitochondrial tRNA methylation / modification (for example GO:0070131 or a related term) | Same |
| Biological process | Mitochondrial translation | Loss-of-function phenotype, but this is a downstream effect |
| Cellular component | Mitochondrion / mitochondrial matrix | PMID:27497299 |

The actual GO ids should be confirmed in OLS or QuickGO before they go into `core_functions`. Two cautions follow from the project guidelines.

- Annotate "mitochondrial translation" only if the term's definition fits an enzyme that modifies a tRNA. This is a tRNA-modification enzyme, and the evidence shows it is necessary for translation, not that it performs translation steps itself.
- Avoid generic "RNA binding" or "protein binding" annotations.

## 8. Open questions and suggested experiments

- Does NSUN3 methylate any non-tRNA mitochondrial RNA, for example through miCLIP or bisulfite sequencing in knockout cells?
- What is the structural basis for selecting mt-tRNA^Met over the other 21 mt-tRNAs? A cryo-EM or crystal structure of NSUN3 bound to the tRNA would address this.
- How is the NSUN3 to ALKBH1 handoff coordinated, and is it regulated by SAM, O₂, 2-oxoglutarate or Fe availability?
- What is the quantitative contribution of m5C versus f5C to AUA decoding? Ribosome profiling of NSUN3-null cells would help.

## 9. Key references

- Nakano S, et al. Nat Chem Biol 2016. PMID:27214402.
- Haag S, et al. EMBO J 2016. PMID:27497299.
- Van Haute L, et al. Nat Commun 2016. PMID:27356879.
- Kawarada L, et al. Nucleic Acids Res 2017. PMID:28531326.
- Delaunay S, et al. Nature 2022. PMID:35768510.
- UniProt Q9H649 (NSUN3_HUMAN), which supports the family and domain classification.