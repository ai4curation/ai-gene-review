---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:31:55.053836'
end_time: '2026-10-30T21:40:32.237214'
duration_seconds: 517.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_1879
  gene_symbol: VC_1879
  uniprot_accession: Q9KQW8
  protein_description: 'SubName: Full=Rec2-related protein {ECO:0000313|EMBL:AAF95027.1};'
  gene_info: OrderedLocusNames=VC_1879 {ECO:0000313|EMBL:AAF95027.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: ComA-like_MBL. (IPR035681); ComEC-like_N. (IPR025405); ComEC_N.
    (IPR004477); Competence_ComEC/Rec2. (IPR004797); Competence_DNA_uptake. (IPR052159)
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
  web_search_requests: 9
  num_turns: 25
  total_cost_usd: 2.28129219
  session_id: a13475b4-adb9-48b1-8d7e-9c928aefaa68
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KQW8
- **Protein Description:** SubName: Full=Rec2-related protein {ECO:0000313|EMBL:AAF95027.1};
- **Gene Information:** OrderedLocusNames=VC_1879 {ECO:0000313|EMBL:AAF95027.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ComA-like_MBL. (IPR035681); ComEC-like_N. (IPR025405); ComEC_N. (IPR004477); Competence_ComEC/Rec2. (IPR004797); Competence_DNA_uptake. (IPR052159)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_1879" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_1879' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_1879** (gene ID: VC_1879, UniProt: Q9KQW8) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking the cached publications for papers on *V. cholerae* ComEC.

# Research Report: *Vibrio cholerae* VC_1879 (Q9KQW8) — ComEC/Rec2, the inner‑membrane DNA translocase of the natural‑transformation machinery

**Target:** UniProtKB **Q9KQW8** (`Q9KQW8_VIBCH`, TrEMBL, unreviewed) · locus **VC_1879** / **VC1879** · *Vibrio cholerae* serotype O1 str. N16961 (NCBI:txid243277) · 752 aa, 85,047 Da · `PE 4: Predicted`
**Report date:** 2026‑10‑30

---

## 1. Identity verification (mandatory check)

The UniProt description "Rec2‑related protein" is a submitter‑derived name (`ECO:0000313|EMBL:AAF95027.1`) and carries no curated content. The identity must therefore be established from domain architecture plus the *V. cholerae* competence literature. Both converge, and they converge on the same gene:

| Line of evidence | Result |
|---|---|
| InterPro/Pfam/NCBIfam signatures on Q9KQW8 | `IPR004797` Competence ComEC/Rec2; `IPR004477` ComEC_N; `IPR025405` ComEC‑like_N (DUF4131); `IPR035681` ComA‑like MBL; TIGR00360 (ComEC_N‑term) **and** TIGR00361 (ComEC_Rec2); Pfam PF03772 (Competence) + PF13567 (DUF4131) + PF00753 (Lactamase_B) |
| PANTHER | PTHR30619 "DNA INTERNALIZATION/COMPETENCE PROTEIN COMEC/REC2", subfamily SF1 |
| eggNOG | COG0658 + COG2333 (the two COGs that together describe ComEC) |
| Literature locus‑tag usage | *V. cholerae* competence reviews and primary papers write the gene as **"comEC (vc1879)"** — e.g. the CytR competence‑regulation study lists *comEC (vc1879)* among genes examined, and the Metzger & Blokesch competence review's gene table pairs `comEC` with `vc1879` ([ASM Microbiol Spectr 2016](https://journals.asm.org/doi/full/10.1128/microbiolspec.ve-0010-2014); [PLoS ONE 2015 CytR paper](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0138834)) |
| Third‑party reconciliation | Wikidata Q23433299 "Rec2‑like protein VC1879" maps the same accession to Competence protein ComEC/Rec2 ([Wikidata](https://www.wikidata.org/wiki/Q23433299)) |

**Conclusion: VC_1879 / Q9KQW8 is *V. cholerae* ComEC.** "Rec2" is the historical *Haemophilus influenzae* name for the same orthologue — *rec‑2* mutants of *H. influenzae* take up DNA normally but fail to translocate it into the cytoplasm, and *rec‑2* was shown to be homologous to the *comE‑ORF3* (ComEC) product ([NCBI CDD TIGR00361](https://www.ncbi.nlm.nih.gov/Structure/cdd/TIGR00361)). The two names denote one protein family; the UniProt name is therefore correct but archaic.

**Caveat carried through this report:** there is, to my knowledge, **no published biochemical or structural study of the *V. cholerae* ComEC protein itself**. The *V. cholerae*-specific evidence is genetic (deletion/epistasis), and the mechanistic detail comes from orthologues in *Bacillus subtilis*, *Moorella*, and *Legionella pneumophila*. I flag below which statements are *V. cholerae* data and which are transferred.

---

## 2. Primary function

ComEC is the **inner‑membrane (cytoplasmic‑membrane) channel through which a single strand of transforming DNA is translocated into the cytoplasm during natural transformation**, and — via its C‑terminal metallo‑β‑lactamase (MBL)-fold domain — it is also the **nuclease that degrades the non‑translocated complementary strand**. It is thus a bifunctional transport‑plus‑catalysis component, not a passive pore.

In pathway terms: ComEC performs the **final, inner‑membrane step** of DNA uptake. It is downstream of the competence type IV pilus (which pulls DNA across the outer membrane) and of the periplasmic DNA‑binding protein ComEA, and upstream of the cytoplasmic ssDNA‑handling proteins DprA/SSB and the recombinase RecA.

### 2.1 Genetic evidence in *V. cholerae* (the directly relevant data)

The decisive *V. cholerae* experiment is **Seitz & Blokesch (2013), PNAS 110(44):17987–17992, PMID 24127573, doi:10.1073/pnas.1315647110** ([PMC3816411](https://pmc.ncbi.nlm.nih.gov/articles/PMC3816411/)). Using a chitin‑independent (TfoX‑induced) transformation assay plus a whole‑cell duplex‑PCR assay that detects transforming DNA (tDNA) that has crossed the outer membrane:

- **Δ*comEC* is non‑transformable.** Transformants were never recovered for the pilus‑unrelated mutants; the detection limit was 7.1 × 10⁻⁸ ± 3.3 × 10⁻⁸. Quote: *"which was not the case for strains lacking comEA, comEC, comF, and recA"*.
- **Δ*comEC* accumulates internalised (periplasmic) tDNA** — the block is after outer‑membrane passage. Quote: *"we detected tDNA only in strains lacking comEC, comF, or recA and not in Tfp‑related mutants or a comEA⁻ strain"*.
- **Epistasis places ComEC downstream of the pilus and of ComEA.** Deleting *comEC* in a pilus mutant or in Δ*comEA* did **not** restore tDNA accumulation: *"The concomitant absence of comEC did not result in accumulation of tDNA in any of the Tfp‑related mutants"*.
- **ComEC acts at the same step as ComF**, since Δ*comF* Δ*comEC* accumulated no more tDNA than Δ*comF* alone; and **upstream of RecA**, since Δ*recA* Δ*comEC* accumulated more.
- The authors' explicit model: *"ComEA shuttles the tDNA through the periplasm and toward the inner membrane aqueous channel ComEC"* and *"ComF, with the membrane channel protein ComEC, participates in DNA translocation across the inner membrane."*

This phenotype — DNA reaches the periplasm via PilQ but is not delivered to the cytoplasm — is restated in the authoritative *V. cholerae* competence review: a Δ*comEC* mutant *takes up DNA into the periplasm via PilQ but does not deliver it into the cytoplasm* ([Metzger & Blokesch, Microbiol Spectr 2016](https://journals.asm.org/doi/full/10.1128/microbiolspec.ve-0010-2014)).

Companion work from the same group established the upstream and parallel steps: ComEA is essential for transfer of external DNA into the periplasm and binds incoming DNA there, acting as a Brownian ratchet ([Seitz & Blokesch, PLoS Genet 2014](https://infoscience.epfl.ch/record/195185?ln=fr)); and outer‑ and inner‑membrane transport are *spatially but not temporally coupled* ([Seitz & Blokesch, mBio 2014;5(4):e01409‑14](https://journals.asm.org/doi/10.1128/mBio.01409-14)) — i.e. DNA can dwell in the periplasm, bound by ComEA, before engaging ComEC.

### 2.2 Transferred mechanistic evidence: what ComEC does molecularly

**(a) It is required for uptake, not for binding.** In *B. subtilis*, ComEC shows *"its absolute requirement for DNA uptake but not for DNA binding to the cell"* ([Draskovic & Dubnau, Mol Microbiol 2005;55(3):881‑896, PMID 15661011](https://doi.org/10.1111/j.1365-2958.2004.04430.x)). Its toxicity when expressed in *E. coli* has long frustrated direct biochemistry: *"Because of its toxicity in E. coli …, no direct biochemical evidence has been acquired to support this hypothesis."*

**(b) One strand enters, the other is destroyed.** The transforming duplex is resolved at the inner membrane: the strand leading with its **3′ end is translocated** into the cytoplasm while the **5′‑leading strand is degraded**. *comEC* null mutations prevent degradation of the non‑transforming strand, tying the nuclease activity to ComEC itself.

**(c) The nuclease is the C‑terminal MBL‑fold domain.** The most detailed study to date is **Stedman et al., *Nucleic Acids Research* 2025;53(18):gkaf932, PMID 40985778, doi:10.1093/nar/gkaf932** (published 2025‑09‑23; ETH Zürich, Hospenthal lab), working on *Moorella glycerini* ComEC domains with *Legionella pneumophila* in vivo transformation:

- Architecture: *"Most ComEC orthologues are comprised of three domains: an OB fold encoded near the N‑terminus, a central competence domain consisting of a bundle of transmembrane helices forming a channel and a C‑terminal β‑lactamase‑like domain."* Pfam mapping given in that paper: **PF13567 = the OB fold (DUF4131)**, **PF03772 = the transmembrane channel/competence domain**, **PF00753 = the β‑lactamase‑like (MBL) nuclease domain**. Q9KQW8 carries **all three**.
- Catalysis: the isolated MBL domain is an **Mn²⁺‑dependent nuclease** (*"BLACT_Mg is also an Mn²⁺‑dependent nuclease"*), coordinating **two Mn²⁺ ions**, with *"a clear preference for ssDNA"*; it cleaves both exonucleolytically from the 5′ end and endonucleolytically, with **no 3′ exonuclease activity** — exactly the polarity needed to destroy the 5′‑leading strand while sparing the 3′‑leading strand that is being threaded inward. Catalytic motif: **H‑X‑D‑X‑D‑H** (H598/D600/D602/H603 in *Moorella*), with alanine substitution of most metal‑coordinating residues rendering the enzyme *"virtually inactive"* and abolishing transformation in vivo.
- The **OB fold is a high‑affinity DNA clamp that feeds the nuclease**: it binds dsDNA with K_D ≈ 0.33 µM (ssDNA 0.79 µM) through an electrostatic, arginine‑rich surface, whereas the MBL domain alone has *"seemingly absent affinity for its DNA substrate (K_D not determinable)."* Supplied *in trans* the OB fold does nothing; **covalently tethered** it gives a ~7‑fold rate increase, so *"an increase in local concentration of the substrate is the main mechanism."*
- **Translocation is ATP‑independent at ComEC**: *"There is no ATP consumed by ComEC for the translocation of DNA."* The pulling force is attributed to cytoplasmic factors — ComFA in Gram‑positives, and **ComF/PriA‑type helicase activity in Gram‑negatives**, which is consistent with the *V. cholerae* finding that ComF and ComEC are epistatic at the same step.
- Channel‑lining aromatic residues (W212A, Y373A) reduced *Legionella* transformation ~5‑fold; a loop near the channel entrance (F689A/F691A), proposed to act as a "pin" that selects which strand goes to the nuclease, **abolished transformation**. The geometric argument for selectivity: *"only a single strand is selectively degraded, as nucleolytic attack of the other strand would require a 180 degree rotation."*
- Structures deposited: **PDB 9IC4** (1.8 Å crystal structure of the β‑lactamase‑like domain) and **PDB 9IEW** (solution NMR structure of the OB domain).

**Mapping this onto VC_1879.** The *V. cholerae* sequence preserves the catalytic apparatus:

- `FT DOMAIN 506..689 Metallo‑beta‑lactamase (SMART SM00849)`
- Motif I **G505‑H506‑G507** (`LDVGHGLAI`)
- The **H‑X‑D‑X‑D‑H motif at H556‑L‑D558‑N‑D560‑H561** (`VILSHLDNDHAGD`) — the exact signature Stedman et al. identify as the metal‑coordinating catalytic centre
- A downstream His pair **H663/H664** (`MIVPHHGSK`) and the motif‑III Asp in `HSVLLSGDVT`

(These positions were computed directly from the Q9KQW8 sequence in this repository, not taken from an annotation.) The predicted OB‑fold/DUF4131 region lies in the N‑terminal ~130–230 segment, and Phobius predicts **10 TM helices** (12–28, 34–49, 234–255, 267–288, 294–314, 321–349, 369–393, 400–427, 476–497, plus the region preceding the MBL domain). So *V. cholerae* ComEC is a **full‑architecture, catalytically intact** family member — it is not one of the reduced orthologues that lack the OB fold or the nuclease domain.

---

## 3. Subcellular localization and topology

**Location: the inner (cytoplasmic) membrane, as a polytopic integral membrane protein.** UniProt records `SUBCELLULAR LOCATION: Cell membrane; Multi-pass membrane protein`, but note this is **ARBA‑rule evidence (`ECO:0000256|ARBA:ARBA00004651`), i.e. an unvetted automatic prediction** — it should not be cited as experimental support. The substantive support is (i) the Phobius TM prediction above (`ECO:0000256|SAM:Phobius`, a legitimate sequence‑analysis feature), (ii) the family assignment, and (iii) the functional genetics: a protein whose loss traps DNA in the periplasm must act at the inner membrane.

**Experimental topology (from *B. subtilis* ComEC, 776 aa; Draskovic & Dubnau 2005):** 59 *phoA*/*lacZ* fusion constructs expressed from the native locus support a model with **seven transmembrane segments (A–G)**, a large **extracytoplasmic N‑terminal loop**, an **extracytoplasmic C‑loop**, and a **cytoplasmic extreme C‑terminus** (*"the N‑terminal loop and the C‑terminal loop face the extracellular environment, while the C‑terminus is in the cytoplasm"*; fusions from E670 to N776 gave high LacZ, and P766/N776 fusions *"fully support DNA uptake"*). Caution: the TM count is model‑dependent — the authors note computational predictions ranged from 9 to 12 segments, and the Phobius prediction for Q9KQW8 returns 10.

Two further *B. subtilis* findings bear on how VC_1879 should be pictured:

- **An intramolecular disulphide bond (C131–C172) in the extracytoplasmic N‑loop is required for protein stability**, introduced by the competence‑induced oxidoreductase pair BdbDC; C131S and C172S mutants were undetectable by Western blot, whereas the other six cysteine substitutions had no effect on stability or transformability. *Whether VC_1879 uses the same device is untested*; the *V. cholerae* protein has 7 cysteines (C40, C273, C298, C373, C477, C589, C620) and lacks an obvious equivalent cysteine pair in the N‑loop, so this is **not** transferable without evidence.
- **ComEC is an oligomer**, cross‑linkable through native cysteines, with an oligomerisation surface that *"includes a transmembrane segment, TMS‑G, near the cytoplasmic C‑terminus."* The 2025 NAR work did not address full‑length oligomerisation (the authors *"are currently unable to produce sufficient amounts of full‑length ComEC"*).

**Topological consequence for the catalytic domains, in a Gram‑negative like *V. cholerae*:** Stedman et al. predict the **OB fold faces the periplasm** in *L. pneumophila* (the extracellular face in Gram‑positives), which positions it to receive DNA handed over by **periplasmic ComEA** — a hand‑off chain that matches the *V. cholerae* epistasis exactly. The MBL nuclease domain, on this model, degrades the rejected strand at the periplasmic mouth of the channel. This topology is **predicted, not measured**, and is the single most important open question for VC_1879.

**Localization in cells:** no ComEC fluorescent‑fusion data exist for *V. cholerae*. Seitz & Blokesch imaged mCherry‑PilQ, PilB‑GFP and PilT, but not ComEC. The mBio 2014 "spatially but not temporally coupled" result implies the inner‑membrane machinery is positioned near the outer‑membrane uptake site, but this was not shown with a ComEC fusion.

---

## 4. Pathway context and regulation

**Pathway:** chitin‑induced natural competence → DNA uptake → RecA‑dependent homologous recombination (horizontal gene transfer).

*V. cholerae* is a chitin‑associated marine organism; growth on chitinous surfaces (crab shells, copepod exoskeletons) induces competence, first shown by **Meibom, Blokesch, Dolganov, Wu & Schoolnik, Science 2005;310(5755):1824, doi:10.1126/science.1120096** ([EPFL Infoscience](https://infoscience.epfl.ch/items/fb6f85a2-b377-446b-9519-59c30a74c43b)). The uptake route:

1. **Competence type IV pilus** (PilQ secretin, PilA major pilin, PilB extension ATPase, PilT/PilU retraction ATPases, minor pilins VC0857–VC0861) binds extracellular DNA and, by forceful retraction, pulls it across the **outer membrane**.
2. **ComEA** binds the DNA in the **periplasm**, ratcheting it in and preventing back‑diffusion.
3. **ComEC (VC_1879)** forms the **inner‑membrane channel**; one strand is threaded 3′‑end‑first into the cytoplasm, the other is nucleolytically destroyed. **ComF** acts at the same step (likely providing motive force).
4. **SSB/DprA** load the incoming ssDNA onto **RecA**, which catalyses homologous recombination into the chromosome.

**Regulation.** Three signals converge: chitin (via the master regulator **TfoX**), quorum sensing/high cell density (via **HapR**), and nutrient/nucleoside status (via **CytR**). *comEA* and *comEC* are **co‑regulated by quorum sensing through QstR** and are *not* in the pilus regulon — Seitz & Blokesch note this co‑regulation explicitly, and HapR‑dependence of *comEA*/*comEC* is a standard feature of the *V. cholerae* competence circuit. **QstR** is a LuxR‑type, c‑di‑GMP‑independent regulator whose production requires both TfoX and HapR; its regulon was mapped by RNA‑seq + ChIP‑seq in **Jaskólska, Stutzmann, Stoudmann & Blokesch, NAR 2018** ([PMC6237807](https://pmc.ncbi.nlm.nih.gov/articles/PMC6237807/)). An important nuance from that paper: although ComEA production is QstR‑dependent, **QstR binding was not detected upstream of *comEA***, implying an unidentified intermediate regulator — so the regulatory wiring to *comEC* should be described as QstR‑dependent but not demonstrated to be QstR‑direct. The nuclease **Dns** degrades extracellular DNA in the absence of HapR, an additional layer gating substrate availability. CytR is a global positive regulator of competence, T6SS and chitinases, but the CytR study lists *comEC (vc1879)* among genes **not** under direct CytR control.

**Downstream significance.** This machinery is the route by which *V. cholerae* acquires new DNA in its environmental reservoir; the same TfoX/QstR circuit also activates the type VI secretion system, coupling killing of neighbouring cells to uptake of the DNA they release — making ComEC the terminal gate of a predatory horizontal‑gene‑transfer programme relevant to the spread of O‑antigen variants and resistance determinants.

---

## 5. Assessment of current database annotations

UniProt Q9KQW8 carries only two GO cross‑references:

| Term | Aspect | Evidence | Assessment |
|---|---|---|---|
| `GO:0005886` plasma membrane | CC | IBA:GO_Central | **Sound.** The phylogenetic inference matches both the TM prediction and the functional requirement for an inner‑membrane step. |
| `GO:0030420` establishment of competence for transformation | BP | IEA:InterPro | **Sound but general.** The InterPro route (IPR004797/TIGR00361) is a well‑founded family mapping, and the *V. cholerae* genetics independently support it. A more precise descendant covering **DNA import across the plasma membrane** would better reflect ComEC's specific step than the umbrella competence‑establishment term. |

Two functions are **not** represented in the current annotation set and are supported by the orthologue work plus full motif conservation in VC_1879:

- **DNA transmembrane transporter / ssDNA translocation across the plasma membrane** — the protein's actual molecular activity.
- **Metal‑dependent (Mn²⁺) single‑strand‑preferring DNA endo/exonuclease activity** in the C‑terminal MBL domain — note this would be an inference from orthologue biochemistry plus conserved H‑X‑D‑X‑D‑H motif, not from *V. cholerae* data.

The `CC SUBCELLULAR LOCATION` line is ARBA‑derived and should not be used as evidence; the protein‑existence level is `PE 4: Predicted`, i.e. no direct experimental evidence of the *V. cholerae* protein itself exists.

---

## 6. Knowledge gaps and experiments that would close them

These are genuine biological unknowns, not curation backlog:

1. **Is VC_1879 catalytically active as a nuclease, and does its MBL domain degrade the non‑translocated strand in *V. cholerae*?** Test: express and purify the isolated VC_1879 505–752 domain, assay Mn²⁺‑dependent ssDNA cleavage, and build chromosomal H556A/D560A/H561A point mutants to ask whether transformation fails while periplasmic DNA uptake persists — the signature phenotype that separates nuclease function from channel function.
2. **What is the membrane topology of VC_1879, and on which side does the OB fold sit?** The Gram‑negative topology is predicted only. Cysteine‑accessibility (SCAM) or split‑reporter fusions in *V. cholerae* would establish whether the DUF4131/OB region is periplasmic, as required for a ComEA → ComEC hand‑off.
3. **Does ComEC physically interact with ComEA and ComF, and does it localise to a discrete site coincident with the pilus?** A functional ComEC fluorescent fusion, combined with the existing mCherry‑PilQ reporter, would test the "spatially coupled" model directly; no ComEC localisation data exist for any Gram‑negative.
4. **What provides the motive force in a Gram‑negative?** ComEC translocation is ATP‑independent; whether *V. cholerae* ComF (or a PriA‑type helicase) is the puller is proposed but untested.
5. **Oligomeric state of the full‑length protein**, which no group has yet purified in any organism.

---

## 7. Summary statement

VC_1879 (Q9KQW8) is *Vibrio cholerae* **ComEC** (historical name Rec2), a 752‑residue polytopic **inner‑membrane** protein of the ComEC/Rec2 family that carries the complete three‑domain architecture of the family: an N‑terminal **OB‑fold DNA‑binding module** (DUF4131/PF13567), a central **transmembrane channel domain** (PF03772, ~10 predicted helices), and a C‑terminal **metallo‑β‑lactamase‑fold nuclease domain** (PF00753; residues 506–689) with an intact **H556‑x‑D558‑x‑D560‑H561** metal‑coordinating motif. It executes the **final step of natural transformation**: translocation of a single strand of exogenous DNA across the cytoplasmic membrane into the cytosol, with concomitant nucleolytic destruction of the complementary strand. *V. cholerae* genetics establish the step unambiguously — Δ*comEC* cells are non‑transformable yet accumulate transforming DNA in the periplasm, and ComEC acts downstream of the competence pilus and ComEA, in the same step as ComF, and upstream of RecA. The molecular mechanism (strand‑selective Mn²⁺‑dependent nuclease, OB‑fold substrate clamp, ATP‑independent channel) is established in orthologues rather than in *V. cholerae* itself, and the protein's own topology, catalytic activity and interactions remain experimentally untested in this organism. Expression is competence‑specific, driven by chitin through TfoX and by quorum sensing through HapR/QstR.

---

## Sources

- [Seitz P & Blokesch M. DNA‑uptake machinery of naturally competent *Vibrio cholerae*. PNAS 2013;110(44):17987‑17992. PMID 24127573](https://pmc.ncbi.nlm.nih.gov/articles/PMC3816411/)
- [Seitz P & Blokesch M. DNA transport across the outer and inner membranes of naturally transformable *Vibrio cholerae* is spatially but not temporally coupled. mBio 2014;5(4):e01409‑14](https://journals.asm.org/doi/10.1128/mBio.01409-14)
- [Seitz P & Blokesch M. ComEA is essential for the transfer of external DNA into the periplasm in naturally transformable *Vibrio cholerae* cells. PLoS Genet 2014](https://infoscience.epfl.ch/record/195185?ln=fr)
- [Stedman MJM, Deselaers S, Braus SAG, Wang D, Gregori Balaguer M, Gossert AD, Hospenthal MK. Molecular interplay between ComEC domains allows for selective degradation of the non‑translocating strand during natural transformation. Nucleic Acids Res 2025;53(18):gkaf932. PMID 40985778](https://pmc.ncbi.nlm.nih.gov/articles/PMC12455585/)
- [Draskovic I & Dubnau D. Biogenesis of a putative channel protein, ComEC, required for DNA uptake: membrane topology, oligomerization and formation of disulphide bonds. Mol Microbiol 2005;55(3):881‑896. PMID 15661011](https://doi.org/10.1111/j.1365-2958.2004.04430.x)
- [Meibom KL, Blokesch M, Dolganov NA, Wu C‑Y, Schoolnik GK. Chitin induces natural competence in *Vibrio cholerae*. Science 2005;310(5755):1824](https://infoscience.epfl.ch/items/fb6f85a2-b377-446b-9519-59c30a74c43b)
- [Metzger LC & Blokesch M. Genetics of natural competence in *Vibrio cholerae* and other Vibrios. Microbiol Spectr](https://journals.asm.org/doi/full/10.1128/microbiolspec.ve-0010-2014)
- [Jaskólska M, Stutzmann S, Stoudmann C, Blokesch M. QstR‑dependent regulation of natural competence and type VI secretion in *Vibrio cholerae*. Nucleic Acids Res 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6237807/)
- [Lo Scrudato M & Blokesch M. The regulatory network of natural competence and transformation of *Vibrio cholerae*. PLoS Genet 2012](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1002778)
- [Watve SS, et al. CytR is a global positive regulator of competence, type VI secretion, and chitinases in *Vibrio cholerae*. PLoS ONE 2015](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0138834)
- [NCBI Conserved Domain Database, TIGR00361 (ComEC/Rec2 family)](https://www.ncbi.nlm.nih.gov/Structure/cdd/TIGR00361)
- [Wikidata Q23433299 — Rec2‑like protein VC1879](https://www.wikidata.org/wiki/Q23433299)
- [PDB 9IC4 — ComEC β‑lactamase‑like domain](https://www.rcsb.org/structure/9IC4) · [PDB 9IEW — ComEC OB domain](https://www.rcsb.org/structure/9IEW)
- UniProtKB Q9KQW8 and the local `VC_1879-uniprot.txt` / `VC_1879-goa.tsv` records (sequence motif positions computed directly from the Q9KQW8 sequence)

## Citations

1. https://journals.asm.org/doi/full/10.1128/microbiolspec.ve-0010-2014
2. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0138834
3. https://www.wikidata.org/wiki/Q23433299
4. https://www.ncbi.nlm.nih.gov/Structure/cdd/TIGR00361
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC3816411/
6. https://infoscience.epfl.ch/record/195185?ln=fr
7. https://journals.asm.org/doi/10.1128/mBio.01409-14
8. https://doi.org/10.1111/j.1365-2958.2004.04430.x
9. https://infoscience.epfl.ch/items/fb6f85a2-b377-446b-9519-59c30a74c43b
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC6237807/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC12455585/
12. https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1002778
13. https://www.rcsb.org/structure/9IC4
14. https://www.rcsb.org/structure/9IEW