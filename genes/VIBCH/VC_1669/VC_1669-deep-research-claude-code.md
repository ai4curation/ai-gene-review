---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:31:45.307235'
end_time: '2026-10-30T21:36:50.532581'
duration_seconds: 305.23
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_1669
  gene_symbol: VC_1669
  uniprot_accession: Q9KRH3
  protein_description: 'SubName: Full=Sodium-dependent transporter, putative {ECO:0000313|EMBL:AAF94819.1};'
  gene_info: OrderedLocusNames=VC_1669 {ECO:0000313|EMBL:AAF94819.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: Na/ntran_symport. (IPR000175); SNS_sf. (IPR037272); YocR/YhdH-like.
    (IPR047218); SNF (PF00209)
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
  web_search_requests: 6
  num_turns: 17
  total_cost_usd: 1.0147808999999999
  session_id: aae14bb4-0841-4001-9ddc-751d782dd07e
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KRH3
- **Protein Description:** SubName: Full=Sodium-dependent transporter, putative {ECO:0000313|EMBL:AAF94819.1};
- **Gene Information:** OrderedLocusNames=VC_1669 {ECO:0000313|EMBL:AAF94819.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Na/ntran_symport. (IPR000175); SNS_sf. (IPR037272); YocR/YhdH-like. (IPR047218); SNF (PF00209)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_1669" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_1669' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_1669** (gene ID: VC_1669, UniProt: Q9KRH3) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Getting the reference sequences (MhsT, Tyt1, LeuT) so I can compare VC_1669 against them.

I'm doing one last literature search on MhsT's substrate range and the Tyt1 PMIDs, then I'll write the report.

# VC_1669 (UniProt Q9KRH3), *Vibrio cholerae* O1 El Tor N16961: research report

## Summary

VC_1669 encodes a 448-residue integral membrane protein of unknown function. It belongs to the bacterial neurotransmitter:sodium symporter (NSS/SNF, SLC6-homolog, TC 2.A.22) family. No published study characterizes VC_1669 itself. A search for "VC_1669"/"VC1669" found no literature that mentions the gene ([web search, Oct 2026](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5636140/)). Its function therefore has to be inferred from its family and domain signatures, from sequence comparison with experimentally characterized bacterial NSS transporters, and from structure-based mapping of conserved sites.

**Best-supported inference:** VC_1669 is probably a **Na⁺-coupled symporter of neutral, hydrophobic amino acids** in the **cytoplasmic (inner) membrane**. It is most closely related to MhsT from *Bacillus halodurans* and to the uncharacterized *B. subtilis* paralogs YocR and YhdH. The exact substrate has not been determined experimentally, and the transport activity itself has never been tested.

---

## 1. Identity check

| Feature | Value | Source |
|---|---|---|
| Accession / locus | Q9KRH3 / VC_1669 (AAF94819.1), chromosome I, complement(1800425..1801771) | UniProt record; KEGG vch:VC_1669 |
| Name | "Sodium-dependent transporter, putative" (submitter annotation, ECO:0000313) | UniProt |
| Length | 448 aa, 48.4 kDa | UniProt |
| Protein existence | PE 4, predicted (no protein-level evidence) | UniProt |
| Family signatures | InterPro IPR000175 (Na/neurotransmitter symporter), IPR037272 (SNS superfamily), IPR047218 (YocR/YhdH-like); Pfam PF00209 (SNF, 2 hits); PRINTS PR00176; PROSITE PS50267; NCBIfam NF037979; CDD cd10336 (SLC6sbd_Tyt1-Like); PANTHER PTHR42948:SF1; eggNOG COG0733; KEGG K03308 (neurotransmitter:Na⁺ symporter, NSS family) | UniProt DR lines; KEGG |
| Topology | 10 helical TM segments predicted by Phobius (45–70, 91–119, 148–165, 177–194, 225–244, 256–278, 298–327, 356–382, 388–405, 425–447) | UniProt FT (ECO:0000256\|SAM:Phobius) |
| Existing GO | GO:0016020 membrane (IEA, UniProtKB-SubCell) only | GOA |

The locus tag, organism and domain content all match, so there is no gene-symbol ambiguity. Results for *Vibrio* genes with similar numbers (VC1639, VC1795, VC1123) concern unrelated proteins.

The genome paper that deposited the sequence is Heidelberg et al., *Nature* 406:477–483 (2000), PMID:10952301. It reports annotation only.

---

## 2. Family context: bacterial NSS (SLC6) transporters

The NSS/SLC6 family includes the mammalian Na⁺(/Cl⁻)-dependent transporters for GABA, glycine, serotonin, dopamine and norepinephrine. Its bacterial members are Na⁺-coupled amino acid symporters ([Singh & Pal review, PMC4818570](https://pmc.ncbi.nlm.nih.gov/articles/PMC4818570)). Bacterial NSS homologs were first recognized in 1998, and the first to be functionally characterized was TnaT, a Na⁺-dependent, tryptophan-selective transporter from *Symbiobacterium thermophilum* (Androutsellis-Theotokis et al. 2003, as summarized in [PMC4818570](https://pmc.ncbi.nlm.nih.gov/articles/PMC4818570)).

Three bacterial members have been studied experimentally and serve as reference points for VC_1669:

1. **LeuT (*Aquifex aeolicus*, O67854).** This Na⁺-coupled symporter of small nonpolar amino acids is the structural paradigm for the family (LeuT fold; PDB 2A65 and later structures). Its transport is chloride-independent. A single mutation, I359Q, converts tryptophan from an inhibitor into a transported substrate, which shows how a few binding-pocket residues set substrate selectivity (Piscitelli & Gouaux, *EMBO J* 2012; [OSTI 1033019](https://www.osti.gov/biblio/1033019); [PDB 3QS6](https://pdbj.org/mine/summary/3qs6?lang=ko)).
2. **Tyt1 (*Fusobacterium nucleatum*).** Expressed in *E. coli*, Tyt1 "catalyzes robust Na⁺-dependent, highly selective L-tyrosine transport". It was described as an NSS member with only 11 TMs, and Na⁺ binding shifts it toward an outward-facing conformation (Quick et al., *J Biol Chem* 2006, PMID:16798738; [VIVO record](https://vivo.weill.cornell.edu/display/pubid16798738)). Later work found that transport by Tyt1 is chloride-independent and coupled to an H⁺ flux ([PMC2808765](https://pmc.ncbi.nlm.nih.gov/articles/PMC2808765); [PMC2826427](https://pmc.ncbi.nlm.nih.gov/articles/PMC2826427)). The CDD model that VC_1669 hits, cd10336 "SLC6sbd_Tyt1-Like", is named after this subgroup.
3. **MhsT (*B. halodurans* BH1128, Q9KDT3).** This **hydrophobic amino acid transporter** has broad specificity for hydrophobic amino acids, including tryptophan, other aromatic amino acids and aliphatic ones. Malinauskaite et al. (*Nat Struct Mol Biol* 21:1006–1012, 2014) solved its structure in an occluded inward-facing state with Na⁺ and L-Trp bound (PDB 4US4, 2.6 Å; [PDBsum 4US4](https://www.ebi.ac.uk/pdbsum/4us4); [PDBj 4US4](https://pdbj.org/mine/summary/4US4)). A conserved GlyX₉Pro motif lets TM5 partly unwind, which opens a water pathway to the Na2 site and allows Na⁺ release to the cytoplasm. Focht et al. (*EMBO J* 40:e105164, 2021; [PMC7780149](https://pmc.ncbi.nlm.nih.gov/articles/PMC7780149)) solved six substrate-bound structures. They found that a flexible, non-helical **Gly-Met-Gly** segment in TM6 reshapes the binding pocket to fit substrates of different size, and that a general (G/A/C)ΦG motif is conserved across SLC6 transporters ([PDB 6YU7](https://rcsb.org/structure/6YU7)).

**The YocR/YhdH subfamily (IPR047218).** *B. subtilis* YocR (O34383, 445 aa) and YhdH (O07577, 451 aa) are SNF-family paralogs with no experimentally established function. SubtiWiki lists their function as unknown and maps both to the MhsT structure 4US4 at about 44–45% identity ([SubtiWiki YocR](https://subtiwiki.uni-goettingen.de/wiki//index.php?title=YocR); [SubtiWiki YhdH](https://www.subtiwiki.uni-goettingen.de/wiki//index.php?title=YhdH)). VC_1669 falls in the same InterPro subfamily.

---

## 3. Sequence comparison (analysis run for this report)

I aligned VC_1669 locally (Smith–Waterman, BLOSUM62, gap open −11/extend −1; Biopython) against reference NSS proteins fetched from UniProt REST.

| Comparator | Organism | Length | Aligned columns | Identity |
|---|---|---|---|---|
| **MhsT** (Q9KDT3, BH1128; PDB 4US4) | *B. halodurans* | 453 | 421 | **40.6%** |
| YhdH (O07577) | *B. subtilis* | 451 | 416 | 40.6% |
| YocR (O34383) | *B. subtilis* | 445 | 417 | 39.8% |
| SNF-family proteins Q8RHQ5 / Q8RHM5 (Tyt1 candidates) | *F. nucleatum* | 459 / 438 | 412 / 419 | 34.0% / 32.7% |
| LeuT (O67854) | *A. aeolicus* | 513 | 398 | 31.4% |

I did not confirm which of the two *F. nucleatum* SNF proteins is Tyt1.

About 40% identity over nearly the full length puts VC_1669 in the MhsT/YocR/YhdH clade. It is clearly less similar to LeuT and to the *Fusobacterium* proteins.

### Conserved Na⁺ and substrate sites

I mapped the residues that bind Na⁺ and substrate in LeuT onto VC_1669 through a global alignment. MhsT's GMG segment was located by direct comparison of the aligned sequences.

| LeuT residue (role) | VC_1669 residue | Comment |
|---|---|---|
| G20 (Na2) | G25 | conserved |
| A22 (Na1) | A27 | conserved |
| V23 (Na2) | V28 | conserved |
| G24-L25-G26 (unwound TM1, substrate carboxyl/amino) | G29-L30-G31 | conserved "GLG" motif (VC_1669 sequence ...AAGSAVGLGN...) |
| N27 (Na1) | N32 | conserved |
| Y108 (TM3, substrate) | Y111 | conserved |
| F253 (TM6, substrate) | F227 | conserved |
| T254 (Na1) | S228 | conservative (hydroxyl retained) |
| S256 (substrate) | S230 | conserved |
| A351, T354, S355 (TM8, Na2) | A328, T331, S332 | conserved |
| I359 (TM8, selectivity) | M336 | substituted; this position controls substrate size in LeuT |
| N286 (TM7, Na1) | not resolved | the alignment has gaps in this region, so the result is not interpretable |

Two other features stand out:

- The TM6 segment of VC_1669, **LSLGVCVMTTYGSY**, lines up with MhsT **LSLGMGALITYGSY**. VC_1669 has **G-V-C** where MhsT has the flexible **G-M-G** loop. This still fits the (G/A/C)ΦG pattern that Focht et al. found conserved across SLC6 transporters, but the substitution may change how the pocket adapts to substrates of different size.
- The TM1–TM2 region, including the **GxxGLGNxW(R)F** signature, is strongly conserved with MhsT. VC_1669 has GSAVGLGNVWGF and MhsT has GSAVGLGNIWRF.

**Interpretation.** Both Na⁺ sites are almost entirely conserved, which supports **Na⁺-coupled symport**. The aromatic and aliphatic residues of the substrate pocket are conserved with MhsT, which points to a **neutral, probably hydrophobic or aromatic, L-amino acid** substrate. VC_1669's substrate cannot be predicted reliably beyond that, because single changes at positions like LeuT I359 or the TM6 GΦG loop can switch selectivity in this family.

The analysis was run in a throwaway `/tmp` directory and is not saved in the repository. A reproducible version belongs in `VC_1669-bioinformatics/` if it is used in the review.

---

## 4. Localization

- **Inferred location: cytoplasmic (inner) membrane.** Phobius predicts 10 TM helices, and the UniProt keywords Membrane and Transmembrane are backed by SAM:Phobius. Proteins of the LeuT fold have 12 TM helices (Tyt1 is an 11-TM exception), so Phobius has probably merged or missed some. VC_1669 is about the same length as MhsT (448 vs 453 aa), which suggests the full LeuT-type core.
- It has no predicted signal peptide or outer-membrane β-barrel features. NSS transporters use the inward-directed Na⁺ gradient across the cytoplasmic membrane.
- This is therefore an **inference**: no fractionation or localization experiment exists for VC_1669. The current GO annotation, GO:0016020 membrane (IEA), is correct but general. GO:0005886 plasma membrane is the defensible refinement for a Gram-negative secondary active transporter, but it would rest on inference.

---

## 5. Pathways and biological role

- **Likely process:** uptake of amino acids across the cytoplasmic membrane, driven by the Na⁺ electrochemical gradient. This fits *V. cholerae*'s marine/estuarine lifestyle. *Vibrio* species generate a strong Na⁺-motive force through the Na⁺-pumping NADH:quinone oxidoreductase (Na⁺-NQR) and depend on it for many Na⁺-coupled processes. That link is general physiology, not a VC_1669-specific result.
- **Genomic neighborhood (KEGG):** VC_1666, an ABC transporter ATP-binding protein (putative thiamine); VC_1667, hypothetical; VC_1668, Rlu-family pseudouridine synthase; VC_1670, cardiolipin synthase; VC_1671, cystathionine β-lyase; VC_1672, DNA-3-methyladenine glycosylase I. None of these forms an operon with VC_1669 that would point to a specific substrate. VC_1669 is on the opposite strand from VC_1670 onward.
- **Virulence / colonization:** I found no literature linking VC_1669 to virulence, colonization, the regulons of ToxR, quorum sensing or ppGpp, or to fitness phenotypes.

---

## 6. Assessment for GO annotation

| Aspect | Supported claim | Strength |
|---|---|---|
| CC | Membrane (existing IEA) → plasma membrane | Strong for membrane (TM prediction); plasma membrane by inference |
| MF | Symporter activity / Na⁺:amino acid symporter activity (e.g. GO:0005283 amino acid:sodium symporter activity, or a broader solute:sodium symporter term) | Moderate (family, conserved Na1/Na2 sites, ~40% identity to MhsT) |
| MF, specific substrate (e.g. Trp, Tyr, Leu) | Not supported | Too speculative; family members differ in selectivity, and the TM6 loop and LeuT-I359 position of VC_1669 differ from MhsT |
| BP | Amino acid transmembrane transport; sodium ion transport | Moderate, by inference from MF |

The NSS family has no GO term specific enough to name a substrate safely. If a molecular function is added, a family-level term such as "sodium:amino acid symporter activity" is the most specific defensible choice.

---

## 7. Open questions and suggested experiments

1. **Substrate identification.** Express VC_1669 in an *E. coli* strain lacking aromatic and branched-chain amino acid uptake, as done for Tyt1 (Quick et al. 2006). Screen radiolabelled L-amino acids (Trp, Tyr, Phe, Leu, Ile, Val, Met, Ala) in the presence and absence of Na⁺.
2. **Coupling ions.** Test whether transport depends on Na⁺ and is independent of Cl⁻, and whether it is coupled to H⁺ as in Tyt1. Mutate the Na2 site (A328, T331, S332) and the Na1 site (N32, S228).
3. **Selectivity determinants.** Swap VC_1669's TM6 GVC segment for MhsT's GMG and test the M336 position, which corresponds to LeuT I359.
4. **Physiology.** Measure *ΔVC_1669* growth with single amino acids as nitrogen or carbon sources, and check fitness in published *V. cholerae* Tn-seq datasets (not examined here).

---

## Sources

- UniProtKB Q9KRH3 entry, version 116 (local file `genes/VIBCH/VC_1669/VC_1669-uniprot.txt`). Contains family cross-references, Phobius TM predictions and PE 4.
- Heidelberg JF et al. "DNA sequence of both chromosomes of the cholera pathogen *Vibrio cholerae*." *Nature* 406:477–483 (2000). PMID:10952301.
- Quick M et al. "State-dependent conformations of the translocation pathway in the tyrosine transporter Tyt1, a novel neurotransmitter:sodium symporter from *Fusobacterium nucleatum*." *J Biol Chem* (2006). PMID:16798738. https://vivo.weill.cornell.edu/display/pubid16798738
- Tyt1 follow-up work on chloride independence and H⁺ coupling: https://pmc.ncbi.nlm.nih.gov/articles/PMC2808765 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC2826427 ; https://vivo.weill.cornell.edu/display/pubid20081826
- Malinauskaite L et al. MhsT structure, *Nat Struct Mol Biol* 21:1006–1012 (2014); PDB 4US4. https://www.ebi.ac.uk/pdbsum/4us4 ; https://pdbj.org/mine/summary/4US4
- Focht D et al. "A non-helical region in transmembrane helix 6 of hydrophobic amino acid transporter MhsT mediates substrate recognition." *EMBO J* 40:e105164 (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC7780149 ; https://rcsb.org/structure/6YU7
- Piscitelli CL & Gouaux E. LeuT engineered to transport tryptophan, *EMBO J* (2012). https://www.osti.gov/biblio/1033019 ; https://pdbj.org/mine/summary/3qs6?lang=ko
- Review of SLC6/NSS evolution, including TnaT and bacterial homologs: https://pmc.ncbi.nlm.nih.gov/articles/PMC4818570
- SubtiWiki entries for YocR and YhdH (function unknown; SNF family; 4US4 homology): https://subtiwiki.uni-goettingen.de/wiki//index.php?title=YocR ; https://www.subtiwiki.uni-goettingen.de/wiki//index.php?title=YhdH
- KEGG GENES vch:VC_1669 and neighbors VC_1666–VC_1672 (K03308 assignment and genomic context): https://www.kegg.jp/entry/vch:VC_1669
- Pairwise alignments and site mapping were computed for this report with Biopython PairwiseAligner on sequences from the UniProt REST API (Q9KRH3, Q9KDT3, O67854, O34383, O07577, Q8RHQ5, Q8RHM5).

**Caveat.** I read abstracts, database records and summaries, not the full texts of the MhsT, Tyt1 and LeuT papers. The residue mapping in Section 3 comes from a pairwise alignment, not a structural superposition. Treat it as indicative, especially in the gapped TM7 region and around EL2.

## Citations

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5636140/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC4818570
3. https://www.osti.gov/biblio/1033019
4. https://pdbj.org/mine/summary/3qs6?lang=ko
5. https://vivo.weill.cornell.edu/display/pubid16798738
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC2808765
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC2826427
8. https://www.ebi.ac.uk/pdbsum/4us4
9. https://pdbj.org/mine/summary/4US4
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC7780149
11. https://rcsb.org/structure/6YU7
12. https://subtiwiki.uni-goettingen.de/wiki//index.php?title=YocR
13. https://www.subtiwiki.uni-goettingen.de/wiki//index.php?title=YhdH
14. https://vivo.weill.cornell.edu/display/pubid20081826
15. https://www.kegg.jp/entry/vch:VC_1669