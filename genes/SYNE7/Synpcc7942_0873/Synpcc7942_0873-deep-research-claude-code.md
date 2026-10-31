---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T22:11:08.692445'
end_time: '2026-10-30T22:14:22.868973'
duration_seconds: 194.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SYNE7
  gene_id: Synpcc7942_0873
  gene_symbol: Synpcc7942_0873
  uniprot_accession: Q31PW6
  protein_description: 'RecName: Full=DUF4062 domain-containing protein {ECO:0000259|Pfam:PF13271};'
  gene_info: OrderedLocusNames=Synpcc7942_0873 {ECO:0000313|EMBL:ABB56903.1};
  organism_full: Synechococcus elongatus (strain ATCC 33912 / PCC 7942 / FACHB-805)
    (Anacystis nidulans R2).
  protein_family: Not specified in UniProt
  protein_domains: DUF4062. (IPR025139); DUF4062 (PF13271)
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
  num_turns: 9
  total_cost_usd: 0.7345148599999999
  session_id: d0ba5d5c-b129-42fa-9847-0ed6c542bcc1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q31PW6
- **Protein Description:** RecName: Full=DUF4062 domain-containing protein {ECO:0000259|Pfam:PF13271};
- **Gene Information:** OrderedLocusNames=Synpcc7942_0873 {ECO:0000313|EMBL:ABB56903.1};
- **Organism (full):** Synechococcus elongatus (strain ATCC 33912 / PCC 7942 / FACHB-805) (Anacystis nidulans R2).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF4062. (IPR025139); DUF4062 (PF13271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Synpcc7942_0873" matches the protein description above**
2. **Verify the organism is correct:** Synechococcus elongatus (strain ATCC 33912 / PCC 7942 / FACHB-805) (Anacystis nidulans R2).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Synpcc7942_0873' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Synpcc7942_0873** (gene ID: Synpcc7942_0873, UniProt: Q31PW6) in SYNE7.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I'm writing the final report now. The research is done: the cyanobacterial protein itself is uncharacterized, so the report relies on 2026 work on its DUF4062 domain family.

# Synpcc7942_0873 (UniProt Q31PW6), a DUF4062 domain protein from *Synechococcus elongatus* PCC 7942: functional annotation research report

## 1. Identity check

| Field | Value | Source |
|---|---|---|
| Accession | Q31PW6 (Q31PW6_SYNE7), TrEMBL, unreviewed | UniProt record (local `Synpcc7942_0873-uniprot.txt`) |
| Locus | Synpcc7942_0873, chromosome (CP000100; ABB56903.1; WP_011242979.1) | UniProt |
| Organism | *S. elongatus* PCC 7942 (Anacystis nidulans R2), NCBI taxon 1140 | UniProt |
| Length | 362 aa, 41.4 kDa | UniProt |
| Name | "DUF4062 domain-containing protein" (assigned from Pfam) | UniProt |
| Domains | DUF4062 (PF13271 / IPR025139) at residues 6–146; predicted coiled coil at residues 170–197 (Coils) | UniProt FT lines |
| Protein existence | PE 4: Predicted | UniProt |
| Existing GO annotations | None. The GOA file contains only a header row | local `Synpcc7942_0873-goa.tsv` |

**Verification.** The locus tag, organism and domain content all match the target. No paper studies this locus specifically. Web searches for "Synpcc7942_0873" found only automated listings, such as a systems-biology network page that calls it a "hypothetical protein" ([networks.systemsbiology.net](https://networks.systemsbiology.net/syf/gene/Synpcc7942_0886)). **No gene-specific experimental literature exists.** Everything below about function is inferred from the DUF4062 domain family. There is no other gene with a confusable symbol.

## 2. Domain architecture and sequence features

- **N-terminal DUF4062 domain (residues 6–146).**
  - Pfam and InterPro describe it as a "presumed domain [that] is functionally uncharacterised", found in bacteria, archaea and eukaryotes, with "a conserved SST sequence motif" ([NCBI CDD pfam13271](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam13271); [InterPro IPR025139 / PF13271](https://www.ebi.ac.uk/interpro/entry/pfam/PF13271/)).
  - Pfam notes the domain "shows structural similarity to TIR domains" and places it in clan CL0173 (STIR).
  - InterPro counts about 4,650 proteins with 764 domain architectures.
  - The eukaryotic member named in InterPro is TEP1 (telomerase protein component 1, a vault component), citing Venteicher et al. 2009, *Science* 323:644 (PMID:19179534).
- **Motifs in Q31PW6.** These were located by direct string search of the sequence. I did not align it to characterized family members.
  - **8-FISSTF-13** matches the family's N-terminal "[KR][VI]FIS[ST]" / SST motif seen in the CDD alignment. It also contains the aromatic residue that corresponds to the essential F11 of Eva01 (see §3).
  - **77-LSYTE-81** resembles the "acidic-SYT region containing a putative catalytic glutamate" described for Eva01 (E87 there). Glu81 of Q31PW6 is therefore a candidate catalytic glutamate. This assignment is a hypothesis and has not been tested.
  - 66-GGRYG-70 and 136-WRNA-139 are other conserved-looking segments inside the domain.
- **C-terminal region (residues ~150–362).** This includes the predicted coiled coil (170–197) and a ~165-residue segment with no Pfam/InterPro match. It is consistent with the variable C-terminal "auxiliary" (AUX) or sensor regions that follow DUF4062 in the characterized bacterial systems (§3). Its role in Q31PW6 is unknown.

## 3. What is known about the DUF4062 family (2026)

Two 2026 preprints give the first functional data for this family. **Neither has been peer reviewed, and neither studied Q31PW6.**

### 3.1 DUF4062 is a TIR-like NAD⁺ hydrolase (Osinski et al., 2026)

Osinski A, Mayro B, Lopez VA, …, Pawłowski K, Forsberg K, Shahmoradian SH, Tagliabracci VS. *TIR-like NADases act in bacterial immunity and the RNA vault.* bioRxiv preprint, 5 May 2026, doi:10.64898/2026.05.01.722283; PMID:42146377 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/42146377/); [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.05.01.722283v1)). I read only the abstract and figure legends; the full text was blocked by a CAPTCHA.

- **Activity.** "DUF4062 is a widespread family of TIR-like NADases that hydrolyze NAD+ to ADP-ribose and nicotinamide." HPLC detects nicotinamide and ADP-ribose as products. The abstract and legends mention no cyclic ADPR-type products.
- **Catalytic residue.** In the *Klebsiella* system they named Swarożyc (KpSwz), the E97A mutant is "inactive" and loses phage defence. In human TEP1 the corresponding residue is E1008.
- **Activation and assembly.**
  - KpSwz has a DUF4062 domain plus an auxiliary (AUX) domain with a "rigid HTH/winged helical core".
  - It forms dimers and higher oligomers.
  - It "assembles with the phage portal into a supramolecular NADase complex to induce abortive infection": cryo-EM shows 13 KpSwz AUX domains bound to a dodecameric portal ring. The figure title reads "Kp_Swz is a portal activated NADase."
- **Genomic context.** DUF4062 loci are often next to known defence genes or inside antiphage defence islands or operons. The Pfam/InterPro summary of this work gives about 20% inside predicted defence islands and over half next to at least one defence gene; I could not confirm these numbers in the parts of the paper I read.
- **Eukaryotes.** TEP1 "functions as an active NADase within the RNA vault", with ADP-ribose seen bound at the vault shoulder. NWD1, NWD2 and NPHP3 also contain DUF4062.

### 3.2 Evangelion: a plasmid-borne DUF4062 antiphage system (Ibarra-Chavez et al., 2026)

Ibarra-Chavez R, Azam AH, Chihara K, …, Madsen JS, Kiga K. *Antimicrobial-resistance plasmids encode Evangelion, a widespread DUF4062 anti-phage defence family.* bioRxiv preprint, June 2026, doi:10.64898/2026.06.25.731849 ([bioRxiv](https://www.biorxiv.org/content/10.64898/2026.06.25.731849v1.full)). I read part of it.

- **Architecture.** Eva01 has "a compact N-terminal DUF4062 region with an α/β fold resembling TIR-like proteins, followed by a short C-terminal auxiliary region (AUX)". The AUX region is highly variable across the family.
- **Essential residues.** These include "a conserved acidic-SYT region containing a putative catalytic glutamate E87", an N-terminal aromatic motif centred on F11, and a Q/W/E motif. "F11A, E87A, W162A, W162F and the AUX truncation Eva01::L177* disrupted defence."
- **Mechanism.** Eva01 "couples activation of a DUF4062 effector to NAD+ depletion and abortive infection". The paper notes that direct enzymology was not shown. The activating signal is not known for certain but seems linked to phage replication and recombination functions. I could not verify this point in the part of the text I read.
- **Hosts.** In a survey of 447 Evangelion-positive plasmids, *Synechococcus* hosts made up 1.1%. This suggests DUF4062 defence genes do occur in this genus, although Synpcc7942_0873 is chromosomal.

## 4. Inferred function of Synpcc7942_0873

**Most likely molecular function.** Q31PW6 has an N-terminal DUF4062 domain followed by a variable C-terminal region. That matches the "DUF4062 effector + AUX/sensor" layout of the characterized bacterial systems. Its sequence also has candidates for the essential N-terminal aromatic/SST motif (F8–F13) and the acidic-SYT glutamate (Glu81 in LSYTE). Together these suggest **a TIR-like NAD⁺ glycohydrolase (NAD⁺ → ADP-ribose + nicotinamide) that is normally inactive and is switched on by a trigger.** The trigger is probably a phage component sensed by its C-terminal region. Confidence is low to moderate: the evidence is domain membership plus motif similarity, the family data are preprints, and no biochemistry exists for any cyanobacterial member.

**Probable biological process.** By analogy, it is likely an antiviral (antiphage) defence effector acting by abortive infection: it depletes NAD⁺ so the infected cell dies before the phage can spread. Whether Synpcc7942_0873 sits in a defence island in PCC 7942 has not been checked. Its gene neighbourhood should be inspected (e.g. in IMG, KEGG or the FitnessBrowser) before relying on this.

**Localization.** No signal peptide or transmembrane segment is annotated, so it is probably cytoplasmic. This is consistent with an NAD⁺-depleting effector. No experimental data exist.

**Pathway context.** No metabolic pathway applies. If the inference is right, the protein belongs to a phage-defence or abortive-infection system rather than to housekeeping NAD⁺ metabolism.

**Fitness and essentiality.** PCC 7942 has a genome-wide RB-TnSeq essential gene set (Rubin et al. 2015, PNAS), but I could not get the result for this locus: the FitnessBrowser and VSPfam pages returned HTTP 403. Defence genes are usually non-essential under laboratory conditions.

## 5. Implications for GO annotation

- **Current state.** There are no GOA annotations, so nothing needs reviewing.
- **Candidate terms.** These are inferences only and should be held back or flagged pending peer-reviewed or gene-specific evidence:
  - MF: NAD⁺ nucleosidase activity (GO:0003953, or a child term), by analogy to the DUF4062 family.
  - BP: defense response to virus, by analogy.
  - CC: cytoplasm, from the lack of targeting signals.
  - None of these meets the bar for a `NEW` experimental-quality annotation for this gene. At most they are domain-based (ISS/IEA-level) inferences, and both papers behind them are preprints.
- **Annotation caution.** TEP1 and the vault connection are eukaryote-specific. They should not be transferred to this bacterial protein.

## 6. Open questions and suggested experiments

1. Does recombinant Q31PW6 (or its DUF4062 domain alone) hydrolyse NAD⁺ to ADP-ribose and nicotinamide? Does an E81A mutation (and F8A or F13A) abolish this activity?
2. Is the full-length protein self-inhibited by its C-terminal region, and what activates it (e.g. a cyanophage portal or a replication/recombination protein)?
3. Does expressing the protein in *S. elongatus*, or a deletion mutant, change sensitivity to cyanophages (e.g. AS-1 or S-PM2-like phages)? Does activation deplete NAD⁺ in vivo?
4. Gene neighbourhood: does Synpcc7942_0873 lie next to other defence genes or mobile elements in the PCC 7942 chromosome?

## 7. Summary

Synpcc7942_0873 encodes a 362-aa protein with no experimental study, so its function is known only from its domain family. It has an N-terminal DUF4062 domain (residues 6–146), a coiled coil (170–197) and an unassigned C-terminal region. In 2026 the DUF4062 family was identified as TIR-like NAD⁺ hydrolases that serve as abortive-infection effectors in bacterial antiphage systems such as Swarożyc and Evangelion, with a catalytic glutamate in a conserved acidic-S(S/Y)T region. By homology, Q31PW6 is predicted to be a cytoplasmic NADase that a trigger switches on during phage defence. This prediction rests on preprint-level family data and sequence similarity, and nothing has been tested for this protein.

## Sources

- UniProt Q31PW6 record (local file `genes/SYNE7/Synpcc7942_0873/Synpcc7942_0873-uniprot.txt`, entry version 73, 02-Sep-2026)
- [NCBI CDD pfam13271 (DUF4062)](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam13271)
- [InterPro PF13271 / IPR025139](https://www.ebi.ac.uk/interpro/entry/pfam/PF13271/)
- [Osinski et al. 2026, TIR-like NADases act in bacterial immunity and the RNA vault (PubMed 42146377)](https://pubmed.ncbi.nlm.nih.gov/42146377/); [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.05.01.722283v1); [PMC13174449](https://pmc.ncbi.nlm.nih.gov/articles/PMC13174449/)
- [Ibarra-Chavez et al. 2026, Evangelion DUF4062 anti-phage defence family (bioRxiv)](https://www.biorxiv.org/content/10.64898/2026.06.25.731849v1.full)
- Venteicher AS et al. 2009, *Science* 323:644–648 (PMID:19179534), TEP1 reference cited by InterPro
- [networks.systemsbiology.net, *S. elongatus* gene listing](https://networks.systemsbiology.net/syf/gene/Synpcc7942_0886)

## Citations

1. https://networks.systemsbiology.net/syf/gene/Synpcc7942_0886
2. https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam13271
3. https://www.ebi.ac.uk/interpro/entry/pfam/PF13271/
4. https://pubmed.ncbi.nlm.nih.gov/42146377/
5. https://www.biorxiv.org/content/10.64898/2026.05.01.722283v1
6. https://www.biorxiv.org/content/10.64898/2026.06.25.731849v1.full
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC13174449/