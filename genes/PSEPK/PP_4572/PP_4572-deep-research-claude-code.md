---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:32:27.136975'
end_time: '2026-10-30T21:37:39.643127'
duration_seconds: 312.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4572
  gene_symbol: PP_4572
  uniprot_accession: Q88E94
  protein_description: 'RecName: Full=DUF748 domain-containing protein {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_4572 {ECO:0000313|EMBL:AAN70145.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AsmA-related. (IPR052894)
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
  num_turns: 20
  total_cost_usd: 1.0771804400000002
  session_id: a7c779e4-99c8-47f2-b3f3-470beec2d6db
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 7
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88E94
- **Protein Description:** RecName: Full=DUF748 domain-containing protein {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_4572 {ECO:0000313|EMBL:AAN70145.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AsmA-related. (IPR052894)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4572" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4572' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4572** (gene ID: PP_4572, UniProt: Q88E94) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking fitness data and the AsmA-family papers, then writing the report.

I found the key paper (Sposato 2024), which covers PA2708, the likely *P. aeruginosa* ortholog. Next I'll check orthology against PP_4572.

# PP_4572 (UniProt Q88E94), a small AsmA-like protein of *Pseudomonas putida* KT2440

## Summary

- **Identity is confirmed.** PP_4572 (Q88E94) is a 357-residue protein from *P. putida* KT2440. UniProt has not reviewed the entry, and its name, "DUF748 domain-containing protein", is a ProtNLM machine prediction. Its only domain match is to the **AsmA-like family** (InterPro IPR052894 / PANTHER PTHR30441, subfamily SF4 "PROTEIN ASMA", covering residues 8–244). No paper studies PP_4572 itself.
- **Closest characterized relative: PA2708 of *P. aeruginosa* PAO1** (Q9I0D4, 361 aa). In my local alignment the two proteins are **71.7% identical across almost their full length** (256 identical residues; PP_4572 residues 1–357 against PA2708 residues 1–359). PA2708 is also a PTHR30441:SF4 protein carrying Pfam PF05359 (DUF748). They are almost certainly orthologs.
- **Likely function:** PP_4572 is probably a **non-essential, inner-membrane-anchored periplasmic AsmA-like protein**. It belongs to the family proposed to move glycerophospholipids (GPLs) to the outer membrane (OM). Its specific role is **unknown**, and the main study argues it is too short to bridge the periplasm on its own. It has no predicted enzyme activity, substrate or pathway.

---

## 1. Identity and sequence features

| Feature | Value | Source |
|---|---|---|
| Locus / accession | PP_4572 / Q88E94 (TrEMBL, PE 4 "Predicted") | UniProt record (local file `PP_4572-uniprot.txt`) |
| Length / mass | 357 aa / 40.3 kDa | UniProt |
| Name in GenBank (KEGG) | "conserved exported protein of unknown function" | KEGG ppu:PP_4572 |
| Family | IPR052894 "Protein AsmA-like"; PANTHER PTHR30441 "DUF748 domain-containing protein", subfamily SF4 "PROTEIN ASMA" | InterPro API (live query); local `panther.obo` |
| Orthology group | eggNOG COG2982 (AsmA family) | UniProt DR lines |
| Genomic position | 5,191,546–5,192,619 (+ strand). Neighbours: PP_4571 cysteine synthase A (opposite strand), PP_4573 AAA-family ATPase (same strand, starts 202 bp downstream) | KEGG |

**Topology (my own analysis).** I ran a Kyte–Doolittle hydropathy scan (19-residue window). It finds one hydrophobic segment and nothing else: windows starting at residues 5–16 score above 1.6, covering about residues 5–34 ("…WPLVGLASLIVLLVALHLALPYLV…"). This matches the family's typical layout: one N-terminal helix anchors the protein in the inner membrane, and the rest of the protein sits in the periplasm. Sposato et al. (2025) describe AsmA-like proteins as having "an N-terminal transmembrane α-helix (TMH), which anchors them to the IM, and a large soluble domain" [Sposato et al., *Protein Sci* 2025;34:e70227, PMID 40970438]. UniProt has no curated transmembrane or signal-peptide annotation for Q88E94. Treat the topology as a prediction.

## 2. The AsmA-like protein family

- **History of the family name.** *E. coli* AsmA ("assembly of outer membrane proteins") was found because *asmA* mutations suppress a defective OmpF assembly mutant (OmpF315). AsmA fractionated with the **inner membrane**, so its effect on OM protein assembly was judged indirect. *asmA* nulls lowered OM LPS levels, which the authors linked to changes in OM fluidity (Deng & Misra, *Mol Microbiol* 1996;21:605–612). The GO term that GOA gives PP_4572 by IEA, "regulation of protein targeting to membrane" (GO:0090313), probably reflects this historical OMP-assembly phenotype passed down through the PANTHER family. No PP_4572-specific evidence supports it.
- **Current model: anterograde GPL transport.** In *E. coli*, the large AsmA-like proteins YhdP, TamB and YdbH are redundant, but losing all three is lethal. Cells lacking them show defects in OM lipid homeostasis and GPL transport (Ruiz lab, *mBio* 2021, [PMC8593681](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8593681/); Douglass, McLean & Trent, *PLoS Genet* 2022, [PMC8912898](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8912898/)). AlphaFold models show a long β-taco/tube with a hydrophobic groove, resembling the Lpt periplasmic bridge and the eukaryotic chorein/VPS13 bridge-like lipid transporters. This supports a model where lipids slide along the groove between the membranes.
- **The family in *P. aeruginosa*.** There are seven AsmA-like proteins: TamB, YhdP (PA4476), YhjG (PA4879), AsmA (PA5146), YdbH (PA5307), PA4735/EpaF, and **PA2708**. YhdP, TamB, YdbH and PA4735 are essential but redundant (Sposato et al., *mSphere* 2024, PMID 38305166, [PMC10900882](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10900882/)). The 2025 follow-up shows that two C-terminal amphipathic helices of YhdP are needed for OM anchoring and probably for GPL insertion. It also proposes that only YhdP is long enough to span the periplasm (PMID 40970438, [PMC12447247](https://pmc.ncbi.nlm.nih.gov/articles/PMC12447247)).

## 3. What is known about PA2708, the ortholog of PP_4572

The only experimental data on this subfamily come from Sposato et al. (2024), whose full text I retrieved through Europe PMC:

- **Size and family:** PA2708 (361 aa, PF05359) has no counterpart in *E. coli*. Its AlphaFold model has the family's N-terminal TMH and β-rich tube, but "PA2708 is much smaller than the other AsmA-like proteins of both *P. aeruginosa* and *E. coli*… and the length of its periplasmic domain is likely not sufficient to span the entire periplasmic space."
- **Not essential and not part of the redundant essential set:** The authors depleted TamB in a ΔyhdP ΔydbH background (a strain that grows poorly without its inducer) and then deleted PA2708. Growth did not get worse. The authors conclude "PA2708… is not required for *P. aeruginosa* growth". In contrast, deleting PA4735 in the same background abolished growth.
- **Conserved across the genus, function open:** The size of PA2708 "is not expected to allow to cross the periplasmic space unless PA2708 can interact with OM partners protruding into the periplasm… this protein is conserved in different *Pseudomonas* species… Further studies are required to uncover its role."

PP_4572 is 71.7% identical to PA2708 and nearly the same length, so these conclusions very likely apply to it too.

## 4. Proposed function, location and pathway

| Aspect | Best-supported statement | Confidence |
|---|---|---|
| Molecular function | Unknown. Its fold suggests it could bind or shuttle lipids with a hydrophobic groove, as other AsmA-like/chorein-type proteins do. No catalytic activity is predicted. | Low (inferred from family) |
| Location | Cell inner membrane (single N-terminal anchor helix), with the C-terminal domain in the periplasm. The IEA term GO:0005886 "plasma membrane" is consistent with this. | Moderate (sequence feature plus family architecture) |
| Process | Possibly a minor role in outer-membrane lipid homeostasis or envelope biogenesis. It is not part of the essential GPL-transport bridge set. | Low |
| GO:0090313 "regulation of protein targeting to membrane" (IEA, TreeGrafter) | Weakly grounded. It comes from the *E. coli* AsmA OMP-assembly suppressor phenotype, which was itself judged indirect, and there is no evidence for the PA2708/PP_4572 subfamily. | Probably an over-annotation |

I found no experimental data on PP_4572 itself: no mutant, localization or interaction studies. KT2440 fitness data from the Fitness Browser could not be retrieved because the site blocked the automated request with a bot check. The genes next to it (cysteine synthase, AAA ATPase) do not point to any obvious functional link.

## 5. Open questions and suggested experiments

1. Does PP_4572 need an OM-associated partner (for example a lipoprotein, the way YdbH pairs with YnbE) to reach the OM? Pull-down or crosslinking of a tagged PP_4572 would test this.
2. Does deleting PP_4572 cause OM-integrity phenotypes (SDS/EDTA, vancomycin, NPN uptake) when combined with depletion of YhdP, TamB, YdbH or the PA4735 ortholog? Check the KT2440 RB-TnSeq fitness data first.
3. Does PP_4572 bind lipids? Purify the periplasmic domain and test GPL co-purification.

## Sources

- UniProt Q88E94 entry (local `genes/PSEPK/PP_4572/PP_4572-uniprot.txt`); InterPro API for Q88E94; KEGG ppu:PP_4572–PP_4573
- Sposato D. et al. 2024. Redundant essentiality of AsmA-like proteins in *Pseudomonas aeruginosa*. *mSphere*. PMID 38305166. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10900882/
- Sposato D. et al. 2025. Structure–function relationship of the *P. aeruginosa* AsmA-like proteins YhdP and YdbH. *Protein Sci* 34:e70227. PMID 40970438. https://pmc.ncbi.nlm.nih.gov/articles/PMC12447247
- Ruiz N. et al. 2021. YhdP, TamB, and YdbH are redundant but essential for growth and lipid homeostasis of the Gram-negative outer membrane. *mBio*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8593681/
- Douglass M.V., McLean A.B., Trent M.S. 2022. Absence of YhdP, TamB, and YdbH leads to defects in glycerophospholipid transport. *PLoS Genet*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8912898/
- Deng M., Misra R. 1996. Examination of AsmA and its effect on the assembly of *E. coli* outer membrane proteins. *Mol Microbiol* 21:605–612. https://asu.elsevierpure.com/en/publications/examination-of-asma-and-its-effect-on-the-assembly-of-escherichia
- EcoliWiki, YhjG: https://ecoliwiki.org/colipedia/index.php/yhjG:Gene_Product(s); STRING b3524: https://string-db.org/network/511145/b3524
- My own analyses: hydropathy scan of Q88E94, and a local Smith–Waterman alignment (BLOSUM62) of Q88E94 against Q9I0D4, giving 71.7% identity. Neither result was saved to the repository.

## Citations

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8593681/
2. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8912898/
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10900882/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC12447247
5. https://asu.elsevierpure.com/en/publications/examination-of-asma-and-its-effect-on-the-assembly-of-escherichia
6. https://ecoliwiki.org/colipedia/index.php/yhjG:Gene_Product(s
7. https://string-db.org/network/511145/b3524