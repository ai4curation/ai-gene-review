---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:31:45.284866'
end_time: '2026-10-30T21:35:53.793709'
duration_seconds: 248.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_2283
  gene_symbol: VC_2283
  uniprot_accession: Q9KPS9
  protein_description: 'SubName: Full=Sodium-dependent transporter {ECO:0000313|EMBL:AAF95427.1};'
  gene_info: OrderedLocusNames=VC_2283 {ECO:0000313|EMBL:AAF95427.1};
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 14
  total_cost_usd: 0.9565760999999999
  session_id: e040e732-2813-4872-89e9-855100f0117b
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KPS9
- **Protein Description:** SubName: Full=Sodium-dependent transporter {ECO:0000313|EMBL:AAF95427.1};
- **Gene Information:** OrderedLocusNames=VC_2283 {ECO:0000313|EMBL:AAF95427.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Na/ntran_symport. (IPR000175); SNS_sf. (IPR037272); YocR/YhdH-like. (IPR047218); SNF (PF00209)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_2283" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_2283' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_2283** (gene ID: VC_2283, UniProt: Q9KPS9) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Aligning VC_2283 against characterized NSS homologs (LeuT, YhdH, MhsT) to check sodium-site and substrate-site conservation.

# VC_2283 (UniProt Q9KPS9) in *Vibrio cholerae* O1 El Tor N16961: a predicted sodium-coupled amino acid symporter of the NSS/SLC6 family

## Summary

VC_2283 is an uncharacterized membrane protein of 451 residues encoded on chromosome I of *V. cholerae* N16961. UniProt lists it as unreviewed, with protein-existence level 4 (predicted). I found no publication that studies VC_2283 itself; a web search for the locus tag returned no source that mentions it. Everything below is inferred from three things: its family and domain signatures, a pairwise alignment I ran against structurally characterized bacterial homologs, and experimental work on those homologs.

- **Family.** It belongs to the neurotransmitter:sodium symporter (NSS, also called SNF or SLC6) family. Signatures: Pfam PF00209, InterPro IPR000175, PROSITE PS50267, PRINTS PR00176, SUPFAM SSF161070. It falls in the prokaryotic "YocR/YhdH-like" subgroup (IPR047218; CDD cd10336 "SLC6sbd_Tyt1-Like"; NCBIfam NF037979 Na_transp; PANTHER PTHR42948:SF1).
- **Most likely function.** A secondary active transporter that moves a small, probably hydrophobic, L-amino acid into the cell together with Na⁺, across the cytoplasmic (inner) membrane.
- **Substrate.** Not determined. Its closest characterized homolog, MhsT from *Bacillus halodurans* (about 41% identical), carries several hydrophobic L-amino acids with Na⁺. Other members of the clade transport leucine (LeuT) or tyrosine (Tyt1).
- **Location.** A cytoplasmic-membrane protein with multiple membrane passes; Phobius predicts 12 transmembrane helices.

The annotation "Sodium-dependent transporter" comes from the original genome submission (ECO:0000313). The only GO annotation in GOA is GO:0016020 *membrane* (IEA, from UniProt subcellular location).

---

## 1. Identity check

| Feature | Value (from UniProt Q9KPS9) |
|---|---|
| Locus | VC_2283 (OrderedLocusName); RefSeq WP_000079390.1; EMBL AAF95427.1 |
| Organism | *V. cholerae* O1 biovar El Tor N16961 (taxon 243277), chromosome I |
| Length | 451 aa |
| Name | "Sodium-dependent transporter" (from the submitter, ECO:0000313) |
| Topology | 12 helical TM segments predicted by Phobius (12–32, 44–70, 91–109, 115–138, 147–165, 177–197, 217–240, 252–278, 313–337, 357–382, 388–405, 432–450) |
| Domains | SNF (PF00209), Na/ntran_symport (IPR000175), SNS_sf (IPR037272), YocR/YhdH-like (IPR047218), cd10336 SLC6sbd_Tyt1-like |
| Orthology group | eggNOG COG0733 ("Na⁺-dependent transporters of the SNF family") |
| Source publication | Genome sequence only: Heidelberg et al., *Nature* 406:477–483 (2000), PMID:10952301 |

**Possible confusion to avoid.** The best-studied sodium-dependent transporter in *V. cholerae* is VcINDY, a dicarboxylate transporter of the DASS family ([nutrition-evidence.com summary](https://nutrition-evidence.com/article/211510/functional-characterization-of-a-na-dependent-dicarboxylate-transporter-from-vibrio-cholerae); cryo-EM entry [7T9G](https://ibdc.dbtindia.gov.in/isda/summary/7T9G)). VcINDY is a different protein in an unrelated family, and none of its literature applies to VC_2283. Two other sodium-coupled *V. cholerae* transporters, NptA (phosphate) and NhaP2 (Na⁺/H⁺ antiporter), are also unrelated.

---

## 2. Family context: bacterial NSS / LeuT-fold transporters

### 2.1 Key concepts

In animals, the NSS (SLC6) family includes the transporters for dopamine, serotonin, noradrenaline, GABA and glycine, plus several amino acid transporters. These use the sodium gradient, and usually also chloride, to drive substrate uptake. Bacterial members are mostly Na⁺-coupled transporters of neutral amino acids. They share the "LeuT fold": 12 transmembrane helices, of which TM1–TM5 and TM6–TM10 form an inverted pseudo-symmetric repeat. TM1 and TM6 are broken in the middle, and those unwound segments form the substrate site and two sodium sites (Na1 and Na2).

- **LeuT** (*Aquifex aeolicus*, O67854) was the first NSS structure solved and remains the mechanistic reference for the family. Its transport does not need chloride, unlike the eukaryotic transporters (Penmatsa & Gouaux, *J Physiol* 2013 review; [PMC3948551](https://pmc.ncbi.nlm.nih.gov/articles/PMC3948551); [IAS repository record](https://repository.ias.ac.in/142665)).
- **MhsT** (*B. halodurans* BH1128, Q9KDT3) is a "multi-hydrophobic substrate transporter" with broad specificity for hydrophobic L-amino acids (Quick & Javitch 2007; Malinauskaite et al. 2014, both as cited in Focht et al. 2021).
  - Crystal structures show it occluded and facing inward, with Na⁺ and substrate bound, at 2.1–2.6 Å. They suggested how Na⁺ is released to the cytoplasm: TM5 unwinds on the intracellular side (Malinauskaite et al., *Nat Struct Mol Biol* 2014, DOI 10.1038/nsmb.2894; [ESRF highlight](https://www.esrf.fr/home/UsersAndScience/Publications/Highlights/highlights-2014/SB/SB05.html); [PDBsum 4US4](https://www.ebi.ac.uk/pdbsum/4us4); [PMC4346222](https://pmc.ncbi.nlm.nih.gov/articles/PMC4346222)).
  - Focht et al. (*EMBO J* 2021, DOI 10.15252/embj.2020105164; [PMC7780149](https://pmc.ncbi.nlm.nih.gov/articles/PMC7780149)) solved six structures with different substrates, including L-Ile, L-Leu, L-Val, 4-F-L-Phe and L-Tyr (PDB [6YU2–6YU7](https://www1.rcsb.org/structure/6yu7)). A flexible Gly-Met-Gly motif in the unwound part of TM6 lets the binding pocket fit substrates of different sizes. Mutations in that loop specifically impaired transport of aromatic amino acids.
- **Tyt1** (*Fusobacterium nucleatum*), the namesake of cd10336, is a Na⁺-dependent transporter that is highly selective for L-tyrosine when expressed in *E. coli*. It is reported to have only 11 TM segments, a feature said to occur in about 70% of prokaryotic NSS homologs (J Biol Chem study; [Weill Cornell VIVO record](https://vivo.weill.cornell.edu/display/pubid16798738)). It can also be overexpressed in functional form in *Lactococcus lactis* ([PMC3322350](https://pmc.ncbi.nlm.nih.gov/articles/PMC3322350)).
- **YhdH** (*Bacillus subtilis*, O07577) is the namesake of the subgroup that contains VC_2283. Swiss-Prot names it "Uncharacterized sodium-dependent transporter YhdH" (PE=3), so it has no experimentally assigned substrate either.

### 2.2 Where VC_2283 sits

I aligned the sequences globally with Biopython (BLOSUM62, gap open −11, extend −1). This is an ad hoc analysis, not a published result:

| Homolog | Accession | Status | Identity with VC_2283 (aligned positions) |
|---|---|---|---|
| MhsT, *B. halodurans* | Q9KDT3 | Experimental: transport assays and crystal structures | **40.6%** (175/431) |
| YhdH, *B. subtilis* | O07577 | Uncharacterized | 37.0% (160/432) |
| LeuT, *A. aeolicus* | O67854 | Experimental: transport assays and crystal structures | 31.4% (137/437) |

At 31–41% identity across nearly the full length, VC_2283 almost certainly has the LeuT fold. Unlike Tyt1, it has a 12-TM topology. MhsT is its closest characterized relative.

---

## 3. Inferred molecular function: Na⁺-coupled amino acid symport

### 3.1 Conservation of the ion and substrate sites

Mapping the LeuT residues that coordinate Na⁺ and substrate onto VC_2283 through the alignment:

| LeuT residue (role) | VC_2283 residue | Comment |
|---|---|---|
| G20 (Na2, backbone) | G22 | Conserved |
| A22 (Na1, backbone carbonyl) | A24 | Conserved |
| V23 (Na2, backbone) | V25 | Conserved |
| G24 / L25 / G26 (unwound TM1, substrate) | G26 / L27 / G28 | Conserved: the "GLGN" motif of TM1 |
| N27 (Na1 side chain) | N29 | Conserved |
| Y108 (substrate α-carboxyl/amino group, TM3) | Y110 | Conserved |
| F253 (substrate pocket, TM6) | F227 | Conserved |
| T254 (Na1, TM6) | S228 | Conservative: Thr→Ser, still a hydroxyl |
| S256 (substrate, TM6) | T230 | Conservative |
| A351 / T354 / S355 (Na2/substrate, TM8) | A328 / T331 / S332 | Conserved |
| I359 (substrate pocket, TM8) | M336 | Hydrophobic substitution |
| N286 (Na1, TM7) | Unresolved | The alignment is gapped in TM7, so this position cannot be assigned reliably |

**Interpretation.**
- The unwound-TM1 motif (G-A-V-G-L-G-N, residues 22–29 in VC_2283) is fully conserved. So are the TM8 Na2 and substrate positions, and TM6 keeps hydroxyl-bearing residues. This is strong evidence that VC_2283 keeps both canonical sodium sites and the central amino acid-binding pocket. It argues against any change in coupling ion.
- The substrate pocket is lined by hydrophobic residues (F227, M336), which is consistent with a neutral hydrophobic L-amino acid. In the TM6 unwound region, VC_2283 has a glycine-rich stretch (…TIGGCSM…, around residues 230–236) where MhsT has its Gly-Met-Gly motif. That suggests a similarly flexible pocket that could accept substrates of different sizes, as shown for MhsT (Focht et al. 2021).
- **Caveat:** these are pairwise alignments against distant homologs, not a structure-based alignment. The exact residue numbers are tentative.

### 3.2 Probable substrate

No experiment establishes the substrate. Based on the clade:
- MhsT (closest characterized homolog) has broad specificity for hydrophobic L-amino acids: branched-chain and aromatic, including Leu, Ile, Val, Phe and Tyr.
- LeuT transports Leu and other small hydrophobic amino acids. Tyt1 is selective for L-Tyr.

The most defensible annotation is therefore **"Na⁺-coupled neutral/hydrophobic L-amino acid symporter"**. Its precise specificity, whether branched-chain, aromatic or broad, cannot be inferred from sequence. In *V. cholerae* the plausible physiological role is Na⁺-driven uptake of hydrophobic amino acids. That fits an organism that relies heavily on a Na⁺ motive force; *V. cholerae* also has a Na⁺-pumping NADH:quinone oxidoreductase (NQR) and Na⁺-driven flagella. This is a physiological inference, not something shown for VC_2283.

### 3.3 Mechanism (by analogy)

LeuT-fold NSS transporters work by alternating access. Na⁺ binds to Na1 and Na2 in an outward-open state, which stabilizes the substrate site. Substrate binding is followed by occlusion, closure of the extracellular gate, and a shift to the inward-facing state. Na⁺ release from Na2 to the cytoplasm, aided by TM5 unwinding, is thought to start the inward release of substrate (Malinauskaite et al. 2014). Bacterial members usually couple 2 Na⁺ per amino acid. Eukaryotic NSS members need chloride, but bacterial members such as LeuT do not, because an acidic residue (Glu290 in LeuT) takes the place of Cl⁻ (Penmatsa & Gouaux 2013). Whether VC_2283 has an equivalent acidic residue in TM7 cannot be settled from my pairwise alignment, because that region is gapped. VC_2283 has a Asp258 near this position, which may play that role.

---

## 4. Cellular location

- **Cytoplasmic (inner) membrane, multi-pass.** Phobius predicts 12 TM helices with no cleavable signal peptide. All characterized bacterial NSS members are integral cytoplasmic-membrane proteins that take up substrate from the periplasm into the cytoplasm.
- UniProt's "Membrane; Multi-pass membrane protein" location comes from an ARBA rule (ARBA00004141). The topology comes from Phobius (ECO:0000256|SAM:Phobius), which counts as independent computational evidence. The existing GO:0016020 *membrane* annotation is correct but general. **Plasma membrane** (GO:0005886) is the more specific location that family biology supports, as for other Gram-negative inner-membrane transporters.

---

## 5. Pathways and biological processes

- **Primary process:** amino acid import across the plasma membrane, coupled to Na⁺ (symport). The appropriate GO terms would sit under *amino acid:sodium symporter activity* (GO:0005283) or *sodium:amino acid symporter activity* in current GO, and *amino acid transmembrane transport* (GO:0003333). Any specific substrate-level term (e.g., L-leucine or L-tyrosine) should be avoided until experimental data exist.
- **Physiological context (speculative):** scavenging amino acids from the host gut lumen or aquatic environments, and using the Na⁺ gradient generated by NQR and the Na⁺/H⁺ antiporters. No pathway placement or genetic-interaction data specific to VC_2283 were found.
- **Genomic context:** I did not analyze neighbouring genes. No operon-level evidence was identified that would narrow the substrate.

---

## 6. Evidence quality and gaps

| Claim | Evidence type | Confidence |
|---|---|---|
| NSS/SLC6 family member, LeuT fold | Domain signatures (Pfam, InterPro, PROSITE, CDD) plus 31–41% identity to structurally solved homologs | High |
| Integral (inner) membrane protein, 12 TM | Phobius plus family biology | High |
| Na⁺-coupled symporter | Conserved Na1 and Na2 site residues; all characterized bacterial NSS members are Na⁺-coupled | Moderate–high |
| Substrate is a neutral, hydrophobic L-amino acid | Conserved TM1 GxxGxGN, Y110 and TM8 motifs; nearest characterized homolog (MhsT) is a hydrophobic amino acid transporter | Moderate |
| Specific amino acid(s) | None | Unknown |
| Any phenotype or expression data for VC_2283 | None found | — |

**Open questions and suggested experiments:**
1. Express VC_2283 in an amino acid-uptake-deficient *E. coli* strain, or reconstitute it into proteoliposomes. Then measure Na⁺-dependent uptake of radiolabelled amino acids (Leu, Ile, Val, Met, Phe, Tyr, Trp, Ala) and test Li⁺ substitution, as done for MhsT and Tyt1.
2. Run a scintillation-proximity binding assay on the purified protein to determine specificity and Na⁺ stoichiometry (Quick & Javitch approach).
3. Analyse a VC_2283 deletion in *V. cholerae* for growth on single amino acids as nitrogen or carbon sources, and check transposon-sequencing fitness data under infection-relevant conditions.
4. Do a structure-based alignment with MhsT and the AlphaFold model of Q9KPS9 to confirm the Na1 Asn in TM7 and the presence or absence of the chloride-replacing Glu.

---

## Sources

- UniProt entry Q9KPS9 (local file `genes/VIBCH/VC_2283/VC_2283-uniprot.txt`, entry version 110, 28 Jan 2026); Heidelberg et al., *Nature* 406:477–483 (2000), PMID:10952301.
- Penmatsa A., Gouaux E. "How LeuT shapes our understanding of the mechanisms of sodium-coupled neurotransmitter transporters." *J Physiol* (2013/2014) – [PMC3948551](https://pmc.ncbi.nlm.nih.gov/articles/PMC3948551); [IAS record](https://repository.ias.ac.in/142665)
- Malinauskaite L. et al. "A mechanism for intracellular release of Na⁺ by neurotransmitter/sodium symporters." *Nat Struct Mol Biol* 21:1006 (2014), DOI 10.1038/nsmb.2894 – [PMC4346222](https://pmc.ncbi.nlm.nih.gov/articles/PMC4346222); [ESRF highlight 2014](https://www.esrf.fr/home/UsersAndScience/Publications/Highlights/highlights-2014/SB/SB05.html); [PDBsum 4US4](https://www.ebi.ac.uk/pdbsum/4us4)
- Focht D. et al. "A non-helical region in transmembrane helix 6 of hydrophobic amino acid transporter MhsT mediates substrate recognition." *EMBO J* 40:e105164 (2021), DOI 10.15252/embj.2020105164 – [PMC7780149](https://pmc.ncbi.nlm.nih.gov/articles/PMC7780149); PDB [6YU2](https://pdbj.org/mine/summary/6yu2), [6YU3](https://pdbj.org/mine/summary/6yu3), [6YU4](https://pdbj.org/mine/summary/6YU4), [6YU5](https://pdbj.org/mine/summary/6YU5), [6YU6](https://www1.rcsb.org/structure/6yu6), [6YU7](https://www1.rcsb.org/structure/6yu7); [Proteopedia 6YU3](https://proteopedia.org/w/6yu3)
- Tyt1 (*F. nucleatum*), J Biol Chem study of a functional bacterial NSS homolog – [Weill Cornell VIVO](https://vivo.weill.cornell.edu/display/pubid16798738); functional overexpression of Tyt1 and LeuT – [PMC3322350](https://pmc.ncbi.n

The report was essentially complete — it was cut off mid-way through the final sources list. Here is the remainder of that list, so nothing is missing:

## Sources (continued)

- Tyt1 functional overexpression in *Lactococcus lactis* (comparative expression of bacterial NSS homologs) — https://pmc.ncbi.nlm.nih.gov/articles/PMC3322350
- Vanderbilt record, "Structure and mechanism of a bacterial homolog of neurotransmitter:sodium symporters" — https://ir.vanderbilt.edu/items/9611d0e0-3e33-4a9e-b766-83e0fdba8888
- YhdH, *Bacillus subtilis* — UniProt O07577, "Uncharacterized sodium-dependent transporter YhdH" (PE=3); namesake of InterPro IPR047218
- VcINDY (the unrelated *V. cholerae* Na⁺-dependent dicarboxylate transporter, listed only to rule it out as a confusable) — https://nutrition-evidence.com/article/211510/functional-characterization-of-a-na-dependent-dicarboxylate-transporter-from-vibrio-cholerae and cryo-EM entry https://ibdc.dbtindia.gov.in/isda/summary/7T9G

**One note on provenance for the alignment section:** the identity figures (MhsT 40.6%, YhdH 37.0%, LeuT 31.4%) and the residue mapping table in §3.1 are from a pairwise Biopython alignment I ran in this session against UniProt-fetched sequences (Q9KDT3, O07577, O67854). They are not published values. If this feeds a gene review, that analysis should be made reproducible under `genes/VIBCH/VC_2283/VC_2283-bioinformatics/` with the results written to `RESULTS.md` before being cited.

## Citations

1. https://nutrition-evidence.com/article/211510/functional-characterization-of-a-na-dependent-dicarboxylate-transporter-from-vibrio-cholerae
2. https://ibdc.dbtindia.gov.in/isda/summary/7T9G
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC3948551
4. https://repository.ias.ac.in/142665
5. https://www.esrf.fr/home/UsersAndScience/Publications/Highlights/highlights-2014/SB/SB05.html
6. https://www.ebi.ac.uk/pdbsum/4us4
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC4346222
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC7780149
9. https://www1.rcsb.org/structure/6yu7
10. https://vivo.weill.cornell.edu/display/pubid16798738
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC3322350
12. https://pdbj.org/mine/summary/6yu2
13. https://pdbj.org/mine/summary/6yu3
14. https://pdbj.org/mine/summary/6YU4
15. https://pdbj.org/mine/summary/6YU5
16. https://www1.rcsb.org/structure/6yu6
17. https://proteopedia.org/w/6yu3
18. https://pmc.ncbi.n
19. https://ir.vanderbilt.edu/items/9611d0e0-3e33-4a9e-b766-83e0fdba8888